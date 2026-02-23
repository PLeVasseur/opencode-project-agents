# PR-83 up-rust Idiomatic Usage Codebase Sweep Plan

Date: 2026-02-17
Source PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/83
Primary review signal: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/83#pullrequestreview-3807115879
Execution repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
PR-83 head branch (locked target): `cleanup/refactor-upstream-main-prA-architecture`
Delivery policy: phased local confidence commits, then one squashed remediation commit before first push

## Execution status snapshot

- [x] Phase 0 baseline/branch lock complete.
- [x] Phase 1 discovery inventory complete.
- [x] Phase 2 standards lock complete.
- [x] Phase 3 implementation workstreams complete.
- [x] Phase 4 validation matrix complete for this scope.
- [x] Phase 5 local phased confidence commits complete.
- [x] Phase 3F residual whole-codebase idiom closure pass complete.
- [x] Phase 4B residual-closure validation pass complete.
- [x] Phase 5 squash complete.
- [ ] Phase 5 pre-push/push steps pending by user request.

## Goals and guardrails

- [ ] Align code with canonical `up-rust` APIs where equivalent semantics already exist.
  - [ ] Prefer accessor/helper methods over direct protobuf field traversal.
  - [ ] Prefer semantic URI helpers over string literal checks.
  - [ ] Prefer canonical test utilities (`MockTransport` from `up-rust/test-util`) over ad-hoc mocks.
- [ ] Keep behavior stable while improving API idiomaticity.
  - [ ] Treat this as a readability/maintainability sweep, not a feature rewrite.
  - [ ] Preserve existing fallback behavior unless a fallback is demonstrably incorrect.
- [ ] Keep diffs reviewer-friendly.
  - [ ] Use mechanical, pattern-based commits where possible.
  - [ ] Isolate any semantic changes behind explicit tests and commit boundaries.
- [ ] Preserve artifact hygiene and execution traceability.
  - [ ] Keep plan/report artifacts under `$OPENCODE_CONFIG_DIR` only.
  - [ ] Store sweep inventories/results under `$OPENCODE_CONFIG_DIR/reports/`.

## Feedback taxonomy distilled from PR-83

- [ ] Pattern A - Accessors instead of deep option chaining.
  - [ ] Replace chains like `message.attributes.as_ref().and_then(|a| a.id.as_ref())` with `message.id()` where available.
  - [ ] Replace direct `source/sink` extraction through nested fields with `source()` / `sink()` accessors where available.
  - [ ] Replace `type_.enum_value_or_default()` through raw field access with `type_()` accessor where equivalent.
- [ ] Pattern B - Canonical UUID formatting method references.
  - [ ] Prefer `.map(UUID::to_hyphenated_string)` where compatible with surrounding types.
- [ ] Pattern C - URI semantic helpers over string checks.
  - [ ] Replace `authority_name == "*"` with `has_wildcard_authority()`.
  - [ ] Replace direct field comparisons with accessor-based comparisons (for example `authority_name().as_str()`).
- [ ] Pattern D - Shared test/mock primitives.
  - [ ] Replace local doctest `MockTransport` scaffolding with `up-rust::MockTransport` (`test-util` feature).
  - [ ] Keep mock usage internal to doctests/test helpers only; do not expose via public API.

## Scope definition (codebase-wide sweep)

- [ ] Include all first-party crates in this workspace for API-usage consistency.
  - [ ] `up-streamer`
  - [ ] `configurable-streamer`
  - [ ] `example-streamer-implementations`
  - [ ] `example-streamer-uses`
  - [ ] `utils/integration-test-utils`
  - [ ] `utils/usubscription-static-file` (if relevant patterns appear)
  - [ ] `up-linux-streamer-plugin` (if relevant patterns appear)
- [ ] Include code categories where reviewer comments imply standards.
  - [ ] Library/runtime code (`src/**/*.rs`)
  - [ ] Tests (`tests/**/*.rs`, inline `#[cfg(test)]` modules)
  - [ ] Doctests and rustdoc snippets in module docs
