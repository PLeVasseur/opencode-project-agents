# Part 6 Table 1 Retrieval Restart: Implementation Runbook (Rip-and-Replace)

This runbook defines deterministic command lanes for restart implementation cycles.

This is not a legacy dual-run flow.

- No legacy control artifact freeze/copy/compare.
- No legacy-vs-new delta gating.

All commands assume repo root:

- `/home/pete.levasseur/personal/iso-26262-rust-mapping-coding-guidelines`

## Canonical Active DB Policy (Required)

- Active retrieval/materialization DB path is fixed:
  - `.cache/sqlite_kb/current/rust_reference.sqlite`
- Canonical manifest and snapshot roots remain fixed:
  - `data/sqlite_kb_manifest.yaml`
  - `.cache/sqlite_kb/snapshots/rust_reference`
- Restart cycle directories under `.cache/sqlite_kb/reports/rust_reference/restart_phase0/<RUN_ID>/`
  are artifact-only (reports, bundles, run status, copied contract), not active DB locations.

## Required Interfaces Before Running Cycles

Execution must not start until these are true:

- `scripts/sqlite_build_rust_reference.py` accepts `--retrieval-corpus chunk`.
- `config/sqlite_query_contracts/rust_reference_chunk.yaml` exists.
- Chunk contract includes query IDs:
  - `chunk_corpus_v1_all`
  - `lexical_chunk_search_v1`
  - `table1_row_requirements_v2`
  - `snapshot_metadata`
  - `semantic_model_metadata`
- Query and eval paths execute against chunk contract without legacy query-id fallback.
- Deterministic source pinning is enforced for build runs.

If any interface is missing, implement it first.

## Commit Policy During Execution (Required)

- Complete one restart-plan step at a time.
- When a step is complete, create a commit before starting the next step.
- Use Conventional Commits and include the step number in the subject.
- Commit body must include:
  - commands run,
  - artifact/report paths,
  - any blocker notes.

Suggested commit flow at each step boundary:

```bash
git status
git add -A
git commit -m "<type>(<scope>): <summary> (step <N>)"
git status
```

## 1) Shell Setup

```bash
export RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
export RESTART_ROOT_REL=".cache/sqlite_kb/reports/rust_reference/restart_phase0/${RUN_ID}"

export PROMPT_PACK_REL="data/query_testsets/rust_reference_table1_retrieval_eval.yaml"
export EXTRACTOR_DB_ABS="/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/.cache/iso26262/iso26262_index.sqlite"

export ACTIVE_DB_REL=".cache/sqlite_kb/current/rust_reference.sqlite"
export ACTIVE_SNAPSHOT_REL=".cache/sqlite_kb/snapshots/rust_reference"
export ACTIVE_MANIFEST_REL="data/sqlite_kb_manifest.yaml"
export ACTIVE_QUERY_LOG_REL=".cache/sqlite_kb/query_logs/rust_reference"
export ACTIVE_REPORT_REL=".cache/sqlite_kb/reports/rust_reference"

export CHUNK_REPORT_REL="${RESTART_ROOT_REL}/reports"
export CHUNK_CONTRACT_REL="${RESTART_ROOT_REL}/rust_reference_chunk.contract.yaml"

mkdir -p "${RESTART_ROOT_REL}" "${CHUNK_REPORT_REL}" "${ACTIVE_DB_REL%/*}" "${ACTIVE_SNAPSHOT_REL}" "${ACTIVE_QUERY_LOG_REL}" "${ACTIVE_REPORT_REL}"
test -f "${EXTRACTOR_DB_ABS}"

cp "config/sqlite_query_contracts/rust_reference_chunk.yaml" "${CHUNK_CONTRACT_REL}"
sha256sum "${CHUNK_CONTRACT_REL}" > "${CHUNK_REPORT_REL}/chunk_contract_sha256.txt"
```

## 2) Pin Source Revision Deterministically

