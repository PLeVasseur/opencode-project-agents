# Part 6 Table 1 Real Lexical/Semantic Retrieval Rebuild Plan

## Objective

- [ ] Make `rust_reference.sqlite` answer real user questions about ISO 26262 Part 6 Table 1 with grounded, useful evidence.
  - [x] Support lexical queries (keyword-driven) and semantic queries (natural-language intent/paraphrase).
  - [x] Support two primary user intents: identifying potential issues and identifying candidate resolutions.
  - [x] Keep traceability to Table 1 rows (`1a`..`1i`) without making row/category hints the ranking engine.
  - [ ] Return explainable results: anchors, snippets, row linkage, and score components.

## Model Stack and Backend Choice

- [x] Use real embedding and reranking models (no token-overlap surrogate scoring).
  - [x] Primary embedder: `Qwen/Qwen3-Embedding-4B`.
  - [x] Primary reranker: `BAAI/bge-reranker-v2-m3`.
  - [ ] Challenger embedder for bakeoff: `BAAI/bge-m3` (latency/quality tradeoff check).
- [x] Run model inference through explicit backend profile.
  - [x] Primary backend: `tei-http` profile with configurable endpoint/timeouts.
  - [x] Add startup/backend health check for semantic and hybrid modes.
  - [x] In `semantic` mode, fail loudly when backend is unavailable (no silent fake semantic fallback).

## Local-Only Operation (No Hosted Dependency)

- [x] Keep the entire retrieval system runnable on one machine.
  - [x] SQLite DB, query scripts, eval scripts, and semantic inference all run locally.
  - [x] Default semantic endpoint is `http://127.0.0.1:8080`.
  - [x] No hosted API dependency for normal query/eval runs.
- [ ] Support air-gapped operation after one-time model acquisition.
  - [x] Cache models locally and pin model IDs/revisions used by each snapshot.
  - [x] Record local cache path and model metadata in retrieval reports.
  - [ ] Ensure semantic/hybrid eval can run offline once models are present.

## Local Backend Implementation Workstream (Required)

- [x] Make local semantic backend startup fully owned by repo tooling (no manual side setup).
  - [x] Add a local backend launcher script to start/stop/status a local embedding+reranker stack.
  - [x] Run embedder and reranker as separate local services (default loopback ports) and wire both into query/eval scripts.
  - [x] Add readiness wait logic and fail-loud diagnostics when either local service is unavailable.
  - [x] Add optional auto-start/auto-stop flow for semantic CI/eval commands so one command can run end-to-end locally.
- [x] Standardize local backend config.
  - [x] Add explicit env/CLI config for embed and rerank base URLs (`RUST_REF_TEI_EMBED_BASE_URL`, `RUST_REF_TEI_RERANK_BASE_URL`).
  - [x] Keep backward-compatible single-URL mode for existing scripts while preferring split URLs for local backend services.
  - [x] Record backend profile and endpoint details in retrieval reports for reproducibility.
- [x] Add operational docs for local backend lifecycle.
  - [x] Document local launch command(s), model cache volume, and teardown command.
  - [x] Document CPU-first defaults and optional GPU flags for faster local runs.
  - [x] Document troubleshooting for health, embed, and rerank failures.

## Local Backend Pivot (Python-First, Docker-Optional)

- [x] Make Python local backend the default runtime for semantic/hybrid retrieval.
  - [x] Run local embedding and reranking workers as native Python processes bound to loopback.
  - [x] Keep Docker launcher as optional fallback, not default path.
  - [x] Keep endpoint contract identical (`/health`, `/v1/embeddings`, `/v1/rerank`).
- [x] Preserve mandated model choices on local backend.
  - [x] Embedder: `Qwen/Qwen3-Embedding-4B`.
  - [x] Reranker: `BAAI/bge-reranker-v2-m3`.
  - [x] Fail loudly with actionable diagnostics when model loading/runtime fails.
- [x] Update CI/eval launcher defaults for Python-first backend.
  - [x] Semantic lane auto-start uses Python backend by default.
  - [x] Eval auto-start uses Python backend by default.
  - [x] Startup timeout defaults reduced to practical values (120-180s) with override.
