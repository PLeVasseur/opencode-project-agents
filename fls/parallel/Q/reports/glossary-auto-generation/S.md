# Glossary audit S

## Per-letter checklist
- Letter: S
- [ ] Reconcile S terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate S terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for S
- [ ] Update `migration-checklist.md` for all S terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint S migration`
- [ ] Letter complete

## Term checklist
- [ ] safety invariant (safety_invariant)
- [ ] scalar type (scalar_type)
- [ ] scope (scope)
- [ ] scope hierarchy (scope_hierarchy)
- [ ] selected field (selected_field)
- [ ] Self (self)
- [ ] self parameter (self_parameter)
- [ ] self public modifier (self_public_modifier)
- [ ] Self scope (self_scope)
- [ ] send type (send_type)
- [ ] separator (separator)
- [ ] sequence type (sequence_type)
- [ ] shadowing (shadowing)
- [ ] shared borrow (shared_borrow)
- [ ] shared reference (shared_reference)
- [ ] shared reference type (shared_reference_type)
- [ ] shift left assignment (shift_left_assignment)
- [ ] shift left assignment expression (shift_left_assignment_expression)
- [ ] shift left expression (shift_left_expression)
- [ ] shift right assignment (shift_right_assignment)
- [ ] shift right assignment expression (shift_right_assignment_expression)
- [ ] shift right expression (shift_right_expression)
- [ ] shorthand deconstructor (shorthand_deconstructor)
- [ ] shorthand initializer (shorthand_initializer)
- [ ] signed integer type (signed_integer_type)
- [ ] simple byte string literal (simple_byte_string_literal)
- [ ] simple c string literal (simple_c_string_literal)
- [ ] simple import (simple_import)
- [ ] simple path (simple_path)
- [ ] simple path prefix (simple_path_prefix)
- [ ] simple path public modifier (simple_path_public_modifier)
- [ ] simple path resolution (simple_path_resolution)
- [ ] simple public modifier (simple_public_modifier)
- [ ] simple register expression (simple_register_expression)
- [ ] simple string literal (simple_string_literal)
- [ ] single segment path (single_segment_path)
- [ ] size (size)
- [ ] size operand (size_operand)
- [ ] sized type (sized_type)
- [ ] slice (slice)
- [ ] slice pattern (slice_pattern)
- [ ] slice type (slice_type)
- [ ] source file (source_file)
- [ ] statement (statement)
- [ ] static (static)
- [ ] static initializer (static_initializer)
- [ ] static lifetime elision (static_lifetime_elision)
- [ ] str (str)
- [ ] strict keyword (strict_keyword)
- [ ] string literal (string_literal)
- [ ] struct (struct)
- [ ] struct expression (struct_expression)
- [ ] struct field (struct_field)
- [ ] struct pattern (struct_pattern)
- [ ] struct type (struct_type)
- [ ] struct value (struct_value)
- [x] structurally equal (structurally_equal)
- [ ] subexpression (subexpression)
- [ ] subject expression (subject_expression)
- [ ] subject let expression (subject_let_expression)
- [ ] subpattern (subpattern)
- [ ] subtraction assignment (subtraction_assignment)
- [ ] subtraction assignment expression (subtraction_assignment_expression)
- [ ] subtraction expression (subtraction_expression)
- [ ] subtrait (subtrait)
- [ ] subtype (subtype)
- [ ] subtyping (subtyping)
- [ ] suffixed float (suffixed_float)
- [ ] suffixed integer (suffixed_integer)
- [ ] super public modifier (super_public_modifier)
- [ ] supertrait (supertrait)
- [ ] sync type (sync_type)
- [ ] syntactic category (syntactic_category)

## safety invariant (safety_invariant)

### Before glossary entry (origin/main)

```rst
.. _fls_Q4MRIo7cWv5K:

safety invariant
^^^^^^^^^^^^^^^^

:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.
```

### After glossary entry (generated)

```rst
.. _fls_IV5awpQCMrQk:

safety invariant
^^^^^^^^^^^^^^^^

:dp:`fls_Lo3vSpTxbier`
 A :t:`safety invariant <safety_invariant>` is an invariant that when violated may result in :t:`undefined behavior <undefined_behavior>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.

.. _fls_fki32ns69q4j:

rustc
^^^^^


:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.

.. _fls_Q4MRIo7cWv5K:

safety invariant
^^^^^^^^^^^^^^^^


:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.

.. _fls_fki32ns69q4j:

rustc
^^^^^


:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.

.. _fls_Q4MRIo7cWv5K:

safety invariant
^^^^^^^^^^^^^^^^


:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## scalar type (scalar_type)

### Before glossary entry (origin/main)

```rst
.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^

:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.
```

### After glossary entry (generated)

```rst
.. _fls_N3n7FHW8BhtQ:

scalar type
^^^^^^^^^^^

:dp:`fls_6nxNNOZx2Fkq`
 A :t:`scalar type <scalar_type>` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or a :t:`numeric type <numeric_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.

.. _fls_Q4MRIo7cWv5K:

safety invariant
^^^^^^^^^^^^^^^^


:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.

.. _fls_Q4MRIo7cWv5K:

safety invariant
^^^^^^^^^^^^^^^^


:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## scope (scope)

### Before glossary entry (origin/main)

```rst
.. _fls_fj8mdxi967px:

scope
^^^^^

:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
```

### After glossary entry (generated)

```rst
.. _fls_LJHud1zNfP2B:

scope
^^^^^

:dp:`fls_hTNWEn2kL2aP`
 A :t:`scope` is a region of program text where a :t:`name` can be referred to.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.

.. _fls_XeMNghZZOBqL:

scalar type
^^^^^^^^^^^


:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## scope hierarchy (scope_hierarchy)

### Before glossary entry (origin/main)

```rst
.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^

:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.
```

### After glossary entry (generated)

```rst
.. _fls_90sgyjQKstNe:

scope hierarchy
^^^^^^^^^^^^^^^

:dp:`fls_rksUc4oC46V3`
 The :t:`scope hierarchy <scope_hierarchy>` reflects the nesting of :t:`scopes <scope>` as introduced by :t:`scoping constructs <scoping_construct>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_GgBqFW2NywoA`
A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
a :t:`numeric type`.

.. _fls_fj8mdxi967px:

scope
^^^^^


:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## selected field (selected_field)

### Before glossary entry (origin/main)

```rst
.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^

:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.
```

### After glossary entry (generated)

```rst
.. _fls_sIsKdRSTvmff:

selected field
^^^^^^^^^^^^^^

:dp:`fls_8NWhTj5TYVCE`
 A :t:`selected field <selected_field>` is a :t:`field` that is selected by a :t:`field access expression <field_access_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.

.. _fls_xZUiNkBN5e00:

scope hierarchy
^^^^^^^^^^^^^^^


:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.

.. _fls_rfk06mm3pdxg:

selected field
^^^^^^^^^^^^^^


:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## Self (self)

### Before glossary entry (origin/main)

```rst
.. _fls_9o2hcy6t7dac:

