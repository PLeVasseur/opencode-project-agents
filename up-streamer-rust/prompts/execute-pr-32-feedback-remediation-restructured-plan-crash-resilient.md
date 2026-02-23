# Execute PR-32 remediation plan (start-or-resume, crash-resilient)

Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/pr-32-feedback-remediation-restructured-plan.md`

Mission:

- Complete the full PR-32 remediation execution with strict phase/gate integrity.
- Be resilient to any session crash: safe for fresh start and safe for resume.

## Non-negotiable operating rules

1. Manual execution only; no autopilot shortcuts.
2. Follow the plan exactly, including all commit scopes and manifest timing guardrails.
3. Update checkboxes immediately after each completed item; never batch-check later.
4. Parent checkbox may be `[x]` only when all child checkboxes are `[x]`.
5. Push/PR only to fork (`origin` / `$FORK_REPO`), never upstream during remediation.

## Crash-resilient startup algorithm (must run first)

Set canonical paths:

- `PLAN_PATH="$OPENCODE_CONFIG_DIR/plans/pr-32-feedback-remediation-restructured-plan.md"`
- `PROGRESS_FILE="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-progress.env"`
- `SUMMARY_REPORT="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-run-summary.md"`

Then execute this decision flow:

1. Verify `PLAN_PATH` exists.
2. If both `PROGRESS_FILE` and `SUMMARY_REPORT` are absent:
   - Start a new run from Phase 1.
3. If either file exists:
   - Enter resume mode.
   - Source `PROGRESS_FILE` (if present) and treat persisted values as authoritative (`CHECKPOINT_TAG_PREFIX`, `RESTACK_BRANCH`, `BASE_SHA`, `SOURCE_SHA`, `BACKUP_BRANCH`, `PRA_BRANCH`, `PRB_BRANCH`, `PRC_BRANCH`, `FORK_*`).
   - Run Phase 7 crash/restart checks before any new mutation.
   - Resume from the first unchecked checkbox in the plan.
4. Never start a second parallel run when `PROGRESS_FILE` exists; reuse the same run state.

## Required resume hardening checks

Before continuing in resume mode:

1. Verify current branch + `HEAD`.
2. Compare `HEAD` with `LAST_SHA` from `PROGRESS_FILE`.
3. If mismatch:
   - locate nearest checkpoint tag (`$CHECKPOINT_TAG_PREFIX-cN`),
   - either continue from consistent checkpoint,
   - or rollback to `$BACKUP_BRANCH` and restart at Phase 2.
4. If a git operation is mid-flight (`rebase`, `cherry-pick`, etc.), resolve that state before plan progression.
5. Remove stale temporary worktrees from aborted runs if needed.

## Execution invariants to enforce continuously

1. Keep Commit 0 intentionally small exactly per plan scope.
2. Enforce manifest mutation schedule exactly (including C2/C3/C5 dependency timing).
3. Enforce Commit 2 gate proving no dangling `subscription-cache` path deps in workspace manifests.
4. Run commit gates from isolated worktrees with shared `CARGO_TARGET_DIR` cache.
5. Run overlap subroutine after each commit (`c0`..`c5`) and fail fast on disallowed overlap.
6. Persist progress and summary evidence after each commit and each phase transition.

## Publish safety rules

Before creating PRs:

1. Phase 5 validation must be fully green.
2. Verify fork base sync exactly:
   - `origin/$FORK_BASE_BRANCH` SHA must equal `BASE_SHA`.
3. If fork base mismatches, stop and sync fork base first.
4. Create PRs only in `$FORK_REPO` with correct stacked bases.

## Blocking policy

If any gate fails:

1. Stop progression immediately.
2. Record exact command, failure output, and remediation in `SUMMARY_REPORT`.
3. Resume only from the failed gate after fix.
4. Ask one targeted question only if blocked by a true external prerequisite or ambiguity that changes outcomes.

## Completion output requirements

When execution completes, report:

1. Final phase/gate status with evidence paths.
2. Final commit list (hash + subject + scope).
3. Proof of content identity vs `SOURCE_SHA` tip.
4. PR URLs (A/B/C), bases, and dependency chain.
5. Recovery artifacts (`PROGRESS_FILE`, `SUMMARY_REPORT`, checkpoint tags, backup refs).
