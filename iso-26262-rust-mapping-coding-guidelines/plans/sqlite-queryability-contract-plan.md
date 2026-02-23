# SQLite Plan: Queryability Contract (Cross-DB)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for the active query-contract task plus shared SQLite guardrail files.
  - [ ] Do not read unrelated repository code while defining or validating this contract.
  - [ ] If additional files are required, record the reason first.

- [ ] Define one cross-database query contract for row-first tuple closure workflows.
  - [ ] Standardize queryable identities (`row_node_id`, `row_marker`, `violation_pattern_id`, `mechanism_id`).
  - [ ] Standardize evidence projections (`source_id`, `source_anchor`, `evidence_kind`, `confidence`).
  - [ ] Ensure all resource DBs can satisfy controller-critical lookups deterministically.

## Phase 0 - Contract Discovery

- [ ] Enumerate required query families for implementation and autonomous runs.
  - [ ] Row lane closure queries (missing mechanisms, weak evidence, unresolved exclusions).
  - [ ] Mechanism expansion queries (all mechanisms for one row+violation).
  - [ ] Drift queries (version changes affecting previously accepted tuples).
- [ ] Define canonical output shape for each query family.
  - [ ] Stable column names and value domains.
  - [ ] Deterministic ordering and tie-breaking rules.

## Contract Specification

- [ ] Publish SQL contract templates and expected result schema.
  - [ ] Define required joins from source DBs into `rust_iso_evidence_hub.sqlite`.
  - [ ] Define null-handling and fallback semantics for partial evidence.
  - [ ] Define confidence aggregation and ranking rules.
  - [ ] Define per-row verdict domain: `applicable` or `not_applicable` only (no `unknown`).
  - [ ] Define mandatory rationale shape for `not_applicable` (reason + source anchors + stable IDs).

## Access Boundary and Safety Guardrails

- [ ] Place a Python wrapper in front of each SQLite DB and disallow direct ad-hoc mutation paths.
  - [ ] Wrapper location convention: `scripts/sqlite_query_<db_name>.py`.
  - [ ] Query contracts location: `config/sqlite_query_contracts/<db_name>.yaml`.
  - [ ] Shared guardrail module: `scripts/sqlite_query_guardrails.py`.
- [ ] Enforce read-only query execution semantics.
  - [ ] Open SQLite with read-only mode and set `PRAGMA query_only=ON`.
  - [ ] Allow only contract query IDs and parameterized statements.
  - [ ] Block write/DDL/ATTACH/extension operations.
- [ ] Enforce operational limits and auditability.
  - [ ] Set max rows, timeout, and deterministic ordering requirements per query family.
  - [ ] Emit query logs to `.cache/sqlite_kb/query_logs/<db_name>/`.
  - [ ] Track active snapshot metadata in `data/sqlite_kb_manifest.yaml`.

## Performance and Index Strategy

- [ ] Define latency SLOs for controller usage.
  - [ ] Per-query latency targets for interactive and autonomous modes.
  - [ ] Batch query throughput targets for row closure scans.
- [ ] Define baseline indexing requirements.
  - [ ] Required B-tree indexes for key joins.
  - [ ] Required FTS indexes for text-backed discovery paths.

## Validation and Gating

- [ ] Build a queryability conformance suite.
  - [ ] Add deterministic fixtures with expected query outputs.
  - [ ] Fail if any required query cannot execute or violates schema/ordering contract.
  - [ ] Fail if latency exceeds SLO thresholds.
  - [ ] Fail if any Table 1 row (`1a`..`1i`) is missing a verdict.
  - [ ] Fail if any `not_applicable` verdict lacks source-backed rationale and joinable anchors.
  - [ ] Fail if wrapper guardrails permit non-contract queries or write-capable statements.

## Deliverables

- [ ] Deliver query contract spec and conformance tests.
  - [ ] Add reusable SQL templates for controller iterations.
  - [ ] Add a machine-readable query contract manifest consumed by DB-specific plans.
  - [ ] Add shared wrapper test harness under `tests/unit/sqlite_kb/`.
