# Rendered Output Layout and Source Co-location Plan (Worktree-First)

Date: 2026-02-16
Status: Draft execution plan
Priority: High
Plan type: Rendering quality, information architecture, and source-structure remediation

## 0) Locked decisions
- [x] Execute all implementation in a dedicated git worktree (no direct edits in the currently active repo folder).
- [x] Keep canonical traceability identifiers stable.
  - [x] Keep table IDs (`table-01` ... `table-26`) unchanged.
  - [x] Keep existing IRM and anchor behavior unchanged unless a break is explicitly required and documented.
- [x] Split rendered content by page using source-level page boundaries (not CSS-only hacks).
- [x] Split granularity is locked to top-level section pages only (no deeper subsection split in this pass).
- [x] Co-locate page content with the table files that belong to that page in source.
- [x] Co-location migration mode is locked to hard cutover in one pass (no temporary fallback pathing).
- [x] Widen layout and tables by default for desktop while preserving mobile readability.
- [x] Desktop width target is locked to moderate widening (not aggressive full-bleed).
- [x] Fix list formatting at the source so rendered HTML does not show literal bullet glyph paragraphs or escaped list text.
- [x] Preserve existing content semantics; this is a structure/layout remediation, not a standards-content rewrite.

## 0A) Required implementation base (new-session hard gate)
- [x] Required base branch for implementation: `docs/iso26262-sphinx-traceability-migration-20260214T184350Z`.
- [x] Required base pin: `ccd270723b62e4bcad5ec9d00d1a0abd07a80dfc`.
- [ ] New session must verify base ancestry before any edits.
  - [ ] `git merge-base --is-ancestor ccd270723b62e4bcad5ec9d00d1a0abd07a80dfc HEAD` returns success.
- [ ] New session must verify required Sphinx sources are tracked and present.
  - [ ] `docs/conf.py`
  - [ ] `exts/iso26262_spec/table_directive.py`
  - [ ] `exts/iso26262_spec_lints/legacy_token_check.py`
  - [ ] `exts/iso26262_spec_lints/native_table_check.py`
  - [ ] `exts/iso26262_spec_lints/paragraph_id_check.py`
  - [ ] `src/index.md`

## 1) Problem statement (current observed state)
- [ ] Output is effectively one long page (`build/html/iso26262_rust_mapping.html`) and is difficult to scan.
- [ ] Default theme width is constrained and tables are visually squished.
- [ ] Literal bullets and escaped ordered-list text render as plain paragraph text in multiple sections.
- [ ] Table files are globally centralized (`src/tables/`) instead of being grouped with the page content they support.
- [ ] Existing checks/scripts include top-level markdown assumptions and must be updated for multi-page source.

## 2) Objectives and acceptance criteria
- [ ] Rendered output is split into multiple pages with clear navigation and predictable section ownership.
  - [ ] `index` is a real entry page with toctree links to page files.
  - [ ] No single monolithic content page remains.
- [ ] Desktop layout and tables are widened by default.
  - [ ] Main content area width is increased to locked moderate targets.
  - [ ] Wide tables are readable without severe column collapse.
  - [ ] Mobile still works via responsive/table-overflow behavior.
- [ ] List formatting is normalized.
  - [ ] No literal `*` bullet paragraphs remain where markdown list syntax should be used.
  - [ ] No escaped ordered-list artifacts like `1\.` and `1\)` remain in rendered prose where proper lists are intended.
- [ ] Source structure is page-first.
  - [ ] Each page has nearby table sources for the tables it renders.
  - [ ] Table lookup is deterministic and validated.
- [ ] Trace and lint gates pass with the new structure.

## 3) Scope boundaries
- [ ] In scope:
  - [ ] Source file split and navigation wiring.
  - [ ] Table file relocation/co-location and resolver updates.
  - [ ] List/text normalization for rendering correctness.
  - [ ] CSS/theme overrides for layout and table width behavior.
  - [ ] Validation/lint/build pipeline adjustments required by the new source topology.
