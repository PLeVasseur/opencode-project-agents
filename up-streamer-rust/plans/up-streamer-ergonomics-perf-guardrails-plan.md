# up-streamer Ergonomics + Performance Guardrails Plan

## 0) Goal and Scope

Primary goal: improve Rust ergonomics/idiomatic composition in `up-streamer` and adjacent binaries while proving no meaningful performance regression.

Secondary goal: leave behind repeatable benchmark guardrails so future ergonomic refactors remain safe.

### In scope

- Internal API ergonomics and composition quality (lifetime minimization where practical, simpler ownership boundaries, clearer layering).
- Public API compatibility-preserving ergonomic additions.
- Benchmark harness + baseline + threshold-based comparisons.
- CI/preflight guardrail integration for regressions.

### Out of scope

- Intentional public API breakage in this cycle.
- Behavior/feature changes not required for ergonomics.
- Unrelated transport functionality changes.

---

## 1) Execution Contract (for fresh sessions)

- [x] Manual execution only; no autopilot orchestration.
- [x] Pin one execution branch at session start and hard-fail on branch drift:
  - [x] require `EXEC_BRANCH` to be pre-set for the session
  - [x] hard-fail if unset: `test -n "$EXEC_BRANCH"`
  - [x] record `EXEC_BRANCH` in preflight report
  - [x] before each phase/commit: `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
- [x] Before each phase and before each commit, run:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Follow phases and gates in strict order; if a gate fails, stop progression and remediate.
- [x] Continuously update this plan; flip every completed checkbox from `[ ]` to `[x]` immediately.
- [x] Keep all assistant-generated artifacts under OPENCODE config directories only.
- [x] Before every commit, ensure no OPENCODE artifacts are staged:
  - [x] `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/'` returns no matches

### 1.1 Fresh-session quickstart commands

