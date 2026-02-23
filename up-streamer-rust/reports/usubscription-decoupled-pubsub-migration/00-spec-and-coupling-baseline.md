# Phase 0 - Spec and Coupling Baseline

Status: completed

## 0.1 Baseline behavior capture

### Startup bootstrap flow and failure mode (`up-streamer`)

- `UStreamer::new(name, message_queue_size, usubscription)` currently accepts `Arc<dyn USubscription>` directly (no provider abstraction yet): `up-streamer/src/ustreamer.rs:43-47`.
- Startup builds a wildcard subscriber URI (`authority="*"`, `ue_id=0x0000_FFFF`, `ue_version_major=0xFF`, `resource_id=0xFFFF`) and sends `FetchSubscriptionsRequest` by subscriber: `up-streamer/src/ustreamer.rs:54-73`.
- Fetch path calls `subscription_runtime::fetch_subscriptions(...)`, which executes:
  - `SUBSCRIPTION_RUNTIME.block_on(usubscription.fetch_subscriptions(...)).expect("Failed to fetch subscriptions")`
  - File: `up-streamer/src/runtime/subscription_runtime.rs:21-29`
- Resulting failure semantics:
  - Fetch error causes panic (`expect`) before constructor can return a recoverable error.
  - Snapshot parse/build error in `SubscriptionCache::new(...)` returns `Err(UStatus::INVALID_ARGUMENT)` from constructor: `up-streamer/src/ustreamer.rs:74-85`.

### Route registration/listener behavior for request vs publish traffic

- Request/notification/RPC listener path:
  - Registers one listener using source wildcard of ingress authority and sink wildcard of egress authority (`authority_to_wildcard_filter(...)` for both): `up-streamer/src/data_plane/ingress_registry.rs:143-156`.
  - This listener is always attempted first; failure triggers rollback and returns `FailedToRegisterRequestRouteListener`: `up-streamer/src/data_plane/ingress_registry.rs:151-166`.
- Publish listener path:
  - Loads route subscribers from `SubscriptionDirectory::lookup_route_subscribers(out_authority, ...)` with wildcard merge behavior: `up-streamer/src/data_plane/ingress_registry.rs:173-180`, `up-streamer/src/routing/subscription_directory.rs:21-39`.
  - `PublishRouteResolver` derives source filters from subscription topics where topic authority is ingress authority or `*`, then rewrites authority to ingress authority for listener registration: `up-streamer/src/routing/publish_resolution.rs:34-91`.
  - Each derived source filter is registered with sink `None` (publish semantics): `up-streamer/src/data_plane/ingress_registry.rs:189-216`.
- Route lifecycle/idempotency:
  - Registry is refcounted by transport+ingress+egress key; duplicate route increments count and avoids duplicate listener registrations: `up-streamer/src/data_plane/ingress_registry.rs:127-137`.
  - Unregister decrements refcount; physical listener removal only at zero: `up-streamer/src/data_plane/ingress_registry.rs:241-303`.

### Current wildcard-based subscription fetch assumptions

- Constructor uses wildcard subscriber URI to fetch "all" subscriptions via `FetchSubscriptionsRequest.subscriber`.
- Assumption: backend accepts wildcard subscriber identity and returns a comprehensive snapshot.
- This assumption is not guaranteed by current uSubscription spec constraints (see section 0.2, spec-risk classification).

### Provider-wiring capabilities in streamer binaries

- `example-streamer-implementations` (`zenoh_someip`):
  - Always instantiates static adapter `USubscriptionStaticFile` from `config.usubscription_config.file_path`.
  - Passes static adapter directly into `UStreamer::new(...)`.
  - No provider mode switch (`static_file` vs `live_usubscription`) exists yet.
  - File: `example-streamer-implementations/src/bin/zenoh_someip.rs:59-67`.
- `configurable-streamer`:
  - Same static-only wiring pattern (`USubscriptionStaticFile` + direct constructor pass).
  - No runtime mode selector for reserved live mode.
  - File: `configurable-streamer/src/main.rs:62-70`.

## 0.2 Spec alignment notes

### Captured spec clauses

- `up-spec/up-l3/usubscription/v3/README.adoc`
  - Remote subscription architecture requires dispatcher (`uStreamer`) forwarding and `uSubscription` bookkeeping as source of subscription state (`lines 50-52`).
  - `FetchSubscriptions()` by subscriber must return topics subscribed by that subscriber (`lines 253-256`).
  - `FetchSubscriptions()` must reject wildcard topic/subscriber fields with `INVALID_ARGUMENT` (`lines 263-284`).
