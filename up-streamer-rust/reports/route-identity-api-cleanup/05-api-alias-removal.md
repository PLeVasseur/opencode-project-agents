# Phase 5 - Remove backward-compatible route alias APIs

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
  - `M up-streamer/src/control_plane/route_lifecycle.rs`
  - `M up-streamer/src/routing/subscription_cache.rs`
  - `M utils/usubscription-static-file/src/lib.rs`
- Conclusion: expected in-progress branch state captured before alias removal.

## API removal and migration evidence

3) Command: `rg -n "pub async fn add_route|pub async fn delete_route|add_forwarding_rule|delete_forwarding_rule" up-streamer/src/ustreamer.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `150:    pub async fn add_route(&mut self, r#in: Endpoint, out: Endpoint) -> Result<(), UStatus> {`
  - `181:    pub async fn delete_route(&mut self, r#in: Endpoint, out: Endpoint) -> Result<(), UStatus> {`
- Conclusion: canonical route APIs remain, and alias methods are removed from `UStreamer`.

4) Command: `rg -n "add_route\(" configurable-streamer/src/main.rs example-streamer-implementations/src/bin/zenoh_someip.rs up-linux-streamer-plugin/src/lib.rs up-streamer/tests`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `configurable-streamer/src/main.rs:176:                .add_route(left_endpoint.to_owned(), right_endpoint.to_owned())`
  - `example-streamer-implementations/src/bin/zenoh_someip.rs:153:        .add_route(zenoh_endpoint.clone(), someip_endpoint.clone())`
  - `up-linux-streamer-plugin/src/lib.rs:233:                .add_route(mechatronics_endpoint.clone(), host_endpoint.clone())`
  - `up-streamer/tests/support/mod.rs:18:        .add_route(r#in.clone(), out.clone())`
- Conclusion: production and test call sites now use `add_route`.

5) Command: `rg -n "delete_route\(" up-streamer/tests`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `up-streamer/tests/api_contract_forwarding_rules.rs:97:            .delete_route(local_endpoint.clone(), remote_endpoint.clone())`
  - `up-streamer/tests/support/mod.rs:30:        .delete_route(r#in.clone(), out.clone())`
- Conclusion: test call sites now use `delete_route`.

6) Command: `rg -n "add_route\(|delete_route\(" up-streamer/src/lib.rs up-streamer/README.md`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `up-streamer/src/lib.rs:79://!     .add_route(left.clone(), right.clone())`
  - `up-streamer/src/lib.rs:82://! streamer.delete_route(left, right).await.unwrap();`
  - `up-streamer/README.md:31:    main thread->>main thread: ustreamer.add_route(local_endpoint, remote_endpoint)`
- Conclusion: docs and compatibility references are updated to canonical route API names.

7) Command: `rg -n "add_forwarding_rule|delete_forwarding_rule" . || true`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - (no matches)
- Conclusion: no stale alias API references remain.

## Focused validation

8) Command: `cargo test -p up-streamer --tests`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `test add_delete_route_contract_duplicate_and_missing_rules ... ok`
  - `test add_delete_route_contract_rejects_same_authority ... ok`
  - `test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out` (integration contract file)
- Conclusion: caller migration to canonical route APIs is behavior-preserving for API contracts.

## Breaking-change migration note

- Breaking change: `UStreamer::add_forwarding_rule` and `UStreamer::delete_forwarding_rule` were removed.
- Required migration: replace all calls with `UStreamer::add_route` and `UStreamer::delete_route`.

## Gate 5 decision

- Result: **PASS**
- Rationale: legacy aliases were removed, all production/tests/docs references migrated, and no stale references remain.
