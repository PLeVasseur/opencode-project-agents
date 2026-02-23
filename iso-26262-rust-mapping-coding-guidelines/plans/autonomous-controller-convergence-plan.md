# Autonomous Controller Plan: ISO 26262 x Rust Convergence Loop

This plan defines a controller that can run unattended and drive the repository from seed-heavy generic content to convergence-grade guideline coverage.

It is intentionally explicit about state, actions, scoring, acceptance, and stopping logic so autonomous operation remains deterministic, auditable, and hard to game.

## 1) Scope and outcomes

- [ ] Build a top-level controller that repeatedly executes: observe -> plan -> mutate -> evaluate -> accept/reject -> iterate.
- [ ] Use existing gate scripts and artifacts as the objective measurement layer, not free-form judgment.
- [ ] Ensure one ISO target can expand into many guidelines (including 15-20+ where justified).
- [ ] Use FLS coverage as an imperfect Rust-surface proxy, combined with decomposition and quality checks.
- [ ] Define objective stopping conditions (success and stall) that terminate unattended runs safely.

## 2) New components to add

### 2.1 Controller entrypoint

- [ ] Add `scripts/autonomous_controller.py` as the orchestrator above `scripts/orchestrate.py`.
- [ ] CLI options:
  - [ ] `--session-id <id>`
  - [ ] `--mode growth|change` (default `growth`)
  - [ ] `--profile quick|full`
  - [ ] `--max-iterations <int>`
  - [ ] `--stall-window <int>`
  - [ ] `--beam-width <int>`
  - [ ] `--full-eval-every <int>`
  - [ ] `--commit-each-accept` (optional)
  - [ ] `--dry-run`

### 2.2 Controller state and journal

- [ ] Add `.cache/controller/<session_id>/state.json` with:
  - [ ] `session_id`
  - [ ] `started_at`, `updated_at`
  - [ ] `iteration`
  - [ ] `accepted_run_id`
  - [ ] `best_metrics`
  - [ ] `no_improvement_count`
  - [ ] `status` (`running|success|blocked|error`)
  - [ ] `history[]` entries (proposal, score, decision, rationale)
- [ ] Add `.cache/controller/<session_id>/iterations/<n>/` folder per iteration:
  - [ ] `observe.json`
  - [ ] `deficits.json`
  - [ ] `candidates.json`
  - [ ] `evaluation.json`
  - [ ] `decision.json`

### 2.3 Action engine

- [ ] Add `scripts/controller_actions.py` to implement action primitives.
- [ ] Add `scripts/controller_scoring.py` to score candidates and detect improvement.
- [ ] Add `scripts/controller_observe.py` to collect metrics/deficits from run artifacts.

## 3) Canonical deficit model (what the controller optimizes)

- [ ] Standardize deficits into machine-typed categories:
  - [ ] `iso_obligation_gap` (missing coverage rows for obligation units)
  - [ ] `target_fanout_gap` (decomposition shortfall vs policy floor)
  - [ ] `fls_span_gap` (target span below threshold)
  - [ ] `fls_chapter_gap` (global chapter coverage below threshold)
  - [ ] `quality_gap` (guideline score below minimum)
  - [ ] `placeholder_gap` (generic/template text still present)
  - [ ] `example_gap` (example compile/lint mismatch or placeholder docs)
  - [ ] `traceability_gap` (matrix references missing/unknown)
- [ ] Encode each deficit with fields:
  - [ ] `deficit_id`
  - [ ] `type`
  - [ ] `severity` (`critical|high|medium|low`)
  - [ ] `target_id` (optional)
  - [ ] `obligation_unit_id` (optional)
  - [ ] `guideline_id` (optional)
  - [ ] `evidence_ref` (path to report row/message)
  - [ ] `distance_to_pass` (numeric gap)

## 4) Action primitives (controller mutation vocabulary)

All actions are deterministic transforms over tracked files.

### 4.1 Decomposition actions

- [ ] `split_generic_rule_family`:
  - [ ] Input: `target_id`, optional `obligation_unit_id` subset.
  - [ ] Behavior: create sibling guidelines under shared `rule_family_id` with distinct scopes/construct focus.
  - [ ] Guarantee: preserve parent rule as anchor or mark parent as decomposed shell.