Self
^^^^

:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters.
```

### After chapter excerpt (current)

```rst
Definition missing in current chapters.
```

### Role classification

no definition roles detected

### Standalone edits

Definition missing.

## self parameter (self_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^

:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.
```

### After glossary entry (generated)

```rst
.. _fls_nVK925xn9eWL:

self parameter
^^^^^^^^^^^^^^

:dp:`fls_iaoZviSYT5xT`
 A :t:`self parameter <self_parameter>` is a :t:`function parameter <function_parameter>` expressed by :t:`keyword` ``self``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8otlvwlqrd4e`
A :dt:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

.. _fls_9o2hcy6t7dac:

Self
^^^^


:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## self public modifier (self_public_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.

:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.
```

### After glossary entry (generated)

```rst
.. _fls_6DXbKvV4vXYs:

self public modifier
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_S6zT9EZSSQtX`
 A :t:`self public modifier <self_public_modifier>` is a :t:`visibility modifier <visibility_modifier>` that grants a :t:`name` :t:`private visibility <private_visibility>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.

.. _fls_6wjlbzmlx9n4:

self parameter
^^^^^^^^^^^^^^


:dp:`fls_ksne48eip15`
A :dt:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

.. _fls_jq213cesxhyp:

self public modifier
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## Self scope (self_scope)

### Before glossary entry (origin/main)

```rst
.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^

:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.
```

### After glossary entry (generated)

```rst
.. _fls_qnu2NCDLBVf0:

Self scope
^^^^^^^^^^

:dp:`fls_TPWHzr3XfdKj`
 A :t:`Self scope <self_scope>` is a :t:`scope` for :c:`Self <self>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.


:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## send type (send_type)

### Before glossary entry (origin/main)

```rst
.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^

:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.
```

### After glossary entry (generated)

```rst
.. _fls_MKr2USViKpql:

send type
^^^^^^^^^

:dp:`fls_JoWwrqqlkfmL`
 A :t:`send type <send_type>` is a :t:`type` that implements the `core::marker::Send <https://doc.rust-lang.org/stable/std/?search=core%3A%3Amarker%3A%3ASend>`__ :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.

.. _fls_exMZlNMxQvP7:

Self scope
^^^^^^^^^^


:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## separator (separator)

### Before glossary entry (origin/main)

```rst
.. _fls_at8q1svh3isg:

separator
^^^^^^^^^

:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.
```

### After glossary entry (generated)

```rst
.. _fls_DI5leyrjn2Q5:

separator
^^^^^^^^^

:dp:`fls_13lq1cJctZC8`
 A :t:`separator` is a character or a string that separates adjacent :t:`lexical elements <lexical_element>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pSvqWGRmFmH0`
A :dt:`Self scope` is a :t:`scope` for :c:`Self`.

.. _fls_8spw41g0dbqw:

send type
^^^^^^^^^


:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## sequence type (sequence_type)

### Before glossary entry (origin/main)

```rst
.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^

:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.
```

### After glossary entry (generated)

```rst
.. _fls_g8DhUmC2GFUn:

sequence type
^^^^^^^^^^^^^

:dp:`fls_uApKs8qPY355`
 A :t:`sequence type <sequence_type>` represents a sequence of elements.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

.. _fls_at8q1svh3isg:

separator
^^^^^^^^^


:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shadowing (shadowing)

### Before glossary entry (origin/main)

```rst
.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^

:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.
```

### After glossary entry (generated)

```rst
.. _fls_a3YG8V7Lz8py:

Shadowing
^^^^^^^^^

:dp:`fls_iyT59yAORHDv`
 :t:`Shadowing <shadowing>` is a property of :t:`names <name>`. A :t:`name` is said to be :t:`shadowed` when another :t:`name` with the same characters is introduced in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_128xny4qfcj5`
A :dt:`separator` is a character or a string that separates adjacent
:t:`[lexical element]s`.

.. _fls_rtgis2k7by2r:

sequence type
^^^^^^^^^^^^^


:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shared borrow (shared_borrow)

### Before glossary entry (origin/main)

```rst
.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^

:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.
```

### After glossary entry (generated)

```rst
.. _fls_twSRdqgH5S6r:

shared borrow
^^^^^^^^^^^^^

:dp:`fls_yMwvubg3rNA9`
 A :t:`shared borrow <shared_borrow>` is a :t:`borrow` produced by evaluating an :t:`immutable borrow expression <immutable_borrow_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.

.. _fls_HUklMSWzx8Mg:

shadowing
^^^^^^^^^


:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shared reference (shared_reference)

### Before glossary entry (origin/main)

```rst
.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^

:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.
```

### After glossary entry (generated)

```rst
.. _fls_jWcorz8SG878:

shared reference
^^^^^^^^^^^^^^^^

:dp:`fls_tSlcu2sYSsxY`
 A :t:`shared reference <shared_reference>` is a :t:`value` of a :t:`shared reference type <shared_reference_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_li3NXOPEH9cL`
:dt:`Shadowing` is a property of :t:`[name]s`. A :t:`name` is said to be
:dt:`shadowed` when another :t:`name` with the same characters is introduced
in the same :t:`scope` within the same :t:`namespace`, effectively hiding it.

.. _fls_c9xwhhg639u5:

shared borrow
^^^^^^^^^^^^^


:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shared reference type (shared_reference_type)

### Before glossary entry (origin/main)

```rst
.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.
```

### After glossary entry (generated)

```rst
.. _fls_y5hrVFKydLeA:

shared reference type
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tlq9MCqBZ1gO`
 A :t:`shared reference type <shared_reference_type>` is a :t:`reference type <reference_type>` not subject to :t:`keyword` ``mut``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.

.. _fls_18xazs7sp4:

shared reference
^^^^^^^^^^^^^^^^


:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift left assignment (shift_left_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.
```

### After glossary entry (generated)

```rst
.. _fls_jj8bMjI2jbJ1:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_SVvsBlNeOYIu`
 For :t:`shift left assignment <shift_left_assignment>`, see :t:`shift left assignment expression <shift_left_assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.

.. _fls_antrblstppyf:

shared reference type
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift left assignment expression (shift_left_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.

:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_DvQRxyPBXEls:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_EcS6BIUkJqhh`
 A :t:`shift left assignment expression <shift_left_assignment_expression>` is a :t:`compound assignment expression <compound_assignment_expression>` that uses bit shift left arithmetic.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8z9wb3eu5yp1`
A :dt:`shared reference type` is a :t:`reference type` not subject to
:t:`keyword` ``mut``.

.. _fls_o8EVuKgr0Y98:

shift left assignment
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. _fls_29n0oe4d7lwa:

shift left assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift left expression (shift_left_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.

:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_TCpFBLOiGyP6:

shift left expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_dD45v4bVP1Iy`
 A :t:`shift left expression <shift_left_expression>` is a :t:`bit expression <bit_expression>` that uses bit shift left arithmetic.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.


:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_j15ke2p8cjfp`
A :dt:`shift left assignment expression` is a
:t:`compound assignment expression` that uses bit shift left arithmetic.


:dp:`fls_ozu74fsakomn`
See :s:`ShiftLeftAssignmentExpression`.

.. _fls_sru4wi5jomoe:

shift left expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.


:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift right assignment (shift_right_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.
```

### After glossary entry (generated)

```rst
.. _fls_CA4I8EBMSdZL:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_OKknsCFAFm1O`
 For :t:`shift right assignment <shift_right_assignment>`, see :t:`shift right assignment expression <shift_right_assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.


:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_phiv6k4emauc`
A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
arithmetic.


:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift right assignment expression (shift_right_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.

:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_MXsb6DYN2P39:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Cx57Tu3ohkK4`
 A :t:`shift right assignment expression <shift_right_assignment_expression>` is a :t:`compound assignment expression <compound_assignment_expression>` that uses bit shift right arithmetic.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_56lu9kenzig9`
See :s:`ShiftLeftExpression`.

.. _fls_V5LMAe8ijiMQ:

shift right assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. _fls_cqfzbsasnd1t:

shift right assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shift right expression (shift_right_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.

:dp:`fls_ex1mopil8w1p`
See :s:`ShiftRightExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_8kdNrpp3geiP:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_yp0e4PObhxsm`
 A :t:`shift right expression <shift_right_expression>` is a :t:`bit expression <bit_expression>` that uses bit shift right arithmetic.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.


:dp:`fls_ex1mopil8w1p`
See :s:`ShiftRightExpression`.

.. _fls_5sxhx0w3d63z:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_1jpnp7hatlmu`
A :dt:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.


:dp:`fls_naqzlebew1uf`
See :s:`ShiftRightAssignmentExpression`.

.. _fls_dj6epbraptqn:

shift right expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.


:dp:`fls_ex1mopil8w1p`
See :s:`ShiftRightExpression`.

.. _fls_5sxhx0w3d63z:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shorthand deconstructor (shorthand_deconstructor)

### Before glossary entry (origin/main)

```rst
.. _fls_5sxhx0w3d63z:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.

:dp:`fls_rlo4237bgbwt`
See :s:`ShorthandDeconstructor`.
```

### After glossary entry (generated)

```rst
.. _fls_OnCiuWkjdREH:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_p03LtmAlJ4o2`
 A :t:`shorthand deconstructor <shorthand_deconstructor>` is a :t:`construct` that matches the :t:`name` of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a :t:`binding`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.


:dp:`fls_ex1mopil8w1p`
See :s:`ShiftRightExpression`.

.. _fls_5sxhx0w3d63z:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.


:dp:`fls_rlo4237bgbwt`
See :s:`ShorthandDeconstructor`.

.. _fls_oa4p10yles30:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_j6itily0u0k9`
A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
right arithmetic.


:dp:`fls_ex1mopil8w1p`
See :s:`ShiftRightExpression`.

.. _fls_5sxhx0w3d63z:

shorthand deconstructor
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.


:dp:`fls_rlo4237bgbwt`
See :s:`ShorthandDeconstructor`.

.. _fls_oa4p10yles30:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## shorthand initializer (shorthand_initializer)

### Before glossary entry (origin/main)

```rst
.. _fls_oa4p10yles30:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.

:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.
```

### After glossary entry (generated)

```rst
.. _fls_USFDUZiOZf3O:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_p0O405naO3u7`
 A :t:`shorthand initializer <shorthand_initializer>` is a :t:`construct` that specifies the :t:`name` of a :t:`field` in a :t:`struct expression <struct_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.


:dp:`fls_rlo4237bgbwt`
See :s:`ShorthandDeconstructor`.

.. _fls_oa4p10yles30:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.


:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_22yxrde244w8`
A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
of a :t:`field` and binds the :t:`value` of the matched :t:`field` to a
:t:`binding`.


:dp:`fls_rlo4237bgbwt`
See :s:`ShorthandDeconstructor`.

.. _fls_oa4p10yles30:

shorthand initializer
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.


:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## signed integer type (signed_integer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.
```

### After glossary entry (generated)

```rst
.. _fls_orQDn1W8LjsP:

signed integer type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_oHLsHDNwyYvm`
 A :t:`signed integer type <signed_integer_type>` is an :t:`integer type <integer_type>` whose :t:`values <value>` denote negative whole numbers, zero, and positive whole numbers.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.


:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bgxxg48snck1`
A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
of a :t:`field` in a :t:`struct expression`.


:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple byte string literal (simple_byte_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.

:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_jNYJAMBE2Lyn:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Aamr2y4KOySx`
 A :t:`simple byte string literal <simple_byte_string_literal>` is a :t:`byte string literal <byte_string_literal>` that consists of multiple :s:`AsciiCharacters <asciicharacter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qc08ydgmqudi`
See :s:`ShorthandInitializer`.

.. _fls_nmw95nc951iu:

signed integer type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.

.. _fls_4GvXiDfcPlRD:

simple byte string literal
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple c string literal (simple_c_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).

:dp:`fls_ggm5FNUqg9EY`
See :s:`SimpleCStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_xuqeEpw8qJjr:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Lyyd0D92f51U`
 A :t:`simple c string literal <simple_c_string_literal>` is any :t:`Unicode <unicode>` character except characters 0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00 (null byte).
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).


:dp:`fls_ggm5FNUqg9EY`
See :s:`SimpleCStringLiteral`.

.. _fls_6mcm7xdcyn40:

simple import
^^^^^^^^^^^^^


:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.


:dp:`fls_OfI70zK68TnQ`
See :s:`SimpleByteStringLiteral`.

.. _fls_fx2hhB0HHSUG:

simple c string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).


:dp:`fls_ggm5FNUqg9EY`
See :s:`SimpleCStringLiteral`.

.. _fls_6mcm7xdcyn40:

simple import
^^^^^^^^^^^^^


:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple import (simple_import)

### Before glossary entry (origin/main)

```rst
.. _fls_6mcm7xdcyn40:

simple import
^^^^^^^^^^^^^

:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.

:dp:`fls_ta5t4h25unsw`
See :s:`SimpleImport`.
```

### After glossary entry (generated)

```rst
.. _fls_2md8pZsvZXXL:

simple import
^^^^^^^^^^^^^

:dp:`fls_B3KHVaUI82YR`
 A :t:`simple import <simple_import>` is a :t:`use import <use_import>` that binds a :t:`simple path <simple_path>` to a local :t:`name` by using an optional :t:`renaming`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).


:dp:`fls_ggm5FNUqg9EY`
See :s:`SimpleCStringLiteral`.

.. _fls_6mcm7xdcyn40:

simple import
^^^^^^^^^^^^^


:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.


:dp:`fls_ta5t4h25unsw`
See :s:`SimpleImport`.

.. _fls_o5kv9lrtz4fq:

simple path
^^^^^^^^^^^


:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qoHXrmds9SgI`
A :dt:`simple c string literal` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
(null byte).


:dp:`fls_ggm5FNUqg9EY`
See :s:`SimpleCStringLiteral`.

.. _fls_6mcm7xdcyn40:

simple import
^^^^^^^^^^^^^


:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.


:dp:`fls_ta5t4h25unsw`
See :s:`SimpleImport`.

.. _fls_o5kv9lrtz4fq:

simple path
^^^^^^^^^^^


:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple path (simple_path)

### Before glossary entry (origin/main)

```rst
.. _fls_o5kv9lrtz4fq:

simple path
^^^^^^^^^^^

:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.

:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.
```

### After glossary entry (generated)

```rst
.. _fls_oD3oBaQYu4aj:

simple path
^^^^^^^^^^^

:dp:`fls_ZsTBxjttVhdj`
 A :t:`simple path <simple_path>` is a :t:`path` whose :t:`path segments <path_segment>` consist of either :t:`identifiers <identifier>` or certain :t:`keywords <keyword>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.


:dp:`fls_ta5t4h25unsw`
See :s:`SimpleImport`.

.. _fls_o5kv9lrtz4fq:

simple path
^^^^^^^^^^^


:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.


:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.

.. _fls_23G6TAntJXqa:

simple path prefix
^^^^^^^^^^^^^^^^^^


:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_jrlzpoauui9g`
A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
local :t:`name` by using an optional :t:`renaming`.


:dp:`fls_ta5t4h25unsw`
See :s:`SimpleImport`.

.. _fls_o5kv9lrtz4fq:

simple path
^^^^^^^^^^^


:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.


:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.

.. _fls_23G6TAntJXqa:

simple path prefix
^^^^^^^^^^^^^^^^^^


:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple path prefix (simple_path_prefix)

### Before glossary entry (origin/main)

```rst
.. _fls_23G6TAntJXqa:

simple path prefix
^^^^^^^^^^^^^^^^^^

:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.

:dp:`fls_ImHceyHhK6OZ`
See :s:`SimplePathPrefix`.
```

### After glossary entry (generated)

```rst
.. _fls_2aaw3xAXtSMJ:

simple path prefix
^^^^^^^^^^^^^^^^^^

:dp:`fls_Nr1IoihJxqjS`
 A :t:`simple path prefix <simple_path_prefix>` is the leading :t:`simple path <simple_path>` of a :t:`glob import <glob_import>` or a :t:`nesting import <nesting_import>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.


:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.

.. _fls_23G6TAntJXqa:

simple path prefix
^^^^^^^^^^^^^^^^^^


:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.


:dp:`fls_ImHceyHhK6OZ`
See :s:`SimplePathPrefix`.

.. _fls_sgy9q06yt6cl:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.


:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.

.. _fls_23G6TAntJXqa:

simple path prefix
^^^^^^^^^^^^^^^^^^


:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.


:dp:`fls_ImHceyHhK6OZ`
See :s:`SimplePathPrefix`.

.. _fls_sgy9q06yt6cl:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple path public modifier (simple_path_public_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_sgy9q06yt6cl:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.

:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.
```

### After glossary entry (generated)

```rst
.. _fls_HDqidxsTOAQi:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_rmlyqyRomhGt`
 A :t:`simple path public modifier <simple_path_public_modifier>` is a :t:`visibility modifier <visibility_modifier>` that grants a :t:`name` :t:`public visibility <public_visibility>` within the provided :t:`simple path <simple_path>` only.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.


:dp:`fls_ImHceyHhK6OZ`
See :s:`SimplePathPrefix`.

.. _fls_sgy9q06yt6cl:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.


:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ijc2yHQuIltY`
A :dt:`simple path prefix` is the leading :t:`simple path` of a
:t:`glob import` or a :t:`nesting import`.


:dp:`fls_ImHceyHhK6OZ`
See :s:`SimplePathPrefix`.

.. _fls_sgy9q06yt6cl:

simple path public modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.


:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple path resolution (simple_path_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.
```

### After glossary entry (generated)

```rst
.. _fls_0lsMdRAEBfMU:

Simple path resolution
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NO72W32wKuLf`
 :t:`Simple path resolution <simple_path_resolution>` is a kind of :t:`path resolution <path_resolution>` that applies to a :t:`simple path <simple_path>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.


:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.


:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple public modifier (simple_public_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.

:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.
```

### After glossary entry (generated)

```rst
.. _fls_rhI7qR03dFGY:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_dfM4iN3iTn8g`
 A :t:`simple public modifier <simple_public_modifier>` is a :t:`visibility modifier <visibility_modifier>` that grants a :t:`name` :t:`public visibility <public_visibility>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.

.. _fls_gT5rZ4qC3pHo:

simple path resolution
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_CQlepoN6PmKq`
:dt:`Simple path resolution` is a kind of :t:`path resolution` that applies to
a :t:`simple path`.

.. _fls_k5uqt5oj7wvl:

simple public modifier
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple register expression (simple_register_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.

:dp:`fls_kKaqHDxPTTUC`
See :s:`SimpleRegisterExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_ueNmTMniwFDq:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_av7opDRTloKM`
 A :t:`simple register expression <simple_register_expression>` is either an :t:`expression` or an :t:`underscore expression <underscore_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.


:dp:`fls_kKaqHDxPTTUC`
See :s:`SimpleRegisterExpression`.

.. _fls_dpod2gc7a0u:

simple string literal
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.


:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.

.. _fls_JDB3eBO0DY4o:

simple register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.


:dp:`fls_kKaqHDxPTTUC`
See :s:`SimpleRegisterExpression`.

.. _fls_dpod2gc7a0u:

simple string literal
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## simple string literal (simple_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_dpod2gc7a0u:

simple string literal
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.

:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_euNGhl8Nv71w:

simple string literal
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_rVNSmNFYdLTU`
 A :t:`simple string literal <simple_string_literal>` is a :t:`string literal <string_literal>` where the characters are :t:`Unicode <unicode>` characters.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.


:dp:`fls_kKaqHDxPTTUC`
See :s:`SimpleRegisterExpression`.

.. _fls_dpod2gc7a0u:

simple string literal
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.


:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4Yp4R7gXucL2`
A :dt:`simple register expression` is either an :t:`expression` or an
:t:`underscore expression`.


:dp:`fls_kKaqHDxPTTUC`
See :s:`SimpleRegisterExpression`.

.. _fls_dpod2gc7a0u:

simple string literal
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.


:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## single segment path (single_segment_path)

### Before glossary entry (origin/main)

```rst
.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^

:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.
```

### After glossary entry (generated)

```rst
.. _fls_fTzqIbtszvMQ:

single segment path
^^^^^^^^^^^^^^^^^^^

:dp:`fls_dIPfXylMbD85`
 A :t:`single segment path <single_segment_path>` is a :t:`path` consisting of exactly one :t:`path segment <path_segment>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.


:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_p6qyyptz8w8w`
A :dt:`simple string literal` is a :t:`string literal` where the characters are
:t:`Unicode` characters.


:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## size (size)

### Before glossary entry (origin/main)

```rst
.. _fls_oy5xy5pm1enx:

size
^^^^

:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.
```

### After glossary entry (generated)

```rst
.. _fls_Su6nlMMKq72q:

size
^^^^

:dp:`fls_ncMCPlw5AoXd`
 The :t:`size` of a :t:`value` is the offset in bytes between successive elements in an :t:`array type <array_type>` with the same :t:`element type <element_type>`, including any padding for :t:`alignment`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_osj0c4dmr6e0`
See :s:`SimpleStringLiteral`.

.. _fls_JS91BDzd03Qj:

single segment path
^^^^^^^^^^^^^^^^^^^


:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## size operand (size_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^

:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.

:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_gttv0NcrcvnH:

size operand
^^^^^^^^^^^^

:dp:`fls_X49ewzYpvmv0`
 A :t:`size operand <size_operand>` is an :t:`operand` that specifies the size of an :t:`array` or an :t:`array type <array_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Hun5BCZsqd6k`
A :dt:`single segment path` is a :t:`path` consisting of exactly one
:t:`path segment`.

.. _fls_oy5xy5pm1enx:

size
^^^^


:dp:`fls_3obnilqhkjux`
The :dt:`size` of a :t:`value` is the offset in bytes between successive
elements in an :t:`array type` with the same :t:`element type`, including any
padding for :t:`alignment`.

.. _fls_2y5oyon3y1za:

size operand
^^^^^^^^^^^^


:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## sized type (sized_type)

### Before glossary entry (origin/main)

```rst
.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^

:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.
```

### After glossary entry (generated)

```rst
.. _fls_xkjcBVewlmx1:

sized type
^^^^^^^^^^

:dp:`fls_ZK6fAgXK91jS`
 A :t:`sized type <sized_type>` is a :t:`type` with statically known size.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_srajsqi5i3py`
A :dt:`size operand` is an :t:`operand` that specifies the size of an
:t:`array` or an :t:`array type`.


:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## slice (slice)

### Before glossary entry (origin/main)

```rst
.. _fls_srkftses9sxn:

slice
^^^^^

:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.
```

### After glossary entry (generated)

```rst
.. _fls_88v2nuBM98L8:

slice
^^^^^

:dp:`fls_lSQX4njr36BT`
 A :t:`slice` is a :t:`value` of a :t:`slice type <slice_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_228ioayvdguv`
See :s:`SizeOperand`.

.. _fls_oiaoWEQQDE7I:

sized type
^^^^^^^^^^


:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## slice pattern (slice_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^

:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.

:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_XNCxvnzydLmB:

slice pattern
^^^^^^^^^^^^^

:dp:`fls_TLlZATXLzpd6`
 A :t:`slice pattern <slice_pattern>` is a :t:`pattern` that matches :t:`arrays <array>` of fixed size and :t:`slices <slice>` of dynamic size.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^


:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.

.. _fls_srkftses9sxn:

slice
^^^^^


:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.

.. _fls_1s3a31o9zx1a:

slice pattern
^^^^^^^^^^^^^


:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^


:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## slice type (slice_type)

### Before glossary entry (origin/main)

```rst
.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^

:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.

:dp:`fls_y7gscwf29htg`
See :s:`SliceTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_jp3BJegdPuz5:

slice type
^^^^^^^^^^

:dp:`fls_3LMAk8aF1hgO`
 A :t:`slice type <slice_type>` is a :t:`sequence type <sequence_type>` that provides a view into a sequence of elements.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^


:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.


:dp:`fls_y7gscwf29htg`
See :s:`SliceTypeSpecification`.

.. _fls_wlwwxzpnhk6i:

source file
^^^^^^^^^^^


:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7613qu4igwiw`
A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed
size and :t:`[slice]s` of dynamic size.


:dp:`fls_3qey00280x27`
See :s:`SlicePattern`.

.. _fls_x3kr88m5gvwv:

slice type
^^^^^^^^^^


:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.


:dp:`fls_y7gscwf29htg`
See :s:`SliceTypeSpecification`.

.. _fls_wlwwxzpnhk6i:

source file
^^^^^^^^^^^


:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## source file (source_file)

### Before glossary entry (origin/main)

```rst
.. _fls_wlwwxzpnhk6i:

source file
^^^^^^^^^^^

:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.

:dp:`fls_zgh1m5357ex1`
See :s:`SourceFile`.
```

### After glossary entry (generated)

```rst
.. _fls_fv8MKbTgnW4a:

source file
^^^^^^^^^^^

:dp:`fls_f4Mgwsr1L6pv`
 A :t:`source file <source_file>` contains the program text of :t:`inner attributes <inner_attribute>`, :t:`inner doc comments <inner_doc_comment>`, and :t:`items <item>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.


:dp:`fls_y7gscwf29htg`
See :s:`SliceTypeSpecification`.

.. _fls_wlwwxzpnhk6i:

source file
^^^^^^^^^^^


:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.


:dp:`fls_zgh1m5357ex1`
See :s:`SourceFile`.

.. _fls_e7cvo0usw86i:

statement
^^^^^^^^^


:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bvpszep1w90g`
A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
of elements.


:dp:`fls_y7gscwf29htg`
See :s:`SliceTypeSpecification`.

.. _fls_wlwwxzpnhk6i:

source file
^^^^^^^^^^^


:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.


:dp:`fls_zgh1m5357ex1`
See :s:`SourceFile`.

.. _fls_e7cvo0usw86i:

statement
^^^^^^^^^


:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## statement (statement)

### Before glossary entry (origin/main)

```rst
.. _fls_e7cvo0usw86i:

statement
^^^^^^^^^

:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.

:dp:`fls_th7edvxml3mn`
See :s:`Statement`.
```

### After glossary entry (generated)

```rst
.. _fls_eSbWasVQOiEG:

statement
^^^^^^^^^

:dp:`fls_JlnOUsh5SSvj`
 A :t:`statement` is a component of a block expression.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.


:dp:`fls_zgh1m5357ex1`
See :s:`SourceFile`.

.. _fls_e7cvo0usw86i:

statement
^^^^^^^^^


:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.


:dp:`fls_th7edvxml3mn`
See :s:`Statement`.

.. _fls_tpazbmuq9hag:

static
^^^^^^


:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_nh737q4mn27u`
A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
:t:`[inner doc comment]s`, and :t:`[item]s`.


:dp:`fls_zgh1m5357ex1`
See :s:`SourceFile`.

.. _fls_e7cvo0usw86i:

statement
^^^^^^^^^


:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.


:dp:`fls_th7edvxml3mn`
See :s:`Statement`.

.. _fls_tpazbmuq9hag:

static
^^^^^^


:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## static (static)

### Before glossary entry (origin/main)

```rst
.. _fls_tpazbmuq9hag:

static
^^^^^^

:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.

:dp:`fls_1b7gpk8e98pw`
See :s:`StaticDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_gLtmV893XCu9:

static
^^^^^^

:dp:`fls_KLeYehDyGmEn`
 A :t:`static` is a :t:`value` that is associated with a specific memory location.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.


:dp:`fls_th7edvxml3mn`
See :s:`Statement`.

.. _fls_tpazbmuq9hag:

static
^^^^^^


:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.


:dp:`fls_1b7gpk8e98pw`
See :s:`StaticDeclaration`.

.. _fls_x331kxllyzim:

static initializer
^^^^^^^^^^^^^^^^^^


:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.


:dp:`fls_th7edvxml3mn`
See :s:`Statement`.

.. _fls_tpazbmuq9hag:

static
^^^^^^


:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.


:dp:`fls_1b7gpk8e98pw`
See :s:`StaticDeclaration`.

.. _fls_x331kxllyzim:

static initializer
^^^^^^^^^^^^^^^^^^


:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## static initializer (static_initializer)

### Before glossary entry (origin/main)

```rst
.. _fls_x331kxllyzim:

static initializer
^^^^^^^^^^^^^^^^^^

:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.

:dp:`fls_igbl5uv0dlhl`
See :s:`StaticInitializer`.
```

### After glossary entry (generated)

```rst
.. _fls_mCn0NsWCN6TI:

static initializer
^^^^^^^^^^^^^^^^^^

:dp:`fls_rib00yM66P23`
 A :t:`static initializer <static_initializer>` is a :t:`construct` that provides the :t:`value` of its related :t:`static`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.


:dp:`fls_1b7gpk8e98pw`
See :s:`StaticDeclaration`.

.. _fls_x331kxllyzim:

static initializer
^^^^^^^^^^^^^^^^^^


:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.


:dp:`fls_igbl5uv0dlhl`
See :s:`StaticInitializer`.

.. _fls_jCqiKgW9g8n5:

static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_srx4v1e20yxa`
A :dt:`static` is a :t:`value` that is associated with a specific memory
location.


:dp:`fls_1b7gpk8e98pw`
See :s:`StaticDeclaration`.

.. _fls_x331kxllyzim:

static initializer
^^^^^^^^^^^^^^^^^^


:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.


:dp:`fls_igbl5uv0dlhl`
See :s:`StaticInitializer`.

.. _fls_jCqiKgW9g8n5:

static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## static lifetime elision (static_lifetime_elision)

### Before glossary entry (origin/main)

```rst
.. _fls_jCqiKgW9g8n5:

static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.
```

### After glossary entry (generated)

```rst
.. _fls_uPzjbV6zDmSB:

Static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_F7QGRXZtEJzb`
 :t:`Static lifetime elision <static_lifetime_elision>` is a form of :t:`lifetime elision <lifetime_elision>` that applies to :t:`constants <constant>` and :t:`statics <static>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.


:dp:`fls_igbl5uv0dlhl`
See :s:`StaticInitializer`.

.. _fls_jCqiKgW9g8n5:

static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^


:dp:`fls_6977zxb0resa`
:dc:`str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit
unsigned bytes.

.. _fls_bzhaq3q378ay:

strict keyword
^^^^^^^^^^^^^^


:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6jjbfni87tax`
A :dt:`static initializer` is a :t:`construct` that provides the :t:`value` of
its related :t:`static`.


:dp:`fls_igbl5uv0dlhl`
See :s:`StaticInitializer`.

.. _fls_jCqiKgW9g8n5:

static lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^


:dp:`fls_6977zxb0resa`
:dc:`str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit
unsigned bytes.

.. _fls_bzhaq3q378ay:

strict keyword
^^^^^^^^^^^^^^


:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## str (str)

### Before glossary entry (origin/main)

```rst
.. _fls_1ricdj86o457:

str
^^^

:dp:`fls_6977zxb0resa`
:dc:`str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit
unsigned bytes.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters.
```

### After chapter excerpt (current)

```rst
Definition missing in current chapters.
```

### Role classification

no definition roles detected

### Standalone edits

Definition missing.

## strict keyword (strict_keyword)

### Before glossary entry (origin/main)

```rst
.. _fls_bzhaq3q378ay:

strict keyword
^^^^^^^^^^^^^^

:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.

:dp:`fls_67pzayd9qzzs`
See :s:`StrictKeyword`.
```

### After glossary entry (generated)

```rst
.. _fls_3oHmNw0t4xDU:

strict keyword
^^^^^^^^^^^^^^

:dp:`fls_OD4MWNUMMAeZ`
 A :t:`strict keyword <strict_keyword>` is a :t:`keyword` that always holds its special meaning.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^


:dp:`fls_6977zxb0resa`
:dc:`str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit
unsigned bytes.

.. _fls_bzhaq3q378ay:

strict keyword
^^^^^^^^^^^^^^


:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.


:dp:`fls_67pzayd9qzzs`
See :s:`StrictKeyword`.

.. _fls_cck2tmyzmpja:

string literal
^^^^^^^^^^^^^^


:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_NbVewjYRnQPF`
:dt:`Static lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[constant]s` and :t:`[static]s`.

.. _fls_1ricdj86o457:

str
^^^


:dp:`fls_6977zxb0resa`
:dc:`str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit
unsigned bytes.

.. _fls_bzhaq3q378ay:

strict keyword
^^^^^^^^^^^^^^


:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.


:dp:`fls_67pzayd9qzzs`
See :s:`StrictKeyword`.

.. _fls_cck2tmyzmpja:

string literal
^^^^^^^^^^^^^^


:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## string literal (string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_cck2tmyzmpja:

string literal
^^^^^^^^^^^^^^

:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.

:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_oMXQ0alEVVkZ:

string literal
^^^^^^^^^^^^^^

:dp:`fls_oT8gUsi72vsT`
 A :t:`string literal <string_literal>` is a :t:`literal` that consists of multiple characters.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.


:dp:`fls_67pzayd9qzzs`
See :s:`StrictKeyword`.

.. _fls_cck2tmyzmpja:

string literal
^^^^^^^^^^^^^^


:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.


:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hza9spr6behn`
A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.


:dp:`fls_67pzayd9qzzs`
See :s:`StrictKeyword`.

.. _fls_cck2tmyzmpja:

string literal
^^^^^^^^^^^^^^


:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.


:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct (struct)

### Before glossary entry (origin/main)

```rst
.. _fls_yphnf56fa58r:

struct
^^^^^^

:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.
```

### After glossary entry (generated)

```rst
.. _fls_8TKMSqI7swU4:

struct
^^^^^^

:dp:`fls_gCWxtyZAWTOT`
 A :t:`struct` is an :t:`item` that declares a :t:`struct type <struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.


:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^


:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_dphk5br0ag35`
A :dt:`string literal` is a :t:`literal` that consists of multiple characters.


:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^


:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct expression (struct_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^

:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.

:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_kCBbilay8zlK:

struct expression
^^^^^^^^^^^^^^^^^

:dp:`fls_U45Mj0xyiNnG`
 A :t:`struct expression <struct_expression>` is an :t:`expression` that constructs an :t:`enum value <enum_value>`, a :t:`struct value <struct_value>`, or a :t:`union value <union_value>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^


:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_z0t3ae24h5h5`
See :s:`StringLiteral`.

.. _fls_yphnf56fa58r:

struct
^^^^^^


:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.

.. _fls_dxfyejkbiz3p:

struct expression
^^^^^^^^^^^^^^^^^


:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct field (struct_field)

### Before glossary entry (origin/main)

```rst
.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^

:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.
```

### After glossary entry (generated)

```rst
.. _fls_nqesUmJDRfel:

struct field
^^^^^^^^^^^^

:dp:`fls_mQ7eTZPZZSMs`
 A :t:`struct field <struct_field>` is a :t:`field` of a :t:`struct type <struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^


:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_m8n9e0sxyb95`
A :dt:`struct expression` is an :t:`expression` that constructs an
:t:`enum value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^


:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct pattern (struct_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^

:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.

:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_18kzNz4X6Ww7:

struct pattern
^^^^^^^^^^^^^^

:dp:`fls_XIuFbyN7DVud`
 A :t:`struct pattern <struct_pattern>` is a :t:`pattern` that matches an :t:`enum value <enum_value>`, a :t:`struct value <struct_value>`, or a :t:`union value <union_value>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^


:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^


:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_odm68rhu2j1`
See :s:`StructExpression`.

.. _fls_OT6dJ7CWkSTG:

struct field
^^^^^^^^^^^^


:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.

.. _fls_ook43xes5t34:

struct pattern
^^^^^^^^^^^^^^


:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^


:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct type (struct_type)

### Before glossary entry (origin/main)

```rst
.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^

:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_bSREq9zKmUM7:

struct type
^^^^^^^^^^^

:dp:`fls_GwgOsMWzuZe2`
 A :t:`struct type <struct_type>` is an :t:`abstract data type <abstract_data_type>` that is a product of other :t:`types <type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^


:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.


:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_xbtoiwegp8gu`
A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.


:dp:`fls_pn8e50ep2fln`
See :s:`StructPattern`.

.. _fls_pzj88ust6qrq:

struct type
^^^^^^^^^^^


:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.


:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## struct value (struct_value)

### Before glossary entry (origin/main)

```rst
.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^

:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.
```

### After glossary entry (generated)

```rst
.. _fls_Ip1k9Sho8NxK:

struct value
^^^^^^^^^^^^

:dp:`fls_1LBdH8fsIKMq`
 A :t:`struct value <struct_value>` is a :t:`value` of a :t:`struct type <struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.


:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7v4dhh3nl8h9`
A :dt:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.


:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## structurally equal (structurally_equal)

### Before glossary entry (origin/main)

```rst
.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^

:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_dhlww4yrnb2v`
See :s:`StructDeclaration`.


.. _fls_GOnQHAsYw1oi:

struct value
^^^^^^^^^^^^


:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subexpression (subexpression)

### Before glossary entry (origin/main)

```rst
.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^

:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.
```

### After glossary entry (generated)

```rst
.. _fls_V73VBE1kpoie:

subexpression
^^^^^^^^^^^^^

:dp:`fls_YIHLLV6Pu4AI`
 A :t:`subexpression` is an :t:`expression` nested within another :t:`expression`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.

.. _fls_P7920ALJisrH:

structurally equal
^^^^^^^^^^^^^^^^^^


:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subject expression (subject_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^

:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.

:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_Ms1XTaqwyADi:

subject expression
^^^^^^^^^^^^^^^^^^

:dp:`fls_v5Il7eZiXWMM`
 A :t:`subject expression <subject_expression>` is an :t:`expression` that controls :t:`for loops <for_loop>`, :t:`if expressions <if_expression>`, and :t:`match expressions <match_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_glRZUKhmaWmP`
A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
for equality by structure.

.. _fls_feZ3iDff05Cb:

subexpression
^^^^^^^^^^^^^


:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.

.. _fls_wee9stfk0abp:

subject expression
^^^^^^^^^^^^^^^^^^


:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subject let expression (subject_let_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_WYZnwK9WI9Wj:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_CYHhAVGxzh02`
 A :t:`subject let expression <subject_let_expression>` is an :t:`expression` that controls :t:`if let expressions <if_let_expression>` and :t:`while let loops <while_let_loop>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.


:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.


:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.

.. _fls_dc5ibvnnhs7e:

subject let expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.


:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subpattern (subpattern)

### Before glossary entry (origin/main)

```rst
.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^

:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.
```

### After glossary entry (generated)

```rst
.. _fls_aANTiMzpYfdq:

subpattern
^^^^^^^^^^

:dp:`fls_NWi0BEUQwMWy`
 A :t:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.


:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.


:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtraction assignment (subtraction_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.
```

### After glossary entry (generated)

```rst
.. _fls_uXfr82ODF3QM:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_W51B3RHjWM2y`
 For :t:`subtraction assignment <subtraction_assignment>`, see :t:`subtraction assignment <subtraction_assignment>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.

.. _fls_k7ro8n23wtdc:

subpattern
^^^^^^^^^^


:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtraction assignment expression (subtraction_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.

:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_GkMkeEq1Aaqh:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_mxX14avBhauv`
 A :t:`subtraction assignment expression <subtraction_assignment_expression>` is a :t:`compound assignment expression <compound_assignment_expression>` that uses subtraction.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_942ulj9qsdes`
A :dt:`subpattern` is a :t:`pattern` nested within another :t:`pattern`.

.. _fls_0hf1gNf90qKr:

subtraction assignment
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. _fls_a4iu72zn4h0:

subtraction assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtraction expression (subtraction_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.

:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_BRAemqVkJLTQ:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Hk4nu5FxTuks`
 A :t:`subtraction expression <subtraction_expression>` is an :t:`arithmetic expression <arithmetic_expression>` that uses subtraction.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.


:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4pb85nl4r7vs`
A :dt:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.


:dp:`fls_mye9yj5tc8hr`
See :s:`SubtractionAssignmentExpression`.

.. _fls_25ru96mfdcsn:

subtraction expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.


:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtrait (subtrait)

### Before glossary entry (origin/main)

```rst
.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^

:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.
```

### After glossary entry (generated)

```rst
.. _fls_BH0n84hys5Vt:

subtrait
^^^^^^^^

:dp:`fls_evqxBU3kS3DW`
 A :t:`subtrait` is a :t:`trait` with a :t:`supertrait`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.


:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_caamjgpw59id`
A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
subtraction.


:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtype (subtype)

### Before glossary entry (origin/main)

```rst
.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^

:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.
```

### After glossary entry (generated)

```rst
.. _fls_edhaTI9cIa3I:

subtype
^^^^^^^

:dp:`fls_1nV0W7lo1sjK`
 A :t:`subtype` is a :t:`type` with additional constraints.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mx3olnbntpye`
See :s:`SubtractionExpression`.

.. _fls_qw3fn1116se9:

subtrait
^^^^^^^^


:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## subtyping (subtyping)

### Before glossary entry (origin/main)

```rst
.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^

:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.
```

### After glossary entry (generated)

```rst
.. _fls_Oahf6UaAlHxs:

Subtyping
^^^^^^^^^

:dp:`fls_w6Z53fUrHbKg`
 :t:`Subtyping <subtyping>` is a property of :t:`types <type>`, allowing one :t:`type` to be used where another :t:`type` is expected.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wnj95vozis6n`
A :dt:`subtrait` is a :t:`trait` with a :t:`supertrait`.

.. _fls_pu4zqJ1tGrfH:

subtype
^^^^^^^


:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## suffixed float (suffixed_float)

### Before glossary entry (origin/main)

```rst
.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^

:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.
```

### After glossary entry (generated)

```rst
.. _fls_TLowBTwUVNqm:

suffixed float
^^^^^^^^^^^^^^

:dp:`fls_1RSK0XMoh9FT`
 A :t:`suffixed float <suffixed_float>` is a :t:`float literal <float_literal>` with a :t:`float suffix <float_suffix>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.

.. _fls_f5dxz8pvs1kz:

subtyping
^^^^^^^^^


:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## suffixed integer (suffixed_integer)

### Before glossary entry (origin/main)

```rst
.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^

:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.
```

### After glossary entry (generated)

```rst
.. _fls_DWsMsg4Dnzhg:

suffixed integer
^^^^^^^^^^^^^^^^

:dp:`fls_3YnrmSZ08ApM`
 A :t:`suffixed integer <suffixed_integer>` is an :t:`integer literal <integer_literal>` with an :t:`integer suffix <integer_suffix>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bo5xzjsdd3lj`
:dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be
used where another :t:`type` is expected.

.. _fls_qar9v52smi9j:

suffixed float
^^^^^^^^^^^^^^


:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## super public modifier (super_public_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.

:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.
```

### After glossary entry (generated)

```rst
.. _fls_GAExJ72cDrG4:

super public modifier
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_qviT0CHdzrs0`
 A :t:`super public modifier <super_public_modifier>` is a :t:`visibility modifier <visibility_modifier>` that grants a :t:`name` :t:`public visibility <public_visibility>` within the parent :t:`module` only.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7reb4jp0x1wf`
A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. _fls_bmbu11ycjpor:

suffixed integer
^^^^^^^^^^^^^^^^


:dp:`fls_ltzetxu3sq7k`
A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. _fls_12bluakt0jnj:

super public modifier
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## supertrait (supertrait)

### Before glossary entry (origin/main)

```rst
.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^

:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.
```

### After glossary entry (generated)

```rst
.. _fls_yCAiejsWYEyh:

supertrait
^^^^^^^^^^

:dp:`fls_K6GPIBnJblOd`
 A :t:`supertrait` is a transitive :t:`trait` that a :t:`type` must additionally implement.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.


:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## sync type (sync_type)

### Before glossary entry (origin/main)

```rst
.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^

:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.
```

### After glossary entry (generated)

```rst
.. _fls_07WJcqonYfHa:

sync type
^^^^^^^^^

:dp:`fls_lyiyePAcyloE`
 A :t:`sync type <sync_type>` is a :t:`type` that implements the `core::marker::Sync <https://doc.rust-lang.org/stable/std/?search=core%3A%3Amarker%3A%3ASync>`__ :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^


:dp:`fls_6k873f1knasi`
A :dt:`tail expression` is the last :t:`expression` within a
:t:`block expression`.

.. _fls_4omay4i65dwz:

temporary
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.

.. _fls_1axcyv628aov:

supertrait
^^^^^^^^^^


:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^


:dp:`fls_6k873f1knasi`
A :dt:`tail expression` is the last :t:`expression` within a
:t:`block expression`.

.. _fls_4omay4i65dwz:

temporary
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## syntactic category (syntactic_category)

### Before glossary entry (origin/main)

```rst
.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^

:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.
```

### After glossary entry (generated)

```rst
.. _fls_lSWGwVskklgr:

syntactic category
^^^^^^^^^^^^^^^^^^

:dp:`fls_wGoJpeMv6moX`
 A :t:`syntactic category <syntactic_category>` is a nonterminal in the Backus-Naur Form grammar definition of the Rust programming language.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^


:dp:`fls_6k873f1knasi`
A :dt:`tail expression` is the last :t:`expression` within a
:t:`block expression`.

.. _fls_4omay4i65dwz:

temporary
^^^^^^^^^


:dp:`fls_fathkxu9kxvw`
A :dt:`temporary` is an anonymous :t:`variable` produced by some intermediate
computation.

.. _fls_ihv02usuziw8:

terminated
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_s4chur1wutwh`
A :dt:`supertrait` is a transitive :t:`trait` that a :t:`type` must
additionally implement.

.. _fls_r4eoz3ohvpdi:

sync type
^^^^^^^^^


:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

.. _fls_44djv0wocacs:

syntactic category
^^^^^^^^^^^^^^^^^^


:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.

.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^


:dp:`fls_6k873f1knasi`
A :dt:`tail expression` is the last :t:`expression` within a
:t:`block expression`.

.. _fls_4omay4i65dwz:

temporary
^^^^^^^^^


:dp:`fls_fathkxu9kxvw`
A :dt:`temporary` is an anonymous :t:`variable` produced by some intermediate
computation.

.. _fls_ihv02usuziw8:

terminated
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
