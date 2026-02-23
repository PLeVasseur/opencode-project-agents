# IRM ID Full Backfill and Interactive Generator Plan

Date: 2026-02-15
Status: Draft execution plan
Priority: High
Plan type: Traceability identity remediation

## 0) Locked decisions
- [x] Perform a full IRM ID backfill now (not incremental-only for new statements).
- [x] Make day-to-day authoring rely on an interactive generator script.
- [x] Generator must support both `{dp}` and `{ts}` workflows for MyST metadata prefaces.
- [x] Generator should guide the author through prompts about what output they need.
- [x] Generate `irm_` IDs with FLS-style payload shape (`[A-Za-z0-9]{12}`) using Python `secrets` APIs (not `random`).
- [x] Keep backfill mapping artifacts run-scoped only; do not commit them to the repository.
- [x] Enforce strict cutover immediately after backfill: reject legacy `SRCN-*` IDs in strict validation/build gates.
- [x] Keep ID generation exclusively in tooling scripts (generator + backfill), never in Sphinx extension runtime.
- [x] Add a dedicated extension check module named `paragraph_id_check.py` for duplicate/format enforcement.
- [x] Refactor `exts/iso26262_spec/__init__.py` into a thin wiring module, following FLS-style extension decomposition.
- [x] Use "ISO 26262 Rust Mapping ID" / "IRM ID" terminology across code, logs, docs, schemas, and user-facing output.
- [x] Define S4 as the strict cutover stage: enforce hard rejection of legacy `SRCN-*` only after backfill apply.

## 0A) Terminology and stage glossary
- [ ] Term policy: use "IRM ID" (or "ISO 26262 Rust Mapping ID") everywhere in prose, diagnostics, and code symbols.
- [ ] Legacy term policy: treat `source_id` as deprecated naming and remove it from user-facing text.
- [ ] Stage glossary:
  - [ ] S1 = safe module decomposition (no behavior changes)
  - [ ] S2 = strict-check implementation in shadow mode (report-only, no repository-breaking fail)
  - [ ] S3 = tooling introduction (interactive generator + backfill tooling)
  - [ ] S4 = one-time cutover apply (full backfill + strict enforcement on, no compatibility window)

## 1) Objectives
- [ ] Replace all existing positional/legacy IRM metadata IDs with stable opaque IDs that are safe to move within documents.
- [ ] Preserve semantic trace metadata (`trace_status`, `anchor_ids`, `relation`) during migration.
- [ ] Preserve statement-level coverage and strict build/lint/trace gates.
- [ ] Add an interactive authoring tool for future ID minting with minimal manual formatting work.

## 2) Scope and boundaries
- [ ] In scope: markdown statement IDs in `src/iso26262_rust_mapping.md`.
- [ ] In scope: YAML row/cell IDs in `src/tables/table-*.yaml`.
- [ ] In scope: any statement references (`{p}` role usage) that point to IDs being replaced.
- [ ] In scope: schema/regex/lint rules that validate IRM ID format and uniqueness.
- [ ] In scope: operator docs for the new generation workflow.
- [ ] Out of scope: changing ISO anchor registry semantics.
- [ ] Out of scope: changing table business content beyond ID fields and required references.

## 3) Target IRM ID contract (post-remediation)
- [ ] Adopt a single canonical pattern for IRM IDs: `irm_<random-id>`.
- [ ] Use FLS-like random ID shape for the payload: 12 alphanumeric characters (`[A-Za-z0-9]{12}`).
- [ ] Use lowercase `irm_` prefix to distinguish this project while keeping FLS-style ergonomics.
- [ ] Example valid ID: `irm_qTgd9xuAY3n3`.
- [ ] Keep payload case-sensitive to match FLS-style linking behavior.
- [ ] Treat IDs as immutable once committed.
- [ ] Require uniqueness across markdown and YAML combined.
- [ ] Keep human-readable numbering (`display_number`) as derived build output only.
- [ ] Statement anchor policy: paragraph/list anchors use the exact IRM ID string (`irm_...`) rather than slug canonicalization.
- [ ] Collision policy: any duplicate anchor derived from distinct IRM IDs is a hard error.