- [ ] Explicitly track currently known hotspots from initial scan.
  - [ ] `up-streamer/src/observability/fields.rs`
  - [ ] `up-streamer/src/routing/publish_resolution.rs`
  - [ ] `up-streamer/src/control_plane/mod.rs`
  - [ ] `up-streamer/src/data_plane/mod.rs`
  - [ ] `up-streamer/src/routing/mod.rs`
  - [ ] `up-streamer/src/lib.rs`
  - [ ] `utils/integration-test-utils/src/integration_test_utils.rs`
  - [ ] `utils/integration-test-utils/src/up_client_foo.rs`
  - [ ] `example-streamer-uses/src/bin/common/mod.rs`

## Residual idiom closure backlog (pre-squash)

- [ ] Classify and resolve residual non-idiomatic spots from the post-remediation audit.
  - [ ] Category R-A (easy read-accessor substitutions; convert by default).
    - [ ] `up-streamer/src/data_plane/ingress_listener.rs:78`
      - [ ] Replace direct payload format field path (`msg.attributes.payload_format.enum_value_or_default()`) with `msg.payload_format().unwrap_or_default()`.
    - [ ] `up-streamer/src/routing/subscription_cache.rs:144`
      - [ ] Replace `uri.authority_name.clone()` with `uri.authority_name()` if no behavior/perf regression.
    - [ ] `up-streamer/src/routing/uri_identity_key.rs:43`
      - [ ] Replace borrowed-form clone access with `uri.authority_name()`.
    - [ ] `utils/usubscription-static-file/src/lib.rs:63`
      - [ ] Replace borrowed-form clone access with `uri.authority_name()`.
    - [ ] `example-streamer-uses/src/bin/common/cli.rs:126`
      - [ ] Prefer accessor in assertion (`uuri.authority_name()`) for style consistency.
  - [ ] Category R-B (ownership/perf-sensitive reads; decide explicitly).
    - [ ] `up-streamer/src/routing/uri_identity_key.rs:32`
      - [ ] Keep direct move of `uri.authority_name` if accessor conversion would add an unnecessary clone.
    - [ ] `utils/usubscription-static-file/src/lib.rs:52`
      - [ ] Keep direct move of `uri.authority_name` under the same rule.
  - [ ] Category R-C (API-gap mutable internals; document if retained).
    - [ ] `utils/integration-test-utils/src/integration_test_utils.rs:365`
    - [ ] `utils/integration-test-utils/src/integration_test_utils.rs:367`
    - [ ] Confirm there is no equivalent `up-rust` mutable setter path for message ID mutation in this flow.
    - [ ] If retained, record explicit exemption rationale with follow-up option.
  - [ ] Category R-D (no equivalent helper semantics in `up-rust`; document if retained).
    - [ ] Direct `ue_id` reads in projection/build paths (for example `up-streamer/src/routing/publish_resolution.rs`).
    - [ ] Direct `resource_id` writes used for static-file canonicalization (`utils/usubscription-static-file/src/lib.rs:170`, `utils/usubscription-static-file/src/lib.rs:172`, `utils/usubscription-static-file/src/lib.rs:308`).
    - [ ] Verify each retained direct access is either required for mutation or lacks a helper equivalent.

## Whole-codebase idiom maximization pass (strict but practical)

- [ ] Lock strictness policy before edits.
  - [ ] Accessor-first for read paths when equivalent helper methods exist.
  - [ ] Do not force accessor conversion if it introduces avoidable clones on owned-move paths.
  - [ ] Keep direct mutation only where `up-rust` lacks setter APIs; require explicit rationale.
- [ ] Run full search matrix and classify results.
  - [ ] `UMessage/UAttributes` direct field access (`.attributes`, `.type_`, `.id`, `.source`, `.sink`, payload format paths).
  - [ ] `UUri` direct field access (`.authority_name`, `.ue_id`, `.ue_version_major`, `.resource_id`).
  - [ ] Protobuf wrapper internals (`.0`, direct option box manipulation).
- [ ] Execute in two passes.
  - [ ] Pass 1 (mechanical): apply all Category R-A conversions.
  - [ ] Pass 2 (judgment): resolve Category R-B/C/D with either conversion or explicit exemption.
