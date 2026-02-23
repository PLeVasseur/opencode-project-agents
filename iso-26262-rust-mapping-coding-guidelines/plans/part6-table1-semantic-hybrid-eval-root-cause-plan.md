# Part 6 Table 1 Semantic/Hybrid Eval Root Cause Plan

## Objective

Identify the true failure mode behind semantic/hybrid eval instability, prove it with reproducible evidence, and land the smallest safe fix set so eval runs are reliable on the canonical DB path.

## Non-Negotiable Guardrails

- Keep active DB fixed to `.cache/sqlite_kb/current/rust_reference.sqlite`.
- Keep contract fixed to the chunk contract used by the failing baseline run.
- Keep source revision fixed during the root-cause cycle (no corpus drift mid-debug).
- Keep lexical mode out of triage matrix (semantic/hybrid only) unless explicitly needed.
- Never run the full 66-case eval per matrix cell.
- Keep `allow_degraded=false` in triage and confirmation runs.
- Use deterministic artifact naming per matrix cell to avoid result mixing.

## Problem Statement (Current Baseline)

- Canonical DB was rebuilt and is healthy at `.cache/sqlite_kb/current/rust_reference.sqlite`.
- Chunk schema/materialization gates pass:
  - `user_version=6`
  - `chunks=1418`
  - `chunk_embeddings=1418`
  - `missing_chunk_embeddings_qwen_chunkv1=0`
- Eval artifact shows failures concentrated in semantic/hybrid modes:
  - `.cache/sqlite_kb/reports/rust_reference/restart_phase0/20260222T231818Z/reports/retrieval_eval.json`
  - `failed_cases=54` (42 case failures + 12 gate failures)
  - Failure codes: `SEMANTIC_BACKEND_UNAVAILABLE` and `HYBRID_BACKEND_UNAVAILABLE`
- Five-query review bundle passed with `candidate_limit=200`, but each hybrid query is slow (about 58s to 101s):
  - `.cache/sqlite_kb/reports/rust_reference/restart_phase0/20260222T231818Z/reports/query_reviews/chunk-five-query-20260222T231818Z/manifest.json`

## Scope

### In scope

- Root-cause analysis for semantic/hybrid eval failures.
- Reranker endpoint/timeout behavior under eval load.
- Config and runtime differences between eval and review paths.
- Minimal code or config changes required to make eval runs reliable.

### Out of scope

- Reworking retrieval ranking logic itself.
- Adjusting quality thresholds for convenience.
- Large architecture changes unrelated to the reranker/eval failure path.

## Working Hypotheses

- H1: Eval load (`candidate_limit=5000`, timeout defaults) exceeds local reranker throughput; requests time out.
- H2: Client fallback to `/rerank` after `/v1/rerank` timeout adds noisy 404 tails that mask primary timeout cause.
- H3: Local python reranker worker is healthy at low load but unstable/slow at eval-scale payloads.
- H4: Eval profile settings are materially more aggressive than successful review bundle settings.
- H5: A large share of latency may be in backend Python runtime overhead (tokenization/serialization/locking) rather than model forward compute.

## Investigation Plan

## Workstream A0 - Instrumentation Before Matrix (Required)

- [ ] Add per-case timing buckets to eval artifacts before any matrix sweep:
  - `preflight_ms`
  - `lexical_ms`
  - `semantic_embed_ms`
  - `semantic_score_ms`
  - `rerank_ms`
  - `projection_ms`
  - `total_case_ms`
- [ ] Add per-case workload counters to eval artifacts:
  - `lexical_pool_size`
  - `semantic_pool_size`
  - `rerank_pool_size`
  - `rerank_doc_count`
- [ ] Add backend attempt traces for semantic/rerank calls:
  - endpoint (`/v1/rerank`, fallback endpoint),
  - timeout setting,
  - attempt latency,
  - HTTP status,
  - normalized error class (`timeout`, `http_404`, `connection`, `payload`),
  - retry index.
- [ ] Add per-cell artifact isolation for diagnostics:
  - `.../root_cause/<RUN_ID>/matrix/<CELL_ID>/eval.json`
  - `.../root_cause/<RUN_ID>/matrix/<CELL_ID>/backend_attempts.jsonl`
  - `.../root_cause/<RUN_ID>/matrix/<CELL_ID>/worker_rerank_requests.jsonl`
  - `.../root_cause/<RUN_ID>/matrix/<CELL_ID>/summary.json`
