# up-streamer Subscription-Provider Decoupling + Pub/Sub Refresh Plan

Date: 2026-02-10
Execution branch: `refactor/up-streamer-domain-architecture`

## Why this plan exists

This plan captures the agreed architecture to keep `uStreamer` useful as the primary library for streamer binaries while avoiding hard coupling to `up-subscription-rust` and aligning with `up-spec` expectations.

The plan is detailed so a fresh session can execute without rediscovery.

## Context and findings (source-of-truth for this plan)

- `uSubscription` is the canonical subscription ledger and remote subscription orchestrator (per `up-spec` L3 uSubscription docs).
- `uStreamer` is the dispatcher/router (per `up-spec` L2 dispatchers docs), and should forward subscribe/unsubscribe RPC traffic via routes like any other RPC messages.
- Current `up-streamer` startup bootstrap fetch uses wildcard subscriber semantics that are risky for canonical live mode compatibility.
- Current startup path can hard-fail on subscription fetch; this creates undesirable bootstrap coupling.
- Example binaries currently work because they rely on static-file subscription data.
- Target workspace topology should remove `subscription-cache` as a standalone crate while retaining `usubscription-static-file` as an adapter crate.
- Live interoperability against a running `up-subscription-rust` runtime is deferred from this phase and captured as follow-up readiness.

## Locked design decisions (do not re-open unless blocker)

1. **No direct dependency on `up-subscription-rust` crates from `up-streamer`.**
   - Live mode integration uses `up-rust` APIs (including `RpcClientUSubscription`) only.

2. **`up-streamer` constructor accepts `Arc<dyn USubscription>`.**
   - `USubscription` from `up-rust` is the subscription source contract for both static and live modes.
   - We do not require backward-compatible constructor overloads.

3. **Static mode remains default for example binaries and plugin configs.**
   - Deterministic and portable out-of-the-box behavior is preserved.

4. **Live canonical mode is optional and adapter-driven.**
   - Production cases can call out to a real uSubscription service through the live adapter.

5. **Startup bootstrap is best-effort, not fatal.**
   - Streamer starts with empty publish-derived routing state if initial fetch fails.
   - Request/response/notification route setup still succeeds.

6. **Only one new public lifecycle mutator API is required: `refresh_subscriptions()`.**
   - Public `replace_subscriptions(snapshot)` is intentionally not added.
   - `refresh_subscriptions()` returns `Result<SubscriptionSyncHealth, UStatus>`.
   - On failed refresh attempts, internal sync health is still updated and retrievable via `subscription_sync_health()`.

7. **Public refresh visibility is health-only metadata, not subscription data.**
   - Expose lightweight sync health only (timestamps + attempt success booleans).
   - Do not expose subscription counts/deltas/listings through `uStreamer` refresh APIs.
   - Canonical subscription details remain the responsibility of the `uSubscription` service.

8. **Rust docs must show both usage modes.**
   - Static-file mode example.
   - Live canonical mode example.

9. **Workspace crate topology target is explicit: one fewer crate.**
   - Remove standalone `subscription-cache` crate by folding its logic into `up-streamer` internal modules.
   - Keep `usubscription-static-file` as an adapter crate.
   - Ensure `up-streamer` does not rely on `usubscription-static-file` as a runtime dependency.

10. **Live `up-subscription-rust` integration is deferred from this phase.**
   - This phase uses static mode as default and keeps `live_usubscription` as a reserved/fail-fast runtime option in required streamer binaries.
   - `up-streamer` crate must not gain direct `up-subscription-rust` dependency.
   - Follow-up phase will add real live-runtime E2E once compatibility/stability are explicitly approved.

## High-level architecture target

`UStreamer` consumes `USubscription` at creation time:

```rust
pub async fn new(
    name: &str,
    message_queue_size: u16,
    usubscription: Arc<dyn USubscription>,
) -> Result<Self, UStatus>
```

Public refresh API:

```rust
pub async fn refresh_subscriptions(&mut self) -> Result<SubscriptionSyncHealth, UStatus>
```

Internal-only apply API (not public):

```rust
async fn apply_subscription_snapshot(
    &mut self,
    snapshot: FetchSubscriptionsResponse,
) -> Result<(), UStatus>
```

Public sync-health API:

```rust
pub struct SubscriptionSyncHealth {
    pub last_attempt_at: Option<SystemTime>,
    pub last_success_at: Option<SystemTime>,
    pub last_attempt_succeeded: Option<bool>,
    pub previous_attempt_succeeded: Option<bool>,
}

pub fn subscription_sync_health(&self) -> SubscriptionSyncHealth
```

## USubscription wiring strategy required by this plan

