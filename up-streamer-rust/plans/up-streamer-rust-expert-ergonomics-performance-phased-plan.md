# Up-Streamer Rust Expert Ergonomics and Performance Phased Plan

Date: 2026-02-11
Status: ready-for-execution
Execution branch: `refactor/up-streamer-domain-architecture`

## Objective

Improve correctness, ergonomics, and performance across core and workspace entry points while preserving forwarding behavior and structured tracing contract stability.

## Locked decisions (resolved)

- [x] Branch: execute on current branch `refactor/up-streamer-domain-architecture`.
- [x] Cycle model: two cycles (`Cycle 1 = Phases 0-2`, `Cycle 2 = Phases 3-5`).
- [x] Snapshot strategy in Phase 2: `ArcSwap`-based immutable snapshots.
- [x] Plugin runtime strategy in Phase 1: own runtime in plugin state (lifetime-safe).
- [x] Dependency policy: adding `arc-swap` is allowed where justified.
- [x] Validation cadence: staged validation by phase/commit, plus mandatory smoke gates.
- [x] Performance gate: no regressions required; improvements are measured and reported.
- [x] Commit granularity: per-phase commits.

## Session bootstrap (must be first action in every new session)

- [x] Manual execution only (no autopilot orchestration).
- [x] Pin branch and hard-fail on mismatch:
  - [x] `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
- [x] Record baseline branch/status:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git rev-parse HEAD`
- [x] Validate artifact root env:
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `ls "$OPENCODE_CONFIG_DIR/plans"`
- [x] Create report directories:
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills"`
- [x] Ensure no repo-local plan/prompt/report artifacts are introduced.

## Environment and prerequisite preflight

- [x] Base environment:
  - [x] `source build/envsetup.sh highest`
  - [x] `rustc --version` (confirm MSRV-compatible toolchain)
  - [x] `cargo --version`
- [x] Docker availability for MQTT smoke:
  - [x] `docker --version`
  - [x] `docker compose version`
- [x] SOME/IP prerequisites:
  - [x] bundled path resolvable from `target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib`
  - [x] `LD_LIBRARY_PATH` update path documented in evidence
- [x] Unbundled matrix precondition (conditional if integration touched):
  - [x] `VSOMEIP_INSTALL_PATH` points to valid install tree

## Guardrails

- [x] Preserve control-plane and data-plane behavior unless explicitly called out.
- [x] Keep egress `Lagged` and `Closed` behavior unchanged.
- [x] Keep structured tracing contract stable (`event`, `worker_id`, `route_label`, field keys).
- [x] Prefer fallible error propagation over `panic!/expect/unwrap` in runtime paths.
- [x] Keep all generated operational artifacts under `$OPENCODE_CONFIG_DIR`.

## Cycle plan

### Cycle 1 (Hardening + high-impact perf)

- [x] Execute Phase 0, Phase 1, and Phase 2 only.
- [x] Run full 8-scenario smoke matrix immediately after Phase 2.
- [x] Publish Cycle 1 summary report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/cycle-1-summary.md`

### Cycle 2 (Runtime + ergonomics + test reliability)

- [x] Execute Phase 3, Phase 4, and Phase 5 only after Cycle 1 acceptance.
- [x] Re-run full 8-scenario smoke matrix if Cycle 2 touches runtime/transport/plugin behavior.
- [x] Publish Cycle 2 summary report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/cycle-2-summary.md`

## Commit sequence and boundaries

- [x] Phase 0: evidence only, no code commit required.
- [x] Phase 1: single commit for correctness hardening.
- [x] Phase 2: single commit for snapshot/caching performance.
- [x] Phase 3: single commit for worker runtime/hot-path optimization.
- [x] Phase 4: single commit for ergonomic/API cleanup.
- [x] Phase 5: single commit for test determinism.
- [ ] If fixes are needed after review/gates, use follow-up commits (no amend unless explicitly requested).

## Phase 0 - Baseline and scoping

### Intent

Establish reproducible baseline before refactors.

### Checklist

