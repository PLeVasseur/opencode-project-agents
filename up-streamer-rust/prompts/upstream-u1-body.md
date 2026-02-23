## Summary
- Reconstruct the remediation stack into reviewable boundaries for commits c0-c3: mechanical tracing anchor, observability leaf module, architecture/domain extraction with subscription-cache fold-in, and deterministic test refresh.
- Preserve content identity with `cleanup/refactor-upstream-main` while removing prior mixed-concern commit boundaries that blocked review.
- Keep benchmark and smoke-heavy fixture additions out of this PR (stacked into PR #U2 and PR #U3).

## Stack Context
- Current PR: #U1 (architecture restack)
- Target branch: `main`
- Depends on: none
- Review order: #U1 -> #U2 -> #U3

## Commit-by-commit
- `fb49056` c0: mechanical `log`/`env_logger` to `tracing` anchor across a deliberately small finalizable file set.
- `cd436ae` c1: introduce `up-streamer/src/observability/*` vocabulary as a leaf review commit.
- `fba6eaf` c2: fold `subscription-cache` into `up-streamer`, extract routing/data/control/runtime modules, and rewire integration manifests without benchmark/smoke scope.
- `fd2e326` c3: finalize deterministic tests + integration helpers, complete `utils/integration-test-utils` and `utils/usubscription-static-file` logging/runtime migration, and retire workspace `async-std`.

## Reviewer feedback closure
- R1: cross-commit overlap is constrained to approved wiring exceptions and pre-approved legacy test files only; disallowed overlap is zero.
- R2: observability, architecture/rewire, benchmark, and smoke scopes are explicitly separated across PR #U1, PR #U2, and PR #U3.
- R3: no standalone copyright-fixup commit remains in reconstructed stack.
- R4: `benchmark_support.rs` creation is isolated to PR #U2 commit scope.
- R5: fixture-collapsing `.gitattributes` is deferred with smoke scope discussion in PR #U3 (source-parity constraint documented in run report).
- R6: each commit carries a non-empty body with what/why/key files/mechanical-vs-behavioral guidance.
- Dead-code remediation note: `lookup_route_subscribers` cleanup is amended into c2 (no fifth fixup commit).

## Validation
- PASS: `source build/envsetup.sh highest && cargo clippy --all-targets -- -W warnings -D warnings`
- PASS: `source build/envsetup.sh highest && env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- PASS: `source build/envsetup.sh highest && cargo test --workspace`
- SKIP (environment): unbundled clippy because `VSOMEIP_INSTALL_PATH` is unset/invalid after `source build/envsetup.sh highest`

## Compatibility notes
- MSRV remains Rust 1.88.
- Transport dependency matrix remains on current repo targets (`up-rust 0.9.x`, `up-transport-zenoh 0.9.0`, `up-transport-mqtt5 0.4.0`, `up-transport-vsomeip` pinned git rev `278ab26415559d6cb61f40facd21de822032cc83`).
