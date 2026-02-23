# Execute rebase for `cleanup/refactor-upstream-main` after PR #77 squash merge

Execute the checklist plan at:

`$OPENCODE_CONFIG_DIR/plans/rebase-cleanup-refactor-upstream-main-after-pr77-squash-plan.md`

Execution requirements:

1. Manual execution only; no autopilot shortcuts.
2. Start by re-validating the confirmed context:
   - PR #77 merged as squash commit `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`.
   - PR #77 had 10 commits pre-merge.
   - There are no duplicate commit IDs to drop; this is a tail-replay rebase problem.
3. Update plan checkboxes in place as each step completes (`[ ]` -> `[x]`).
4. Create a backup ref before rewriting history.
5. Fetch remotes and ensure local `upstream/main` is current before rewrite.
6. Use the cutpoint strategy from the plan and run:
   - `git rebase --onto upstream/main 7d1a6c7`
7. Resolve conflicts/empty-picks carefully and continue to completion.
8. Run targeted validation checks after rebase.
9. Push rewrite with `git push --force-with-lease origin cleanup/refactor-upstream-main`.

Completion requirements:

- Confirm final branch head SHA and that history shape is correct vs `upstream/main`.
- Confirm PR diff is clean and only shows intended branch-specific changes.
- Report any conflicts and their resolutions.
- If blocked by a true external prerequisite, ask exactly one targeted question with a recommended default.