- [ ] Out of scope:
  - [ ] Rewriting normative mapping judgments or safety classifications.
  - [ ] Changing canonical IDs unless required by a proven technical constraint.
  - [ ] Introducing new rendering backends.

## 4) Worktree execution plan
- [ ] Create a new branch and dedicated worktree for this remediation.
- [ ] Capture baseline evidence before edits.
  - [ ] Save baseline HTML output snapshot.
  - [ ] Save baseline screenshots for representative pages/tables.
  - [ ] Save baseline diagnostics for list-format artifacts.
- [ ] Keep changes isolated to the worktree branch until acceptance criteria are met.

## 4A) New-session bootstrap checklist (verbatim)
- [ ] Run this bootstrap in a fresh shell session before any implementation edits:

```bash
printenv OPENCODE_CONFIG_DIR
git fetch --all --prune
git worktree add "../iso26262-render-remediation" \
  -b feat/iso26262-render-remediation-<timestamp> \
  docs/iso26262-sphinx-traceability-migration-20260214T184350Z
cd "../iso26262-render-remediation"
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
git merge-base --is-ancestor ccd270723b62e4bcad5ec9d00d1a0abd07a80dfc HEAD
test -f docs/conf.py
test -f exts/iso26262_spec/table_directive.py
test -f exts/iso26262_spec_lints/legacy_token_check.py
test -f exts/iso26262_spec_lints/native_table_check.py
test -f exts/iso26262_spec_lints/paragraph_id_check.py
test -f src/index.md
uv sync
export SPHINX_MIGRATION_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-render-remediation-<run-id>"
uv run python make.py --help
uv run python make.py validate
uv run python make.py build
```

- [ ] If any command above fails, stop and reconcile before continuing.
- [ ] Confirm `uv run python make.py --help` includes Sphinx flow commands (`validate`, `build`, `trace-validate`, `trace-report`, `verify`, `migrate-sphinx`).

## 5) Information architecture and page split strategy
- [x] Use top-level section split (locked).
  - [ ] One source page per top-level numbered section, plus landing/index pages.
  - [ ] Keep section titles and IDs stable where possible to avoid link churn.
- [x] Do not split further into subsection-level pages in this remediation.
- [ ] Introduce explicit source hierarchy under `src/`.
  - [ ] `src/index.md` as root navigation document.
  - [ ] `src/pages/<page-slug>/page.md` for each rendered page.
  - [ ] Toctree order matches the canonical document order.

## 5A) Locked page map and toctree order
- [ ] `src/pages/01-introduction-and-scope/page.md` -> Section 1.
- [ ] `src/pages/02-review-notes-and-critiques/page.md` -> Section 2.
- [ ] `src/pages/03-clause-5-general-topics/page.md` -> Section 3.
- [ ] `src/pages/04-clause-7-architectural-design/page.md` -> Section 4.
- [ ] `src/pages/05-clause-8-unit-design-and-implementation/page.md` -> Section 5.
- [ ] `src/pages/06-clause-9-unit-verification/page.md` -> Section 6.
- [ ] `src/pages/07-clause-10-integration-and-verification/page.md` -> Section 7.
- [ ] `src/pages/08-clause-11-testing-of-embedded-software/page.md` -> Section 8.
- [ ] `src/pages/09-configurable-software-annex-c/page.md` -> Section 9.
- [ ] `src/pages/10-rust-language-inventory/page.md` -> Section 10.
- [ ] `src/pages/11-standard-library-inventory/page.md` -> Section 11.
- [ ] `src/pages/12-tooling-qualification-and-evidence/page.md` -> Section 12.
- [ ] `src/pages/13-asil-profile-summary-matrices/page.md` -> Section 13.
- [ ] `src/pages/14-references/page.md` -> Section 14.

## 6) Table co-location design
- [ ] Move table YAML files from global `src/tables/` into page-owned locations.
  - [ ] Locked path pattern: `src/pages/<page-slug>/tables/table-XX.yaml`.
- [ ] Update table resolution behavior to support page-local lookup.
  - [ ] Primary lookup: current page-local `tables/` directory.
  - [x] No fallback lookup path will be kept during migration.
  - [ ] Hard-cut table resolver behavior is required at merge-ready state.
