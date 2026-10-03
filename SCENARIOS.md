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
| P13 First acceptance | B0 has no past quality proof; C1@B0 establishes every required criterion and compatible protected obligations, with current conclusions and resolved findings at 4 | With affordable precharged acceptance and designated exact authority at 5, confirm B1 matches C1 before Accepted at 6; missing comparison/evidence leaves Unresolved | Syntax and legacy storage are not first-acceptance evidence |

## Heterogeneous credits: bounded paper trace

Illustrative only, not defaults or measured costs: initial work W=20, protected
return R=4. Bounded scopes/prices declared before work: framing/evidence inspection
of one named exception=2; edit one exception paragraph=5; targeted review of its
hold claim=3; one named check invocation=2; adjudicate one finding=1; exact
authorized acceptance attempt with commit confirmation=3. Review descendants
use the same bounded review price; extra scope requires a new precharge.
R covers identity reconciliation from recorded snapshots=1 and minimal outcome,
findings/evidence/accounting/continuation report plus upward return=3. Neither
return operation acquires evidence or settles findings.

| Operation, charged before attempt | Work spent / remaining | Evidence and decision |
|---|---|---|
| Inspection 2, edit 5, review 3, check 2, adjudication 1 | 13 / 7 | C1@B0; supported correction identified, old conclusion names claim/hold criterion, C1/B0/context, exception witness and why deletion violates the hold |
| Proposed repair 5 | Before: 13 / 7; after: 18 / 2 | Prospective 18/20 crosses 80%; signal prepare-to-return before admission, justify this bounded repair, invalidate affected C1 conclusions; C2 remains uncommitted |
| Recheck 2 | 20 / 0 | New C2 check result recorded; required refreshed substantive assessment remains Unknown |
| Proposed review 3 or acceptance 3 | Not admitted: 20 / 0 | No substantive work; neither a passing check nor reserve substitutes for assessment or exact authority |
| Return reconciliation 1, report/upward return 3 | Work 20 / 0; return 4 / 0 | Unresolved, reason work exhausted; B0 unchanged, exact C2@B0 retained, gaps/evidence/charges and resume conditions returned |

At exactly 16/20 consumed the same signal applies. A proposed charge taking
15 to 16 also signals before admission. With W remaining 2, a cost-3 operation
is already unaffordable even before zero: stop and report, do not borrow R.
If the cost-5 repair is interrupted at 18/20, it stays charged; a retry costs
another 5 and cannot start with 2. Resume reconciles actual candidate/main and
the same W/R history; it does not manufacture a fresh 20. If an admitted
acceptance attempt was interrupted, report actual main as known or Unknown and
reconcile before any Accepted claim; never assert B0 unchanged without evidence.

The worked review above also needs precharges: correcting its review does not
refund the initial review, and a justified descendant plus revalidation costs
again. Its new conclusion records the unchanged C1/B0/context, hold witness and
reason F1 is unsupported; affected review conclusions refresh, rather than a
blanket reuse claim. The seven aspects still receive applicability decisions.

## Proportional risk and mission command examples

A reversible typo correction may justify omitted substantive source assessment
with an exact scope/reason and applicable checks. A protected hold deletion has
consequential risk: inspect the exception witness and targeted disputed review;
neither convenience nor low remaining credit waives required evidence.

An affordable repair within intent stays local. Discovering that intent requires
removing the protected hold is material: report trigger=Surprise,
scope=PackageLevel, observation=F1/hold witness, intent_relevance=required hold
conflicts with proposed deletion, local_action=paused deletion/preserved C1,
requested_response=AdjustIntent, confidence=high. Only the commander decides;
the payload itself grants no deletion or credit authority. Ordinary threshold
return instead records the bounded outcome above without inventing Surprise.

If new defect classes persist beyond three rounds, or defensive scaffolding
exceeds twice core logic, pause; already round three with accumulating layers
calls for a halt. Record the friction, remaining credits and a material
BackBrief; commander obtains orientation before operator choices. Investigation
must be affordable/precharged or deferred in the return report. Two repeat
rejections on one class is a different stop cue, not three rounds of novelty.
These examples apply fleet judgement doctrine, not measured universal limits.

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
