# Ordinary Git SCAR workflow

The [protocol](ALGORITHM.html#environment) and [authority boundary](ALGORITHM.html#authority) govern. Use existing Git and project checks, not a new VCS, custom gate, lock, permission system or daemon. One named drafter owns one active candidate for one task; observers and reviewers may work in parallel without editing that candidate. This is cooperative doctrine, not prevention of noncooperating writers, external copies or offline edits.

## Observe and frame

From the named repository, inspect `git status --porcelain=v1 --untracked-files=all`, `git diff`, `git diff --cached` and `git log --oneline -10`. Resolve accepted main with `git rev-parse --verify refs/heads/main^{commit}` and record its full ID and observation context. HEAD is checkout context, not fallback acceptance authority. Missing or stale accepted state is Unknown/Unresolved.

Record scope, baseline dirty/untracked/staged work, drafter, reviewer, decision-maker, acceptance authority and permitted operations in [the template](REVIEW-TEMPLATE.md). Identify the exact candidate including new files and deletions using scoped bytes/digests or snapshots. Do not reset, overwrite, clean or stage unrelated work. No feature branch or candidate stack is required.

Declare the full accepted history baseline ID and observation context. After that declared baseline, every accepted successor must be a single-parent append-only commit whose sole parent is the immediately preceding exact accepted main commit. No merges or rewriting accepted history; inherited history at or before the baseline is not certified by this rule.

## Draft, check and review

The drafter makes small coherent increments within the one candidate. Observers/reviewers inspect exact content and return evidence/findings, not competing edits. Run the task's declared checks plus `git diff --check`. This repository supplies documentation, not a packaging checker or test runner: inspect tracked references with `git grep` and manually compare local Markdown/HTML link targets and fragments with tracked files and HTML IDs. Record coverage and gaps; whitespace/reference/link inspection is not substantive review or model effectiveness.

Bind check/review results to candidate, accepted baseline, criteria and evidence context. Adjudicate supported, unsupported and unresolved findings; changed content or context invalidates affected evidence/authorization. Reconcile if another writer or main movement is observed; do not overwrite it. Single-writer agreement is not a race-free technical guarantee.

## Authorized acceptance only

Commands are guidance, not authorization to execute. If this task forbids commit/push, stop with the exact reviewed candidate and an Unresolved acceptance outcome. Successful checks alone cannot confer authority.

When designated authority explicitly permits ordinary Git acceptance, recheck actual main, candidate, staged content, criteria, evidence and authority. Use `git add -- <explicit scoped paths>`, inspect `git diff --cached` and `git status`, then `git commit -m '<authorized intent>'` only for the authorized content. If a path mixes unrelated changes, separate the scoped staging safely or stop; never use blanket `git add .`. Record the resulting full commit ID, inspect its actual content and sole parent, and confirm `refs/heads/main` names that exact authorized single-parent successor of the expected accepted main before reporting Accepted. A commit elsewhere or a pre-existing candidate commit is not acceptance. If ordinary Git cannot perform the authorized advancement safely, report Unresolved rather than introduce advanced plumbing or overwrite work. Push needs separate authority.

Correct accepted mistakes by a new scoped task and authorized single-parent append-only corrective commit. Never merge into, rewrite, amend, rebase, reset or force-push accepted history after the declared baseline. A supplied linear log does not prove no rewrite, exclusivity, intent or historical authority; unavailable witnesses remain Unknown.

## Scratch and learning

Beads holds durable records. Owned ignored `.scratchpad/` remains an ephemeral adjunct with owner, recovery pointers and retention deadline recorded before use; promote needed evidence to Beads before deleting only owned temporary files. Missing scratch-dependent evidence is Unknown. Ignore is not secrecy, untracking, backup exclusion or secure deletion; do not store secrets. Existing `.ooda/` remains unchanged.

Use [scenario evals](SCENARIO-EVALS.md) to inspect action/evidence traces. Findings are learning signals, not bespoke enforcement or demonstrated model effectiveness.
