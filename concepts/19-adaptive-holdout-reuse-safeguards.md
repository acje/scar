# 19 — Adaptive holdout reuse safeguards

Additional idea 5 of 5. Status: external candidate mechanism, not adopted SCAR policy.

## Mechanism

Repeatedly adapting proposals to holdout feedback can overfit the holdout itself.
A dataset called validation is not automatically independent of the search choices
it has influenced. The cited author abstract presents protected adaptive reuse with
differential-privacy and description-length approaches.

## SCAR relationship

SCAR freshness checks bind evidence to exact content/context; they do not by themselves
protect statistical generalization across adaptive trials. No named adaptive-holdout
protection was observed in surveyed protocol/template/catalogue/proposals/eight skills.
Absence is scoped, not an exhaustive historical search or an adoption decision.

## Example

An agent iterates prompts after seeing validation failures. Eventually that set has
influenced the prompt. Reserve an independent final assessment under an explicit
disclosure policy; if using specialized protected reuse, obtain its actual assumptions
and implementation rather than borrowing a paper's guarantee from its abstract.

## Tradeoffs and limits

Withholding feedback can reduce search information; protected reuse can introduce
noise and accounting complexity. The appropriate evaluation design depends on the
task and budget. No privacy parameter, reusable-holdout algorithm or generalization
guarantee is transferred to SCAR here. Repeated clean review is not statistical protection.

## Sources and provenance

- https://arxiv.org/abs/1506.02629 — author abstract, v2 (2015-09-25),
  read by research 2026-10-04; full paper/guarantee conditions unread (`gacr-cvo` C5).
- [SCAR derivation](../ALGORITHM.html#derivation), read locally 2026-10-04.
