# Glossary-only See role

## Goal
Introduce an explicit glossary-only role for legacy "See ..." lines so they are
included in the generated glossary but omitted from chapter output, reducing
noise while keeping the audit satisfied.

## Scope
Main chapters only (see orchestrate-glossary-improvements.md). Appendices and
_misc are excluded.

## Implementation
1. Add a new explicit role `:gsee:` to the spec domain that takes the term name
   as its text (e.g., ``:gsee:`addition assignment``) and records the target
   term id.
   - Implement as a `SphinxRole` and register with
     `app.add_role_to_domain("spec", "gsee", ...)`.
   - Add a custom node and register it with `app.add_node(...)` so writers
     do not encounter unknown nodes.
2. Implement a transform that marks any paragraph containing `:gsee:` with
   metadata (e.g., `glossary_only_term_id`). Enforce adjacency by warning if
   the paragraph is not immediately after a matching `:dt:` definition paragraph
   for the same term, *unless* the paragraph itself contains the matching
   `:dt:` (alias-only legacy case).
3. Update glossary generation to append glossary-only paragraphs for a term
   after the term definition paragraph. These paragraphs should:
   - Be normalized the same way as definition paragraphs (DefId -> DefRef,
     `ref_source_doc` set).
   - Serialize without the `:gsee:` node so the output starts with the legacy
     "See ..." line verbatim.
4. Add a transform that removes glossary-only paragraphs from non-glossary
   output documents so chapters stay clean. Prefer a post-transform or
   `doctree-resolved` hook so writers never see the custom node.
5. Run `./make.py --check-generated-glossary` to confirm no warnings or build
   regressions.

## Conversion
1. Use legacy content verbatim. Do not add new alias sentences.
2. In main chapter sources, convert legacy alias lines of the form:
   ``For :t:`<term>`, see :t:`<target>`.`` or ``See ...`` into glossary-only
   lines:
   ``:gsee:`<term>` <legacy See line>``.
3. Remove any adjacent explicit "See ..." paragraphs that were added solely to
   satisfy legacy mapping, so only the glossary-only line remains.
4. For alias-only legacy terms, keep only the `:gsee:` paragraph (the term
   disappears from chapter output). For legacy definitions with a "See ..."
   line, keep the legacy definition sentence in the chapter and convert only
   the legacy "See ..." line to `:gsee:`.
5. Run `./make.py --check-generated-glossary` again after conversion.
6. Commit: `docs(glossary): add glossary-only See role`.
