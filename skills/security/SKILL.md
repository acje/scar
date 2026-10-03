---
name: scar-security
description: Model scoped adversarial misuse, trust boundaries and mitigations.
---
# Security concern

## Applicability
Use for assets, sensitive data, external inputs or authority boundaries exposed to misuse. Declare system boundary, actors, assets and consequences; do not infer security from protocol acceptance controls.

## Techniques
1. Model processes, stores, external entities, data flows and trust crossings; compare the model to the actual scoped system.
2. Ask what can go wrong at each crossing; write a concrete misuse path. Select a threat technique only with a scope-fit reason (STRIDE is optional).
3. Trace each material threat to reject/mitigate/transfer/accept disposition by the appropriate owner; exercise declared mitigations and retain residual risk.

## Evidence and output
Record threat ID, actor/preconditions, asset/flow, consequence, control, actual test or witness, residual risk and decision owner. Cross-map to correctness, counterexamples and ratchet without claiming those aspects alone establish security.

## Limitations
No exhaustive threat inventory, physical-safety certification, legal compliance or runtime protection follows from this guidance. Missing system/control evidence is Unknown, not safe. No technique is universally sufficient.

## Sources
[OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html), Overview, System Modeling, Choosing a Threat Modeling Technique, Response and Mitigations, Review and Validation; [audit](../../SOURCE-AUDIT.md) N5.
