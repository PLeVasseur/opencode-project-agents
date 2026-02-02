# Glossary Migration Plan

## Goal

Migrate all glossary-only definitions from origin/main into the correct
chapters, then generate the glossary from chapter definitions only, with
complete audit and verification.

## At a glance

- Open the migration checklist and the current letter audit file.
- Reconcile the letter against the legacy glossary snapshot.
- Migrate terms into chapters (upgrade/add `:dt:` definitions).
- Update placement report, per-letter audit file, and migration checklist.
- Run `./make.py --check-generated-glossary`.
- Update the coverage report.
- Commit the letter checkpoint.

## Session context

- Repo root: `/home/pete.levasseur/project/fls`
- OPENCODE_CONFIG_DIR: `/home/pete.levasseur/opencode-project-agents/fls`
- Plan: `$OPENCODE_CONFIG_DIR/plans/glossary-migration.md`
- Checklist: `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md`
- Per-letter audit file: `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/<LETTER>.md`
- Placement report: `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-only-placement.md`
- Coverage report: `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-coverage-compare.md`
- Legacy glossary: `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- Origin/main snapshot: `$OPENCODE_CONFIG_DIR/legacy/origin-main/src/glossary.rst`
- Generated glossary: `/home/pete.levasseur/project/fls/build/glossary.generated.rst`

Current progress:

- Last completed letter: L
- Next letter: M (start at the first unchecked term)
- Latest commit: 5d95464
- Last validation: `./make.py --check-generated-glossary` with coverage report refreshed

## Non-negotiable constraints

- The glossary is generated from chapter definitions only.
- `src/glossary.rst` is a strict stub (only SPDX header, default-domain,
  informational-page, anchor, title, and spec-glossary directive).
- Do not introduce or keep `src/glossary-definitions.rst`.
- Never place glossary-only definitions into a generic catch-all chapter.
- Each definition paragraph must define exactly one term.
- Temporary artifacts (including intermediate logs or analysis outputs) must be
  written under `$OPENCODE_CONFIG_DIR/` and never in the repo.
- Do not delete files outside the repo, including under `$OPENCODE_CONFIG_DIR/`,
  without explicit permission.

## Discipline

- Carefully comb through all usages of each term before deciding to upgrade an
  existing `:t:` to `:dt:` or add a new definition paragraph.
- Investigate and fix anomalies (unexpected usages, duplicate IDs, inconsistent
  references) before marking a term complete.

## Workflow (per-letter steps)

1) Reconcile the letter against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`.
2) For each term:
   - Review all usages across chapters.
   - Upgrade an existing `:t:` to `:dt:` or add a new `:dp:` paragraph.
   - Update `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-only-placement.md`.
   - Check off the term in `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md`.
3) Update the per-letter audit file:
   `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/<LETTER>.md`.
4) Run `./make.py --check-generated-glossary`.
5) Update `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-coverage-compare.md`.
6) Commit: `docs(glossary): checkpoint <LETTER> migration`.

## Placement rules

- Place each definition in the chapter/section that owns the normative semantics.
- If a term appears in multiple chapters, define it where the normative rules live.
- Avoid creating new top-level sections solely for glossary terms.

Preferred chapters by topic:

- Lexical/grammar/token concepts: `src/lexical-elements.rst`
- Expressions/semantics: `src/expressions.rst`
- Items: `src/items.rst`
- Types/traits/type system: `src/types-and-traits.rst`
- Patterns: `src/patterns.rst`
- Ownership/borrowing/drop: `src/ownership-and-deconstruction.rst`
- Program structure/compilation units: `src/program-structure-and-compilation.rst`
- Macros: `src/macros.rst`
- Unsafe/UB: `src/unsafety.rst` or `src/undefined-behavior.rst`
- Attributes: `src/attributes.rst`
- Concurrency: `src/concurrency.rst`
- FFI/extern/C: `src/ffi.rst`
- Inline assembly: `src/inline-assembly.rst`
- Errors/exceptions: `src/exceptions-and-errors.rst`
- Generics/impls: `src/generics.rst` or `src/implementations.rst`

## Audit/report requirements

- Update placement report:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-only-placement.md`
- Maintain per-letter audit files:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/A.md` .. `Z.md`,
  `0-9.md`, `symbols.md`.
  - Each file includes a per-letter checklist and a term checklist.
  - Each term entry uses `## Term (term_id)` and a short bullet list:
    placement, action, rationale.
  - Legacy letters may include earlier verbose excerpts; new/updated letters
    should use the short format.
- Regenerate coverage report:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-coverage-compare.md`.
  - Term IDs are derived from glossary section titles and normalized as:
    lowercase + non-alphanumeric -> `_`.
- Maintain migration checklist:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md`.

## Letter checklist

- [x] A
- [x] B
- [x] C
- [x] D
- [x] E
- [x] F
- [x] G
- [x] H
- [x] I
- [x] J
- [x] K
- [x] L
- [ ] M
- [ ] N
- [ ] O
- [ ] P
- [ ] Q
- [ ] R
- [ ] S
- [ ] T
- [ ] U
- [ ] V
- [ ] W
- [ ] X
- [ ] Y
- [ ] Z
- [ ] 0-9
- [ ] symbols

Note: 0-9 and symbols remain unchecked until explicitly migrated.

## Testing plan

- Per letter:
  - Run `./make.py --check-generated-glossary`.
  - Update the coverage report.
  - Commit the checkpoint.
- After all letters:
  - Run `./make.py --clear`.
  - Fix any build errors and re-run until clean.
  - Run `./make.py --check-generated-glossary` again.
  - Optional: `./make.py --check-links`.

## Completion criteria

- All terms checked in the migration checklist.
- All letters marked complete in the letter checklist.
- Per-letter checks run and coverage report refreshed.
- Reports consistent with chapter-only definitions.
