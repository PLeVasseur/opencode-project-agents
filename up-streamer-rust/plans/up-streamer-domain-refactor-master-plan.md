# Up-Streamer Domain Refactor Master Plan

Date: 2026-02-09  
Starting branch: `bugfix/issue-74-left-topic-authority`  
Execution branch to create: `refactor/up-streamer-domain-architecture` (or equivalent)
Autopilot script: `$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py`

## Objective

Refactor `up-streamer` from a monolithic, tightly-coupled implementation into domain-oriented modules that are easier to maintain, reason about, and safely evolve. The refactor must preserve behavior, keep the outward-facing API (`Endpoint`, `UStreamer`) simple for most users, and make behavior changes locatable in one logical place.

This single plan covers both:

1. additional research/discovery, and
2. execution of the refactor.

It is written to be executable in a fresh session without relying on hidden context.

---

## Non-Negotiable Constraints

- [ ] Keep outward API expectations stable for common users (`up_streamer::{Endpoint, UStreamer}` remains primary).
- [ ] Keep **streamer naming** as the outward-facing terminology (public API surface and user-first docs).
- [ ] Use middleware/communications terminology internally where it improves maintainability and discoverability.
- [ ] Preserve issue-74 baseline behavior and issue-74 follow-up behavior.
- [ ] Preserve the **entire existing test behavior** baseline, not only issue-74-related behavior.
- [ ] Refactor may include unit tests, integration tests, and test harness/mocks (`UPClientFoo` and related utilities).
- [ ] Refactor consumers of `up-streamer` only as needed for compatibility and clarity (avoid churn when not required).
- [ ] Use middleware/communications domain concepts in naming and module boundaries.
- [ ] Transition logging/telemetry from `log`-style usage to `tracing` + `tracing-subscriber` **workspace-wide** in this refactor.
- [ ] Audit for `async-std` usage; migrate any such usage to `tokio`.
- [ ] Add strong rustdoc + doctests for each major abstraction layer.
- [ ] Every extracted internal module file contains meaningful rustdoc; each layer has at least one doctest.
- [ ] No placeholder scaffolding remains in refactor modules at completion.
- [ ] `up-streamer/src/ustreamer.rs` trends toward ~500 code lines through meaningful extractions (non-comment, non-blank lines), with hard fail threshold enforced at >900 code lines.
- [ ] All code-line quality metrics count only actual code lines (comments/doc comments/blank lines excluded).
- [ ] `up-streamer/src/ustreamer.rs` must not retain duplicate legacy implementations that were extracted to domain modules.
- [ ] All pre-existing tests that currently pass must still pass at the end.
- [ ] Keep artifacts in `$OPENCODE_CONFIG_DIR` (plans/reports), not repo-local.

### Locked Decisions (Pre-Resolved)

- [x] Outward naming remains streamer-centric; internal module/type naming may use conventional middleware/comms concepts.
- [x] Tracing migration scope is workspace-wide for this refactor (not only touched/refactored surfaces).

### Type/Compatibility Constraint

- [ ] Treat transport identity keying constructs as compatibility-sensitive.
- [ ] Do not force naming changes based on assumptions about ownership/origin of transport identity types (for example, `ComparableTransport` handling) until verified and approved in design gate.
- [ ] Where `ComparableTransport` or equivalent transport-identity keying is compatibility-sensitive, prefer introducing wrapper aliases/docs over semantic rewrites unless explicitly justified.

---

## Execution Prerequisites (Fresh Session)

- [ ] `OPENCODE_CONFIG_DIR` is set and writable.
- [ ] Rust toolchain meets workspace MSRV (`1.88`).
- [ ] Cargo commands run from workspace root.
- [ ] If running transport-feature matrices, environment prerequisites from `build/envsetup.sh` and optional unbundled vsomeip paths are understood.
- [ ] Load and apply available skills as needed (for example, artifact hygiene and CI parity preflight workflows).
- [ ] Autopilot non-interactive runs allow external directory access to `$OPENCODE_CONFIG_DIR/**` (script sets `OPENCODE_PERMISSION` for this).
- [ ] Fresh session reads this plan and creates all listed report artifacts before implementation waves.

---

## Known Baseline (Seeded)

### Core file sizes (seeded baseline)

