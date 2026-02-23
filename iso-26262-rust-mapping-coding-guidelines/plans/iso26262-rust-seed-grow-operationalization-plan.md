# ISO 26262 Rust Mapping Operationalization Plan (Seed -> Grow)

This plan operationalizes the concept in `ideas/iso26262_guideline_seeding_plan_v4.md` using the existing extractor/query tool in `../iso-26262-coding-standard-extraction`.

## 0) Preconditions and boundaries

- [ ] Use extractor at `../iso-26262-coding-standard-extraction` as the system of record for ISO corpus ingest/query/validation.
- [ ] Keep licensed PDFs, SQLite DB, and raw extracted text local to extractor workspace only.
- [ ] Keep this repo focused on mappings, guideline definitions, and evidence metadata (no verbatim ISO content dumps).
- [ ] Enforce a rule that tracked artifacts in this repo store references, paraphrases, IDs, and citations only.
- [ ] Keep planning documents outside the operationalization repo (store plans under `$OPENCODE_CONFIG_DIR/plans/`, not in project source control).

## 1) Repository scaffolding for operation

- [ ] Create and track: `config/`, `schemas/`, `seeds/`, `data/`, `scripts/`, `audit_checklists/`, `tests/guidelines/`, `docs/`, `feedback/`, `docs_snapshots/`, `enforcement/`.
- [ ] Add root `.gitignore` contract with `.cache/` as the canonical root for ephemeral data.
- [ ] Require `.gitignore` entries (minimum):
  - [ ] `.cache/`
  - [ ] `.cache/**`
  - [ ] any local temporary/export paths used by scripts
- [ ] Standardize Python orchestration tooling:
  - [ ] use `uv` for dependency management and script execution,
  - [ ] use `ruff` for linting and formatting checks,
  - [ ] track `pyproject.toml` and `uv.lock` in source control,
  - [ ] pin Python version and tool versions in `pyproject.toml`.
- [ ] Use Python as the canonical orchestration language for this repo (no required shell-script pipeline).
- [ ] Keep durable templates/processes in source control; keep per-run evidence payloads and working snapshots in `.cache/`.
- [ ] Add `README.md` section describing the end-to-end flow: extractor -> seeds -> categories -> guideline backlog -> evidence.

## 2) Extractor integration contract

- [ ] Add `config/extractor_paths.yaml` with:
  - [ ] `repo_root: ../iso-26262-coding-standard-extraction`
  - [ ] `cache_root: ../iso-26262-coding-standard-extraction/.cache/iso26262`
  - [ ] `manifest_dir: ../iso-26262-coding-standard-extraction/.cache/iso26262/manifests`
- [ ] Define path-resolution precedence for all scripts:
  - [ ] environment variables (`EXTRACTOR_REPO_ROOT`, `EXTRACTOR_CACHE_ROOT`, `EXTRACTOR_MANIFEST_DIR`) win,
  - [ ] then `config/extractor_paths.yaml`,
  - [ ] then default relative path fallback.
- [ ] Validate resolved paths early and fail fast with actionable errors when extractor repo/cache/manifests are missing.
- [ ] Persist resolved path snapshot to `.cache/ops/runs/<run_id>/resolved_paths.json` for reproducibility.
- [ ] Define language/runtime split for orchestration:
  - [ ] Rust extractor CLI remains the query/validation engine,
  - [ ] Python scripts in this repo orchestrate runs (`uv run ...`),
  - [ ] shell scripts are optional convenience launchers only and are not part of the required execution path.
- [ ] Add `scripts/check_extractor_health.py` to run extractor readiness checks (`status`, `validate` preflight).
- [ ] Treat extractor health as a hard gate before seed generation.

## 3) Seed manifest and deterministic query orchestration

- [ ] Add `config/corpus_registry.yaml` to declare corpus packs (ISO-only now, Rust-doc packs enabled later) and associated seed manifests.
- [ ] Add `schemas/corpus_registry.schema.json` and validate `config/corpus_registry.yaml` in CI.
- [ ] Define `config/corpus_registry.yaml` fields (minimum):
  - [ ] `corpus_pack_id`
  - [ ] `enabled`
  - [ ] `extractor_target_parts[]`
  - [ ] `seed_manifest_path`
  - [ ] `default_profile` (`quick|full`)
  - [ ] `allowed_modes` (`change|growth`)
  - [ ] `notes` (non-normative)
