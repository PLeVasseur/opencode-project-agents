# up-streamer Deterministic Transport Smoke Capstone Plan

Date: 2026-02-12
Status: ready-for-execution
Execution branch: runtime-selected (optional guard via CLI/env)

## 0) Objective

Deliver a deterministic, auditable, one-command transport smoke capstone where each of the 8 canonical scenarios is executed by a dedicated Rust binary, and each binary contains an explicit claims section that validates communication evidence from logs.

## Fresh Session Kickoff (Locked Contract)

- [x] Do not change locked decisions in this plan unless explicitly requested.
- [x] Artifact root defaults to `target/transport-smoke/...` with optional `--artifacts-root <path>` override.
- [x] Do not reference project-specific config directory names in code, CLI help, or workflows.
- [x] Deterministic sender defaults are locked:
  - [x] `--send-count 12`
  - [x] `--send-interval-ms 1000`
- [x] Full bounded run is required before validation:
  - [x] active sender completes all configured sends before final claim evaluation.
  - [x] no early-pass termination in v1.
- [x] Readiness marker channel and text are locked:
  - [x] readiness markers are canonical raw stdout lines via `println!`.
  - [x] passive marker exact text: `READY listener_registered`.
  - [x] streamer marker exact text: `READY streamer_initialized`.
  - [x] emit readiness markers exactly once with no prefixes/suffixes.
- [x] Claim thresholds are locked:
  - [x] endpoint communication claims `>= 4`.
  - [x] `egress_send_attempt >= 2`.
  - [x] `egress_send_ok >= 2`.
  - [x] `egress_worker_create|egress_worker_reuse >= 1`.
- [x] Claim semantics are locked:
  - [x] non-overlapping regex match counts.
  - [x] case-sensitive matching unless regex explicitly uses `(?i)`.
  - [x] one line may satisfy multiple claims; claims evaluate independently.
- [x] Matrix behavior is locked:
  - [x] run all selected scenarios sequentially.
  - [x] continue after per-scenario failures.
  - [x] emit full per-scenario and matrix summaries.
  - [x] return non-zero exit when any scenario fails.
- [x] SOME/IP profile v1 is bundled-only.
- [x] Timeout defaults are locked:
  - [x] broker readiness timeout: `30s`.
  - [x] streamer readiness timeout: `60s`.
  - [x] passive endpoint readiness timeout: `30s`.
  - [x] MQTT scenario hard timeout: `120s`.
  - [x] SOME/IP scenario hard timeout: `180s`.
  - [x] SIGINT grace: `5s`.
  - [x] SIGTERM grace: `5s`.
  - [x] log polling interval: `100ms`.
- [x] Branch guard is optional only:
  - [x] supports `--expected-branch <name>` or `SMOKE_EXPECTED_BRANCH`.
  - [x] branch mismatch fails only when this guard is explicitly provided.
  - [x] without guard, runs are branch-agnostic.
- [x] CI mode is locked:
  - [x] `workflow_dispatch` and nightly `schedule` only.
  - [x] split MQTT and SOME/IP into separate jobs.
  - [x] nightly schedule fixed at `03:00 UTC` (`0 3 * * *`).
  - [x] artifact upload uses `if: always()`.

## 1) Locked Decisions

- [x] The existing smoke skills are operational references only and are not checked into the code path as the runtime mechanism.
- [x] Implement one deterministic Rust binary per smoke scenario (8 total).
- [x] Every smoke binary must contain a clearly visible claims section (required/forbidden log checks).
- [x] Add a matrix runner binary for one-command execution across all scenarios.
- [x] CI mode is manual/nightly only (not PR-required and not PR-advisory).

### 1.1 Locked runtime constants and policies (final)

- [x] Artifact root defaults to `target/transport-smoke/...` with optional `--artifacts-root <path>` override.
- [x] No project-specific config directory names are referenced in code, CLI help, or workflow steps.
- [x] Sender defaults for deterministic runs are locked to:
  - [x] `--send-count 12`
  - [x] `--send-interval-ms 1000`
