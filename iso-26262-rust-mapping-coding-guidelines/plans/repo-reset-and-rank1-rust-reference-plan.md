# Repo Reset + Rank 1 Rust Reference Plan

## Objective

- [x] Reset `/home/pete.levasseur/personal/iso-26262-rust-mapping-coding-guidelines` to an almost-blank baseline, then rebuild only Rank 1 (`rust_reference.sqlite`).
  - [x] Keep only `.git/`, `.gitignore`, `pyproject.toml`, and `uv.lock` in the repo.
  - [x] Rebuild only the Rust Reference SQLite path first.
  - [x] Stop after Rank 1 and report results.

## Hard Guardrails

- [x] Never remove or modify anything under `$OPENCODE_CONFIG_DIR`.
  - [x] `$OPENCODE_CONFIG_DIR` path: `/home/pete.levasseur/opencode-project-agents/iso-26262-rust-mapping-coding-guidelines`.
  - [x] Plan files in `$OPENCODE_CONFIG_DIR/plans/` are preserved.
- [x] Follow strict context hygiene during implementation.
  - [x] Read only files needed for active Rank 1 work.
  - [x] Do not inspect unrelated repo files.

## Branching

- [x] Create a dedicated implementation branch from the current branch.
  - [x] Branch name: `feat/table1-rank1-rust-reference-rebuild`
  - [ ] Keep commits scoped and descriptive.

## Phase 0 - Safety Snapshot (Pre-Reset)

- [x] Create an external safety backup before destructive cleanup.
  - [x] Store backup outside the repo root.
  - [x] Record backup path and timestamp in run notes.

## Phase 1 - Destructive Reset (Repo Only)

- [x] Remove all repo contents except keep-list files.
  - [x] Keep `.git/` untouched.
  - [x] Keep `.gitignore`, `pyproject.toml`, `uv.lock`.
  - [x] Remove all other files/directories under repo root.
- [x] Verify reset result.
  - [x] Confirm only keep-list items remain.

## Phase 2 - Rank 1 Skeleton (Rust Reference Only)

- [x] Create minimal required structure for Rank 1 implementation.
  - [x] `scripts/`
  - [x] `config/sqlite_query_contracts/`
  - [x] `tests/unit/sqlite_kb/`
  - [x] `data/`
- [x] Create canonical paths/metadata for Rank 1.
  - [x] Active DB target: `.cache/sqlite_kb/current/rust_reference.sqlite`
  - [x] Snapshot target: `.cache/sqlite_kb/snapshots/rust_reference/<snapshot_id>.sqlite`
  - [x] Query logs target: `.cache/sqlite_kb/query_logs/rust_reference/`
  - [x] Manifest file: `data/sqlite_kb_manifest.yaml`

## Phase 3 - Implement Rank 1 Artifacts

- [x] Implement shared query guardrails.
  - [x] `scripts/sqlite_query_guardrails.py`
  - [x] Enforce read-only mode and `PRAGMA query_only=ON`.
  - [x] Allow only contract query IDs + parameterized execution.
  - [x] Block write/DDL/ATTACH/extension operations.
- [x] Implement Rust Reference builder.
  - [x] `scripts/sqlite_build_rust_reference.py`
  - [x] Ingest pinned Rust Reference source.
  - [x] Create schema, insert snapshot metadata, and materialize DB.
- [x] Implement Rust Reference query wrapper.
  - [x] `scripts/sqlite_query_rust_reference.py`
  - [x] Use contract-only query execution.
  - [x] Emit query audit logs.
- [x] Implement Rust Reference smoke runner.
  - [x] `scripts/sqlite_smoke_rust_reference.py`
  - [x] Validate core contract queries and Table 1 row verdict coverage.
- [x] Define Rank 1 query contract.
  - [x] `config/sqlite_query_contracts/rust_reference.yaml`

## Phase 4 - Tests and Gates (Rank 1)

- [x] Add focused unit tests.
  - [x] `tests/unit/sqlite_kb/test_query_rust_reference.py`
  - [x] `tests/unit/sqlite_kb/test_smoke_rust_reference.py`
  - [x] `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`
- [x] Pass Rank 1 DoD gate.
  - [x] For each Table 1 row (`1a`..`1i`), return `applicable` or `not_applicable`.
  - [x] No `unknown` verdicts.
  - [x] Every `not_applicable` includes source-backed rationale + joinable anchors.
  - [x] Queryability and latency checks pass.

## Phase 5 - Commit + Report (Stop After Rank 1)

- [ ] Commit Rank 1 implementation with Conventional Commit message.
  - [ ] Include scripts, contract file, tests, and manifest updates.
- [x] Stop and report back.
  - [x] Summarize what passed/failed.
  - [x] Provide next-step recommendation before Rank 2.

## Phase 6 - Query Reasonableness Test Set (45 Cases)

- [x] Define a fixed 45-case query test set for ISO 26262 Part 6 Table 1 reasonableness checks.
  - [x] Use 5 query intents per row marker (`1a`..`1i`) for 45 total cases.
  - [x] Include both row-level and evidence-level checks in each row bundle.
  - [x] Keep cases deterministic and parameterized by canonical `row_node_id`/`row_marker`.
