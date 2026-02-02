# Glossary auto-generation from chapter definitions

## Goals

- Author term definitions once in chapters and generate the glossary at build time.
- Keep glossary paragraph IDs stable and deterministic with the fls_ prefix.
- Preserve existing FLS authoring conventions (paragraph IDs, section IDs, alphabetical glossary sections).
- Keep parallel builds enabled and fast.
- Provide a drop-in generated glossary artifact for debugging and validation.

## Non-goals

- Do not change reference role behavior (:t:, :s:, :c: still resolve to their canonical targets).
- Do not auto-fix content quality in this change beyond explicit migrations.

## Requirements and constraints

- src/glossary.rst must be a strict stub (only SPDX header, default-domain, informational-page, anchor, title, and spec-glossary directive). Any other content is a build error.
- Do not introduce or keep src/glossary-definitions.rst; definitions live in chapters only.
- Glossary output is generated from chapter definitions; there must be only one definition per term.
- Generated glossary content must not introduce :dt: definitions; chapter-defined terms appear as :t: in the glossary.
- Paragraph IDs for glossary entries must be deterministic and stable; IDs must remain fls_*.
- Parallel builds remain enabled (no forced -j1; extensions are parallel-safe).
- All reports must be written under $OPENCODE_CONFIG_DIR.
- Stub-only validation must not run during the generated-source build used by --check-generated-glossary.

## Repository state and checkpoints

- Preserve the current working tree; do not reset or drop unrelated changes.
- Before implementing the new plan, create a checkpoint commit on the working branch capturing the current state for traceability.
- Continue from the existing branch unless asked to start a new one.

## Sphinx best-practice references

- Build phases (why source-read runs before env is complete):
  https://www.sphinx-doc.org/en/master/extdev/index.html#build-phases
- Event callbacks API (source-read, doctree-resolved):
  https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html

## Design summary

### Glossary generation

- Keep glossary generation in a post-transform to avoid ordering dependencies and keep parallel builds safe.
- The post-transform replaces the spec-glossary marker with generated sections.
- For each term definition gathered from chapters (including :dt: and :dc:):
  - Clone the definition paragraph.
  - Replace any DefIdNode in the clone (:dt:, :ds:, :dc:) with DefRefNode (:t:, :s:, :c:) to avoid duplicate definitions.
  - Remove existing :dp: in the clone and insert a deterministic glossary :dp: ID.
  - Update DefRefNode.ref_source_doc to the glossary docname so references are resolved correctly.
- Sections are sorted case-insensitively and then by term id to satisfy alphabetical linting.
- Glossary entries defined only in the glossary (legacy) are not allowed; we will migrate them into chapters and keep the glossary stub-only.

### Deterministic glossary IDs

- Generate glossary paragraph IDs with base62 (string.ascii_letters + string.digits), length 12, fls_ prefix.
- Use sha256("glossary:" + term_id) to produce stable IDs.
- Use sha256("glossary-section:" + term_id) for section IDs.
- On collision, rehash with suffix ":2", ":3", ... until unique.
- IDs remain stable unless term_id changes. Use :dt:`Display <canonical>` to preserve term_id if display text changes.

### Strict glossary stub

- src/glossary.rst contains only:
  - SPDX header
  - .. default-domain:: spec
  - .. informational-page::
  - top anchor
  - Glossary title
  - .. spec-glossary::
- Add a lint that errors if any other content is present (comment lines are allowed between the title and spec-glossary).
- Add a lint that errors if any term is defined in multiple documents.

Lint details (stub-only check):

- Use the source-read event to validate the glossary content without direct file reads.
- Guard the stub-only check behind a config flag (e.g., spec_glossary_stub_only_check = True).
- The generated-source build in --check-generated-glossary sets this flag to False so the stub-only lint is skipped.
- Allow only:
  - SPDX header block
  - blank lines
  - .. default-domain:: spec
  - .. informational-page::
  - .. _fls_...: anchor line
  - Glossary title + underline
  - .. spec-glossary::
