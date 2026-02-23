# 2026-02-15 make.py FLS Execution Parity Plan

## Context

`./make.py` currently fails with `ModuleNotFoundError` when invoked directly with system Python.
This is not aligned with FLS behavior, where direct `./make.py` execution works via `uv` shebang and dependency-managed runtime.

## Objective

Restore FLS-style operator experience while preserving the Sphinx traceability command contract.

## Scope

- In scope: `make.py` execution model, dependency bootstrap behavior, direct invocation UX, Python style/lint parity (Black + Flake8), CI checks, and docs updates.
- Out of scope: changing traceability schema/content semantics, reworking migration stage outputs.

## Plan

### 0) Execution discipline (mandatory)

- [x] Use checkbox-driven execution as the system of record for this plan.
- [x] Every completed task and child task must be checked (`[x]`) immediately before moving on.
- [x] Do not advance to the next parent section until required child checkboxes in the current section are complete.
- [x] If blocked, record blocker details inline under the blocked task and keep it unchecked.

### 0A) New-session preflight runbook (mandatory)

- [x] Add a copy/paste-safe preflight block for first-time operators.
  - [x] Include repository root check (`pwd`) and expected directory.
  - [x] Include `uv --version` check and fallback note if missing.
  - [x] Include `uv sync` and expected success criteria.
  - [x] Include direct launcher checks: `./make.py --help`, then `./make.py`.
  - [x] Include explicit fallback checks: `uv run python make.py --help`, `uv run python make.py build`.
- [x] Add expected outcomes for each preflight command (pass/fail signals).

### 0B) Runtime environment contract (mandatory)

- [x] Add explicit env var contract for traceability commands.
  - [x] Define `OPENCODE_CONFIG_DIR` requirement with example export command.
  - [x] Define `SPHINX_MIGRATION_RUN_ROOT` requirement with example export command.
  - [x] Define minimal command set that requires env vars (`trace-validate`, `trace-report`, `verify`).
  - [x] Define command set that can run without run-root env var (`validate`, `build`, `--help`).
- [x] Add a verification checklist to confirm env vars are set in new sessions.

### 1) Baseline + FLS cross-check

- [x] Reconfirm FLS `make.py` invocation model (shebang, default behavior, dependency expectations).
  - [x] Confirm FLS launcher uses uv shebang (`#!/usr/bin/env -S uv run`).
  - [x] Confirm FLS documentation expects direct `./make.py` execution.
- [x] Investigate FLS Python style/lint checks and config baseline.
  - [x] Confirm FLS CI runs `uvx black . --check --diff --color`.
  - [x] Confirm FLS CI runs `uvx flake8 . --exclude .venv`.
  - [x] Confirm FLS `.flake8` Black compatibility settings (`max-line-length = 88`, `extend-ignore = E203`).
- [x] Capture current local failure path for `./make.py`, `./make.py --help`, and `./make.py validate` with command transcript artifacts.
- [x] Document compatibility constraints from current migration contract (`validate/build/trace-validate/trace-report/verify`).

### 2) make.py runtime alignment

- [x] Switch `make.py` to FLS-compatible launcher behavior (`uv`-managed direct invocation).
  - [x] Update shebang to uv launcher style.
  - [x] Preserve executable direct-run behavior from repository root.
- [x] Remove top-level import hard-fail path for third-party modules before command dispatch.
- [x] Ensure `./make.py` with no args executes a sensible default build flow (FLS-style behavior).
- [x] Preserve explicit command entrypoints used by migration (`validate`, `build`, `trace-validate`, `trace-report`, `verify`, `migrate-sphinx`).

### 3) Compatibility validation

- [x] Validate direct invocation succeeds from a clean shell: `./make.py --help`.
- [x] Validate default direct invocation succeeds: `./make.py`.
- [x] Validate direct subcommand invocation succeeds: `./make.py validate`.
- [x] Validate strict traceability gate via direct invocation: `./make.py trace-validate` (with required env vars set).
- [x] Validate existing contract still works: `uv run python make.py verify`.
- [x] Validate no-global-deps assumption using direct launcher behavior.
  - [x] Run direct invocation in an environment where system Python lacks project deps.
  - [x] Confirm `./make.py` still resolves project deps via uv-managed execution path.
  - [x] Capture transcript proving `ModuleNotFoundError` is eliminated.

