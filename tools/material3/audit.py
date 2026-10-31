#!/usr/bin/env python3
"""Audits the CSS / design-token files of a repository against the Material 3 registry in docs/material3.

  python3 tools/material3/audit.py <repo-or-dir> [--format text|json|md] [--out FILE]
                                   [--fail-on error|warn|info] [--ignore GLOB ...] [--max-per-rule N]
                                   [--no-coverage] [--ref DIR]

Reads (text only, nothing is executed): *.css *.scss *.less *.pcss, <style> blocks of *.html *.vue *.svelte,
and *.json design tokens whose keys map to --md-* names (md.sys.color.primary -> --md-sys-color-primary).

Validate (findings): unknown --md-* tokens, tokens that differ from the baseline, hard-coded colours / radii /
durations / easings / font sizes, touch targets under 48dp, off-grid spacing, text contrast under WCAG, colour
role pairs (X / on-X) under 4.5:1, removed focus outline, missing reduced-motion / dark-theme support.
Compare (coverage): how many registry guidelines (guidelines.json) the repository implements, by name and exactly.

It is a heuristic text scanner (no CSS cascade, no real selectors matching): findings are leads to review, not proofs.
Limits: a value coming from the cascade, JS or a preprocessor mixin is not seen; dark-mode contrast is checked only for
pairs defined inside the same block.
"""
import argparse
import bisect
import colorsys
import difflib
import fnmatch
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REF = os.path.join(HERE, "..", "..", "docs", "material3")
SEVERITY = {"info": 0, "warn": 1, "error": 2}
DEFAULT_IGNORE = ["node_modules/*", "*/node_modules/*", ".git/*", "*/.git/*", "dist/*", "build/*", "*.min.css",
                  "*/vendor/*", "vendor/*"]
# The official site and the @material/web package disagree on these; both are accepted (see docs/material3/VERIFICATION.md).
ALT_VALUES = {
    "--md-sys-state-focus-state-layer-opacity": {"0.1"},
    "--md-sys-state-pressed-state-layer-opacity": {"0.1"},
}
# Spacing: the site says multiples of 8dp, nested 2/4/6/10dp; 4dp multiples are accepted as the common practical grid.
NESTED_OK = {2, 6, 10}

# ---------------------------------------------------------------- value helpers
NUM = re.compile(r"(?<![\w#.-])(-?\d*\.?\d+)(px|rem|em|dp|ms|s|%)?(?![\w.-])")
HEX = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b")
FUNC_COLOR = re.compile(r"\b(?:rgba?|hsla?)\([^()]*\)", re.I)
VAR = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*((?:[^()]|\([^()]*\))*))?\)")
NAMED = {"white": (255, 255, 255, 1), "black": (0, 0, 0, 1), "transparent": (0, 0, 0, 0)}


def _hex(m):
    h = m.group(1).lower()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    return "#" + h


def _num(m):
    v, u = float(m.group(1)), m.group(2)
    if u in ("rem", "em"):
        v, u = v * 16, "px"
    if u in ("px", "dp"):
        return "0" if v == 0 else f"{v:g}px"
    if u == "s":
        v, u = v * 1000, "ms"
    return f"{v:g}{u or ''}"


def canon(v):
    """Canonical form of a CSS value, so 0.5rem == 8px, 0.2s == 200ms, #FFF == #ffffff."""
    v = HEX.sub(_hex, v.strip().rstrip(";"))
    v = re.sub(r"\s+", " ", v.lower())
    v = re.sub(r"\s*,\s*", ",", v).replace("( ", "(").replace(" )", ")")
    return NUM.sub(_num, v)


def to_rgba(s):
    s = s.strip().lower()
    if s in NAMED:
        return NAMED[s]
    m = HEX.fullmatch(s)
    if m:
        h = _hex(m)[1:]
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)
    m = re.fullmatch(r"(rgba?|hsla?)\((.*)\)", s)
    if not m:
        return None
    parts = [p for p in re.split(r"[\s,/]+", m.group(2).strip()) if p]
    if len(parts) < 3:
        return None
    try:
        alpha = 1.0
        if len(parts) > 3:
            alpha = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1)
        if m.group(1).startswith("rgb"):
            ch = [float(p[:-1]) * 2.55 if p.endswith("%") else float(p) for p in parts[:3]]
            return (*[round(c) for c in ch], alpha)
        h = float(parts[0].rstrip("deg")) / 360 % 1
        r, g, b = colorsys.hls_to_rgb(h, float(parts[2].rstrip("%")) / 100, float(parts[1].rstrip("%")) / 100)
        return (round(r * 255), round(g * 255), round(b * 255), alpha)
    except ValueError:
        return None


