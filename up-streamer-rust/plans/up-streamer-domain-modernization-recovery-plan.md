# Up-Streamer Domain Modernization Recovery Plan (Manual)

Date: 2026-02-09
Execution branch: `refactor/up-streamer-domain-architecture`

## Intent

Finish the refactor as a true domain modernization (not just file shuffling), while preserving behavior and keeping the outward API streamer-centric (`Endpoint`, `UStreamer`).

## Locked decisions

- [x] Execution is manual (no autopilot orchestration for this recovery plan).
- [x] `ComparableTransport` is not provided by pinned `up-rust = 0.9.0` as a public reusable type; local transport identity keying must be handled in-crate with explicit rationale.
- [x] Artifact set is minimal: keep only essential reports.

## Checkbox integrity policy (always on)

- A parent checkbox may be `[x]` only when every nested child checkbox under it is `[x]`.
- If work is partially complete, set the parent checkbox to `[ ]` and add explicit child checkboxes showing what is complete vs pending.
- For conditional command steps, split the condition branches into child checkboxes and leave the parent unchecked until the session-specific branch is evidenced.
- When evidence is missing or ambiguous, default to `[ ]` and record what proof is required to check it.

---

## Fresh-session bootstrap (required)

Use this exact startup sequence in a new session before touching code:

Re-run and re-verify each step in the current session; prior checkmarks are historical evidence, not a substitute for fresh-session execution.

- [x] `printenv OPENCODE_CONFIG_DIR` *(re-verified in this restart session; see `restart-session-audit.md` Entry R1)*
- [x] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust status --short --branch` *(re-verified in this restart session; see Entry R2)*
- [x] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust switch refactor/up-streamer-domain-architecture` *(re-verified in this restart session; see Entry R3)*
- [x] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust rev-parse --abbrev-ref --symbolic-full-name @{u}` *(re-verified in this restart session; no upstream; see Entry R4)*
- [ ] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust pull --ff-only` *(run only when upstream tracking exists)*
  - [x] No-upstream branch handled: exact failure captured (`fatal: no upstream configured for branch 'refactor/up-streamer-domain-architecture'`) in this restart session (Entry R5).
  - [ ] Upstream fast-forward pull completed.
