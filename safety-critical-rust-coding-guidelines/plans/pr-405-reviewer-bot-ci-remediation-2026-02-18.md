# PR #405 Reviewer Bot CI Failure: Diagnosis and Remediation Plan

Date: 2026-02-18
PR: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/405

## What failed

- The required `reviewer-bot` check failed on run `22077620805` (event: `pull_request_review`, action: `submitted`).
- Other required checks were green; the failure was isolated to reviewer-bot.

## Diagnosis and evidence

### Observed error

From failed job logs:

```
ERROR: Unexpected status while acquiring reviewer-bot lease lock (status 400):
{"message":"Bad Request", ... "errors":["Conditional request headers are not allowed in unsafe requests unless supported by the endpoint"],"status":"400"}
```

### Why this happens

1. The hardening in PR #405 added lease lock acquisition before event handling in `main()`.
2. Lease acquisition uses `PATCH /issues/{STATE_ISSUE_NUMBER}` with `If-Match` (`conditional_patch_state_issue`).
3. GitHub REST rejects conditional headers on unsafe methods for this endpoint (unless explicitly supported), returning HTTP 400.
4. For this specific run, the event is a cross-repo PR review (`PR_IS_CROSS_REPOSITORY=true`) and should be deferred, but deferral is inside `handle_pull_request_review_event()`.
5. Because lock acquisition runs first, execution fails before deferral logic is reached.

### Secondary effect

- The reconcile handoff artifact step only runs on success; because the first workflow fails, `Reviewer Bot Reconcile` never triggers.

## Root cause

The new lock path assumes optimistic concurrency via `If-Match` on Issue PATCH. That assumption is invalid for this endpoint in GitHub REST. The failure is deterministic for any lock attempt, including the cross-repo review path that should have remained non-mutating.

## Unblock plan (fast, low-risk)

### Goal

Restore green CI for PR review events without weakening the intended cross-repo safety model.

### Recommended unblock changes

1. **Skip lease lock for cross-repo `pull_request_review/submitted` at top-level routing.**
   - In `main()` (or `event_requires_lease_lock`), compute whether the event is cross-repo review (`PR_IS_CROSS_REPOSITORY=true`) and do not acquire lock for that path.
   - Preserve existing handler behavior that defers with a message and returns without state mutation.
2. **Keep lock for all truly mutating paths** (`issues`, `pull_request_target`, `issue_comment`, `workflow_dispatch`, `schedule`, trusted `workflow_run`).
3. **Add regression test coverage for top-level lock gating.**
   - Assert `main()` does not call `acquire_state_issue_lease_lock` for cross-repo review submit events.
   - Assert no failure exit when handler defers.

### Acceptance criteria for unblock

- `reviewer-bot` workflow succeeds for cross-repo PR review submissions.
- `reviewer-bot` still acquires/release lock for mutating events.
- Existing reconcile and review-state tests remain green.
- Targeted runbook verification on PR #405 re-run shows the failure is gone.

## Follow-up hardening plan

### Objective

Keep state serialization hardening, but replace unsupported conditional-write assumptions with a lock approach compatible with GitHub APIs.

### Work items

1. **Replace `If-Match` issue PATCH locking with API-supported coordination primitive.**
   Candidate directions (evaluate and pick one):
   - **Workflow-level global concurrency group** for reviewer-bot state mutators (simple and robust).
   - **External lock record using API semantics that support safe compare/update behavior** (if available and justified).
2. **Separate lock policy by event mutability.**
   - Non-mutating/deferred paths must never require lock acquisition.
   - Mutating paths must fail closed if lock cannot be acquired.
3. **Harden lock telemetry and diagnostics.**
   - Emit explicit logs for lock required/skip decision.
   - Include event type, mutating decision, and lock strategy version in logs.
4. **Expand test matrix for CI parity.**
   - Add tests covering top-level event routing + lock gating.
   - Add tests simulating 400 from unsupported conditional headers (to prevent regression if code is reintroduced).
5. **Add an operational fallback.**
   - If lock backend fails, non-mutating paths should continue; mutating paths should fail with actionable error and recovery guidance.

### Follow-up acceptance criteria

- No use of unsupported conditional headers on unsafe Issue/Pull APIs.
- Concurrency behavior is explicit, tested, and documented.
- Cross-repo review flows cannot deadlock/fail pre-handler.
- Reviewer-bot required check remains stable across fork and same-repo events.

## Validation checklist

1. `uv run pytest .github/reviewer-bot-tests/test_reviewer_bot.py`
2. Manual/local simulation for:
   - `pull_request_review/submitted` with `PR_IS_CROSS_REPOSITORY=true`
   - `pull_request_target/opened` mutating flow
   - `workflow_run/completed` reconcile flow
3. Re-run failed check on PR #405 and confirm green status.

## Notes

- This unblock intentionally minimizes behavior change: it restores pre-hardening behavior for cross-repo review submissions while preserving hard-fail semantics on mutating paths.
- Follow-up hardening should be delivered as a separate PR to reduce rollout risk and keep diagnosis/remediation auditable.
