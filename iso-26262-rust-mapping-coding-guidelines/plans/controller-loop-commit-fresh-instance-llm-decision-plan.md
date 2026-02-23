# Controller Loop Commit + Fresh-Instance + LLM Decision Plan

This plan defines how to run the autonomous controller in a production-grade loop model with:

1) commit-on-accepted-iteration behavior,
2) fresh OpenCode context per iteration,
3) LLM-guided candidate decisioning under deterministic safety rails.

The goal is to improve convergence quality while preventing context-window drift and preserving full auditability.

## 0) Confirmed decisions

- [x] Commit policy is **accepted-loop only** (no empty checkpoint commits for rejected/no-op loops).
- [x] Fresh OpenCode instance per loop is desired to avoid context saturation.
- [x] LLM remains in the loop for decision support, but deterministic gates and schema validation remain authoritative.
- [x] Conventional Commit style remains required.

## 1) Outcomes, scope, and non-goals

### 1.1 Outcomes

- [ ] Each accepted iteration produces a deterministic commit with traceable metadata.
- [ ] Each iteration can execute in a fresh OpenCode process with bounded prompt/context size.
- [ ] Candidate selection can use LLM reasoning with strict output schema and fallback.
- [ ] Convergence remains deterministic: hard gates, lane status, regression checks, and scoring remain enforced.
- [ ] All decision artifacts are persisted for replay, review, and debugging.

### 1.2 In scope

- [ ] `scripts/autonomous_controller.py` (single-iteration + commit policy + decision hooks).
- [ ] New supervisor entrypoint for fresh-instance orchestration.
- [ ] New decision packet/output schemas and validator path.
- [ ] Tests for commit behavior, supervisor resume/idempotency, and LLM decision fallback behavior.

### 1.3 Non-goals (initial release)

- [ ] No replacement of deterministic acceptance with pure LLM judgment.
- [ ] No remote push/PR automation as part of iteration loop runtime.
- [ ] No interactive/manual prompt inside iteration execution path.

## 2) Current baseline and delta

### 2.1 Already present

- [x] Beam candidate generation and two-pass quick/full evaluation.
- [x] Known-good alignment gate integrated into observation and scoring.
- [x] Handoff package generation with lane/delta status.
- [x] Optional commit-on-accept behavior exists (`--commit-each-accept`).

### 2.2 Gaps to close

- [ ] Commit-on-accept is not yet default policy.
- [ ] No dedicated single-iteration execution mode for supervisor-driven fresh process model.
- [ ] No first-class supervisor loop process launching fresh OpenCode per iteration.
- [ ] No LLM decision contract/schema integrated between candidate generation and evaluation.
- [ ] No persisted prompt/decision packet audit files for model decision stage.

## 3) Target architecture

### 3.1 Runtime model

- [ ] **Supervisor layer** controls lifecycle and repeatedly launches one-loop workers in fresh context.
- [ ] **Worker layer** executes exactly one controller iteration from persisted state and exits.
- [ ] **Decision layer** composes packet -> invokes LLM policy -> validates output -> selects plan.
- [ ] **Deterministic enforcement layer** still applies candidate, runs gates, and accepts/rejects based on objective rules.

### 3.2 Data flow per iteration

- [ ] Load state and prior iteration artifacts.
- [ ] Observe deficits and generate candidate bundles.
- [ ] Build decision packet and optional LLM recommendation.
- [ ] Validate recommendation and resolve final candidate set/order.
- [ ] Evaluate candidates (quick/full), apply acceptance rules.
- [ ] If accepted and changed, create commit and persist commit metadata.
- [ ] Write iteration record + updated state + handoff artifacts.

## 4) Workstream A - Commit policy hardening (accepted loops only)

### 4.1 Policy behavior

- [ ] Make accepted-loop commit behavior default for autonomous runs.
- [ ] Preserve an opt-out flag for debugging (`--no-commit-on-accept`).
- [ ] Never create empty commits.
- [ ] Never commit on rejected/no-op iterations.

### 4.2 Commit content controls

- [ ] Stage only mutation scope artifacts from accepted loop:
  - [ ] `data/todo_guidelines.yaml`
  - [ ] `data/coverage_matrix.csv`
  - [ ] `data/guideline_categories.yaml`
  - [ ] `data/target_scope.yaml`
  - [ ] `data/decomposition_report.yaml`
  - [ ] `tests/guidelines/`
- [ ] Keep benchmark/reference packs out of loop commits unless explicitly changed by selected actions.

### 4.3 Commit message contract

- [ ] Use Conventional Commit format:
  - [ ] `chore(controller-loop): accept <session_id> i<iteration> <candidate_id>`