- [ ] Add runtime hygiene hooks:
  - rotate backend logs per matrix block,
  - record backend restart events in matrix metadata.
- [ ] Enforce pre-matrix instrumentation gate:
  - run one smoke triage pass,
  - confirm timing/workload/attempt fields are populated and non-null,
  - block matrix expansion until this gate passes.

## Workstream A1 - Backend Profiling and Runtime Attribution (Required)

- [ ] Add backend worker request timing instrumentation for rerank/embed paths, with per-request JSONL events including:
  - request id, operation, prompt/cell context,
  - doc count and effective sequence length,
  - queue wait/lock wait time,
  - preprocess/tokenization time,
  - model forward time,
  - postprocess/serialization time,
  - total request time and outcome.
- [ ] Add a sampled profiling mode for rerank worker to distinguish Python runtime overhead vs model compute:
  - low-overhead sampling (`py-spy` or `perf`) while running a controlled rerank-heavy triage cell,
  - optional PyTorch profiler trace for one bounded probe request.
- [ ] Emit backend profiling artifacts per profiled cell:
  - `worker_rerank_requests.jsonl` (request timing spans),
  - `worker_profile.svg` or `worker_profile.txt` (sampling profile),
  - `torch_profile_trace.json` (optional, bounded probe).
- [ ] Compute attribution summary per profiled cell:
  - `%python_runtime_overhead` (queue/lock/preprocess/postprocess),
  - `%model_forward_compute`,
  - `%network_or_io_overhead`.
- [ ] Enforce backend attribution gate before broad matrix expansion:
  - attribution summary present,
  - at least 90% of wall time explained by captured worker and client timing buckets,
  - hotspot list identifies top 3 cost centers with evidence links.

### A1.1 Tooling order and availability checks

- [x] Use this profiling order for rerank-heavy cells:
  1. structured worker spans + client attempt logs (required),
  2. `py-spy` sampling profile (primary),
  3. `perf` sampling profile (secondary, if permissions allow),
  4. bounded `torch.profiler` trace (optional deep dive).
- [x] Use uv best practices for profiler tooling:
  - prefer ephemeral execution with pinned versions via `uvx` (do not use `uv pip install` for matrix tooling),
  - record exact tool spec strings used per cell (`py-spy==...`, `perf` version, `torch` version) in `summary.json`.
- [x] Pinned tool specs (default):
  - `py-spy==0.4.1` (via `uvx --from py-spy==0.4.1 py-spy ...`),
  - `torch` from project lock/sync state (record `torch.__version__`).
- [ ] If repeated ephemeral installs are too slow, use a pinned `uv tool install` flow and record the installed version; do not switch to unpinned installs mid-run.
- [x] Run availability checks before matrix profiling:
  - `command -v py-spy`
  - `command -v perf`
  - `uv run python -c "import torch; print(torch.__version__)"`
- [x] Run a throwaway py-spy sanity probe before long cells:
  - use child-process mode (`py-spy record -- <command>`) against a short dummy script,
  - verify output artifact exists and is non-empty,
  - if probe fails, do not start a long profiled eval cell.
- [x] Record tool availability in per-cell `summary.json`.

### A1.2 Profiling command recipes (copy/paste templates)

```bash
# py-spy preferred mode when ptrace attach is restricted (no sudo):
# run the rerank worker as a child of py-spy so stacks can be sampled.
uvx --from py-spy==0.4.1 py-spy record \
  --rate 99 \
  --native \
  --output "${CELL_DIR}/worker_profile.svg" \
  -- \
  uv run python scripts/sqlite_local_semantic_worker.py \
    --mode rerank \
    --host 127.0.0.1 \
    --port 8081 \
    --model-id "BAAI/bge-reranker-v2-m3" \
    --cache-dir ".cache/sqlite_kb/models/hf" \
    --request-span-log-path "${CELL_DIR}/worker_rerank_requests.jsonl" \
    --service-role rerank

# py-spy attach mode (use only when permissions allow)
BACKEND_STATE=".cache/sqlite_kb/runtime/local_semantic_backend_state.json"
BACKEND_PID="$(jq -r '.rerank.pid' "${BACKEND_STATE}")"
sudo -E env "PATH=$PATH" uvx --from py-spy==0.4.1 py-spy record \
  --pid "${BACKEND_PID}" \
  --duration 120 \
  --rate 99 \
  --native \
  --output "${CELL_DIR}/worker_profile.svg"

# perf (secondary, native/kernel stacks)
sudo perf record -F 99 -g -p "${BACKEND_PID}" -- sleep 120
sudo perf report --stdio -i perf.data > "${CELL_DIR}/perf_report.txt"

# optional torch profiler deep-dive (bounded probe only)
# emits ${CELL_DIR}/torch_profile_trace.json
```

