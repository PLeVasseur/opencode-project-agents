Execute the recovery checklist at:
`$OPENCODE_CONFIG_DIR/plans/glossary-single-source-phase1-phase8-9-recovery-checklist-20260214.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Recovery scope: restart at Phase 8/9 defect boundary only
- Preserve strict four-commit stack over pinned `UPSTREAM_MAIN_PIN`
- Do not rerun Phases 1-7
- Do not add a fifth commit
- Do not push to upstream

Fresh-or-Resume contract (must work for both):
1. Canonical run files:
   - `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
   - `STATE_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.lock`
   - `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
2. Recovery-run discovery:
   - If `RECOVERY_RUN_ID` is already set and corresponding recovery state exists, resume that run.
   - Otherwise scan `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-phase8-9-recovery-*/recovery.state.env` and pick the newest incomplete run (`R10_DONE!=1`) if present.
   - If no incomplete recovery run exists, start a new recovery run using Stage R0.
3. Resume behavior:
   - Load `RECOVERY_STATE_FILE`, validate immutable keys, and run Stage R1b reconciliation before proceeding.
   - Resume from reconciled `CURRENT_STAGE`; do not repeat already-completed stages unless reconciliation requires it.
4. New-run behavior:
   - Initialize recovery root/state/log and all required flags exactly as specified in the checklist.
5. Concurrency safety:
   - Enforce single-writer lock behavior and stale-lock handling exactly as specified.

Execution requirements:
1. Execute the checklist stages in order, persisting checkpoint flags and critical values atomically.
2. Enforce all hard gates for staging, verifier policy markers, topology, and clean working state.
3. Keep integrity decision policy strict:
   - Required pass/fail gates:
     - `diff-commit3-vs-commit4.txt` -> no differences under configured policy
     - `capstone-repro-commit4.txt` -> no differences under configured policy
   - Informational-only (non-blocking):
     - `diff-upstream-main-vs-commit3.txt`
     - `diff-upstream-main-vs-commit4.txt`
4. Preserve crash resilience semantics:
   - Stage R8 is pre-push preparation only.
   - Stage R9 performs push with explicit `--force-with-lease=refs/heads/$REPACK_BRANCH:$OLD_REMOTE_SHA`.
   - Stage R9b performs canonical state/report finalization only after push confirmation.
5. If any invariant or mandatory stop condition fails, stop immediately and report blocker details.
6. Stop after Stage R10/manual review checkpoint; do not replace original branch.

Finish by returning:
- Whether this was a new run or resumed run, and how it was selected.
- Recovery identifiers and paths:
  - `RECOVERY_RUN_ID`
  - `RECOVERY_ROOT`
  - `RECOVERY_STATE_FILE`
  - `RECOVERY_ARTIFACT_ROOT`
- Stage completion matrix (`R0_DONE`..`R10_DONE`, including `R1B_DONE`, `R9B_DONE`).
- Reconciliation decisions taken (if resumed) and crash-window branch followed.
- Commit/remote map:
  - `OLD_COMMIT4_SHA`
  - `NEW_COMMIT4_SHA`
  - `OLD_REMOTE_SHA`
  - `REPACK_REMOTE_SHA`
- Verification results with exit codes and result lines for all four reports.
- Exact paths for generated artifacts and integrity-chain report.
- Confirmation that upstream comparison diffs were treated as informational-only and non-blocking.
- Confirmation that execution stopped at the planned manual-review stop point.
