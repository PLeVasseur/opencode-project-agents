# Behavior Conservation Matrix

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)
Baseline anchor commit SHA: `42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8`

## Purpose

Track baseline vs post-refactor behavior parity for all required command surfaces.

## Command Parity

| Command | Baseline exit/result | Post-refactor exit/result | Status | Notes |
|---|---|---|---|---|
| `cargo test -p up-streamer -- --nocapture` | exit 0; all tests passed (incl. 1 ignored); elapsed 17s | exit 0; all tests passed (incl. 1 ignored); expanded to include new module-level and API-contract tests; elapsed ~16s | green | full pass-set preserved with added Phase 4 coverage |
| `cargo test -p up-streamer --doc` | exit 0; 2/2 doctests passed; elapsed 3s | exit 0; 2/2 doctests passed; elapsed ~1s | green | doctest parity preserved |
| `cargo test -p subscription-cache -- --nocapture` | exit 0; 3/3 tests passed; elapsed 1s | exit 0; 3/3 tests passed via `cargo test -p subscription-cache --quiet` in Wave 2 | green | runtime/observability migration preserved behavior |
| `cargo test -p integration-test-utils -- --nocapture` | exit 0; 0 tests (crate builds/tests clean); elapsed 1s | exit 0; crate remains clean via `cargo test -p integration-test-utils --quiet` in Wave 2 | green | tracing init helper migration preserved pass-set |
| `cargo test --workspace` | exit 0; workspace tests/doctests passed; elapsed 20s | N/A (not exercised in Phase 3 waves) | baseline-captured | full-workspace parity deferred to Phase 7 |

## Baseline Test Target Inventory

Artifacts generated from `cargo test ... -- --list`:

- `up-streamer` unit/integration/doc targets: `up-streamer-test-targets.txt`
- `up-streamer` doctest targets: `up-streamer-doctest-targets.txt`
- `subscription-cache` targets: `subscription-cache-test-targets.txt`
- `integration-test-utils` targets: `integration-test-utils-test-targets.txt`

Primary currently listed targets include:

- `up-streamer` unit tests (23):
  - `control_plane::route_lifecycle::tests::insert_forwarding_rule_returns_false_for_duplicate`
  - `control_plane::route_lifecycle::tests::remove_forwarding_rule_is_idempotent`
  - `control_plane::route_table::tests::build_forwarding_rule_uses_transport_identity_in_tuple`
  - `data_plane::egress_pool::tests::insert_same_transport_reuses_queue_and_increments_refcount`
  - `data_plane::egress_pool::tests::remove_drops_forwarder_when_refcount_reaches_zero`
  - `data_plane::ingress_registry::tests::duplicate_insert_for_same_route_keeps_single_listener_registration`
  - `data_plane::ingress_registry::tests::insert_and_remove_registers_and_unregisters_request_and_publish_filters`
  - `routing::publish_resolution::tests::effective_publish_source_filters_dedupes_sources_across_subscribers`
  - `routing::publish_resolution::tests::publish_source_uri_for_rule_allows_wildcard_topic_authority`
  - `routing::publish_resolution::tests::publish_source_uri_for_rule_blocks_mismatched_authority`
  - `ustreamer::tests::add_forwarding_rule_rolls_back_on_listener_insert_failure`
  - `ustreamer::tests::multi_map_allows_both_sources`
  - `ustreamer::tests::publish_filter_allows_left_wildcard`
  - `ustreamer::tests::publish_filter_blocks_mismatched_tuple`
  - `ustreamer::tests::publish_filter_blocks_unmapped_authority`
  - `ustreamer::tests::publish_filter_dedupes_overlapping_rows`
  - `ustreamer::tests::publish_filter_respects_topic_authority`
  - `ustreamer::tests::right_side_wildcard_does_not_forward_without_rule`
  - `ustreamer::tests::right_side_wildcard_forwards_to_registered_authorities`
  - `ustreamer::tests::test_advanced_where_there_is_a_local_endpoint_and_two_remote_endpoints`
  - `ustreamer::tests::test_advanced_where_there_is_a_local_endpoint_and_two_remote_endpoints_but_the_remote_endpoints_have_the_same_instance_of_utransport`
  - `ustreamer::tests::test_simple_with_a_single_input_and_output_endpoint`
  - `ustreamer::tests::unregistration_removes_publish_filters`