- [x] `export EXEC_BRANCH="<target-branch>"`
- [x] `test -n "$OPENCODE_CONFIG_DIR"`
- [x] `test -n "$EXEC_BRANCH"`
- [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
- [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data"`
- [x] `if command -v taskset >/dev/null; then export BENCH_PIN_PREFIX="taskset -c 2"; else export BENCH_PIN_PREFIX=""; fi`
- [x] `export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02"`
- [x] proceed to Phase 0 preflight, then use Phase 4.3 commands for harness smoke validation

### Artifact locations

- Plan: `$OPENCODE_CONFIG_DIR/plans/up-streamer-ergonomics-perf-guardrails-plan.md`
- Reports root: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/`
- Benchmark raw exports: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/`
- Smoke reports root (plan-unique): `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/`

### Evidence requirements (all reports)

Every evidence entry must include:

- exact command
- working directory (if not repo root)
- exit status/pass-fail
- key output lines proving result
- concise conclusion

---

## 2) Performance Guardrail Policy (Criterion)

### 2.1 Framework decision (fixed)

- [x] Criterion is the required benchmark framework and performance gate for this plan.
- [x] Optional profilers (`perf`, flamegraph, allocator profilers) are diagnostic-only, not merge gates.

### 2.2 Fixed benchmark surface

- [x] Required benchmark target: `up-streamer/benches/streamer_criterion.rs`
- [x] Required benchmark groups (exact names):
  - [x] `routing_lookup`
  - [x] `publish_resolution`
  - [x] `ingress_registry`
  - [x] `egress_forwarding`
- [x] Required benchmark IDs (exact names):
  - [x] `routing_lookup/exact_authority`
  - [x] `routing_lookup/wildcard_authority`
  - [x] `publish_resolution/source_filter_derivation`
  - [x] `ingress_registry/register_route`
  - [x] `ingress_registry/unregister_route`
  - [x] `egress_forwarding/single_route_dispatch`
- [x] Benchmarks must be deterministic and in-process (no broker/router/network dependency).

### 2.3 Canonical criterion arguments (fixed)

- [x] `export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02"`

### 2.4 Canonical benchmark commands (fixed)

- [x] Baseline run:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_baseline`
- [x] Candidate snapshot run:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline <phase_candidate>`
- [x] Optional human-readable comparison output capture (non-gating):
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --baseline ergonomics_baseline --output-format bencher | tee "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/criterion-compare-bencher.txt"`
- [x] Threshold gate command (CLI added in Phase 1):
  - [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate <phase_candidate> --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/criterion-guardrail.json"`

### 2.5 Regression thresholds (fixed)

- [x] Throughput regression must be <= 3%
- [x] p95 latency regression must be <= 5%
- [x] Allocation-sensitive proxy regression must be <= 5%

### 2.6 Pass/fail and flakiness policy (fixed)

- [x] A gate fails when `criterion-guardrail` exits non-zero.
- [x] On first threshold breach for a phase candidate, rerun compare once using `<phase_candidate>_rerun`.
- [x] Rerun commands (exact):
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline <phase_candidate>_rerun`
  - [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate <phase_candidate>_rerun --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/<phase_candidate>-guardrail-rerun.json"`
- [x] Gate passes only if rerun is within thresholds; otherwise gate fails and progression stops.

### 2.7 Benchmark discipline

- [x] Use release benchmarks only (`cargo bench`).
- [x] Keep command args and fixture sizes identical between baseline and candidate runs.
- [x] Do not modify source between baseline and candidate runs for one comparison cycle.
- [x] Stabilize execution environment before benchmark cycles:
  - [x] if available, set `export BENCH_PIN_PREFIX="taskset -c 2"`; otherwise set `export BENCH_PIN_PREFIX=""`
  - [x] if available and permitted, set CPU governor to `performance`
- [x] Prefix every `cargo bench` benchmark command in this plan with `$BENCH_PIN_PREFIX`.
- [x] Record environment snapshot each benchmark cycle:
  - [x] `rustc -Vv`
  - [x] `cargo -V`
  - [x] `lscpu`
  - [x] `date -Is`

### 2.8 Missing prerequisite policy

- [x] After Phase 1 introduces the CLI, if `cargo run -p criterion-guardrail -- --help` fails, stop and record blocker with remediation.
- [x] If benchmark pinning/governor commands are unavailable, continue only with constrained-run notation in report.
- [x] If Criterion bench execution is blocked by environment constraints, stop and record blocker with concrete remediation.
- [x] Do not proceed to ergonomics phases without at least one valid Criterion baseline.

### 2.9 Guardrail metric extraction rules (fixed)

- [x] `criterion-guardrail` must read baseline/candidate `raw.csv` files (stable Criterion output), not private JSON internals.
- [x] For each benchmark ID, compute candidate and baseline metric as median of `sample_measured_value / iteration_count` (ns/iter).
- [x] Group-to-threshold mapping:
  - [x] throughput-sensitive groups: `egress_forwarding`, `ingress_registry` -> 3%
  - [x] latency-sensitive groups: `routing_lookup`, `publish_resolution` -> 5%
  - [x] allocation-proxy benchmark IDs: `routing_lookup/wildcard_authority`, `publish_resolution/source_filter_derivation` -> 5%
- [x] Regression formulas (fixed):
  - [x] latency/alloc proxy: `delta_pct = ((candidate_ns - baseline_ns) / baseline_ns) * 100`; fail if `delta_pct > threshold`
  - [x] throughput: `baseline_ops = 1e9 / baseline_ns`, `candidate_ops = 1e9 / candidate_ns`, `delta_pct = ((baseline_ops - candidate_ops) / baseline_ops) * 100`; fail if `delta_pct > threshold`
- [x] Any required benchmark ID missing in either baseline or candidate is a hard fail.
- [x] CLI must emit both human-readable summary and JSON report artifact.

### 2.10 Rust CLI design (fixed)

- [x] Create workspace crate: `utils/criterion-guardrail` with package name `criterion-guardrail`.
- [x] Compatibility contract:
  - [x] guardrail supports the pinned Criterion version configured in `up-streamer/Cargo.toml`
  - [x] if detected CSV/header layout is unsupported, guardrail exits non-zero with remediation message
- [x] CLI contract:
  - [x] `criterion-guardrail --criterion-root <path> --baseline <name> --candidate <name> --throughput-threshold-pct <f64> --latency-threshold-pct <f64> --alloc-proxy-threshold-pct <f64> --report <path>`
  - [x] exits `0` when all checks pass, non-zero on threshold breach or malformed/missing input
  - [x] prints concise table to stdout (bench id, baseline value, candidate value, delta%, threshold, pass/fail)
- [x] Parsing contract:
  - [x] discover all benchmark directories under `<criterion-root>`
  - [x] read named baseline CSV from supported layouts:
    - [x] `<bench>/<name>/raw.csv`
    - [x] `<bench>/<name>/new/raw.csv` (fallback layout)
  - [x] validate expected CSV header columns before parse
  - [x] compute per-benchmark median ns/iter and derived throughput where applicable
- [x] Reporting contract:
  - [x] write JSON report to `--report` with per-benchmark results + aggregate pass/fail
  - [x] include threshold values and timestamp in report payload
- [x] Error contract:
  - [x] actionable error messages for missing baseline/candidate directories
  - [x] actionable error messages for parse failures and schema mismatches
  - [x] actionable error when required benchmark IDs are missing in either side

---

## 3) Phase 0 - Fresh Session Preflight

- [x] Verify env/artifact roots:
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data"`
- [x] Capture repo baseline:
  - [x] `test -n "$EXEC_BRANCH"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH"`
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git log --oneline -n 12`
- [x] Tooling sanity:
  - [x] `command -v cargo`
  - [x] `command -v rg`
  - [x] `command -v taskset || true`
- [x] Write preflight evidence report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/00-preflight.md`

### Gate P0

- [x] Preflight complete; artifacts and toolchain ready.

---

## 4) Phase 1 - Build Benchmark Foundation (before ergonomics edits)

### 4.1 Harness creation

- [x] Add Criterion benchmark scaffolding under `up-streamer/benches/`.
- [x] Add `up-streamer/benches/streamer_criterion.rs` with required group names:
  - [x] routing wildcard/subscriber lookup hot path
  - [x] publish source filter derivation
  - [x] ingress register/unregister path (mocked transport)
  - [x] egress forwarding loop (mocked transport)
- [x] Add Criterion dev-dependency and benchmark target wiring in `up-streamer/Cargo.toml`.
- [x] Pin Criterion crate version for harness/CLI compatibility and record the pinned version.
- [x] Add workspace member `utils/criterion-guardrail` in root `Cargo.toml`.
- [x] Ensure deterministic inputs/fixtures and bounded benchmark durations.
- [x] Ensure each group has stable fixture sizes and no I/O/network dependencies.

### 4.2 Baseline/compare command contract

- [x] Add benchmark helper script:
  - [x] `scripts/bench_streamer_criterion.sh` with subcommands `baseline`, `candidate`, `export`
  - [x] script must run the exact canonical commands defined in Section 2.4
  - [x] script is orchestration-only (no threshold logic)
- [x] Add threshold evaluator CLI:
  - [x] implement Rust CLI crate `criterion-guardrail`
  - [x] CLI reads Criterion output under `target/criterion`
  - [x] CLI enforces thresholds from Section 2.5 and exits non-zero on failure
  - [x] CLI supports group mapping via explicit constants/config in crate source
  - [x] CLI writes JSON artifact payload compatible with report requirements
  - [x] CLI includes unit tests for parse success, missing files, threshold breach, and pass case
  - [x] CLI includes fixture-based parser tests using checked-in Criterion sample trees
  - [x] CLI includes schema/header compatibility tests for supported Criterion layout(s)
- [x] Responsibility split is explicit in docs:
  - [x] helper script runs benches and names baselines
  - [x] `criterion-guardrail` alone decides pass/fail thresholds
- [x] Document benchmark + CLI usage in repo docs (`README` or `up-streamer/README` section).

### 4.3 Validation for harness

- [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_smoke_base` runs successfully.
- [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_smoke_candidate` runs successfully.
- [x] `cargo run -p criterion-guardrail -- --help` runs successfully.
- [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_smoke_base --candidate ergonomics_smoke_candidate --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/01-guardrail-smoke.json"` passes.
- [x] Benchmark outputs are generated under `target/criterion` and parseable by guardrail CLI.

### 4.4 Reports

- [x] Write harness evidence report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/01-benchmark-harness.md`

### Commit Stage A (harness only)

- [x] Stage only benchmark/harness files.
- [x] Ensure no OPENCODE artifact paths are staged.
- [x] Before commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit A created with scope: Criterion harness + `criterion-guardrail` CLI foundation only.
- [x] Run `git status --short --branch` and record post-commit state.

### Gate 1

- [x] Benchmark harness exists and is runnable before ergonomics changes.

---

## 5) Phase 2 - Capture Performance Baseline

- [x] `export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02"`
- [x] Run baseline command:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_baseline`
- [x] Optional baseline bencher capture for report readability (non-gating):
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --output-format bencher | tee "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/criterion-baseline-bencher.txt"`
- [x] Save baseline artifacts under:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/baseline/`
  - [x] copy relevant `target/criterion/**/ergonomics_baseline` directories into baseline artifact root
- [x] Record environment details:
  - [x] `rustc -Vv`
  - [x] `cargo -V`
  - [x] CPU/model info (e.g., `lscpu`)
- [x] Write baseline report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/02-baseline.md`

### Gate 2

- [x] Baseline locked and referenced for all later comparisons.

---

## 6) Phase 3 - Ergonomics Slice A (API ergonomics, compatibility preserved)

### 6.1 API strategy

- [x] Keep existing owned route APIs intact.
- [x] Add borrowed ergonomic APIs with fixed signatures:
  - [x] `pub async fn add_route_ref(&mut self, in_ep: &Endpoint, out_ep: &Endpoint) -> Result<(), UStatus>`
  - [x] `pub async fn delete_route_ref(&mut self, in_ep: &Endpoint, out_ep: &Endpoint) -> Result<(), UStatus>`
- [x] Delegate owned APIs to borrowed APIs without semantic changes.
- [x] Update internal call paths to prefer borrowed forms where ownership is not needed.

### 6.2 Candidate touch points

- [x] Must-touch:
  - [x] `up-streamer/src/ustreamer.rs`
  - [x] `configurable-streamer/src/main.rs` call sites
- [ ] May-touch:
  - [ ] docs/examples where internal duplication can be reduced
  - [ ] `up-streamer/src/lib.rs` docs snippets (if signatures/examples change)

### 6.3 Correctness + perf checks

- [x] Run targeted tests for API behavior and routing contracts:
  - [x] `cargo test -p up-streamer --test api_contract_forwarding_rules`
  - [x] `cargo test -p up-streamer --test usubscription`
  - [x] `cargo test -p up-streamer --test single_local_single_remote`
- [x] Run candidate benchmark snapshot:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_a`
- [x] Run threshold gate:
  - [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_a --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/03-slice-a-guardrail.json"`
- [x] Record delta against thresholds.

### 6.4 Reports

- [x] Write report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/03-ergonomics-slice-a.md`

### Commit Stage B (API ergonomics)

- [x] Stage only Slice A files.
- [x] Ensure no OPENCODE artifact paths are staged.
- [x] Before commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit B created with scope: compatibility-preserving API ergonomics.
- [x] Run `git status --short --branch` and record post-commit state.

### Gate 3

- [x] No benchmark metric exceeds regression thresholds.
- [x] Public API compatibility preserved.

---

## 7) Phase 4 - Ergonomics Slice B (composition + lifetime simplification)

### 7.1 Composition improvements

- [x] Simplify borrowed coordinator structs where practical.
- [x] Prefer narrower lifetime scopes and simpler ownership handoff patterns.
- [x] Improve module boundaries so pieces fit with fewer ad hoc conversions.

### 7.2 Candidate touch points

- [x] Must-touch:
  - [x] `up-streamer/src/control_plane/route_lifecycle.rs`
  - [x] `up-streamer/src/routing/publish_resolution.rs`
- [x] May-touch:
  - [x] closely-related routing/control-plane internals as needed
  - [ ] `up-streamer/src/routing/mod.rs` module wiring/doc comments

### 7.3 Correctness + perf checks

- [x] Run focused unit tests for touched modules:
  - [x] `cargo test -p up-streamer route_lifecycle`
  - [x] `cargo test -p up-streamer publish_resolution`
- [x] Run candidate benchmark snapshot:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_b`
- [x] Run threshold gate:
  - [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_b --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/04-slice-b-guardrail.json"`
- [x] Record deltas and ergonomics outcomes.

### 7.4 Reports

- [x] Write report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/04-ergonomics-slice-b.md`

### Commit Stage C (composition/lifetime simplification)

- [x] Stage only Slice B files.
- [x] Ensure no OPENCODE artifact paths are staged.
- [x] Before commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit C created with scope: composition + lifetime ergonomics.
- [x] Run `git status --short --branch` and record post-commit state.

### Gate 4

- [x] No benchmark metric exceeds regression thresholds.
- [x] Behavior parity confirmed.

---

## 8) Phase 5 - Ergonomics Slice C (async + ownership hygiene)

### 8.1 Async ergonomics/hygiene

- [x] Remove lock-held-across-`.await` patterns in touched paths.
- [x] Narrow mutex guard scope and use two-phase state transitions where needed.

### 8.2 Error ergonomics

- [x] Replace production `unwrap/expect` in touched runtime/binary paths with explicit errors.
- [x] Preserve existing behavior and error mapping semantics.

### 8.3 Candidate touch points

- [x] Must-touch:
  - [x] `up-streamer/src/data_plane/ingress_registry.rs`
  - [x] `configurable-streamer/src/main.rs`
- [ ] May-touch:
  - [ ] adjacent touched runtime code as required
  - [ ] `up-streamer/src/data_plane/ingress_listener.rs`
  - [ ] `up-streamer/src/data_plane/egress_pool.rs`

### 8.4 Correctness + perf checks

- [x] Run targeted tests for concurrency/routing correctness:
  - [x] `cargo test -p up-streamer ingress_registry`
  - [x] `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules`
  - [x] `cargo test -p configurable-streamer`
- [x] Run candidate benchmark snapshot:
  - [x] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_c`
- [x] Run threshold gate:
  - [x] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_c --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/05-slice-c-guardrail.json"`
- [x] Record deltas and any contention-related improvements.

### 8.5 Reports

- [x] Write report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/05-ergonomics-slice-c.md`

### Commit Stage D (async + error ergonomics)

- [x] Stage only Slice C files.
- [x] Ensure no OPENCODE artifact paths are staged.
- [x] Before commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit D created with scope: async/ownership and error-path ergonomics.
- [x] Run `git status --short --branch` and record post-commit state.

### Gate 5

- [x] No benchmark metric exceeds regression thresholds.
- [x] Concurrency correctness preserved.

---

## 9) Phase 6 - Optional Slice D (higher-risk internals, only if needed)

Execute only if prior phases indicate ergonomics debt remains in queue/message topology.

- [x] Evaluate queue topology ergonomics changes (e.g., broadcast vs single-consumer semantics).
- [x] Implement only if behavior parity and measurable non-regression are demonstrable.
- [ ] Re-run full benchmark matrix and compare to baseline:
  - [ ] `$BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_d`
  - [ ] `cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_d --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/06-slice-d-guardrail.json"`
- [ ] Write optional report:
  - [ ] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/06-optional-topology.md`

### Commit Stage E (optional)

- [ ] Stage only optional-slice files.
- [ ] Ensure no OPENCODE artifact paths are staged.
- [ ] Before commit, run and record:
  - [ ] `git rev-parse --abbrev-ref HEAD`
  - [ ] `git status --short --branch`
  - [ ] `git diff --name-only --cached`
  - [ ] `git diff --stat --cached`
- [ ] Commit E created (only if Phase 6 executed).
- [ ] Run `git status --short --branch` and record post-commit state.

### Gate 6

- [x] Optional changes only land if thresholds and behavior gates pass.

---

## 10) Phase 7 - Validation Matrix + Guardrails Integration

### 10.1 Required validation

- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### 10.2 CI parity matrix (from project instructions)

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] Unbundled matrix when `VSOMEIP_INSTALL_PATH` available:
  - [x] verify/install path
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] if unavailable, record constrained skip + remediation

### 10.3 Mandatory smoke validation

- [x] Prepare and record smoke prerequisites:
  - [x] `source build/envsetup.sh highest`
  - [x] start MQTT broker: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
  - [x] ensure SOME/IP runtime libs are available on `LD_LIBRARY_PATH` for SOME/IP scenarios
  - [x] run each scenario from the working directory/config expected by that skill
- [x] Run each smoke skill and write scenario evidence under `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/`:
  - [x] Skill: `transport-smoke-validation`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/transport-smoke-validation.md`
  - [x] Skill: `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
  - [x] Skill: `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
  - [x] Skill: `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
  - [x] Skill: `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
  - [x] Skill: `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
  - [x] Skill: `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
  - [x] Skill: `smoke-zenoh-someip-rr-zenoh-client-someip-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
  - [x] Skill: `smoke-zenoh-someip-rr-someip-client-zenoh-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`
- [x] Record command/output evidence and pass/fail conclusion for each scenario report above.
- [x] If any scenario is blocked by missing external prerequisites, record constrained skip + concrete remediation in that scenario report.

### 10.4 Guardrails wiring

- [x] Add/update developer-facing benchmark guardrail docs/commands.
- [x] Add/update check target that invokes `criterion-guardrail` for baseline-vs-candidate comparison.
- [x] Add a reproducible local command entry point (e.g., `scripts/bench_streamer_criterion.sh`).
- [x] Add CI advisory step that runs criterion guardrail and uploads JSON/text artifacts.
- [x] Guardrail mode policy:
  - [x] local execution for this plan is hard-fail on threshold breach
  - [x] CI integration is advisory-first (report + warning) until runner-noise baseline is characterized
  - [ ] promotion criteria from advisory to hard-fail are explicitly met:
    - [ ] at least 20 consecutive CI runs produce complete guardrail artifacts
    - [ ] unchanged-commit replay shows <= 5% false-positive alerts
    - [ ] p95 per-benchmark run-to-run variance is <= 2% on CI runners
  - [x] document promotion decision and date in validation report

### 10.5 Reports

- [x] Write validation + guardrail report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/07-validation-and-guardrails.md`

### Commit Stage F (guardrails/docs/integration)

- [x] Stage only guardrail/doc/integration files.
- [x] Ensure no OPENCODE artifact paths are staged.
- [x] Before commit, run and record:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
- [x] Commit F created with scope: guardrails and integration.
- [x] Run `git status --short --branch` and record post-commit state.

### Gate 7

- [x] Validation matrix passes (or constrained skips documented with remediation).
- [x] Mandatory smoke validation scenarios are completed (or constrained skips documented with remediation).
- [x] Benchmark guardrail process is operational.

---

## 11) Phase 8 - Finalization

- [x] Verify plan checklist is fully updated.
- [x] Write final summary report:
  - [x] `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/08-final-summary.md`
- [x] Final summary must include:
  - [x] phase/gate completion status
  - [x] commit list (hash + subject + scope)
  - [x] ergonomics outcomes (composition/lifetimes/API ergonomics)
  - [x] benchmark outcomes vs baseline (with thresholds)
  - [x] validation outcomes (fmt/clippy/check/test/CI parity)
  - [x] mandatory smoke validation outcomes (all scenarios)
  - [x] accepted deviations and rationale

### Gate 8

- [x] Plan complete, reproducible in fresh session, and ready for execution handoff.

---

## 12) Success Criteria

- [x] Ergonomics and idiomatic composition improved in targeted modules.
- [x] Public API compatibility preserved while adding more ergonomic call paths.
- [x] No benchmark metric exceeds agreed regression thresholds.
- [x] Criterion benchmark harness and guardrail CLI are the canonical regression mechanism.
- [x] Benchmark baseline and guardrail workflow exist for future refactors.
- [x] Validation, CI parity, and mandatory smoke checks pass (or constrained skips documented).
