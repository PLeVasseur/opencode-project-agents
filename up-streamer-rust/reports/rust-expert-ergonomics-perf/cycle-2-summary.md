# Cycle 2 Summary

Date: 2026-02-11
Branch: `refactor/up-streamer-domain-architecture`
Cycle: 2 (`Phase 3 -> Phase 4 -> Phase 5`)
Result: PASS

## Phase Completion Summary

- Phase 3 (`runtime + throughput`): PASS
  - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/phase-3.md`
- Phase 4 (`ergonomics + API maintainability`): PASS
  - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/phase-4.md`
- Phase 5 (`test determinism + reliability`): PASS
  - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/phase-5.md`

## Commit List (hash + subject + scope)

1. `7fe9c3a` - `fix: harden plugin lifecycle and ingress listener teardown`
   - scope: `up-linux-streamer-plugin/src/lib.rs`, `up-streamer/src/data_plane/ingress_registry.rs`, `up-streamer/src/ustreamer.rs`
2. `91c3290` - `perf: cut routing and ingress overhead with snapshot caching`
   - scope: `up-streamer/src/routing/subscription_cache.rs`, `up-streamer/src/routing/subscription_directory.rs`, `up-streamer/src/routing/publish_resolution.rs`, `up-streamer/src/data_plane/ingress_registry.rs`, manifests/lock updates
3. `ba87921` - `perf: shift egress workers to shared runtime tasks`
   - scope: `up-streamer/src/runtime/worker_runtime.rs`, `up-streamer/src/data_plane/egress_worker.rs`, `up-streamer/src/data_plane/ingress_listener.rs`, `up-streamer/src/data_plane/egress_pool.rs`
4. `04a3563` - `refactor: improve startup ergonomics and static-file reload options`
   - scope: `configurable-streamer/src/main.rs`, `example-streamer-implementations/src/bin/zenoh_someip.rs`, `utils/usubscription-static-file/src/lib.rs`, `Cargo.toml`/`Cargo.lock` updates
5. `4ed7f10` - `test: stabilize integration scenarios with bounded wait controls`
   - scope: `utils/integration-test-utils/src/integration_test_utils.rs`, `utils/integration-test-utils/src/lib.rs`, targeted `up-streamer/tests/*`, deterministic publish-resolution dedupe fix

## Correctness, Ergonomics, Runtime, and Test-Determinism Outcomes

- Correctness: plugin runtime ownership and ingress unregister exactness remain stable from Cycle 1 hardening.
- Runtime: egress workers now prefer shared Tokio runtime task strategy with preserved worker identity/observability semantics.
- Ergonomics: startup paths now use fallible `Result` flow; shutdown is signal-aware (`ctrl_c`) in streamer entrypoints.
- Test determinism: flaky-prone integration paths now use bounded count/delta waits and stabilized pacing; repeated reruns passed.

## Benchmark Deltas and No-Regression Status

Reference baseline: Phase 0 -> latest measured after Phase 3 changes.

- `routing_lookup/exact_authority`: `62.989 us -> 41.276 us` (~34.5% faster)
- `routing_lookup/wildcard_authority`: `68.905 us -> 44.465 us` (~35.5% faster)
- `publish_resolution/source_filter_derivation`: `86.594 us -> 23.818 us` (~72.5% faster)
- `ingress_registry/register_route`: `1.4955 ms -> 735.84 us` (~50.8% faster)
- `ingress_registry/unregister_route`: `1.5051 ms -> 680.46 us` (~54.8% faster)
- `egress_forwarding/single_route_dispatch`: `263.51 ns -> 254.22 ns` (~3.5% faster)

No-regression performance gate status: PASS.

## CI Parity Preflight Outcomes (Cycle 2 End)

- Base matrix: PASS
  - `source build/envsetup.sh highest`
  - `cargo build`
  - `cargo clippy --all-targets -- -W warnings -D warnings`
  - `cargo fmt -- --check`
- Bundled transport matrix: PASS
  - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Unbundled transport matrix: PASS
  - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Workspace matrix: PASS
  - `cargo check --workspace --all-targets`
  - `cargo test --workspace`

## Cycle 2 Smoke-8 Outcomes

All scenarios rerun in Cycle 2 and passed:

1. `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-cycle-2.md`
2. `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-cycle-2.md`
3. `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-cycle-2.md`
4. `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service-cycle-2.md`
5. `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-cycle-2.md`
6. `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-cycle-2.md`
7. `smoke-zenoh-someip-rr-zenoh-client-someip-service` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service-cycle-2.md`
8. `smoke-zenoh-someip-rr-someip-client-zenoh-service` -> PASS
   - report: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-cycle-2.md`

Structured logging assertion status across all Cycle 2 smoke scenarios:

- `event=egress_send_attempt` with `worker_id`: PASS
- `event=egress_send_ok` with `worker_id`: PASS
- `event=egress_worker_create|egress_worker_reuse` with `route_label`: PASS
- `egress_recv_lagged` / `egress_recv_closed`: not observed in bounded run (documented per report)

## Accepted Deviations and Rationale

1. Bounded smoke executables return `124` due `timeout 45s` wrappers.
   - Rationale: publisher/client binaries are continuous loops by design; bounded timeout is expected and treated as PASS when traffic/response assertions pass.
2. `egress_recv_lagged` / `egress_recv_closed` not observed in Cycle 2 smoke logs.
   - Rationale: bounded healthy runs did not induce channel pressure or closure races; explicit `not observed in bounded run` notes were recorded.
3. Phase 4 package selector adjustment (`example-streamer-implementations` -> `up-linux-streamer`) retained.
   - Rationale: workspace package ID is `up-linux-streamer`; command intent and feature scope were preserved.

## Overall Cycle 2 Conclusion

Cycle 2 completed successfully: phases, parity gates, and smoke rerun all passed with no performance regressions and with improved runtime ergonomics and test determinism.
