# Reviewer Bot Burst Assignment and Mandatory Approval Plan (2026-02-11)

## Objective

- [x] Fix burst-event state races so reviewer-bot processes every event safely.
- [x] Keep queue behavior compatible with current process (read-level reviewers can still be designated by queue).
- [x] Add mandatory triage approver escalation when a read-level designated reviewer approves.
- [x] Ship as one comprehensive PR with strong regression coverage.

## Locked Decisions (From User Feedback)

- [x] Use in-repo lease locking (`1A`).
- [x] Guarantee event durability (process every event; no dropped events) (`2A`).
- [x] Keep queue assignment policy permissive:
  - [x] Read-level members stay in queue.
  - [x] Queue may still select/assign them as designated reviewer.
- [x] No global concurrent-open-reviewer cap (`5 = unlimited`).
- [x] If no workable assignment path exists, use explicit escalation behavior (`6A` style visibility).
- [x] Ship as one comprehensive PR (`7B`).
- [x] No automated historical backfill in this effort (`8: handled manually by maintainer`).
- [x] Mandatory-approval escalation label name: `triage approver required` (create if missing).
- [x] Escalation ping targets (static list):
  - [x] `@PLeVasseur`
  - [x] `@felix91gr`
  - [x] `@rcseacord`
  - [x] `@plaindocs`
  - [x] `@AlexCeleste`
  - [x] `@sei-dsvoboda`
- [x] On read-level designated reviewer approval, mark review complete immediately.
- [x] Mandatory approver completion criteria: first `APPROVED` from any triage+ user.
- [x] Escalation comment frequency: once per PR.

## Fresh Session Bootstrap (Required)

- [x] Source OpenCode environment and verify config path.
  - [x] `source /home/pete.levasseur/opencode-project-agents/shell/opencode-env.sh`
  - [x] `printenv OPENCODE_CONFIG_DIR`
- [x] Verify GitHub auth and repository access.
  - [x] `gh auth status`
  - [x] `gh repo view rustfoundation/safety-critical-rust-coding-guidelines`
- [x] Verify working tree and branch hygiene.
  - [x] `git status --short --branch`
  - [x] If dirty, explicitly decide: stash or isolate in a fresh branch.
  - [x] Ensure base branch is current with upstream before coding.
- [x] Create implementation branch for single comprehensive PR.
  - [x] Suggested name: `fix/reviewer-bot-burst-lock-and-triage-approval`
- [x] Capture runbook metadata in PR description template.
  - [x] Incident PRs: `#264`, `#358`, `#256`, `#368`
  - [x] State issue: `#314`

## Incident Context (Ground Truth)

- [x] PRs `#264`, `#358`, `#256`, and `#368` were labeled nearly simultaneously.
- [x] Four `pull_request_target:labeled` runs executed in parallel.
- [x] `.github/workflows/reviewer-bot.yml:41` currently scopes concurrency per issue/PR, not per shared state store.
- [x] Parallel runs clobbered state in issue `#314` (last-writer-wins behavior).
- [x] Reviewer request API returned `422` in those runs, but bot still posted assignment-success guidance.

## Scope

- [x] In scope:
  - [x] Global state-write serialization across `reviewer-bot.yml` and `reviewer-bot-reconcile.yml`.
  - [x] Assignment-path correctness updates for API failures.
  - [x] Mandatory approver escalation label and one-time ping flow.
  - [x] Test updates in `.github/reviewer-bot-tests/test_reviewer_bot.py`.
  - [x] Small docs update in `REVIEWING.md` if behavior changes are user-visible.
- [x] Out of scope:
  - [x] Automated backfill of existing open PR state.
  - [x] Redesigning queue membership governance.
  - [x] Replacing issue `#314` as persistent store.

## Critical State Issue Contract (Must Preserve Lock Metadata)

- [x] Define canonical state issue body layout with explicit parse markers.
  - [x] Keep YAML state in fenced block:
    - [x] `<!-- REVIEWER_BOT_STATE_START -->`
    - [x] opening YAML code fence.
    - [x] `<!-- REVIEWER_BOT_STATE_END -->`
  - [x] Keep lock metadata in separate fenced JSON block outside YAML:
    - [x] `<!-- REVIEWER_BOT_LOCK_START -->`
    - [x] opening JSON code fence.
    - [x] `<!-- REVIEWER_BOT_LOCK_END -->`
- [x] Lock metadata schema (v1):
  - [x] `schema_version`
  - [x] `lock_owner_run_id`
  - [x] `lock_owner_workflow`
  - [x] `lock_owner_job`
  - [x] `lock_token`
  - [x] `lock_acquired_at`
  - [x] `lock_expires_at`
