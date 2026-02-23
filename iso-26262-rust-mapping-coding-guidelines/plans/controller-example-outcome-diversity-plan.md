# Controller Example Outcome and Diversity Plan

This plan upgrades guideline examples from basic presence checks into outcome-driven evidence that improves clarity, diversity, and controller convergence quality.

It explicitly treats example behavior as first-class quality signal:

- compliant examples should demonstrate expected behavior (typically via assertions),
- non-compliant examples should fail in a meaningful, declared way (compile failure, lint failure, or runtime panic),
- the autonomous loop should optimize and validate those outcomes, not just markdown existence.

---

## 0) Objectives

- [ ] Require each guideline to carry executable positive and negative evidence.
- [ ] Encode expected outcomes per example (assertion pass, compile fail, panic, lint trigger, documented-only).
- [ ] Make example quality and diversity visible in controller deficits and scoring.
- [ ] Add deterministic and optional LLM-assisted actions that improve example evidence depth.
- [ ] Preserve reproducibility and fallback safety rails.

---

## 1) Current State and Gaps

### 1.1 What already exists

- [ ] Guidelines already require `examples.compliant` and `examples.non_compliant` records.
- [ ] `check_guideline_completeness.py` validates required example fields/files.
- [ ] `check_guideline_examples.py` runs rustdoc/clippy checks against examples.
- [ ] Controller observes `example_gap` and can run `upgrade_examples_non_placeholder`.

### 1.2 What is missing

- [ ] No explicit, unified outcome contract per example beyond coarse `compile_expectation`.
- [ ] No direct requirement that compliant examples prove behavior using assertions.
- [ ] Runtime panic outcomes are not first-class policy targets.
- [ ] Example checks emphasize pass/fail mechanics more than explanatory/evidence quality.
- [ ] Controller scoring gives limited emphasis to example-specific improvement quality.

---

## 2) Example Outcome Contract (Design)

### 2.1 New canonical expectation model

- [ ] Keep existing `compile_expectation` for backward compatibility.
- [ ] Add new field `examples.<side>.expected_outcome` with allowed values:
  - [ ] `assertion_pass`
  - [ ] `compile_fail`
  - [ ] `runtime_panic`
  - [ ] `lint_trigger`
  - [ ] `documented_only`
- [ ] Add optional field `examples.<side>.expected_signals` (array of substrings/regex hints) for stronger diagnostics.
- [ ] Add optional field `examples.<side>.verification_notes` for concise reviewer context.

### 2.2 Outcome semantics

- [ ] `assertion_pass`
  - [ ] Example must compile and run successfully.
  - [ ] Code should include at least one assertion (`assert!` or `assert_eq!`) unless an explicit exception reason is provided.
- [ ] `compile_fail`
  - [ ] Example must fail compilation (rustdoc compile_fail or equivalent harness behavior).
- [ ] `runtime_panic`
  - [ ] Example must compile and panic at runtime (e.g., `should_panic` or equivalent runtime harness).
- [ ] `lint_trigger`
  - [ ] Example must trigger the mapped lint for non-compliant evidence (where applicable).
- [ ] `documented_only`
  - [ ] Permitted only when automated execution is not practical; requires `verification_notes` justification.

### 2.3 Side-specific policy rules

- [ ] `examples.compliant.expected_outcome` should default to `assertion_pass` (or `documented_only` with justification).
- [ ] `examples.non_compliant.expected_outcome` should default to one of `compile_fail`, `runtime_panic`, or `lint_trigger`.
- [ ] For `decidable_status=compiler`, non-compliant should strongly prefer `compile_fail`.
- [ ] For `decidable_status=clippy`, non-compliant should strongly prefer `lint_trigger`.

---

## 3) Workstream A - Spec, Schema, and Policy Updates

### 3.1 Spec updates

- [ ] Update `docs/guideline-record-spec.md` with new `expected_outcome` contract.
- [ ] Document assertion requirement for compliant examples.
- [ ] Document acceptable negative evidence modes (compile failure, panic, lint).

### 3.2 Schema updates

- [ ] Extend guideline schema to include:
  - [ ] `expected_outcome`
  - [ ] `expected_signals`
  - [ ] `verification_notes`
- [ ] Add strict enum validation and backward-compatible migration handling.

### 3.3 Policy config

- [ ] Add/extend policy file (e.g., `config/example_quality_policy.yaml`) with:
  - [ ] allowed outcomes per side,
  - [ ] minimum assertion density,
  - [ ] `documented_only` usage threshold,
  - [ ] gate mode (`warn|error`) progression settings.

---

## 4) Workstream B - Example Execution and Evidence Validation

### 4.1 Enhance `check_guideline_examples.py`

- [ ] Evaluate behavior based on `expected_outcome`, not only `compile_expectation`.
- [ ] Support runtime panic verification path (`should_panic` or harness-based panic detection).
- [ ] Enforce assertion presence for `assertion_pass` compliant examples.
- [ ] Validate `expected_signals` against tool output where applicable.

### 4.2 New report fields

- [ ] Add per-guideline/example outcome diagnostics:
  - [ ] `expected_outcome`
  - [ ] `observed_outcome`
  - [ ] `outcome_match`
  - [ ] `assertion_present`
  - [ ] `signal_matches`
- [ ] Aggregate metrics:
  - [ ] outcome-match ratio,
  - [ ] assertion-backed compliant ratio,
  - [ ] negative-evidence strength ratio,
  - [ ] documented-only ratio.

### 4.3 Completeness guard upgrades

- [ ] Extend `check_guideline_completeness.py` to require `expected_outcome` for both sides.
- [ ] Require justification when `documented_only` is used.

---

