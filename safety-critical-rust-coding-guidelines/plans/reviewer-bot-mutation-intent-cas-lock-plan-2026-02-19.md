# Reviewer Bot Mutation-Intent + CAS Lock Plan (2026-02-19)

## Objective

Eliminate reviewer-bot state data races while preserving fork-PR approval handling, by:

1. Locking only when a code path can mutate state.
2. Replacing unsupported issue `If-Match` lease writes with a real compare-and-swap lock backend.
3. Ensuring mutating events are serialized and processed safely across both workflows.

## Why this plan is needed

- Current lock path uses issue `PATCH` with `If-Match`, which fails with HTTP 400 on GitHub for this endpoint.
- Lock acquisition currently happens before event-specific deferral logic, so fork `pull_request_review` runs fail too early.
- First-hop/second-hop architecture is correct, but lock backend and lock timing are wrong.

## Required guarantees

- No concurrent mutation of reviewer state issue `#314`.
- Cross-repo first-hop review runs remain non-mutating and successful.
- Trusted second-hop reconcile performs all needed writes under lock.
- Mutating runs fail closed on lock/save failures.
- Event handling converges correctly even under bursts/races.

## Non-goals

- Replacing issue `#314` as the state store.
- Reworking queue fairness or reviewer selection semantics.
- Replacing the existing artifact handshake for second-hop reconcile.

## Execution discipline

- [x] Plan file created in `$OPENCODE_CONFIG_DIR/plans/`.
- [ ] Check off items immediately when completed (no batch check-offs).
- [ ] If blocked, add a timestamped note under "Blockers" and stop at that step.
- [ ] Use `uv run` for all Python/test/lint commands.

## Phase 0 - Baseline capture and preflight

- [ ] Source env and verify config dir:
  - `source /home/pete.levasseur/opencode-project-agents/shell/opencode-env.sh`
  - `printenv OPENCODE_CONFIG_DIR`
- [ ] Record branch/worktree state:
  - `git status --short --branch`
