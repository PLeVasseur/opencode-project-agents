# WP3 Semantic Query and Schema Expansion Plan (Chunk-First Hybrid Retrieval)

## Objective

- Add semantic retrieval to `query` as an additive capability while preserving the current citation-accurate lexical behavior.
- Expand the SQLite schema with a chunk-level embedding sidecar so semantic search can run fully local.
- Introduce measurable quality gates for semantic relevance, exact-reference non-regression, citation parity, and latency.
- Deliver chunk-level hybrid retrieval first; treat node embeddings as a second-pass refinement step only.
- Keep embedding generation in a dedicated `embed` command (separate from `ingest`) so ingest determinism and semantic index lifecycle stay decoupled.

## Scope and Guardrails

- [x] Keep all licensed corpus data local (`.cache/iso26262`) and avoid outbound text by default.
- [x] Keep planning artifacts in `$OPENCODE_CONFIG_DIR/plans/`.
- [x] Hard gate: preflight modularization outcome from `plans/wp3-preflight-modularization-plan.md` is at least `provisional` (prefer `ready`) before WP3 semantic coding starts.
- [x] Keep lexical retrieval as the authoritative baseline for exact-reference intent.
- [x] Keep citation rendering sourced from canonical `chunks` metadata (`ref`, pages, anchor fields, source hash).
- [x] Keep semantic retrieval optional and feature-gated until Stage B semantic checks are green.
- [x] Do not introduce remote embedding providers in the initial implementation phase.
- [x] Keep semantic indexing out of `ingest`; use dedicated `embed` workflow for generation/refresh.
- [x] Enforce maintainability budgets during WP3 (`scripts/check_file_size_budget.sh` and clippy thresholds); document any temporary breach in `plans/wp3-modularization-exceptions.md`.

## Baseline Snapshot (Current State)

- [x] Last known full-target Stage B validation run is green (`48/48` pass) for run `run-20260218T105419Z`.
- [x] Current query pipeline is modularized and still lexical-first (exact + FTS5 + optional node text matching): `src/commands/query/run.rs`, `src/commands/query/retrieval.rs`, `src/commands/query/ranking_and_output.rs`, `src/commands/query/hierarchy_and_citation.rs`.
- [x] Corpus scale is small enough for exact KNN bootstrap: `10` docs, `627` chunks, `6496` nodes.
- [x] Citation parity lockfile policy is active (`manifests/citation_parity_baseline.lock.json`).
- [x] Existing checks for exact reference ranking (`Q-005`) and keyword relevance (`Q-006`) are already green.
- [x] Gap to close in WP3-E: `Q-005` currently validates exact-reference presence, so WP3 must add query-path exact-intent regression probes for semantic non-regression.

## Modularization Delta (Post-Preflight Reality)

- [x] `ingest`, `validate`, and `query` were split into module trees with thin `mod.rs` entry points.
- [x] Refresh runbook is now modularized into `scripts/lib/refresh/{env,state,compatibility,steps,decisions}.sh`.
- [x] Guardrails are active (`clippy.toml` thresholds + `scripts/check_file_size_budget.sh`).
- [x] No active modularization exceptions are currently recorded (`plans/wp3-modularization-exceptions.md`).
- [x] WP3 additions must avoid re-accumulating near-cap files; prefer new semantic-focused modules over appending to large validate/query files.

## Research-Informed Design Principles

References consulted:

- SQLite FTS5 docs: `https://www.sqlite.org/fts5.html`
- sqlite-vec project/docs: `https://github.com/asg017/sqlite-vec`
- Hybrid retrieval patterns:
  - Azure AI Search hybrid overview
  - Weaviate hybrid concepts
  - Qdrant hybrid queries
  - Pinecone hybrid guidance
- Evaluation baselines:
  - BEIR (`https://arxiv.org/abs/2104.08663`)
  - MTEB (`https://arxiv.org/abs/2210.07316`)

Design takeaways translated into this plan:

- [x] Hybrid retrieval (lexical + semantic) is preferred over semantic-only for technical corpora.
- [x] Rank fusion (RRF) is safer than naive score mixing across heterogeneous rankers.
- [x] Exact reference intent should remain first-class and must not regress.
- [x] Candidate pools should be wider than final output `k` before fusion/rerank.
- [x] Evaluation must separate exact-intent queries from paraphrase/concept-intent queries.

## Embedding Backend Decision Record (Phase 1 Locked)

### Decision Summary

- [x] Phase 1 backend is `pure Rust local embeddings + chunk_embeddings sidecar + exact cosine KNN in app layer`.
- [x] Text handling remains local-only by default (no remote embedding API path in the initial implementation).
- [x] `sqlite-vec` acceleration remains an optional Phase 2 optimization path.
- [x] ANN/libSQL vector index path remains deferred pending measured scale/latency pressure.

### Option Comparison (Performance vs Maintenance)

| Option | Query performance at current scale (~627 chunks) | Implementation complexity | Operational maintenance | Fit for current repo |
|---|---|---|---|---|
| Rust local embeddings + exact cosine KNN | High (exact scan is cheap at this size) | Low to medium | Low | Strong |
| SQLite extension path (`sqlite-vec`) | High | Medium to high (extension loading/packaging) | Medium | Good later |
| libSQL ANN / DiskANN path | Very high at large scale | High (platform shift) | Medium to high | Premature now |
| External vector service | High | Medium | High (service ops + egress controls) | Not aligned with current guardrails |

### Why This Is the Right First Choice

- [x] Corpus size is currently small enough that exact cosine search is not the bottleneck.
- [x] This minimizes moving parts while preserving deterministic local behavior.
- [x] It avoids SQLite extension lifecycle issues during first semantic rollout.
- [x] It preserves the easiest rollback path (`--retrieval-mode lexical`) if semantic gates fail.

### Maintenance Contract for the Chosen Backend

- [ ] Implement a backend boundary (trait/interface) so embedding generation and vector search can be swapped later without query-contract breakage.
- [x] Keep vector row format backend-neutral (`embedding BLOB`, `embedding_dim`, `text_hash`, `model_id`).
- [x] Keep all model identity/config in lockfiles (`semantic_model_config.lock.json`) for reproducibility.
- [ ] Keep query output contract stable regardless of retrieval backend choice.
- [x] Keep lexical-only mode fully supported as a long-term safety fallback.

### Default Local Model Policy (Initial)

- [x] Select one lightweight, local-friendly default model for Phase 1 (for example, `all-MiniLM-L6-v2` class).
- [x] Record model metadata in `embedding_models` (`model_name`, `dimensions`, normalization, runtime backend).
- [ ] Require explicit decision-log entry for model change, including before/after metric deltas.
- [x] Rebuild embeddings whenever `model_id` or embedding input format changes.

### Promotion Criteria for Optional Acceleration (`sqlite-vec`)

Only evaluate acceleration path when one or more of these are true for two consecutive benchmark runs:

- [ ] Corpus exceeds `20,000` chunk embeddings.
- [ ] Hybrid query p95 exceeds `500 ms` on the benchmark query set.
- [ ] Hybrid p95 exceeds `2.5x` lexical p95 after fusion/candidate tuning.
- [ ] Exact-scan CPU cost materially impacts expected CLI usage patterns.

### Re-evaluation Protocol (If Promotion Criteria Trigger)

- [ ] Benchmark both backends on the same frozen corpus, model, and evaluation set.
- [ ] Compare relevance metrics (`Q-033`, `Q-034`, `Q-035`, `Q-036`, `Q-045`, `Q-046`, `Q-047`, `Q-048`) and latency metrics (`Q-037`).
- [ ] Keep acceleration candidate only if relevance is non-regressing and latency improvement is material.
- [ ] Keep rollback procedure documented and tested before switching default backend.

## Target Architecture (Chunk-First)

### Retrieval Overview

- [x] Add retrieval modes to `query`:
  - `lexical` (current behavior)
  - `semantic` (embedding-only candidate generation)
  - `hybrid` (lexical + semantic + fusion)
- [x] Keep existing exact/reference matching logic unchanged as one branch of hybrid.
- [x] Use RRF for fusion with deterministic tie-breakers (part, page, chunk_id).
- [x] Hydrate final results from `chunks` exactly as today so citation fields remain stable.

### Schema Expansion

- [x] Add `embedding_models` table for model identity and reproducibility metadata.
- [x] Add `chunk_embeddings` sidecar table keyed by `chunk_id`.
- [x] Store per-row text fingerprint so stale embeddings can be detected after ingest changes.
- [x] Add indexes for `model_id`, `chunk_id`, and freshness lookup.
- [x] Keep schema compatible with optional future acceleration (`sqlite-vec` or libSQL vector index), but do not require it for first milestone.

Proposed table contract (implementation target):

```sql
CREATE TABLE IF NOT EXISTS embedding_models (
  model_id TEXT PRIMARY KEY,
  backend TEXT NOT NULL,
  model_name TEXT NOT NULL,
  dimensions INTEGER NOT NULL,
  normalize INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  config_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chunk_embeddings (
  chunk_id TEXT NOT NULL,
  model_id TEXT NOT NULL,
  embedding BLOB NOT NULL,
  embedding_dim INTEGER NOT NULL,
  text_hash TEXT NOT NULL,
  generated_at TEXT NOT NULL,
  PRIMARY KEY (chunk_id, model_id),
  FOREIGN KEY (chunk_id) REFERENCES chunks(chunk_id),
  FOREIGN KEY (model_id) REFERENCES embedding_models(model_id)
);
```

## Post-Modularization Implementation Map (Normative)

- [ ] Keep retrieval contract work anchored to current query modules:
  - [x] orchestration and argument flow in `src/commands/query/run.rs`.
  - [ ] lexical/semantic candidate acquisition in `src/commands/query/retrieval.rs`.
  - [ ] fusion/ranking/dedup/output wiring in `src/commands/query/ranking_and_output.rs`.
  - [x] citation and hierarchy helpers in `src/commands/query/hierarchy_and_citation.rs`.
- [x] Keep schema DDL/migration in `src/commands/ingest/db_setup.rs` and treat it as additive-only for WP3 phase 1.
- [x] Keep schema-version fanout synchronized in:
  - [x] `src/commands/ingest/run.rs` (`DB_SCHEMA_VERSION`),
  - [x] `src/commands/validate/prelude_types_part1.rs` (`DB_SCHEMA_VERSION`),
  - [x] `scripts/refresh_quality_artifacts.sh` (`EXPECTED_DB_SCHEMA_VERSION`).
- [x] Add a dedicated semantic indexing command surface in:
  - [x] `src/cli.rs` (new `Embed` args),
  - [x] `src/main.rs` dispatch,
  - [x] `src/commands/mod.rs` export,
  - [x] `src/commands/embed/*` implementation modules.
- [x] Keep semantic/pinpoint validate growth split across new modules under `src/commands/validate/*` rather than extending near-cap files.

Suggested `embed` module baseline (phase 1):

```text
src/commands/embed/
  mod.rs
  run.rs
  model.rs
  payload.rs
  backend.rs
  store.rs
  manifest.rs
  tests.rs
```

## Phase 1 Default Configuration (Locked for Initial Build)

### Runtime Defaults

| Setting | Default | Rationale |
|---|---|---|
| `retrieval_mode` | `lexical` | Safe default while semantic gates are maturing |
| `semantic_model_id` | `miniLM-L6-v2-local-v1` | Lightweight local baseline model identity |
| `semantic_model_name` | `sentence-transformers/all-MiniLM-L6-v2` | Widely used compact embedding model |
| `embedding_dim` | `384` | Expected dimension for initial model |
| `embedding_normalization` | `l2` | Stable cosine similarity behavior |
| `lexical_k` | `96` | Adequate lexical candidate breadth before fusion |
| `semantic_k` | `96` | Symmetric candidate pool for hybrid fusion |
| `rrf_k` | `60` | Common robust RRF rank constant |
| `pinpoint_top_chunks_m` | `12` | Limit intra-chunk precision work to top chunks |
| `pinpoint_units_per_chunk` | `1` | Deterministic default output per result |
| `pinpoint_min_confidence` | `0.55` | Avoid unstable pinpoint claims |

### Embedding Input Canonicalization

- [x] Use a deterministic embedding payload format per chunk type.
- [x] Clause/subclause/annex payload format:
  - [x] `ref + "\n" + heading + "\n\n" + text` (empty fields omitted, whitespace normalized).
- [x] Table payload format:
  - [x] `ref + "\n" + heading + "\n\n" + table_md` (fallback to table text representation if needed).
- [x] Lowercase is not forced; preserve case and normalize only whitespace.
- [x] Hash input exactly as embedded (`text_hash`) so staleness checks are strict.

### Default Operational Switches

- [x] Keep semantic and pinpoint code paths behind explicit flags until gate activation criteria are met.
- [x] Keep lexical-only fallback always available (`--retrieval-mode lexical`).
- [x] Reject semantic/hybrid mode with actionable error when model/index is missing and fallback is disabled.

## Execution Plan

## WP3-A0 - Modularization Gate Revalidation (Hard Prerequisite)

- [x] Revalidate preflight status from `plans/wp3-preflight-modularization-plan.md` and classify outcome as `blocked|provisional|ready`.
- [x] Run structural guardrail command bundle before semantic coding starts:
  - [x] `cargo check`
  - [x] `cargo clippy --all-targets -- -W clippy::too_many_lines -W clippy::cognitive_complexity`
  - [x] `scripts/check_file_size_budget.sh`
- [x] Confirm no unresolved/expired exception entries in `plans/wp3-modularization-exceptions.md`.
- [x] Record the gate outcome and any temporary exception rationale in decision artifacts before WP3-A.

Exit criteria:

- [x] Gate outcome is `provisional` or `ready` (not `blocked`).
- [x] No unapproved file-size guardrail breaches remain.

Evidence snapshot:

- [x] Preflight promoted to `ready` in `plans/wp3-preflight-modularization-plan.md`.
- [x] Ready evidence manifest: `.cache/iso26262/manifests/modularization_baseline/preflight_ready_evidence_20260218T020524Z.json`.
- [x] Decision entry: `.cache/iso26262/manifests/decisions_log.jsonl` (`D-0034`).

## WP3-S0 - Session Bootstrap and Resume Contract

### Startup Preconditions

- [x] Confirm config workspace path via `printenv OPENCODE_CONFIG_DIR`.
- [x] Confirm execution branch via `git rev-parse --abbrev-ref HEAD` (expect `main` for mainline-first mode unless branch/PR mode was explicitly requested).
- [x] Confirm preflight gate outcome in `plans/wp3-preflight-modularization-plan.md` is `provisional` or `ready`.
- [x] Confirm code workspace is cleanly readable and buildable.
- [x] Confirm required paths exist:
  - [x] `.cache/iso26262/`
  - [x] `.cache/iso26262/manifests/`
  - [x] `manifests/` (repo lockfiles)
- [x] Confirm current baseline report exists: `.cache/iso26262/manifests/extraction_quality_report.json`.
- [x] Confirm whether baseline freshness is stale (`Q-022` fail / stale parts present); if stale, run full-target refresh before using baseline validate outcomes.
- [x] Confirm existing citation lockfile exists: `manifests/citation_parity_baseline.lock.json`.
- [x] Confirm semantic model artifacts are available locally (no network dependency at runtime).
- [x] Confirm model cache location is pinned and writable for local-only operation.
- [x] Confirm current implementation stage: semantic-only startup commands are conditional until WP3-A (`query` flags) and WP3-C (`embed` command) are implemented.

### Startup Command Sequence (Deterministic)

1. [x] `printenv OPENCODE_CONFIG_DIR`
2. [x] `git rev-parse --abbrev-ref HEAD`
3. [x] `cargo check`
4. [x] `cargo run -- status --cache-root .cache/iso26262`
5. [x] `cargo run -- validate --cache-root .cache/iso26262`
6. [x] If freshness is stale (`Q-022` failed or stale parts are reported), refresh full target set:
   - [x] `FULL_TARGET_SET=1 TARGET_PARTS="2 6 8 9" WP2_GATE_STAGE=A scripts/refresh_quality_artifacts.sh`
7. [x] Re-run baseline validation after any refresh:
   - [x] `cargo run -- validate --cache-root .cache/iso26262`
8. [x] Run lexical smoke query:
   - [x] `cargo run -- query --query "Table 6" --limit 5 --json`
9. [x] If `embed` command is implemented (WP3-C) and semantic index is missing, build/update embeddings:
   - [x] `cargo run -- embed --cache-root .cache/iso26262 --model-id miniLM-L6-v2-local-v1 --refresh-mode missing-or-stale --batch-size 64`
10. [x] If semantic query flags are implemented (WP3-A), run semantic smoke query:
    - [x] `cargo run -- query --query "single entry single exit" --retrieval-mode semantic --semantic-model-id miniLM-L6-v2-local-v1 --limit 5 --json`

### Resume Tracking Requirements

- [ ] Record current WP3 step and status in run-state/decision artifacts before code edits.
- [x] Record model/config identity in `manifests/semantic_model_config.lock.json` before generating embeddings.
- [x] Record embedding refresh evidence in `.cache/iso26262/manifests/embedding_run_<timestamp>.json`.
- [ ] Record any threshold or formula changes in `decisions_log.jsonl` with rationale.
- [x] Do not rotate semantic/pinpoint baselines without explicit bootstrap/rotation mode and decision entry.

## WP3-A - Retrieval Contract and CLI Surface

- [x] Wire new retrieval options through modular command surfaces (`src/cli.rs`, `src/main.rs`, `src/commands/query/run.rs`).
- [x] Add query flags:
  - [x] `--retrieval-mode lexical|semantic|hybrid` (default `lexical` initially).
  - [x] `--lexical-k` and `--semantic-k` candidate pool sizes.
  - [x] `--fusion rrf` and `--rrf-k` (rank constant).
  - [x] `--semantic-model-id` (required for semantic/hybrid).
- [x] Add JSON response metadata:
  - [x] retrieval mode,
  - [x] candidate source tags,
  - [x] component rank/score traces (metadata-only).
- [x] Add exact-intent detector (clause/table/annex pattern) to preserve strict exact ranking behavior.
- [x] Keep retrieval implementation split by concern (candidate generation in `query/retrieval.rs`, fusion/ranking in `query/ranking_and_output.rs`, citation rendering in `query/hierarchy_and_citation.rs`).

Exit criteria:

- [x] Query CLI can execute all three retrieval modes deterministically.
- [x] Exact-intent queries retain lexical priority semantics.

## WP3-B - Schema Migration and Embedding Sidecar

- [x] Extend ingest schema management (`src/commands/ingest/db_setup.rs`) to create embedding tables with additive migration semantics.
- [x] Add schema version bump and compatibility checks for semantic-capable DBs.
- [x] Synchronize schema-version constants in `src/commands/ingest/run.rs`, `src/commands/validate/prelude_types_part1.rs`, and `scripts/refresh_quality_artifacts.sh`.
- [ ] Add migration tests for existing DBs without embeddings.
- [x] Ensure no extracted text is duplicated in semantic manifest lockfiles.

Exit criteria:

- [ ] Fresh database initializes semantic tables correctly.
- [ ] Existing database migrates without data loss.
- [x] Compatibility checks and runbook defaults accept the new schema version without blocked-state drift.

## WP3-C - Local Embedding Generation Pipeline

- [x] Add dedicated `embed` command (separate from `ingest`) for chunk semantic indexing.
- [x] Add CLI/config surface for `embed` (at minimum: `--cache-root`, `--db-path`, `--model-id`, `--refresh-mode`, `--batch-size`, optional chunk-type filters).
- [x] Add `src/commands/embed/*` module set so embedding payload, backend invocation, storage, and manifest output are separated.
- [x] Default to local model execution only (no network path in default config).
- [x] Compute deterministic `text_hash` from normalized chunk text for staleness detection.
- [x] Embed only eligible chunk types in phase 1 (`clause`, `annex`, `table` text representation where applicable).
- [x] Skip empty/non-text chunks with explicit counters in manifest output.
- [ ] Add resumable batching and progress logging.
- [x] Ensure `embed` writes deterministic run manifests to `.cache/iso26262/manifests/embedding_run_<timestamp>.json`.
- [x] Keep ingest deterministic: `ingest` must not generate or refresh embeddings implicitly.

### Embed Command Contract (Phase 1 Locked)

- [x] Command name for phase 1 is `embed`.
- [x] Minimum command examples:
  - [x] Bootstrap/full refresh:
    - [x] `cargo run -- embed --cache-root .cache/iso26262 --model-id miniLM-L6-v2-local-v1 --refresh-mode full --batch-size 64 --chunk-type clause --chunk-type annex --chunk-type table`
  - [x] Delta refresh (default operational mode):
    - [x] `cargo run -- embed --cache-root .cache/iso26262 --model-id miniLM-L6-v2-local-v1 --refresh-mode missing-or-stale --batch-size 64`