- [ ] Keep schema validation behavior correct.
  - [ ] Ensure table schema resolution still maps by table ID.
  - [ ] Update schema tooling if schema files are also co-located or if paths change.
- [ ] Add deterministic ownership checks.
  - [ ] Document table-to-page ownership map.
  - [ ] Add lint/check that a table is not ambiguously owned by multiple pages.

## 6A) Locked table ownership matrix (hard cutover)
- [ ] `table-01` -> `src/pages/01-introduction-and-scope/tables/table-01.yaml`
- [ ] `table-02` -> `src/pages/03-clause-5-general-topics/tables/table-02.yaml`
- [ ] `table-03` -> `src/pages/04-clause-7-architectural-design/tables/table-03.yaml`
- [ ] `table-04` -> `src/pages/04-clause-7-architectural-design/tables/table-04.yaml`
- [ ] `table-05` -> `src/pages/04-clause-7-architectural-design/tables/table-05.yaml`
- [ ] `table-06` -> `src/pages/05-clause-8-unit-design-and-implementation/tables/table-06.yaml`
- [ ] `table-07` -> `src/pages/06-clause-9-unit-verification/tables/table-07.yaml`
- [ ] `table-08` -> `src/pages/06-clause-9-unit-verification/tables/table-08.yaml`
- [ ] `table-09` -> `src/pages/06-clause-9-unit-verification/tables/table-09.yaml`
- [ ] `table-10` -> `src/pages/07-clause-10-integration-and-verification/tables/table-10.yaml`
- [ ] `table-11` -> `src/pages/07-clause-10-integration-and-verification/tables/table-11.yaml`
- [ ] `table-12` -> `src/pages/08-clause-11-testing-of-embedded-software/tables/table-12.yaml`
- [ ] `table-13` -> `src/pages/10-rust-language-inventory/tables/table-13.yaml`
- [ ] `table-14` -> `src/pages/10-rust-language-inventory/tables/table-14.yaml`
- [ ] `table-15` -> `src/pages/10-rust-language-inventory/tables/table-15.yaml`
- [ ] `table-16` -> `src/pages/10-rust-language-inventory/tables/table-16.yaml`
- [ ] `table-17` -> `src/pages/10-rust-language-inventory/tables/table-17.yaml`
- [ ] `table-18` -> `src/pages/10-rust-language-inventory/tables/table-18.yaml`
- [ ] `table-19` -> `src/pages/10-rust-language-inventory/tables/table-19.yaml`
- [ ] `table-20` -> `src/pages/11-standard-library-inventory/tables/table-20.yaml`
- [ ] `table-21` -> `src/pages/11-standard-library-inventory/tables/table-21.yaml`
- [ ] `table-22` -> `src/pages/11-standard-library-inventory/tables/table-22.yaml`
- [ ] `table-23` -> `src/pages/11-standard-library-inventory/tables/table-23.yaml`
- [ ] `table-24` -> `src/pages/11-standard-library-inventory/tables/table-24.yaml`
- [ ] `table-25` -> `src/pages/12-tooling-qualification-and-evidence/tables/table-25.yaml`
- [ ] `table-26` -> `src/pages/13-asil-profile-summary-matrices/tables/table-26.yaml`
- [ ] Sections with no co-located mapping tables in this pass: Sections 2, 9, and 14.

## 7) Formatting normalization plan (lists and paragraph artifacts)
- [ ] Convert pseudo-lists to real markdown lists.
  - [ ] Replace literal bullet-glyph-prefixed text blocks with markdown unordered lists.
  - [ ] Replace escaped ordered-list lines with true ordered list syntax.
- [ ] Remove style hints that cause undesired HTML list behavior when equivalent markdown structure is available.
- [ ] Verify no residual formatting artifacts remain in rendered HTML source dumps.

