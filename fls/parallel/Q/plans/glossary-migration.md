# Glossary Migration Plan

## Goal

Migrate all glossary-only definitions from origin/main into the correct
chapters, then generate the glossary from chapter definitions only, with
complete audit and verification.

## At a glance

- Open the migration checklist and the current letter audit file.
- Reconcile the letter against the legacy glossary snapshot.
- Migrate terms into chapters (upgrade/add `:dt:` definitions).
- Ensure each `:dt:` sentence is glossary-ready and self-contained.
- Update placement report, per-letter audit file, and migration checklist.
- Run `./make.py --check-generated-glossary`.
- Update the coverage report.
- Commit the letter checkpoint.

## Quick start (session kickoff)

- Confirm context in “Session context”; open the checklist + next letter audit file.
- Use “Workflow (per-letter steps)” as the canonical sequence for the letter.
- Apply “Placement rules” to choose the owning chapter for each term.
- Follow “Audit/report requirements” when updating the per-letter file and reports.
- Run the steps under “Testing plan” for the per-letter checkpoint.

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

- Last completed letter: O
- Next letter: P (start at the first unchecked term)
- Latest commit: 0261484
- Last validation: `./make.py --check-generated-glossary` with coverage report refreshed

## Non-negotiable constraints

- The glossary is generated from chapter definitions only.
- `src/glossary.rst` is a strict stub (only SPDX header, default-domain,
  informational-page, anchor, title, and spec-glossary directive).
- Do not introduce or keep `src/glossary-definitions.rst`.
- Never place glossary-only definitions into a generic catch-all chapter.
- Each definition paragraph must define exactly one term.
- Every `:dt:` definition sentence must be glossary-ready: it reads clearly in
  isolation without relying on nearby text (no "subject to the following",
  "as follows", "see below").
- Keep restrictions, lists, and examples in subsequent paragraphs; the `:dt:`
  sentence must stand alone as a complete statement.
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
   - If a definition would collide with an existing glossary entry, do a
     thorough sweep of nearby sections and similarly named terms to find an
     established phrase; if none fits, define a qualified term. The qualified
     term does not need to start with the same letter as the original entry.
   - Upgrade an existing `:t:` to `:dt:` or add a new `:dp:` paragraph.
   - Reuse the existing `:dp:` when upgrading; generate new `:dp:` IDs only
     when adding new definition paragraphs.
   - Verify the `:dt:` sentence reads in isolation; avoid forward-references
     such as "subject to the following", "as follows", or "see below".
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
  - Per-letter checklist must include (in order):
    reconcile letter, migrate terms, update placement report, update migration
    checklist, run `./make.py --check-generated-glossary`, update coverage
    report, commit checkpoint, mark letter complete.
  - Each term entry uses `## Term (term_id)` and a short bullet list:
    placement, action, rationale.
  - If a per-letter audit file is verbose/auto-generated, rewrite it in-place
    to the short format (no before/after excerpts), keeping only the per-letter
    checklist and the term entries.
  - Legacy letters may include earlier verbose excerpts; new/updated letters
    should use the short format.
- Regenerate coverage report:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-coverage-compare.md`.
  - Term IDs are derived from glossary section titles and normalized as:
    lowercase + non-alphanumeric -> `_`.
- Maintain migration checklist:
  `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md`.

## Coverage report recipe (python3)

Use `python3` (not `python`) to avoid missing aliases. Generate the report
content and replace `$OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-coverage-compare.md` with the output.

```bash
python3 - <<'PY'
import os
import re
from pathlib import Path


def extract_terms(path: Path):
    lines = path.read_text().splitlines()
    terms = []
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        underline = lines[i + 1].strip()
        if not line or line.startswith(".."):
            continue
        if underline and set(underline) == {"^"} and len(underline) >= len(line):
            terms.append(line)
    return terms


def norm(term: str) -> str:
    return re.sub(r"[^0-9a-zA-Z]+", "_", term.strip().lower()).strip("_")


config_dir = Path(os.environ["OPENCODE_CONFIG_DIR"])
origin = config_dir / "legacy/origin-main/src/glossary.rst"
generated = Path("/home/pete.levasseur/project/fls/build/glossary.generated.rst")

origin_terms = {norm(t) for t in extract_terms(origin)}
generated_terms = {norm(t) for t in extract_terms(generated)}

missing = sorted(origin_terms - generated_terms)
extra = sorted(generated_terms - origin_terms)

print(f"Origin/main glossary entries: {len(origin_terms)}")
print(f"Generated glossary entries: {len(generated_terms)}")
print(f"Missing entries: {len(missing)}")
print(f"Extra entries: {len(extra)}")
print()
print("## Missing entries")
print()
for term in missing:
    print(f"- {term}")
print()
print("## Extra entries")
print()
for term in extra:
    print(f"- {term}")
PY
```

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
- [x] M
- [x] N
- [x] O
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

## Backfill checklist

- [ ] A-L glossary-ready `:dt:` sweep complete

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