- [x] `embedding_run_<timestamp>.json` required fields:
  - [x] `run_id`, `generated_at`, `model_id`, `model_name`, `embedding_dim`, `normalization`,
  - [x] `eligible_chunks`, `embedded_chunks`, `updated_chunks`, `skipped_empty_chunks`, `stale_rows_before`, `stale_rows_after`,
  - [x] `batch_size`, `duration_ms`, `status`, `warnings`.
- [x] Non-zero stale rows after a successful delta refresh are treated as warning in Stage A and failure in Stage B (`Q-032`).

Exit criteria:

- [ ] `embed` command can bootstrap semantic index from a lexical-only DB.
- [x] `chunk_embeddings` coverage is measurable and reproducible.
- [x] Re-run updates only changed/stale chunks.
- [x] Ingest-only runs and embed runs are independently repeatable.

## WP3-D - Hybrid Query Execution (Chunk Level)

- [x] Implement lexical candidate generation using current exact + FTS logic.
- [x] Implement semantic candidate generation from chunk embeddings.
- [x] Fuse lexical + semantic ranks with RRF.
- [x] Deduplicate by `chunk_id`, then apply current result hydration and citation rendering.
- [x] Keep `with_ancestors` and `with_descendants` behavior compatible with fused results.
- [x] Add deterministic fallback behavior when semantic index/model is missing.
- [x] Keep semantic failure policy explicit: actionable error by default, lexical fallback only when an explicit fallback flag is set.

Exit criteria:

- [x] `query --retrieval-mode hybrid` returns citation-complete results.
- [x] Reference-intent queries remain at least as good as lexical baseline.

## WP3-E - Quality Metrics, Validation, and Gates

- [x] Add semantic evaluation manifest (`semantic_eval_queries.json`) with query intents:
  - [x] exact reference intent,
  - [x] keyword intent,
  - [x] paraphrase intent,
  - [x] concept intent.
- [x] Add semantic quality report artifact (`semantic_quality_report.json`).
- [x] Extend `validate` with semantic/pinpoint check IDs (`Q-031` to `Q-048`) and stage-aware policy.
- [x] Add baseline lockfile for semantic retrieval expectations (`manifests/semantic_retrieval_baseline.lock.json`) using metadata-only fields.
- [x] Add bootstrap/rotation governance mode with decision-log rationale requirements.
- [x] Add explicit query-path exact-intent regression harness (deterministic query probes) so semantic promotion does not rely only on DB-presence checks.

Exit criteria:

- [x] Semantic metrics are generated deterministically and included in validation output.
- [x] Stage A warns and Stage B enforces agreed thresholds.
- [x] Exact-intent non-regression evidence includes end-to-end `query` outputs, not only aggregate DB checks.

## WP3-F - Performance and Operational Hardening

- [x] Add latency benchmark harness for lexical vs semantic vs hybrid modes.
- [x] Record p50/p95 latency and candidate counts per mode.
- [x] Add execution safeguards:
  - [x] bounded `semantic-k`,
  - [x] timeout budget,
  - [x] clear error messages for missing model/index.
- [x] Add operational runbook updates for embedding refresh lifecycle.

Exit criteria:

- [x] Hybrid latency is within accepted budget.
- [x] Operational commands are documented and reproducible.

## WP3-G - Node-Level Second Pass (Deferred After Chunk Green)

- [ ] Define node embedding eligibility policy (only informative node types, minimum text length).
- [ ] Prototype node rerank scoped to top-N chunk candidates (not full-corpus node search).
- [ ] Map node hits back to parent chunk for citation output.
- [ ] Add node-rerank-specific relevance and non-regression checks.

Recommended node scope for first trial:

- [ ] Include: `requirement_atom`, `list_item`, `paragraph`, selected `table_cell`.
- [ ] Exclude: `document`, `list`, `note` containers, empty/short-text nodes.
- [ ] Enforce minimum normalized text length (for example, `>= 32` chars) before embedding.

Exit criteria:

- [ ] Node rerank improves targeted fine-grain intents without citation regressions.

## WP3-H - Intra-Chunk Pinpoint Retrieval (Citation-Safe Precision Layer)

### Purpose

- [x] Add a deterministic second-pass mechanism that finds the most relevant text/table fragment inside a retrieved chunk.
- [x] Improve snippet precision without changing citation authority (citation remains anchored to canonical chunk metadata).
- [x] Support both narrative chunks and table-heavy chunks with row/cell-aware pinpointing.

### Pinpoint Data Model and Relationships

Core relationship (must hold for every pinpoint hit):

- [x] `pinpoint_unit -> parent chunk_id -> canonical citation fields in chunks`.
- [x] Optional node linkage: `pinpoint_unit.origin_node_id -> nodes.node_id` for row/cell/list context.

Phase 1 implementation model (no mandatory new persisted unit table):

- [x] Build pinpoint candidates on demand from top chunk candidates:
  - [x] text windows (sentence/window spans) derived from `chunks.text`.
  - [ ] node-derived spans from `nodes` using `origin_node_id` lineage.
  - [x] table row/cell text from `nodes` where `table_node_id` matches the parent table node.
- [x] Keep output metadata-only for pinpoint structure (no new citation truth source).

Optional Phase 2 persisted model (if latency requires precomputation):

```sql
CREATE TABLE IF NOT EXISTS chunk_units (
  unit_id TEXT PRIMARY KEY,
  chunk_id TEXT NOT NULL,
  unit_type TEXT NOT NULL,         -- sentence_window|list_item|requirement_atom|table_row|table_cell
  unit_index INTEGER NOT NULL,
  text TEXT NOT NULL,
  char_start INTEGER,
  char_end INTEGER,
  origin_node_id TEXT,
  row_idx INTEGER,
  col_idx INTEGER,
  text_hash TEXT NOT NULL,
  FOREIGN KEY(chunk_id) REFERENCES chunks(chunk_id),
  FOREIGN KEY(origin_node_id) REFERENCES nodes(node_id)
);

CREATE TABLE IF NOT EXISTS unit_embeddings (
  unit_id TEXT NOT NULL,
  model_id TEXT NOT NULL,
  embedding BLOB NOT NULL,
  embedding_dim INTEGER NOT NULL,
  text_hash TEXT NOT NULL,
  generated_at TEXT NOT NULL,
  PRIMARY KEY (unit_id, model_id),
  FOREIGN KEY(unit_id) REFERENCES chunk_units(unit_id),
  FOREIGN KEY(model_id) REFERENCES embedding_models(model_id)
);
```

### Pinpoint Query Execution Flow

1. [x] Run normal retrieval (`lexical`/`semantic`/`hybrid`) to get top `M` chunks.
2. [x] Expand each chunk into pinpoint candidates:
   - [ ] narrative: sentence windows with overlap.
   - [ ] list/requirement: `list_item` and `requirement_atom` descendants.
   - [x] table: `table_row`/`table_cell` descendants, preserving `row_idx`/`col_idx`.
