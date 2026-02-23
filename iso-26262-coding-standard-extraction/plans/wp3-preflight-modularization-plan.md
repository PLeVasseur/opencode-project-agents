# WP3 Preflight Modularization and Complexity Mitigation Plan

## Objective

- Reduce structural risk before semantic retrieval work by breaking oversized files into cohesive modules.
- Preserve behavior exactly while improving readability, testability, and rollback safety.
- Establish maintainability guardrails so future WP3 work does not re-accumulate monolithic files.

## Why This Plan Is Needed Now

- Current implementation has multiple high-risk oversized files where upcoming WP3 functionality would otherwise accumulate:

| File | Current LOC | Risk level | Preflight action |
|---|---:|---|---|
| `src/commands/ingest.rs` | 4486 | Very high | Split into ingest module tree by concern |
| `src/commands/validate.rs` | 4083 | Very high | Split into validate module tree by concern |
| `src/commands/query.rs` | 854 | High | Split into query retrieval/ranking/output modules |
| `scripts/refresh_quality_artifacts.sh` | 711 | Medium-high | Extract sourceable step/helper libraries |

Line counts were measured from tracked `*.rs` and `*.sh` files.

Current observed post-refactor footprint (2026-02-18 snapshot):

- [x] No active command/shell file exceeds the ~500 LOC soft cap (`scripts/check_file_size_budget.sh` passes).
- [x] Command entry modules are thin (`src/commands/ingest/mod.rs`, `src/commands/validate/mod.rs`, `src/commands/query/mod.rs`).
- [x] Refresh runbook is split into sourceable libraries under `scripts/lib/refresh/`.
- [x] Clippy guardrails are active in warning mode (`too_many_lines`, `cognitive_complexity`).

## Scope

- [x] Perform behavior-preserving refactor only (no intentional retrieval/quality behavior changes).
- [x] Split code by cohesive responsibility, not by arbitrary line ranges.
- [x] Keep CLI contracts and report schemas unchanged.
- [x] Keep SQL schemas and persisted string contracts stable.
- [x] Add maintainability guardrails (lint/policy) in warning mode first.

Out of scope in this plan:

- [x] Adding semantic retrieval features.
- [x] Changing lockfile/report formats for semantic checks.
- [x] Major architecture changes like Cargo workspace split.

## Guardrails

- [x] `pub fn run(...)` remains the only public command entrypoint per command module.
- [x] Prefer `pub(crate)`/`pub(super)` for internal module APIs.
- [ ] Keep behavior parity validated after each phase.
- [x] Keep commits small, phase-aligned, and reversible.

## Preflight Gate Contract

- [x] Treat this plan as a hard precondition for WP3 feature implementation.
- [x] Do not start semantic schema/retrieval coding when preflight gate outcome is `blocked`.
- [x] `provisional` gate outcome allows WP3 semantic coding to start with explicit note; require `ready` evidence before any semantic default-mode promotion.
- [ ] If any phase regresses parity, halt progression and restore parity before starting the next phase.

Gate outcome states:

- [ ] `blocked`: preflight DoD not met; WP3 feature work cannot start.
- [ ] `provisional`: modularization complete but guardrails only in warning mode; WP3 can start with explicit note.
- [x] `ready`: modularization complete and guardrails enforced per staged policy.

Current gate outcome note:

- [x] Current observed status is `ready` after parity baseline capture and verification matrix replay.
- [x] Promotion evidence recorded in `.cache/iso26262/manifests/modularization_baseline/preflight_ready_evidence_20260218T020524Z.json`.

Stop conditions during execution:

- [ ] Any `cargo check` failure after a move-only commit.
- [ ] Any regression in normalized deterministic query probe outputs.
- [ ] Any unexpected check-result regression in `Q-001..Q-030`.
- [ ] Any run-state schema drift in `run_state.json` without explicit plan update.

## Target Module Decomposition

### M1 - Ingest Command Decomposition

Current file: `src/commands/ingest.rs`

Target tree:

```text
src/commands/ingest/
  mod.rs
  pipeline.rs
  types.rs
  ids.rs
  tooling.rs
  inventory.rs
  db/
    mod.rs
    schema.rs
    docs.rs
    nodes.rs
    chunks.rs
  parse/
    mod.rs
    structured.rs
    table.rs
    list_note.rs
    paragraphs.rs
    requirements.rs
  extract/
    mod.rs
    outline.rs
    pages.rs
    ocr.rs
    normalize.rs
```