```bash
export REF_CACHE_DIR=".cache/sqlite_kb/sources/rust-reference"

if [ ! -d "${REF_CACHE_DIR}/.git" ]; then
  git clone --quiet "https://github.com/rust-lang/reference.git" "${REF_CACHE_DIR}"
fi

git -C "${REF_CACHE_DIR}" fetch --quiet origin
export RUST_REF_REMOTE_HEAD="$(git -C "${REF_CACHE_DIR}" symbolic-ref refs/remotes/origin/HEAD)"
export RUST_REF_REV="$(git -C "${REF_CACHE_DIR}" rev-parse "${RUST_REF_REMOTE_HEAD}")"

printf '%s\n' "${RUST_REF_REV}" > "${RESTART_ROOT_REL}/source_revision.txt"
printf '%s\n' "${RUST_REF_REMOTE_HEAD}" > "${RESTART_ROOT_REL}/source_remote_head_ref.txt"
```

### 2.1 Canonical DB staleness preflight (required)

```bash
export ACTIVE_DB_USER_VERSION="0"
export ACTIVE_DB_HAS_CHUNKS="0"

if [ -f "${ACTIVE_DB_REL}" ]; then
  ACTIVE_DB_USER_VERSION="$(sqlite3 "file:${ACTIVE_DB_REL}?mode=ro" "PRAGMA user_version;" 2>/dev/null || printf '0')"
  ACTIVE_DB_HAS_CHUNKS="$(sqlite3 "file:${ACTIVE_DB_REL}?mode=ro" "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='chunks';" 2>/dev/null || printf '0')"
fi

if [ "${ACTIVE_DB_USER_VERSION}" -lt 6 ] || [ "${ACTIVE_DB_HAS_CHUNKS}" -eq 0 ]; then
  printf 'stale canonical db detected: user_version=%s has_chunks=%s\n' "${ACTIVE_DB_USER_VERSION}" "${ACTIVE_DB_HAS_CHUNKS}"
  printf 'action: rebuild in section 3 (mandatory)\n'
fi
```

## 3) Build Chunk DB

Do not reuse an existing DB file. This step is mandatory for restart cycles and rebuilds
`${ACTIVE_DB_REL}` in place.

```bash
export CHUNK_DB_REL="${ACTIVE_DB_REL}"
export CHUNK_SNAPSHOT_REL="${ACTIVE_SNAPSHOT_REL}"
export CHUNK_MANIFEST_REL="${ACTIVE_MANIFEST_REL}"
export CHUNK_QUERY_LOG_REL="${ACTIVE_QUERY_LOG_REL}"

uv run python scripts/sqlite_build_rust_reference.py \
  --db-path "${CHUNK_DB_REL}" \
  --snapshot-root "${CHUNK_SNAPSHOT_REL}" \
  --manifest-path "${CHUNK_MANIFEST_REL}" \
  --report-root "${CHUNK_REPORT_REL}" \
  --extractor-db "${EXTRACTOR_DB_ABS}" \
  --reference-revision "${RUST_REF_REV}" \
  --retrieval-mode hybrid \
  --retrieval-corpus chunk
```

### 3.1 Chunk schema sanity gate (required before materialization)

```bash
test "$(sqlite3 "file:${CHUNK_DB_REL}?mode=ro" "PRAGMA user_version;")" -ge 6
test "$(sqlite3 "file:${CHUNK_DB_REL}?mode=ro" "SELECT COUNT(*) FROM chunks;")" -gt 0
```

## 4) Build Embeddings (when Step 4 of plan is active)

```bash
uv run python scripts/sqlite_materialize_rust_reference_embeddings.py \
  --db-path "${CHUNK_DB_REL}" \
  --contract-path "${CHUNK_CONTRACT_REL}" \
  --query-log-root "${CHUNK_QUERY_LOG_REL}" \
  --batch-size 32 \
  --semantic-retries 2 \
  --progress-log-path "${CHUNK_REPORT_REL}/materialize_progress.jsonl"
```

### 4.1 Embedding completeness gate (required before eval/review)

```bash
export EMBED_MODEL_ID="${RUST_REF_EMBED_MODEL_ID:-Qwen/Qwen3-Embedding-4B}"
export MISSING_CHUNK_EMBEDDINGS="$(sqlite3 "file:${CHUNK_DB_REL}?mode=ro" "SELECT COUNT(*) FROM chunks AS c LEFT JOIN chunk_embeddings AS e ON e.chunk_uid = c.chunk_uid AND e.model_id = '${EMBED_MODEL_ID}' AND e.embed_version = 'chunk-v1' WHERE e.chunk_uid IS NULL;")"

test "$(sqlite3 "file:${CHUNK_DB_REL}?mode=ro" "SELECT COUNT(*) FROM chunks;")" -gt 0
test "${MISSING_CHUNK_EMBEDDINGS}" -eq 0
```

