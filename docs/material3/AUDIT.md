# Auditing a repository against Material 3

`tools/material3/audit.py` reads the CSS and design-token files of any repository and compares them with this registry (`m3.css`, `guidelines.json`). Python 3 standard library only; files are read as text, nothing is executed.

```
python3 tools/material3/audit.py path/to/repo                       # text report
python3 tools/material3/audit.py path/to/repo --format md --out m3-audit.md
python3 tools/material3/audit.py path/to/repo --format json         # for CI / dashboards
python3 tools/material3/audit.py path/to/repo --fail-on warn        # exit 1 on warn or worse (CI gate)
python3 tools/material3/audit.py path/to/repo --ignore 'legacy/*' --max-per-rule 50 --no-coverage
```

## What it reads

| Input | How |
|---|---|
| `*.css *.scss *.less *.pcss` | nested selectors (`&`, comma lists) are flattened; SCSS `$x` and Less `@x` variables are substituted; simple arithmetic (`$gap * 2`, `math.div(24px, 2)`) is evaluated |
| `<style>` blocks of `*.html *.vue *.svelte`; `style="..."` attributes of html/vue/svelte/jsx/tsx | parsed as CSS (line numbers kept) |
| `*.js *.jsx *.ts *.tsx *.mjs *.cjs` | CSS-in-JS tagged templates (`css`, `styled.tag`, `styled(X)`, `keyframes`, `createGlobalStyle`, `injectGlobal`; `${expr}` marked as not evaluable) and JSX `style={{...}}` / `sx={{...}}` object literals |
| `*.json` | design tokens whose keys map to `--md-*` (`md.sys.color.primary`; `$value` / `value` leaves) |
| `colors.xml`, `Color.kt`, `color_schemes.g.dart` | Material Theme Builder exports (`md_theme_light_primary`, `Brightness.dark` blocks) mapped to `--md-sys-color-*` in light and dark |

`node_modules`, `.git`, `dist`, `build`, `vendor`, `*.min.css` and files over 2 MB are skipped.

## Validate (findings)

| Rule | Severity | Checks |
|---|---|---|
| `token-unknown` | warn | `--md-sys-*`/`--md-ref-*` name not in the registry (suggests the closest, typos) |
| `token-value` | warn (info for colours) | known token with a value different from the baseline; `0.5rem` = `8px`, `.2s` = `200ms`, `var()` chains resolved per mode |
| `hardcoded-color` | info | literal colour in a colour property; suggests the nearest baseline role |
| `shape-radius` | warn | `border-radius` not in the shape scale (0, 4, 8, 12, 16, 28, full), also when reached through a custom property or variable (`via var(--x)`) |
| `motion-duration`, `motion-easing` | warn | duration or easing outside the M3 tokens; CSS keywords such as `ease-in-out` |
| `type-size`, `type-weight` | warn, info | font size not in the type scale (icon sizes ignored); weight other than 400/500/700 |
| `touch-target` | warn | interactive selector with width/height under 48px (heuristic) |
| `spacing-grid` | info | margin/padding/gap off the 4dp grid (M3: multiples of 8dp, nested 2, 4, 6, 10dp) |
| `contrast` | warn / error under 3:1 | `color` vs `background` of one selector merged across files, in light and in dark; `:hover`, `:focus`, `:active`... inherit from their base selector; disabled states are exempt (as the site says); 4.5:1, or 3:1 for text of 24px or more |
| `role-pair-contrast` | warn | `--md-sys-color-on-X` vs `X` under 4.5:1, checked in light and in dark (`[light]` / `[dark]` in the message) |
| `focus-removed` | warn | `:focus { outline: none }` with no replacement indicator |
| `no-reduced-motion`, `no-focus-visible`, `no-dark-theme` | warn, info, info | project-level hooks missing |

Dark mode is recognised from `@media (prefers-color-scheme: dark)`, `[data-theme=dark]` (and `data-*-scheme/mode`), `.dark`, `.theme-dark`, `.dark-theme`.

## Compare (coverage)

For each of the 329 guidelines, the repository is `exact` (every CSS string of the guideline is present, same value, in light or dark), `name` (the token is defined with another value, for example a brand colour) or `missing`. The report prints counts per category. Auditing `docs/material3/m3.css` itself gives 329/329 exact and no findings (it is a test).

## What it cannot see (and how that is made visible)

The report prints a line `Not evaluated: N check(s) over M declaration(s) (reason: count, ...)` and the JSON has `not_evaluated`. Reasons: `preprocessor` (an unresolved `$x`/`@x`/`#{}`, mixin or function), `js-expression` (`${...}` in CSS-in-JS), `calc/min/max/clamp/env`, `unresolved var()` (custom property defined nowhere in the scan), `contrast: colour not resolvable` (gradients, images, system colours). A clean report with a large "Not evaluated" is not a pass.

Remaining limits:
- No DOM and no browser: inheritance from ancestors (`color` set on a parent), specificity, `!important`, the real cascade order across files, and which element a selector actually matches are not modelled. State selectors inherit from their base selector, and same-selector rules are merged across files, but that is an approximation.
- No code execution: JS-computed styles, mixins, SCSS functions/maps/`@each`, Tailwind classes, MUI/Compose/Flutter themes other than the Theme Builder colour exports, and Android `<style>` resources are not read.
- Dark mode is limited to the detected selectors above; a custom mechanism (class names such as `.night`) is not recognised.
- The reference itself: `spec` guidelines are verified against the crawled site text only (see `VERIFICATION.md`); a diagram-only rule is not covered.
