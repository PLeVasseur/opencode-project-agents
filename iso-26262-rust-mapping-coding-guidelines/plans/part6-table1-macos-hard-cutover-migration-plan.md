# Part 6 Table 1 macOS Host Hard-Cutover Migration Plan

## Objective

Hard-cut semantic/hybrid retrieval runtime from the Ubuntu `x86_64` VM to native macOS `arm64` host execution, enable Apple MPS acceleration for local semantic workers, and keep A1-grade observability and reproducibility intact.

## Why This Cutover Is Justified

From host benchmark output in `reports/macos-host-reranker-capability-check.md`:

- Host device is `Apple M3 Max`, `64 GB RAM`, `arm64`.
- PyTorch backend on host supports MPS (`mps_built=True`, `mps_available=True`).
- Rerank benchmark (`64` pairs):
  - CPU: `9.482s` at `max_len=512`, `20.053s` at `1024`.
  - MPS: `2.742s` at `max_len=512`, `7.062s` at `1024`.
- Current VM A1 evidence shows rerank model-forward for `doc_count=64` around `93-95s`.

Conclusion: host+MPS is the highest ROI path and should be the default runtime lane.

## Non-Negotiable Guardrails

- Keep canonical DB policy: `.cache/sqlite_kb/current/rust_reference.sqlite`.
- Keep current chunk contract flow and chunk-first restart constraints.
- Preserve A1 tracing/profiling artifact schema and correlation gates.
- Do not weaken eval quality gates to make migration look successful.
- Keep VM runnable as a rollback lane until host passes full validation.

## Scope

### In scope

- Runtime migration to host macOS for semantic backend and eval runs.
- Worker device selection support (`auto/cpu/mps/cuda`) and telemetry.
- Endpoint/fallback hardening for `python-local` backend profile.
- Host-oriented runbook + validation ladder + rollback plan.

### Out of scope

- Changing retrieval quality definitions or contract semantics.
- Rebuilding ranking methodology from scratch.
- Cloud deployment or distributed serving.

## Workstream M0 - Freeze Baseline and Artifacts

- [ ] Freeze known VM baseline artifacts and reference them in migration notes:
  - A1 profiled cell: `.cache/sqlite_kb/reports/rust_reference/root_cause/20260223T163527Z/matrix/retryprobe_cl80_to120_rt0_tk5_profiled_pyspychild_v4/`
  - Warmup attribution: `.cache/sqlite_kb/reports/rust_reference/root_cause/20260223T150733Z/matrix/cl80_to120_rt0_tk5_profiled/warmup_summary.json`
- [ ] Keep VM code path untouched until host passes M4 success gates.

## Workstream M1 - Host Bootstrap (macOS)

- [ ] Place repo on host filesystem (not inside Linux VM mount).
- [ ] Install/sync runtime deps on host:

```bash
cd "${HOST_REPO_ABS}"
uv python install 3.11
uv sync --python 3.11 --extra semantic-local
```

- [ ] Verify host backend capabilities:

```bash
uv run python - <<'PY'
import torch
print(torch.__version__)
print("cuda", torch.cuda.is_available())
print("mps", torch.backends.mps.is_built(), torch.backends.mps.is_available())
PY
```

- [ ] Optional stability env defaults for host workers:
  - `PYTORCH_ENABLE_MPS_FALLBACK=1`
  - `TOKENIZERS_PARALLELISM=false`

## Workstream M2 - Device Selection and Telemetry Hardening

- [ ] Add worker CLI arg `--device {auto,cpu,mps,cuda}` (default `auto`).
- [ ] Add deterministic resolver in worker runtime:
  - `auto -> cuda if available -> mps if available -> cpu`.
- [ ] Add selected device metadata to:
  - worker startup log,
  - `worker_rerank_requests.jsonl` (`device`, `dtype` when available),
  - summary output (`summary.json`) for each profiled cell.
- [ ] Add backend launcher support to pass distinct devices:
  - `--embed-device`
  - `--rerank-device`
- [ ] Keep embed/rerank default single-worker model to avoid host memory pressure during cutover.

## Workstream M3 - Endpoint/Retry Policy Fixes Before Cutover

- [ ] Hard-code profile endpoint capabilities:
  - `python-local`: use `/v1/embed` and `/v1/rerank` only.
  - `tei`: use configured TEI endpoints only.
- [ ] Disable fallback-to-unknown-endpoint behavior for `python-local`.
- [ ] Keep retries bounded and single-layer:
  - default `semantic_retries=0` during migration validation,
  - if retries are re-enabled later, add capped backoff + jitter.
- [ ] Add explicit metric in attempt logs: `fallback_attempted` and `fallback_endpoint`.

## Workstream M4 - Host Runtime Defaults (Latency-Safe)

- [ ] Set reranker truncation default to `max_length=512`.
- [ ] Keep rerank doc budget at current validated behavior first; tune only after parity pass.
- [ ] Keep timeout at `120s` for first host parity run, then tighten once stable.
- [ ] Keep canonical query/eval inputs unchanged for parity comparisons.

## Workstream M5 - Validation Ladder (Required)

### M5.1 Fast sanity

- [ ] Start host backend with MPS rerank.
- [ ] Run one semantic + one hybrid query smoke.
- [ ] Gate: both pass, no backend unavailable errors.

### M5.2 Profiled retry-probe subset

- [ ] Run retry-probe subset with full A1 artifacts:
  - `eval.json`
  - `backend_attempts.jsonl`
  - `worker_rerank_requests.jsonl`
  - `worker_profile.svg`
  - `summary.json`
- [ ] Gate:
  - trace join rate `>=95%`,
  - zero `/rerank` fallback attempts for `python-local`,
  - no `SEMANTIC_BACKEND_UNAVAILABLE`/`HYBRID_BACKEND_UNAVAILABLE` failures.

### M5.3 Warmup triage subset

- [ ] Run warmup subset used in root-cause cycle with same config controls.
- [ ] Gate:
  - no backend unavailable failures,
  - timeout waste `<=5%` of case wall time,
  - rerank `doc_count=64` p95 `model_forward_ms <= 25000` on host.

### M5.4 Full eval parity run (66-case)

- [ ] Run full retrieval eval once on host with canonical DB/contract.
- [ ] Gate:
  - no backend unavailable failures,
  - gate pass rate meets or exceeds current baseline,
  - artifact completeness and schema parity preserved.

## Workstream M6 - Hard Cutover

- [ ] Mark host lane as default in runbook/docs.
- [ ] Update commands to launch backend from host by default.
- [ ] Archive VM-specific runtime path as rollback-only.
- [ ] Require future root-cause/eval runs to record host machine metadata.

## Rollback Plan

- [ ] Keep VM runtime scripts and configs untouched until M5.4 passes.
- [ ] If host has blocker:
  - switch backend profile back to VM lane,
  - preserve host artifacts for diagnosis,
  - open follow-up issue tagged `host-cutover-blocker` with evidence links.

## Deliverables

- [ ] Updated runtime scripts with device selection and endpoint hardening.
- [ ] Host runbook commands (bootstrap, start/stop, eval, profiling).
- [ ] Host validation artifact set for retry-probe, warmup, and full eval.
- [ ] Cutover note with before/after latency/failure metrics and rollback status.

## Expected Wall-Clock for Migration

- M1-M3 implementation and script updates: `1.5-3.0 hours`
- M5 validation ladder (including one full eval): `2.0-4.0 hours`
- Cutover docs + cleanup: `0.5-1.0 hours`
- Total expected: `4-8 hours` depending on model download/cache state.
