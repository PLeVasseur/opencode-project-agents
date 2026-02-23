# Execute PR #33/#34/#35 stacked CI remediation v5 (start-or-resume, crash-resilient)

Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/pr-33-pr-35-stacked-ci-remediation-plan-v5.md`

Mission:

- Execute the full v5 remediation with strict stack/scope integrity.
- Be crash-resilient: safe for fresh start and safe for resume.

## Non-negotiable operating rules

1. Manual execution only; no autopilot shortcuts.
2. Follow the v5 plan exactly, including phase gates and conflict-scope firewall.
3. Update checkboxes immediately after each completed item; never batch-check.
4. Parent checkbox may be `[x]` only when all child checkboxes are `[x]`.
5. Push to fork only (`origin` / `PLeVasseur/up-streamer-rust`), never upstream.
6. Do not use interactive git commands (`-i`); use headless/non-interactive equivalents.

## Crash-resilient startup algorithm (must run first)

Set canonical paths:

- `PLAN_PATH="$OPENCODE_CONFIG_DIR/plans/pr-33-pr-35-stacked-ci-remediation-plan-v5.md"`
- `PROGRESS_FILE="$OPENCODE_CONFIG_DIR/reports/pr-33-35-remediation-v5-progress.env"`
- `SUMMARY_REPORT="$OPENCODE_CONFIG_DIR/reports/pr-33-35-remediation-v5-run-summary.md"`

Then execute this decision flow:

1. Verify `PLAN_PATH` exists.
2. If both `PROGRESS_FILE` and `SUMMARY_REPORT` are absent:
   - Start a new run from Phase 0.
   - Initialize persisted state in `PROGRESS_FILE` (authoritative for resume):
     - `PLAN_VERSION=v5`
     - `PRA_BRANCH=cleanup/refactor-upstream-main-prA-architecture`
     - `PRB_BRANCH=cleanup/refactor-upstream-main-prB-benchmark`
     - `PRC_BRANCH=cleanup/refactor-upstream-main-prC-smoke`
     - `FORK_OWNER=PLeVasseur`
     - `FORK_REPO=PLeVasseur/up-streamer-rust`
     - `FORK_BASE_BRANCH=main`
     - `LAST_PHASE=phase0`
     - `LAST_SHA=$(git rev-parse HEAD)`
     - `RUN_STATUS=running`
   - Create `SUMMARY_REPORT` with run header and timestamp.
3. If either file exists:
   - Enter resume mode.
   - Source `PROGRESS_FILE` (if present) and treat persisted values as authoritative.
   - Run resume hardening checks before any new mutation.
   - Resume from the first unchecked checkbox in `PLAN_PATH`.
4. Never start a second parallel run when `PROGRESS_FILE` exists; reuse the same run state.

## Required resume hardening checks

Before continuing in resume mode:

1. Verify current branch + `HEAD`.
2. Compare current `HEAD` with `LAST_SHA` from `PROGRESS_FILE`.
3. If `HEAD != LAST_SHA`:
   - Determine whether mismatch is expected from last completed step (e.g., after successful push/rebase step).
   - If not expected, recover to the last safe checkpoint (backup ref/tag created in Phase 0) and resume from first unchecked item.
4. If any git operation is mid-flight (`rebase`, `cherry-pick`, `merge`, `revert`):
   - Resolve/continue if it belongs to the planned current step.
   - Otherwise abort operation, return to last safe checkpoint, and resume from the related checkbox.
5. Remove stale temporary worktrees from aborted runs if present.

## Continuous execution invariants

1. Keep PR A as exactly 4 commits; fix dead code in c2 scope, not as a fifth commit.
2. Enforce c3 conflict-scope firewall:
   - If c3 replay conflicts, resolve within c3 test/helper scope only.
   - Do not widen c2 amendment scope.
3. Enforce PR B API drift fix in benchmark scope and amend PR B commit accordingly.
4. Enforce PR C `.gitattributes` R5 closure by amending smoke commit (no second commit).
5. Run `source build/envsetup.sh highest` before cargo commands in each phase.
6. Unbundled clippy is conditional on valid `VSOMEIP_INSTALL_PATH` and must be recorded as run/skip with rationale.
7. Persist progress after each mutation and each phase transition:
   - update `LAST_PHASE`, `LAST_SHA`, `RUN_STATUS` in `PROGRESS_FILE`
   - append evidence lines (commands/results/decisions) to `SUMMARY_REPORT`

## Publish safety rules

Before and during push operations:

1. Ensure the phase's mandatory validation gates are green (or validly skipped with rationale for unbundled).
2. Push branches to `origin` only, using `--force-with-lease` for rewritten history.
3. Refresh PR bodies after each branch update to keep SHAs/validation notes accurate.
4. Preserve stack topology:
   - PR A base `main`
   - PR B base PR A
   - PR C base PR A

## Blocking policy

If any gate fails:

1. Stop progression immediately.
2. Record exact command, key failure output, and remediation attempt in `SUMMARY_REPORT`.
3. Set `RUN_STATUS=blocked` in `PROGRESS_FILE`.
4. Resume only from the failed checkbox after fix.
5. Ask one targeted question only if blocked by an external prerequisite or true ambiguity.

## Completion output requirements

When execution completes, report:

1. Final phase/gate status with evidence paths.
2. Final branch heads and stack shape proof (`A`, `B`, `C` commit deltas).
3. CI check status for PR #33/#34/#35.
4. Proof that c3 conflict policy was respected (or not needed).
5. Recovery artifacts:
   - `PROGRESS_FILE`
   - `SUMMARY_REPORT`
   - backup refs/tags used for rollback safety.