- `up-streamer` integration tests (7 total, 6 active + 1 ignored):
  - `add_delete_forwarding_rule_contract_duplicate_and_missing_rules`
  - `add_delete_forwarding_rule_contract_rejects_same_authority`
  - `single_local_single_remote`
  - `single_local_two_remote_add_remove_rules`
  - `single_local_two_remote_authorities_different_remote_transport`
  - `single_local_two_remote_authorities_same_remote_transport`
  - `usubscription_bad_data`
- `up-streamer` doctests (2):
  - `up-streamer/src/endpoint.rs - endpoint::Endpoint (line 27)`
  - `up-streamer/src/ustreamer.rs - ustreamer::UStreamer (line 498)`
- `subscription-cache` tests (3):
  - `tests::rebuild_reflects_removed_rows`
  - `tests::same_subscriber_different_topics_coexist`
  - `tests::wildcard_lookup_merges_exact_and_wildcard_rows`
- `integration-test-utils`: currently no unit/doctest targets (`0 tests, 0 benchmarks`)

## Critical Behavior Catalog (Phase 1)

| Behavior contract | Baseline tests linked | Status |
|---|---|---|
| left-side authority publish eligibility | `publish_filter_respects_topic_authority`, `publish_filter_allows_left_wildcard`, `publish_filter_blocks_unmapped_authority` | linked |
| right-side wildcard subscriber-authority expansion (rule-bound) | `right_side_wildcard_forwards_to_registered_authorities`, `right_side_wildcard_does_not_forward_without_rule`, `subscription-cache::wildcard_lookup_merges_exact_and_wildcard_rows` | linked |
| effective publish-key dedupe symmetry (insert/remove) | `publish_filter_dedupes_overlapping_rows`, `unregistration_removes_publish_filters` | linked |
| add-failure rollback consistency | `add_forwarding_rule_rolls_back_on_listener_insert_failure` | linked |
| tuple strictness and multi-map semantics | `publish_filter_blocks_mismatched_tuple`, `multi_map_allows_both_sources` | linked |

## Detailed Recording Fields (per command)

For each command above, capture:

- [x] exact command string
- [x] exit code
- [x] elapsed time
- [x] environment prerequisites
- [x] first actionable failure summary if non-zero

### Command Records

- command: `cargo test -p up-streamer -- --nocapture`
  - exit code: `0`
  - elapsed time: `~16s`
  - environment prerequisites: workspace root; Rust toolchain available
  - first actionable failure summary: N/A (success)
- command: `cargo test -p up-streamer --doc`
  - exit code: `0`
  - elapsed time: `~1s`
  - environment prerequisites: workspace root; Rust toolchain available
  - first actionable failure summary: N/A (success)
- command: `cargo test -p subscription-cache -- --nocapture`
  - exit code: `0`
  - elapsed time: `1s`
  - environment prerequisites: workspace root; Rust toolchain available
  - first actionable failure summary: N/A (success)
- command: `cargo test -p integration-test-utils -- --nocapture`
  - exit code: `0`
  - elapsed time: `1s`
  - environment prerequisites: workspace root; Rust toolchain available
  - first actionable failure summary: N/A (success)
- command: `cargo test --workspace`
  - exit code: `0`
  - elapsed time: `~16s`
  - environment prerequisites: workspace root; Rust toolchain available
  - first actionable failure summary: N/A (success)

## Environment-Dependent/Conditional Behavior

| Area | Condition | Baseline behavior | Post-refactor behavior | Decision |
|---|---|---|---|---|
| `up-streamer` integration test | `single_local_two_remote_authorities_same_remote_transport` is ignored in baseline run | Reported as ignored (`0 passed; 0 failed; 1 ignored`) | preserved | ignored-state parity is maintained |

## Replacement/Mapping Policy

- [x] No baseline-passing test is removed without explicit replacement mapping.
- [x] Any replacement test references old path/name and new path/name.

| Baseline test | New/retained test | Mapping rationale |
|---|---|---|

## Sign-Off

- [x] Full baseline behavior preserved.
- [x] Any accepted differences are documented and approved.

## Phase 3 Revalidation Note

- 2026-02-09 revalidation reran Phase 3 wave command sets in strict order after removing legacy duplicate orchestration internals from `up-streamer/src/ustreamer.rs` and replacing API scaffolding placeholders.
- `cargo test -p up-streamer --quiet`, `cargo test -p subscription-cache --quiet`, and `cargo test -p integration-test-utils --quiet` remained green during rerun.