- [ ] Preserve behavior and readability while maximizing idiomatic usage.
  - [ ] Keep log output/fallback strings stable.
  - [ ] Keep hidden doctest setup readable despite mock expectations.
  - [ ] Avoid broad refactors that obscure review intent.
- [ ] Update artifacts as first-class deliverables.
  - [ ] Inventory report lists each residual item with `done`/`exempt` outcome.
  - [ ] Exemptions report captures every retained direct-field site with exact line and reason.
  - [ ] Validation report includes search-output evidence proving closure coverage.

## Branch lock and publication discipline (mandatory)

- [ ] Resolve and lock to PR-83 head branch before editing code.
  - [ ] `EXPECTED_BRANCH="$(gh pr view 83 --repo eclipse-uprotocol/up-streamer-rust --json headRefName --jq .headRefName)"`
  - [ ] `test "$EXPECTED_BRANCH" = "cleanup/refactor-upstream-main-prA-architecture"`
  - [ ] If session starts on a different branch (for example `cleanup/refactor-upstream-main-prC-smoke`), switch immediately before any other command.
  - [ ] `git switch "$EXPECTED_BRANCH"`
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXPECTED_BRANCH"`
- [ ] Verify upstream tracking for the locked branch.
  - [ ] `git fetch origin "$EXPECTED_BRANCH"`
  - [ ] `test "$(git rev-parse --abbrev-ref --symbolic-full-name @{u})" = "origin/$EXPECTED_BRANCH"`
  - [ ] `git status -sb` shows `## $EXPECTED_BRANCH...origin/$EXPECTED_BRANCH`
- [ ] Apply hard branch guardrails throughout execution.
  - [ ] Re-run `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXPECTED_BRANCH"` before each phase.
  - [ ] Re-run branch guard before each commit.
  - [ ] Re-run branch guard immediately before push.
  - [ ] If guard fails, stop, switch back to `EXPECTED_BRANCH`, and re-run phase gates.
- [ ] Do not push phased local commits.
  - [ ] Keep all intermediate confidence commits local-only.
  - [ ] Push exactly once, after creating the single squashed remediation commit.

## Session resume protocol (new sessions)

- [ ] Persist sweep state in one progress file.
  - [ ] `PROGRESS_FILE="$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep-progress.env"`
  - [ ] Initialize keys: `EXPECTED_BRANCH`, `BASE_SHA`, `BRANCH_START_SHA`, `REMOTE_BRANCH_SHA`, `ROLLBACK_TAG`, `LAST_PHASE=phase0`, `LAST_LOCAL_COMMIT=none`, `PRE_SQUASH_SHA=unset`, `PRE_SQUASH_TAG=unset`.
- [ ] Restart rule for each new session.
  - [ ] If `PROGRESS_FILE` exists, source it before any edits.
  - [ ] Re-run branch guard and clean-tree checks before resuming.
  - [ ] Resume from `LAST_PHASE` and update markers immediately after each completed phase.
- [ ] Persist status checkpoints as work advances.
  - [ ] After each local `L*` commit, update `LAST_PHASE=phase5`, `LAST_LOCAL_COMMIT`, and `LAST_SHA`.
  - [ ] After squash, update `LAST_PHASE=phase5_squashed`, `PRE_SQUASH_SHA`, `PRE_SQUASH_TAG`, and `LAST_SHA`.
  - [ ] Before push, update `LAST_PHASE=pre_push_verified`.

## Phase 0 - Baseline and safety setup

- [ ] Capture immutable sweep anchors on the locked PR branch.
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXPECTED_BRANCH"`
  - [ ] `git status --short --branch`
  - [ ] `test -z "$(git status --porcelain)"`
  - [ ] If working tree is dirty, stop and reconcile local changes before sweep start.
  - [ ] `git fetch --all --prune`
  - [ ] `BASE_SHA="$(git rev-parse upstream/main)"`
  - [ ] `BRANCH_START_SHA="$(git rev-parse HEAD)"`
  - [ ] `REMOTE_BRANCH_SHA="$(git rev-parse origin/$EXPECTED_BRANCH)"`
  - [ ] `test "$BRANCH_START_SHA" = "$REMOTE_BRANCH_SHA"`
  - [ ] If local/remote branch tips differ, stop and reconcile to a deterministic start point before edits.
  - [ ] Record `BASE_SHA`, `BRANCH_START_SHA`, and `REMOTE_BRANCH_SHA` in validation report.
