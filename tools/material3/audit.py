#!/usr/bin/env python3
"""Audits the CSS / design-token files of a repository against the Material 3 registry in docs/material3.

  python3 tools/material3/audit.py <repo-or-dir> [--format text|json|md] [--out FILE]
                                   [--fail-on error|warn|info|never] [--ignore GLOB ...] [--max-per-rule N]
                                   [--no-coverage] [--ref DIR]

Reads (text only, nothing is executed):
  - *.css *.scss *.less *.pcss (nested selectors with &, SCSS $vars and Less @vars, simple arithmetic), <style> blocks
    and inline style="" attributes of *.html *.vue *.svelte *.jsx *.tsx;
  - CSS-in-JS in *.js *.jsx *.ts *.tsx: css``, styled.tag``, styled(X)``, keyframes``, createGlobalStyle``, and JSX style={{}} / sx={{}};
  - *.json design tokens whose keys map to --md-* names (md.sys.color.primary -> --md-sys-color-primary);
  - Material Theme Builder exports: Android colors.xml (md_theme_light_primary), Compose Color.kt, Flutter color_schemes.g.dart.

Validate (findings): unknown --md-* tokens, tokens that differ from the baseline, hard-coded colours / radii /
durations / easings / font sizes (also when reached through a custom property), touch targets under 48dp, off-grid spacing,
text contrast under WCAG in light and dark (state selectors such as :hover inherit from their base selector), colour role
pairs (X / on-X) under 4.5:1, removed focus outline, missing reduced-motion / dark-theme support.
Compare (coverage): how many registry guidelines (guidelines.json) the repository implements, by name and exactly.

It is a heuristic text scanner, not a browser: no DOM, so no inheritance from ancestors, no JS evaluation, no mixins or
functions. What it could not evaluate is counted and printed ("Not evaluated"), so silence is not read as a pass.
Findings are leads to review, not proofs.
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
# The registry follows the site (0.10); the @material/web package value (0.12) is also accepted (see docs/material3/VERIFICATION.md).
ALT_VALUES = {
    "--md-sys-state-focus-state-layer-opacity": {"0.12"},
    "--md-sys-state-pressed-state-layer-opacity": {"0.12"},
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
AT_KEYWORDS = {"media", "include", "import", "use", "forward", "charset", "namespace", "mixin", "function", "return", "if",
               "else", "each", "for", "while", "extend", "supports", "font-face", "keyframes", "layer", "container",
               "property", "page", "plugin", "debug", "warn", "error", "at-root", "content"}
UNITLESS = {"opacity", "font-weight", "line-height", "z-index", "flex", "flex-grow", "flex-shrink", "order", "zoom",
            "scale", "aspect-ratio"}
DARK_AT = re.compile(r"prefers-color-scheme:\s*dark", re.I)
DARK_SEL = re.compile(r"""\[data-[\w-]*(?:theme|scheme|mode)[\w-]*=["']?dark|\.dark\b|\.theme-dark|\.dark-theme|\.md-dark""", re.I)
ROOTISH = re.compile(r"(:root|html|:host|\*|body)(?![\w-])")
PROP_NAME = re.compile(r"-{0,2}[\w-]+")


class Decl:
    __slots__ = ("path", "line", "sels", "at", "prop", "value", "dyn")

    def __init__(self, path, line, sels, at, prop, value):
        self.path, self.line, self.sels, self.at, self.prop, self.value = path, line, list(sels), at, prop, value
        self.dyn = set()

    @property
    def selector(self):
        return ", ".join(self.sels)


def is_dark(d):
    return bool(DARK_AT.search(d.at) or DARK_SEL.search(d.selector))


def rootish(d):
    return any(ROOTISH.match(s.strip()) for s in d.sels)


def split_top(s, sep=","):
    out, depth, quote, cur = [], 0, None, []
    for ch in s:
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif ch == sep and depth == 0:
            out.append("".join(cur))
            cur = []
            continue
        cur.append(ch)
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def combine(parents, prelude):
    """Flattens nested selectors: `&` is replaced by the parent, comma lists are expanded."""
    out = []
    for kid in split_top(prelude):
        if "&" in kid:
            out += [kid.replace("&", p) if p else kid for p in (parents or [""])]
        else:
            out += [f"{p} {kid}" if p else kid for p in (parents or [""])]
    return out or list(parents)


def parse_css(text, path, line_offset=0, scss=False):
    text = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group()), text, flags=re.S)
    if scss:
        text = re.sub(r"(?<![:\"'(])//[^\n]*", "", text)
    starts = [0] + [m.end() for m in re.finditer(r"\n", text)]
    line_of = lambda i: bisect.bisect_right(starts, i) + line_offset  # noqa: E731
    out, stack, cur, paren, quote = [], [], 0, 0, None

    def emit(end):
        stmt = text[cur:end]
        s = stmt.strip()
        if not s or ":" not in s:
            return
        lead = len(stmt) - len(stmt.lstrip())
        mv = re.match(r"([$@][\w-]+)\s*:\s*(.*)$", s, re.S)
        if mv and not (mv.group(1)[0] == "@" and mv.group(1)[1:] in AT_KEYWORDS):
            prop, value = mv.group(1), mv.group(2)
        elif stack and not s.startswith("@"):
            prop, _, value = s.partition(":")
            prop = prop.strip()
            if not PROP_NAME.fullmatch(prop):
                return
            if not prop.startswith("--"):
                prop = prop.lower()
        else:
            return
        value = " ".join(re.sub(r"\s*!(default|global|important)\b", "", value).split())
        if value:
            sels = stack[-1][0] if stack else [""]
            at = " ".join(f[1] for f in stack if f[1])
            out.append(Decl(path, line_of(cur + lead), sels, at, prop, value))

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
            prelude = " ".join(text[cur:i].split())
            parent = stack[-1][0] if stack else []
            if prelude.startswith("@"):
                stack.append((parent, prelude))
            else:
                stack.append((combine(parent, prelude), ""))
            cur = i + 1
        elif paren == 0 and ch == "}":
            emit(i)
            if stack:
                stack.pop()
            cur = i + 1
    return out


