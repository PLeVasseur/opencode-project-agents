# Glossary migration review plan (pattern identification)

## Goals
- Identify questionable patterns in migrated glossary directives (no fixes yet).
- Produce a reproducible list of findings with concrete examples.

## Scope
- Focus only on identifying problematic patterns.
- A separate plan will handle term-by-term quality review and fixes.

## Inputs
- Repo: `/home/pete.levasseur/project/fls`
- Migration plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration-phase2.md`
- Static glossary: `src/glossary.static.rst.inc`
- Generated glossary: `build/generated.glossary.rst`
- Directives: `.. glossary-entry::` in `src/*.rst`

## Pre-flight
- Confirm the repo is clean: `git -C /home/pete.levasseur/project/fls status -sb`.
- Record the latest glossary migration commit hash.
- Record the full list of glossary migration commits and total count.
- Record the commit range to audit (first migration commit through latest) and confirm it spans multiple commits.
- Optional sanity check: confirm checklist and term-map timestamps are not newer than the latest migration commit.

## Deliberate review rules (mandatory, no shortcuts)
- Do not reuse previous-session findings or assumptions; verify everything in the current checkout.
- Use scripts only for inventory and sampling; validate each finding manually.
- For every sampled directive, review 10 lines of context before and after.
- Confirm verbatim comparisons directly against `src/glossary.static.rst.inc` and the pre-migration chapter text.
- If a potential issue cannot be confirmed by direct inspection, do not list it.

## Sampling requirements (mandatory)
- Review at least 2 dual-block directives per migration commit (both `:glossary:` and `:chapter:`), when available.
- Review at least 2 glossary-only directives per migration commit (`:glossary:` only), when available.
- Selection must be deterministic: within each commit/category, sort by file path + line number and take the first 2 (or all if fewer).
- After per-commit sampling, top up to at least `2 × commit_count` directives in each category using remaining directives sorted by file path + line number.

## Data collection
1) Build a directive inventory from `src/*.rst`.
   - Record: term, file, line, indent level, has_glossary, has_chapter, introduced-in commit.
   - Flag indented directives (indent > 0) for list-nesting review.
2) Split into categories:
   - Dual-block list (has `:glossary:` and `:chapter:`).
   - Glossary-only list (has `:glossary:` only).
3) Capture context for sampled entries:
   - 10 lines before and after each directive for manual inspection.

## Pattern checks (apply to each sampled directive)
1) Block structure
   - `:glossary:` block exists and is non-empty.
   - Dual-block entries also include a non-empty `:chapter:` block.
   - `:glossary:` starts with the expected `:dp:` line.
2) Indentation and list nesting
   - If the directive is inside a list item, check whether the `:chapter:` block
     includes its own list bullets (`*` / `-`). Flag likely double-list nesting.
   - Ensure indentation is consistent with surrounding list or rubric structure.
3) Glossary-only placement (priority concern)
   - Confirm the directive is placed near the most relevant section.
   - Flag glossary-only blocks that appear inside other directives, code blocks,
     syntax blocks, or unrelated list contexts.
4) Verbatim copying
   - Compare `:glossary:` block text to the static glossary entry (exact text).
   - For dual-block entries, compare `:chapter:` block to the original chapter
     definition (no rewrap, no wording changes).
5) Cross-reference sanity
   - If the static glossary includes `See :s:`, ensure it appears in `:glossary:`.
   - Ensure `:chapter:` uses the original `:t:`/`:dt:` markup from the chapter.
6) Duplicate or missing directives
   - Flag duplicate directives for the same term.
   - Flag directives whose terms do not exist in the static glossary.

## Reporting
- Write the report to: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-migration-patterns.md`.
- Format: Markdown with issue-first structure.
  - Start with **Issues** section (priority-ordered list of pattern types).
  - For each issue, include an **Examples** block with 3+ entries formatted as:
    - `term` — `path:line` — category — short description
  - Add a **Counts** section at the end (totals and sample sizes).
- The report should emphasize issues: lead with the problem, then evidence, then counts.
- Include metadata at the top of the report: audit date, commit range, and commit count.
- Include per-commit sample coverage totals (dual/glossary-only counts and any commits missing a category).

## Exit criteria
- Sampled 2 dual-block and 2 glossary-only directives per migration commit (when available).
- Met the `2 × commit_count` minimum for each category after top-up.
- Findings report completed with actionable examples.
