# PR Approval Smoke Test Plan

## Goal

Validate that PR approvals are being captured correctly in GitHub by opening a disposable test PR and having it approved.

## Checklist

- [x] Confirm working tree state and note any unrelated local changes
- [x] Check out `main`
- [x] Fetch latest remote refs
- [x] Hard reset local `main` to `origin/main`
- [x] Create a disposable branch from synced `main` (for example, `test/pr-approval-smoke-<date>`)
- [x] Make one trivial, non-functional change clearly marked as test-only
- [x] Commit with a Conventional Commit message indicating this is a test PR
- [x] Push branch to remote
- [x] Open a non-draft PR with clear do-not-merge labeling
- [x] Share PR link for manual approval by collaborator
- [ ] Confirm approval appears on the PR
- [ ] Close the PR without merging

## Notes

- This is a process validation PR only and is not intended to be merged.
- Use a PR title prefix such as `[DO NOT MERGE]` to minimize accidental merge risk.
