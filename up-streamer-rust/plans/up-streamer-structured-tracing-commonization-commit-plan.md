# Up-Streamer Structured Tracing Commonization Plan (Commit-Bounded)

Date: 2026-02-11
Execution branch: `refactor/up-streamer-domain-architecture`
Status: ready

## Objective

Add grep-friendly, structured tracing across `up-streamer` while preserving behavior and correlation semantics:

- Keep stable egress worker identity (`worker_id`) per worker lifecycle.
- Add standardized event names and structured field keys.
- Correlate route intent (`route_label`) with pooled worker identity.
- Commonize field extraction/formatting helpers so event output stays consistent.
- Expand observability to key core files that currently have little/no runtime logging.

## Execution mode and guardrails

- [x] Manual execution only.
- [x] Stay on branch `refactor/up-streamer-domain-architecture`.
- [x] Before each phase and before each commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Before each commit, run and record:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
  - [x] `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/'` (must return no repo-local artifact paths)
- [x] Do not alter behavior beyond logging/traceability unless explicitly called out in this plan.
- [x] If any commit gate fails, stop and remediate before moving to next commit.

## Artifact and smoke report paths

- [x] Base report root: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/`
- [x] Commit/gate reports root: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/phase-reports/`
- [x] Smoke reports root: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/`
- [x] Smoke artifact root: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/<scenario>-artifacts/`
- [x] Do not create repo-local `plans/`, `prompts/`, or `reports/` artifacts for this execution.

## Scope and coverage matrix

### Core modules with existing logging (migrate to structured events)

- [x] `up-streamer/src/data_plane/egress_worker.rs`
- [x] `up-streamer/src/data_plane/egress_pool.rs`
- [x] `up-streamer/src/data_plane/ingress_listener.rs`
- [x] `up-streamer/src/data_plane/ingress_registry.rs`
- [x] `up-streamer/src/routing/publish_resolution.rs`
- [x] `up-streamer/src/routing/subscription_directory.rs`
- [x] `up-streamer/src/ustreamer.rs`

### Core modules with no/low runtime logging (add targeted structured events)

- [x] `up-streamer/src/control_plane/route_lifecycle.rs`
- [x] `up-streamer/src/runtime/worker_runtime.rs`
- [x] `up-streamer/src/routing/subscription_cache.rs`

### Core modules intentionally low-noise (leave mostly unchanged)

- [x] `up-streamer/src/control_plane/route_table.rs`
- [x] `up-streamer/src/control_plane/transport_identity.rs`
- [x] `up-streamer/src/routing/authority_filter.rs`
- [x] `up-streamer/src/routing/uri_identity_key.rs`
- [x] `up-streamer/src/subscription_sync_health.rs`
- [x] `up-streamer/src/endpoint.rs`
- [x] `up-streamer/src/lib.rs`
- [x] `up-streamer/src/*/mod.rs`

### Optional workspace propagation (follow-up)

- [ ] `configurable-streamer/src/main.rs`
- [ ] `up-linux-streamer-plugin/src/lib.rs`
- [ ] `example-streamer-implementations/src/bin/zenoh_someip.rs`
- [ ] `example-streamer-uses/src/bin/*`
- [ ] `utils/usubscription-static-file/src/lib.rs`
- [ ] `utils/integration-test-utils/src/*` (only if needed for parity)

---

## Structured tracing contract (target)

### Event names

- [x] Egress worker and pool:
  - [x] `egress_send_attempt`
  - [x] `egress_send_ok`
  - [x] `egress_send_failed`
  - [x] `egress_recv_lagged`
  - [x] `egress_recv_closed`
  - [x] `egress_worker_create`
  - [x] `egress_worker_reuse`
  - [x] `egress_worker_remove`
- [x] Ingress path and routing:
  - [x] `ingress_receive`
  - [x] `ingress_drop_unsupported_payload`
  - [x] `ingress_send_to_pool_failed`
  - [x] `ingress_register_request_listener_ok`
  - [x] `ingress_register_request_listener_failed`
  - [x] `ingress_register_publish_listener_ok`
  - [x] `ingress_register_publish_listener_failed`
  - [x] `ingress_unregister_request_listener_ok`
  - [x] `ingress_unregister_request_listener_failed`
  - [x] `ingress_unregister_publish_listener_ok`
  - [x] `ingress_unregister_publish_listener_failed`
  - [x] `subscription_lookup_empty`
  - [x] `publish_source_filter_skipped`
  - [x] `publish_source_filter_build_failed`
- [x] Control-plane lifecycle:
  - [x] `route_add_start`
  - [x] `route_add_ok`
  - [x] `route_add_failed`
  - [x] `route_delete_start`
  - [x] `route_delete_ok`
  - [x] `route_delete_failed`

### Field keys

