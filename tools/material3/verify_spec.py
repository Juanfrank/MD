#!/usr/bin/env python3
"""Checks every non-token guideline (spec / site / impl) of docs/material3/guidelines.json against its evidence in
docs/material3/spec_evidence.json: each pattern must match in the crawled m3.material.io text (site/) or in m3.css.

  python3 tools/material3/verify_spec.py            # prints the table, exit 1 if anything fails
  python3 tools/material3/verify_spec.py --write    # also refreshes the generated table in VERIFICATION.md

Limits: the site text has no diagrams or images (only alt text), and a regex match shows that the page says the thing,
not that the page is right. Refresh site/ first with tools/material3/crawl_site.js if the site changed.
"""
import argparse
import fnmatch
import json
import os
import re
import sys

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "material3")
BEGIN, END = "<!-- BEGIN GENERATED -->", "<!-- END GENERATED -->"


def load(name):
    with open(os.path.join(DOCS, name), encoding="utf-8") as f:
        return json.load(f)


def site_files():
    d = os.path.join(DOCS, "site")
    return {n: open(os.path.join(d, n), encoding="utf-8").read() for n in sorted(os.listdir(d)) if n.endswith(".md")}


def check():
    guides = [g for g in load("guidelines.json") if g["source"] != "token"]
    evid = load("spec_evidence.json")
    site = site_files()
    with open(os.path.join(DOCS, "m3.css"), encoding="utf-8") as f:
        css = f.read()
    rows, problems = [], []
    for g in guides:
        e = evid.get(g["id"])
        if e is None:
            problems.append(f"{g['id']}: no evidence entry")
            continue
        failed = []
        for ev in e["evidence"]:
            rx = re.compile(ev["pattern"], re.I)
            if ev.get("in") == "css":
                ok = bool(rx.search(css))
            else:
                ok = any(rx.search(t) for n, t in site.items() if fnmatch.fnmatch(n, ev["file"]))
            if not ok:
                failed.append(ev["pattern"])
        if e["status"] == "impl" and e["evidence"]:
            problems.append(f"{g['id']}: impl guideline should have no evidence")
        if e["status"] in ("ok", "partial") and not e["evidence"]:
            problems.append(f"{g['id']}: {e['status']} but no evidence")
        if e["status"] == "partial" and not e.get("gap"):
            problems.append(f"{g['id']}: partial needs a `gap`")
        for pat in failed:
            problems.append(f"{g['id']}: evidence not found: {pat}")
        rows.append((g["id"], g["source"], e["status"] if not failed else "FAIL", e.get("gap", "")))
    stale = set(evid) - {g["id"] for g in guides} - {"_doc"}
    problems += [f"{i}: evidence for a guideline that is not spec/site/impl" for i in sorted(stale)]
    return rows, problems


def table(rows):
    count = {}
    for r in rows:
        count[r[2]] = count.get(r[2], 0) + 1
    L = ["| Result | Count |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(count.items())]
    L += ["", "| Guideline | Source | Result | Gap (what the site does not state) |", "|---|---|---|---|"]
    L += [f"| `{i}` | {s} | {r} | {g} |" for i, s, r, g in rows]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    rows, problems = check()
    t = table(rows)
    print(t)
    for p in problems:
        print("PROBLEM:", p, file=sys.stderr)
    if a.write:
        path = os.path.join(DOCS, "VERIFICATION.md")
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if BEGIN in text:
            text = re.sub(re.escape(BEGIN) + ".*?" + re.escape(END), lambda m: f"{BEGIN}\n{t}\n{END}", text, flags=re.S)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
