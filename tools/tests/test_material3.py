"""Material 3 guideline registry (docs/material3): counts the guidelines it declares, checks each one is
really present in m3.css with its CSS, and checks the light/dark mapping and the contrast of the pairs.

Run from the repository root:  python -m unittest discover -s tools/tests
Regenerate the data with:      python3 tools/material3/build_material3.py <unpacked @material/web dir>
"""
import collections
import json
import os
import re
import unittest

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "material3")
load = lambda n: open(os.path.join(DOCS, n), encoding="utf-8").read()  # noqa: E731
CSS = load("m3.css")
TOKENS = json.loads(load("tokens.json"))
GUIDES = json.loads(load("guidelines.json"))

# Independent expectations (the M3 spec's own counts), so a silently shrunken registry fails.
EXPECTED = {
    "color-roles-sys": 49,   # md.sys.color.* incl. fixed roles, containers, surfaces, inverse
    "typescale-styles": 15,  # display/headline/title/body/label x large/medium/small
    "shape-corners": 7,      # none, xs, s, m, l, xl, full
    "elevation-levels": 6,   # 0..5
    "state-opacities": 4,    # hover, focus, pressed, dragged
    "motion-durations": 16,  # short1-4, medium1-4, long1-4, extra-long1-4
    "motion-easings": 10,    # emphasized(3), standard(3), legacy(3), linear
    "window-classes": 5,
    "components": 84,
}


def lum(hexc):
    h = hexc.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


