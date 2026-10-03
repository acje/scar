# SCAR — Strategic Correctness Accuracy Ratchet

SCAR is an author-defined reusable documentation protocol and template:
**S = Strategic, C = Correctness, A = Accuracy, R = Ratchet**. Build what matters,
check the evidence, resolve supported findings, and advance only an exact,
authorized candidate. It replaces the earlier GACR specification; earlier
rationale remains in Git history, notably `2ef0fb7`. Naming is not established
terminology from the cited sources.

## Read and use

| Document | Purpose |
|---|---|
| [Algorithm](ALGORITHM.html) | Adaptive lifecycle, environment, seven aspects and inline diagram |
| [Review template](REVIEW-TEMPLATE.md) | Compact framing, review, finding and authority record |
| [Worked scenarios](SCENARIOS.md) | Paper counterexamples and evidence/authority decisions |
| [Source notes](SOURCES.md) | Observed material, adaptations and explicit research gaps |

Adaptive **understand/change/verify** progression is the default where designs
collide, especially during high churn. Frame proportionally, build a coherent
increment, interleave checks, assess the coherent candidate, then refine or
revisit understanding when assumptions break. Finish unresolved or rejected
when appropriate; do not retry merely to obtain a clean verdict. Substantive
review is not required after every edit. Exactly one active task at any time.

## Seven aspects

1. Strategic significance — consequential value within the task's intent.
2. Correctness — declared invariants and structural obligations.
3. Accuracy — supported claims and explicit uncertainty.
4. Structure and counterexamples — dependencies, exceptions and falsifiers.
5. Economy — remove redundancy without sacrificing obligations.
6. Ratchet integrity — protected obligations and acceptance authority.
7. Structured environment — organized state, evidence and recoverability.

No improving aggregate score can conceal a failed required aspect. For example,
`(0.9, 0.5)` becoming `(0.8, 0.8)` raises the mean while one aspect regresses.
Aspect verdicts are `Satisfied | Violated | Unknown`; required unknowns block
acceptance. Findings are allegations, adjudicated as
`Supported | Unsupported | Unresolved`, not automatic instructions to edit.
Review-of-review is targeted to concrete doubt, not a compulsory repeated pass.

## Structured environment and ratchet

The repository is the only codebase. Its exact main HEAD is current state;
Git main is trunk-based history. The candidate is uncommitted repository changes
based on that exact commit, with exact content identity, not another durable
store. The scratchpad, typically Beads, holds intent, status, findings, decisions,
uncertainties and evidence references for memory and communication; it is not
an alternate codebase and cannot authorize acceptance.

Advances are verified, authorized commits on main; corrections append to history.
Preserve unrelated edits. Resume by reconciling main, candidate and scratchpad
and checking which evidence still applies. Main is authoritative state, not
automatic proof of quality. The ratchet protects obligations and authority;
the structured environment makes state recoverable. They are distinct aspects.

## Verification and authority boundary

Run from the repository root:

```sh
python3 scripts/verify_docs.py
git diff --check
```

The read-only checker covers local links, aspect names, lifecycle/diagram
structure and selected textual obligations. It does not establish substantive
correctness, validate external sources, execute SCAR, enforce authorization or
prove convergence. Paper scenarios require judgement review. This is not an
executable workflow, security control or calibrated quality metric; no
application test suite or separate local CI entry point is provided.

Designated authority must authorize the exact candidate and baseline; the drafter
cannot self-authorize. Standing authorization can be defined without requiring
a human at every step. Confirm the resulting main commit matches the authorized
candidate before claiming `Accepted`. This documentation mission authorizes
edits only: its verified uncommitted implementation awaits review and designated
commit authority, and does not advance main or claim protocol acceptance.