- [x] Core correlation keys:
  - [x] `event`
  - [x] `component`
  - [x] `worker_id`
  - [x] `worker_thread`
  - [x] `route_label`
- [x] Message keys:
  - [x] `msg_id`
  - [x] `msg_type`
  - [x] `src`
  - [x] `sink`
- [x] Lifecycle/outcome keys:
  - [x] `ref_count`
  - [x] `skipped`
  - [x] `reason`
  - [x] `err`
  - [x] `in_authority`
  - [x] `out_authority`
  - [x] `source_filter`
  - [x] `sink_filter`

### Field formatting policy

- [x] `src`/`sink`: compact form `authority/ue_id/version/resource`.
  - [x] Use `none` when absent.
- [x] `msg_id`: hyphenated UUID when present, otherwise `none`.
- [x] `msg_type`: stable enum string representation.
- [x] `reason`: fixed machine-friendly strings (for example `broadcast_closed`).
- [x] Avoid payload dumps in hot paths.
- [x] Keep field names stable to avoid grep drift.

### Span policy

- [ ] Use spans only where they add stable contextual value.
- [ ] Keep explicit event fields even when spans are present.
- [ ] Candidate spans:
  - [ ] Per-worker dispatch span (`worker_id`, `worker_thread`)
  - [ ] Route lifecycle span (`route_label`, authorities)

---

## Commit 1 - Observability primitives and shared helpers

### Intent

Create reusable tracing constants and formatting helpers so all later commits share one schema implementation.

### Files

- [x] Add `up-streamer/src/observability/mod.rs`
- [x] Add `up-streamer/src/observability/events.rs`
- [x] Add `up-streamer/src/observability/fields.rs`
- [x] Update `up-streamer/src/lib.rs` to wire the module

### Implementation checklist

- [x] Add centralized event-name constants.
- [x] Add helper APIs for message fields:
  - [x] message id extractor/formatter
  - [x] message type extractor/formatter
  - [x] source URI formatter
  - [x] sink URI formatter with `none` fallback
- [x] Add helper APIs for worker context:
  - [x] thread-name fallback helper
  - [x] optional context struct for repeated fields (`worker_id`, `worker_thread`)
- [x] Ensure helpers are unwrap-free and panic-free for production paths.

### Verification

- [x] Add helper unit tests:
  - [x] present/absent msg id
  - [x] present/absent sink
  - [x] URI format stability
  - [x] thread-name fallback behavior
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo test -p up-streamer observability`

### Commit message target

- [x] `chore: add structured tracing event and field helpers`

### Gate 1

- [x] Shared helpers compile and are covered by tests.
- [x] No behavior changes outside helper module wiring.

---

## Commit 2 - Egress worker structured events + stable worker identity

### Intent

Migrate egress worker logs to structured events while preserving loop semantics and stable worker identity.

### Files

- [x] `up-streamer/src/data_plane/egress_worker.rs`
- [x] tests in `up-streamer/src/data_plane/egress_worker.rs`

### Implementation checklist

- [x] Keep worker ID generated once per worker lifecycle.
- [x] Emit structured events for send path:
  - [x] `egress_send_attempt`
  - [x] `egress_send_ok`
  - [x] `egress_send_failed`
- [x] Emit structured events for recv error path:
  - [x] `egress_recv_lagged` with `skipped`
  - [x] `egress_recv_closed` with `reason=broadcast_closed`
- [x] Include fields in all events:
  - [x] `worker_id`
  - [x] `worker_thread`
  - [x] `msg_id`, `msg_type`, `src`, `sink` where applicable
- [x] Add `worker_id()` accessor for downstream pool correlation logs.
- [ ] Optional span work:
  - [ ] add per-worker dispatch span
  - [ ] ensure event fields remain explicit

### Verification

- [x] `cargo test -p up-streamer egress_worker`
- [x] existing behavior tests still prove:
  - [x] `Lagged` continues
  - [x] `Closed` breaks
  - [x] no post-close forwarding
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`

### Commit message target

- [x] `refactor: convert egress worker logs to structured tracing events`

### Gate 2

- [x] Egress semantics unchanged.
- [x] Structured fields present and grepable.

---

## Commit 3 - Pool/lifecycle route-to-worker correlation

### Intent

Correlate human route context (`route_label`) with pooled worker identity so grep can pivot from route intent to worker events.

### Files

- [x] `up-streamer/src/data_plane/egress_pool.rs`
- [x] `up-streamer/src/control_plane/route_lifecycle.rs`
- [x] `up-streamer/src/ustreamer.rs`
- [x] tests in `up-streamer/src/data_plane/egress_pool.rs`

### Implementation checklist

- [x] Update attach signature(s) to carry `route_label` into pool operations.
- [x] Emit structured pool lifecycle events:
  - [x] `egress_worker_create` (`worker_id`, `route_label`, `ref_count=1`)
  - [x] `egress_worker_reuse` (`worker_id`, `route_label`, `ref_count`)
  - [x] `egress_worker_remove` (`worker_id`, `ref_count=0`)
