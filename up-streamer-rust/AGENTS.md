# Project Instructions

## Overview

`up-streamer-rust` is a multi-crate Rust workspace for cross-transport uProtocol streaming.

- Core streamer crate: `up-streamer`
- Streamer implementations: `example-streamer-implementations`, `configurable-streamer`
- Transport usage examples: `example-streamer-uses`
- Zenoh plugin: `up-linux-streamer-plugin`

Primary engineering focus is transport compatibility, forwarding behavior, and CI-stable validation across Zenoh, SOME/IP, and MQTT5.

## Workflow

### Artifact location policy (strict)

- `$OPENCODE_CONFIG_DIR` is the canonical location for all assistant-generated operational artifacts.
- Read execution plans from `$OPENCODE_CONFIG_DIR/plans/`.
- Write prompts to `$OPENCODE_CONFIG_DIR/prompts/`.
- Write validation/report artifacts to `$OPENCODE_CONFIG_DIR/reports/`.
- Write any ad hoc analysis notes/checklists/runbooks to `$OPENCODE_CONFIG_DIR` subdirs (not the repo).
- Do **not** create repo-local plan/prompt/report artifacts unless explicitly requested.
  - Disallowed default locations include repo `plans/*.md`, repo `prompts/*.md`, repo `reports/*.md`, and root-level ad hoc markdown artifacts.
- If accidental repo-local artifacts are created, remove them before push/merge.

### Branching and commit expectations

- Keep work on one branch and one PR unless explicitly asked otherwise.
- Split work into logical commits aligned to plan phases/chunks.
- Do not squash locally; do not amend unless explicitly requested.
- Before each commit, verify scope with:
  - `git diff --name-only --cached`
  - `git diff --stat --cached`

### CI parity preflight (run from repo root)

Always run these before push for transport-affecting changes:

1. Base checks (no transport features):
   - `source build/envsetup.sh highest`
   - `cargo build`
   - `cargo clippy --all-targets -- -W warnings -D warnings`
   - `cargo fmt -- --check`

2. Bundled transport feature matrix:
   - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
   - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`

3. Unbundled transport feature matrix (when touching transport/plugin integration):
   - Ensure `VSOMEIP_INSTALL_PATH` points to a valid vsomeip install tree.
   - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
   - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`

4. Workspace checks (unless environment-constrained):
   - `cargo check --workspace --all-targets`
   - `cargo test --workspace`

### PR description minimums

For dependency/transport migrations, include:

- MSRV rationale
- Target dependency matrix
- Temporary pin rationale and explicit follow-up action
- Validation commands and key outcomes
- Commit-by-commit summary

### Test quality defaults (progressive disclosure)

- Keep always-on test guidance lightweight in this file; put detailed playbooks in skills to avoid context pollution.
- Prefer deterministic tests over timing-sensitive behavior; avoid sleeps unless no deterministic trigger exists.
- Keep tests short and behavior-first:
  - one primary behavior per test
  - explicit assertions with clear expected values
  - names that describe behavior, not issue IDs
- For non-trivial test authoring or refactors, load `rust-test-quality-gate`.

## Canonical Validation Scenarios

Maintain two canonical cross-transport smoke tests for this repo.

### A) Zenoh <-> SOME/IP (request/response)

- Streamer: `up-linux-streamer` bin `zenoh_someip`
- Entities: `someip_client` + `zenoh_service` (`example-streamer-uses`)
- Required setup:
  - `source build/envsetup.sh highest`
  - If using bundled vsomeip, include `target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib` in `LD_LIBRARY_PATH`
  - Run from `example-streamer-implementations` (or pass absolute config path)
- Pass criteria:
  - No repeating `Routing info for remote service could not be found`
  - Client receives `UMESSAGE_TYPE_RESPONSE` with `commstatus: Some(OK)`

### B) Zenoh <-> MQTT5 (request/response)

- Streamer: `configurable-streamer` using `CONFIG.json5`
- Entities: `mqtt_client` + `zenoh_service` (or inverse pairing)
- Required setup:
  - Start broker from `utils/mosquitto/docker-compose.yaml`
  - For local router mode in `configurable-streamer/ZENOH_CONFIG.json5`, use `listen.endpoints` (not `connect.endpoints`) to avoid self-connect failures.
- Pass criteria:
  - Stable continuous request/response flow across streamer
  - No transport-level failures in streamer/entity logs

### Logging profile for routing/classification debugging

- Use:
  - `RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
- For SOME/IP classification issues, inspect logs for:
  - `registration_type`
  - `streamer_use_case final result`
  - `Routing info for remote service could not be found`

### Known doc caveat

- Some older docs mention `zenoh_mqtt` under `example-streamer-implementations`.
- Current MQTT bridge path is `configurable-streamer`; `example-streamer-implementations` currently provides `zenoh_someip`.

### Current coverage note

- Pub/sub was not validated in this bug-1 execution cycle.
- Use pub/sub pairs (e.g. `someip_publisher` <-> `zenoh_subscriber`, `mqtt_publisher` <-> `zenoh_subscriber`) as additional coverage when needed.

## Known CI Failure Patterns

- Feature-gated dead code in no-feature clippy:
  - If a module is only used behind features, gate both `mod` declaration and usage with matching `#[cfg(...)]`.
- Zenoh plugin API drift (`up-linux-streamer-plugin`):
  - Use `DynamicRuntime` for plugin start args.
  - Read plugin config via runtime generic config APIs.
  - Match `RunningPluginTrait::config_checker` signature with `JsonKeyValueMap`.

## Code Standards

- MSRV: Rust `1.88`
- Current transport target matrix:
  - `up-rust = 0.9.x`
  - `up-transport-zenoh = 0.9.0`
  - `up-transport-mqtt5 = 0.4.0`
  - `up-transport-vsomeip` pinned to git rev `278ab26415559d6cb61f40facd21de822032cc83` until crates.io catches up
- Preserve existing behavior unless change is explicitly requested.
- Keep lint fixes narrow; avoid broad `allow` usage when source fixes are possible.
- When using temporary pins, always include an explicit follow-up note to remove them.

## Files To Know

- Workspace manifest: `Cargo.toml`
- CI definitions:
  - `.github/workflows/bundled-lint-and-test.yaml`
  - `.github/workflows/unbundled-lint-and-test.yaml`
- Env bootstrap: `build/envsetup.sh`
- Canonical streamer binaries/configs:
  - `example-streamer-implementations/src/bin/zenoh_someip.rs`
  - `example-streamer-implementations/DEFAULT_CONFIG.json5`
  - `configurable-streamer/src/main.rs`
  - `configurable-streamer/CONFIG.json5`
- Plans: `$OPENCODE_CONFIG_DIR/plans/`
- Prompts: `$OPENCODE_CONFIG_DIR/prompts/`
- Reports: `$OPENCODE_CONFIG_DIR/reports/`

## Available Skills

- `skills/ci-parity-preflight/SKILL.md`
- `skills/gh-ci-triage/SKILL.md`
- `skills/artifact-hygiene-guard/SKILL.md`
- `skills/transport-smoke-validation/SKILL.md`
- `skills/rust-test-quality-gate/SKILL.md`
