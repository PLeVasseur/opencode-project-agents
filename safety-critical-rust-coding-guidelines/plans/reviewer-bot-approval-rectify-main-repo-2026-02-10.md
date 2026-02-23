# Plan: One-Shot `/rectify` Rollout, Then Full Validation (Main Repo)

## Pre-Flight (Mandatory, Must Be Checked Off)

- [x] **Mandate acknowledged:** every checklist item in this plan must be checked off as it is completed; do not batch-check at the end.
- [x] **Stop condition acknowledged:** do not begin implementation until all pre-flight items below are checked off.
- [x] **Branch/PR isolation acknowledged:** each piece of work (PR1, PR1b if needed, PR2) must use its own new branch and its own PR.
- [x] **Base source acknowledged:** every branch must be created from `upstream/main` (never `origin/main`, even if SHAs currently match).
- [x] Verify upstream base setup for all branch creation:
  - [x] Run: `git remote -v | rg "^upstream\s+.*rustfoundation/safety-critical-rust-coding-guidelines"`
  - [x] Run: `git fetch upstream main`
  - [x] Run: `git rev-parse upstream/main`
  - [x] Confirm: upstream remote exists for the canonical repository and the recorded base SHA for all work comes from `upstream/main`.
- [x] Verify canonical broken PR context (`#302`):
  - [x] Run: `gh pr view 302 --repo rustfoundation/safety-critical-rust-coding-guidelines --json isCrossRepository,reviews,reviewRequests`
  - [x] Confirm: assigned reviewer has an `APPROVED` review, but review state is still stuck.
- [x] Verify prior fix attempt context (`#391`):
  - [x] Run: `gh pr view 391 --repo rustfoundation/safety-critical-rust-coding-guidelines --json number,title,state,mergedAt`
  - [x] Confirm: this was merged but did not resolve stuck state for `#302`.
- [x] Verify current state issue evidence (`#314`):
  - [x] Run: `gh issue view 314 --repo rustfoundation/safety-critical-rust-coding-guidelines --json body,updatedAt`
  - [x] Confirm: `active_reviews['302']` lacks completion fields before rollout.
- [x] Verify failing run signature (review-event persistence failure):
  - [x] Run: `gh run view 21722921588 --repo rustfoundation/safety-critical-rust-coding-guidelines --log | rg "GITHUB_TOKEN Permissions|Issues:|PullRequests:|Contents:|Resource not accessible|Failed to save state|Marked review complete"`
  - [x] Confirm: read-only permissions on this run and `403` save failure.
- [x] Verify control run signature (comment-event write path):
  - [x] Run: `gh run view 21725270603 --repo rustfoundation/safety-critical-rust-coding-guidelines --log | rg "GITHUB_TOKEN Permissions|Issues:|PullRequests:|Contents:"`
  - [x] Confirm: `issue_comment` path has write permissions.
- [x] Gate-1 criteria acknowledged before coding:
  - [x] After **user confirms PR1 is merged**, post `@guidelines-bot /rectify` on PR `#302`.
  - [x] Verify bot reactions and success response.
  - [x] Verify `#314` updates `active_reviews['302']` completion fields.

## Context and Evidence

- [x] Primary stuck case: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/302
- [x] Prior attempt: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/391
- [x] State issue: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/314
- [x] Confirmed failure mode to eliminate:
  - [x] `pull_request_review` run for PR #302 processed approval in memory.
  - [x] Save to issue #314 failed with `403 Resource not accessible by integration`.
  - [x] Workflow still reported success, leaving state stale.

## Strategy (Gated)

- [ ] **PR1 (must pass first):** ship only what is needed so `/rectify` works immediately on real stuck PRs.
- [ ] **Gate 1:** user merges PR1, then run `/rectify` on PR #302 and verify state fixed.
- [ ] **PR2 (follow-up):** broader automation + dummy issue/PR validation after `/rectify` is proven.
- [ ] **Branching rule for all pieces:**
  - [x] PR1 uses a fresh branch from current `upstream/main`.
  - [ ] PR1b (if needed) uses a different fresh branch from current `upstream/main` (never reuse PR1 branch).
  - [ ] PR2 uses a fresh branch from latest `upstream/main` after PR1 merge confirmation.

## Scope Guardrails

- [x] Keep implementation in `scripts/reviewer_bot.py`, `.github/workflows/reviewer-bot.yml`, and reviewer-bot tests.
- [ ] Do all live validation against `rustfoundation/safety-critical-rust-coding-guidelines`.
- [x] Preserve assignment/fairness semantics; only change completion/reconciliation reliability.
- [x] Do not add typo aliases (only official command: `/rectify`).
- [x] **Merge policy:** assistant opens/updates PRs only; assistant never merges to `main`; wait for user to merge and confirm before post-merge steps.

## Branch / PR Base Checks (Mandatory For Each Piece)

- [x] Before creating each work branch (PR1, PR1b if needed, PR2), record current `upstream/main` SHA:
  - [x] Run: `git fetch upstream main && git rev-parse upstream/main`
- [x] Create the piece branch directly from `upstream/main`:
  - [x] Run: `git checkout -b <piece-branch-name> upstream/main`
  - [x] Run: `git rev-parse HEAD`
  - [x] Confirm: branch-start `HEAD` equals the recorded `upstream/main` SHA.
- [x] Before opening each PR, verify branch ancestry is based on upstream main:
  - [x] Run: `git merge-base --is-ancestor upstream/main HEAD`
  - [x] Confirm: command exits `0`.
- [x] Open one PR per piece branch (no multi-piece branch/PR).