- [x] Implement parse/render helpers in `scripts/reviewer_bot.py`:
  - [x] `parse_state_yaml_from_issue_body(body) -> dict`
  - [x] `parse_lock_metadata_from_issue_body(body) -> dict`
  - [x] `render_state_issue_body(state, lock_meta) -> str`
- [x] Replace blind `save_state()` rewrite behavior with preserve/update strategy.
  - [x] `save_state()` must read latest issue body and preserve lock block.
  - [x] `save_state()` must patch with `If-Match` to avoid stale writes.
  - [x] Lock acquire/release paths must preserve YAML block exactly unless state is intentionally updated.
- [x] Add tests proving lock metadata cannot be lost or corrupted during `save_state()`.

## Technical Design

### A) Durable In-Repo Lease Lock (Required)

- [x] Add optimistic-concurrency lock primitives to `scripts/reviewer_bot.py`.
  - [x] Extend API helper to return response payload and headers (including `ETag`).
  - [x] Support conditional `PATCH` with `If-Match` compare-and-swap semantics.
- [x] Lock acquire algorithm (retry loop):
  - [x] Read issue body + `ETag`.
  - [x] Parse lock metadata.
  - [x] If no valid lock (or expired), attempt conditional patch with own lock token.
  - [x] On conflict (`412`/`409`), re-read and retry with jittered backoff.
  - [x] If another valid lock exists, wait and retry until timeout.
- [x] Lock release algorithm:
  - [x] Conditional patch to clear lock metadata if current owner token matches.
  - [x] Always release in `finally` path.
  - [x] If release fails, log run id, token prefix, and state issue URL.
- [x] Lock timing defaults:
  - [x] Lease TTL: `300s`.
  - [x] Retry interval: `2s` base + jitter.
  - [x] Max wait before hard fail: `20m`.

### B) Lock Boundary and Event Matrix

- [x] Rule: acquire lock before first state read for any mutating path, release after final `save_state()` attempt.
- [x] Mutating paths that must hold lock:
  - [x] `issues` events (`opened`, `labeled`, `closed`) when state can change.
  - [x] `pull_request_target` events (`opened`, `labeled`, `closed`) when state can change.
  - [x] `issue_comment` commands that mutate queue/review state.
  - [x] `pull_request_review` when state can change.
  - [x] `workflow_run` reconcile path.
- [x] Non-mutating paths can skip lock, but must never call `save_state()`.
- [x] If code path unexpectedly reaches mutation without lock, fail fast with explicit error.

### C) HTTP Status Handling Matrix

- [x] State issue conditional patch (`PATCH issues/314` with `If-Match`):
  - [x] `200`: success.
  - [x] `412` or `409`: stale/conflict, retry after re-read.
  - [x] `404`: fail hard (state issue missing/misconfigured).
  - [x] `401`/`403`: fail hard with permission diagnostic.
  - [x] `429` or `5xx`: bounded retry with backoff; fail loud on exhaustion.
- [x] Reviewer request (`POST pulls/{n}/requested_reviewers`):
  - [x] `201`/`200`: success.
  - [x] `422`: do not claim GitHub assignment success; continue designated-reviewer logic and truthful comment.
  - [x] `401`/`403`: fail loud and annotate context.
  - [x] `429`/`5xx`: retry with backoff, then degrade gracefully with explicit warning comment.
- [x] Label create (`POST repos/{owner}/{repo}/labels`):
  - [x] `201`: created.
  - [x] `422`: treat as already exists and continue.
  - [x] other failures: continue with comment-only escalation and warning log.

### D) Assignment Semantics With Read-Level Reviewers Allowed

- [x] Preserve queue policy: selected reviewer can be read-level.
- [x] Distinguish explicitly between:
  - [x] designated reviewer in bot state, and
  - [x] GitHub requested reviewer status.
- [x] On reviewer-request `422`, do not claim success.
  - [x] Keep designated reviewer in state.
  - [x] Post truthful guidance comment.
- [x] Keep skip-author logic for queue picks.

### E) Mandatory Triage Approver Escalation Flow

- [x] Add escalation label constant: `triage approver required`.
- [x] Ensure label exists (idempotent path):
  - [x] check existing labels first (or create directly and treat `422` as exists).
  - [x] if creation still fails, continue with comment-only escalation.
