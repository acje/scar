# SCAR — Strategic Correctness Accuracy Ratchet

SCAR is an algorithm for agents or humans to refine a piece of information inside a structures environment.

| Document | Purpose |
|---|---|
| [Algorithm](ALGORITHM.html) | Normative protocol |
| [Review template](REVIEW-TEMPLATE.md) | Fillable task-specific criteria, evidence, findings and authority records |
| [Sources](SOURCES.md) | Attribution, author adaptations, limits and research gaps |
| [Source audit](SOURCE-AUDIT.md) | Observed passages, actual protocol use, scoped adoption and gaps |
| [Portable skill catalogue](skills/README.md) | Eight reading units: review questions/concerns × subject guidance |
| [Ordinary Git workflow](GIT-WORKFLOW.md) | One drafter/candidate, parallel observation/review and authorized append-only correction |
| [Scenario evals](SCENARIO-EVALS.md) | Expected actions, evidence criteria and limits; packaging checks are not model effectiveness |
| [Historical Jujutsu exploration](JJ-WORKFLOW.md) | Superseded optional exploration, not a tooling mandate |

Select and actually read applicable guidance before assessment; record exact loaded content and local policy using the template. Portable Markdown is not automatic skill-tool installation or discovery. Unsupported subjects remain Unknown without silent generic substitution.

Beads remains durable cross-agent authority for records. `.scratchpad/` is an owned, ignored workspace-local ephemeral adjunct, not a second codebase or acceptance store; `.ooda/` is unchanged. Candidate commits do not imply acceptance. Ordinary Git is sufficient; no jj migration, bespoke controls or enforced writer exclusion is required. Doctrine and scenario evals guide cooperative agents, not arbitrary external/offline writers.

Local packaging checks (not substantive quality or runtime loading):
`python3 scripts/check_skills.py`; `python3 -m unittest discover -s tests -p 'test_*.py'`; `git diff --check`.