- comment lines (".. " with no directive "::")
- Any other non-blank content triggers raise_error, following existing lint patterns.

### Generated glossary artifact (debug-only)

- Emit build/glossary.generated.rst on every build.
- The file is drop-in ready and includes:
  - SPDX header
  - .. default-domain:: spec
  - .. informational-page::
  - top anchor
  - Glossary title
  - generated glossary entries (RST-like, role-preserving)
  - a short generated warning comment in front-matter
- This file is not read by default builds; it exists for debugging and validation.
- Do not include .. spec-glossary:: in this file (it must be a static, drop-in glossary source).

RST serialization algorithm (exacting):

- Emit the stub header lines exactly as in src/glossary.rst plus a generated comment.
- For each glossary entry section in the post-transform doctree:
  - Emit the section title line.
  - Emit the underline using ^ characters matching title length.
  - Emit each paragraph in order:
    - First line is :dp:`<paragraph_id>` from the paragraph DefIdNode.
    - Second line is the paragraph text serialized from inline nodes (single line, no wrapping, for deterministic diffs).
  - Insert a blank line between paragraphs and between sections.
- Inline serialization rules:
  - DefRefNode -> :t: / :s: / :c: depending on ref_kind, with explicit target if ref_text differs from ref_target.
  - DefIdNode should not appear (converted to DefRefNode earlier); if present, serialize using :d<role>:
  - emphasis -> *text*, strong -> **text**, literal -> ``text``.
  - reference nodes -> `text <url>`__.
  - default to node.astext() for unsupported inline nodes.
- Enforce ASCII output unless the source already contains Unicode.

### Nightly validation (byte-for-byte)

- Add a new ./make.py flag: --check-generated-glossary
- Behavior:
  1. Normal build (produces build/html and build/glossary.generated.rst).
  2. Second build uses source-read to replace glossary source with build/glossary.generated.rst and writes to build/html-generated (doctrees to build/doctrees-generated).
     - The stub-only lint is disabled for this build via the config flag.
  3. Compare build/html/glossary.html vs build/html-generated/glossary.html (byte-for-byte).
  4. Compare build/html/paragraph-ids.json vs build/html-generated/paragraph-ids.json (byte-for-byte).
  5. If differences exist, produce ANSI diff output using delta and write to:
     - build/glossary-compare/glossary.html.diff
     - build/glossary-compare/paragraph-ids.json.diff
- Debug artifacts must be stable so the diff can pass.

### Delta dependency

- Delta is a hard dependency for the nightly check only.
- Pin delta to the current latest release (0.18.2).
- Add a Python installer script (tools/install-delta.py) that:
  - Downloads the pinned release for the current OS/arch.
  - Installs it under ./.cache/delta/0.18.2/<platform>/
  - Exposes a stable path used by the nightly check.
  - Warns when the pinned version is >=2 releases behind latest.
  - Version check uses the GitHub releases API; if the check fails (offline, API error), log a warning and continue without failing the build.
- Read ~/.gitconfig to detect existing delta settings; if present, mirror them into a repo-local config (build/glossary-compare/delta.conf).
- The nightly check always runs delta with --config build/glossary-compare/delta.conf (do not rely on ~/.gitconfig directly).
- If ~/.gitconfig has no delta config, write a minimal deterministic config and use it.

### CI workflow

- Add a new workflow (e.g., .github/workflows/nightly.yml) that:
  - Installs delta via tools/install-delta.py.
  - Runs ./make.py --check-generated-glossary.
  - Uploads build/glossary-compare artifacts on failure.

## Reports and audit trail

All reports are written under $OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/.
Context-dependent glossary migrations are tracked under $OPENCODE_CONFIG_DIR/reports/glossary-auto-migration/.

### Report 1: Glossary-only definitions and placement

