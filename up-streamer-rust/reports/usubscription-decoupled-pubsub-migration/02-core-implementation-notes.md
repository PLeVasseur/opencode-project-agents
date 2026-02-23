# Phase 2 - Core Implementation Notes

Status: completed

## Revision note

Core implementation was aligned to the revised design lock: `UStreamer` now uses `Arc<dyn USubscription>` directly.

## Core changes

- Refactored `UStreamer` in `up-streamer/src/ustreamer.rs`:
  - `UStreamer::new(...)` is async and takes `Arc<dyn USubscription>`.
  - startup bootstrap performs best-effort `refresh_subscriptions()`.
  - `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>` added.
  - `subscription_sync_health()` accessor added.
  - private `apply_subscription_snapshot(...)` remains internal-only.
  - every attempt updates health (success/failure).
- Added public health metadata type in `up-streamer/src/subscription_sync_health.rs`.
- Inlined former `subscription-cache` crate into `up-streamer` internals:
  - new module: `up-streamer/src/routing/subscription_cache.rs`
  - routing/data-plane imports switched to internal module paths
  - old runtime bootstrap helper removed (`up-streamer/src/runtime/subscription_runtime.rs` deleted)
- `SubscriptionDirectory` enhancements in `up-streamer/src/routing/subscription_directory.rs`:
  - `empty()` constructor
  - `apply_snapshot(...)` atomic replace behavior (build-next-then-swap)
- Workspace topology updates:
  - removed `subscription-cache` from workspace members (`Cargo.toml`)
  - deleted `subscription-cache` crate files
  - removed `subscription-cache` dep from `utils/usubscription-static-file/Cargo.toml`
  - removed runtime deps on `subscription-cache` and `usubscription-static-file` from `up-streamer/Cargo.toml`

## Behavior preservation

- Request/response/notification route behavior preserved via existing ingress registry + route lifecycle tests.
- Publish listener derivation remains deterministic; dedupe still keyed by source identity (`routing/publish_resolution.rs` tests passing).
- Route lifecycle idempotency preserved (`route_table`, `egress_pool`, and ingress registry duplicate registration tests passing).

## Internal validation

### New/updated tests

- `UStreamer` health/refresh tests in `up-streamer/src/ustreamer.rs`:
  - default empty health state
  - startup best-effort on failed bootstrap fetch
  - successful refresh health return semantics
  - failed refresh health visibility via accessor
  - failed apply after prior success marks health correctly
- rollback-focused directory test in `up-streamer/src/routing/subscription_directory.rs`:
  - failed snapshot rebuild does not replace prior cache
- integration tests updated to async `UStreamer::new(...).await` usage

### Commands and outcomes

1) Command:
```bash
cargo check -p up-streamer
```
- Working directory: repo root
- Exit: 0
- Key output line: `Finished 'dev' profile ...`
- Conclusion: core crate compiles with `USubscription`-based constructor and internalized cache.

2) Command:
```bash
cargo test -p up-streamer --lib
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `running 18 tests`
  - `test ustreamer::tests::startup_fetch_failure_is_non_fatal_and_sets_first_failed_attempt ... ok`
  - `test routing::subscription_directory::tests::apply_snapshot_keeps_previous_cache_when_rebuild_fails ... ok`
  - `test result: ok. 18 passed; 0 failed`
- Conclusion: startup best-effort, refresh/sync-health, rollback, and routing behavior tests pass.

3) Command:
```bash
cargo test -p up-streamer --tests --no-run
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - executables produced for all integration tests under `up-streamer/tests/*`
- Conclusion: integration tests compile with revised constructor contract.

## Gate 2 conclusion

Gate status: pass.

- Core `USubscription`-based constructor and refresh behavior are implemented and validated.
- Startup is non-fatal for initial fetch failures.
- Health-only refresh visibility is in place.
- `subscription-cache` standalone crate is removed and inlined into `up-streamer` internals.
