# Issue #74 Follow-Up Validation Matrix Plan (Session-Ready, Challenge-Integrated)

## Goal

- [x] Add explicit, deterministic regression coverage for three follow-up assertions that were not separately instrumented:
  - [x] right-side wildcard subscriber authority (`*`) forwards to any destination authority that has a matching forwarding rule
  - [x] mismatched source tuple does not forward
  - [x] multi-map (`A -> B` and `C -> B`) forwards from both A and C
- [x] Keep current left-side authority fix behavior intact.
- [x] Expand only subscriber-authority wildcard semantics on the right side (`//*/...` as subscriber authority); keep all other wildcard dimensions unchanged.
- [x] Prevent duplicate publish listener registration/unregistration attempts from overlapping subscription rows so forwarding rule setup cannot fail due to duplicate listener keys.
- [x] Ensure failed forwarding-listener setup cannot leave stale forwarding-rule bookkeeping or stale forwarder refcounts.

## Execution Discipline (Mandatory)

- [x] Execute phases and gates in strict order; do not skip gates.
- [x] Tick each checkbox from `[ ]` to `[x]` immediately after completion.
- [x] Keep all artifacts under `$OPENCODE_CONFIG_DIR` (no repo-local plans/prompts/reports).
- [x] If a step is blocked, record blocker and fallback in report before proceeding.
- [x] Record Decision Gate DG-1 outcome explicitly in report artifacts before coding runtime semantics.
- [x] Default DG-1 for this plan execution is Path A; only deviate if explicitly instructed.
- [x] Do not begin runtime code changes until DG-1 decision checkbox is marked and logged in report artifacts.

## Test Readability Gate (Mandatory)

- [x] Keep one primary behavior per test.
- [x] Use behavior-first test names with no issue IDs/tags.
- [x] Keep test bodies compact (target roughly 15-35 lines before helper extraction).
- [x] Use explicit assertions with concrete expected values/call counts; avoid bare `is_ok()`-only checks where stronger assertions are possible.
- [x] Use helpers/builders to reduce setup duplication, but keep core assertions visible in the test body.

## Branch and PR Continuity

- [x] Stay on the current implementation branch `bugfix/issue-74-left-topic-authority` for all follow-up work in this plan (do not create a new branch).
- [x] Use upstream PR `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77` as the canonical review thread for this follow-up.
- [x] Keep one branch and one canonical upstream PR (base `main`); fork PR `https://github.com/PLeVasseur/up-streamer-rust/pull/31` is a non-canonical stacked-history mirror unless explicitly requested.
- [x] Continue on the existing issue branch/PR unless explicitly instructed otherwise:
  - [x] `git fetch --all --prune`
  - [x] `git switch bugfix/issue-74-left-topic-authority`
  - [x] `git pull --ff-only`

## Phase/Gate Overview

- [x] Phase 1: Bootstrap and baseline characterization complete.
- [x] Phase 1 gate: baseline notes/logs saved in `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/`.
- [x] Phase 2: Add deterministic automated coverage for A/B/C plus duplicate-safety assertion D and add-failure rollback assertion E.
- [x] Phase 2 gate: pre-change failure evidence captured for right-side wildcard, duplicate-safety, and add-failure rollback tests, then full follow-up matrix passes after implementation.
- [x] Phase 3: Run full validation + CI parity commands.
- [x] Phase 3 gate: all required commands pass.
- [x] Phase 4: Report + PR notes updated.
- [x] Phase 4 gate: handoff artifacts complete and reproducible.

## Scope (In / Out)

- [x] In scope:
  - [x] new deterministic tests for A/B/C assertions
  - [x] duplicate listener-key safety regression test(s) for overlap scenarios (assertion D)
  - [x] add-forwarding-rule rollback consistency regression test(s) (assertion E)
  - [x] targeted runtime updates required for right-side wildcard authority expansion
  - [x] dedupe of effective publish source filters used for listener register/unregister
  - [x] rollback consistency fix in `add_forwarding_rule` when listener insertion fails
  - [x] minimal harness adjustments only if tests expose real contract mismatch
  - [x] report evidence and PR-note update
- [x] Out of scope:
  - [x] wildcard semantic changes outside subscriber authority `*` on right side
  - [x] unrelated refactors
  - [x] transport feature additions unrelated to these assertions

