## Summary
- Stacked increment for smoke scope; contains smoke-suite scope equivalent to c5 with deterministic scenario claims, matrix runner, smoke CI workflow, and deferred `example-streamer-uses` readiness/sender controls.
- Finalize workspace/example logging migration for smoke binaries (`tracing-subscriber` adoption and `log`/`env_logger` removal).
- Include fixture-backed smoke assertions under `utils/transport-smoke-suite/tests/fixtures`.
- Close R5 in this commit by adding `.gitattributes` linguist collapsing rules for smoke fixtures and claims.

## Stack Context
- Current PR: #U3 (smoke layer)
- Target branch: `main`
- Depends on: #84 (transitively #83)
- Review order: #83 -> #84 -> #U3
- Incremental review scope: compare against PR #84 to isolate smoke-only additions.

## SHA note (linear stack topology)
- PR #U3 branch commit: `8011c08`
- This commit is rebased onto the benchmark layer to preserve true linear stacking.

## Validation
- PASS: `source build/envsetup.sh highest && cargo check --workspace --all-targets`
- PASS: `source build/envsetup.sh highest && cargo check -p transport-smoke-suite --all-targets`
- PASS: `source build/envsetup.sh highest && cargo test -p transport-smoke-suite --tests`
- PASS: `source build/envsetup.sh highest && cargo test --workspace`
- PASS: `source build/envsetup.sh highest && cargo clippy --all-targets -- -W warnings -D warnings`
- PASS: `source build/envsetup.sh highest && env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- SKIP (environment): unbundled clippy because `VSOMEIP_INSTALL_PATH` is unset/invalid after `source build/envsetup.sh highest`
