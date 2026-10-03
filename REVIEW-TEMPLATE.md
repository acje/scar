# SCAR task and review template

Use a compact scratchpad record, typically Beads, for a task and its coherent
candidate. Expand detail with risk; straightforward failures need a compact
disposition, not separate mandatory documents. This template is not enforcement.
Exactly one active task at any time.

## Frame and understand

| Field | Content |
|---|---|
| Intent | Objective, audience, consequence, scope and protected obligations |
| Criteria | Required aspect criteria, applicability and criteria revision |
| Environment | Repository, exact main HEAD, main history and scratchpad references |
| Candidate | Exact base commit, scoped changes and exact content identity; preserve unrelated edits |
| Roles | Drafter, reviewer, finding decision-maker and designated acceptance authority; overlaps and limits |
| Evidence | Exact target/context, source/check references, uncertainties and reuse rationale |
| Task status | Frame and understand; Coherent increment; Check and assess; Resolve findings and refine; Accept and advance main; Record outcome and select next task |
| Credits | Initial/remaining work and protected return reserve; bounded scopes and heterogeneous prices; precharge history shared across attempts/participants; no refunds/reset |
| Return bound | Reserve-priced minimal outcome, main/candidate reconciliation from existing records, findings/evidence/accounting and upward return; no substantive work |

## Coherent increment and assessment

Interleave useful checks while building. Review a coherent candidate substantively,
not every edit. Adaptive understand/change/verify is the default on collisions,
especially high churn. Scale review strength to risk rather than compulsory recursion.

| Aspect | Task-specific criterion, result and evidence |
|---|---|
| Strategic significance | Consequential value and priority rationale |
| Correctness | Checks and invariants |
| Accuracy | Claim support and uncertainty |
| Structure and counterexamples | Dependencies, exceptions and alternative readings |
| Economy | Redundancy removable without lost obligations |
| Ratchet integrity | Protected obligations and authority preserved |
| Structured environment | Main/candidate/scratchpad identity and recoverability |

For each aspect record `Satisfied | Violated | Unknown`, evidence locator,
scope and applicable counterexample; justify omissions or reuse. Unavailable
checks and missing evidence are Unknown, not violations or satisfaction.
Any required Unknown blocks acceptance. Investigate unknowns when useful;
explicitly excluded claims cannot be presented as established.

Bind each conclusion compactly: claim/criterion → exact target/base and
criteria/context identity → witness locator and result → witness-to-conclusion reasoning
→ uncertainty and applicability. A locator without derivation is not a justified
conclusion. Corrected reviews refresh affected derivations even when the candidate
is unchanged; reuse needs exact unchanged content/context and a reason.

## Resolve findings and refine

| Field | Content per finding |
|---|---|
| Target | Stable ID, exact candidate or review content identity and location |
| Allegation | Claimed defect, criterion, consequence and priority |
| Support | Evidence, counterexample and disputed interpretation |
| Decision | `Supported \| Unsupported \| Unresolved` |
| Decision-maker | Name and evidence-based rationale |
| Disposition | Supported repair and new revision; unsupported allegation rejected; unresolved issue and effect |
| Refresh | Affected checks/conclusions invalidated; fresh results; justified reuse on unchanged content/context |

Repair only supported changes. A review allegation never automatically edits the
candidate. Targeted review-of-review needs concrete doubt: unsupported evidence,
contradictions, threatened obligations, disputed interpretation or consequential
coverage gaps. Name that doubt and inspect the relevant claim, not an obligatory
review chain. Correcting a review may leave the candidate unchanged but still
requires refreshed affected conclusions. Continue building or revisit understanding
if assumptions break; otherwise finish unresolved/rejected or proceed to acceptance.

## Accept, advance and record

- Readiness within position 4: one compact record names exact candidate/base,
  current required evidence/conclusions, resolved required findings, remaining
  credit for the bounded acceptance attempt and any blockers; no extra position.
- Eligibility: exact candidate/base, current applicable evidence, required criteria,
  supported repairs and resolved required findings; compare protected obligations.
- Authorization: designated authority, exact candidate content identity, expected
  exact main baseline, criteria and evidence context, decision and limitations.
  The drafter cannot self-authorize; name applicable standing authorization.
- Advance: recheck baseline/content/authority; only an authorized verified commit
  on main advances state. Confirm the main commit matches the candidate. Do not
  include unrelated edits or claim acceptance from a scratchpad entry.
- Outcome: `Accepted | Rejected | Unresolved`, resulting exact main HEAD, candidate
  disposition, findings, uncertainties and evidence references. When edits alone
  are authorized, record verified uncommitted work awaiting authority, not Accepted.
- Resume: reconcile exact main, candidate and scratchpad; justify evidence reuse
  or refresh; append corrections rather than rewrite history. Select the next
  task only after recording this task's outcome.
- Credit stop: at/crossing 80% of initial work, signal prepare-to-return with a
  justified bounded closure plan. If the next operation is unaffordable, halt
  new substantive work; required gaps remain Unknown, never credit-based acceptance.
  Use only the protected reserve for its declared report from existing records.
- Continuation: position/outcome, stop reason, exact main/candidate identities,
  evidence/uncertainty/findings, initial/spent/remaining work and reserve, next
  affordable action and conditions/authority to resume. Preserve charges after
  interruption; no retry/review/session reset. Actual interrupted commits need
  reconciliation, not an assumed unchanged main.
- Material BackBrief, when warranted: trigger, scope, cited observation,
  intent_relevance, local_action, requested_response and confidence. Commander
  decides scope/allowance changes; routine planned return uses the outcome record.

See [algorithm](ALGORITHM.html) and [paper scenarios](SCENARIOS.md).
