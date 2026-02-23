# Search Regression Before/After Drift Plan

## Objective

- [ ] Add a deterministic regression workflow that runs in one repo/worktree.
  - [ ] Detect lexical retrieval regressions.
  - [ ] Detect semantic/hybrid retrieval regressions.
  - [ ] Detect benchmarked wall-clock and latency drift.
  - [ ] Emit a single compare report under `.cache/` for commit gating.
  - [ ] Support two execution modes: `lite` and `full`.

- [ ] Remove dependence on maintaining a second git worktree for routine refactor validation.
  - [ ] Capture `before` and `after` snapshots in an isolated artifact layout.
  - [ ] Compare snapshots with fixed thresholds and deterministic rules.
  - [ ] Make `full` mode the default for large refactor phases.

## Scope

- [ ] In scope
  - [ ] Snapshot capture tooling for `before` and `after` phases.
  - [ ] Deterministic comparison tooling and gate status output.
  - [ ] Drift reporting for lexical, semantic, and benchmark performance dimensions.

- [ ] Out of scope
  - [ ] Changing query ranking behavior as part of this tooling work.
  - [ ] Retuning quality thresholds/check logic in validate.
  - [ ] CI wiring beyond local scripts (can be a follow-up).

## Artifact Layout

- [ ] Standardize regression artifact tree under `.cache/iso26262/regression/<run_id>/`.
  - [ ] `before/`
    - [ ] `capture_manifest.json`
    - [ ] `quality_report_quick_stageb.json`
    - [ ] `quality_report_full_stageb.json`
    - [ ] `search_snapshot_lexical.jsonl`
    - [ ] `search_snapshot_semantic.jsonl`
    - [ ] `benchmark_quick.json`
  - [ ] `after/`
    - [ ] `capture_manifest.json`
    - [ ] `quality_report_quick_stageb.json`
    - [ ] `quality_report_full_stageb.json`
    - [ ] `search_snapshot_lexical.jsonl`
    - [ ] `search_snapshot_semantic.jsonl`
    - [ ] `benchmark_quick.json`
  - [ ] `compare/`
    - [ ] `drift_report.json`
    - [ ] `drift_report.md`
    - [ ] `gate_status.txt`

## Deterministic Capture Contract

- [ ] Fix all major inputs so `before` and `after` are comparable.
  - [ ] Use a fixed query set manifest (default: `.cache/iso26262/manifests/semantic_eval_queries.json`).
  - [ ] Sort queries by `query_id` before execution.
  - [ ] Use fixed retrieval knobs (`LEXICAL_K`, `SEMANTIC_K`, `RRF_K`, `TIMEOUT_MS`).
  - [ ] Use fixed semantic model id (default `miniLM-L6-v2-local-v1`) unless explicitly overridden.
  - [ ] Use fixed benchmark profile (`quick` by default, optional `standard`).

- [ ] Capture run environment to explain drift sources.
  - [ ] Record CPU, memory, kernel, rustc/cargo, filesystem device/type.
  - [ ] Record git `HEAD`, branch name, dirty status, and command-line args.

- [ ] Isolate state between `before` and `after` snapshots.
  - [ ] Use phase-local cache roots under snapshot folder.
  - [ ] Seed both phase cache roots from the same canonical PDF source cache.
  - [ ] Avoid shared DB/manifests between `before` and `after` runs.

## Execution Modes and Frequency

- [ ] Define two explicit regression execution modes.
  - [ ] `lite` mode (fast feedback)
    - [ ] Run compile/tests, smoke, determinism, quick Stage B, and quick benchmark.
    - [ ] Skip full-target refresh/validate unless explicitly requested.
    - [ ] Intended for intra-phase checkpoints and exploratory commits.
  - [ ] `full` mode (release confidence)
    - [ ] Run everything in `lite` plus full-target Stage A/Stage B and complete drift compare.
    - [ ] Intended for large refactors, phase completion, and pre-merge checkpoints.

- [ ] Frequency policy
  - [ ] Large refactor phases default to `full` mode for `before` and `after` capture.
  - [ ] `lite` mode is allowed between large phase boundaries for fast iteration.
  - [ ] A `full` compare is required before committing a large refactor phase bundle.
  - [ ] A `full` compare is required before final closeout/merge.

## Size-Budget Handling for This Plan

