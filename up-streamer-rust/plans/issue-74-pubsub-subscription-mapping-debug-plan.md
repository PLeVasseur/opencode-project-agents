# Issue #74 Debug and Validation Plan (Session-Ready)

## Goal

- [ ] Fix issue #74 by enforcing left-side/topic authority constraints for publish forwarding from `subscription_data.json`.
- [ ] Add deterministic regression tests so a fresh session can prove fail-before / pass-after.
- [ ] Make example binaries parameterizable (with existing defaults preserved) so issue scenarios can be reproduced from the CLI without code edits.
- [ ] Preserve existing behavior for notification/request/response forwarding.
- [ ] Keep right-side wildcard behavior out of scope for this fix (no semantic expansion in this issue).

## Branching Baseline (Required)

- [x] Start from branch `perf/ci-pr-latency-reduction` because it already includes dependency and CI improvements needed for this work.
- [x] Refresh that base before branching:
  - [x] `git fetch --all --prune`
  - [x] `git checkout perf/ci-pr-latency-reduction`
  - [x] `git pull --ff-only`
- [x] Create the issue branch from that base (example):
  - [x] `git checkout -b bugfix/issue-74-left-topic-authority`
- [x] Do not base this fix branch directly from `main` for this execution.

## Execution Phases and Gates (Strict Order)

- [x] Phase 1: Branch/bootstrap + baseline reproduction evidence captured.
- [x] Phase 1 gate: issue #74 reproduction notes and logs are saved under `$OPENCODE_CONFIG_DIR/reports/issue-74/`.
- [x] Phase 2: Introduce shared CLI parsing/helpers for example binaries.
- [x] Phase 2 gate: helper unit tests pass and representative `--help` output validates new flags and defaults.
- [x] Phase 3: Roll CLI parameterization across all example binaries.
- [x] Phase 3 gate: all targeted binaries start with default args (backward compatibility) and parse override args correctly.
- [x] Phase 4: Implement streamer left-side/topic authority fix and required unregister symmetry adjustments.
- [x] Phase 4 gate: fail-before/pass-after regression tests demonstrate issue resolution.
- [x] Phase 5: Manual issue #74 verification using parameterized binaries and generated configs.
- [x] Phase 5 gate: logs show publisher C is blocked while A is allowed for map `A -> B`.
- [x] Phase 6: docs + CI parity preflight + report/PR notes.
- [x] Phase 6 gate: preflight commands pass and handoff artifacts are complete.

## Session Bootstrap (First 10 Minutes)

- [x] Confirm artifact root and read this plan from `$OPENCODE_CONFIG_DIR/plans/issue-74-pubsub-subscription-mapping-debug-plan.md`.
- [x] Pull issue context directly:
  - [x] `gh issue view 74 --repo eclipse-uprotocol/up-streamer-rust --json number,title,body,state,url`
- [x] Capture workspace state before edits:
  - [x] `git status --short`
  - [x] `git branch --show-current`
- [x] Confirm likely hotspot files are unchanged before implementation:
  - [x] `up-streamer/src/ustreamer.rs`
  - [x] `subscription-cache/src/lib.rs`
  - [x] `utils/usubscription-static-file/src/lib.rs`

## Expected File Touch Map

- [x] Required streamer/core files:
  - [x] `up-streamer/src/ustreamer.rs`
  - [x] `up-streamer/src/ustreamer.rs` tests section and/or `up-streamer/tests/*.rs`
- [x] Required example CLI files:
  - [x] `example-streamer-uses/src/bin/common/mod.rs`
  - [x] add shared parser/helper module under `example-streamer-uses/src/bin/common/` (for numeric parsing + URI arg building)
  - [x] `example-streamer-uses/src/bin/mqtt_client.rs`
  - [x] `example-streamer-uses/src/bin/mqtt_service.rs`
  - [x] `example-streamer-uses/src/bin/mqtt_publisher.rs`
  - [x] `example-streamer-uses/src/bin/mqtt_subscriber.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_client.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_service.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_publisher.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_subscriber.rs`
  - [x] `example-streamer-uses/src/bin/someip_client.rs`
  - [x] `example-streamer-uses/src/bin/someip_service.rs`
  - [x] `example-streamer-uses/src/bin/someip_publisher.rs`
  - [x] `example-streamer-uses/src/bin/someip_subscriber.rs`