- [x] Update docs and reports for Python-first backend profile.
  - [x] Document dependency bootstrap path for local Python backend.
  - [x] Document cache and process lifecycle commands.
  - [x] Record backend profile (`python-local` vs `docker`) in retrieval reports.

## Python-Only Execution Policy (No Docker for This Rebuild)

- [ ] Enforce python-local backend only for all remaining semantic/hybrid work in this plan.
  - [ ] Do not use `docker` backend engine for local semantic startup, eval, CI, or smoke execution.
  - [ ] Treat python-local startup/runtime failures as issues to fix in launcher/worker/config, not reasons to switch engines.
  - [ ] Keep fail-loud behavior when python-local backend is unavailable in non-degraded runs.

## Semantic Indexing Policy (Materialize-First)

- [ ] Make semantic/hybrid retrieval materialization-first for corpus embeddings.
  - [ ] Require corpus embedding materialization before semantic/hybrid query and eval runs.
  - [ ] Keep query-time embedding limited to query text by default (no corpus backfill in request path).
  - [ ] Keep explicit opt-in online corpus embedding only for local experimentation.
- [ ] Enforce semantic index completeness in non-degraded modes.
  - [ ] If candidate corpus rows are missing embeddings for active model, fail with explicit index-incomplete error.
  - [ ] Include missing-embedding counts and sample IDs in fail-loud diagnostics.
  - [ ] Keep degraded mode behavior explicit and unchanged (`--allow-degraded` only).
- [ ] Improve startup/query reliability for required large models.
  - [ ] Tune default semantic timeouts for local large-model CPU runs.
  - [ ] Add bounded candidate pool defaults for semantic/rerank stages.
  - [ ] Ensure preflight health+probe does not hide long-running inference timeout risks.
- [ ] Add CI/eval checks for materialize-first behavior.
  - [ ] Semantic CI lane must run materialization before semantic/hybrid eval.
  - [ ] Add test that semantic query fails fast with index-incomplete error when materialization is skipped.
  - [ ] Add non-degraded semantic smoke with required model IDs using pre-materialized embeddings.
- [x] Add long-run materialization progress telemetry.
  - [x] Persist periodic progress checkpoints to a file under `.cache/sqlite_kb/reports/rust_reference/`.
  - [x] Include cached count, remaining count, throughput, and ETA in progress events.
  - [x] Record completion/failure event so interrupted sessions can resume with audit trail.

## Mechanism-Gating Removal Plan (Critical Unblocker)

- [x] Replace mechanism-gated corpus contract with a full statement corpus contract.
  - [x] Add `statement_corpus_v3_all` selecting from `statements + sections + source_documents` only.
  - [x] Remove `mechanism_evidence` / `row_mechanisms` joins from corpus membership.
  - [x] Keep deterministic ordering and no hidden row-limit truncation for full-corpus runs.
- [x] Make semantic materialization and semantic query use full statement corpus by default.
  - [x] `sqlite_materialize_rust_reference_embeddings.py` materializes all statements unless explicit scope flag is set.
  - [x] `sqlite_query_rust_reference.py` semantic/hybrid candidate loading uses full-corpus contract.
  - [x] Keep query-time embedding limited to query text in non-degraded modes.
- [x] Rebuild row projection to avoid build-time row-mechanism priors.
  - [x] Derive row relevance at query time from retrieved statements against `table1_rows.requirement_text`.
  - [x] Stop depending on preassigned `row_markers` from build-time mappings for projection.
  - [x] Return row evidence trace (`statement_id`, anchor, contribution) from retrieved hits.
- [x] Keep mechanism taxonomy optional and non-gating.
  - [x] Mechanism metadata may be surfaced as explainability, but never as corpus inclusion gate.
  - [x] Retrieval corpus coverage must not depend on mechanism detection.
  - [x] CI fails if full-corpus coverage drops below `COUNT(statements)` without explicit scoped mode.
