# Phase 4 Clippy Allow Remnants and Lint Cleanup

Date: 2026-02-10

## Burn-down actions completed

- Removed avoidable `#[allow(dead_code)]` in `up-linux-streamer-plugin/src/lib.rs` by deleting unused fields.
- Removed avoidable `#[allow(clippy::too_many_arguments)]` in `utils/integration-test-utils/src/integration_test_utils.rs` by introducing `SendMessageContext` and reducing argument count.
- Removed production `clippy::mutable_key_type` allowances from routing/cache/static-subscription code by switching dedupe/indexing to immutable identity keys with hash maps/sets.
- Restored O(1)-capable external lookup interfaces after review feedback by returning hash-indexed lookups in subscription cache/directory/resolution boundaries.

## Verification evidence

### 1) Source allow inventory

- exact command: `rg -n "#\\!\\[allow\\(|#\\[allow\\(" . --glob "*.rs" --glob "!target/**"`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./example-streamer-uses/src/bin/common/cli.rs:79:#[allow(dead_code)]`
  - `./up-streamer/tests/support/mod.rs:22:#[allow(dead_code)]`
  - `./utils/integration-test-utils/src/integration_test_utils.rs:67:#[allow(clippy::mutable_key_type)]`
- concise conclusion: All remaining `allow` attributes are in test/example-only code paths; none remain in production crates.

### 2) Strict workspace clippy

- exact command: `cargo clippy --workspace --all-targets --all-features -- -W warnings -D warnings`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `Checking usubscription-static-file v0.1.0 (...)`
  - `Checking up-streamer v0.1.0 (...)`
  - `Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 4.94s`
- concise conclusion: Workspace is strict-clippy clean after removing production `allow` remnants.

### 3) O(1) interface restoration evidence

- exact command: `rg -n "pub type SubscriptionLookup|pub fn fetch_cache_entry\(|pub fn fetch_cache_entry_with_wildcard\(" subscription-cache/src/lib.rs`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `63:pub type SubscriptionLookup = HashMap<SubscriptionIdentityKey, SubscriptionInformation>;`
  - `189:    pub fn fetch_cache_entry(&self, entry: String) -> Option<SubscriptionLookup> {`
  - `197:    pub fn fetch_cache_entry_with_wildcard(&self, entry: &str) -> Option<SubscriptionLookup> {`
- concise conclusion: `subscription-cache` now exposes hash-indexed lookup interfaces (O(1)-capable).

- exact command: `rg -n "lookup_route_subscribers\(|type SourceFilterLookup|derive_source_filters\(" up-streamer/src/routing/subscription_directory.rs up-streamer/src/routing/publish_resolution.rs`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `up-streamer/src/routing/publish_resolution.rs:8:pub(crate) type SourceFilterLookup = HashMap<UUriIdentityKey, UUri>;`
  - `up-streamer/src/routing/subscription_directory.rs:22:    pub(crate) async fn lookup_route_subscribers(`
  - `up-streamer/src/routing/publish_resolution.rs:76:    pub(crate) fn derive_source_filters(`
- concise conclusion: routing interfaces now pass hash-indexed lookups instead of linear-only collections.

- exact command: `rg -n "for source_uri in publish_source_filters\.into_values\(\)" up-streamer/src/data_plane/ingress_registry.rs`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `189:        for source_uri in publish_source_filters.into_values() {`
  - `289:                for source_uri in publish_source_filters.into_values() {`
- concise conclusion: ingress registry consumes hash lookup values directly without requiring vector-based dedupe pathways.

## Required remnant inventory (line-level)

| lint name | exact file:line | technical reason it must remain now | alternatives attempted | owner/follow-up action |
|---|---|---|---|---|
| `dead_code` | `example-streamer-uses/src/bin/common/mod.rs:13` | Shared helper type is intentionally used by some example binaries but not all; all-targets clippy compiles each bin independently. | Removed allow and reran strict clippy; failures occurred in bins not using this listener type. | `example-streamer-uses` maintainers: split shared listeners into role-specific modules. |
| `dead_code` | `example-streamer-uses/src/bin/common/mod.rs:33` | Same shared-module topology issue across service/client/publisher/subscriber example binaries. | Removed allow and reran strict clippy; responder flagged unused in non-service bins. | `example-streamer-uses` maintainers: isolate service-only helpers. |
| `dead_code` | `example-streamer-uses/src/bin/common/mod.rs:38` | Constructor is required where responder is used but appears unused in binaries that do not instantiate it. | Removed allow and reran strict clippy; constructor flagged unused in non-service bins. | `example-streamer-uses` maintainers: colocate constructor with service-only module. |
| `dead_code` | `example-streamer-uses/src/bin/common/mod.rs:76` | Publish listener helper is subscriber-flow specific and unused in non-subscriber example binaries. | Removed allow and reran strict clippy; helper flagged unused in non-subscriber bins. | `example-streamer-uses` maintainers: split subscriber helpers into dedicated module. |
| `dead_code` | `example-streamer-uses/src/bin/common/cli.rs:79` | SOME/IP CLI helper is transport-specific and unused in every compiled example target. | Removed allow and reran strict clippy; helper flagged unused in bins without SOME/IP flow. | `example-streamer-uses` maintainers: move SOME/IP-only helpers to transport-specific module. |
| `dead_code` | `up-streamer/tests/support/mod.rs:22` | Test support helper is used by selected integration tests but not all test binaries. | Removed allow and reran strict clippy; helper flagged unused in unaffected test targets. | `up-streamer` test maintainers: split support helpers by test suite scope. |
| `clippy::mutable_key_type` | `utils/integration-test-utils/src/integration_test_utils.rs:67` | Test utility groups messages by `UUri`; this is test-harness-only behavior and not production runtime logic. | Kept as test-only exception after production code migrated to immutable key indexes. | `integration-test-utils` maintainers: optional follow-up to mirror immutable key wrappers in test helpers. |