3. [ ] Score pinpoint candidates with a local blend:
   - [ ] semantic similarity (query embedding vs candidate embedding or on-demand embed),
   - [ ] lexical overlap (query token hit, exact phrase bonus),
   - [ ] structural prior (bonus for `requirement_atom` and table marker rows when query intent suggests them).
4. [x] Select top pinpoint unit per returned chunk (or top `n` if requested).
5. [x] Return pinpoint payload alongside unchanged canonical citation fields.
6. [ ] Fallback to chunk snippet when pinpoint confidence is below threshold.

### Table-Specific Pinpointing Rules

- [x] For `type=table` chunks, prioritize row-level candidates before cell-level candidates.
- [x] Keep `row_idx`/`col_idx` in response metadata when available.
- [ ] Add ASIL/marker-aware lexical hints for known patterns (`asil`, `qm`, `a`, `b`, `c`, `d`, marker tokens like `1a`, `1b`, etc.).
- [ ] For multi-cell matches in the same row, emit row-composed snippet first, then best supporting cell snippet.
- [x] Preserve table citation at chunk level; include row/cell locator as non-authoritative precision metadata.

### Query JSON Contract Additions (Pinpoint)

- [ ] `pinpoint_text`
- [ ] `pinpoint_unit_type`
- [ ] `pinpoint_score`
- [ ] `pinpoint_confidence` (`low|medium|high`)
- [ ] `pinpoint_origin_node_id` (optional)
- [ ] `pinpoint_row_idx` / `pinpoint_col_idx` (optional)
- [ ] `pinpoint_char_start` / `pinpoint_char_end` (optional)
- [x] `pinpoint_fallback_used` (boolean)

Exit criteria:

- [x] Pinpoint snippets improve within-chunk relevance on evaluation set while preserving citation parity.
- [x] Table queries can surface row/cell-level evidence metadata without changing citation authority.

## Evaluation Dataset Contracts (Normative)

### Semantic Evaluation Set Schema (`semantic_eval_queries.json`)

- [ ] Required fields per query record:
  - [ ] `query_id` (stable identifier)
  - [ ] `query_text`
  - [ ] `intent` (`exact_ref|keyword|paraphrase|concept|table_intent`)
  - [ ] `expected_chunk_ids` (non-empty for scored queries)
  - [ ] `expected_refs` (optional, for human review + exact-intent checks)
  - [ ] `expected_anchor_ids` (optional)
  - [ ] `must_hit_top1` (boolean; required for exact-intent queries)
  - [ ] `part_filter` / `chunk_type_filter` (optional)
  - [ ] `notes`
- [ ] Keep `query_id` stable across runs; never recycle IDs for different intent semantics.

### Pinpoint Evaluation Set Schema (`pinpoint_eval_queries.json`)

- [ ] Required fields per query record:
  - [ ] `query_id`
  - [ ] `query_text`
  - [ ] `parent_expected_chunk_ids` (candidate chunk ground truth)
  - [ ] `expected_unit_ids` (optional when stable unit IDs are available)
  - [ ] `expected_token_sets` (array of token arrays; any set can satisfy relevance)
  - [ ] `expected_row_keys` (optional for table intents, format `chunk_id:row_idx`)
  - [ ] `high_confidence` (boolean; used by fallback-ratio metric)
  - [ ] `intent` (`narrative|requirement|table_row|table_cell`)
  - [ ] `notes`

### Labeling and Review Protocol

- [ ] Maintain at least two labeled queries per target reference family (Part 2/6/8/9 coverage preserved).
- [ ] For every new semantic model or scoring rule change:
  - [ ] re-review a stratified sample,
  - [ ] update labels only with decision-log rationale,
  - [ ] rotate baselines explicitly.
- [ ] Avoid labels that depend on copyrighted verbatim text in repo-tracked lockfiles; keep lockfiles metadata-only.

### Query Slice Coverage Contract (for Holistic Progress Tracking)

- [ ] Keep explicit intent slices in eval sets:
  - [ ] `exact_ref`
  - [ ] `keyword`
  - [ ] `paraphrase`
  - [ ] `concept`
  - [ ] `table_intent`
- [ ] Stage A minimum query counts:
  - [ ] `exact_ref >= 35` (at least one per target reference),
  - [ ] `keyword >= 25`,
  - [ ] `paraphrase >= 25`,
  - [ ] `concept >= 25`,
  - [ ] `table_intent >= 20`.
- [ ] Stage B minimum query counts:
  - [ ] `exact_ref >= 70`,
  - [ ] `keyword >= 40`,
  - [ ] `paraphrase >= 40`,
  - [ ] `concept >= 40`,
  - [ ] `table_intent >= 30`.
- [ ] Use graded relevance labels (`0/1/2` minimum) where feasible so `nDCG@10` reflects ranking quality beyond binary hits.
- [ ] Keep a fixed holdout subset that is never used for tuning thresholds/weights.

## Metric Definitions (Normative Formula Set)

### Notation

- [ ] Let `Q_sem` be semantic/paraphrase/concept evaluation queries.
- [ ] Let `Q_exact` be exact-reference intent queries.
- [ ] Let `Q_pin` be pinpoint evaluation queries.
- [ ] Let `TopK(q, mode)` be ranked result set for query `q` and retrieval mode.
- [ ] Let `G_chunk(q)` be expected chunk IDs for query `q`.
- [ ] Let `G_row(q)` be expected row keys (`chunk_id:row_idx`) for table pinpoint queries.

### Coverage and Freshness Metrics

- [ ] `Q-031 Chunk embedding coverage ratio`
  - [ ] Formula: `eligible_embedded_chunks / eligible_chunks`.
  - [ ] `eligible_chunks` = non-empty chunks in allowed phase-1 types.
- [ ] `Q-032 Stale embedding ratio`
  - [ ] Formula: `stale_embedding_rows / embedding_rows_for_active_model`.
  - [ ] `stale_embedding_rows` = rows where `text_hash` mismatch, wrong `embedding_dim`, or missing active `model_id` mapping.

### Retrieval Relevance and Non-Regression Metrics

- [ ] `Q-033 Semantic nDCG@10` (primary relevance metric)
  - [ ] Per-query: `nDCG@10(q) = DCG@10(q) / IDCG@10(q)`.
  - [ ] `DCG@10(q) = sum_{i=1..10} ((2^{rel_i} - 1) / log2(i + 1))` using graded labels where available.
  - [ ] Aggregate: mean over `Q_sem`.
- [ ] `Q-034 Hybrid nDCG@10 uplift vs lexical baseline` (primary improvement metric)
  - [ ] Formula: `mean_q(nDCG@10_hybrid(q)) - mean_q(nDCG@10_lexical(q))` over `Q_sem`.
- [ ] `Q-035 Exact reference Top-1 hit rate`
  - [ ] Per-query hit: `1` if top result chunk in `Top1(q, hybrid)` belongs to `G_chunk(q)`.
  - [ ] Aggregate: mean over `Q_exact`.
