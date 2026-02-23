# Plan: Fix reviewer-bot sign-off for PR approvals and issue labels

## References
- Issue: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/388
- PR with bug: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/302
- Docs PR to align with: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/331
- GitHub Actions docs: pull_request_review + fork behavior: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review
- GitHub Actions docs: schedule event (default branch): https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule
- GitHub Actions docs: workflow_dispatch (default branch): https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#defining-inputs-for-manually-triggered-workflows

## Current Behavior Summary
- The reviewer bot stores active review state per issue/PR and sets `assigned_at` and `last_reviewer_activity` when a reviewer is assigned.
- `last_reviewer_activity` only updates on `issue_comment` by the current reviewer, not on PR review submissions.
- The nightly schedule uses `last_reviewer_activity` (fallback `assigned_at`) to post reminders after 14 days and transition notices after 28 days; it reassigns on transition.
- Review state is cleared only when the issue/PR is closed.
- The `sign-off: create pr` label on issues is not treated as review completion and does not stop reminders.

## Desired Behavior
- PR approval by the assigned reviewer ends the reminder lifecycle for that PR.
- PR review comments or changes-requested by the assigned reviewer reset the 14-day clock.
- The `sign-off: create pr` label on issues marks the issue review complete and stops reminders.
- Reviews from non-assigned reviewers do not affect the review timer.

## Execution Checklist

Mark each item off as it is completed during implementation.

- [x] Create a feature branch in the fork for this work (name it consistently; keep upstream `main` untouched).
- [x] Plan logical commit chunks and use Conventional Commits for each chunk.
- [x] Verify fork Actions prerequisites before integration validation:
  - [x] Actions enabled on the fork.
  - [x] Workflow permissions allow writing to issues/PRs (`GITHUB_TOKEN` write for issues/pull-requests).
  - [x] If the workflow requires secrets (bot token), add them to the fork or plan to validate via logs only.

- [x] Workflow: capture PR review events
  - [x] Update `.github/workflows/reviewer-bot.yml` to listen for `pull_request_review` events (`submitted`).
  - [x] Provide review context env vars to the bot, including:
    - [x] `REVIEW_STATE` (APPROVED, COMMENTED, CHANGES_REQUESTED)
    - [x] `REVIEW_AUTHOR`
    - [x] PR number in `ISSUE_NUMBER`
    - [x] `IS_PULL_REQUEST=true`

- [x] Bot state: record completion
  - [x] Extend `active_reviews[issue_number]` with `review_completed_at` (and optionally `review_completed_by` and `review_completion_source`).
  - [x] Add a helper like `mark_review_complete(state, issue_number, reviewer, source)` that:
    - [x] sets `review_completed_at`
    - [x] updates `last_reviewer_activity`
    - [x] clears `transition_warning_sent`
  - [x] Add migration defaults for existing state entries in `set_current_reviewer` or a small helper to ensure the new field exists.

- [x] Handle PR review events
  - [x] Add a handler for `pull_request_review` events in `reviewer_bot.py`.
  - [x] If `REVIEW_STATE == APPROVED` and `REVIEW_AUTHOR` matches the current reviewer:
    - [x] mark the review complete (do not reassign).
  - [x] If `REVIEW_STATE` is `COMMENTED` or `CHANGES_REQUESTED` by the current reviewer:
    - [x] update `last_reviewer_activity` and clear any warning.
  - [x] Ignore PR reviews from non-assigned reviewers.

- [x] Treat issue sign-off label as completion
  - [x] In label handling, when `LABEL_NAME == "sign-off: create pr"` and the target is an issue (not PR):
    - [x] mark the review complete.
  - [x] Do not treat this label as a review label for assignment.

- [x] Skip completed reviews in overdue checks
  - [x] Update `check_overdue_reviews` to ignore entries with `review_completed_at`.

- [x] Tests
  - [x] Add unit tests in `.github/reviewer-bot-tests/test_reviewer_bot.py` for:
    - [x] PR review approval by assigned reviewer sets `review_completed_at` and stops overdue checks.
    - [x] PR review comment or changes-requested by assigned reviewer updates `last_reviewer_activity`.
    - [x] PR review by non-assigned reviewer is ignored.
    - [x] Issue label `sign-off: create pr` sets `review_completed_at`.
  - [x] Run:
    - [x] `uv run pytest .github/reviewer-bot-tests`
    - [x] `uv run ruff check --fix`