- [x] Record branch/status/hash before phase start:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git rev-parse HEAD`
- [x] Run baseline checks:
  - [x] `cargo fmt -- --check`
  - [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
  - [x] `cargo test -p up-streamer`
- [x] Capture benchmark baseline (where available):
  - [x] `cargo bench -p up-streamer --bench streamer_criterion -- --noplot`
- [x] Record output and conclusions in:
  - [x] `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/phase-0-baseline.md`

### Exit criteria

- [x] Baseline commands, outputs, and benchmark notes are recorded.

---

## Phase 1 - Correctness hardening first

### Intent

Remove high-risk runtime failure modes and enforce exact listener teardown behavior.

### Scope

- `up-linux-streamer-plugin/src/lib.rs`
- `up-streamer/src/data_plane/ingress_registry.rs`
- `up-streamer/src/ustreamer.rs` (targeted correctness/consistency only)

### Checklist

- [x] Plugin runtime lifecycle and error model:
  - [x] Store plugin runtime in plugin state so spawned tasks outlive `start()` return.
  - [x] Replace panic/expect startup/runtime failures with `ZResult` propagation.
  - [x] Keep deterministic plugin shutdown behavior.
- [x] Ingress listener exactness:
  - [x] Persist exact listener filters registered for each binding.
  - [x] Unregister exactly persisted filters (no recomputation drift).
  - [x] Preserve duplicate-register refcount semantics.
- [x] API consistency fix:
  - [x] Correct same-authority error wording for add/delete route paths in `ustreamer`.

### Verification

- [x] `cargo test -p up-streamer ingress_registry`
- [x] `cargo test -p up-streamer ustreamer`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo check -p up-linux-streamer-plugin --all-targets --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`

### Exit criteria

- [x] Plugin runtime path is lifecycle-safe and panic-light.
- [x] Listener teardown correctness is covered and passing.

---

## Phase 2 - High-impact performance refactors

### Intent

Reduce clone-heavy lookup work and lock contention in routing/subscription paths.

### Scope

- `up-streamer/src/routing/subscription_cache.rs`
- `up-streamer/src/routing/subscription_directory.rs`
- `up-streamer/src/routing/publish_resolution.rs`
- `up-streamer/src/data_plane/ingress_registry.rs` (cache integration)

### Checklist

- [x] Introduce `ArcSwap` snapshot carrier for read-mostly subscription lookup.
- [x] Add snapshot versioning and version-aware derived filter caching.
- [x] Cache publish source-filter derivation by `(in_authority, out_authority, snapshot_version)`.
- [x] Preserve wildcard merge and dedupe semantics exactly.
- [x] Add/adjust focused tests and benchmark coverage for route add/remove and lookup hot paths.

### Verification

- [x] `cargo test -p up-streamer routing`
- [x] `cargo test -p up-streamer ingress_registry`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo bench -p up-streamer --bench streamer_criterion -- --noplot`
- [x] Record benchmark comparison vs Phase 0 baseline.

### Exit criteria

- [x] No benchmark regressions are introduced in tracked hotspots.
- [x] Allocation/lookup behavior is measurably improved or neutral with rationale.
- [x] Subscriber matching and listener registration behavior remains unchanged.

---

## Cycle 1 mandatory smoke gate (full 8 scenarios)

### Execution setup

- [x] `export SMOKE_ROOT="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills"`
- [x] `mkdir -p "$SMOKE_ROOT"`
- [x] Ensure no stale scenario processes before each scenario run.

### Scenario checklist

- [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - [x] Skill: `skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-artifacts/`
- [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] Skill: `skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts/`
- [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] Skill: `skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts/`
- [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] Skill: `skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service-artifacts/`
- [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] Skill: `skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts/`
- [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - [x] Skill: `skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-artifacts/`
- [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] Skill: `skills/smoke-zenoh-someip-rr-zenoh-client-someip-service/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-someip-rr-zenoh-client-someip-service-artifacts/`
- [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] Skill: `skills/smoke-zenoh-someip-rr-someip-client-zenoh-service/SKILL.md`
  - [x] Report: `$SMOKE_ROOT/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`
  - [x] Artifacts: `$SMOKE_ROOT/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts/`

### Required structured logging assertions in every scenario report

- [x] `rg -n "event=\"?egress_send_attempt\"?.*worker_id=|worker_id=.*event=\"?egress_send_attempt\"?" <streamer.log>`
- [x] `rg -n "event=\"?egress_send_ok\"?.*worker_id=|worker_id=.*event=\"?egress_send_ok\"?" <streamer.log>`
- [x] `rg -n "event=\"?egress_worker_create\"?.*route_label=|event=\"?egress_worker_reuse\"?.*route_label=" <streamer.log>`
- [x] If `egress_recv_lagged` / `egress_recv_closed` not observed, include explicit note: `not observed in bounded run`.

### Required evidence schema in every scenario and phase report

- [x] exact command
- [x] working directory (if not repo root)
- [x] exit status and pass/fail
- [x] key output lines proving result
- [x] concise conclusion

### Blocker / constrained-skip policy

- [ ] If external prerequisite is missing, stop scenario progression and mark `constrained-skip` for that scenario.
- [ ] Include blocker command, output, and remediation steps in the scenario report.
- [ ] Continue only after documenting blocker and confirming whether remediation is available.

### Cycle 1 smoke exit criteria

- [x] All 8 scenarios are `PASS`, or constrained-skip with explicit remediation evidence.
- [x] Structured logging assertions are present in each scenario report.
- [x] Cycle 1 summary includes per-scenario outcome table.

---

## Phase 3 - Runtime and throughput optimizations

### Intent

Improve worker/runtime efficiency and trim hot-path overhead while preserving semantics.

### Scope

- `up-streamer/src/runtime/worker_runtime.rs`
- `up-streamer/src/data_plane/egress_worker.rs`
- `up-streamer/src/data_plane/ingress_listener.rs`

### Checklist

- [x] Implement lifecycle-safe worker runtime model (shared-runtime task strategy or equivalent) without changing behavior.
- [x] Preserve stable `worker_id` semantics and structured event names.
- [x] Reduce duplicate message-field formatting in hot logs.
- [x] Validate unchanged `Lagged`/`Closed` behavior.

### Verification

- [x] `cargo test -p up-streamer egress_worker`
- [x] `cargo test -p up-streamer`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] Record throughput/latency deltas vs baseline.

### Exit criteria

- [x] No semantic drift in worker dispatch behavior.
- [x] No performance regressions in tracked hot paths.

---

## Phase 4 - Ergonomics and API maintainability

### Intent

Reduce duplication and improve operator-facing startup/shutdown behavior.

### Scope

- `configurable-streamer/src/main.rs`
- `example-streamer-implementations/src/bin/zenoh_someip.rs`
- `utils/usubscription-static-file/src/lib.rs`
- `up-streamer/Cargo.toml`

### Checklist

- [x] Deduplicate endpoint registration and forwarding wiring helpers.
- [x] Replace `thread::park()` hold pattern with signal-aware graceful shutdown where appropriate.
- [x] Align startup errors with fallible `Result` flow in `zenoh_someip`.
- [x] Add cache/reload strategy option for static-file parse path.
- [x] Remove/move unused dependencies without behavior change.

### Verification

- [x] `cargo check -p configurable-streamer --all-targets`
- [x] `cargo check -p up-linux-streamer --all-targets --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
- [x] `cargo test -p usubscription-static-file`
- [x] `cargo clippy --workspace --all-targets -- -W warnings -D warnings`