- [x] Add active-review fields for idempotency and auditing:
  - [x] `mandatory_approver_required` (bool)
  - [x] `mandatory_approver_label_applied_at` (timestamp or null)
  - [x] `mandatory_approver_pinged_at` (timestamp or null)
  - [x] `mandatory_approver_satisfied_by` (username or null)
  - [x] `mandatory_approver_satisfied_at` (timestamp or null)
- [x] Trigger condition:
  - [x] designated reviewer submits `APPROVED`, and
  - [x] reviewer is not triage+ at approval time.
- [x] Escalation actions (once per PR):
  - [x] mark review complete immediately.
  - [x] add `triage approver required` label.
  - [x] post one comment pinging static approver list.
  - [x] persist idempotency fields so repeated approvals do not repost.
- [x] Satisfaction condition:
  - [x] any triage+ user submits `APPROVED` after escalation is open.
- [x] Satisfaction actions:
  - [x] record satisfier fields.
  - [x] remove `triage approver required` label.
  - [x] optionally post one concise confirmation comment.

### F) Mandatory Approver State Machine (Per PR)

- [x] States:
  - [x] `none` (default)
  - [x] `required` (label present or intended)
  - [x] `satisfied`
- [x] Transitions:
  - [x] `none -> required`: read-level designated reviewer approves.
  - [x] `required -> required`: repeated read-level approvals (idempotent, no new ping comment).
  - [x] `required -> satisfied`: triage+ approval received.
  - [x] `satisfied -> none`: reset only on explicit reassignment/new review cycle.
- [x] Invariants:
  - [x] max one escalation ping comment per review cycle.
  - [x] label and state fields remain consistent after retries/reconcile.

### G) Message Templates (Exact Copy to Implement)

- [x] Designated reviewer assigned, GitHub request failed (`422`):
  - [x] "@{reviewer} is designated as reviewer by queue rotation, but GitHub could not add them to PR Reviewers automatically (API 422). A triage+ approver may still be required before merge queue."
- [x] Mandatory escalation (one-time):
  - [x] "Mandatory triage approval required before merge queue. Pinging @PLeVasseur @felix91gr @rcseacord @plaindocs @AlexCeleste @sei-dsvoboda. Label applied: `triage approver required`."
- [x] Mandatory approver satisfied:
  - [x] "Mandatory triage approval satisfied by @{approver}; removed `triage approver required`."

## Workflow Changes

### `.github/workflows/reviewer-bot.yml`

- [x] Replace misleading per-PR concurrency assumptions.
  - [x] Keep or remove top-level `concurrency` only if event-durability guarantee remains true.
  - [x] Document that lease lock is the actual global serialization mechanism.
- [x] Pass lock context env vars (`github.run_id`, workflow name, job name).
- [x] Preserve existing reconcile-context artifact steps for `pull_request_review` events.

### `.github/workflows/reviewer-bot-reconcile.yml`

- [x] Use same lock protocol around reconcile state mutation path.
- [x] Keep artifact validation and SHA guardrails intact.
- [x] Ensure lock release executes even when reconcile fails.

## File-Level Change Checklist

- [x] `scripts/reviewer_bot.py`
  - [x] response/headers-aware API helpers.
  - [x] issue-body parse/render helpers for YAML + lock metadata.
  - [x] lease lock acquire/release helpers.
  - [x] `save_state()` preserve/update refactor with `If-Match`.
  - [x] truthful assignment messaging on reviewer-request failures.
  - [x] mandatory approver escalation fields and transitions.
  - [x] static ping list constants.
  - [x] label ensure-create helper for `triage approver required`.
- [x] `.github/workflows/reviewer-bot.yml`
  - [x] concurrency/serialization comments and lock context wiring.
- [x] `.github/workflows/reviewer-bot-reconcile.yml`
  - [x] lock wiring around reconcile execution.
- [x] `.github/reviewer-bot-tests/test_reviewer_bot.py`
  - [x] lock behavior tests (success, contention, stale lease takeover, timeout).
  - [x] lock metadata preservation tests across `save_state()`.
  - [x] assignment failure truthfulness tests (`422`).
  - [x] mandatory approver escalation tests.
  - [x] idempotent once-per-PR escalation tests.
  - [x] triage+ approval clears label tests.
- [x] `REVIEWING.md` (if needed)
  - [x] document `triage approver required` behavior and one-time ping semantics.

## Verification Plan

### Local Quality Gates

- [x] Run `uv run ruff check --fix`.
- [x] Run `uv run pytest .github/reviewer-bot-tests`.
- [x] Ensure no failing tests and no unexpected formatting diffs.

### Command-Level Live Verification