- [ ] `spawn_rule_for_obligation_unit`:
  - [ ] Input: uncovered `obligation_unit_id`.
  - [ ] Behavior: create or map at least one guideline row to that unit.
- [ ] `rebalance_seed_to_guideline_links`:
  - [ ] Move/add `iso_seeds` and `obligation_units` so each guideline has precise traceability.

### 4.2 FLS mapping actions

- [ ] `assign_missing_fls_refs`:
  - [ ] For guidelines lacking `fls_refs`, assign top candidates from `data/fls_target_candidates.yaml`.
- [ ] `expand_fls_refs_for_span`:
  - [ ] Add additional valid refs to close target span gaps while keeping relevance.
- [ ] `repair_invalid_fls_refs`:
  - [ ] Replace unknown refs with known inventory refs in same chapter/topic neighborhood.

### 4.3 Quality hardening actions

- [ ] `rewrite_rule_statement_specific`:
  - [ ] Replace generic language with precise Rust constructs, conditions, and expected behavior.
- [ ] `rewrite_amplification_with_boundaries`:
  - [ ] Add scope constraints, acceptable patterns, forbidden patterns, and review criteria.
- [ ] `rewrite_rationale_with_safety_mechanism`:
  - [ ] Tie rationale to hazard prevention/detection mechanics.
- [ ] `upgrade_examples_non_placeholder`:
  - [ ] Ensure rule-specific compliant/non-compliant examples and realistic expectations.

### 4.4 Consistency actions

- [ ] `sync_coverage_rows`:
  - [ ] Ensure each guideline/seed mapping produces canonical matrix rows including `fls_ref`.
- [ ] `normalize_metadata`:
  - [ ] Keep required fields present and aligned with schema/rules.

## 5) Candidate generation strategy

- [ ] Generate a ranked candidate set each iteration from current deficits.
- [ ] Use a bounded beam strategy:
  - [ ] Build action bundles focused on top deficits.
  - [ ] Keep bundle size small (`1-3` actions) to isolate impact.
  - [ ] Keep at most `beam_width` bundles.
- [ ] Prioritize deficit classes in this order:
  - [ ] 1) `iso_obligation_gap`
  - [ ] 2) `target_fanout_gap`
  - [ ] 3) `fls_span_gap` / `fls_chapter_gap`
  - [ ] 4) `placeholder_gap` / `quality_gap`
  - [ ] 5) `example_gap`
- [ ] De-duplicate candidates by normalized action signature.
- [ ] Skip candidates that previously regressed the same metric without new context.

### 5.1 Beam bundle composition rules (Phase C detail)

- [ ] Cluster deficits before bundle construction:
  - [ ] `cluster_key = target_id || obligation_unit_id || guideline_id`
  - [ ] allow cross-cluster bundles only when they share `target_id` or `rule_family_id`
- [ ] Build bundles from deterministic templates:
  - [ ] `spawn_rule_for_obligation_unit` + `assign_missing_fls_refs`
  - [ ] `split_generic_rule_family` + `rewrite_rule_statement_specific`
  - [ ] `assign_missing_fls_refs` + `rewrite_amplification_with_boundaries`
  - [ ] `expand_fls_refs_for_span` + `upgrade_examples_non_placeholder`
- [ ] Enforce compatibility matrix:
  - [ ] disallow duplicate action type on same object in one bundle
  - [ ] disallow two `spawn_rule_for_obligation_unit` actions for the same obligation in one bundle
  - [ ] disallow quality rewrites on a guideline being removed/deprecated in same bundle
- [ ] Bound bundle complexity:
  - [ ] `max_actions_per_bundle = 3`
  - [ ] `max_mutated_guidelines_per_bundle = 5`
  - [ ] reject bundles that touch unrelated targets without explicit rationale
- [ ] Compute expected-impact estimate per bundle:
  - [ ] expected lane deltas (`iso`, `fanout`, `fls`, `quality`)
  - [ ] estimated regression risk (from historical action fingerprints)

### 5.2 Beam ranking and pruning (Phase C detail)