- [ ] Validate closure with explicit parity checks.
  - [x] Full corpus contract count equals `SELECT COUNT(*) FROM statements`.
  - [x] Materialized embeddings for active model equal full corpus count in non-scoped mode.
  - [ ] Non-degraded semantic/hybrid eval passes with required models over pre-materialized embeddings.

## New Session Bootstrap (Copy/Paste Runbook)

- [x] Confirm environment and plan path.
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -f "$OPENCODE_CONFIG_DIR/plans/part6-table1-real-lexical-semantic-retrieval-plan.md"`
- [ ] Export default retrieval env vars.
  - [ ] `export RUST_REF_DB_PATH=.cache/sqlite_kb/current/rust_reference.sqlite`
  - [ ] `export RUST_REF_TEI_BASE_URL=http://127.0.0.1:8080`
  - [ ] `export RUST_REF_TEI_EMBED_BASE_URL=http://127.0.0.1:8080`
  - [ ] `export RUST_REF_TEI_RERANK_BASE_URL=http://127.0.0.1:8081`
  - [ ] `export RUST_REF_EMBED_MODEL_ID=Qwen/Qwen3-Embedding-4B`
  - [ ] `export RUST_REF_RERANK_MODEL_ID=BAAI/bge-reranker-v2-m3`
  - [ ] `export RUST_REF_LOCAL_BACKEND_ENGINE=python`
  - [ ] `export RUST_REF_SEMANTIC_BACKEND_PROFILE=python-local`
  - [ ] `export RUST_REF_SEMANTIC_MODEL_CACHE_DIR=.cache/sqlite_kb/models/hf`
  - [ ] `export RUST_REF_SEMANTIC_TIMEOUT_SEC=60`
  - [ ] `export RUST_REF_ALLOW_DEGRADED=0`
- [x] Validate local toolchain.
  - [x] `uv --version`
  - [x] `sqlite3 --version`
  - [x] `uv run python --version`
- [x] Run semantic backend preflight (must pass for semantic/hybrid).
  - [x] Add and run `uv run python scripts/sqlite_check_semantic_backend.py --embed-base-url "$RUST_REF_TEI_EMBED_BASE_URL" --rerank-base-url "$RUST_REF_TEI_RERANK_BASE_URL" --embed-model "$RUST_REF_EMBED_MODEL_ID" --rerank-model "$RUST_REF_RERANK_MODEL_ID"`.
  - [x] If preflight fails, semantic/hybrid tests must fail (unless explicit degraded local run).

## Hard Constraints (Do Not Regress)

- [x] Do not gate retrieval correctness on "top mechanism family" expectations.
- [ ] Do not pre-bias ranking by forcing category mappings into DB-first ranking logic.
  - [x] Resolved: `statement_corpus_v2` removed from active contract path (full-corpus `statement_corpus_v3_all` only).
- [x] Do not keep compatibility shims for legacy heuristic retrieval when no consumers depend on them.
- [x] Do not label heuristic/token-overlap ranking as semantic retrieval.
- [x] Keep existing read-only guardrails for SQL execution.
- [x] Keep deterministic logging and snapshot metadata for auditability.

## Scope Boundaries

- [ ] In scope:
  - [ ] Statement-first retrieval over Rust Reference corpus.
  - [ ] Optional row scoping/filtering and row aggregation from retrieved evidence.
  - [ ] Real embedding + reranker backend integration.
- [ ] Out of scope for this rebuild:
  - [ ] Rewriting ISO extraction source pipeline outside Table 1 touchpoints.
  - [ ] Expanding mechanism taxonomy as a retrieval dependency.

## Legacy Cleanup Strategy (Immediate Hard Cutover)

- [ ] Perform a direct cutover, not a staged compatibility bridge.
  - [ ] Archive one baseline report bundle for before/after comparison.
  - [ ] Remove legacy heuristic retrieval and family-first ranking code paths.
  - [x] Remove legacy query contracts and suites that encode top-family assertions.
  - [x] Remove verifier branches tied to `allowed_top_families` and similar brittle logic.
  - [x] Update docs/scripts to advertise only v2 lexical/semantic/hybrid retrieval.
