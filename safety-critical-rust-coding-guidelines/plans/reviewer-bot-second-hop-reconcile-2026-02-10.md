# Reviewer Bot Second-Hop Reconcile Plan (2026-02-10)

## Objective

Implement and verify an automatic second-hop reconciliation path so PR approvals on fork-based PRs are persisted without manual `@guidelines-bot /rectify`.

## Root Cause Summary

- `pull_request_review` runs on fork PRs can execute with read-only token permissions.
- In that mode, reviewer-bot can detect approvals but cannot persist state to issue `#314`.
- Current behavior defers with a log message that asks for manual `/rectify`.
- We need an automatic trusted follow-up run with write-capable permissions.

## Known Sequencing Constraint

- GitHub `workflow_run` triggers only when the workflow file exists on the default branch.
- Full end-to-end validation of the second-hop workflow therefore happens **after merge**.
- This plan includes a maintainer hand-off checkpoint: once merged and smoke PR setup is ready, pause and tell the maintainer exactly: `ok, go approve`.

## Mandatory Execution Discipline

- [x] This plan file exists in `$OPENCODE_CONFIG_DIR/plans/`.
- [x] Before starting implementation, confirm this rule: **every completed checkbox must be flipped from `[ ]` to `[x]` immediately before moving to the next step**.
- [x] If blocked, add a short blocker note under "Blockers" with timestamp and stop at that step.
- [x] Before any branch switch/reset, run `git status --short --branch`; if dirty, stash with a clear message (do not lose work).
- [x] Verify CLI auth up front with `gh auth status`.

## Scope

In scope:
- Add a second-hop workflow triggered by `workflow_run` of `Reviewer Bot`.
- Reconcile PR approval state in `scripts/reviewer_bot.py` when event context is `workflow_run`.
- Add/adjust tests in `.github/reviewer-bot-tests/test_reviewer_bot.py`.
- Validate with lint + unit tests + live smoke test.

Out of scope:
- Reworking reviewer assignment logic.
- Changing state storage model away from issue `#314`.

## Phase 0 - Fresh Session Bootstrap

- [x] Source environment and verify config dir:
  - `source ./opencode-env.sh`
  - `printenv OPENCODE_CONFIG_DIR`
- [x] Preflight git/auth state:
  - `git status --short --branch`
  - `gh auth status`
  - If dirty: `git stash push -u -m "wip before reviewer-bot-second-hop plan"`
- [x] Sync local main:
  - `git checkout main`
  - `git fetch origin`
  - `git reset --hard origin/main`
- [x] Create fix branch **from synced `main`**:
  - `git switch -c fix/reviewer-bot-auto-reconcile-fork-pr-approvals || git switch fix/reviewer-bot-auto-reconcile-fork-pr-approvals`

## Phase 1 - Confirm Baseline Failure Signal

- [x] Choose baseline PR for evidence:
  - Prefer PR `#397`.
  - If `#397` is unavailable/stale, choose the latest comparable fork PR with an `APPROVED` review.
  - Example selector command:
    - `gh pr list --repo rustfoundation/safety-critical-rust-coding-guidelines --state all --limit 100 --json number,headRepositoryOwner,reviews,url --jq '.[] | select(.headRepositoryOwner.login != "rustfoundation") | select(any(.reviews[]?; .state == "APPROVED")) | "#\(.number) \(.url)"'`
  - Record the selected PR number as `BASELINE_PR` for all commands in this phase.
  - Selected `BASELINE_PR`: `#397`
- [x] Inspect failing fork-PR approval run and capture evidence:
  - `gh run list --repo rustfoundation/safety-critical-rust-coding-guidelines --workflow reviewer-bot.yml --limit 30`
  - `gh run view <run_id> --repo rustfoundation/safety-critical-rust-coding-guidelines --log`
- [x] Verify logs show all of:
  - `Issues: read`
  - `PullRequests: read`
  - `Deferring cross-repo pull_request_review reconciliation`
- [x] Verify state entry remains incomplete for `BASELINE_PR` in issue `#314` (`review_completed_at: null`).
  - Example check command:
    - `gh api repos/rustfoundation/safety-critical-rust-coding-guidelines/issues/314 --jq '.body' | rg -n "'${BASELINE_PR}'|review_completed_at|review_completion_source" -C 4`

## Phase 2 - Implement Second-Hop Automation

