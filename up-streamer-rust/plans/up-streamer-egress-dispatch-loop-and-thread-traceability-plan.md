# up-streamer Egress Dispatch Loop and Thread Traceability Plan (v2)

Status: ready
Execution mode: manual only (no autopilot orchestration)
Target branch: `refactor/up-streamer-domain-architecture`

## Objective

Address egress worker correctness and observability with strict fresh-session execution discipline:

1. Make egress loop logs transport-agnostic and semantically accurate.
2. Handle broadcast `Lagged` by warning and continuing.
3. Break dispatch loop only on channel `Closed`.
4. Optionally make egress runtime thread names uniquely traceable.
5. Include full mandatory 8-scenario smoke validation coverage.

---

## 1) Execution Contract (strict)

- [x] Manual execution only; no autopilot orchestration.
- [x] Pin and enforce execution branch at session start:
  - [x] `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
  - [x] `test -n "$EXEC_BRANCH"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
- [x] First action must be Phase 0 fresh-session preflight.
- [x] Follow phases and gates in strict order; if a gate fails, stop progression.
- [x] Before each phase and before each commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Before each commit, also run and record:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
  - [x] `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/'` returns no matches
- [x] Continuously update this plan in place; flip completed checkboxes from `[ ]` to `[x]` immediately.

---

## 2) Artifact and Evidence Policy

- [x] Use only OPENCODE config directories for artifacts.
- [x] Plan file:
  - [x] `$OPENCODE_CONFIG_DIR/plans/up-streamer-egress-dispatch-loop-and-thread-traceability-plan.md`
- [x] Reports root:
  - [x] `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/`
- [x] Smoke reports root:
  - [x] `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/`

Every evidence entry must include:

- [x] exact command
- [x] working directory (if not repo root)
- [x] exit status / pass-fail
- [x] key output lines proving result
- [x] concise conclusion

---

## 3) Phase 0 - Fresh-Session Preflight (must be first)

- [x] Verify environment roots:
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills"`
- [x] Verify branch pin:
  - [x] `test -n "$EXEC_BRANCH"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Capture baseline touchpoints:
  - [x] `git log --oneline -n 12`
  - [x] `rg -n "UPClientVsomeip|EGRESS_ROUTE_RUNTIME_THREAD_NAME|recv\(\)\.await" up-streamer/src`
- [x] Tooling sanity:
  - [x] `command -v cargo`
  - [x] `command -v rg`
- [x] Write preflight report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/00-preflight.md`

### Gate P0

- [x] Preflight complete and branch pin validated.

---

## 4) Phase 1 - Egress Loop Semantics and Transport-Agnostic Logging

### 4.1 Receive-loop behavior changes

- [x] Update `up-streamer/src/data_plane/egress_worker.rs` receive loop from `while let Ok(...)` to explicit `match`.
- [x] Handle `tokio::sync::broadcast::error::RecvError::Lagged(skipped)`:
  - [x] `warn!` with route ID and skipped count
  - [x] continue dispatch loop
- [x] Handle `RecvError::Closed`:
  - [x] `info!` transport-agnostic loop-termination message
  - [x] break dispatch loop

### 4.2 Logging cleanup

- [x] Remove transport-specific wording (`UPClientVsomeip`) from generic egress worker path.
- [x] Keep send success/failure logs unchanged in structure.
- [x] Ensure all updated logs remain useful for tracing route lifecycle.

### 4.3 Safety checks

- [x] No new panics introduced in loop handling.
- [x] Closed channel does not spin; loop terminates cleanly.

### Gate 1

- [x] `Lagged` = warn + continue; `Closed` = info + break.
- [x] No transport-specific wording remains in generic egress loop logs.

---

## 5) Phase 2 - Optional Unique Thread Naming

### 5.1 Decision checkpoint

- [x] Decide if unique naming lands now (recommended default: yes).
- [x] If no, record explicit defer rationale in phase report and skip implementation items.

### 5.2 Implementation (if enabled)

- [x] Update `up-streamer/src/runtime/worker_runtime.rs` spawn helper to accept caller-provided thread name.
- [x] Generate short unique egress thread names in worker creation (prefix + short suffix).
- [x] Keep Linux thread-name safe length (<= 15 visible chars).
- [x] Preserve deterministic searchable prefix for observability.
- [x] Add fallback naming behavior if dynamic name generation fails constraints.

