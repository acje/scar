# 01 — Structured environment and recovery

Status: existing SCAR mechanism; explanation, not a storage redesign.
Numbering throughout this library is for retrieval, not lifecycle order.

## Mechanism

Keep four identities distinguishable: Scratchpad, Current state, History and Candidate.
The repository alone is the codebase. Beads carries durable cross-agent intent,
findings, decisions and evidence pointers; owned `.scratchpad/` is an ephemeral
adjunct with recovery pointers and retention deadline in Beads, never secrets or authority.
Ignoring it does not untrack existing content or ensure secrecy/cleanup; `.ooda/` is unchanged.
Current state is the uniquely resolved exact accepted main commit, not arbitrary HEAD,
jj `@`, a change ID or proof of historical quality. History is trunk-based Git main.
Candidate is scoped uncommitted content or a mutable committed jj stack bound to that
base, with exact ordered full revision IDs, sole parents and all introduced content,
including new files and deletions. Candidate commits are not acceptance.

On interruption, reconcile actual main, candidate and scratchpad before continuing.
If main moved, reconcile rather than overwrite; refresh affected evidence and authority.

## Example

A reviewer inspected candidate digest A against accepted main H. After interruption, the
executor finds main J and candidate B. The old review is not silently applicable:
record changed identities, preserved unrelated edits and the next authorized step.

## Limits

A filename or remembered branch does not identify content. Beads records corroborate
state but cannot confer acceptance. Recovery guidance is documentary, not an
implemented transactional recovery system or guarantee of host availability.

## Sources and provenance

- [SCAR environment](../ALGORITHM.html#environment), reconciliation and authority;
  complete local protocol read on 2026-10-04.
- Research inventory: Beads `gacr-cvo`; taxonomy: `gacr-2lk`.
- No external derivation or runtime recovery experiment is claimed.