- [x] Add workflow file `.github/workflows/reviewer-bot-reconcile.yml` with:
  - trigger: `workflow_run` on workflow name `Reviewer Bot`
  - `types: [completed]`
  - job guard: only when `github.event.workflow_run.event == 'pull_request_review'`
  - permissions: `issues: write`, `pull-requests: write`, `contents: read`
  - env passed to script:
    - `EVENT_NAME=workflow_run`
    - `EVENT_ACTION=${{ github.event.action }}`
    - `WORKFLOW_RUN_EVENT`
    - `WORKFLOW_RUN_PULL_REQUESTS`
    - `WORKFLOW_RUN_HEAD_BRANCH`
    - `WORKFLOW_RUN_HEAD_REPO_OWNER`
    - repo owner/name and `STATE_ISSUE_NUMBER`
- [x] Update `scripts/reviewer_bot.py` to support workflow-run reconciliation:
  - parse `WORKFLOW_RUN_PULL_REQUESTS`
  - resolve PR number from payload, fallback to head owner+branch lookup
  - reconcile latest assigned reviewer review and mark completion when `APPROVED`
  - allow reconcile call without strict `IS_PULL_REQUEST=true` guard in workflow_run mode
  - record completion source as `workflow_run:pull_request_review`
- [x] Ensure logic remains idempotent (already-completed reviews remain no-op).

## Phase 3 - Tests and Quality Gates

- [x] Add/adjust tests in `.github/reviewer-bot-tests/test_reviewer_bot.py` for:
  - PR number resolution from workflow_run payload
  - fallback PR lookup by head owner/branch
  - approval reconciliation via workflow_run handler
  - non-review workflow_run events ignored
- [x] Run lint fix:
  - `uv run ruff check --fix`
- [x] Run reviewer bot tests:
  - `uv run pytest .github/reviewer-bot-tests`
- [x] Confirm all tests pass and no unexpected file changes remain.

## Phase 4 - Ship the Fix

- [x] Commit with Conventional Commit message, e.g.:
  - `fix(reviewer-bot): auto-reconcile fork PR approvals via workflow_run`
- [x] Push branch:
  - `git push -u origin fix/reviewer-bot-auto-reconcile-fork-pr-approvals`
- [x] Open PR targeting upstream repo explicitly:
  - `gh pr create --repo rustfoundation/safety-critical-rust-coding-guidelines --base main --head PLeVasseur:fix/reviewer-bot-auto-reconcile-fork-pr-approvals ...`
- [x] Include in PR body:
  - root cause (read-only token on fork `pull_request_review`)
  - why workflow_run second hop resolves it
  - test evidence

## Phase 5 - Live Validation (Post-Merge Handoff)

- [ ] Merge the fix PR to `main`.
- [ ] Sync local `main` to merged remote default branch.
- [ ] Create a disposable fork PR with trivial change.
- [ ] Apply `coding guideline` label.
- [ ] Ensure assigned reviewer has claimed the review if needed.
- [ ] **Handoff checkpoint**: tell maintainer exactly `ok, go approve`, then wait for confirmation that approval is submitted.
- [ ] After maintainer confirmation, verify the approval-triggered behavior.
- [ ] Verify two-run behavior:
  - primary `Reviewer Bot` run may still defer in read-only context
  - `Reviewer Bot Reconcile` run executes and persists state
  - Example check command:
    - `gh run list --repo rustfoundation/safety-critical-rust-coding-guidelines --limit 50 --json workflowName,event,displayTitle,url,createdAt | jq -r '.[] | select(.displayTitle | contains("[DO NOT MERGE]")) | "\(.createdAt) | \(.workflowName) | \(.event) | \(.url)"'`
- [ ] Verify state issue `#314` entry for test PR has:
  - `review_completed_at` non-null
  - `review_completed_by` set to assigned reviewer
  - `review_completion_source: workflow_run:pull_request_review`
  - Example check command:
    - `gh api repos/rustfoundation/safety-critical-rust-coding-guidelines/issues/314 --jq '.body' | rg -n "'${TEST_PR}'|review_completed_at|review_completed_by|review_completion_source" -C 4`
- [ ] Verify no manual `@guidelines-bot /rectify` was required.
- [ ] Close disposable test PR without merging.

## Acceptance Criteria

- [ ] Fork PR approval is persisted automatically.
- [ ] Bot state reflects completion after approval in same end-to-end flow.
- [ ] Unit tests and lint checks pass.
- [ ] No regression to existing `/rectify` behavior.
- [ ] Maintainer handoff point was used correctly (`ok, go approve`) during post-merge validation.

## Blockers

- [x] 2026-02-09T21:40:54Z: Blocked at Phase 5 step "Merge the fix PR to `main`". PR `#399` is not mergeable yet (`mergeStateStatus=BLOCKED`, `reviewDecision=REVIEW_REQUIRED`) and needs an approval before merge.

(If a blocker occurs, replace the line above with timestamped notes and mark the impacted step.)