## 3A) FLS reference baseline
- [ ] Align generator UX and ID appearance with the FLS helper script pattern.
- [ ] Reference implementation source:
  - [ ] `https://github.com/rust-lang/fls/blob/main/generate-random-ids.py`
  - [ ] `https://github.com/rust-lang/fls/blob/main/exts/ferrocene_spec/README.rst` (Paragraph IDs section)
- [ ] Keep this repository's prefix as `irm_` (not `fls_`) while retaining the same visual format.

## 3B) FLS extension architecture ideas to adopt
- [ ] Mirror FLS pattern of a small top-level extension module that mostly wires specialized submodules.
  - [ ] FLS reference: `exts/ferrocene_spec/__init__.py` delegates to `definitions`, `paragraph_ids`, etc.
- [ ] Keep lint orchestration separate from core extension runtime, as FLS does.
  - [ ] FLS reference: `exts/ferrocene_spec_lints/__init__.py` dispatching to dedicated lint modules.
- [ ] Keep paragraph ID policy checks in a dedicated checker module.
  - [ ] FLS reference: `exts/ferrocene_spec_lints/require_paragraph_ids.py`.
- [ ] Keep paragraph export/report logic as a separate concern from parsing/binding.
  - [ ] FLS reference: `exts/ferrocene_spec/paragraph_ids.py`.

## 4) Pre-migration safeguards
- [ ] Require a clean working tree before running apply mode.
- [ ] Create a safety checkpoint commit before any ID rewrite.
- [ ] Freeze content edits during migration window (no paragraph/table text edits while remapping IDs).
- [ ] Capture a baseline build and trace artifact set before rewrite.
  - [ ] `./make.py validate`
  - [ ] `./make.py build`
  - [ ] `SPHINX_MIGRATION_RUN_ROOT=<temp-run-root> ./make.py trace-validate`
- [ ] Capture pre-migration IRM ID inventory from markdown, YAML, and references.
- [ ] Fail early if duplicate or malformed pre-migration IDs are detected.
- [ ] Persist baseline count invariants to run-state artifacts.
  - [ ] Current inventory snapshot at plan update time: markdown `SRCN-*` count = `101`.
  - [ ] Current inventory snapshot at plan update time: tables `SRCN-*` count = `2055`.
  - [ ] Current inventory snapshot at plan update time: total `SRCN-*` count = `2156`.
  - [ ] Recompute counts at run start; if counts differ from snapshot, log diff and require explicit continue marker in `checklist.state.env`.

## 4A) Resumable-execution skill protocol (mandatory)
- [ ] Use the `resumable-execution` skill workflow for this migration run.
- [ ] Create run root under `$OPENCODE_CONFIG_DIR/reports/` with stable task/run id naming.
  - [ ] `TASK=irm-id-full-backfill`
  - [ ] `RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)`
  - [ ] `RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/${TASK}-${RUN_ID}"`
- [ ] Bootstrap durable run files from skill templates before any mutating action.
  - [ ] `state.env` from `skills/resumable-execution/run-state.template.env`
  - [ ] `checklist.state.env` from `skills/resumable-execution/checklist-state.template.env`
  - [ ] `run.log` initialized
  - [ ] `artifacts/` directory initialized
- [ ] Populate immutable contract keys in `state.env` before stage execution.
  - [ ] `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`, `ARTIFACT_ROOT`, `LOCK_FILE`
  - [ ] branch/base pin and expected pre-mutation HEAD SHA
