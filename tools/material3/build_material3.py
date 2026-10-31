#!/usr/bin/env python3
"""Builds docs/material3/{tokens.json,m3.css} from the official @material/web token sources.

The .scss files are only *read as text* (nothing downloaded is executed).
Usage:  python3 tools/material3/build_material3.py <dir with the unpacked @material/web package>
        (npm pack @material/web && tar xzf material-web-*.tgz -C <dir>  ->  <dir>/package)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import curated  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "docs", "material3")
ENTRY = re.compile(r"\n    '([a-z0-9-]+)':\s*(.*?)(?=,\n    '|\n  \);)", re.S)
GET = re.compile(r"map\.get\(\$deps,\s*'([\w-]+)',\s*'([\w-]+)'\)")
IF = re.compile(r"if\(\s*\$exclude-hardcoded-values,\s*null,\s*(.*)\)\s*$", re.S)


def body(path, fn=None):
    text = open(path, encoding="utf-8").read()
    start = 0 if fn is None else text.index(f"@function {fn}")
    start = text.index("@return (", start)
    return text[start:text.index("\n  );", start) + 5]


def value(expr):
    """scss expression -> ('lit', css) | ('ref', system, token); None when it can't be represented
    (composite `font:` shorthands carry the same data as the discrete tokens)."""
    expr = re.sub(r"/\*.*?\*/", "", expr, flags=re.S).strip()
    if "#{" in expr:
        return None
    m = GET.fullmatch(expr)
    if m:
        return ("ref", m.group(1), m.group(2))
    m = IF.match(expr)
    if m:
        lit = " ".join(m.group(1).split())
        if lit.startswith("(") and lit.endswith(")"):
            lit = lit[1:-1]
        return ("lit", lit)
    return None


def parse(path, fn=None):
    out = {}
    for name, expr in ENTRY.findall(body(path, fn)):
        v = value(expr)
        if v:
            out[name] = v
    return out


def css_value(v):
    return v[1] if v[0] == "lit" else f"var(--{v[1]}-{v[2]})"


def main(pkg):
    d = os.path.join(pkg, "package", "tokens", "versions", "v0_192")
    f = lambda n: os.path.join(d, n)  # noqa: E731
    palette = {k: v[1] for k, v in parse(f("_md-ref-palette.scss")).items()}
    typeface = {k: v[1] for k, v in parse(f("_md-ref-typeface.scss")).items()}
    color = {m: {k: v[2] for k, v in parse(f("_md-sys-color.scss"), "values-" + m).items()}
             for m in ("light", "dark")}
    sysd = {n: {k: v[1] for k, v in parse(f(f"_md-sys-{n}.scss")).items()}
            for n in ("shape", "elevation", "state", "motion")}
    scale = {k: css_value(v) for k, v in parse(f("_md-sys-typescale.scss")).items()}
    comps = {}
    for fn in sorted(os.listdir(d)):
        m = re.fullmatch(r"_md-comp-(.+)\.scss", fn)
        if m and not m.group(1).endswith("-meta"):
            comps[m.group(1)] = {k: css_value(v) for k, v in parse(f(fn)).items()}
    # light <-> dark: which ref-palette tone every role uses in each mode
    modes = {r: {"light": color["light"][r], "dark": color["dark"][r]} for r in color["light"]}
    tokens = {"source": "@material/web tokens v0_192", "palette": palette, "typeface": typeface,
              "sys_color": modes, "sys": sysd, "typescale": scale, "components": comps}
    os.makedirs(OUT, exist_ok=True)
    json.dump(tokens, open(os.path.join(OUT, "tokens.json"), "w"), indent=1, sort_keys=True)
    open(os.path.join(OUT, "m3.css"), "w").write(curated.render_css(tokens))
    json.dump(curated.guidelines(tokens), open(os.path.join(OUT, "guidelines.json"), "w"), indent=1)
    print(f"palette={len(palette)} roles={len(modes)} typescale={len(scale)} components={len(comps)}"
          f" comp-tokens={sum(len(c) for c in comps.values())}")


if __name__ == "__main__":
    main(sys.argv[1])