## 5) Query and Eval Smoke

### 5.1 Deterministic lexical reproducibility check

```bash
export REPRO_QUERY_TEXT="How should Rust code handle defensive error paths safely?"

uv run python scripts/sqlite_query_rust_reference.py \
  --mode lexical \
  --query-text "${REPRO_QUERY_TEXT}" \
  --db-path "${CHUNK_DB_REL}" \
  --contract-path "${CHUNK_CONTRACT_REL}" \
  --query-log-root "${CHUNK_QUERY_LOG_REL}" \
  --top-k 10 \
  --candidate-limit 5000 \
  --save-response-path "${CHUNK_REPORT_REL}/repro_run_a.json"

uv run python scripts/sqlite_query_rust_reference.py \
  --mode lexical \
  --query-text "${REPRO_QUERY_TEXT}" \
  --db-path "${CHUNK_DB_REL}" \
  --contract-path "${CHUNK_CONTRACT_REL}" \
  --query-log-root "${CHUNK_QUERY_LOG_REL}" \
  --top-k 10 \
  --candidate-limit 5000 \
  --save-response-path "${CHUNK_REPORT_REL}/repro_run_b.json"

jq -e -s '
  (
    .[0].response.rows
    | map(.chunk_uid // .statement_id // .source_anchor)
  )
  ==
  (
    .[1].response.rows
    | map(.chunk_uid // .statement_id // .source_anchor)
  )
' "${CHUNK_REPORT_REL}/repro_run_a.json" "${CHUNK_REPORT_REL}/repro_run_b.json"
```

### 5.2 Eval report artifact

```bash
uv run python scripts/sqlite_eval_rust_reference_retrieval.py \
  --db-path "${CHUNK_DB_REL}" \
  --contract-path "${CHUNK_CONTRACT_REL}" \
  --eval-path "${PROMPT_PACK_REL}" \
  --query-log-root "${CHUNK_QUERY_LOG_REL}" \
  --top-k 10 \
  --candidate-limit 5000 \
  --semantic-retries 2 \
  --semantic-backend-profile "python-local" \
  --report-path "${CHUNK_REPORT_REL}/retrieval_eval.json"
```

### 5.3 Five-query review bundle artifact

Run this only after 5.1 + 5.2 pass and 4.1 reports zero missing chunk embeddings.

```bash
uv run python scripts/sqlite_capture_rust_reference_query_reviews.py \
  --prompts-path "${PROMPT_PACK_REL}" \
  --prompt-ids "ret-resolve-001,ret-resolve-002,ret-resolve-003,ret-resolve-004,ret-resolve-005" \
  --modes "hybrid" \
  --db-path "${CHUNK_DB_REL}" \
  --contract-path "${CHUNK_CONTRACT_REL}" \
  --query-log-root "${CHUNK_QUERY_LOG_REL}" \
  --top-k 8 \
  --candidate-limit 200 \
  --bundle-id "chunk-five-query-${RUN_ID}" \
  --output-dir "${CHUNK_REPORT_REL}/query_reviews" \
  --include-score-breakdown \
  --semantic-timeout-sec 120 \
  --semantic-retries 0 \
  --persist-semantic-cache \
  --no-allow-online-corpus-embedding
```

## 6) Archive Run Cycle Artifacts

```bash
jq -n \
  --arg run_id "${RUN_ID}" \
  --arg source_revision "${RUST_REF_REV}" \
  --arg db_path "${CHUNK_DB_REL}" \
  --arg chunk_report "${CHUNK_REPORT_REL}/retrieval_eval.json" \
  --arg chunk_bundle "${CHUNK_REPORT_REL}/query_reviews/chunk-five-query-${RUN_ID}" \
  '{run_id: $run_id, source_revision: $source_revision, db_path: $db_path, chunk_report: $chunk_report, chunk_bundle: $chunk_bundle}' \
  > "${RESTART_ROOT_REL}/reports/run_status.json"

tar -czf "${RESTART_ROOT_REL}/restart_cycle_${RUN_ID}.tar.gz" \
  -C "${RESTART_ROOT_REL}" reports rust_reference_chunk.contract.yaml source_revision.txt source_remote_head_ref.txt
```

Update plan checkboxes and session capsule after each cycle.
