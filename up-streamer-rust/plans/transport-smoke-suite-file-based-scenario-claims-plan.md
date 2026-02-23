# Transport Smoke Suite File-Based Scenario Claims Plan

Date: 2026-02-12
Status: in-progress
Owner: OpenCode execution session

## 0) Objective

- [x] Externalize scenario claims into per-scenario JSON files and load them at runtime.
- [x] Keep strict claim-source behavior: claims must load from the resolved file path; no fallback to in-code claim constants.
- [x] Preserve current deterministic orchestration, threshold semantics, claim matching semantics, and pass/fail behavior.

## 1) Locked Decisions

- [x] Claims source policy is strict file-only.
  - [x] Missing claims file is a hard failure.
  - [x] Malformed claims file is a hard failure.
  - [x] Scenario id mismatch between binary and claims file is a hard failure.
  - [x] No fallback to inline `CLAIMS` arrays.
- [x] Default layout is one claims file per scenario id.
  - [x] Default directory: `utils/transport-smoke-suite/claims/`.
  - [x] Default file naming: `<scenario-id>.json`.
- [x] Keep one CLI entry for override.
  - [x] `--claims-path <path>` accepted by scenario and matrix binaries.
  - [x] `<path>` may be omitted, directory, or file.
- [x] Matrix path behavior is explicit.
  - [x] If `--claims-path` is a file and multiple scenarios are selected, fail fast with actionable diagnostics.
  - [x] If exactly one scenario is selected, file path override is valid.
- [x] Existing claim semantics remain unchanged.
  - [x] Non-overlapping regex counting.
  - [x] Case-sensitive regex behavior unless pattern opts in.
  - [x] Independent claim evaluation.
  - [x] Existing threshold defaults and CLI overrides remain authoritative.

## 2) Scope

### 2.1 In scope

- [x] Add claim file schema and loader logic to `transport-smoke-suite`.
- [x] Add per-scenario claims JSON files for all 8 canonical scenarios.
- [x] Wire claim path resolution into scenario and matrix flows.
- [x] Refactor scenario binaries to remove embedded `CLAIMS` definitions.
- [x] Update contract and fixture tests to use file-based claims source.
- [x] Update docs with default claims location and override behavior.

### 2.2 Out of scope

- [x] Changing scenario inventory (still canonical 8 only).
- [x] Changing transport orchestration/process graph behavior.
- [x] Changing claim thresholds or regex semantics beyond source relocation.
- [x] Introducing claim fallback logic.

## 3) Design

### 3.1 Claims file schema (per scenario)

- [x] Define JSON schema represented by serde structs in `utils/transport-smoke-suite/src/claims.rs`.
  - [x] Top-level fields include:
    - [x] `schema_version`
    - [x] `scenario_id`
    - [x] `claims` (array)
  - [x] Claim entry fields include:
    - [x] `claim_id`
    - [x] `category`
    - [x] `kind`
    - [x] `file`
    - [x] `pattern`
    - [x] threshold descriptor (selector-backed or fixed value)
- [x] Map serialized threshold descriptors into existing `ThresholdSelector` semantics.
  - [x] Endpoint communication selector
  - [x] Egress attempt selector
  - [x] Egress ok selector
  - [x] Egress worker selector
  - [x] Fixed numeric threshold
- [x] Keep backward-compatible report semantics where possible.
  - [x] If report schema grows (for claims source metadata), bump schema version deliberately.

### 3.2 Claims path resolution

- [x] Implement centralized resolution logic.
  - [x] Inputs: `repo_root`, `scenario_id`, optional `claims_path`.
  - [x] No override -> `utils/transport-smoke-suite/claims/<scenario-id>.json`.
  - [x] Directory override -> `<dir>/<scenario-id>.json`.
  - [x] File override -> exact file path.
- [x] Validate resolved path semantics.
  - [x] Path exists and is readable.
  - [x] JSON parses successfully.
  - [x] File `scenario_id` matches requested scenario id.
  - [x] At least one claim exists.
  - [x] Claim ids are unique within file.

### 3.3 Matrix-specific rules

- [x] Add matrix prevalidation for `--claims-path` usage.
  - [x] If override is file and selected scenarios count > 1, fail before run loop.
  - [x] Error message includes exactly why and how to fix:
    - [x] use directory override for multi-scenario matrix
    - [x] or select one scenario with `--only`

## 4) Implementation Phases

### Phase A: Loader foundations

- [x] Extend `utils/transport-smoke-suite/src/claims.rs` with file-backed models and loaders.
  - [x] Add serde structs for claim-file payload.
  - [x] Add conversion from file structs to `ClaimTemplate` or directly to `ClaimSpec`.
  - [x] Add dedicated validation errors with actionable context.
  - [x] Keep existing in-memory claim evaluator APIs reusable by loaded claims.

### Phase B: Scenario runtime integration

- [x] Update `utils/transport-smoke-suite/src/scenario.rs` to source claims from file.
  - [x] Add `claims_path: Option<PathBuf>` to `ScenarioCliArgs`.
  - [x] Resolve claims file during `Preflight` phase.
  - [x] Load and validate claims once, then evaluate in `ValidateClaims` phase.
  - [x] Remove `claim_templates` function argument from `run_scenario`.
  - [x] Ensure strict fail-fast behavior on claims load/validation errors.
  - [x] Include resolved claims path in diagnostics/repro/report metadata.