- [ ] Create local rollback refs before code changes.
  - [ ] `ROLLBACK_TAG="pr-83-sweep-start-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `git tag "$ROLLBACK_TAG" "$BRANCH_START_SHA"`
  - [ ] Verify tag points to `BRANCH_START_SHA`.
- [ ] Create sweep evidence files (reports only; no repo-local artifacts).
  - [ ] `REPORT_PREFIX="$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep"`
  - [ ] Write `"$REPORT_PREFIX-inventory.md"`.
  - [ ] Write `"$REPORT_PREFIX-exemptions.md"`.
  - [ ] Write `"$REPORT_PREFIX-validation.md"`.
  - [ ] Initialize or update `PROGRESS_FILE` with the resolved anchors from this phase.
- [ ] Define exemption policy before touching code.
  - [ ] Exemption requires: exact file/line + missing API rationale + follow-up action.
  - [ ] Exemption must not hide correctness issues.

## Phase 1 - Discovery and candidate inventory

- [ ] Run structured searches for each feedback pattern.
  - [ ] Search deep attribute access (`attributes.as_ref()`, nested `.id/.source/.sink`).
  - [ ] Search direct enum default extraction (`type_.enum_value_or_default()`).
  - [ ] Search authority wildcard string checks (`authority_name == "*"`).
  - [ ] Search doc/test custom `MockTransport` implementations.
  - [ ] Search unsafe `unwrap()` around message attributes in responder/test code paths.
- [ ] Normalize findings into an actionable inventory table.
  - [ ] Columns: file, line, pattern, proposed replacement, risk level, owner commit.
  - [ ] Label each finding as `mechanical`, `semantic`, or `needs-decision`.
  - [ ] Record an initial replacement snippet for each pattern class.
- [ ] Define acceptance criteria per finding.
  - [ ] Accessor migration keeps previous `None` fallback behavior.
  - [ ] URI helper migration preserves wildcard semantics.
  - [ ] Mock migration preserves doctest compileability.

## Phase 2 - Pattern decisions and standards lock

- [ ] Lock replacement standards before bulk editing.
  - [ ] Standard accessor style for IDs: `id()` + `UUID::to_hyphenated_string` where type-compatible.
  - [ ] Standard accessor style for message type: `type_()` with equivalent fallback text.
  - [ ] Standard accessor style for `source()` / `sink()` URI extraction.
  - [ ] Standard authority check style: `has_wildcard_authority()` + `authority_name().as_str()`.
- [ ] Resolve decision gates.
  - [ ] Gate D1: Enable and adopt `up-rust::MockTransport` in all targeted doctests.
    - [ ] Add `up-rust` dev-dependency feature wiring required for doctests (`test-util`).
    - [ ] Define one shared hidden doctest helper pattern for reusable mock setup.
  - [ ] Gate D2: Do any locations rely on raw field semantics not exposed by accessors?
    - [ ] If yes: keep local access with explicit exemption rationale.
  - [ ] Gate D3: For each residual direct-field site, is conversion accessor-equivalent without adding avoidable clone/mutation complexity?
    - [ ] If yes: convert.
    - [ ] If no: keep and document in exemptions.
- [ ] Freeze fallback-string constants and output expectations.
  - [ ] Ensure no accidental changes to logging field values used by tests/observability tooling.

## Phase 3 - Implementation workstreams

- [ ] Workstream A - Observability field formatters (`up-streamer` first).
  - [ ] Convert message/attribute ID extraction to accessor style.
  - [ ] Convert message type extraction to accessor style.
  - [ ] Convert source/sink URI extraction to accessor style.
  - [ ] Keep existing fallback strings unless explicitly approved otherwise.
  - [ ] Update/add unit tests in `up-streamer/src/observability/fields.rs` to pin behavior.
- [ ] Workstream B - Routing authority semantics.
  - [ ] Replace wildcard string checks in routing resolution with semantic helpers.
  - [ ] Replace direct authority field comparisons where helper accessor is available.
  - [ ] Add focused tests for wildcard and concrete authority matching behavior.
- [ ] Workstream C - Integration test utilities cleanup.
  - [ ] Replace nested attribute chains in message-order assertions with accessors where available.
  - [ ] Replace wildcard checks in mock client listener unregister logic with semantic helpers.
  - [ ] Preserve panic/error text where tests depend on exact strings, or update tests intentionally.
- [ ] Workstream D - Doctest mock transport modernization.
  - [ ] `up-streamer/src/lib.rs` doctest snippets.
  - [ ] `up-streamer/src/control_plane/mod.rs` doctest snippet.
  - [ ] `up-streamer/src/data_plane/mod.rs` doctest snippet.
  - [ ] `up-streamer/src/routing/mod.rs` doctest snippet.
  - [ ] Add `up-rust/test-util` feature wiring in `up-streamer/Cargo.toml` for doctest/test-only compilation.
  - [ ] Unify all doctests on the shared hidden `MockTransport` setup pattern from Gate D1.
- [ ] Workstream E - Remaining crate sweep.
  - [ ] Scan and remediate `configurable-streamer` for same pattern classes.
  - [ ] Scan and remediate `example-streamer-implementations` for same pattern classes.
  - [ ] Scan and remediate `example-streamer-uses` for same pattern classes.
  - [ ] Scan and remediate `up-linux-streamer-plugin` for same pattern classes.
- [ ] Workstream F - Residual idiom closure pass.
  - [ ] Close all Category R-A items from the residual backlog.
  - [ ] Resolve Category R-B with explicit perf/readability decisions.
  - [ ] Resolve Category R-C/R-D via conversion or explicit exemptions.
  - [ ] Ensure no public API surface changes from test-only or helper migrations.

## Phase 4 - Test and validation matrix

- [ ] Fast local gates after each workstream.
  - [ ] `cargo fmt -- --check`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo check --workspace --all-targets`
