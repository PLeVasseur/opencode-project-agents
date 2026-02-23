Execute this implementation plan end-to-end:
`$OPENCODE_CONFIG_DIR/plans/reviewer-bot-artifact-handshake-reconcile-2026-02-10.md`

Execution rules:
- Treat the plan as the source of truth.
- Check off each checkbox immediately when completed (do not batch updates).
- If blocked, stop and log the blocker in the plan's "Blockers" section with timestamp.
- Run preflight exactly as specified, including branching from `upstream/main` (not stale local `main`).
- Implement the artifact handshake path exactly as specified:
  - first-hop uploads reconcile context artifact
  - second-hop downloads artifact from triggering run id
  - strict validation + fail-closed behavior on missing/invalid/mismatched context
- Include cleanup for obsolete PR `#399` fallback logic if superseded.
- Run quality gates with:
  - `uv run ruff check --fix`
  - `uv run pytest .github/reviewer-bot-tests`
- Use Conventional Commit message style and open the PR against upstream using:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`
- Do not merge to `main` yourself; when PR is ready, report back so maintainer can merge.
- After maintainer confirms merge, complete live validation using a collaborator approval event.

Final report must include:
- root cause
- code changes
- validation evidence
- cleanup performed from earlier PR `#399`
- remaining risks
- exact plan checkbox status