- `up-streamer/src/ustreamer.rs`: ~2060 LOC
- `up-streamer/src/endpoint.rs`: ~113 LOC
- `subscription-cache/src/lib.rs`: ~289 LOC
- `up-streamer/tests/*.rs`: ~1498 LOC total
- `utils/integration-test-utils/src/*.rs`: ~1108 LOC total

### Workspace consumers of `up-streamer` (seeded)

- `configurable-streamer/src/main.rs`
- `example-streamer-implementations/src/bin/zenoh_someip.rs`
- `up-linux-streamer-plugin/src/lib.rs`
- `utils/integration-test-utils` (test harness crate)

---

## Initial Domain Mapping (Seeded Content)

This is the initial mapping to refine during research. Keep terms recognizable to middleware/comms engineers.

| Current construct | Current location | Domain concept | Target layer | Candidate destination |
|---|---|---|---|---|
| `UStreamer` | `up-streamer/src/ustreamer.rs` | Streamer Orchestrator | API Facade + Control Plane | `up-streamer/src/api/streamer.rs` |
| `Endpoint` | `up-streamer/src/endpoint.rs` | Transport Endpoint Descriptor | API Facade | `up-streamer/src/api/endpoint.rs` |
| forwarding rule set | `up-streamer/src/ustreamer.rs` | Route Table | Control Plane | `up-streamer/src/control_plane/route_table.rs` |
| listener lifecycle logic | `up-streamer/src/ustreamer.rs` | Ingress Listener Registry | Data Plane (ingress) | `up-streamer/src/data_plane/ingress_registry.rs` |
| transport forwarder lifecycle | `up-streamer/src/ustreamer.rs` | Egress Forwarder Pool | Data Plane (egress) | `up-streamer/src/data_plane/egress_pool.rs` |
| `TransportForwarder` loop | `up-streamer/src/ustreamer.rs` | Egress Dispatch Worker | Data Plane (egress) | `up-streamer/src/data_plane/egress_worker.rs` |
| publish filter derivation | `up-streamer/src/ustreamer.rs` | Publish Route Resolution Policy | Routing/Resolution | `up-streamer/src/routing/publish_resolution.rs` |
| wildcard subscriber merge | `subscription-cache/src/lib.rs` + `up-streamer/src/ustreamer.rs` | Subscription Directory Lookup Policy | Routing/Resolution | `up-streamer/src/routing/subscription_directory.rs` (adapter/view) |
| `ForwardingListener` | `up-streamer/src/ustreamer.rs` | Ingress Message Adapter | Data Plane (ingress) | `up-streamer/src/data_plane/ingress_listener.rs` |
| callback runtime bootstrap | `up-streamer/src/ustreamer.rs` | Runtime Integration Adapter | Runtime | `up-streamer/src/runtime/subscription_runtime.rs` |

Naming decision:

- [x] Keep streamer-centric naming at outward API/documentation boundaries.
- [x] Use middleware/comms concept naming internally and maintain explicit mapping for reviewers/maintainers.

---

## Artifact Plan

All artifacts below live under:

`$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-refactor/`

- [x] `baseline-inventory.md`
- [x] `behavior-conservation-matrix.md`
- [x] `domain-concept-mapping.md`
- [x] `architecture-blueprint.md`
- [x] `api-surface-drift-report.md`
- [x] `refactor-wave-plan.md` (if split from this master plan during execution)
- [x] `test-matrix.md`
- [x] `behavior-owner-traceability.md`
- [x] `async-runtime-audit.md`
- [x] `tracing-migration-plan.md`
- [x] `workspace-tracing-migration-status.md`
- [x] `rustdoc-doctest-plan.md`
- [x] `consumer-impact-analysis.md`
- [x] `wave-validation-log.md`
- [x] `autopilot-run-log.md`
- [x] `autopilot-state.json`
- [x] `final-refactor-handoff.md`

---

## Autopilot Mode (Segmented Execution)

Use autopilot for long-running execution with bounded context.

- [ ] Run one phase per isolated `opencode run` invocation (fresh session per phase).
- [ ] Attach only the master plan and phase-relevant report files for each invocation.
- [ ] Require machine-readable completion marker from each phase invocation:
  - [ ] `AUTOPILOT_STATUS: {"phase":"Phase X","gate":"Gate X","gate_passed":true|false,"needs_human":true|false,"blockers":[],"summary":"..."}`
