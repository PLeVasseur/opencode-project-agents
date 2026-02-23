# Phase 3 up-streamer Runtime Migration

## Result

- Gate 3 status: PASS
- `up-streamer` runtime routing keying migrated from raw `UUri` keys to canonical projection keys.
- Runtime `mutable_key_type` allowances removed from touched `up-streamer` runtime files.

## Command Evidence

1. Command: `git rev-parse --abbrev-ref HEAD`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `refactor/up-streamer-domain-architecture`
   - Conclusion: Correct branch before Phase 3.

2. Command: `git status --short --branch`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `## refactor/up-streamer-domain-architecture`
     - `M up-streamer/src/routing/mod.rs`
     - `?? up-streamer/src/routing/uri_identity_key.rs`
   - Conclusion: Baseline state captured before migration edits.

3. Command: `cargo test -p up-streamer`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `running 23 tests`
     - `test routing::publish_resolution::tests::resolver_dedupes_sources_across_subscribers ... ok`
     - `test routing::subscription_cache::tests::wildcard_lookup_merges_exact_and_wildcard_rows ... ok`
     - `test routing::subscription_directory::tests::apply_snapshot_keeps_previous_cache_when_rebuild_fails ... ok`
     - `test data_plane::ingress_registry::tests::register_and_unregister_route_registers_and_unregisters_request_and_publish_filters ... ok`
     - `test result: ok. 23 passed; 0 failed`
   - Conclusion: Runtime behavior is preserved under focused crate validation.

4. Command: `rg -n "allow\(clippy::mutable_key_type\)" up-streamer/src/routing/subscription_cache.rs up-streamer/src/routing/publish_resolution.rs up-streamer/src/routing/subscription_directory.rs up-streamer/src/data_plane/ingress_registry.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: Production `mutable_key_type` allowances removed from touched runtime paths.

5. Command: `rg -n "HashMap<\s*UUri|HashSet<\s*UUri" up-streamer/src/routing up-streamer/src/data_plane/ingress_registry.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: No raw `UUri` map/set keying remains in migrated `up-streamer` runtime paths.

## Implemented Changes

- Added shared runtime projection key module:
  - `up-streamer/src/routing/uri_identity_key.rs`
  - wired in `up-streamer/src/routing/mod.rs`
- Migrated runtime keying:
  - `up-streamer/src/routing/subscription_cache.rs`
    - `SubscriptionIdentityKey` now uses `UriIdentityKey` for topic/subscriber identity.
  - `up-streamer/src/routing/publish_resolution.rs`
    - `SourceFilterLookup` now keyed by `UriIdentityKey`, values remain `UUri`.
- Updated call-through runtime surfaces:
  - `up-streamer/src/routing/subscription_directory.rs`
  - `up-streamer/src/data_plane/ingress_registry.rs`
  - removed runtime `#[allow(clippy::mutable_key_type)]` attributes.

## Behavior Preservation Notes

- Wildcard merge and exact-authority merge behavior in subscription lookup remains unchanged.
- Publish source derivation logic remains unchanged; only dedupe key identity switched to immutable projection.
- Route registration/unregistration request/publish listener behavior remains unchanged, validated by existing tests.

## Phase Conclusion

`up-streamer` runtime migration is complete for projection-key keying and lint-policy baseline in touched runtime paths.
