# PR-83 up-rust idiomatic usage sweep validation log

Date: 2026-02-17
Repository: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/83

## Startup checkpoint

- Expected branch: `cleanup/refactor-upstream-main-prA-architecture`
- Current branch: `cleanup/refactor-upstream-main-prA-architecture`
- Base SHA (`upstream/main`): `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`
- Branch start SHA: `fd2e32649a7a26ad3c4897f1b4b05790141ee07c`
- Remote branch SHA: `fd2e32649a7a26ad3c4897f1b4b05790141ee07c`
- Local rollback tag: `pr-83-sweep-start-20260217T140717Z`

## Command outcomes

- [x] Branch lock and upstream tracking validated.
- [x] Clean working tree at sweep start.
- [x] Branch start and remote tip match.
- [x] Local rollback tag created.
- [x] Discovery inventory complete.
- [x] Standards lock complete.
- [x] Implementation complete.
- [x] Validation matrix complete (fast gates + doctests + bundled matrix + workspace test).
- [ ] Squash and pre-push checks complete.

## Additional validation runs (post-exemption removal)

- [x] Doctest mock migration to `up_rust::MockTransport` completed in targeted modules.
- [x] `up-streamer/Cargo.toml` updated with dev-only `up-rust` `test-util` feature wiring.
- [x] `cargo test -p up-streamer --doc` passes after migration.
- [x] `cargo clippy --all-targets -- -W warnings -D warnings` passes.
- [x] `cargo check --workspace --all-targets` passes.

## Command trace highlights

- `cargo test -p up-streamer --doc`
  - Result: pass (`8 passed; 0 failed`).
- `cargo clippy --all-targets -- -W warnings -D warnings`
  - Result: pass.
- `cargo check --workspace --all-targets`
  - Result: pass.
- `source build/envsetup.sh highest && cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport && cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - Result: pass.
- `source build/envsetup.sh highest && cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport && cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (post-doctest-mock migration rerun)
  - Result: pass.
- `cargo check --workspace --all-targets && cargo test --workspace`
  - Result: pass (workspace tests green; expected ignored tests unchanged).
- `source build/envsetup.sh highest && cargo build && cargo clippy --all-targets -- -W warnings -D warnings && cargo fmt -- --check`
  - Result: pass.
- `source build/envsetup.sh highest && cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport && cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (post-local-commit rerun)
  - Result: pass.
- `cargo check --workspace --all-targets && cargo test --workspace && cargo test -p up-streamer --doc`
  - Result: pass.
- Unbundled transport matrix
  - Result: not run for this sweep; skipped intentionally because touched scope is accessor/helper/doctest modernization and does not modify transport/plugin integration codepaths.

## Repository-wide sweep verification

- `grep: attributes.as_ref(), type_.enum_value_or_default(), authority_name == "*", nested .id/.source/.sink as_ref chains, attributes.as_ref().unwrap()`
  - Result: no remaining matches for targeted anti-pattern classes.
- `grep: struct MockTransport / impl UTransport for MockTransport`
  - Result: no remaining custom local mock transport stubs in workspace code/docs.

## Branch/remote guard status

- `git fetch origin cleanup/refactor-upstream-main-prA-architecture && test origin-head == BRANCH_START_SHA`
  - Result: pass (`REMOTE_BASE_UNCHANGED`).
- `git fetch origin cleanup/refactor-upstream-main-prA-architecture && test origin-head == BRANCH_START_SHA` (post-L4 recheck)
  - Result: pass (`REMOTE_BASE_UNCHANGED`).
- Current publication posture
  - Local phased commits were squashed into one remediation commit.
  - Push is intentionally deferred.

## Squash execution and integrity checks

- `git tag pr-83-pre-squash-20260217T161524Z a6dccccd49e25c27b33414199e24a9d21d6ab239`
  - Result: pass (rollback anchor recorded).
- `git reset --soft fd2e32649a7a26ad3c4897f1b4b05790141ee07c && git commit ...`
  - Result: pass; squashed commit `87e0b7e` created.
- Squash commit rationale coverage
  - Result: commit body includes explicit rationale for retained direct-field usages (owned-move allocation avoidance, mutable ID setter gap, full `ue_id` helper gap, resource canonicalization setter gap).
- `git rev-list --count fd2e32649a7a26ad3c4897f1b4b05790141ee07c..HEAD`
  - Result: `1` (single remediation commit ahead of branch start).
- `git diff --name-status a6dccccd49e25c27b33414199e24a9d21d6ab239..HEAD`
  - Result: empty (tree parity with pre-squash tip).

## Local phase commits

- `abea334` - `refactor: use canonical up-rust accessors in observability and routing`
- `4971cf1` - `refactor: standardize test utilities on up-rust message and URI helpers`
- `f45f40d` - `docs: adopt up-rust MockTransport for hidden doctest setup`
- `a6dcccc` - `refactor: close residual up-rust accessor gaps`

## Residual closure pass (Workstream F)

- Converted residual easy-accessor sites.
  - `up-streamer/src/data_plane/ingress_listener.rs` switched SHM payload check to `msg.payload_format().unwrap_or_default()`.
  - `up-streamer/src/routing/subscription_cache.rs` switched borrowed authority clone to `uri.authority_name()`.
  - `up-streamer/src/routing/uri_identity_key.rs` switched borrowed authority clone to `uri.authority_name()`.
  - `utils/usubscription-static-file/src/lib.rs` switched borrowed authority clone to `uri.authority_name()`.
  - `example-streamer-uses/src/bin/common/cli.rs` switched authority assertion to `uuri.authority_name()`.
- Re-ran validation after residual closure.
  - `cargo fmt -- --check` -> pass.
  - `cargo clippy --all-targets -- -W warnings -D warnings && cargo check --workspace --all-targets && cargo test -p up-streamer --doc` -> pass.
  - `source build/envsetup.sh highest && cargo build && cargo clippy --all-targets -- -W warnings -D warnings && cargo fmt -- --check` -> pass.
  - `source build/envsetup.sh highest && cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport && cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` -> pass.
  - `cargo check --workspace --all-targets && cargo test --workspace` -> pass.
  - Post-L4 commit fast gates: `cargo fmt -- --check && cargo clippy --all-targets -- -W warnings -D warnings && cargo check --workspace --all-targets` -> pass.
  - Post-L4 commit doctests: `cargo test -p up-streamer --doc` -> pass.
- Residual closure grep matrix results.
  - Original PR-83 anti-pattern checks (`attributes.as_ref`, raw enum default chains, wildcard literal compares, local custom mock transport) -> no matches.
  - Direct `authority_name` field usage -> reduced to approved-only owned-move sites listed in exemptions.
  - Direct `attributes` field usage -> reduced to approved-only mutable test-helper site listed in exemptions.
  - Direct full `ue_id` reads and `resource_id` canonicalization writes -> approved-only sites listed in exemptions.
