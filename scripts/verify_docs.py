#!/usr/bin/env python3
"""Read-only SCAR documentation checks; not protocol acceptance or enforcement."""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ("README.md", "ALGORITHM.html", "REVIEW-TEMPLATE.md", "SCENARIOS.md", "SOURCES.md")
ASPECTS = (
    "Strategic significance", "Correctness", "Accuracy", "Structure and counterexamples",
    "Economy", "Ratchet integrity", "Structured environment",
)
STEPS = (
    "Frame and understand", "Coherent increment", "Check and assess",
    "Resolve findings and refine", "Accept and advance main", "Record outcome and select next task",
)
EDGES = {("1", "2"), ("2", "3"), ("3", "4"), ("4", "1"), ("4", "2"),
         ("4", "5"), ("4", "6"), ("5", "6"), ("6", "1")}


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.edges = []
        self.rows = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if "href" in a:
            self.links.append(a["href"])
        if "data-from" in a:
            pair = (a["data-from"], a.get("data-to"))
            (self.edges if tag == "path" else self.rows).append(pair)

    def handle_data(self, data):
        self.text.append(data)


def verify():
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    contents = {name: (ROOT / name).read_text() for name in DOCS}
    parsed = Document()
    parsed.feed(contents["ALGORITHM.html"])
    visible = " ".join(parsed.text)
    normalized = {n: re.sub(r"\s+", " ", visible if n.endswith(".html") else t)
                  for n, t in contents.items()}
    forbidden = r"parallel|concurren|mandatory depth|depth[- ]1|six aspects|six-aspect|10-state|W/D/T|accepted pointer|shared ledger|global (?:bounds|budgets)"
    for name, text in contents.items():
        require(not re.search(forbidden, text, re.I), f"{name}: incompatible active terminology")
        for aspect in ASPECTS:
            require(aspect in normalized[name], f"{name}: missing aspect {aspect}")
        links = parsed.links if name.endswith(".html") else re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
        for link in links:
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                continue
            target, _, fragment = link.partition("#")
            path = ROOT / (target or name)
            require(path.is_file(), f"{name}: broken link {link}")
            if fragment and path.is_file():
                if path.suffix == ".html":
                    p = Document()
                    p.feed(path.read_text())
                    require(fragment in p.ids, f"{name}: missing anchor {link}")
                else:
                    require(False, f"{name}: unchecked Markdown anchor {link}")
    require(len(parsed.ids) == len(set(parsed.ids)), "algorithm: duplicate IDs")
    for i, step in enumerate(STEPS, 1):
        require(f"step-{i}" in parsed.ids and f"node-{i}" in parsed.ids,
                f"algorithm: missing lifecycle/diagram state {i}")
        require(step in visible, f"algorithm: missing state label {step}")
    require(set(parsed.edges) == EDGES and len(parsed.edges) == len(EDGES), "algorithm: SVG edges mismatch")
    require(set(parsed.rows) == EDGES and len(parsed.rows) == len(EDGES), "algorithm: transition rows mismatch")
    obligations = {
        "ALGORITHM.html": ("Exactly one active task", "Supported", "Unsupported", "Unresolved", "Unknown",
                           "required Unknown blocks acceptance", "drafter cannot self-authorize",
                           "confirm the main commit matches", "corroborates; it does not confer acceptance",
                           "preserve unrelated edits", "resume", "standing authorization", "concrete doubt"),
        "REVIEW-TEMPLATE.md": ("exact main", "content identity", "Supported", "Unsupported", "Unresolved",
                               "required Unknown blocks acceptance", "reuse", "authority"),
        "SCENARIOS.md": tuple(f"P{i}" for i in range(1, 13)),
        "README.md": ("python3 scripts/verify_docs.py", "Exactly one active task", "high churn"),
        "SOURCES.md": ("gacr-5m7", "author-designed", "not runtime verification"),
    }
    for name, phrases in obligations.items():
        for phrase in phrases:
            require(phrase in normalized[name], f"{name}: missing obligation {phrase}")
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: 5 active documents; local links, seven aspects, six lifecycle states, 9 matching edges, key obligations")
    print("LIMIT: textual/structural checks only; no external-link validation, substantive review, runtime enforcement or acceptance")
    return 0


if __name__ == "__main__":
    sys.exit(verify())
