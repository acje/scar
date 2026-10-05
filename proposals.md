# Proposals for improving SCAR

Status: discussion only. None of these proposals changes the normative algorithm, template, skills or runtime workflow.

## Preserve the existing design

The previous redesign changed too many things at once: lifecycle, state/storage definitions, annotation format, diagram, skills and authority wording. It also treated a future architectural direction as authorization to replace the current protocol. That redesign has been reverted.

Keep the six lifecycle positions, structured environment, seven aspects, diagram, protected obligations, bounded work and acceptance contract intact. Explore changes individually, with a small diff and a concrete reason. Do not migrate opencode or claim effectiveness from documentation/packaging checks.

## 1. Explain OODA as a reading of the existing lifecycle

**Proposal:** add a short explanatory paragraph, not new stages or a replacement lifecycle.

- Strategic OODA concerns consequential intent, framing, assumptions and the decision to continue, redirect or accept.
- Tactical OODA concerns a coherent increment, observation of check/review evidence, interpretation and finding disposition, then refinement.
- Tactical effects can reopen strategic understanding when assumptions or intent no longer hold.

The existing positions need not map one-to-one to OODA phases. Observe and Orient recur during framing and assessment; Decide is not reserved solely for acceptance. Review remains feedback, not a compulsory third loop.

**Benefit:** makes the intended nested-loop relationship explicit without discarding existing safeguards or representations.

**Risk:** a second description could become a competing transition model. Keep it explanatory and state that existing lifecycle text governs.

**Validation:** walk one ordinary repair and one intent-breaking observation through the existing positions. Confirm no new transition or authorization shortcut is introduced.

## 2. Clarify how annotations guide work without creating more paperwork

**Proposal:** explain that the existing template is a recoverable shared record: reference unchanged intent/evidence and update affected fields rather than filling a new complete form for every cycle.

Use the existing fields for intent, current/candidate identity, evidence, findings, decisions and continuation. Do not replace the template or add a parallel annotation schema.

**Benefit:** reduces duplication while retaining current evidence and authority requirements.

**Risk:** terse records could omit required facts. Linking an unchanged record must not imply stale evidence is reusable.

**Validation:** produce one small completed example using the current template; distinguish an illustrative record from an actual review. Inspect whether it is recoverable without copying every field each cycle.

## 3. Make the skill division clearer before adding skills

**Proposal:** clarify the existing catalogue distinction between review questions/concerns and subject guidance.

- Aspect-oriented guidance answers what to inspect: accuracy, correctness, audience access, security, maintainability and related concerns.
- Subject guidance explains techniques for working on and checking the artefact: Rust applications, PowerPoint decks, HTML pages or another declared subject.

As a separate small increment, add a bounded work/refinement subsection to one existing subject skill, preserving its review techniques and limitations. Start with HTML or PowerPoint to demonstrate that subject expertise is not synonymous with Rust policy.

**Benefit:** moves expertise outward without expanding the algorithm or creating an aspect-by-subject file matrix.

**Risk:** work guidance could silently confer permission or duplicate caller policy. Skills must remain techniques, not acceptance authorities or universal house styles.

**Validation:** a subject example should show both construction and assessment with existing lifecycle positions. Loading or packaging a skill is not evidence of successful subject work.

## 4. Consider attended/unattended Rust profiles as a skill-only change

**Proposal:** after agreeing the division above, consider two operational subject profiles composed with the existing shared Rust skill. Do not copy the full Rust guidance into each.

Inspected sf-sdlc definitions use `attended-app` for CLI/terminal applications and `service-unattended` for daemons/async services and supporting libraries. A supporting library is not thereby a deployed service. SCAR names such as `attended-rust-app` and `unattended-rust-app` should explicitly map to those actual classes.

- Attended profile: command/interface behavior, input/error paths, non-interactive invocation, streams and adopted exit contracts.
- Unattended profile: relevant resource ownership, admission, cancellation, shutdown and persistence/recovery contracts.
- Actual repository policy supplies toolchains, verification commands and binding limits; sample template settings must not become universal defaults.

**Reference for discussion:** reusable attended-tool outcome guidance is owned
by `~/.config/opencode/AGENTS.md` § Attended-tool outcomes. Consult that owner
when evaluating this proposed profile; do not create a competing doctrine here.
This reference does not adopt the profiles or change SCAR's normative algorithm,
protected obligations, required Unknown evidence, or acceptance authority.

**Benefit:** removes operational Rust assumptions from general reasoning without adding core stages or a roster.

**Risk:** taxonomy or duplicated policy could overconstrain targets. Apply checks only to actual ownership boundaries.

**Validation:** review a CLI and a supporting-library example; confirm the library is not required to exhibit daemon behavior. Record source revision and applicability before implementing profiles.

## 5. Separate demonstrated improvement from preservation

**Proposal:** add a sentence to framing or comparison asking for task-specific evidence of the intended improvement, separately from evidence that protected obligations remain satisfied. Use existing objective/criteria/evidence fields, not a new score.

**Benefit:** prevents an equally acceptable revision or cosmetic change being presented as demonstrated improvement.

**Risk:** not every information task has a numeric metric. Qualitative evidence is legitimate when its audience, scope, reasoning and uncertainty are explicit.

**Validation:** compare an accuracy correction with a cosmetic presentation edit. Neither may average away a required failure, and preservation alone must not establish effectiveness.

## 6. Pilot before changing the structured environment

**Proposal:** retain current Git/main/candidate/scratchpad definitions for now. First apply SCAR to a versioned HTML page and a presentation, with the actual delivered representation included in evidence. Broader non-Git storage is a separate design decision, not a prerequisite for subject-agnostic review.

**Benefit:** tests whether current constraints are genuinely limiting before introducing storage adapters or changing authority semantics.

**Risk:** source/version review might be confused with rendered delivery checks. Identify both explicitly and retain Unknown for unperformed required checks.

**Validation:** record recovered state after interruption and the exact accepted artefact. If the existing environment cannot represent a real requirement, document the concrete witness and propose the smallest necessary change.

## Recommended order

Discuss and select one proposal first. Prefer the small OODA explanation plus an example using the unchanged lifecycle; then clarify skill composition and trial a single document subject skill. Consider operational Rust profiles and broader storage only when concrete examples justify them.

Effectiveness should be judged by independently assessed defects, unsupported findings, intended-use improvement and actual recording effort under stated conditions—not line count, number of roles, completed forms or clean packaging tests. No new stage, role, mandatory threshold or runtime mechanism is proposed here.