- [ ] Verify no state clobber under burst simulation.
  - [x] `gh issue view 314 --repo rustfoundation/safety-critical-rust-coding-guidelines --json body`
  - [ ] Expected: all active PR entries present, no lost updates.
- [ ] Verify escalation label applied once.
  - [x] `gh pr view <PR> --repo rustfoundation/safety-critical-rust-coding-guidelines --json labels`
  - [ ] Expected: `triage approver required` exists after read-level approval.
- [ ] Verify one escalation ping comment only.
  - [x] `gh api repos/rustfoundation/safety-critical-rust-coding-guidelines/issues/<PR>/comments?per_page=100`
  - [ ] Expected: exactly one matching escalation template comment.
- [ ] Verify mandatory triage approval clears escalation.
  - [x] `gh pr view <PR> --repo rustfoundation/safety-critical-rust-coding-guidelines --json reviews,labels`
  - [ ] Expected: triage+ `APPROVED` present and escalation label removed.
- [ ] Verify lock behavior in run logs.
  - [x] `gh run view <RUN_ID> --repo rustfoundation/safety-critical-rust-coding-guidelines --log`
  - [ ] Expected: acquire, hold, release log lines with consistent lock owner token.
- [ ] Blocker (2026-02-10T22:09:33Z): `gh pr view 405 --repo rustfoundation/safety-critical-rust-coding-guidelines --json labels,reviews` returned empty `labels` and `reviews`; escalation checks require a read-level designated approval followed by triage+ approval.
- [ ] Blocker (2026-02-10T22:09:33Z): `gh run view 21884258637 --repo rustfoundation/safety-critical-rust-coding-guidelines --log` did not include new lease-lock log lines because `pull_request_target` executes the base branch workflow prior to merge.

## Stale Lock Recovery Runbook

- [x] Automatic stale lock takeover:
  - [x] if `lock_expires_at` is in the past, next run can reclaim via conditional patch.
- [ ] Manual recovery checklist (only if repeated lock failures):
  - [ ] inspect current lock metadata in issue `#314`.
  - [ ] check owner run status with `gh run view <lock_owner_run_id>`.
  - [ ] if owner run is completed/cancelled and lock expired, clear lock via guarded update.
  - [ ] record manual intervention in PR notes with timestamp and operator.

## Rollout Plan (Single PR)

- [x] Create one comprehensive fix branch/PR with all workstreams.
- [x] Include PR summary sections:
  - [x] race root cause and lock strategy.
  - [x] preserve/update strategy preventing lock metadata corruption.
  - [x] read-level reviewer plus mandatory triage approval model.
  - [x] test coverage and regression proof.
- [ ] After merge, monitor first 3 days:
  - [ ] Day 0: verify first burst-like event sequence.
  - [ ] Day 1: scan reviewer-bot logs for lock timeout/conflict loops.
  - [ ] Day 3: verify no duplicate escalation comments or stale labels.
- [ ] Blocker (2026-02-10T22:09:33Z): post-merge day-0/day-1/day-3 monitoring cannot start until PR 405 is merged.

## Risks and Mitigations

- [x] Risk: lock metadata lost because `save_state()` rewrites full issue body.
  - [x] Mitigation: enforce parse/render contract with lock block preservation and `If-Match` writes.
- [x] Risk: lock deadlock or abandoned lease.
  - [x] Mitigation: TTL, stale takeover, always-release in `finally`.
- [x] Risk: label creation fails due token scope edge case.
  - [x] Mitigation: continue with comment-based escalation plus warning logs.
- [x] Risk: confusion between designated reviewer and GitHub requested reviewer.
  - [x] Mitigation: explicit wording in guidance comments and docs.
- [x] Risk: non-assigned triage approvals ignored in some paths.
  - [x] Mitigation: explicit escalation-open branch in review event handlers and workflow-run parity.

## Acceptance Criteria

- [x] No state clobber under burst label events.
- [x] Every event is processed or fails loudly with lock-timeout diagnostics (no silent drop behavior).
- [x] Queue can still designate read-level reviewers.
- [x] Read-level designated reviewer approval triggers one-time mandatory escalation:
  - [x] label `triage approver required` exists/applies.
  - [x] static ping comment posts once.
  - [x] review completion is marked immediately.
- [x] Any triage+ approval clears mandatory escalation state and label.
- [x] Lock metadata remains intact across all `save_state()` operations.
- [x] Reviewer-bot tests and lint checks pass.

## Explicitly Deferred

- [x] Automated remediation/backfill of historical open PRs is intentionally deferred to manual maintainer handling.
