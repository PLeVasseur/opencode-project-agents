# ISO↔Rust Grow Pipeline Defect Remediation Plan

This plan addresses defects in the current seed->grow->controller loop that are causing low-diversity guideline text, weak Rust grounding, and over-reliance on deterministic template rewrites.

It is intentionally specific about what to change, where to change it, how to validate it, and what quality bars must be met before continuing long autonomous runs.

---

## 0) Branch and Execution Discipline

- [ ] **Switch implementation work back to `main` first** in `personal/iso-26262-rust-mapping-coding-guidelines`.
- [ ] Confirm clean/expected working tree state before starting remediation changes.
- [ ] Perform implementation on `main` in phased commits, then branch for experimental long-loop sessions.
- [ ] Do **not** push automatically; keep push/PR explicit and user-driven.

### 0.1 Confirmed policy decision (near-duplicates)

- [x] Near-duplicate rules are allowed **only** when both are true:
  - [x] they map to different `obligation_units`, and
  - [x] they include clearly different verification constraints.
- [ ] Encode this rule as explicit diversity-policy configuration and gate logic.
- [ ] Reject near-duplicates that fail either condition above.

---

## 1) Confirmed Defects to Fix

### 1.1 ISO query coverage defects

- [ ] Seed retrieval currently depends on fixed ISO queries from `seeds/seed_manifest.yaml` and does not dynamically widen ISO anchor coverage.
- [ ] Current growth policy (`config/change_growth_policy.yaml`) allows zero deltas, which can permit low-signal "growth" loops.

### 1.2 Rust grounding defects

- [ ] Rust specificity is mostly indirect (synthetic FLS proxy + known-good style pressure), not direct retrieval from Rust references/docs/lints for each target.
- [ ] `scripts/build_fls_inventory.py` is synthetic proxy data, which is useful for scaffolding but weak for high-fidelity semantic grounding.

### 1.3 Generation/rewriting defects

- [ ] `scripts/controller_actions.py` rewrite action (`apply_rewrite_rule_statement_specific`) uses a highly repetitive template shape.
- [ ] Citation expansion (`apply_add_alignment_citation_signals`) appends generic anchors rather than context-specific citations.
- [ ] Candidate bundles repeatedly converge on same 3-action pattern, producing wording monoculture.

### 1.4 Evaluation and control defects

- [ ] There is no dedicated anti-duplication gate for guideline text families.
- [ ] Known-good alignment can be improved by stylistic marker insertion without enough specificity/novelty pressure.
- [ ] LLM fallback semantics can suppress model-led variation when `fallback_recommended=true` appears frequently.

---

## 2) Target Outcomes

- [ ] Guidelines remain traceable to ISO obligations **and** exhibit materially better Rust-specific grounding.
- [ ] Repetition rate for rule lead-ins and near-duplicate guideline pairs drops significantly.
- [ ] Near-duplicate rules are only retained when they satisfy the approved exception policy (distinct obligation unit + distinct verification constraints).
- [ ] Citation and std-ref expansions become target/topic-specific, not boilerplate.
- [ ] Controller still preserves deterministic safety rails, but diversity and specificity are rewarded.
- [ ] 40+ loop sessions show measurable convergence without template collapse.

---

## 3) Workstream A - Rust Signal Retrieval Layer (Direct Grounding)

### 3.1 New artifacts and configuration

- [ ] Add `config/rust_signal_sources.yaml` with explicit source inventory:
  - [ ] std/core API anchor map by topic (Result/Option/unsafe/pointer/FFI/concurrency/etc).
  - [ ] Rust Reference keyword groups by language feature.
  - [ ] Clippy lint families by guideline category.
  - [ ] Optional docs snapshot metadata pointers.
- [ ] Add `schemas/rust_signal_sources.schema.json`.
- [ ] Add `schemas/rust_signals.schema.json` for generated signal pack.

### 3.2 New build step

- [ ] Add `scripts/build_rust_signals.py` to produce `data/rust_signals.yaml`.
- [ ] Include deterministic mappings:
  - [ ] `technical_topic -> recommended std refs`
  - [ ] `fls_refs -> rust concept terms`
  - [ ] `obligation unit class -> evidence anchor families`
- [ ] Persist provenance fields (`source`, `version`, `generated_at`, `signal_count`).

### 3.3 Pipeline integration

- [ ] Insert `build_rust_signals.py` into `scripts/orchestrate.py` before guideline generation.
- [ ] Validate new config/generated artifact in `scripts/validate_schemas.py`.
- [ ] Ensure controller observation can report missing Rust-signal coverage as deficits.

---

## 4) Workstream B - Citation Grounding Engine (Context-Specific, Not Boilerplate)

### 4.1 Replace static citation append logic

