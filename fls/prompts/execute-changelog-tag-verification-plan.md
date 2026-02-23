Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/changelog-tag-verification-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Branch: `changelog-automation-mainline`
- This plan has an explicit reporting exception: write verification artifacts under `build/`.
- Use `--report-dir` and default to `build/changelog-tag-verification`.

Requirements:
1. Run the Session bootstrap checklist first and report pass/fail per item.
2. Implement all planned verifier assets, fixtures, and schemas.
3. Implement verifier modes: `compare`, `extract`, `e2e`, `all`.
4. Enforce required and forbidden tags for all best-practice, synthetic, and no-change control cases.
5. Use targeted extraction assertions only (no full JSON snapshot equality).
6. Integrate CI per plan:
   - PR-gating: `compare` + `extract`
   - Nightly/manual non-gating: `e2e`
   - Upload `build/changelog-tag-verification/*` artifacts.
7. Make commits in logical chunks (Conventional Commits). Do not push unless requested.

Finish by returning:
- Checklist completion status by section.
- Summary of command results.
- Exact artifact paths under `build/changelog-tag-verification`.
- Any failures with missing/extra tags and proposed fix locations in `tools/changelog_assistant.py`.
