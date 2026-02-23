# Deferred Live Integration Readiness

Status: completed

## Deferral rationale

- This phase is intentionally scoped to decouple `up-streamer` from direct `up-subscription-rust` crate coupling while preserving deterministic streamer startup and routing behavior.
- Static `USubscription` provider mode remains the default for required binaries to keep examples/CI portable and reproducible.
- `live_usubscription` is retained as a reserved config mode and must fail fast with explicit `UNIMPLEMENTED` guidance, avoiding silent fallback.
- Real live-runtime E2E interoperability is deferred until environment and compatibility prerequisites are satisfied and explicitly approved.

## Prerequisites

1. Runtime + environment availability
   - A reachable `uSubscription` runtime endpoint compatible with `up-rust` `USubscription` trait/RPC semantics.
   - Stable Zenoh/MQTT/SOMEIP runtime environment for repeatable E2E validation.
   - Valid external vsomeip install tree exported via `VSOMEIP_INSTALL_PATH` to re-enable unbundled CI parity checks.

2. Contract and behavior alignment
   - Confirmed canonical live fetch strategy and query semantics against `uSubscription` service behavior.
   - Confirmed authorization/identity/topic assumptions for subscription fetch and refresh in deployed environments.
   - Preserved public API boundary: `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>` and health-only visibility.

3. Validation coverage readiness
   - Live-mode integration tests that verify startup, refresh success/failure health transitions, and route-update behavior.
   - Cross-transport live-mode smoke coverage (at least RR both directions, then pub/sub) with deterministic pass/fail markers.

## Entry criteria for follow-up phase

Follow-up implementation may begin only when all items below are true:

1. `VSOMEIP_INSTALL_PATH` is valid and unbundled CI parity commands are runnable in the target environment.
2. Live runtime endpoint and credentials/config are available for automated test execution.
3. A concrete adapter implementation plan exists for wiring live `USubscription` provider mode in required binaries without adding direct `up-subscription-rust` dependency to `up-streamer`.
4. Reserved-mode fail-fast behavior can be replaced by real live mode while preserving static default behavior.
5. Validation plan includes:
   - CI parity matrix (base + bundled + unbundled) green,
   - canonical smoke scenarios green,
   - explicit refresh/sync-health behavior checks under live mode.
