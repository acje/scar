# 17 — Reflective Pareto evolutionary search / GEPA

Additional idea 3 of 5. Status: external candidate mechanism, not adopted SCAR policy.
This is the canonical GEPA account; entry 21 compares it with single-incumbent search.

## Mechanism

GEPA combines language-model reflection on execution traces with candidate search.
At the level supported by the project README and author abstract:

1. Select a candidate from the retained pool/frontier.
2. Execute a minibatch and collect traces and evaluation feedback.
3. Reflect on diagnostics and propose a prompt mutation.
4. Evaluate the proposal and update retained candidates/frontier where appropriate.
5. Optionally merge complementary candidates; continue within metric-call allocation.

Candidates can be complementary on different task subsets. Retaining that frontier
is broader evolutionary search, not strict single-incumbent hill climbing.
This summary does not specify unread implementation selection/merge semantics.

## SCAR relationship and example

SCAR has evidence and refinement, but no named optimizer population, task-subset
Pareto frontier or merge was observed in the surveyed protocol/template/catalogue/
proposals/eight skills. A hypothetical prompt experiment could retain candidates
strong on distinct tasks while using traces to propose changes. It is not adoption.

## Tradeoffs and evaluator limits

A pool can preserve useful alternatives; trace reflection supplies contextual search
information. More candidates cost evaluation/storage and can overfit reused tasks.
The README quickstart supplies trainset, valset and max_metric_calls. Separate final
assessment and adaptive-evaluation safeguards still need task-specific design.
Protected failures cannot be averaged away by a frontier or aggregate metric.

## Sources and provenance

- https://arxiv.org/abs/2507.19457 — author abstract, v2 revised 2026-02-14.
- https://raw.githubusercontent.com/gepa-ai/gepa/main/README.md — mutable main,
  How It Works and quickstart; both read by research on 2026-10-04 (`gacr-cvo` C3/S2).
- Full paper and implementation not executed/read in full; reported benchmark gains
  are task/model-specific author claims, not independent verification or guarantees.
- [SCAR comparison](../ALGORITHM.html#comparison), read locally 2026-10-04.
