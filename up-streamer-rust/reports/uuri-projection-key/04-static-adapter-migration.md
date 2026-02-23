# Phase 4 usubscription-static-file Runtime Migration

## Result

- Gate 4 status: PASS
- Static adapter runtime dedupe keying migrated to local immutable projection keys.
- Runtime `mutable_key_type` allowances removed from production adapter paths.

## Command Evidence

1. Command: `git rev-parse --abbrev-ref HEAD`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `refactor/up-streamer-domain-architecture`
   - Conclusion: Correct branch before Phase 4.

2. Command: `git status --short --branch`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `## refactor/up-streamer-domain-architecture`
     - staged/unstaged runtime migration edits visible in `up-streamer` before static adapter work.
   - Conclusion: Baseline captured before Phase 4 adapter migration.

3. Command: `cargo test -p usubscription-static-file`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `running 3 tests`
     - `test tests::uri_projection_key_uses_canonical_major_and_resource_semantics ... ok`
     - `test tests::uri_projection_key_owned_and_borrowed_conversion_match ... ok`
     - `test tests::fetch_subscribers_dedupes_duplicate_subscribers_after_topic_normalization ... ok`
     - `test result: ok. 3 passed; 0 failed`
   - Conclusion: Adapter runtime behavior and key conversion semantics are validated.

4. Command: `rg -n "allow\(clippy::mutable_key_type\)" utils/usubscription-static-file/src/lib.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: No `mutable_key_type` allowances remain in this adapter file.

5. Command: `rg -n "HashMap<\s*UUri|HashSet<\s*UUri" utils/usubscription-static-file/src/lib.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: Runtime dedupe maps no longer key on raw `UUri`.

## Implemented Changes

- Added one local runtime projection key type:
  - `UriProjectionKey { authority_name: String, ue_id: u32, ue_version_major: u8, resource_id: u16 }`
  - with `From<UUri>` and `From<&UUri>` conversion boundaries.
- Kept one local subscription identity wrapper:
  - `SubscriptionIdentityKey { topic: UriProjectionKey, subscriber: UriProjectionKey }`
  - reused for topic/subscriber projection in static subscription dedupe.
- Migrated runtime dedupe map keying:
  - `parse_static_subscriptions`: `HashMap<SubscriptionIdentityKey, Subscription>`
  - `fetch_subscribers`: `HashMap<UriProjectionKey, SubscriberInfo>`
- Preserved behavior:
  - topic resource-id normalization to fixed static resource id
  - dedupe of duplicate subscriber rows after normalization
  - response values remain `UUri` via `SubscriberInfo`.

## Move-Path Note

- Move-path conversion is used where ownership is not retained (for normalized requested-topic projection in `fetch_subscribers`).
- Borrowed conversion is used where `UUri` must remain in produced values (`Subscription`/`SubscriberInfo`).

## Phase Conclusion

Static adapter runtime keying and dedupe internals are migrated to canonical immutable projection keys with behavior preserved.
