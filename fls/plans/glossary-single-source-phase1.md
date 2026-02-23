# Glossary Single-Source Plan (Phase 1 + Verification)

Purpose
- Establish a single source of truth for definitions in chapters while keeping the generated glossary and HTML output byte-for-byte identical in Phase 1.
- Provide a clear path to migrate aliases/redirects and extended definitions without losing traceability.

Goals
- Chapter text is canonical for definitions.
- Glossary can be fully generated from chapters (after migration), while `src/glossary.rst` becomes a wrapper and `src/glossary.static.rst.inc` keeps the committed glossary content.
- Phase 1 keeps HTML output identical (or as close as possible) via strict reuse of existing anchors, IDs, and alias/redirect formatting.
- Add a verification script in `$OPENCODE_CONFIG_DIR` that detects any HTML drift.

Execution checklist (use for implementation tracking)
- [x] Create a feature branch (no direct commits on main).
- [x] Add directive + parser changes for `.. glossary-entry::`.
- [x] Implement glossary generator to write `build/generated.glossary.rst`.
- [x] Ensure the generator runs before every build so `build/generated.glossary.rst` exists.
- [x] Update `src/glossary.rst` to use `.. glossary-include::` with `:tag:` gating and `:start-after:` to skip metadata lines.
- [x] Add `src/glossary.rst` wrapper and move current content to `src/glossary.static.rst.inc`.
- [x] Add `./make.py --use-generated-glossary` build tag support.
- [x] Rename `src/glossary.static.rst` to `src/glossary.static.rst.inc` and update references (non-source suffix).
- [x] Add CI check to diff `build/generated.glossary.rst` vs `src/glossary.static.rst.inc`.
- [x] Add HTML verification script under `$OPENCODE_CONFIG_DIR`.
- [x] Update the HTML verification script to normalize `paragraph-ids.json` and ignore `.buildinfo` tag hashes.
- [x] Run the HTML diff script and review the report.
- [ ] Commit in logical stages with Conventional Commits.
- [ ] Push feature branch to origin at logical checkpoints.

Non-goals (Phase 1)
- Do not enforce a single `:dt:` occurrence per term yet.
- Do not refactor existing glossary formatting or move alias/redirect logic into metadata unless needed.

Observed glossary patterns that must be preserved
- Alias entries (24 total) use `For :dt:` and must keep line-wrapping and odd cases:
  - Line-wrapped alias: `multiplication assignment`.
  - Self-target alias: `subtraction assignment` -> `subtraction assignment`.
  - Bracketed target: `unsafe Rust` -> `[unsafe operation]s`.
- Redirect entries (5 total) use `See :t:` with no `:dt:`.
- Many entries include `See :s:` lines.

Directive syntax (Phase 1)
Use a new directive to encapsulate canonical text and optional glossary text.

```
.. glossary-entry:: <Term>
   :kind: term|code|syntax
   :propagate: false|true

   :glossary:
     <glossary-only text, optional>

   :chapter:
     <chapter definition block, optional>
```

Rules
- If `:glossary:` is present, export to glossary using that block.
- If `:chapter:` is present but `:glossary:` is missing, export to glossary only when `:propagate: true`.
- If `:chapter:` is present and `:propagate: false` (default), chapter-only definition (no glossary export).
- If `:chapter:` is missing, `:glossary:` must be present (glossary-only entry).
- Phase 1 does not require `:aliases:` or `:redirects:`. Those stay verbatim in `src/glossary.rst` until migration.

Rationale for this shape
- Keeps existing glossary entries intact by allowing glossary-only blocks.
- Supports chapter-only definitions without forcing glossary growth.
- Allows dual definitions when the glossary must remain brief but the chapter is extended.

Glossary file layout (Phase 1)
- `src/glossary.rst` becomes a wrapper that conditionally includes either the static or generated glossary.
- `src/glossary.static.rst.inc` contains the current committed glossary content (non-source suffix).
- `build/generated.glossary.rst` is generated from directives for debugging and comparison.

Sphinx build switch
- Use `.. glossary-include::` (tag-aware include directive) with build tags to switch between static and generated glossary.
- Wrapper content (conceptual):
  - `.. glossary-include:: ../build/generated.glossary.rst` with `:tag: use_generated_glossary`.
  - `.. glossary-include:: glossary.static.rst.inc` with `:tag: not use_generated_glossary`.
- Build tag enabled via `sphinx-build -t use_generated_glossary` (exposed by `./make.py --use-generated-glossary`).
- The wrapper uses standard `.. include::` so section titles remain at the document level.
- Ensure `build/generated.glossary.rst` exists before any Sphinx build to avoid include errors.

Phase 1 generation strategy (hybrid output)
- Parse all `.. glossary-entry::` directives across chapter files.
- Read the existing `src/glossary.static.rst.inc` and capture:
  - section anchors and headings
  - per-entry `:dp:` IDs
  - alias/redirect entries (verbatim text blocks)