## 8) Layout and table readability plan
- [ ] Add custom CSS (through Sphinx static path and css inclusion) for layout overrides.
- [ ] Increase desktop content width with moderate target bounds.
  - [ ] At viewport `1440x900`, content column width target: `>= 1000px` and `<= 1180px`.
  - [ ] At viewport `1280x800`, content column width target: `>= 900px`.
  - [ ] Keep line-length comfort by avoiding aggressive full-bleed widths.
- [ ] Improve table rendering defaults.
  - [ ] Render mapping tables at full available content width.
  - [ ] Avoid severe column squeeze on table-heavy pages.
  - [ ] Use table-local horizontal overflow for very wide tables.
- [ ] Preserve mobile behavior.
  - [ ] At viewport `390x844`, avoid page-level horizontal overflow.
  - [ ] Keep table overflow constrained to table wrappers.

## 8A) Visual QA matrix (required)
- [ ] Capture before/after screenshots at fixed viewports.
  - [ ] `1440x900`
  - [ ] `1280x800`
  - [ ] `1024x768`
  - [ ] `768x1024`
  - [ ] `390x844`
- [ ] Capture before/after screenshots for fixed pages.
  - [ ] `index`
  - [ ] Page 01 (intro + bullet usage)
  - [ ] Page 10 (table-heavy Rust inventory)
  - [ ] Page 11 (table-heavy standard library inventory)
  - [ ] Page 12 or 13 (mixed prose + matrix)
- [ ] Validate visual acceptance.
  - [ ] No monolithic single-page reading flow.
  - [ ] Tables are materially wider and easier to scan on desktop.
  - [ ] No literal bullet or escaped-ordered-list artifacts.
  - [ ] Mobile remains usable with no global horizontal scroll.

## 9) Tooling, lint, and validation updates
- [ ] Update markdown scanning assumptions from top-level-only to recursive page tree.
- [ ] Update migration/lint scripts that currently glob only `src/*.md`.
- [ ] Ensure trace validation still checks the complete source set.
- [ ] Ensure paragraph-id and anchor outputs still validate after split and relocation.

## 9A) Must-update path-assumption checklist (new-session critical)
- [ ] Update `make.py` legacy token scan from top-level glob to recursive markdown scan.
  - [ ] `make.py` function: `_find_legacy_tokens`.
- [ ] Update `make.py` table validation path assumptions for co-located tables.
  - [ ] `make.py` function: `_validate_all_tables`.
- [ ] Update Sphinx table root/config assumptions for co-located table discovery.
  - [ ] `docs/conf.py` setting: `iso26262_table_root` and related path semantics.
- [ ] Update directive table resolution to use current page-local table directories.
  - [ ] `exts/iso26262_spec/table_directive.py`.
- [ ] Update lint for legacy-token markdown scanning to recurse through `src/pages/**`.
  - [ ] `exts/iso26262_spec_lints/legacy_token_check.py`.
- [ ] Update lint for native table usage scanning to recurse through `src/pages/**`.
  - [ ] `exts/iso26262_spec_lints/native_table_check.py`.
- [ ] Remove hardcoded single-file markdown assumptions from paragraph-id lint checks.
  - [ ] `exts/iso26262_spec_lints/paragraph_id_check.py` currently assumes `iso26262_rust_mapping.md`.
- [ ] Ensure docs/runbook references reflect the new source tree.
  - [ ] `README.md` and relevant docs under `docs/`.

## 10) Stage map and checklist
- [ ] ST0 Baseline capture in worktree.
- [ ] ST1 Source split and toctree wiring.
- [ ] ST2 Table co-location migration + resolver updates.
- [ ] ST3 List-format normalization.
- [ ] ST4 Layout/CSS widening and table readability tuning.
- [ ] ST5 Lint and trace gate updates for recursive multi-page source.
- [ ] ST6 Full build/validation and visual QA.
- [ ] ST7 Acceptance review and merge readiness.

## 10A) Stage command contract and gate artifacts
- [ ] ST0 command gate.
  - [ ] `uv run python make.py validate`
  - [ ] `uv run python make.py build`
  - [ ] Baseline artifacts captured under `$SPHINX_MIGRATION_RUN_ROOT/artifacts/baseline/`.
