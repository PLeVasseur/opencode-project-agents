# ISO 26262 Sphinx Migration Plan (Immediate Cutover, FLS-Style IDs/Roles, Durable v6)

Date: 2026-02-15
Status: Draft execution plan (enriched + hardened for clean-session execution + readability-first metadata placement + table semantics refinement + fresh-session operational hardening)
Priority: High
Plan type: Migration and integration plan

## 0) Stock-taking and plan relationship
- [x] This plan consolidates and operationalizes the two existing plans for a Sphinx-based pipeline.
  - [x] Source traceability plan: `plans/2026-02-14-iso26262-traceability-anchor-plan.md`.
  - [x] Critique remediation plan: `plans/2026-02-14-critique-remediation-plan.md`.
- [x] This plan does not relax the technical requirements of those plans.
  - [x] It defines migration sequencing, architecture, and run discipline to execute both in one Sphinx-first workflow.
  - [x] Any conflict resolves in this order: legal/safety constraints -> traceability invariants -> remediation content edits -> convenience.
- [x] Scope of this plan.
  - [x] Migrate document production and validation orchestration to Sphinx and custom extensions.
  - [x] Preserve source-embedded canonical traceability (no manual tracked mapping source-of-truth).
  - [x] Keep execution durable and resumable with explicit stage gates and artifacts.

## 1) Locked decisions (non-negotiable)
- [x] Immediate hard cutover to Sphinx.
  - [x] No dual-run migration phase.
  - [x] No temporary support for legacy placeholders (`{{TABLE: ...}}`, `{{PAGE_BREAK}}`, `{{BLANK}}`).
  - [x] All source is converted to Sphinx/MyST contracts early in the stage plan.
- [x] `make.py` + `uv` are the only supported execution interfaces.
  - [x] Operators run `uv run python make.py <command>` only.
  - [x] Direct `sphinx-build` invocation is not part of the workflow contract.
- [x] Sphinx + MyST are the canonical document stack.
  - [x] Keep Markdown authoring via `myst-parser`.
  - [x] Implement project-specific Sphinx extensions for traceability and lints.
- [x] FLS-style IDs and roles are mandatory for markdown statement instrumentation.
  - [x] Use role-defined statement IDs and role-defined references, mirroring FLS authoring ergonomics.
  - [x] Markdown paragraph/list-item statement units use a dedicated metadata preface line directly above content.
  - [x] Statement unit taxonomy is fixed: paragraph statements, list-item statements, and table cell entries.
  - [x] Every markdown statement-unit metadata preface includes `dp`; every preface also includes `ts`.
  - [x] Table cell-entry units carry equivalent metadata in structured YAML trace fields (`_trace` / `cell_trace`).
  - [x] Enforce placement and grammar with lints modeled on FLS lint behavior.
- [x] Canonical correlation remains source-embedded.
  - [x] Source files remain canonical for `source_id`, `trace_status`, and `anchor_ids`.
  - [x] ISO hierarchy JSONC remains canonical for anchor definitions and structure.
  - [x] Reverse indexes remain generated artifacts only.
- [x] Statement-level instrumentation is mandatory at closeout.
  - [x] Every statement unit in markdown and table YAML has stable `source_id`.
  - [x] Every statement unit carries a `source_id` marker (`dp` role preface for markdown units, `_trace`/`cell_trace` for YAML units) with no exceptions.
  - [x] Every statement unit has explicit `trace_status`.
  - [x] Mapped statements have one or more valid ISO anchors.
- [x] No copyrighted ISO text leakage in tracked outputs.
  - [x] Keep extracted raw text and low-level extraction artifacts under `.cache/` only.
  - [x] Keep tracked artifacts abstract, structural, and non-verbatim.
- [x] HTML is the required deliverable for this migration closeout.
  - [x] DOCX generation is not a migration requirement.
  - [x] Build quality and trace surfacing are validated against HTML output.
- [x] Migration is stage-gated and resumable.
  - [x] No phase is done without required artifacts and gate pass.
  - [x] Resume from earliest incomplete safe stage.

## 2) Mission and end-state
- [x] Deliver a Sphinx-based pipeline that can build, validate, and report a traceability-complete ISO 26262 Rust mapping document.
- [x] Integrate critique remediation execution into the same durable workflow so content edits cannot bypass traceability gates.
- [x] Produce deterministic assessor-ready outputs.
  - [x] HTML document under `build/html/`.
  - [x] Machine-readable and human-readable reports under `$OPENCODE_CONFIG_DIR/reports/`.
  - [x] Run logs, stage artifacts, and disposition ledger for auditability.

## 3) Target architecture (Sphinx-centric, FLS-inspired)
- [x] Content layer (canonical authoring).
  - [x] Narrative markdown remains canonical source (converted to pure MyST role/directive contracts).
  - [x] Table YAML remains canonical source (`src/tables/table-*.yaml`).
  - [x] Trace metadata remains embedded in source, not split into manual mapping files.
- [x] Sphinx path contract (explicit, no ambiguity).
  - [x] `docs/conf.py` is the Sphinx configuration directory (`confdir`).
  - [x] `src/` is the Sphinx source directory (`sourcedir`), including `src/index.md` as root toctree entrypoint.
  - [x] `src/iso26262_rust_mapping.md` is included from `src/index.md` and remains canonical narrative content.
  - [x] `build/doctrees/` and `build/html/` are the canonical Sphinx build outputs for this migration.
- [x] ISO anchor layer (canonical structure).
  - [x] `traceability/iso26262/**` JSONC hierarchy holds ISO part/unit/leaf anchors.
  - [x] Anchor schema and hierarchy integrity checks are enforced before build success.
- [x] Extension layer (split like FLS).
  - [x] `exts/iso26262_spec/` for domain, roles, directives, transforms, collectors, report writers.
  - [x] `exts/iso26262_spec_lints/` for lint checks wired to `env-check-consistency`.
  - [x] Extension setup declares `parallel_read_safe=True` and `parallel_write_safe=True` once verified.
- [x] Sphinx processing layer.
  - [x] `myst-parser` parses markdown.
  - [x] Custom domain and roles enforce statement IDs/references.
  - [x] Custom transforms and lints enforce statement-level invariants.
  - [x] Build-time report writers emit required JSON and Markdown coverage/remediation outputs.
- [x] Output layer.
  - [x] Primary build output: HTML (diagnostic + handoff).
  - [x] Traceability notes are surfaced in rendered output without ISO text leakage.
- [x] Operations layer.
  - [x] Resumable run root with lock/state/checklist/artifacts.
  - [x] Stage checkpoints and immutable run contract.

## 4) FLS-style ID and role contract (required)
- [x] Domain model mirrors FLS patterns.
  - [x] Add `TraceDomain` in `exts/iso26262_spec/__init__.py`.
  - [x] Domain owns role registrations, object types, object lookup, and cross-reference behavior.
  - [x] Domain data merge behavior is explicit for parallel builds.
- [x] Role set (FLS-like authoring model).
  - [x] `dp` role: defines statement `source_id` on the metadata preface line directly above the statement unit (analogous to FLS paragraph ID role).
  - [x] `p` role: references an existing statement ID (analogous to FLS paragraph reference role).
  - [x] `ts` role: defines `trace_status` token for the statement (`mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`).
  - [x] `trace-status` is a readable alias for `ts` in policy/docs; both map to the same metadata field.
  - [x] `a` role: references ISO anchor IDs from canonical JSONC registry.
  - [x] `rel` role: defines relation code (`direct`, `derived`, `supporting`, `contextual`).