- [ ] Add explicit checklist keys in `checklist.state.env` for each stage gate.
  - [ ] `CB_S1_*` safe-refactor gates
  - [ ] `CB_S2_*` lint/parser strictness implementation gates (shadow mode only)
  - [ ] `CB_S3_*` generator/backfill tooling gates
  - [ ] `CB_S4_*` full apply + strict cutover + validation + docs gates
- [ ] Enforce single-writer lock discipline for the run.
  - [ ] create/update lock file with pid/host/user/timestamp
  - [ ] stop on active non-stale lock
  - [ ] on stale lock: record prior lock metadata in `run.log`, then replace lock
- [ ] Use atomic state persistence for all run-state updates.
  - [ ] write `*.tmp`, parse-check, atomic rename for `state.env` and `checklist.state.env`
- [ ] Define and enforce resume windows.
  - [ ] before mutation
  - [ ] after mutation/before verification
  - [ ] push attempted with unknown outcome
  - [ ] push confirmed/finalization incomplete
- [ ] Enforce mandatory stop conditions from skill guidance.
  - [ ] dirty worktree at mutation boundary
  - [ ] immutable contract drift on resume
  - [ ] missing/unparseable state files
  - [ ] stage marked done with incomplete checklist keys
  - [ ] missing required artifacts for current stage
- [ ] Finalize idempotently and release lock.
  - [ ] avoid duplicate summary/report appends for same `RUN_ID`
  - [ ] set finalization flags only after confirmation
  - [ ] remove lock on success and failure paths
- [ ] Stage artifact gate policy (must exist before stage completion is marked):
  - [ ] S1 artifacts: `artifacts/s1/refactor-manifest.json`, `artifacts/s1/s1-verify.log`
  - [ ] S2 artifacts: `artifacts/s2/paragraph-id-check-shadow.json`, `artifacts/s2/s2-verify.log`
  - [ ] S3 artifacts: `artifacts/s3/generator-smoke.log`, `artifacts/s3/backfill-dry-run-summary.json`
  - [ ] S4 artifacts: `artifacts/s4/id-mapping.json`, `artifacts/s4/rewrite-summary.json`, `artifacts/s4/validation-summary.json`
- [ ] Artifact integrity policy:
  - [ ] write SHA256 and byte-size for each required artifact into `run.log`
  - [ ] fail stage closeout if expected artifact hash/size record is missing

## 5) Migration toolchain additions
- [ ] Add `tools/traceability/generate_irm_ids.py` (interactive-first authoring helper).
- [ ] Add `tools/traceability/backfill_irm_ids.py` (one-time full remap utility).
- [ ] Add `exts/iso26262_spec_lints/paragraph_id_check.py` for IRM ID duplicate/format enforcement.
- [ ] Add reusable IRM ID utilities module for:
  - [ ] FLS-style random ID generation (`irm_` + 12 alnum chars)
  - [ ] pattern validation
  - [ ] collision checks against repository inventory
- [ ] Add IRM terminology harmonization pass in runtime code and docs.
  - [ ] replace user-facing mentions of "source id" / `source_id` with "IRM ID"
  - [ ] keep legacy names only at temporary parser boundaries until S4 cutover
  - [ ] migrate persisted field names from `source_id` to `irm_id` by S4 cutover

## 5A) Extension decomposition blueprint (de-spaghetti `__init__.py`)
- [ ] Create `exts/iso26262_spec/types.py` for shared dataclasses/types.
  - [ ] Move `PrefaceMetadata` from `__init__.py`.
- [ ] Create `exts/iso26262_spec/nodes.py` for custom node classes.
  - [ ] Move `dp_node`, `ts_node`, `a_node`, `rel_node`, `p_node` from `__init__.py`.
- [ ] Create `exts/iso26262_spec/roles.py` for role classes.
  - [ ] Move `_BaseTraceRole`, `DpRole`, `TsRole`, `ARole`, `RelRole`, `PRole` from `__init__.py`.
