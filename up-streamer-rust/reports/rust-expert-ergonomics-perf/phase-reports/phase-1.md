# Phase 1 Report

Date: 2026-02-11
Phase: 1 - Correctness hardening first
Result: PASS (after one blocking check failure was remediated)

## Scope Implemented

- `up-linux-streamer-plugin/src/lib.rs`
  - Plugin runtime is now owned in `RunningPlugin` state (`tokio_runtime: Option<Runtime>`), not dropped at end of `start()`.
  - Startup/runtime `panic!/expect/unwrap` paths in plugin runtime flow were converted to fallible `ZResult` propagation.
  - Plugin `Drop` now signals stop and performs bounded runtime shutdown.
- `up-streamer/src/data_plane/ingress_registry.rs`
  - Registry bindings now persist exact listener filters registered per route binding.
  - Unregister path uses persisted filters directly (no recomputation from updated subscription snapshot).
  - Added focused regression test: `unregister_route_uses_registered_filters_after_snapshot_change`.
- `up-streamer/src/ustreamer.rs`
  - Same-authority error wording now reflects operation intent (`Unable to add.` vs `Unable to delete.`).

## Evidence

### 1) Phase start branch/status

- exact command: `git rev-parse --abbrev-ref HEAD && git status --short --branch`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture`
- concise conclusion: Phase 1 started on the pinned execution branch with a clean tree.

### 2) Targeted verification - ingress registry

- exact command: `source build/envsetup.sh highest && cargo test -p up-streamer ingress_registry`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `test ... duplicate_register_route_keeps_single_listener_registration ... ok`
  - `test ... register_and_unregister_route_registers_and_unregisters_request_and_publish_filters ... ok`
  - `test ... unregister_route_uses_registered_filters_after_snapshot_change ... ok`
- concise conclusion: Ingress registry refcount and exact unregister filter semantics are validated.

### 3) Targeted verification - ustreamer

- exact command: `source build/envsetup.sh highest && cargo test -p up-streamer ustreamer`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `running 5 tests`
  - `test ustreamer::tests::... ... ok` (all five)
  - `test result: ok. 5 passed; 0 failed`
- concise conclusion: UStreamer health and core route-path behavior tests remain green.

### 4) Strict clippy on `up-streamer`

- exact command: `source build/envsetup.sh highest && cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Checking up-streamer v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo]`
- concise conclusion: No new lint debt introduced in `up-streamer`.

### 5) Plugin feature check (initial blocking failure)

- exact command: `source build/envsetup.sh highest && cargo check -p up-linux-streamer-plugin --all-targets --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
- working directory: repo root
- exit status / pass-fail: `101` / FAIL (blocking)
- key output lines:
  - `error[E0308]: mismatched types`
  - `expected 'Box<dyn IError + Send + Sync>', found 'ZError'`
  - failure sites in `up-linux-streamer-plugin/src/lib.rs` for `return Err(zerror!(...))`
- concise conclusion: Gate failed due to direct `Err(zerror!(...))` returns in a `ZResult` path requiring boxed error conversion.

### 6) Blocker remediation and re-check

- exact command: `source build/envsetup.sh highest && cargo check -p up-linux-streamer-plugin --all-targets --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Checking up-linux-streamer-plugin v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo]`
- concise conclusion: Blocker resolved by converting direct returns to `return Err(zerror!(...).into())`.

### 7) Post-phase formatting gate

- exact command: `source build/envsetup.sh highest && cargo fmt -- --check`
- working directory: repo root
- exit status / pass-fail: `0` / PASS (after formatting)
- key output lines:
  - no diff output on final run
- concise conclusion: Source formatting is clean for Phase 1 changes.

## Phase 1 Exit Criteria Assessment

- Plugin runtime path lifecycle-safe and panic-light: PASS
- Listener teardown correctness covered and passing: PASS