- [x] MyST and RST syntax support.
  - [x] Policy notation uses FLS-style role names such as `:dp:` and `:ts:`.
  - [x] Markdown/MyST authoring uses parser-equivalent role syntax: `{dp}`...``, `{p}`...``, `{ts}`...``, `{a}`...``, `{rel}`...``.
  - [x] Metadata preface line format is canonical for readability and consistency.
  - [x] ReStructuredText role form remains available for parity with FLS docs where needed: `:dp:`...``, `:p:`...``.
- [x] ID grammar and stability.
  - [x] Preserve canonical `source_id` contract from traceability plan (stable, unique, immutable once assigned).
  - [x] `dp` role values must match approved source ID regex and uniqueness constraints.
  - [x] Existing IDs are preserved across reorder/move; new IDs minted only for new statements.
- [x] Placement rules (FLS-like lint strictness).
  - [x] Metadata preface line is required directly above each markdown paragraph/list-item statement unit.
  - [x] No blank line or non-metadata line may appear between metadata preface and bound markdown statement unit.
  - [x] Exactly one `dp` and exactly one `ts` are required per markdown statement-unit preface.
  - [x] Coverage is strict: every paragraph/list-item statement has a `dp` marker, and every table cell entry has a `source_id` marker via `_trace`/`cell_trace`.
  - [x] Table cell-entry metadata is validated via `_trace` / `cell_trace` fields rather than markdown preface lines.
  - [x] If `ts=mapped` (or YAML `trace_status=mapped`), at least one anchor reference is required (`a` role for markdown, `anchor_ids[]` for YAML).
  - [x] `rel` is required when `ts=mapped`.
- [x] Reference behavior.
  - [x] `p` resolves to statement anchors in rendered HTML.
  - [x] `a` resolves to ISO anchor detail pages or diagnostics without exposing ISO copyrighted text.
  - [x] Missing references are warnings during parse and hard failures at strict gate.
- [x] Paragraph ID export (FLS parity).
  - [x] Generate `build/html/paragraph-ids.json` from the in-memory bound statement map built from markdown `dp` preface lines and YAML `_trace`/`cell_trace` entries.
  - [x] Markdown statement units and table statement units are both exported into `paragraph-ids.json`.
  - [x] `paragraph-ids.json` validates against `reports/schemas/paragraph-ids.schema.json` (`schema_version=1`).
  - [x] Each record includes at minimum: statement `id`, display number, document link, checksum, `trace_status`, `anchor_ids`, `relation`, and source locator.
  - [x] Table cell-entry records use stable per-cell HTML anchors with canonical format: `<table_label>--r-<row_id>--c-<col_key>`.
  - [x] Build fails if `paragraph-ids.json` cannot be generated or is inconsistent with doctree statement inventory.
- [x] In-memory binding model (no extra canonical registry files).
  - [x] Collector binds each metadata preface line to the next valid statement unit node during doctree processing.
  - [x] Collector also ingests YAML `_trace` and `cell_trace` entries into the same in-memory statement map.
  - [x] Binding map exists only in Sphinx environment state and build artifacts; no additional tracked source-of-truth registry file is introduced.
  - [x] Exporters and validators consume the binding map, not raw line scanning.
  - [x] Orphan metadata prefaces, duplicate prefaces, or ambiguous bindings are hard failures.
- [x] Example authoring contract.

```md
{dp}`SRCN-01J3FQ8A7B4G4E9WQ2X5M6N7P8` {ts}`mapped` {rel}`direct` {a}`ISO26262:2018-ed2:P06:C05.4:P:003`
This statement defines the required coding-guideline rule.

See {p}`SRCN-01J3FQ8A7B4G4E9WQ2X5M6N7P8` for rationale linkage.
```

## 4A) Statement-unit boundary contract (authoritative)
- [x] Paragraph statement units (markdown).
  - [x] Each non-empty paragraph block is exactly one statement unit.
  - [x] Multi-sentence paragraphs remain one statement unit (explicitly not sentence-level instrumentation).
  - [x] Each paragraph statement unit has one metadata preface line directly above it.
- [x] List-item statement units (markdown).
  - [x] Each bullet/numbered list item text block is exactly one statement unit.
  - [x] Nested list items are independently instrumented statement units.
  - [x] Each list-item statement unit has one metadata preface line directly above it.
- [x] Cell-entry statement units (YAML-backed tables).
  - [x] Each non-empty table cell entry is a statement unit.
  - [x] Header/title cells are structural and are not statement units by default.
  - [x] Cell-entry trace metadata is recorded in `cell_trace.<col>` (and row-level metadata in `_trace` when applicable).
  - [x] Cell-entry units are validated to the same `source_id`/`trace_status`/anchor integrity rules as markdown units.
  - [x] Cell-entry units participate in `paragraph-ids.json` export with the same schema contract as markdown units.
- [x] Structural exclusions.
  - [x] Headings are structural and are not independently instrumented as statement units unless explicitly promoted by policy override.
  - [x] Whitespace, separators, and purely formatting constructs are never statement units.
- [x] Binding and adjacency invariants.
  - [x] One metadata preface line binds to exactly one immediate markdown paragraph/list-item statement unit.
  - [x] One markdown statement unit consumes exactly one metadata preface line.
  - [x] Ambiguous, duplicate, or orphan bindings are hard failures.

## 4B) Table trace semantics and precedence contract (authoritative)
- [x] Table trace precedence.
  - [x] `cell_trace` is authoritative for cell-entry statement units.
  - [x] Row `_trace` defines an optional row-level statement unit only; it does not implicitly satisfy missing cell-entry metadata.
  - [x] No inheritance fallback from `_trace` to `cell_trace` is allowed.
- [x] Double-count prevention.
  - [x] One statement unit emits one record in the in-memory statement map and one record in `paragraph-ids.json`.
  - [x] Row-level and cell-level units may coexist only when semantically distinct and IDs are unique.
  - [x] Duplicate semantic coverage caused by overlapping row/cell trace definitions is a hard failure.
- [x] Stable table identity and anchors.
  - [x] Traceable table rows use stable `row_id` values.
  - [x] `row_id` normalization for anchor generation is deterministic: lowercase, non-alphanumeric converted to `-`, repeated `-` collapsed, and leading/trailing `-` trimmed.
  - [x] Column-key normalization for anchor generation follows the same deterministic slug rules as `row_id`.
  - [x] Table cell anchor IDs use canonical format `<table_label>--r-<row_id>--c-<col_key>`.
  - [x] Reordering rows does not change existing `source_id` values when `row_id` is unchanged.

## 5) Directive and content conversion contract (immediate)
- [x] Legacy placeholders are removed, not shimmed.
  - [x] Replace `{{TABLE: table-XX}}` with a project MyST directive (````{iso-table} table-XX````).
  - [x] Remove `{{BLANK}}` placeholders.
  - [x] Remove `{{PAGE_BREAK}}` placeholders (HTML-first output does not require page-break tokens).
