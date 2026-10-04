# 15 — Bayesian optimization

Additional idea 1 of 5. Status: external candidate mechanism, not adopted SCAR policy.

## Mechanism

Use previous expensive trials to update a probabilistic surrogate of performance;
use the model/posterior to guide which trial to spend evaluation budget on next.
The cited author abstract describes Gaussian-process modeling of generalization
performance, sensitivity to prior/inference choices, and duration/parallelism concerns.

## SCAR relationship

SCAR already bounds work and prioritizes evidence, but no named surrogate/posterior
trial-allocation mechanism was observed in the surveyed protocol, template,
catalogue, proposals or eight skill bodies. This is scoped absence, not proof about
all historical conversations or every semantically similar practice.

## Example

A bounded experiment explores prompt settings whose evaluations are expensive.
A surrogate could guide the next setting rather than testing a blind grid.
This is a hypothetical use, not a configured optimizer or measured SCAR improvement.

## Tradeoffs and limits

Potential evaluation efficiency comes with model assumptions, implementation and
surrogate-fit cost. Poor modeling can misallocate trials. Preserve protected criteria
individually; an optimizer objective cannot replace SCAR acceptance authority.
No acquisition formula, implementation detail or universal gain is asserted from
an abstract-only read. Actual budget and evaluation design need a separate decision.

## Sources and provenance

- https://arxiv.org/abs/1206.2944 — author abstract, v2 (2012-08-29),
  read by research 2026-10-04; full paper/math not read (`gacr-cvo` C1).
- [SCAR credits](../ALGORITHM.html#credits); local/skill reads 2026-10-04.