- [ ] Create `exts/iso26262_spec/record_store.py` for env state and record registry behavior.
  - [ ] Move `_ensure_env`, `_record_error`, `_register_record`.
  - [ ] Keep all duplicate-record checks centralized here.
- [ ] Create `exts/iso26262_spec/preface_parser.py` for parsing `{dp}`/`{ts}`/`{rel}`/`{a}` metadata.
  - [ ] Move `_extract_preface` and parsing regexes.
  - [ ] Update parser to accept only `irm_` IDs under strict mode.
- [ ] Create `exts/iso26262_spec/markdown_binding.py` for preface-to-statement binding.
  - [ ] Move `_is_markdown_statement_node`, `_set_paragraph_text`, `_bind_prefaces`.
  - [ ] Keep statement record creation logic here, not in setup/wiring files.
- [ ] Create `exts/iso26262_spec/table_directive.py` for table rendering and trace extraction.
  - [ ] Move `IsoTableDirective` and helpers needed only for table rendering.
  - [ ] Keep table row/cell metadata checks colocated with rendering.
- [ ] Create `exts/iso26262_spec/registry.py` for ISO anchor registry loading.
  - [ ] Move `_read_jsonc`, `_load_anchor_registry`.
- [ ] Create `exts/iso26262_spec/references.py` for `{p}` and `{a}` reference resolution.
  - [ ] Move `{p}` and `{a}` resolution logic from `_on_doctree_resolved`.
- [ ] Create `exts/iso26262_spec/outputs.py` for export/report/schema emission.
  - [ ] Move `_write_json`, `_write_text`, `_emit_trace_outputs`.
  - [ ] Keep build artifact writing isolated from doctree mutation logic.
- [ ] Create `exts/iso26262_spec/domain.py` for `TraceDomain`.
- [ ] Create `exts/iso26262_spec/events.py` for Sphinx event handlers.
  - [ ] Move `_on_builder_inited`, `_on_env_purge_doc`, `_on_env_merge_info`, `_on_doctree_read`, `_on_doctree_resolved`, `_on_build_finished`.
- [ ] Keep `exts/iso26262_spec/__init__.py` as thin composition/wiring only.
  - [ ] Import/register domain, roles, directives, config values, and event callbacks.
  - [ ] No business logic, no parsing logic, no export logic in final `__init__.py`.

## 5B) Lint package decomposition (FLS-style)
- [ ] Keep `exts/iso26262_spec_lints/__init__.py` as lint orchestrator only.
- [ ] Split current lint checks into dedicated modules:
  - [ ] `legacy_token_check.py`
  - [ ] `native_table_check.py`
  - [ ] `anchor_resolution_check.py`
  - [ ] `preface_adjacency_check.py`
  - [ ] `table_anchor_check.py`
  - [ ] `trace_status_check.py`
  - [ ] `paragraph_id_check.py` (new strict `irm_` checks)
- [ ] Add lint summary aggregation in one place (orchestrator), mirroring FLS `run_lints` style.

## 5C) `__init__.py` extraction map (function-level)
- [ ] Extract utility/helpers:
  - [ ] `_sha256_text` -> `exts/iso26262_spec/utils.py`
  - [ ] `_slug` -> `exts/iso26262_spec/utils.py`
  - [ ] `_read_jsonc` -> `exts/iso26262_spec/utils.py`
- [ ] Extract preface parsing:
  - [ ] `_extract_preface` -> `exts/iso26262_spec/preface_parser.py`
  - [ ] IRM ID regex constants -> `exts/iso26262_spec/preface_parser.py`
- [ ] Extract markdown binding:
  - [ ] `_is_markdown_statement_node` -> `exts/iso26262_spec/markdown_binding.py`
  - [ ] `_set_paragraph_text` -> `exts/iso26262_spec/markdown_binding.py`
  - [ ] `_bind_prefaces` -> `exts/iso26262_spec/markdown_binding.py`
  - [ ] `_collect_missing_units` -> `exts/iso26262_spec/markdown_binding.py`