- [ ] Create `seeds/seed_manifest.yaml` containing fixed anchor query sets:
  - [ ] Exact anchors: `Table 1`, `Table 6`, `Table 7`, `Table 9`, `Table 10`, `Table 12`, `Table 13`, `Table 14`, `Table 15`, `5.4.2`, `5.4.3`, `8.4.5`, `9.4.2`, `9.4.4`, `10.4.2`, `10.4.5`, `11.4`, `Annex B`, `Annex C`, `Annex D`.
  - [ ] Concept anchors: `defensive programming`, `error handling`, `language subset`, `complexity`, `concurrency`, `type conversion`.
- [ ] Add orchestrator entrypoint `scripts/orchestrate.py` with command contract:
  - [ ] `--mode change|growth`,
  - [ ] `--corpus-pack <name>`,
  - [ ] `--base-run <run_id>` (required for comparisons),
  - [ ] `--profile quick|full`,
  - [ ] `--emit-cache-root .cache/ops`.
- [ ] Define orchestrator output contract under `.cache/ops/runs/<run_id>/`:
  - [ ] `run_manifest.json` (mode, profile, corpus pack, scope fingerprint, comparator run IDs)
  - [ ] `metrics.json` (coverage, traceability, backlog, gate outcomes)
  - [ ] `summary.md` (human-readable result)
  - [ ] `promotion_candidate.json` (paths eligible for promotion)
- [ ] Define orchestrator exit-code contract:
  - [ ] `0` pass (all required gates passed)
  - [ ] `2` policy/gate failure (non-regression or completeness failure)
  - [ ] `3` tool/runtime failure (extractor/tooling unavailable or crashed)
- [ ] Add `scripts/query_seeds.py` that:
  - [ ] uses lexical mode for exact anchors,
  - [ ] uses semantic/hybrid mode for concept anchors,
  - [ ] always includes context and pinpoint (`--with-ancestors`, `--with-descendants`, `--with-pinpoint`),
  - [ ] stores raw outputs in local run folder (`.cache/seed_runs/<run_id>/`) excluded from git.

## 4) Seed normalization and category extraction

- [ ] Add `schemas/seed_topics.schema.json`.
- [ ] Add `scripts/build_seed_topics.py` to normalize raw query outputs into `data/seed_topics.yaml`.
- [ ] Deduplicate seed rows by stable key (`part + reference + citation_anchor_id + row_key`).
- [ ] Require each seed topic to include:
  - [ ] `seed_id`
  - [ ] `iso_ref`
  - [ ] `chunk_id`
  - [ ] `citation`
  - [ ] `topic_phrase`
  - [ ] `context_summary`
  - [ ] `category_candidate`
  - [ ] `enforceability_hint` (`AUTO|AUDIT|HYBRID` initial recommendation)
- [ ] Build `data/guideline_categories.yaml` from normalized seeds, starting with Table 1 and Table 6 topics.

## 5) Guideline backlog generation (seed -> candidate rule)

- [ ] Add `schemas/todo_guidelines.schema.json`.
- [ ] Generate `data/todo_guidelines.yaml` with mandatory fields:
  - [ ] `id`
  - [ ] `category`
  - [ ] `rule_statement`
  - [ ] `rationale`
  - [ ] `iso_seeds[]`
  - [ ] `scope`
  - [ ] `state` (`DRAFT|TRIAL|ENFORCED|DEPRECATED`)
  - [ ] `enforcement_mode` (`AUTO|AUDIT|HYBRID`)
  - [ ] `enforcement_details`
  - [ ] `evidence_artifacts`
  - [ ] `deviation_requirements`
- [ ] Add `data/enforcement_catalog.yaml` mapping rule patterns to enforcers (`rustc`, `clippy`, `rustfmt`, custom scripts, manual review).

## 6) Traceability and evidence matrix

- [ ] Build `data/coverage_matrix.csv` that links:
  - [ ] extractor target IDs (`target_sections.json`) -> `seed_id`
  - [ ] `seed_id` -> `guideline_id`
  - [ ] `guideline_id` -> evidence artifact path(s)
- [ ] Add `scripts/check_traceability.py` hard gates:
  - [ ] no missing in-scope target IDs,
  - [ ] each guideline linked to at least one ISO seed,
  - [ ] each guideline linked to at least one evidence artifact entry.
- [ ] Add `scripts/check_licensing_guard.py` to prevent accidental verbatim ISO text in tracked artifacts.
- [ ] Add `docs/deviation_process.md` for waiver workflow and approver/evidence requirements.
- [ ] Keep heavy run-specific traceability intermediates in `.cache/traceability_build/`; promote only canonical matrix outputs to tracked `data/`.

## 7) Manual-audit and hybrid operations