## Required File Touch Map

- [x] Core runtime + tests:
  - [x] `up-streamer/src/ustreamer.rs`
- [x] Subscription lookup support:
  - [x] `subscription-cache/src/lib.rs` (merged exact + wildcard subscriber entry lookup helper)
- [ ] Optional integration harness touch only if needed:
  - [ ] `utils/integration-test-utils/src/up_client_foo.rs`
- [x] Report artifacts:
  - [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/*`

## Challenge Register and Resolution Tasks

### Challenge C1: Effective Publish Key Collisions From Distinct Rows

- [x] Problem statement: distinct subscription rows can normalize to the same effective publish listener key for a specific forwarding rule, e.g.:

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"],
  "//*/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [x] For rule `authority-a -> authority-b`, both rows normalize to one effective publish source filter: `//authority-a/5BA0/1/8001` (`sink_filter=None`).
- [x] Resolution tasks:
  - [x] introduce a helper to compute unique effective publish filters per `(in_authority, out_authority)`
  - [x] use the same unique set in both insert and remove paths (register/unregister symmetry)
  - [x] add deterministic tests proving one register and one unregister attempt for colliding rows

### Challenge C2: Transactional Blast Radius on Duplicate Register Failure

- [x] Problem statement: listener setup is transactional; if publish registration fails, rollback also unregisters request/notification/response authority listener for the same rule.
- [x] Concrete failure chain to cover in tests and notes:
  - [x] duplicate publish register attempt returns `ALREADY_EXISTS`
  - [x] streamer backpedals all registered filters for that insertion attempt
  - [x] non-publish listener for that rule is removed as part of rollback
- [x] Resolution tasks:
  - [x] extend existing `RecordingTransport` (do not introduce a second mock unless necessary) with:
    - [x] per-key register/unregister call counters keyed by `(source_filter, sink_filter)`
    - [x] forced register-fail injection by key + `UStatus` (including `ALREADY_EXISTS`)
  - [x] add strict duplicate-fail path and assert insertion succeeds with dedupe enabled
  - [x] assert request/notification/response listener remains active after overlap-driven insert
  - [x] keep rollback behavior for true non-duplicate failures

### Challenge C3: Partial-State Risk in `add_forwarding_rule`

- [x] Problem statement: `add_forwarding_rule` records forwarding rule and acquires transport forwarder before listener insertion; if listener insertion fails, function returns error and must not leave stale control-plane state.
- [x] Resolution tasks:
  - [x] add regression test that forces listener insertion failure and asserts no stale forwarding rule remains
  - [x] assert transport forwarder active-count/refcount is rolled back on insertion failure
  - [x] implement explicit rollback path in `add_forwarding_rule` for listener insertion errors
  - [x] verify retrying the same add after failure is possible and behaves correctly

### Challenge C4: Cache Identity Semantics Under Path A

- [x] Problem statement: Path A (`topic + subscriber` identity) is the semantically correct model for subscription rows but increases row cardinality and overlap exposure.
- [x] Resolution tasks:
  - [x] if Path A selected, update equality/hash in `subscription-cache/src/lib.rs`
  - [x] add/adjust subscription-cache tests validating both rows survive when topic differs and subscriber is identical
  - [x] add tests for reconstruction/update semantics (via rebuilt cache from updated `FetchSubscriptionsResponse`) covering:
    - [x] two topic-distinct rows with same subscriber remain distinct after rebuild
    - [x] row removal in updated payload is reflected after rebuild
  - [x] confirm dedupe mitigation still prevents duplicate effective publish listener registration attempts

## Assertion Definitions (Concrete)

### A) Right-Side Wildcard Expansion to Any Registered Authority

- [x] Implement and assert subscriber-side wildcard authority behavior: map entries with subscriber authority `*` apply to any destination authority that has a forwarding rule from the mapped source authority.
- [x] Concrete example mapping:

```json
{
  "//authority-a/5BA0/1/8001": ["//*/5678/1/1234"]
}
```

- [x] For forwarding rule `authority-a -> authority-b`, assert forwarding registration and delivery to `authority-b` occurs.
- [x] Add second forwarding rule `authority-a -> authority-d` and assert forwarding registration and delivery to `authority-d` also occurs without adding a second map row.
- [x] Assert wildcard does not create forwarding where no rule exists (for example, no `authority-a -> authority-e` rule => no forwarding to `authority-e`).
- [x] Test naming (example):
  - [x] `right_side_wildcard_forwards_to_registered_authorities`
  - [x] `right_side_wildcard_does_not_forward_without_rule`

### B) Mismatched Tuple No-Forward

- [x] Add assertion(s) that only exact mapped tuple is eligible for publish forwarding.
- [x] Concrete example mapping:

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [x] Assert no forwarding registration/dispatch for mismatches such as:
  - [x] `//authority-a/5BA1/1/8001` (ue_id mismatch)
  - [x] `//authority-a/5BA0/2/8001` (version mismatch)
  - [x] `//authority-a/5BA0/1/8002` (resource mismatch)
- [x] Test naming (example):
  - [x] `publish_filter_blocks_mismatched_tuple`

### C) Multi-Map Both-Forward

- [x] Add assertion(s) that when both mappings exist, both sources are forwarded to the same subscriber authority.
- [x] Concrete example mapping (safe default fixture for current cache identity):

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"],
  "//authority-c/5BA0/1/8001": ["//authority-b/5679/1/1234"]
}
```

- [x] With rules `authority-a -> authority-b` and `authority-c -> authority-b`, assert both publish source filters are present and active.
- [ ] Optional stronger fixture if DG-1 selects cache identity change:

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"],
  "//authority-c/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [x] Test naming (example):
  - [x] `multi_map_allows_both_sources`

### D) Overlap / Duplicate Listener-Key Safety (New)

- [x] Add assertion(s) proving that overlapping subscription rows do not cause duplicate listener registrations for the same effective publish key.
- [x] Concrete overlap examples:

```json
{
  "//authority-a/5BA0/1/8001": [
    "//authority-b/5678/1/1234",
    "//authority-b/5679/1/1234"
  ]
}
```

```json
{
  "//authority-a/5BA0/1/8001": ["//authority-b/5678/1/1234"],
  "//*/5BA0/1/8001": ["//authority-b/5678/1/1234"]
}
```

- [x] For rule `authority-a -> authority-b`, assert exactly one effective register/unregister call for publish key `//authority-a/5BA0/1/8001` (`sink_filter=None`).
- [x] Add a strict test transport (or equivalent assertion mechanism) that fails duplicate register calls with `ALREADY_EXISTS` and verify rule insertion still succeeds due to streamer-side dedupe.
- [x] Test naming (example):
  - [x] `publish_filter_dedupes_overlapping_rows`

