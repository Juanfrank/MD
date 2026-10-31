# The 36 `spec` guidelines checked against `site/` (m3.material.io text)

**Status: closed (2026-10-31).** The differences between the registry (`guidelines.json`, `curated.py`, `m3.css`) and the site are recorded here as they are. Nothing was changed in the registry or the CSS; the registry stays as it was, and this file is the record of where it differs from the site. The "Suggested fixes" at the end are left unapplied on purpose.

Method: for each guideline, grep the crawled pages for the same number/claim. Only text, tables and image alt text were available (no diagrams), so "not found" means "not in the text", not "false".

Legend: OK = confirmed by the site; PARTIAL = core claim confirmed, some part not found; WRONG = site says something different; NONE = nothing on the site to check (our implementation hook).

| Result | Count | Guidelines |
|---|---|---|
| OK | 24 | `spacing.step.0,1,2,4,6,8,10,12,14,16` (0, 4, 8, 16, 24, 32, 40, 48, 56, 64dp); `layout.window.compact`, `layout.window.medium`; `layout.pane-spacer`; `layout.grid`; `a11y.touch-target`; `a11y.touch-gap`; `a11y.contrast.text`; `a11y.contrast.ui`; `a11y.focus`; `state.layer`; `color.theme.light`; `color.theme.dark`; `color.scrim`; `surface.base` |
| PARTIAL | 7 | `layout.window.expanded/large/extra-large` (breakpoint and 24dp margin confirmed; 12 columns not stated in text); `a11y.contrast.level.medium/high` (the three contrast levels exist; 0.5 / 1.0 are not on the site); `a11y.disabled` (disabled behaviour confirmed; 12% / 38% not on the site); `a11y.reduced-motion` (site: subtle fades instead of slide/scale, no parallax or shape morphing; ours says "shorten/remove") |
| WRONG | 3 | `spacing.step.3,5,7` (12, 20, 28dp) |
| NONE | 2 | `layout.gutter` (8dp: not mentioned anywhere); `a11y.contrast.prefers-more` (CSS media query, not a spec item) |

## Details

- **Breakpoints.** Site table: compact < 600, medium 600-839, expanded 840-1199, large 1200-1599, extra-large 1600+. Matches. Margins: 16dp compact, 24dp for the rest. Matches. Pane spacer 24dp (medium and up). Matches. Columns: 4 (compact) and 8 (medium) appear in image captions; 12 does not appear. The site now calls these "breakpoints" ("previously window size classes").
- **Spacing (the real problem).** The site says the base unit is `space100` = 8dp, the main units are multiples of 8dp (range 0x-9x), and the only official nested units are 0.25x, 0.5x, 0.75x, 1.25x (2, 4, 6, 10dp). Our rule text "multiples of 4dp (8dp for layout)" is therefore inaccurate for all 13 steps, and 12, 20 and 28dp (1.5x, 2.5x, 3.5x) are not official tokens. Also missing: 72dp (9x) and the nested 2, 6, 10dp. The site names tokens `space100`, `space200`... ours are `spacing-1..16`.
- **Touch target and gap.** 48x48dp confirmed. 8dp between targets is "in most cases", a recommendation, not a hard rule.
- **Contrast.** 4.5:1 small text and 3:1 large text/graphics confirmed (large = 14pt bold / 18pt regular). `outline` (not `outline-variant`) gives at least 3:1 (confirmed). Disabled states are exempt.
- **Scrim.** "Scrims use the scrim color role at an opacity of 32%." Exact match.

## Extra spot checks on `token` guidelines

- State layer opacities: the site says hover 8%, focus 10%, press 10%, drag 16%. The registry (`@material/web` v0_192) has hover 0.08, **focus 0.12, pressed 0.12**, dragged 0.16. So focus and pressed DIFFER (12% vs 10%). An earlier version of this file wrongly said they matched. `tools/material3/audit.py` accepts both values for these two tokens.
- Colour roles: the site says "26 standard color roles" and "all 45 color roles" in one image caption; the registry counts 49 `md.sys.color.*`. Not reconciled (different counting, possibly fixed/surface variants).

## Suggested fixes (not applied)

1. Re-base `spacing.*` on 8dp with nested 2/4/6/10dp, add 72dp, drop or mark 12/20/28 as custom, fix the rule text.
2. Decide whether focus/pressed should be 0.10 (site) or 0.12 (package).
3. Mark `layout.gutter` and `a11y.contrast.prefers-more` as "implementation, no spec source".
4. Reword `a11y.reduced-motion` to match the site.
