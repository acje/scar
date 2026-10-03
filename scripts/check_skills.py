from pathlib import Path
import re


SKILLS = (
    "core", "audience", "security", "maintainability",
    "rust", "powerpoint", "html", "diagrams",
)
SECTIONS = ("Applicability", "Techniques", "Evidence and output", "Limitations", "Sources")


def validate(root):
    errors = []
    expected = {root / "skills" / name / "SKILL.md" for name in SKILLS}
    actual = set((root / "skills").glob("**/SKILL.md"))
    if actual != expected:
        errors.append("Catalogue must contain exactly the eight declared SKILL.md paths")
    documents = [root / name for name in (
        "README.md", "REVIEW-TEMPLATE.md", "SOURCES.md", "SOURCE-AUDIT.md", "skills/README.md",
    )] + sorted(expected)
    for path in documents:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"Cannot inspect {path.relative_to(root)}: {error}")
            continue
        if path in expected:
            name = path.parent.name
            if not re.match(rf"\A---\nname: scar-{name}\ndescription: [^\n]+\n---\n", text):
                errors.append(f"Invalid name/description frontmatter: {name}")
            for section in SECTIONS:
                if not re.search(rf"^## {section}\n\S", text, re.MULTILINE):
                    errors.append(f"Missing or empty {section}: {name}")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            if target.startswith("https://"):
                continue
            file_part, _, fragment = target.partition("#")
            destination = (path.parent / file_part).resolve() if file_part else path.resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f"Link escapes repository: {target}")
            elif not destination.is_file():
                errors.append(f"Missing local link: {path.relative_to(root)} -> {target}")
            elif fragment and destination.suffix == ".html":
                if f'id="{fragment}"' not in destination.read_text(encoding="utf-8"):
                    errors.append(f"Missing HTML anchor: {target}")
    return errors


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(error)
    if not errors:
        print("OK: eight skill paths, frontmatter, sections and local Markdown links; substantive quality/runtime loading unverified")
    raise SystemExit(bool(errors))