- [ ] Define audit trigger conditions (minimum):
  - [ ] `unsafe` usage,
  - [ ] FFI boundaries,
  - [ ] concurrency primitives/atomics,
  - [ ] critical numeric conversions,
  - [ ] changes in error-handling paths.
- [ ] Create `audit_checklists/rule_checklist_template.md` with required checks and expected evidence.
- [ ] Define a persistent audit-record format keyed by PR/change ID and store volatile audit payloads in `.cache/audit_records/`.
- [ ] Require audit-signoff records for rules with `AUDIT` and `HYBRID` modes.

## 8) Guideline fixture tests (AUTO, AUDIT, HYBRID)

- [ ] Introduce `tests/guidelines/<RULE_ID>/` layout with mode-specific fixtures.
- [ ] Require per-rule metadata: mode, toolchain version, pass/fail criteria.
- [ ] For `AUTO`: include violating/compliant examples and expected tool output.
- [ ] For `AUDIT`: include violating/compliant examples, reviewer steps, and expected finding record.
- [ ] For `HYBRID`: include tool-caught violation + residual audit-only violation and explicit boundary statement.

## 9) Rust freshness baseline and rotation

- [ ] Pin toolchain in this repo via `rust-toolchain.toml`.
- [ ] Add `scripts/snapshot_rust_docs.py` for rustup offline docs snapshot.
- [ ] Track `docs_snapshots/rust/manifest.yaml` with toolchain version, timestamps, and hashes.
- [ ] Store lint baseline inventories in `enforcement/baselines/<toolchain>/`:
  - [ ] `rustc -W help`
  - [ ] clippy lint inventory/config snapshot
  - [ ] rustfmt config snapshot
- [ ] Add `docs/baseline-rotation.md` procedure for controlled toolchain upgrades and evidence updates.

## 10) CI gates and promotion policy

- [ ] Add CI workflow that runs:
  - [ ] `uv sync --frozen`,
  - [ ] `uv run ruff format --check .`,
  - [ ] `uv run ruff check .`,
  - [ ] `uv run python scripts/check_extractor_health.py` (extractor health preflight),
  - [ ] `uv run python scripts/validate_schemas.py` (schema validation for config + generated YAML/CSV),
  - [ ] `uv run python scripts/orchestrate.py --mode change --profile quick --corpus-pack <default_pack> --base-run <accepted_run_id>` (seed/category/backlog consistency and diff gates),
  - [ ] `uv run python scripts/check_traceability.py` (traceability completeness checks),
  - [ ] `uv run python scripts/check_licensing_guard.py` (licensed-content guard).
- [ ] Enforce state transition policy for rules:
  - [ ] `DRAFT -> TRIAL` requires seed linkage + enforcement plan,
  - [ ] `TRIAL -> ENFORCED` requires evidence and acceptable noise metrics,
  - [ ] `ENFORCED -> DEPRECATED` requires documented rationale and replacement/impact note.
- [ ] Block `TRIAL -> ENFORCED` when extractor findings contain open high-severity issues affecting mapped rule areas.

## 11) Pilot rollout sequence

- [ ] Pilot first 10 rules sourced from Table 1 and Table 6 coverage.
- [ ] Target mode mix in pilot: majority AUTO/HYBRID, minority AUDIT/HYBRID.
- [ ] Capture pilot metrics: false positives, remediation cost, findings yield, waiver rate.
- [ ] Refine taxonomy/templates and scale to full target set.

## 12) Before/after snapshots and growth governance (`.cache/`)

- [ ] Introduce run modes:
  - [ ] `change` mode: same target scope, strict non-regression expected.
  - [ ] `growth` mode: expanded scope, old scope must remain non-regressing while new scope is added.
- [ ] Add `config/change_growth_policy.yaml` for explicit pass/fail thresholds and warning bands.
- [ ] Add `schemas/change_growth_policy.schema.json` and validate in CI.
- [ ] Add tracked `data/run_registry.yaml` as accepted baseline ledger:
  - [ ] `corpus_pack_id`
  - [ ] `mode`
  - [ ] `accepted_run_id`
  - [ ] `scope_fingerprint`
  - [ ] `accepted_at`
  - [ ] `accepted_by`
- [ ] Define policy defaults in `config/change_growth_policy.yaml` (minimum):
  - [ ] `change_mode.max_coverage_drop = 0.0`
  - [ ] `change_mode.max_traceability_drop = 0.0`
  - [ ] `change_mode.max_evidence_link_drop = 0.0`
  - [ ] `growth_mode.require_old_scope_non_regression = true`
  - [ ] `growth_mode.min_new_scope_coverage_delta` (explicit target)
  - [ ] `growth_mode.min_new_guidelines_delta` (explicit target)
