Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-stacked-dedup-anchor-validation-plan.md`

Context:
- Base repo: `/home/pete.levasseur/project/fls`
- Build a fresh stacked worktree/branch from `origin/system-abi-variadic`.
- The stack must include:
  - Dedup base commit: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
  - Anchor logic commit for `tools/changelog_assistant.py` (resolve or create if missing)
- Canonical upstream URL under validation:
  - `https://github.com/rust-lang/rust/pull/145954`
- Artifacts must be written under `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run bootstrap and create timestamped `REPORT_ROOT`.
2. Create a clean stacked worktree from `origin/system-abi-variadic`.
3. Resolve anchor-logic commit SHA (create commit from `tools/changelog_assistant.py` only if not already committed), then cherry-pick dedup + anchor commits in order.
4. Validate readiness (duplicate-ID zero state + changelog assistant anchor flags/metadata present).
5. Run pre-check/update/update-second/post-check exactly as described in the plan with explicit `BASE_REF`.
6. Capture all stdout/stderr/exit codes and produce anchor evidence (`before`, `after first`, `after second`) with expected canonical count `1`.
7. Write final report to `$REPORT_ROOT/summary.md` with acceptance-criteria pass/fail.

Finish by returning:
- Checklist completion status by section.
- Stacked commit manifest (`dedup_sha`, `anchor_sha`, `head_sha`).
- Command summary with exit codes.
- Exact artifact paths under `$REPORT_ROOT`.
- Exact worktree path and active branch.
- Readiness-check outcome and pre-check vs post-check results.
- Anchor behavior verdict for canonical URL (`replace` expected).
- Remediation suggestions for any failed acceptance criteria.
