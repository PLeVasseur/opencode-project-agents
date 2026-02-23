# Phase1 v2 remediation summary

- Run directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1`
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Branch: `glossary-step-1-main-text-coverage`
- Execution boundary: completed Wave A and Wave B; stopped at Gate B+ boundary.

## Supersession

- Prior invalid/aborted run kept immutable and superseded: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T173959Z-v2-phase1`.
- Supersession rationale recorded in `reports/supersession-note.md`.

## Policy decisions and exceptions

- Conceptual-home-first policy frozen in `reports/policy-decisions-v2.md`.
- Analyzer destinations treated as non-binding diagnostic input.
- Missing-term closure accepted: `crate import` -> `[crate import]s`, `declaration` -> `[declaration]s`.
- Wave B deterministic scope frozen in `waves/wave-b-terms.json` (high/medium priorities excluding Wave A).

## Wave outcomes

- Wave A: 15 terms completed (`WA-001`..`WA-015`); validator progress pass; strict fail (`missing_count=14`); build/link pass.
- Wave A evidence commit range: `19e75856eac5694e5d613c7c59b429848d333992` .. `52f1285682360265eb49061c6a00755cc6ae96c0` (1 commits).
- Wave B: 89 terms completed (`WB-001`..`WB-089`); validator gate pass; strict fail (`missing_count=100`); build/link pass.
- Wave B evidence commit range: `52f1285682360265eb49061c6a00755cc6ae96c0` .. `63bde8968e31742477e0f320d86212b9c5704da8` (5 commits).

## Execution integrity

- START_HEAD: `19e75856eac5694e5d613c7c59b429848d333992`
- WAVE_A_END_HEAD: `52f1285682360265eb49061c6a00755cc6ae96c0`
- END_HEAD: `63bde8968e31742477e0f320d86212b9c5704da8`
- new_commit_count: `6`
- execution integrity verdict: `pass`
- Integrity artifacts: `reports/execution-integrity.json`, `reports/execution-integrity.md`, `reports/execution-integrity-manual-check.json`.

## New commit hashes (this run)

- `63bde8968e31742477e0f320d86212b9c5704da8`
- `fc8154a8c03876b21857bf03ce7ac58a4e9453ca`
- `ec7ff962b15a64c525e21feca8051d926b6129ad`
- `af86b2d61bbb483d8dc37debb3a1286c4d3f5562`
- `53f3c47e640dd222e0fd0014bd327bc50c60d84f`
- `52f1285682360265eb49061c6a00755cc6ae96c0`

## Changed src files (START_HEAD..END_HEAD)

- `src/attributes.rst`
- `src/entities-and-resolution.rst`
- `src/expressions.rst`
- `src/general.rst`
- `src/generics.rst`
- `src/implementations.rst`
- `src/inline-assembly.rst`
- `src/macros.rst`
- `src/ownership-and-deconstruction.rst`
- `src/patterns.rst`
- `src/program-structure-and-compilation.rst`
- `src/statements.rst`
- `src/types-and-traits.rst`
- `src/unsafety.rst`
- `src/values.rst`

## Before/after counts

- Placement priorities (input v2): {"high": 49, "low_forward_ref": 48, "medium": 49, "none": 630}.
- Placement outcomes (Wave A+B ledger): {"resolved-high": 104} across 104 scoped terms.
- Divergence summary snapshot (input v2): {"chapter_only": 185, "chapter_redirect": 1, "cosmetic": 50, "exact_match": 461, "extended": 27, "glossary_xref": 24, "inline_definition": 7, "missing_from_chapter": 2, "moderate_divergence": 44, "significant_reword": 160}.
- Divergence reliability snapshot (input v2): {"high": 535, "low": 160, "medium": 79, "missing": 2, "new_term": 185}.
- Divergence after-counts from v3 are deferred because Gate B+ is blocked by missing external v3 artifacts.

## Unresolved terms

- None in scoped Wave A+B universe (all 104 rows completed).

## Commit manifest by batch

- Manifest rows: 6 (`batches/commit-manifest.csv`).
- Batch summaries: `batch-001-summary.json` .. `batch-006-summary.json`.
- Per-batch validator outputs: `batch-00x-validate-progress.json` and `batch-00x-validate-post-commit.json`.

## Gate B+ decision

- Gate B+ status: `blocked-missing-v3`.
- Blocker: external v3 artifacts absent; no internal regeneration path used.
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/v3/fls-pr6-updated-analysis-v3.md`
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/v3/fls-pr6-placement-fitness-v3.json`
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/v3/fls-pr6-definition-divergence-v3.json`
- v2-v3 delta and C/D scope freeze deferred until artifacts are provided (`reports/rescope-after-wave-b.md`).

## Rewrite review summary

- action_type counts: {"retain": 3, "retain+rewrite": 101}
- semantic_change_flag counts: {"clarification-only": 101, "none": 3}
- reason_code counts: {"no-change-not-mislocated": 3, "retain-link-mitigated": 101}
- Rows with rewrite action_type: 101.
