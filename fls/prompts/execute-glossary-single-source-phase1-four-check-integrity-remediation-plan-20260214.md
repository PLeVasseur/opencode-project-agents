Execute the crash-resumable checklist at:
`$OPENCODE_CONFIG_DIR/plans/glossary-single-source-phase1-four-check-integrity-remediation-plan-20260214.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Goal: make all four verification checks pass with `exit 0` and `result: no differences under configured comparison policy.`
- Preserve strict four-commit topology over pinned `UPSTREAM_MAIN_PIN`.
- Do not add a fifth commit.
- Do not push to upstream.
- Script-first policy is mandatory: use repo scripts (`./make.py`, `./tools/verify-html-diff.py`, `./generate-glossary.py` as defined in the checklist), never direct `sphinx-build`/`sphinx-autobuild`.

Fresh-or-Resume contract (must work for both):
1. Canonical cross-run files:
   - `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
   - `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
   - `RUN_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation.lock`
   - `RUN_SUMMARY_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-summary.md`
2. Remediation run discovery:
   - If `REMEDIATION_RUN_ID` is set and matching `remediation.state.env` exists, validate and resume that run.
   - Otherwise scan `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-*/remediation.state.env` and pick newest incomplete (`M10_DONE!=1`), using the checklist tie-break/corrupt-state rules.
   - If no incomplete run exists, start a new run at Stage `M0`.
3. Resume behavior:
   - Load and validate both run files before proceeding:
     - `RUN_STATE_FILE=$RUN_ROOT/remediation.state.env`
     - `RUN_CHECKLIST_STATE_FILE=$RUN_ROOT/checklist.state.env`
   - Run Stage `M1b` reconciliation and resume from reconciled `CURRENT_STAGE`.
   - Do not repeat completed stages unless reconciliation requires it.
4. Concurrency safety:
   - Enforce single-writer lock behavior and stale-lock handling exactly as specified.

Execution requirements:
1. Execute stages in order (`M0`..`M10`) with atomic state persistence.
2. Enforce checkbox guardrails strictly:
   - Mirror child checklist completion in `RUN_CHECKLIST_STATE_FILE` (`CB_*` keys).
   - Do not set `M*_DONE=1` unless required checklist keys are complete and `M*_CHECKLIST_DONE=1` is persisted.
3. Enforce all hard gates:
   - repo-root/branch handoff checks
   - immutable key validation
   - topology and ancestry checks
   - commit-scope allowlist manifests
   - clean index/worktree constraints
4. Enforce strict verification policy:
   - `diff-upstream-main-vs-commit3.txt` -> required pass
   - `diff-commit3-vs-commit4.txt` -> required pass
   - `diff-upstream-main-vs-commit4.txt` -> required pass
   - `capstone-repro-commit4.txt` -> required pass
5. Preserve crash-window semantics:
   - `M8`: pre-push preparation only.
   - `M9`: push with explicit `--force-with-lease=refs/heads/$REPACK_BRANCH:$OLD_REMOTE_SHA`.
   - `M9b`: canonical state/report + run summary finalization only after push confirmation.
6. If any invariant or mandatory stop condition fails, stop immediately and report blockers.
7. Stop at Stage `M10` manual-review checkpoint.

Finish by returning:
- Whether run was new or resumed, and selection basis.
- Identifiers and paths:
  - `REMEDIATION_RUN_ID`
  - `RUN_ROOT`
  - `RUN_STATE_FILE`
  - `RUN_CHECKLIST_STATE_FILE`
  - `RUN_ARTIFACT_ROOT`
  - `RUN_LOG`
- Completion matrix:
  - `M0_DONE..M10_DONE`
  - `M0_CHECKLIST_DONE..M10_CHECKLIST_DONE`
- Reconciliation decisions and crash-window path taken.
- Commit/remote map:
  - `OLD_COMMIT4_SHA`
  - `NEW_COMMIT4_SHA`
  - `OLD_REMOTE_SHA`
  - `REPACK_REMOTE_SHA`
- Verification results (exit code + result line) for all four reports.
- Exact artifact/report paths, including:
  - four verification reports
  - integrity-chain report
  - commit-scope allowlist manifests
  - `RUN_SUMMARY_FILE` block reference
- Confirmation that repo scripts were used (no direct `sphinx-build`/`sphinx-autobuild`).
- Confirmation execution stopped at the manual-review stop point.
