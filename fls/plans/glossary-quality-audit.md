# Glossary quality audit (generated vs legacy)

## Goals

- Compare the generated glossary against the legacy glossary and rate every term for usefulness.
- Identify missing terms (red text), nonsensical or tautological definitions, and legacy definitions that are superior.
- Treat legacy link-only/alias-only entries as intentional; expanded generated definitions for those are regressions.
- Treat legacy :dt: vs generated :t: as an expected role-only change; rate 5 with tag `definition-same-role-change-expected`.
- Treat missing legacy "See ..." lines as actionable gaps; rate 3 with tag `missing-see-line` and include the missing "See ..." line in Notes.
- Only annotate recommendations for missing "See ..." lines; do not edit spec source.
- Produce a single report with one `##` heading per term and a concise usefulness evaluation.
- Capture quality lessons in a reusable definition skill.

## Baseline

- Legacy glossary baseline: `/home/pete.levasseur/opencode-project-agents/fls/legacy/origin-main/src/glossary.rst`.
- Generated glossary source: `build/glossary.generated.rst` (created via `./make.py --check-generated-glossary`).

## Deliverables

- Report: `$OPENCODE_CONFIG_DIR/reports/glossary-quality-report.md`.
- Intermediate chapter notes: `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/<chapter>.md`.
- Chapter index: `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/README.md`.
- Definition quality skill: `$OPENCODE_CONFIG_DIR/skills/fls-glossary-definitions/SKILL.md`.

## Plan

- [ ] Generate `build/glossary.generated.rst` with `./make.py --check-generated-glossary` and confirm the file exists.
- [ ] Parse the generated glossary into a term -> definition map (including multi-paragraph entries and "See" cross-references).
- [ ] Parse the legacy glossary into a term -> definition map for comparison.
- [ ] Capture recurring/systemic definition issues during a holistic read of the generated glossary and summarize them in the report (list lead-ins without lists, truncated/dangling sentences, alias-only definitions, circular term chains, sentence fragments, tautologies, link-only "See ..." definitions, missing scope/discriminators, low-signal definitions, editorial noise/typos/spacing).
- [ ] Build a chapter index: list chapter files from `src/index.rst`, then map each term to the chapter where its `:dt:` definition lives.
- [ ] Define the rating rubric and issue tags used by sub-agents; include `missing-see-line` and `definition-same-role-change-expected` plus override rules in stubs and `chapters/README.md`.
- [ ] Update the helper script to enforce override rules (role-only -> rating 5, missing-see-line -> rating 3 + missing "See ..." line in Notes).
- [ ] Create per-chapter stub files (plus `_misc.md`) under `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/` with checklists, conventions, and a per-term template.
- [ ] Write `chapters/README.md` with the stub file list, conventions, and sub-agent instructions.
- [ ] Seed each stub with alphabetical `## <term>` headings after mapping and record `expected <count> / found <count>` coverage.
- [ ] Validate coverage counts match the mapping before launching sub-agents.
- [ ] Find missing terms by comparing all `:t:` references in `src/**/*.rst` against the generated glossary term set; confirm the "namespace qualifier" gap and any other red-text entries.
- [ ] Launch one sub-agent per chapter to review that chapter's terms against legacy definitions and rate usefulness (following the new override rules).
- [ ] Save each chapter review in `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/` before consolidation.
- [ ] Consolidate chapter outputs into `glossary-quality-report.md` with a `## <term>` heading for every term and a concise usefulness evaluation + rating.
- [ ] Add a priority index near the top of the report that groups terms by rating and flags (missing, nonsensical/tautological, regression vs legacy, missing-see-line).
- [ ] Write the definition quality skill file with do/don't rules and examples drawn from the audit.
- [ ] Quick QA pass: verify the report covers all terms in the generated glossary and explicitly lists missing/red-text terms.