- [ ] Add deterministic trailers in body:
  - [ ] `Controller-Session: <session_id>`
  - [ ] `Controller-Iteration: <n>`
  - [ ] `Controller-Candidate: <candidate_id>`
  - [ ] `Controller-Profile: quick|full`
  - [ ] `Controller-Run-Id: <run_id|none>`

### 4.4 Commit telemetry

- [ ] Persist commit SHA in iteration artifact (e.g., `commit.json`).
- [ ] Record commit SHA in controller history entries.
- [ ] Include commit SHA in handoff summary when available.

## 5) Workstream B - Single-iteration worker mode

### 5.1 CLI and control flow

- [ ] Add `--single-iteration` mode to run exactly one iteration and exit.
- [ ] Add `--resume-session <id>` semantics for deterministic continuation.
- [ ] Add clear exit reasons (`accepted`, `rejected`, `stall`, `stop-success`, `stop-blocked`, `stop-error`).

### 5.2 Idempotency and safety

- [ ] Ensure repeated invocation at same state does not duplicate side effects.
- [ ] Ensure failed candidate application restores workspace snapshot.
- [ ] Ensure commit step runs only once for accepted state transition.

### 5.3 Artifact contract (per iteration)

- [ ] Continue writing:
  - [ ] `observe.json`
  - [ ] `candidates.json`
  - [ ] `evaluation.json`
  - [ ] `iteration.json`
- [ ] Add:
  - [ ] `decision_packet.json`
  - [ ] `llm_decision.raw.json`
  - [ ] `llm_decision.validated.json`
  - [ ] `selection_resolution.json`
  - [ ] `known_good_alignment_overrides.json`

## 6) Workstream C - Fresh-instance supervisor

### 6.1 New supervisor entrypoint

- [ ] Add `scripts/controller_supervisor.py`.
- [ ] Inputs:
  - [ ] `--session-id`
  - [ ] `--max-iterations`
  - [ ] `--spawn-command` (OpenCode invocation template)
  - [ ] `--controller-args-file` (static args payload)
  - [ ] `--poll-interval-seconds`

### 6.2 Supervisor state model

- [ ] Add `.cache/controller/<session>/supervisor_state.json`.
- [ ] Track:
  - [ ] `loop_index`
  - [ ] `worker_pid` / process token
  - [ ] `last_exit_code`
  - [ ] `last_iteration_decision`
  - [ ] `status` (`running|success|blocked|error`)

### 6.3 Process lifecycle

- [ ] On each cycle, launch worker as fresh OpenCode process.
- [ ] Wait for worker completion and inspect iteration/state artifacts.
- [ ] Continue until controller status is terminal.
- [ ] Handle crash recovery by resuming from persisted controller state.

### 6.4 Concurrency guards

- [ ] Add lock file to prevent duplicate supervisors for same session.
- [ ] Fail fast if active lock exists and process is alive.
- [ ] Support `--force-recover-lock` with stale-lock detection.

## 7) Workstream D - LLM decision layer integration

### 7.1 Decision packet schema

- [ ] Add `schemas/controller_decision_packet.schema.json` with:
  - [ ] session/iteration metadata
  - [ ] before-observation metrics/deficits summary
  - [ ] candidate list with pre-score, expected deltas, risk, footprint
  - [ ] suppression history and prior failed signatures
  - [ ] progression thresholds active for this iteration

### 7.2 Decision output schema

- [ ] Add `schemas/controller_llm_decision.schema.json` with:
  - [ ] `selected_candidate_ids[]` (ordered)
  - [ ] `rejected_candidate_ids[]` (optional)
  - [ ] `rationale`
  - [ ] `risk_notes[]`
  - [ ] `confidence` (`low|medium|high`)
  - [ ] `fallback_recommended` (bool)

### 7.3 Prompt + execution adapter

- [ ] Add `scripts/controller_decision.py`.
- [ ] Build compact prompt from decision packet.
- [ ] Invoke configured LLM runner (OpenCode command adapter) with strict output format requirement.
- [ ] Persist raw model output and validated parsed payload.

### 7.4 Deterministic resolution policy

- [ ] Validate model output against schema.
- [ ] Reject unknown candidate IDs.
- [ ] Reject plans violating compatibility/suppression constraints.
- [ ] If invalid/unavailable, fallback to deterministic rank order.
- [ ] Record resolution reason (`llm_valid`, `llm_invalid_fallback`, `llm_unavailable_fallback`).

### 7.5 Guardrails

- [ ] LLM cannot introduce new action types not already generated.
- [ ] LLM cannot bypass hard gates or regression checks.
- [ ] LLM cannot force commit if candidate is rejected.
- [ ] LLM cannot expand mutation footprint beyond policy bounds.