- [ ] Score each bundle pre-evaluation with:
  - [ ] deficit severity coverage score
  - [ ] expected-impact score
  - [ ] novelty score (avoid repeating stale bundles)
  - [ ] risk penalty
- [ ] Keep top `beam_width` bundles after pruning dominated candidates.
- [ ] Track historical fingerprints (`bundle_signature`) to avoid retry loops:
  - [ ] if same signature fails `N` times with no context changes, auto-suppress.

## 6) Evaluation protocol

### 6.1 Per-candidate evaluation

- [ ] Apply candidate action bundle on working tree branch/workspace.
- [ ] Run `scripts/orchestrate.py` in quick mode for fast feedback.
- [ ] Run required gates and collect machine reports:
  - [ ] `validate_schemas`
  - [ ] `check_guideline_completeness`
  - [ ] `check_traceability`
  - [ ] `check_rule_decomposition`
  - [ ] `check_fls_proxy_coverage`
  - [ ] `check_guideline_quality`
  - [ ] `check_guideline_examples`
- [ ] Every `full_eval_every` iterations, force a full profile run.

### 6.2 Scoring function

- [ ] Use lexicographic objective to prevent gaming:
  - [ ] Level 1: no new runtime errors.
  - [ ] Level 2: no regression in already-passing lanes.
  - [ ] Level 3: maximize reduction in critical/high deficits.
  - [ ] Level 4: maximize net weighted score improvement.
- [ ] Suggested weighted score (secondary comparator only):
  - [ ] `score = 1000*iso_coverage + 500*(1 - fanout_gap_ratio) + 400*fls_proxy + 300*quality_pass_ratio - penalties`
  - [ ] Penalties for regressions, placeholder reintroduction, or invalid refs.

### 6.3 Two-pass beam evaluation (quick -> full)

- [ ] Pass 1 (quick): evaluate all beam candidates with quick gates.
- [ ] Pass 2 (full): re-evaluate top `K` quick winners with full profile (`K=1..2`).
- [ ] Accept candidate only if:
  - [ ] quick result improves and has no regressions,
  - [ ] full result (when required this iteration) also improves and has no regressions.
- [ ] If quick and full disagree, prefer full and log discrepancy for tuning.

### 6.4 Deterministic tie-break order

- [ ] Tie-break accepted candidates in this strict order:
  - [ ] smallest lexicographic metric vector
  - [ ] greatest reduction in critical/high deficits
  - [ ] highest weighted score
  - [ ] smallest mutation footprint (fewer files changed)
  - [ ] stable sort by `candidate_id`

## 7) Acceptance and rollback logic

- [ ] Accept candidate only if all are true:
  - [ ] no runtime failures
  - [ ] no hard policy regressions
  - [ ] objective improves (lexicographic compare)
- [ ] If accepted:
  - [ ] persist artifacts
  - [ ] update controller state `best_metrics`
  - [ ] increment iteration and reset `no_improvement_count`
- [ ] If rejected:
  - [ ] discard candidate changes
  - [ ] record rejection rationale
  - [ ] continue evaluating next candidate
- [ ] If all candidates rejected in iteration:
  - [ ] increment `no_improvement_count`

## 8) Convergence and stopping conditions

### 8.1 Success stop (DONE)

- [ ] Stop with `success` only when all pass for `K` consecutive full evaluations (recommend `K=3`):
  - [ ] ISO obligation coverage at required threshold (default `1.0`)
  - [ ] decomposition deficits `= 0` under policy
  - [ ] FLS span deficits `= 0` and chapter coverage meets threshold
  - [ ] quality deficits `= 0` under policy mode
  - [ ] traceability and example gates pass
  - [ ] no unresolved blocker review findings for changed scope

### 8.2 Stall stop (BLOCKED)

- [ ] Stop with `blocked` when:
  - [ ] `no_improvement_count >= stall_window` (recommend `5`), or
  - [ ] `iteration >= max_iterations`.
- [ ] Emit blocker report containing:
  - [ ] unresolved deficit list
  - [ ] closest attempted actions
  - [ ] likely causes and next manual interventions

### 8.3 Safety stop (ERROR)