- [x] Persist queries and expected results in separate files.
  - [x] Queries file (shape + parameters + query id per case): `data/query_testsets/rust_reference_table1_queries.yaml`.
  - [x] Expected results file (assertions + thresholds per case): `data/query_testsets/rust_reference_table1_expected.yaml`.
  - [x] Ensure both files can be loaded independently and joined by stable `case_id`.
- [x] Implement an executable verifier that loads both files and validates outcomes.
  - [x] Verifier script: `scripts/sqlite_verify_rust_reference_query_set.py`.
  - [x] Execute through read-only wrapper/guardrails only (no direct write-capable SQL).
  - [x] Emit machine-readable verification report under `.cache/sqlite_kb/reports/rust_reference/`.
- [x] Vet reasonableness of returned results and enforce stop conditions.
  - [x] For each case, verify returned rows satisfy expected anchors, timestamps, and ranking constraints.
  - [x] Mark each case as `pass`/`fail` with explicit evidence excerpts in the report.
  - [x] If any case fails reasonableness, stop and open a searchability remediation loop before proceeding.
- [x] Searchability remediation loop (must run on any failure before continuation).
  - [x] Diagnose whether failure is lexical retrieval weakness, semantic classification weakness, or schema/index weakness.
  - [x] Propose and apply targeted DB/search updates (query contract, indexes, extraction mapping, optional FTS/semantic layer).
  - [x] Re-run full 45-case suite and require green before considering Rank 1 complete.
- [x] Add test harness coverage.
  - [x] Unit test to validate query/expected file loading and `case_id` completeness.
  - [x] Unit test to validate verifier behavior on at least one forced fail and one pass case.
  - [x] Smoke invocation for full 45-case run.

## Phase 7 - Quality-First Semantic Retrieval Upgrade (Rank 1.5)

### 7.0 Model and Retrieval Profile

- [ ] Lock the quality-first semantic stack for `rust_reference.sqlite`.
  - [ ] Primary dense embedding model: `Qwen/Qwen3-Embedding-4B`.
  - [ ] Reranker model: `BAAI/bge-reranker-v2-m3`.
  - [ ] Vector index technology: `sqlite-vec` (active maintenance path).
  - [ ] Serving runtime: Hugging Face `text-embeddings-inference` for embeddings and reranking endpoints.
- [ ] Persist model governance metadata for auditability.
  - [ ] Record model IDs, revisions, embedding dimensions, distance metric, and licenses.
  - [ ] Record runtime endpoint configuration and retrieval profile in reports.
  - [ ] Store these fields in snapshot metadata and queryable DB tables.

### 7.1 Schema + Migration (User Version 3)

- [ ] Extend `rust_reference.sqlite` schema with explicit semantic retrieval tables.
  - [ ] Add `semantic_models(model_id, model_name, model_revision, embedding_dim, distance_metric, license, created_at)`.
  - [ ] Add `semantic_corpus(corpus_id, source_kind, source_id, row_node_id, mechanism_id, anchor, text, text_sha256, source_fetched_at)`.
  - [ ] Add `row_mechanism_scores(row_node_id, mechanism_id, lexical_score, semantic_score, reranker_score, hybrid_score, score_version, top_statement_id, scored_at)`.
  - [ ] Add `CREATE VIRTUAL TABLE ... USING vec0(...)` tables for statement/mechanism/row embeddings via `sqlite-vec`.
- [ ] Preserve existing queryability contracts while extending score detail.
  - [ ] Keep `row_node_id` and `row_marker` as canonical row identity inputs.
  - [ ] Keep `row_mechanisms.relevance_score` populated (now from hybrid ranking).
  - [ ] Add backward-compatible views where needed so existing query IDs keep working.
- [ ] Update migration tooling.
  - [ ] Bump `PRAGMA user_version` from `2` to `3`.
  - [ ] Update `scripts/sqlite_migrate_rust_reference_schema.py` for additive migration only.
  - [ ] Add migration tests for both fresh DB and upgraded DB paths.

### 7.2 Semantic Corpus Construction

- [ ] Build deterministic semantic corpus text units from existing extracted artifacts.
  - [ ] Include row requirement payloads (`table1_rows.requirement_text`) and row metadata text.
  - [ ] Include mechanism descriptors assembled from `mechanisms` + top evidence excerpts.
  - [ ] Include statement-level evidence units from `statements`/`mechanism_evidence`.
- [ ] Apply robust normalization without losing provenance.
  - [ ] Normalize whitespace/casing and strip formatting noise only.
  - [ ] Keep original text in source tables; write normalized text into `semantic_corpus`.
  - [ ] Add targeted cleanup for known noisy row text (notably row marker `1i`) with deterministic rules.
- [ ] Guarantee stable IDs and reproducible chunking.
  - [ ] Derive `corpus_id` from canonical source IDs + `text_sha256`.
  - [ ] Ensure row/chunk linkage remains joinable to evidence anchors.