- [x] Docs alignment (PR #331)
  - [x] Update `CONTRIBUTING.md` to state:
    - [x] Issues: `sign-off: create pr` marks issue review complete and prompts PR creation.
    - [x] PRs: assigned reviewer approval completes the review and stops reminders.
    - [x] Review comments on PR reset the timer.
  - [x] Coordinate edits with PR #331 to avoid conflicting changes.

## Non-Goals
- No change to assignment mechanics beyond completion behavior.
- No automatic merge-queue actions or new commands.

## Edge Cases / Notes
- If the sign-off label is removed, reminders will not resume unless we add `unlabeled` handling later.
- Approvals from non-assigned reviewers are ignored to avoid false completion.
- Fork-specific: PR events from a forked repo are delivered to the base repo, not the fork. For integration validation, create PRs inside the fork itself to generate `pull_request_review` events in the fork.
- Schedule + workflow_dispatch only run on default branch; when running manual validations, ensure the workflow file exists on the default branch and select the correct ref for the run.
- For fork validation, the workflow change must temporarily be on the fork default branch. This does not require merging to upstream `main`.
- Self-approval may be blocked by GitHub; full approval E2E needs a second account. Otherwise rely on unit tests for approval behavior and use `COMMENTED` reviews to validate activity updates.

## Validation Checklist

### Local (required)

- [x] Run unit tests: `uv run pytest .github/reviewer-bot-tests`
- [x] Run lint fixes: `uv run ruff check --fix`
- [x] Confirm unit coverage for:
  - [x] PR review approval by assigned reviewer marks completion and prevents overdue reminders.
  - [x] PR review comments/changes requested update activity timestamps.
  - [x] Non-assigned reviewer reviews do not affect state.
  - [x] Issue `sign-off: create pr` label marks completion.

### Fork-only integration (required for PR review event, safe, no upstream impact)

All steps below are performed in the fork `PLeVasseur/safety-critical-rust-coding-guidelines` and must not touch upstream state issue #314.

- [x] Create a fork-local test state issue (e.g., "Reviewer Bot State (test)") and note its issue number. (Issue #6)
  - Copy the body format from upstream state issue #314 so `reviewer_queue` and `active_reviews` schema are intact.
- [x] Create a fork-only validation branch from the feature branch (e.g., `validation/issue-388`).
- [x] In the validation branch, update `.github/workflows/reviewer-bot.yml` `STATE_ISSUE_NUMBER` to the fork test issue and commit (Conventional Commit; this commit is fork-only and will be reverted from fork `main`).
  - Do not merge this change into the feature branch or upstream PR.
- [x] Merge the validation branch into fork `main` using a **merge commit** (record the merge SHA for later revert). (SHA: a409ee78a53eafcdf8ffac4b0eda74ded400dd6a)
- [x] Open a test PR **inside the fork** (branch -> fork default branch) so that `pull_request_review` events are emitted in the fork. (PR #7)
- [x] Seed state in the fork test state issue with an `active_reviews` entry for the PR number:
  - `current_reviewer`: your GitHub username
  - `assigned_at`: a recent timestamp
  - (Optional) `last_reviewer_activity`: same as assigned_at
- [x] Submit a PR review as the assigned reviewer:
  - [x] If GitHub blocks self-approval, submit a `COMMENTED` review to validate activity updates.
  - [ ] If a second account is available, submit an `APPROVED` review to validate completion end-to-end.
- [x] Manually run the workflow in the fork via `workflow_dispatch` on fork `main` (Action: reviewer-bot), using the `check-overdue` action where applicable.
- [ ] Confirm in the fork test state issue:
  - [ ] `review_completed_at` set after approval.
  - [ ] No reminder comments are posted after completion.
  - [x] Activity timestamp updates for comment/changes-requested reviews.
- [x] Restore fork `main` to its pre-validation state:
  - Revert the merge commit: `git revert -m 1 <merge_sha>` and push.
  - Do not use force-push or hard reset.
- [x] Close fork test issue and PR when validation is complete and delete the validation branch.

### Outcome checks (required)

- [ ] Confirm PR review approvals stop reminders (no scheduled warning after approval).
- [ ] Confirm issue sign-off label stops reminders.
- [ ] Confirm reminder behavior remains unchanged for items without completion.
