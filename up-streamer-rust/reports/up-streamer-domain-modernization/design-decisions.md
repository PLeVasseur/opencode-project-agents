# Phase 2 Domain Design Decisions

## Entry D1: pinned dependency reality and local transport identity keying
- Command: `rg -n "up-rust\s*=\s*\{\s*version\s*=\s*\"0\.9\"" Cargo.toml`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: 0 (pass)
- Key output lines:
  - `54:up-rust = { version = "0.9", default-features = false }`
- Conclusion: Workspace is pinned to `up-rust 0.9.x`.

## Entry D2: lockfile confirms concrete `up-rust` version
- Command: `rg -n "name = \"up-rust\"|version = \"0\.9\.0\"" Cargo.lock`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `4849:name = "up-rust"`
  - `4850:version = "0.9.0"`
- Conclusion: Resolved dependency is `up-rust 0.9.0`.

## Entry D3: `ComparableTransport` is not reusable from pinned `up-rust`
- Command: `rg -n "ComparableTransport" "$HOME/.cargo/registry/src" --glob "**/up-rust-0.9.0/**" || true`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - no matches
- Conclusion: Local transport identity keying must remain in-crate.

## Entry D4: current local keying is still generic/legacy naming
- Command: `rg -n "struct ComparableTransport|ComparableTransport::new|type ForwardingRule" up-streamer/src`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `up-streamer/src/ustreamer.rs:234:pub(crate) struct ComparableTransport`
  - `up-streamer/src/control_plane/route_table.rs:6:pub(crate) type ForwardingRule = (String, String, ComparableTransport, ComparableTransport);`
  - multiple usages in control-plane/data-plane modules
- Conclusion: rename is required to modernize intent and reduce legacy terminology.

## Entry D5: redundant streamer facade wrappers are unused
- Command: `rg -n "api::streamer|crate::api::streamer|up_streamer::api::streamer" up-streamer/src up-streamer/tests || true`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - no matches
- Conclusion: `api::streamer` thin wrappers can be removed without affecting outward API behavior.

## Entry D6: domain module inventory for ownership mapping
- Command: `ls up-streamer/src/control_plane up-streamer/src/routing up-streamer/src/data_plane up-streamer/src/runtime`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `control_plane: route_lifecycle.rs, route_table.rs`
  - `routing: publish_resolution.rs, subscription_directory.rs`
  - `data_plane: ingress_registry.rs, ingress_listener.rs, egress_pool.rs, egress_worker.rs`
  - `runtime: subscription_runtime.rs, worker_runtime.rs`
- Conclusion: Each behavior family can be mapped to one logical owner module.

## Decisions to execute in modernization waves
- `Transport identity keying`: rename `ComparableTransport` to `TransportIdentityKey`; keep pointer-identity semantics; move ownership into control-plane module so route identity is explicit while remaining reusable by data-plane internals.
- `Facade consolidation`: remove unused `api::streamer` wrappers; retain outward API at `Endpoint::new`, `UStreamer::new`, `UStreamer::add_forwarding_rule`, `UStreamer::delete_forwarding_rule`; make internal API helper module non-public.
- `Domain ownership map`:
  - route lifecycle owner: `up-streamer/src/control_plane/route_lifecycle.rs`
  - subscription/routing resolution owner: `up-streamer/src/routing/` (`publish_resolution.rs` + `subscription_directory.rs`)
  - ingress listener lifecycle owner: `up-streamer/src/data_plane/ingress_registry.rs`
  - egress forwarding/pooling owner: `up-streamer/src/data_plane/egress_pool.rs` (worker runtime in `egress_worker.rs`)
  - runtime bootstrap/spawn boundary owner: `up-streamer/src/runtime/`

## Gate 2 readiness
- Status: PASS
- Rationale: dependency constraints, naming decisions, facade consolidation direction, and ownership map are captured before implementation waves.