- [x] Deterministic conversion map (required for reproducible runs).
  - [x] `{{TABLE: table-XX}}` -> ````{iso-table} table-XX````.
  - [x] `{{PAGE_BREAK}}` -> removed, with section flow preserved by headings/toctree only.
  - [x] `{{BLANK}}` -> removed unless a semantic separator is needed (then replace with explicit subsection heading text).
  - [x] `<!-- fmt: ... -->` docgen hints -> removed from canonical source or translated into explicit MyST/Sphinx structures where semantically necessary.
- [x] Conversion quality gates.
  - [x] Pre/post counts must match for headings, table insertions, and list blocks unless an intentional change is recorded.
  - [x] Zero legacy tokens remain in canonical source after conversion.
  - [x] Any semantic reshaping requires artifacted rationale and source ID reconciliation notes.
- [x] Table directive contract.
  - [x] `iso-table` directive loads and renders a table from `src/tables/table-XX.yaml`.
  - [x] Required argument: table ID (`table-XX`) resolving to a single YAML table file.
  - [x] Required options for traceable tables: `:caption:` and `:label:`.
  - [x] `:label:` value is canonical table label and is used as the prefix for generated table cell anchor targets.
  - [x] Optional options: `:class:`, `:name:` (Sphinx-native styling/navigation only).
  - [x] Directive participates in trace validation by attaching table/row/cell trace nodes to doctree metadata.
  - [x] Directive fails fast on missing table files, unknown options, schema mismatch, or duplicate table labels.
- [x] Native MyST table policy.
  - [x] Traceable mapping tables must use `iso-table` (first-class project directive).
  - [x] A table is classified as traceable if its YAML payload includes `_trace` or `cell_trace` metadata, or if project policy marks the table as trace-required.
  - [x] Native MyST `{table}`, `{list-table}`, and `{csv-table}` are allowed only for non-trace informational tables.
  - [x] Using native MyST table directives for traceable mapping content is a hard lint failure.
- [x] Metadata directive contract (for non-preface edge cases only).
  - [x] Add compact `trace-meta` directive for structures where metadata preface lines are not practical.
  - [x] Directive compiles into the same internal node model used by role-based statements.
  - [x] Directive payload is not rendered as body text.
- [x] Canonical migrated table example (must be in docs and tests).
  - [x] Include one end-to-end example showing markdown `iso-table` invocation, YAML `row_id`, `_trace`, and `cell_trace`.
  - [x] Include expected `paragraph-ids.json` record examples for one markdown statement unit and one table cell-entry unit.
- [x] Immediate conversion policy.
  - [x] Convert all narrative source to role/directive contracts before downstream traceability implementation stages.
  - [x] No stage proceeds with mixed legacy/Sphinx syntax.

## 5A) Table schema migration contract (YAML trace metadata)
- [x] Canonical schema update requirements.
  - [x] Extend `src/schemas/table_common.schema.json` to support row-level `_trace` metadata.
  - [x] Add optional `cell_trace` maps for cell-level statement metadata where needed.
  - [x] Add stable `row_id` for traceable rows.
  - [x] Keep existing table semantic fields unchanged outside trace metadata additions.
- [x] Per-table schema compatibility rules.
  - [x] Each `table-XX.schema.json` continues to lock column keys and required semantic fields.
  - [x] Trace metadata keys are explicitly allowed and validated (not silently accepted as unknown properties).
  - [x] `additionalProperties` rules remain strict after trace metadata expansion.
- [x] Row and cell trace payload minimum fields.
  - [x] `row_id` is required for rows participating in trace exports.
  - [x] `_trace.source_id` and `_trace.trace_status` required for all row-level statements.
  - [x] `_trace.anchor_ids[]` required when `_trace.trace_status=mapped`.
  - [x] `cell_trace.<col>.source_id` and `cell_trace.<col>.trace_status` required for all cell-level statements.
  - [x] `cell_trace.<col>.anchor_ids[]` required when `cell_trace.<col>.trace_status=mapped`.
- [x] Row vs cell precedence and counting rules.
  - [x] `cell_trace` entries define cell-entry statement units.
  - [x] `_trace` defines optional row-level statement units only.
  - [x] `_trace` does not satisfy missing `cell_trace` fields.
  - [x] Overlapping row/cell trace definitions that cause duplicate semantic units are rejected.
- [x] Migration safety checks.
  - [x] Schema migration must not alter business/semantic table data fields.
  - [x] Existing YAML files are reformatted deterministically and pass schema validation after migration.
  - [x] Stable `row_id` population is deterministic and recorded in migration artifacts.
  - [x] All schema changes are covered by validation smoke artifacts in migration stages.

## 6) Sphinx event and lint pipeline (concrete)
- [x] Event hook plan.
  - [x] `config-inited`: validate required config and dependency versions.
  - [x] `builder-inited`: initialize run-scoped reporter context.
  - [x] `env-purge-doc`: drop per-doc trace objects during incremental rebuilds.
  - [x] `env-merge-info`: merge per-process trace/domain data in parallel mode.
  - [x] `doctree-read`: collect metadata preface lines, bind them to statement units, and collect table trace metadata.
  - [x] `doctree-resolved`: resolve cross-refs (`p`, `a`), finalize bindings, and render trace-note markers.
  - [x] `env-check-consistency`: run strict lints (FLS-like central lint gate).
  - [x] `build-finished`: emit coverage reports, `paragraph-ids.json`, and latest-pointer artifacts.
- [x] Transform and collector model.
  - [x] Collector stores statement objects in environment (FLS collector pattern).
  - [x] Collector builds in-memory metadata-preface -> statement-unit bindings for paragraph/list-item/cell-entry units.
  - [x] Post-transform replaces definition/ref nodes with final render/reference nodes.
  - [x] Collector and transform contracts are versioned with `env_version` in extension setup metadata.
- [x] Lint modules (`exts/iso26262_spec_lints/`).
  - [x] `require_paragraph_ids.py`: enforce `dp` placement/coverage rules for every statement unit (FLS-style parity).
  - [x] `require_trace_status.py`: enforce exactly one `ts` status per statement.
  - [x] `preface_adjacency.py`: enforce metadata preface adjacency (directly above target statement unit).
  - [x] `orphan_preface.py`: fail on metadata preface lines that do not bind to exactly one statement unit.
  - [x] `traceable_table_usage.py`: enforce `iso-table` usage for traceable mapping tables.
  - [x] `table_trace_coverage.py`: enforce required `_trace`/`cell_trace` coverage and `row_id` requirements.
  - [x] `table_trace_precedence.py`: enforce row/cell precedence contract and no double-count overlap.
  - [x] `table_anchor_targets.py`: enforce canonical per-cell anchor target format and uniqueness.
  - [x] `anchor_resolution.py`: enforce mapped statements have resolvable anchor refs.
  - [x] `id_uniqueness.py`: enforce no duplicate or malformed source IDs.
  - [x] `no_legacy_tokens.py`: fail if legacy placeholder tokens exist.
- [x] Strict warning policy.
  - [x] Build runs with warnings-as-errors and no unapproved suppressions.
  - [x] `show_warning_types` enabled for diagnosability.
  - [x] `suppress_warnings` restricted to explicitly documented, temporary exceptions.

## 7) Migration strategy (immediate hard cutover)
- [x] Hard-cutover approach.
  - [x] Establish Sphinx skeleton and extension contracts.
  - [x] Immediately convert all source content to MyST roles/directives.
  - [x] Remove legacy parser assumptions from workflow contract.
