# Phase 3 - Subscription Modes and Docs

Status: completed

## Static mode

- `usubscription-static-file` remains a standalone adapter crate implementing `USubscription`.
- Static mode remains default in required configs:
  - `configurable-streamer/CONFIG.json5`
  - `example-streamer-implementations/DEFAULT_CONFIG.json5`
  - `up-linux-streamer-plugin/DEFAULT_CONFIG.json5`
- `UStreamer` constructor call sites now pass `Arc<dyn USubscription>`.

## Reserved live mode

- Config schema includes `live_usubscription` in required binaries and plugin:
  - `configurable-streamer/src/config.rs`
  - `example-streamer-implementations/src/bin/config/mod.rs`
  - `up-linux-streamer-plugin/src/config.rs`
- Required binaries and plugin fail fast with explicit deferral text when live mode is selected:
  - `configurable-streamer/src/main.rs`
  - `example-streamer-implementations/src/bin/zenoh_someip.rs`
  - `up-linux-streamer-plugin/src/lib.rs`

## Rust docs updates

- `up-streamer` rustdoc now documents:
  - **Static Configuration Mode** (`Arc<dyn USubscription>` + static adapter)
  - **Live Canonical uSubscription Mode** (`Arc<dyn USubscription>` live-client handoff)
- Docs explicitly state `refresh_subscriptions()` returns health-only metadata and canonical subscription details remain in `uSubscription`.
- Docs explicitly state `live_usubscription` is reserved/fail-fast in this migration phase.

### Documentation command evidence

1) Command:
```bash
cargo test -p up-streamer --doc
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `running 8 tests`
  - doctests passed for `up-streamer/src/lib.rs` static/live sections and domain module docs.
- Conclusion: rustdoc updates are valid and compile.

## Coupling guard proof

1) Command:
```bash
cargo tree --workspace --all-features | rg "up-subscription-rust|(^| )up-subscription v" || true
```
- Working directory: repo root
- Exit: 0
- Key output lines: none
- Conclusion: no direct `up-subscription-rust`/`up-subscription` crate dependency in workspace manifests.

2) Command:
```bash
rg -n "subscription-cache" Cargo.toml up-streamer/Cargo.toml utils/usubscription-static-file/Cargo.toml || true
```
- Working directory: repo root
- Exit: 0
- Key output lines: none
- Conclusion: `subscription-cache` is removed from workspace/target manifests.

3) Command:
```bash
cargo tree -i usubscription-static-file
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `usubscription-static-file ...`
  - `up-streamer` appears only under `[dev-dependencies]`.
- Conclusion: `up-streamer` has no runtime dependency on `usubscription-static-file`; only dev/test usage remains.

4) Command:
```bash
rg -n "static_file" configurable-streamer/CONFIG.json5 example-streamer-implementations/DEFAULT_CONFIG.json5 up-linux-streamer-plugin/DEFAULT_CONFIG.json5
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - each required config contains `mode: "static_file"`
- Conclusion: static mode is the default across required binaries/plugin.

5) Command:
```bash
rg -n "live_usubscription mode is reserved" configurable-streamer/src/main.rs example-streamer-implementations/src/bin/zenoh_someip.rs up-linux-streamer-plugin/src/lib.rs
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - each required runtime path contains explicit reserved/deferred fail-fast message.
- Conclusion: reserved live mode behavior is implemented with explicit guidance.

## Gate 3 conclusion

Gate status: pass.

- Static mode and reserved live mode are implemented and documented.
- Workspace topology target remains satisfied (`subscription-cache` removed, `usubscription-static-file` retained).
- Required streamer binaries expose deterministic reserved `live_usubscription` fail-fast behavior.
