# 14 — Subject and concern technique families

Status: existing SCAR catalogue techniques; scoped inspection, not certification.

## Audience, usability and accessibility

Walk a named audience task; inspect language, visible cues, error prevention,
relationships, meaningful sequence and non-color equivalents. Separate heuristic
inspection from observed participant/keyboard/assistive-technology tests.
Nielsen heuristics are rules of thumb; adopted WCAG requirements need explicit scope.

## Security and threat modeling

Name assets, actors, flows and trust crossings; construct misuse paths, choose a
scope-fit technique, trace mitigations and residual risk to their decision owner.
Protocol acceptance controls alone do not establish implemented security.

## Maintainability and guard proof

Trace callers, callees, types and synchronized representations through a plausible
next change. Avoid speculative abstraction. Separate tidying from behavior changes.
For edited guards: plant a real violation, observe failure, revert, observe clean.
The separation and four-step proof are SCAR author adaptations.

## Rust legal construction and unsafe contracts

Inventory fields/literals, constructors, defaults, conversions, deserialization and
mutation, including defining-module routes. Prefer legal domain alternatives without
inventing constraints on genuine optionality or independent booleans. Seek safe-client
routes that violate unsafe contracts; compiler success alone is not soundness proof.
Async/resource claims require actual budgets, ownership and shutdown evidence.

## PowerPoint delivery

Check slide meaning, unique titles, reading order, reviewed alt text and non-color
cues; run adopted native/access tests and inspect the final export separately.
Product/platform identity matters. Font advice is not a universal threshold.

## HTML rendering

Inspect semantics and adopted criterion witnesses, then exercise required navigation,
keyboard, assistive technology, reflow and output paths in named environments.
Static link/HTML parsing is not browser behavior or accessibility certification.

## Diagram semantic equivalence

Compare nodes, edges, labels, conditions and deliberate omissions to the governing
source; try misleading readings. Provide essential accessible relationships and
check delivered clipping/legibility where required. Supplementary figures do not
replace normative text; aria-describedby can flatten necessary structure.

## Example and limits

A presentation diagram composes diagrams + PowerPoint + audience with core.
Its correct arrows do not prove accessible export. Unknown required delivery evidence
remains Unknown. None of these families is an unused candidate for entries 15–19.

## Sources and provenance

All eight [skill bodies](../skills/README.md) read locally 2026-10-04.
The [2026-10-03 audit N1–N8](../SOURCE-AUDIT.md) records bounded historical sources:

- https://www.nngroup.com/articles/ten-usability-heuristics/ — selected heuristics
  freshly read by research on 2026-10-04.
- https://www.w3.org/WAI/tutorials/images/complex/ — selected sections freshly read
  on 2026-10-04; informative, no rendering/AT test.
- https://google.github.io/eng-practices/review/reviewer/looking-for.html — selected
  sections freshly read on 2026-10-04; caller Rust style still governs.
- https://www.w3.org/TR/2024/REC-WCAG22-20241212/ — historical selected criteria only.
- https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html —
  historical local audit only; current fetch truncated before substantive body.
- https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html and
  https://doc.rust-lang.org/nomicon/safe-unsafe-meaning.html — historical audit only.
- https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25
  — historical audit only; no deck tested.

External sources were read by the recorded research/audit, not freshly fetched by
this drafting turn. `gacr-cvo` distinguishes successful reads, truncation and gaps.