- [ ] Persist orchestration state in `autopilot-state.json`.
- [ ] Persist per-phase execution transcript summary in `autopilot-run-log.md`.
- [ ] Stop autopilot on first gate failure or `needs_human=true`.
- [ ] Gate success requires both:
  - [ ] valid `AUTOPILOT_STATUS` marker from the agent, and
  - [ ] objective local validator pass in autopilot script for that phase.
- [ ] Auto-retry policy for context/response failures:
  - [ ] retry up to configured attempt limit when status marker is missing or malformed
  - [ ] on retry, reduce attached context to phase-minimal files
  - [ ] stop and escalate to human if retries are exhausted
- [ ] Auto-retry policy for objective validator failures:
  - [ ] retry up to configured attempt limit with explicit blocker list injected into next prompt
  - [ ] stop and escalate to human if validators still fail after retries

### Hardening recovery note

- [ ] If prior autopilot runs marked phases complete without objective validator checks, treat those checks as provisional.
- [ ] Re-validate Phase 3+ with objective validators before considering the plan execution complete.

### Autopilot operator commands

- [ ] kickoff:
  - [ ] `python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- [ ] kickoff from clean autopilot state:
  - [ ] `python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust --reset-state --start-phase 3`
- [ ] monitor:
  - [ ] `tail -f "$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-refactor/autopilot-run-log.md"`
- [ ] inspect state:
  - [ ] `python3 -m json.tool "$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-refactor/autopilot-state.json"`
- [ ] run local objective validators only:
  - [ ] `python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust --start-phase 3 --end-phase 7 --validate-only`
- [ ] resume from specific phase:
  - [ ] `python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust --start-phase 3`

---

## Phase 0 - Bootstrap

- [x] `git fetch --all --prune`
- [x] `git switch bugfix/issue-74-left-topic-authority`
- [x] `git pull --ff-only`
- [x] `git switch -c refactor/up-streamer-domain-architecture`
- [x] Create report directory: `mkdir -p "$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-refactor"`
- [x] Capture starting point in `baseline-inventory.md`:
  - [x] `git status --short --branch`
  - [x] `git log --oneline -15`
  - [x] record baseline anchor commit SHA and treat it as comparison source for all conservation checks
  - [x] file-size inventory for refactor targets
- [x] Capture full current behavior baseline in `behavior-conservation-matrix.md`:
  - [x] list all current unit/integration/doc test targets for `up-streamer`, `subscription-cache`, and `integration-test-utils`
  - [x] run exact baseline commands and record pass/fail + environment notes:
    - [x] `cargo test -p up-streamer -- --nocapture`
    - [x] `cargo test -p up-streamer --doc`
    - [x] `cargo test -p subscription-cache -- --nocapture`
    - [x] `cargo test -p integration-test-utils -- --nocapture`
    - [x] `cargo test --workspace`
  - [x] for each command record: command string, exit code, elapsed time, environment prereqs, and failure summary (if any)
  - [x] record known environment-dependent tests separately (if any)
- [x] Initialize autopilot tracking artifacts if using autopilot mode:
  - [x] create/update `autopilot-state.json`
  - [x] create/update `autopilot-run-log.md`

### Gate 0

- [x] Execution branch created from required base branch.
- [x] Baseline inventory report created.
- [x] Full behavior baseline matrix created from currently passing test surfaces.
- [x] Baseline anchor SHA and command reproducibility fields are complete.
- [x] Autopilot state/log artifacts initialized (if autopilot mode is used).

---

## Phase 1 - Research and Domain Model Hardening

### 1.1 Responsibilities and coupling map

- [x] Partition current logic into responsibilities:
  - [x] API facade responsibilities
  - [x] control-plane route lifecycle
  - [x] routing/subscription resolution
  - [x] data-plane ingress/egress flow
  - [x] runtime/threading concerns
  - [x] observability/logging behavior
- [x] Record tight coupling and candidate seam points in `domain-concept-mapping.md`.

### 1.2 Preserve-critical behavior catalog

- [x] List behavior contracts that cannot regress (full current baseline + issue-74 baseline + follow-up):
  - [x] all currently passing tests remain represented in behavior-conservation matrix
  - [x] left-side authority publish eligibility
  - [x] right-side wildcard subscriber-authority expansion (rule bound)
  - [x] effective publish-key dedupe symmetry (insert/remove)
  - [x] add-failure rollback consistency
  - [x] tuple strictness and multi-map semantics

### 1.3 Runtime/logging technology audit

- [x] Audit async runtime usage and document in `async-runtime-audit.md`:
  - [x] search for `async-std` usage across workspace
  - [x] classify each finding: direct dependency, indirect dependency, or none
  - [x] plan migration to `tokio` where direct usage exists
- [x] Audit logging usage and document in `tracing-migration-plan.md`:
  - [x] inventory `log::*` macro and `env_logger` initialization sites across the entire workspace
  - [x] define workspace-wide `tracing` migration approach (events, spans, subscriber initialization boundaries)
  - [x] define cross-crate subscriber initialization policy to avoid double-init and preserve expected CLI/plugin behavior
  - [x] record per-crate status in `workspace-tracing-migration-status.md`
- [x] Track audit status per workspace member (no omissions):
  - [x] `example-streamer-uses`
  - [x] `utils/hello-world-protos`
  - [x] `utils/integration-test-utils`
  - [x] `example-streamer-implementations`
  - [x] `configurable-streamer`
  - [x] `up-linux-streamer-plugin`
  - [x] `up-streamer`
  - [x] `subscription-cache`
  - [x] `utils/usubscription-static-file`
- [x] Verify member checklist against root `Cargo.toml` `[workspace].members` to prevent drift/omissions.
- [x] Dependency migration ledger (workspace-wide):
  - [x] for each crate, classify `log`, `env_logger`, and `async-std` as migrated / retained-with-rationale / not-applicable
  - [x] capture ledger in `workspace-tracing-migration-status.md`

### 1.4 External-consumer usage profiling

- [x] For each consumer crate, record exactly how `Endpoint`/`UStreamer` are used.
- [x] Mark each consumer with expected impact level: none / minimal / required.

### Gate 1

- [x] `domain-concept-mapping.md` completed with refined glossary and boundaries.
- [x] critical behavior catalog approved and linked to tests.
- [x] full behavior-conservation matrix approved and complete.
- [x] async runtime audit complete.
- [x] tracing migration plan complete.
- [x] workspace tracing migration status baseline complete.
- [x] dependency migration ledger complete for all workspace members.
- [x] consumer impact pre-assessment completed.

---

## Phase 2 - Architecture Blueprint and Refactor Design

### 2.1 Target internal module layout (design level)

- [x] Finalize target structure (representative):
  - [x] `up-streamer/src/api/`
  - [x] `up-streamer/src/control_plane/`
  - [x] `up-streamer/src/routing/`
  - [x] `up-streamer/src/data_plane/`
  - [x] `up-streamer/src/runtime/`
  - [x] `up-streamer/src/test_support/` (if needed)
- [x] Define dependency direction (for example: api -> control/routing/data_plane/runtime; no reverse leaks).
- [x] Define file/module chunking rules aligned with Rust best practices:
  - [x] each module owns one cohesive concept
  - [x] avoid oversized files where unrelated responsibilities are mixed
  - [x] prefer `module.rs` + submodules or `module/thing.rs` when concept fan-out is natural
  - [x] ensure behavior changes can be made in one logical location

### 2.2 Public API preservation strategy

- [x] Keep re-exports in `up-streamer/src/lib.rs` stable for common usage.
- [x] Track any unavoidable outward API changes and migration notes.
- [ ] Capture public API baseline and post-refactor diff in `api-surface-drift-report.md`:
  - [x] snapshot baseline public items for `up-streamer` (re-exports, public types, public methods)
  - [ ] snapshot post-refactor public items for `up-streamer` using the same method
  - [ ] document each diff as intentional/non-breaking or provide migration notes

### 2.3 Decision gates (must resolve before code movement)

- [x] DG-A: module boundary finalization and naming approval.
- [x] DG-B: transport identity keying treatment (including compatibility-sensitive types).
- [x] DG-C: runtime model strategy for worker dispatch and subscription bootstrap.
- [x] DG-D: test split strategy (unit/component/integration) finalized.
- [x] DG-E: workspace-wide tracing migration sequencing and initialization strategy finalized.
  - [x] library crates must not perform unconditional global subscriber initialization
  - [x] binaries/plugins own one-time subscriber initialization boundaries
- [x] DG-F: async runtime alignment decision (`async-std` -> `tokio`) finalized.
- [x] DG-G: API drift acceptance finalized (public surface stability + allowed exceptions).

### Gate 2

- [x] `architecture-blueprint.md` completed.
- [x] Decision gates DG-A..DG-G resolved and logged.
- [x] blueprint demonstrates localized change points for each major behavior family.
- [x] blueprint includes outward-streamer/internal-domain naming boundary rules.

---

## Phase 3 - Execution Waves (Implementation)

Execute in order. Do not skip gates.

- [x] Prior `[x]` marks from earlier autopilot runs are provisional for Phase 3-6 until objective validators pass.

### Wave 1: Scaffolding and no-behavior-change extraction

- [x] Introduce module skeleton and move type aliases/helpers without semantic changes.
- [x] Keep all tests compiling/running after each extraction commit.

### Wave 2: Observability and runtime alignment

- [x] Migrate workspace crates from `log` macros to `tracing` events/spans (workspace-wide scope).
- [x] Introduce/align subscriber initialization strategy (`tracing-subscriber`) without breaking consumer expectations.
- [x] Update `workspace-tracing-migration-status.md` with per-crate completion state and exceptions (if any).
- [x] Replace direct `async-std` usage with `tokio` where found.
- [x] Verify no behavior drift from observability/runtime alignment changes.

### Wave 3: Routing and subscription resolution extraction

- [x] Extract publish source filter derivation and wildcard subscription merge logic.
- [x] Keep issue-74/follow-up behavior contracts intact.

### Wave 4: Control plane extraction

- [x] Extract route registration/removal lifecycle.
- [x] Preserve transactional rollback behavior.

### Wave 5: Data plane extraction

- [x] Extract ingress listener registry and egress forwarder pool/worker concerns.
- [x] Preserve register/unregister symmetry and dedupe guarantees.

### Wave 6: Runtime extraction

- [x] Isolate runtime bootstrap/runtime-specific logic.
- [x] Keep behavior unchanged unless explicitly approved.

### Phase 3 hardening checks (authoritative)

- [x] `up-streamer/src/api/endpoint.rs` and `up-streamer/src/api/streamer.rs` are implemented (no placeholder stubs).
- [x] No `Wave 1 scaffolding placeholder` markers remain under `up-streamer/src/**`.
- [x] `up-streamer/src/ustreamer.rs` trends toward ~500 code lines (non-comment, non-blank); hard fail threshold is >900 code lines.
- [x] Legacy duplicate internals are removed from `ustreamer.rs` after extraction (forwarding listeners/forwarders and related constants/types).

### Gate 3 (after each wave)

- [x] `cargo build`
- [x] targeted tests for touched wave pass
- [x] no known behavior-contract regressions
- [x] behavior-conservation matrix remains green for all baseline tests exercised in this wave
- [x] `wave-validation-log.md` updated
- [x] autopilot phase status marker captured and logged in `autopilot-run-log.md` (if autopilot mode is used)
- [x] objective local validator passes for Phase 3 hardening checks
- [x] Wave failure playbook executed when needed:
  - [x] stop progression to next wave (not required; no failures)
  - [x] capture failing command, error, and first actionable root cause (not required; no failures)
  - [x] add characterization test if behavior ambiguity exists (not required; no failures)
  - [x] either fix within wave scope or rollback the wave commit set (not required; no failures)

---

## Phase 4 - Test Refactor and Expansion (All Levels)

### 4.1 Unit-level domain tests

- [x] Add/relocate deterministic tests for routing policies.
- [x] Add/relocate deterministic tests for control-plane invariants.
- [x] Add/relocate deterministic tests for data-plane components.

### 4.2 Component-level tests (internal integration)

- [x] Verify interactions between control plane + routing resolution.
- [x] Verify interactions between ingress registry + egress pool.

### 4.3 API contract tests

- [x] Keep clear tests around `UStreamer::add_forwarding_rule` and `delete_forwarding_rule` contract.
- [x] Preserve issue-74 + follow-up behavior tests.

### 4.4 Integration tests and mocks

- [x] Refactor/split integration tests in `up-streamer/tests/` as needed for clarity.
- [x] Refactor `UPClientFoo` and related mocks/utilities as needed.
- [x] Ensure existing integration scenarios retain coverage intent.

### 4.5 Test matrix report

- [x] Maintain `test-matrix.md` mapping each domain concept/layer to concrete tests.
- [x] Explicitly map pre-existing tests to their new locations if moved.
- [x] Maintain `behavior-owner-traceability.md`:
  - [x] each preserved behavior maps to owning module/file
  - [x] each behavior maps to primary validation tests
  - [x] each behavior lists the intended single logical change point
- [x] Maintain `behavior-conservation-matrix.md` mapping baseline test expectations to post-refactor outcomes.
- [x] Ensure every currently passing test from baseline is represented with post-refactor pass evidence.

### 4.6 Test readability hardening checks (authoritative)

- [x] `up-streamer/src/ustreamer.rs` no longer carries a large monolithic in-file test suite (tests moved to domain modules/integration where appropriate).
- [x] Layer-owned module tests exist for extracted control/routing/data-plane files.
- [x] API contract integration tests remain explicit and reviewer-friendly.
- [x] Very long test bodies are reduced via helper extraction so reviewers can validate intent quickly.
- [x] Test mapping reports contain no placeholder relocation rows.

### Gate 4

- [x] Robust test coverage present at each abstraction level.
- [x] existing pass-set preserved in full (unit + integration + doctest surfaces captured at baseline).
- [x] objective local validator passes for Phase 4 test readability/refactor checks.

---

## Phase 5 - Rustdoc and Doctest Hardening

### 5.1 Crate and module docs

- [x] Update crate-level docs to explain layered architecture and outward API-first usage.
- [x] Add module docs for control plane, routing, data plane, runtime.
- [x] Document observability model (tracing events/spans and subscriber expectations).

### 5.2 Concept-focused doctests

- [x] Add compile/run doctests for outward API usage.
- [x] Add targeted doctests for key domain concepts (route lifecycle, routing resolution, etc.).

### 5.4 Documentation hardening checks (authoritative)

- [x] Every extracted module file under `up-streamer/src/{api,control_plane,routing,data_plane,runtime}/*.rs` has rustdoc comments.
- [x] Each layer (`api`, `control_plane`, `routing`, `data_plane`, `runtime`) contains at least one doctest fence in that layer's files.

### 5.3 Documentation quality checks

- [x] `cargo doc -p up-streamer --no-deps`
- [x] `cargo test -p up-streamer --doc`

### Gate 5

- [x] Rustdoc and doctests explain each domain concept and abstraction layer clearly.
- [x] objective local validator passes for Phase 5 documentation hardening checks.

---

## Phase 6 - Consumer Validation and As-Needed Adaptation

- [x] Validate compile for each workspace consumer using `up-streamer`.
- [x] Apply minimal required consumer adjustments (if any) with rationale in `consumer-impact-analysis.md`.
- [x] Prefer no consumer changes unless required.
- [x] For workspace-wide tracing migration, keep consumer-facing initialization changes minimal and document exact reasons where required.
- [x] Revalidate Phase 6 objective validator with zero blockers before confirming Gate 6.

Validation targets:

- [x] `cargo check -p configurable-streamer`
- [x] `cargo check -p example-streamer-implementations` (validated via `cargo check --manifest-path example-streamer-implementations/Cargo.toml` because package id is `up-linux-streamer`)
- [x] `cargo check -p up-linux-streamer-plugin`
- [x] `cargo check -p integration-test-utils`

### Gate 6

- [x] All consumers compile; any modifications are minimal and justified.

---

## Phase 7 - Full Validation and CI Parity

Run from repo root.

### 7.1 Core validation

- [x] `cargo build`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo test -p up-streamer -- --nocapture`
- [x] `cargo test -p subscription-cache -- --nocapture`
- [x] `cargo test -p integration-test-utils -- --nocapture`
- [x] workspace tracing hygiene check recorded (remaining `log`/`env_logger` usages are either migrated or explicitly justified)

### 7.2 Workspace validation

- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### 7.3 CI parity matrix (transport-affecting)

- [x] `source build/envsetup.sh highest`
- [x] base matrix
- [x] bundled matrix
- [x] unbundled matrix if prerequisites available
- [x] if unbundled prerequisites unavailable, log explicit skip reason and continue

### Gate 7

- [x] Validation passes or documented environment-constrained skips only.
- [x] `workspace-tracing-migration-status.md` finalized with per-crate completion and explicit deferred items (if any).
- [x] objective local validator passes for Phase 7 final gate checks.

---

## Behavior Conservation Checklist (Full Existing Surface)

- [x] Baseline test manifest (captured in `behavior-conservation-matrix.md`) is complete.
- [x] Baseline and post-refactor command parity captured for:
  - [x] `cargo test -p up-streamer -- --nocapture`
  - [x] `cargo test -p up-streamer --doc`
  - [x] `cargo test -p subscription-cache -- --nocapture`
  - [x] `cargo test -p integration-test-utils -- --nocapture`
  - [x] `cargo test --workspace`
- [x] `up-streamer` unit tests pass post-refactor.
- [x] `up-streamer` integration tests pass post-refactor.
- [x] `up-streamer` doctests pass post-refactor.
- [x] `subscription-cache` tests pass post-refactor.
- [x] `integration-test-utils` tests pass post-refactor.
- [x] Workspace-level baseline test behavior (as captured at Phase 0) is preserved.
- [x] No baseline-passing test regressed without explicit approved replacement and mapping.

---

## Commit and Review Slicing

- [ ] Keep commits aligned to waves/layers; avoid mixing unrelated concerns.
- [ ] Before each commit:
  - [ ] `git diff --name-only --cached`
  - [ ] `git diff --stat --cached`
- [ ] Suggested commit groups:
  - [ ] scaffolding/module split (no behavior change)
  - [ ] workspace-wide tracing migration + runtime alignment (`async-std` -> `tokio` if present)
  - [ ] routing extraction
  - [ ] control-plane extraction
  - [ ] data-plane extraction
  - [ ] runtime extraction
  - [ ] tests/mocks restructuring
  - [ ] rustdoc/doctests
  - [ ] as-needed consumer adaptations

---

## Risk Controls

- [ ] Maintain a running behavior-contract checklist in `wave-validation-log.md`.
- [ ] If a wave introduces ambiguous regressions, pause and add targeted characterization tests before proceeding.
- [ ] Avoid broad renames without domain rationale and cross-reference updates.
- [ ] Keep rollback-ready commits (small, reviewable, wave-scoped).
- [ ] Maintain a "single logical change point" map for major behaviors in `architecture-blueprint.md` and verify it stays true as modules evolve.
- [ ] Apply module-size/cohesion guardrails:
  - [ ] prefer concept modules that are typically <= 300 LOC (excluding tests/docs)
  - [ ] when exceeding guideline, add explicit justification + follow-up split note in `architecture-blueprint.md`
  - [ ] avoid introducing new mixed-responsibility mega-files

---

## Definition of Done

- [x] `up-streamer` internals are split into domain-oriented modules with clear ownership boundaries.
- [x] Streamer-centric terminology remains consistent at outward API/doc boundaries, with internal domain terminology documented and intentional.
- [x] Outward-facing API remains straightforward for typical users.
- [x] Existing behavior is preserved across the full baseline test surface (including issue-74 baseline and follow-up contracts).
- [x] `api-surface-drift-report.md` confirms stable public API or documents approved, minimal exceptions.
- [x] Tests are robust at unit/component/API/integration levels.
- [x] Rust documentation and doctests explain each domain concept/layer.
- [x] Tracing migration completed workspace-wide with documented subscriber expectations.
- [x] Async runtime audit completed and any `async-std` usage migrated to `tokio` or explicitly justified.
- [x] Consumer crates remain compatible with minimal/no required changes.
- [x] Final handoff report completed: `final-refactor-handoff.md`.

---

## New-Session Execution Protocol

Use this exact sequence in a fresh session:

1. Read this plan completely.  
2. Execute Phase 0 and capture full behavior baseline matrix.  
3. Complete research phases (1-2), including tracing/async audits, before moving code.  
4. Execute waves in order, validating after each wave against behavior matrix.  
5. Refactor tests/mocks and docs before consumer adaptations.  
6. Run full validation/CI parity and behavior-conservation checklist.  
7. Produce final handoff report with commit-by-commit summary and unresolved follow-ups.

Autopilot variant:

1. Start autopilot script using the kickoff command in “Autopilot operator commands” (use `--reset-state --start-phase 3` for hardened reruns).  
2. Monitor `autopilot-run-log.md` and `autopilot-state.json`.  
3. If autopilot stops with `gate_passed=false` or `needs_human=true`, resolve blocker and resume with `--start-phase`.  
4. Continue until all phases and gates are complete.
