# Up-Streamer Runtime and Lint Debt Cleanup Plan

Date: 2026-02-10
Execution branch: `refactor/up-streamer-domain-architecture`

## Intent

Close the remaining runtime and lint modernization work on the current branch by:

- removing any `async-std` usage and standardizing on Tokio,
- removing project-owned `log`-style usage and standardizing on `tracing`,
- removing dead code where possible and documenting any intentional remnants,
- removing `#[allow(...)]` usage where possible and documenting any intentional remnants.

## Execution mode

- [x] Manual execution only (no autopilot orchestration for this run).
- [x] Keep work on `refactor/up-streamer-domain-architecture`.
- [x] Follow phases and gates in strict order.

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
- [x] Confirm no stale transport processes before starting:
  - [x] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`

### Preflight gate

- [x] Session preconditions are satisfied for deterministic execution.

## Artifact policy

All artifacts for this plan are written under:

`$OPENCODE_CONFIG_DIR/reports/runtime-lint-debt-cleanup/`

- [x] `baseline-inventory.md`
- [x] `async-runtime-migration.md`
- [x] `log-to-tracing-migration.md`
- [x] `dead-code-remnants.md`
- [x] `clippy-allow-remnants.md`
- [ ] `final-validation-summary.md`

Each evidence entry must include:

- exact command
- working directory (if not repo root)
- exit status / pass-fail
- key output lines
- concise conclusion

## Blocking policy

- [ ] If a gate fails, stop progression and do not continue to later phases.
- [ ] Record blocker details in the active phase report with:
  - [ ] exact failing command
  - [ ] working directory
  - [ ] exit status
  - [ ] key output lines
  - [ ] concrete remediation path
- [ ] Resume only after blocker resolution is evidenced.

---

## Phase 0 - Baseline inventory and checkpoint

- [x] Confirm current branch and working tree state:
  - [x] `git status --short --branch`
- [x] Create report directory:
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/runtime-lint-debt-cleanup"`
- [x] Capture baseline runtime inventory:
  - [x] `rg -n "async-std|async_std" . --glob "Cargo.toml"`
  - [x] `rg -n "async-std|async_std|async_std::" . --glob "*.rs"`
  - [x] `cargo tree --workspace --all-features | rg "async-std|async_std|async-io|async-global-executor|smol" || true`
- [x] Capture baseline logging inventory:
  - [x] `rg -n "\\blog::|tracing::log::|try_init_log_from_env" . --glob "*.rs"`
- [x] Capture baseline allow inventory (source only, excluding `target/`).
  - [x] `rg -n "#\\!\\[allow\\(|#\\[allow\\(" . --glob "*.rs" --glob "!target/**"`
  - [x] `rg -n "allow\\(dead_code\\)|allow\\(clippy::|allow\\(unused" . --glob "*.rs" --glob "!target/**"`
- [x] Capture baseline dead-code marker inventory:
  - [x] `rg -n "todo!\\(|unimplemented!\\(" . --glob "*.rs"`
- [x] Capture baseline strict lint status:
  - [x] `cargo clippy --workspace --all-targets --all-features -- -W warnings -D warnings`
- [x] Record all baseline evidence in `baseline-inventory.md`.

### Gate 0

- [x] Baseline inventories and strict clippy baseline are captured with evidence.

---

## Phase 1 - Async runtime modernization (`async-std` -> Tokio)

### 1.1 Source and dependency cleanup

- [x] Remove direct `async-std` usage from source (if present).
- [x] Remove direct `async-std` dependencies from manifests (if present).
- [x] Replace any async-std APIs with Tokio equivalents (`tokio::spawn`, `tokio::time::sleep`, Tokio runtime primitives).

### 1.2 Verification

- [x] Verify no remaining async-std references:
  - [x] `rg -n "async-std|async_std|async_std::" . --glob "*.rs"`
  - [x] `rg -n "async-std|async_std" . --glob "Cargo.toml"`
  - [x] `cargo tree --workspace --all-features | rg "async-std|async_std|async-io|async-global-executor|smol" || true`