- [ ] Keep only minimal archival artifacts.
  - [ ] Preserve one timestamped legacy report snapshot for audit history.
  - [ ] Do not run legacy suites in CI after cutover.

## File-Level Cutover Map (What To Delete/Replace)

- [ ] Remove legacy ranking logic from `scripts/sqlite_build_rust_reference.py`.
  - [ ] Delete row-family-first semantic scoring and top-family tie-break dependence.
  - [ ] Keep only traceability projections needed for row linkage.
- [x] Replace legacy contracts in `config/sqlite_query_contracts/rust_reference.yaml`.
  - [x] Remove fixed-term lexical query requirements (`term_a/term_b/term_c`) from active path.
  - [x] Remove semantic substring-boost patterns that are not real semantic retrieval.
  - [x] Add v2 lexical candidate query contracts for FTS-backed retrieval.
- [x] Replace/remove legacy verifier and query suites.
  - [x] Remove family-top checks and `allowed_top_families` logic from `scripts/sqlite_verify_rust_reference_query_set.py`.
  - [x] Retire legacy query suites under `data/query_testsets/` tied to family-top pass/fail.
  - [x] Add retrieval eval suite and evaluator script as canonical quality gate path.
- [x] Replace unit tests tied to legacy assumptions.
  - [x] Remove tests that assert family-top behavior as semantic correctness.
  - [x] Add lexical/semantic/hybrid retrieval quality tests with judged prompts.

## Phase 0 - Baseline and Regression Snapshot

- [ ] Freeze baseline behavior before changes.
  - [ ] Capture current lexical and semantic query outputs for a fixed prompt set.
  - [ ] Save baseline reports under `.cache/sqlite_kb/reports/rust_reference/` with timestamp.
- [ ] Capture current failure modes explicitly.
  - [ ] Document noisy hits for defensive-programming prompt.
  - [ ] Document row `1i` overlong/noisy requirement text impact.

## Phase 1 - Retrieval Architecture Reset (Statement-First)

- [ ] Separate retrieval artifacts from traceability artifacts.
  - [ ] Keep `table1_rows`, `row_verdicts`, `row_mechanisms` as traceability outputs only.
  - [ ] Define statement-level retrieval as primary path for search quality.
- [x] Define retrieval data model.
  - [x] Lexical index source: normalized statement text + section heading + anchor context.
  - [x] Semantic index source: statement embeddings with model/version provenance.
  - [x] Rerank input: top-N lexical/semantic candidate statements.
- [ ] Add row linkage as projection, not rank prior.
  - [ ] Maintain mapping `statement -> section -> row relevance signals`.
  - [ ] Compute row relevance from retrieved evidence after retrieval.
- [x] Define schema migration and version bump plan.
  - [x] Add new retrieval artifacts with `PRAGMA user_version` bump (v3 -> v4).
  - [x] Migrations must be idempotent and safe to rerun.
  - [ ] Backfill embeddings/indexes atomically; no partial semantic state on failure.

## Phase 2 - Lexical Retrieval Implementation

- [ ] Add FTS5-backed lexical search for statements.
  - [x] Create FTS virtual table over statement corpus fields.
  - [x] Use BM25 ranking + deterministic tie-break (`statement_id ASC`).
  - [ ] Add snippet/highlight support for returned evidence.
  - [x] Add explicit index rebuild command and verification query.
- [x] Add lexical query contract(s).
  - [x] Free-text lexical query (`query_text`) instead of fixed `term_a/term_b/term_c` only.
  - [x] Optional row filter (`row_marker`/`row_node_id`) and top-k controls.
  - [x] Add lexical explainability fields (`token_overlap_count`, `phrase_match`, `bm25_raw`).
- [x] Remove legacy fixed-term lexical query path.
  - [x] Delete `term_a/term_b/term_c`-style contract usage from active verification flow.

## Phase 3 - Real Semantic Retrieval + Reranker

- [x] Implement pluggable semantic backend (real models, not token overlap heuristics).
  - [x] Embed query and statement corpus with configured embedding model (`Qwen/Qwen3-Embedding-4B` primary).
  - [x] Retrieve nearest statements by vector similarity.
  - [x] Rerank top candidates with configured reranker model (`BAAI/bge-reranker-v2-m3`).