- [x] Required docs:
  - [x] `example-streamer-uses/README.md`
  - [x] `configurable-streamer/README.md` and/or `example-streamer-implementations/README.md` where reproduction commands are documented
- [ ] Optional helper/test files only if needed:
  - [x] `utils/integration-test-utils/src/*` (only if integration coverage requires harness changes)
- [ ] Scope guard:
  - [x] if additional files are touched, document why in the report.

## Contract and Assumptions to Lock

- [x] Treat mapping as: left side = allowed publish source topic filter, right side = subscriber URIs.
- [x] Treat authority names as exact string matches unless wildcard `*` is explicitly used.
- [x] Confirm wildcard expectation before coding tests:
  - [x] left side `//*/...` means any source authority may match.
  - [x] right side wildcard semantics are intentionally not changed in this issue.
- [x] Keep fix scoped to issue #74 unless a directly-related bug blocks validation (e.g., unregister symmetry for case 7).

## Example Binary Investigation Summary (Current State)

- [x] Confirm current limitations to remove:
  - [x] Most example binaries hardcode authority and entity IDs (publishers/subscribers/clients/services).
  - [x] Only Zenoh binaries currently expose `--endpoint`; MQTT and SOME/IP binaries have no equivalent CLI config for IDs.
  - [x] SOME/IP binaries still have TODOs for configurable vsomeip config path.
  - [x] Reproducing issue #74 with existing binaries requires changing code constants (especially second publisher authority).
- [x] Confirm dependency support already present:
  - [x] `clap` is already in `example-streamer-uses/Cargo.toml` with derive feature.
  - [x] Shared code location exists at `example-streamer-uses/src/bin/common/` for reusable CLI parsing helpers.

## Example Binary CLI Parameterization Workstream

- [x] Introduce reusable CLI helpers under `example-streamer-uses/src/bin/common/`:
  - [x] parser helpers for numeric IDs accepting decimal and hex (`1234`, `0x4D2`).
  - [x] URI construction helpers with consistent validation/error messages.
- [x] Define common local-entity flags for all binaries (defaults remain current constants):
  - [x] `--uauthority <string>`
  - [x] `--uentity <u32-dec-or-hex>`
  - [x] `--uversion <u8-dec-or-hex>`
  - [x] `--resource <u16-dec-or-hex>`
- [x] Define peer/filter flags where role requires remote addressability:
  - [x] client binaries: `--target-authority`, `--target-uentity`, `--target-uversion`, `--target-resource`
  - [x] subscriber binaries: `--source-authority`, `--source-uentity`, `--source-uversion`, `--source-resource`
  - [ ] optional generic response/listener overrides only where needed for compatibility tests
- [x] Define transport-specific flags:
  - [x] MQTT binaries: `--broker-uri` (default `localhost:1883`)
  - [x] Zenoh binaries: keep `--endpoint` and ensure other URI args compose correctly
  - [x] SOME/IP binaries: add `--vsomeip-config <path>` and `--remote-authority <string>` (preserve existing defaults)
- [x] Apply parameterization consistently across all 12 binaries in `example-streamer-uses/src/bin/`:
  - [x] `mqtt_{publisher,subscriber,client,service}`
  - [x] `zenoh_{publisher,subscriber,client,service}`
  - [x] `someip_{publisher,subscriber,client,service}`
- [x] Backward compatibility checks:
  - [x] running each binary with no args keeps previous behavior
  - [x] old docs/commands still work unchanged
- [x] Documentation updates for usability:
  - [x] `example-streamer-uses/README.md` with default and override CLI examples
  - [x] relevant pub/sub setup docs (`configurable-streamer/README.md` and/or `example-streamer-implementations/README.md`) with issue-74 style reproducible commands

## CLI Contract (Required)

- [x] Numeric flag parsing contract:
  - [x] accept decimal (`1234`) and hex with `0x`/`0X` prefix (`0x4D2`)
  - [x] reject underscores/spaces in numeric args for first version (simple and deterministic)
  - [x] `--uentity` and `--target-uentity` / `--source-uentity` parse as `u32`
  - [x] `--uversion` and peer/source version flags parse as `u8`
  - [x] `--resource` and peer/source resource flags parse as `u16`
  - [x] range checks produce deterministic errors (no silent truncation)
