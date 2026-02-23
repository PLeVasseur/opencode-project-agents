# ISO 26262 Part 6 Table 1 Retrieval Review Package

## What this package is for

This package is a handoff bundle for manual quality review of retrieval behavior.

Goal: validate whether query results make practical sense for ISO 26262 Part 6,
Table 1 style prompts (not just whether row projection labels look good).

## What was done

1. Rebuilt retrieval to be statement-first and full-corpus (no mechanism-gated
   corpus membership).
2. Ran local semantic backend in python-local mode with:
   - embed model: `Qwen/Qwen3-Embedding-4B`
   - reranker model: `BAAI/bge-reranker-v2-m3`
3. Materialized embeddings for the full statement corpus:
   - total statements: `2896`
   - cached embeddings for active model: `2896`
4. Captured 5 representative query runs in `hybrid` mode (non-degraded) from
   the prompt set.
5. Saved full response payloads (query + runtime metadata + full rows + row
   projection + score fields) into JSON files for inspection.

## Source prompt pack and capture command

Prompt pack:

- `data/query_testsets/rust_reference_table1_retrieval_eval.yaml`

Capture command used:

```bash
uv run python scripts/sqlite_capture_rust_reference_query_reviews.py \
  --prompts-path data/query_testsets/rust_reference_table1_retrieval_eval.yaml \
  --prompt-ids RET-RESOLVE-001,RET-RESOLVE-002,RET-RESOLVE-003,RET-RESOLVE-004,RET-RESOLVE-005 \
  --modes hybrid \
  --bundle-id five-query-hybrid-20260222 \
  --top-k 8 \
  --candidate-limit 200 \
  --semantic-embed-base-url http://127.0.0.1:19080 \
  --semantic-rerank-base-url http://127.0.0.1:19081 \
  --embed-model-id Qwen/Qwen3-Embedding-4B \
  --reranker-model-id BAAI/bge-reranker-v2-m3 \
  --semantic-timeout-sec 120 \
  --semantic-retries 0
```

## What is in this folder

- `manifest.json`: machine-readable index of captured query artifacts.
- `FIVE_QUERIES_AND_OUTPUTS.md`: human-readable summary of the 5 prompts and
  top returned evidence.
- `query_outputs/*.json`: full raw retrieval outputs for each query.

## How to review quickly

From this folder:

```bash
jq '.summary' manifest.json
jq -r '.entries[] | [.prompt_id,.mode,.status,.artifact_path] | @tsv' manifest.json
```

Inspect one query deeply:

```bash
FILE="query_outputs/20260222T001709Z__ret-resolve-001__hybrid.json"
jq '{query, runtime}' "$FILE"
jq '.response.rows[:5] | map({statement_id, source_anchor, relevance_score, text_preview: .statement_text[0:280]})' "$FILE"
```

Important: treat row projection as secondary. Primary review criterion is
whether returned evidence actually answers the prompt.
