# 03 — Seven review aspects

Status: existing SCAR mechanism; distinct questions, not a calibrated score.

## Mechanism

| Aspect | Question |
|---|---|
| Strategic significance | Does the work serve consequential scoped intent? |
| Correctness | Do declared invariants, structure and checks hold? |
| Accuracy | Do actual sources support the claims? |
| Structure and counterexamples | Are dependencies, exceptions and falsifiers represented? |
| Economy | Can redundancy go without losing obligations? |
| Ratchet integrity | Are protection, adjudication and authority preserved? |
| Structured environment | Are identities, evidence and resume state recoverable? |

Assess all seven for applicability. For each applicable aspect record a concrete
criterion, scope, counterexample and Satisfied, Violated or Unknown conclusion.
Justify omissions. For review targets, assess the review's claims and coverage,
not automatically the candidate it criticizes.

## Example

A link checker errors. That is Unknown for the required link criterion, not proof
that links work or that they are broken. Obtain evidence or exclude the claim through
applicable authority; a required Unknown blocks acceptance.

## Limits

Seven labels are not seven independent measurements. No averaging can hide a
required failure. Repeated review cannot manufacture missing source evidence.

## Sources and provenance

- [SCAR aspects](../ALGORITHM.html#aspects) and [core techniques](../skills/core/SKILL.md),
  complete local reads on 2026-10-04; `gacr-cvo`, `gacr-2lk`.
- These questions are SCAR author adaptations, not externally proven dimensions.
