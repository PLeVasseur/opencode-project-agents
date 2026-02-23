Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/glossary-pr6-feedback-remediation-execution-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Primary objective: remediate PR6/PR7 feedback with evidence, then restack downstream branches/PRs.
- Canonical worktree paths:
  - `/home/pete.levasseur/project/fls-wt/step1`
  - `/home/pete.levasseur/project/fls-wt/step2`
  - `/home/pete.levasseur/project/fls-wt/step3`
  - `/home/pete.levasseur/project/fls-wt/step4`
  - `/home/pete.levasseur/project/fls-wt/step5`
- Canonical step branches:
  - `glossary-step-1-main-text-coverage`
  - `glossary-step-2-align-duplicate-text`
  - `glossary-step-3-dt-main-only`
  - `glossary-step-4-remove-see-paragraphs`
  - `glossary-step-5-generated-glossary-parity`
- Feedback bundle root:
  - `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/`
- Stacked PRs on fork:
  - `https://github.com/PLeVasseur/fls/pull/6`
  - `https://github.com/PLeVasseur/fls/pull/7`
  - `https://github.com/PLeVasseur/fls/pull/8`
  - `https://github.com/PLeVasseur/fls/pull/9`
  - `https://github.com/PLeVasseur/fls/pull/10`
- Hard constraints:
  - Preserve stacked ordering and branch ancestry.
  - Keep all generated artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
  - Use project entrypoints (`./make.py`, `./generate-glossary.py`) for build/parity flows.
  - Do not run `sphinx-build` / `sphinx-autobuild` directly.
  - Preserve unrelated user edits; do not reset/revert unrelated changes.

Execution requirements:
1. Run full **Fresh-session preflight** and **Bootstrap** from the plan; report pass/fail per item.
2. Use the plan's absolute path/branch variables for all git/worktree commands; do not rely on relative paths.
3. Create and print timestamped `REMEDIATION_DIR` exactly as defined in the plan.
4. Capture baseline reports and run **baseline reconciliation** against current step1/step2 heads.
5. If expected PRs (#6-#10) are missing or remapped, discover active PR IDs by step-branch head, persist `pr-stack-discovery.json`, and use discovered IDs for all updates/comments.
6. Execute Workstream A (policy gate + coverage-accounting tooling fix) and Workstream B (missing terms) on PR6/step1.
7. Enforce Gate G1 strictly: if it fails, stop and document blocker/remediation before any PR7 edits.
8. If Gate G1 passes, execute Workstream C and D on PR7/step2 (divergence adjudication + placement disposition).
9. Enforce Gate G2 strictly before push/restack.
10. Run validation matrix commands for PR6 and PR7 exactly as specified in the plan.
11. Restack step3-step5 using FF-only path first; if FF fails, apply the explicit fallback loop in the plan and document decisions.
12. Push updated branches, update PR6/PR7 bodies from generated body files, and post restack notes to PR8-PR10 (or discovered equivalent PRs).
13. Produce all required deliverables listed in the plan (including command logs, exit codes, reconciliation, policy decisions, and sync decisions).

Completion requirements:
- Do not skip failed checks; either fix and rerun, or stop with explicit blocker notes.
- Ensure all plan gates and exit criteria are satisfied or clearly marked blocked.

Finish by returning:
- Checklist completion by section/workstream.
- Gate outcomes (G1/G2) with pass/fail evidence.
- PR6 missing-term resolution status (`casting`, `namespace qualifier`, `shadowed`) with locations.
- PR7 divergence adjudication summary (counts by decision and unresolved items).
- Placement disposition summary (`relocate-now` / `keep-conceptual-home` / `forward-reference-only`).
- Restack and ancestry verification outcomes for step2->step5.
- Push and PR update results (expected PR6-PR10 or discovered replacements, with base/head confirmation).
- Exact artifact paths under `REMEDIATION_DIR`.
- Any blockers/deviations and proposed next actions.
