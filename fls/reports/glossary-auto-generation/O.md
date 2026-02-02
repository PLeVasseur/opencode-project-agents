# Glossary audit O

## Per-letter checklist
- Letter: O
- [ ] Reconcile O terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate O terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for O
- [ ] Update `migration-checklist.md` for all O terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint O migration`
- [ ] Letter complete

## Term checklist
- [x] object safe (object_safe)
- [ ] object safety (object_safety)
- [ ] obsolete range pattern (obsolete_range_pattern)
- [ ] octal literal (octal_literal)
- [ ] operand (operand)
- [ ] operator expression (operator_expression)
- [ ] opt-out trait bound (opt_out_trait_bound)
- [ ] or-pattern (or_pattern)
- [ ] outer attribute (outer_attribute)
- [ ] outer block doc (outer_block_doc)
- [ ] outer doc comment (outer_doc_comment)
- [ ] outer line doc (outer_line_doc)
- [ ] outline module (outline_module)
- [ ] outlives bound (outlives_bound)
- [ ] output register (output_register)
- [ ] output register expression (output_register_expression)
- [x] overlap (overlap)
- [ ] owner (owner)
- [ ] ownership (ownership)

## object safe (object_safe)

### Before glossary entry (origin/main)

```rst
.. _fls_a226qzrb4iq9:

object safe
^^^^^^^^^^^

:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_QYDZm7pKy1nW`
See :s:`LiteralPattern`.

.. _fls_rayjriyofmpa:

numeric type
^^^^^^^^^^^^


:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.

.. _fls_a226qzrb4iq9:

object safe
^^^^^^^^^^^


:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_QYDZm7pKy1nW`
See :s:`LiteralPattern`.

.. _fls_rayjriyofmpa:

numeric type
^^^^^^^^^^^^


:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.

.. _fls_a226qzrb4iq9:

object safe
^^^^^^^^^^^


:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## object safety (object_safety)

### Before glossary entry (origin/main)

```rst
.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^

:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.
```

### After glossary entry (generated)

```rst
.. _fls_zltJwL3Kxxb7:

Object safety
^^^^^^^^^^^^^

:dp:`fls_40gFKLQFWnwd`
 :t:`Object safety <object_safety>` is the process of determining whether a :t:`trait` can be used as a :t:`trait object type <trait_object_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.

.. _fls_a226qzrb4iq9:

object safe
^^^^^^^^^^^


:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.

.. _fls_a226qzrb4iq9:

object safe
^^^^^^^^^^^


:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## obsolete range pattern (obsolete_range_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.

:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_JVmbihVMRiCh:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wjWftWEeS6Ib`
 An :t:`obsolete range pattern <obsolete_range_pattern>` is a :t:`range pattern <range_pattern>` that uses obsolete syntax to express an :t:`inclusive range pattern <inclusive_range_pattern>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^


:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_oa2jiklr5nl2`
A :t:`trait` is :dt:`object safe` when it can be used as a
:t:`trait object type`.

.. _fls_vomlqv7i1fc4:

object safety
^^^^^^^^^^^^^


:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.

.. _fls_bo889w63y7oi:

obsolete range pattern
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^


:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## octal literal (octal_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^

:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.

:dp:`fls_8u0n6xu0mizm`
See ``OctalLiteral.``
```

### After glossary entry (generated)

```rst
.. _fls_yJh1QW0fBvMZ:

octal literal
^^^^^^^^^^^^^

:dp:`fls_4JJ2HsWeLKMe`
 An :t:`octal literal <octal_literal>` is an :t:`integer literal <integer_literal>` in base 8.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^


:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.


:dp:`fls_8u0n6xu0mizm`
See ``OctalLiteral.``

.. _fls_pv4lok5qcn8y:

operand
^^^^^^^


:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ave42vwb45zb`
An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete
syntax to express an :t:`inclusive range pattern`.


:dp:`fls_ta0wa8ta9ol4`
See :s:`ObsoleteRangePattern`.

.. _fls_q47u2zq6clon:

octal literal
^^^^^^^^^^^^^


:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.


:dp:`fls_8u0n6xu0mizm`
See ``OctalLiteral.``

.. _fls_pv4lok5qcn8y:

operand
^^^^^^^


:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## operand (operand)

### Before glossary entry (origin/main)

```rst
.. _fls_pv4lok5qcn8y:

operand
^^^^^^^

:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.

:dp:`fls_8299xfhdsd1`
See :s:`Operand`.
```

### After glossary entry (generated)

```rst
.. _fls_jW7xdmwoBj0c:

u8-to-char cast
^^^^^^^^^^^^^^^

:dp:`fls_Nx1wim8wJK6M`
 An :t:`operand` of :t:`type` :c:`u8` and a target :t:`type` :c:`char` performs :t:`u8-to-char cast <u8_to_char_cast>`. A :t:`u8-to-char cast <u8_to_char_cast>` converts an :t:`operand` of :t:`type` :c:`u8` to the :t:`value` of the corresponding :t:`code point <code_point>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.