SUBST = re.compile(r"#\{\s*([$@][\w-]+)\s*\}|@\{([\w-]+)\}|(?<![\w@])(\$[\w-]+|@[\w-]+)")
ARITH = re.compile(r"^\(?\s*(-?\d*\.?\d+)(px|rem|em)?\s*([*/+-])\s*(-?\d*\.?\d+)(px|rem|em)?\s*\)?$")
MATHDIV = re.compile(r"^math\.div\(\s*(-?\d*\.?\d+)(px|rem|em)?\s*,\s*(-?\d*\.?\d+)(px|rem|em)?\s*\)$")


def arith(v):
    m = ARITH.match(v)
    if m:
        a, ua, op, b, ub = float(m.group(1)), m.group(2), m.group(3), float(m.group(4)), m.group(5)
    else:
        m = MATHDIV.match(v)
        if not m:
            return v
        a, ua, op, b, ub = float(m.group(1)), m.group(2), "/", float(m.group(3)), m.group(4)
    if op in "+-" and ua != ub:
        return v
    if op in "*/" and ua and ub:
        return v
    try:
        r = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}[op]
    except ZeroDivisionError:
        return v
    return f"{r:g}{ua or ub or ''}"


def finalize(decls):
    """Substitutes SCSS ($x) and Less (@x) variables, evaluates simple arithmetic, flags what cannot be evaluated."""
    glob, per = {}, {}
    for d in decls:
        if d.prop[0] in "$@":
            per.setdefault(d.path, {})[d.prop] = d.value
            glob[d.prop] = d.value

    def expand(path, v):
        for _ in range(8):
            changed = [False]

            def rep(m):
                name = m.group(1) or (f"@{m.group(2)}" if m.group(2) else m.group(3))
                val = per.get(path, {}).get(name, glob.get(name))
                if val is None:
                    return m.group(0)
                changed[0] = True
                return val
            v2 = SUBST.sub(rep, v)
            if not changed[0]:
                break
            v = v2
        return v

    for d in decls:
        if d.prop[0] not in "$@":
            d.value = arith(expand(d.path, d.value))
        v = d.value
        if re.search(r"\$[\w-]|(?<![\w@])@[\w-]|@\{|#\{", v):
            d.dyn.add("preprocessor")
        if "__js__" in v:
            d.dyn.add("js-expression")
        if re.search(r"\b(calc|min|max|clamp|env)\(", v):
            d.dyn.add("calc")
    return decls


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
            out.append(Decl(path, 1, [":root"], "", name, str(val)))
    return out