- [ ] Extract table directive:
  - [ ] `IsoTableDirective` -> `exts/iso26262_spec/table_directive.py`
  - [ ] row/cell anchor helper functions -> `exts/iso26262_spec/table_directive.py`
- [ ] Extract output/reporting:
  - [ ] `_write_json` -> `exts/iso26262_spec/outputs.py`
  - [ ] `_write_text` -> `exts/iso26262_spec/outputs.py`
  - [ ] `_emit_trace_outputs` -> `exts/iso26262_spec/outputs.py`
- [ ] Extract runtime hooks:
  - [ ] `_on_builder_inited` -> `exts/iso26262_spec/events.py`
  - [ ] `_on_env_purge_doc` -> `exts/iso26262_spec/events.py`
  - [ ] `_on_env_merge_info` -> `exts/iso26262_spec/events.py`
  - [ ] `_on_doctree_read` -> `exts/iso26262_spec/events.py`
  - [ ] `_on_doctree_resolved` -> `exts/iso26262_spec/events.py`
  - [ ] `_on_build_finished` -> `exts/iso26262_spec/events.py`
- [ ] Extract domain/directive metadata:
  - [ ] `TraceDomain` -> `exts/iso26262_spec/domain.py`
  - [ ] `TraceMetaDirective` -> `exts/iso26262_spec/directives.py`
- [ ] Keep final `exts/iso26262_spec/__init__.py` responsibilities strictly limited to:
  - [ ] config value registration
  - [ ] role/directive/domain registration
  - [ ] event hook wiring

## 5D) FLS-to-ISO module mapping checklist
- [ ] Apply FLS extension architecture patterns with explicit local mapping:
  - [ ] FLS `exts/ferrocene_spec/__init__.py` -> local thin `exts/iso26262_spec/__init__.py`
  - [ ] FLS `exts/ferrocene_spec/paragraph_ids.py` -> local `exts/iso26262_spec/outputs.py`
  - [ ] FLS `exts/ferrocene_spec_lints/__init__.py` -> local `exts/iso26262_spec_lints/__init__.py`
  - [ ] FLS `exts/ferrocene_spec_lints/require_paragraph_ids.py` -> local `exts/iso26262_spec_lints/paragraph_id_check.py`
- [ ] Confirm local split keeps current ISO-specific behaviors while adopting FLS modular style.
- [ ] Verify no feature regressions from extraction by running full strict build/lint/trace gates after each major extraction commit.

## 6) Interactive generator requirements
- [ ] Default mode is guided prompts (wizard mode).
- [ ] Default generated output is MyST preface snippets including both `{dp}` and `{ts}` (not raw IDs).
- [ ] First prompt asks what the author needs:
  - [ ] MyST metadata preface lines (`{dp}` + `{ts}`)
  - [ ] YAML `cell_trace` snippets
  - [ ] YAML `_trace` snippets
  - [ ] raw ID list only (advanced/secondary mode)
- [ ] Prompt for quantity (`count`) and generate unique IDs.
- [ ] Prompt for trace status behavior:
  - [ ] one status applied to all
  - [ ] prompt status per generated entry
- [ ] For mapped status, prompt for relation and anchor handling:
  - [ ] relation value
  - [ ] optional anchor list entry or placeholder
- [ ] Support output presets:
  - [ ] MyST default line: `{dp}`...` {ts}`unmapped_with_rationale``
  - [ ] MyST mapped line: `{dp}`...` {ts}`mapped` {rel}`...` {a}`...``
  - [ ] MyST out-of-scope line: `{dp}`...` {ts}`out_of_scope_with_rationale``
  - [ ] YAML block with `irm_id`, `trace_status`, `anchor_ids`, `relation`