### 7.3 Embedding + Index Build Pipeline

- [ ] Add an embedding build stage to `scripts/sqlite_build_rust_reference.py`.
  - [ ] Add CLI/config parameters for endpoint URL, model ID, batch size, timeout, and retry policy.
  - [ ] Generate embeddings for semantic corpus rows, row requirement texts, and mechanism profiles.
  - [ ] Insert vectors into `sqlite-vec` virtual tables with deterministic row mappings.
- [ ] Add robust failure handling.
  - [ ] Hard-fail semantic mode if embedding generation fails (quality-first default).
  - [ ] Keep an explicit lexical fallback mode only for emergency operation (non-default).
  - [ ] Emit per-run diagnostics: total vectors, missing vectors, retry counts, and duration.

### 7.4 Retrieval + Ranking Algorithm

- [ ] Replace heuristic row-mechanism assignment with embedding-driven retrieval.
  - [ ] For each `row_node_id`, query ANN top-K candidates from semantic statement/mechanism vectors.
  - [ ] Rerank top-N candidates using `BAAI/bge-reranker-v2-m3`.
  - [ ] Aggregate candidate evidence to mechanism-level scores.
- [ ] Define deterministic hybrid scoring.
  - [ ] Compute `hybrid_score = w_semantic * semantic_score + w_reranker * reranker_score + w_lexical * lexical_score`.
  - [ ] Set default weight profile to semantic-first (quality mode).
  - [ ] Use deterministic tie-break ordering (`hybrid_score DESC`, `semantic_score DESC`, `mechanism_id ASC`).
- [ ] Persist transparent score breakdowns.
  - [ ] Keep top evidence anchor/section/statement IDs per selected mechanism.
  - [ ] Store per-row top-K score components in `row_mechanism_scores`.
  - [ ] Keep `row_verdicts` and mandatory rationale fields unchanged.

### 7.5 Query Contract + Wrapper Extensions

- [ ] Extend `config/sqlite_query_contracts/rust_reference.yaml` with semantic-aware query IDs.
  - [ ] Add `semantic_model_metadata` query for model/version/license audit.
  - [ ] Add `semantic_statement_hits_for_row` query for top semantic evidence by row.
  - [ ] Add `row_mechanism_score_breakdown` query exposing lexical/semantic/reranker/hybrid components.
- [ ] Keep existing query IDs stable for callers.
  - [ ] `mechanisms_for_row` continues to return ranked mechanisms, now driven by hybrid score.
  - [ ] Existing row-verdict and evidence queries remain contract-compatible.
- [ ] Update wrapper/reporting behavior.
  - [ ] Ensure query logs capture retrieval mode + semantic model ID.
  - [ ] Keep read-only guardrails and no-extension SQL restrictions intact.

### 7.6 Validation, Reasonableness, and Regression Gates

- [ ] Preserve current baseline correctness.
  - [ ] Keep the existing 45-case suite green with no contract regressions.
  - [ ] Keep hard row gate: all rows `1a..1i` must resolve to `applicable` or `not_applicable`.
  - [ ] Keep mandatory rationale anchor/timestamp requirements for all verdicts.
- [ ] Add semantic-focused verification cases (+5 per row, +45 total).
  - [ ] Add a second 45-case suite for semantic retrieval behavior and evidence plausibility.
  - [ ] Include paraphrase-style prompts that lexical-only retrieval would miss.
  - [ ] Add explicit row `1i` noisy-text robustness checks.
- [ ] Upgrade verifier and tests.
  - [ ] Extend `scripts/sqlite_verify_rust_reference_query_set.py` to run lexical + semantic suites.
  - [ ] Add unit tests for new query types and score-shape assertions.
  - [ ] Require full 90-case pass before semantic rollout signoff.

### 7.7 Rollout Strategy and Safety

- [ ] Implement a staged rollout path.
  - [ ] Stage A: shadow mode computes semantic scores and reports drift without changing outputs.
  - [ ] Stage B: hybrid mode becomes default ranking for `row_mechanisms`.
  - [ ] Stage C: retire heuristic-only family mapping from active ranking path.
- [ ] Keep deterministic rollback.
  - [ ] Support `--retrieval-mode lexical` switch for incident response.
  - [ ] Preserve prior snapshot comparison for before/after ranking diffs.
  - [ ] Fail build if semantic dependencies are unavailable in quality-first mode.

### 7.8 Deliverables

- [ ] Updated scripts and contracts.
  - [ ] `scripts/sqlite_build_rust_reference.py` semantic build path.
  - [ ] `scripts/sqlite_migrate_rust_reference_schema.py` user-version-3 migration.
  - [ ] `config/sqlite_query_contracts/rust_reference.yaml` semantic query additions.
  - [ ] `scripts/sqlite_verify_rust_reference_query_set.py` expanded suite support.
- [ ] Updated testsets and reports.
  - [ ] Existing 45-case lexical suite retained.
  - [ ] New 45-case semantic suite added and wired into CI/smoke flow.
  - [ ] Report artifacts include semantic score breakdowns and model metadata.