- **Static mode** (default examples): pass `USubscriptionStaticFile` as `Arc<dyn USubscription>`.
- **Live mode** (future phase): pass a live `USubscription` client (e.g. `RpcClientUSubscription`) using a spec-compatible fetch strategy.
- `up-streamer` core remains runtime-agnostic while using the canonical `USubscription` contract.
- `usubscription-static-file` remains outside `up-streamer` as an adapter crate implementing `USubscription`.
- `example-streamer-implementations` and `configurable-streamer` must expose a reserved `live_usubscription` mode that fails fast with clear guidance in this phase.

## Explicit non-goals

- No direct embedding of `up-subscription-rust` service logic into `up-streamer`.
- No second public API for snapshot replacement.
- No public API that duplicates canonical `uSubscription` state introspection.
- No widening this effort into unrelated transport or domain refactors.
- No direct `up-subscription-rust` dependency added to `up-streamer` crate.

## Execution mode

- [x] Manual execution only.
- [x] Follow phases/gates in strict order.
- [x] Update checkboxes continuously (`[ ]` -> `[x]` immediately when completed).

## Fresh-session preflight

- [x] Confirm OPENCODE config path is available and writable:
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `[ -n "$OPENCODE_CONFIG_DIR" ] && [ -w "$OPENCODE_CONFIG_DIR" ]`
- [x] Confirm branch and working tree:
  - [x] `git status --short --branch`
  - [x] Branch is `refactor/up-streamer-domain-architecture`.
- [x] Confirm required tooling exists:
  - [x] `command -v cargo`
  - [x] `command -v rg`
  - [x] `docker compose version`
  - [x] `command -v gh`
