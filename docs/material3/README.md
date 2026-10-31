# Material 3 guidelines (registry, CSS and tests)

| File | What |
|---|---|
| `m3.css` | All the CSS: reference palette, 49 colour roles (light, dark by `prefers-color-scheme` or `data-theme`), type scale with line height and tracking, shape, elevation, state layers, motion, spacing, layout grid, a11y hooks, and 3,064 component tokens (84 components). |
| `tokens.json` | The extracted data (palette, light/dark tone per role, type scale, components). |
| `guidelines.json` | 328 guidelines, each with the CSS strings that must be in `m3.css`. |
| `tools/material3/` | `build_material3.py` (regenerates the above from the unpacked `@material/web` package, reading the `.scss` as text only), `curated.py` (data not in the tokens, and the registry). |
| `tools/tests/test_material3.py` | Counts the guidelines against the spec's own counts, checks every one has its CSS in `m3.css`, plus contrast, line spacing and light/dark checks. |

Regenerate: `npm pack @material/web && mkdir w && tar xzf material-web-*.tgz -C w && python3 tools/material3/build_material3.py w`.

## Sources and limits (read this)

- **`token` guidelines (292)** come from the official `@material/web` tokens (v0_192): exact.
- **`spec` guidelines (36)**: layout classes and margins, 4/8dp spacing, 48dp touch target, elevation shadows, WCAG ratios, contrast hooks. Written by hand from the m3.material.io spec; m3.material.io is rendered by JavaScript and was not fetched, so these are **not machine-verified**.
- "Every guideline in M3" is not something a test can prove: the test proves the registry's own count and that each entry's CSS exists. It cannot know about guidelines nobody listed (for example per-component anatomy text, M3 Expressive, or the Wear OS / large-screen pattern pages).
- **Light/dark algorithm.** Dark is not an inversion. Both modes read the same tonal palettes; each role picks a different tone (`tokens.json` -> `sys_color`): key colours 40 -> 80, containers 90 -> 30, on-colours 100 -> 20, surface 98 -> 6, on-surface 10 -> 90; fixed roles (`*-fixed`) keep their tone. Arbitrary-seed schemes and the medium/high contrast palettes need the HCT solver of `material-color-utilities`; that code was not run here, so `data-contrast` and `prefers-contrast` are hooks (`--md-sys-contrast-level`), not new palettes. The CSS carries the baseline (purple) palette.
