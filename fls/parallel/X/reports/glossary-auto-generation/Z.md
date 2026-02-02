# Glossary audit Z

## Per-letter checklist
- Letter: Z
- [ ] Reconcile Z terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate Z terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for Z
- [ ] Update `migration-checklist.md` for all Z terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint Z migration`
- [ ] Letter complete

## Term checklist
- [ ] zero-sized type (zero_sized_type)
- [ ] zero-variant enum type (zero_variant_enum_type)

## zero-sized type (zero_sized_type)

### Before glossary entry (origin/main)

```rst
.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^

:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.
```

### After glossary entry (generated)

```rst
.. _fls_ktbsATopxcZG:

zero-sized type
^^^^^^^^^^^^^^^

:dp:`fls_dAsrpx56CXIq`
 A :t:`zero-sized type <zero_sized_type>` is a :t:`fixed sized type <fixed_sized_type>` with :t:`size` zero.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## zero-variant enum type (zero_variant_enum_type)

### Before glossary entry (origin/main)

```rst
.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### After glossary entry (generated)

```rst
.. _fls_EUThbmsUhrC0:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Cg2ClpQpXzjy`
 A :t:`zero-variant enum type <zero_variant_enum_type>` is an :t:`enum type <enum_type>` without any :t:`enum variants <enum_variant>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
