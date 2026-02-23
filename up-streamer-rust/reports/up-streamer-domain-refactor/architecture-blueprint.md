# Architecture Blueprint

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Define target internal architecture for `up-streamer` before code movement, with explicit decision-gate outcomes and compatibility constraints.

## Naming Boundary Rule

- [x] Outward API and user-facing docs remain streamer-centric (`Endpoint`, `UStreamer`, forwarding rule language).
- [x] Internal module/type names use middleware/comms concepts when they improve locality and maintenance.

## Target Module Layout

```text
up-streamer/src/
  lib.rs                         # stable outward re-exports
  api/
    mod.rs
    endpoint.rs                  # outward Endpoint façade and constructor contract
    streamer.rs                  # outward UStreamer façade and public methods
  control_plane/
    mod.rs
    route_table.rs               # forwarding rule identity, insert/remove dedupe
    route_lifecycle.rs           # transactional add/delete orchestration + rollback
  routing/
    mod.rs
    publish_resolution.rs        # source filter derivation policy
    subscription_directory.rs    # wildcard/exact subscriber authority merge adapter
  data_plane/
    mod.rs
    ingress_registry.rs          # listener registration/unregistration lifecycle
    ingress_listener.rs          # forwarding listener callback adaptation
    egress_pool.rs               # per-out-transport forwarder pooling + refcounts
    egress_worker.rs             # dispatch loop and send behavior
  runtime/
    mod.rs
    subscription_runtime.rs      # subscription bootstrap runtime ownership
    worker_runtime.rs            # worker runtime/thread spawning strategy
  test_support/                  # optional; test-only builders/mocks/helpers
```

- [x] Structure finalized
- [x] Ownership per module documented

## Layer Ownership and Responsibilities

| Layer | Primary ownership | Exposed to other layers |
|---|---|---|
| `api` | outward type contracts, constructor validation, stable method signatures | narrow façade calls into control/data/routing/runtime collaborators |
| `control_plane` | forwarding-rule lifecycle, dedupe, rollback sequencing | route transaction APIs and errors |
| `routing` | publish resolution and subscription lookup policy | pure/domain routing functions and adapter traits |
| `data_plane` | listener/forwarder lifecycle and ingress->egress flow | registration APIs and queue/send coordination |
| `runtime` | runtime/thread creation and async execution boundaries | runtime adapters/factories only |

## Dependency Direction Rules

- [x] Allowed direction documented (`api -> control_plane/routing/data_plane/runtime`).
- [x] Reverse/deep cross-layer access disallowed and guarded.

### Rule table

| From | Can depend on | Cannot depend on |
|---|---|---|
| `api` | `control_plane`, `routing`, `data_plane`, `runtime` | none at higher layer (top façade) |
| `control_plane` | `routing`, `data_plane`, `runtime` (through traits/adapters) | `api` |
| `routing` | `subscription-cache` adapter boundary, shared domain/value types | `api`, `control_plane`, `data_plane`, `runtime` |
| `data_plane` | `routing` read-only policy helpers, `runtime` worker adapters | `api`, direct `control_plane` mutation internals |
| `runtime` | tokio/std only, shared domain/value types | `api`, `control_plane`, `data_plane`, `routing` policy logic |

### Guard enforcement

- `lib.rs` is the only outward re-export boundary for public API symbols.
- Cross-layer calls use narrow traits or function arguments, not module reach-through.
- No module may mutate another layer's private state container directly.
- `runtime` remains policy-free (execution plumbing only).

## Single Logical Change Point Map

| Behavior family | Single logical owner module/file | Why this is the change point |
|---|---|---|
| route add/remove lifecycle | `up-streamer/src/control_plane/route_lifecycle.rs` | Owns add/remove transaction sequencing, rollback, and error mapping in one coordinator. |
| publish filter resolution | `up-streamer/src/routing/publish_resolution.rs` | Centralizes authority/topic tuple policy used by listener registration/removal. |
| wildcard subscriber merge | `up-streamer/src/routing/subscription_directory.rs` | Encapsulates exact+wildcard merge semantics and `subscription-cache` adaptation. |
| listener registry lifecycle | `up-streamer/src/data_plane/ingress_registry.rs` | Localizes register/unregister symmetry and backpedal handling. |
| transport forwarder pooling | `up-streamer/src/data_plane/egress_pool.rs` | Maintains one-worker-per-out-transport pooling and active-refcount ownership. |

