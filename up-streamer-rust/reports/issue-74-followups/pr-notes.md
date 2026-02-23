## PR notes draft for https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77

### What changed

- Added right-side wildcard subscriber-authority support only (`//*/...` on the right side). Forwarding lookup now merges exact subscriber authority `<out_authority>` with wildcard subscriber authority `*`.
- Added effective publish listener-key dedupe in both register and unregister paths so overlapping rows do not trigger duplicate listener registration/unregistration attempts.
- Added explicit rollback consistency in `add_forwarding_rule`: if listener insertion fails, the just-added forwarding rule and acquired transport-forwarder reference are rolled back.
- Adopted DG-1 Path A cache identity semantics (`topic + subscriber`) and added cache rebuild/removal reflection coverage.

### Assertion outcomes (A/B/C/D/E)

- A: `right_side_wildcard_forwards_to_registered_authorities`, `right_side_wildcard_does_not_forward_without_rule` now pass.
- B: `publish_filter_blocks_mismatched_tuple` confirms strict tuple matching (`ue_id`, `version`, `resource` mismatch does not forward).
- C: `multi_map_allows_both_sources` confirms both sources forward to the shared destination authority when both map rows/rules exist.
- D: `publish_filter_dedupes_overlapping_rows` confirms one effective publish register/unregister despite overlapping rows and strict duplicate-fail transport behavior.
- E: `add_forwarding_rule_rolls_back_on_listener_insert_failure` confirms no stale forwarding rule/forwarder refcount remains and retry succeeds after removing failure source.

### DG-1 decision

- Path A selected (semantic identity `topic + subscriber`) to preserve multiple topic-distinct rows for the same subscriber and support rebuild/removal-reflection correctness.

### Validation commands and outcomes

- Targeted tests for A/B/C/D/E: pass (`cargo test -p up-streamer ...`).
- Additional targeted coverage: `cargo test -p up-streamer publish_filter_ -- --nocapture`, `cargo test -p up-streamer unregistration_removes_publish_filters -- --nocapture`, `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules -- --nocapture` all pass.
- Path A cache tests: `cargo test -p subscription-cache -- --nocapture` passes.
- Full crate: `cargo test -p up-streamer -- --nocapture` passes.
- CI parity:
  - base + bundled matrices pass
  - unbundled matrix skipped because `VSOMEIP_INSTALL_PATH` is unavailable in this environment (documented in `ci-parity-results.md`)
  - workspace checks pass (`cargo check --workspace --all-targets`, `cargo test --workspace`)

### Harness touch rationale

- No integration harness updates were needed; behavior changes are confined to streamer/runtime + cache semantics and deterministic tests.
