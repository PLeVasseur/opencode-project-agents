## Summary
- Stacked increment for benchmark scope; contains only commit c4 (`c1a61bc`) relative to the intended stack.
- Add deterministic benchmark support in `up-streamer`, Criterion bench wiring, benchmark advisory workflow, and the `utils/criterion-guardrail` crate with fixture-backed threshold checks.
- Include benchmark-scope API drift fix to call `lookup_route_subscribers_with_version(...).await.1` from `up-streamer/src/benchmark_support.rs`.
- Keep smoke-suite runner/fixtures and endpoint readiness changes out of this PR.

## Stack Context
- Current PR: #U2 (benchmark layer)
- Target branch: `main`
- Depends on: #83
- Review order: #83 -> #U2 -> #U3
- Incremental review scope: compare against PR #83 to isolate benchmark-only additions.

## Validation
- PASS: `source build/envsetup.sh highest && cargo check -p criterion-guardrail --all-targets`
- PASS: `source build/envsetup.sh highest && cargo test -p criterion-guardrail --all-targets`
- PASS: `source build/envsetup.sh highest && cargo check -p up-streamer --benches`
- PASS: `source build/envsetup.sh highest && cargo test --workspace`
- PASS: `source build/envsetup.sh highest && cargo clippy --all-targets -- -W warnings -D warnings`
- PASS: `source build/envsetup.sh highest && env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- SKIP (environment): unbundled clippy because `VSOMEIP_INSTALL_PATH` is unset/invalid after `source build/envsetup.sh highest`
