# Refactor Wave Plan

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Track execution sequencing, scope, and gate checks for each implementation wave.

## Hardening Status (authoritative)

- [x] All wave rows avoid unresolved commit placeholders.
- [x] Wave completion claims are backed by objective local validator checks.
- [x] Phase 3 structural hardening checks are complete.
- [ ] Phase 5 documentation hardening checks are complete.

## Waves

### Wave 1 - Scaffolding and no-behavior-change extraction

- [x] scope finalized
- [x] commit slices listed
- [x] gate checks passed

### Wave 2 - Workspace tracing and runtime alignment

- [x] scope finalized
- [x] workspace tracing migration sequence recorded
- [x] async runtime alignment actions recorded
- [x] gate checks passed

### Wave 3 - Routing and subscription resolution extraction

- [x] scope finalized
- [x] gate checks passed

### Wave 4 - Control plane extraction

- [x] scope finalized
- [x] gate checks passed

### Wave 5 - Data plane extraction

- [x] scope finalized
- [x] gate checks passed

### Wave 6 - Runtime extraction

- [x] scope finalized
- [x] gate checks passed

## Per-Wave Checklist Template

| Wave | Commit(s) | Primary files | Commands run | Result | Notes |
|---|---|---|---|---|---|
| Wave 1 | working tree only (no phase-scoped commit hash recorded) | `up-streamer/src/lib.rs`, `up-streamer/src/{api,control_plane,data_plane,routing,runtime}/**/*` | `cargo build`; `cargo test -p up-streamer --quiet` | pass | Scaffolded target module layout with no behavior changes. |
| Wave 2 | working tree only (no phase-scoped commit hash recorded) | workspace `Cargo.toml` + crate manifests; logging call sites across workspace crates | `cargo build`; `cargo test -p up-streamer --quiet`; `cargo test -p subscription-cache --quiet`; `cargo test -p integration-test-utils --quiet` | pass | Migrated from `log`/`env_logger` to `tracing`/`tracing-subscriber`; removed stale `async-std` deps. |
| Wave 3 | working tree only (no phase-scoped commit hash recorded) | `up-streamer/src/routing/{publish_resolution.rs,subscription_directory.rs}`, `up-streamer/src/ustreamer.rs` | `cargo build`; `cargo test -p up-streamer --quiet` | pass | Extracted publish filter derivation and wildcard subscriber merge lookup. |
| Wave 4 | working tree only (no phase-scoped commit hash recorded) | `up-streamer/src/control_plane/{route_table.rs,route_lifecycle.rs}`, `up-streamer/src/ustreamer.rs` | `cargo build`; `cargo test -p up-streamer --quiet` | pass | Extracted route registration/removal lifecycle and rollback-safe rule-table operations. |
| Wave 5 | working tree only (no phase-scoped commit hash recorded) | `up-streamer/src/data_plane/{ingress_registry.rs,ingress_listener.rs,egress_pool.rs,egress_worker.rs}`, `up-streamer/src/ustreamer.rs` | `cargo build`; `cargo test -p up-streamer --quiet` | pass | Extracted ingress/egress lifecycle ownership while preserving dedupe and unregister symmetry. |
| Wave 6 | working tree only (no phase-scoped commit hash recorded) | `up-streamer/src/runtime/{subscription_runtime.rs,worker_runtime.rs}`, `up-streamer/src/data_plane/egress_worker.rs`, `up-streamer/src/ustreamer.rs` | `cargo build`; `cargo test -p up-streamer --quiet` | pass | Isolated subscription/bootstrap and worker runtime concerns into runtime layer modules. |

## Rollback Notes

| Wave | Trigger | Rollback action | Follow-up |
|---|---|---|---|
|  |  |  |  |