### Phase C: Scenario binary cleanup

- [x] Refactor all 8 scenario binaries in `utils/transport-smoke-suite/src/bin/`.
  - [x] Remove inline `const CLAIMS` blocks.
  - [x] Remove now-unused claim imports.
  - [x] Call `run_scenario(SCENARIO_ID, cli.common)` using file-backed runtime loading.
  - [x] Keep binary names, scenario ids, and CLI behavior intact.

### Phase D: Matrix integration

- [x] Update `utils/transport-smoke-suite/src/bin/transport-smoke-matrix.rs`.
  - [x] Add `--claims-path <path>` option.
  - [x] Forward claims path to child scenario invocations.
  - [x] Enforce multi-scenario + file override guard.
  - [x] Preserve sequential continue-on-failure behavior.

### Phase E: Add claims files

- [x] Create `utils/transport-smoke-suite/claims/` files for all 8 scenarios.
  - [x] `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.json`
  - [x] `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.json`
  - [x] `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.json`
  - [x] `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.json`
  - [x] `smoke-zenoh-someip-rr-zenoh-client-someip-service.json`
  - [x] `smoke-zenoh-someip-rr-someip-client-zenoh-service.json`
  - [x] `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.json`
  - [x] `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.json`
- [x] Mirror current claim sets exactly.
  - [x] Preserve claim ids and categories.
  - [x] Preserve endpoint/egress/forbidden patterns.
  - [x] Preserve SOME/IP-only forbidden routing signature claim.

### Phase F: Tests

- [x] Update `utils/transport-smoke-suite/tests/scenario_contracts.rs`.
  - [x] Assert 8 scenario ids remain registered.
  - [x] Assert each scenario has a corresponding claims JSON file.
  - [x] Assert each claims file has required category coverage:
    - [x] endpoint communication
    - [x] streamer egress
    - [x] forbidden signature
- [x] Update `utils/transport-smoke-suite/tests/fixture_audit.rs`.
  - [x] Load claim definitions from scenario claims files.
  - [x] Remove duplicated ad hoc per-test claim construction.
  - [x] Keep pass and fail fixture assertions unchanged in intent.
- [x] Add loader unit tests in `utils/transport-smoke-suite/src/claims.rs`.
  - [x] Successful load path (default and override patterns).
  - [x] Missing file error.
  - [x] Malformed JSON error.
  - [x] Scenario id mismatch error.
  - [x] Duplicate claim id error.
  - [x] Invalid threshold descriptor error.

### Phase G: Documentation

- [x] Update `README.md` deterministic smoke section.
  - [x] Document default claims location.
  - [x] Document `--claims-path` behavior for scenario and matrix.
  - [x] Document matrix file-override restriction for multi-scenario runs.
  - [x] Add one example command for single scenario with custom claims file.
  - [x] Add one example command for matrix with custom claims directory.

## 5) Validation Plan

- [x] Code quality and correctness.
  - [x] `cargo fmt -- --check`
  - [x] `cargo clippy -p transport-smoke-suite --all-targets -- -W warnings -D warnings`
  - [x] `cargo test -p transport-smoke-suite`
- [x] Runtime smoke verification.
  - [x] Run one scenario with default claims path.
  - [x] Run one scenario with explicit claims file override.
  - [x] Run matrix with default claims path.
  - [x] Run matrix with explicit claims directory override.
  - [x] Confirm matrix fails fast for multi-scenario run with claims file override.
- [x] Artifact/repro checks.
  - [x] Scenario report includes enough context to identify claims source path.
  - [x] Repro command includes claims override when provided.

## 6) Risks and Mitigations

- [x] Risk: JSON schema drift or ambiguity during future edits.
  - [x] Mitigation: strict loader validation + unit tests + clear README examples.
- [x] Risk: duplicate claim logic in tests and runtime.
  - [x] Mitigation: tests load the same JSON claim source as runtime.
- [x] Risk: matrix override misuse (file path for multiple scenarios).
  - [x] Mitigation: explicit prevalidation and actionable error messaging.

## 7) Commit Strategy

- [x] Commit 1: loader + CLI plumbing + scenario runtime refactor.
  - [x] Claims schema structs and loader/validation APIs.
  - [x] Scenario CLI and runtime integration.
  - [x] Matrix CLI forwarding and prevalidation.
- [x] Commit 2: claims JSON files + tests + docs.
  - [x] Add per-scenario claims files.
  - [x] Update scenario contract and fixture tests.
  - [x] Update README usage examples.

## 8) Acceptance Criteria

- [x] All scenario binaries run without inline claim constants.
- [x] Every scenario loads claims from file by default.
- [x] `--claims-path` works as documented for file/directory use.
- [x] Matrix enforces multi-scenario file-override guard.
- [x] `cargo fmt`, `cargo clippy` (crate scope), and `cargo test` (crate scope) pass.
- [x] Single-scenario and full-matrix dry runs pass using default claim files.
