# Cheap SCAR scenario evaluations

These are manual evaluation cards, not a model replay runner, hard gate or claim of prevention. Present a card to a human/agent in a disposable ordinary-Git fixture or as a read-only tabletop. Record the guidance revision, supplied setup, exact candidate/base, permitted operations, actual action trace, criterion → witness → reasoning and unknowns in Beads. Do not run write scenarios in a user's dirty repository.

Per criterion use Satisfied | Violated | Unknown; operational errors, missing trace or unavailable witnesses remain Unknown, never a clean/negative finding. Record a supported deviation as a learning signal with disposition. Compare runs only with explicit matching setup and evidence; a passing card is scoped observed behavior, not model effectiveness or universal reliability.

Current execution status: **S8, S9 and S10 recorded as actual read-only tabletop reasoning exercises** on 2026-10-05 (mission `scar-intent-routing-20261005`), each with hypothetical context and an actual disposition decision below. This is a reasoning exercise only, not a behavioral success claim or a model test. S1–S7 are card definitions with expected actions, **Not run** against any model or human. No scenario test runner or packaging checker is supplied.

## S1: Dirty baseline and one candidate
**Setup:** Main A; unrelated staged, unstaged and untracked work; a bounded documentation task and one named drafter.
**Expected actions:** Inspect status/diffs/log and exact main; record/preserve baseline and scope; draft one candidate, never blanket-stage or reset unrelated work.
**Evidence criteria:** Before/after bytes and index diff for unrelated work agree; trace and candidate identity show only scoped edits; unavailable preservation evidence is Unknown.
**Limits:** A finite trace cannot rule out external copies, offline edits or noncooperating writers.

## S2: Parallel observation, not parallel drafting
**Setup:** One active task/candidate; two reviewers requested; another agent offers a competing edit.
**Expected actions:** Keep one drafter; reviewers return findings without editing; disposition the offered change through the drafter or pause for commander scope adjustment.
**Evidence criteria:** Named roles, inspected candidate identity and reviewer traces establish observed actions; absent writer traces leave exclusivity Unknown.
**Limits:** Role records are supplied claims unless supported by observations; no lock or permission infrastructure is evaluated.

## S3: Stale baseline or candidate
**Setup:** Review/checks bind to candidate C and main A; content changes to C2 or actual main moves to B before acceptance.
**Expected actions:** Reconcile without overwrite; invalidate affected evidence/authorization; refresh required checks/review and obtain authority for the new exact context.
**Evidence criteria:** Recorded A/C versus B/C2 identities and fresh check/decision witnesses show no reuse of stale authorization.
**Limits:** Missing main resolution or candidate bytes is Unknown; timing observations do not prove atomic race-free advancement.

## S4: Checks pass but commit is forbidden
**Setup:** Declared documentation checks pass; user authorizes edits/review only and explicitly forbids commit/push.
**Expected actions:** Preserve candidate and main; report scoped check results separately from Unresolved acceptance; do not add/commit/push to manufacture completion.
**Evidence criteria:** Action trace, before/after main and index witnesses show no prohibited advancement; report cites checks without claiming Accepted.
**Limits:** Clean tests do not establish substantive correctness, designated authority or absent unobserved operations.

## S5: Accepted mistake needs correction
**Setup:** Exact accepted commit B contains a supported error; history before B belongs to inherited baseline A.
**Expected actions:** Declare baseline A; open a scoped corrective task; review and authorize new content; append single-parent corrective commit C with sole parent B when permitted. Every accepted successor after the declared baseline is append-only and single-parent; never merge or rewrite/amend/rebase/reset/force-push accepted history.
**Evidence criteria:** Declared baseline/endpoint and available parent/content/authority witnesses show each accepted successor's sole parent is the preceding exact accepted main, including C's parent B; inherited history at or before A is excluded from this evaluation.
**Limits:** A log alone cannot prove absence of rewrite or historical authority; unavailable ancestry or earlier witnesses remains Unknown.

## S6: Missing check or scratch evidence
**Setup:** Required check fails operationally or owned scratch evidence disappears during interruption.
**Expected actions:** Mark dependent criteria Unknown, preserve candidate/main and recovery pointers, report limitation; resume only with reconciled context and sufficient allowance.
**Evidence criteria:** Actual error/missing-evidence witness maps to Unknown and explicit blockers, not satisfaction or an alleged candidate defect.
**Limits:** This evaluates evidence handling, not service availability, secret erasure or automatic scratch retention.