- [ ] Support either stdout output or write-to-file mode.
- [ ] Support non-interactive flags for scripted usage (`--mode`, `--count`, `--ts`, etc.).
- [ ] Lock explicit non-interactive flags and defaults:
  - [ ] `--mode` (`myst-preface`, `yaml-cell`, `yaml-row`, `raw`)
  - [ ] `--count`
  - [ ] `--trace-status`
  - [ ] `--relation`
  - [ ] `--anchor`
  - [ ] `--output` (`stdout` or file path)
  - [ ] `--no-prompt` (required for CI/scripted mode)
- [ ] Define output ordering and formatting guarantees so generated snippets are deterministic in shape.
- [ ] Define exit-code contract (`0` success, non-zero on validation/collision errors).
- [ ] Implement ID randomness with `secrets.choice` over explicit FLS-style alphanumeric alphabet.
- [ ] Validate generated outputs before emitting.
- [ ] Include generator terminology checks:
  - [ ] prompt text uses "IRM ID" and avoids legacy naming
  - [ ] help text and `--help` examples use "IRM ID" terminology

## 7) Full backfill rewrite design
- [ ] Build a one-to-one mapping `old_id -> new_id` for all existing IDs.
- [ ] Keep mapping deterministic within the run by storing it in memory and writing it to an artifact.
- [ ] Make dry-run default and require explicit apply mode.
- [ ] Dry-run must emit full mapping artifact plus per-file replacement counts.
- [ ] Apply mode must consume a mapping artifact (`--mapping-json`) instead of reminting IDs.
- [ ] Fail apply mode if mapping artifact is missing IDs discovered in source at execution time.
- [ ] Rewrite all ID-bearing locations in one migration pass:
  - [ ] markdown `{dp}` role IDs
  - [ ] markdown `{p}` references
  - [ ] YAML `cell_trace.*.irm_id`
  - [ ] YAML `_trace.irm_id`
  - [ ] legacy key rewrite: `source_id` -> `irm_id`
- [ ] Do not alter `trace_status`, `anchor_ids`, or `relation` unless formatting normalization is required.
- [ ] Fail migration if any old ID occurrence is left unresolved.
- [ ] Use atomic file writes to avoid partial rewrite when interrupted.
- [ ] Emit migration ledger artifact with:
  - [ ] old/new ID pairs
  - [ ] occurrence counts
  - [ ] touched file list
  - [ ] timestamp and tool version
- [ ] Write migration artifacts under `$SPHINX_MIGRATION_RUN_ROOT/artifacts/traceability/id-backfill/`.
- [ ] Ensure migration artifacts are ignored/untracked and never included in commits.

## 8) Validation and gating after rewrite
- [ ] Run strict repository checks after backfill:
  - [ ] `./make.py validate`
  - [ ] `./make.py build`
  - [ ] `SPHINX_MIGRATION_RUN_ROOT=<temp-run-root> ./make.py trace-validate`
  - [ ] `uvx black . --check --diff --color`
  - [ ] `uvx flake8 . --exclude .venv`
- [ ] Add/enable IRM ID lint checks:
  - [ ] format regex check
  - [ ] uniqueness check across markdown and YAML
  - [ ] unresolved `{p}` target check
  - [ ] run `paragraph_id_check.py` inside extension lint pipeline
- [ ] Add post-rewrite count invariants:
  - [ ] pre-backfill and post-backfill statement-unit ID totals match
  - [ ] every pre-backfill ID maps to exactly one post-backfill ID
  - [ ] no duplicate post-backfill IDs exist across markdown and YAML
- [ ] Verify no legacy positional patterns remain:
  - [ ] `SRCN-000...` markdown sequence patterns
  - [ ] table index-derived `SRCN-Txx-Rxxxx-Cxx` patterns
  - [ ] any non-`irm_` IDs in source metadata fields
- [ ] Run idempotency gate: second apply run with the same mapping must produce zero file diffs.