## 5) Workstream C - Controller Observation, Deficits, and Scoring

### 5.1 Observation integration

- [ ] Extend `controller_observe.py` to ingest new example report metrics.
- [ ] Add new deficit types:
  - [ ] `example_outcome_gap` (declared vs observed mismatch),
  - [ ] `example_assertion_gap` (missing assertion evidence),
  - [ ] `example_negative_evidence_gap` (weak non-compliant mode),
  - [ ] `example_diversity_gap` (over-reused template patterns).

### 5.2 Scoring integration

- [ ] Update `controller_scoring.py` metric vector with outcome-based example metrics.
- [ ] Increase penalty for weak/placeholder example behavior even when text quality looks acceptable.
- [ ] Reward bundles that increase executable evidence diversity and determinism.

### 5.3 Lane behavior

- [ ] Keep examples in quality lane, but expose sub-metrics in lane status and final report.
- [ ] Add regression checks to block accepted candidates that worsen outcome-match ratio.

---

## 6) Workstream D - Controller Actions for Stronger Examples

### 6.1 Deterministic action upgrades

- [ ] Expand `upgrade_examples_non_placeholder` into outcome-aware rewrites.
- [ ] Add dedicated action(s):
  - [ ] `strengthen_example_assertions`
  - [ ] `convert_non_compliant_to_compile_fail_or_panic`
  - [ ] `align_example_with_decidable_status`
- [ ] Ensure action-generated examples preserve guideline scope and obligation context.

### 6.2 Topic-aware templates

- [ ] Use `technical_topic`, `fls_refs`, and `rust_signals` to produce less generic examples.
- [ ] Prefer domain-relevant examples over trivial variable assignments.
- [ ] Add anti-repetition checks for example prose and code structure.

### 6.3 Optional LLM rewrite extension

- [ ] Extend rewrite packet/schema to optionally include example payload fields.
- [ ] Require model to return example outcomes and code/prose edits with strict schema validation.
- [ ] Keep deterministic fallback for invalid or missing LLM output.

---

## 7) Workstream E - Prompt and Runbook Updates

### 7.1 Decision prompt updates

- [ ] Instruct selector to prioritize candidates improving outcome-match, assertion coverage, and negative-evidence strength.
- [ ] Explicitly prefer candidates reducing example-specific deficits.

### 7.2 Rewrite prompt updates

- [ ] Instruct rewrite stage to produce behaviorally meaningful example evidence:
  - [ ] compliant example with assertions,
  - [ ] non-compliant example with compile fail, panic, or lint trigger,
  - [ ] concise verification rationale tied to expected outcome.

### 7.3 Prompt pack versioning

- [ ] Add new prompt file under `$OPENCODE_CONFIG_DIR/prompts/` for "post-remediation + outcome-driven examples" runs.
- [ ] Keep previous prompt packs as baseline controls.

---

## 8) Testing and Validation Plan

### 8.1 Unit tests

- [ ] Outcome parser and classifier tests (`assertion_pass`, `compile_fail`, `runtime_panic`, `lint_trigger`).
- [ ] Assertion detection tests with positive/negative cases.
- [ ] Completeness tests for missing/invalid `expected_outcome` and undocumented `documented_only`.
- [ ] Controller deficit generation tests for all new example gap types.

### 8.2 Integration tests

- [ ] Run `validate_schemas` with strict generated data.
- [ ] Run example checks on representative guideline subsets:
  - [ ] one compile-fail case,
  - [ ] one should-panic case,
  - [ ] one assertion-pass case,
  - [ ] one lint-trigger case.
- [ ] Ensure orchestrate + controller observe produce expected metrics/deficits.

### 8.3 Loop validation

- [ ] Execute 20-iteration supervised session with decision+rewrite LLM enabled.
- [ ] Compare against prior baseline session(s) on:
  - [ ] example outcome-match ratio,
  - [ ] assertion-backed compliant ratio,
  - [ ] negative-evidence strength,
  - [ ] documented-only rate,
  - [ ] overall acceptance and regression rates.

---

## 9) Rollout Strategy

- [ ] Phase 1 (warn mode): introduce fields/checks/metrics without hard-blocking.
- [ ] Phase 2 (mixed): enforce for changed/new guidelines, warn for legacy.
- [ ] Phase 3 (error mode): enforce globally after migration stability.

Migration support:

- [ ] Add a helper script to backfill `expected_outcome` defaults from current `compile_expectation` + `decidable_status`.
- [ ] Produce migration report listing guidelines requiring manual edits.

---

## 10) Exit Criteria

- [ ] 100% guidelines have explicit outcome contracts for compliant and non-compliant examples.
- [ ] Compliant assertion-backed ratio meets target threshold.
- [ ] Non-compliant strong-negative-evidence ratio meets target threshold.
- [ ] Example outcome mismatch count trends downward across loop iterations.
- [ ] Controller accepts improvements that increase example clarity/diversity without introducing regressions.
- [ ] Prompt/runbook artifacts are documented and reusable for future comparative experiments.

---

## 11) Risks and Mitigations

- [ ] **Risk:** Runtime-heavy checks slow loop iterations.
  - [ ] **Mitigation:** staged profiles (quick smoke checks in quick mode, full behavior checks in full mode).
- [ ] **Risk:** Legacy examples fail strict assertion requirement.
  - [ ] **Mitigation:** temporary warn mode and scripted backfill.
- [ ] **Risk:** LLM rewrites introduce flaky examples.
  - [ ] **Mitigation:** strict schema + deterministic fallback + replayable harness.
- [ ] **Risk:** Overfitting to synthetic patterns.
  - [ ] **Mitigation:** diversify by topic/obligation and score novelty over repeated templates.
