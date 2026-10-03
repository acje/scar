---
name: scar-maintainability
description: Inspect comprehension, change propagation and synchronized evidence.
---
# Maintainability concern

## Applicability
Use when an artefact is likely to be maintained or when a change affects callers, dependencies, documentation or alternate representations. State the expected next change, not speculative future features.

## Techniques
1. Trace the changed concept through direct callers, callees, defining types and dependent representations; identify what must change together.
2. Walk a plausible small future change and inspect understandable names, unnecessary indirection and speculative abstractions.
3. Separate structural tidying from behavior changes. Check synchronized build/test/use documentation; for edited guards plant a real violation, observe failure, revert, then observe clean.

## Evidence and output
Record affected paths, change scenario, coupling witness, preserved obligations and check results. Report large out-of-scope opportunities rather than silently executing them. Map to economy, structure, correctness and structured environment; safe future change is a distinct concern question.

## Limitations
Readability judgement is scoped, not a measured universal score. A green test never observed failing is weak evidence of guard bite. External comment advice cannot override observed binding house style, especially Rust rules.

## Sources
[Google code-review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html), Complexity, Tests, Documentation, Context, Functionality; [audit](../../SOURCE-AUDIT.md) N6. Structural/behavior separation and four-step guard proof are explicit SCAR author adaptations.