- [ ] `Q-036 Citation parity`
  - [ ] No regression allowed on lockfile comparisons for top1/top3/page-range parity.

### Additional Standard IR Quality Metrics

- [ ] `Q-045 Hybrid MRR@10 on first-hit intents`
  - [ ] Query subset: first-hit intents (`exact_ref`, high-priority `keyword`, and selected `table_intent`).
  - [ ] Per-query reciprocal rank: `RR@10(q) = 1/r` for first relevant rank `r <= 10`, else `0`.
  - [ ] Aggregate: `MRR@10 = mean_q(RR@10(q))`.
- [ ] `Q-046 Hybrid Recall@50 non-regression`
  - [ ] Per-query recall: `Recall@50(q) = |Top50(q, hybrid) ∩ G_chunk(q)| / |G_chunk(q)|`.
  - [ ] Gate is evaluated as delta to lexical baseline over same query IDs.
- [ ] `Q-047 Judged@10 label completeness`
  - [ ] Per-query judged ratio: `Judged@10(q) = judged_docs_in_top10 / 10`.
  - [ ] Aggregate: mean over query set slices; used as evaluation-trustworthiness guardrail.
- [ ] `Q-048 Significance + effect-size confidence for nDCG uplift`
  - [ ] Require paired per-query comparison between hybrid and lexical on identical query IDs.
  - [ ] Compute p-value (paired test) and bootstrap 95% CI for `delta nDCG@10`.
  - [ ] Stage gates depend on both statistical confidence and practical effect size (not p-value alone).

### Determinism and Latency Metrics

- [ ] `Q-037 Hybrid p95 latency budget`
  - [ ] Formula: p95 over benchmark query set, compared against lexical p95 and absolute cap.
- [ ] `Q-038 Retrieval determinism`
  - [ ] Run same query set `N` repeated times.
  - [ ] Per-query score: Jaccard overlap of top-k chunk IDs between run pairs.
  - [ ] Aggregate: mean overlap across queries and run pairs.

### Pinpoint Precision Metrics

- [ ] `Q-039 Pinpoint@1 relevance`
  - [ ] Per-query hit: `1` if top pinpoint unit matches `expected_unit_ids` OR contains all tokens from at least one `expected_token_sets` entry.
  - [ ] Aggregate: mean over `Q_pin`.
- [ ] `Q-040 Table pinpoint row accuracy@1`
  - [ ] Per-query hit: `1` if top pinpoint row key (`chunk_id:row_idx`) is in `G_row(q)`.
  - [ ] Aggregate: mean over table-intent subset of `Q_pin`.
- [ ] `Q-041 Pinpoint citation-anchor consistency`
  - [ ] Mismatch count where pinpoint payload cannot be proven descendant/compatible with parent result citation context.
  - [ ] Required value: `0`.
- [ ] `Q-042 Pinpoint fallback ratio`
  - [ ] Formula: `fallback_count / high_confidence_query_count` over `high_confidence=true` subset.
- [ ] `Q-043 Pinpoint determinism`
  - [ ] Per-query hit: `1` if repeated runs choose same top pinpoint `unit_id` (or same row key/token signature when unit IDs unavailable).
  - [ ] Aggregate: mean over `Q_pin`.
- [ ] `Q-044 Pinpoint latency overhead`
  - [ ] Formula: `p95(query_with_pinpoint) - p95(query_without_pinpoint)` on identical query set.

### Denominator and Null Handling Rules

- [ ] If any metric denominator is zero, report metric as `null`, emit warning, and mark check `pending` (never silently pass).
- [ ] Stage B cannot be enabled for checks with unresolved `pending` status in two consecutive runs.
- [ ] All metric computations must be deterministic under fixed corpus, fixed model, and fixed query set.
- [ ] If `Judged@10` drops below stage threshold, relevance metrics (`nDCG`, `MRR`, `Recall`) are reported with degraded confidence and cannot be used for Stage B promotion.

## Validation and Test Matrix (Normative)

### Unit-Level Tests

- [ ] Embedding payload canonicalization tests:
  - [ ] same input text yields same hash,
  - [ ] whitespace normalization is deterministic,
  - [ ] chunk-type-specific payload builder works for clause and table paths.
- [ ] Similarity math tests:
  - [ ] cosine similarity bounds and monotonic ordering checks,
  - [ ] stable ordering with deterministic tie-breaks.
- [ ] RRF fusion tests:
  - [ ] known candidate lists produce expected fused ranking,
  - [ ] missing branch candidates handled without panic.
- [ ] Pinpoint candidate extraction tests:
  - [ ] sentence window boundaries,
  - [ ] list/requirement extraction from lineage,
  - [ ] table row/cell locator mapping.

### Integration Tests

- [ ] Query mode contract tests (`lexical`, `semantic`, `hybrid`) with deterministic JSON fields.
- [ ] Exact reference non-regression fixture tests (`Q-035` behavior).
- [ ] Citation parity fixture tests (`Q-036` behavior) under hybrid and pinpoint-enabled paths.
- [ ] Pinpoint JSON payload contract tests (presence/typing of pinpoint fields, fallback semantics).
- [ ] Intent-slice metric tests ensure all required slices are present and independently scored.
- [ ] Judged-coverage tests ensure low-judgment slices are flagged before promotion.

### End-to-End Gate Tests

- [ ] `validate` generates semantic and pinpoint quality reports with all check IDs (`Q-031` to `Q-048`).
- [ ] Stage policy tests for warning vs hard-fail transitions.
- [ ] Baseline lockfile bootstrap/verify/rotation path tests.
- [ ] Determinism replay tests across repeated runs.
- [ ] Paired significance test checks (`hybrid` vs `lexical`) and bootstrap CI checks for `delta nDCG@10`.

## Metric Targets and Stage Policy

Proposed semantic checks for `validate`:

| Check ID | Metric | Stage A warning | Stage B hard fail |
|---|---|---:|---:|
| Q-031 | Chunk embedding coverage ratio | < 0.98 | < 0.995 |
| Q-032 | Stale embedding ratio | > 0.02 | > 0.0 |
| Q-033 | Semantic nDCG@10 on paraphrase/concept set | < 0.60 | < 0.72 |
| Q-034 | Hybrid nDCG@10 uplift vs lexical baseline | < +0.03 | < +0.06 |
| Q-035 | Exact reference Top-1 hit rate in hybrid | < 1.0 | < 1.0 |
| Q-036 | Citation parity (top1/top3/page range) in hybrid | any drop | any drop |
| Q-037 | Hybrid p95 latency budget | > 2.5x lexical p95 | > 2.5x lexical p95 or > 500 ms |
| Q-038 | Retrieval determinism (top-k overlap repeated runs) | < 0.95 | < 0.98 |
| Q-045 | Hybrid MRR@10 on first-hit intents | < 0.80 | < 0.90 |
| Q-046 | Hybrid Recall@50 non-regression vs lexical baseline | drop > 0.02 | any drop |
| Q-047 | Judged@10 label completeness | < 0.70 | < 0.85 |
| Q-048 | Significance + effect-size confidence for `delta nDCG@10` | CI includes 0 or p >= 0.10 | CI includes 0 or p >= 0.05 |
| Q-039 | Pinpoint@1 relevance (expected span/token set hit) | < 0.70 | < 0.82 |
| Q-040 | Table pinpoint row accuracy@1 (table-intent set) | < 0.70 | < 0.85 |
| Q-041 | Pinpoint citation-anchor consistency | any mismatch > 0 | any mismatch > 0 |
| Q-042 | Pinpoint fallback ratio (high-confidence queries) | > 0.35 | > 0.20 |
| Q-043 | Pinpoint determinism (same top unit repeated runs) | < 0.95 | < 0.98 |
| Q-044 | Pinpoint latency overhead per result | > +60 ms p95 | > +40 ms p95 |