- [ ] Keep file-size budget checks explicitly non-gating while implementing regression tooling.
  - [ ] Do not split scripts/modules solely to satisfy legacy 500-line limits.
  - [ ] `scripts/check_file_size_budget.sh` is informational for this plan and does not block capture/compare implementation.
  - [ ] Prefer maintainable workflow cohesion over artificial line-count fragmentation.
  - [ ] If size-budget output is recorded, treat it as advisory (`MODE=warn`) unless policy is revised after this plan.

## Metrics and Signals to Compare

- [ ] Lexical retrieval regression signals
  - [ ] `semantic_quality.lexical_ndcg_at_10`
  - [ ] `semantic_quality.lexical_recall_at_50`
  - [ ] No new failed check IDs in Stage B report.
  - [ ] Exact-intent lexical top-1 parity for protected lexical query subset.
  - [ ] Lexical top-1 exact `chunk_id` match rate for protected lexical queries.
  - [ ] Lexical top-k overlap (`Jaccard@10`) for protected lexical queries.
  - [ ] Lexical no-result rate and timeout rate do not regress.

- [ ] Semantic/hybrid retrieval regression signals
  - [ ] `semantic_quality.semantic_ndcg_at_10`
  - [ ] `semantic_quality.hybrid_ndcg_at_10`
  - [ ] `semantic_quality.hybrid_recall_at_50`
  - [ ] `semantic_quality.hybrid_mrr_at_10_first_hit`
  - [ ] `semantic_quality.citation_parity_top1`
  - [ ] Citation parity top-3 containment and page-range parity.
  - [ ] `semantic_quality.retrieval_determinism_topk_overlap`
  - [ ] `semantic_quality.pinpoint_determinism_top1`
  - [ ] Semantic/hybrid top-1 exact `chunk_id` match rate on protected semantic queries.
  - [ ] Semantic/hybrid top-k overlap (`Jaccard@10`) and optional rank correlation (`Kendall/Spearman`).
  - [ ] Fallback-used rate and fallback-reason distribution do not regress unexpectedly.
  - [ ] Candidate count distribution drift (`lexical_candidate_count`, `semantic_candidate_count`, `fused_candidate_count`).

- [ ] Performance drift signals (from benchmark report)
  - [ ] `overall.valid` must remain true.
  - [ ] `timed_failure_count` must not increase.
  - [ ] Per mode (`lexical`, `semantic`, `hybrid`): compare `latency_ms.p50/p95/mean/p99`.
  - [ ] Per mode (`lexical`, `semantic`, `hybrid`): compare `wall_ms.p50/p95/mean/p99`.
  - [ ] Compare end-to-end capture phase runtime (`before` vs `after`) for major drift.

## Protected Query Set Definition

- [ ] Define fixed query subsets used by regression gates.
  - [ ] Lexical protected set manifest (exact-intent and citation-sensitive prompts).
  - [ ] Semantic/hybrid protected set manifest (conceptual prompts with judged sets).
  - [ ] Benchmark query manifest remains fixed per profile.

- [ ] Query-set governance
  - [ ] Sort all subsets by `query_id` before execution.
  - [ ] Version each subset manifest and track ownership for edits.
  - [ ] Require explicit changelog notes when adding/removing protected queries.
  - [ ] Do not modify query subsets in the same commit as refactor validation evidence unless explicitly intended.

## Drift Policy (Initial Defaults)

- [ ] Hard-fail regressions
  - [ ] Any new failed check ID appears in Stage B report.
  - [ ] Determinism fields expected at `1.0` drop below `1.0`.
  - [ ] Citation top-1 parity regresses.
  - [ ] Benchmark `overall.valid` becomes false.
  - [ ] Top-1 exact match rate for protected sets drops below configured floor.
  - [ ] No-result rate or timeout rate increases beyond hard threshold.

- [ ] Soft-fail (warn) regressions
  - [ ] nDCG/recall/MRR drops by more than `0.005` absolute.
  - [ ] benchmark p95 drift exceeds `max(+5 ms, +10%)` for any mode.
  - [ ] fallback-used rate rises by more than `0.02` absolute.
  - [ ] top-k overlap/rank-correlation drifts outside configured tolerances.
  - [ ] candidate-count distribution drift exceeds configured tolerance.

- [ ] Override policy
  - [ ] Any hard fail blocks commit.
  - [ ] Any soft fail requires explicit rationale in `compare/drift_report.md`.
  - [ ] Override record includes approver, date, scope, and expiry condition.
  - [ ] Override approver defaults to project maintainer/repo owner unless delegated explicitly.

