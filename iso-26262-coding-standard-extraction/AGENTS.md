# Project Instructions

When asked to confirm AGENTS, run `printenv OPENCODE_CONFIG_DIR` and reply `AGENTS loaded from <value>`. Do not search for AGENTS.md or use Python for this check.

## Overview

Describe the project purpose, architecture, and key conventions.

## Workflow

- Preferred commands for build/test/lint
- Base branch is `main` unless explicitly overridden
- Mainline-first workflow: for initial bootstrap and solo execution, commit directly to `main`
- Use small, phase-aligned Conventional Commits on `main` to preserve rollback points
- If branch/PR mode is explicitly requested later, use `type/phase-<n>-short-topic`
- Use Conventional Commits for commit messages
- Conventional Commit format is mandatory: `type(scope): short summary`
- Allowed commit types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`, `build`, `ci`
- Keep commits small, phase-oriented, and reversible (one concern per commit)
- Do not mix unrelated changes in one commit (for example, parser behavior and docs updates)
- Never commit licensed extracted artifacts from `.cache/`
- Prefer a sequence of incremental commits that map to execution phases
  - Example phase order: project bootstrap -> manifests/state -> DB schema -> ingest -> query -> validation -> docs/traceability
- Keep config-only planning artifacts in `$OPENCODE_CONFIG_DIR`; do not mirror AGENTS/plans files into the implementation repo unless explicitly requested

## Code Standards

- Language/version expectations
- Style or formatting rules
- Error handling or safety requirements

## Files to Know

- Important directories or entry points
- Docs or specs to consult