def luminance(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def resolve(v, lookup, depth=0):
    def sub(m):
        val = lookup(m.group(1))
        if val is None:
            val = m.group(2)
        return resolve(val, lookup, depth + 1) if val is not None and depth < 12 else m.group(0)
    return VAR.sub(sub, v)


# ---------------------------------------------------------------- parsing
class Decl:
    __slots__ = ("path", "line", "selector", "at", "prop", "value")

    def __init__(self, path, line, selector, at, prop, value):
        self.path, self.line, self.selector, self.at, self.prop, self.value = path, line, selector, at, prop, value


def parse_css(text, path, line_offset=0, scss=False):
    text = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group()), text, flags=re.S)
    if scss:
        text = re.sub(r"(?<![:\"'(])//[^\n]*", "", text)
    starts = [0] + [m.end() for m in re.finditer(r"\n", text)]
    line_of = lambda i: bisect.bisect_right(starts, i) + line_offset  # noqa: E731
    out, stack, cur, paren, quote = [], [], 0, 0, None

    def emit(end):
        stmt = text[cur:end]
        if stack and ":" in stmt and not stmt.lstrip().startswith("@"):
            prop, _, value = stmt.partition(":")
            prop = prop.strip()
            if re.fullmatch(r"-{0,2}[\w-]+", prop) and value.strip():
                lead = len(stmt) - len(stmt.lstrip())
                sel = " ".join(s for s in stack if not s.startswith("@"))
                at = " ".join(s for s in stack if s.startswith("@"))
                out.append(Decl(path, line_of(cur + lead), sel, at, prop.lower() if not prop.startswith("--") else prop,
                                " ".join(value.split())))

    for i, ch in enumerate(text):
        if quote:
            if ch == quote and text[i - 1] != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "(":
            paren += 1
        elif ch == ")":
            paren = max(0, paren - 1)
        elif paren == 0 and ch == ";":
            emit(i)
            cur = i + 1
        elif paren == 0 and ch == "{":
            stack.append(" ".join(text[cur:i].split()))
            cur = i + 1
        elif paren == 0 and ch == "}":
            emit(i)
            if stack:
                stack.pop()
            cur = i + 1
    return out


def flatten_tokens(obj, path=()):
    if isinstance(obj, dict):
        for leaf in ("$value", "value"):
            if leaf in obj and not isinstance(obj[leaf], (dict, list)):
                yield path, obj[leaf]
                return
        for k, v in obj.items():
            if not k.startswith("$"):
                yield from flatten_tokens(v, path + (k,))
    elif isinstance(obj, (str, int, float)) and not isinstance(obj, bool):
        yield path, obj


def parse_json_tokens(text, path):
    try:
        data = json.loads(text)
    except ValueError:
        return []
    out = []
    for keys, val in flatten_tokens(data):
        name = "--" + re.sub(r"[._ ]+", "-", "-".join(keys)).lower()
        if name.startswith("--md-"):
            out.append(Decl(path, 1, ":root", "", name, str(val)))
    return out


