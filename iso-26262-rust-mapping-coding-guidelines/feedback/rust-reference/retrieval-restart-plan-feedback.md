# Retrieval Restart Plan (Rip-and-Replace)

If we’re willing to throw the current pipeline away and restart, the cleanest path is to rebuild around **stable identities + concept-sized chunks**, and treat **ISO 26262 Part 6 Table 1 mapping** as a **post-retrieval annotation layer** (never a ranking gate).

Below is a step-by-step restart plan based on what we know about the current system (statement-id keyed embeddings, sentence-derived positional IDs, occasional upstream drift unless pinned).

---

## 0) Lock in the invariants (so we don’t rebuild twice)

Decide these up front:

- **Pinned source revision is mandatory** (`--reference-revision` required; no default remote HEAD).
- Retrieval unit is **chunk**, not “sentence statement.”
- IDs are **content-addressed** (stable across rebuilds unless the content changes).
- Store **raw_text** for citation and **clean_text** for embedding/rerank.
- Row projection is **post-retrieval annotation** with **abstain** baked in.

This eliminates most current failure modes: positional-ID drift, sentence caps, embed-text mismatch, and row-label skew poisoning results.

---

## 1) Redesign the data model first

Build a schema where rebuilds are safe and comparable.

### Core tables (minimum)

- `kb_metadata(kb_id, source_name, source_revision, extractor_version, built_at, notes)`
- `docs(doc_uid, source_path, title, revision, fetched_at, …)`
- `sections(section_uid, doc_uid, anchor, heading, order, …)`
- `chunks(chunk_uid, section_uid, raw_text, clean_text, char_len, token_len, …)`
- `chunk_spans(chunk_uid, source_anchor, start_offset, end_offset)`  
  (or enough info to cite precisely and deterministically)

### Embeddings and lexical index

- `chunk_embeddings(chunk_uid, model_id, embed_version, vector_blob, fingerprint)`
- `chunks_fts` (SQLite FTS5 over `clean_text` + boosted title/heading fields)

**Key point:** `chunk_uid` should be **content-addressed**, e.g. a hash of `(doc_uid + anchor + normalized clean_text)`.

You can still generate sentence-level “statement IDs” later *as a view*, but don’t key embeddings to them.

---

## 2) Rebuild ingestion as a deterministic pipeline

Replace “regex sentence split + cap/drop” with a structured parse that preserves spec intent.

### Ingestion steps

1. **Fetch pinned Rust Reference revision** (fail fast if not pinned).
2. **Parse to structure**: doc → section → paragraph/list/code/admonition blocks.
3. Generate **clean_text**:
   - remove markup noise (`[!NOTE]`, footnote markers, `r[...]` artifacts)
   - normalize whitespace/bullets
4. Preserve **raw_text** and anchors for citation.

Rule: parsing must be **deterministic**, **versioned**, and have **no hidden caps**.

---

## 3) Define a chunking policy that matches how humans cite specs

Stop treating “sentence = unit.” Use concept-sized chunks.

### Default chunking behavior

- chunk by **paragraph / list block / short contiguous set of paragraphs**
- target size window: **~150–500 tokens** (tune for your models)
- never merge across section boundaries
- split huge lists into coherent subchunks (don’t embed a 2,000-token mega-bullet block)

Always keep a map to the original anchor(s) so you can cite precisely.

---

## 4) Build indexes (fresh) on the new chunk units

With stable `chunk_uid`:

1. Compute embeddings for `clean_text`
2. Store in `chunk_embeddings(chunk_uid, model_id, embed_version, …)`
3. Build FTS index over `clean_text` + heading/title boosts

This yields a robust hybrid retrieval system without positional-id fragility.

---

## 5) Re-implement retrieval with explicit, interpretable scoring

Define **one final score** that drives rank, and keep component scores consistent.

### Retrieval flow

1. Optional **query rewrite** (logged and inspectable)
2. Get candidates from:
   - semantic top-N (vector search)
   - lexical top-M (FTS/BM25-ish)
3. Union + dedupe
4. Rerank top-K with cross-encoder (or chosen reranker)
5. Return top results with:
   - `final_score`
   - component scores (semantic/lexical/reranker) with fixed definitions
   - provenance (doc/section/anchor/revision)

**No ISO row labels participate in ranking.** (Row projection happens later.)

---

## 6) Rebuild Table 1 row metadata as clean structured inputs

Treat ISO Table 1 as its own “spec source” with hygiene.

Store per row:

- `row_id` (1a..1i)
- `requirement_text_clean`
- `footnotes[]` stored separately
- `row_profile_terms[]` (curated synonyms + Rust-native expansions)
- optional examples/counterexamples

Do **not** build row profiles from one giant raw table-text blob.

---

## 7) Rebuild row projection as a calibrated, abstaining classifier

Operate on **returned evidence chunks**, not queries.

### Reliable approach

- multi-label classifier: `chunk → {row labels}`
- multi-signal scoring:
  - embedding similarity to row profiles (normalized)
  - lexical hits against curated row terms
  - optional section priors
- calibrate thresholds **per row**
- explicitly support **abstain** (“none apply”)

### Dataset guidance (restart-style)

Label **chunks**, not prompts:

- sample chunks from diverse retrieval runs
- label each chunk with 0..n applicable rows
- include lots of negatives

This directly answers: “does this evidence support row X?”

---

## 8) Rebuild ISO↔Rust rewrite as config + logging (not magic)

Make rewriting deterministic and testable:

- per-row term maps
- strategy tags (“expanded with Rust-native vocabulary”, “synonym expansion”, etc.)
- always log original + rewritten query and what terms were added

This prevents silent intent drift and makes A/B comparisons easy.

---

## 9) Rebuild evaluation from day one (with skew alarms)

The prior system’s failure mode was “one row dominates everything.” Add detectors that scream early.

### Minimum eval suite

- “golden query pack” with expected evidence anchors (human-reviewed)
- row-projection labeled set (chunk labels)
- skew detectors:
  - max-row share threshold
  - entropy/Gini of row distribution
  - abstain rate per row

Every run emits a report artifact including pinned build metadata.

---

## 10) Only then add UX features

After retrieval + row projection are credible:

- context windows (neighbor chunks/heading)
- nicer citation formatting
- CLI profiles (manual vs eval)
- caching and other ergonomics

In a chunk-based architecture, context windows are cheap and don’t require re-embedding.

---

## What this restart buys you

- No more “IDs shift because parsing changed.”
- Embedding cache correctness becomes obvious (fingerprints/versioned models).
- Chunking matches how spec text is written and cited.
- Row projection becomes measurable, calibratable, and allowed to abstain.
- ISO terminology mismatch is handled explicitly (row profiles + query rewrite).

## The trade-off

You lose direct A/B comparability with the old `statement_id`-based corpus unless you build a migration map (e.g., old statement → new chunk via anchor+text similarity). Only do that if you truly need continuity.

---

### Minimal viable restart scope

If you want a bounded rip-and-replace, ship **Steps 1–5 + 6–7** first:
- new ingestion + chunking + indexing + retrieval
- clean row metadata + abstaining row projection

Everything else is incremental on top.
