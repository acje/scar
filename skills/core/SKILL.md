---
name: scar-core
description: Apply concrete techniques to all seven SCAR review questions.
---
# Core review techniques

## Applicability
Consider all seven aspects for every SCAR task, including review targets. Declare task-specific criteria and justified omissions; selecting profiles never removes this obligation. Read the [protocol](../../ALGORITHM.html#aspects) before assessment.

## Techniques
| Aspect | Concrete inspection | Counterexample to seek |
|---|---|---|
| Strategic significance | Trace requested change or finding to named audience, consequence and intent; rank consequential effects before polish. | A correct change serves a different task. |
| Correctness | Enumerate declared invariants; walk normal, boundary and failure paths; run declared checks. | A supported input or transition violates an invariant. |
| Accuracy | Compare each material claim with the actual cited passage, version and scope; distinguish observation from adaptation. | Citation exists but says something weaker or different. |
| Structure and counterexamples | Draw dependency/exception paths; try an alternative reading and a concrete falsifier for the leading conclusion. | A direct caller, exception or omitted premise reverses it. |
| Economy | Identify duplicated work/criticism; simulate deletion against protected obligations and required evidence. | Shorter text removes a necessary qualification or witness. |
| Ratchet integrity | Trace per-aspect protection, finding adjudication and exact designated authority; compare required obligations individually. | Averaging, stale authorization or self-authorization bypasses a failure. |
| Structured environment | Reconstruct main/base/candidate/scratchpad identities and resume state from the record; test evidence reuse against unchanged context. | Filename-only identity hides changed content. |

## Evidence and output
Record criterion → exact target/base/criteria/context → witness locator/result → reasoning → uncertainty/applicability, with Satisfied | Violated | Unknown and counterexample/omission rationale. For a review target inspect the allegation's support, not automatically the candidate. Disposition belongs at protocol position 4.

## Limitations
These are SCAR author techniques, not a validated score or independent mathematical basis. Errors and incomplete required coverage are Unknown. No recursive clean-pass requirement, extra stage or acceptance authority is introduced.

## Sources
[SCAR aspects and derivation](../../ALGORITHM.html#aspects), [framing](../../ALGORITHM.html#step-1), [authority](../../ALGORITHM.html#authority); [source audit](../../SOURCE-AUDIT.md) E1–E5 distinguish inspiration from protocol-specific adaptations.
