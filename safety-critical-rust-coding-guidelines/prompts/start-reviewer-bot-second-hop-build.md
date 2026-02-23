Execute this implementation plan end-to-end:
`$OPENCODE_CONFIG_DIR/plans/reviewer-bot-second-hop-reconcile-2026-02-10.md`

Execution rules:
- Treat the plan as the source of truth.
- Check off each checkbox immediately when completed (do not batch updates).
- If blocked, stop and log the blocker in the plan's "Blockers" section with timestamp.
- Run preflight exactly as specified (git status, stash if needed, gh auth check, sync main, branch from synced main).
- For baseline evidence, use PR `#397` first; if stale/unavailable, choose the latest comparable fork PR with an `APPROVED` review and record it as `BASELINE_PR`.
- Implement the second-hop `workflow_run` reconcile path exactly as specified.
- Run quality gates with:
  - `uv run ruff check --fix`
  - `uv run pytest .github/reviewer-bot-tests`
- Use Conventional Commit message style and open the PR against upstream using:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`

Post-merge handoff behavior:
- Full `workflow_run` validation is post-merge because the workflow file must exist on default branch.
- At the handoff checkpoint after smoke PR setup, stop and tell the maintainer exactly: `ok, go approve`.
- After maintainer confirms approval was submitted, complete validation and report outcomes.

Final report must include:
- root cause
- code changes
- validation evidence
- remaining risks
- exact plan checkbox status