## 8A) Resume and recovery contract
- [ ] On interruption, resume from the latest completed artifacted checkpoint (inventory, mapping, rewrite, validation).
- [ ] Require checkpoint files before moving to next phase:
  - [ ] `inventory.json`
  - [ ] `id-mapping.json`
  - [ ] `rewrite-summary.json`
  - [ ] `validation-summary.json`
- [ ] Require explicit operator confirmation in logs when resuming from an existing mapping artifact.

## 9) Schema and contract updates
- [ ] Update IRM metadata schema expectations to enforce new `irm_id` pattern.
- [ ] Update any regex used in extension parsing/lints to match the new pattern.
- [ ] Ensure paragraph export schema remains compatible with new IDs.
- [ ] Enforce immediate strictness after migration: no compatibility window for `SRCN-*` in strict gates.
- [ ] Cutover field naming contract in S4: runtime and schemas require `irm_id`; reject `source_id`.

## 9A) Required code touchpoints checklist
- [ ] Update markdown preface parsing regex in `exts/iso26262_spec/preface_parser.py` to accept strict `irm_` IDs.
- [ ] Update legacy plain-text preface fallback parser so it rejects `SRCN-*` under strict mode after cutover.
- [ ] Add IRM ID shape checks in `exts/iso26262_spec_lints/paragraph_id_check.py` and orchestrate from `exts/iso26262_spec_lints/__init__.py`.
- [ ] Update decomposed extension imports/wiring in `exts/iso26262_spec/__init__.py`.
- [ ] Update `src/schemas/table_common.schema.json` to require `irm_id` and disallow `source_id` after S4.
- [ ] Update statement record ID constraints in `traceability/iso26262/schema/paragraph-ids.schema.json`.
- [ ] Update migration/instrumentation scripts in `tools/traceability/` so they no longer mint positional `SRCN-*` IDs.

## 9B) Paragraph ID check module and collision protections
- [ ] Implement `exts/iso26262_spec_lints/paragraph_id_check.py` with these checks:
  - [ ] IRM ID format validation (`^irm_[A-Za-z0-9]{12}$`)
  - [ ] uniqueness across markdown and YAML records
  - [ ] unresolved `{p}` references
  - [ ] statement-anchor collision detection with exact-anchor policy
- [ ] Ensure check runs in strict build/lint path and fails CI on findings.
- [ ] Add focused regression fixtures for near-collision IDs (case-only and punctuation-only differences).
- [ ] Document paragraph ID check contract and failure modes in runbook and migration notes.

## 10) Documentation updates
- [ ] Add generator usage section in `README.md`.
- [ ] Add generator workflow details in `docs/makepy-runbook.md`.
- [ ] Add short authoring rules:
  - [ ] use generator for new statements
  - [ ] move IDs with text when reordering
  - [ ] never manually reformat IDs
  - [ ] only mint new IDs for new statements
- [ ] Record full-backfill rationale and migration evidence in a dated doc artifact.

## 11) Execution sequencing (safe refactor first, then behavior changes)

### 11A) Safe refactor first (no intended behavior change)
- [ ] Stage S1 - Module extraction scaffolding only.
  - [ ] create target module files and move code without changing semantics
  - [ ] keep legacy behavior green after each extraction slice
  - [ ] keep `exts/iso26262_spec/__init__.py` as compatibility wiring during transition
- [ ] Stage S1 verification gate.
  - [ ] `./make.py validate`
  - [ ] `./make.py build`
  - [ ] `uvx black . --check --diff --color`
  - [ ] `uvx flake8 . --exclude .venv`
- [ ] Commit group A (safe only).
  - [ ] Commit A1: create modules + move shared types/nodes/roles/utils
  - [ ] Commit A2: extract parser/binding/store/events/output/domain/directives
  - [ ] Commit A3: split lint package orchestration and check modules (behavior preserved)