def kebab(name):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower()
    return {"on-inverse-surface": "inverse-on-surface"}.get(name, name)


def argb_hex(h):
    h = h.lower()
    return "#" + (h[2:] if len(h) == 8 else h)  # Android / Compose / Flutter are AARRGGBB


def parse_theme_exports(text, path, ext, roles):
    """Material Theme Builder exports: Android colors.xml, Compose Color.kt, Flutter color_schemes.g.dart."""
    out = []
    line = lambda i: text.count("\n", 0, i) + 1  # noqa: E731

    def add(mode, role, hexc, pos):
        role = kebab(role)
        if roles is None or f"--md-sys-color-{role}" in roles:
            out.append(Decl(path, line(pos), [":root"], "@media (prefers-color-scheme: dark)" if mode == "dark" else "",
                            f"--md-sys-color-{role}", argb_hex(hexc)))
    if ext == ".xml":
        for m in re.finditer(r'<color\s+name="md_theme_(light|dark)_(\w+?)"\s*>\s*#([0-9a-fA-F]{6,8})\s*</color>', text):
            add(m.group(1), m.group(2), m.group(3), m.start())
    elif ext == ".kt":
        for m in re.finditer(r"val\s+md_theme_(light|dark)_(\w+?)\s*=\s*Color\(\s*0x([0-9a-fA-F]{8})\s*\)", text):
            add(m.group(1), m.group(2), m.group(3), m.start())
    elif ext == ".dart":
        for blk in re.finditer(r"Brightness\.(light|dark)(.*?)\);", text, re.S):
            for m in re.finditer(r"(\w+)\s*:\s*Color\(\s*0x([0-9a-fA-F]{8})\s*\)", blk.group(2)):
                add(blk.group(1), m.group(1), m.group(2), blk.start(2) + m.start())
    return out


CSS_IN_JS = re.compile(r"(?:\b(?P<kind>css|keyframes|createGlobalStyle|injectGlobal)|\bstyled(?:\.(?P<tag>\w+)|\([^)]*\)"
                       r"(?:\.attrs\([^)]*\))?(?:\.(?P<tag2>\w+))?))\s*`(?P<body>[^`]*)`")
STYLE_OBJ = re.compile(r"\b(?:style|sx)=\{\{(.*?)\}\}", re.S)
STYLE_PAIR = re.compile(r"""(\w+)\s*:\s*('[^']*'|"[^"]*"|-?\d*\.?\d+)\s*(?=,|$)""")
STYLE_ATTR = re.compile(r"""\bstyle\s*=\s*(?:"([^"]*)"|'([^']*)')""")


