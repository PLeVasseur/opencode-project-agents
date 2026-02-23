# Issue #74 Execution Report

Date: 2026-02-08
Branch: `bugfix/issue-74-left-topic-authority`
Base: `perf/ci-pr-latency-reduction`
PR: `https://github.com/PLeVasseur/up-streamer-rust/pull/31`

## Scope Delivered

- Implemented left-side/topic authority enforcement for publish forwarding (issue #74 primary runtime fix).
- Added deterministic regression coverage with fail-before/pass-after evidence.
- Added CLI parameterization across all `example-streamer-uses` binaries with defaults preserved.
- Added docs/runbook updates for issue-74 repro without source edits.
- Integrated harness skepticism guidance and fixed integration harness contract mismatch that blocked CI parity.

## Root Cause

Primary issue root cause:

- In `up-streamer/src/ustreamer.rs` (`ForwardingListeners::insert`), publish listener registration used `in_authority` + topic tuple for source filters without enforcing that the topic authority (left side of mapping) matched `in_authority`.
- Result: for map `A -> B`, forwarding rule `C -> B` still registered a publish listener for authority `C` and forwarded disallowed publishes.

Fix details:

- Added `publish_source_uri_for_rule(...)` in `up-streamer/src/ustreamer.rs` to enforce:
  - allow when `topic.authority_name == in_authority`, or
  - allow left wildcard `topic.authority_name == "*"`,
  - otherwise skip registration with explicit debug log evidence.
- Updated remove-path behavior to unregister request and publish listeners consistently with registered filters.

Secondary CI blocker root cause (post-fix):

- `utils/integration-test-utils/src/up_client_foo.rs` registered authority listeners keyed by sink authority but unregistered only via a legacy source/sink-any pattern.
- With streamer unregister symmetry, stale authority listeners were left behind, causing duplicated receives and integration test failures.

Harness remediation:

- `register_listener` now supports both:
  - authority listeners for `sink_filter: Some(...)`
  - topic listeners for `sink_filter: None`
- `unregister_listener` now supports symmetric unregister by concrete sink authority and preserves legacy sink-any behavior.
- This aligns the harness with `UTransport` contract expectations without changing issue-74 forwarding semantics.

## Fail-Before / Pass-After Evidence

Fail-before (pre-fix worktree at commit `08b3c0e`):

- Command: `cargo test -p up-streamer issue_74_left_authority_regression_temp -- --nocapture`
- Log: `$OPENCODE_CONFIG_DIR/reports/issue-74/phase4_fail_before.log`
- Evidence:
  - panic: `disallowed publish source listener was unexpectedly registered`
  - test result: `FAILED` (1 failed)

Pass-after (fix branch):

- Command: `cargo test -p up-streamer issue_74 -- --nocapture`
- Log: `$OPENCODE_CONFIG_DIR/reports/issue-74/phase4_pass_after.log`
- Evidence:
  - tests passed:
    - `issue_74_publish_filter_respects_topic_authority`
    - `issue_74_publish_filter_allows_left_wildcard`
    - `issue_74_publish_filter_blocks_unmapped_authority`
    - `issue_74_unregistration_removes_publish_filters`
  - test result: `ok` (4 passed, 0 failed)

## Manual Reproduction Evidence (Parameterized Binaries)

Artifacts:

- Config: `$OPENCODE_CONFIG_DIR/reports/issue-74/CONFIG.issue74.json5`
- Subscription map: `$OPENCODE_CONFIG_DIR/reports/issue-74/subscription_data.issue74.json`
- Streamer log: `$OPENCODE_CONFIG_DIR/reports/issue-74/manual_streamer.log`
- Allowed subscriber log: `$OPENCODE_CONFIG_DIR/reports/issue-74/manual_subscriber_allowed.log`
- Disallowed subscriber log: `$OPENCODE_CONFIG_DIR/reports/issue-74/manual_subscriber_disallowed.log`

Commands used:

```bash
docker compose -f utils/mosquitto/docker-compose.yaml up -d
target/debug/configurable-streamer --config "$OPENCODE_CONFIG_DIR/reports/issue-74/CONFIG.issue74.json5"
target/debug/zenoh_subscriber --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001
target/debug/mqtt_publisher --uauthority authority-a --uentity 0x5BA0 --uversion 0x1 --resource 0x8001
target/debug/zenoh_subscriber --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-c --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001
target/debug/mqtt_publisher --uauthority authority-c --uentity 0x5BA0 --uversion 0x1 --resource 0x8001
```

Observed outcomes:

- Allowed source A forwarded:
  - `manual_subscriber_allowed.log` contains repeated `PublishReceiver: Received a message` with source authority `authority-a`.
- Disallowed source C blocked:
  - `manual_subscriber_disallowed.log` contains startup logs only; no `PublishReceiver: Received a message` entries.
- Streamer objective mismatch evidence:
  - `manual_streamer.log` contains `skipping publish listener insert` for `in_authority='authority-c'` with topic authority `authority-a`.

## CI / Parity Command Outcomes

Base checks (all passed):

- `source build/envsetup.sh highest`
- `cargo build` -> `ci_base_build.log`
- `cargo clippy --all-targets -- -W warnings -D warnings` -> `ci_base_clippy.log`
- `cargo fmt -- --check` -> `ci_base_fmt.log`

Bundled matrix checks (all passed):

- `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport` -> `ci_bundled_build.log`
- `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` -> `ci_bundled_clippy.log`

Unbundled matrix checks (all passed):

- Used:
  - `VSOMEIP_INSTALL_PATH=$(pwd)/target/debug/build/vsomeip-sys-6199f84eca5fb0e1/out/vsomeip/vsomeip-install`
  - `LD_LIBRARY_PATH=$VSOMEIP_INSTALL_PATH/lib:$LD_LIBRARY_PATH`
- `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport` -> `ci_unbundled_build.log`
- `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` -> `ci_unbundled_clippy.log`

Workspace checks (all passed):

- `cargo check --workspace --all-targets` -> `ci_workspace_check.log`
- `cargo test --workspace` -> `ci_workspace_test.log`

Integration harness recheck evidence:

- Before harness fix:
  - `recheck_single_local_two_remote_add_remove_rules.log` failed with send/receive discrepancy panic.
- After harness fix:
  - `recheck_single_local_two_remote_add_remove_rules_after_harness.log` passed (`test ... ok`).

## Deferred / Follow-up Items

- Validation matrix cases not separately instrumented in this run:
  - right-side wildcard unchanged behavior (case 4)
  - mismatched topic tuple no-forward assertion (case 5)
  - explicit multi-map `A -> B` and `C -> B` both-forward assertion (case 6)
- SOME/IP runtime behavior was not manually exercised end-to-end for issue #74; CLI parsing/help/build coverage was completed and documented.