def read_target(root, ignore):
    decls, files = [], []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in sorted(fn):
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if any(fnmatch.fnmatch(rel, g) for g in ignore):
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext not in (".css", ".scss", ".less", ".pcss", ".html", ".vue", ".svelte", ".json"):
                continue
            try:
                text = open(full, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            if ext == ".json":
                if '"md"' in text or re.search(r"\bmd[._-](sys|ref|comp)\b", text):
                    files.append(rel)
                    decls += parse_json_tokens(text, rel)
            elif ext in (".html", ".vue", ".svelte"):
                for m in re.finditer(r"<style[^>]*>(.*?)</style>", text, re.S | re.I):
                    files.append(rel)
                    decls += parse_css(m.group(1), rel, text.count("\n", 0, m.start(1)))
            else:
                files.append(rel)
                decls += parse_css(text, rel, scss=ext in (".scss", ".less"))
    return decls, sorted(set(files))


# ---------------------------------------------------------------- reference
class Ref:
    def __init__(self, ref_dir):
        css = open(os.path.join(ref_dir, "m3.css"), encoding="utf-8").read()
        self.guides = json.load(open(os.path.join(ref_dir, "guidelines.json"), encoding="utf-8"))
        self.decls = [d for d in parse_css(css, "m3.css") if d.prop.startswith("--")]
        first = {}
        for d in self.decls:
            first.setdefault(d.prop, d.value)
        self.first = first
        self.values = {}
        for d in self.decls:
            r = canon(resolve(d.value, first.get))
            self.values.setdefault(d.prop, set()).add(r)
        light = {}
        for d in self.decls:
            if d.selector == ":root" and not d.at:
                light.setdefault(d.prop, d.value)
        self.light = light
        nums = lambda pat: {float(x) for n, vs in self.values.items() if re.fullmatch(pat, n)  # noqa: E731
                            for v in vs for x in re.findall(r"-?\d*\.?\d+(?=px)", v)}
        self.radii = nums(r"--md-sys-shape-corner-(?!.*-top)[\w-]+") | {0.0}
        self.type_px = nums(r"--md-sys-typescale-[\w-]+-size")
        self.durations = {v for n, vs in self.values.items() if "motion-duration" in n for v in vs} | {"0", "0ms"}
        self.easings = {v for n, vs in self.values.items() if "motion-easing" in n for v in vs}
        self.roles = {}
        for n in light:
            if n.startswith("--md-sys-color-"):
                c = to_rgba(canon(resolve(light[n], light.get)))
                if c:
                    self.roles[n] = c

    def nearest_role(self, rgba):
        best = min(self.roles.items(), key=lambda kv: sum((a - b) ** 2 for a, b in zip(kv[1][:3], rgba[:3])))
        dist = sum((a - b) ** 2 for a, b in zip(best[1][:3], rgba[:3])) ** 0.5
        return best[0], dist


# ---------------------------------------------------------------- checks
class Finding:
    def __init__(self, rule, severity, d, msg, hint=None):
        self.rule, self.severity, self.file, self.line, self.msg, self.hint = \
            rule, severity, d.path, d.line, msg, hint

    def as_dict(self):
        return {"rule": self.rule, "severity": self.severity, "file": self.file, "line": self.line,
                "message": self.msg, "hint": self.hint}


COLOR_PROPS = {"color", "background", "background-color", "border", "border-color", "outline", "outline-color",
               "fill", "stroke", "caret-color", "accent-color", "text-decoration-color", "box-shadow",
               "border-top-color", "border-bottom-color", "border-left-color", "border-right-color"}
RADIUS = re.compile(r"^border(-(top|bottom)-(left|right)|-(start|end)-(start|end))?-radius$")
SPACING = re.compile(r"^(margin|padding)(-(top|right|bottom|left|inline|block)(-(start|end))?)?$|^(row-|column-)?gap$")
INTERACTIVE = re.compile(r"(^|[\s,>+~])(button|a|input|select|textarea|summary)\b(?![-\w])|\[role=[\"']?"
                         r"(button|tab|menuitem|checkbox|radio|switch|option)|\.(btn|button|chip|fab|icon-button|tab)\b", re.I)
SIZE_PROPS = {"width", "height", "min-width", "min-height", "inline-size", "block-size", "min-inline-size",
              "min-block-size"}


def px_values(value):
    return [float(m.group(1)) * (16 if m.group(2) in ("rem", "em") else 1)
            for m in re.finditer(r"(?<![\w#.-])(-?\d*\.?\d+)(px|rem|em)\b", value)]


def target_env(decls):
    env, roots = {}, {}
    for d in decls:
        if d.prop.startswith("--"):
            (roots if d.selector in (":root", "html", ":host", "*", "") and not d.at else env)[d.prop] = d.value
    env.update(roots)
    return env


def run_checks(decls, ref):
    out = []
    env = target_env(decls)
    lookup = lambda n: env.get(n, ref.light.get(n))  # noqa: E731

    # tokens
    known = list(ref.first)
    for d in decls:
        if not d.prop.startswith("--md-"):
            continue
        if d.prop not in ref.values:
            if re.match(r"--md-(sys|ref)-", d.prop) or "comp" in d.prop:
                near = difflib.get_close_matches(d.prop, known, n=1, cutoff=0.85)
                out.append(Finding("token-unknown", "warn", d, f"{d.prop} is not a known Material 3 token",
                                   f"did you mean {near[0]}?" if near else None))
            continue
        val = canon(resolve(d.value, lookup))
        if "var(" in val:
            continue
        if val in ref.values[d.prop] or val in ALT_VALUES.get(d.prop, ()):
            continue
        is_color = d.prop.startswith(("--md-sys-color", "--md-ref-palette"))
        out.append(Finding("token-value", "info" if is_color else "warn", d,
                           f"{d.prop}: {val} differs from baseline ({' | '.join(sorted(ref.values[d.prop])[:2])})",
                           "custom brand colours are expected; check it is intentional" if is_color else None))

    # per-declaration
    for d in decls:
        if d.prop.startswith("--") or "@font-face" in d.at:
            continue
        v, p = d.value, d.prop
        if p in COLOR_PROPS:
            for m in list(HEX.finditer(v)) + list(FUNC_COLOR.finditer(v)):
                rgba = to_rgba(m.group(0))
                if not rgba or rgba[3] == 0 or (p == "box-shadow" and rgba[:3] == (0, 0, 0)):
                    continue
                role, dist = ref.nearest_role(rgba)
                exact = dist == 0
                out.append(Finding("hardcoded-color", "info", d, f"{p}: literal {m.group(0)}",
                                   f"use var({role})" + ("" if exact else f" (nearest baseline role, distance {dist:.0f})")))
        if RADIUS.match(p) and "var(" not in v and "calc(" not in v:
            for x in px_values(v):
                if x not in ref.radii and x < 1000:
                    out.append(Finding("shape-radius", "warn", d, f"{p}: {x:g}px is not in the M3 shape scale",
                                       "scale: " + ", ".join(f"{r:g}" for r in sorted(ref.radii))))
        if p.startswith(("transition", "animation")) and "var(" not in v:
            for m in re.finditer(r"(?<![\w.-])(\d*\.?\d+)(ms|s)\b", v):
                t = canon(m.group(0))
                if t not in ref.durations:
                    out.append(Finding("motion-duration", "warn", d, f"{p}: {m.group(0)} is not an M3 duration token",
                                       "M3: 50-1000ms in short/medium/long/extra-long steps"))
            for m in re.finditer(r"cubic-bezier\([^)]*\)", v):
                if canon(m.group(0)) not in ref.easings:
                    out.append(Finding("motion-easing", "warn", d, f"{p}: {m.group(0)} is not an M3 easing"))
            for m in re.finditer(r"(?<![\w-])(ease|ease-in|ease-out|ease-in-out)(?![\w-])", v):
                out.append(Finding("motion-easing", "warn", d, f"{p}: CSS keyword '{m.group(1)}' is not an M3 easing",
                                   "use --md-sys-motion-easing-*"))
        if p == "font-size" and "var(" not in v and "calc(" not in v:
            for x in px_values(v):
                if x not in ref.type_px:
                    out.append(Finding("type-size", "warn", d, f"font-size: {x:g}px is not in the M3 type scale",
                                       "scale px: " + ", ".join(f"{s:g}" for s in sorted(ref.type_px))))
        if p == "font-weight":
            if re.fullmatch(r"\d+", v) and v not in ("400", "500", "700"):
                out.append(Finding("type-weight", "info", d, f"font-weight: {v}; M3 uses 400, 500 and 700"))
        if p in SIZE_PROPS and INTERACTIVE.search(d.selector) and "var(" not in v and "calc(" not in v:
            for x in px_values(v):
                if 0 < x < 48 and not (p in ("width", "height", "inline-size", "block-size") and ":before" in d.selector):
                    out.append(Finding("touch-target", "warn", d, f"{d.selector} {p}: {x:g}px is under the 48dp target",
                                       "ok if padding or a pseudo-element extends the hit area to 48dp"))
        if SPACING.match(p) and "var(" not in v and "calc(" not in v:
            for x in px_values(v):
                a = abs(x)
                if a and a % 4 and a not in NESTED_OK:
                    out.append(Finding("spacing-grid", "info", d, f"{p}: {x:g}px is off the 4/8dp grid",
                                       "M3: multiples of 8dp; nested 2, 4, 6, 10dp"))

    # per-rule (same file + selector + at-rule)
    rules = {}
    for d in decls:
        rules.setdefault((d.path, d.selector, d.at), {})[d.prop] = d
    for (path, sel, at), props in rules.items():
        fg = props.get("color")
        bg = props.get("background-color") or props.get("background")
        if fg and bg and not sel.endswith(("::selection",)):
            c1 = to_rgba(canon(resolve(fg.value, lookup)))
            c2 = to_rgba(canon(resolve(bg.value, lookup)))
            if c1 and c2 and c1[3] == 1 and c2[3] == 1:
                size = px_values(props["font-size"].value)[0] if "font-size" in props and px_values(props["font-size"].value) else 0
                need = 3.0 if size >= 24 else 4.5
                r = contrast(c1, c2)
                if r < need:
                    out.append(Finding("contrast", "error" if r < 3 else "warn", fg,
                                       f"{sel or '(root)'}: text/background contrast {r:.2f}:1 < {need}:1",
                                       "WCAG: 4.5:1 small text, 3:1 large text"))
        for key, dd in props.items():
            if key in ("outline", "outline-style") and re.fullmatch(r"none|0|0px", dd.value.strip().lower().split(" ")[0]) \
                    and ":focus" in sel and ":focus-visible" not in sel \
                    and not any(k in props for k in ("box-shadow", "outline-color", "border", "border-color", "background", "background-color")):
                out.append(Finding("focus-removed", "warn", dd, f"{sel}: outline removed without a replacement focus indicator"))

    # colour role pairs defined in the target (X / on-X)
    groups = {}
    for d in decls:
        if d.prop.startswith("--md-sys-color-"):
            groups.setdefault((d.selector, d.at), {})[d.prop] = d
    seen = set()
    for (sel, at), defs in groups.items():
        local = dict(env)
        local.update({k: dd.value for k, dd in defs.items()})
        lk = lambda n: local.get(n, ref.light.get(n))  # noqa: E731
        for name, dd in defs.items():
            base = None
            if name.startswith("--md-sys-color-on-"):
                base = name.replace("--md-sys-color-on-", "--md-sys-color-", 1)
            elif name.startswith("--md-sys-color-inverse-on-"):
                base = name.replace("--md-sys-color-inverse-on-", "--md-sys-color-inverse-", 1)
            if base and base in ref.first and (name, sel, at) not in seen:
                seen.add((name, sel, at))
                c1 = to_rgba(canon(resolve(f"var({name})", lk)))
                c2 = to_rgba(canon(resolve(f"var({base})", lk)))
                if c1 and c2 and c1[3] == 1 and c2[3] == 1 and contrast(c1, c2) < 4.5:
                    out.append(Finding("role-pair-contrast", "warn", dd,
                                       f"{name} on {base}: {contrast(c1, c2):.2f}:1 < 4.5:1 ({sel}{' ' + at if at else ''})"))

    # project level
    if decls:
        anchor = decls[0]
        text_at = " ".join(d.at for d in decls)
        sels = " ".join(d.selector for d in decls)
        if not re.search(r":focus-visible", sels):
            out.append(Finding("no-focus-visible", "info", anchor, "no :focus-visible rule found (keyboard focus indicator)"))
        if any(d.prop.startswith(("transition", "animation")) for d in decls) and "prefers-reduced-motion" not in text_at:
            out.append(Finding("no-reduced-motion", "warn", anchor, "transitions/animations but no prefers-reduced-motion rule"))
        if "prefers-color-scheme" not in text_at and "data-theme" not in sels and "dark" not in sels:
            out.append(Finding("no-dark-theme", "info", anchor, "no dark theme support found (prefers-color-scheme / data-theme)"))
    return out


# ---------------------------------------------------------------- coverage (compare)
def coverage(decls, ref):
    env = target_env(decls)
    lookup = lambda n: env.get(n)  # noqa: E731
    allv = {}  # every value a token is given (light, dark, per breakpoint), canonical and resolved
    for d in decls:
        if d.prop.startswith("--"):
            allv.setdefault(d.prop, set()).add(canon(resolve(d.value, lookup)))
    blob = re.sub(r"\s+", "", " ".join(f"{d.at}{{{d.selector}{{{d.prop}:{d.value}" for d in decls)).lower()
    rows = []
    for g in ref.guides:
        status = "exact"
        for s in g["css"]:
            m = re.match(r"^(--[\w-]+)\s*:\s*(.*)$", s)
            if m and m.group(1) in env:
                want = canon(resolve(m.group(2), ref.first.get))
                level = "exact" if (want in allv[m.group(1)] or allv[m.group(1)] & ALT_VALUES.get(m.group(1), set())) else "name"
            elif m:
                level = "missing"
            elif re.sub(r"\s+", "", s).lower() in blob:
                level = "exact"
            else:
                level = "missing"
            if level == "missing":
                status = "missing"
                break
            if level == "name":
                status = "name"
        rows.append({"id": g["id"], "category": g["category"], "source": g["source"], "status": status})
    return rows


# ---------------------------------------------------------------- reporting
def report(findings, cov, files, fmt, max_per_rule):
    by_rule = {}
    for f in findings:
        by_rule.setdefault(f.rule, []).append(f)
    sev = {k: sum(1 for f in findings if f.severity == k) for k in SEVERITY}
    cats = {}
    for r in cov or []:
        c = cats.setdefault(r["category"], {"exact": 0, "name": 0, "missing": 0})
        c[r["status"]] += 1
    if fmt == "json":
        return json.dumps({"files": files, "summary": sev, "findings": [f.as_dict() for f in findings],
                           "coverage": {"by_category": cats, "guidelines": cov}}, indent=1)
    md = fmt == "md"
    L = [("# " if md else "") + f"Material 3 audit: {len(files)} file(s), {sev['error']} error, {sev['warn']} warn, {sev['info']} info", ""]
    for rule, fs in sorted(by_rule.items(), key=lambda kv: (-max(SEVERITY[f.severity] for f in kv[1]), kv[0])):
        top = max(fs, key=lambda f: SEVERITY[f.severity]).severity
        L.append(("## " if md else "") + f"[{top}] {rule} ({len(fs)})")
        for f in fs[:max_per_rule]:
            L.append(f"  {f.file}:{f.line}  {f.msg}" + (f"  -> {f.hint}" if f.hint else ""))
        if len(fs) > max_per_rule:
            L.append(f"  ... {len(fs) - max_per_rule} more (--max-per-rule or --format json)")
        L.append("")
    if cov is not None:
        L.append(("## " if md else "") + "Coverage of the registry (exact = same value, name = defined with another value)")
        tot = {"exact": 0, "name": 0, "missing": 0}
        for c, n in sorted(cats.items()):
            L.append(f"  {c:18} exact {n['exact']:4}  name {n['name']:4}  missing {n['missing']:4}")
            for k in tot:
                tot[k] += n[k]
        L.append(f"  {'TOTAL':18} exact {tot['exact']:4}  name {tot['name']:4}  missing {tot['missing']:4}  of {len(cov)}")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("target", help="repository or directory to audit")
    ap.add_argument("--ref", default=DEFAULT_REF, help="dir with m3.css and guidelines.json (default: docs/material3)")
    ap.add_argument("--format", choices=("text", "json", "md"), default="text")
    ap.add_argument("--out", help="write the report to this file instead of stdout")
    ap.add_argument("--fail-on", choices=("error", "warn", "info", "never"), default="error")
    ap.add_argument("--ignore", action="append", default=[], help="glob (relative path) to skip; repeatable")
    ap.add_argument("--max-per-rule", type=int, default=10)
    ap.add_argument("--no-coverage", action="store_true")
    a = ap.parse_args(argv)
    ref = Ref(a.ref)
    decls, files = read_target(a.target, DEFAULT_IGNORE + a.ignore)
    findings = run_checks(decls, ref)
    cov = None if a.no_coverage else coverage(decls, ref)
    text = report(findings, cov, files, a.format, a.max_per_rule)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
    else:
        sys.stdout.write(text)
    if a.fail_on != "never" and any(SEVERITY[f.severity] >= SEVERITY[a.fail_on] for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
