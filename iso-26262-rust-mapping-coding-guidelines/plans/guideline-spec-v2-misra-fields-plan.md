# Guideline Spec v2 Plan (MISRA-style Metadata + Examples)

This plan updates guideline records to support the new spec while keeping deterministic generation from ISO 26262 seeds.

## 0) Decisions locked in

- [x] Use corrected canonical spellings:
  - [x] `decidable` (not `decideable`)
  - [x] `undecidable` (not `undecideable`)
  - [x] `decidable_status` (not `decideable-status`)
- [x] Preserve compatibility for incoming legacy spellings via alias mapping on read/import.
- [x] Canonical persisted data in `data/todo_guidelines.yaml` will only use corrected names.
- [x] `scope` is analysis boundary only (`system|crate|module`), not a maturity/specificity ranking axis.
- [x] Do not enforce any ratchet that prefers `module` over `crate` or `system`.
- [x] `decidable_status` is conditional:
  - [x] if `decidable = undecidable`, then `decidable_status` must be absent.
  - [x] if `decidable = decidable`, then `decidable_status` is required.
- [x] If `decidable_status = clippy`, require existing lint reference from Clippy stable index.
- [x] If `decidable_status = possible-with-clippy`, require a tracker link so candidates do not go stale.
- [x] Example source-of-truth can be rustdoc-tested Markdown (`.md`) containing Rust fenced code and prose explanation.
- [x] For `decidable_status = compiler`, non-compliant example defaults to `compile_fail` expectation.
- [x] For `decidable_status = compiler`, non-`compile_fail` non-compliant examples are allowed only with explicit metadata exception + reason.

## 1) Target guideline record shape

- [ ] Adopt this required v2 structure for each guideline:
  - [ ] `id`
  - [ ] `category` (`Mandatory|Required|Advisory|Disapplied`)  
  - [ ] `technical_topic` (existing category taxonomy, renamed from old `category`)
  - [ ] `rule_statement`
  - [ ] `amplification`
  - [ ] `exceptions`
  - [ ] `rationale`
  - [ ] `iso_seeds`
  - [ ] `scope` (`system|crate|module`)
  - [ ] `decidable` (`decidable|undecidable`)
  - [ ] `decidable_status` (`compiler|clippy|possible-with-clippy|impossible-with-clippy`) when `decidable = decidable`
  - [ ] `decidability_rationale`
  - [ ] `clippy_lint_id` (required when `decidable_status = clippy`)
  - [ ] `clippy_lint_url` (required when `decidable_status = clippy`; source from `https://rust-lang.github.io/rust-clippy/stable/index.html`)
  - [ ] `clippy_candidate_tracker` (required when `decidable_status = possible-with-clippy`)
  - [ ] `state`
  - [ ] `enforcement_mode`
  - [ ] `enforcement_details`
  - [ ] `evidence_artifacts`
  - [ ] `deviation_requirements`
  - [ ] `examples.non_compliant.code_path`
  - [ ] `examples.non_compliant.explanation`
  - [ ] `examples.non_compliant.doc_path`
  - [ ] `examples.non_compliant.compile_expectation` (`compile_fail|compile_pass|documented-only`)
  - [ ] `examples.non_compliant.expectation_exception_reason` (required when compiler rule overrides default `compile_fail`)
  - [ ] `examples.compliant.code_path`
  - [ ] `examples.compliant.explanation`
  - [ ] `examples.compliant.doc_path`
  - [ ] `examples.compliant.compile_expectation` (`compile_pass|no_run|documented-only`)

## 2) Schema and compatibility updates

- [ ] Update `schemas/todo_guidelines.schema.json` to require v2 fields and enums.
- [ ] Keep `additionalProperties: false` so drift is rejected.
- [ ] Implement conditional schema logic with `if/then/else`:
  - [ ] if `decidable = undecidable`, forbid `decidable_status`, `clippy_lint_id`, `clippy_lint_url`, `clippy_candidate_tracker`.
  - [ ] if `decidable = decidable`, require `decidable_status`.
  - [ ] if `decidable_status = clippy`, require `clippy_lint_id` and `clippy_lint_url`.
  - [ ] if `decidable_status = possible-with-clippy`, require `clippy_candidate_tracker`.
  - [ ] if `decidable_status = compiler`, require `examples.non_compliant.compile_expectation`; default to `compile_fail`.
  - [ ] if `decidable_status = compiler` and `examples.non_compliant.compile_expectation != compile_fail`, require `examples.non_compliant.expectation_exception_reason`.