- [x] Persist semantic artifacts with provenance.
  - [x] Store per-statement embeddings and model metadata/version.
  - [ ] Ensure rebuild invalidates/recomputes embeddings on source or model change.
- [x] Provide runtime configuration.
  - [x] Backend mode: `tei-http` (primary) plus explicit offline/test fallback.
  - [x] Timeouts, batch size, and cache controls.
  - [x] Fail loudly if semantic backend unavailable in semantic-only mode.
  - [ ] Add embedder bakeoff checkpoint before signoff.
  - [ ] Compare `Qwen/Qwen3-Embedding-4B` vs `BAAI/bge-m3` on the retrieval gold set.
  - [ ] Select default by semantic quality first, latency/cost second.

## Failure Policy (Backend/Model Outage Handling)

- [x] Enforce explicit fail-loud semantics.
  - [x] If `--mode semantic` and backend/model preflight fails: return `SEMANTIC_BACKEND_UNAVAILABLE` and non-zero exit.
  - [x] If `--mode hybrid` and backend/model preflight fails: return `HYBRID_BACKEND_UNAVAILABLE` and non-zero exit.
  - [x] If `--mode lexical`: continue normally regardless of semantic backend status.
- [x] Allow explicit degraded local runs only.
  - [x] Require `--allow-degraded` or `RUST_REF_ALLOW_DEGRADED=1`.
  - [x] Output must include `requested_mode`, `executed_mode`, `degraded=true`, and degradation reason.
  - [x] Degraded mode is disallowed in blocking CI jobs.
- [x] Add bounded retry policy for transient backend failures.
  - [x] Retry at most 2 times with short backoff before fail-loud exit.
  - [x] Log retry count and final failure reason in report artifacts.

## Phase 4 - Hybrid Fusion and Row-Aware Outputs

- [x] Implement hybrid fusion from lexical + semantic candidate sets.
  - [x] Merge candidates, rerank, and expose score breakdown per result.
  - [ ] Use explicit weighted fusion config with versioned defaults (tuned on eval set).
  - [x] Keep deterministic ordering with explicit tie-breaks.
- [x] Add row relevance projection.
  - [x] Aggregate statement evidence to row-level scores after retrieval.
  - [x] Return both statement results and row summary for Part 6 Table 1 usage.
- [x] Expose user-facing modes in query CLI.
  - [x] `--mode lexical|semantic|hybrid`
  - [x] `--query-text "..."`
  - [x] optional `--row-marker`, `--top-k`, `--include-score-breakdown`.

## Phase 5 - Query Contract and Script Changes

- [x] Update `config/sqlite_query_contracts/rust_reference.yaml` for retrieval-aligned lexical SQL.
- [x] Add/adjust scripts:
  - [x] `scripts/sqlite_query_rust_reference.py` for interactive search modes.
  - [x] New evaluator script for retrieval quality (`scripts/sqlite_eval_rust_reference_retrieval.py`).
  - [x] New backend preflight script (`scripts/sqlite_check_semantic_backend.py`).
  - [x] Build/migrate scripts to create and maintain FTS + embedding artifacts.
- [x] Keep SQL guardrails intact (`scripts/sqlite_query_guardrails.py`).
- [x] Remove legacy verification/query-set machinery replaced by retrieval evaluation.
  - [x] Delete or retire legacy query-set definitions under `data/query_testsets/` that encode family-top pass/fail.
  - [x] Remove `allowed_top_families` handling from verification scripts.

## Phase 6 - Real Tests (No Nonsense)

- [x] Add a curated retrieval gold set with real prompts and judgments.
  - [x] New file: `data/query_testsets/rust_reference_table1_retrieval_eval.yaml`.
  - [x] Include lexical and semantic prompts per row intent (not just keyword variants).
  - [x] Include expected relevant anchors/statement IDs and non-relevant traps.
  - [x] Lock schema for each eval prompt record:
    - [x] `prompt_id`, `slice`, `query_text`, `modes`.
    - [x] `expected_row_markers` (ordered by priority).
    - [x] `relevant_statement_ids` and/or `relevant_anchor_prefixes`.
    - [x] `hard_negative_statement_ids` (must not appear in top-k).
    - [x] Optional per-prompt minimum metrics overrides.