- [x] Confirm no stale transport processes before starting:
  - [x] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`

### Preflight gate

- [x] Session preconditions are satisfied.

## Artifact policy

All artifacts for this effort must be written under:

`$OPENCODE_CONFIG_DIR/reports/usubscription-decoupled-pubsub-migration/`

- [x] `00-spec-and-coupling-baseline.md`
- [x] `01-api-contract-and-design-lock.md`
- [x] `02-core-implementation-notes.md`
- [x] `03-provider-modes-and-docs.md`
- [x] `04-validation-summary.md`
- [x] `05-live-integration-deferred.md`

Smoke-skill evidence must be under:

`$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`

Each evidence entry must include:

- exact command
- working directory (if not repo root)
- exit status/pass-fail
- key output lines proving the result
- concise conclusion

## Blocking policy

- [ ] If a gate fails, stop progression.
- [ ] Record blocker details in the active phase report:
  - [ ] exact failing command
  - [ ] working directory
  - [ ] exit status
  - [ ] key output lines
  - [ ] concrete remediation path
- [ ] Resume only after blocker resolution evidence is captured.

---

## Phase 0 - Baseline and compatibility constraints

### 0.1 Baseline behavior capture

- [x] Capture current startup bootstrap flow and failure mode in `up-streamer`.
- [x] Capture current route registration/listener behavior for request vs publish traffic.
- [x] Capture current wildcard-based subscription fetch assumptions.
- [x] Capture current provider-wiring capabilities in:
  - [x] `example-streamer-implementations` (Zenoh<->SOME/IP)
  - [x] `configurable-streamer` (Zenoh<->MQTT)

### 0.2 Spec alignment notes

- [x] Capture relevant spec clauses from:
  - [x] `up-spec/up-l3/usubscription/v3/README.adoc`
  - [x] `up-spec/up-l2/dispatchers/README.adoc`
  - [x] `up-spec/basics/uattributes.adoc`
- [x] Map each current behavior to spec-compatible / spec-risk / unknown.

### 0.3 Coupling baseline

- [x] Verify dependency/coupling state:
  - [x] `cargo tree --workspace --all-features | rg "up-subscription-rust|(^| )up-subscription v" || true`
  - [x] `cargo tree -i subscription-cache`
  - [x] `cargo tree -i usubscription-static-file`
  - [x] `rg -n "subscription-cache|usubscription-static-file" Cargo.toml up-streamer/Cargo.toml utils/usubscription-static-file/Cargo.toml`
  - [x] `rg -n "up-subscription|RpcClientUSubscription|InMemoryRpcClient" up-streamer/Cargo.toml configurable-streamer/Cargo.toml example-streamer-implementations/Cargo.toml`
- [x] Record crate-level vs runtime-level coupling risks.

### Gate 0

- [x] Baseline and constraints are captured with explicit go-forward rules.

---

## Phase 1 - API contract and design-lock implementation plan

### 1.1 Public API contract

- [x] Update `UStreamer::new(...)` to require `Arc<dyn USubscription>`.
- [x] Define and expose `refresh_subscriptions()` as the only new public lifecycle API.
  - [x] Return type: `Result<SubscriptionSyncHealth, UStatus>`.
- [x] Do not expose `replace_subscriptions(snapshot)` publicly.
- [x] Define and expose `SubscriptionSyncHealth` public struct:
  - [x] `last_attempt_at: Option<SystemTime>`
  - [x] `last_success_at: Option<SystemTime>`
  - [x] `last_attempt_succeeded: Option<bool>`
  - [x] `previous_attempt_succeeded: Option<bool>`
- [x] Define and expose `subscription_sync_health()` accessor.
- [x] Ensure refresh-related public API does not expose subscription list/count/delta detail.

### 1.2 Internal behavior contract

- [x] Define internal atomic snapshot-apply helper with rollback on failure.
- [x] Define startup bootstrap semantics:
  - [x] initial snapshot fetch attempts on startup
  - [x] startup does not fail when fetch fails
  - [x] startup logs include explicit deferred-refresh status
- [x] Define sync-health update semantics for startup/bootstrap and explicit refresh attempts.
- [x] Define refresh failure semantics: health is updated even when `refresh_subscriptions()` returns `Err(UStatus)`.

### 1.3 Call-site migration contract

- [x] Define migration for required streamer binaries:
  - [x] `configurable-streamer/src/main.rs`
  - [x] `example-streamer-implementations/src/bin/zenoh_someip.rs`
- [x] Define optional migration scope for `up-linux-streamer-plugin/src/lib.rs` (only if touched in this execution).
- [x] Ensure static mode remains default in migrated call sites.
- [x] Add explicit runtime config switch for provider mode in required streamer binaries (e.g. `static_file` vs `live_usubscription`).
- [x] Define reserved/fail-fast behavior for `live_usubscription` mode in this phase:
  - [x] select mode -> deterministic `UNIMPLEMENTED`/config error at startup
  - [x] error message must state live integration is deferred and point to follow-up plan/report

### 1.4 Workspace topology migration contract

- [x] Plan removal of standalone `subscription-cache` crate and inlining into `up-streamer`.
- [x] Plan retention of `usubscription-static-file` as external adapter crate.
- [x] Plan dependency cleanup so `up-streamer` has no runtime dependency on `usubscription-static-file`.
- [x] Plan dependency cleanup so `usubscription-static-file` has no stale dependency on removed `subscription-cache` crate.
- [x] Do not add workspace-level `up-subscription-rust` dependencies in this phase.

### Gate 1

- [x] API contract is documented and locked in `01-api-contract-and-design-lock.md`.

---

## Phase 2 - Core implementation in `up-streamer`

### 2.1 Core changes

- [x] Wire `USubscription` into `UStreamer` construction path.
- [x] Store `USubscription` handle in `UStreamer` state for later refresh calls.
- [x] Implement `refresh_subscriptions()`.
- [x] Implement internal snapshot apply/rollback helper.
- [x] Ensure startup path is non-fatal when initial snapshot fetch fails.
- [x] Add `SubscriptionSyncHealth` state ownership in `UStreamer`.
- [x] Update sync-health state on every refresh attempt (success/failure) and startup bootstrap attempt.
- [x] Ensure successful `refresh_subscriptions()` returns current `SubscriptionSyncHealth`.
- [x] Move `subscription-cache` code into `up-streamer` internal module(s) and update imports/call sites.
- [x] Remove `subscription-cache` crate from workspace manifests.
- [x] Remove stale `subscription-cache` dependency from `utils/usubscription-static-file/Cargo.toml`.

### 2.2 Behavior preservation requirements

- [x] Request/response/notification route behavior remains unchanged.
- [x] Publish listener registration behavior remains deterministic under snapshot refresh.
- [x] Existing route lifecycle idempotency remains intact.

### 2.3 Internal validation

- [x] Add/adjust tests for startup best-effort + refresh semantics.
- [x] Add/adjust tests for apply rollback when refresh fails mid-apply.
- [x] Add/adjust tests for `SubscriptionSyncHealth` transitions:
  - [x] initial empty state
  - [x] first failed attempt
  - [x] subsequent successful attempt
  - [x] `previous_attempt_succeeded` rollover behavior
  - [x] `refresh_subscriptions()` success path returns expected `SubscriptionSyncHealth`
  - [x] failed `refresh_subscriptions()` still updates health retrievable via `subscription_sync_health()`
- [x] Record implementation evidence in `02-core-implementation-notes.md`.

### Gate 2

- [x] Core compiles and tests pass with `USubscription`-based constructor and refresh behavior.

---

## Phase 3 - Subscription modes and docs

### 3.1 Static mode (default mode)

- [x] Implement/retain static `USubscription` adapter for deterministic examples.
- [x] Keep static mode default in example binaries/plugin configs.
- [x] Keep `usubscription-static-file` as a standalone adapter crate.

### 3.2 Reserved live mode (deferred implementation in this phase)

- [x] Keep live mode represented in config schema as `live_usubscription`.
- [x] Implement fail-fast runtime path for `live_usubscription` in required binaries (no silent fallback).
- [x] Ensure error text clearly explains deferral and follow-up work item.
- [x] Do not introduce direct dependency on `up-subscription-rust` crates in `up-streamer`.

### 3.3 Rust docs updates (mandatory)

- [x] Update `up-streamer` rustdoc with two explicit setup sections and snippets:
  - [x] **Static Configuration Mode**
  - [x] **Live Canonical uSubscription Mode**
- [x] Ensure docs clearly explain what trait object is handed to `UStreamer::new(...)` in each case.
- [x] Document public sync-health semantics and explicitly state that canonical subscription detail remains in `uSubscription`.
- [x] For this phase, document `live_usubscription` as reserved/fail-fast in streamer binaries and reference deferred integration follow-up.
- [x] `cargo test -p up-streamer --doc` passes.

### 3.4 Coupling guard proof

- [x] Capture dependency proof showing no direct `up-subscription-rust` crate coupling in `up-streamer`.
- [x] Capture dependency proof that `subscription-cache` crate no longer exists as a workspace member.
- [x] Capture dependency proof that `up-streamer` has no runtime dependency on `usubscription-static-file`.
- [x] Record in `03-provider-modes-and-docs.md`.

### Gate 3

- [x] Static mode and reserved-live mode behavior are implemented and documented; static remains default.
- [x] Workspace topology target is met: one fewer crate (`subscription-cache` removed, `usubscription-static-file` retained).
- [x] Required streamer binaries expose reserved `live_usubscription` mode with deterministic fail-fast behavior.

---

## Phase 4 - CI parity + transport smoke validations

### 4.1 CI parity matrix

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] If transport/plugin integration is touched, run unbundled checks:
  - [x] confirm `VSOMEIP_INSTALL_PATH` valid (checked and unavailable in this environment)
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport` (constrained skip: missing `VSOMEIP_INSTALL_PATH`)
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (constrained skip: missing `VSOMEIP_INSTALL_PATH`)
  - [x] if unavailable, record constrained skip + remediation in `04-validation-summary.md`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### 4.2 Full smoke skill execution (all 8)

