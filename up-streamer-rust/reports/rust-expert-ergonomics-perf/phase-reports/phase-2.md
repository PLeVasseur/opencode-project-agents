# Phase 2 Report

Date: 2026-02-11
Phase: 2 - High-impact performance refactors
Result: PASS (after one benchmark-gate remediation)

## Scope Implemented

- `up-streamer/Cargo.toml`
  - Added `arc-swap` dependency for lock-free snapshot publication.
- `up-streamer/src/routing/subscription_directory.rs`
  - Replaced `Arc<Mutex<SubscriptionCache>>` read path with `ArcSwap` snapshot carrier.
  - Added snapshot versioning and version-aware lookup API (`lookup_route_subscribers_with_version`).
- `up-streamer/src/routing/subscription_cache.rs`
  - Added precomputed wildcard-merged lookup map at snapshot-build time to remove per-lookup merge overhead.
- `up-streamer/src/routing/publish_resolution.rs`
  - Added `PublishSourceFilterCacheKey(in_authority, out_authority, snapshot_version)`.
  - Optimized derivation hot path by deduping topic projection before source-URI construction.
- `up-streamer/src/data_plane/ingress_registry.rs`
  - Integrated version-aware publish source-filter caching keyed by `(in_authority, out_authority, snapshot_version)`.
  - Preserved duplicate-register semantics and exact persisted listener teardown behavior.
  - Added focused tests for snapshot-version cache behavior.

## Evidence

### 1) Phase start branch/status

- exact command: `git rev-parse --abbrev-ref HEAD && git status --short --branch`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- concise conclusion: Phase 2 started on the pinned branch with only prior committed work.

### 2) Routing verification

- exact command: `source build/envsetup.sh highest && cargo test -p up-streamer routing`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `running 12 tests`
  - `routing::subscription_directory::tests::apply_snapshot_advances_version_and_lookup_version_matches ... ok`
  - `routing::publish_resolution::tests::cache_key_is_version_sensitive ... ok`
- concise conclusion: Routing behavior and added version/caching tests pass.

### 3) Ingress registry verification

- exact command: `source build/envsetup.sh highest && cargo test -p up-streamer ingress_registry`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `running 4 tests`
  - `register_route_cache_key_uses_snapshot_version ... ok`
  - `unregister_route_uses_registered_filters_after_snapshot_change ... ok`
- concise conclusion: Ingress cache integration keeps correctness semantics and validates version-aware behavior.

### 4) Clippy verification

- exact command: `source build/envsetup.sh highest && cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Checking up-streamer v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo]`
- concise conclusion: Phase 2 changes are lint-clean under strict warnings.

### 5) Initial benchmark gate (blocking failure)

- exact command: `source build/envsetup.sh highest && cargo bench -p up-streamer --bench streamer_criterion -- --noplot`
- working directory: repo root
- exit status / pass-fail: `0` / FAIL (performance gate)
- key output lines:
  - `routing_lookup/exact_authority time: [73.503 us 73.826 us 74.195 us]`
  - `routing_lookup/wildcard_authority time: [77.005 us 77.820 us 78.762 us]`
  - `Performance has regressed.` for both routing lookup benchmarks
- concise conclusion: No-regression gate failed versus Phase 0 baseline; progression paused for remediation.

### 6) Remediation actions

- exact command: code refactor (no shell command) in:
  - `up-streamer/src/routing/subscription_cache.rs`
  - `up-streamer/src/routing/subscription_directory.rs`
  - `up-streamer/src/routing/publish_resolution.rs`
- working directory: n/a
- exit status / pass-fail: PASS
- key output lines: n/a (source-level remediation)
- concise conclusion: Removed per-lookup wildcard merge cost, switched ArcSwap reads to guard-based loads, and reduced repeated publish source URI reconstruction.

### 7) Final benchmark gate and baseline comparison

- exact command: `source build/envsetup.sh highest && cargo bench -p up-streamer --bench streamer_criterion -- --noplot`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines (final run medians):
  - `routing_lookup/exact_authority time: [40.765 us 40.951 us 41.184 us]`
  - `routing_lookup/wildcard_authority time: [43.987 us 44.215 us 44.523 us]`
  - `publish_resolution/source_filter_derivation time: [23.287 us 23.364 us 23.457 us]`
  - `ingress_registry/register_route time: [718.13 us 723.06 us 729.52 us]`
  - `ingress_registry/unregister_route time: [653.80 us 661.41 us 672.21 us]`
  - `egress_forwarding/single_route_dispatch time: [254.48 ns 257.43 ns 260.46 ns]`
- concise conclusion: All tracked hotspots are improved versus Phase 0 baseline (no regressions).

## Baseline vs Final Benchmark Delta (Phase 0 -> Phase 2)

- `routing_lookup/exact_authority`: `62.989 us -> 40.951 us` (`~35.0%` faster)
- `routing_lookup/wildcard_authority`: `68.905 us -> 44.215 us` (`~35.8%` faster)
- `publish_resolution/source_filter_derivation`: `86.594 us -> 23.364 us` (`~73.0%` faster)
- `ingress_registry/register_route`: `1.4955 ms -> 723.06 us` (`~51.7%` faster)
- `ingress_registry/unregister_route`: `1.5051 ms -> 661.41 us` (`~56.1%` faster)
- `egress_forwarding/single_route_dispatch`: `263.51 ns -> 257.43 ns` (`~2.3%` faster)

## Phase 2 Exit Criteria Assessment

- No benchmark regressions in tracked hotspots: PASS
- Allocation/lookup behavior improved: PASS
- Subscriber matching and listener registration behavior unchanged: PASS
