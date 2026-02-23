# CI Strictness-Preserving Latency Follow-Up Plan (Session-Handoff Grade)

## 0) Purpose and Success Definition

This plan is for execution in a new session, on top of the existing PR branch:

- Branch: `perf/ci-pr-latency-reduction`
- PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/76

Primary goal:

- Reduce CI latency further **without reducing strictness signal** and without renaming required checks.

Success means all are true:

- Required checks unchanged and green:
  - Bundled: `Lint`, `Test`, `Build documentation`
  - Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- Bundled lint still preserves the spirit of the bundled path:
  - `vsomeip` build/compile signal remains part of bundled lint feature validation
  - no dilution of strict clippy policy (`-W warnings -D warnings`)
- Unbundled `Lint` regression is investigated with evidence and mitigated if safe
- Any bundled `Lint` aggregator simplification is branch-protection-safe and deterministic
- No cache contention regressions (`Unable to reserve cache` absent)
- Measured timing evidence is captured with run URLs and before/after tables

## 1) Current Evidence Snapshot (Starting Point)

Historical baseline reference:

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569522
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569519
- Timings baseline: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569523

Latest post-Phase-D reference at head `9578b4d`:

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327
  - Stability rerun (attempt 2): https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327/attempts/2
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749323
- Timings profile: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749332

Known observations to validate/improve:

- OpenSSL vendored bottleneck mitigation succeeded (~0.1s `openssl-sys build script (run)` in latest timings)
- Bundled feature remains dominated by `vsomeip-sys build script (run)` (expected)
- Unbundled `Lint` shows regression vs historical baseline and needs root-cause investigation
- Bundled `Lint` currently uses internal shards plus required-check aggregator; simplification is desired only if signal-safe

## 2) Hard Constraints and Non-Goals

### Constraints

- Keep one branch and one PR (no branch split, no additional PR)
- CI/workflow/docs scope only; no runtime behavior changes
- Preserve required check names exactly (do not rename)
- Preserve branch-protection signal
- Keep one-writer rust-cache policy unless a phase explicitly trials a change with rollback
- Do not squash or amend unless explicitly requested
- Treat `eclipsefdn/eca` as external blocker unless commit metadata evidence points otherwise

### Bundled strictness constraint (explicit)

