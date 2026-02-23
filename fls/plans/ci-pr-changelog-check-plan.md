# CI PR Changelog Check Plan

## Goal

Add PR-gating changelog coverage validation in CI using existing `tools/changelog_assistant.py --check`, without enabling `--require-tags`.

## Scope

- Update `.github/workflows/ci.yml` only.
- Gate PRs on changelog coverage check for actual branch diff.
- Reuse existing artifact directory under `build/changelog-tag-verification/pr`.

## Checklist

- [x] Add a CI step to fetch the PR base branch ref in the changelog verification job.
- [x] Add a CI step to run `tools/changelog_assistant.py --check` with explicit `--base origin/${{ github.base_ref }}` and `--emit-report`.
- [x] Keep the new changelog check PR-only and do not add `--require-tags`.
- [x] Ensure the existing artifact upload path still includes the assistant report outputs.
- [x] Run local command verification for the same assistant check flow.
- [x] Summarize results and confirm what is now PR-gated.
