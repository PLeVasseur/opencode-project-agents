# Glossary audit Z

## Per-letter checklist
- Letter: Z
- [x] Reconcile Z terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate Z terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for Z
- [x] Update `migration-checklist.md` for all Z terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint Z migration`
- [x] Letter complete

## Term checklist
- [x] zero-sized type (zero_sized_type)
- [x] zero-variant enum type (zero_variant_enum_type)

## zero-sized type (zero_sized_type)
- Placement: `src/types-and-traits.rst`
- Action: Migrated definition into chapter.
- Rationale: Reviewed usages in `src/types-and-traits.rst`; definition placed in owning section.

## zero-variant enum type (zero_variant_enum_type)
- Placement: `src/types-and-traits.rst`
- Action: Migrated definition into chapter.
- Rationale: Reviewed usages in `src/types-and-traits.rst`; definition placed in owning section.