- [x] Validation boundary for deterministic runs is locked to full bounded execution:
  - [x] active sender must complete all configured sends before final claim evaluation.
  - [x] no early-pass termination in v1 capstone runs.
  - [x] rationale: reduces transient false-pass risk and keeps artifact windows comparable run-to-run.
- [x] Claim thresholds are locked to:
  - [x] endpoint communication claims `>= 4`
  - [x] `egress_send_attempt >= 2`
  - [x] `egress_send_ok >= 2`
  - [x] `egress_worker_create|egress_worker_reuse >= 1`
- [x] Matrix execution mode is locked to continue-all + final aggregate status:
  - [x] run all selected scenarios even after failures
  - [x] emit full summary for every scenario
  - [x] exit non-zero if any scenario fails
- [x] SOME/IP v1 profile is bundled-only for deterministic baseline.
- [x] Branch check is optional guard only (`--expected-branch` / `SMOKE_EXPECTED_BRANCH`).
- [x] Orchestration model is phase-barrier driven (no fixed startup sleeps):
  - [x] streamer readiness marker: `READY streamer_initialized`
  - [x] passive readiness marker: `READY listener_registered`
- [x] Readiness marker emission method is locked:
  - [x] readiness markers are emitted as raw stdout lines via `println!`.
  - [x] readiness parsing must not depend on `RUST_LOG` filtering or tracing subscriber formatting.
  - [x] optional mirrored tracing event is allowed, but stdout marker is canonical.
- [x] Claim semantics are locked:
  - [x] non-overlapping regex match-count semantics
  - [x] case-sensitive by default (`(?i)` opt-in)
  - [x] one line may satisfy multiple claims; claims evaluate independently
- [x] Runner bootstrap policy is locked:
  - [x] self-bootstrap child processes by default
  - [x] allow advanced override via `--no-bootstrap`
- [x] Process supervision policy is locked:
  - [x] PID/process-group tracking is primary control path
  - [x] readiness is detected from live log streams
- [x] Report schema policy is locked:
  - [x] scenario reports include per-phase timings, claim outcomes, and repro command
  - [x] matrix summary includes failed-scenario reasons and aggregate exit rationale
- [x] Timeout defaults are locked to:
  - [x] broker readiness timeout: `30s`
  - [x] streamer readiness timeout: `60s`
  - [x] passive endpoint readiness timeout: `30s`
  - [x] MQTT scenario hard timeout: `120s`
  - [x] SOME/IP scenario hard timeout: `180s`
  - [x] SIGINT grace: `5s`
  - [x] SIGTERM grace: `5s`
  - [x] log polling interval: `100ms`
- [x] CI split-jobs policy is locked:
  - [x] MQTT and SOME/IP run in separate jobs
  - [x] manual (`workflow_dispatch`) and nightly (`schedule`) only
  - [x] artifact upload executes even on failed scenario subsets
- [x] CI operational defaults are locked:
  - [x] MQTT job timeout: `45m`
  - [x] SOME/IP job timeout: `60m`
  - [x] artifact retention: `14 days`
  - [x] set workflow/job artifact upload steps to `if: always()`
  - [x] concurrency guard prevents overlapping nightly runs
  - [x] nightly schedule is fixed at `03:00 UTC` daily (`0 3 * * *`).

## 2) Scope

### 2.1 In scope

- [x] Add a new workspace crate for smoke orchestration and validation.
- [x] Implement 8 scenario binaries with deterministic process orchestration.
- [x] Add deterministic sender controls to example entities (`send-count`, `send-interval-ms`).
- [x] Add deterministic readiness markers in passive entities (service/subscriber).
- [x] Add a matrix binary that executes all scenarios and emits summary artifacts.
- [x] Add fixture-backed Rust tests for the claim engine and scenario contracts.
- [x] Add manual/nightly workflow for reproducible capstone runs.
- [x] Document exact execution commands and artifact locations.

### 2.2 Out of scope

