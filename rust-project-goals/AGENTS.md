# Project Instructions

## Overview

Describe the project purpose, architecture, and key conventions.

## Workflow

- Preferred commands for build/test/lint
- Branching or PR expectations

## Git Conventions

- Use Conventional Commits for commit messages (`feat:`, `fix:`, `docs:`, `chore:`).
- Create a new feature branch for each change.
- Do not amend commits unless explicitly requested.
- Open PRs with GitHub CLI, targeting the main repo explicitly:
  `gh pr create --repo rust-lang/rust-project-goals --base main --head PLeVasseur:<branch>`
- Keep PR content professional and plain: no emojis, no em dashes, no LLM-isms.

## Code Standards

- Language/version expectations
- Style or formatting rules
- Error handling or safety requirements

## Files to Know

- Important directories or entry points
- Docs or specs to consult