- [ ] Define execution profiles:
  - [ ] `quick` profile for PR/new-session checks (reduced query pack, deterministic gates only)
  - [ ] `full` profile for nightly/release checks (full query pack + full diff reporting)
- [ ] Write run manifests under `.cache/ops/runs/<run_id>/` with:
  - [ ] run mode,
  - [ ] source run(s) for comparison,
  - [ ] scope fingerprint (hash of in-scope target IDs),
  - [ ] generated metric bundle paths.
- [ ] Build deterministic before/after diff outputs under `.cache/ops/diffs/<before>__<after>.{json,md}`.
- [ ] In `change` mode, fail the run when any of the following regress:
  - [ ] in-scope target coverage completeness,
  - [ ] seed -> guideline traceability completeness,
  - [ ] guideline -> evidence linkage completeness,
  - [ ] extractor health gate status.
- [ ] Require growth diffs to report two lanes explicitly:
  - [ ] old-scope non-regression checks,
  - [ ] new-scope coverage and guideline backlog deltas.
- [ ] In `growth` mode, fail the run when old-scope non-regression fails; evaluate new-scope thresholds using `config/change_growth_policy.yaml`.
- [ ] Promote only approved canonical outputs from `.cache/` into tracked `data/`; keep raw/working artifacts ephemeral.

## 13) Extractor feedback loop and upstream issue tracking

- [ ] Add tracked backlog `feedback/extractor_findings.yaml` with fields:
  - [ ] `finding_id`, `date`, `opened_at`, `owner`, `due_by`, `run_id_before`, `run_id_after`, `tool_version`, `tool_commit_sha`, `stage`, `severity`, `status`, `expected`, `observed`, `repro_cmd`, `upstream_issue_url`.
- [ ] Define severity taxonomy and SLA in `docs/extractor-feedback-policy.md`:
  - [ ] `S0` blocking correctness/safety mapping defect,
  - [ ] `S1` high-impact quality regression,
  - [ ] `S2` moderate issue with workaround,
  - [ ] `S3` minor issue/documentation gap.
- [ ] Store reproducibility evidence for each finding under `.cache/extractor_feedback_evidence/<finding_id>/`.
- [ ] Add script workflow:
  - [ ] `scripts/report_extractor_finding.py` to append normalized findings,
  - [ ] `scripts/link_upstream_issue.py` to create/link upstream issue in extractor repo and write back URL.
- [ ] Use triage lifecycle states: `new -> triaged -> upstream-open -> fixed-upstream -> verified`.
- [ ] Require closure/mitigation of `S0/S1` findings before promoting affected rules to `ENFORCED`.

## 14) New-session bootstrap (first 30 minutes)

- [ ] Add `docs/new-session-bootstrap.md` with a deterministic startup flow for fresh sessions.
- [ ] Bootstrap flow must include:
  - [ ] verify `uv` is available,
  - [ ] run `uv sync --frozen`,
  - [ ] resolve/print extractor paths (env -> config -> fallback),
  - [ ] run extractor health check (`uv run python scripts/check_extractor_health.py`),
  - [ ] load accepted baseline from `data/run_registry.yaml`,
  - [ ] execute seed query run to `.cache/seed_runs/<run_id>/`,
  - [ ] build normalized seed/category/backlog artifacts,
  - [ ] run change/growth diff against previous accepted run using `scripts/orchestrate.py`,
  - [ ] update feedback backlog if regressions are tool-related.
- [ ] Add a single wrapper command (`scripts/bootstrap_session.py`) that runs the above sequence via `uv run` and emits next actions.

## 15) Open decisions with defaults (session-proofing)

- [ ] Record decision defaults in `docs/decision-log.md` and keep them synchronized with config files.
- [ ] Set default corpus pack to `iso-core-part6` until additional packs are formally enabled in `config/corpus_registry.yaml`.
- [ ] Set default retrieval behavior:
  - [ ] exact anchors use lexical mode,
  - [ ] concept anchors use hybrid mode,
  - [ ] pinpoint/context flags are always enabled for seed generation.
- [ ] Set default comparison behavior:
  - [ ] PR/new-session checks use `--profile quick`,
  - [ ] nightly/release checks use `--profile full`.
- [ ] Set default promotion behavior:
  - [ ] no auto-promotion from `.cache/` to tracked `data/`,
  - [ ] promotion requires explicit reviewer sign-off and run ID registration in `data/run_registry.yaml`.
- [ ] Set default failure behavior:
  - [ ] any missing required artifact in orchestrator output contract is a hard failure,
  - [ ] policy violations return exit code `2`, runtime/tool failures return exit code `3`.

