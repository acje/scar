#!/usr/bin/env python3
"""Executable checker regression tests, not execution of the SCAR protocol."""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import verify_docs


class VerifyDocsTests(unittest.TestCase):
    def run_fixture(self, filename=None, old=None, new=""):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in verify_docs.DOCS:
                text = (verify_docs.ROOT / name).read_text()
                if name == filename:
                    self.assertIn(old, text, "mutation target must exist")
                    text = text.replace(old, new, 1)
                (root / name).write_text(text)
            output = io.StringIO()
            with patch.object(verify_docs, "ROOT", root), contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                result = verify_docs.verify()
            return result, output.getvalue()

    def assert_rejected(self, filename, old, new, diagnostic):
        result, output = self.run_fixture(filename, old, new)
        self.assertEqual(result, 1, output)
        self.assertIn(diagnostic, output)
        clean_result, clean_output = self.run_fixture()
        self.assertEqual(clean_result, 0, clean_output)

    def test_clean_documents(self):
        result, output = self.run_fixture()
        self.assertEqual(result, 0, output)
        self.assertIn("LIMIT: textual/structural checks only", output)

    def test_no_extra_lifecycle_position(self):
        self.assert_rejected("ALGORITHM.html", "</ol>", '<li id="step-7">Extra</li></ol>', "lifecycle IDs mismatch")

    def test_no_extra_diagram_position(self):
        self.assert_rejected("ALGORITHM.html", "</svg>", '<g id="node-7"></g></svg>', "diagram IDs mismatch")

    def test_credit_obligation_deletions(self):
        for phrase in (
            "initial work allocation", "protected return reserve", "debit before",
            "no refunds or silent reset", "80% of initial work", "cannot fund substantive work",
            "insufficient for the next operation", "no new substantive work",
        ):
            with self.subTest(phrase=phrase):
                self.assert_rejected("ALGORITHM.html", phrase, "REMOVED", f"missing obligation {phrase}")

    def test_conclusion_and_readiness_deletions(self):
        for phrase in ("witness-to-conclusion reasoning", "Readiness within position 4"):
            with self.subTest(phrase=phrase):
                self.assert_rejected("REVIEW-TEMPLATE.md", phrase, "REMOVED", f"missing obligation {phrase}")

    def test_first_acceptance_scenario_required(self):
        self.assert_rejected("SCENARIOS.md", "P13 First acceptance", "REMOVED", "missing obligation P13 First acceptance")

    def test_command_payload_required(self):
        for phrase in ("intent_relevance", "requested_response", "local_action", "confidence"):
            with self.subTest(phrase=phrase):
                self.assert_rejected("ALGORITHM.html", phrase, "REMOVED", f"missing obligation {phrase}")

    def test_legacy_terminology_still_rejected(self):
        self.assert_rejected("README.md", "# SCAR", "# 10-state SCAR", "incompatible active terminology")

    def test_broken_local_link(self):
        self.assert_rejected("README.md", "(ALGORITHM.html)", "(MISSING.html)", "broken link")

    def test_required_unknown_guard(self):
        self.assert_rejected("ALGORITHM.html", "required Unknown blocks acceptance", "required Unknown permits acceptance", "missing obligation required Unknown blocks acceptance")

    def test_exact_authority_guard(self):
        self.assert_rejected("ALGORITHM.html", "confirm the main commit matches", "skip confirmation of", "missing obligation confirm the main commit matches")

    def test_transition_corruption(self):
        self.assert_rejected("ALGORITHM.html", 'data-from="4" data-to="5"', 'data-from="3" data-to="5"', "SVG edges mismatch")


if __name__ == "__main__":
    unittest.main()
