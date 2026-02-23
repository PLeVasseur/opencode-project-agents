# Cycle 1 Summary

Date: 2026-02-11
Branch: `refactor/up-streamer-domain-architecture`
Head: `91c32908d3810e3c390f652adb5e9782035e815e`
Result: PASS

## Phase and Gate Completion

- Phase 0 (baseline/scoping): PASS (`phase-0-baseline.md`)
- Phase 1 (correctness hardening): PASS (`phase-1.md`)
- Phase 2 (performance refactor): PASS (`phase-2.md`)
- Cycle 1 smoke-8 gate: PASS (8/8 scenarios)
- Cycle 1 CI parity preflight: PASS (base, bundled, unbundled, workspace)

## Commit List (Cycle 1)

1. `7fe9c3a` - `fix: harden plugin lifecycle and ingress listener teardown`
   - scope: `up-linux-streamer-plugin/src/lib.rs`, `up-streamer/src/data_plane/ingress_registry.rs`, `up-streamer/src/ustreamer.rs`
2. `91c3290` - `perf: cut routing and ingress overhead with snapshot caching`
   - scope: `up-streamer/Cargo.toml`, `up-streamer/src/routing/subscription_cache.rs`, `up-streamer/src/routing/subscription_directory.rs`, `up-streamer/src/routing/publish_resolution.rs`, `up-streamer/src/data_plane/ingress_registry.rs`, `Cargo.lock`

## Correctness and Performance Outcomes vs Baseline

- Correctness outcomes:
  - plugin runtime lifecycle now owned in plugin state and startup/runtime failures use fallible `ZResult` flow (no panic-path dependency in runtime path)
  - ingress unregister uses persisted listener filters (no recomputation drift)
  - same-authority add/delete route error wording is operation-consistent
- Performance outcomes (Phase 0 -> Phase 2 medians):
  - `routing_lookup/exact_authority`: `62.989 us -> 40.951 us` (`~35.0%` faster)
  - `routing_lookup/wildcard_authority`: `68.905 us -> 44.215 us` (`~35.8%` faster)
  - `publish_resolution/source_filter_derivation`: `86.594 us -> 23.364 us` (`~73.0%` faster)
  - `ingress_registry/register_route`: `1.4955 ms -> 723.06 us` (`~51.7%` faster)
  - `ingress_registry/unregister_route`: `1.5051 ms -> 661.41 us` (`~56.1%` faster)
  - `egress_forwarding/single_route_dispatch`: `263.51 ns -> 257.43 ns` (`~2.3%` faster)
- No-regression performance gate: PASS

## Smoke-8 Outcomes and Structured Logging Assertions

| Scenario | Outcome | Report |
|---|---|---|
| `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md` |
| `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md` |
| `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md` |
| `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md` |
| `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md` |
| `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md` |
| `smoke-zenoh-someip-rr-zenoh-client-someip-service` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md` |
| `smoke-zenoh-someip-rr-someip-client-zenoh-service` | PASS | `reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md` |

- Structured logging assertions status across all 8 reports:
  - `egress_send_attempt` with `worker_id`: PASS
  - `egress_send_ok` with `worker_id`: PASS
  - `egress_worker_create` or `egress_worker_reuse` with `route_label`: PASS
  - `egress_recv_lagged` / `egress_recv_closed`: not observed in bounded run (explicitly documented per report)

## CI Parity Preflight Outcomes

- Base checks:
  - `source build/envsetup.sh highest` PASS
  - `cargo build` PASS
  - `cargo clippy --all-targets -- -W warnings -D warnings` PASS
  - `cargo fmt -- --check` PASS
- Bundled transport matrix:
  - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport` PASS
  - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` PASS
- Unbundled transport matrix:
  - `VSOMEIP_INSTALL_PATH=/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install`
  - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport` PASS
  - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` PASS
- Workspace checks:
  - `cargo check --workspace --all-targets` PASS
  - `cargo test --workspace` PASS

## Accepted Deviations and Rationale

- `egress_recv_lagged` and `egress_recv_closed` were not observed in bounded smoke windows; this is expected for healthy bounded runs without backpressure/receiver closure conditions.
- During some scenario teardowns, target processes were already exited (`kill: ... No such process`); follow-up `pgrep` checks confirmed no residual scenario processes.