- [x] Split eval prompts into two mandatory intent slices.
  - [x] `issue_identification`: prompts that ask what can go wrong or what risks exist.
  - [x] `resolution_identification`: prompts that ask how to mitigate/control/address those risks.
  - [x] Each prompt entry includes expected row markers and accepted evidence anchors.
- [x] Lexical tests that verify actual lexical behavior.
  - [x] Assert top-k contains evidence with strong token overlap for targeted keywords.
  - [x] Assert unrelated lexical prompts do not rank target-row evidence highly.
  - [x] Assert deterministic ranking and stable tie-break behavior.
- [ ] Semantic tests that verify actual semantic behavior.
  - [ ] Use paraphrase prompts with low literal overlap.
  - [ ] Assert top-k still surfaces judged-relevant anchors/statements.
  - [ ] Assert semantic mode outperforms lexical mode on paraphrase subset.
- [ ] Hybrid tests.
  - [ ] Assert hybrid >= best(single mode) on judged prompt set for MRR/nDCG.
  - [ ] Assert score breakdown fields are present and consistent.
- [ ] Intent-quality tests (issue/resolution correctness).
  - [ ] Issue prompts must surface risk/problem statements aligned to expected Table 1 row intent.
  - [ ] Resolution prompts must surface mitigation/control statements aligned to expected Table 1 row intent.
  - [ ] Add issue->resolution consistency check per scenario (same row intent family of evidence).
- [x] Unit and integration split.
  - [x] Unit: normalization, fusion math, candidate merge, tie-break determinism.
  - [x] Integration: end-to-end retrieval on fixture DB with real query prompts.
  - [x] Integration: backend preflight and fail-loud policy tests.

## Phase 7 - Quality Gates and CI Adoption

- [x] Replace brittle family-top assertions with retrieval-quality gates.
  - [x] Gate metrics: Precision@k, MRR, nDCG, anchor hit-rate.
  - [x] Separate lexical and semantic thresholds.
  - [x] Keep threshold deltas explicit and versioned.
- [x] Set initial numeric thresholds (update only by PR with evidence).
  - [x] Lexical overall: `Precision@5 >= 0.55`, `MRR@10 >= 0.65`, `row_hit_rate@5 >= 0.80`.
  - [x] Semantic paraphrase slice: `Recall@10 >= 0.75`, `MRR@10 >= 0.60`, `row_hit_rate@5 >= 0.75`.
  - [x] Semantic-vs-lexical requirement on paraphrase slice: `MRR_semantic >= MRR_lexical + 0.05`.
  - [x] Hybrid overall: `Precision@5 >= 0.65`, `nDCG@10 >= 0.72`, `MRR@10 >= best_single_mode - 0.01`.
- [x] Add slice-level gating to prevent metric hiding.
  - [x] Gate issue-identification and resolution-identification slices independently.
  - [x] Require semantic mode to beat lexical mode on paraphrase-heavy semantic slice.
  - [x] Require hybrid mode to meet or exceed best single mode on overall judged set.
- [x] Remove legacy row-mechanism/family-top suites from CI immediately after v2 gates are in place.
- [x] Publish report artifact with per-prompt failures and top-k evidence traces.

## Query/Response Review Artifacts (Manual Quality Review)

- [x] Persist ad-hoc query inputs and full retrieval outputs for manual review.
  - [x] Add query CLI flags to save outputs per run (for example: `--save-response-path` / `--save-response-dir`).
  - [x] Default review artifact location: `.cache/sqlite_kb/reports/rust_reference/query_reviews/`.
  - [x] Save full response payload (`rows`, `row_projection`, score breakdown, mode/degraded metadata), not just top IDs.
  - [x] Include reproducibility metadata (`query_text`, `row_marker`, `top_k`, `candidate_limit`, backend profile, model IDs, db path, timestamp).
