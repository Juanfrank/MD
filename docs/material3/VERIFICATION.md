# The non-token guidelines checked against `site/` (m3.material.io text)

**Status: corrections applied (2026-10-31).** The first pass found 24 OK / 7 partial / 3 wrong / 2 without source for the 36 hand-written (`spec`) guidelines. The wrong and unsupported ones were fixed in `tools/material3/curated.py`, the CSS, tokens and registry were regenerated from `@material/web` v0_192, and the check is now a script instead of a one-off grep:

```
python3 tools/material3/verify_spec.py            # table + exit 1 if any evidence stops matching
python3 tools/material3/verify_spec.py --write    # refresh the table below
```

Evidence lives in `spec_evidence.json` (a regex per claim, searched in `site/*.md` or in `m3.css`) and is enforced by `tools/tests/test_verify_spec.py`. Only text, tables and image alt text were crawled (no diagrams), and a regex match proves that the page says it, not that the page is right.

## What changed

| Before | After |
|---|---|
| 13 spacing steps `--md-sys-spacing-N` on a "4dp grid" (4, 12, 20, 28dp not official) | 14 tokens `--md-sys-measurement-space<pct>`: base unit space100 = 8dp, 0x-9x (0..72dp) plus nested 0.25x/0.5x/0.75x/1.25x (2, 4, 6, 10dp); ids `spacing.space*` |
| focus / pressed state layer 0.12 (package) | 0.10 (site). Recorded in `tokens.json` `overrides` with both values; guideline source `site`. The auditor still accepts 0.12 |
| `layout.gutter` and `prefers-contrast` listed as `spec` | source `impl` (no spec source) |
| Window rules said "8dp gutters" (not on the site) | rule text is columns + margins; gutter lives only in `layout.gutter` (impl) |
| Pane spacer "on large windows" | "medium breakpoint and up" (what the site says) |
| `a11y.reduced-motion`: "shorten/remove transitions" | the site's wording (fades instead of slide/scale, no parallax or shape morphing) and what this CSS really does (zeroes the short durations) |
| Contrast levels 0.5 / 1.0 presented as spec | marked as coming from material-color-utilities (the site names the levels, gives no numbers) |
| 12% / 38% disabled opacities "not machine-verified" | checked against the official component tokens in `m3.css` (evidence `in: css`) |

Sources now: `token` 290 (exact, from `@material/web`), `site` 2, `spec` 35, `impl` 2.

## Result

<!-- BEGIN GENERATED -->
| Result | Count |
|---|---|
| impl | 2 |
| ok | 32 |
| partial | 5 |

| Guideline | Source | Result | Gap (what the site does not state) |
|---|---|---|---|
| `state.focus-state-layer-opacity` | site | ok |  |
| `state.pressed-state-layer-opacity` | site | ok |  |
| `spacing.space0` | spec | ok |  |
| `spacing.space25` | spec | ok |  |
| `spacing.space50` | spec | ok |  |
| `spacing.space75` | spec | ok |  |
| `spacing.space100` | spec | ok |  |
| `spacing.space125` | spec | ok |  |
| `spacing.space200` | spec | ok |  |
| `spacing.space300` | spec | ok |  |
| `spacing.space400` | spec | ok |  |
| `spacing.space500` | spec | ok |  |
| `spacing.space600` | spec | ok |  |
| `spacing.space700` | spec | ok |  |
| `spacing.space800` | spec | ok |  |
| `spacing.space900` | spec | ok |  |
| `layout.window.compact` | spec | ok |  |
| `layout.window.medium` | spec | ok |  |
| `layout.window.expanded` | spec | partial | 12 columns is not stated in the page text |
| `layout.window.large` | spec | partial | 12 columns is not stated in the page text |
| `layout.window.extra-large` | spec | partial | 12 columns is not stated in the page text |
| `layout.gutter` | impl | impl | no gutter value on m3.material.io (text) |
| `layout.pane-spacer` | spec | ok |  |
| `layout.grid` | spec | ok |  |
| `a11y.touch-target` | spec | ok |  |
| `a11y.touch-gap` | spec | ok |  |
| `a11y.contrast.text` | spec | ok |  |
| `a11y.contrast.ui` | spec | ok |  |
| `a11y.contrast.level.medium` | spec | partial | the levels exist but 0.5 is not on the site (it comes from material-color-utilities) |
| `a11y.contrast.level.high` | spec | partial | the levels exist but 1.0 is not on the site (it comes from material-color-utilities) |
| `a11y.contrast.prefers-more` | impl | impl | CSS media query hook, not an M3 spec item |
| `a11y.reduced-motion` | spec | ok |  |
| `a11y.focus` | spec | ok |  |
| `a11y.disabled` | spec | ok |  |
| `state.layer` | spec | ok |  |
| `color.theme.light` | spec | ok |  |
| `color.theme.dark` | spec | ok |  |
| `color.scrim` | spec | ok |  |
| `surface.base` | spec | ok |  |
<!-- END GENERATED -->

## Still open

- 12 columns for expanded / large / extra-large: the layout pages state margins and breakpoints but not the column count in text.
- Contrast level numbers (0.5, 1.0) and the exact `data-contrast` hook are ours.
- Colour roles: the site says "26 standard color roles" and, in one image caption, "45"; the registry has 49 `md.sys.color.*` from the package. Not reconciled (counting differs: fixed, surface-container and inverse roles).
- Focus / pressed 0.10 follows the site; if the package is right and the site stale, flip `SITE_OVERRIDES` in `curated.py` and rebuild.