### E) Add Failure Rollback Consistency (New)

- [x] Add assertion(s) proving failed listener insertion does not leave stale forwarding-rule control-plane state.
- [x] Required behavior under forced insert failure:
  - [x] `add_forwarding_rule(...)` returns error
  - [x] no residual forwarding-rule entry remains for that `(in_authority, out_authority, in_transport, out_transport)` tuple
  - [x] no leaked transport-forwarder active count for that failed rule add
  - [x] repeating the same `add_forwarding_rule(...)` after fixing failure source can succeed
- [x] Test naming (example):
  - [x] `add_forwarding_rule_rolls_back_on_listener_insert_failure`

## Decision Gate DG-1: Cache Identity vs Fixture Scope

- [x] Decide and document one path before runtime implementation:
  - [x] Path A (semantic change): broaden cache identity from `subscriber` to `topic + subscriber` in `subscription-cache/src/lib.rs`.
  - [ ] Path B (scope-narrowing): keep current cache identity and use distinct subscriber URIs in multi-map fixtures where needed.
- [x] DG-1 final choice for this execution: **Path A selected** (unless explicitly overridden by user before implementation starts).
- [x] Recommended default for this follow-up: **Path A + mandatory effective-key dedupe mitigation**.
- [x] Guardrail: even with Path A, do not rely on transport idempotence; always dedupe effective publish listener keys in streamer insert/remove paths.

## Expected Runtime Behavior Contract (Must Hold)

- [x] Contract 1: Right-side wildcard authority expansion
  - [x] Given map `"//authority-a/5BA0/1/8001": ["//*/5678/1/1234"]`
  - [x] And forwarding rules `authority-a -> authority-b` and `authority-a -> authority-d`
  - [x] Then publish from `//authority-a/5BA0/1/8001` forwards to subscribers on both destination authorities (`authority-b` and `authority-d`) if registered.
