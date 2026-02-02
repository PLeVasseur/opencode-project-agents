# Plan: Triage FLS issues 646, 648, 649

## Shared workflow (per issue, per branch)
- Use the `fls-issue-triage` skill for each issue (`/home/pete.levasseur/opencode-project-agents/fls/skills/fls-issue-triage/SKILL.md`).
- Create a new branch from `main` for the issue (one branch per issue).
- Gather issue details with `gh issue view` and capture linked Rust PRs/Reference links.
- Decide impact and locate relevant FLS sections in `src/` using targeted searches.
- Update spec text in `src/*.rst` with required anchors and roles (`:t:`, `:s:`, `:c:`).
- Add `:dp:` IDs for all new paragraphs/list items via `./generate-random-ids.py`.
- Keep modified/new paragraphs single-line (no manual line wrapping).
- Update `src/changelog.rst` with new/changed `:p:` IDs and any `:s:` entries; keep a blank line between top-level items.
- Run `./make.py` (and `./make.py --check-links` if relevant) and fix errors.
- Create `$OPENCODE_CONFIG_DIR/reports/issue-<id>.md` with impact assessment, files changed, IDs, build status, and Reference alignment.
- Add grammar-validation snippets in `$OPENCODE_CONFIG_DIR/reports/issue-<id>/`, include derivations and rubric checks, and compile with `rustc` as needed.
- Consistency sweep: align structure/terminology with nearby sections; document any deviations in the report.

## Issue 646: system ABI C-style variadic declarations
- Issue URL: https://github.com/rust-lang/fls/issues/646
- Reference: rust-lang/rust PR 145954.
- Target areas: ABI chapter and function declaration/ABI sections covering `system` ABI and C-style variadics.
- Update spec wording to reflect stabilization and any constraints or syntax notes.

## Issue 648: const-eval pointer byte copying
- Issue URL: https://github.com/rust-lang/fls/issues/648
- Reference: rust-lang/rust PR 148259.
- Target areas: const evaluation rules around memory/pointer operations.
- Update semantics to allow byte-by-byte pointer copying during const-eval and note any limitations.

## Issue 649: LUB coercions and function item types/safety
- Issue URL: https://github.com/rust-lang/fls/issues/649
- Reference: rust-lang/rust PR 148602.
- Target areas: coercions (LUB), function item types, and safe/unsafe function type coercions.
- Update LUB coercion rules to cover function item types and differing safeties.

## Git and PR flow (per issue)
- Commit using Conventional Commits and a descriptive branch name.
- Push the branch to `origin` (fork) and open a PR there.
- Do not push upstream.
- PR body uses `## Summary`, `## Reference alignment`, `## Testing`; include `Closes #<issue>` as the last line in the Summary when applicable.