- [ ] Doctest-specific verification for mock migration.
  - [ ] `cargo test -p up-streamer --doc`
  - [ ] Confirm doctests compile without introducing brittle feature coupling.
- [ ] Full CI parity preflight (transport-affecting safe default matrix).
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo build`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo fmt -- --check`
  - [ ] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - [ ] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo test --workspace`
- [ ] Optional unbundled transport matrix (if touched code intersects transport/plugin integration paths).
  - [ ] Verify `VSOMEIP_INSTALL_PATH` is set and valid.
  - [ ] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Residual-closure verification gates.
  - [ ] Re-run targeted grep matrix for direct-field anti-patterns and capture zero/approved-only outcomes.
  - [ ] Verify Category R-A entries are fully converted.
  - [ ] Verify every retained Category R-B/C/D site appears in exemptions with exact file/line and rationale.

## Phase 5 - Local phased confidence commits + single squashed delivery commit

- [ ] Use local-only phased commits to build confidence while implementing.
  - [ ] Local commit L1: `up-streamer` accessor/helper migration (observability + routing).
  - [ ] Local commit L2: `utils/integration-test-utils` and related example alignment.
  - [ ] Local commit L3: doctest mock strategy migration (`up-rust::MockTransport` + feature wiring).
  - [ ] Local commit L4: residual sweep + tests + exemptions docs.
  - [ ] Do not push any `L*` local commits.
- [ ] For each local phase commit, enforce scope discipline.
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXPECTED_BRANCH"`
  - [ ] `git diff --name-only --cached`
  - [ ] `git diff --stat --cached`
  - [ ] Verify staged diff matches the declared phase intent only.