- [x] Compatibility stance.
  - [x] Structural/content parity is measured against source semantics, not DOCX byte-level parity.
  - [x] Existing `validate/build/verify` command ergonomics are retained through `make.py`, with Sphinx behavior under the hood.
- [x] Completion criterion.
  - [x] All document generation, validation, and reporting operate through Sphinx + custom extensions only.

## 8) Durable and resumable execution contract
- [x] Run root convention.
  - [x] `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/`.
  - [x] Required files: `state.env`, `checklist.state.env`, `run.log`, `artifacts/`, `run.lock`.
- [x] Immutable run contract fields (write once at bootstrap).
  - [x] `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`.
  - [x] `BASE_BRANCH`, `TARGET_BRANCH`, `BASE_PIN_SHA`, `EXPECTED_OLD_REMOTE_SHA`.
  - [x] `SOURCE_PDFSET_ID`, `P06_SHA256`, `P08_SHA256`, `P09_SHA256`.
  - [x] `SPHINX_VERSION_PIN`, `MYST_VERSION_PIN`.
  - [x] `TRACEABILITY_PLAN_PATH`, `CRITIQUE_PLAN_PATH`.
  - [x] `COMMIT_LEDGER_FILE`, `COMMIT_LEDGER_JSON_FILE`.
- [x] Mutable stage fields.
  - [x] `CURRENT_STAGE`, `LAST_COMPLETED_STAGE`, `STAGE_STATUS`.
  - [x] `LAST_GATE_RESULT`, `LAST_GATE_FAILURE_REASON`.
  - [x] `LAST_ARTIFACT_UPDATE_UTC`, `LAST_RESUME_HINT`.
- [x] Stage schema contract (explicit M-stage keys, no ambiguity).
  - [x] `CURRENT_STAGE` values are `M0..M14` only.
  - [x] `M0_DONE..M14_DONE` are explicit `0|1` values.
  - [x] `M0_CHECKLIST_DONE..M14_CHECKLIST_DONE` are explicit `0|1` values.
  - [x] If legacy `S*` keys are present from templates, they are migrated/ignored and never used as execution truth.
- [x] Checklist discipline.
  - [x] Each stage has explicit checklist keys with `0|1` values (example: `CB_M3_NO_LEGACY_TOKENS=1`).
  - [x] Stage close requires all required checklist keys set to `1`.
- [x] Lock discipline.
  - [x] Acquire lock before state mutation.
  - [x] Use atomic writes via `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" <write|update> ...`.
  - [x] Release lock only at stage completion or controlled pause.
- [x] Resume rules.
  - [x] Resume from earliest incomplete stage.
  - [x] If stage marked done but gate artifact missing, reopen that stage.
  - [x] If remote state unknown, reconcile before commit/push stages.
  - [x] If run interrupted in closeout, resume closeout only.

## 8A) Session-zero preflight (mandatory, copy/paste-safe)
- [x] Execute preflight in this exact order for new runs.
  - [x] `printenv OPENCODE_CONFIG_DIR` and verify expected config root path.
  - [x] `uv sync` from repository root.
  - [x] `REPO_ROOT="$(pwd)"` from repository root.
  - [x] `BASE_BRANCH="${BASE_BRANCH:-main}"`.
  - [x] `CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"`.
  - [x] `RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)`.
  - [x] If `CURRENT_BRANCH==BASE_BRANCH`, create and switch to `TARGET_BRANCH="docs/iso26262-sphinx-traceability-migration-$RUN_ID"`; otherwise set `TARGET_BRANCH="$CURRENT_BRANCH"`.
  - [x] `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/bootstrap_sphinx_migration_run.py" --repo-root "$REPO_ROOT" --run-id "$RUN_ID" --base-branch "$BASE_BRANCH" --target-branch "$TARGET_BRANCH"`.
  - [x] Capture emitted `RUN_ROOT` and export it for remaining commands.
- [x] Preflight post-conditions.
  - [x] Run root exists with state/checklist/log/artifact paths.
  - [x] `state.env` contains immutable bootstrap keys at minimum: `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`, `ARTIFACT_ROOT`, `LOCK_FILE`, `REPORT_FILE`, `STARTED_AT_UTC`, `BASE_BRANCH`, `TARGET_BRANCH`, `TARGET_REMOTE`, `COMMIT_LEDGER_FILE`, `COMMIT_LEDGER_JSON_FILE`.
  - [x] `TARGET_BRANCH!=BASE_BRANCH` for mutating stages.
  - [x] `checklist.state.env` includes `M0..M14` lifecycle checklist keys and task-specific `CB_M*_*` keys.
  - [x] `run.log` exists and has a bootstrap entry with `RUN_ID` and timestamp.
  - [x] `CURRENT_STAGE` is set to `M0` and M-stage key set is materialized before execution continues.

## 8B) Required durable key seed set (minimum)
- [x] State keys that must exist before `M1` starts.
  - [x] `CURRENT_STAGE=M0`.
  - [x] `M0_DONE=0` ... `M14_DONE=0`.
  - [x] `M0_CHECKLIST_DONE=0` ... `M14_CHECKLIST_DONE=0`.
  - [x] `LAST_COMPLETED_STAGE=` and `STAGE_STATUS=in_progress`.
- [x] Checklist keys that must exist before `M1` starts.
  - [x] `CB_M0_STAGE_START=0` ... `CB_M14_STAGE_START=0`.
  - [x] `CB_M0_STAGE_COMPLETE=0` ... `CB_M14_STAGE_COMPLETE=0`.
  - [x] `CB_M0_BRANCH_CONTRACT_VALID=0`.
  - [x] `CB_M0_COMMIT_LEDGER_INITIALIZED=0`.
  - [x] `CB_M2_PATH_CONTRACT_LOCKED=0`.
  - [x] `CB_M2_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M3_NO_LEGACY_TOKENS=0`.
  - [x] `CB_M3_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M6_SCHEMA_TRACE_MIGRATED=0`.
  - [x] `CB_M6_TABLE_PRECEDENCE_GREEN=0`.
  - [x] `CB_M6_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M8_LINT_STRICT_GREEN=0`.
  - [x] `CB_M8_TRACEABLE_TABLE_USAGE_GREEN=0`.
  - [x] `CB_M8_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M10_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M12_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M14_PHASE_COMMIT_CREATED=0`.
  - [x] `CB_M13_CLEAN_ROOM_VERIFY_GREEN=0`.
- [x] Key management rules.
  - [x] All state/checklist keys are explicit `0|1` or explicit scalar strings; no implicit/missing semantics.
  - [x] New checklist keys are added before entering the stage that consumes them.
  - [x] Stage close fails if any required key is missing or unset.

## 8C) Fresh-session run discovery and lock contract (mandatory)
- [x] Deterministic run discovery algorithm.
  - [x] Candidate run roots match: `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-*`.
  - [x] A run is considered incomplete if any of: `M14_DONE!=1`, `M14_CHECKLIST_DONE!=1`, missing `artifacts/summary.md`, missing commit-ledger artifacts, or missing required closeout reports.
  - [x] Select newest incomplete run by parsed `RUN_ID` timestamp; if timestamp parse fails, fall back to filesystem `mtime`.
  - [x] If no incomplete run exists and no explicit `RUN_ID` is provided, bootstrap a new run.
