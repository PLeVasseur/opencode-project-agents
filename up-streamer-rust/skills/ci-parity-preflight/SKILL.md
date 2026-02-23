---
name: ci-parity-preflight
description: Run the local command matrix that mirrors bundled and unbundled CI lint/build checks before push.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: ci-preflight
---

## When to use

Use this skill for transport, plugin, feature-gating, or dependency-version changes that can affect CI matrix behavior.

## Workflow

1. Run from repo root.
2. Prepare environment:
   - `source build/envsetup.sh highest`
3. Base matrix (no transport features):
   - `cargo build`
   - `cargo clippy --all-targets -- -W warnings -D warnings`
   - `cargo fmt -- --check`
4. Bundled transport matrix:
   - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
   - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
5. Unbundled transport matrix (when transport/plugin code changed):
   - Set `VSOMEIP_INSTALL_PATH` to a valid vsomeip install tree.
   - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
   - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
6. Workspace sanity:
   - `cargo check --workspace --all-targets`
   - `cargo test --workspace`

## Guardrails

- Treat no-feature clippy and feature-enabled clippy as separate gates; passing one does not imply passing the other.
- If CI fails after local green, diff local command set against workflow YAML and rerun with exact flags.

## Report template

Always capture:

1. Commands run
2. Pass/fail outcomes
3. Any environment variables used (`VSOMEIP_INSTALL_PATH`, stdlib paths)
4. If skipped, why skipped