- [ ] Add optional temporary alias ingestion support in code paths that read guideline records:
  - [ ] map `decideable -> decidable`
  - [ ] map `decideable-status -> decidable_status`
  - [ ] map value `undecideable -> undecidable`
- [ ] Ensure canonical write paths normalize and emit corrected names only.

## 3) Generator updates (seed -> guideline)

- [ ] Update `scripts/generate_guideline_artifacts.py` to emit v2 records.
- [ ] Replace old free-text `scope` with enum mapping:
  - [ ] default `crate` for early generic ISO-derived guidelines
  - [ ] use `module` when seed clearly maps to local construct-level checks
  - [ ] use `system` when cross-crate/system integration behavior is required
- [ ] Add deterministic defaults for new fields:
  - [ ] `category` default `Required` (unless specific downgrade/upgrade rule applies)
  - [ ] `decidable` / `decidable_status` derived from existing enforceability hints
  - [ ] when `decidable_status = clippy`, derive `clippy_lint_id` + `clippy_lint_url` if a known lint exists; otherwise classify as `possible-with-clippy` or `impossible-with-clippy`
  - [ ] when `decidable_status = possible-with-clippy`, require `clippy_candidate_tracker` placeholder until linked issue exists
  - [ ] `amplification` generic starter text linked to seed reference
  - [ ] `exceptions` generic starter text with deviation path
- [ ] Preserve existing deterministic ID/order guarantees.

## 3.1) Clippy capability knowledge and references

- [ ] Add a tracked Clippy lint catalog snapshot (ID + canonical URL):
  - [ ] `data/clippy_lints_catalog.yaml`
- [ ] Add script to refresh catalog from the stable index page (manual/infrequent update is acceptable):
  - [ ] `scripts/update_clippy_lints_catalog.py`
- [ ] Add validation checks:
  - [ ] `clippy_lint_id` must exist in catalog when `decidable_status = clippy`
  - [ ] `clippy_lint_url` must match the canonical stable-index anchor for that lint
- [ ] Add guidance doc for deciding between `possible-with-clippy` vs `impossible-with-clippy`:
  - [ ] `docs/clippy-feasibility-guidance.md`

## 4) Fixture and example scaffolding

- [ ] Update `scripts/scaffold_guideline_fixtures.py` to always generate per-rule examples:
  - [ ] `tests/guidelines/<RULE_ID>/examples/non_compliant.md`
  - [ ] `tests/guidelines/<RULE_ID>/examples/compliant.md`
  - [ ] optional convenience code files (`.rs`) if needed by tool-specific runners
- [ ] Update generated `metadata.yaml` to include new fields needed by test harnesses.
- [ ] Ensure `data/todo_guidelines.yaml` example paths point to these files.
- [ ] Keep existing mode-specific fixture directories (`auto/`, `audit/`, `hybrid/`) for enforcement checks.

## 4.1) Example storage and execution contract

- [ ] Treat each `*.md` example file as the canonical artifact containing:
  - [ ] prose explanation
  - [ ] at least one fenced Rust block for execution checks
- [ ] Support rustdoc fence annotations (`compile_fail`, `no_run`, etc.) as compile intent markers.
- [ ] Add parser/extractor utility for converting code fences into temporary runnable snippets when needed.

## 5) Data migration and backfill

- [ ] Add one migration script for current backlog (27 guidelines) to v2 shape.
- [ ] Rename old topic `category` -> `technical_topic`.
- [ ] Populate new required fields for all existing guidelines with deterministic defaults.
- [ ] Generate missing example files and explanations for all existing rules.
- [ ] Regenerate `data/todo_guidelines.yaml` and validate schema.

## 6) Quality gates and policy enforcement

- [ ] Add `scripts/check_guideline_completeness.py`:
  - [ ] verify required v2 fields are present/non-empty
  - [ ] verify example file paths exist
  - [ ] verify explanation files are not placeholders
  - [ ] verify example markdown contains Rust code fences
  - [ ] verify scope/category/decidability enums are valid
  - [ ] verify `decidable_status` conditional presence/absence rules
  - [ ] verify `clippy` status has valid lint ID + URL from catalog
  - [ ] verify `possible-with-clippy` has non-empty tracker link
  - [ ] verify compiler non-compliant example expectation defaults to `compile_fail` unless exception reason is present