class GuidelineCount(unittest.TestCase):
    def test_counts_match_the_spec(self):
        n = lambda pat: sum(1 for g in GUIDES if re.fullmatch(pat, g["id"]))  # noqa: E731
        got = {
            "color-roles-sys": n(r"color\.role\..+"),
            "typescale-styles": n(r"type\.(display|headline|title|body|label)-(large|medium|small)"),
            "shape-corners": n(r"shape\.corner-(none|extra-small|small|medium|large|extra-large|full)"),
            "elevation-levels": n(r"elevation\.level[0-5]"),
            "state-opacities": n(r"state\..+-state-layer-opacity"),
            "motion-durations": n(r"motion\.duration-.+"),
            "motion-easings": n(r"motion\.easing-.+") - 0,
            "window-classes": n(r"layout\.window\..+"),
            "components": n(r"component\..+"),
        }
        self.assertEqual(got, EXPECTED)

    def test_every_guideline_has_its_css(self):
        missing = {g["id"]: [n for n in g["css"] if n not in CSS] for g in GUIDES}
        missing = {k: v for k, v in missing.items() if v}
        by_src = collections.Counter(g["source"] for g in GUIDES)
        with_css = sum(1 for g in GUIDES if g["css"])
        print(f"\nMaterial 3 guidelines declared: {len(GUIDES)} "
              f"({dict(by_src)}); with CSS: {with_css}; "
              f"present in m3.css: {len(GUIDES) - len(missing)}; missing: {len(missing)}")
        print("by category:", dict(sorted(collections.Counter(g['category'] for g in GUIDES).items())))
        self.assertEqual(with_css, len(GUIDES), "a guideline without CSS")
        self.assertEqual(missing, {}, "guidelines whose CSS is not in m3.css")

    def test_ids_are_unique(self):
        ids = [g["id"] for g in GUIDES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_component_token_is_in_the_css(self):
        n = 0
        for comp, toks in TOKENS["components"].items():
            for k, v in toks.items():
                self.assertIn(f"--md-{comp}-{k}: {v};", CSS)
                n += 1
        self.assertGreater(n, 3000)


class Typography(unittest.TestCase):
    def rem(self, s):
        return float(s.replace("rem", ""))

    def test_line_spacing(self):
        ts = TOKENS["typescale"]
        for s in {k.rsplit("-", 1)[0] for k in ts if k.endswith("-size")}:
            size, lh = self.rem(ts[s + "-size"]), self.rem(ts[s + "-line-height"])
            self.assertGreater(lh, size, s)
            self.assertAlmostEqual(lh * 16 % 4, 0, msg=f"{s} line-height is on the 4dp grid")
            self.assertGreaterEqual(lh / size, 1.1, s)

    def test_body_text_line_height_ratio(self):
        ts = TOKENS["typescale"]
        for s in ("body-large", "body-medium", "body-small"):
            self.assertGreaterEqual(self.rem(ts[s + "-line-height"]) / self.rem(ts[s + "-size"]), 1.33, s)


class LightDark(unittest.TestCase):
    PAIRS = [("primary", "on-primary"), ("primary-container", "on-primary-container"),
             ("secondary", "on-secondary"), ("secondary-container", "on-secondary-container"),
             ("tertiary", "on-tertiary"), ("tertiary-container", "on-tertiary-container"),
             ("error", "on-error"), ("error-container", "on-error-container"),
             ("surface", "on-surface"), ("surface", "on-surface-variant"), ("background", "on-background"),
             ("inverse-surface", "inverse-on-surface"), ("surface-container", "on-surface"),
             ("surface-container-highest", "on-surface"), ("surface-dim", "on-surface")]

    def hexof(self, role, mode):
        return TOKENS["palette"][TOKENS["sys_color"][role][mode]]

    def test_contrast_of_pairs(self):
        for mode in ("light", "dark"):
            for bg, fg in self.PAIRS:
                r = ratio(self.hexof(bg, mode), self.hexof(fg, mode))
                self.assertGreaterEqual(r, 4.5, f"{mode}: {fg} on {bg} = {r:.2f}")

    def test_outline_meets_non_text_contrast(self):
        for mode in ("light", "dark"):
            self.assertGreaterEqual(ratio(self.hexof("outline", mode), self.hexof("surface", mode)), 3.0, mode)

    def test_dark_is_not_a_plain_inversion(self):
        """Light and dark use the same palette with different tones: key colours 40 <-> 80, containers 90 <-> 30,
        on-colours 100 <-> 20, surface 98 <-> 6. No role maps light tone T to dark tone 100-T by rule."""
        sc = TOKENS["sys_color"]
        tone = lambda s: int("".join(c for c in s if c.isdigit()) or 0)  # noqa: E731
        self.assertEqual((tone(sc["primary"]["light"]), tone(sc["primary"]["dark"])), (40, 80))
        self.assertEqual((tone(sc["primary-container"]["light"]), tone(sc["primary-container"]["dark"])), (90, 30))
        self.assertEqual((tone(sc["on-primary"]["light"]), tone(sc["on-primary"]["dark"])), (100, 20))
        self.assertEqual((tone(sc["surface"]["light"]), tone(sc["surface"]["dark"])), (98, 6))
        self.assertEqual((tone(sc["on-surface"]["light"]), tone(sc["on-surface"]["dark"])), (10, 90))
        # fixed roles keep the same tone in both modes
        for r in ("primary-fixed", "primary-fixed-dim", "on-primary-fixed", "secondary-fixed", "tertiary-fixed"):
            self.assertEqual(sc[r]["light"], sc[r]["dark"], r)

    def test_every_role_is_defined_in_both_modes_in_css(self):
        for role, m in TOKENS["sys_color"].items():
            self.assertIn(f"--md-sys-color-{role}: var(--md-ref-palette-{m['light']});", CSS)
            self.assertIn(f"--md-sys-color-{role}: var(--md-ref-palette-{m['dark']});", CSS)


class Spacing(unittest.TestCase):
    """m3.material.io/styles/spacing/tokens: base unit space100 = 8dp, range 0x-9x, nested 0.25x/0.5x/0.75x/1.25x."""

    def test_spacing_tokens_match_the_site(self):
        got = {}
        for g in GUIDES:
            if g["id"].startswith("spacing."):
                name, val = g["css"][0].split(": ")
                got[name.replace("--md-sys-measurement-", "")] = float(val.replace("rem", "")) * 16
        want = {"space0": 0, "space25": 2, "space50": 4, "space75": 6, "space100": 8, "space125": 10}
        want.update({f"space{n * 100}": n * 8 for n in range(2, 10)})
        self.assertEqual(got, want)
        for name, dp in got.items():
            self.assertIn(f"--md-sys-measurement-{name}: {dp / 16:g}rem;", CSS)


class Sources(unittest.TestCase):
    def test_sources_are_known_and_counted(self):
        by = collections.Counter(g["source"] for g in GUIDES)
        self.assertEqual(set(by), {"token", "site", "spec", "impl"})
        self.assertEqual(by["site"], 2)
        self.assertEqual(by["impl"], 2)

    def test_site_overrides_are_recorded_and_applied(self):
        self.assertEqual(TOKENS["overrides"]["state.focus-state-layer-opacity"], {"package": "0.12", "site": "0.1"})
        self.assertEqual(TOKENS["overrides"]["state.pressed-state-layer-opacity"], {"package": "0.12", "site": "0.1"})
        self.assertIn("--md-sys-state-focus-state-layer-opacity: 0.1;", CSS)
        self.assertIn("--md-sys-state-hover-state-layer-opacity: 0.08;", CSS)

    def test_disabled_opacities_are_the_packages_own(self):
        """The 12% / 38% of a11y.disabled are not on the site, but the official component tokens use them."""
        vals = {v for comp in TOKENS["components"].values() for k, v in comp.items() if "disabled" in k and "opacity" in k}
        self.assertTrue({"0.12", "0.38"} <= vals, vals)


if __name__ == "__main__":
    unittest.main()
