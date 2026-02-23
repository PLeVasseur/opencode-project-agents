# Revise glossary collection for legacy See lines

## Goal
Include adjacent legacy "See ..." paragraphs in the generated glossary output so
the glossary-quality audit no longer flags missing-see-line for main chapters.

## Scope
- Glossary generation logic in `exts/ferrocene_spec/glossary.py`.
- No edits to `src/` content in this plan.

## Steps
1. Extend glossary collection to attach adjacent "See ..." paragraphs to the
   term definition:
   - After locating the :dt: paragraph in `GlossaryTransform.build_paragraphs`,
     scan following sibling paragraphs.
   - Include consecutive paragraphs that begin with "See" or "For ... see"
     (case-insensitive) after stripping the `:dp:` line.
   - Stop when you encounter the next :dt: paragraph or the first non-See
     paragraph.
2. Ensure each attached paragraph is normalized the same way as the definition:
   - Remove paragraph `DefIdNode` IDs.
   - Replace term definitions (`DefIdNode` kinds TERM_KIND/SYNTAX_KIND/
     CODE_TERM_KIND) with glossary references.
   - Set `ref_source_doc` on `DefRefNode` nodes.
3. In `GlossaryTransform.replace_node`, insert a stable paragraph ID for each
   attached paragraph using `stable_fls_id("glossary:", term_id, used_ids)` so
   subsequent See paragraphs get unique IDs (e.g., `:2`, `:3`, ...).
4. Run `./make.py --check-generated-glossary`.
5. Spot-check `build/glossary.generated.rst` for a known term (e.g.,
   "binary literal") to confirm the See paragraph is present.
6. Commit: `fix(glossary): include adjacent See lines in generated glossary`.

## Notes
- This plan is required before running the full glossary-quality audit so
  missing-see-line counts can drop to zero for main chapters.