- [ ] Refactor `apply_add_alignment_citation_signals` in `scripts/controller_actions.py` to use a new resolver function rather than fixed marker list.
- [ ] Add resolver that chooses citations/refs from:
  - [ ] `obligation_units` and `iso_seeds` (ISO-specific anchors)
  - [ ] `technical_topic` and `fls_refs` (Rust std/core refs)
  - [ ] optional nearest known-good feature hints

### 4.2 New citation mapping config

- [ ] Add `config/citation_grounding_policy.yaml` with:
  - [ ] ISO citation templates by obligation type
  - [ ] std/core reference defaults by topic
  - [ ] max repeats per guideline/rationale
  - [ ] minimum citation diversity requirement
- [ ] Add `schemas/citation_grounding_policy.schema.json`.

### 4.3 Enforcement

- [ ] Add checks to avoid repeated generic phrases (e.g., repeated "Safety evidence anchor" sentences).
- [ ] Add per-guideline citation provenance in metadata/report for auditability.

---

## 5) Workstream C - Diversity / Anti-Duplication Gate

### 5.1 New gate

- [ ] Add `scripts/check_guideline_diversity.py`.
- [ ] Add `schemas/guideline_diversity_report.schema.json`.
- [ ] Gate computes:
  - [ ] normalized rule-statement similarity clusters
  - [ ] repeated-lead-in frequency
  - [ ] pairwise near-duplicate count within same/different `rule_family_id`
  - [ ] topical lexical diversity score
  - [ ] near-duplicate exception eligibility verdict per pair (`allowed_exception` vs `violation`)

### 5.2 Policy

- [ ] Add `config/diversity_policy.yaml` with thresholds:
  - [ ] `max_exact_rule_statement_duplicates`
  - [ ] `max_similarity_above_threshold`
  - [ ] `min_topic_lexical_diversity`
  - [ ] gate mode (`warn|error`)
  - [ ] `allow_near_duplicate_with_distinct_obligation_unit: true`
  - [ ] `require_verification_constraint_divergence: true`
  - [ ] `min_verification_constraint_delta_count`
  - [ ] `disallow_near_duplicate_within_same_rule_family`
- [ ] Add `schemas/diversity_policy.schema.json`.

### 5.2.1 Verification-constraint divergence definition

- [ ] Define and enforce divergence using at least one of:
  - [ ] different `decidable_status`
  - [ ] different non-compliant `compile_expectation`
  - [ ] different enforcement mode/details
  - [ ] different required evidence artifact class/pattern
  - [ ] different bounded condition in rule/amplification text
- [ ] Add machine-readable reason codes in diversity report for each accepted exception pair.

### 5.3 Controller integration

- [ ] Add diversity gate to `scripts/controller_observe.py`.
- [ ] Emit deficits of type `duplication_gap`.
- [ ] Emit deficits of type `duplication_exception_missing` when near-duplicates exist without valid exception criteria.
- [ ] Update `scripts/controller_scoring.py` with duplication penalty and regression detection.
- [ ] Add candidate generation/actions for duplication remediation.

---

## 6) Workstream D - Rewrite Strategy Redesign (Topic-Aware + Deterministic Variety)

### 6.1 Deterministic variant families

- [ ] Replace single rewrite template in `apply_rewrite_rule_statement_specific` with variant bank by:
  - [ ] `technical_topic`
  - [ ] `scope`
  - [ ] dominant `fls_refs`
  - [ ] obligation class (table/clause/annex)
- [ ] Use stable variant selection keyed by guideline ID hash (reproducible diversity).

### 6.2 Content-shape constraints

- [ ] Ensure each rewrite contains:
  - [ ] explicit normative intent (shall/must/avoid/require)
  - [ ] concrete bounded condition
  - [ ] verification/evidence clause
  - [ ] domain-relevant Rust concepts from `data/rust_signals.yaml`

### 6.3 Repeat suppression

- [ ] Add phrase-bank suppression so overused openings are deprioritized.
- [ ] Penalize generated rewrite if it exceeds similarity threshold with existing rules.

---

## 7) Workstream E - LLM Integration for Controlled Diversity (Beyond Selection Only)

### 7.1 Preserve selector role with clearer semantics

- [ ] Update decision policy behavior so `fallback_recommended` can be configured as:
  - [ ] advisory (valid selection still usable)
  - [ ] authoritative (current behavior)
- [ ] Persist both model-selected and resolved-selected IDs in `selection_resolution.json`.

### 7.2 Add LLM micro-rewriter phase (new)

- [ ] Add `scripts/controller_rewrite.py` (or equivalent helper) invoked only for selected candidate guideline(s).
- [ ] Input packet includes:
  - [ ] current guideline fields
  - [ ] deficit context
  - [ ] nearest duplicates
  - [ ] Rust signals + citation requirements