- [x] Record migration or no-op rationale in `async-runtime-migration.md`.

### Gate 1

- [x] No project source/manifests use `async-std`.
- [x] Report documents exact proof (or explicit blocker).

---

## Phase 2 - Logging modernization (`log` usage -> `tracing`)

### 2.1 Source migration

- [x] Replace direct `tracing::log::*` calls with `tracing::*` macros.
- [x] Replace/retire runtime log initialization paths that rely on non-tracing logging APIs where feasible.
- [x] Ensure initialization stays safe (no panic from double-init) and preserves plugin/runtime behavior.

### 2.2 Verification

- [x] Verify no project-owned `log` API usage remains:
  - [x] `rg -n "\\blog::|tracing::log::" . --glob "*.rs"`
- [x] Verify `log` crate presence is only transitive dependency usage (not direct source API usage):
  - [x] `cargo tree -i log`
- [x] Verify any remaining `try_init_log_from_env` call sites are either removed or explicitly justified in report with plugin/runtime rationale.
- [x] Record commands and outcomes in `log-to-tracing-migration.md`.

### Gate 2

- [x] Project-authored code uses `tracing` APIs for logging.
- [x] Any unavoidable residual logging bridge usage is explicitly justified, and transitive `log` usage is called out as external-only.

---

## Phase 3 - Dead code removal and justification

### 3.1 Removal pass

- [x] Remove dead/private helpers that are truly unused.
- [x] Refactor shared modules to avoid symbol-level dead code where practical.
- [x] Keep behavior and public compatibility intact.

### 3.2 Verification

- [x] Run dead/unused-focused strict lint:
  - [x] `cargo clippy --workspace --all-targets --all-features -- -W dead_code -W unused -D warnings`
- [x] Re-scan for dead-code allowances and dead-code markers in source.
  - [x] `rg -n "allow\\(dead_code\\)" . --glob "*.rs" --glob "!target/**"`
  - [x] `rg -n "todo!\\(|unimplemented!\\(" . --glob "*.rs"`

### 3.3 Required remnant report

- [x] If dead code remains intentionally, record each instance in `dead-code-remnants.md` with:
  - [x] file path and exact line
  - [x] why removal is currently unsafe/unwanted
  - [x] alternatives attempted
  - [x] follow-up removal trigger
- [ ] If no dead code remains, write explicit "none remaining" conclusion in `dead-code-remnants.md`.

### Gate 3

- [x] Dead code is removed where feasible.
- [x] Any remaining dead code is explicitly justified with concrete follow-up.

---

## Phase 4 - Clippy allow elimination and lint cleanups

### 4.1 `allow` burn-down

- [x] Inventory all source-level `#[allow(...)]` and `#![allow(...)]` (excluding generated `target/`).
  - [x] `rg -n "#\\!\\[allow\\(|#\\[allow\\(" . --glob "*.rs" --glob "!target/**"`
- [x] Remove avoidable `allow` attributes by rewriting code to satisfy lint intent.
- [x] Rewrite code to avoid lint triggers instead of silencing them.

### 4.2 Strict lint verification

- [x] Run strict clippy across workspace and all features:
  - [x] `cargo clippy --workspace --all-targets --all-features -- -W warnings -D warnings`

### 4.3 Required allow-remnant report

- [x] For each remaining `allow`, document in `clippy-allow-remnants.md`:
  - [x] lint name
  - [x] exact file and line
  - [x] technical reason it must remain now
  - [x] alternatives attempted
  - [x] owner/follow-up action to remove later
- [ ] If no `allow` remains, write explicit "none remaining" conclusion in `clippy-allow-remnants.md`.

### 4.4 O(1) interface restoration (user-directed correction)