- [x] Error message contract:
  - [x] include flag name, raw value, and expected format/range
  - [x] example: `invalid value for --uentity: '0x1_0000_0000' (expected u32 in decimal or 0x-prefixed hex)`
- [x] Defaults contract:
  - [x] defaults exactly match current hardcoded constants per binary
  - [x] CLI override must only change explicitly provided fields
- [x] Help output contract:
  - [x] every new arg has a concise description and default value display
  - [x] examples for decimal + hex included in README (not necessarily in clap help text)

## SOME/IP Caveat and Handling

- [x] Document that SOME/IP runtime behavior may depend on `vsomeip-config` application IDs in addition to UURI overrides.
- [x] Add `--vsomeip-config` to each SOME/IP binary and prefer explicit config path in reproducibility docs.
- [x] If `--uentity` override conflicts with provided SOME/IP config expectations, emit clear startup warning/error and document remediation.
- [x] Include a deterministic SOME/IP test note:
  - [x] for issue #74 validation path, MQTT<->Zenoh is canonical; SOME/IP parameterization is compatibility work and should not block left-authority fix validation.

## Manual Reproduction Runbook Enabled by CLI Args

- [x] Add a reproducible issue #74 manual runbook that uses binaries only (no source edits):
  - [x] one Zenoh subscriber with authority B
  - [x] two MQTT publishers with authorities A and C, same topic tuple
  - [x] streamer forwarding rules for `A<->B` and `C<->B`
  - [x] subscription map containing only `A -> B`
- [x] Add concrete command examples in docs/plan with new flags, including two concurrent publisher commands:
  - [x] publisher A command with `--uauthority authority-a`
  - [x] publisher C command with `--uauthority authority-c`
  - [x] subscriber B command(s) with `--uauthority authority-b` and explicit source filter args for both allowed and disallowed source checks
- [x] Store temporary test configs under `$OPENCODE_CONFIG_DIR/reports/issue-74/` during validation to avoid repo-local artifact clutter.
- [ ] Record expected observations:
  - [ ] before fix: subscriber incorrectly receives from C
  - [x] after fix: subscriber receives only A when map is `A -> B`

## Issue #74 Template Configs (Ready to Drop in `$OPENCODE_CONFIG_DIR/reports/issue-74/`)

- [x] Template `subscription_data.issue74.json`:

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [x] Template `CONFIG.issue74.json5` (with absolute paths adjusted at runtime):

```json5
{
  up_streamer_config: {
    message_queue_size: 10000,
  },
  streamer_uuri: {
    authority: "authority-b",
    ue_id: 78,
    ue_version_major: 1,
  },
  usubscription_config: {
    file_path: "/ABS/PATH/TO/$OPENCODE_CONFIG_DIR/reports/issue-74/subscription_data.issue74.json",
  },
  transports: {
    zenoh: {
      config_file: "/ABS/PATH/TO/configurable-streamer/ZENOH_CONFIG.json5",
      endpoints: [
        {
          authority: "authority-b",
          endpoint: "endpoint_zenoh_b",
          forwarding: ["endpoint_mqtt_a", "endpoint_mqtt_c"],
        },
      ],
    },
    mqtt: {
      config_file: "/ABS/PATH/TO/configurable-streamer/MQTT_CONFIG.json5",
      endpoints: [
        {
          authority: "authority-a",
          endpoint: "endpoint_mqtt_a",
          forwarding: ["endpoint_zenoh_b"],
        },
        {
          authority: "authority-c",
          endpoint: "endpoint_mqtt_c",
          forwarding: ["endpoint_zenoh_b"],
        },
      ],
    },
  },
}
```

- [ ] Runtime prep commands should set variables to avoid path mistakes:
  - [ ] `REPO_ROOT=$(pwd)` (from repo root)
  - [x] `ISSUE74_DIR="$OPENCODE_CONFIG_DIR/reports/issue-74"`
  - [x] replace `/ABS/PATH/TO/` in template with concrete absolute paths.

## Reproduce Current Bug (Baseline)

- [ ] Reproduce with authorities A, B, C and rules `A->B`, `C->B`, `B->A`, `B->C`.
- [ ] Baseline mapping (use repo-style authority names with lowercase + hyphen for executable repro):

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [ ] Confirm broken behavior: B still receives C publishes.
- [x] Capture baseline evidence in report notes under `$OPENCODE_CONFIG_DIR/reports/`.