- [ ] Output schema includes:
  - [ ] `rule_statement`, `amplification`, `exceptions`, `rationale`
  - [ ] `citation_plan`
  - [ ] `uniqueness_rationale`
- [ ] Add `schemas/controller_llm_rewrite.schema.json`.

### 7.3 Guardrails and fallback

- [ ] Validate output against strict schema and hard constraints.
- [ ] Reject rewrites that violate citation/scope/traceability constraints.
- [ ] Fallback to deterministic topic-variant rewrite if invalid/unavailable.

---

## 8) Workstream F - Growth Logic Corrections

### 8.1 Policy hardening

- [ ] Update `config/change_growth_policy.yaml` to require non-zero, meaningful growth deltas.
- [ ] Add explicit diversity and Rust-grounding growth metrics to policy.

### 8.2 Acceptance logic

- [ ] Extend `improves()` and related scoring to include:
  - [ ] duplication reduction
  - [ ] citation specificity score increase
  - [ ] Rust-signal coverage increase
- [ ] Prevent repeated acceptance of changes that only rephrase boilerplate with no structural gain.

---

## 9) Workstream G - Observability and Auditability Enhancements

- [ ] Add per-iteration decision trace fields:
  - [ ] `model_selected_candidate_ids`
  - [ ] `resolved_candidate_ids`
  - [ ] `final_applied_candidate_id`
  - [ ] `fallback_reason`
- [ ] Add rewrite provenance fields:
  - [ ] `rewrite_source` (`deterministic_variant|llm|fallback`)
  - [ ] `citation_sources` (which mapping generated each citation)
- [ ] Add compact iteration event log (`event_log.jsonl`) to simplify crash recovery and postmortem analysis.

---

## 10) Test Plan

### 10.1 Unit tests

- [ ] Citation resolver produces topic-specific refs and avoids duplicates.
- [ ] Diversity checker flags near duplicates and repeated lead-ins.
- [ ] Diversity checker allows near-duplicate pair only when both (distinct obligation unit + distinct verification constraints) are true.
- [ ] Diversity checker rejects near-duplicates with same obligation unit even if wording differs slightly.
- [ ] Diversity checker rejects near-duplicates with different obligation unit but same verification constraints.
- [ ] Rewrite variant selector produces deterministic but diverse outputs.
- [ ] LLM rewrite validator rejects malformed/low-shape outputs.

### 10.2 Integration tests

- [ ] Orchestrate run includes Rust signal build + diversity gate successfully.
- [ ] Controller loop handles duplication deficits and resolves them over iterations.
- [ ] LLM selector + micro-rewriter + deterministic fallback all function under failure injection.

### 10.3 Regression tests

- [ ] Existing schema checks and controller logic tests remain green.
- [ ] No regression in traceability/completeness/example gates.

---

## 11) Phased Implementation Commits

### Phase 1 - Grounding infrastructure

- [ ] Add Rust signal config/schemas/build step and wire into orchestrate.
- [ ] Commit: `feat(grow): add rust signal retrieval and schema-validated signal pack`.

### Phase 2 - Citation engine and rewrite variants

- [ ] Replace fixed citation append with context-specific resolver.
- [ ] Introduce topic-aware rewrite variants and repeat suppression.
- [ ] Commit: `feat(guidelines): add contextual citation grounding and variant rewrites`.

### Phase 3 - Diversity gate and controller scoring

- [ ] Add diversity checker, policy, observation deficits, and scoring penalties.
- [ ] Commit: `feat(controller): enforce diversity gate and duplication penalties`.

### Phase 4 - LLM rewrite layer and decision telemetry

- [ ] Add schema-validated LLM micro-rewriter + fallback.
- [ ] Expand selection/provenance telemetry in iteration artifacts.
- [ ] Commit: `feat(controller): add constrained llm rewrite stage and audit telemetry`.

### Phase 5 - Growth policy hardening + docs

- [ ] Tighten growth thresholds and improve success criteria.
- [ ] Update docs/runbook for new metrics and recovery steps.
- [ ] Commit: `docs(grow): document rust grounding, diversity gates, and growth criteria`.

---

## 12) Exit Criteria (Definition of Done)

- [ ] Repeated boilerplate lead-ins reduced below diversity threshold.
- [ ] No disallowed near-duplicate pairs remain; all retained near-duplicate pairs include auditable exception reason codes.
- [ ] Citation/std-ref usage is context-specific and auditable per guideline.
- [ ] Rust grounding coverage metrics improve measurably across loops.
- [ ] LLM contributes controlled diversity without violating deterministic safety rails.
- [ ] 40-loop session shows improved quality/diversity trends and complete audit trail.

---

## 13) Execution Note for Next Step

- [ ] **Before coding this remediation plan, switch to `main` and implement from there.**
- [ ] After remediation implementation is complete on `main`, create a new experiment branch for the next 40-loop run with OpenCode in the loop.
