# Phase 1 - Inventory and decision capture

## Phase pre-check

1) Command: `git rev-parse --abbrev-ref HEAD`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
- Conclusion: phase started on required branch.

2) Command: `git status --short --branch`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture`
- Conclusion: worktree baseline captured before Phase 1 execution.

## Inventory evidence

3) Command: `rg -n "UUriIdentityKey|SubscriptionIdentityKey|SourceFilterLookup" up-streamer/src/routing/subscription_cache.rs up-streamer/src/routing/publish_resolution.rs utils/usubscription-static-file/src/lib.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `up-streamer/src/routing/subscription_cache.rs:10:pub(crate) struct UUriIdentityKey {`
  - `up-streamer/src/routing/publish_resolution.rs:9:pub(crate) type SourceFilterLookup = HashMap<UUriIdentityKey, UUri>;`
  - `utils/usubscription-static-file/src/lib.rs:31:struct UUriIdentityKey {`
- Conclusion: URI identity wrapper usage is present at all three targeted files.

4) Command: `rg -n "enum AddRouteError|enum RemoveRouteError" up-streamer/src/control_plane/route_lifecycle.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `10:pub(crate) enum AddRouteError {`
  - `17:pub(crate) enum RemoveRouteError {`
- Conclusion: route lifecycle error enums exist and are the correct trait-implementation targets.

5) Command: `rg -n "TransportIdentityKey" up-streamer/src/control_plane/transport_identity.rs up-streamer/src/control_plane/route_table.rs up-streamer/src/data_plane/egress_pool.rs up-streamer/src/data_plane/ingress_registry.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `up-streamer/src/control_plane/transport_identity.rs:9:pub(crate) struct TransportIdentityKey {`
  - `up-streamer/src/control_plane/route_table.rs:16:    pub(crate) ingress_transport: TransportIdentityKey,`
  - `up-streamer/src/data_plane/egress_pool.rs:26:    pub(crate) workers: Mutex<HashMap<TransportIdentityKey, EgressRouteBinding>>,`
  - `up-streamer/src/data_plane/ingress_registry.rs:65:    transport: TransportIdentityKey,`
- Conclusion: one local transport identity key type is already used across targeted `up-streamer` internals.

6) Command: `rg -n "add_forwarding_rule|delete_forwarding_rule" up-streamer/src/ustreamer.rs configurable-streamer/src/main.rs example-streamer-implementations/src/bin/zenoh_someip.rs up-linux-streamer-plugin/src/lib.rs up-streamer/tests up-streamer/src/lib.rs up-streamer/README.md`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `up-streamer/src/ustreamer.rs:207:    pub async fn add_forwarding_rule(`
  - `up-streamer/src/ustreamer.rs:216:    pub async fn delete_forwarding_rule(`
  - `configurable-streamer/src/main.rs:176:                .add_forwarding_rule(left_endpoint.to_owned(), right_endpoint.to_owned())`
  - `example-streamer-implementations/src/bin/zenoh_someip.rs:153:        .add_forwarding_rule(zenoh_endpoint.clone(), someip_endpoint.clone())`
  - `up-linux-streamer-plugin/src/lib.rs:233:                .add_forwarding_rule(mechatronics_endpoint.clone(), host_endpoint.clone())`
  - `up-streamer/tests/support/mod.rs:18:        .add_forwarding_rule(r#in.clone(), out.clone())`
  - `up-streamer/src/lib.rs:114://! Compatibility note: \`add_forwarding_rule\` / \`delete_forwarding_rule\` remain`
  - `up-streamer/README.md:31:    main thread->>main thread: ustreamer.add_forwarding_rule(local_endpoint, remote_endpoint)`
- Conclusion: legacy alias APIs are still exported and used across production, tests, and docs.

## Decision capture

- Keep transport identity handling local to `up-streamer`; no external transport-abstraction migration in this run.
- Replace `UUriIdentityKey` with `UUri` map keys in targeted files where semantics remain unchanged.
- Clippy mutable-key strategy: no scoped allow planned; proceed with direct `UUri` keys and verify via clippy in validation phases.

## Gate 1 decision

- Result: **PASS**
- Rationale: all required touchpoints were inventoried with file-level evidence and explicit decisions were captured.
