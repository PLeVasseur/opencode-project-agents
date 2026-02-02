---
name: fls-issue-triage
description: Triage FLS issues and implement spec updates from linked Rust changes.
compatibility: opencode
---

## What I do

- Gather issue details and linked PRs with `gh issue view` and `gh pr view`.
- Determine whether the change impacts FLS (language semantics, syntax, or glossary).
- Confirm the change applies to the Rust 2021 edition (exclude 2024+ edition-only rules unless explicitly backported).
- Identify any new terms introduced and define them in the glossary with `:dt:`; use `:t:` in prose thereafter.
- When justifying impact/no-change with spec passages, include verbatim excerpts with file paths and line numbers in the report.
- Map changes to `src/*.rst` sections using targeted searches.
- Apply spec updates and add new `:dp:` IDs from `./generate-random-ids.py`.
- Update `src/changelog.rst` with new/changed/removed `:p:` IDs and any syntax changes (`:s:`).
- Ensure changelog formatting: keep a blank line between each top-level item and the next entry.
- Build with `./make.py` and fix errors.
- Create a report in `$OPENCODE_CONFIG_DIR/reports/issue-<id>.md`.
- Generate grammar-driven validation snippets in `$OPENCODE_CONFIG_DIR/reports/issue-<id>/` and compile them with rustc.
- Record grammar derivations and rubric verification inside the snippet source files, with line-numbered evidence.
- Expand derivations to terminal tokens and cite spec line numbers for each grammar step.
- Sweep similar FLS sections to align structure, wording, and roles with established patterns.
- Align updates with the Rust Reference where applicable and document any deviations with rationale.
- Prefer normative language; avoid tutorial or implementation-detail notes unless they affect semantics.
- Include a Reference alignment section in the report and PR body with links and deviations.
- Use `:t:` for glossary-defined terms and `:s:` for grammar categories; mixing is expected when constraining syntax with semantics.
- Do not linewrap newly added or modified paragraphs in FLS `.rst` files; keep them single-line.
- Avoid abbreviations in grammar category names unless they mirror Rust surface syntax or established standard acronyms.
- When adding numbered algorithms (`#.` lists), each step must start with its own `:dp:` ID.
- When behavior depends on implementation-level semantics below the Reference/FLS surface (e.g., const-eval interpreter behavior, pointer provenance, byte-level representation), add a `Non-normative references` section to the report and PR. Cite current, maintained sources (rustc-dev-guide, Miri) and explain why the behavior is non-normative.
- When a no-change decision relies on non-normative references, include short verbatim excerpts with section anchors and URLs to ground the rationale in the report and PR body.

## When to use me

- An FLS issue requests new content or a spec update tied to a Rust PR.
- You need a repeatable checklist for impact assessment and execution.

## Workflow

1. Read the issue and capture key links (Rust PR, reference PR, tracking issue).
2. Decide impact:
    - If no FLS impact, add a concise “No change” reason in `src/changelog.rst`.
    - If impact exists, identify relevant sections in `src/`.
    - Validate that any Reference-aligned content reflects the 2021 edition.
3. Implement changes in the spec with required roles and anchors.
4. Add `:dp:` IDs for all new paragraphs/list items; generate IDs via `./generate-random-ids.py`.
5. Record in `src/changelog.rst`:
   - New/changed/removed paragraph IDs (`:p:`).
   - Any syntax changes (`:s:`) or new section references (`:ref:`).
   - Leave a blank line between the last sub-bullet and the next top-level `-` item.
6. Build with `./make.py` (and optionally `./make.py --check-links`).
7. Create `$OPENCODE_CONFIG_DIR/reports/issue-<id>.md` with:
    - Impact assessment and rationale.
    - Short verbatim excerpts (with file paths and line numbers) for any cited FLS passages used to justify a “no change” decision.
   - Files changed, syntax changes, and `:p:` IDs.
   - Build status and validation results.
   - Pointers to the snippet files that contain grammar derivations and rubric verification.
   - Reference alignment: links to the Reference PR and relevant sections, plus deviations.
8. Grammar-driven validation (keep artifacts out of the repo):
   - Put Rust snippets in `$OPENCODE_CONFIG_DIR/reports/issue-<id>/`.
   - In each snippet file, add:
     - An argument index map (comma-separated positions) with line numbers.
     - Grammar derivations that map productions to snippet lines.
     - Full derivations down to terminal tokens, with spec line numbers.
     - Rubric verification that quotes the exact spec sentences being checked, with spec line numbers.
     - Evidence lists that cite code line numbers.
    - Install the needed toolchain with `rustup toolchain install <version>` if missing.
    - Compile positive and negative examples with `rustc +<version>` and record diagnostics.
9. Consistency sweep:
   - Scan related sections (same feature area or similar constructs) for matching rubric structure.
   - Align terminology (`:t:`, `:s:`, `:c:`) and phrasing with nearby sections.
   - Prefer `:t:` for glossary terms and `:s:` for grammar categories in prose rules.
   - Ensure updated paragraphs in FLS `.rst` are single-line (no manual linewrap).
   - Use full words for grammar category names unless the abbreviation mirrors surface syntax (e.g., `cfg_attr`, `asm`) or an established acronym (e.g., ABI, ASCII).
   - Note any deviations or follow-up items in the report.
10. Reference alignment:
    - Compare against the Rust Reference section(s) and linked reference PRs.
    - Mirror structure and rigor where appropriate; record deviations and why.
    - Add a short Reference alignment section to the PR body with links.

## References

- `src/`
- `src/changelog.rst`
- `./generate-random-ids.py`
- `./make.py`
- `exts/ferrocene_spec/README.rst`
