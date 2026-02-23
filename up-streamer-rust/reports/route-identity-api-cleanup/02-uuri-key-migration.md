# Phase 2 - Replace URI identity wrappers with `UUri`

## Phase pre-check

1) Command: `git rev-parse --abbrev-ref HEAD`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
- Conclusion: phase started on required branch.

2) Command: `git status --short --branch`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture`
- Conclusion: phase baseline captured.

## Migration evidence

3) Command: `rg -n "struct SubscriptionIdentityKey|topic: UUri|subscriber: Option<UUri>" up-streamer/src/routing/subscription_cache.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `10:pub(crate) struct SubscriptionIdentityKey {`
  - `11:    topic: UUri,`
  - `12:    subscriber: Option<UUri>,`
- Conclusion: `subscription_cache` keying now uses `UUri` directly.

4) Command: `rg -n "SourceFilterLookup|HashMap<UUri, UUri>|entry\(source_uri\.clone\)" up-streamer/src/routing/publish_resolution.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `9:pub(crate) type SourceFilterLookup = HashMap<UUri, UUri>;`
- Conclusion: publish source filter dedupe map now keys directly on `UUri`.

5) Command: `rg -n "struct SubscriptionIdentityKey|topic: UUri|subscriber: UUri|requested_topic_identity = canonical_topic|HashMap<UUri, SubscriberInfo>" utils/usubscription-static-file/src/lib.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `31:struct SubscriptionIdentityKey {`
  - `32:    topic: UUri,`
  - `33:    subscriber: UUri,`
  - `207:        let requested_topic_identity = canonical_topic;`
  - `210:        let mut subscribers_by_key: HashMap<UUri, SubscriberInfo> = HashMap::new();`
- Conclusion: static-file adapter dedupe and `fetch_subscribers` identity now use `UUri` keys directly.

6) Command: `rg -n "UUriIdentityKey" up-streamer/src/routing/subscription_cache.rs up-streamer/src/routing/publish_resolution.rs utils/usubscription-static-file/src/lib.rs || true`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - (no matches)
- Conclusion: `UUriIdentityKey` is removed from all targeted files.

## Behavior protection evidence

7) Command: `rg -n "same_subscriber_different_topics_coexist|rebuild_reflects_removed_rows|wildcard_lookup_merges_exact_and_wildcard_rows" up-streamer/src/routing/subscription_cache.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `159:    fn same_subscriber_different_topics_coexist() {`
  - `183:    fn rebuild_reflects_removed_rows() {`
  - `213:    fn wildcard_lookup_merges_exact_and_wildcard_rows() {`
- Conclusion: routing-cache behavior tests for coexistence/rebuild/wildcard merge remain in place.

8) Command: `rg -n "fetch_subscribers_dedupes_duplicate_subscribers_after_topic_normalization" utils/usubscription-static-file/src/lib.rs`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `269:    async fn fetch_subscribers_dedupes_duplicate_subscribers_after_topic_normalization() {`
- Conclusion: adapter dedupe regression test was added.

9) Command: `cargo test -p up-streamer`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `test routing::subscription_cache::tests::same_subscriber_different_topics_coexist ... ok`
  - `test routing::subscription_cache::tests::rebuild_reflects_removed_rows ... ok`
  - `test routing::subscription_cache::tests::wildcard_lookup_merges_exact_and_wildcard_rows ... ok`
  - `test result: ok. 18 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out`
- Conclusion: `up-streamer` behavior remains stable after URI key migration.

10) Command: `cargo test -p usubscription-static-file`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `test tests::fetch_subscribers_dedupes_duplicate_subscribers_after_topic_normalization ... ok`
  - `test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out`
- Conclusion: static-file dedupe behavior remains correct with direct `UUri` keys.

## Gate 2 decision

- Result: **PASS**
- Rationale: targeted files now use `UUri` keys directly, `UUriIdentityKey` is removed from touched files, and focused tests passed.