- Generate `build/generated.glossary.rst` that:
  - preserves ordering and headings
  - reuses existing `:dp:` IDs and anchors for matching entries
  - splices verbatim alias/redirect entries for any not yet migrated
  - uses `:glossary:` blocks when present; otherwise uses `:chapter:` only if `:propagate: true`
- Emit `:dt:` in glossary output exactly as present in the block (Phase 1 preserves current behavior).

HTML identity strategy
- Reuse existing glossary anchors and `:dp:` IDs.
- Preserve alias/redirect entries verbatim (including line wrapping) until migrated.
- Avoid changes to glossary ordering and section titles.
- Avoid removing duplicate `:dt:` in chapters during Phase 1.

Verification script (required)
- Location: `$OPENCODE_CONFIG_DIR/verify-html-diff.py` (or similar).
- Output reports under `$OPENCODE_CONFIG_DIR/reports/`.
- Steps:
  1) Build baseline HTML (static glossary): `./make.py --clear` and copy `build/html` to `$OPENCODE_CONFIG_DIR/reports/html-baseline/`.
  2) Regenerate `build/generated.glossary.rst` from chapters.
  3) Build HTML with generated glossary (enable `use_generated_glossary` tag, e.g., `./make.py --use-generated-glossary --clear`) and copy `build/html` to `$OPENCODE_CONFIG_DIR/reports/html-generated/`.
  4) Diff the two trees; write a summary report with changed files to `$OPENCODE_CONFIG_DIR/reports/html-diff.txt`.
- Success criteria: no diffs or only expected diffs (explicitly enumerated).

CI guardrails (Phase 1)
- Add a check that diffs `build/generated.glossary.rst` against `src/glossary.static.rst.inc` and fails on mismatch.
- Provide a manual script/step to overwrite `src/glossary.static.rst.inc` with the generated file when explicitly desired.

Branching, commits, and pushes
- Create a new feature branch before any code changes.
- Use Conventional Commits for messages: `type(scope?): subject`.
- Suggested commit stages:
  - Commit 1: add directive/parsing support (no wrapper changes yet).
  - Commit 2: generator outputs `build/generated.glossary.rst`.
  - Commit 3: wrapper swap (`src/glossary.rst` + `src/glossary.static.rst.inc`) and build tag support.
  - Commit 4: CI diff check + verification script.
- Push the feature branch to origin after each logical stage (or at least after wrapper + generator are in place).

Example entries (Phase 1)

Glossary-only alias (ABI)
```
.. glossary-entry:: ABI
   :kind: term

   :glossary:
     For :dt:`ABI`, see :t:`Application Binary Interface`.
```

Glossary-only redirect (assignment)
```
.. glossary-entry:: assignment
   :kind: term

   :glossary:
     See :t:`assignment expression`.
```

Dual entry (macro) with extended chapter and brief glossary
```
.. glossary-entry:: macro
   :kind: term

   :glossary:
     A :dt:`macro` is a custom definition that extends Rust by defining callable
     syntactic transformations.

   :chapter:
     A :t:`macro` is a custom definition that extends Rust by defining callable
     syntactic transformations. The effects of a :t:`macro` are realized through
     :t:`[macro invocation]s` or :t:`attribute` use. :t:`[Macro]s` come in two
     distinct forms:

     * :t:`[Declarative macro]s` define rules for recognizing syntactic patterns and
       generating direct syntax.

     * :t:`[Procedural macro]s` define augmented :t:`[function]s` that operate on and
       return a stream of :t:`[lexical element]s`.
```

Chapter-only definition (scope)
```
.. glossary-entry:: scope
   :kind: term
   :propagate: false

   :chapter:
     A :dt:`scope` is a region of program text where an :t:`entity` can be referred
     to. An :t:`entity` is :t:`in scope` when it can be referred to.
```

Phase 2 (migration and cleanup)
- Add `:aliases:` and `:redirects:` metadata to generate glossary-only entries.
  - `:aliases:` generates `For :dt:` entries.
  - `:redirects:` generates `See :t:` entries (no `:dt:`).
  - Must preserve line wrapping and raw role text (for `[unsafe operation]s`).
- Migrate alias/redirect entries from glossary-only blocks into metadata.
- Add a lint that prevents duplicate `:dt:` for glossary-exported terms; consider auto-rewriting chapter `:dt:` to `:t:`.
- Decide whether `:glossary:` should accept summary-only blocks for terser glossary output (optional future change).

Open questions to resolve before implementation
- Should `:glossary:` be a flag for "export chapter" or require a block for glossary output? (Current plan allows a block; export-from-chapter uses `:propagate: true`.)
- How strict should Phase 1 be about missing `:chapter:` for glossary-exported entries?
- Whether to enforce any lint in Phase 1 beyond minimal structural checks.