## Root-Cause Confirmation Checklist

- [x] Inspect listener registration in `up-streamer/src/ustreamer.rs`:
  - [x] `ForwardingListeners::insert` where publish source filter is constructed.
  - [x] Verify whether `subscriber.topic.authority_name` is enforced or overwritten by `in_authority`.
- [x] Inspect subscriber lookup in `subscription-cache/src/lib.rs`:
  - [x] Verify cache is keyed by subscriber authority (`out_authority`) and returns all topics for that subscriber authority.
- [x] Inspect static subscription parsing in `utils/usubscription-static-file/src/lib.rs`:
  - [x] Verify map key authority is parsed into `topic`.
  - [x] Note parser caveat: resource id is currently normalized to `0x8001`.
- [x] Inspect `ForwardingListeners::remove` unregister filters for symmetry with `insert`.

## Integration Harness Skepticism and Remediation

- [x] Treat `utils/integration-test-utils/src/up_client_foo.rs` as a test harness approximation, not a source of transport truth.
- [x] If CI parity fails in integration tests after streamer fix, validate whether the harness violates `register_listener`/`unregister_listener` symmetry before changing streamer logic.
- [x] Add/adjust harness behavior only to align with `UTransport` contract expectations:
  - [x] support unregister by the same `(source_filter, sink_filter)` pair used at registration.
  - [x] keep backward compatibility for existing authority-listener patterns already used by tests.
  - [x] avoid changing issue-74 forwarding semantics to compensate for harness bugs.
- [x] Re-run affected integration tests after harness fixes:
  - [x] `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules -- --nocapture`
  - [x] `cargo test --workspace`

## Implementation Plan

- [x] Enforce topic authority checks during publish listener registration:
  - [x] register publish listener only when `topic.authority_name == in_authority` or topic authority is `*`.
- [x] Keep existing request/response/notification listener registration unchanged.
- [x] Ensure rollback/unregister paths use the same filters that were registered.
- [x] Add targeted debug logs for skipped topic authority mismatch cases.
- [x] Keep patch narrow to streamer internals and tests.

## Test Plan (Deterministic, CI-Friendly)

- [x] Add focused unit/regression tests in `up-streamer` that assert registration filters, not only message counts.
- [x] Add a recording mock `UTransport` to capture `register_listener` / `unregister_listener` calls with source/sink filters.
- [x] Add/rename tests to clearly map to issue behavior, e.g.:
  - [x] `issue_74_publish_filter_respects_topic_authority`
  - [x] `issue_74_publish_filter_allows_left_wildcard`
  - [x] `issue_74_publish_filter_blocks_unmapped_authority`
  - [x] `issue_74_unregistration_removes_publish_filters` (if remove-path fix is in scope)
- [x] Add at least one end-to-end style assertion (can be integration test or high-fidelity unit) that a publish from unmapped authority does not reach subscriber.

## Validation Matrix (Must Pass)

- [x] Case 1: exact map `A -> B`; publish from A is forwarded to B.
- [x] Case 2: exact map `A -> B`; publish from C is not forwarded to B.
- [x] Case 3: left wildcard `* -> B`; publishes from A and C are both forwarded.
- [ ] Case 4: right-side wildcard mapping behavior is unchanged by this patch (no regression, no new semantics).
- [ ] Case 5: mismatched topic tuple (ue_id/version/resource where applicable) is not forwarded.
- [ ] Case 6: multi-map (`A -> B` and `C -> B`) forwards from both A and C.
- [x] Case 7: delete forwarding rule then verify publishes stop forwarding for deleted path.
- [x] Case 8: existing non-pubsub tests remain green.

## Commit Plan (Logical Slices)

