"""Tests for tools/material3/audit.py: the registry's own CSS must audit clean, and seeded mistakes must be found.

Run from the repository root:  python -m unittest discover -s tools/tests
"""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "material3"))
import audit  # noqa: E402

REF = audit.Ref(audit.DEFAULT_REF)


def scan(files, stats=False):
    with tempfile.TemporaryDirectory() as d:
        for name, text in files.items():
            with open(os.path.join(d, name), "w", encoding="utf-8") as f:
                f.write(text)
        decls, names = audit.read_target(d, audit.DEFAULT_IGNORE, roles=set(REF.first))
    f, st = audit.analyze(decls, REF)
    return (f, audit.coverage(decls, REF), names, st) if stats else (f, audit.coverage(decls, REF), names)


def rules(findings):
    return {f.rule for f in findings}


class SelfAudit(unittest.TestCase):
    def test_registry_css_is_clean_and_fully_covered(self):
        text = open(os.path.join(audit.DEFAULT_REF, "m3.css"), encoding="utf-8").read()
        findings, cov, _ = scan({"m3.css": text})
        self.assertEqual([f.msg for f in findings], [])
        self.assertEqual(len(cov), len(REF.guides))
        self.assertEqual({r["status"] for r in cov}, {"exact"})


class Detects(unittest.TestCase):
    def test_token_checks(self):
        f, _, _ = scan({"a.css": ":root{--md-sys-color-primry:#fff;--md-sys-shape-corner-medium:10px;"
                                 "--md-sys-state-focus-state-layer-opacity:0.1;--md-sys-state-hover-state-layer-opacity:.08}"})
        by = {x.rule: x for x in f}
        self.assertIn("--md-sys-color-primary", by["token-unknown"].hint)
        self.assertEqual([x.msg.split(":")[0] for x in f if x.rule == "token-value"], ["--md-sys-shape-corner-medium"])

    def test_value_equivalence(self):
        f, _, _ = scan({"a.css": ":root{--md-sys-motion-duration-short1:.05s;--md-sys-shape-corner-extra-small:.25rem}"})
        self.assertEqual([x for x in f if x.rule.startswith("token")], [])

    def test_literals(self):
        css = (".b{background:#1976d2;border-radius:6px;transition:opacity .37s ease-in-out;font-size:15px;"
               "padding:7px;font-weight:600}")
        f, _, _ = scan({"a.css": css})
        self.assertTrue({"hardcoded-color", "shape-radius", "motion-duration", "motion-easing", "type-size",
                         "spacing-grid", "type-weight"} <= rules(f))

    def test_contrast_and_touch_and_focus(self):
        css = "button{color:#777;background:#888;height:36px}\nbutton:focus{outline:none}"
        f, _, _ = scan({"a.css": css})
        self.assertTrue({"contrast", "touch-target", "focus-removed"} <= rules(f))
        self.assertEqual([x.severity for x in f if x.rule == "contrast"], ["error"])

    def test_role_pair_contrast(self):
        f, _, _ = scan({"a.css": ":root{--md-sys-color-primary:#6750a4;--md-sys-color-on-primary:#7a68b0}"})
        self.assertIn("role-pair-contrast", rules(f))

    def test_good_css_has_no_warnings(self):
        css = (":root{--md-sys-color-primary:#6750a4}\nbutton{min-height:48px;padding:8px 16px;"
               "border-radius:var(--md-sys-shape-corner-full);color:var(--md-sys-color-on-primary);"
               "background:var(--md-sys-color-primary);transition:opacity 200ms cubic-bezier(.2,0,0,1)}\n"
               "button:focus-visible{outline:2px solid var(--md-sys-color-primary)}\n"
               "@media (prefers-reduced-motion:reduce){button{transition:none}}\n"
               "@media (prefers-color-scheme:dark){:root{--md-sys-color-primary:#d0bcff}}")
        f, _, _ = scan({"a.css": css})
        self.assertEqual([x.msg for x in f if x.severity != "info"], [])

    def test_inputs(self):
        tokens = json.dumps({"md": {"sys": {"shape": {"corner": {"medium": {"$value": "10px"}}}}}})
        html = "<html><style>\n.x{border-radius:6px}\n</style></html>"
        f, _, names = scan({"t.json": tokens, "p.html": html, "s.scss": "// c\n.a{ .b{ padding: 5px } }"})
        self.assertEqual(sorted(names), ["p.html", "s.scss", "t.json"])
        self.assertIn("token-value", rules(f))
        self.assertEqual([x.line for x in f if x.rule == "shape-radius"], [2])
        self.assertIn("spacing-grid", rules(f))

    def test_coverage_partial(self):
        _, cov, _ = scan({"a.css": ":root{--md-sys-shape-corner-medium:10px;--md-sys-shape-corner-small:8px}"
                                 ".md-shape-medium{border-radius:1px}.md-shape-small{border-radius:1px}"})
        st = {r["id"]: r["status"] for r in cov}
        self.assertEqual(sum(1 for v in st.values() if v == "exact"), 1)
        self.assertEqual(sum(1 for v in st.values() if v == "name"), 1)