## Gate Semantics and Decision Rules

- [ ] Gate status precedence is explicit and deterministic.
  - [ ] `FAIL` if any hard-fail rule triggers.
  - [ ] `WARN` if no hard-fail rule triggers and one or more soft-fail rules trigger.
  - [ ] `PASS` only when no hard-fail or soft-fail rules trigger.

- [ ] Comparison semantics are explicit.
  - [ ] Use exact equality for identity fields (`check_id` sets, deterministic IDs, protected top-1 IDs where required).
  - [ ] Use configured numeric tolerances for aggregate metrics.
  - [ ] Evaluate per-mode deltas (`lexical`, `semantic`, `hybrid`) and global deltas separately.
  - [ ] Do not hide mode-specific regressions inside global averages.

## Threshold Governance

- [ ] Threshold configuration ownership is explicit.
  - [ ] Keep all numeric thresholds in `scripts/lib/regression/thresholds.json`.
  - [ ] Include threshold schema version in compare output.
  - [ ] Capture threshold file hash in `capture_manifest.json` and `drift_report.json`.

- [ ] Threshold update process is controlled.
  - [ ] Threshold changes require a dedicated commit.
  - [ ] Threshold changes require rationale with before/after examples.
  - [ ] Threshold changes are forbidden in the same commit as major refactor code moves.

## Script Implementation Plan

- [ ] Add capture script
  - [ ] Create `scripts/regression_capture.sh`.
  - [ ] Inputs:
    - [ ] `--run-id <id>`
    - [ ] `--phase before|after`
    - [ ] `--mode lite|full`
    - [ ] `--source-cache-root <path>`
    - [ ] `--output-root <path>` (default `.cache/iso26262/regression`)
  - [ ] Actions:
    - [ ] Create phase-local cache root and seed it from source cache.
    - [ ] Run `cargo check` and tests.
    - [ ] Run smoke and determinism checks.
    - [ ] Run quick-cycle Stage A refresh + Stage B validate and snapshot report.
    - [ ] If `--mode full`, run full-target Stage A refresh + Stage B validate and snapshot report.
    - [ ] Run benchmark (`BENCH_PROFILE=quick`) and save report path.
    - [ ] If `--mode full`, optionally run benchmark twice and keep median p95 for noise control.
    - [ ] Run lexical and semantic query sweeps into JSONL snapshots.
    - [ ] Write `capture_manifest.json` with all input knobs and paths.

- [ ] Add compare script
  - [ ] Create `scripts/regression_compare.sh`.
  - [ ] Inputs:
    - [ ] `--run-id <id>`
    - [ ] `--mode lite|full`
    - [ ] `--output-root <path>` (default `.cache/iso26262/regression`)
    - [ ] `--thresholds <path>` (optional)
  - [ ] Actions:
    - [ ] Load `before` and `after` artifacts.
    - [ ] Compute quality and benchmark deltas.
    - [ ] Compute lexical/semantic snapshot parity and top-k overlap deltas.
    - [ ] Compute no-result/timeout/fallback/candidate-count drift.
    - [ ] Apply mode-aware gate policy (`lite` omits full-target requirements, `full` requires them).
    - [ ] Emit `compare/drift_report.json` and `compare/drift_report.md`.
    - [ ] Emit `compare/gate_status.txt` with `PASS`, `WARN`, or `FAIL`.
    - [ ] Exit non-zero on `FAIL`.

- [ ] Add comparator library and thresholds
  - [ ] Add `scripts/lib/regression/compare.jq`.
  - [ ] Add `scripts/lib/regression/thresholds.json`.
  - [ ] Keep thresholds configurable without script edits.
  - [ ] Add comparator helpers for top-k overlap and rank correlation.
  - [ ] Add benchmark summarization support for `p99`.

- [ ] Add optional one-command wrapper
  - [ ] Create `scripts/regression_gate.sh`.
  - [ ] Run capture for `before`/`after` and then compare in one flow.
  - [ ] Default to `--mode full` for refactor workflows.

## Critical Safety Adjustment

- [ ] Avoid repo-dirty side effects during capture.
  - [ ] Add an embed lockfile output override for semantic model lock path.
  - [ ] Use phase-local lock path during regression capture.
  - [ ] Keep default path unchanged for normal developer workflows.
  - [ ] Ensure capture paths for run-state, manifests, and benchmark outputs stay under phase-local cache roots.
  - [ ] Ensure compare step reads only from snapshot artifacts, not mutable repo-root manifests.