### 11B) Behavior-changing stages (controlled rollout)
- [ ] Stage S2 - IRM ID policy implementation (shadow mode only).
  - [ ] implement `paragraph_id_check.py` strict `irm_` regex checks in report-only mode
  - [ ] implement duplicate checks across markdown+YAML in report-only mode
  - [ ] implement unresolved `{p}` detection in report-only mode
  - [ ] do not fail repository gates on legacy IDs during S2
- [ ] Stage S2 verification gate.
  - [ ] shadow report flags seeded invalid fixtures
  - [ ] shadow report produced cleanly on repository source
  - [ ] strict hard-fail still disabled before S4
- [ ] Stage S3 - Tooling behavior introduction.
  - [ ] add interactive generator (`{dp}` + `{ts}` default templates)
  - [ ] add backfill tool with dry-run mapping artifact and apply-from-mapping mode
  - [ ] keep scope limited: no separate operator wrapper script
- [ ] Stage S3 verification gate.
  - [ ] generator interactive mode smoke test
  - [ ] generator non-interactive mode smoke test
  - [ ] backfill dry-run produces inventory/mapping/rewrite summary artifacts
- [ ] Stage S4 - One-time full backfill apply.
  - [ ] apply mapping to markdown + YAML + `{p}` references
  - [ ] migrate YAML/runtime key naming from `source_id` to `irm_id`
  - [ ] enforce immediate strict rejection of `SRCN-*` in strict gates
  - [ ] enable hard-fail mode in `paragraph_id_check.py` and schema validators
  - [ ] update schemas/contracts/docs accordingly
- [ ] Stage S4 verification gate.
  - [ ] `./make.py validate`
  - [ ] `./make.py build`
  - [ ] `SPHINX_MIGRATION_RUN_ROOT=<temp-run-root> ./make.py trace-validate`
  - [ ] `uvx black . --check --diff --color`
  - [ ] `uvx flake8 . --exclude .venv`
  - [ ] idempotency rerun (same mapping) yields zero diffs

### 11C) Commit and PR batching strategy
- [ ] Commit B1: checker module wiring in shadow mode (no strict cutover yet).
- [ ] Commit B2: generator + backfill tooling.
- [ ] Commit B3: full backfill source rewrite.
- [ ] Commit B4: schema/regex strictness cutover + docs + evidence.
- [ ] Push and monitor CI to green before merge.

### 11D) Suggested conventional commit messages
- [ ] `refactor(iso26262-spec): split extension into focused modules with thin __init__ wiring`
- [ ] `refactor(iso26262-spec-lints): split lint checks and add paragraph_id_check shadow mode`
- [ ] `feat(traceability): add IRM ID generator templates for {dp} and {ts}`
- [ ] `feat(traceability): add IRM ID backfill tooling with dry-run mapping artifacts`
- [ ] `chore(traceability): apply one-time IRM ID backfill across markdown, tables, and references`
- [ ] `feat(traceability)!: enable strict IRM cutover and reject legacy SRCN/source_id metadata`
- [ ] `docs(traceability): rename legacy ID terminology to IRM ID and publish migration evidence`

## 12) Risks and mitigations
- [ ] Risk: missing rewrite of a `{p}` reference causes unresolved links.
  - [ ] Mitigation: inventory + post-rewrite unresolved-reference lint.
- [ ] Risk: accidental semantic edits while touching files.
  - [ ] Mitigation: restrict rewrite to ID fields and role payloads; review focused diff.
- [ ] Risk: collisions from generated IDs.
  - [ ] Mitigation: repository-wide collision scan before final write.
- [ ] Risk: partial rewrite if script is interrupted.
  - [ ] Mitigation: dry-run default; atomic write strategy on apply mode.

## 13) Completion criteria
- [ ] All markdown and YAML statement IDs use the new canonical format.
- [ ] All IRM ID references are updated and resolvable.
- [ ] Full build/trace/style/lint checks pass.
- [ ] Interactive generator script is documented and usable for normal authoring.
- [ ] Migration ledger artifact exists and is attached to closeout evidence.
