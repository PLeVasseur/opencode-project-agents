# Wave A feedback tooling hardening plan (2026-02-13)

## Objective

Strengthen the Wave A/B remediation tooling so definition operation metadata stays truthful, gate artifacts are generated automatically, and reruns are not blocked by stale historical hard-fail metadata.

## Scope

- Scripts in `reports/` only:
  - `reports/validate-ledger-and-checklist-v3.py`
  - `reports/glossary-batch-orchestrator-v3.py`
- No edits to `src/` spec content.
- Keep default behavior safe for ongoing runs and add stricter checks where they improve reviewer confidence.

## Planned changes

- [x] **P0: Operation truth checks in validator**
  - Add explicit detection for `definition_operation=promote` rows that actually perform insertion-like changes.
  - Reuse hunk/diff evidence logic so both `insert` and `promote` classifications are validated from commit diffs.
  - Emit `WARN_DEFINITION_OPERATION_MISMATCH` by default; support optional fail mode for stricter runs.
  - Include operation-diff modes in validator JSON summary for reviewer traceability.

- [x] **P0: Pre-commit operation truth checks in orchestrator**
  - Extend pre-commit row precheck to quarantine `promote` rows when hunk evidence indicates insertion for the same term.
  - Keep existing strict `insert` checks (`insert_pass`, `swap_detected`) in place.
  - Tighten implementer prompt language so operation choice is explicitly tied to observed diff behavior.

- [x] **P1: Auto-generate Wave A quality gate artifact**
  - Generate/update `wa-quality-gate.json` automatically from current checklist/quarantine state.
  - Mark pass only when WA is fully checked and has no open WA quarantine IDs.
  - Ensure artifact is available before Wave B gate check so WB can proceed without manual gate file creation.

- [x] **P1: Run-local hard-fail reporting**
  - Track hard-fail codes for the current invocation separately from historical failed batches in state.
  - Avoid rerun failures caused solely by stale historical hard-fail records.
  - Preserve total historical failure visibility in summary output.

- [x] **P1: Validation and smoke checks**
  - Run Python compile checks on modified scripts.
  - Run focused smoke checks on known scenarios:
    - promote/insert operation mismatch classification logic
    - WA quality gate auto-generation behavior
    - run-local hard-fail reporting behavior

## Completion criteria

- [x] Validator can surface promote-vs-insert mismatches with clear evidence.
- [x] Orchestrator quarantines promote rows that are actually insert-like before commit.
- [x] `wa-quality-gate.json` is created/updated automatically with pass/block status.
- [x] Orchestrator summary distinguishes current-run vs historical hard-fail context.
- [x] Modified scripts compile and targeted smokes pass.
