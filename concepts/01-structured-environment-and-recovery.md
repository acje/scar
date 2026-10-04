# 01 — Structured environment and recovery

Status: existing SCAR mechanism; explanation, not a storage redesign.
Numbering throughout this library is for retrieval, not lifecycle order.

## Mechanism

Keep four identities distinguishable: Scratchpad, Current state, History and Candidate.
The repository alone is the codebase. Scratchpad, usually Beads, carries intent,
findings, decisions and evidence pointers; it is not an alternate codebase.
Current state is exact main HEAD, not proof of historical quality.
History is trunk-based Git main. Candidate is scoped uncommitted content bound
to an exact main base, including new files and deletions.

On interruption, reconcile actual main, candidate and scratchpad before continuing.
If main moved, reconcile rather than overwrite; refresh affected evidence and authority.

## Example

A reviewer inspected candidate digest A against HEAD H. After interruption, the
executor finds HEAD J and candidate B. The old review is not silently applicable:
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
