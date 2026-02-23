## Test evidence

Date: 2026-02-09
Branch: `bugfix/issue-74-left-topic-authority`

### Fail-before evidence (pre-runtime)

- `cargo test -p up-streamer right_side_wildcard -- --nocapture` -> failed (`left: 0`, `right: 2`) in both right-side wildcard tests.
- `cargo test -p up-streamer publish_filter_dedupes_overlapping_rows -- --nocapture` -> failed (`insert(...).is_ok()` assertion).
- `cargo test -p up-streamer add_forwarding_rule_rolls_back_on_listener_insert_failure -- --nocapture` -> failed (`left: 1`, `right: 0` stale-state assertion).

Saved logs:

- `prechange-right-wildcard.log`
- `prechange-dedupe.log`
- `prechange-add-rollback.log`

### Pass-after evidence (post-runtime)

Command outcomes:

```text
cargo test -p up-streamer right_side_wildcard -- --nocapture                                ok (2 passed)
cargo test -p up-streamer publish_filter_blocks_mismatched_tuple -- --nocapture             ok (1 passed)
cargo test -p up-streamer multi_map_allows_both_sources -- --nocapture                      ok (1 passed)
cargo test -p up-streamer publish_filter_dedupes_overlapping_rows -- --nocapture            ok (1 passed)
cargo test -p up-streamer add_forwarding_rule_rolls_back_on_listener_insert_failure -- --nocapture  ok (1 passed)
cargo test -p up-streamer publish_filter_ -- --nocapture                                     ok (5 passed)
cargo test -p up-streamer unregistration_removes_publish_filters -- --nocapture              ok (1 passed)
cargo test -p up-streamer --test single_local_two_remote_add_remove_rules -- --nocapture    ok (1 passed)
cargo test -p subscription-cache -- --nocapture                                              ok (3 passed)
cargo test -p up-streamer -- --nocapture                                                     ok (13 unit + integration/doc tests passing)
```

### Assertion-to-test mapping

- A (`right_side_wildcard_forwards_to_registered_authorities`, `right_side_wildcard_does_not_forward_without_rule`): validates right-side wildcard subscriber authority expansion (`//*/...`) for registered destinations only.
- B (`publish_filter_blocks_mismatched_tuple`): validates strict tuple matching; mismatched `ue_id`, `version`, or `resource` register counts remain `0`.
- C (`multi_map_allows_both_sources`): validates both A and C source topics register independently for shared destination authority.
- D (`publish_filter_dedupes_overlapping_rows`): validates duplicate effective publish key registers/unregisters exactly once despite overlapping rows.
- E (`add_forwarding_rule_rolls_back_on_listener_insert_failure`): validates failed add leaves no stale forwarding-rule entry and no leaked transport-forwarder count; retry succeeds after failure removal.

### Path A cache semantics checks

- `same_subscriber_different_topics_coexist`: same subscriber with two topics remains two rows.
- `rebuild_reflects_removed_rows`: rebuilt cache reflects row removal from updated payload.
- `wildcard_lookup_merges_exact_and_wildcard_rows`: merged lookup returns exact+wildcard subscriber-authority rows.