- [ ] Run confidence gates after each local phase commit.
  - [ ] `cargo fmt -- --check`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo check --workspace --all-targets`
  - [ ] Run focused tests for changed modules.
  - [ ] Log outcomes to `$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep-validation.md`.
- [ ] After all phases are green, squash only the remediation delta into one commit.
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXPECTED_BRANCH"`
  - [ ] `test -z "$(git status --porcelain)"`
  - [ ] `PRE_SQUASH_SHA="$(git rev-parse HEAD)"`
  - [ ] `PRE_SQUASH_TAG="pr-83-pre-squash-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `git tag "$PRE_SQUASH_TAG" "$PRE_SQUASH_SHA"`
  - [ ] `git reset --soft "$BRANCH_START_SHA"`
  - [ ] `git commit -m "<single PR-83 remediation commit message>"`
- [ ] Verify squash integrity before push.
  - [ ] `test "$(git rev-list --count "$BRANCH_START_SHA"..HEAD)" = "1"`
  - [ ] `test -z "$(git diff --name-status "$PRE_SQUASH_SHA"..HEAD)"`
  - [ ] Re-run at least fast gates (`fmt`, `clippy`, `check`) from the squashed commit.
- [ ] Publish policy for this remediation.
  - [ ] `git fetch origin "$EXPECTED_BRANCH"`
  - [ ] `REMOTE_PRE_PUSH_SHA="$(git rev-parse origin/$EXPECTED_BRANCH)"`
  - [ ] `test "$REMOTE_PRE_PUSH_SHA" = "$BRANCH_START_SHA"`
  - [ ] If remote branch drifted during local work, stop and restack from new remote head before push.
  - [ ] Push only the single squashed remediation commit on `origin/$EXPECTED_BRANCH`.
  - [ ] `git push origin "$EXPECTED_BRANCH"`
  - [ ] Never force-push for this sweep.
  - [ ] If accidental push occurs before squash, stop and define a recovery path before continuing.
- [ ] Preserve review ergonomics with explicit mapping.
  - [ ] Include a phased execution ledger in PR narrative.
  - [ ] Map each PR-83 review suggestion to exact file/line changes.
  - [ ] Where not adopted, provide concise rationale + exemption reference.

## Interruption and recovery playbook

- [ ] If interrupted before squash (during local `L*` commits), recover safely.
  - [ ] Re-run branch guard and clean-tree check.
  - [ ] Resume from current local `HEAD` and continue remaining phases.
  - [ ] If rollback is required, recover to `ROLLBACK_TAG` on the locked branch.
- [ ] If interrupted after creating `PRE_SQUASH_TAG` but before final push.
  - [ ] If squashed commit is missing or suspect, recover phased local stack from `PRE_SQUASH_TAG`.
  - [ ] Re-run squash integrity checks (`BRANCH_START_SHA..HEAD` count and tree parity).
- [ ] If interrupted after squash but before push.
  - [ ] Re-run fast validation gates (`fmt`, `clippy`, `check`).
  - [ ] Re-run remote drift checks before pushing.

## Phase 6 - Completion criteria

- [ ] All PR-83 review comments are either resolved in code or explicitly justified.
  - [ ] `up-rust` mock transport suggestion addressed by adopting `up-rust::MockTransport` in doctests.
  - [ ] Accessor-style suggestions (`id`, `type_`, `source`, `sink`) addressed.
  - [ ] Wildcard authority helper suggestion addressed.
- [ ] Branch discipline and squash policy are satisfied.
  - [ ] All remediation work executed on `cleanup/refactor-upstream-main-prA-architecture`.
  - [ ] Remediation delta from `BRANCH_START_SHA` to `HEAD` is exactly one commit.
  - [ ] No intermediate phase commits were pushed.
  - [ ] Remote pre-push drift check passed (`origin/$EXPECTED_BRANCH` still equals `BRANCH_START_SHA`).
  - [ ] `PROGRESS_FILE` finalized with completion markers.
- [ ] Sweep-level quality bars are met.
  - [ ] No remaining unreviewed occurrences of prioritized anti-patterns.
  - [ ] Residual backlog categories R-A through R-D are fully dispositioned (`done` or `exempt`).
  - [ ] Category R-A closure is complete without regressions.
  - [ ] Any retained direct-field usage in R-B/C/D is explicitly justified in exemptions.
  - [ ] All validation commands required by touched scope pass.
  - [ ] No new lint warnings or formatting drift.
- [ ] Handoff artifacts are complete.
  - [ ] Final sweep summary in `$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep-summary.md`.
  - [ ] Exemptions list in `$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep-exemptions.md`.
  - [ ] Command log/outcomes in `$OPENCODE_CONFIG_DIR/reports/pr-83-up-rust-sweep-validation.md`.

## Risk register and mitigations

- [ ] Risk R1 - Subtle behavior drift during accessor migration.
  - [ ] Mitigation: preserve fallback behavior and pin with unit tests before/after replacements.
- [ ] Risk R2 - Doctest dependency friction for `up-rust::MockTransport` feature wiring.
  - [ ] Mitigation: keep `test-util` scoped to dev-dependencies and validate via `cargo test -p up-streamer --doc`.
- [ ] Risk R3 - Over-broad local phase commits can hide regressions.
  - [ ] Mitigation: keep each local phase commit pattern-focused with staged scope checks.
- [ ] Risk R4 - Workspace feature interactions in CI matrices.
  - [ ] Mitigation: run CI parity preflight matrix before publishing updates.
- [ ] Risk R5 - Single-commit delivery can reduce execution traceability.
  - [ ] Mitigation: keep local phased ledger in validation report and summarize phase outcomes in PR notes.
- [ ] Risk R6 - Remote branch drift during local phased work invalidates squash base assumptions.
  - [ ] Mitigation: enforce pre-push remote SHA check against `BRANCH_START_SHA`; if drifted, stop and restack.
- [ ] Risk R7 - Over-eager accessor conversion introduces avoidable clones in owned-move paths.
  - [ ] Mitigation: keep direct owned-field moves where accessor conversion would add unnecessary allocation.
- [ ] Risk R8 - API-gap mutation paths get hidden instead of documented.
  - [ ] Mitigation: require explicit exemptions for any retained direct mutable protobuf internals (`.as_mut()`, `.0` field manipulation).

## Immediate first execution checklist

- [ ] Lock onto PR-83 branch and capture sweep anchor.
  - [ ] Resolve `EXPECTED_BRANCH` from PR metadata and verify it is `cleanup/refactor-upstream-main-prA-architecture`.
  - [ ] If currently on another branch (including `cleanup/refactor-upstream-main-prC-smoke`), switch before any build/test/edit action.
  - [ ] `git switch "$EXPECTED_BRANCH"` and verify tracking branch.
  - [ ] Assert clean start (`test -z "$(git status --porcelain)"`).
  - [ ] Capture `BRANCH_START_SHA` and create `ROLLBACK_TAG`.
- [ ] Initialize session-resume bookkeeping.
  - [ ] Create/update `PROGRESS_FILE` with `EXPECTED_BRANCH`, `BRANCH_START_SHA`, `REMOTE_BRANCH_SHA`, and `LAST_PHASE`.
  - [ ] Write a one-line startup checkpoint to validation report.
- [ ] Create inventory report skeleton and populate with current known hotspots.
  - [ ] Start with `up-streamer/src/observability/fields.rs` and `up-streamer/src/routing/publish_resolution.rs`.
  - [ ] Add `utils/integration-test-utils` and doctest modules next.
- [ ] Resolve Gate D1 (`up-rust::MockTransport` adoption) early to avoid churn.
  - [ ] Apply across all doctest modules in one focused pass.
  - [ ] Validate feature scoping remains internal and does not alter public API surface.
- [ ] Execute Workstream A first (highest signal from existing review comments).
  - [ ] Re-run focused tests/doctests.
  - [ ] Capture result snapshot in validation report.
- [ ] Run Workstream F (residual idiom closure) before squash.
  - [ ] Tackle `up-streamer/src/data_plane/ingress_listener.rs:78` first (`payload_format()` accessor conversion).
  - [ ] Then apply low-risk authority accessor conversions (R-A list).
  - [ ] Decide R-B/C/D items and record exemptions where conversion is not appropriate.
  - [ ] Re-run residual-closure verification gates and update reports.