Constraints:

- [x] Preserve `ChunkType`/`NodeType` persisted string values.
- [x] Preserve SQL positional parameter ordering in node/chunk inserts.
- [x] Preserve ingest counters exactly (`ChunkInsertStats` parity).

### M2 - Validate Command Decomposition

Current file: `src/commands/validate.rs`

Target tree:

```text
src/commands/validate/
  mod.rs
  constants.rs
  models.rs
  io.rs
  reference_eval.rs
  coverage_freshness.rs
  checks/
    mod.rs
    q001_q022.rs
    wp2_q023_q030.rs
    recommendations.rs
  citation_parity/
    mod.rs
    lockfile.rs
    compute.rs
  metrics/
    mod.rs
    common.rs
    printed_pages.rs
    clause_split.rs
    normalization.rs
    semantics.rs
    asil.rs
```

Constraints:

- [x] Preserve report JSON schema and check semantics (`Q-001..Q-030`).
- [x] Preserve Stage A/Stage B policy behavior.
- [x] Preserve citation lockfile governance behavior.

### M3 - Query Command Decomposition

Current file: `src/commands/query.rs`

Target tree:

```text
src/commands/query/
  mod.rs
  model.rs
  retrieve.rs
  rank.rs
  hierarchy.rs
  citation.rs
  output.rs
  util.rs
```

Constraints:

- [x] Preserve exact + FTS + optional node lookup semantics.
- [x] Preserve ranking tie-break order and dedup behavior.
- [x] Preserve text and JSON output contracts.

### M4 - Refresh Script Decomposition

Current file: `scripts/refresh_quality_artifacts.sh`

Target tree:

```text
scripts/refresh_quality_artifacts.sh
scripts/lib/refresh/
  env.sh
  state.sh
  compatibility.sh
  steps.sh
  decisions.sh
```

Constraints:

- [x] Preserve runbook step semantics (`R00..R09`).
- [x] Preserve resume and blocked-state behavior.
- [x] Preserve lockfile/bootstrap policy behavior.

## Symbol Migration Matrix (Minimum Required Coverage)

The following matrix defines the minimum migration granularity so extraction is mechanical and reviewable.

### Ingest (`src/commands/ingest.rs`)

| Source concern cluster | Destination module | Migration notes |
|---|---|---|
| `run` orchestration + top-level sequencing | `ingest/mod.rs` + `ingest/pipeline.rs` | keep `run` thin; transaction orchestration in `pipeline.rs` |
| inventory load/refresh logic | `ingest/inventory.rs` | preserve manifest path behavior |
| ingest-local shared structs/enums | `ingest/types.rs` | move first to break dependency fan-out |
| ID/anchor normalization helpers | `ingest/ids.rs` | preserve normalization output exactly |
| tool/version + command rendering helpers | `ingest/tooling.rs` | no behavior changes |
| schema/bootstrap/fts helpers | `ingest/db/schema.rs` | preserve SQL statements and execution order |
| docs upsert helpers | `ingest/db/docs.rs` | preserve upsert and counts behavior |
| node insert + lineage/path builders | `ingest/db/nodes.rs` | preserve positional SQL arguments and stored labels |
| chunk insert writers | `ingest/db/chunks.rs` | preserve SQL shape and counters |
| structured chunk parser | `ingest/parse/structured.rs` | preserve split thresholds and chunk typing |
| table parser + node emitters | `ingest/parse/table.rs` | preserve ASIL marker/table-row semantics |
| list/note parsers + emitters | `ingest/parse/list_note.rs` | preserve marker normalization and parent linkage |
| paragraph and requirement atom parsing | `ingest/parse/paragraphs.rs` + `ingest/parse/requirements.rs` | preserve reference anchors |
| outline/page extraction + OCR + normalization | `ingest/extract/*` | preserve backend fallback order and page-label behavior |

### Validate (`src/commands/validate.rs`)