- [ ] Remove branch-policy ambiguity during scripted runs.
  - [ ] Pass explicit `BASE_BRANCH` and record it in `capture_manifest.json`.
  - [ ] Record current branch and `HEAD` for `before`/`after` phases.
  - [ ] Fail fast when `before` and `after` snapshots are captured from different base commits unless explicitly allowed.

## Baseline Lifecycle and Freshness

- [ ] Baseline validity rules are explicit.
  - [ ] `before` snapshot must exist for a compare to run.
  - [ ] `before` and `after` must target the same `run_id` and schema version.
  - [ ] `before` snapshot older than configured freshness window requires explicit renewal.

- [ ] Baseline management workflow
  - [ ] `regression_capture --phase before` creates a new baseline for a refactor session.
  - [ ] A subsequent `before` capture with same `run_id` requires `--force` to replace.
  - [ ] Compare report records baseline capture timestamp and freshness status.

## Performance Noise Controls

- [ ] Control benchmark noise to reduce false positives.
  - [ ] Capture benchmark runs with stable profile and fixed query order.
  - [ ] Allow configurable repeat count in full mode (default 2) and aggregate with median for p95/p99.
  - [ ] Record raw per-run benchmark paths in capture manifest for auditability.

- [ ] Control quality metric noise
  - [ ] Keep deterministic checks mandatory (`SMOKE_DETERMINISM=1`).
  - [ ] Require explainable rationale if non-deterministic drift appears between repeated runs.

## Operator Workflow (No Worktree)

- [ ] Step 1: choose regression mode
  - [ ] Use `full` mode for large refactor phases (recommended default).
  - [ ] Use `lite` mode for intermediate local checkpoints.

- [ ] Step 2: capture `before` snapshot (pre-refactor state)
  - [ ] `scripts/regression_capture.sh --run-id <run_id> --phase before --mode <lite|full> --source-cache-root .cache/iso26262`

- [ ] Step 3: apply refactor edits in same working tree.

- [ ] Step 4: capture `after` snapshot (post-refactor state)
  - [ ] `scripts/regression_capture.sh --run-id <run_id> --phase after --mode <lite|full> --source-cache-root .cache/iso26262`

- [ ] Step 5: compare drift and gate commit
  - [ ] `scripts/regression_compare.sh --run-id <run_id> --mode <lite|full>`
  - [ ] Review `compare/drift_report.md`.
  - [ ] Commit only on `PASS` or approved `WARN` rationale.
  - [ ] Require `full`-mode compare before committing large refactor phase bundles.

## Rollout and Commit Sequence

- [ ] Phase 1: plumbing and side-effect controls
  - [ ] `feat(embed): support override path for semantic model lockfile`

- [ ] Phase 2: deterministic capture harness
  - [ ] `feat(regression): add before/after capture script and manifests`
  - [ ] `feat(regression): add lite/full mode controls and phase-local cache isolation`

- [ ] Phase 3: deterministic comparator and gate outputs
  - [ ] `feat(regression): add drift comparator and gate status artifacts`
  - [ ] `feat(regression): add top-k overlap and rank-correlation drift checks`

- [ ] Phase 4: query-set and threshold governance
  - [ ] `chore(regression): add protected lexical/semantic query manifests`
  - [ ] `chore(regression): add threshold versioning and schema metadata`

- [ ] Phase 5: docs and operationalization
  - [ ] `docs(scripts): document regression capture and compare workflow`
  - [ ] `chore(plan): reference regression gate flow from modularization plan`

## Final Calibration Step (One-Time)

- [ ] Run one-time calibration to prove the quality comparison catches intentional regressions.
  - [ ] Keep this as a temporary validation campaign, not a permanent canary framework.
  - [ ] Run calibration in `full` mode only.

- [ ] Calibration scenario A: lexical degradation should fail.
  - [ ] Capture `before` snapshot in `full` mode.
  - [ ] Apply a temporary lexical ranking degradation in query code.
  - [ ] Capture `after` snapshot in `full` mode and run compare.
  - [ ] Confirm gate status is `FAIL` and lexical drift signals are triggered.
  - [ ] Revert temporary degradation.