### 4) Python style/lint parity (FLS-aligned)

- [x] Add `.flake8` with FLS-compatible Black settings.
  - [x] Set `max-line-length = 88`.
  - [x] Set `extend-ignore = E203`.
- [x] Add CI checks equivalent to FLS Python quality gate.
  - [x] Add `uvx black . --check --diff --color` step.
  - [x] Add `uvx flake8 . --exclude .venv` step.
- [x] Add/verify CI workflow file details for this repository.
  - [x] Create/update `.github/workflows/ci.yml` (or documented equivalent path).
  - [x] Ensure triggers include at least `pull_request`.
  - [x] Ensure uv setup is present before Black/Flake8 steps.
  - [x] Ensure CI fails on formatting/lint violations.
- [x] Document local developer commands for Black + Flake8 parity checks.
- [x] Decide and record whether lint checks remain CI-only (strict FLS parity) or are also exposed in `make.py`.
- [x] Run local parity verification and capture artifacts.
  - [x] `uvx black . --check --diff --color`
  - [x] `uvx flake8 . --exclude .venv`

### 5) Documentation and operator guidance

- [x] Update repository README usage to explicitly support direct `./make.py` execution.
- [x] Keep `uv run python make.py ...` examples as supported/explicit fallback path.
- [x] Add a short troubleshooting note for missing `uv` installation or PATH issues.
- [x] Add troubleshooting entries for common direct-run failure modes.
  - [x] `ModuleNotFoundError` on `./make.py`.
  - [x] `env: uv: No such file or directory`.
  - [x] `permission denied` for `./make.py`.
  - [x] missing required trace env vars for strict trace commands.
- [x] Add style/lint section covering local Black/Flake8 checks and CI enforcement.

### 6) Failure-handling matrix (mandatory)

- [x] Add a compact failure-handling matrix with deterministic fallback actions.
  - [x] Missing uv executable -> install path + rerun commands.
  - [x] Direct launcher unavailable -> use `uv run python make.py ...` fallback.
  - [x] Missing env vars -> export contract vars + rerun strict commands.
  - [x] CI lint failure -> local reproduction commands + remediation loop.
  - [x] Unexpected dependency resolution failure -> `uv sync` + lockfile check.

### 7) Evidence artifact map (mandatory)

- [x] Define exact artifact paths for before/after transcripts.
  - [x] `artifacts/validation/makepy-direct-help.before.log`
  - [x] `artifacts/validation/makepy-direct-help.after.log`
  - [x] `artifacts/validation/makepy-direct-default.after.log`
  - [x] `artifacts/validation/makepy-direct-validate.after.log`
  - [x] `artifacts/validation/makepy-uv-fallback.after.log`
- [x] Define exact artifact paths for style/lint evidence.
  - [x] `artifacts/validation/python-black-check.log`
  - [x] `artifacts/validation/python-flake8-check.log`
  - [x] `artifacts/validation/python-style-lint-summary.json`

### 8) Closeout

- [x] Record before/after command transcripts in run artifacts.
- [x] Record assumptions and deviations (if any) in run summary.
- [x] Confirm no regressions in traceability output generation.

## Acceptance criteria

- [x] `./make.py` no longer fails with `ModuleNotFoundError` in normal operator workflow.
- [x] Direct and explicit (`uv run ...`) invocation paths both pass strict validation gates.
- [x] Command behavior is aligned with FLS operator expectations and documented in-repo.
- [x] Black + Flake8 checks are enforced with FLS-equivalent configuration and CI steps.
- [x] New-session operators can run the documented preflight successfully without hidden setup steps.
- [x] Required env var contract is documented, validated, and sufficient for strict trace commands.
- [x] Evidence artifacts exist at the exact mapped paths for runtime and style/lint parity validation.