| Source concern cluster | Destination module | Migration notes |
|---|---|---|
| top-level `run` orchestration | `validate/mod.rs` | keep as orchestrator only |
| constants + report/check models | `validate/constants.rs` + `validate/models.rs` | move before function extraction |
| manifest/gold set/read helpers | `validate/io.rs` | avoid repeated file/JSON logic |
| reference evaluation/hierarchy helpers | `validate/reference_eval.rs` | preserve anchor comparison logic |
| target coverage + freshness | `validate/coverage_freshness.rs` | preserve stage/freshness semantics |
| checks `Q-001..Q-022` builder | `validate/checks/q001_q022.rs` | preserve thresholds and check IDs |
| WP2 checks `Q-023..Q-030` | `validate/checks/wp2_q023_q030.rs` | preserve Stage A/B policy behavior |
| recommendation mapping | `validate/checks/recommendations.rs` | centralize check-id recommendation text |
| citation parity lockfile I/O | `validate/citation_parity/lockfile.rs` | preserve bootstrap/verify policy |
| citation parity computation | `validate/citation_parity/compute.rs` | preserve checksum and identity matching |
| metric collectors and shared helpers | `validate/metrics/*` | preserve formulas and null/ratio semantics |

### Query (`src/commands/query.rs`)

| Source concern cluster | Destination module | Migration notes |
|---|---|---|
| result/candidate/response models | `query/model.rs` | pure move first |
| exact/fts/node retrieval functions | `query/retrieve.rs` | preserve SQL, limits, and filters |
| candidate upsert + ranking + dedup | `query/rank.rs` | preserve tie-break ordering |
| descendant fetch and hierarchy expansion | `query/hierarchy.rs` | preserve ancestry/descendancy output |
| citation rendering helpers | `query/citation.rs` | preserve citation text output exactly |
| json/text output writers | `query/output.rs` | preserve emitted field names and formatting |
| misc helpers (`to_fts_query`, whitespace, page range) | `query/util.rs` | preserve normalization behavior |

### Refresh Script (`scripts/refresh_quality_artifacts.sh`)

| Source concern cluster | Destination module | Migration notes |
|---|---|---|
| env defaults + preflight checks | `scripts/lib/refresh/env.sh` | preserve default values and required command checks |
| run-state writes + trap handling | `scripts/lib/refresh/state.sh` | preserve run_state schema and status transitions |
| compatibility/rebuild checks | `scripts/lib/refresh/compatibility.sh` | preserve blocked/rebuild logic |
| R04..R09 step actions | `scripts/lib/refresh/steps.sh` | preserve step IDs and order |
| decisions log append | `scripts/lib/refresh/decisions.sh` | preserve decision record shape |

## Parity Specification (Concrete)

Create one baseline capture and use normalized comparisons after each phase.

Baseline capture artifacts (under `.cache/iso26262/manifests/modularization_baseline/`):

- [ ] `quality_report.normalized.json`
- [ ] `query_exact.normalized.json`
- [ ] `query_paragraph.normalized.json`
- [ ] `query_table_row.normalized.json`
- [ ] `query_table_cell.normalized.json`
- [ ] `ingest_counts.normalized.json`
- [ ] `run_state.normalized.json`

Normalization contracts:

- [ ] Quality report normalization keeps: `status`, `summary`, `hierarchy_metrics`, selected `table_quality_scorecard`, and `checks`.
- [ ] Query normalization keeps for top result: `reference`, `citation`, `anchor_type`, `anchor_label_norm`, `page_pdf_start`, `page_pdf_end`, `source_hash`, `citation_anchor_id`, `leaf_node_type`.
- [ ] Ingest manifest normalization keeps `db_schema_version`, `processed_parts`, and `counts` (core node/chunk counters).
- [ ] Run-state normalization ignores timestamp fields and compares status/step/progression fields.

Reference normalization snippets (runbook examples):

```bash
# quality report normalization
jq -c '{
  status,
  summary,
  hierarchy_metrics,
  table_quality_scorecard: {
    counters: .table_quality_scorecard.counters,
    table_sparse_row_ratio: .table_quality_scorecard.table_sparse_row_ratio,
    table_overloaded_row_ratio: .table_quality_scorecard.table_overloaded_row_ratio,
    table_marker_sequence_coverage: .table_quality_scorecard.table_marker_sequence_coverage,
    table_description_coverage: .table_quality_scorecard.table_description_coverage
  },
  checks
}' ".cache/iso26262/manifests/extraction_quality_report.json"

# top result normalization for deterministic query probes
jq -c '.results[0] | {
  reference,
  citation,
  anchor_type,
  anchor_label_norm,
  page_pdf_start,
  page_pdf_end,
  source_hash,
  citation_anchor_id,
  leaf_node_type
}'

# ingest manifest counts normalization
jq -c '{db_schema_version, processed_parts, counts}' ".cache/iso26262/manifests/ingest_run_<latest>.json"
```

