# Phase 8 Final Summary

Date: 2026-02-10
Execution branch: `refactor/up-streamer-domain-architecture`

## Phase and gate completion

- Phase 0 / Gate 0: PASS (fresh-session preflight, branch pin, tool/env readiness).
- Phase 1 / Gate 1: PASS (Criterion harness + `criterion-guardrail` crate + smoke harness validation).
- Phase 2 / Gate 2: PASS (baseline captured and copied to report artifact root).
- Phase 3 / Gate 3: PASS (API ergonomics slice A, guardrail pass).
- Phase 4 / Gate 4: PASS (composition/lifetime slice B, guardrail pass).
- Phase 5 / Gate 5: PASS after mandatory rerun (slice C first breach then rerun pass).
- Phase 6 / Gate 6: PASS (optional topology evaluated; no additional topology changes landed).
- Phase 7 / Gate 7: PASS (validation matrix, CI parity, smoke scenarios, and guardrail integrations complete).
- Phase 8 / Gate 8: PASS (plan/report artifacts finalized for handoff).

## Commit list (hash + subject + scope)

- `2043298` - `feat: add Criterion harness and guardrail CLI foundation`
  - scope: `up-streamer` Criterion benches, benchmark fixtures, `utils/criterion-guardrail`, helper script, docs.
- `cae6282` - `refactor: add borrowed route APIs for ergonomic call sites`
  - scope: borrowed `add_route_ref`/`delete_route_ref` API and `configurable-streamer` call-site migration.
- `e8e5fb5` - `refactor: simplify route lifecycle and publish resolver composition`
  - scope: narrower mutable borrow scopes, stateless publish resolver composition.
- `2440388` - `refactor: narrow ingress registry locks and explicit config errors`
  - scope: lock-held-across-await removal and explicit runtime error propagation.
- `bdf3cef` - `ci: add advisory benchmark guardrail integration`
  - scope: CI advisory workflow, script guardrail subcommand, updated benchmark guardrail docs.

## Ergonomics outcomes

- API ergonomics: added borrowed route APIs while preserving existing owned public APIs.
- Composition/lifetimes: removed coordinator-owned mutable pool borrowing and converted publish resolver to stateless associated functions.
- Async/ownership ergonomics: eliminated lock-held-across-await pattern in ingress registry with race-safe two-phase updates.
- Runtime ergonomics: replaced touched runtime-path `unwrap/expect` usage in `configurable-streamer` with explicit `UStatus` propagation.

## Benchmark and threshold outcomes

- Baseline: `ergonomics_baseline` captured with pinned Criterion args and CPU pinning (`taskset -c 2`).
- Slice A (`ergonomics_candidate_slice_a`): PASS; all regressions within thresholds (worst throughput regression `+1.191%`).
- Slice B (`ergonomics_candidate_slice_b`): PASS; all regressions within thresholds (worst throughput regression `+1.978%`).
- Slice C (`ergonomics_candidate_slice_c`): first run FAIL (`ingress_registry/unregister_route` `+5.263%` > `3%` throughput threshold); rerun policy applied.
- Slice C rerun (`ergonomics_candidate_slice_c_rerun`): PASS; all regressions within thresholds (worst throughput regression `+2.123%`).
- Guardrail CLI operational check: PASS via `scripts/bench_streamer_criterion.sh guardrail ...`.

## Validation and CI parity outcomes

- Required validation: `cargo fmt -- --check`, `cargo clippy --all-targets -- -W warnings -D warnings`, `cargo check --workspace --all-targets`, `cargo test --workspace` all PASS.
- CI parity base matrix: PASS.
- CI parity bundled feature matrix: PASS.
- CI parity unbundled matrix: PASS after remediation to absolute `VSOMEIP_INSTALL_PATH` (initial relative-path include failure resolved).

## Smoke skill outcomes (mandatory scenarios)

- PASS: `transport-smoke-validation`
- PASS: `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
- PASS: `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
- PASS: `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
- PASS: `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
- PASS: `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
- PASS: `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
- PASS: `smoke-zenoh-someip-rr-zenoh-client-someip-service`
- PASS: `smoke-zenoh-someip-rr-someip-client-zenoh-service`

## Accepted deviations and rationale

- CI promotion-to-hard-fail criteria remain pending by design:
  - 20 consecutive advisory artifact runs, unchanged-commit replay false-positive characterization, and CI variance characterization are not yet available in this execution window.
  - Current mode remains advisory-first in CI (implemented), hard-fail locally (implemented), with promotion decision explicitly documented in Phase 7 report.
