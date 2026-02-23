# Script fix validation summary (v2 orchestrator)

Validation root: `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z`

This validation set focuses on the three reviewer-blocking script issues:

- zero-passed batch handling,
- outer exception rollback,
- out-of-scope checklist/ledger edit enforcement.

## Scenario A: zero-passed batches do not clobber and do not crash run

- Run: `results/zero-pass-run`
- Behavior:
  - `batch-001-failure.json` and `batch-002-failure.json` are both preserved with detailed fields (`passed`, `quarantined`, `reason`, `rolled_back`).
  - Orchestrator continues after the first zero-pass batch and quarantines each failed term.
  - `orchestrator-summary.json` reports `batches_failed=2` and completes cleanly.

## Scenario B: outer exception restores run-local checklist/ledger

- Run: `results/outer-exception-run3`
- Trigger: failing `--extra-check "false"` after term evaluation.
- Behavior:
  - `batch-001-failure.json` includes rollback evidence.
  - `manual-placement-checklist-v2.md` and `manual-placement-ledger-v2.csv` match pre-batch state after failure.

## Scenario C: out-of-scope changes are detected and blocked

- Run: `results/out-of-scope-run`
- Trigger: batch scope WA-001, but agent simulation also edits WA-002.
- Behavior:
  - `batch-001-failure.json` records `Unexpected out-of-scope changes` for WA-002.
  - Orchestrator restores run-local checklist/ledger to pre-batch state.

## Scenario D: failure/crash file collision preserves original failure record

- Run: `results/crash-file-collision-run`
- Setup: pre-seeded `batch-001-failure.json`.
- Behavior:
  - Existing `batch-001-failure.json` remains intact.
  - New outer-exception details are written to `batch-001-crash.json`.

Conclusion: v2 orchestrator script fixes are validated for the reviewer-reported failure modes.

## Scenario E: v3 follow-up fixes (outer handler git rollback and clearer labels)

- Runs:
  - `results/outer-exception-run4`
  - `results/out-of-scope-run2`
- Behavior:
  - Outer exception now executes git worktree rollback (`git restore --staged --worktree .`) in addition to checklist/ledger snapshot restore.
  - Failure payload `rolled_back` now explicitly includes `"worktree (git restore)"`.
  - Raised exception text now states checklist/ledger **and git worktree** are restored.
  - Out-of-scope checklist errors now include sub-item labels (`WA-002.1`..`WA-002.6`) instead of repeated identical parent-only lines.

These follow-up checks close the remaining v3 feedback items required before Wave A execution.