- [x] Lock file metadata format.
  - [x] Lock file path is `state.env:LOCK_FILE` and must be under `RUN_ROOT`.
  - [x] Lock payload includes: `pid`, `host`, `user`, `run_id`, `acquired_at_utc`.
  - [x] Active valid lock is a hard stop condition.
  - [x] Stale lock reconciliation appends prior lock contents to `run.log` before replacement.
  - [x] Lock is always released on normal exit and recorded failure exit.

## 8D) Branch and phased-commit contract (mandatory)
- [x] Branch strategy.
  - [x] All mutating work occurs on `TARGET_BRANCH`; direct mutation on `BASE_BRANCH` is forbidden.
  - [x] `TARGET_BRANCH` must diverge from `BASE_BRANCH` before any stage beyond `M0` can start.
  - [x] If execution starts on `BASE_BRANCH`, create run-scoped migration branch: `docs/iso26262-sphinx-traceability-migration-<run-id>`.
  - [x] `BASE_PIN_SHA` is recorded at branch bootstrap and used for replay/debug comparisons.
- [x] Commit strategy.
  - [x] Commits are phased and aligned with stage boundaries; no omnibus end-only commit.
  - [x] Each phase commit is created only after its stage gate is green.
  - [x] Commit messages follow Conventional Commits and explain intent (why), not only file movement.
  - [x] Commit groups remain logically scoped to one migration concern at a time.
- [x] Commit durability artifacts.
  - [x] `COMMIT_LEDGER_FILE` and `COMMIT_LEDGER_JSON_FILE` are initialized during `M0`.
  - [x] Each phase commit appends: `stage_or_stage_range`, `commit_sha`, `subject`, `timestamp_utc`, and artifact pointers.
  - [x] Use `reports/tooling/record_phase_commit.py` to append commit checkpoints idempotently.
  - [x] Resume reconciliation reads commit ledger before deciding whether a phase must be re-run.

## 9) Stage plan (detailed)

### M0) Bootstrap and contract pinning
- [x] Initialize run root, lock, and state files.
- [x] Use `reports/tooling/bootstrap_sphinx_migration_run.py` for deterministic run bootstrap and M-stage schema materialization.
- [x] Materialize explicit M-stage state/checklist keys (`M0..M14`, `CB_M*_*`) with `0|1` values.
- [x] Migrate or ignore any template `S*` keys so M-stage keys are the only execution truth.
- [x] Enforce branch contract (`TARGET_BRANCH!=BASE_BRANCH`) before mutating stages.
- [x] Initialize commit durability artifacts (`COMMIT_LEDGER_FILE`, `COMMIT_LEDGER_JSON_FILE`).
- [x] Pin immutable run contract values and plan references.
- [x] Capture current repository and dependency baseline.
- [x] Record explicit resume command and handoff hint.

### M1) Baseline capture and migration readiness
- [x] Record baseline outputs and metrics from current repository state.
  - [x] Existing command behavior and source inventories.
  - [x] Statement and table-node count snapshots.
- [x] Capture baseline traceability status snapshot from existing plans and tooling.

### M2) Sphinx skeleton and dependency pinning
- [x] Add Sphinx project skeleton and strict configuration.
  - [x] `docs/conf.py` with strict warnings.
  - [x] Build path contract locked: `confdir=docs`, `sourcedir=src`, `outdir=build/html`, `doctreedir=build/doctrees`.
  - [x] Add `src/index.md` as root toctree entrypoint and include canonical narrative content pages.
  - [x] `myst-parser` configuration and source suffix policy.
  - [x] Extension import path wiring for `exts/iso26262_spec*`.
- [x] Pin dependencies in `pyproject.toml` with `uv` lock update.
- [x] Produce first strict Sphinx smoke build through `make.py` only.
- [x] Create phase commit for Sphinx skeleton/pinning and record in commit ledger.

### M3) Immediate source conversion to MyST contracts
- [x] Convert narrative markdown to Sphinx/MyST-native syntax.
  - [x] Replace all legacy placeholders with directives/clean markdown.
  - [x] Normalize headings/sections for deterministic TOC behavior.
  - [x] Remove legacy docgen-only formatting constructs.
  - [x] Insert metadata preface lines directly above each paragraph/list-item statement unit.
- [x] Apply deterministic conversion map from Section 5 and capture pre/post inventories.
- [x] Add conversion audit proving zero remaining legacy tokens.
- [x] Create phase commit for immediate source conversion and record in commit ledger.

### M4) FLS-style domain, IDs, and role scaffold
- [x] Implement `TraceDomain` and role nodes (`dp`, `p`, `ts`, `a`, `rel`).
- [x] Implement object storage, object lookup, and cross-reference creation.
- [x] Implement statement/section collectors, in-memory binding map, and `paragraph-ids.json` exporter contract (FLS-style output parity).
- [x] Add setup metadata, config values, and `env_version` discipline.
- [x] Produce extension smoke test report.

### M5) Statement segmentation and markdown instrumentation enforcement
- [x] Implement deterministic statement segmentation per Section 4A paragraph/list-item/cell-entry unit contract.
- [x] Enforce `dp` and `ts` role presence on all markdown paragraph/list-item statement units.
- [x] Enforce equivalent `source_id`/`trace_status` field presence on all YAML cell-entry statement units.
- [x] Validate metadata preface placement constraints (directly above statement unit, no gap).
- [x] Emit missing/duplicate/malformed source ID reports.

### M6) YAML table traceability and `iso-table` integration
- [x] Implement `iso-table` directive for YAML-backed rendering.
- [x] Migrate table schemas to trace-aware contracts per Section 5A before enforcing row/cell metadata gates.
- [x] Parse and validate row/cell `_trace` metadata and status contracts.
- [x] Enforce row/cell precedence rules and no-double-count semantics.
- [x] Enforce stable `row_id` and canonical per-cell anchor target format.
- [x] Attach YAML trace nodes to unified statement ledger.
- [x] Emit YAML-specific coverage and exception reports.
- [x] Create phase commit for table trace integration and record in commit ledger.

### M7) ISO anchor registry and reference integrity
- [x] Load ISO JSONC anchor hierarchy into registry.
- [x] Validate anchor grammar and hierarchy link consistency.
- [x] Validate all mapped source nodes resolve to known anchor IDs.
- [x] Emit unknown/dangling/orphan integrity reports.

### M8) Lints and strict consistency gate
- [x] Implement `iso26262_spec_lints` module set.
- [x] Connect lints to `env-check-consistency`.
- [x] Enforce no-legacy-token lint, preface-adjacency lint, and orphan-preface lint.
- [x] Enforce traceable-table-usage lint and table-precedence/no-double-count lint.
- [x] Promote all lint warnings to strict gate failures via build policy.
- [x] Create phase commit for lint and consistency gate expansion and record in commit ledger.

### M9) Report generation and reverse index generation
- [x] Generate run-scoped statement coverage JSON and Markdown reports.
- [x] Generate and validate `build/html/paragraph-ids.json` from in-memory bound statement map.
- [x] Validate table-derived `paragraph-ids.json` entries (row/cell units) and anchor targets.
- [x] Generate reverse indexes under `.cache/iso26262/indexes/` (untracked).
- [x] Generate latest-pointer report files under `$OPENCODE_CONFIG_DIR/reports/`.
- [x] Validate report schemas and minimum required sections.

### M10) `make.py` orchestration contract completion
- [x] Implement/replace `make.py` commands for Sphinx workflow only.
  - [x] `validate`, `build`, `trace-validate`, `trace-report`, `verify`.
  - [x] Optional one-shot `migrate-sphinx` helper for reproducible conversion.