- [x] Add a batch review runner for row-by-row analysis sessions.
  - [x] Accept a small YAML/JSON list of prompts (for example 5-query or per-row packs).
  - [x] Run requested modes and emit a bundle (`manifest.json` + one response file per query/mode).
  - [x] Use deterministic filenames (`<timestamp>__<prompt_id>__<mode>.json`) for easy diff/review.
- [x] Add docs for a "5 representative queries" quality review workflow.
  - [x] Document one command to generate a review bundle.
  - [x] Document quick inspection commands (`jq`) to compare query text to returned evidence.
  - [x] Make clear that row projection is secondary to reviewing whether evidence actually answers the prompt.
- [ ] Add tests for artifact generation and schema stability.
  - [x] Unit test artifact writer path creation and required response metadata keys.
  - [ ] Integration test 1 lexical + 1 hybrid query artifact end-to-end on fixture DB.
  - [x] Guard against silent no-op (fail if review mode requested but no files written).

## CI Topology (Fast PR vs Full Retrieval)

- [x] Define explicit CI lanes.
  - [x] `ci-pr-fast` (blocking): unit tests, lexical retrieval integration, schema/migration checks.
  - [x] `ci-pr-semantic` (blocking when retrieval code/eval changes): local TEI-backed semantic + hybrid eval subset.
  - [x] `ci-nightly-full` (blocking nightly): full lexical/semantic/hybrid eval across full judged set.
- [x] Enforce failure policy in CI.
  - [x] If semantic/hybrid lane is scheduled and backend is unavailable, job fails hard.
  - [x] Degraded mode is disabled in all CI lanes.

## Determinism and Performance Budgets

- [ ] Determinism requirements.
  - [x] Lexical ties break by `statement_id ASC`.
  - [x] Semantic/hybrid ties break by `reranker_score DESC`, then `statement_id ASC`.
  - [ ] Repeated runs on unchanged DB + models produce identical top-k ordering.
- [ ] Latency budgets on local baseline hardware (warm cache, `top_k=20`).
  - [ ] Lexical p95 <= 150 ms.
  - [ ] Semantic p95 <= 1500 ms.
  - [ ] Hybrid p95 <= 1800 ms.
  - [ ] If budgets fail, capture profile report before tuning thresholds.

## First PR Scope (Minimum Vertical Slice)

- [x] Land one end-to-end vertical slice before broader expansion.
  - [x] Remove legacy family-top semantic gating.
  - [x] Add v2 lexical FTS query path + CLI mode switch.
  - [x] Add semantic backend preflight + fail-loud error codes.
  - [x] Add retrieval eval schema file with at least 20 judged prompts (issue/resolution split).
  - [x] Add CI wiring for `ci-pr-fast` and initial `ci-pr-semantic` subset.

## Definition of Done

- [ ] Query "What kinds of defensive programming is available in Rust?" returns defensively relevant evidence near top in semantic and hybrid modes.
- [ ] Lexical mode returns high-overlap, grounded evidence for keyword-style queries.
- [ ] Semantic mode handles paraphrases without requiring exact substring matches.
- [ ] Issue-identification prompts return relevant risk/problem evidence for expected Table 1 intents.
- [ ] Resolution-identification prompts return relevant mitigation/control evidence for expected Table 1 intents.
- [x] No production/blocking gate depends on forced mechanism-family top-rank checks.
- [x] Legacy heuristic/family-top verification paths are removed from active CI and query workflow.
- [x] Test suite includes meaningful lexical + semantic retrieval evaluations and fails on real quality regressions.

## Implementation Sequence

- [ ] Step 1: Archive baseline report bundle, then remove legacy heuristic and family-top verification paths.
- [x] Step 2: Implement FTS5 lexical path and v2 query CLI surface.
- [x] Step 3: Implement semantic backend integration and embedding storage.
- [x] Step 4: Implement hybrid fusion and row projection.
- [x] Step 5: Implement evaluator and real lexical/semantic/hybrid tests (issue + resolution slices).
- [ ] Step 6: Switch CI gates to v2 retrieval metrics and delete remaining legacy suite wiring.
