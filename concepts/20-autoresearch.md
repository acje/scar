# 20 — Autoresearch

Status: separately requested researched repository exemplar, not SCAR adoption.
It is not a sixth designated addition; entries 15–19 own the five candidate mechanisms.

## Actual repository mechanism

The observed project runs single-NVIDIA-GPU training experiments; README reports H100
testing, Python 3.10+ and uv. The agent edits train.py, the human edits program.md,
and prepare.py fixes preparation/evaluation. No new packages or evaluator edits are
allowed by the observed agent instructions.

1. Start a dedicated autoresearch/tag branch and establish a baseline.
2. Propose/edit train.py, commit the candidate and run `uv run train.py`.
3. Log commit, val_bpb, memory, status and description in results.tsv.
4. Keep lower val_bpb; otherwise reset to the incumbent. Fix/skip crashes;
   instructions treat a run exceeding ten minutes as a failure.
5. Continue autonomously until interrupted under the source instructions.

Those branch/reset/commit and indefinite-loop instructions are observations, not
permission to import them into this edits-only SCAR mission or its trunk/budget policy.

## Evaluator and time accounting

Lower validation bits per byte is the target. prepare.py fixes VAL_SHARD=6542;
tokenizer training excludes it. Evaluation sums masked non-special-token cross-entropy
nats and target bytes, returning nats divided by log(2) × bytes.
MAX_SEQ_LEN=2048, TIME_BUDGET=300 and EVAL_TOKENS=40×524288 are observed constants.
Evaluation steps floor-divide token budget by batch × sequence length: arbitrary
batch changes need not yield exactly that token count.

train.py seeds torch/CUDA with 42, uses CUDA, Muon+AdamW and torch.compile.
The loop charges training time only when step > 10 and stops at a step boundary
after charged time reaches 300 seconds; final evaluation follows training.
Thus five minutes is charged steady-state training time, not exact total wall time.
Startup/compilation/evaluation and hardware identity matter to fair comparison.

## Example, tradeoffs and instruction tension

An agent changes a training setting and compares val_bpb within the fixed evaluator.
Fast local comparisons can aid iteration, but do not prove a global optimum or
cross-hardware comparability. Broad mutations need not define a fixed neighborhood.
The simplicity section allows substantial equal-result simplification while the loop
says equal/worse reset. This tension is recorded, not resolved as a strict algorithm.

## Limits and SCAR relationship

No repeated seeds, confidence interval or independent final-test mechanism was observed
in the four read files. Reused evaluation can be adaptively overfit (entry 19).
README permission-disabling advice is source text, not adopted authority.
SCAR requires finite shared work, protected obligations and exact acceptance authority;
a lower metric alone cannot confer acceptance. No training/dependency execution occurred.

## Sources and provenance

Entire returned bodies read by research 2026-10-04 (`gacr-cvo`):

- https://raw.githubusercontent.com/karpathy/autoresearch/master/README.md
- https://raw.githubusercontent.com/karpathy/autoresearch/master/program.md
- https://raw.githubusercontent.com/karpathy/autoresearch/master/prepare.py
- https://raw.githubusercontent.com/karpathy/autoresearch/master/train.py

These are mutable master URLs, not a pinned release; no source commit was established.
Repository: https://github.com/karpathy/autoresearch . Runtime claims remain untested here.
