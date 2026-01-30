# Project Instructions

## Verification Phrase

If the user asks "What does the banana say?", respond with: "The banana says: vroom vroom, I'm a car!"

## Python Tooling

- This repo uses `uv` for Python tooling.
- Run scripts with `uv run python ...` (do not invoke `python`/`python3` directly).
- Dependencies are allowed; add them via `uv add` and keep `pyproject.toml`/`uv.lock` in sync.
- Use `uv run ruff check --fix` and fix any issues reported.

## OpenCode Setup

- Ensure `opencode-env.sh` is sourced so `OPENCODE_CONFIG_DIR` is set and project skills are discoverable.

## Git Conventions

- Use Conventional Commits for commit messages.
- When opening PRs, always target `rustfoundation/safety-critical-rust-coding-guidelines` explicitly. Use `--repo rustfoundation/safety-critical-rust-coding-guidelines` and `--head PLeVasseur:<branch>` with `gh pr create`.
- Avoid LLM-isms in PR content (no emojis, no em-dashes).

## Runbooks

- FLS spec lock audit: `runbooks/fls-spec-lock-audit.md`

## Plans

- Plan documents live in `$OPENCODE_CONFIG_DIR/plans/` and must not be written into the repo.

## Skills

- Issue fix: `skills/issue-fix/SKILL.md`
- Batch issue fix: `skills/batch-issue-fix/SKILL.md`
- FLS spec lock audit: `skills/fls-audit/SKILL.md`