:dp:`fls_8u0n6xu0mizm`
See ``OctalLiteral.``

.. _fls_pv4lok5qcn8y:

operand
^^^^^^^


:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.


:dp:`fls_8299xfhdsd1`
See :s:`Operand`.

.. _fls_smk8mi72lt57:

operator expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pf4341vnqiin`
An :dt:`octal literal` is an :t:`integer literal` in base 8.


:dp:`fls_8u0n6xu0mizm`
See ``OctalLiteral.``

.. _fls_pv4lok5qcn8y:

operand
^^^^^^^


:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.


:dp:`fls_8299xfhdsd1`
See :s:`Operand`.

.. _fls_smk8mi72lt57:

operator expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## operator expression (operator_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_smk8mi72lt57:

operator expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.

:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_Yb9kNwtY9txC:

operator expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_QInGhUulo5Ud`
 An :t:`operator expression <operator_expression>` is an :t:`expression` that involves an operator.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.


:dp:`fls_8299xfhdsd1`
See :s:`Operand`.

.. _fls_smk8mi72lt57:

operator expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.


:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_3mnn1au9ob6q`
An :dt:`operand` is an :t:`expression` nested within an expression.


:dp:`fls_8299xfhdsd1`
See :s:`Operand`.

.. _fls_smk8mi72lt57:

operator expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.


:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## opt-out trait bound (opt_out_trait_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^

:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.
```

### After glossary entry (generated)

```rst
.. _fls_tm5Wq0zcIJAy:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^

:dp:`fls_yq7nYnHgK81m`
 An :t:`opt-out trait bound <opt_out_trait_bound>` is a :t:`trait bound <trait_bound>` with :s:`Punctuation <punctuation>` ``?`` that nullifies an implicitly added :t:`trait bound <trait_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.


:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^


:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6ev01xwcfow1`
An :dt:`operator expression` is an :t:`expression` that involves an operator.


:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^


:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## or-pattern (or_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^

:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).

:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.
```

### After glossary entry (generated)

```rst
.. _fls_JJ3glV0crNwI:

or-pattern
^^^^^^^^^^

:dp:`fls_pOR930VPvFUi`
 An :t:`or-pattern <or_pattern>` is a :t:`pattern` that matches on one of two or more :t:`pattern-without-alternations <pattern_without_alternation>` and or-s them using character 0x7C (vertical line, i.e. ``|``).
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^


:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^


:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qdszbyeuo7w1`
See :s:`OperatorExpression`.

.. _fls_C5DiCsvsaBsj:

opt-out trait bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.


.. _fls_LnPDQW3bnNUw:

or-pattern
^^^^^^^^^^


:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^


:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outer attribute (outer_attribute)

### Before glossary entry (origin/main)

```rst
.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^

:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.

:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.
```

### After glossary entry (generated)

```rst
.. _fls_D832N2AbuZ1K:

outer attribute
^^^^^^^^^^^^^^^

:dp:`fls_Ij0AjsWCllse`
 An :t:`outer attribute <outer_attribute>` is an :t:`attribute` that applies to a subsequent :t:`item`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^


:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.


:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.

.. _fls_toncretg92qh:

outer block doc
^^^^^^^^^^^^^^^


:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_LnPDQW3bnNUw`
An :dt:`or-pattern` is a :t:`pattern` that matches on one of two or more :t:`[pattern-without-alternation]s` and or-s them using character 0x7C (vertical line, i.e. ``|``).


:dp:`fls_urIJ5JNHLhm6`
See :s:`Pattern`.

.. _fls_gllzixm9yt9w:

outer attribute
^^^^^^^^^^^^^^^


:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.


:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.

.. _fls_toncretg92qh:

outer block doc
^^^^^^^^^^^^^^^


:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outer block doc (outer_block_doc)

### Before glossary entry (origin/main)

```rst
.. _fls_toncretg92qh:

outer block doc
^^^^^^^^^^^^^^^

:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.
```

### After glossary entry (generated)

```rst
.. _fls_dXYssUZYbLcg:

outer block doc
^^^^^^^^^^^^^^^

:dp:`fls_vd2RWkgyBs9l`
 An :t:`outer block doc <outer_block_doc>` is a :t:`block comment <block_comment>` that applies to a subsequent :t:`non-comment <comment>` :t:`construct`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.


:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.

.. _fls_toncretg92qh:

outer block doc
^^^^^^^^^^^^^^^


:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.


:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.

.. _fls_toncretg92qh:

outer block doc
^^^^^^^^^^^^^^^


:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outer doc comment (outer_doc_comment)

### Before glossary entry (origin/main)

```rst
.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^

:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.
```

### After glossary entry (generated)

```rst
.. _fls_Zvu02PBQfBg6:

outer doc comment
^^^^^^^^^^^^^^^^^