- [x] Do not silence profiler failures:
  - do not redirect py-spy stderr to `/dev/null` during setup,
  - capture profiler stderr/stdout to `${CELL_DIR}/worker_profile.log`.

### A1.3 `worker_rerank_requests.jsonl` schema contract (required)

- [x] Every worker request span record must include:
  - identity: `timestamp_utc`, `run_id`, `cell_id`, `trace_id`, `request_id`, `prompt_id`, `mode`, `operation`,
  - endpoint/attempt: `endpoint`, `attempt_index`, `max_attempts`, `timeout_sec`,
  - workload: `doc_count`, `effective_seq_len`,
  - timing (milliseconds): `queue_wait_ms`, `lock_wait_ms`, `tokenize_ms`, `model_forward_ms`, `postprocess_ms`, `serialize_ms`, `total_ms`,
  - result: `status`, `error_class`, optional `error_detail`.
- [x] Units and types:
  - all `*_ms` fields are numeric milliseconds (`float`),
  - counts are integers,
  - IDs are non-empty strings.

### A1.4 Correlation key contract (required)

- [x] Generate `trace_id` per semantic/rerank attempt on client side.
- [x] Propagate `trace_id` to backend request headers and include it in:
  - client attempt logs (`backend_attempts.jsonl`),
  - worker span logs (`worker_rerank_requests.jsonl`),
  - eval case artifacts (`eval.json`).
- [x] Correlation gate:
  - at least 95% of client attempts must join to worker span records by `trace_id`.

### A1.5 Decision thresholds for root-cause classification

- [x] Compute per-cell attribution percentages:
  - `%python_runtime_overhead = (queue_wait + lock_wait + tokenize + postprocess + serialize) / total`,
  - `%model_forward_compute = model_forward / total`,
  - `%timeout_waste = timeout-attempt-duration / total`.
- [x] Use explicit thresholds to pick fix path:
  - Python-overhead dominant: `%python_runtime_overhead > 35%`,
  - model-compute dominant: `%model_forward_compute > 60%`,
  - policy waste dominant: `%timeout_waste > 15%`,
  - lock contention hotspot: `%lock_wait > 10%`.

### A1.6 Reproducible attribution summary command

- [x] Add and use a single summary command for every profiled cell:

```bash
uv run python scripts/sqlite_root_cause_attribution_summary.py \
  --eval-path "${CELL_DIR}/eval.json" \
  --backend-attempts-path "${CELL_DIR}/backend_attempts.jsonl" \
  --worker-spans-path "${CELL_DIR}/worker_rerank_requests.jsonl" \
  --output-path "${CELL_DIR}/summary.json"
```

- [x] `summary.json` must include:
  - explained-vs-wall-clock percentage,
  - python-vs-model-vs-timeout split,
  - top 3 hotspots,
  - recommended fix lane for the cell.

### A1.7 Environment controls for low-noise comparisons

- [x] Warmup policy:
  - run one warmup pass per cell configuration before recording profiler artifacts.
- [ ] Backend reset policy:
  - restart backend before each matrix block,
  - restart immediately after sustained timeout streak,
  - record restart events in `summary.json`.
- [ ] Background-load controls:
  - avoid concurrent heavy jobs during profiled cells,
  - record basic host state (CPU load, memory pressure) in `summary.json`.

## Workstream A - Freeze Repro Baseline

- [ ] Keep this run as fixed baseline:
  - Run ID: `20260222T231818Z`
  - Eval report: `.../reports/retrieval_eval.json`
  - Five-query bundle: `.../reports/query_reviews/chunk-five-query-20260222T231818Z/`
- [ ] Generate one summary JSON with:
  - failed case counts by mode/error code,
  - gate failures,
  - average/peak query durations for successful lexical path.
- [ ] Create a triage prompt subset artifact from known failures (semantic/hybrid only):
  - include at least 6 prompts spanning issue/resolution/negative slices,
  - include both failure shapes (`preflight rerank fail`, `rerank timeout after retries`),
  - persist as a timestamped artifact under run reports so the same subset is reused across matrix cells.
