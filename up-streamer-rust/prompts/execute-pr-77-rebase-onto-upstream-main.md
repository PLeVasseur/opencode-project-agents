# Execute PR 77 Rebase Onto Upstream Main

Execute the checklist plan at:

`$OPENCODE_CONFIG_DIR/plans/pr-77-rebase-onto-upstream-main-checklist-plan.md`

Execution requirements:

1. Manual execution only (no autopilot/orchestration).
2. Run the plan in strict order, starting at **Phase 1: Session bootstrap and invariant checks**.
3. Hard-fail immediately on invariant violations (dirty tree, remote mismatch, HEAD/PR SHA mismatch, missing keep set).
4. Use only non-interactive git commands (no `-i` flows).
5. Use `--force-with-lease` only for remote rewrite push.
6. Derive keep commits dynamically from `git cherry -v`; do not substitute hardcoded commit lists.
7. Prefer the direct rebase path first; use fallback cherry-pick rebuild only if rebase becomes noisy/high-risk.
8. Keep all artifacts under:
   - `$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/`
9. Update plan checkboxes in place immediately as each item completes (`[ ]` -> `[x]`).

Validation and completion requirements:

- Run all Phase 4 validation commands exactly as listed.
- Verify post-rewrite duplicate-proof checks (`git cherry -v` has no `-` lines).
- Verify PR compare stats after push and include final `ahead_by/behind_by/total_commits`.
- Write final execution report to:
  - `$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-77-rebase-execution-report.md`

Final response must include:

- branch + head SHA
- backup branch created
- whether preferred path or fallback path was used
- conflict summary and resolutions
- validation results
- final PR URL + compare stats + merge state

If blocked by a true external prerequisite or irreversible decision point, ask exactly one targeted question with a recommended default.