- [x] Restore O(1)-capable external interfaces where set-like behavior was regressed.
- [x] Keep mutable-key lint compliance by using immutable identity-key wrappers (no `#[allow(clippy::mutable_key_type)]` in production code).
- [x] Update affected modules:
  - [x] `subscription-cache` cache fetch interfaces and merge path
  - [x] `up-streamer` subscription-directory lookup interface
  - [x] `up-streamer` publish-resolution source-filter interface
  - [x] `up-streamer` ingress-registry call sites
- [x] Re-run strict clippy after interface restoration:
  - [x] `cargo clippy --workspace --all-targets --all-features -- -W warnings -D warnings`
- [x] Re-scan for `allow` and dead-code markers:
  - [x] `rg -n "#\\!\\[allow\\(|#\\[allow\\(" . --glob "*.rs" --glob "!target/**"`
  - [x] `rg -n "todo!\\(|unimplemented!\\(" . --glob "*.rs"`
- [x] Update `clippy-allow-remnants.md` and `dead-code-remnants.md` evidence to reflect restored O(1) interfaces.

### Gate 4

- [x] Code is rewritten to avoid clippy lints where practical.
- [x] Remaining `allow` usage (if any) is fully justified with actionable follow-up.

---

## Phase 5 - Full validation matrix and transport confidence

### 5.1 Build/lint/test matrix

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] If transport/plugin integration was touched, run unbundled transport checks:
  - [ ] Confirm `VSOMEIP_INSTALL_PATH` points to a valid install tree.
  - [ ] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is unavailable, record constrained skip and remediation in `final-validation-summary.md`.
- [x] `cargo check --workspace --all-targets`
- [ ] `cargo test --workspace`

### 5.2 Expanded transport smoke confidence

- [ ] Re-run the 8 smoke skills and verify pass evidence.
  - [ ] Pre-run stale-process check and cleanup evidence captured.
  - [ ] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`
  - [ ] Skills location: `$OPENCODE_CONFIG_DIR/skills/`
  - [ ] Skill index/reference: `$OPENCODE_CONFIG_DIR/skills/transport-smoke-validation/SKILL.md`
  - [ ] Run `smoke-zenoh-someip-rr-someip-client-zenoh-service` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-someip-rr-someip-client-zenoh-service/SKILL.md`)
  - [ ] Run `smoke-zenoh-someip-rr-zenoh-client-someip-service` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-someip-rr-zenoh-client-someip-service/SKILL.md`)
  - [ ] Run `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber/SKILL.md`)
  - [ ] Run `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber/SKILL.md`)
  - [ ] Run `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service/SKILL.md`)
  - [ ] Run `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service/SKILL.md`)
  - [ ] Run `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber/SKILL.md`)
  - [ ] Run `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber` (`$OPENCODE_CONFIG_DIR/skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber/SKILL.md`)
  - [ ] Post-run teardown verification captured (no lingering streamer/entity processes).
  - [ ] `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`
  - [ ] Verify per-skill evidence directories under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-*/`
  - [ ] Verify run summary at `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`
  - [ ] Include per-skill pass/fail table in `final-validation-summary.md`.

### Gate 5

- [ ] Validation matrix passes.
- [ ] Transport smoke matrix remains green.

---

## Commit discipline (mandatory for this plan)

Before every commit:

- [ ] `git diff --name-only --cached`
- [ ] `git diff --stat --cached`

Suggested commit chunks:

- [ ] runtime + logging modernization
- [ ] dead code removals and related refactors
- [ ] clippy allow removals and lint-driven rewrites
- [ ] validation/report updates

---

## Final gate

- [ ] `async-std` usage removed (or proven absent with evidence).
- [ ] Project-owned `log` usage removed in favor of `tracing`.
- [ ] Dead code removed where feasible; remaining instances documented.
- [ ] `allow` usage removed where feasible; remaining instances documented.
- [ ] Full build/lint/test + transport smoke validation remains green.
- [ ] Final outcomes summarized in `final-validation-summary.md`.
