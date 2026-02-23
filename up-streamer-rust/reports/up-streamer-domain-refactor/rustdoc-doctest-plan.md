# Rustdoc and Doctest Plan

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Define how docs and doctests explain each abstraction layer while keeping outward API usage simple.

## Crate-Level Documentation

- [x] update crate overview for layered architecture
- [x] keep outward-facing streamer usage front-and-center
- [x] include short architecture map pointing maintainers to internal layer modules

## Module-Level Documentation

| Module/layer | Required docs | Owner | Status |
|---|---|---|---|
| API Facade | public usage and guarantees | OpenCode | complete (per-file rustdoc + layer doctest fence in `api/mod.rs`) |
| Control Plane | route lifecycle, rollback invariants | OpenCode | complete (per-file rustdoc + layer doctest fence in `control_plane/mod.rs`) |
| Routing | wildcard/tuple/dedupe policy semantics | OpenCode | complete (per-file rustdoc + layer doctest fence in `routing/mod.rs`) |
| Data Plane | ingress/egress responsibilities | OpenCode | complete (per-file rustdoc + layer doctest fence in `data_plane/mod.rs`) |
| Runtime | bootstrap and threading/runtime boundaries | OpenCode | complete (per-file rustdoc + layer doctest fence in `runtime/mod.rs`) |

## Per-File Documentation Hardening Checklist

For each file under `up-streamer/src/{api,control_plane,routing,data_plane,runtime}/*.rs`:

- [x] has at least one rustdoc comment (`//!` or `///`)
- [x] listed with doc status below

| File | Rustdoc present | Doctest fence present | Notes |
|---|---|---|---|
| `up-streamer/src/api/mod.rs` | yes | yes | layer doctest added (`ignore`) |
| `up-streamer/src/api/endpoint.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/api/streamer.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/control_plane/mod.rs` | yes | yes | layer doctest added (`ignore`) |
| `up-streamer/src/control_plane/route_lifecycle.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/control_plane/route_table.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/routing/mod.rs` | yes | yes | layer doctest added (`ignore`) |
| `up-streamer/src/routing/publish_resolution.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/routing/subscription_directory.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/data_plane/mod.rs` | yes | yes | layer doctest added (`ignore`) |
| `up-streamer/src/data_plane/ingress_listener.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/data_plane/ingress_registry.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/data_plane/egress_pool.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/data_plane/egress_worker.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/runtime/mod.rs` | yes | yes | layer doctest added (`ignore`) |
| `up-streamer/src/runtime/subscription_runtime.rs` | yes | no | file-level rustdoc added |
| `up-streamer/src/runtime/worker_runtime.rs` | yes | no | file-level rustdoc added |

## Doctest Targets

| Concept | Doctest location | Type (compile/run) | Validation command |
|---|---|---|---|
| basic `Endpoint` + `UStreamer` usage | `up-streamer/src/lib.rs` (Quick start), `up-streamer/src/endpoint.rs`, `up-streamer/src/ustreamer.rs`, `up-streamer/src/api/mod.rs` | run+compile (+ignored layer sample) | `cargo test -p up-streamer --doc` |
| add/delete forwarding rule contract | `up-streamer/src/lib.rs` (Forwarding-rule contract) | run | `cargo test -p up-streamer --doc` |
| routing/control/data/runtime concept examples | `up-streamer/src/{routing,control_plane,data_plane,runtime}/mod.rs` | ignored layer-focused fences | `cargo test -p up-streamer --doc` |

## Validation

- [x] `cargo doc -p up-streamer --no-deps`
- [x] `cargo test -p up-streamer --doc`

### Results

```text
cargo doc -p up-streamer --no-deps -> PASS (generated target/doc/up_streamer/index.html)
cargo test -p up-streamer --doc -> PASS (8 doctests total: 3 passed, 5 ignored layer fences)
python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust --start-phase 5 --end-phase 5 --validate-only -> PASS (0 blockers)
```