### Exit criteria

- [x] Startup/shutdown ergonomics are improved and documented.
- [x] No regressions in streamer behavior or wiring semantics.

---

## Phase 5 - Test determinism and reliability

### Intent

Reduce sleep-driven flakiness and improve diagnostics.

### Scope

- `utils/integration-test-utils/src/integration_test_utils.rs`
- `up-streamer/tests/*.rs`

### Checklist

- [x] Replace fixed sleeps with event/count-driven waits and bounded timeouts.
- [x] Refactor order-check utilities to avoid unwrap-driven panic chains.
- [x] Keep scenario intent unchanged while reducing timing variance.
- [x] Consolidate duplicated test setup where practical.

### Verification

- [x] `cargo test -p up-streamer --tests`
- [x] Re-run flaky-prone scenarios at least 3 times and record consistency.

### Exit criteria

- [x] Scenario tests are more deterministic and diagnostically richer.

---

## CI parity preflight gates

### Cycle 1 end (mandatory)

- [x] Base checks:
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo build`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `cargo fmt -- --check`
- [x] Bundled transport matrix:
  - [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] Unbundled transport matrix (if plugin/transport integration touched):
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] Workspace checks (environment permitting):
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo test --workspace`

### Cycle 2 end (mandatory)

- [x] Repeat Cycle 1 preflight matrix after Phase 5 completion.
- [x] Re-run smoke matrix if Cycle 2 touched runtime/transport/plugin paths.

---

## Cross-phase commit and gate protocol

- [x] Before each phase and before each commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Before each commit, run and record:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
  - [x] `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/'` (must be empty)
- [x] After each phase, run and record:
  - [x] `cargo fmt -- --check`
  - [x] phase-targeted tests
  - [x] relevant `cargo clippy` checks with `-D warnings`
- [x] Update this plan in place during execution (`[ ]` to `[x]` immediately when done).
- [x] Write phase report immediately after each phase to:
  - [x] `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/phase-<n>.md`

## Restart/resume protocol (fresh session safety)

- [x] Re-run Session bootstrap section completely.
- [x] Re-read this plan and locate first unchecked item.
- [x] Confirm staged area is empty unless intentionally preparing a commit.
- [x] Confirm last executed phase report exists and matches git history.
- [x] If mismatch exists, stop and write blocker note before continuing.

## Definition of done

- [x] Cycle 1 complete (Phases 0-2, smoke-8 pass, cycle report).
- [x] Cycle 2 complete (Phases 3-5, final validation gates, cycle report).
- [x] No unapproved semantic behavior changes introduced.
- [x] Structured tracing contract remains stable.
- [x] No benchmark regressions in tracked hotspots.
- [x] Final summary report includes:
  - [x] commit list and scope
  - [x] validation command outcomes
  - [x] smoke scenario outcomes
  - [x] measured perf deltas
  - [x] accepted deviations and rationale