- [ ] Add a triage-run command template to the run artifact root so operators do not accidentally run full-pack eval during matrix sweeps.

## Workstream B - Endpoint and Client Contract Validation

- [ ] Verify local worker supports expected endpoints:
  - `/v1/embeddings`
  - `/v1/rerank`
- [ ] Confirm fallback behavior in `scripts/semantic_backend_client.py` when `/v1/rerank` times out.
- [ ] Confirm whether fallback to `/rerank` should remain enabled for this backend profile.
- [ ] Add explicit debug classification in logs: `timeout`, `http_404`, `connection`, `payload`.
- [ ] Produce a one-page endpoint contract note for `python-local` backend profile:
  - expected rerank endpoint(s),
  - whether fallback endpoints are supported,
  - expected behavior on timeout.

## Workstream C - Controlled Experiment Matrix

- [ ] Enforce a two-phase run budget to avoid repeated 66-case eval runs:
  - Phase C1 (triage): run matrix on a small failed-case subset only.
  - Phase C2 (confirmation): run full 66-case eval once, after selecting stable settings.
  - Do not run full 66-case eval per matrix cell.
- [ ] Start Workstream C only after Workstream A0 + A1 gates are green.
- [ ] Define triage prompt subset from known failures (minimum 6 prompts, semantic/hybrid only), including both failure shapes:
  - reranker timeout after retries,
  - preflight rerank failure.
  - Recommended IDs: `RET-ISSUE-001`, `RET-ISSUE-007`, `RET-ISSUE-010`, `RET-RESOLVE-001`, `RET-RESOLVE-004`, `RET-NEG-001`.
- [ ] Run a deterministic matrix against canonical DB using triage subset:
  - `candidate_limit`: `200`, `500`, `1000`, `5000`
  - `semantic-timeout-sec`: `60`, `120`, `180`
  - `semantic-retries`: `0`, `2`
  - `top_k`: `5`, `8`, `10`
  - modes tracked separately: `semantic`, `hybrid`
- [ ] For each triage matrix cell, capture:
  - pass/fail count,
  - median and p95 query duration,
  - reranker timeout incidence,
  - preflight rerank check result.
- [ ] Capture rerank workload explicitly per cell:
  - rerank candidate count actually scored,
  - semantic candidate pool size,
  - query duration by mode.
- [ ] If rerank workload is not observable in current artifacts, add temporary instrumentation before continuing matrix expansion.
- [ ] Use per-cell artifact paths:
  - `.../root_cause/<RUN_ID>/matrix/<CELL_ID>/...`
  - where `<CELL_ID>` includes key knobs (for example `cl200_to120_rt0_tk8`).
- [ ] Use fail-fast policy for clearly bad cells:
  - abort cell early after repeatable backend-unavailable failures on first 3 prompts,
  - mark cell as fail-fast with reason, do not continue wasting runtime.
- [ ] Select a candidate stable profile from triage evidence, then execute exactly one full 66-case eval run for confirmation.

## Workstream D - Runtime Diagnostics

- [ ] Correlate eval failures to runtime logs:
  - `.cache/sqlite_kb/runtime/logs/rerank.log`
  - `.cache/sqlite_kb/runtime/logs/embed.log`
- [ ] Rotate and snapshot backend logs by matrix block to preserve clean attribution.
- [ ] Capture process health while matrix runs:
  - PID liveness,
  - CPU saturation,
  - memory growth,
  - request queue/latency if observable.
- [ ] Determine whether `BrokenPipeError` is primarily client timeout fallout or server fault.
- [ ] Define backend reset policy:
  - restart backend before first cell of each matrix block,
  - force restart on sustained timeout streak,
  - record restart events in matrix metadata.

## Workstream E - Decision and Fix Selection

- [ ] Use evidence to choose one primary root cause class:
  - `throughput_timeout`, `endpoint_contract`, `backend_stability`, or `mixed`.
- [ ] Apply smallest fix set that resolves failures without lowering quality bars.
- [ ] Keep infra and quality decisions separate:
  - first clear infra reliability (no backend-unavailable failures),
  - then assess retrieval quality gates on stable infra.

Candidate fix options (ranked by likely impact):

1. Eval profile controls:
   - Introduce explicit eval profile defaults aligned to backend capacity.
   - Keep review and eval profiles separate and declared in artifacts.