- [x] Pre-run stale-process evidence:
  - [x] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`
- [x] Skill reference: `$OPENCODE_CONFIG_DIR/skills/transport-smoke-validation/SKILL.md`
- [x] Execute all eight smoke skills (recovered from existing evidence from prior run in this branch/session window):
  - [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
- [x] Post-run stale-process evidence:
  - [x] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`
- [x] Verify smoke artifacts:
  - [x] per-skill evidence directories under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-*/`
  - [x] summary at `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`

### 4.3 Mode-specific acceptance checks

- [x] Static mode passes CI + smoke checks.
- [x] `live_usubscription` mode fails fast with expected error semantics in required binaries.
- [x] Both outcomes documented in `04-validation-summary.md`.

### 4.4 Deferred live integration follow-up readiness

- [x] Record deferred-live rationale and prerequisites in `05-live-integration-deferred.md`.
- [x] Capture explicit follow-up entry criteria for enabling real `up-subscription-rust` E2E in a later phase.

### Gate 4

- [x] CI parity matrix green (base + bundled green; unbundled constrained-skip documented with remediation).
- [x] All 8 smoke skills green.
- [x] Both subscription modes validated.
- [x] Deferred-live follow-up readiness is documented.

---

## Commit discipline (mandatory)

Before every commit:

- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`

Suggested commit chunks:

- [x] `USubscription` API + core startup/refresh behavior
- [x] static adapter + reserved-live config/fail-fast call-site migration
- [x] rustdocs + tests + validation artifacts

---

## Final gate

- [x] `uSubscription` remains canonical subscription source; `uStreamer` remains dispatcher/router.
- [x] `uStreamer` accepts `Arc<dyn USubscription>` at creation for both static and live modes.
- [x] Startup is non-fatal when initial subscription fetch fails.
- [x] Public API includes `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>`; no public `replace_subscriptions(snapshot)` is added.
- [x] Public refresh visibility is limited to `SubscriptionSyncHealth` (timestamps + attempt outcomes only).
- [x] Example binaries remain deterministic by default static mode.
- [x] Live canonical mode remains deferred; `live_usubscription` is reserved/fail-fast in this phase.
- [x] Workspace has one fewer crate: `subscription-cache` removed; `usubscription-static-file` retained as adapter.
- [x] CI parity + full 8-skill smoke validations are green with evidence (unbundled matrix constrained-skip with remediation recorded).
- [x] Fresh session can execute end-to-end using this plan alone.