- Identify glossary-only definitions from main.
- For each, propose target chapter placement and rationale.
- Markdown file: glossary-only-placement.md

### Report 2: Glossary coverage comparison vs main

- Extract all glossary entries from origin/main (or local main).
- Extract all generated entries from current build (build/glossary.generated.rst).
- Compare and list any gaps.
- Markdown file: glossary-coverage-compare.md

### Report 3: Per-term before/after audit

- One Markdown file per letter: A.md .. Z.md, plus 0-9.md and symbols.md.
- Each term entry includes:
  - Term heading with display text and term id.
  - Before glossary entry (from origin/main:src/glossary.rst, full entry section).
  - After glossary entry (from build/glossary.generated.rst, full entry section).
  - Before chapter excerpt (2 :dp: paragraphs before/after in origin/main). If the definition did not exist in origin/main, show the same location context without the definition and note it explicitly.
  - After chapter excerpt (2 :dp: paragraphs before/after in current branch).
  - Role classification: which nodes were :dt: vs :dc: vs :ds: and why.
- Explanation of any text edits needed to make the definition stand-alone.

### Report 4: Context-dependent glossary definitions (manual review)

- Identify chapter definitions whose glossary entry is not a safe copy-paste due to surrounding context.
- Record these for manual rewrite instead of auto-migrating.
- Markdown file: $OPENCODE_CONFIG_DIR/reports/glossary-auto-migration/context-dependent-definitions.md
- Include: term id, docname + section, definition snippet, context note, and the reason it needs manual edit.

## Migration plan

1. Take a one-time snapshot of the legacy glossary source:
   - Copy src/glossary.rst to $OPENCODE_CONFIG_DIR/legacy/src/glossary.rst.
2. Take a baseline snapshot from origin/main:
   - Copy origin/main:src/glossary.rst to $OPENCODE_CONFIG_DIR/legacy/origin-main/src/glossary.rst.
3. Replace src/glossary.rst with the strict stub (errors if extra content remains).
4. Move glossary-only definitions into chapters, adjusting text to be standalone.
5. Update chapter definitions so they read well both in context and standalone.
6. Keep glossary output generated from chapters only.

Placement rules for migrating glossary-only definitions:

- Never place definitions in a generic catch-all chapter (for example, do not add glossary-only content to src/general.rst unless the term is genuinely about general spec structure and is referenced there).
- Place each term definition in the most specific chapter/section that owns the concept. Use existing term usage as the primary signal:
  - If a term is defined by a grammar or token concept, prefer src/lexical-elements.rst.
  - If a term is about expressions, prefer src/expressions.rst.
  - If a term is about items, prefer src/items.rst.
  - If a term is about types/traits or type system semantics, prefer src/types-and-traits.rst.
  - If a term is about patterns, prefer src/patterns.rst.
  - If a term is about ownership/borrowing/drop, prefer src/ownership-and-deconstruction.rst.
  - If a term is about program structure or compilation units, prefer src/program-structure-and-compilation.rst.
  - If a term is about macros, prefer src/macros.rst.
  - If a term is about unsafe/UB, prefer src/unsafety.rst or src/undefined-behavior.rst.
  - If a term is about attributes, prefer src/attributes.rst.
  - If a term is about concurrency, prefer src/concurrency.rst.
  - If a term is about FFI/extern/C, prefer src/ffi.rst.
  - If a term is about inline assembly, prefer src/inline-assembly.rst.
  - If a term is about errors/exceptions, prefer src/exceptions-and-errors.rst.
  - If a term is about generics or implementations, prefer src/generics.rst or src/implementations.rst.
- If the term appears in multiple chapters, place the definition where its normative semantics are specified and add cross-references elsewhere if needed.
- If a term is only mentioned in one chapter, place it adjacent to the first normative use of the term.
- Keep definitions close to the related section and avoid adding new top-level sections solely for glossary terms.
- Update $OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-only-placement.md to reflect the final per-term placements and rationales.

