# Phase 7 Validation and Guardrails Report

Date: 2026-02-10

## Evidence

1) Command: `git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture`
- Conclusion: Phase 7 executed on the pinned execution branch.

2) Command: `cargo fmt -- --check && cargo clippy --all-targets -- -W warnings -D warnings && cargo check --workspace --all-targets && cargo test --workspace`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ...` (fmt/clippy/check)
  - `test result: ok. 23 passed; 0 failed` (`up-streamer` unit tests)
  - `test result: ok. 2 passed; 0 failed` (`api_contract_forwarding_rules`)
  - `test result: ok. 1 passed; 0 failed` (integration tests)
- Conclusion: Required validation matrix (fmt/clippy/check/test) passed.

3) Command set: CI parity base + bundled + unbundled matrices
- Base commands:
  - `source build/envsetup.sh highest`
  - `cargo build`
  - `cargo clippy --all-targets -- -W warnings -D warnings`
  - `cargo fmt -- --check`
- Bundled commands:
  - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Unbundled commands:
  - first attempt with relative `VSOMEIP_INSTALL_PATH` failed (`vsomeip/vsomeip.hpp file not found`)
  - remediation: set absolute `VSOMEIP_INSTALL_PATH` from `target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install`
  - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Exit status: pass after remediation
- Key output:
  - base/bundled/unbundled builds finished successfully
  - unbundled remediation command with absolute path succeeded
- Conclusion: CI parity matrix passed; one path-resolution blocker was remediated in-session.

4) Command: smoke scenario execution and report pass-scan
- `rg -n "^## Result|^PASS" "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills"/*.md`
- Exit status: 0 (pass)
- Key output:
  - PASS markers present for all required smoke reports:
    - `transport-smoke-validation.md`
    - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
    - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
    - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
    - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
    - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
    - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
    - `smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
    - `smoke-zenoh-someip-rr-someip-client-zenoh-service.md`
- Conclusion: Mandatory smoke validation scenarios completed and documented.

5) Command: `bash -n scripts/bench_streamer_criterion.sh`
- Exit status: 0 (pass)
- Key output:
  - no syntax errors
- Conclusion: Guardrail helper script remains syntactically valid after integration updates.

6) Command: `scripts/bench_streamer_criterion.sh guardrail ergonomics_candidate_slice_c_rerun "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/07-guardrail-check.json"`
- Exit status: 0 (pass)
- Key output:
  - `criterion-guardrail: PASS`
  - JSON report written to `.../07-guardrail-check.json`
- Conclusion: Local reproducible guardrail entry point is operational and hard-fails on threshold breach by CLI exit code.

7) Integration updates (repo changes)
- Added CI advisory workflow: `.github/workflows/benchmark-guardrail-advisory.yaml`
- Updated local command entry point: `scripts/bench_streamer_criterion.sh` adds `guardrail` subcommand
- Updated developer docs: `up-streamer/README.md` includes baseline/candidate/guardrail/export command set
- Conclusion: Guardrail process is wired for local hard-fail and CI advisory artifact publishing.

8) Command: `git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `M scripts/bench_streamer_criterion.sh`
  - `M up-streamer/README.md`
  - `?? .github/workflows/benchmark-guardrail-advisory.yaml`
- Conclusion: Pre-commit F branch pin and guardrail/doc/integration scope confirmed.

9) Command: `git add .github/workflows/benchmark-guardrail-advisory.yaml scripts/bench_streamer_criterion.sh up-streamer/README.md && git diff --name-only --cached && git diff --stat --cached && git diff --name-only --cached | rg -n '^(plans|prompts|reports)/' || true`
- Exit status: 0 (pass)
- Key output:
  - staged paths limited to workflow/script/README
  - `3 files changed, 83 insertions(+), 1 deletion(-)`
  - no repo-local `plans|prompts|reports` staged
- Conclusion: Commit F staging scope is correct and artifact hygiene is preserved.

10) Command: `git commit -m "ci: add advisory benchmark guardrail integration"`
- Exit status: 0 (pass)
- Key output:
  - `[refactor/up-streamer-domain-architecture bdf3cef] ci: add advisory benchmark guardrail integration`
- Conclusion: Commit F created with guardrail/integration scope.

11) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- Conclusion: Post-commit F branch state is clean.

## Guardrail Mode Policy

- Local execution mode: hard-fail on threshold breach (`criterion-guardrail` non-zero exit).
- CI mode: advisory-first via `benchmark-guardrail-advisory.yaml` (`continue-on-error: true` on guardrail step, artifacts always uploaded).
- Promotion criteria status (as of 2026-02-10): pending accumulation of CI run history (20 consecutive artifacts, <=5% false positives on replay, <=2% p95 variance).

## Phase 7 result

PASS - Validation matrix, smoke validations, and guardrail integrations are operational.
