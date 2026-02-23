# Execute fork-main sync to upstream/main (fresh session)

Execute this plan exactly:

- `$OPENCODE_CONFIG_DIR/plans/sync-origin-main-to-upstream-main-plan.md`

Execution requirements:

1. Manual execution only (no autopilot shortcuts).
2. Treat the plan as a live ledger and tick checkboxes immediately after each completed item (`[ ]` -> `[x]`); do not batch updates.
3. Assume fresh session defaults: re-verify remotes, branch state, and invariants from scratch.
4. Never push to or modify `upstream`; only fetch from `upstream` and push to `origin`.
5. Enforce race guards and rollback anchor steps before updating `origin/main`.
6. Verify end state:
   - `origin/main` equals `upstream/main`
   - the fork PR from `cleanup/refactor-upstream-main` to `main` shows exactly 6 commits
   - upstream-only commit `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81` is not in that PR commit list
7. If blocked by a true external prerequisite, ask exactly one targeted question, include a recommended default, and explain what changes based on the answer.

Completion output requirements:

- Report old/new `origin/main` SHA and final `upstream/main` SHA.
- Report rollback backup tag name/SHA and remote verification evidence.
- Report fork PR URL and final commit count.