- [x] Commit 1: add shared CLI parse/helper module and tests (no behavior changes yet).
- [x] Commit 2: parameterize MQTT + Zenoh binaries (pub/sub first) with defaults preserved.
- [x] Commit 3: parameterize remaining binaries (MQTT/Zenoh client-service + all SOME/IP bins).
- [x] Commit 4: implement left-side/topic authority forwarding fix in streamer + regression tests.
- [x] Commit 5: docs/manual runbook updates and final polish.
- [x] Commit 6: align integration harness unregister behavior with `UTransport` register/unregister symmetry.
- [x] Before each commit, capture scope:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`

## Command Runbook

- [x] CLI contract sanity checks (post-implementation):
  - [x] `cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --help`
  - [x] `cargo run -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport -- --help`
  - [x] `cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport -- --help`
  - [x] `cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --help`
  - [x] `cargo run -p example-streamer-uses --bin someip_client --features vsomeip-transport -- --help`
- [x] Full binary coverage sanity checks:
  - [x] validate `--help` for all 12 binaries (feature-appropriate invocations)
  - [x] if SOME/IP environment is unavailable, document skipped SOME/IP runtime checks while still validating clap parsing/build paths
- [x] Manual issue #74 scenario using parameterized binaries (after CLI args are added):
  - [x] start MQTT broker (`utils/mosquitto/docker-compose.yaml`)
  - [x] create dedicated `CONFIG.json5` and `subscription_data.json` under `$OPENCODE_CONFIG_DIR/reports/issue-74/` for `A<->B` and `C<->B` forwarding with map `A -> B`
  - [x] run streamer: `cargo run -p configurable-streamer -- --config "$OPENCODE_CONFIG_DIR/reports/issue-74/CONFIG.issue74.json5"`
  - [x] run subscriber B (allowed-source assertion):
    - [x] `cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001`
  - [x] run subscriber B (disallowed-source assertion, separate terminal/run):
    - [x] `cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-c --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001`
  - [x] run publisher A:
    - [x] `cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --uauthority authority-a --uentity 0x5BA0 --uversion 0x1 --resource 0x8001`
  - [x] run publisher C:
    - [x] `cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --uauthority authority-c --uentity 0x5BA0 --uversion 0x1 --resource 0x8001`
  - [x] capture before/after behavior evidence in logs for C publish filtering
- [x] Targeted test loop while implementing:
  - [x] `cargo test -p up-streamer issue_74 -- --nocapture`
  - [x] `cargo test -p up-streamer -- --nocapture` (before full workspace)
- [x] Baseline quality checks:
  - [x] `cargo fmt -- --check`
  - [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`

## Manual Verification Criteria (Objective)

- [ ] Before fix (expected bug):
  - [ ] in disallowed-source subscriber run (`source-authority authority-c`), `PublishReceiver: Received a message` appears repeatedly.
- [x] After fix (expected correct behavior):
  - [x] in allowed-source subscriber run (`source-authority authority-a`), `PublishReceiver: Received a message` appears.
  - [x] in disallowed-source subscriber run (`source-authority authority-c`), no `PublishReceiver: Received a message` lines after warm-up window.
- [x] Streamer-side evidence:
  - [x] log includes explicit skip/mismatch message for left-side authority mismatch (new logging added in fix).
  - [x] no registration line equivalent to a publish source filter for authority-c when map is only `A -> B`.

## CI-Parity Preflight (Per Repo Guidance)

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] If transport/plugin integration files are touched and environment is ready:
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

## Handoff Outputs for New Session

- [x] Report file in `$OPENCODE_CONFIG_DIR/reports/` containing:
  - [x] root cause statement with code references.
  - [x] fail-before / pass-after test evidence.
  - [x] command list executed and outcomes.
  - [x] manual runbook evidence using parameterized binaries (commands + observed logs).
  - [x] any unresolved follow-up items.
- [x] PR notes include left-side authority fix scope, CLI parameterization additions, and regression matrix outcomes.

## Risk and Fallback Plan

- [x] Primary target is full parameterization across all example binaries in this execution.
- [ ] If timeline risk appears, preserve issue #74 delivery by prioritizing in order:
  - [ ] streamer fix + regression tests
  - [ ] MQTT/Zenoh pub/sub binaries parameterization and docs needed for issue-74 manual reproduction
  - [ ] remaining binaries parameterization (complete in same branch if feasible, otherwise clearly tracked follow-up)
- [ ] Any de-scoping must be documented in `$OPENCODE_CONFIG_DIR/reports/issue-74/` with explicit follow-up actions and owners.

## Exit Criteria

- [x] Issue #74 no longer reproducible.
- [x] New tests catch the old bug and pass with the fix.
- [x] Existing suites stay green.
- [x] Plan is executable without prior chat context.
