# Auditing a repository against Material 3

`tools/material3/audit.py` reads the CSS and design-token files of any repository and compares them with this registry (`m3.css`, `guidelines.json`). Python 3 standard library only; files are read as text, nothing is executed.

```
python3 tools/material3/audit.py path/to/repo                       # text report
python3 tools/material3/audit.py path/to/repo --format md --out m3-audit.md
python3 tools/material3/audit.py path/to/repo --format json         # for CI / dashboards
python3 tools/material3/audit.py path/to/repo --fail-on warn        # exit 1 on warn or worse (CI gate)
python3 tools/material3/audit.py path/to/repo --ignore 'legacy/*' --max-per-rule 50 --no-coverage
```

Files read: `*.css *.scss *.less *.pcss`, `<style>` blocks in `*.html *.vue *.svelte`, and `*.json` token files whose keys map to `--md-*` names (`md.sys.color.primary` -> `--md-sys-color-primary`; `$value`/`value` leaves). `node_modules`, `.git`, `dist`, `build`, `vendor`, `*.min.css` are skipped.

## Validate (findings)

| Rule | Severity | Checks |
|---|---|---|
| `token-unknown` | warn | `--md-sys-*`/`--md-ref-*` name not in the registry (suggests the closest, typos) |
| `token-value` | warn (info for colours) | known token with a value different from the baseline; `0.5rem` = `8px`, `.2s` = `200ms`, `var()` chains are resolved |
| `hardcoded-color` | info | literal colour in a colour property; suggests the nearest baseline role |
| `shape-radius` | warn | `border-radius` not in the shape scale (0, 4, 8, 12, 16, 28, full) |
| `motion-duration`, `motion-easing` | warn | duration or easing outside the M3 tokens; CSS keywords such as `ease-in-out` |
| `type-size`, `type-weight` | warn, info | font size not in the type scale; weight other than 400/500/700 |
| `touch-target` | warn | interactive selector with width/height under 48px (heuristic) |
| `spacing-grid` | info | margin/padding/gap off the 4dp grid (M3: multiples of 8dp, nested 2/4/6/10dp) |
| `contrast` | warn / error under 3:1 | `color` vs `background` in one rule, WCAG 4.5:1 (3:1 for text of 24px or more) |
| `role-pair-contrast` | warn | `--md-sys-color-on-X` vs `X` defined in the same block under 4.5:1 |
| `focus-removed` | warn | `:focus { outline: none }` with no replacement indicator |
| `no-reduced-motion`, `no-focus-visible`, `no-dark-theme` | warn, info, info | project-level hooks missing |

## Compare (coverage)

For each of the 328 guidelines, the repository is `exact` (every CSS string of the guideline is present, same value), `name` (the token is defined with another value, for example a brand colour) or `missing`. The report prints counts per category. Auditing `docs/material3/m3.css` itself gives 328/328 exact and no findings (it is a test).

## Limits

- Text scan, not a CSS engine: no cascade, no selector matching, no JS or preprocessor evaluation. Findings are leads to review.
- Dark-mode contrast is only checked for pairs defined in one block.
- The reference has two known open differences with m3.material.io (see `VERIFICATION.md`): focus/pressed state layer 0.12 (package) vs 0.10 (site, both accepted), and the 12/20/28dp spacing steps.
- Rules for `spec` guidelines inherit the "not machine-verified" caveat of the README.