- [ ] Replacing transport implementations or changing transport semantics.
- [ ] Making smoke validation a PR hard gate in this cycle.
- [ ] Introducing non-deterministic fuzzy validators without explicit thresholds.

## 3) Success Criteria

- [x] A reviewer runs one command and gets PASS/FAIL for all 8 scenarios with artifacts.
- [x] Each scenario binary has an explicit claims block that is easy to audit.
- [x] Scenario binaries fail non-zero on missing required evidence or forbidden signatures.
- [x] Matrix runner emits machine-readable JSON and human-readable summary.
- [x] Validator tests prove claim logic correctness independent of live transports.

## 4) Scenario Inventory (Canonical 8)

- [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
- [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
- [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
- [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
- [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
- [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
- [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
- [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`

## 5) Execution Contract

- [x] Manual execution only; no autonomous plan skipping.
- [x] Optional branch guard:
  - [x] support `--expected-branch <name>` and `SMOKE_EXPECTED_BRANCH`.
  - [x] fail fast on mismatch only when guard is provided.
- [x] Capture branch/status before each phase and before each commit:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Keep artifact handling tool-agnostic (no dependency on environment-specific config paths).
- [x] Environment bootstrap policy:
  - [x] scenario and matrix runners self-bootstrap child processes with `source build/envsetup.sh highest`.
  - [x] provide `--no-bootstrap` for advanced environments where setup is already prepared.
- [x] Before each commit, verify only intended files are staged:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`

## 6) Architecture and File Layout

### 6.1 New crate

- [x] Add workspace member: `utils/transport-smoke-suite`.
- [x] Add package metadata and dependencies:
  - [x] `tokio` (process, signal, fs/time where needed)
  - [x] `clap`
  - [x] `regex`
  - [x] `serde` / `serde_json`
  - [x] `chrono`
  - [x] `walkdir` (if needed for artifact scans)
  - [x] `anyhow` or explicit error enum

### 6.2 Internal modules

- [x] `utils/transport-smoke-suite/src/lib.rs`
- [x] `utils/transport-smoke-suite/src/claims.rs`
- [x] `utils/transport-smoke-suite/src/process.rs`
- [x] `utils/transport-smoke-suite/src/logs.rs`
- [x] `utils/transport-smoke-suite/src/scenario.rs`
- [x] `utils/transport-smoke-suite/src/report.rs`
- [x] `utils/transport-smoke-suite/src/env.rs`

### 6.3 Binaries

- [x] `utils/transport-smoke-suite/src/bin/transport-smoke-matrix.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-rr-zenoh-client-someip-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-rr-someip-client-zenoh-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.rs`

## 7) Determinism Controls in Example Binaries

### 7.1 Active senders: bounded execution controls

- [x] Add `--send-count` and `--send-interval-ms` to:
  - [x] `example-streamer-uses/src/bin/mqtt_client.rs`
  - [x] `example-streamer-uses/src/bin/mqtt_publisher.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_client.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_publisher.rs`
  - [x] `example-streamer-uses/src/bin/someip_client.rs`
  - [x] `example-streamer-uses/src/bin/someip_publisher.rs`
- [x] Preserve backward compatibility:
  - [x] default `send-count=0` means infinite behavior (current semantics).
  - [x] default interval remains 1000ms.
- [x] Runner defaults for deterministic smoke execution:
  - [x] scenario and matrix runners pass `--send-count 12` unless explicitly overridden.
  - [x] scenario and matrix runners pass `--send-interval-ms 1000` unless explicitly overridden.

### 7.2 Passive listeners: readiness markers

- [x] Emit explicit readiness line after successful listener registration in:
  - [x] `example-streamer-uses/src/bin/mqtt_service.rs`
  - [x] `example-streamer-uses/src/bin/mqtt_subscriber.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_service.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_subscriber.rs`
  - [x] `example-streamer-uses/src/bin/someip_service.rs`
  - [x] `example-streamer-uses/src/bin/someip_subscriber.rs`
- [x] Standardize marker text (exact): `READY listener_registered`.
- [x] Standardize readiness marker emission behavior:
  - [x] emit marker with `println!("READY listener_registered")` exactly once after successful listener registration.
  - [x] emit marker before blocking/parking or entering long-lived wait.
  - [x] keep marker free of prefixes/suffixes for exact-match parsing.

### 7.3 Streamer readiness markers

- [x] Emit explicit streamer readiness line after transport initialization and route wiring in:
  - [x] `configurable-streamer/src/main.rs`
  - [x] `example-streamer-implementations/src/bin/zenoh_someip.rs`
- [x] Standardize marker text (exact): `READY streamer_initialized`.
- [x] Standardize readiness marker emission behavior:
  - [x] emit marker with `println!("READY streamer_initialized")` exactly once after successful startup wiring.
  - [x] emit marker only when streamer is ready to forward traffic.
  - [x] keep marker free of prefixes/suffixes for exact-match parsing.

### 7.4 Optional graceful shutdown improvements

- [ ] Evaluate replacing `thread::park()` with signal-aware wait where low-risk.
- [ ] If behavior risk is non-trivial, keep `thread::park()` and rely on orchestrator stop policy.

## 8) Claims Engine Requirements (Core Audit Surface)

### 8.1 Claim model

- [x] Implement explicit claim types:
  - [x] `must_match(file, regex, min_count)`
  - [x] `must_not_match(file, regex)`
- [x] Include clear failure diagnostics:
  - [x] file path
  - [x] regex
  - [x] observed count
  - [x] threshold

### 8.2 Scenario contract visibility rule

- [x] Each scenario binary must define a top-level `CLAIMS` section near the top of the file.
- [x] No hidden scenario-specific regex logic inside shared modules.
- [x] Shared modules may evaluate claims, but not define per-scenario requirements.

### 8.3 Standard cross-scenario streamer claims

- [x] Require egress evidence in every scenario:
  - [x] `egress_send_attempt`
  - [x] `egress_send_ok`
  - [x] `egress_worker_create|egress_worker_reuse` signatures
- [x] Require no panic signatures:
  - [x] forbid `panicked at`

### 8.4 Standard claim thresholds (v1)

- [x] Endpoint communication evidence thresholds:
  - [x] request/response or publish/receive claims must each match `>= 4` occurrences.
- [x] Streamer structured egress thresholds:
  - [x] `egress_send_attempt` must match `>= 2` occurrences.
  - [x] `egress_send_ok` must match `>= 2` occurrences.
  - [x] `egress_worker_create|egress_worker_reuse` must match `>= 1` occurrence.
- [x] Thresholds must be configurable per run (CLI), with these values as defaults.

### 8.5 Claim evaluation semantics (locked)

- [x] Counting semantics:
  - [x] counts are non-overlapping regex match occurrences (not just line presence).
  - [x] one log line may satisfy multiple claims; each claim is evaluated independently.
- [x] Regex behavior semantics:
  - [x] case-sensitive by default.
  - [x] case-insensitive matching only when regex explicitly includes `(?i)`.
- [x] File handling semantics:
  - [x] missing required log file is a hard claim failure.
  - [x] unreadable log file reports explicit file-system error in scenario report.

## 9) Shared Orchestration Behavior

### 9.0 Orchestration model (phase-barrier coordinator)

- [x] Implement an explicit state machine per scenario:
  - [x] `Preflight`
  - [x] `StartInfra`
  - [x] `WaitStreamerReady`
  - [x] `StartPassive`
  - [x] `WaitPassiveReady`
  - [x] `StartActive`
  - [x] `ValidateClaims`
  - [x] `Teardown`
  - [x] `FinalizeReport`
- [x] Persist per-phase start/end timestamps in scenario report.

### 9.1 Process lifecycle

- [x] Build required binaries first (deterministic build stage).
- [x] Start dependencies in fixed order.
- [x] Wait for readiness by log marker (not arbitrary sleep).
- [x] Use phase barriers for orchestration (state machine):
  - [x] Phase A: start infra dependencies (broker/streamer).
  - [x] Phase B: wait for streamer readiness marker(s).
  - [x] Phase C: start passive endpoint (service/subscriber) and wait for `READY listener_registered`.
  - [x] Phase D: start active endpoint (client/publisher) with bounded sends.
- [x] Run active endpoint with bounded sends.
- [x] Use deterministic completion logic:
  - [x] wait for active sender to finish full bounded run (`send-count`) before final claim evaluation.
  - [x] do not terminate scenarios early on partial claim satisfaction in v1.
  - [x] if scenario timeout is reached first, fail with phase + unmet-claim diagnostics.
- [x] Validate claims.
- [x] Teardown always, even on failure.

### 9.2 Teardown policy

- [x] Send SIGINT first.
- [x] Wait fixed grace period.
- [x] Send SIGTERM if still running.
- [x] Verify no stale scenario processes remain.
- [x] Track spawned PIDs explicitly; avoid broad process-name kill patterns for normal teardown.
- [x] Keep emergency cleanup mode as fallback only.

### 9.3 Artifact policy

- [x] Per run create deterministic artifact directory:
  - [x] default `target/transport-smoke/<scenario>/<timestamp>/`
  - [x] optional override `--artifacts-root`
- [x] Artifact path behavior must not rely on project-specific environment variables.
- [x] Persist:
  - [x] `streamer.log`
  - [x] endpoint logs (`client.log`/`service.log`/`publisher.log`/`subscriber.log`)
  - [x] `scenario-report.json`
  - [x] `scenario-report.txt`

### 9.4 Timeout constants and behavior

- [x] Implement default timeouts exactly as locked in Section 1.1:
  - [x] broker readiness timeout: `30s`
  - [x] streamer readiness timeout: `60s`
  - [x] passive endpoint readiness timeout: `30s`
  - [x] MQTT scenario hard timeout: `120s`
  - [x] SOME/IP scenario hard timeout: `180s`
  - [x] SIGINT grace: `5s`
  - [x] SIGTERM grace: `5s`
  - [x] log polling interval: `100ms`
- [x] Timeout failure diagnostics:
  - [x] identify phase where timeout occurred.
  - [x] include unmet readiness/claim details in report.

### 9.5 Strict preflight stage

- [x] Common preflight checks:
  - [x] validate repository root and required config file paths.
  - [x] validate required binaries are buildable.
  - [x] verify no stale PIDs from prior smoke runs.
- [x] MQTT-specific preflight checks:
  - [x] docker CLI availability.
  - [x] broker compose file exists (`utils/mosquitto/docker-compose.yaml`).
  - [x] broker port target available or recoverable via controlled teardown.
- [x] SOME/IP-specific preflight checks:
  - [x] bundled vsomeip library path resolvable from build outputs.
  - [x] required SOME/IP configs exist for scenario binaries.

### 9.6 Process supervision and log streaming

- [x] Process supervision model:
  - [x] spawn each child in tracked PID/process-group context.
  - [x] persist PID metadata per process in artifact directory.
  - [x] normal teardown uses tracked PIDs first.
- [x] Live log handling model:
  - [x] stream stdout/stderr to scenario log files continuously.
  - [x] scan streamed lines for readiness markers in near-real-time.
  - [x] retain last N lines per process for failure summaries.

## 10) Per-Scenario Implementation Checklist

### 10.1 `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`

- [x] Encode process graph: broker -> configurable-streamer -> mqtt_service -> zenoh_client.
- [x] Add explicit `CLAIMS` block:
  - [x] client response evidence (`ServiceResponseListener` and/or `UMESSAGE_TYPE_RESPONSE`).
  - [x] service request/response evidence (`Sending Response message`).
  - [x] streamer structured egress evidence.
  - [x] forbidden failure signatures.
- [x] Validate local run PASS.

### 10.2 `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`

- [x] Encode process graph: broker -> configurable-streamer -> zenoh_service -> mqtt_client.
- [x] Add explicit `CLAIMS` block with RR-specific must/forbid checks.
- [x] Validate local run PASS.

### 10.3 `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`

- [x] Encode process graph: broker -> configurable-streamer -> mqtt_subscriber -> zenoh_publisher.
- [x] Add explicit `CLAIMS` block:
  - [x] publisher emitted publish messages.
  - [x] subscriber received publish messages.
  - [x] streamer structured egress evidence.
- [x] Validate local run PASS.

### 10.4 `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`

- [x] Encode process graph: broker -> configurable-streamer -> zenoh_subscriber -> mqtt_publisher.
- [x] Add explicit `CLAIMS` block for pub/sub must/forbid checks.
- [x] Validate local run PASS.

### 10.5 `smoke-zenoh-someip-rr-zenoh-client-someip-service`

- [x] Encode process graph: zenoh_someip streamer -> someip_service -> zenoh_client.
- [x] Add explicit `CLAIMS` block:
  - [x] RR communication evidence.
  - [x] structured egress evidence.
  - [x] forbid `Routing info for remote service could not be found`.
- [x] Validate local run PASS.

### 10.6 `smoke-zenoh-someip-rr-someip-client-zenoh-service`

- [x] Encode process graph: zenoh_someip streamer -> zenoh_service -> someip_client.
- [x] Add explicit `CLAIMS` block for RR must/forbid checks.
- [x] Validate local run PASS.

### 10.7 `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`

- [x] Encode process graph: zenoh_someip streamer -> someip_subscriber -> zenoh_publisher.
- [x] Add explicit `CLAIMS` block for pub/sub must/forbid checks.
- [x] Validate local run PASS.

### 10.8 `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`

- [x] Encode process graph: zenoh_someip streamer -> zenoh_subscriber -> someip_publisher.
- [x] Add explicit `CLAIMS` block for pub/sub must/forbid checks.
- [x] Validate local run PASS.

### 10.9 Source-of-truth scenario manifests

- [x] Implement one authoritative manifest entry per scenario containing:
  - [x] scenario id and transport family.
  - [x] required build targets + feature flags.
  - [x] process startup specs (streamer, passive endpoint, active endpoint).
  - [x] readiness markers to wait for.
  - [x] expected artifact log filenames.
  - [x] scenario-specific claims and forbidden signatures.
- [x] Create and validate manifest entries for all 8 scenarios:
  - [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`

## 11) Matrix Runner (`transport-smoke-matrix`)

- [x] Implement CLI options:
  - [x] `--all` (default)
  - [x] `--only <scenario-id>` (repeatable)
  - [x] `--skip-build`
  - [x] `--artifacts-root <path>`
  - [x] `--send-count <n>` (default 12)
  - [x] `--send-interval-ms <ms>` (default 1000)
  - [x] `--scenario-timeout-secs <n>` (transport-aware defaults)
  - [x] `--expected-branch <name>` (optional)
- [x] Execute scenarios sequentially in stable order.
- [x] Continue running remaining scenarios after a failure.
- [x] Enforce completion semantics in matrix runs:
  - [x] each scenario must run through full bounded sender completion before final validation.
  - [x] no `--early-pass` style option in v1.
- [x] Emit:
  - [x] `matrix-summary.json`
  - [x] `matrix-summary.txt`
- [x] Exit non-zero when any scenario fails.

### 11.1 Report schema (stable, auditable)

- [x] Scenario report JSON includes:
  - [x] scenario id and transport family.
  - [x] overall pass/fail status and exit code.
  - [x] phase timing breakdown (`start_ts`, `end_ts`, `duration_ms`).
  - [x] process metadata (name, pid, command, exit status).
  - [x] claim outcomes (`pattern`, `min_count`, `observed_count`, pass/fail).
  - [x] forbidden claim outcomes and first offending match (if any).
  - [x] first actionable failure reason.
  - [x] exact local repro command.
- [x] Matrix summary JSON includes:
  - [x] selected scenarios, pass/fail counts, total duration.
  - [x] per-scenario artifact directory path.
  - [x] list of failed scenarios with first failure reason.
  - [x] aggregate non-zero exit rationale.

## 12) Validator and Contract Test Suite

### 12.1 Claim engine tests

- [x] Add unit tests for `must_match` count logic.
- [x] Add unit tests for `must_not_match` forbidden logic.
- [x] Add error-path tests for missing log files and malformed regex.

### 12.2 Scenario contract tests

- [x] Add contract registry test asserting exactly 8 scenario IDs.
- [x] Add test that each scenario defines at least:
  - [x] one endpoint-level communication claim
  - [x] one streamer egress claim
  - [x] one forbidden signature claim

### 12.3 Fixture-based audit tests

- [x] Add `tests/fixtures/<scenario>/pass/*.log` fixtures.
- [x] Add `tests/fixtures/<scenario>/fail-*.log` fixtures.
- [x] Add tests asserting pass/fail outcomes per fixture set.

## 13) Documentation and Operability

- [x] Document capstone usage in root `README.md`.
- [x] Document deterministic sender flags in `example-streamer-uses/README.md`.
- [x] Document scenario binary list and example commands.
- [x] Document artifact layout and interpretation of JSON summary.
- [x] Add failure triage playbook documentation:
  - [x] triage order: preflight -> readiness -> claims -> teardown.
  - [x] commands to rerun one failed scenario deterministically.
  - [x] commands to rerun only failed scenarios from prior matrix summary.
  - [x] minimum evidence to include when filing regression issues.

## 14) Manual/Nightly Workflow

- [x] Add `.github/workflows/transport-smoke-capstone.yaml`.
- [x] Trigger modes:
  - [x] `workflow_dispatch`
  - [x] nightly `schedule`
- [x] Nightly schedule details:
  - [x] run once daily at `03:00 UTC`.
  - [x] use cron `0 3 * * *`.
- [x] Install required dependencies and environment setup.
- [x] Split into two jobs:
  - [x] MQTT scenario subset job.
  - [x] SOME/IP scenario subset job.
- [x] Configure workflow strategy to avoid fail-fast cancellation between transport jobs.
- [x] Run matrix subset per job and upload artifacts.
- [x] Keep workflow non-PR-gating by design.
- [x] CI operational details:
  - [x] set explicit per-job timeout values.
  - [x] upload artifacts with `if: always()`.
  - [x] set artifact retention duration.
  - [x] configure workflow concurrency policy to avoid overlapping nightly runs.

## 15) Validation Matrix (Implementation Completion Gate)

- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`
- [x] `cargo test -p transport-smoke-suite`
- [x] Dry run one scenario locally via new binary.
- [x] Dry run full matrix locally via `transport-smoke-matrix`.

## 16) Commit Plan (Scoped Chunks)

- [x] Commit A: workspace + new crate skeleton + shared claim/process/report modules.
- [x] Commit B: deterministic sender controls + readiness markers in example binaries.
- [x] Commit C: MQTT scenario binaries + tests.
- [x] Commit D: SOME/IP scenario binaries + tests.
- [x] Commit E: matrix runner + docs + nightly/manual workflow.

## 17) Risks and Mitigations

- [x] Risk: readiness race in passive endpoints.
  - [x] Mitigation: explicit `READY listener_registered` markers and bounded wait.
- [x] Risk: SOME/IP environment variability.
  - [x] Mitigation: deterministic LD path discovery + explicit preflight checks with actionable failures.
- [x] Risk: false positives from broad forbidden regexes.
  - [x] Mitigation: scoped, reviewed forbidden patterns and fixture tests.
- [x] Risk: process leakage between scenarios.
  - [x] Mitigation: enforced teardown policy and residual-process assertions.

## 18) Definition of Done

- [x] All 8 smoke scenarios run via dedicated Rust binaries with deterministic lifecycle orchestration.
- [x] Every scenario binary contains a clear, auditable claims section.
- [x] Matrix runner provides one-command PASS/FAIL and complete artifacts.
- [x] Validator tests are deterministic, fixture-based, and reviewer-auditable.
- [x] Manual/nightly workflow executes capstone and publishes artifacts.
- [x] Documentation enables a new contributor to run and interpret capstone results unassisted.
