# PR #11 Review: refactor(glossary): switch to generated-only glossary source and reproducibility checks

**Repository:** PLeVasseur/fls  
**PR:** [#11](https://github.com/PLeVasseur/fls/pull/11)  
**Branch:** `glossary-single-source-phase1-repack-upstream-main` → `main`  
**Commits:** 4  

---

## Commit Ordering Assessment

The four commits follow a clean layered-dependency order:

**Commit 1** (`06da2fd` — `feat(glossary): add single-source glossary tooling core`) introduces the Sphinx extension (`glossary.py`), the generation scripts (`generate-glossary.py`, `generate-glossary-entry.py`), build system changes in `make.py`, and the glossary prelude include. This is the infrastructure layer — nothing else can work without it.

**Commit 2** (`85a60b6` — `docs(glossary): migrate glossary content to single-source entries`) is the massive content migration. It places `.. glossary-entry::` directives into all 23 chapter files, extracting definitions from the monolithic `glossary.rst` into a generated `glossary.rst.inc`. This depends entirely on commit 1's tooling.

**Commit 3** (`6716db3` — `ci(glossary): add transitional html parity verification`) adds `tools/verify-html-diff.py` and a CI workflow step. This logically belongs after the migration content exists so the verification tool has something to verify against.

**Commit 4** (`8e93f35` — `refactor(glossary): switch to generated-only glossary source and reproducibility checks`) is the capstone: removes the old `glossary.rst` static content and `glossary.rst.inc`, hardens the verification tool (normalized paragraph IDs, `searchindex.js` handling, deterministic worktree export), and adds a repro-mode check. Lint/formatting fixes for the Python tool are folded in here.

**Verdict: The ordering is correct and I wouldn't propose changes.** Each commit builds on the previous one's outputs, and the stack is structured so that intermediate commits leave the build in a functional state (commit 3's verification can confirm parity between upstream and the commit 2 migration). The only minor alternative would be to split commit 4's lint/format fixes into a commit 4a, but since the PR description explicitly notes this was a deliberate choice to keep the stack at four commits, that's a reasonable editorial call.

---

## Glossary Directive Placement Assessment

I examined all 779 `.. glossary-entry::` directives across the 23 chapter files. A companion JSONL artifact (`glossary_placement_scores.jsonl`) has per-entry scores and rationale.

### Score Distribution

| Score | Count | Description |
|-------|-------|-------------|
| 10    | 587   | Has `:chapter:` content replacing upstream inline `:dp:` definition at verified same-file position |
| 9     | 190   | Glossary-only; term referenced in surrounding text or shares keywords with section name |
| 8     | 2     | Glossary-only; reasonable semantic grouping but no direct textual reference nearby |

### Key Findings

The placement strategy is methodical: entries with `:chapter:` content sit exactly where the upstream inline definitions lived, and glossary-only entries are grouped adjacent to their most closely related concept. For example, `incomplete associated constant` (glossary-only) sits directly after `associated constant` (which has `:chapter:` content) — this co-locates the "incomplete" variant with its parent concept.

I verified all 603 chapter-content DPs match the same file as upstream — **zero cross-file misplacements**.

### Entries with Special Annotations

The 4 entries flagged with annotations in the JSONL are the closest things to debatable placements:

1. **`concrete type`** in `attributes.rst` (line 1844) — Conceptually a type concept, but its only `:t:` usage anywhere in the FLS is in the `type_length_limit` attribute section. Co-locating with usage is defensible. The JSONL includes a low-confidence alternative at `fls_Led1Nxfcd70K` in `types-and-traits.rst`.

2. **`mutability`** in `types-and-traits.rst` Type Unification section (line 3030) — Cross-cutting concept that could live in several places. Current placement aligns with where mutability constraints are formally specified.

3. **`mutable`** in `types-and-traits.rst` Type Unification section (line 3037) — Same rationale as `mutability` above.

4. **`Self`** in `entities-and-resolution.rst` between Label Scope and Self Scope (line 891) — Could be seen as a types concept, but `Self` has dedicated scope rules here, making `entities-and-resolution` the right home.

### Bottom Line

The placement quality is very high. No entries need to be moved for correctness. The only entry I'd flag for discussion (not a defect) is `concrete type` in `attributes.rst`, and even that one has a solid rationale.
