# Rebase `cleanup/refactor-upstream-main` onto `upstream/main` after PR #77

## Confirmed Context

- [x] Verified PR #77 merged on 2026-02-12 as squash commit `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`.
- [x] Verified squash commit `b6bc245...` has one parent (`ae8afd92c1285bb09beadb0dfb5cf1f8884e1e52`), confirming squash merge semantics.
- [x] Verified PR #77 contained 10 commits pre-merge.
- [x] Integrated key fact: there are no duplicate commit IDs to drop; the rebase must replay only the post-cutpoint branch tail.

## Execution Plan

- [x] Create a safety backup ref before rewriting history (e.g., `backup/cleanup-refactor-upstream-main-pre-rebase-2026-02-13`).
- [x] Fetch remotes and update local `upstream/main` so it points to `b6bc245...`.
- [x] Confirm branch/working tree preconditions (`cleanup/refactor-upstream-main`, no unrelated staged conflict state).
- [x] Reconfirm cutpoint commit where already-integrated (squashed) work ends (expected `7d1a6c7467250c72ac61cee992a559ef45264715`).
- [x] Run tail-only replay rebase: `git rebase --onto upstream/main 7d1a6c7`.
- [x] Resolve conflicts and/or empty-pick prompts as needed, then continue to completion.
- [x] Verify post-rebase history shape and diff scope against `upstream/main`.
- [x] Run targeted validation for affected crates/workflows.
- [x] Push rewritten branch with `git push --force-with-lease origin cleanup/refactor-upstream-main`.
- [x] Confirm PR diff is clean and only contains intended branch-specific changes.

## Recovery Contingency

- [ ] If rebase outcome is not acceptable, restore from the backup ref and retry with an adjusted cutpoint.
