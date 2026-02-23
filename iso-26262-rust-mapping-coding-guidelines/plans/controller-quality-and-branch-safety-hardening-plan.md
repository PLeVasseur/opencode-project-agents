# Controller Quality and Branch Safety Hardening Plan

## Goal

Reduce low-quality accepted iterations, prevent commits on `main`, and promote only guideline sets that satisfy strong quality/diversity/alignment criteria.

## Preflight Branch Discipline

1. Switch back to `main` before implementing this plan.
2. Pull latest `origin/main`.
3. Create a dedicated implementation branch from `main` (for example: `feat/controller-quality-hardening`).
4. Implement and validate all changes on that branch only.

This directly addresses the prior issue where iterative controller commits landed on `main`.

## Phase 1: Commit Flow Hardening (Stop Intermediate Noise)

### 1.1 Make non-committing runs the default
- In `scripts/autonomous_controller.py`, change default behavior to **not** commit each accepted iteration.
- Keep explicit opt-in flags for commit behavior.

### 1.2 Add branch guardrails
- In `scripts/autonomous_controller.py` commit path, reject commits when current branch is `main`/`master` unless an explicit override flag is present.
- Emit a clear error message with recovery steps.

### 1.3 Promotion-only commit policy
- Keep explore iterations uncommitted.
- Commit only after a promotion check succeeds with strict gate settings.

## Phase 2: Two-Stage Controller Execution

### 2.1 Explore stage (no commits)
- Run controller with gates in advisory mode to search candidate improvements.
- Persist reports and candidate traces, but do not write commits.

### 2.2 Promote stage (strict)
- Re-evaluate selected candidate with strict settings (`error` gate mode where applicable).
- Commit only if promotion passes all required lanes.

## Phase 3: Policy Tightening for Promotion

Update promotion configuration so weak placeholder-heavy outputs fail fast.

### 3.1 Example quality
- In `config/example_quality_policy.yaml`:
  - set `gate_mode: error`
  - increase `min_outcome_match_ratio` to `0.95`
  - increase `min_assertion_backed_compliant_ratio` to `0.90`
  - increase `min_negative_evidence_strength_ratio` to `0.80`
  - lower `max_documented_only_ratio` to `0.10`
  - increase `min_unique_example_signature_ratio` to `0.70`
  - lower `max_repeated_example_signature_count` to `1` or `2`

### 3.2 Diversity
- In `config/diversity_policy.yaml`:
  - set `gate_mode: error`
  - keep/disallow same-rule-family near duplicates
  - tighten lead-in repetition tolerance
  - raise `min_unique_token_ratio` moderately above current baseline

### 3.3 Known-good alignment
- In `config/alignment_policy.yaml`:
  - set `gate_mode: error` for promotion
  - keep current global threshold intent (`>= 0.75`) and changed-guideline threshold (`>= 0.80`)
  - evaluate whether changed-guideline threshold should be tightened after stabilization

### 3.4 Guideline quality gate
- In `config/completeness_policy.yaml`:
  - set `gate_modes.guideline_quality: error`
  - keep placeholder terms strict and extend if additional template phrases are observed

## Phase 4: Generator and Scaffold Safety Controls

### 4.1 Mark scaffold outputs as non-promotable
- Prevent generic scaffold text from being promotable without rewrite.
- Add an explicit indicator (for example, metadata flag or quality marker) for scaffold-originated content.

### 4.2 Block placeholder carry-through
- In generation/scaffold scripts (`scripts/generate_guideline_artifacts.py`, `scripts/scaffold_guideline_fixtures.py`), ensure placeholder text cannot satisfy promotion checks.

## Phase 5: Candidate Selection and Scoring Improvements

### 5.1 Penalize repetitive bundles more strongly
- In `scripts/controller_actions.py`, increase penalties for action bundles that repeatedly generate low-diversity wording and repeated example signatures.

### 5.2 Prioritize evidence-critical deficits first
- Prefer actions that fix outcome mismatches and weak negative evidence before style-only rewrites.

### 5.3 Reject non-progress on touched guidelines
- Add a reject condition when a candidate mutates a guideline but leaves placeholder/quality deficits unchanged.

## Phase 6: Known-Good Alignment Refinements

### 6.1 Reduce single-anchor collapse
- In `scripts/check_known_good_alignment.py`, consider topic-filtered nearest-neighbor pools rather than broad corpus-only matching.

### 6.2 Add dimension floors for changed guidelines
- Require minimum levels on citations/evidence/granularity dimensions, not just aggregate alignment score.

## Phase 7: Operational Workflow and Acceptance Criteria

### 7.1 Workflow
1. `main` -> feature branch
2. Implement Phases 1-3 first (highest impact)
3. Run controller in explore mode (no commits)
4. Run promotion gate in strict mode
5. Commit only promotion-passing result
6. Open PR for review

### 7.2 Acceptance criteria
- No controller commits land on `main` by default.
- Explore runs produce zero commits.
- Promotion fails if placeholder-heavy or duplicate-heavy outputs remain.
- Repeated signature and lead-in violations are eliminated or within strict policy.
- Known-good alignment meets configured strict thresholds for global and changed-guideline checks.

## Suggested Implementation Order

1. Branch guard + default no-commit behavior.
2. Strict promotion gate wiring.
3. Policy threshold tightening.
4. Generator/scaffold non-promotable controls.
5. Candidate scoring and alignment heuristic refinements.