:dp:`fls_4fShnpooyjiN`
 An :t:`outer doc comment <outer_doc_comment>` is either an :t:`outer block doc <outer_block_doc>` or an :t:`outer line doc <outer_line_doc>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^


:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_531ggn1f8f6u`
An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^


:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outer line doc (outer_line_doc)

### Before glossary entry (origin/main)

```rst
.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^

:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.
```

### After glossary entry (generated)

```rst
.. _fls_T9uSyY2VT6rs:

outer line doc
^^^^^^^^^^^^^^

:dp:`fls_Lay8VzZ8K8ok`
 An :t:`outer line doc <outer_line_doc>` is a :t:`line comment <line_comment>` that applies to a subsequent :t:`non-comment <comment>` :t:`construct`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^


:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^


:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ddy9a66tpytp`
See :s:`OuterBlockDoc`.

.. _fls_PuTD100sWO5N:

outer doc comment
^^^^^^^^^^^^^^^^^


:dp:`fls_mgSEUNUPcPBs`
An :dt:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

.. _fls_eqjbv8sovvfl:

outer line doc
^^^^^^^^^^^^^^


:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^


:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outline module (outline_module)

### Before glossary entry (origin/main)

```rst
.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^

:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.

:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_UwFjZ5mp5fIq:

outline module
^^^^^^^^^^^^^^

:dp:`fls_yLm2CqWwRZ6v`
 An :t:`outline module <outline_module>` is a :t:`module` with an :s:`OutlineModuleSpecification <outlinemodulespecification>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^


:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.


:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_m3u30fu8uac3`
An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.


:dp:`fls_1ppwidw7szk5`
See :s:`OuterLineDoc`.

.. _fls_de935b1pzd28:

outline module
^^^^^^^^^^^^^^


:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.


:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## outlives bound (outlives_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^

:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.
```

### After glossary entry (generated)

```rst
.. _fls_3d1phiPhMU0c:

outlives bound
^^^^^^^^^^^^^^

:dp:`fls_2V0Pf7B1nEps`
 An :t:`outlives bound <outlives_bound>` is a :t:`trait bound <trait_bound>` which requires that a :t:`generic parameter <generic_parameter>` outlives a :t:`lifetime parameter <lifetime_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.


:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.


:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## output register (output_register)

### Before glossary entry (origin/main)

```rst
.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^

:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.
```

### After glossary entry (generated)

```rst
.. _fls_IwQ4st4bzFkj:

output register
^^^^^^^^^^^^^^^

:dp:`fls_YFYMDTZn3R2m`
 An :t:`output register <output_register>` is a :t:`register` whose :t:`register name <register_name>` is used in a :t:`register argument <register_argument>` subject to :t:`direction modifier <direction_modifier>` ``out``, ``lateout``, ``inout``, or ``inlateout``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wu5wqylzx9ke`
See :s:`OutlineModuleSpecification`.

.. _fls_5LhIr1kOIEO5:

outlives bound
^^^^^^^^^^^^^^


:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## output register expression (output_register_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.

:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_23ZTJyC2IjNZ:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_d6ISsgaQG81H`
 An :t:`output register expression <output_register_expression>` is an :t:`expression` that is assigned the :t:`value` of a :t:`register`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_J5dt34II7Pm6`
An :dt:`outlives bound` is a :t:`trait bound` which requires that a
:t:`generic parameter` outlives a :t:`lifetime parameter`.

.. _fls_XsGnaA47Nen0:

output register
^^^^^^^^^^^^^^^


:dp:`fls_4METI8qE9JiY`
An :dt:`output register` is a :t:`register` whose :t:`register name` is
used in a :t:`register argument` subject to :t:`direction modifier` ``out``,
``lateout``, ``inout``, or ``inlateout``.

.. _fls_t79aKPilX8jk:

output register expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## overlap (overlap)

### Before glossary entry (origin/main)

```rst
.. _fls_nhamq7xtz384:

overlap
^^^^^^^

:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_w95YRZ4JjBxl`
An :dt:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.


:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## owner (owner)

### Before glossary entry (origin/main)

```rst
.. _fls_ke52l9lsvyu2:

owner
^^^^^

:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_LPfzVWtc9UKO:

owner
^^^^^

:dp:`fls_h4GYj02usDZO`
 An :t:`owner` is a :t:`variable` that holds a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8B3ldFZVy7PA`
See :s:`OutputRegisterExpression`.

.. _fls_nhamq7xtz384:

overlap
^^^^^^^


:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## ownership (ownership)

### Before glossary entry (origin/main)

```rst
.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^

:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.
```

### After glossary entry (generated)

```rst
.. _fls_KTgCVYxe9jLg:

Ownership
^^^^^^^^^

:dp:`fls_Ka9q7gG2uu8T`
 :t:`Ownership <ownership>` is a property of :t:`values <value>` that is central to the resource management model of Rust.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_itkz9y19923k`
Two :t:`[value]s` :dt:`overlap` when their memory locations overlap, or both
values are elements of the same :t:`array`.

.. _fls_ke52l9lsvyu2:

owner
^^^^^


:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
