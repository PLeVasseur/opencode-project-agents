# Phase 1 Inventory and Decisions

## Result

- Gate 1 status: PASS
- Runtime migration surface: fully identified.
- Projection-key placement decision: confirmed (one shared runtime key type in `up-streamer`, one local runtime key type in `usubscription-static-file`).

## Command Evidence

1. Command: `git rev-parse --abbrev-ref HEAD`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `refactor/up-streamer-domain-architecture`
   - Conclusion: Correct branch before Phase 1.

2. Command: `git status --short --branch`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `## refactor/up-streamer-domain-architecture`
   - Conclusion: Baseline status captured before Phase 1.

3. Command: `rg -n "allow\(clippy::mutable_key_type\)" up-streamer utils`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `up-streamer/src/routing/subscription_cache.rs:53`
     - `up-streamer/src/routing/subscription_cache.rs:102`
     - `up-streamer/src/routing/subscription_directory.rs:44`
     - `up-streamer/src/routing/publish_resolution.rs:77`
     - `up-streamer/src/data_plane/ingress_registry.rs:118`
     - `up-streamer/src/data_plane/ingress_registry.rs:230`
     - `utils/usubscription-static-file/src/lib.rs:84`
     - `utils/usubscription-static-file/src/lib.rs:195`
     - plus test/test-support locations (`up-streamer` test modules, `utils/usubscription-static-file` test, `utils/integration-test-utils`).
   - Conclusion: Runtime and test `mutable_key_type` allowances are present and must be migrated/scoped.

4. Command: `git show 7f91836:up-streamer/src/routing/subscription_cache.rs`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - Historical key type: `UUriIdentityKey { authority_name: String, ue_id: u32, ue_version_major: u8, resource_id: u16 }`
     - Historical subscription key uses projected topic/subscriber keys (not raw `UUri`).
   - Conclusion: Canonical pre-`0a27762` projection key pattern recovered for routing cache.

5. Command: `git show 7f91836:up-streamer/src/routing/publish_resolution.rs`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - Historical lookup: `type SourceFilterLookup = HashMap<UUriIdentityKey, UUri>`
     - Dedupe keyed by projected identity, value kept as `UUri`.
   - Conclusion: Historical publish dedupe keying model recovered.

6. Command: `git show 3ae173b:utils/usubscription-static-file/src/lib.rs`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - Historical adapter had local `UUriIdentityKey` and `SubscriptionIdentityKey`.
     - Historical field used `resource_id: u32` directly.
   - Conclusion: Local-key pattern existed historically; this run will apply canonical `u16` resource semantics per source-of-truth constraints.

7. Command: `rg -n "HashMap<\s*UUri|HashSet<\s*UUri|struct\s+SubscriptionIdentityKey|type\s+SourceFilterLookup|allow\(clippy::mutable_key_type\)" up-streamer/src/routing/subscription_cache.rs up-streamer/src/routing/publish_resolution.rs up-streamer/src/routing/subscription_directory.rs up-streamer/src/data_plane/ingress_registry.rs utils/usubscription-static-file/src/lib.rs`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `up-streamer/src/routing/subscription_cache.rs:10` (`SubscriptionIdentityKey` currently holds `UUri` values)
     - `up-streamer/src/routing/publish_resolution.rs:9` (`HashMap<UUri, UUri>`)
     - `utils/usubscription-static-file/src/lib.rs:212` (`HashMap<UUri, SubscriberInfo>`)
   - Conclusion: Runtime `UUri` keying surface is explicit and bounded to planned files.

## Classification Summary

- Runtime allowances to remove in touched paths:
  - `up-streamer/src/routing/subscription_cache.rs` (2)
  - `up-streamer/src/routing/publish_resolution.rs` (1)
  - `up-streamer/src/routing/subscription_directory.rs` (1)
  - `up-streamer/src/data_plane/ingress_registry.rs` (2)
  - `utils/usubscription-static-file/src/lib.rs` (2)
- Test/test-support allowances (may remain with rationale if needed):
  - `up-streamer/src/routing/subscription_cache.rs` test module
  - `up-streamer/src/routing/publish_resolution.rs` test module
  - `up-streamer/src/routing/subscription_directory.rs` test module
  - `utils/usubscription-static-file/src/lib.rs` test case
  - `utils/integration-test-utils/src/integration_test_utils.rs`

## Fixed Decisions Applied

- Use canonical projection field widths: `ue_version_major: u8`, `resource_id: u16`.
- Introduce one shared runtime key type in `up-streamer/src/routing/uri_identity_key.rs` reused by routing internals.
- Introduce one local runtime key type in `utils/usubscription-static-file/src/lib.rs` reused by both topic/subscriber dedupe paths.

## Phase Conclusion

Inventory completed with exact migration scope and implementation decisions locked for Phase 2 onward.
