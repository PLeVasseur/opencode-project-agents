# Glossary batch orchestrator recovery/reset/rerun plan

## Objective

- [x] Repair orchestrator safeguards after no-commit failure mode.
- [x] Fully reset poor/questionable execution state.
- [x] Re-run orchestrator (no max batches) and capture outcome evidence.

## Stage A: failure-mode hardening

- [x] Keep checklist run-local inside each remediation directory (do not mutate canonical checklist during execution).
- [x] Add explicit gate requiring step1 repo diffs before commit.
- [x] Add pre-batch snapshots and rollback of run-local checklist/ledger on pre-commit failure.
- [x] Strengthen batch prompt to require spec/tooling edits in step1 worktree before checking IDs.
- [x] Keep one-commit-per-batch behavior unchanged.

## Stage B: full reset

- [x] Regenerate canonical checklist with all parent and sub-items unchecked.
- [x] Regenerate canonical seeded ledger and immutable baseline reference from source snapshot.
- [x] Verify canonical checklist/ledger IDs and counts match expected scope (202 parent, 1010 sub).

## Stage C: rerun

- [x] Validate script syntax/help after hardening.
- [x] Start new remediation run with no max-batches cap.
- [x] Capture run directory, first failure/success point, and validator outcomes.

## Exit reporting

- [x] Report script changes made.
- [x] Report reset verification evidence.
- [x] Report rerun result, blockers (if any), and next actions.
