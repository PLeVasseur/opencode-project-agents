# Behavior Owner Traceability

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Ensure every preserved behavior has a clear owner and one logical change point.

## Traceability Table

| Behavior | Owning module/file | Single logical change point | Primary tests | Secondary tests/docs |
|---|---|---|---|---|
| left-side authority publish eligibility | `up-streamer/src/routing/publish_resolution.rs` | `publish_source_uri_for_rule` authority gate | `routing::publish_resolution::tests::publish_source_uri_for_rule_blocks_mismatched_authority`, `ustreamer::tests::publish_filter_respects_topic_authority` | `ustreamer::tests::publish_filter_allows_left_wildcard` |
| right-side wildcard subscriber-authority expansion | `up-streamer/src/routing/subscription_directory.rs` + `up-streamer/src/data_plane/ingress_registry.rs` | `fetch_subscribers_for_authority` merge + listener registration loop in `ForwardingListeners::insert` | `ustreamer::tests::right_side_wildcard_forwards_to_registered_authorities` | `ustreamer::tests::right_side_wildcard_does_not_forward_without_rule`, `subscription-cache::tests::wildcard_lookup_merges_exact_and_wildcard_rows` |
| dedupe symmetry register/unregister | `up-streamer/src/routing/publish_resolution.rs` + `up-streamer/src/data_plane/ingress_registry.rs` | `effective_publish_source_filters` + `ForwardingListeners::remove` | `routing::publish_resolution::tests::effective_publish_source_filters_dedupes_sources_across_subscribers` | `ustreamer::tests::publish_filter_dedupes_overlapping_rows`, `ustreamer::tests::unregistration_removes_publish_filters` |
| add-failure rollback consistency | `up-streamer/src/ustreamer.rs` | `UStreamer::add_forwarding_rule` rollback path after listener insert failure | `ustreamer::tests::add_forwarding_rule_rolls_back_on_listener_insert_failure` | `up-streamer/tests/usubscription.rs::usubscription_bad_data` |
| tuple strictness | `up-streamer/src/routing/publish_resolution.rs` | `publish_source_uri_for_rule` + strict `UUri::try_from_parts` tuple mapping | `ustreamer::tests::publish_filter_blocks_mismatched_tuple` | `routing::publish_resolution::tests::publish_source_uri_for_rule_allows_wildcard_topic_authority` |
| multi-map union behavior | `subscription-cache/src/lib.rs` + `up-streamer/src/routing/subscription_directory.rs` | `SubscriptionCache::fetch_cache_entry_with_wildcard` and authority fetch adapter | `ustreamer::tests::multi_map_allows_both_sources` | `subscription-cache::tests::same_subscriber_different_topics_coexist` |
| authority listener lifecycle | `up-streamer/src/data_plane/ingress_registry.rs` | `ForwardingListeners::{insert,remove}` refcount and register/unregister symmetry | `data_plane::ingress_registry::tests::insert_and_remove_registers_and_unregisters_request_and_publish_filters` | `up-streamer/tests/api_contract_forwarding_rules.rs` |
| forwarder pool reference lifecycle | `up-streamer/src/data_plane/egress_pool.rs` | `TransportForwarders::{insert,remove}` active-count transitions | `data_plane::egress_pool::tests::insert_same_transport_reuses_queue_and_increments_refcount` | `data_plane::egress_pool::tests::remove_drops_forwarder_when_refcount_reaches_zero` |

## Verification Checklist

- [x] Every baseline behavior mapped to owner.
- [x] Every owner has explicit primary tests.
- [x] No behavior maps to multiple conflicting owners.
- [x] Change-point map aligned with `architecture-blueprint.md`.
- [x] No behavior owner remains duplicated in `up-streamer/src/ustreamer.rs` after extraction.
- [ ] Each behavior can be changed in one logical module/file without cross-cutting edits.