- [ ] Stop immediately on persistent runtime/infrastructure failure (for example extractor path failure repeated `N` times).
- [ ] Preserve last known-good accepted snapshot and full logs.

## 9) Generic-to-specific decomposition algorithm

- [ ] Detect generic guidelines using deterministic predicates:
  - [ ] placeholder terms in core fields
  - [ ] low quality score
  - [ ] broad rule statement lacking Rust construct nouns
  - [ ] examples marked `documented-only` on both sides repeatedly
- [ ] For each generic guideline, derive decomposition axes:
  - [ ] obligation unit axis (`obligation_units`)
  - [ ] Rust construct axis (ownership, traits, macros, unsafe, concurrency, etc.)
  - [ ] enforceability axis (`AUTO`, `HYBRID`, `AUDIT` residual)
  - [ ] failure-mode axis (compile-time, lint-time, audit-time)
- [ ] Spawn sibling rules from Cartesian slices with bounded growth:
  - [ ] start with top 2-4 highest-value slices
  - [ ] add more only if deficits remain
- [ ] Maintain family integrity:
  - [ ] shared `rule_family_id`
  - [ ] optional `decomposition_parent`
  - [ ] non-overlapping intent statements

## 10) FLS proxy search logic

- [ ] For each target/obligation:
  - [ ] start from candidate refs from `data/fls_target_candidates.yaml`
  - [ ] compute current covered refs from guideline `fls_refs`
  - [ ] if span below threshold, propose add/remove edits minimizing irrelevant refs
- [ ] Chapter balancing heuristic:
  - [ ] prioritize missing in-scope chapters with high target density
  - [ ] avoid overfitting by assigning refs only when lexical/topic match evidence exists
- [ ] Validate every changed ref against `data/fls_inventory.yaml`.

## 11) Data contracts and schemas to extend

- [ ] Add `schemas/controller_state.schema.json` for session state.
- [ ] Add `schemas/controller_iteration.schema.json` for iteration records.
- [ ] Add `schemas/controller_blocker_report.schema.json` for blocked outcomes.
- [ ] Enforce schema validation in controller before accepting an iteration.

## 12) Git and branch strategy for unattended runs

- [ ] Run controller on dedicated working branch (for example `auto/convergence-<session_id>`).
- [ ] Optional commit policy:
  - [ ] commit only accepted iterations,
  - [ ] Conventional Commit style with lane tags.
- [ ] Commit cadence:
  - [ ] one commit per accepted iteration, or
  - [ ] squash every `M` accepted iterations for noise control.
- [ ] Never auto-push unless explicitly enabled by config.

## 13) Observability and reporting

- [ ] Add rolling dashboard markdown:
  - [ ] `.cache/controller/<session_id>/dashboard.md`
  - [ ] latest metrics, deficit trends, accepted actions, ETA heuristic.
- [ ] Emit `final_report.md` on termination:
  - [ ] termination reason (`success|blocked|error`)
  - [ ] final metric vector
  - [ ] remaining deficits (if any)
  - [ ] reproducible command list

### 13.1 Strict promotion handoff package

- [ ] Add `.cache/controller/<session_id>/handoff/` artifacts:
  - [ ] `handoff.json` (machine-readable promotion decision)
  - [ ] `handoff.md` (reviewer-facing summary)
  - [ ] `lane_status.json` (per-lane pass/fail + thresholds)
  - [ ] `delta_summary.json` (accepted baseline -> candidate deltas)
  - [ ] `run_registry_candidate.yaml` (proposed accepted-run entry)
- [ ] Encode promotion recommendation state:
  - [ ] `ready`
  - [ ] `needs_review`
  - [ ] `blocked`
- [ ] Include mandatory evidence in handoff:
  - [ ] ISO obligation coverage proof
  - [ ] decomposition/fanout proof
  - [ ] FLS proxy proof (target spans + chapter ratio)
  - [ ] quality proof (no below-threshold rules)
  - [ ] traceability/examples gate proofs
  - [ ] unresolved blocker list (if any)

### 13.2 Accepted-run registration handoff workflow

