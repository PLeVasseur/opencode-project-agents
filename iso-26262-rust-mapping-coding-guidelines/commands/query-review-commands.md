# Query Review Commands (Manual Inspection)

Use these commands from the repo root:

`/home/pete.levasseur/personal/iso-26262-rust-mapping-coding-guidelines`

## 1) Pick a review bundle

Latest bundle:

```bash
BUNDLE="$(ls -1dt .cache/sqlite_kb/reports/rust_reference/query_reviews/* | head -n 1)"
echo "$BUNDLE"
```

Or use the known bundle from the recent 5-query run:

```bash
BUNDLE=".cache/sqlite_kb/reports/rust_reference/query_reviews/five-query-hybrid-20260222"
```

## 2) Quick status view

```bash
jq '.summary' "$BUNDLE/manifest.json"
```

```bash
jq -r '.entries[] | [.prompt_id, .mode, .status, .artifact_path] | @tsv' "$BUNDLE/manifest.json"
```

## 3) Show prompt + top evidence for all files

```bash
for f in "$BUNDLE"/*__hybrid.json; do
  echo "\n=== $(basename "$f") ==="
  jq -r '.query.query_text' "$f"
  jq -r '.response.rows[:3][] | "- \(.statement_id)\n  \(.source_anchor)"' "$f"
done
```

## 4) Deep-inspect one query file

Pick file:

```bash
FILE="$BUNDLE/20260222T001709Z__ret-resolve-001__hybrid.json"
```

Show query and runtime details:

```bash
jq '{query, runtime}' "$FILE"
```

Show top 5 rows with shortened text:

```bash
jq '.response.rows[:5] | map({
  statement_id,
  source_anchor,
  row_markers,
  relevance_score,
  text_preview: (.statement_text[0:280])
})' "$FILE"
```

Show row projection (optional; secondary signal):

```bash
jq '.response.row_projection' "$FILE"
```

## 5) Regenerate the 5-query bundle

```bash
uv run python scripts/sqlite_capture_rust_reference_query_reviews.py \
  --prompts-path data/query_testsets/rust_reference_table1_retrieval_eval.yaml \
  --prompt-ids RET-RESOLVE-001,RET-RESOLVE-002,RET-RESOLVE-003,RET-RESOLVE-004,RET-RESOLVE-005 \
  --modes hybrid \
  --bundle-id five-query-hybrid-$(date -u +%Y%m%dT%H%M%SZ) \
  --top-k 8 \
  --candidate-limit 200 \
  --semantic-embed-base-url http://127.0.0.1:19080 \
  --semantic-rerank-base-url http://127.0.0.1:19081 \
  --embed-model-id Qwen/Qwen3-Embedding-4B \
  --reranker-model-id BAAI/bge-reranker-v2-m3 \
  --semantic-timeout-sec 120 \
  --semantic-retries 0
```