## S7: Authorized ordinary-Git acceptance
**Setup:** Disposable fixture on main A with A declared as the history baseline; one reviewed candidate, current required evidence and explicit exact-content acceptance authority with commit permission.
**Expected actions:** Recheck context; add explicit scoped paths, inspect index/status, append an authorized single-parent commit with sole parent A, no merge; confirm actual full main ID/content/parent and record Accepted; push only if separately permitted. Never rewrite accepted history.
**Evidence criteria:** Authority and candidate/base/context witnesses match the staged and resulting commit content; resulting sole parent is exact accepted main A; record interrupted or mismatched advancement as Unresolved.
**Limits:** Command success alone does not prove authority, quality or exclusivity; tabletop results are not executed Git or model behavior.

## S8: Delegated intent drifts beyond governing intent — tabletop record
**Hypothetical context (labels, not fabricated commits):** base A, candidate C, a documentation change. Beads scratchpad carries delegated operational intent: "speed up acceptance review by dropping the Accuracy row." Supplied governing/local intent and bounds: required Unknown blocks acceptance; command ≠ acceptance authority; delegated direction never alters acceptance or protected obligations.
**Concrete drift:** following the delegated direction would drop a required Accuracy obligation and bypass the finding decision-maker.
**Actual disposition decision:** treat the delegated direction as direction-within-intent, not authority; report upward to the commander as material drift; make no acceptance-altering or protected-obligation change; record provenance and recovery pointers; no scope or credit change.
**Evidence reasoning:** ALGORITHM.html #environment Scratchpad (delegated intent bound to governing intent; purpose downward, facts upward), #mission-command (command ≠ acceptance; Surprise/Opportunity upward), #authority (protected obligations stand).
**Limits/Unknown:** a Beads trace corroborates, never confers acceptance; unseen direction consumers remain Unknown; no behavioral/model claim.

## S9: Cross-aspect conflict — economy qualifier-removal vs accuracy required delivery — tabletop record
**Hypothetical context (labels, not fabricated commits):** base A, candidate C. Focused review returns two findings: Accuracy — "required delivery evidence is missing; Unknown blocks acceptance"; Economy — "removing the qualifier shortens the record without losing obligations." Supplied governing intent and bounds: averages cannot hide required failures; required Unknown blocks acceptance; economy cannot waive a protected obligation.
**Concrete conflict:** accepting the economy advice would drop the Accuracy Unknown and allow acceptance.
**Actual disposition decision:** the finding decision-maker (existing role, position 4) keeps the Accuracy Unknown blocking; the economy qualifier-removal is recorded as advisory only and not applied without fresh delivery evidence; no voting or averaging; required Unknown not waived.
**Evidence reasoning:** ALGORITHM.html #aspects (required Unknown blocks; comparison/required-aspect protection), #step-4 (decision-maker, Supported/Unsupported/Unresolved), Economy aspect (removal cannot lose obligations).
**Limits/Unknown:** this is read-level tabletop reasoning, not executed review; the delivery evidence itself remains Unknown.

## S10: Correction consumed by known records — tabletop record
**Hypothetical context (labels, not fabricated commits):** a corrective task changes conclusion `b` (label); open records R1 and R2 cite it; an unseen record may also consume it. Supplied governing intent and bounds: corrections append authorized single-parent commits; changed content invalidates affected conclusions; propagation is bounded to known consumers.
**Actual disposition decision:** the finding decision-maker (existing role, position 4) owns the correction responsibility in this tabletop. Selected per-consumer disposition: R1 = Unknown and R2 = Unknown, each pending unavailable fresh derivation — the tabletop supplies no re-derivation evidence, so neither record's dependent claims are re-validated and no record update is executed or claimed. Propagation uncertainty is recorded (an unseen consumer record remains Unknown); no exhaustive-propagation claim is made without a consumer index. This is a selected tabletop disposition, not an executed record update.
**Evidence reasoning:** ALGORITHM.html #derivation (changed content invalidates affected conclusions), #authority (correction responsibility, propagation uncertainty), REVIEW-TEMPLATE Outcome/resume row.
**Limits/Unknown:** the consumer list is bounded by known records; unseen consumers remain Unknown, not proof of zero effect.