- [x] Contract 2: Rule-bound expansion only
  - [x] Wildcard subscriber authority does not bypass forwarding-rule topology.
  - [x] If no `authority-a -> authority-e` rule exists, no forwarding to `authority-e` occurs.
- [x] Contract 3: Tuple strictness preserved
  - [x] Right-side wildcard expansion does not loosen tuple matching on source topic fields (`authority`, `ue_id`, `uversion`, `resource`).
  - [x] Mismatched tuple publish does not forward.
- [x] Contract 4: Multi-map union
  - [x] Given both `A -> B` and `C -> B` map entries and both forwarding rules exist, publishes from A and C both forward to B.
- [x] Contract 5: Duplicate-key dedupe
  - [x] Overlapping rows that normalize to the same effective publish listener key register exactly once and unregister exactly once.
- [x] Contract 6: Transactional safety retained
  - [x] Duplicate overlap does not trigger publish registration failure and does not roll back request/notification/response listener setup.
- [x] Contract 7: Add-failure rollback consistency
  - [x] If listener insertion fails during `add_forwarding_rule`, no stale forwarding rule or forwarder refcount remains.
  - [x] Subsequent retry after failure source is removed can succeed normally.

## Phase 1: Bootstrap and Baseline Characterization

- [x] Create report directory:
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/issue-74-followups"`
- [x] Capture baseline branch/state:
  - [x] `git status --short`
  - [x] `git log --oneline -10`
- [x] Capture baseline code pointer inventory:
  - [x] `rg -n "fetch_cache_entry|publish_source_uri_for_rule|register_listener\(|unregister_listener\(" subscription-cache/src/lib.rs up-streamer/src/ustreamer.rs`
  - [x] `rg -n "add_forwarding_rule\(|forwarding_listeners\.insert\(|transport_forwarders\.insert\(" up-streamer/src/ustreamer.rs`
