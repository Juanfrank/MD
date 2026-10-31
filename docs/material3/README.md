# Material 3 guidelines (registry, CSS and tests)

| File | What |
|---|---|
| `m3.css` | All the CSS: reference palette, 49 colour roles (light, dark by `prefers-color-scheme` or `data-theme`), type scale with line height and tracking, shape, elevation, state layers, motion, spacing, layout grid, a11y hooks, and 3,064 component tokens (84 components). |
| `tokens.json` | The extracted data (palette, light/dark tone per role, type scale, components). |
| `guidelines.json` | 328 guidelines, each with the CSS strings that must be in `m3.css`. |
| `tools/material3/` | `build_material3.py` (regenerates the above from the unpacked `@material/web` package, reading the `.scss` as text only), `curated.py` (data not in the tokens, and the registry). |
| `tools/tests/test_material3.py` | Counts the guidelines against the spec's own counts, checks every one has its CSS in `m3.css`, plus contrast, line spacing and light/dark checks. |

| `site/` | Text of the 375 pages of m3.material.io (see `site/INDEX.md`), crawled with `tools/material3/crawl_site.js` (Playwright, from the sitemap). Text, tables and image alt text only; not machine-checked against `guidelines.json`. About 10 pages (blog videos, a few overviews) are nearly empty because they have no text. |
| `VERIFICATION.md`, `spec_evidence.json`, `tools/material3/verify_spec.py` | Reproducible check of every non-token guideline against `site/` (32 ok, 5 partial, 2 implementation-only) and the corrections that came out of it. Enforced by `tools/tests/test_verify_spec.py`. |
| `AUDIT.md` + `tools/material3/audit.py` | Tool to audit any repository's CSS / SCSS / Less / CSS-in-JS / token / Theme Builder files against this registry (findings + coverage, light and dark). Tests in `tools/tests/test_audit.py`. |

Regenerate: `npm pack @material/web && mkdir w && tar xzf material-web-*.tgz -C w && python3 tools/material3/build_material3.py w`.

## Sources and limits (read this)

- **`token` guidelines (290)** come from the official `@material/web` tokens (v0_192): exact. **`site` (2)**: the focus and pressed state-layer opacity, where m3.material.io (0.10) and the package (0.12) disagree and the site wins (`tokens.json` `overrides`).
- **`spec` guidelines (35)**: breakpoints and margins, 8dp spacing tokens, 48dp touch target, WCAG ratios, state layer, scrim, light/dark. Hand-written, but every one now has regex evidence in `spec_evidence.json` checked against the crawled site text (`verify_spec.py`); 5 are only partly stated by the site (listed with their gap in `VERIFICATION.md`). **`impl` (2)**: gutter and `prefers-contrast`, implementation choices with no spec source.
- "Every guideline in M3" is not something a test can prove: the test proves the registry's own count and that each entry's CSS exists. It cannot know about guidelines nobody listed (for example per-component anatomy text, M3 Expressive, or the Wear OS / large-screen pattern pages).
- **Light/dark algorithm.** Dark is not an inversion. Both modes read the same tonal palettes; each role picks a different tone (`tokens.json` -> `sys_color`): key colours 40 -> 80, containers 90 -> 30, on-colours 100 -> 20, surface 98 -> 6, on-surface 10 -> 90; fixed roles (`*-fixed`) keep their tone. Arbitrary-seed schemes and the medium/high contrast palettes need the HCT solver of `material-color-utilities`; that code was not run here, so `data-contrast` and `prefers-contrast` are hooks (`--md-sys-contrast-level`), not new palettes. The CSS carries the baseline (purple) palette.