### 5.3 Scope hygiene

- [x] Touch `up-streamer/src/data_plane/egress_pool.rs` only if name plumbing requires it.
- [x] Touch `up-streamer/src/benchmark_support.rs` only if signature updates force it.

### Gate 2

- [x] Unique naming is implemented and validated, or explicit defer/no-op rationale is recorded.

---

## 6) Phase 3 - Tests (behavior-first)

### 6.1 Egress loop semantic tests

- [x] Add/update tests in `up-streamer` for closed-channel behavior:
  - [x] dispatch loop exits on `Closed`
  - [x] no post-close forwarding
- [x] Add/update tests for lag behavior:
  - [x] lagged receive does not terminate loop
  - [x] subsequent messages continue forwarding

### 6.2 Optional thread-name tests

- [x] If Phase 2 enabled, add targeted assertions for thread-name shape/prefix/length.

### 6.3 Commands

- [x] `cargo test -p up-streamer egress_worker`
- [x] `cargo test -p up-streamer egress_pool`
- [x] `cargo test -p up-streamer`

### Gate 3

- [x] Targeted and package tests pass deterministically.

---

## 7) Phase 4 - Validation and Quality Gate

- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo check -p up-streamer --all-targets`
- [x] Search guards:
  - [x] `rg -n "UPClientVsomeip" up-streamer/src` returns no matches
  - [x] `rg -n "RecvError::Lagged|RecvError::Closed" up-streamer/src/data_plane/egress_worker.rs`

### Gate 4

- [x] Validation checks pass and intended semantics are present.

---

## 8) Phase 5 - Commit Staging

### Commit plan

- [x] Commit A: egress loop semantics + transport-agnostic logs + tests.
- [x] Commit B (optional): unique thread naming + optional tests. (implemented in same scoped commit as A)

### Per-commit checklist

- [x] `git rev-parse --abbrev-ref HEAD`
- [x] `git status --short --branch`
- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`
- [x] `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/'` returns no matches
- [x] run `git status --short --branch` after each commit and record post-commit state

### Gate 5

- [x] Commits are scoped cleanly and reflect plan phases.

---

## 9) Phase 6 - Mandatory Smoke Validation (8 scenarios)

### 9.1 Prerequisites

- [x] `source build/envsetup.sh highest`
- [x] start MQTT broker: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- [x] ensure SOME/IP runtime libs are exported on `LD_LIBRARY_PATH` for SOME/IP scenarios
- [x] run each scenario from the working directory/config expected by the skill

### 9.2 Required smoke scenarios and reports

- [x] Skill: `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
- [x] Skill: `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
- [x] Skill: `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
- [x] Skill: `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
- [x] Skill: `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
- [x] Skill: `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
- [x] Skill: `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
- [x] Skill: `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] Report: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`

### 9.3 Smoke blocker policy

- [x] If blocked by external prerequisite, mark scenario constrained-skip in that scenario report.
- [x] Include exact blocker command/output and concrete remediation steps.

### Gate 6

- [x] All 8 smoke scenarios are PASS, or constrained skips are fully documented with remediation.

---

## 10) Phase 7 - Finalization and Handoff

- [x] Verify this plan checklist is fully updated.
- [x] Write final summary report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/07-final-summary.md`
- [x] Final summary includes:
  - [x] phase/gate completion status
  - [x] commit list (hash + subject + scope)
  - [x] exact recv-loop semantics before/after
  - [x] log wording changes
  - [x] optional thread naming decision/outcome
  - [x] validation results (fmt/clippy/check/tests)
  - [x] 8-scenario smoke outcomes
  - [x] accepted deviations and rationale

### Gate 7

- [x] Plan complete and reproducible in a fresh session.

---

## 11) Success Criteria

- [x] Egress dispatch loop handles `Lagged` as recoverable and `Closed` as terminal.
- [x] Generic egress worker logs are transport-agnostic.
- [x] Optional unique thread naming is either implemented cleanly or explicitly deferred with rationale.
- [x] Targeted tests and package tests pass.
- [x] Validation checks pass for touched scope.
- [x] Mandatory 8 smoke scenarios are executed and reported (or constrained skips documented with remediation).
