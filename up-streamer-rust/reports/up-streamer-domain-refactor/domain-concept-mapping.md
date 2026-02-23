# Domain Concept Mapping

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Map current implementation concepts to middleware/communications domain concepts and ownership layers.

## Naming Boundary Rule

- [x] Outward API and user-facing docs remain streamer-centric.
- [x] Internal modules/types use domain terminology where it improves maintainability.

## Glossary and Mapping

| Current construct | Current location | Domain concept | Target layer | Target module/file | Notes |
|---|---|---|---|---|---|
| `UStreamer` | `up-streamer/src/ustreamer.rs` | Streamer Orchestrator | API Facade + Control Plane | `up-streamer/src/api/streamer.rs` | Owns route lifecycle orchestration, rollback, and outward API contract. |
| `Endpoint` | `up-streamer/src/endpoint.rs` | Transport Endpoint Descriptor | API Facade | `up-streamer/src/api/endpoint.rs` | Keep streamer-centric outward naming; remove implicit global logger init in later phase. |
| forwarding rule set | `up-streamer/src/ustreamer.rs` | Route Table | Control Plane | `up-streamer/src/control_plane/route_table.rs` | Compatibility-sensitive key includes authorities + `ComparableTransport` pointer identity. |
| listener lifecycle logic | `up-streamer/src/ustreamer.rs` | Ingress Listener Registry | Data Plane | `up-streamer/src/data_plane/ingress_registry.rs` | Handles register/unregister symmetry and add-failure backpedal paths. |
| transport forwarder lifecycle | `up-streamer/src/ustreamer.rs` | Egress Forwarder Pool | Data Plane | `up-streamer/src/data_plane/egress_pool.rs` | Active-count reference tracking around per-out-transport worker ownership. |
| publish filter derivation | `up-streamer/src/ustreamer.rs` | Publish Route Resolution Policy | Routing | `up-streamer/src/routing/publish_resolution.rs` | Left authority and tuple strictness encoded in `publish_source_uri_for_rule`. |
| wildcard subscriber merge | `subscription-cache/src/lib.rs` + `up-streamer/src/ustreamer.rs` | Subscription Directory Lookup Policy | Routing | `up-streamer/src/routing/subscription_directory.rs` | Exact + wildcard authority merge is split across cache and listener setup/removal. |
| `TransportForwarder` loop | `up-streamer/src/ustreamer.rs` | Egress Dispatch Worker | Data Plane | `up-streamer/src/data_plane/egress_worker.rs` | Thread-spawned runtime forwards queued messages and logs send failures. |
| callback runtime bootstrap (`CB_RUNTIME`) | `up-streamer/src/ustreamer.rs` | Runtime Integration Adapter | Runtime | `up-streamer/src/runtime/subscription_runtime.rs` | Dedicated runtime currently used for subscription bootstrap fetch in constructor. |

## Coupling and Seam Analysis

| Concern | Current coupling symptom | Proposed seam | Risk | Validation |
|---|---|---|---|---|
| Route lifecycle + listener/forwarder side effects | `add_forwarding_rule` mutates route set, allocates forwarder, registers listeners, and performs rollback in one method | Extract `RouteTable` + transactional coordinator | Medium: rollback correctness can regress | Existing `add_forwarding_rule_rolls_back_on_listener_insert_failure` and `unregistration_removes_publish_filters` tests |
| Routing resolution split across crates | `effective_publish_source_filters` relies on `subscription-cache` wildcard merge behavior | Introduce routing adapter that owns publish source resolution inputs/outputs | Medium: publish authorization drift | Existing publish filter tests and wildcard forwarding tests in `ustreamer` |
| Runtime/threading concerns mixed into transport logic | `TransportForwarder::new` spawns std thread + Tokio runtime inside data-path setup | Isolate worker runtime bootstrap behind runtime module | Medium: shutdown/worker leak behavior | Existing integration tests plus targeted component tests during extraction |
| Observability init mixed into library API | `Endpoint::new` performs `env_logger::try_init` from library code | Move subscriber/logger init to binary/plugin boundaries | High: double-init and consumer side effects | Consumer smoke checks for plugin/bin startup after migration |
| Transport identity compatibility hidden in local type | `ComparableTransport` hashes pointer identity (`Arc::as_ptr`) in rule keys | Preserve semantics behind explicit alias/docs before any redesign | High: route de-dupe/removal compatibility | Existing dedupe and multi-map tests (`multi_map_allows_both_sources`, delete symmetry tests) |

## Behavior Contracts -> Concept Owners

| Behavior contract | Domain owner concept | Planned module owner | Primary tests |
|---|---|---|---|
| left-side authority publish eligibility | Publish Route Resolution Policy | `routing/publish_resolution.rs` | `publish_filter_respects_topic_authority`, `publish_filter_allows_left_wildcard`, `publish_filter_blocks_unmapped_authority` |
| right-side wildcard subscriber-authority expansion | Subscription Directory Lookup Policy | `routing/subscription_directory.rs` + `routing/publish_resolution.rs` | `right_side_wildcard_forwards_to_registered_authorities`, `right_side_wildcard_does_not_forward_without_rule`, `subscription-cache::wildcard_lookup_merges_exact_and_wildcard_rows` |
| dedupe symmetry insert/remove | Route Table + Ingress Listener Registry | `control_plane/route_table.rs` + `data_plane/ingress_registry.rs` | `publish_filter_dedupes_overlapping_rows`, `unregistration_removes_publish_filters` |
| add-failure rollback consistency | Transactional Route Lifecycle Coordinator | `control_plane/route_lifecycle.rs` | `add_forwarding_rule_rolls_back_on_listener_insert_failure` |

## Unresolved Mapping Decisions

- [x] DG-A inputs captured
- [x] DG-B inputs captured

### Notes

```text
# DG-A input (module boundaries): extracted candidate seams align to API facade, control plane,
# routing, data plane, and runtime boundaries without altering public naming.
#
# DG-B input (transport identity): ComparableTransport uses Arc pointer identity for hashing/equality;
# this is compatibility-sensitive and should be preserved through wrapper aliasing/documentation before
# any semantic rewrite.
```
