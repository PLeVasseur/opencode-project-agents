# Glossary audit symbols

## Per-letter checklist
- Letter: symbols
- [ ] Reconcile symbols terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate symbols terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for symbols
- [ ] Update `migration-checklist.md` for all symbols terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint symbols migration`
- [ ] Letter complete

## Term checklist
- [ ] :dp:`fls_DfTszT1PjV7o` (proc_macro_crate)

## :dp:`fls_DfTszT1PjV7o` (proc_macro_crate)

### Before glossary entry (origin/main)

```rst
.. _fls_AjjdLZWiL9Tq:

:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.
```

### After glossary entry (generated)

```rst
.. _fls_gIjveZ8on0Qx:

proc-macro crate
^^^^^^^^^^^^^^^^

:dp:`fls_uWGvmomi2yx3`
 A :t:`proc-macro crate <proc_macro_crate>` is a :t:`crate` whose :t:`crate type <crate_type>` is ``proc-macro``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