class Limits(unittest.TestCase):
    """The scanner reaches beyond plain CSS: nesting, preprocessors, states, dark mode, JS, app exports."""

    def test_nested_selectors_and_comma_lists(self):
        decls = audit.parse_css(".a, .b { &:hover { color: red } .c & { x: 1 } .d { y: 2 } }", "t.scss", scss=True)
        sels = {(d.prop, d.selector) for d in decls}
        self.assertIn(("color", ".a:hover, .b:hover"), sels)
        self.assertIn(("x", ".c .a, .c .b"), sels)
        self.assertIn(("y", ".a .d, .b .d"), sels)

    def test_scss_and_less_variables_and_arithmetic(self):
        scss = "$r: 6px;\n$gap: 4px;\n.b{ border-radius: $r; padding: $gap * 2; margin: math.div(24px, 2) }"
        less = "@r: 6px;\n.l{ border-radius: @r }"
        f, _, _, st = scan({"a.scss": scss, "b.less": less}, stats=True)
        self.assertEqual([x.file for x in f if x.rule == "shape-radius"], ["a.scss", "b.less"])
        self.assertNotIn("spacing-grid", rules(f))  # 8px and 12px are fine
        self.assertNotIn("preprocessor", st["not_evaluated"])

    def test_unresolved_preprocessor_is_counted_not_silently_passed(self):
        f, _, _, st = scan({"a.scss": ".b{ border-radius: $missing; width: calc(100% - 4px) }"}, stats=True)
        self.assertEqual(st["not_evaluated"].get("preprocessor"), 1)
        self.assertEqual(st["not_evaluated"].get("calc/min/max/clamp/env"), 1)
        self.assertNotIn("shape-radius", rules(f))

    def test_values_reached_through_custom_properties(self):
        f, _, _ = scan({"a.css": ":root{--my-radius:6px}.c{border-radius:var(--my-radius)}"})
        self.assertIn("(via var(--my-radius))", [x.msg for x in f if x.rule == "shape-radius"][0])

    def test_state_selector_inherits_from_base_selector(self):
        css = ".btn{background:#6750a4;color:#fff}.btn:hover{color:#8a78b8}"
        f, _, _ = scan({"a.css": css})
        self.assertEqual([x.msg.split(": ")[0] for x in f if x.rule == "contrast"], [".btn:hover"])
        f, _, _ = scan({"a.css": css.replace(".btn:hover", ".btn:disabled")})
        self.assertNotIn("contrast", rules(f))  # disabled is exempt

    def test_rules_are_merged_across_files(self):
        f, _, _ = scan({"a.css": ".x{color:#777}", "b.css": ".x{background:#888}"})
        self.assertIn("contrast", rules(f))

    def test_dark_mode_contrast(self):
        css = (":root{--bg:#ffffff;--fg:#202020}\n@media (prefers-color-scheme: dark){:root{--bg:#222222;--fg:#2a2a2a}}\n"
               ".t{background:var(--bg);color:var(--fg)}")
        f, _, _ = scan({"a.css": css})
        msgs = [x.msg for x in f if x.rule == "contrast"]
        self.assertEqual(len(msgs), 1)
        self.assertTrue(msgs[0].endswith("[dark]"), msgs)

    def test_role_pair_contrast_in_dark_only(self):
        css = (":root{--md-sys-color-primary:#6750a4;--md-sys-color-on-primary:#ffffff}\n"
               "[data-theme=\"dark\"]{--md-sys-color-primary:#d0bcff;--md-sys-color-on-primary:#e0d0ff}")
        f, _, _ = scan({"a.css": css})
        self.assertEqual([x.msg.endswith("[dark]") for x in f if x.rule == "role-pair-contrast"], [True])

    def test_css_in_js_and_inline_styles(self):
        js = ("const B = styled.button`\n  min-height: 36px;\n  border-radius: ${p => p.r}px 6px;\n`;\n"
              "const C = () => <div style={{ borderRadius: 6, padding: '7px' }} />;\n")
        html = '<p style="font-size: 15px; border-radius: 6px">x</p>'
        f, _, names = scan({"c.jsx": js, "p.html": html})
        self.assertEqual(sorted(names), ["c.jsx", "p.html"])
        by = {(x.file, x.rule) for x in f}
        self.assertIn(("c.jsx", "touch-target"), by)
        self.assertIn(("c.jsx", "shape-radius"), by)
        self.assertIn(("c.jsx", "spacing-grid"), by)
        self.assertIn(("p.html", "type-size"), by)

    def test_theme_builder_exports(self):
        xml = ('<resources><color name="md_theme_light_primary">#0061A4</color>'
               '<color name="md_theme_light_onPrimary">#FFFFFF</color>'
               '<color name="md_theme_dark_primary">#D0BCFF</color>'
               '<color name="md_theme_dark_onPrimary">#E8DEF8</color></resources>')
        kt = "val md_theme_light_inverseOnSurface = Color(0xFFF5EFF7)\nval md_theme_light_bogus = Color(0xFF000000)"
        dart = ("static const darkColorScheme = ColorScheme(brightness: Brightness.dark, error: Color(0xFFF2B8B5), "
                "onError: Color(0xFF601410), onInverseSurface: Color(0xFF322F35));")
        f, cov, names = scan({"colors.xml": xml, "Color.kt": kt, "schemes.dart": dart})
        self.assertEqual(sorted(names), ["Color.kt", "colors.xml", "schemes.dart"])
        self.assertEqual([x.msg.endswith("[dark]") for x in f if x.rule == "role-pair-contrast"], [True])
        self.assertNotIn("token-unknown", rules(f))  # `bogus` is not a role: ignored, not reported
        st = {r["id"]: r["status"] for r in cov}
        self.assertEqual(st["color.role.primary"], "name")  # defined, with another value than the baseline
        self.assertEqual(st["color.role.error"], "name")
        self.assertEqual(st["color.role.inverse-on-surface"], "exact")  # both values are the baseline ones

    def test_stats_are_reported(self):
        out = audit.report([], [], ["a.css"], "text", 5, {"declarations": 3, "not_evaluated": {"calc/min/max/clamp/env": 1}})
        self.assertIn("Not evaluated: 1 check(s) over 3 declaration(s) (calc/min/max/clamp/env: 1)", out)


class Cli(unittest.TestCase):
    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "a.css"), "w").write("p{color:#777;background:#888}")
            self.assertEqual(audit.main([d, "--no-coverage", "--out", os.path.join(d, "r.txt")]), 1)
            self.assertEqual(audit.main([d, "--no-coverage", "--fail-on", "never", "--out", os.path.join(d, "r.txt")]), 0)


if __name__ == "__main__":
    unittest.main()
