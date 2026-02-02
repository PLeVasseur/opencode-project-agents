# Glossary audit Q

## Per-letter checklist
- Letter: Q
- [ ] Reconcile Q terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate Q terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for Q
- [ ] Update `migration-checklist.md` for all Q terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint Q migration`
- [ ] Letter complete

## Term checklist
- [ ] qualified path expression (qualified_path_expression)
- [ ] qualified type (qualified_type)
- [ ] qualified type path (qualified_type_path)
- [ ] qualifying trait (qualifying_trait)

## qualified path expression (qualified_path_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.

:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_4g4hsEPfjZ2p:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wrIEagA5DGX1`
 A :t:`qualified path expression <qualified_path_expression>` is a :t:`path expression <path_expression>` that resolves through a :t:`qualified type <qualified_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^


:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^


:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## qualified type (qualified_type)

### Before glossary entry (origin/main)

```rst
.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^

:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.

:dp:`fls_a4heXjzO3jem`
See :s:`QualifiedType`.
```

### After glossary entry (generated)

```rst
.. _fls_HTU05j0O4WX5:

qualified type
^^^^^^^^^^^^^^

:dp:`fls_1lW263YLGtVl`
 A :t:`qualified type <qualified_type>` is a :t:`type` that is restricted to a set of :t:`implementations <implementation>` that exhibit :t:`implementation conformance <implementation_conformance>` to a :t:`qualifying trait <qualifying_trait>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^


:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.


:dp:`fls_a4heXjzO3jem`
See :s:`QualifiedType`.

.. _fls_koVlQq8aPdPv:

qualified type path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^


:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.


:dp:`fls_a4heXjzO3jem`
See :s:`QualifiedType`.

.. _fls_koVlQq8aPdPv:

qualified type path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## qualified type path (qualified_type_path)

### Before glossary entry (origin/main)

```rst
.. _fls_koVlQq8aPdPv:

qualified type path
^^^^^^^^^^^^^^^^^^^

:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.

:dp:`fls_RR8fFLD7Rxlt`
See :s:`QualifiedTypePath`.
```

### After glossary entry (generated)

```rst
.. _fls_mTpZwhWo8LfD:

qualified type path
^^^^^^^^^^^^^^^^^^^

:dp:`fls_JqldyTp4gh1G`
 A :t:`qualified type path <qualified_type_path>` is a :t:`type path <type_path>` that resolves through a :t:`qualified type <qualified_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.


:dp:`fls_a4heXjzO3jem`
See :s:`QualifiedType`.

.. _fls_koVlQq8aPdPv:

qualified type path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.


:dp:`fls_RR8fFLD7Rxlt`
See :s:`QualifiedTypePath`.

.. _fls_B0m82A8jIerQ:

qualifying trait
^^^^^^^^^^^^^^^^


:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_e7YyZXOFo6ei`
A :dt:`qualified type` is a :t:`type` that is restricted to a set of
:t:`[implementation]s` that exhibit :t:`implementation conformance` to a
:t:`qualifying trait`.


:dp:`fls_a4heXjzO3jem`
See :s:`QualifiedType`.

.. _fls_koVlQq8aPdPv:

qualified type path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.


:dp:`fls_RR8fFLD7Rxlt`
See :s:`QualifiedTypePath`.

.. _fls_B0m82A8jIerQ:

qualifying trait
^^^^^^^^^^^^^^^^


:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## qualifying trait (qualifying_trait)

### Before glossary entry (origin/main)

```rst
.. _fls_B0m82A8jIerQ:

qualifying trait
^^^^^^^^^^^^^^^^

:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.

:dp:`fls_z6OeUWBnec90`
See :s:`QualifyingTrait`.
```

### After glossary entry (generated)

```rst
.. _fls_OWNEOZRHEPTQ:

qualifying trait
^^^^^^^^^^^^^^^^

:dp:`fls_OSYKnCfbdYkc`
 A :t:`qualifying trait <qualifying_trait>` is a :t:`trait` that imposes a restriction on a :t:`qualified type <qualified_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.


:dp:`fls_RR8fFLD7Rxlt`
See :s:`QualifiedTypePath`.

.. _fls_B0m82A8jIerQ:

qualifying trait
^^^^^^^^^^^^^^^^


:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.


:dp:`fls_z6OeUWBnec90`
See :s:`QualifyingTrait`.

.. _fls_tbvugpuvcluj:

range expression
^^^^^^^^^^^^^^^^


:dp:`fls_bffrbucfwu7`
A :dt:`range expression` is an :t:`expression` that constructs a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_S0QT9ib38i8E`
A :dt:`qualified type path` is a :t:`type path` that resolves through a
:t:`qualified type`.


:dp:`fls_RR8fFLD7Rxlt`
See :s:`QualifiedTypePath`.

.. _fls_B0m82A8jIerQ:

qualifying trait
^^^^^^^^^^^^^^^^


:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.


:dp:`fls_z6OeUWBnec90`
See :s:`QualifyingTrait`.

.. _fls_tbvugpuvcluj:

range expression
^^^^^^^^^^^^^^^^


:dp:`fls_bffrbucfwu7`
A :dt:`range expression` is an :t:`expression` that constructs a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
