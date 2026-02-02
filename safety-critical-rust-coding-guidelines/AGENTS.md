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

## Artifact Location (Default + Examples)

Default: working artifacts go under `$OPENCODE_CONFIG_DIR`. Repo changes are only for deliverables the user wants in the codebase.

Put in `$OPENCODE_CONFIG_DIR` (examples):
- plans, checklists, scratch notes, investigation logs
- PR triage notes, CI failure summaries
- stale branch fix writeups (for example, `$OPENCODE_CONFIG_DIR/stale/<PR>/...`)
- drafts or temporary analysis not meant to ship

Put in the repo (examples):
- code changes (src/, tests/, scripts/) needed to fix the task
- documentation updates the user asked to publish (README, docs/)
- config changes required to run, build, or test

If the user asks for a note, report, or summary without a location, default to `$OPENCODE_CONFIG_DIR`.
If they explicitly ask to add or update files in the repo, do so.
If it is ambiguous whether it should be shipped, ask.

## Skills

- Issue fix: `skills/issue-fix/SKILL.md`
- Batch issue fix: `skills/batch-issue-fix/SKILL.md`
- FLS spec lock audit: `skills/fls-audit/SKILL.md`
- Coding guideline review: `skills/coding-guideline-review/SKILL.md`
- Stale branch fix: `skills/stale-branch-fix/SKILL.md`