def parse_embedded(text, path, ext):
    """CSS-in-JS tagged templates, JSX style objects and inline style attributes."""
    out = []
    line0 = lambda i: text.count("\n", 0, i)  # noqa: E731
    if ext in (".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
        for m in CSS_IN_JS.finditer(text):
            body = re.sub(r"\$\{[^}]*\}", "__js__", m.group("body"))
            kind = m.group("kind")
            if kind in ("createGlobalStyle", "injectGlobal", "keyframes"):
                out += parse_css(body, path, line0(m.start("body")))
            else:
                tag = m.group("tag") or m.group("tag2") or "&"
                out += parse_css(f"{tag}{{{body}}}", path, line0(m.start("body")))
        for m in STYLE_OBJ.finditer(text):
            for k, v in STYLE_PAIR.findall(m.group(1)):
                prop = re.sub(r"([A-Z])", lambda x: "-" + x.group(1).lower(), k)
                val = v[1:-1] if v[0] in "'\"" else (v if prop in UNITLESS else f"{v}px")
                out.append(Decl(path, line0(m.start()) + 1, ["[style]"], "", prop, val))
    if ext in (".html", ".vue", ".svelte", ".jsx", ".tsx"):
        for m in STYLE_ATTR.finditer(text):
            body = m.group(1) or m.group(2) or ""
            if ":" in body and "{" not in body:
                out += parse_css(f"[style]{{{body}}}", path, line0(m.start()))
    return out


def read_target(root, ignore, roles=None, max_bytes=2_000_000):
    decls, files = [], []
    if os.path.isfile(root):  # a single file: audit just that one
        root, only = os.path.dirname(root) or ".", os.path.basename(root)
    else:
        only = None
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        if only:
            fn = [only] if only in fn else []
        for f in sorted(fn):
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if any(fnmatch.fnmatch(rel, g) for g in ignore):
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext not in (".css", ".scss", ".less", ".pcss", ".html", ".vue", ".svelte", ".json", ".js", ".jsx", ".ts",
                           ".tsx", ".mjs", ".cjs", ".xml", ".kt", ".dart"):
                continue
            try:
                if os.path.getsize(full) > max_bytes:
                    continue
                with open(full, encoding="utf-8") as fh:
                    text = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            got = []
            if ext == ".json":
                if '"md"' in text or re.search(r"\bmd[._-](sys|ref|comp)\b", text):
                    got = parse_json_tokens(text, rel)
            elif ext in (".xml", ".kt", ".dart"):
                if "md_theme_" in text or "Brightness." in text:
                    got = parse_theme_exports(text, rel, ext, roles)
            else:
                if ext in (".html", ".vue", ".svelte"):
                    for m in re.finditer(r"<style[^>]*>(.*?)</style>", text, re.S | re.I):
                        got += parse_css(m.group(1), rel, text.count("\n", 0, m.start(1)),
                                         scss=bool(re.search(r"lang=[\"']?(scss|less)", m.group(0)[:200])))
                elif ext in (".css", ".scss", ".less", ".pcss"):
                    got = parse_css(text, rel, scss=ext in (".scss", ".less"))
                got += parse_embedded(text, rel, ext)
            if got:
                files.append(rel)
                decls += got
    return finalize(decls), sorted(set(files))


# ---------------------------------------------------------------- reference
class Ref:
    def __init__(self, ref_dir):
        with open(os.path.join(ref_dir, "m3.css"), encoding="utf-8") as fh:
            css = fh.read()
        with open(os.path.join(ref_dir, "guidelines.json"), encoding="utf-8") as fh:
            self.guides = json.load(fh)
        self.decls = [d for d in parse_css(css, "m3.css") if d.prop.startswith("--")]
        first = {}
        for d in self.decls:
            first.setdefault(d.prop, d.value)
        self.first = first
        self.values = {}
        for d in self.decls:
            r = canon(resolve(d.value, first.get))
            self.values.setdefault(d.prop, set()).add(r)
        light, dark = {}, {}
        for d in self.decls:
            if d.selector == ":root" and not d.at:
                light.setdefault(d.prop, d.value)
            elif is_dark(d) and d.selector.startswith(":root"):
                dark[d.prop] = d.value
        self.light = light
        self.dark = {**light, **dark}
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
STATE = re.compile(r":(hover|focus|focus-visible|focus-within|active|visited|checked|selected)\b|"
                   r"\[aria-(pressed|selected|checked|expanded)[^\]]*\]", re.I)
DISABLED = re.compile(r":disabled|\[disabled\]|\[aria-disabled|\.disabled\b|\.is-disabled|::placeholder|::selection", re.I)
NO_OUTLINE = re.compile(r"none|0|0px")


def px_values(value):
    return [float(m.group(1)) * (16 if m.group(2) in ("rem", "em") else 1)
            for m in re.finditer(r"(?<![\w#.-])(-?\d*\.?\d+)(px|rem|em)\b", value)]


def build_env(decls, dark):
    """Custom properties in effect: global (root-like selectors win). dark=True overlays the dark-mode definitions."""
    def collect(want_dark):
        base, roots = {}, {}
        for d in decls:
            if d.prop.startswith("--") and is_dark(d) == want_dark:
                (roots if rootish(d) else base)[d.prop] = d.value
        base.update(roots)
        return base
    env = collect(False)
    if dark:
        env.update(collect(True))
    return env


def outline_removed(own, sel):
    """`:focus { outline: none }` with no replacement indicator in the same merged rule."""
    if ":focus" not in sel or ":focus-visible" in sel:
        return None
    for key in ("outline", "outline-style"):
        dd = own.get(key)
        if dd and NO_OUTLINE.fullmatch(dd.value.strip().lower().split(" ")[0]):
            if not any(k in own for k in ("box-shadow", "outline-color", "border", "border-color")):
                return dd
    return None


def analyze(decls, ref):
    out, stats = [], {"declarations": 0, "not_evaluated": {}}
    env_l, env_d = build_env(decls, False), build_env(decls, True)
    lk_l = lambda n: env_l.get(n, ref.light.get(n))  # noqa: E731
    lk_d = lambda n: env_d.get(n, ref.dark.get(n))  # noqa: E731

    def skip(reason):
        stats["not_evaluated"][reason] = stats["not_evaluated"].get(reason, 0) + 1

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
        if d.dyn - {"calc"}:
            continue
        val = canon(resolve(d.value, lk_d if is_dark(d) else lk_l))
        if "var(" in val:
            continue
        if val in ref.values[d.prop] or val in ALT_VALUES.get(d.prop, ()):
            continue
        is_color = d.prop.startswith(("--md-sys-color", "--md-ref-palette")) or any(
            to_rgba(x) for x in ref.values[d.prop])
        if is_color and not to_rgba(val):
            continue  # system colours (canvastext), currentcolor, gradients: not comparable
        out.append(Finding("token-value", "info" if is_color else "warn", d,
                           f"{d.prop}: {val} differs from baseline ({' | '.join(sorted(ref.values[d.prop])[:2])})",
                           "custom brand colours are expected; check it is intentional" if is_color else None))

    # per-declaration
    for d in decls:
        if d.prop[0] in "$@" or d.prop.startswith("--") or "@font-face" in d.at:
            continue
        stats["declarations"] += 1
        v, p = d.value, d.prop
        if d.dyn & {"preprocessor", "js-expression"}:
            for r in d.dyn & {"preprocessor", "js-expression"}:
                skip(r)
            continue
        lk = lk_d if is_dark(d) else lk_l
        uses_md = bool(re.search(r"var\(\s*--md-", v))
        rv = resolve(v, lk) if "var(" in v else v
        dim_ok = not uses_md and "var(" not in rv and "calc" not in d.dyn
        if "var(" in rv and not uses_md:
            skip("unresolved var()")
        if "calc" in d.dyn:
            skip("calc/min/max/clamp/env")
        if p in COLOR_PROPS:
            for m in list(HEX.finditer(v)) + list(FUNC_COLOR.finditer(v)):
                rgba = to_rgba(m.group(0))
                if not rgba or rgba[3] == 0 or (p == "box-shadow" and rgba[:3] == (0, 0, 0)):
                    continue
                role, dist = ref.nearest_role(rgba)
                out.append(Finding("hardcoded-color", "info", d, f"{p}: literal {m.group(0)}",
                                   f"use var({role})" + ("" if dist == 0 else f" (nearest baseline role, distance {dist:.0f})")))
        if not dim_ok:
            continue
        via = "" if rv == v else f" (via {v})"
        if RADIUS.match(p):
            for x in px_values(rv):
                if x not in ref.radii and x < 1000:
                    out.append(Finding("shape-radius", "warn", d, f"{p}: {x:g}px{via} is not in the M3 shape scale",
                                       "scale: " + ", ".join(f"{r:g}" for r in sorted(ref.radii))))
        if p.startswith(("transition", "animation")):
            for m in re.finditer(r"(?<![\w.-])(\d*\.?\d+)(ms|s)\b", rv):
                if canon(m.group(0)) not in ref.durations:
                    out.append(Finding("motion-duration", "warn", d, f"{p}: {m.group(0)}{via} is not an M3 duration token",
                                       "M3: 50-1000ms in short/medium/long/extra-long steps"))
            for m in re.finditer(r"cubic-bezier\([^)]*\)", rv):
                if canon(m.group(0)) not in ref.easings:
                    out.append(Finding("motion-easing", "warn", d, f"{p}: {m.group(0)} is not an M3 easing"))
            for m in re.finditer(r"(?<![\w-])(ease|ease-in|ease-out|ease-in-out)(?![\w-])", rv):
                out.append(Finding("motion-easing", "warn", d, f"{p}: CSS keyword '{m.group(1)}' is not an M3 easing",
                                   "use --md-sys-motion-easing-*"))
        if p == "font-size" and not re.search(r"icon|symbol|glyph", d.selector + v, re.I):  # icon sizes are not text
            for x in px_values(rv):
                if x not in ref.type_px:
                    out.append(Finding("type-size", "warn", d, f"font-size: {x:g}px{via} is not in the M3 type scale",
                                       "scale px: " + ", ".join(f"{s:g}" for s in sorted(ref.type_px))))
        if p == "font-weight" and re.fullmatch(r"\d+", rv) and rv not in ("400", "500", "700"):
            out.append(Finding("type-weight", "info", d, f"font-weight: {rv}; M3 uses 400, 500 and 700"))
        if p in SIZE_PROPS and any(INTERACTIVE.search(s) for s in d.sels):
            for x in px_values(rv):
                if 0 < x < 48 and not (p in ("width", "height", "inline-size", "block-size") and ":before" in d.selector):
                    out.append(Finding("touch-target", "warn", d, f"{d.selector} {p}: {x:g}px{via} is under the 48dp target",
                                       "ok if padding or a pseudo-element extends the hit area to 48dp"))
        if SPACING.match(p):
            for x in px_values(rv):
                a = abs(x)
                if a and a % 4 and a not in NESTED_OK:
                    out.append(Finding("spacing-grid", "info", d, f"{p}: {x:g}px{via} is off the 4/8dp grid",
                                       "M3: multiples of 8dp; nested 2, 4, 6, 10dp"))

    # per-rule: same selector + at-rule, merged across files; state selectors inherit from their base selector
    rules = {}
    for d in decls:
        if d.prop[0] in "$@" or d.prop.startswith("--"):
            continue
        for s in d.sels:
            rules.setdefault((s, d.at), {})[d.prop] = d
    for (sel, at), own in rules.items():
        dd = outline_removed(own, sel)
        if dd:
            out.append(Finding("focus-removed", "warn", dd, f"{sel}: outline removed without a replacement focus indicator"))
        if not ({"color", "background", "background-color"} & set(own)) or DISABLED.search(sel):
            continue
        base = STATE.sub("", sel).strip() or sel
        eff = {}
        if base != sel:
            eff.update(rules.get((base, ""), {}))
            eff.update(rules.get((base, at), {}))
        eff.update(own)
        fg, bg = eff.get("color"), eff.get("background-color") or eff.get("background")
        if not (fg and bg):
            continue
        anchor = own.get("color") or own.get("background-color") or own.get("background") or fg
        size = (px_values(eff["font-size"].value) or [0])[0] if "font-size" in eff else 0
        need = 3.0 if size >= 24 else 4.5
        dark_rule = any(is_dark(x) for x in own.values())
        raw_var = "var(" in fg.value or "var(" in bg.value
        for mode in (["dark"] if dark_rule else ["light"] + (["dark"] if raw_var else [])):
            lk = lk_d if mode == "dark" else lk_l
            c1, c2 = to_rgba(canon(resolve(fg.value, lk))), to_rgba(canon(resolve(bg.value, lk)))
            if c1 and c2 and c1[3] == 1 and c2[3] == 1:
                r = contrast(c1, c2)
                if r < need:
                    out.append(Finding("contrast", "error" if r < 3 else "warn", anchor,
                                       f"{sel or '(root)'}: text/background contrast {r:.2f}:1 < {need}:1"
                                       + (" [dark]" if mode == "dark" else ""), "WCAG: 4.5:1 small text, 3:1 large text"))
            else:
                skip("contrast: colour not resolvable")

    # colour role pairs (X / on-X), in light and in dark
    first_def = {}
    for d in decls:
        if d.prop.startswith("--md-sys-color-"):
            first_def.setdefault(d.prop, d)
    pairs = set()
    for name in first_def:
        base = None
        if name.startswith("--md-sys-color-on-"):
            base = name.replace("--md-sys-color-on-", "--md-sys-color-", 1)
        elif name.startswith("--md-sys-color-inverse-on-"):
            base = name.replace("--md-sys-color-inverse-on-", "--md-sys-color-inverse-", 1)
        if base and base in ref.first:
            pairs.add((name, base))
    for name, base in sorted(pairs):
        for mode, lk in (("light", lk_l), ("dark", lk_d)):
            c1, c2 = to_rgba(canon(resolve(f"var({name})", lk))), to_rgba(canon(resolve(f"var({base})", lk)))
            if c1 and c2 and c1[3] == 1 and c2[3] == 1 and contrast(c1, c2) < 4.5:
                out.append(Finding("role-pair-contrast", "warn", first_def[name],
                                   f"{name} on {base}: {contrast(c1, c2):.2f}:1 < 4.5:1 [{mode}]"))

    # project level
    if decls:
        anchor = decls[0]
        text_at = " ".join(d.at for d in decls)
        sels = " ".join(d.selector for d in decls)
        if not re.search(r":focus-visible", sels):
            out.append(Finding("no-focus-visible", "info", anchor, "no :focus-visible rule found (keyboard focus indicator)"))
        if any(d.prop.startswith(("transition", "animation")) for d in decls) and "prefers-reduced-motion" not in text_at:
            out.append(Finding("no-reduced-motion", "warn", anchor, "transitions/animations but no prefers-reduced-motion rule"))
        if "prefers-color-scheme" not in text_at and not any(is_dark(d) for d in decls):
            out.append(Finding("no-dark-theme", "info", anchor, "no dark theme support found (prefers-color-scheme / data-theme / .dark)"))
    seen, uniq = set(), []
    for f in out:
        k = (f.rule, f.file, f.line, f.msg)
        if k not in seen:
            seen.add(k)
            uniq.append(f)
    return uniq, stats


def run_checks(decls, ref):
    return analyze(decls, ref)[0]


# ---------------------------------------------------------------- coverage (compare)
def coverage(decls, ref):
    env = build_env(decls, True)
    env_l = build_env(decls, False)
    allv = {}  # every value a token is given (light, dark, per breakpoint), canonical and resolved in both modes
    for d in decls:
        if d.prop.startswith("--"):
            for e in (env_l, env):
                allv.setdefault(d.prop, set()).add(canon(resolve(d.value, e.get)))
    blob = re.sub(r"\s+", "", " ".join(f"{d.at}{{{d.selector}{{{d.prop}:{d.value}" for d in decls)).lower()
    rows = []
    for g in ref.guides:
        status = "exact"
        for s in g["css"]:
            m = re.match(r"^(--[\w-]+)\s*:\s*(.*)$", s)
            if m and m.group(1) in allv:
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
def report(findings, cov, files, fmt, max_per_rule, stats=None):
    by_rule = {}
    for f in findings:
        by_rule.setdefault(f.rule, []).append(f)
    sev = {k: sum(1 for f in findings if f.severity == k) for k in SEVERITY}
    cats = {}
    for r in cov or []:
        c = cats.setdefault(r["category"], {"exact": 0, "name": 0, "missing": 0})
        c[r["status"]] += 1
    if fmt == "json":
        return json.dumps({"files": files, "summary": sev, "not_evaluated": stats, "findings": [f.as_dict() for f in findings],
                           "coverage": {"by_category": cats, "guidelines": cov}}, indent=1)
    md = fmt == "md"
    L = [("# " if md else "") + f"Material 3 audit: {len(files)} file(s), {sev['error']} error, {sev['warn']} warn, {sev['info']} info", ""]
    if stats and stats["declarations"]:
        ne = stats["not_evaluated"]
        L.append(("## " if md else "") + f"Not evaluated: {sum(ne.values())} check(s) over {stats['declarations']} declaration(s)"
                 + (" (" + ", ".join(f"{k}: {v}" for k, v in sorted(ne.items())) + ")" if ne else " (none)"))
        L.append("")
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
    decls, files = read_target(a.target, DEFAULT_IGNORE + a.ignore, roles=set(ref.first))
    findings, stats = analyze(decls, ref)
    cov = None if a.no_coverage else coverage(decls, ref)
    text = report(findings, cov, files, a.format, a.max_per_rule, stats)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
    else:
        sys.stdout.write(text)
    if a.fail_on != "never" and any(SEVERITY[f.severity] >= SEVERITY[a.fail_on] for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