- Do not remove bundled feature validation intent:
  - bundled feature lint must continue validating with feature set
    `vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - evidence must show `vsomeip` compile/build signal is still exercised in bundled lint path

### Non-goals

- Eliminating bundled `vsomeip-sys` heavy compile cost entirely (likely intrinsic)
- Runtime refactors or cargo feature-model redesigns beyond CI workflow scope

## 3) Execution Phases (Run In Order)

### Phase A - Preflight, Baseline Freeze, and Variance Control

- [x] Confirm branch and PR head state:
  - `git status --short --branch`
  - `gh pr view 76 --repo eclipse-uprotocol/up-streamer-rust --json headRefOid,statusCheckRollup,url`
- [x] Confirm required check names currently visible in status rollup
- [x] Freeze baseline durations for this follow-up wave:
  - Bundled: `Lint`, `Test`
  - Unbundled: `Lint`, `Test`
- [x] Capture at least one rerun sample for bundled and unbundled workflows to reduce one-run noise
- [x] Confirm current cache policy still one-writer-per-workflow

Acceptance gate:

- [x] Stop if required check names are missing/renamed or if bundled feature lint signal is already diluted

---

### Phase B - Investigate and Mitigate Unbundled `Lint` Regression

Goal: explain and reduce unbundled `Lint` latency regression without weakening validation.

- [x] Build step-level timing diff for unbundled `Lint`:
  - historical baseline run (`21781569519`)
  - latest run (`21782749323`)
  - one fresh rerun sample
- [x] Identify top contributors (setup/install vs cache restore vs compile)
- [x] Validate whether regression is persistent or variance-driven
- [x] Implement one minimal, high-confidence mitigation if warranted (CI-only)
- [x] Push and validate required checks
- [ ] If mitigation fails or regresses signal/stability, rollback immediately

Acceptance gate:

- [x] Unbundled `Lint` signal unchanged and timing evidence captured

Rollback trigger:

- [ ] Any required-check failure or evidence of reduced lint coverage

---

### Phase C - Branch-Protection-Safe Bundled `Lint` Aggregator Simplification

Goal: simplify bundled `Lint` orchestration if possible, without weakening the bundled-vsomeip lint spirit.

- [x] Document current aggregator semantics and failure behavior (`always()` + explicit result checks)
- [x] Define at most 1 simplification trial with explicit safety criteria
- [x] Preserve required check name `Lint` and deterministic non-skipped behavior
- [x] Preserve strict clippy policy and bundled feature signal
- [x] Verify logs show `vsomeip` compile/build signal in bundled lint feature shard
- [x] Push and validate bundled/unbundled required checks
- [x] Run one additional bundled rerun for stability proof

Acceptance gate:

- [x] `Lint` remains required-name-compatible, deterministic, and strict
- [x] No loss of bundled-vsomeip lint signal

Rollback trigger:

- [ ] Any ambiguity in branch-protection behavior, skipped `Lint`, or coverage reduction

---

### Phase D - Optional Narrow Optimization (Only If Needed)

Execute only if Phases B-C leave meaningful ROI on the table.

Decision in this run:

- Skipped; remaining variance appears environment-driven, and no additional high-confidence, strictly-safe optimization showed clear ROI.

- [ ] Trial one narrow, reversible CI optimization
- [ ] Require measured gain with no signal regression
- [ ] Revert immediately on mixed/unstable results

## 4) Validation Checklist (After Each Phase Push)

- [x] Required checks triggered and completed
- [x] Required check names unchanged
- [x] `Unable to reserve cache` absent
- [x] No `unable to find library -lvsomeip3` in bundled lint feature logs
- [x] For timing phases, collect run URLs and durations for bundled/unbundled `Lint` + `Test`

Useful command:

- `gh run view <run_id> --log | rg -n "Unable to reserve cache|unable to find library -lvsomeip3"`

## 5) Reporting and Deliverables

Write report artifact under:

- `$OPENCODE_CONFIG_DIR/reports/ci-strictness-preserving-latency-followup-report.md`

Required report content:

- [x] Commit list (hash + subject)
- [x] PR URL
- [x] Before/after timing comparison table
- [x] Confirmation required check names stayed intact
- [x] Cache behavior summary (writer vs restore-only jobs; contention status)
- [x] Bottleneck summary and follow-up opportunities not included

Before/after table template:

| Workflow | Job | Before (s) | After (s) | Delta (s) | Delta (%) | Run URL (After) |
|---|---:|---:|---:|---:|---:|---|
| Bundled | Lint |  |  |  |  |  |
| Bundled | Test |  |  |  |  |  |
| Unbundled | Lint |  |  |  |  |  |
| Unbundled | Test |  |  |  |  |  |

## 6) Commit Chunk Plan

- [x] Commit A: Unbundled lint regression investigation scaffolding and/or minimal mitigation
- [x] Commit B: Bundled lint aggregator simplification (if retained)
- [ ] Commit C: Optional narrow optimization (only if executed)
- [ ] Commit D: Plan/report updates with evidence

Commit hygiene before each commit:

- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`

## 7) Rollback Order

If regression appears, revert in this order:

1. Phase D optional trial
2. Phase C aggregator simplification
3. Phase B unbundled lint mitigation

After each rollback step:

- [ ] Re-run bundled/unbundled required workflows
- [ ] Confirm required checks green and names unchanged

## 8) Session Handoff Checklist

- [x] Read this plan completely
- [x] Confirm current head SHA and latest run IDs
- [x] Execute phases in order with push + validation at each gate
- [x] Update checkboxes immediately as tasks complete
- [ ] Stop at first unexpected regression and report run URL + log proof