## 16) Phased implementation and commit strategy

- [x] Execute remaining implementation in small, end-to-end slices, with one Conventional Commit per logical capability.
- [x] Use commit format `<type>(<scope>): <subject>` for every phase (`feat`, `fix`, `test`, `ci`, `docs`, `chore` as applicable).
- [x] Keep commit scope narrow: avoid mixing generator/orchestration/gating/docs changes in a single commit unless they are inseparable.
- [x] Treat bootstrap allowances as temporary scaffolding only: strict traces/gates should be default once generator artifacts exist.

### Recommended phase sequence (commit-sized slices)

- [x] Phase A: guideline artifact generation from normalized seeds.
  - [x] Add generator logic that derives non-empty `data/guideline_categories.yaml`, `data/todo_guidelines.yaml`, and `data/coverage_matrix.csv` from `data/seed_topics.yaml`.
  - [x] Implemented commit: `feat(generator): derive guideline artifacts from seed topics` (`4fb78f2`).
- [x] Phase B: orchestrator integration of guideline generation.
  - [x] Wire generator execution and step reporting into `scripts/orchestrate.py`.
  - [x] Implemented commit: `feat(orchestrate): wire guideline generation into run pipeline` (`6db07bd`).
- [x] Phase C: traceability gate hardening.
  - [x] Prevent empty-placeholder artifacts from passing non-bootstrap checks.
  - [x] Implemented commit: `fix(traceability): enforce non-empty completeness gates` (`5c5c414`).
- [x] Phase D: pilot backlog population.
  - [x] Seed initial Table 1/Table 6-oriented guideline candidates and category mappings.
  - [x] Implemented commit: `feat(backlog): seed initial pilot guideline candidates` (`029437a`).
- [x] Phase E: rule fixture scaffolding for pilot rules.
  - [x] Add `tests/guidelines/<RULE_ID>/` pilot fixtures and metadata for deterministic verification.
  - [x] Implemented commit: `test(guidelines): add pilot fixture skeletons and metadata` (`025c5a2`).
- [x] Phase F: CI gate enforcement.
  - [x] Add workflow(s) for `uv sync --frozen`, `ruff`, schema validation, orchestration, traceability, and licensing guard checks.
  - [x] Implemented commit: `ci(gates): add workflow for lint and policy checks` (`0ccc988`).
- [x] Phase G: operator workflow documentation.
  - [x] Update docs for promotion flow, baseline acceptance, and run-registry updates.
  - [x] Implemented commit: `docs(workflow): document promotion and baseline acceptance flow` (`59d3d38`).

### Per-commit quality gate checklist

- [x] Run before every commit:
  - [x] `uv run ruff format --check .`
  - [x] `uv run ruff check .`
  - [x] `uv run python scripts/validate_schemas.py`
- [x] For commits touching generation/orchestration/gates, also run:
  - [x] `uv run python scripts/bootstrap_session.py --profile quick`
- [x] Ensure each commit has auditable evidence pointers (at minimum run summary path under `.cache/ops/runs/<run_id>/summary.md`).
- [x] Keep `.cache/`, `.venv/`, `.ruff_cache/` excluded from commit scope unless explicitly needed for local recovery only.

### Phase completion criteria

- [x] A phase is complete only when all code/data/doc changes for that phase are committed and local quality gates pass.
- [x] Any phase that changes policy/gating behavior must include an explicit non-regression validation run with recorded artifact path.
- [x] Do not collapse phases into a single commit unless an implementation dependency makes isolation impossible; if collapsed, document why in commit body.

## Definition of done

- [ ] `data/seed_topics.yaml` generated and schema-valid.
- [ ] `data/guideline_categories.yaml` generated and reviewed.
- [ ] `data/todo_guidelines.yaml` generated, schema-valid, and checklisted.
- [ ] `data/coverage_matrix.csv` complete for in-scope targets.
- [ ] `data/run_registry.yaml` tracks accepted baseline runs for active corpus packs/modes.
- [ ] Audit checklist + records workflow operational.
- [ ] Rust baseline snapshot and rotation process documented.
- [ ] CI gates enforce traceability and completeness.
- [ ] `.cache/` before/after and growth diff workflow is operational and used for change acceptance.
- [ ] Extractor feedback loop is active with upstream linkage and promotion gates.
- [ ] A brand-new session can execute the bootstrap flow end-to-end without manual path/debug intervention.
- [ ] Python orchestration runs through `uv` and passes `ruff` formatting/lint checks in CI.
- [ ] Core orchestration path is Python-first (`uv run ...`) with no required shell-script dependency.
