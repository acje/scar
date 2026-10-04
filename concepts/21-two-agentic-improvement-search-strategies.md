# 21 — Two agentic improvement-search strategies

Status: requested comparison/synthesis, not adoption or another designated addition.
AI proposals generate candidates; evaluation and protected obligations decide usability.

## Strategy 1: evaluator-gated single-incumbent search

1. Define the task, candidate boundary, incumbent, objective and required constraints.
2. Evaluate the baseline under fixed, recorded conditions.
3. Have the agent propose one bounded change and run the same evaluator.
4. Keep an admissible improvement; otherwise restore/preserve the incumbent.
5. Log identities, outcomes, uncertainty and spending; repeat only within allocation.

[Autoresearch](20-autoresearch.md) is the concrete observed exemplar; its source-specific
branch/reset instructions are not imported SCAR authority. Strict hill climbing means
strictly improving accepted moves under a fixed objective and neighborhood.
Broad LLM mutations or equal-quality simplification exceed that strict definition.

## Strategy 2: reflective population/Pareto evolutionary search

1. Start with evaluated candidates and a bounded retained pool.
2. Select a frontier candidate; execute a minibatch and collect diagnostics/traces.
3. Reflect on those traces to propose a mutation.
4. Evaluate the proposal and update complementary task-subset candidates/frontier.
5. Optionally merge complementary candidates; stop at the evaluation allocation.

[GEPA](17-reflective-pareto-evolutionary-search-gepa.md) owns the canonical account.
This is broader evolutionary search, not strict single-incumbent hill climbing;
exact implementation selection/merge rules are outside the source-read scope.

## Tradeoffs

| Dimension | Single incumbent | Reflective pool/frontier |
|---|---|---|
| State/accounting | Smaller, easy keep/discard trail | More candidates and evaluation accounting |
| Search information | One incumbent and evaluator feedback | Traces plus complementary task-subset strengths |
| Failure mode | Local trapping, noisy wins, lost alternatives | Pool cost, overfitting, misleading frontier criteria |
| Useful setting | Cheap bounded incremental trials | Task diversity and informative diagnostics |

Neither strategy guarantees improvement, safety, generalization or convergence.
Both need explicitly bounded evaluations, storage and retained work before adoption.

## Evaluator safeguards

- Freeze and identify evaluator, data, candidate scope and required constraints;
  proposals cannot improve scores by weakening the harness or protected obligations.
- Match task/context/model/hardware/time accounting; record failures and uncertainty,
  not only winners. Distinguish preservation from intended improvement.
- Use task-appropriate randomization/replication (entry 18), not an invented sample quota.
- Limit adaptive feedback reuse and arrange independently assessed final evidence
  where required (entry 19). Reused validation is not an untouched final test.
- LLM self-feedback is search information, not independent correctness evidence.
  Required failures/Unknowns cannot be averaged away or authorized by an optimizer.

## Sources and provenance

- Entry 20's four autoresearch mutable master sources; entry 17's GEPA README and
  author abstract: research reads 2026-10-04, not executed or independently replicated.
- https://arxiv.org/abs/2303.17651 — Self-Refine author abstract v2 (2023-05-25),
  read by research 2026-10-04; same-LLM feedback/refinement across reported tasks
  is task-specific author evidence, not calibration.
- Entries 18/19 identify NIST and adaptive-analysis read limits; `gacr-cvo` S1/S2.
- [SCAR comparison](../ALGORITHM.html#comparison), [improvement proposal](../proposals.md),
  locally read 2026-10-04. This synthesis introduces no runtime mechanism.