- [x] Ensure commands call Sphinx internals from Python and never require direct `sphinx-build` usage by operators.
- [x] Update README workflow to `uv run python make.py ...` examples only.
- [x] Create phase commit for CLI/orchestration contract updates and record in commit ledger.

### M11) Critique remediation execution within Sphinx gates
- [x] Execute critique claim remediation stages under Sphinx validation contract.
- [x] Require traceability reconciliation after each remediation stage batch.
- [x] Block advancement on missing statement metadata or unresolved required mappings.
- [x] Emit stage evidence mapping claims -> edits -> traceability outcomes.

### M12) Full-document instrumentation freeze
- [x] Run full source instrumentation audit (markdown + YAML).
- [x] Enforce zero missing `source_id` and zero missing `trace_status` for all statements.
- [x] Reconcile moved/reordered statements while preserving existing IDs.
- [x] Freeze statement ledger snapshot for closeout audit.
- [x] Create phase commit for instrumentation freeze and record in commit ledger.

### M13) Integrated validation and HTML quality gates
- [x] Run strict Sphinx build gates via `make.py`.
- [x] Run traceability validators and report validators.
- [x] Confirm report completeness and latest-pointer updates.
- [x] Confirm no-leak checks over tracked artifacts.
- [x] Execute clean-room reproducibility check (`uv sync` + `uv run python make.py verify`) and artifact log.

### M14) Canonical cutover closeout and legacy retirement
- [x] Mark Sphinx pipeline as canonical path in docs and command defaults.
- [x] Retire legacy DOCX/docgen assumptions from workflow docs.
- [x] Write final disposition ledger and run summary.
- [x] Create final phase commit for closeout artifacts/docs and record in commit ledger.
- [x] Release lock and finalize resumable state.

## 10) Stage artifact checklist (required)
- [x] `M0` artifacts.
  - [x] `artifacts/bootstrap/contract.json`.
  - [x] `artifacts/bootstrap/state-init.log`.
  - [x] `artifacts/bootstrap/m-stage-schema-init.log`.
  - [x] `artifacts/bootstrap/run-bootstrap-summary.json`.
  - [x] `artifacts/bootstrap/lock-contract-check.md`.
  - [x] `artifacts/bootstrap/branch-contract.json`.
  - [x] `artifacts/commits/commit-ledger.md`.
  - [x] `artifacts/commits/commit-ledger.json`.
- [x] `M1` artifacts.
  - [x] `artifacts/baseline/current-state-baseline.md`.
  - [x] `artifacts/baseline/source-statement-inventory.json`.
- [x] `M2` artifacts.
  - [x] `artifacts/sphinx/skeleton-smoke.log`.
  - [x] `artifacts/sphinx/version-pin-record.json`.
  - [x] `artifacts/sphinx/path-contract.md`.
- [x] `M3` artifacts.
  - [x] `artifacts/source/myst-conversion-report.md`.
  - [x] `artifacts/source/no-legacy-token-scan.json`.
  - [x] `artifacts/source/conversion-prepost-inventory.json`.
- [x] `M4` artifacts.
  - [x] `artifacts/traceability/domain-role-smoke-results.json`.
  - [x] `artifacts/traceability/domain-setup-metadata.json`.
  - [x] `artifacts/traceability/paragraph-ids-export-smoke.json`.
- [x] `M5` artifacts.
  - [x] `artifacts/source/statement-segmentation-report.json`.
  - [x] `artifacts/source/source-id-role-audit.json`.
  - [x] `artifacts/source/preface-binding-audit.json`.
- [x] `M6` artifacts.
  - [x] `artifacts/source/yaml-trace-coverage.json`.
  - [x] `artifacts/source/iso-table-render-smoke.md`.
  - [x] `artifacts/source/table-schema-migration-report.md`.
  - [x] `artifacts/source/table-trace-precedence-audit.json`.
  - [x] `artifacts/source/table-anchor-format-audit.json`.
  - [x] `artifacts/source/iso-table-canonical-example.md`.
- [x] `M7` artifacts.
  - [x] `artifacts/iso/anchor-registry-integrity.json`.
  - [x] `artifacts/iso/source-anchor-resolution.json`.
- [x] `M8` artifacts.
  - [x] `artifacts/lints/lint-summary.json`.
  - [x] `artifacts/lints/no-legacy-token-lint.log`.
  - [x] `artifacts/lints/preface-adjacency-lint.log`.
  - [x] `artifacts/lints/orphan-preface-lint.log`.
  - [x] `artifacts/lints/traceable-table-usage-lint.log`.
  - [x] `artifacts/lints/table-trace-coverage-lint.log`.
  - [x] `artifacts/lints/table-trace-precedence-lint.log`.
  - [x] `artifacts/lints/table-anchor-targets-lint.log`.
- [x] `M9` artifacts.
  - [x] `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/traceability-statement-coverage.json`.
  - [x] `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/traceability-statement-coverage.md`.
  - [x] `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.json`.
  - [x] `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.md`.
  - [x] `build/html/paragraph-ids.json`.
  - [x] `artifacts/traceability/paragraph-ids-schema-validation.json`.
  - [x] `artifacts/traceability/paragraph-ids-table-entry-audit.json`.
  - [x] `artifacts/indexes/source_to_anchor.stats.json`.
  - [x] `artifacts/indexes/anchor_to_source.stats.json`.
- [x] `M10` artifacts.
  - [x] `artifacts/cli/command-contract.md`.
  - [x] `artifacts/cli/command-smoke.log`.
- [x] `M11` artifacts.
  - [x] `artifacts/critique/claim-to-edit-ledger.csv`.
  - [x] `artifacts/critique/stage-evidence.md`.
- [x] `M12` artifacts.
  - [x] `artifacts/source/full-document-source-id-audit.json`.
  - [x] `artifacts/source/full-document-trace-status-audit.json`.
  - [x] `artifacts/source/freeze-ledger.md`.
- [x] `M13` artifacts.
  - [x] `artifacts/validation/sphinx-strict-build.log`.
  - [x] `artifacts/validation/integrated-validator-summary.json`.
  - [x] `artifacts/validation/no-leak-validation.json`.
  - [x] `artifacts/validation/clean-room-verify.log`.
  - [x] `artifacts/validation/trace-validate.log`.
- [x] `M14` artifacts.
  - [x] `artifacts/disposition/final-ledger.md`.
  - [x] `artifacts/commits/commit-ledger.md` (finalized).
  - [x] `artifacts/commits/commit-ledger.json` (finalized).
  - [x] `artifacts/summary.md`.

## 11) Validation gates (must pass)
- [x] Sphinx strict gate.
  - [x] Strict build runs from `make.py` command path only.
  - [x] Warnings-as-errors with no unapproved suppressions.
- [x] Durable state schema gate.
  - [x] `CURRENT_STAGE` and stage completion keys use `M0..M14` schema only.
  - [x] Required `CB_M*_*` checklist keys exist and are explicit `0|1` values.
- [x] Run bootstrap and lock gate.
  - [x] Fresh-session run discovery selects the correct incomplete run or bootstraps a new run deterministically.
  - [x] Lock metadata format is valid and stale-lock reconciliation behavior is logged.