- [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization"` *(re-verified in this restart session; see Entry R6)*

If any mandatory command fails, record blocker and stop before proceeding. For conditional steps, follow the documented unchecked branch and do not mark it complete without evidence.

## Restart audit (mandatory before new coding)

- [x] Parent/child checkbox integrity was re-audited in this session (`NO_PARENT_CHILD_VIOLATIONS`; `restart-session-audit.md` Entry R7).
- [x] Checked historical claims are re-validated against available evidence artifacts for Phases 0, 1, 2, 4, 5, and 6.
  - [x] Phases 0, 1, 2, 4, and 5 were re-validated in this restart session (Entry R8).
  - [x] Phase 6 non-ignored layer-doctest claim was re-validated with fresh command-level evidence in this session (`phase6-doctest-hardening.md` Entry D6-4).
- [x] Missing/ambiguous evidence defaults were resolved in this session:
  - [x] Dedicated command-level Phase 3 hardening evidence linkage/artifact (resolved in `phase3-hardening-evidence.md`).
  - [x] Non-ignored layer doctest execution for control-plane/routing/data-plane/runtime.
  - [x] Phase 7 full validation rerun + final transport matrix + final summary artifacts.

## Current restart focus (strict)

- [x] Resume from the earliest incomplete gate with evidence integrity: Gate 6 first, then Gate 7.
  - [x] Phase 6 doctest evidence is reconciled so report and raw logs agree on ignored vs executed status.
  - [x] Gate 6 is only checked after fresh non-ignored doctest proof for control-plane/routing/data-plane/runtime is captured.
  - [x] Gate 7 remains blocked until Gate 6 is green in this session.
- [x] Complete Phase 7 evidence closure after Gate 6.
  - [x] Core/workspace validation commands have command-level evidence entries.
  - [x] `transport-matrix-final.md` exists and matches the final scenario logs.
  - [x] `final-validation-summary.md` exists and reflects all final outcomes/blockers.

---

## Non-negotiable constraints

- [x] First action is a checkpoint commit to preserve current progress.
- [x] Start execution with canonical transport matrix baseline (Zenoh<=>SOME/IP, Zenoh<=>MQTT5).
- [x] Internal modules must be domain-scoped and cohesive (control-plane, routing, data-plane, runtime, API facade).
- [x] Refactor must modernize naming/mechanics, not only move code.
- [x] Test readability must improve for human reviewers (shorter tests, explicit assertions, helper extraction).
- [x] Rustdoc/doctests must explain each layer and key abstractions.
  - [x] Layer/module rustdoc narratives are present.
  - [x] Layer doctests execute for control-plane/routing/data-plane/runtime (non-ignored, command-evidenced in this session).
- [x] E2E example binaries, integration tests, unit tests, and workspace checks must still pass.
- [x] Code-line metrics count only actual code (exclude comments/doc comments/blank lines).

## Canonical smoke test runbook (applies to Phase 1 baseline and Phase 7 rerun)

This is the authoritative setup/teardown/validation procedure for both canonical transport scenarios.
If any step fails, capture blocker evidence and stop gate progression.

### Shared preflight and logging discipline

1. Set report output location and clear stale process context:
   - `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization"`
   - `mkdir -p "$REPORT_DIR"`
   - `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|mqtt_client" || true`
2. Source environment from repo root before each scenario:
   - `source build/envsetup.sh highest`
3. Capture streamer/service logs in background with PID files:
   - `<command> > "$REPORT_DIR/<name>.log" 2>&1 & echo $! > "$REPORT_DIR/<name>.pid"`
4. Run client loops in foreground with timeout:
   - `timeout 45s <client command> > "$REPORT_DIR/<name>.log" 2>&1; echo $? > "$REPORT_DIR/<name>.exit"`
   - Exit code `124` is acceptable only when pass criteria are proven from logs.

### Scenario A runbook: Zenoh <=> SOME/IP request/response

Setup:

1. From repo root, build binaries:
   - `source build/envsetup.sh highest`
   - `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
   - `cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
   - `cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"`
2. Export bundled SOME/IP runtime library path (repo root):
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`

Launch order:

1. Streamer (must run from `example-streamer-implementations/` working directory):
   - `source ../build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `export RUST_LOG="info,up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug"`
   - `cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/scenarioA_final_streamer.log" 2>&1 & echo $! > "$REPORT_DIR/scenarioA_final_streamer.pid"`
   - Critical caveat: running this from repo root can fail with `Static subscription file not found` because config paths are relative.
2. Service (repo root):
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info"`
   - `cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/scenarioA_final_service.log" 2>&1 & echo $! > "$REPORT_DIR/scenarioA_final_service.pid"`
3. Client (repo root):
   - `source build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `export RUST_LOG="info,up_transport_vsomeip=trace"`
   - `timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" > "$REPORT_DIR/scenarioA_final_client.log" 2>&1; echo $? > "$REPORT_DIR/scenarioA_final_client.exit"`

Validation:

1. Client responses present:
   - `rg -n "UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" "$REPORT_DIR/scenarioA_final_client.log"`
2. Service request/response loop present:
   - `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/scenarioA_final_service.log"`
3. Streamer has no routing-miss or startup panic signatures:
   - `rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/scenarioA_final_streamer.log" || true`

Teardown:

1. Stop service/streamer with SIGINT (using saved PIDs) and verify no leftovers:
   - `for pidf in "$REPORT_DIR/scenarioA_final_service.pid" "$REPORT_DIR/scenarioA_final_streamer.pid"; do test -f "$pidf" && kill -INT "$(cat "$pidf")" || true; done`
   - `pgrep -fa "zenoh_someip|zenoh_service|someip_client" || true`

Pass criteria:

- Repeated response markers in client and service logs.
- No repeated routing-miss signatures in streamer log.
- No startup panic in streamer log.

### Scenario B runbook: Zenoh <=> MQTT5 request/response

Setup:

1. Start broker (repo root):
   - `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
   - `docker compose -f utils/mosquitto/docker-compose.yaml ps`
2. Validate local router mode config (repo root):
   - `rg -n "listen:|connect:|endpoints" configurable-streamer/ZENOH_CONFIG.json5`
   - Required: `listen.endpoints` must be used for local router mode.
3. Build binaries (repo root):
   - `source build/envsetup.sh highest`
   - `cargo build -p configurable-streamer`
   - `cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
   - `cargo build -p example-streamer-uses --bin mqtt_client --features mqtt-transport`

Launch order:

1. Streamer (must run from `configurable-streamer/` working directory):
   - `source ../build/envsetup.sh highest`
   - `export RUST_LOG="info,up_streamer=debug,up_transport_mqtt5=debug"`
   - `cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/scenarioB_final_streamer.log" 2>&1 & echo $! > "$REPORT_DIR/scenarioB_final_streamer.pid"`
   - Critical caveat: running from repo root can break relative config paths (`MQTT_CONFIG.json5`, `subscription_data.json`).
2. Service (repo root):
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info"`
   - `cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/scenarioB_final_service.log" 2>&1 & echo $! > "$REPORT_DIR/scenarioB_final_service.pid"`
3. Client (repo root):
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info,up_transport_mqtt5=debug"`
   - `timeout 45s cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/scenarioB_final_client.log" 2>&1; echo $? > "$REPORT_DIR/scenarioB_final_client.exit"`

Validation:

1. Client responses present:
   - `rg -n "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/scenarioB_final_client.log"`
2. Service request/response loop present:
   - `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/scenarioB_final_service.log"`
3. Streamer forwarding activity present:
   - `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/scenarioB_final_streamer.log"`
4. Streamer/client have no transport-failure signatures:
   - `rg -ni "error|failed|disconnect" "$REPORT_DIR/scenarioB_final_streamer.log" "$REPORT_DIR/scenarioB_final_client.log" || true`
5. Benign Zenoh startup warning handling:
   - `Scouting delay elapsed before start conditions are met` may appear in `zenoh_service` logs and is not a failure by itself when request/response flow is proven.

Teardown:

1. Stop service/streamer with SIGINT and verify no leftovers:
   - `for pidf in "$REPORT_DIR/scenarioB_final_service.pid" "$REPORT_DIR/scenarioB_final_streamer.pid"; do test -f "$pidf" && kill -INT "$(cat "$pidf")" || true; done`
   - `pgrep -fa "configurable-streamer|zenoh_service|mqtt_client" || true`
2. Stop broker:
   - `docker compose -f utils/mosquitto/docker-compose.yaml down`

Pass criteria:

- Repeated request/response markers in client/service logs.
- Repeated forwarding success in streamer log.
- No transport failure signatures in streamer/client logs.

---

## Minimal artifacts

All artifacts live under:

`$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/`

- [x] `checkpoint-commit.md`
- [x] `transport-matrix-baseline.md`
- [x] `transport-matrix-final.md`
- [x] `final-validation-summary.md`

Optional (only if needed for clarity):

- [x] `design-decisions.md`
- [x] `test-readability-delta.md`
- [x] `semantic-coherence-pass.md`
- [x] `phase3-hardening-evidence.md`
- [x] `phase6-doctest-hardening.md`

---

## Phase 0 - Checkpoint commit (mandatory first step)

- [x] Confirm branch and scope:
  - [x] `git status --short --branch`
  - [x] `git diff --stat`
- [x] Stage current work:
  - [x] `git add -A`
- [x] Pre-commit scope verification:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit checkpoint:
  - [x] `git commit -m "chore: checkpoint domain modernization baseline"`
- [x] Record commit hash + files in `checkpoint-commit.md`.

### Gate 0

- [x] Checkpoint commit exists.
- [x] Working tree is clean before Phase 1.

---

## Phase 1 - Canonical transport matrix baseline (must run before refactor edits)

Execution reference: use the section `Canonical smoke test runbook (applies to Phase 1 baseline and Phase 7 rerun)` for setup, validation, and teardown details.

### A) Zenoh <=> SOME/IP request/response

- [x] Terminal A (repo root) bootstrap:
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
  - [x] `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
  - [x] `export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
- [x] Terminal B (run streamer from `example-streamer-implementations/`):
  - [x] `cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5"`
- [x] Terminal C (repo root, run service):
  - [x] `cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- [x] Terminal D (repo root, run client):
  - [x] `cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"`
- [x] Verify criteria:
  - [x] no repeating `Routing info for remote service could not be found`
  - [x] `UMESSAGE_TYPE_RESPONSE` with `commstatus: Some(OK)`
  - [x] someip_client log shows continuous request/response progression (no transport fatal errors)
  - [x] zenoh_service log shows request handling without repeated failures

Stop/cleanup before Scenario B:

- [x] stop client/service/streamer processes cleanly (Ctrl-C each terminal)

### B) Zenoh <=> MQTT5 request/response

- [x] Terminal M1 (repo root, start broker):
  - [x] `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- [x] Terminal M2 (from `configurable-streamer/`, run streamer):
  - [x] verify local-router config uses `listen.endpoints` in `ZENOH_CONFIG.json5` (not `connect.endpoints`)
  - [x] `cargo run -- --config "CONFIG.json5"`
- [x] Terminal M3 (repo root, run service):
  - [x] `cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- [x] Terminal M4 (repo root, run client):
  - [x] `cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883`
- [x] Verify criteria:
  - [x] stable request/response flow
  - [x] no transport-level failures in logs
  - [x] mqtt_client log shows responses without disconnect loops
  - [x] configurable-streamer log shows no repeated bridge transport errors

Stop/cleanup after Scenario B:

- [x] stop client/service/streamer processes cleanly (Ctrl-C each terminal)
- [x] `docker compose -f utils/mosquitto/docker-compose.yaml down`

### Evidence

- [x] Record commands, env, and pass/fail in `transport-matrix-baseline.md`.

### Gate 1

- [x] Both scenarios pass, or explicit environment blocker documented and work paused.
  - [x] Scenario A passed.
  - [x] Scenario B passed.
  - [x] Environment-blocker branch was not triggered in this baseline run.
- [x] Blocker policy enforced for this run:
  - [x] No prerequisite blocker occurred; remediation capture branch is N/A for this run.
  - [x] Work did not proceed to Phase 2 until baseline matrix was green.

Future-run policy (instructional): if any scenario fails due to missing prerequisites (broker, vsomeip libs/config, ports), capture exact remediation in `transport-matrix-baseline.md` and pause before Phase 2 unless reviewer explicitly accepts the blocker.

---

## Phase 2 - Domain design decisions (before more rewrites)

### 2.1 ComparableTransport / transport identity keying

- [x] Document in `design-decisions.md` why local transport identity keying remains necessary (pinned dependency evidence).
- [x] Rename local keying type to domain-meaningful name if still generic/legacy.
  - [x] Decision captured in `design-decisions.md` (target name: `TransportIdentityKey`).
  - [x] Implemented in Wave 3B commit `e6c510142f90fd9aabba103faddd55dc8e2373f9`.

### 2.2 Facade consolidation

- [x] Remove redundant thin wrappers that provide no abstraction value.
  - [x] Decision captured in `design-decisions.md`.
  - [x] Implemented in Wave 3A commit `a26bec131ad57259f58142d6a8afb262f837f248`.
- [x] Keep one clear outward API path for `Endpoint` and `UStreamer`.
  - [x] Decision captured in `design-decisions.md`.
  - [x] Implemented in Wave 3A commit `a26bec131ad57259f58142d6a8afb262f837f248`.
- [x] Ensure runtime modules contain runtime concerns only.
  - [x] Decision captured in `design-decisions.md`.
  - [x] Implemented in Wave 3E commit `036e526b52a1c7859f5e00bdfa6e2f54584909ad`.

### 2.3 Domain ownership map

- [x] Assign single logical owner file/module per behavior family:
  - [x] route lifecycle
  - [x] subscription/routing resolution
  - [x] ingress listener registration lifecycle
  - [x] egress forwarding/pooling
  - [x] runtime bootstrap/spawn boundaries

### Gate 2

- [x] Decisions captured and agreed before implementation waves.

---

## Phase 3 - Domain modernization waves (commit each wave)

### Wave 3A - API facade and top-level consolidation

- [x] Remove/merge duplicate facade layers.
- [x] Keep outward API stable and intuitive.
- [ ] Commit wave.
  - [x] Commit exists: `a26bec131ad57259f58142d6a8afb262f837f248` (`refactor: consolidate streamer api facade ownership`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Wave 3B - Control-plane modernization

- [x] Modernize route table/lifecycle naming and mechanics.
- [x] Keep rollback/idempotency contracts.
- [ ] Commit wave.
  - [x] Commit exists: `e6c510142f90fd9aabba103faddd55dc8e2373f9` (`refactor: modernize control-plane route lifecycle boundaries`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Wave 3C - Routing modernization

- [x] Modernize publish resolution/subscription directory semantics and naming.
- [x] Preserve tuple strictness + wildcard behavior.
- [ ] Commit wave.
  - [x] Commit exists: `c08669e36b65ca3c0d7c98d843d2783e0ad8781a` (`refactor: modernize routing resolution policies`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Wave 3D - Data-plane modernization

- [x] Modernize ingress/egress internals (structs/impls/traits as useful).
- [x] Remove legacy names/mechanics that survived extraction.
- [ ] Commit wave.
  - [x] Commit exists: `7309904b5706459c278634dcda74d41ec215330f` (`refactor: modernize data-plane ingress and egress abstractions`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Wave 3E - Runtime modernization

- [x] Keep runtime adapters cohesive and isolated.
- [x] Remove API/domain leakage from runtime modules.
- [ ] Commit wave.
  - [x] Commit exists: `036e526b52a1c7859f5e00bdfa6e2f54584909ad` (`refactor: isolate runtime adapters and remove leakage`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Wave 3 hardening checks

- [x] `up-streamer/src/ustreamer.rs` trends toward ~500 actual code lines; hard fail if >900 actual code lines. *(measured actual code lines: 204; comments/doc-comments/blanks excluded)*
- [x] No duplicate legacy orchestration implementations remain in `ustreamer.rs`.
- [x] No placeholder stubs remain in new modules.
- [x] Each touched file has one coherent domain responsibility.

### Gate 3

- [x] Wave checks pass.
  - [x] Wave 3 hardening checks are recorded in this plan.
  - [x] Command-level hardening evidence is consolidated in `phase3-hardening-evidence.md`.
- [x] One commit exists per wave.
  - [x] Wave 3A: `a26bec131ad57259f58142d6a8afb262f837f248`
  - [x] Wave 3B: `e6c510142f90fd9aabba103faddd55dc8e2373f9`
  - [x] Wave 3C: `c08669e36b65ca3c0d7c98d843d2783e0ad8781a`
  - [x] Wave 3D: `7309904b5706459c278634dcda74d41ec215330f`
  - [x] Wave 3E: `036e526b52a1c7859f5e00bdfa6e2f54584909ad`

---

## Phase 4 - Test refactor for readability and trustworthiness

- [x] Move tests toward owning modules when appropriate.
- [x] Keep integration tests scenario-focused and readable.
- [x] Extract fixtures/helpers for long tests.
- [x] Ensure tests remain behavior-first and explicit.
- [x] Refactor harness/mocks as needed to match modernized domains.
- [ ] Commit phase.
  - [x] Commit exists: `4bf98615f810ec2086c3c8a68115d0be1342a805` (`test: improve readability and ownership of streamer tests`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).

### Required validation

- [x] `cargo test -p up-streamer -- --nocapture`
- [x] `cargo test -p subscription-cache -- --nocapture`
- [x] `cargo test -p integration-test-utils -- --nocapture`

### Gate 4

- [x] Readability improved with preserved behavior coverage.
  - [x] Readability deltas are documented in `test-readability-delta.md`.
  - [x] Required Phase 4 validation logs are green (`phase4_up_streamer_test.log`, `phase4_subscription_cache_test.log`, `phase4_integration_test_utils_test.log`).

---

## Phase 5 - Internal semantic coherence pass (route-first internals)

### Canonical internal terminology policy

- [x] Internal canonical terminology is `route`/`routing`/`ingress`/`egress`.
- [x] Keep outward API streamer-centric (`Endpoint`, `UStreamer`) and compatibility-safe.
- [x] `add_forwarding_rule` / `delete_forwarding_rule` remain supported while internals standardize on route semantics.

### Structural coherence requirements (Rust-idiomatic)

- [x] Control-plane ownership clarity:
  - [x] `route_table.rs` contains a concrete `RouteTable` owner (not only aliases/helpers).
  - [x] `route_lifecycle.rs` contains lifecycle transition/orchestration semantics (not only storage wrappers).
  - [x] route identity uses named model types (`RouteKey` and related structs), not tuple-centric contracts.
- [x] Data-plane egress clarity:
  - [x] eliminate tuple-heavy aliasing for worker pool internals; use named entry types.
  - [x] remove/replace underscore keepalive fields that hide intent; worker lifetime ownership is explicit.
  - [x] `egress_worker.rs` contains meaningful worker state/handle model (no empty worker marker struct).
- [x] Data-plane ingress clarity:
  - [x] replace tuple key/value aliases in ingress registry with named binding key/state structs.
  - [x] remove anonymous `String, String` / `usize` tuple semantics from registry state.
- [x] Routing directory clarity:
  - [x] `subscription_directory.rs` uses a meaningful abstraction (stateful type or cohesive free-function module), not an empty namespace struct.
- [x] Internal cross-layer boundaries:
  - [x] no control/routing/data-plane dependency on helpers owned by `ustreamer.rs`.
  - [x] shared helpers live in neutral domain modules.
- [x] Naming/log coherence:
  - [x] log tags and internal symbols match route-first terminology (API compatibility names may remain at the public facade).

### Optional external API modernization (compatibility-safe)

- [x] If introduced, canonical route-named public methods (`add_route` / `delete_route`) delegate or are delegated-to by compatibility methods.
- [x] Existing external usages of `add_forwarding_rule` / `delete_forwarding_rule` continue to compile and behave identically.

### Required validation

- [x] `cargo check -p up-streamer`
- [x] `cargo test -p up-streamer -- --nocapture`

### Evidence

- [x] Record structural rationale, commands, and outcomes in `semantic-coherence-pass.md`.

### Gate 5

- [ ] Commit phase.
  - [x] Commit exists: `425cca3cdf49fde040ca6de7a80177d0a0cd712f` (`refactor: align internal route semantics with domain modules`).
  - [ ] Pre-commit scope verification evidence captured (`git diff --name-only --cached`, `git diff --stat --cached`).
- [x] File names and internal semantics are aligned for control-plane/routing/data-plane/runtime.
  - [x] Structural ownership checks are captured in `semantic-coherence-pass.md` (Entries S1-S5).
  - [x] Cross-layer boundary checks are captured in `semantic-coherence-pass.md` (Entry S6).
- [x] Internal route terminology is coherent and middleware-appropriate.
  - [x] Canonical route terminology checks are captured in `semantic-coherence-pass.md` (Entries S7 and S10).
- [x] Behavior is preserved.
  - [x] `cargo check -p up-streamer` passed (`phase5_cargo_check.log`).
  - [x] `cargo test -p up-streamer -- --nocapture` passed (`phase5_cargo_test.log`).

---

## Phase 6 - Rustdoc and doctest hardening

- [x] Add meaningful rustdoc for domain modules/types.
- [x] Add at least one doctest example per layer (API/control-plane/routing/data-plane/runtime).
  - [x] API layer doctests execute (`up-streamer/src/lib.rs`, `up-streamer/src/endpoint.rs`).
  - [x] Control-plane layer doctest executes (`up-streamer/src/control_plane/mod.rs`).
  - [x] Routing layer doctest executes (`up-streamer/src/routing/mod.rs`).
  - [x] Data-plane layer doctest executes (`up-streamer/src/data_plane/mod.rs`).
  - [x] Runtime layer doctest executes (`up-streamer/src/runtime/mod.rs`).

### Required validation

- [x] `cargo doc -p up-streamer --no-deps`
- [x] `cargo test -p up-streamer --doc`
- [x] `cargo test -p up-streamer --doc` output shows control-plane/routing/data-plane/runtime layer doctests executed (not ignored).

### Evidence

- [x] Record command-level rustdoc/doctest outcomes in `phase6-doctest-hardening.md`.

### Gate 6

- [x] Docs and doctests explain abstractions and usage clearly.
  - [x] Rustdoc narrative coverage exists for API/control-plane/routing/data-plane/runtime.
  - [x] Doctest execution coverage exists for API/control-plane/routing/data-plane/runtime.

---

## Phase 7 - Final validation and transport matrix re-run

### Core/workspace checks

- [x] `cargo build`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### E2E and example binaries

Use the section `Canonical smoke test runbook (applies to Phase 1 baseline and Phase 7 rerun)` as the single source of truth for setup, validation, and teardown.

- [x] Re-run canonical Zenoh<=>SOME/IP matrix and record in `transport-matrix-final.md`.
- [x] Re-run canonical Zenoh<=>MQTT5 matrix and record in `transport-matrix-final.md`.
- [x] Verify expected example binaries used for those E2E scenarios still work.
- [x] Execute expanded example-binary smoke matrix (both request/response directions and both pub/sub directions for Zenoh<=>SOME/IP and Zenoh<=>MQTT).
  - [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service`
  - [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - [x] Evidence captured in `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md` and per-skill run directories under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-*/`.

### Final evidence

- [x] Summarize all outcomes in `final-validation-summary.md`.

### Gate 7

- [x] Final validation passes with evidence.

---

## Evidence minimums (applies to every phase)

- [x] Every evidence entry includes required fields for each phase.
  - [x] Phase 0 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 1 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 2 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 3 dedicated command-level hardening evidence is captured in `phase3-hardening-evidence.md`.
  - [x] Phase 4 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 5 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 6 evidence includes exact command, working directory, exit status, key lines, and conclusion.
  - [x] Phase 7 evidence includes exact command, working directory, exit status, key lines, and conclusion.
- [x] No phase is marked complete with narrative-only notes.
  - [x] Phases 0, 1, 2, 4, and 5 are backed by command-level evidence artifacts.
  - [x] Phase 6 evidence reconciliation is complete with fresh non-ignored doctest proof.
  - [x] Phase 3 hardening evidence linkage is now present (`phase3-hardening-evidence.md`).

---

## Final cleanup gate

- [x] Mandatory artifacts exist and are up to date.
- [x] `git status --short` is clean after the final commit (or intentionally staged for explicit next action).
- [x] No placeholder/TBD language remains in final evidence artifacts.

---

## Commit discipline (always on)

- [ ] Before every commit, pre-commit scope verification is evidenced.
  - [x] Phase 0 checkpoint commit evidence includes `git diff --name-only --cached` and `git diff --stat --cached`.
  - [ ] Transport baseline evidence commit is not yet created.
  - [ ] Wave 3A commit evidence includes both pre-commit verification commands.
  - [ ] Wave 3B commit evidence includes both pre-commit verification commands.
  - [ ] Wave 3C commit evidence includes both pre-commit verification commands.
  - [ ] Wave 3D commit evidence includes both pre-commit verification commands.
  - [ ] Wave 3E commit evidence includes both pre-commit verification commands.
  - [ ] Phase 4 commit evidence includes both pre-commit verification commands.
  - [ ] Phase 5 commit evidence includes both pre-commit verification commands.
  - [ ] Phase 6 commit evidence includes both pre-commit verification commands.
  - [ ] Phase 7 final evidence commit is pending.
- [x] Commits are wave-scoped and rationale-focused for completed phases.
  - [x] Phase 0 checkpoint commit subject is scoped and rationale-focused.
  - [x] Wave 3A-3E commit subjects are scoped to their modernization wave.
  - [x] Phase 4, Phase 5, and Phase 6 commit subjects are scoped to their phase outcomes.

Commit message templates:

- [x] Phase 0 checkpoint: `chore: checkpoint domain modernization baseline`
- [ ] Transport baseline: `test: capture canonical transport baseline matrix`
- [x] Wave 3A: `refactor: consolidate streamer api facade ownership`
- [x] Wave 3B: `refactor: modernize control-plane route lifecycle boundaries`
- [x] Wave 3C: `refactor: modernize routing resolution policies`
- [x] Wave 3D: `refactor: modernize data-plane ingress and egress abstractions`
- [x] Wave 3E: `refactor: isolate runtime adapters and remove leakage`
- [x] Phase 4: `test: improve readability and ownership of streamer tests`
- [x] Phase 5: `refactor: align internal route semantics with domain modules`
- [x] Phase 6: `docs: add layered rustdoc and doctest coverage`
- [ ] Phase 7: `test: record final transport matrix and validation evidence`

Suggested commit sequence:

- [x] checkpoint baseline commit
- [ ] transport baseline evidence commit
- [x] wave 3A commit
- [x] wave 3B commit
- [x] wave 3C commit
- [x] wave 3D commit
- [x] wave 3E commit
- [x] tests readability commit
- [x] internal semantic coherence commit
- [x] rustdoc/doctest commit
- [ ] final validation + transport final evidence commit

---

## Definition of done

- [x] Domain internals are modernized (not merely relocated).
- [x] Outward streamer API remains simple and stable.
- [x] Test suite remains green and easier for humans to review.
- [x] Canonical Zenoh<=>SOME/IP and Zenoh<=>MQTT matrix pass before and after finalization.
- [x] Both request/response directions and both pub/sub directions were exercised across Zenoh<=>SOME/IP and Zenoh<=>MQTT example binaries.
  - [x] Evidence link: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`.
- [x] All refactor work is captured in logical commits.