- [x] Keep refcount behavior unchanged.
- [x] Keep rollback behavior unchanged in add-route failure paths.
- [x] Ensure route labels in logs match current label construction.

### Verification

- [x] `cargo test -p up-streamer egress_pool`
- [x] `cargo test -p up-streamer ustreamer`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`

### Commit message target

- [x] `refactor: correlate route labels to pooled egress workers`

### Gate 3

- [x] Route-to-worker mapping is grepable and stable.
- [x] No control-plane behavior drift.

---

## Commit 4 - Migrate remaining currently-logging core modules

### Intent

Apply shared structured schema to remaining core files that already log.

### Files

- [x] `up-streamer/src/data_plane/ingress_listener.rs`
- [x] `up-streamer/src/data_plane/ingress_registry.rs`
- [x] `up-streamer/src/routing/publish_resolution.rs`
- [x] `up-streamer/src/routing/subscription_directory.rs`
- [x] `up-streamer/src/ustreamer.rs` (route operation events)

### Implementation checklist

- [x] Replace ad hoc string-only logs with structured event + fields.
- [x] Standardize `component` values.
- [x] Ensure warning/error paths include machine-grep details:
  - [x] authorities
  - [x] source/sink filters
  - [x] error details
- [x] Keep branch logic/behavior unchanged.

### Verification

- [x] `cargo test -p up-streamer`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo check -p up-streamer --all-targets`

### Commit message target

- [x] `refactor: migrate ingress and routing logs to structured tracing`

### Gate 4

- [x] All previously logging core modules now follow shared schema.

---

## Commit 4b - Add targeted structured events to key no-log core modules

### Intent

Close the key observability gaps in core modules that currently have little/no runtime tracing but materially impact debugging.

### Files

- [x] `up-streamer/src/control_plane/route_lifecycle.rs`
- [x] `up-streamer/src/runtime/worker_runtime.rs`
- [x] `up-streamer/src/routing/subscription_cache.rs`

### Implementation checklist

- [x] `route_lifecycle.rs` events:
  - [x] `route_add_start` with `route_label` + authorities
  - [x] `route_add_ok`
  - [x] `route_add_failed` with failure variant/reason
  - [x] `route_delete_start`
  - [x] `route_delete_ok`
  - [x] `route_delete_failed`
- [x] `worker_runtime.rs` events:
  - [x] runtime thread-name fallback triggered (`reason=invalid_thread_name`)
  - [x] runtime spawn start/success/failure boundary events (where failure can be observed without semantic change)
- [x] `subscription_cache.rs` events (low-volume, non-hot-path):
  - [x] snapshot rebuild start/success/failure summary
  - [x] wildcard merge summary (exact count, wildcard count, merged count)
  - [x] avoid per-row noisy logs by default
- [x] Keep noisy lower-level structures intentionally quiet:
  - [x] no broad logging in `route_table.rs`
  - [x] no broad logging in identity/value-object modules

### Verification