- [x] Capture baseline coverage gap (expected missing tests) in:
  - [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/baseline-characterization.md`
  - [x] include command output from:
    - [x] `rg -n "right_side_wildcard|publish_filter_blocks_mismatched_tuple|multi_map_allows_both_sources|publish_filter_dedupes_overlapping_rows|add_forwarding_rule_rolls_back_on_listener_insert_failure" up-streamer/src/ustreamer.rs`

## Phase 2: Implement Deterministic Automated Coverage + Runtime Support

### 2.1 Add Tests First (Fail-Before Evidence)

- [x] Reuse deterministic `RecordingTransport` test pattern in `up-streamer/src/ustreamer.rs`.
- [x] Extend `RecordingTransport` for D/E assertions with per-key counters and fail-injection hooks so tests remain deterministic and short.
- [x] Add test(s) for A/B/C/D/E using concrete fixtures from this plan.
- [x] Run targeted tests before runtime updates and capture expected failures in:
  - [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-right-wildcard.log`
  - [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-dedupe.log`
  - [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-add-rollback.log`

### 2.2 Runtime Implementation

- [x] Implement right-side wildcard runtime support:
  - [x] update subscriber lookup path so forwarding for `out_authority=<X>` includes both exact subscriber authority `<X>` and wildcard subscriber authority `*` entries
  - [x] apply lookup change symmetrically in listener insert and remove paths
- [x] Implement dedupe over effective publish listener keys:
  - [x] collect normalized publish source filters into a unique set before register
  - [x] unregister using the same unique set shape (register/unregister symmetry)
  - [x] keep transactional rollback behavior for true failures
- [x] Implement add-failure rollback consistency in `add_forwarding_rule`:
  - [x] if `forwarding_listeners.insert(...)` fails, remove just-added forwarding rule bookkeeping entry
  - [x] if `forwarding_listeners.insert(...)` fails, decrement/remove transport forwarder reference acquired for this attempted rule add
  - [x] preserve existing success-path behavior and duplicate-rule rejection behavior
- [x] Preferred implementation touch points:
  - [x] `subscription-cache/src/lib.rs` (helper to fetch merged exact + wildcard entries)
  - [x] `up-streamer/src/ustreamer.rs` (consume merged entries + dedupe source filters)
- [x] If DG-1 chooses Path A, update `SubscriptionInformation` equality/hash and add/adjust tests accordingly.

### 2.3 Re-Run Targeted Matrix

- [x] Re-run A/B/C/D/E targeted tests and verify pass.
- [x] Save pass evidence snippets in `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/test-evidence.md`.

### Optional Harness Remediation (Only if Needed)

- [x] If test failures indicate harness contract mismatch (not streamer logic), update harness minimally.
- [x] Ensure `register_listener` and `unregister_listener` symmetry by `(source_filter, sink_filter)` semantics.
- [x] Avoid using harness changes to mask streamer behavior regressions.

## Phase 3: Validation and CI Parity

### Targeted First

- [x] `cargo test -p up-streamer right_side_wildcard -- --nocapture`
- [x] `cargo test -p up-streamer publish_filter_blocks_mismatched_tuple -- --nocapture`
- [x] `cargo test -p up-streamer multi_map_allows_both_sources -- --nocapture`
- [x] `cargo test -p up-streamer publish_filter_dedupes_overlapping_rows -- --nocapture`
- [x] `cargo test -p up-streamer add_forwarding_rule_rolls_back_on_listener_insert_failure -- --nocapture`
- [x] `cargo test -p up-streamer publish_filter_ -- --nocapture`
- [x] `cargo test -p up-streamer unregistration_removes_publish_filters -- --nocapture`
- [x] `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules -- --nocapture`
- [x] if DG-1 Path A selected: `cargo test -p subscription-cache -- --nocapture`
- [x] `cargo test -p up-streamer -- --nocapture`

### CI Parity Matrix

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Set unbundled prerequisites before unbundled matrix:
  - [ ] ensure `VSOMEIP_INSTALL_PATH` points to a valid vsomeip install tree
  - [ ] `export LD_LIBRARY_PATH="$VSOMEIP_INSTALL_PATH/lib:${LD_LIBRARY_PATH:-}"`
- [x] If unbundled prerequisites are unavailable locally, mark unbundled matrix as skipped with explicit reason in `ci-parity-results.md` and continue bundled/base/workspace matrices.
- [ ] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
- [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

## Commit Slicing

- [x] Commit 1: runtime support for merged exact+wildcard subscriber lookup plus effective publish-key dedupe in register/unregister paths.
- [x] Commit 2: add-failure rollback consistency fix in `add_forwarding_rule` (including transport-forwarder rollback).
- [x] Commit 3: explicit regression tests for A/B/C/D/E assertions.
- [x] Commit 4: PR notes update only (report artifacts remain under `$OPENCODE_CONFIG_DIR` and are not committed).
- [ ] Commit 5 (optional): minimal harness adjustments only if integration tests reveal contract mismatch unrelated to streamer semantics.
- [x] Before each commit:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`

## Evidence Artifacts (Required)

- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/baseline-characterization.md`
- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-right-wildcard.log`
- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-dedupe.log`
- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/prechange-add-rollback.log`
- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/test-evidence.md`
- [x] `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/ci-parity-results.md`
- [x] Include concrete snippets proving:
  - [x] right-side wildcard authority forwards to registered destination authorities and does not forward without a rule
  - [x] mismatched tuple no-forward
  - [x] multi-map both-forward
  - [x] overlap dedupe avoids duplicate register/unregister attempts
  - [x] failed add path does not leave stale forwarding-rule/forwarder state

## PR Notes Minimums

- [x] Explicitly state right-side wildcard authority semantic expansion introduced in this follow-up and its exact limits.
- [x] Explicitly state duplicate-key dedupe mitigation and why it avoids transactional rollback side effects.
- [x] Explicitly state add-failure rollback consistency mitigation in `add_forwarding_rule`.
- [x] List added tests and exact assertions for A/B/C/D/E.
- [x] Include command list and outcomes.
- [x] Include DG-1 decision (Path A or Path B) and rationale.
- [x] Include any harness change rationale (if touched) and why it is contract-alignment, not behavior masking.

## Exit Criteria

- [x] All five assertions (A/B/C/D/E) are explicitly covered by automated tests.
- [x] CI parity commands pass.
- [x] Report artifacts are complete under `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/`.
- [x] Plan checkboxes are fully updated to reflect actual execution state.