- [ ] ST1-ST4 command gate after each stage.
  - [ ] `uv run python make.py validate`
  - [ ] `uv run python make.py build`
  - [ ] Stage notes and diffs captured under `$SPHINX_MIGRATION_RUN_ROOT/artifacts/stages/<stage-id>/`.
- [ ] ST5 command gate.
  - [ ] `uv run python make.py trace-validate`
  - [ ] `uv run python make.py trace-report`
  - [ ] Validate report/log outputs in run root.
- [ ] ST6 command gate.
  - [ ] `uv run python make.py verify`
  - [ ] Confirm `trace-validate` and `trace-report` status is pass.
- [ ] ST7 closeout gate.
  - [ ] Final checklist complete.
  - [ ] Evidence bundle complete.

## 11) Validation protocol
- [ ] Functional checks.
  - [ ] Build succeeds without warnings elevated to failures in strict mode.
  - [ ] Page navigation works and all toctree links resolve.
  - [ ] Table directives resolve from co-located paths.
- [ ] Rendering checks.
  - [ ] No monolithic long-form page output remains.
  - [ ] Desktop width and table readability are materially improved.
  - [ ] Mobile layout remains intact.
  - [ ] No literal bullet artifacts or escaped list text artifacts remain.
- [ ] Traceability checks.
  - [ ] Anchor and paragraph-id outputs remain valid.
  - [ ] No new unresolved references introduced.

## 11A) Definition of done (artifact bundle)
- [ ] Build outputs.
  - [ ] `build/html/index.html` exists and links to all page files.
  - [ ] Page outputs exist for all files listed in Section 5A.
  - [ ] `build/html/_static/custom.css` is present and loaded.
  - [ ] `build/paragraph-ids.json` exists and validates.
- [ ] Run-root outputs.
  - [ ] `$SPHINX_MIGRATION_RUN_ROOT/artifacts/validation/trace-validate.log`
  - [ ] `$SPHINX_MIGRATION_RUN_ROOT/traceability-statement-coverage.json`
  - [ ] `$SPHINX_MIGRATION_RUN_ROOT/traceability-statement-coverage.md`
- [ ] Visual evidence outputs.
  - [ ] Before screenshots under `$SPHINX_MIGRATION_RUN_ROOT/artifacts/qa/before/`
  - [ ] After screenshots under `$SPHINX_MIGRATION_RUN_ROOT/artifacts/qa/after/`
  - [ ] Viewport/page coverage matches Section 8A.
- [ ] Review outputs.
  - [ ] Short remediation summary with file/path changes.
  - [ ] Table ownership matrix verified against moved files.
  - [ ] Remaining risks and follow-ups documented.

## 12) Risks and mitigations
- [ ] Risk: page split breaks existing links/anchors.
  - [ ] Mitigation: preserve heading IDs where possible and add compatibility aliasing where required.
- [ ] Risk: hard-cut table relocation breaks directive resolution.
  - [ ] Mitigation: pre-move ownership audit + resolver tests + single-pass hard-cut migration checks.
- [ ] Risk: layout widening causes mobile regressions.
  - [ ] Mitigation: explicit breakpoint testing and overflow containment rules.
- [ ] Risk: legacy scripts miss nested markdown files.
  - [ ] Mitigation: recursive glob migration and strict pre-merge validation.
- [ ] Risk: new session starts from wrong branch and misses Sphinx source files.
  - [ ] Mitigation: enforce Section 0A and Section 4A base/bootstrap gates before edits.

## 13) Locked defaults summary (handoff quick reference)
- [x] Page split granularity: top-level sections only.
- [x] Co-location structure: `src/pages/<slug>/page.md` + `src/pages/<slug>/tables/`.
- [x] Migration mode: one-pass hard cutover with no fallback path.
- [x] Desktop layout target: moderate widening, not aggressive full-bleed.
- [x] Required base: `docs/iso26262-sphinx-traceability-migration-20260214T184350Z` pinned to `ccd270723b62e4bcad5ec9d00d1a0abd07a80dfc`.
