# Phase 2 Projection Key Types and Conversions

## Result

- Gate 2 status: PASS
- Projection key conversion logic added with canonical `u8`/`u16` semantics.
- Owned (`From<UUri>`) and borrowed (`From<&UUri>`) conversion paths produce identical keys.

## Command Evidence

1. Command: `git rev-parse --abbrev-ref HEAD`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `refactor/up-streamer-domain-architecture`
   - Conclusion: Correct branch before Phase 2.

2. Command: `git status --short --branch`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `## refactor/up-streamer-domain-architecture`
   - Conclusion: Baseline status captured before Phase 2 edits.

3. Command: `cargo test -p up-streamer uri_identity_key`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `running 3 tests`
     - `test routing::uri_identity_key::tests::projection_uses_canonical_major_and_resource_semantics ... ok`
     - `test routing::uri_identity_key::tests::owned_and_borrowed_projection_are_identical ... ok`
     - `test routing::uri_identity_key::tests::projection_key_hashing_dedupes_equal_projected_uris ... ok`
     - `test result: ok. 3 passed; 0 failed`
   - Conclusion: Conversion correctness/equality tests pass.

4. Command: `rg -n "to_uri\(|from_str\(" up-streamer/src/routing/uri_identity_key.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: Conversion code path does not perform parse/serialize roundtrips.

## Implemented Changes

- Added `up-streamer/src/routing/uri_identity_key.rs` with `UriIdentityKey` fields:
  - `authority_name: String`
  - `ue_id: u32`
  - `ue_version_major: u8`
  - `resource_id: u16`
- Derived `Clone, Debug, Eq, PartialEq, Hash`.
- Added explicit conversion boundaries:
  - `impl From<UUri> for UriIdentityKey` (move path; authority moved, no authority clone)
  - `impl From<&UUri> for UriIdentityKey` (borrowed path; authority clone when ownership unavailable)
- Reverse conversion was not added because no call site requires converting projected keys back to `UUri`.

## Notes

- `cargo test -p up-streamer uri_identity_key` reports a temporary `dead_code` warning for `UriIdentityKey` before runtime map migration. This is expected and resolved in Phase 3 when runtime maps are switched to this key type.

## Phase Conclusion

Projection key type and conversion boundaries are implemented and validated; runtime migration is ready.