Placement verification for migrated definitions:

- The LLM must carefully comb through all usages of each migrated glossary-only term across chapters.
- The LLM must decide whether an existing :t: usage should be upgraded to :dt: (if it is already the normative definition), or whether a new definition paragraph must be added.
- The LLM must record the decision and rationale in $OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/glossary-only-placement.md.
- The LLM must investigate and fix any anomalies found during migration (unexpected term usages, duplicate IDs, inconsistent references) before marking migration complete.

Migration checklist:

- Create $OPENCODE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md with one checkbox per glossary term from origin/main.
- The migration checklist must include a top-level checkbox that can only be checked when every term checkbox is complete.
- The migration checklist is the authoritative execution order; iterate it top-to-bottom and complete each unchecked term before moving on.
- Definition of done for a term:
  - D-style audit entry completed (before/after glossary entries, chapter excerpts, role classification, standalone edits).
  - Chapter definition present in current source with exactly one :dt:/:ds:/:dc: for the term.
  - Generated glossary entry exists and matches the chapter definition.
- Do not infer completion from partial audits or other artifacts; only the checklist drives completion.

Per-letter checkpoints:

- After finishing each letter or symbol block, run `./make.py`.
- Commit and push the letter checkpoint.
- Check for missing items from the legacy glossary for that letter.
- As needed, add missing terms to the checklist and process them.

## Implementation steps (ordered)

- [x] Update glossary generation to enforce stub-only source and generate only from chapters.
- [x] Add lint for stub-only glossary (source-read) and duplicate term definitions (error patterns match existing lints).
- [x] Emit build/glossary.generated.rst (drop-in ready, role-preserving, no spec-glossary directive) using the RST serialization algorithm above.
- [x] Add make.py flag --check-generated-glossary (two builds + delta diff output, stub lint disabled in generated build).
- [x] Move glossary-only definitions into chapters and adjust text to stand alone.
- [x] Add tools/install-delta.py and pin delta 0.18.2 (include GitHub API version check and offline fallback warning).
- [x] Add new nightly CI workflow to install delta and run the check.
- [x] Remove any src/glossary-definitions.rst and drop it from src/index.rst (definitions remain in chapters only).
- [x] Update documentation (exts/ferrocene_spec/README.rst) to reflect strict stub-only glossary behavior.
- [x] Update .gitignore to ignore /.cache (delta install path).
- [x] Create reports directory under $OPENCODE_CONFIG_DIR and generate all audit reports, including context-dependent definitions.
- [x] Update AGENTS.md to require reports under $OPENCODE_CONFIG_DIR.
- [x] Create migration checklist with per-term checkboxes and ensure all are complete.

## Version control

- Create a feature branch before starting implementation.
- Create a checkpoint commit capturing the pre-plan-update state.
- Commit in logical chunks:
  1. Extension core changes (generation, stub enforcement, deterministic IDs).
  2. Lints and glossary stub enforcement.
  3. Generated glossary artifact + make.py nightly flag.
  4. Delta installer + nightly workflow.
  5. Documentation updates and reports.
- Push intermediate commits to origin after each logical chunk to keep progress synced.

## Testing plan

- [x] ./make.py --clear
- [x] Fix any build errors and re-run until the build passes cleanly.
- [ ] Validate glossary completeness:
  - [ ] After migration, compare original glossary entries from main against build/glossary.generated.rst.
  - [ ] Ensure all chapter-defined terms are present in the generated glossary.
- [ ] Nightly check (manual verification during implementation):
  - [ ] ./make.py --check-generated-glossary
  - [ ] Ensure byte-for-byte match for glossary.html and paragraph-ids.json.
  - [ ] Debug and remove non-determinism until the diff is clean.
- [ ] Optional: ./make.py --check-links

## Open questions

- None at this time.
