Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-rebase-cherrypick-changelog-verification-plan.md`

Context:
- Base repo: `/home/pete.levasseur/project/fls`
- Assistant branch source: `changelog-assistant-upstream-pr-anchor`
- ABI branch base: `system-abi-variadic`
- Canonical upstream URL under validation:
  - `https://github.com/rust-lang/rust/pull/145954`
- Include assistant CI commit in the integration cherry-pick stack after functional commits.
- Write all run artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run bootstrap checklist and create a timestamped `REPORT_ROOT`.
2. Rebase/verify both source branches against current `origin/main` (explicitly record whether ABI rebase is a no-op).
3. Create a clean integration worktree/branch on ABI, then resolve and cherry-pick assistant commits in the plan-defined order.
4. Validate integration readiness (`--require-anchor` help flag + report metadata fields).
5. Compute `BASE_REF` via `git merge-base HEAD origin/main` and use that exact value for every assistant invocation.
6. Run full validation flow: `pre-check`, `update`, `update-second`, `post-check`; capture stdout/stderr + exit codes + report artifacts.
7. Prove canonical URL behavior is replacement (not append) with line/count evidence before/after/after-second.
8. Write final report to `$REPORT_ROOT/summary.md` with explicit acceptance-criteria pass/fail and remediation for any failures.

Finish by returning:
- Checklist completion status by section.
- Rebase outcomes (assistant + ABI) with pre/post SHAs and divergence notes.
- Integration stack manifest (base SHA, cherry-picked SHAs, final HEAD SHA).
- Command summary with exit codes.
- Exact artifact paths under `$REPORT_ROOT`.
- Exact integration worktree path and active branch.
- Anchor behavior verdict for canonical URL (`replace` expected).
- Pre-check vs post-check outcome and whether post-check exited `0`.
- Remediation suggestions for any failed acceptance criteria.
