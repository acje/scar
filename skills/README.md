# Portable two-axis catalogue

SCAR's [protocol](../ALGORITHM.html) governs; skills supply techniques, not new lifecycle positions, universal gates or acceptance authority. These eight plain Markdown files are portable reading units, not installed opencode configuration. No automatic discovery or runtime loader is implemented.

| Axis | Skill | Technique-to-aspect mapping |
|---|---|---|
| Review questions | [Core](core/SKILL.md) | All seven: intent trace, invariant test, citation audit, dependency/falsifier walk, protected deletion, authority trace, identity reconstruction |
| Review concerns | [Audience](audience/SKILL.md) | Task/access walkthrough → correctness, structure, accuracy |
| Review concerns | [Security](security/SKILL.md) | Trust/misuse/control witnesses → correctness, counterexamples, ratchet |
| Review concerns | [Maintainability](maintainability/SKILL.md) | Change propagation/guard bite → economy, structure, correctness, environment |
| Subject | [Rust](rust/SKILL.md) | Construction and unsafe routes → correctness, structure, security, maintenance |
| Subject | [PowerPoint](powerpoint/SKILL.md) | Slide meaning/order/export → accuracy, structure, audience |
| Subject | [HTML pages](html/SKILL.md) | Semantics and exercised delivery → correctness, accuracy, audience |
| Subject | [Diagrams](diagrams/SKILL.md) | Relationship/source/text equivalence → correctness, structure, accuracy, audience |

These axes distinguish what question to ask from what artefact to inspect. They overlap; no mathematical independence, calibrated score, universal thresholds or aspect-by-subject file product is claimed. Additional concerns require explicit applicability, not universal mandatory rows.

## Select, read, bind, assess
At framing, classify subject(s) and select core plus applicable concerns and every relevant subject profile. Before assessment, actually read each selected complete SKILL.md and applicable caller policy. A tool-capable agent may use its supported skill-loading mechanism; otherwise read the files directly. Naming a skill or configuring a path is not evidence of loading.

Record path and exact content identity (for example SHA-256), version/revision if present, loaded-by/read witness, applicability, derived criteria and limitations. Read local binding house style and record exact identity too. Protected SCAR/authority obligations and explicit task constraints remain governing; binding caller policy precedes provisional profile defaults and external advice. Record conflict plus disposition/decision owner; unresolved binding conflicts stop affected assessment rather than silently choosing a default. Revisions to loaded guidance invalidate affected criteria, evidence and authorization under protocol derivation.

Unsupported subjects or unavailable required guidance remain **Unknown**: explicitly identify missing profile/coverage and obtain scoped authorized guidance or exclude the claim through applicable authority. Never silently substitute generic core coverage for missing subject techniques. Loading/checks/review share precharged work; protected return reserve cannot fund loading.

## Selection examples
- Rust API change: core + Rust + maintainability; security if unsafe/trust exposure is relevant. Load actual repository rules, not imagined fleet defaults.
- Static embedded SVG explanation: core + diagrams + HTML + audience when reader access is in scope. Read-level equivalence does not establish browser/AT behavior.
- PowerPoint diagram: core + PowerPoint + diagrams + audience when applicable; inspect delivered export, not just source deck.
- Uncatalogued spreadsheet: core questions still apply, subject guidance is Unknown until scoped guidance is obtained; no silent HTML substitution.
- Ordinary-Git workflow documentation: core + maintainability + HTML/diagrams for the normative page and supplementary SVG; security/audience for authority, scratch secrecy limits and reader misuse. Read the [active workflow](../GIT-WORKFLOW.md) and [scenario eval limits](../SCENARIO-EVALS.md); no runtime enforcement is supplied. Candidate commits alone cannot establish acceptance.

## Local check
Run `git diff --check` from the repository root. Inspect tracked references with `git grep`; manually compare local Markdown/HTML link targets and fragments with tracked files and HTML IDs. Read the eight skill bodies for frontmatter, required sections and source/criterion consistency; record actual coverage and gaps. No packaging checker or test runner is supplied. These inspections do not establish external availability, runtime loading, rendered accessibility or substantive review quality. Source support and gaps are in the [audit](../SOURCE-AUDIT.md).