## Module Size/Cohesion Guardrails

- [x] Target concept modules are usually <= 300 LOC (excluding tests/docs).
- [x] Any module over guideline has justification and follow-up split note.
- [x] No new mixed-responsibility mega-files introduced.

| Module/file | LOC | Justification if >300 | Follow-up split issue |
|---|---:|---|---|
| `control_plane/route_lifecycle.rs` | target 220-320 | May exceed due to transactional rollback paths and rich error mapping | Split rollback helpers into `route_rollback.rs` if sustained >300 after Wave 4 |
| `data_plane/ingress_registry.rs` | target 220-320 | May exceed due to registration/unregistration symmetry and publish listener sets | Split publish-specific helpers into `ingress_publish.rs` if sustained >300 after Wave 5 |
| all other listed modules | target <=300 | N/A | N/A |

## Decision Gates (Resolved)

### DG-A: Module boundary and naming approval

- [x] Decision: approve five internal layers (`api`, `control_plane`, `routing`, `data_plane`, `runtime`) plus optional `test_support`.
- [x] Decision: preserve outward streamer naming; use domain naming internally.
- [x] Rationale: aligns to Phase 1 seam map and keeps user-facing churn near zero.

### DG-B: Transport identity keying treatment

- [x] Decision: preserve current pointer-identity semantics (`Arc::as_ptr` / `Arc::ptr_eq`) for rule keys and forwarder/listener maps.
- [x] Decision: expose this as a documented internal alias/wrapper concept in control/data-plane modules; no semantic rewrite in refactor waves.
- [x] Rationale: existing dedupe/remove behavior depends on current key semantics and is compatibility-sensitive.

### DG-C: Runtime model strategy

- [x] Decision: isolate runtime ownership in `runtime/subscription_runtime.rs` and `runtime/worker_runtime.rs`.
- [x] Decision: preserve behavioral model (subscription bootstrap runtime + worker dispatch runtime) during extraction; optimize only after parity is proven.
- [x] Rationale: avoids lifecycle regressions while untangling execution concerns from domain policy code.

### DG-D: Test split strategy

- [x] Decision: maintain three layers of tests during refactor:
  - API contract tests continue validating `UStreamer::{new,add_forwarding_rule,delete_forwarding_rule}` and `Endpoint::new` behavior.
  - Component tests target control/routing/data-plane seams.
  - Integration tests continue end-to-end transport/listener workflows.
- [x] Decision: baseline behavior-contract tests from `behavior-conservation-matrix.md` remain mandatory parity checks for each extraction wave.

### DG-E: Tracing sequencing and init strategy

- [x] Decision: migrate libraries to `tracing` instrumentation without unconditional global subscriber initialization.
- [x] Decision: binaries/plugins own one-time `tracing-subscriber` initialization boundaries.
- [x] Decision: remove `Endpoint::new` global-init side effect in observability wave behind parity validation.

### DG-F: Async runtime alignment (`async-std` -> `tokio`)

- [x] Decision: no direct `async-std` runtime code remains; keep tokio as runtime standard.
- [x] Decision: remove stale manifest-level `async-std` deps in runtime-alignment wave after crate-scoped checks.
- [x] Rationale: Phase 1 audit found only manifest residue in `subscription-cache` and `utils/usubscription-static-file`.

### DG-G: API drift acceptance policy

- [x] Decision: preserve crate root API shape for common users:
  - `up_streamer::Endpoint`
  - `up_streamer::UStreamer`
  - `Endpoint::new`, `UStreamer::new`, `UStreamer::add_forwarding_rule`, `UStreamer::delete_forwarding_rule`
- [x] Decision: internal module paths may change freely as long as root re-exports and common signatures/behavior remain stable.
- [x] Decision: any unavoidable public drift requires explicit migration guidance in `api-surface-drift-report.md` with compatibility classification.

## Decision Gate Inputs Checklist

- [x] DG-A boundary and naming decisions recorded
- [x] DG-B transport identity keying decisions recorded
- [x] DG-C runtime model decisions recorded
- [x] DG-D test split decisions recorded
- [x] DG-E tracing sequence/init decisions recorded
- [x] DG-F async runtime decisions recorded
- [x] DG-G API drift acceptance decisions recorded