- `up-spec/up-l2/dispatchers/README.adoc`
  - Dispatcher role is routing/forwarding without payload inspection (`lines 23-40`).
  - Dispatcher must forward UMessage attributes (`line 71`).
  - Dispatcher handles delivery failures with response/error semantics for RPC (`line 80+`).
- `up-spec/basics/uattributes.adoc`
  - Publish source resource range `[0x8000, 0xFFFE]`, optional sink authority-only (`lines 205-226`).
  - Request: source resource `0`, sink resource `[1, 0x7FFF]` (`lines 290-311`).
  - Response: source resource `[1, 0x7FFF]`, sink resource `0` (`lines 371-392`).

### Behavior map: spec-compatible vs spec-risk vs unknown

- **Spec-compatible**
  - Dispatcher/router role separation in architecture intent (route-centric forwarding across transports).
  - Request vs publish listener split aligns with attribute-domain distinctions (request/notification with sink; publish with sink `None`).
  - Route registry refcount lifecycle preserves deterministic listener registration/unregistration.
- **Spec-risk**
  - Wildcard subscriber bootstrap in `UStreamer::new` conflicts with explicit `FetchSubscriptions` invalid-subscriber wildcard constraints.
  - Startup hard dependency on successful fetch (`expect`) violates best-effort startup objective and risks coupled availability.
  - `up-streamer` currently directly depends on `usubscription-static-file`, reducing provider-agnosticity.
- **Unknown / follow-up needed**
  - Real live-runtime interoperability behavior against canonical `up-subscription-rust` under current fetch strategy.
  - Pagination and stable ordering handling for large subscription sets in future live provider implementation.

## 0.3 Coupling baseline

### Commands and outputs

1) Command:
```bash
cargo tree --workspace --all-features | rg "up-subscription-rust|(^| )up-subscription v" || true
```
- Working directory: repo root
- Exit: 0
- Key output: no crate matches reported
- Conclusion: no direct workspace dependency on `up-subscription-rust` / `up-subscription` crate names at baseline.

2) Command:
```bash
cargo tree -i subscription-cache
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `subscription-cache v0.1.0 (.../subscription-cache)`
  - reverse deps include `up-streamer`, `usubscription-static-file`, and transitive consumers (`configurable-streamer`, `up-linux-streamer`, `up-linux-streamer-plugin`).
- Conclusion: `subscription-cache` is still a shared workspace crate with broad transitive coupling.

3) Command:
```bash
cargo tree -i usubscription-static-file
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `usubscription-static-file v0.1.0 (.../utils/usubscription-static-file)`
  - reverse deps include `up-streamer` directly and streamer binaries/plugins.
- Conclusion: `up-streamer` currently has a runtime dependency on static adapter crate (must be removed).

4) Command:
```bash
rg -n "subscription-cache|usubscription-static-file" Cargo.toml up-streamer/Cargo.toml utils/usubscription-static-file/Cargo.toml
```
- Working directory: repo root
- Exit: 0
- Key output lines:
  - `Cargo.toml:22:    "subscription-cache",`
  - `up-streamer/Cargo.toml:34:subscription-cache = {path="../subscription-cache"}`
  - `up-streamer/Cargo.toml:35:usubscription-static-file = {path="../utils/usubscription-static-file"}`
  - `utils/usubscription-static-file/Cargo.toml:27:subscription-cache = {path="../../subscription-cache"}`
- Conclusion: workspace topology still includes `subscription-cache`, and both `up-streamer` and static adapter point to it.

5) Command:
```bash
rg -n "up-subscription|RpcClientUSubscription|InMemoryRpcClient" up-streamer/Cargo.toml configurable-streamer/Cargo.toml example-streamer-implementations/Cargo.toml
```
- Working directory: repo root
- Exit: 1
- Key output lines: none
- Conclusion: no direct `up-subscription-rust` runtime dependency currently present in target manifests.

### Coupling risk summary

- **Crate-level coupling risk:** `subscription-cache` is a standalone crate used by both `up-streamer` and `usubscription-static-file`, preventing the target topology reduction and internalization.
- **Runtime-level coupling risk:** `up-streamer` directly depends on static-file adapter crate and directly speaks `USubscription` in constructor, reducing clean provider abstraction boundaries.

## Gate 0 conclusion

Gate status: pass.

Go-forward rules captured from baseline:

1. Replace direct `USubscription` constructor input with provider trait object owned by `up-streamer` API.
2. Remove wildcard-only bootstrap assumption and shift startup to non-fatal best-effort refresh semantics.
3. Internalize subscription-cache logic into `up-streamer`; remove standalone `subscription-cache` crate.
4. Keep `usubscription-static-file` as adapter crate, but remove `up-streamer` runtime dependency on it.
5. Keep direct `up-subscription-rust` integration deferred, with reserved/fail-fast `live_usubscription` mode at required call sites.
