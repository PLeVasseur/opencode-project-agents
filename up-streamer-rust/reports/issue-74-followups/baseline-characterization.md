## Baseline characterization

Date: 2026-02-09
Branch: `bugfix/issue-74-left-topic-authority`
Canonical PR: <https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77>

### Baseline branch/state

Command: `git status --short`

Output:

```text
(clean working tree)
```

Command: `git log --oneline -10`

Output:

```text
f470b22 chore: remove issue-74 mentions from docs and tests
a553a37 fix integration harness listener unregister symmetry
c51bfc8 document issue74 runbook and CLI override usage
c026489 fix publish forwarding authority matching in streamer
08b3c0e parameterize remaining example binaries for CLI overrides
b134d5a parameterize MQTT and Zenoh pubsub binaries
0d441dc add shared CLI parsing helpers for example binaries
5f7e6b6 ci: simplify bundled lint aggregator checks
ec4af3b ci: trim unbundled lint apt deps
9578b4d ci: harden bundled lint cleanup for vsomeip artifacts
```

### Baseline code pointers

Command:

`rg -n "fetch_cache_entry|publish_source_uri_for_rule|register_listener\(|unregister_listener\(" subscription-cache/src/lib.rs up-streamer/src/ustreamer.rs`

`rg -n "add_forwarding_rule\(|forwarding_listeners\.insert\(|transport_forwarders\.insert\(" up-streamer/src/ustreamer.rs`

Key hits:

```text
up-streamer/src/ustreamer.rs:194:    fn publish_source_uri_for_rule(
up-streamer/src/ustreamer.rs:266:            .register_listener(
up-streamer/src/ustreamer.rs:304:            .fetch_cache_entry(out_authority.into())
up-streamer/src/ustreamer.rs:332:                .register_listener(&source_uri, None, forwarding_listener.clone())
up-streamer/src/ustreamer.rs:428:                    .fetch_cache_entry(out_authority.into())
up-streamer/src/ustreamer.rs:453:                        .unregister_listener(&source_uri, None, forwarding_listener.clone())
subscription-cache/src/lib.rs:144:    pub fn fetch_cache_entry(&self, entry: String) -> Option<HashSet<SubscriptionInformation>> {
up-streamer/src/ustreamer.rs:365:        forwarding_listeners.insert(
up-streamer/src/ustreamer.rs:798:    pub async fn add_forwarding_rule(
```

### Baseline coverage gap

Command: `rg -n "right_side_wildcard|publish_filter_blocks_mismatched_tuple|multi_map_allows_both_sources|publish_filter_dedupes_overlapping_rows|add_forwarding_rule_rolls_back_on_listener_insert_failure" up-streamer/src/ustreamer.rs`

Output:

```text
(no matches)
```

Conclusion: follow-up A/B/C/D/E regression tests are not yet present under the expected names.