- [ ] Calibration scenario B: semantic/hybrid degradation should fail.
  - [ ] Capture fresh `before` snapshot in `full` mode.
  - [ ] Apply a temporary semantic/hybrid degradation in query code.
  - [ ] Capture `after` snapshot in `full` mode and run compare.
  - [ ] Confirm gate status is `FAIL` and semantic/hybrid drift signals are triggered.
  - [ ] Revert temporary degradation.

- [ ] Calibration scenario C: performance degradation should warn/fail.
  - [ ] Capture fresh `before` snapshot in `full` mode.
  - [ ] Apply a temporary fixed-latency overhead in query path.
  - [ ] Capture `after` snapshot in `full` mode and run compare.
  - [ ] Confirm benchmark drift thresholds trigger `WARN` or `FAIL` as configured.
  - [ ] Revert temporary degradation.

- [ ] Calibration evidence and closure.
  - [ ] Save calibration run IDs and compare report paths under `.cache/iso26262/regression/`.
  - [ ] Add a short summary of observed vs expected gate outcomes.
  - [ ] Require clean tree verification after all temporary degradations are reverted.
  - [ ] Mark calibration complete before treating regression gate as trusted for large refactors.

## New Session Reliability Addendum

- [ ] Session bootstrap checklist is explicit and mandatory.
  - [ ] Confirm toolchain availability (`cargo`, `jq`, benchmark helper dependencies).
  - [ ] Confirm free disk headroom before capture (cache and benchmark artifacts can be large).
  - [ ] Confirm canonical source cache root and PDF corpus path.
  - [ ] Confirm selected mode (`lite` or `full`) and intended scope for this session.
  - [ ] Generate and record a unique `run_id` before first capture.

- [ ] Mode selection matrix is documented for quick decisions.
  - [ ] Use `lite` for small/local checkpoints where query behavior is not materially changed.
  - [ ] Use `full` for any large refactor phase, query/retrieval/ranking changes, or commit gating.
  - [ ] Require `full` before phase completion and before merge/closeout.

- [ ] Compare script exit-code contract is fixed.
  - [ ] `PASS` exits `0`.
  - [ ] `WARN` exits `10` (non-blocking with explicit acknowledgement requirement).
  - [ ] `FAIL` exits `20` (blocking).
  - [ ] Exit-code meanings are documented in script help and `drift_report.md`.

- [ ] Failure triage playbook is included.
  - [ ] New failed check IDs: stop, inspect stage report deltas, and block commit.
  - [ ] Determinism regressions: rerun once to rule out noise; if persistent, block commit.
  - [ ] Performance-only drift: classify as `WARN` or `FAIL` per threshold and capture rationale.
  - [ ] Pre-existing red checks: verify strict no-worsening before proceeding.

- [ ] Artifact retention and cleanup policy is defined.
  - [ ] Keep latest N run folders by default (for example 10) and prune older runs.
  - [ ] Keep all runs referenced by active refactor phases until closeout.
  - [ ] Provide a script-assisted cleanup path that never deletes the current run.

- [ ] Comparator self-tests and schema guards are required.
  - [ ] Add fixture-based tests for comparator logic and threshold application.
  - [ ] Add schema compatibility guardrails with actionable errors when required fields are missing.
  - [ ] Fail fast when report schema version is unsupported.

- [ ] Session handoff template is standardized.
  - [ ] Include `run_id`, mode, and overall gate status.
  - [ ] Include top drift deltas (quality + performance).
  - [ ] Include override record reference (if any) and expiry.
  - [ ] Include exact next action and required command.

## Definition of Done

- [ ] `before` and `after` snapshots are reproducible in one working tree.
  - [ ] No second worktree required.
  - [ ] No accidental loss of uncommitted refactor work.
  - [ ] `lite` and `full` modes are both implemented and documented.

- [ ] Drift report is complete and deterministic.
  - [ ] Lexical regression section present.
  - [ ] Semantic/hybrid regression section present.
  - [ ] Wall-clock/latency regression section present.
  - [ ] Report includes explicit mode, threshold version, and gate-rule trace.

- [ ] Commit gate is clear and enforceable.
  - [ ] `gate_status.txt` produced for every run.
  - [ ] Hard-fail and soft-fail policies are applied consistently.
  - [ ] Override records include approver, rationale, and expiry.

- [ ] One-time calibration campaign has been completed successfully.
  - [ ] Intentional lexical and semantic degradations are detected as `FAIL`.
  - [ ] Intentional performance degradation is detected as `WARN`/`FAIL` per policy.
  - [ ] All temporary degradation code is removed and repository state is clean.
