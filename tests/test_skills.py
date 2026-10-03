import importlib.util
from pathlib import Path
import tempfile
import unittest
import shutil


SPEC = importlib.util.spec_from_file_location(
    "check_skills", Path(__file__).resolve().parents[1] / "scripts/check_skills.py"
)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class CatalogueTests(unittest.TestCase):
    def test_missing_catalogue_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(CHECKER.validate(Path(directory)), "Missing eight-skill catalogue must be rejected")

    def test_real_catalogue_is_clean(self):
        self.assertEqual([], CHECKER.validate(Path(__file__).resolve().parents[1]))

    def test_corrupted_catalogue_is_rejected(self):
        original = Path(__file__).resolve().parents[1]
        mutations = (
            ("skills/core/SKILL.md", "name: scar-core", "name: wrong"),
            ("skills/core/SKILL.md", "## Techniques", "## Other"),
            ("skills/core/SKILL.md", "../../ALGORITHM.html#aspects", "../../ALGORITHM.html#missing"),
            ("skills/core/SKILL.md", "../../SOURCE-AUDIT.md", "../../missing.md"),
            ("skills/core/SKILL.md", "../../SOURCE-AUDIT.md", "../../../outside.md"),
        )
        for relative, before, after in mutations:
            with self.subTest(mutation=after), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                shutil.copytree(original / "skills", root / "skills")
                for name in ("README.md", "REVIEW-TEMPLATE.md", "SOURCES.md", "SOURCE-AUDIT.md", "ALGORITHM.html"):
                    shutil.copy2(original / name, root / name)
                path = root / relative
                path.write_text(path.read_text().replace(before, after), encoding="utf-8")
                self.assertTrue(CHECKER.validate(root))

    def test_extra_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            extra = root / "skills" / "extra"
            extra.mkdir(parents=True)
            (extra / "SKILL.md").write_text("extra", encoding="utf-8")
            self.assertIn("Catalogue must contain exactly the eight declared SKILL.md paths", CHECKER.validate(root))


if __name__ == "__main__":
    unittest.main()