## PR1 Implementation Checklist (Rectify First)

### A) Command surface

- [x] Add `rectify` to command registry/help output.
- [x] Parse and route `@guidelines-bot /rectify` in `handle_comment_event`.
- [x] Keep behavior single-target in PR1:
  - [x] On an issue/PR comment, reconcile that issue/PR only.
  - [x] Do not add global state-issue reconcile path in PR1.

### B) Rectify reconciliation engine

- [x] Add helper to reconcile one active review entry by issue/PR number.
- [x] Resolve assigned reviewer from `active_reviews[issue].current_reviewer`.
- [x] For PR targets, fetch reviews from GitHub API and pick latest review by assigned reviewer.
- [x] Apply transitions:
  - [x] Latest `APPROVED` -> set `review_completed_at`, `review_completed_by`, `review_completion_source`.
  - [x] Latest `COMMENTED` -> update `last_reviewer_activity` and clear warning.
  - [x] Latest `CHANGES_REQUESTED` -> update `last_reviewer_activity` and clear warning.
  - [x] No matching assigned-reviewer review -> no-op with explicit reason.
- [x] Make rectify idempotent (re-running after completion is a no-op).

### C) Permission model for `/rectify`

- [x] Allow if comment author is current assigned reviewer.
- [x] Allow if comment author has triage+ permission.
- [x] Deny otherwise with explicit message.

### D) Silent-failure hardening

- [x] Ensure mutating flows do not silently pass when `save_state(...)` fails.
- [x] Update `main` save block to treat persistence failure as failure (non-zero exit).
- [x] Add explicit log lines for deferred/non-writable scenarios.

### E) Pull-request-review handling safety

- [x] Add env context to detect cross-repo PR review events.
- [x] For cross-repo `pull_request_review`, do not rely on immediate persistence path.
- [x] Log clear deferral message instructing maintainers to use `/rectify`.

## PR1 Test Plan (Extensive but Focused)

- [x] Add tests for command parsing/routing of `/rectify`.
- [x] Add tests for `/rectify` permission checks:
  - [x] assigned reviewer allowed.
  - [x] triage+ allowed.
  - [x] unauthorized user denied.
- [x] Add tests for rectify outcomes:
  - [x] assigned reviewer latest review `APPROVED` marks complete.
  - [x] assigned reviewer latest review `COMMENTED` updates activity.
  - [x] assigned reviewer latest review `CHANGES_REQUESTED` updates activity.
  - [x] non-assigned reviewer reviews ignored.
  - [x] already-completed entry is idempotent no-op.
  - [x] missing active review entry returns clear no-op/error message.
- [x] Add test for persistence failure path (mutation + failed save => failure, not silent success).
- [x] Run and pass:
  - [x] `uv run ruff check --fix`
  - [x] `uv run pytest .github/reviewer-bot-tests`
  - [x] `uv run pytest .github/guideline-from-issue-tests`
  - [x] `uv run pytest`

## Gate 1 Rollout and Real-Case Verification (No Dummy Artifacts Yet)

- [x] Create PR1 branch from recorded current `upstream/main` and capture the branch-base evidence from the mandatory base checks.
- [x] Open PR1 with only `/rectify` + hardening scope.
- [x] Post PR1 URL with scope summary and test evidence.
- [x] **STOP and wait for user feedback and merge.**
- [ ] **User merges PR1 to `main` and confirms merge in chat.**
- [ ] After user confirmation, immediately comment on PR #302 with `@guidelines-bot /rectify`.
- [ ] Verify the command comment gets bot reactions (`eyes` and `+1`) and success response.
- [ ] Verify `#314` now contains completion data for `'302'`:
  - [ ] `review_completed_at` is populated.
  - [ ] `review_completed_by` is `Dillonmcewan`.
  - [ ] `review_completion_source` references rectify/reconcile path.
- [ ] Trigger manual overdue check (`workflow_dispatch` with `check-overdue`) and confirm no reminder for #302.
- [ ] If Gate 1 fails, create a **new** PR1b branch from current `upstream/main`, open PR1b immediately (same scope only), share evidence, and repeat the same user-merge gate until passing.

## PR2 Follow-Up (After `/rectify` Proven)

### A) Broader reconciliation automation

- [ ] Add `workflow_dispatch` action for global reconciliation (for example `rectify-all`).
- [ ] Run reconciliation before overdue checks in scheduled path.
- [ ] Add summary logging of changed/no-op/error counts for global runs.
- [ ] Create PR2 branch from latest `upstream/main` after PR1 merge confirmation.
- [ ] Open PR2 from that branch and share URL + evidence.
- [ ] **STOP and wait for user feedback and merge.**
- [ ] **User merges PR2 to `main` and confirms merge in chat** before any post-merge validation.

### B) Main-repo dummy validation

- [ ] Create dummy issue with review label and validate assignment lifecycle.
- [ ] Create dummy PR with trivial change and validate activity updates.
- [ ] Use `/rectify` on dummy PR to confirm on-demand repair/no-op behavior.
- [ ] Create cross-repo dummy PR path to mirror real failure mode.
- [ ] Friend-assisted step:
  - [ ] Have friend claim/review/approve once on dummy PR.
  - [ ] Confirm assigned-reviewer approval is represented correctly in state.

## Definition of Done

- [ ] Gate 1 passes on real stuck PR #302 immediately after **user merges PR1**.
- [ ] `/rectify` is reliable and operator-friendly for targeted remediation.
- [ ] State persistence failures are no longer silent.
- [ ] PR2 completes with dummy-flow evidence and friend-assisted approval evidence.