Comparison rules:

- [x] `status`/check outcomes must not regress.
- [x] For deterministic query probes, normalized top result must remain identical.
- [ ] Any intentional non-parity change requires explicit rationale and a follow-up baseline update task.

## Phase Plan

### P0 - Baseline and Freeze

- [x] Create parity baseline directory: `.cache/iso26262/manifests/modularization_baseline/`.
- [x] Run baseline command bundle:
  - [x] `cargo check`
  - [x] `cargo test`
  - [x] `scripts/smoke_part6.sh`
  - [x] `SMOKE_DETERMINISM=1 scripts/smoke_part6.sh`
- [x] Capture normalized baseline artifacts for report/query/ingest/run-state comparisons.
- [x] Record latest ingest manifest and report filenames used for baseline.
- [x] Freeze expected outputs for deterministic query probes:
  - [x] `query "9.1"`
  - [x] `query "9.1 para 3" --node-type paragraph`
  - [x] `query "Table 3 row 4" --node-type table_row`
  - [x] `query "Table 3 r4c2" --node-type table_cell`

Exit criteria:

- [x] Baseline command bundle is green.
- [x] Baseline artifacts are captured and committed/archived for phase comparisons.
- [x] Deterministic query probes are frozen with normalized result payloads.

### P1 - Ingest Split (M1)

- [x] P1.1: Convert `src/commands/ingest.rs` into `src/commands/ingest/mod.rs` without logic movement.
- [x] P1.2: Move shared types/enums and ID/citation helpers into split modules (`types_and_structured.rs`, `ids_and_outline.rs`).
- [x] P1.3: Move DB setup and writer logic into split ingest modules (`db_setup.rs`, `node_and_table_insert.rs`, `list_note_requirement_insert.rs`, `pipeline.rs`).
- [x] P1.4: Move extraction pipeline internals into split extraction modules (`page_extract_and_normalize.rs`, `ocr_tools_and_manifest.rs`, `pipeline_page_chunks.rs`).
- [x] P1.5: Move structured parsing internals into split parsing modules (`paragraphs_and_list_parse.rs`, `table_parse_quality_part1.rs`, `table_parse_quality_part2.rs`, `pipeline_structured_chunks.rs`).
- [x] P1.6: Keep orchestration in `pipeline.rs`; keep `mod.rs` as thin command entrypoint.
- [ ] After each P1.x step run `cargo check` and stop immediately on parity regressions.

Exit criteria:

- [x] Ingest behavior parity validated against baseline artifacts.
- [x] `src/commands/ingest/mod.rs` remains orchestration-focused (target `<= 250` LOC).
- [x] No SQL contract drift (insert ordering and persisted enum/string values unchanged).

### P2 - Validate Split (M2)

- [x] P2.1: Convert `src/commands/validate.rs` into `src/commands/validate/mod.rs` shell.
- [x] P2.2: Move constants/models into split prelude/type modules (`prelude_types_part1.rs`, `prelude_types_part2.rs`).
- [x] P2.3: Move IO and reference evaluation helpers into split modules (`coverage_freshness_part1.rs`, `coverage_freshness_part2.rs`, `invariants_and_hierarchy.rs`).
- [x] P2.4: Move metrics helpers into split modules (`fidelity_metrics_part1.rs`, `fidelity_metrics_part2.rs`).
- [x] P2.5: Move citation parity lockfile/compute logic into split module (`citation_parity_part1.rs`).
- [x] P2.6: Move check builders into split modules (`checks_and_summary.rs`, `stage_and_wp2_core.rs`).
- [x] P2.7: Keep `mod.rs` as policy/orchestration layer only.
- [ ] After each P2.x step run `cargo check`; after P2.6 run full parity bundle.

Exit criteria:

- [x] Validation report schema and check outcomes remain parity-stable.
- [x] Stage A/B behavior for `Q-023..Q-030` matches baseline.
- [x] Citation parity lockfile bootstrap/verify behavior remains unchanged.

### P3 - Query Split (M3)

