# Phase1 v2 remediation summary

- Run directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T173959Z-v2-phase1`
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Branch: `glossary-step-1-main-text-coverage`
- Execution boundary: completed Wave A and Wave B; stopped at Gate B+ boundary.

## Policy decisions and exceptions

- Conceptual-home-first policy frozen in `reports/policy-decisions-v2.md`.
- Analyzer destinations treated as non-binding diagnostic input.
- Missing-term closure accepted: `crate import` -> `[crate import]s`, `declaration` -> `[declaration]s`.
- Explicit Wave B exceptions recorded: 3 term(s) with `final_quality=resolved-exception`.

## Wave outcomes

- Wave A: 15 terms completed (`WA-001`..`WA-015`); validator progress pass; strict/build/link pass.
- Wave A evidence commit range: `e36e04ac1815930f9dbabd6de3f8c0bcc1a55d7e` .. `26e6f487a9270d75b1ff58d17e6bf82f81f89405` (8 commits).
- Wave B: 89 terms completed (`WB-001`..`WB-089`); validator gate pass; strict/build/link pass.
- Wave B evidence commit range: `e36e04ac1815930f9dbabd6de3f8c0bcc1a55d7e` .. `19e75856eac5694e5d613c7c59b429848d333992` (11 commits).

## Before/after counts

- Placement priorities (input v2): high=49, medium=49, low_forward_ref=48, none=630.
- Scoped remediation universe (Wave A+B): total=104, resolved-high=101, resolved-exception=3, pending=0.
- Divergence summary snapshot (input v2): {"chapter_only": 185, "chapter_redirect": 1, "cosmetic": 50, "exact_match": 461, "extended": 27, "glossary_xref": 24, "inline_definition": 7, "missing_from_chapter": 2, "moderate_divergence": 44, "significant_reword": 160}.
- Divergence reliability snapshot (input v2): {"high": 535, "low": 160, "medium": 79, "missing": 2, "new_term": 185}.

## Unresolved terms

- `WB-007` `undefined behavior` -> `resolved-exception` (`No prior remediation row; retained as explicit Wave B exception`).
- `WB-083` `qualifying trait` -> `resolved-exception` (`No prior remediation row; retained as explicit Wave B exception`).
- `WB-089` `base initializer` -> `resolved-exception` (`No prior remediation row; retained as explicit Wave B exception`).

## Commit manifest by batch

- Manifest rows: 19 (`batches/commit-manifest.csv`).
- Distinct evidence commits: 11.

## Gate B+ decision

- Gate B+ status: `blocked-missing-v3`.
- Blocker: external v3 artifacts absent; no internal regeneration path used.
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T173959Z-v2-phase1/inputs/v3/fls-pr6-updated-analysis-v3.md`
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T173959Z-v2-phase1/inputs/v3/fls-pr6-placement-fitness-v3.json`
- Missing: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T173959Z-v2-phase1/inputs/v3/fls-pr6-definition-divergence-v3.json`
- v2-v3 delta and C/D scope freeze deferred until artifacts are provided.

## Rewrite review summary

- action_type counts: {"move": 96, "retain": 8}
- semantic_change_flag counts: {"clarification-only": 3, "none": 101}
- reason_code counts: {"relocate-conceptual-owner": 15, "relocate-first-use-owner": 81, "retain-link-mitigated": 6, "retain-reordered": 2}
- Rows with rewrite action_type: 0.