- [ ] Add scripted generation of registration payload from handoff artifacts.
- [ ] Validate that `scope_fingerprint` and selected `accepted_run_id` are consistent.
- [ ] Refuse `ready` status if `K` consecutive full-pass condition is not met.
- [ ] Refuse `ready` status if any lane is pass-by-warning when policy requires hard pass.

## 14) Test plan for controller logic

- [ ] Unit tests for:
  - [ ] deficit extraction/parsing
  - [ ] candidate generation determinism
  - [ ] scoring comparator and lexicographic acceptance
  - [ ] stopping condition transitions
- [ ] Integration tests for:
  - [ ] happy path convergence with synthetic mini-dataset
  - [ ] stall scenario with intentionally unfixable deficits
  - [ ] regression rejection scenario
  - [ ] restart/resume from saved state

## 15) Rollout phases

### Phase A: Dry-run planner

- [ ] Implement observe + deficits + candidate generation without mutating files.
- [ ] Produce ranked proposed actions and expected impact.

### Phase B: Single-action closed loop

- [ ] Enable one accepted action per iteration.
- [ ] Run quick gate evaluation and accept/reject decisions.

### Phase C: Beam search and periodic full eval

- [ ] Enable multi-action bundles (`2-3` actions) with compatibility matrix.
- [ ] Implement beam ranking/pruning and history-aware suppression.
- [ ] Add two-pass evaluation (quick sweep + full rerank of top candidates).
- [ ] Add deterministic tie-break and mutation-footprint minimization.

### Phase D: Hardened autonomous mode

- [ ] Enable unattended continuous loop with stop conditions.
- [ ] Optionally enable commit-per-accept on dedicated branch.

### Phase E: Hard-gate promotion policy

- [ ] Flip policy modes from `warn` to `error` once quality/decomposition are consistently clean.
- [ ] Require `K` consecutive full-pass iterations before promotion recommendation.

### Phase F: Promotion handoff hardening

- [ ] Generate strict handoff package under `.cache/controller/<session_id>/handoff/`.
- [ ] Add machine-evaluable `ready|needs_review|blocked` promotion decision.
- [ ] Emit `run_registry_candidate.yaml` only when decision is `ready`.
- [ ] Validate handoff package via dedicated JSON schemas.

### Phase G: Convergence ratchet and closure

- [ ] Introduce ratchet policy to tighten thresholds across windows:
  - [ ] decomposition warnings -> errors
  - [ ] quality warnings -> errors
  - [ ] stricter minimum scores once baseline quality stabilizes
- [ ] Require no measurable improvement window to confirm true convergence (not oscillation).
- [ ] Freeze candidate generation once all lanes hard-pass and convergence window is satisfied.

## 16) Recommended default configuration

- [ ] `max_iterations: 30`
- [ ] `stall_window: 5`
- [ ] `beam_width: 4`
- [ ] `max_actions_per_bundle: 3`
- [ ] `full_eval_top_k: 2`
- [ ] `full_eval_every: 3`
- [ ] `commit_each_accept: false` (initially)
- [ ] gate modes initially `warn` for decomposition and quality, then ratchet to `error`

## 17) Definition of "autonomous completion"

- [ ] Completion is achieved only when:
  - [ ] all objective lanes pass under current policy,
  - [ ] no measurable improvements remain across the convergence window,
  - [ ] no blocker findings remain unresolved for changed scope,
  - [ ] final report is emitted with reproducible evidence.

## 18) Immediate implementation checklist

- [ ] Create `scripts/autonomous_controller.py` skeleton with session state load/save.
- [ ] Implement `controller_observe.py` to parse run reports into normalized deficits.
- [ ] Implement `controller_actions.py` for first three actions:
  - [ ] `assign_missing_fls_refs`
  - [ ] `spawn_rule_for_obligation_unit`
  - [ ] `rewrite_rule_statement_specific`
- [ ] Implement lexicographic scorer and accept/reject engine.
- [ ] Add blocker/final report generation.
- [ ] Add unit tests and one end-to-end integration test.
- [ ] Add bundle composer + compatibility matrix for Phase C.
- [ ] Add two-pass (quick/full) evaluator and deterministic tie-breaker.
- [ ] Add strict promotion handoff artifact generator and recommendation state.