- [ ] Wire completeness check into orchestration (`scripts/orchestrate.py`) after guideline generation.
- [ ] Add completeness check to CI workflow (`.github/workflows/quality-gates.yml`).

## 6.1) Compile/lint execution checks for examples

- [ ] Add `scripts/check_guideline_examples.py` for executable validation.
- [ ] Run rustdoc tests against example markdown files:
  - [ ] `rustdoc --test` for compliant/non-compliant docs
- [ ] Compiler-status enforcement:
  - [ ] compliant example must satisfy `compile_pass`/`no_run` expectation
  - [ ] non-compliant example must be `compile_fail` by default
  - [ ] allow override only when metadata exception reason exists
- [ ] Clippy-status enforcement:
  - [ ] run clippy against extracted snippets/harness and assert referenced lint behavior
- [ ] For `possible-with-clippy` and `impossible-with-clippy`, run compile sanity as configured and enforce metadata/tracker requirements.
- [ ] Emit machine-readable report per run under `.cache/ops/runs/<run_id>/`.

## 7) Diffset/review integration

- [ ] Update `scripts/build_diffset.py` item context extraction for new fields:
  - [ ] `category`, `technical_topic`, `scope`, `decidable`, `decidable_status`
  - [ ] `amplification`, `exceptions`
  - [ ] example path changes
- [ ] Add/refresh tests so diffset render/review remains stable with v2 records.

## 8) Documentation updates

- [ ] Add `docs/guideline-record-spec.md` with field definitions and examples.
- [ ] Update `README.md` workflow section for v2 requirements.
- [ ] Update `tests/guidelines/README.md` with required example layout.
- [ ] Update promotion docs so sign-off expects compliant/non-compliant examples plus rationale/amplification/exceptions.
- [ ] Document decidability semantics explicitly:
  - [ ] `undecidable` means no `decidable_status` field at all
  - [ ] `scope` expresses required analysis boundary, not maturity level
  - [ ] `clippy` status requires a real stable-index lint reference

## 9) Commit phases (Conventional Commits)

- [ ] Phase A: schema + contracts
  - [ ] `feat(guidelines): adopt v2 schema with decidability and scope enums`
- [ ] Phase B: generator + migration
  - [ ] `feat(generator): emit v2 guideline records and migrate existing backlog`
- [ ] Phase B.1: clippy knowledge base
  - [ ] `feat(clippy): add lint catalog references and feasibility guidance`
- [ ] Phase C: fixture/examples
  - [ ] `feat(fixtures): scaffold compliant and non-compliant examples with explanations`
- [ ] Phase D: gates + orchestration + CI
  - [ ] `ci(gates): enforce guideline completeness and example compile/lint checks`
- [ ] Phase E: diffset/test updates
  - [ ] `test(guidelines): update diffset and unit coverage for v2 records`
- [ ] Phase F: docs
  - [ ] `docs(guidelines): document v2 guideline record and review expectations`

## 10) Verification checklist

- [ ] `uv run ruff format --check .`
- [ ] `uv run ruff check .`
- [ ] `uv run python scripts/validate_schemas.py --strict-generated`
- [ ] `uv run python scripts/check_guideline_completeness.py`
- [ ] `uv run python scripts/check_guideline_examples.py`
- [ ] `uv run python scripts/update_clippy_lints_catalog.py --check` (or equivalent no-drift mode)
- [ ] `uv run python scripts/check_traceability.py`
- [ ] `uv run python scripts/check_licensing_guard.py`
- [ ] `uv run python -m unittest discover -s tests/unit -p "test_*.py"`
- [ ] `uv run python scripts/bootstrap_session.py --profile quick`

## 11) Definition of done

- [ ] All guideline records are v2 schema-valid with corrected decidability spelling.
- [ ] `undecidable` guidelines contain no `decidable_status` field.
- [ ] `clippy` guidelines contain valid stable-index lint ID/URL references.
- [ ] `possible-with-clippy` guidelines contain tracker links.
- [ ] Every guideline has one compliant and one non-compliant Rust example plus explanation text.
- [ ] Completeness gate fails on missing sections/examples and is enforced in CI.
- [ ] Compiler-status rules enforce non-compliant `compile_fail` by default unless explicit metadata exception reason is provided.
- [ ] Example compile/lint checks run in orchestration + CI with reproducible reports.
- [ ] Diffset review shows meaningful changes for the new fields.
- [ ] Docs reflect the v2 model and promotion expectations.
