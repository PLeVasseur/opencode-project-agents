# Execute Upstream-Main Branch Cleanup Plan

Execute the checklist plan at:

`$OPENCODE_CONFIG_DIR/plans/upstream-main-branch-cleanup-plan.md`

Execution requirements:

1. Manual execution only (no autopilot/orchestration).
2. First action must be the plan's **Session Bootstrap (must-pass)** section.
3. Canonical base is `upstream/main` (not `origin/main`).
4. Use non-interactive git operations only (no `-i` workflows).
5. Keep both keeper ranges exactly as planned; do not drop checkpoint commits unless explicitly requested.
6. Prefer the single contiguous replay command from the plan:
   - `git cherry-pick 0d441dc^..4ed7f10`
7. Hard-fail immediately on invariant violations:
   - dirty worktree at rewrite start
   - missing boundary commits
   - missing backup refs before rewrite
   - PR-preservation assertion mismatch
8. Update plan checkboxes in place immediately as each task completes (`[ ]` -> `[x]`).

Validation and safety requirements:

- Run all validation gates listed in the plan.
- Push temporary cleanup branch first and only then overwrite target branch using `--force-with-lease`.
- Keep rollback path available via backup refs until final merge.

Reporting requirements:

- Write post-cutover summary to:
  - `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/branch-cleanup-summary.md`
- Include exact commands, pass/fail status, and key output lines for:
  - session bootstrap checks
  - replay/cherry-pick execution
  - obsolete-range removal verification
  - PR-preservation assertions
  - validation gates
  - final push/cutover and post-cutover counts

Final response must include:

- final branch + head SHA
- backup refs created
- dropped range and kept range confirmation
- PR-preservation check results (expected `10` preserved patch-equivalent commits)
- validation outcomes
- push/cutover status and rollback readiness

If blocked by a true external prerequisite or irreversible decision point, ask exactly one targeted question with a recommended default.