Notes:

- Baseline values should be established from a locked lexical-only run before enabling hybrid by default.
- Stage B semantic checks should remain disabled until WP3-A through WP3-E are complete and baseline lockfiles are present.
- Pinpoint checks (`Q-039` to `Q-044`) should run as Stage A warnings until WP3-H implementation is complete and evaluation labels are stable.

## Benchmark Protocol (Normative)

### Environment Lock

- [ ] Record benchmark host manifest for each run:
  - [ ] CPU model and core/thread count,
  - [ ] RAM,
  - [ ] storage type,
  - [ ] OS/kernel,
  - [ ] Rust toolchain,
  - [ ] active model ID.
- [ ] Run benchmarks on AC power, stable governor settings, minimal background load.

### Execution Method

- [ ] Use a fixed benchmark query set snapshot for comparability.
- [ ] Warmup: run 2 untimed passes per mode.
- [ ] Timed runs: run 5 passes per mode (`lexical`, `semantic`, `hybrid`, and `hybrid+pinpoint` when enabled).
- [ ] Randomize query order identically across modes for each pass.
- [ ] Measure end-to-end query latency at CLI command boundary.

### Aggregation Rules

- [ ] p50/p95 are computed over all timed queries in all timed passes for a mode.
- [ ] Report mode-specific candidate counts (`lexical_k`, `semantic_k`, fused size) with latency metrics.
- [ ] Compute overhead metrics against lexical baseline from the same benchmark session.
- [ ] Flag run invalid if timed query failures exceed `1%`.

## Gate Activation and Promotion Criteria

### Stage Transition Rules

- [ ] Phase `A0` (implementation): checks `Q-031` to `Q-048` run as warnings only.
- [ ] Phase `A1` (stabilization):
  - [ ] require 3 consecutive Stage A runs with no `pending` metrics for semantic core checks (`Q-031` to `Q-038`, `Q-045` to `Q-048`),
  - [ ] require baseline lockfiles present and validated,
  - [ ] require exact-reference non-regression (`Q-035`) already perfect.
- [x] Phase `B1` (hard gate semantic core): promote semantic core checks (`Q-031` to `Q-038`, `Q-045` to `Q-048`) to Stage B hard fail.
- [x] Phase `B2` (hard gate pinpoint): promote `Q-039` to `Q-044` only after 2 consecutive Stage A passes with stable labels and no `pending` status.

### Default Mode Promotion

- [ ] Keep default query mode as `lexical` until `B1` passes in 2 consecutive full-target runs.
- [ ] Change default to `hybrid` only after:
  - [ ] `Q-033`, `Q-034`, `Q-035`, `Q-036`, `Q-037`, `Q-038`, `Q-045`, `Q-046`, `Q-047`, `Q-048` all pass in Stage B,
  - [ ] decision-log entry records rationale and rollback command.
- [ ] Keep pinpoint disabled-by-default until `B2` passes.

## Failure Handling and Rollback Playbook

### Runtime Failure Policy

- [x] Missing semantic model/index in semantic/hybrid mode:
  - [x] return actionable error by default,
  - [x] optionally fallback to lexical only when explicit fallback flag is enabled.
- [ ] Pinpoint failure (candidate generation/scoring error):
  - [ ] mark `pinpoint_fallback_used=true`,
  - [ ] preserve parent chunk result and citation output,
  - [ ] emit structured warning counter.

### Gate Failure Policy

- [ ] If any Stage B semantic check fails, keep default mode `lexical` and block promotion.
- [ ] If exact-reference check (`Q-035`) fails once, require rollback to last passing retrieval configuration.
- [ ] If citation parity (`Q-036`) fails, treat as release blocker until resolved.

### Rollback Procedure (Operational)

1. [ ] Set query mode default to lexical and disable semantic/pinpoint feature flags.
2. [ ] Re-run `validate` to confirm lexical baseline remains green.
3. [ ] Revert model/config change or fusion parameter change that triggered regression.
4. [ ] Re-run Stage A benchmark/evaluation loop before any re-promotion attempt.
5. [ ] Record rollback decision and evidence in `decisions_log.jsonl`.

## Artifacts and Governance

Repo-tracked (safe metadata only):

- [x] `manifests/semantic_retrieval_baseline.lock.json`
- [x] `manifests/semantic_model_config.lock.json`
- [ ] `manifests/pinpoint_retrieval_baseline.lock.json`

Required metadata contract (repo-tracked lockfiles):

- [x] `semantic_model_config.lock.json` must include:
  - [x] `model_id`, `model_name`, `embedding_dim`, `normalization`, `runtime_backend`, `created_at`, `checksum`.
- [x] `semantic_retrieval_baseline.lock.json` must include:
  - [x] check IDs (`Q-031` to `Q-038`, `Q-045` to `Q-048`),
  - [x] query IDs used,
  - [x] threshold values,
  - [x] summary metrics,
  - [x] baseline run ID/checksum.
- [ ] `pinpoint_retrieval_baseline.lock.json` must include:
  - [ ] check IDs (`Q-039` to `Q-044`),
  - [ ] query IDs used,
  - [ ] summary metrics,
  - [ ] baseline run ID/checksum.
- [x] All lockfiles must exclude extracted text/snippets/table payloads.

Cache-local runtime artifacts:

- [x] `.cache/iso26262/manifests/semantic_eval_queries.json`
- [x] `.cache/iso26262/manifests/semantic_quality_report.json`
- [x] `.cache/iso26262/manifests/embedding_run_<timestamp>.json`
- [x] `.cache/iso26262/manifests/pinpoint_eval_queries.json`
- [x] `.cache/iso26262/manifests/pinpoint_quality_report.json`

Governance controls:

- [x] No automatic baseline creation in standard validate path.
- [x] Explicit bootstrap mode required for first baseline creation.
- [x] Explicit rotation mode required for baseline updates with decision-log rationale.

## Commit and Rollout Plan

