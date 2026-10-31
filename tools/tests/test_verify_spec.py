"""Every non-token guideline (spec / site / impl) must have evidence, and the evidence must match the crawled site / m3.css.

Run from the repository root:  python -m unittest discover -s tools/tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "material3"))
import verify_spec  # noqa: E402


class SpecEvidence(unittest.TestCase):
    def test_all_evidence_matches(self):
        rows, problems = verify_spec.check()
        self.assertEqual(problems, [])
        self.assertEqual({r[2] for r in rows}, {"ok", "partial", "impl"})

    def test_counts(self):
        rows, _ = verify_spec.check()
        by = {}
        for r in rows:
            by[r[2]] = by.get(r[2], 0) + 1
        self.assertEqual(by, {"ok": 32, "partial": 5, "impl": 2})

    def test_partials_say_what_is_missing(self):
        rows, _ = verify_spec.check()
        for gid, _src, res, gap in rows:
            if res in ("partial", "impl"):
                self.assertTrue(gap, gid)


if __name__ == "__main__":
    unittest.main()