2. Reranker call discipline:
   - Better timeout and retry tuning for rerank path.
   - Optional hard cap for rerank candidate pool in eval profile.
3. Client/backend contract cleanup:
   - Optional `/rerank` compatibility endpoint in local worker, or
   - disable unsupported fallback for known local backend profile.
4. Observability hardening:
   - first-class failure reason codes in eval report for timeout vs endpoint mismatch.

## Verification Gates

- [ ] Instrumentation gate:
  - per-case timing/workload/attempt telemetry is present for every triage cell.
- [ ] Attribution gate:
  - timing buckets account for at least 90% of observed wall-clock runtime per cell.
- [ ] Backend attribution gate:
  - worker-level timing spans and profiler artifact exist for at least one rerank-heavy semantic cell and one rerank-heavy hybrid cell,
  - report includes split between Python overhead and model-forward compute,
  - top 3 backend hotspots are named with direct artifact evidence.
- [ ] Correlation gate:
  - at least 95% of client attempts join to worker spans by `trace_id`.
- [ ] Tooling gate:
  - `py-spy` and/or `perf` availability status is recorded per profiled cell,
  - if one tool is unavailable, fallback path and rationale are recorded.
- [ ] Infra reliability gate:
  - zero `SEMANTIC_BACKEND_UNAVAILABLE` and `HYBRID_BACKEND_UNAVAILABLE` case failures on selected stable config.
- [ ] Full 66-case eval confirmation is executed exactly once after triage selection (unless an explicit follow-up rerun is requested).
- [ ] Full 66-case confirmation run completes within declared timeout budget and writes report artifact.
- [ ] Quality gate review occurs after infra reliability gate passes (do not conflate infra and retrieval-quality regressions).
- [ ] Five-query bundle still passes on same config lane.
- [ ] No regression in canonical DB invariants (schema/materialization gates remain green).
- [ ] Root-cause summary report emitted with evidence links and final decision.

## Deliverables

- [ ] Root-cause summary markdown in run artifact directory (timestamped).
- [ ] Matrix results JSON/CSV with per-cell pass/fail + latency stats + rerank workload counts.
- [ ] Per-case timing breakdown in eval artifacts for triage and confirmation runs.
- [ ] Backend attempt trace artifacts per matrix cell.
- [ ] Backend worker timing trace artifacts (`worker_rerank_requests.jsonl`) for profiled cells.
- [ ] At least one sampling profiler artifact (`worker_profile.svg` or equivalent) with hotspot summary.
- [ ] Optional native-level profile artifact (`perf_report.txt`) when permissions allow.
- [ ] Backend attribution summary table separating Python overhead vs model-forward compute.
- [ ] Reproducible per-cell summary artifact (`summary.json`) generated by one standard command.
- [ ] Triage subset definition artifact used for matrix runs.
- [ ] Cell-index artifact mapping `<CELL_ID>` to exact settings.
- [ ] Any code/config patches needed to fix selected root cause.
- [ ] Updated runbook guidance for semantic/hybrid eval profile settings.

## File Targets (Expected)

- `scripts/sqlite_eval_rust_reference_retrieval.py`
- `scripts/sqlite_query_rust_reference.py` (only if rerank pool/profile wiring needs changes)
- `scripts/semantic_backend_client.py`
- `scripts/sqlite_local_semantic_worker.py` (only if endpoint compatibility is selected)
- `scripts/sqlite_local_semantic_backend.py` (only if profiler launch hooks are needed)
- `scripts/sqlite_root_cause_attribution_summary.py`
- `scripts/sqlite_capture_rust_reference_query_reviews.py` (only if triage harness or cell labeling support is added)
- `plans/part6-table1-retrieval-restart-implementation-runbook.md`

## Recommended Execution Order

- [ ] Step 1: Workstream A0 (instrumentation and pre-matrix gate)
- [ ] Step 2: Workstream A1 (backend profiling and runtime attribution gate)
- [ ] Step 3: Workstreams A + B (freeze baseline, triage subset, endpoint contract)
- [ ] Step 4: Workstream D setup (log rotation + backend reset policy)
- [ ] Step 5: Workstream C Phase C1 (triage subset matrix with fail-fast)
- [ ] Step 6: Workstream E (select + implement smallest fix set)
- [ ] Step 7: Workstream C Phase C2 (single full 66-case confirmation run)
- [ ] Step 8: Run verification gates and publish deliverables