- [ ] `feat(query): add backend abstraction for local semantic retrieval and future acceleration`
- [x] `feat(schema): add chunk embedding sidecar tables and versioning`
- [x] `feat(cli): add dedicated embed command surface and semantic config flags`
- [x] `feat(embed): add local chunk embedding generation pipeline and freshness tracking`
- [x] `feat(query): add semantic and hybrid retrieval modes with rrf fusion`
- [x] `feat(query): add within-chunk pinpoint retrieval and response metadata`
- [ ] `test(query): add deterministic fusion and pinpoint extraction coverage`
- [x] `feat(validate): add semantic retrieval metrics and staged gates`
- [ ] `test(validate): add pinpoint relevance and table-row precision checks`
- [x] `perf(bench): add semantic benchmark harness and environment manifest output`
- [x] `docs(runbook): add semantic indexing and baseline governance workflow`
- [ ] `feat(query): add optional node-level rerank within chunk candidate set` (deferred)

Rollout phases:

- [x] Phase 1: lexical default, semantic optional (developer opt-in).
- [x] Phase 2: hybrid recommended when Stage A semantic checks are stable.
- [ ] Phase 3: hybrid default only after Stage B semantic checks are green.

## Risks and Mitigations

- [ ] Risk: semantic retrieval regresses exact-reference precision.
  - [ ] Mitigation: exact-intent routing + Q-035 hard fail.
- [ ] Risk: embedding drift from model/config changes.
  - [ ] Mitigation: model config lockfile + explicit baseline rotation policy.
- [ ] Risk: embedding refresh is skipped because indexing is now command-separated from ingest.
  - [ ] Mitigation: enforce `Q-032` stale-row checks, require `embed` step in runbook, and return actionable semantic-mode errors when index/model is missing.
- [ ] Risk: short/noisy node text hurts second-pass quality.
  - [ ] Mitigation: defer node pass and enforce node eligibility thresholds.
- [ ] Risk: performance regressions from large candidate pools.
  - [ ] Mitigation: bounded pools, latency gates, optional backend acceleration later.
- [ ] Risk: accidental text egress via remote providers.
  - [ ] Mitigation: local-only default, no remote provider wiring in initial milestone.

## Definition of Done (WP3 Chunk-Level Completion)

- [x] Query supports `lexical`, `semantic`, and `hybrid` modes.
- [ ] Dedicated `embed` command exists, is resumable, and can refresh missing-or-stale embeddings without re-running ingest.
- [x] Semantic index exists for chunks with >=99.5% coverage and zero stale rows after refresh.
- [x] Hybrid mode improves paraphrase/concept ranking quality by at least +0.06 `nDCG@10` vs lexical baseline.
- [x] Hybrid first-hit quality is strong on first-hit intents (`Q-045` Stage B pass).
- [x] Evaluation label coverage and confidence gates pass (`Q-047`, `Q-048`).
- [x] Exact-reference Top-1 behavior remains perfect (`Q-035` pass).
- [x] Citation parity remains unchanged from lexical baseline (`Q-036` pass).
- [x] Hybrid latency remains within agreed p95 budget (`Q-037` pass).
- [x] Pinpoint@1 relevance and table-row pinpoint accuracy meet Stage B targets (`Q-039`, `Q-040`).
- [x] Pinpoint units remain citation-consistent with parent chunk metadata (`Q-041` pass).
- [x] Semantic lockfiles and evaluation artifacts are generated and governed.
- [x] Node-level rerank remains explicitly deferred until chunk-level semantic gates are green.
- [x] Ingest and semantic indexing lifecycles remain decoupled (ingest does not mutate `chunk_embeddings` directly).

## Suggested First Implementation Sequence

1. [x] Revalidate modularization gate (`WP3-A0`) and record `blocked|provisional|ready` outcome.
2. [x] Lock backend decision record (local-first, exact KNN baseline, acceleration criteria).
3. [x] Lock semantic schema + model config contracts and apply schema-version fanout updates.
4. [x] Implement dedicated `embed` command and manifest workflow (missing-or-stale refresh first).
5. [x] Implement semantic-only query path and JSON traces.
6. [x] Implement hybrid RRF fusion with exact-intent guardrails.
7. [x] Add semantic evaluation set plus query-path exact-intent regression harness; wire `validate` checks (`Q-031` to `Q-038`, `Q-045` to `Q-048`).
8. [x] Run Stage A tuning loop, set semantic baseline lockfiles, then enable Stage B semantic-core gate.
9. [x] Implement within-chunk pinpoint retrieval and then add/activate `Q-039` to `Q-044` promotion flow.

## Active Tuning Loop (Current Sprint)

### Pinpoint Quality Recovery Steps (Q-039 to Q-044)

1. [ ] Diagnose dominant pinpoint misses from `pinpoint_quality_report.json`:
   - [ ] classify `relevance_hit_at_1=false` by intent (`narrative|requirement|table_row|table_cell`),
   - [ ] classify row-key misses and anchor mismatches,
   - [ ] identify cases where parent chunk was correct but top unit ranking was weak.
2. [ ] Improve pinpoint candidate generation:
   - [ ] prioritize node-derived `table_row` candidates before `table_cell` for table intents,
   - [ ] include sentence windows plus requirement/list descendants for narrative/requirement intents,
   - [ ] preserve deterministic tie-breakers by `(score desc, structural-priority desc, unit_id asc)`.
3. [ ] Improve pinpoint scoring:
   - [ ] add intent-aware structural priors (requirement/list vs table row),
   - [ ] strengthen phrase-containment and token-coverage blend,
   - [ ] penalize anchor-incompatible units and low-signal boilerplate fragments.
4. [ ] Improve fallback behavior:
   - [ ] require minimum confidence before replacing parent snippet,
   - [ ] force fallback for low-confidence top units while keeping citation-safe metadata.

### Pinpoint Label Stabilization Steps

1. [ ] Tighten `pinpoint_eval_queries.json` labels:
   - [ ] ensure `parent_expected_chunk_ids` align with current semantic eval chunk IDs,
   - [ ] enrich `expected_unit_ids` for high-confidence table/requirement intents,
   - [ ] normalize and dedupe `expected_token_sets` and `expected_row_keys`.
2. [ ] Add label-review guardrails:
   - [ ] preserve stable `query_id`s,
   - [ ] document any label rotations with decision-log rationale,
   - [ ] avoid introducing verbatim extracted text into repo-tracked lockfiles.

### Semantic Stage-B Gap Closure Steps (Q-033)

1. [ ] Slice semantic misses by intent and chunk type using `semantic_quality_report.json`.
2. [ ] Tune hybrid ranking for non-exact intents without weakening `Q-035`/`Q-036`:
   - [ ] adjust lexical/semantic blend and exact-intent routing boundaries,
   - [ ] verify uplift remains statistically meaningful (`Q-048`).
3. [ ] Re-run full Stage A validation loop after each tuning batch:
   - [ ] `cargo check`, `cargo test`, `scripts/check_file_size_budget.sh`,
   - [ ] `scripts/smoke_part6.sh`,
   - [ ] `WP2_GATE_STAGE=A cargo run -- validate --cache-root .cache/iso26262`.
4. [ ] Track per-batch metric deltas and stop criteria:
   - [ ] target `Q-033 >= 0.72`,
   - [ ] maintain `Q-035 = 1.0` and `Q-036 = 1.0`,
   - [ ] keep pinpoint overhead/fallback within Stage B budgets before promotion.
