# Phase 1 - API Contract and Design Lock

Status: completed

## Revision note

This phase was re-locked to use `USubscription` from `up-rust` directly instead of a custom snapshot-provider trait.

## Public API contract

Locked API shape for `up-streamer`:

```rust
pub struct SubscriptionSyncHealth {
    pub last_attempt_at: Option<SystemTime>,
    pub last_success_at: Option<SystemTime>,
    pub last_attempt_succeeded: Option<bool>,
    pub previous_attempt_succeeded: Option<bool>,
}

impl UStreamer {
    pub async fn new(
        name: &str,
        message_queue_size: u16,
        usubscription: Arc<dyn USubscription>,
    ) -> Result<Self, UStatus>;

    pub async fn refresh_subscriptions(&mut self) -> Result<SubscriptionSyncHealth, UStatus>;

    pub fn subscription_sync_health(&self) -> SubscriptionSyncHealth;
}
```

Contract constraints:

- `refresh_subscriptions()` is the only new public lifecycle mutator.
- No public `replace_subscriptions(snapshot)` API.
- Public refresh visibility is metadata only (`SubscriptionSyncHealth`) and does not expose subscription list/count/delta internals.

## Internal behavior contract

Locked internal semantics:

1. `UStreamer::new(...)` performs one bootstrap fetch attempt via `USubscription::fetch_subscriptions(...)`.
2. Bootstrap fetch failure is non-fatal:
   - Streamer still starts with empty publish-derived subscription state.
   - Request/response/notification route setup remains available.
3. Internal apply helper is private and atomic from public perspective:
   - Build candidate subscription state from fetched snapshot.
   - On apply failure, retain prior state (rollback/no partial externally visible state).
4. Sync-health update rules:
   - Every fetch attempt (startup and explicit refresh) updates `last_attempt_at`.
   - Success updates `last_success_at` and rolls `previous_attempt_succeeded`.
   - Failure updates attempt booleans and rolls previous attempt, even when returning `Err(UStatus)`.
5. `refresh_subscriptions()` behavior:
   - On success: returns current health snapshot.
   - On failure: returns `Err(UStatus)` while still updating internal health retrievable by `subscription_sync_health()`.

## Call-site migration contract

Required binaries:

- `configurable-streamer/src/main.rs`
- `example-streamer-implementations/src/bin/zenoh_someip.rs`

Optional (touched in this execution):

- `up-linux-streamer-plugin/src/lib.rs`

Mode contract for required binaries:

1. Add explicit mode config selector:
   - `static_file` (default)
   - `live_usubscription` (reserved in this phase)
2. `static_file` path:
   - instantiate static adapter and pass `Arc<dyn USubscription>` to `UStreamer::new(...)`.
3. `live_usubscription` path (this phase):
   - deterministic fail-fast startup return (`UNIMPLEMENTED`/config error semantics)
   - explicit error text: live integration deferred; point to deferred follow-up report
   - no silent fallback to static mode.

## Workspace topology migration contract

Locked workspace topology changes:

1. Remove standalone workspace crate `subscription-cache`.
2. Inline equivalent subscription cache/index logic into `up-streamer` internal modules.
3. Retain `utils/usubscription-static-file` as adapter crate.
4. Remove `up-streamer -> usubscription-static-file` runtime dependency.
5. Remove `usubscription-static-file -> subscription-cache` dependency.
6. Do not add `up-subscription-rust` direct dependency to `up-streamer` or workspace in this phase.

## Gate 1 conclusion

Gate status: pass.

Design/API is locked for implementation in Phase 2 with the following non-negotiables:

- Canonical subscription source remains `uSubscription`; `uStreamer` stays dispatcher/router.
- Constructor takes `Arc<dyn USubscription>`.
- Startup bootstrap is best-effort non-fatal.
- Refresh API returns health-only metadata.
- Static mode stays default; `live_usubscription` is reserved fail-fast.
- `subscription-cache` crate is removed from workspace topology.