- [x] Branch discipline gate.
  - [x] `TARGET_BRANCH!=BASE_BRANCH` for all mutating stages (`M1..M14`).
  - [x] `TARGET_BRANCH` exists and HEAD matches `state.env:TARGET_BRANCH`.
  - [x] `BASE_PIN_SHA` remains reachable from run history for reconciliation.
- [x] Legacy syntax elimination gate.
  - [x] Zero occurrences of `{{TABLE:`, `{{PAGE_BREAK}}`, `{{BLANK}}` in canonical source.
- [x] FLS-style role coverage gate.
  - [x] Every markdown paragraph/list-item statement unit has exactly one `dp` and one `ts`.
  - [x] Metadata preface line appears directly above every markdown paragraph/list-item statement unit.
  - [x] No blank/non-metadata line separates preface and bound markdown statement unit.
  - [x] Table cell-entry units satisfy equivalent `_trace` / `cell_trace` metadata requirements.
  - [x] Markdown `ts=mapped` statements include `a` role refs and a `rel` role.
- [x] Table semantics gate.
  - [x] Traceable tables use `iso-table` directive.
  - [x] `row_id` is present for trace-exported rows.
  - [x] Row/cell precedence contract is satisfied with no inheritance fallback and no duplicate semantic units.
  - [x] Header/title cells are excluded from statement-unit exports by default.
- [x] Paragraph ID export gate.
  - [x] `build/html/paragraph-ids.json` exists and validates against schema.
  - [x] `paragraph-ids.json` inventory count equals statement-unit inventory count from instrumentation collectors.
  - [x] `paragraph-ids.json` is generated from in-memory bound statement map, not raw line scanning.
  - [x] `paragraph-ids.json` includes both markdown-derived and table-derived statement-unit entries.
  - [x] Table-derived entries use canonical per-cell anchor format `<table_label>--r-<row_id>--c-<col_key>`.
  - [x] Each paragraph-ID record resolves to a valid HTML anchor target.
- [x] Source instrumentation gate.
  - [x] Every statement unit has stable `source_id` and explicit `trace_status`.
  - [x] Mapped statements resolve to valid anchor IDs.
- [x] ISO hierarchy gate.
  - [x] JSONC files are schema-valid with consistent parent-child links.
- [x] Integrity gate.
  - [x] No duplicate `source_id` values.
  - [x] No malformed ID values.
  - [x] No orphan metadata preface lines.
  - [x] No unknown anchor references.
  - [x] No orphan required units/leaves.
- [x] No-leak gate.
  - [x] No prohibited verbatim ISO text fields in tracked files.
  - [x] No watermark/license/order/email leakage in tracked files.
- [x] Reporting gate.
  - [x] Required JSON and Markdown reports exist and pass schema/section checks.
- [x] Phased commit gate.
  - [x] Phase commits exist for required checkpoint stages and are recorded in commit ledger.
  - [x] Commit messages follow Conventional Commits and align to migration concerns.
  - [x] No mutation commits are made directly on `BASE_BRANCH`.
- [x] Remediation gate.
  - [x] Critique claim dispositions are complete and evidence-backed.
  - [x] Required unresolved counts are zero at closeout.
- [x] Clean-room reproducibility gate.
  - [x] From a fresh session: `uv sync` then `uv run python make.py verify` succeeds without manual bootstrapping steps outside this plan.
  - [x] Runbook/prompt instructions are sufficient for a first-time operator to reproduce success.

## 12) Integration map (traceability plan + critique plan -> migration stages)
- [x] Traceability plan integration.
  - [x] `S0-S3` map to migration `M0-M4` (bootstrap, contracts, scaffold, role/domain foundation).
  - [x] `S4-S6` map to migration `M6-M9` (ISO anchors, source embedding, indexes/reports).
  - [x] `S7-S9` map to migration `M10-M14` (rendering, freeze, validation/closeout).
- [x] Critique remediation integration.
  - [x] `CR0-CR1` run during migration `M0-M1` (bootstrap and claim normalization).
  - [x] `CR2-CR7` run during migration `M11` with Sphinx gate enforcement.
  - [x] `CR8-CR10` run during migration `M12-M13` (trace reconciliation + integrated validation).
  - [x] `CR11-CR12` run during migration `M13-M14` (reporting and final handoff).
- [x] Advancement rule.
  - [x] No critique stage may close with red traceability gates.

## 13) `make.py` and workflow contract (mandatory)
- [x] Operator-facing command contract (`uv` only).
  - [x] `uv run python make.py validate`.
  - [x] `uv run python make.py build` (HTML build).
  - [x] `uv run python make.py trace-validate` (full traceability integrity gate, including paragraph-ID consistency).
  - [x] `uv run python make.py trace-report`.
  - [x] `uv run python make.py verify` (validate + build + report + strict gates).
  - [x] Optional one-shot `uv run python make.py migrate-sphinx` for deterministic source conversion.
- [x] Internal invocation policy.
  - [x] `make.py` may call Sphinx Python APIs or subprocesses internally.
  - [x] Workflow docs and runbooks never require direct `sphinx-build` usage.
- [x] Durable run helper commands.
  - [x] `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" write "$RUN_ROOT/state.env" key=value ...` (initialize write-once snapshots where required).
  - [x] `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" update "$RUN_ROOT/state.env" key=value ...` (all normal state/checklist updates).
  - [x] `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/record_phase_commit.py" --run-root "$RUN_ROOT" --stage-checkpoint "M<N>"` (idempotent phase commit ledger update).
  - [x] State reads are done by sourcing env files or parser helpers in the execution prompt; `state_tool.py` has no standalone `get` command.
- [x] Session startup sequence.
  - [x] Resolve run root from explicit `RUN_ID` or latest incomplete run.
  - [x] Validate immutable contract fields.
  - [x] Validate branch contract (`TARGET_BRANCH` exists, checked out, and differs from `BASE_BRANCH` for mutating stages).
  - [x] Validate commit ledger files exist and are writable before phase commits.
  - [x] Resume earliest incomplete stage.

## 13A) `trace-validate` command contract (normative)
- [x] `uv run python make.py trace-validate` required behavior.
  - [x] Run strict traceability checks without relying on manual post-processing.
  - [x] Validate markdown metadata preface coverage and adjacency constraints.
  - [x] Validate YAML table `_trace`/`cell_trace` coverage, `row_id` requirements, and row/cell precedence/no-double-count rules.
  - [x] Validate anchor resolution for mapped markdown and YAML statement units.
  - [x] Validate `paragraph-ids.json` schema, statement-unit inventory parity, and anchor target reachability.
  - [x] Validate zero legacy placeholder tokens in canonical source.
- [x] Exit and artifact behavior.
  - [x] Exit code `0` only when all required traceability checks pass.
  - [x] Exit code non-zero on first failed hard gate and emit actionable diagnostics.
  - [x] Write detailed failure diagnostics to `artifacts/validation/trace-validate.log`.
  - [x] Update run-scoped summary artifacts with pass/fail counts by check family.

## 14) `pyproject.toml` and dependency policy (`uv` managed)
- [x] Add and pin Sphinx stack dependencies in project metadata.
  - [x] `sphinx` pinned to a tested major/minor patch line for the migration run.
  - [x] `myst-parser` pinned to a tested version compatible with the chosen Sphinx version.
  - [x] Keep `PyYAML` and `jsonschema` for YAML/source validation.