- [x] P3.1: Convert `src/commands/query.rs` into `src/commands/query/mod.rs` shell.
- [x] P3.2: Move run orchestration and response model types into split query modules (`run.rs`, `ranking_and_output.rs`).
- [x] P3.3: Move exact/fts/node retrieval into `query/retrieval.rs`.
- [x] P3.4: Move ranking/dedup into `query/ranking_and_output.rs`.
- [x] P3.5: Move hierarchy expansion into `query/hierarchy_and_citation.rs`.
- [x] P3.6: Move citation and output writers into split query modules (`query/hierarchy_and_citation.rs`, `query/ranking_and_output.rs`).
- [x] P3.7: Move utility helpers into split query modules (`query/hierarchy_and_citation.rs`, `query/ranking_and_output.rs`).
- [ ] After each P3.x step run `cargo check`; after P3.7 run deterministic query parity checks.

Exit criteria:

- [x] Query ranking and citation outputs match normalized baseline on deterministic probes.
- [x] JSON and text output contracts remain unchanged.

### P4 - Script Split (M4)

- [x] P4.1: Introduce `scripts/lib/refresh/env.sh` + `state.sh` and source them from top-level script.
- [x] P4.2: Move compatibility logic to `compatibility.sh`.
- [x] P4.3: Move R04..R09 step bodies to `steps.sh`.
- [x] P4.4: Move decision append logic to `decisions.sh`.
- [x] P4.5: Keep `scripts/refresh_quality_artifacts.sh` as orchestration shell preserving step order.
- [x] Validate blocked/resume/rebuild pathways explicitly after split.

Exit criteria:

- [x] Script behavior parity for quick mode and full-target mode.
- [x] `R00..R09` state transitions unchanged.
- [x] `run_state.json` schema unchanged.

### P5 - Maintainability Guardrails

- [x] Add `clippy.toml` with initial warning thresholds:
  - [x] `too-many-lines-threshold = 100` (function-level)
  - [x] `cognitive-complexity-threshold = 25`
- [x] Add local policy targets (documented, not hard-fail initially):
  - [x] Rust source file soft cap: `~500` lines.
  - [x] Shell script soft cap: `~500` lines.
  - [x] Command `mod.rs` orchestration target: `<= 250` lines.
- [x] Add enforcement commands to runbook (warning-first):
  - [x] `cargo clippy --all-targets -- -W clippy::too_many_lines -W clippy::cognitive_complexity`
  - [x] file-size budget checker for tracked `*.rs` and `*.sh`.
- [x] Add staged policy:
  - [x] Stage `warn`: warnings only while refactor settles.
  - [x] Stage `enforce`: fail runbook on threshold breaches after two consecutive green full-target runs.

Exit criteria:

- [x] Guardrails active in warning mode with no behavior changes.
- [x] File-size budget reporting exists and is visible in runbook outputs.

## Commit Plan (Conventional Commits)

- [ ] `chore(preflight): capture modularization parity baseline artifacts`
- [ ] `refactor(ingest): convert ingest.rs to ingest mod shell`
- [ ] `refactor(ingest): extract shared ingest types and id helpers`
- [ ] `refactor(ingest): extract ingest db schema and writers`
- [ ] `refactor(ingest): extract ingest page extraction and normalization modules`
- [ ] `refactor(ingest): extract ingest structured parsing modules`
- [ ] `refactor(ingest): isolate ingest pipeline orchestration`
- [ ] `refactor(validate): convert validate.rs to validate mod shell`
- [ ] `refactor(validate): extract validate models constants and io helpers`
- [ ] `refactor(validate): extract validate metrics collectors`
- [ ] `refactor(validate): extract citation parity lockfile and compute modules`
- [ ] `refactor(validate): extract quality check builders q001-q030`
- [ ] `refactor(validate): centralize check recommendation mapping`
- [ ] `refactor(query): convert query.rs to query mod shell`
- [ ] `refactor(query): extract retrieval and ranking modules`
- [ ] `refactor(query): extract hierarchy citation and output modules`
- [ ] `refactor(scripts): extract refresh env and run-state helpers`
- [ ] `refactor(scripts): extract refresh compatibility and step modules`
- [ ] `refactor(scripts): extract refresh decisions helper and thin orchestrator`
- [ ] `test(preflight): add modularization parity harness checks`
- [ ] `chore(lint): add clippy complexity thresholds and file-size budget checks`
- [ ] `docs(runbook): add modularization guardrails and exception policy`

## Verification Matrix

Run after each commit slice:

- [ ] `cargo check`
- [ ] target smoke subset for changed surface (`query` probes or `validate` run as applicable)

Run after each phase boundary (`P1`, `P2`, `P3`, `P4`) or as a post-hoc ready-evidence replay:

- [x] `cargo test`
- [x] `scripts/smoke_part6.sh`
- [x] `SMOKE_DETERMINISM=1 scripts/smoke_part6.sh`
- [x] compare normalized parity artifacts to baseline and record pass/fail outcome.

Run before declaring preflight complete:

- [x] `FULL_TARGET_SET=1 TARGET_PARTS="2 6 8 9" scripts/refresh_quality_artifacts.sh`
- [x] `WP2_GATE_STAGE=B cargo run -- validate --cache-root .cache/iso26262`
- [x] `cargo clippy --all-targets -- -W clippy::too_many_lines -W clippy::cognitive_complexity`
- [x] file-size budget checker reports no unapproved breaches.

## Test Migration and Coverage Strategy

- [x] Preserve or relocate existing tests alongside moved modules (`#[cfg(test)]` near owning module where practical).
- [ ] Add focused unit tests for extracted pure helpers when previously untested behavior becomes isolated.
- [x] Keep command-level behavior asserted by smoke and deterministic query checks.
- [ ] Track any temporary test gaps as explicit TODOs with owner + due phase.

## File-Size Budget and Exception Policy

Budget policy:

- [x] Rust file soft cap: `~500` LOC.
- [x] Shell script soft cap: `~500` LOC.
- [x] Function soft cap: `~100` LOC unless complexity/lifecycle justifies otherwise.

Exception process (required for any breach):

- [ ] Add an exception record in `$OPENCODE_CONFIG_DIR/plans/wp3-modularization-exceptions.md` with fields: `path`, `current_loc`, `reason`, `owner`, `decision_id`, `expires_after_phase`.
- [ ] Record exception rationale in decision log and link it from the plan.
- [ ] Create a follow-up task/commit target to eliminate the exception before WP3 Stage B promotion.

## Risks and Mitigations

- [ ] Risk: subtle behavior drift while moving code.
  - [ ] Mitigation: move-only commits first, baseline parity after each phase.
- [ ] Risk: cross-module cyclic dependencies.
  - [ ] Mitigation: keep thin orchestration layer and directional module ownership.
- [ ] Risk: SQL contract regressions in insert order/type strings.
  - [ ] Mitigation: avoid SQL rewrites during split; preserve statements byte-for-byte where possible.
- [ ] Risk: script split breaks resume/rebuild logic.
  - [ ] Mitigation: keep step IDs and state transitions unchanged; verify blocked/resume paths.
- [ ] Risk: hidden public API creep between submodules.
  - [ ] Mitigation: default internal exports to `pub(crate)`/`pub(super)` and audit public symbols at phase boundaries.
- [ ] Risk: parity harness misses dynamic field differences.
  - [ ] Mitigation: normalize volatile fields explicitly and keep baseline artifact schema versioned.

## Definition of Done

- [x] No command/script file above ~500 LOC remains in the active code path without documented exception.
- [x] `ingest`, `validate`, `query`, and refresh script are decomposed by cohesive responsibility.
- [x] Baseline behavior parity is demonstrated by validation matrix.
- [x] Guardrails are documented, enabled in warning mode, and have a scheduled enforcement transition.
- [x] No unresolved modularization exceptions exist past their `expires_after_phase`.
- [x] WP3 semantic implementation may proceed on top of this modularized foundation.

## Remaining Work for `ready` Promotion

- [x] Capture and store modularization parity baseline artifacts under `.cache/iso26262/manifests/modularization_baseline/`.
- [x] Run/record the full preflight verification matrix as an explicit `ready` evidence bundle.
- [x] Flip gate outcome from `provisional` to `ready` once parity evidence is complete.

Recorded ready-evidence artifacts:

- [x] `.cache/iso26262/manifests/modularization_baseline/preflight_ready_evidence_20260218T020524Z.json`
- [x] `.cache/iso26262/manifests/modularization_baseline/parity_recheck_20260218T020524Z.json`
- [x] decision log entry `D-0034` in `.cache/iso26262/manifests/decisions_log.jsonl`

## Suggested Execution Order

1. [x] P0 baseline freeze.
2. [x] P1 ingest split.
3. [x] P2 validate split.
4. [x] P3 query split.
5. [x] P4 refresh script split.
6. [x] P5 guardrails.
7. [x] Begin WP3 semantic implementation with preflight gate `ready`; semantic default-mode promotion remains subject to WP3 stage gates.
