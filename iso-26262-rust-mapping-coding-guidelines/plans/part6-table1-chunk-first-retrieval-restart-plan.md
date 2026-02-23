# Part 6 Table 1 Retrieval Restart Plan (Rip-and-Replace)

This plan replaces the statement-first pipeline with a chunk-first architecture using stable identities and deterministic provenance.

Execution mode is rip-and-replace:

- No legacy dual-run gating window.
- No legacy-control freeze/copy/compare as a gating requirement.
- Legacy artifacts are historical reference only.

## Delivery and Commit Cadence (Required)

- [ ] Execute steps strictly in order (`0` through `10`).
- [ ] Do not start the next step until the current step has:
  - [ ] code/config changes landed,
  - [ ] tests/checks run,
  - [ ] plan checkbox updates committed.
- [ ] Commit at step boundaries.
  - [ ] One step-completion commit per step (no batching multiple steps in one commit).
  - [ ] Use Conventional Commits.
  - [ ] Commit message includes the step number.
- [ ] Record step completion evidence in commit body.
  - [ ] key commands run,
  - [ ] artifact/report paths,
  - [ ] explicit blockers if step is partial.

## 0) Lock Invariants First (do this before coding)

- [ ] Pinned source revision is mandatory.
  - [ ] `--reference-revision` is required in production build paths.
  - [ ] Build fails if revision is missing, unresolved, or ambiguous.
- [ ] Retrieval unit is chunk, not sentence statement.
- [ ] IDs are content-addressed and stable unless content changes.
- [ ] Store dual text forms: `raw_text` for citation, `clean_text` for retrieval/indexing.
- [ ] Row projection is post-retrieval annotation only, with explicit abstain.
- [ ] Active runtime DB path is fixed to `.cache/sqlite_kb/current/rust_reference.sqlite`.
  - [ ] Restart run directories are artifacts-only and must not be used as active `--db-path`.
  - [ ] Existing canonical DBs with `user_version < 6` or no `chunks` table are stale and must be rebuilt before materialization/eval/review.

## 1) Redesign Data Model First

- [ ] Add core provenance and chunk tables.
  - [ ] `kb_metadata(kb_id, source_name, source_revision, extractor_version, built_at, notes)`.
  - [ ] `docs(doc_uid, source_path, title, revision, fetched_at, ...)`.
  - [ ] `sections(section_uid, doc_uid, anchor, heading, order, ...)`.
  - [ ] `chunks(chunk_uid, section_uid, raw_text, clean_text, char_len, token_len, ...)`.
  - [ ] `chunk_spans(chunk_uid, source_anchor, start_offset, end_offset, span_order)`.
- [ ] Add indexing tables.
  - [ ] `chunk_embeddings(chunk_uid, model_id, embed_version, vector_blob, fingerprint)`.
  - [ ] `chunks_fts` over `clean_text` with heading/title boosts.
- [ ] Define `chunk_uid` as a content-addressed hash of deterministic inputs.

## 2) Rebuild Ingestion As Deterministic Pipeline

- [ ] Fetch pinned Rust Reference revision only.
- [ ] Parse structure deterministically: doc -> section -> block.
- [ ] Build deterministic `clean_text` normalization (versioned).
  - [ ] Remove markup/noise artifacts.
  - [ ] Normalize whitespace and list formatting.
- [ ] Preserve `raw_text` and source anchor lineage for citation.
- [ ] Remove hidden caps/truncation behavior.

## 3) Implement Concept-Sized Chunking

- [ ] Chunk by paragraph/list block/short contiguous paragraph groups.
- [ ] Target chunk size around 150-500 tokens.
- [ ] Never merge across section boundaries.
- [ ] Split oversized blocks/lists into coherent subchunks.
- [ ] Keep deterministic anchor/span mapping for every chunk.

## 4) Build Fresh Indexes On Chunk Units

- [ ] Compute embeddings from `clean_text` for chunk corpus.
- [ ] Persist embeddings keyed by `(chunk_uid, model_id, embed_version)`.
- [ ] Build lexical FTS index over chunk `clean_text` with heading/title boosts.
- [ ] Record explicit model provenance metadata (id/revision/license/provider).
- [ ] Materialize on the canonical active DB immediately after rebuild, and gate eval/review on zero missing chunk embeddings.

## 5) Rebuild Retrieval With Interpretable Scores

- [ ] Implement retrieval flow:
  - [ ] Optional deterministic query rewrite (logged).
  - [ ] Lexical top-M + semantic top-N candidate generation.
  - [ ] Union + dedupe by `chunk_uid`.
  - [ ] Rerank top-K.
- [ ] Return one ranking score and stable components:
  - [ ] `final_score`
  - [ ] `lexical_score`
  - [ ] `semantic_score`
  - [ ] `reranker_score`
- [ ] Ensure deterministic ordering/tie-break chain.
- [ ] Enforce: row labels do not affect ranking.

## 6) Rebuild Table 1 Row Metadata Hygiene