- [x] Version-pair compatibility gate.
  - [x] Record the tested `sphinx` + `myst-parser` pair in `artifacts/sphinx/version-pin-record.json`.
  - [x] Block stage close if runtime versions drift from the pinned pair.
- [x] Remove DOCX-only runtime dependencies from canonical migration target when no longer needed.
  - [x] `python-docx` and `pillow` are retired after Sphinx cutover is verified.
- [x] Keep development tool dependencies in `dependency-groups.dev`.
  - [x] Include test/lint/build helper packages required for extension validation.
- [x] Lock and reproducibility policy.
  - [x] Dependency changes are applied with `uv` and lockfile updates.
  - [x] Version pins are recorded in run artifacts for audit replay.

## 15) Risk register and mitigations
- [x] Risk: immediate conversion causes broad content churn.
  - [x] Mitigation: deterministic conversion pass + explicit `no_legacy_token` gate.
  - [x] Mitigation: preserve stable source IDs; reconcile only where structurally necessary.
- [x] Risk: role-heavy markup harms readability.
  - [x] Mitigation: metadata preface line directly above each markdown paragraph/list-item statement unit for human scanning.
  - [x] Mitigation: lint hints with actionable remediation messages.
- [x] Risk: doctree segmentation mismatch vs expected statement boundaries.
  - [x] Mitigation: deterministic segmentation tests and fixture corpus.
  - [x] Mitigation: freeze segmentation contract at M12.
- [x] Risk: extension complexity causes build instability.
  - [x] Mitigation: stage isolation (domain, directives, lints, reports) and smoke gates.
- [x] Risk: source ID churn during critique remediation edits.
  - [x] Mitigation: reconciliation tooling preserving existing IDs and flagging churn.
- [x] Risk: table row/cell trace overlap creates duplicate statement accounting.
  - [x] Mitigation: explicit row/cell precedence rules with no inheritance fallback.
  - [x] Mitigation: dedicated table-precedence lint and paragraph-ID table-entry audits.
- [x] Risk: accidental ISO text leakage.
  - [x] Mitigation: schema constraints, anti-leak scanners, and human spot checks.
- [x] Risk: long-running migration interruptions.
  - [x] Mitigation: lock/state discipline, artifact checkpoints, explicit resume hints.
- [x] Risk: accidental execution on base branch.
  - [x] Mitigation: enforce `TARGET_BRANCH!=BASE_BRANCH` before mutating stages.
  - [x] Mitigation: branch-discipline validation gate blocks progression.
- [x] Risk: commit drift reduces auditability.
  - [x] Mitigation: required phase commit checkpoints tied to stage groups.
  - [x] Mitigation: commit ledger artifacts and reconciliation rule for interrupted commit updates.

## 16) Commit phasing (Conventional Commits)
- [x] Phase commit map (required checkpoints).
  - [x] `C01` (`M2`): `build(sphinx): scaffold sphinx project and strict config`.
  - [x] `C02` (`M3`): `feat(traceability): convert source placeholders to myst directives and metadata preface syntax`.
  - [x] `C03` (`M4-M5`): `feat(traceability): add fls-style trace domain and statement-unit instrumentation enforcement`.
  - [x] `C04` (`M6`): `feat(traceability): integrate yaml iso-table directive and table trace validators`.
  - [x] `C05` (`M7-M8`): `feat(traceability): enforce anchor integrity and strict lint consistency gates`.
  - [x] `C06` (`M9-M10`): `feat(traceability): add coverage exports and make.py sphinx orchestration contract`.
  - [x] `C07` (`M11-M12`): `docs(remediation): execute critique-aligned updates with instrumentation freeze`.
  - [x] `C08` (`M13-M14`): `docs(migration): finalize cutover, closeout reports, and legacy retirement`.
- [x] Commit hygiene rules.
  - [x] One phase commit must not mix unrelated concerns across non-adjacent stage groups.
  - [x] Every phase commit is created only after associated stage gates pass.
  - [x] Every phase commit hash and subject are appended to commit ledger artifacts.
  - [x] If interruption occurs after commit but before state update, resume reconciliation records commit in ledger before continuing.

## 17) Prompt and new-session operations
- [x] Add a dedicated execution prompt for this migration plan.
  - [x] File: `prompts/execute-sphinx-traceability-migration-resumable.md`.
  - [x] Inputs: optional `RUN_ID`, optional `MAX_STAGES` (default 1).
  - [x] Outputs: stage before/after, gates, artifacts changed, blockers, exact next step.
- [x] Provide deterministic bootstrap helper.
  - [x] File: `reports/tooling/bootstrap_sphinx_migration_run.py`.
  - [x] Helper initializes M-stage keys and required checklist keys from templates.
  - [x] Helper writes required immutable bootstrap keys (`BASE_BRANCH`, `TARGET_BRANCH`, commit-ledger paths) and appends run-log bootstrap entry.
  - [x] Helper seeds commit ledger artifacts and branch contract artifact.
  - [x] Helper fails fast when `TARGET_BRANCH==BASE_BRANCH`.
- [x] Provide deterministic commit-ledger helper.
  - [x] File: `reports/tooling/record_phase_commit.py`.
  - [x] Helper appends phase commit checkpoint entries to markdown and JSON ledgers.
  - [x] Helper is idempotent on (`stage_checkpoint`, `commit_sha`) for crash-safe resume.
- [x] New session checklist.
  - [x] Verify `OPENCODE_CONFIG_DIR`, `REPO_ROOT`, and `PLAN_PATH`.
  - [x] Run session-zero preflight from Section 8A before stage mutations.
  - [x] Load run state and checklist; verify lock status.
  - [x] Resume at earliest incomplete safe stage.
  - [x] Record explicit next resume command before ending session.

## 18) Definition of done
- [x] Sphinx is the canonical and only document build/validation engine for this workflow.
- [x] Legacy placeholder syntax is fully removed from canonical source.
- [x] FLS-style role-driven statement IDs and references are fully enforced across paragraph/list-item/cell-entry statement units (no exceptions).
- [x] Metadata preface line placement (directly above each markdown paragraph/list-item statement unit) is fully enforced by lints and gates.
- [x] `build/html/paragraph-ids.json` is generated from markdown `dp` statement IDs and YAML `_trace`/`cell_trace` statement IDs, and passes schema/inventory consistency checks.
- [x] Table trace semantics (traceable-table usage, row/cell precedence, and no double-count) are enforced and green.
- [x] Source-embedded statement-level traceability invariants are fully enforced.
- [x] ISO hierarchy and source-anchor integrity gates are consistently green.
- [x] Critique remediation is complete and evidence-linked under the same gate model.
- [x] Required reports are generated under `$OPENCODE_CONFIG_DIR/reports/` (run-scoped and latest pointers).
- [x] `reports/schemas/paragraph-ids.schema.json` is authoritative and used in traceability validation.
- [x] `reports/tooling/bootstrap_sphinx_migration_run.py` enables deterministic fresh-session bootstraps.
- [x] Migration execution is performed on a dedicated non-base branch with branch-discipline gates enforced.
- [x] Phase commit checkpoints are complete, logically scoped, and captured in commit ledger artifacts.
- [x] Durable run artifacts support deterministic resume and audit handoff.
- [x] Clean-room reproducibility gate is green from a new session (`uv sync` + `uv run python make.py verify`).
- [x] Execution prompt exists and is sufficient for a first-time operator with no prior session context.
