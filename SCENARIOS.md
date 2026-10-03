# Worked SCAR paper scenarios

These are illustrative paper walkthroughs, not executed software tests or
operational enforcement proofs. `B0`, `B1` and `BX` denote imagined exact main
commits; `C1` and `C2` denote exact candidate content based on a named commit.
Review references denote scratchpad evidence, not code storage or acceptance.
Use the [algorithm](ALGORITHM.html) and [template](REVIEW-TEMPLATE.md).

## Worked targeted review of a review

Intent: clarify exception handling without removing a required safety hold.
Main `B0` contains the hold; candidate `C1@B0` preserves it. The coherent
candidate assessment covers Strategic significance, Correctness, Accuracy,
Structure and counterexamples, Economy, Ratchet integrity and Structured environment.
The reviewer alleges F1: “The hold is redundant; remove it for economy”.
This is concrete doubt: deletion threatens a protected obligation and lacks
support. A targeted review-of-review checks F1 against the hold criterion and
exception witness; no further review is required merely to certify that review.

The decision-maker records F1 `Unsupported` and the correction to the review
`Supported`. Retract F1 with its rationale; `C1` remains unchanged. Refresh
affected review conclusions and justify reuse of unchanged candidate checks.
Economy cannot override the protected hold. The structured environment records
the exact base, candidate and evidence references; ratchet integrity keeps the
authority decision separate. Designated authority may now consider the exact
candidate and baseline, but the review correction itself does not accept it.

## Scenario matrix

Numbers refer to the six [lifecycle positions](ALGORITHM.html#lifecycle).
Exactly one active task at any time, including during renewed understanding.

| ID | Inputs and progression | Expected disposition / main effect | Counterexample caught |
|---|---|---|---|
| P1 Unsupported criticism | `C1@B0`; targeted assessment of disputed allegation at 4 finds no evidence | `Unsupported`; no candidate edit; required coverage still needed before 5 | Criticism is not an automatic editor |
| P2 Stale amendment approval | Supported change creates `C2@B0` (4→2→3) | Refresh affected evidence; C1 authorization cannot accept C2; B0 unchanged | Approval binds exact content |
| P3 Stale prune approval | Supported simplification mistakenly removes mandated evidence; recheck exposes it | Adjudicate loss, repair or finish `Rejected`; B0 unchanged | Pruning is an edit, not proof of economy |
| P4 Broken assumption | Checks show the original dependency model is wrong (3→4→1) | Reframe within intent or record `Unresolved`; never silently weaken criteria | Adaptive progression revisits understanding |
| P5 Unavailable evidence | Required source/check unavailable; Unknown at 3 | Investigate if useful; required Unknown blocks acceptance; finish `Unresolved` if unresolved | Probe error is not a negative verdict |
| P6 Seed without acceptance evidence | B0 has legacy content but no evidence for the required quality criterion | Main is current authoritative state, not automatic quality proof; candidate must establish criteria | Git storage does not confer quality |
| P7 Authorized advance | C2@B0 meets criteria with current evidence; designated authority authorizes exact C2/context/B0 at 5 | Commit on main and confirm B1 matches C2; only then `Accepted`; scratchpad records B1 at 6 | Both authority and exact commit confirmation required |
| P8 Baseline moved | P7 review holds, but main is now BX | Do not overwrite BX; reconcile/rebase candidate, reassess applicability and obtain current authorization | Authorization binds expected baseline |
| P9 High churn | Several edits form one coherent increment; interleaved checks, then substantive assessment (2→3→4) | Repair supported findings via 4→2; no mandatory review after every edit | Process proportion follows risk/coherence |
| P10 Consequential review gap | Review ignores a protected exception; concrete doubt at 4 | Targeted review-of-review and evidence-based disposition, not automatic repeated clean passes | Risk strengthens review without compulsory recursion |
| P11 Unsupported check | Structural checker alleges a violation; decision-maker disproves it at 4 | Record compact disposition, complete missing assessment; only then eligibility at 5 | Rejecting a check is not acceptance |
| P12 Resume and limited authority | Scratchpad says accepted, but candidate is still uncommitted and mission permits edits only | Reconcile main/candidate/scratchpad; report verified uncommitted work awaiting authority; B0 unchanged | Memory corroborates, never authorizes |

## Recoverability and evidence boundary

On resume, identify exact main, candidate base/content and scratchpad task status;
preserve unrelated edits. Reuse only evidence still applicable to exact content,
criteria and context. A stale scratchpad status cannot substitute for an actual
main commit. If a prior accepted result proves wrong, start a corrective task
and append a new authorized correction on main; do not erase history.

These examples test reasoning on paper. Repository checker results establish
only its documented textual/structural checks; substantive judgement and
designated commit authority remain separate. This mission performs no commits,
staging, amendments, pushes or PR operations.