- [ ] Capture failing reference run details (PR #405 current failure).
- [ ] Confirm baseline tests pass before changes:
  - `uv run pytest .github/reviewer-bot-tests/test_reviewer_bot.py -k "cross_repo or workflow_run"`

## Phase 1 - Design freeze (mutation intent + lock contract)

### 1A) Mutation-intent policy

- [ ] Add a central classifier (for example, `classify_mutation_intent`) that returns one of:
  - `mutating`
  - `non_mutating_defer`
  - `non_mutating_readonly`
- [ ] Lock policy decision rule:
  - acquire lock only for `mutating`
  - never acquire lock for non-mutating intents

### 1B) Event-to-intent matrix (authoritative)

- [ ] Freeze and document matrix in code comments/tests:

| Event | Action | Context | Intent |
|---|---|---|---|
| `issues` | `opened/labeled/closed` | any | `mutating` |
| `pull_request_target` | `opened/labeled/closed` | any | `mutating` |
| `pull_request_review` | `submitted` | `PR_IS_CROSS_REPOSITORY=true` | `non_mutating_defer` |
| `pull_request_review` | `submitted` | same-repo PR | `mutating` |
| `issue_comment` | `created` | command/activity path | `mutating` |
| `workflow_run` | `completed` + source `pull_request_review` | trusted reconcile | `mutating` |
| `workflow_dispatch` | `show-state` | read-only | `non_mutating_readonly` |
| `workflow_dispatch` | `sync-members/check-overdue` | mutating paths | `mutating` |
| `schedule` | nightly | any | `mutating` |

- [ ] Add explicit logs at start of each run:
  - event/action/context
  - computed intent
  - lock required (`true/false`)

### 1C) Lock backend contract

- [ ] Define lock API boundary in script:
  - `acquire_state_lock()`
  - `release_state_lock()`
  - `assert_lock_held()`
  - `ensure_lock_fresh()` (if TTL near expiry)
- [ ] Lock ownership identity fields:
  - `run_id`, `workflow`, `job`, `token`, `acquired_at`, `expires_at`

## Phase 2 - Implement Git-ref CAS lock backend

### 2A) Storage primitive

- [ ] Use dedicated lock ref (for example `refs/heads/reviewer-bot-state-lock`).
- [ ] Represent lock state in lock-commit message (v1 schema), with fields:
  - `schema_version`
  - `state` (`locked` or `unlocked`)
  - `lock_token`
  - `owner_run_id`
  - `owner_workflow`
  - `owner_job`
  - `acquired_at`
  - `expires_at`

### 2B) Acquire algorithm (CAS)

- [ ] Read lock ref head SHA.
- [ ] Parse current lock record from head commit message.
- [ ] If lock valid and owned by another run, wait + retry with jitter.
- [ ] If lock absent/expired/unlocked, create candidate `locked` commit with parent=head.
- [ ] Advance lock ref via `PATCH git/refs/...` with `force=false`.
- [ ] On 409/422 conflict, retry (another run won).
- [ ] On timeout, fail closed with actionable error.

### 2C) Release algorithm

- [ ] Re-read lock ref and verify current owner token matches active context.
- [ ] Append `unlocked` commit and CAS-update ref (`force=false`).
- [ ] Retry conflict/rate-limit errors with bounded backoff.
- [ ] If token mismatch, fail release loudly (do not clobber another owner).

### 2D) Lease freshness/TTL

- [ ] Set sane default TTL (for example 15 minutes) and max wait.
- [ ] Before save/final mutation commit, ensure remaining TTL is above threshold.
- [ ] If near expiry, append renewal lock commit under CAS.

### 2E) Remove broken conditional-write usage

- [ ] Remove lock dependence on `If-Match` issue PATCH.
- [ ] Ensure `save_state` writes issue body under lock without unsupported conditional headers.

## Phase 3 - Main flow integration

- [ ] Refactor `main()` to:
  - compute intent first
  - acquire lock only for `mutating`
  - skip lock for defer/read-only intents
- [ ] Keep fail-closed guard: mutation cannot reach `save_state` without lock.
- [ ] Ensure cross-repo `pull_request_review/submitted` returns success + deferral log (no mutation attempt).
- [ ] Ensure same-repo review path remains mutating + locked.
- [ ] Ensure `workflow_run` reconcile path remains mutating + locked.

## Phase 4 - Workflow and permission updates

### 4A) Permissions

- [ ] Keep `reviewer-bot.yml` with write-capable permissions needed for lock/state updates.
- [ ] Update `.github/workflows/reviewer-bot-reconcile.yml` to include `contents: write` (needed for lock ref CAS updates).

### 4B) Concurrency semantics (important)

- [ ] Review current workflow-level `concurrency` behavior and remove/adjust settings that can drop pending events.
- [ ] Prefer lock-based serialization over workflow pending-run replacement.
- [ ] Document final event-processing semantics clearly in workflow comments.

## Phase 5 - Test plan (comprehensive)

### 5A) Unit tests: intent routing

- [ ] Add tests for each matrix row in Phase 1B.
- [ ] Add explicit regression test: cross-repo review submit does **not** call lock acquire.
- [ ] Add test: same-repo review submit **does** call lock acquire.

### 5B) Unit tests: lock backend

- [ ] Acquire succeeds on unlocked lock ref.
- [ ] Acquire retries and eventually succeeds on CAS conflict.
- [ ] Acquire waits on valid foreign lock and times out correctly.
- [ ] Acquire takes over expired lock.
- [ ] Release succeeds for owner token.
- [ ] Release rejects token mismatch.
- [ ] Renewal path extends TTL safely.

### 5C) Unit tests: main behavior

- [ ] Save-state failure still exits non-zero.
- [ ] Lock-release failure exits non-zero.
- [ ] Non-mutating defer paths do not fail and do not save state.
- [ ] Workflow-run invalid context still fails closed.

### 5D) Lint + test commands

- [ ] `uv run ruff check --fix`
- [ ] `uv run pytest .github/reviewer-bot-tests`
- [ ] `uv run pytest`

## Phase 6 - Race and sequencing validation

### 6A) Controlled race simulation

- [ ] Trigger near-simultaneous mutating events (for example label + comment command + review reconcile).
- [ ] Verify only one mutating run holds lock at a time in logs.
- [ ] Verify all mutating runs either:
  - wait and then succeed, or
  - fail closed with explicit lock timeout/error.

### 6B) Fork-PR approval end-to-end

- [ ] Use a fork PR approval scenario.
- [ ] Verify first-hop review run succeeds and uploads reconcile artifact.
- [ ] Verify second-hop reconcile run acquires lock, mutates state, and saves.
- [ ] Verify issue `#314` shows completion fields populated.

## Phase 7 - Rollout plan

- [ ] Open PR with focused scope (intent routing + lock backend + tests + workflow permission update).
- [ ] Include migration note: removes unsupported `If-Match` lease mechanism.
- [ ] After merge, re-run previously failing PR #405 check path.
- [ ] Validate no regressions on same-repo and fork PRs.

## Phase 8 - Observability and operations

- [ ] Add stable lock log lines:
  - `LOCK_ACQUIRE_ATTEMPT`
  - `LOCK_ACQUIRED`
  - `LOCK_WAIT`
  - `LOCK_RENEW`
  - `LOCK_RELEASED`
  - `LOCK_RELEASE_FAILED`
- [ ] Include structured fields in logs:
  - `event_name`, `event_action`, `intent`, `run_id`, `lock_token_prefix`
- [ ] Add short runbook section for stuck lock recovery (TTL wait, diagnostics, escalation).

## Phase 9 - Rollback strategy

- [ ] Keep rollback patch prepared that disables new lock path and forces non-mutating defer for fork review events.
- [ ] If production instability appears:
  - revert lock backend change quickly
  - keep second-hop reconcile flow intact
  - keep fail-closed persistence behavior
- [ ] Capture incident evidence (run IDs, logs, impacted PRs) for postmortem.

## Acceptance criteria

- [ ] No path uses issue `If-Match` conditional writes for locking.
- [ ] Cross-repo `pull_request_review/submitted` no longer fails pre-handler.
- [ ] All mutating paths are serialized by CAS lock backend.
- [ ] No concurrent state writes observed in race tests.
- [ ] Fork-PR approvals auto-persist via second-hop reconcile without manual `/rectify`.
- [ ] Full reviewer-bot tests and repo tests pass.

## Open decisions to resolve before coding starts

- [ ] Lock ref name finalized (recommended: `refs/heads/reviewer-bot-state-lock`).
- [ ] TTL/max-wait defaults finalized.
- [ ] Concurrency policy finalized (recommended: remove event-dropping workflow concurrency and rely on lock serialization).

## Blockers

- [ ] None currently.
- [ ] (Add timestamped blocker notes here if encountered.)