- [x] `cargo test -p up-streamer`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo check -p up-streamer --all-targets`

### Commit message target

- [x] `feat: add structured lifecycle and runtime observability events`

### Gate 4b

- [x] Core observability coverage includes key no-log control/runtime/cache modules.
- [x] Added logs are high-signal and non-noisy.

---

## Optional Commit 5 - Workspace propagation (post-core)

### Intent

Apply stabilized structured schema outside core crate for end-to-end grep parity.

### Candidate files

- [ ] `configurable-streamer/src/main.rs`
- [ ] `up-linux-streamer-plugin/src/lib.rs`
- [ ] `example-streamer-implementations/src/bin/zenoh_someip.rs`
- [ ] `example-streamer-uses/src/bin/*`
- [ ] `utils/usubscription-static-file/src/lib.rs`
- [ ] `utils/integration-test-utils/src/*` (if needed)

### Implementation checklist

- [ ] Standardize startup/shutdown and route-init events for binaries.
- [ ] Add `component` and consistent `event` naming.
- [ ] Keep CLI/demo output expectations intact where needed.

### Verification

- [ ] Build/test affected packages.
- [ ] Re-run full mandatory 8-scenario smoke gate and confirm grep contract end-to-end.

### Commit message target

- [ ] `chore: align workspace binaries and utilities with structured tracing schema`

### Gate 5

- [ ] Workspace-level observability parity achieved for selected modules.

---

## Mandatory smoke validation gate (all 8 scenarios required)

- [x] Execute this gate after Commit 4b (and re-run after Commit 5 if Commit 5 is executed).
- [x] Ensure smoke report directories exist:
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"`

### Scenario matrix with exact skill path and report path

- [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-artifacts/`
- [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts/`
- [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts/`
- [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service-artifacts/`
- [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts/`
- [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-artifacts/`
- [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-someip-rr-zenoh-client-someip-service/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service-artifacts/`
- [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] Skill path: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/skills/smoke-zenoh-someip-rr-someip-client-zenoh-service/SKILL.md`
  - [x] Report path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`
  - [x] Artifact path: `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts/`

### Per-scenario report evidence requirements

- [x] Include exact command(s).
- [x] Include working directory (if not repo root).
- [x] Include exit status and pass/fail.
- [x] Include key output lines proving transport behavior.
- [x] Include concise conclusion.

### Mandatory logging validation within each smoke report

- [x] Verify structured logging in streamer logs using grep-style checks:
  - [x] `event` field emitted for egress dispatch (attempt and success/failure).
  - [x] `worker_id` emitted on egress dispatch events.
  - [x] `route_label` emitted on worker create/reuse mapping events.
- [x] Minimum assertions per scenario report:
  - [x] `rg -n "event=\"?egress_send_attempt\"?.*worker_id=|worker_id=.*event=\"?egress_send_attempt\"?" <streamer.log>`
  - [x] `rg -n "event=\"?egress_send_ok\"?.*worker_id=|worker_id=.*event=\"?egress_send_ok\"?" <streamer.log>`
  - [x] `rg -n "event=\"?egress_worker_create\"?.*route_label=|event=\"?egress_worker_reuse\"?.*route_label=" <streamer.log>`
- [x] If lag or close events are not naturally observed in a scenario run, record explicit `not observed in bounded run` note (do not fail scenario solely for that).

### Constrained-skip policy

- [x] If blocked by missing external prerequisites, mark constrained-skip in that scenario report. (N/A: no external blockers encountered)
- [x] Include exact blocker output and a concrete remediation path. (N/A: no constrained-skip scenarios)

### Gate smoke-8

- [x] PASS only when all 8 scenarios are PASS, or constrained-skip with remediation evidence.
- [x] PASS only when logging assertions above are satisfied (or explicitly justified where not naturally observable).

---

## Cross-commit quality gates

- [x] After each commit:
  - [x] `cargo fmt -- --check`
  - [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
  - [x] run targeted tests for changed modules
- [x] Final core gate (after Commit 4b):
  - [x] `cargo test -p up-streamer`
  - [x] `cargo check -p up-streamer --all-targets`
  - [ ] optional `cargo test --workspace` (environment permitting)
  - [x] Mandatory smoke gate `smoke-8` passes.

## Grep acceptance checks (must pass)

- [x] Egress event checks:
  - [x] `event=egress_send_attempt` includes `worker_id`, `msg_id`, `msg_type`, `src`, `sink`
  - [x] `event=egress_send_ok` includes `worker_id`, `msg_id`
  - [x] `event=egress_recv_lagged` includes `worker_id`, `skipped`
  - [x] `event=egress_recv_closed` includes `worker_id`, `reason=broadcast_closed`
  - [x] `event=egress_worker_reuse` includes `worker_id`, `ref_count`, `route_label`
- [x] Control/routing checks:
  - [x] `event=route_add_start|ok|failed` present and correlated by `route_label`
  - [x] `event=route_delete_start|ok|failed` present and correlated by `route_label`
  - [x] `event=subscription_lookup_empty` includes `out_authority`
  - [x] `event=publish_source_filter_skipped|build_failed` includes relevant authority/topic fields
- [x] Runtime/cache checks:
  - [x] thread-name fallback event emitted when invalid name path is hit
  - [x] cache snapshot/merge summary events emitted (non-row-spam)

## Risks and mitigations

- [x] Risk: log-volume explosion.
  - [x] Mitigation: structured summaries for loops/cache operations, no payload dumps, no per-row spam by default.
- [x] Risk: semantic drift while touching route lifecycle and pool signatures.
  - [x] Mitigation: commit-bounded rollout with module-targeted tests and strict gates.
- [x] Risk: confusion between worker identity and route identity.
  - [x] Mitigation: explicit dual fields and events (`worker_id` + `route_label` mapping events).
- [x] Risk: inconsistent field naming across modules.
  - [x] Mitigation: central event/field helpers and constants in Commit 1.

## Definition of done

- [x] Five core commits (1, 2, 3, 4, 4b) land cleanly.
- [x] Stable worker identity semantics remain intact.
- [x] Route-to-worker correlation is grepable and documented.
- [x] Shared observability helpers are used by all touched core modules.
- [x] Core grep acceptance checks pass.
- [x] Mandatory smoke gate `smoke-8` passes with structured logging assertions.
- [x] Optional workspace propagation (Commit 5) completed or explicitly deferred with rationale.
  - Deferred in this execution: core-crate scope completed and smoke-8 passed without workspace propagation changes.