## 8) Workstream E - Progressive strictness and convergence policy

### 8.1 Keep progression active

- [ ] Continue `controller_progression` threshold ramp in `config/alignment_policy.yaml`.
- [ ] Persist active override values per iteration artifact.

### 8.2 Tightening policy phases

- [ ] Early iterations: permissive warn thresholds for exploration.
- [ ] Mid iterations: increase changed-guideline minimum alignment.
- [ ] Late iterations: tighten global threshold and outlier allowance.
- [ ] Optional terminal mode: switch to `error` gate mode near convergence.

### 8.3 Oscillation control

- [ ] Track split/merge or rewrite oscillation patterns per guideline.
- [ ] Suppress repetitive oscillatory signatures after threshold.

## 9) Workstream F - Schema + docs + observability updates

### 9.1 Schemas

- [ ] Update `schemas/controller_state.schema.json` for commit and supervisor metadata.
- [ ] Update `schemas/controller_iteration.schema.json` for decision artifacts.
- [ ] Update `schemas/controller_handoff.schema.json` for decision/commit summaries.

### 9.2 Documentation

- [ ] Update `README.md` with:
  - [ ] single-iteration worker usage
  - [ ] supervisor orchestration usage
  - [ ] commit policy defaults
  - [ ] LLM decision fallback semantics

### 9.3 Dashboard/reporting

- [ ] Add decision provenance fields in dashboard/final report.
- [ ] Show per-iteration selected-by (`deterministic|llm|fallback`).
- [ ] Show per-iteration commit SHA when present.

## 10) Testing strategy

### 10.1 Unit tests

- [ ] Commit policy tests:
  - [ ] accepted-change -> commit created
  - [ ] accepted-no-change -> no commit
  - [ ] rejected -> no commit
- [ ] Decision schema tests:
  - [ ] valid payload accepted
  - [ ] invalid candidate ID rejected
  - [ ] malformed output triggers fallback
- [ ] Progression/override tests:
  - [ ] interpolation correctness
  - [ ] gate-mode transition logic

### 10.2 Integration tests

- [ ] Single-iteration end-to-end in dry mode.
- [ ] Supervisor launching multiple one-iteration workers with resume.
- [ ] Crash/restart recovery from mid-session state.
- [ ] LLM unavailable path -> deterministic fallback path.

### 10.3 Regression tests

- [ ] No regression in existing controller lane/handoff schema validations.
- [ ] Known-good alignment metrics still included in lane status and scoring.

## 11) Rollout phases and commit plan

### Phase 1 - Commit policy + worker mode

- [ ] Implement default accepted-loop commit behavior and single-iteration mode.
- [ ] Add/adjust tests for commit semantics and single-iteration exit behavior.
- [ ] Commit: `feat(controller): default accepted-loop commits and single-iteration mode`.

### Phase 2 - Supervisor (fresh OpenCode per loop)

- [ ] Implement supervisor script and lock/resume behavior.
- [ ] Add supervisor state schema and integration tests.
- [ ] Commit: `feat(controller): add fresh-instance supervisor loop orchestration`.

### Phase 3 - LLM decision contract + fallback

- [ ] Add decision packet/output schemas and decision adapter.
- [ ] Integrate model decision between candidate generation and evaluation.
- [ ] Add fallback and guardrail enforcement tests.
- [ ] Commit: `feat(controller): add schema-validated llm decision layer with fallback`.

### Phase 4 - Docs + observability + hardening

- [ ] Update docs, dashboards, final reports, and handoff artifacts.
- [ ] Run full lint/tests/schema validation and one smoke supervisor run.
- [ ] Commit: `docs(controller): document stateless loop supervisor and decision policy`.

## 12) Exit criteria (definition of done)

- [ ] Accepted iterations auto-commit by default without empty commits.
- [ ] Supervisor can run a full session using fresh process per iteration.
- [ ] LLM decisioning is operational, validated, and safely fallback-capable.
- [ ] All controller schemas/tests pass.
- [ ] End-to-end dry-run and at least one non-dry smoke session complete with auditable artifacts.

## 13) Operational runbook (post-implementation)

- [ ] Start session with supervisor:
  - [ ] `uv run python scripts/controller_supervisor.py --session-id <id> ...`
- [ ] Inspect progress:
  - [ ] `.cache/controller/<id>/state.json`
  - [ ] `.cache/controller/<id>/iterations/<n>/iteration.json`
  - [ ] `.cache/controller/<id>/handoff/handoff.json`
- [ ] Verify commit cadence:
  - [ ] `git log --oneline --grep "controller-loop"`
- [ ] Validate benchmark alignment trend:
  - [ ] compare `known_good_alignment_average` and `known_good_alignment_gap_count` across iterations.
