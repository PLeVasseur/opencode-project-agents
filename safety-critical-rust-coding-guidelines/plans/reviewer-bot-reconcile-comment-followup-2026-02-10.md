# Reviewer Bot Reconcile Comment Follow-up Plan (2026-02-10)

## Goal

- Ensure second-hop `workflow_run` reconcile both persists state and posts the reconcile result as a PR comment when it actually changes state.
- Keep artifact-handshake and fail-closed validation behavior from PR `#400` unchanged.
- Validate end-to-end on a fresh upstream-based smoke PR after maintainer merges the fix.

## Why the eye/+1 reactions did not trigger

- Reactions are currently only added in `handle_comment_event()` for `issue_comment` bot commands, where `COMMENT_ID` exists.
- Approval/reconcile flow (`pull_request_review` -> `workflow_run`) does not go through `handle_comment_event()` and does not provide `COMMENT_ID` for that path.
- In the current reconcile implementation, the success message is printed to logs only; no PR comment is posted, so there is nothing to react to.

## Scope

- In scope:
  - Post reconcile comment on PR when workflow-run reconcile changes state.
  - Add tests for comment emission behavior.
  - Keep fail-closed semantics intact.
- Out of scope (for this follow-up PR):
  - Adding reactions to review objects/events (separate feature; would require explicit review-reaction API handling).

## Execution Checklist

### 1) Preflight + branch setup

- [x] Source env and confirm `OPENCODE_CONFIG_DIR`.
- [x] Verify clean/stashed worktree (`git status --short --branch`).
- [x] Verify `gh auth status`.
- [x] Ensure `upstream` remote points to `rustfoundation/safety-critical-rust-coding-guidelines`.
- [x] Fetch and branch from `upstream/main` (new fix branch, no stale base).

### 2) Implement reconcile PR comment emission

- [x] Update `scripts/reviewer_bot.py` in `handle_workflow_run_event()`:
  - [x] Keep strict context resolution + fail-closed logic unchanged.
  - [x] When `success` and `state_changed` are true, call `post_comment(issue_number, message)`.
  - [x] If comment post fails, log a warning but do not roll back persisted state.
  - [x] Keep idempotent no-op behavior (already complete => no state change, no comment).

### 3) Test coverage updates

- [x] Update `.github/reviewer-bot-tests/test_reviewer_bot.py`:
  - [x] Assert reconcile posts PR comment when state changes.
  - [x] Assert no PR comment on idempotent no-op reconcile.
  - [x] Assert comment-post failure does not hard-fail reconcile state change.
- [x] Run `uv run ruff check --fix`.
- [x] Run `uv run pytest .github/reviewer-bot-tests`.

### 4) Commit + PR + maintainer handoff

- [x] Commit using Conventional Commit style.
- [x] Push branch and open upstream PR with:
  - [x] `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - [x] `--head PLeVasseur:<branch>`
- [x] Post heads-up to maintainer/user with PR URL and note that it is ready to merge.

### 5) Post-merge live validation (user requested flow)

- [x] After maintainer merges fix PR, sync local from `upstream/main`.
- [x] Create a fresh smoke branch from `upstream/main`.
- [x] Make a trivial repo change on that branch and open a new PR (unmerged smoke PR).
- [x] Ask collaborator to submit PR approval on smoke PR.
- [ ] Verify first hop (`Reviewer Bot`) behavior:
  - [ ] deferral log for cross-repo as expected
  - [ ] reconcile context artifact uploaded
- [ ] Verify second hop (`Reviewer Bot Reconcile`) behavior:
  - [ ] artifact downloaded/validated
  - [ ] reconcile message logged
  - [ ] reconcile message posted as PR comment
  - [ ] state issue `#314` updated (`review_completed_at` set)
- [ ] Capture run IDs + URLs for final report.

### 6) Cleanup

- [ ] Close smoke PR after validation (no merge).
- [ ] Restore any preflight stash if used.

## Risks / Notes

- `post_comment()` is best-effort network I/O; we should not let transient comment failures undo already-persisted state.
- Reactions (eye/+1) are still command-comment specific unless we explicitly add review-reaction support in a separate change.

## Blockers

- [x] 2026-02-09T23:45:21Z: Waiting for maintainer merge confirmation on PR #401 before running post-merge smoke-validation steps.