- [ ] Store clean per-row structured inputs (`1a`..`1i`).
  - [ ] `requirement_text_clean`
  - [ ] separate `footnotes[]`
  - [ ] curated `row_profile_terms[]` with Rust-native expansions
- [ ] Add validation gates.
  - [ ] marker completeness/uniqueness
  - [ ] length/token sanity checks
  - [ ] malformed/contaminated text fails build

## 7) Rebuild Row Projection As Abstaining Classifier

- [ ] Classify retrieved chunks to row labels (multi-label), not query text.
- [ ] Combine multiple signals.
  - [ ] profile semantic similarity
  - [ ] lexical term hits
  - [ ] optional section priors
- [ ] Calibrate thresholds per row.
- [ ] Support explicit abstain with reason codes.
- [ ] Emit evidence trace for mapped decisions.

## 8) Rebuild ISO<->Rust Rewrite As Config + Logging

- [ ] Keep rewrite rules deterministic and versioned.
- [ ] Log original query, rewritten query, and added terms.
- [ ] Support no-rewrite A/B mode.
- [ ] Add tests for rewrite drift and destructive rewrites.

## 9) Rebuild Evaluation Early (with skew alarms)

- [ ] Build eval sets for chunk-level relevance and row-projection labels.
- [ ] Include negatives and abstain-expected prompts.
- [ ] Report retrieval metrics: Precision@k, MRR@k, nDCG@k, anchor hit rates.
- [ ] Report projection metrics: macro F1, abstain precision/recall/rate.
- [ ] Add skew alarms.
  - [ ] max-row share
  - [ ] row entropy/Gini
  - [ ] abstain-rate collapse alerts
- [ ] Emit pinned build/provenance metadata in every report artifact.

## 10) Add UX and Operational Features Last

- [ ] Add context-window helpers (neighbor chunks/section context).
- [ ] Improve citation formatting ergonomics.
- [ ] Add CLI profiles for manual vs eval workflows.
- [ ] Add caching and runtime ergonomics after correctness is stable.

## File-Level Implementation Targets

- [ ] `scripts/sqlite_build_rust_reference.py`
  - [ ] deterministic pinning enforcement
  - [ ] chunk-native schema + ingestion + chunking
- [ ] `scripts/sqlite_migrate_rust_reference_schema.py`
  - [ ] additive migration for chunk-native artifacts
- [ ] `config/sqlite_query_contracts/rust_reference_chunk.yaml`
  - [ ] chunk corpus + lexical chunk query IDs
- [ ] `scripts/sqlite_materialize_rust_reference_embeddings.py`
  - [ ] chunk embedding materialization and completeness checks
- [ ] `scripts/sqlite_query_rust_reference.py`
  - [ ] chunk retrieval and abstaining row projection
- [ ] `scripts/sqlite_eval_rust_reference_retrieval.py`
  - [ ] chunk-level retrieval + projection + skew metrics
- [ ] `data/query_testsets/rust_reference_table1_retrieval_eval.yaml`
  - [ ] chunk-era prompt and label coverage
- [ ] Tests
  - [ ] `tests/unit/sqlite_kb/test_query_rust_reference.py`
  - [ ] `tests/unit/sqlite_kb/test_smoke_rust_reference.py`
  - [ ] `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Non-Goals

- [ ] No long-term `statement_id` compatibility map.
- [ ] No row-label-driven ranking logic.
- [ ] No silent semantic/hybrid degradation in quality-gated runs.

## Trade-off (Accepted)

- [ ] Direct A/B comparability with old statement-id corpora is not required for this restart.

## Phased Commit Sequence (Required)

- [ ] Step `0` complete -> `chore(restart): lock invariants and pinning policy (step 0)`
- [ ] Step `1` complete -> `feat(schema): add chunk-first core data model (step 1)`
- [ ] Step `2` complete -> `feat(ingest): make ingestion deterministic and pinned (step 2)`
- [ ] Step `3` complete -> `feat(chunking): add concept-sized deterministic chunks (step 3)`
- [ ] Step `4` complete -> `feat(index): add chunk embeddings and lexical index (step 4)`
- [ ] Step `5` complete -> `feat(retrieval): implement chunk retrieval scoring pipeline (step 5)`
- [ ] Step `6` complete -> `feat(table1): rebuild structured row metadata hygiene (step 6)`
- [ ] Step `7` complete -> `feat(projection): add abstaining row classifier (step 7)`
- [ ] Step `8` complete -> `feat(rewrite): add deterministic ISO-Rust rewrite logging (step 8)`
- [ ] Step `9` complete -> `feat(eval): add chunk-era evaluation and skew alarms (step 9)`
- [ ] Step `10` complete -> `feat(ux): finalize operational and UX hardening (step 10)`

Use these as templates; scope words can be adjusted, but step numbers are mandatory.

## Definition of Done

- [ ] Chunk-first retrieval is the only active production/eval/CI path.
- [ ] IDs and provenance are deterministic and audit-ready.
- [ ] Row projection is calibrated, abstaining, and distribution-stable.
- [ ] Query rewrite is deterministic, logged, and test-covered.
- [ ] Legacy statement-first path is retired from active flows.
