# Glossary audit R

## Per-letter checklist
- Letter: R
- [ ] Reconcile R terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate R terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for R
- [ ] Update `migration-checklist.md` for all R terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint R migration`
- [ ] Letter complete

## Term checklist
- [ ] range expression (range_expression)
- [ ] range expression high bound (range_expression_high_bound)
- [ ] range expression low bound (range_expression_low_bound)
- [ ] range pattern (range_pattern)
- [ ] range pattern bound (range_pattern_bound)
- [ ] range pattern high bound (range_pattern_high_bound)
- [ ] range pattern low bound (range_pattern_low_bound)
- [ ] range-from expression (range_from_expression)
- [ ] range-from-to expression (range_from_to_expression)
- [ ] range-full expression (range_full_expression)
- [ ] range-inclusive expression (range_inclusive_expression)
- [ ] range-to expression (range_to_expression)
- [ ] range-to-inclusive expression (range_to_inclusive_expression)
- [ ] raw borrow expression (raw_borrow_expression)
- [ ] raw byte string literal (raw_byte_string_literal)
- [ ] raw c string literal (raw_c_string_literal)
- [ ] raw pointer (raw_pointer)
- [ ] raw pointer type (raw_pointer_type)
- [ ] raw string literal (raw_string_literal)
- [ ] reachable control flow path (reachable_control_flow_path)
- [ ] receiver operand (receiver_operand)
- [ ] receiver type (receiver_type)
- [ ] record enum variant (record_enum_variant)
- [ ] record struct (record_struct)
- [ ] record struct field (record_struct_field)
- [ ] record struct pattern (record_struct_pattern)
- [ ] record struct type (record_struct_type)
- [ ] record struct value (record_struct_value)
- [ ] recursive type (recursive_type)
- [ ] reference (reference)
- [ ] reference identifier pattern (reference_identifier_pattern)
- [ ] reference pattern (reference_pattern)
- [ ] reference type (reference_type)
- [ ] referent (referent)
- [ ] refutability (refutability)
- [ ] refutable constant (refutable_constant)
- [ ] refutable pattern (refutable_pattern)
- [ ] refutable type (refutable_type)
- [ ] register (register)
- [ ] register argument (register_argument)
- [ ] register class (register_class)
- [ ] register class argument (register_class_argument)
- [ ] register class name (register_class_name)
- [ ] register expression (register_expression)
- [ ] register name (register_name)
- [ ] register parameter (register_parameter)
- [ ] register parameter modifier (register_parameter_modifier)
- [ ] remainder assignment (remainder_assignment)
- [ ] remainder assignment expression (remainder_assignment_expression)
- [ ] remainder expression (remainder_expression)
- [ ] renaming (renaming)
- [ ] repeat operand (repeat_operand)
- [ ] repetition operator (repetition_operator)
- [ ] representation modifier (representation_modifier)
- [ ] reserved keyword (reserved_keyword)
- [ ] resolution (resolution)
- [ ] rest pattern (rest_pattern)
- [ ] return expression (return_expression)
- [ ] return type (return_type)
- [ ] right operand (right_operand)
- [ ] rule matching (rule_matching)
- [ ] rustc (rustc)

## range expression (range_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_tbvugpuvcluj:

range expression
^^^^^^^^^^^^^^^^

:dp:`fls_bffrbucfwu7`
A :dt:`range expression` is an :t:`expression` that constructs a range.

:dp:`fls_1jk43yvxa8ks`
See :s:`RangeExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_Mz8j7158eNRg:

range expression
^^^^^^^^^^^^^^^^

:dp:`fls_lN4IBePdsPcL`
 A :t:`range expression <range_expression>` is an :t:`expression` that constructs a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
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


:dp:`fls_1jk43yvxa8ks`
See :s:`RangeExpression`.

.. _fls_mdvdxr6u13fw:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
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


:dp:`fls_1jk43yvxa8ks`
See :s:`RangeExpression`.

.. _fls_mdvdxr6u13fw:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range expression high bound (range_expression_high_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_mdvdxr6u13fw:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.

:dp:`fls_yxem0ckicxav`
See :s:`RangeExpressionHighBound`.
```

### After glossary entry (generated)

```rst
.. _fls_YaFkat1SYYFO:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_BtXC8AdLJivB`
 A :t:`range expression high bound <range_expression_high_bound>` is an :t:`operand` that specifies the end of a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bffrbucfwu7`
A :dt:`range expression` is an :t:`expression` that constructs a range.


:dp:`fls_1jk43yvxa8ks`
See :s:`RangeExpression`.

.. _fls_mdvdxr6u13fw:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.


:dp:`fls_yxem0ckicxav`
See :s:`RangeExpressionHighBound`.

.. _fls_smvgd160eynr:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bffrbucfwu7`
A :dt:`range expression` is an :t:`expression` that constructs a range.


:dp:`fls_1jk43yvxa8ks`
See :s:`RangeExpression`.

.. _fls_mdvdxr6u13fw:

range expression high bound
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.


:dp:`fls_yxem0ckicxav`
See :s:`RangeExpressionHighBound`.

.. _fls_smvgd160eynr:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range expression low bound (range_expression_low_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_smvgd160eynr:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.

:dp:`fls_vmb2z7oh6gzm`
See :s:`RangeExpressionLowBound`.
```

### After glossary entry (generated)

```rst
.. _fls_kKxJI0Jx9zSS:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_9VRF2gXbhIiv`
 A :t:`range expression low bound <range_expression_low_bound>` is an :t:`operand` that specifies the start of a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.


:dp:`fls_yxem0ckicxav`
See :s:`RangeExpressionHighBound`.

.. _fls_smvgd160eynr:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.


:dp:`fls_vmb2z7oh6gzm`
See :s:`RangeExpressionLowBound`.

.. _fls_6pxg401r6juc:

range pattern
^^^^^^^^^^^^^


:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_c70pj8w15nmc`
A :dt:`range expression high bound` is an :t:`operand` that specifies the end
of a range.


:dp:`fls_yxem0ckicxav`
See :s:`RangeExpressionHighBound`.

.. _fls_smvgd160eynr:

range expression low bound
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.


:dp:`fls_vmb2z7oh6gzm`
See :s:`RangeExpressionLowBound`.

.. _fls_6pxg401r6juc:

range pattern
^^^^^^^^^^^^^


:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range pattern (range_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_6pxg401r6juc:

range pattern
^^^^^^^^^^^^^

:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.

:dp:`fls_r36uf3y2denr`
See ``RangePattern``.
```

### After glossary entry (generated)

```rst
.. _fls_bsJzrMYQLJsq:

range pattern
^^^^^^^^^^^^^

:dp:`fls_uuvHHLJHa4f5`
 A :t:`range pattern <range_pattern>` is a :t:`pattern` that matches :t:`values <value>` which fall within a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.


:dp:`fls_vmb2z7oh6gzm`
See :s:`RangeExpressionLowBound`.

.. _fls_6pxg401r6juc:

range pattern
^^^^^^^^^^^^^


:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.


:dp:`fls_r36uf3y2denr`
See ``RangePattern``.

.. _fls_3ls9xlgt8ei1:

range pattern bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_t10o1p950u00`
A :dt:`range expression low bound` is an :t:`operand` that specifies the start
of a range.


:dp:`fls_vmb2z7oh6gzm`
See :s:`RangeExpressionLowBound`.

.. _fls_6pxg401r6juc:

range pattern
^^^^^^^^^^^^^


:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.


:dp:`fls_r36uf3y2denr`
See ``RangePattern``.

.. _fls_3ls9xlgt8ei1:

range pattern bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range pattern bound (range_pattern_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_3ls9xlgt8ei1:

range pattern bound
^^^^^^^^^^^^^^^^^^^

:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.

:dp:`fls_80736cs3axo4`
See :s:`RangePatternBound`.
```

### After glossary entry (generated)

```rst
.. _fls_1dZhslT90skQ:

range pattern bound
^^^^^^^^^^^^^^^^^^^

:dp:`fls_ZLvkLLXU2kXS`
 A :t:`range pattern bound <range_pattern_bound>` is a constraint on the range of a :t:`range pattern <range_pattern>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.


:dp:`fls_r36uf3y2denr`
See ``RangePattern``.

.. _fls_3ls9xlgt8ei1:

range pattern bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.


:dp:`fls_80736cs3axo4`
See :s:`RangePatternBound`.

.. _fls_y4rv5cbowvwg:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vf42zdyq23lc`
A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.


:dp:`fls_r36uf3y2denr`
See ``RangePattern``.

.. _fls_3ls9xlgt8ei1:

range pattern bound
^^^^^^^^^^^^^^^^^^^


:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.


:dp:`fls_80736cs3axo4`
See :s:`RangePatternBound`.

.. _fls_y4rv5cbowvwg:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range pattern high bound (range_pattern_high_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_y4rv5cbowvwg:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.

:dp:`fls_dnwqcswftw71`
See :s:`RangePatternHighBound`.
```

### After glossary entry (generated)

```rst
.. _fls_n3QT5nwTftpd:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NkEkO7h8J0RX`
 A :t:`range pattern high bound <range_pattern_high_bound>` is a :t:`range pattern bound <range_pattern_bound>` that specifies the end of a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.


:dp:`fls_80736cs3axo4`
See :s:`RangePatternBound`.

.. _fls_y4rv5cbowvwg:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.


:dp:`fls_dnwqcswftw71`
See :s:`RangePatternHighBound`.

.. _fls_laev4lmmv0cw:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_l9xq96bjs4o2`
A :dt:`range pattern bound` is a constraint on the range of a
:t:`range pattern`.


:dp:`fls_80736cs3axo4`
See :s:`RangePatternBound`.

.. _fls_y4rv5cbowvwg:

range pattern high bound
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.


:dp:`fls_dnwqcswftw71`
See :s:`RangePatternHighBound`.

.. _fls_laev4lmmv0cw:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range pattern low bound (range_pattern_low_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_laev4lmmv0cw:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.

:dp:`fls_j695o93wsu3i`
See :s:`RangePatternLowBound`.
```

### After glossary entry (generated)

```rst
.. _fls_Dz8DFHzibJza:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_1VULLAdBbGua`
 A :t:`range pattern low bound <range_pattern_low_bound>` is a :t:`range pattern bound <range_pattern_bound>` that specifies the start of a range.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.


:dp:`fls_dnwqcswftw71`
See :s:`RangePatternHighBound`.

.. _fls_laev4lmmv0cw:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.


:dp:`fls_j695o93wsu3i`
See :s:`RangePatternLowBound`.

.. _fls_iqpxlg7w3cvf:

range-from expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_arp7y7yme7yp`
A :dt:`range pattern high bound` is a :t:`range pattern bound` that specifies
the end of a range.


:dp:`fls_dnwqcswftw71`
See :s:`RangePatternHighBound`.

.. _fls_laev4lmmv0cw:

range pattern low bound
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.


:dp:`fls_j695o93wsu3i`
See :s:`RangePatternLowBound`.

.. _fls_iqpxlg7w3cvf:

range-from expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-from expression (range_from_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_iqpxlg7w3cvf:

range-from expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.

:dp:`fls_e1smn0b478ik`
See :s:`RangeFromExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_PCfZAxJVE376:

range-from expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_4Ul4HXhw3KSB`
 A :t:`range-from expression <range_from_expression>` is a :t:`range expression <range_expression>` that specifies an included :t:`range expression low bound <range_expression_low_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.


:dp:`fls_j695o93wsu3i`
See :s:`RangePatternLowBound`.

.. _fls_iqpxlg7w3cvf:

range-from expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.


:dp:`fls_e1smn0b478ik`
See :s:`RangeFromExpression`.

.. _fls_125h4p4zt86q:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_rt7q0msh3op4`
A :dt:`range pattern low bound` is a :t:`range pattern bound` that specifies
the start of a range.


:dp:`fls_j695o93wsu3i`
See :s:`RangePatternLowBound`.

.. _fls_iqpxlg7w3cvf:

range-from expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.


:dp:`fls_e1smn0b478ik`
See :s:`RangeFromExpression`.

.. _fls_125h4p4zt86q:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-from-to expression (range_from_to_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_125h4p4zt86q:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.

:dp:`fls_mjbxfjulryt`
See :s:`RangeFromToExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_qLOrOT9niZJT:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2QJhbBUfLeqC`
 A :t:`range-from-to expression <range_from_to_expression>` is a :t:`range expression <range_expression>` that specifies an included :t:`range expression low bound <range_expression_low_bound>` and an excluded :t:`range expression high bound <range_expression_high_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.


:dp:`fls_e1smn0b478ik`
See :s:`RangeFromExpression`.

.. _fls_125h4p4zt86q:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.


:dp:`fls_mjbxfjulryt`
See :s:`RangeFromToExpression`.

.. _fls_8z8nrblarxrv:

range-full expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6enyv2oa4abq`
A :dt:`range-from expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound`.


:dp:`fls_e1smn0b478ik`
See :s:`RangeFromExpression`.

.. _fls_125h4p4zt86q:

range-from-to expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.


:dp:`fls_mjbxfjulryt`
See :s:`RangeFromToExpression`.

.. _fls_8z8nrblarxrv:

range-full expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-full expression (range_full_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_8z8nrblarxrv:

range-full expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.

:dp:`fls_u7kd8w5g2icd`
See :s:`RangeFullExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_BFbhhXy39W9W:

range-full expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_pNqsOXXaBtcv`
 A :t:`range-full expression <range_full_expression>` is a :t:`range expression <range_expression>` that covers the whole range of a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.


:dp:`fls_mjbxfjulryt`
See :s:`RangeFromToExpression`.

.. _fls_8z8nrblarxrv:

range-full expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.


:dp:`fls_u7kd8w5g2icd`
See :s:`RangeFullExpression`.

.. _fls_tie80ejz8s19:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_nzf6y64jz83f`
A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an excluded
:t:`range expression high bound`.


:dp:`fls_mjbxfjulryt`
See :s:`RangeFromToExpression`.

.. _fls_8z8nrblarxrv:

range-full expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.


:dp:`fls_u7kd8w5g2icd`
See :s:`RangeFullExpression`.

.. _fls_tie80ejz8s19:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-inclusive expression (range_inclusive_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_tie80ejz8s19:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.

:dp:`fls_lpcsb8dtldk3`
See :s:`RangeInclusiveExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_bmDvN7YrlUBe:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_HWkU1RQjkor1`
 A :t:`range-inclusive expression <range_inclusive_expression>` is a :t:`range expression <range_expression>` that specifies an included :t:`range expression low bound <range_expression_low_bound>` and an included :t:`range expression high bound <range_expression_high_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.


:dp:`fls_u7kd8w5g2icd`
See :s:`RangeFullExpression`.

.. _fls_tie80ejz8s19:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.


:dp:`fls_lpcsb8dtldk3`
See :s:`RangeInclusiveExpression`.

.. _fls_etvgkb8zcfpd:

range-to expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6mchm7kb7i41`
A :dt:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.


:dp:`fls_u7kd8w5g2icd`
See :s:`RangeFullExpression`.

.. _fls_tie80ejz8s19:

range-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.


:dp:`fls_lpcsb8dtldk3`
See :s:`RangeInclusiveExpression`.

.. _fls_etvgkb8zcfpd:

range-to expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-to expression (range_to_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_etvgkb8zcfpd:

range-to expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.

:dp:`fls_lft9cd7h8cfv`
See :s:`RangeToExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_dl4GVjjE36SP:

range-to expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_S33elqgA9Two`
 A :t:`range-to expression <range_to_expression>` is a :t:`range expression <range_expression>` that specifies an excluded :t:`range expression high bound <range_expression_high_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.


:dp:`fls_lpcsb8dtldk3`
See :s:`RangeInclusiveExpression`.

.. _fls_etvgkb8zcfpd:

range-to expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.


:dp:`fls_lft9cd7h8cfv`
See :s:`RangeToExpression`.

.. _fls_ap5754dfltt5:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_9vja0wev84a7`
A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
included :t:`range expression low bound` and an included
:t:`range expression high bound`.


:dp:`fls_lpcsb8dtldk3`
See :s:`RangeInclusiveExpression`.

.. _fls_etvgkb8zcfpd:

range-to expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.


:dp:`fls_lft9cd7h8cfv`
See :s:`RangeToExpression`.

.. _fls_ap5754dfltt5:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## range-to-inclusive expression (range_to_inclusive_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_ap5754dfltt5:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.

:dp:`fls_krei7lc6lo8q`
See :s:`RangeToInclusiveExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_iW15MnbVQnHz:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_q4SIrDvpJ84V`
 A :t:`range-to-inclusive expression <range_to_inclusive_expression>` is a :t:`range expression <range_expression>` that specifies an included :t:`range expression high bound <range_expression_high_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.


:dp:`fls_lft9cd7h8cfv`
See :s:`RangeToExpression`.

.. _fls_ap5754dfltt5:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.


:dp:`fls_krei7lc6lo8q`
See :s:`RangeToInclusiveExpression`.

.. _fls_YLhE2qpzYXRK:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_urnfp1j9d5v4`
A :dt:`range-to expression` is a :t:`range expression` that specifies an
excluded :t:`range expression high bound`.


:dp:`fls_lft9cd7h8cfv`
See :s:`RangeToExpression`.

.. _fls_ap5754dfltt5:

range-to-inclusive expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.


:dp:`fls_krei7lc6lo8q`
See :s:`RangeToInclusiveExpression`.

.. _fls_YLhE2qpzYXRK:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw borrow expression (raw_borrow_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_YLhE2qpzYXRK:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_E6tFMQIePdYw:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2xYUfL5sdLT0`
 A :t:`raw borrow expression <raw_borrow_expression>` is an :t:`expression` that creates a :t:`raw pointer <raw_pointer>` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.


:dp:`fls_krei7lc6lo8q`
See :s:`RangeToInclusiveExpression`.

.. _fls_YLhE2qpzYXRK:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.


:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.

.. _fls_ipeh92kh17ze:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_t4fjanjvkd69`
A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
an included :t:`range expression high bound`.


:dp:`fls_krei7lc6lo8q`
See :s:`RangeToInclusiveExpression`.

.. _fls_YLhE2qpzYXRK:

raw borrow expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.


:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.

.. _fls_ipeh92kh17ze:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw byte string literal (raw_byte_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_ipeh92kh17ze:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.

:dp:`fls_5x71i3ay3na2`
See :s:`RawByteStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_CPcvPiKuoz0N:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_xYgfTjOFaclW`
 A :t:`raw byte string literal <raw_byte_string_literal>` is a :t:`simple byte string literal <simple_byte_string_literal>` that does not recognize :t:`escaped characters <escaped_character>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.


:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.

.. _fls_ipeh92kh17ze:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.


:dp:`fls_5x71i3ay3na2`
See :s:`RawByteStringLiteral`.

.. _fls_yGGvg3e0nPOh:

raw c string literal
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.


:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.

.. _fls_ipeh92kh17ze:

raw byte string literal
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.


:dp:`fls_5x71i3ay3na2`
See :s:`RawByteStringLiteral`.

.. _fls_yGGvg3e0nPOh:

raw c string literal
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw c string literal (raw_c_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_yGGvg3e0nPOh:

raw c string literal
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.

:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_1YnKFSsteMQF:

raw c string literal
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_jhTyo2ubg39g`
 A :t:`raw c string literal <raw_c_string_literal>` is a :t:`simple c string literal <simple_c_string_literal>` that does not recognize :t:`escaped characters <escaped_character>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.


:dp:`fls_5x71i3ay3na2`
See :s:`RawByteStringLiteral`.

.. _fls_yGGvg3e0nPOh:

raw c string literal
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8v5k3wemy4tl`
A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
not recognize :t:`[escaped character]s`.


:dp:`fls_5x71i3ay3na2`
See :s:`RawByteStringLiteral`.

.. _fls_yGGvg3e0nPOh:

raw c string literal
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw pointer (raw_pointer)

### Before glossary entry (origin/main)

```rst
.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^

:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.
```

### After glossary entry (generated)

```rst
.. _fls_0vDrykye2Zw7:

raw pointer
^^^^^^^^^^^

:dp:`fls_VL3UwGKMLYcd`
 A :t:`raw pointer <raw_pointer>` is a pointer of a :t:`raw pointer type <raw_pointer_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^


:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qhWBzqoYZL0e`
A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^


:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw pointer type (raw_pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^

:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.

:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_iqvQ7fKnieKd:

raw pointer type
^^^^^^^^^^^^^^^^

:dp:`fls_REfyN3BGRDfP`
 A :t:`raw pointer type <raw_pointer_type>` is an :t:`indirection type <indirection_type>` without safety and liveness guarantees.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^


:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^


:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_WpFJyq6q4k6E`
See :s:`RawCStringLiteral`.

.. _fls_uv4dyt4gi32x:

raw pointer
^^^^^^^^^^^


:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.

.. _fls_9los8hwh60z0:

raw pointer type
^^^^^^^^^^^^^^^^


:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^


:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## raw string literal (raw_string_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^

:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.

:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_n3pikw1abtsP:

raw string literal
^^^^^^^^^^^^^^^^^^

:dp:`fls_Rz8wX0zMacSC`
 A :t:`raw string literal <raw_string_literal>` is a :t:`simple string literal <simple_string_literal>` that does not recognize :t:`escaped characters <escaped_character>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^


:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wspawcoqxfbh`
A :dt:`raw pointer type` is an :t:`indirection type` without safety and
liveness guarantees.


:dp:`fls_ctksliaxhzo9`
See :s:`RawPointerTypeSpecification`.

.. _fls_echjohx6fjc:

raw string literal
^^^^^^^^^^^^^^^^^^


:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reachable control flow path (reachable_control_flow_path)

### Before glossary entry (origin/main)

```rst
.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.
```

### After glossary entry (generated)

```rst
.. _fls_9ysvQcPBrzaF:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_S0Nj7Hwq57H2`
 A :t:`reachable control flow path <reachable_control_flow_path>` is a control flow path that can be taken by the execution of a program between two given points in the program.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^


:dp:`fls_odbg4bizvqxq`
A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
:t:`method` is being invoked by a :t:`method call expression`.


:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_48t4v316951j`
A :dt:`raw string literal` is a :t:`simple string literal` that does not
recognize :t:`[escaped character]s`.


:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^


:dp:`fls_odbg4bizvqxq`
A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
:t:`method` is being invoked by a :t:`method call expression`.


:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## receiver operand (receiver_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^

:dp:`fls_odbg4bizvqxq`
A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
:t:`method` is being invoked by a :t:`method call expression`.

:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_RBWLrVMAlEgw:

receiver operand
^^^^^^^^^^^^^^^^

:dp:`fls_EUhGWjpsW1kp`
 A :t:`receiver operand <receiver_operand>` is an :t:`operand` that denotes the :t:`value` whose :t:`method` is being invoked by a :t:`method call expression <method_call_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^


:dp:`fls_odbg4bizvqxq`
A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
:t:`method` is being invoked by a :t:`method call expression`.


:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^


:dp:`fls_vgQmMlpFas5t`
A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_26ol7lrnux94`
See :s:`RawStringLiteral`.

.. _fls_sAe1HaaVSPvP:

reachable control flow path
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.

.. _fls_nfb3ciarl50w:

receiver operand
^^^^^^^^^^^^^^^^


:dp:`fls_odbg4bizvqxq`
A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
:t:`method` is being invoked by a :t:`method call expression`.


:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^


:dp:`fls_vgQmMlpFas5t`
A :t:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## receiver type (receiver_type)

### Before glossary entry (origin/main)

```rst
.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^

:dp:`fls_vgQmMlpFas5t`
A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.
```

### After glossary entry (generated)

```rst
.. _fls_GryGsCocD6J8:

receiver type
^^^^^^^^^^^^^

:dp:`fls_GwIft67iXKBF`
 A :t:`receiver type <receiver_type>` is the :t:`type` of the :t:`receiver operand <receiver_operand>` of a :t:`method call expression <method_call_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
entities-and-resolution.rst
:dp:`fls_nm06mru40tyg`
A :t:`field access expression` shall resolve to exactly one :t:`field`.

.. _fls_wqazkzle0ix9:

Method Resolution
~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules


:dp:`fls_e5a5z5yht26l`
:t:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.


:dp:`fls_mbdS0xiNlj92`
A :dt:`receiver type` is the :t:`type` of the :t:`receiver operand`
of a :t:`method call expression`.


:dp:`fls_z80ylmlu1f3q`
A :dt:`candidate receiver type` is the :t:`type` of the :t:`receiver operand`
of a :t:`method call expression` :t:`under resolution`.


:dp:`fls_e1029pvq706h`
A :dt:`candidate receiver type chain` is a sequence of
:t:`[candidate receiver type]s`. The :t:`candidate receiver type chain` starts
with the :t:`type` of the :t:`receiver operand` of the
:t:`method call expression` :t:`under resolution`. From then on, the
:t:`candidate receiver type chain` is treated as a :t:`dereference type chain`.

```

### After chapter excerpt (current)

```rst
entities-and-resolution.rst
:dp:`fls_nm06mru40tyg`
A :t:`field access expression` shall resolve to exactly one :t:`field`.

.. _fls_wqazkzle0ix9:

Method Resolution
~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules


:dp:`fls_e5a5z5yht26l`
:t:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.


:dp:`fls_mbdS0xiNlj92`
A :dt:`receiver type` is the :t:`type` of the :t:`receiver operand`
of a :t:`method call expression`.


:dp:`fls_z80ylmlu1f3q`
A :dt:`candidate receiver type` is the :t:`type` of the :t:`receiver operand`
of a :t:`method call expression` :t:`under resolution`.


:dp:`fls_e1029pvq706h`
A :dt:`candidate receiver type chain` is a sequence of
:t:`[candidate receiver type]s`. The :t:`candidate receiver type chain` starts
with the :t:`type` of the :t:`receiver operand` of the
:t:`method call expression` :t:`under resolution`. From then on, the
:t:`candidate receiver type chain` is treated as a :t:`dereference type chain`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record enum variant (record_enum_variant)

### Before glossary entry (origin/main)

```rst
.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^

:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.
```

### After glossary entry (generated)

```rst
.. _fls_PWcBvyI5y0aG:

record enum variant
^^^^^^^^^^^^^^^^^^^

:dp:`fls_cfXz1CMUFLun`
 A :t:`record enum variant <record_enum_variant>` is an :t:`enum variant <enum_variant>` with a :s:`RecordStructFieldList <recordstructfieldlist>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^


:dp:`fls_vgQmMlpFas5t`
A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^


:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.

.. _fls_jdd6h8pdp30x:

record struct
^^^^^^^^^^^^^


:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4rme1x6romeg`
See :s:`ReceiverOperand`.

.. _fls_Kpkm0J40xq5J:

receiver type
^^^^^^^^^^^^^


:dp:`fls_vgQmMlpFas5t`
A :t:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^


:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.

.. _fls_jdd6h8pdp30x:

record struct
^^^^^^^^^^^^^


:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record struct (record_struct)

### Before glossary entry (origin/main)

```rst
.. _fls_jdd6h8pdp30x:

record struct
^^^^^^^^^^^^^

:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.

:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_olpvNuuZ0esh:

record struct
^^^^^^^^^^^^^

:dp:`fls_h8nQklfsqAzM`
 A :t:`record struct <record_struct>` is a :t:`struct` with a :s:`RecordStructFieldList <recordstructfieldlist>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vgQmMlpFas5t`
A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^


:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.

.. _fls_jdd6h8pdp30x:

record struct
^^^^^^^^^^^^^


:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^


:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vgQmMlpFas5t`
A :t:`receiver type` is the :t:`type` of a :t:`receiver operand`.

.. _fls_nG6ikjLsCW7m:

record enum variant
^^^^^^^^^^^^^^^^^^^


:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.

.. _fls_jdd6h8pdp30x:

record struct
^^^^^^^^^^^^^


:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^


:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record struct field (record_struct_field)

### Before glossary entry (origin/main)

```rst
.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^

:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.

:dp:`fls_bjwmhxf3ae14`
See :s:`RecordStructField`.
```

### After glossary entry (generated)

```rst
.. _fls_hJOLopRKWaAh:

record struct field
^^^^^^^^^^^^^^^^^^^

:dp:`fls_urbja9DKwHpY`
 A :t:`record struct field <record_struct_field>` is a :t:`field` of a :t:`record struct type <record_struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^


:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.


:dp:`fls_bjwmhxf3ae14`
See :s:`RecordStructField`.

.. _fls_at2caaqlpva1:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.


:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.

.. _fls_hzkwzbk5wp54:

record struct field
^^^^^^^^^^^^^^^^^^^


:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.


:dp:`fls_bjwmhxf3ae14`
See :s:`RecordStructField`.

.. _fls_at2caaqlpva1:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record struct pattern (record_struct_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_at2caaqlpva1:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_H152Q9wW3Cph:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_0Rnpf3Adhrqg`
 A :t:`record struct pattern <record_struct_pattern>` is a :t:`pattern` that matches a :t:`enum variant value <enum_variant_value>`, a :t:`struct value <struct_value>`, or a :t:`union value <union_value>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.


:dp:`fls_bjwmhxf3ae14`
See :s:`RecordStructField`.

.. _fls_at2caaqlpva1:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.


:dp:`fls_bjwmhxf3ae14`
See :s:`RecordStructField`.

.. _fls_at2caaqlpva1:

record struct pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record struct type (record_struct_type)

### Before glossary entry (origin/main)

```rst
.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^

:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.
```

### After glossary entry (generated)

```rst
.. _fls_kdbK3ueqOsV3:

record struct type
^^^^^^^^^^^^^^^^^^

:dp:`fls_roqh6XZCbDo8`
 A :t:`record struct type <record_struct_type>` is the :t:`type` of a :t:`record struct <record_struct>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q7njznxhmmw`
A :dt:`record struct pattern` is a :t:`pattern` that matches a
:t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.


:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## record struct value (record_struct_value)

### Before glossary entry (origin/main)

```rst
.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^

:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.
```

### After glossary entry (generated)

```rst
.. _fls_4pC8BiGxbobB:

record struct value
^^^^^^^^^^^^^^^^^^^

:dp:`fls_kBQvpvFSBqlP`
 A :t:`record struct value <record_struct_value>` is a :t:`value` of a :t:`record struct type <record_struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_viwieu1p3hds`
See :s:`RecordStructPattern`.

.. _fls_uthd12hz3h4v:

record struct type
^^^^^^^^^^^^^^^^^^


:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## recursive type (recursive_type)

### Before glossary entry (origin/main)

```rst
.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^

:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.
```

### After glossary entry (generated)

```rst
.. _fls_WNMgm6MNobBR:

recursive type
^^^^^^^^^^^^^^

:dp:`fls_nXiNyVquYbsx`
 A :t:`recursive type <recursive_type>` is a :t:`type` that may define other types within its :t:`type specification <type_specification>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.

.. _fls_cPs5C1chWmce:

record struct value
^^^^^^^^^^^^^^^^^^^


:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reference (reference)

### Before glossary entry (origin/main)

```rst
.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^

:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.
```

### After glossary entry (generated)

```rst
.. _fls_f4pkPTyvZvuP:

reference
^^^^^^^^^

:dp:`fls_Xh2DJS1Ll7VI`
 A :t:`reference` is a :t:`value` of a :t:`reference type <reference_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.

.. _fls_94fkxohlnq9i:

recursive type
^^^^^^^^^^^^^^


:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reference identifier pattern (reference_identifier_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.
```

### After glossary entry (generated)

```rst
.. _fls_VfVrmEVEnBcz:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_6qr4ETW4uYNF`
 A :t:`reference identifier pattern <reference_identifier_pattern>` is an :t:`identifier pattern <identifier_pattern>` with :t:`keyword` ``ref``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2t8qom6dhcjb`
A :dt:`recursive type` is a :t:`type` that may define other types within its
:t:`type specification`.

.. _fls_onv3cs5tckgo:

reference
^^^^^^^^^


:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reference pattern (reference_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^

:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.

:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_s26gEGSwSp4n:

reference pattern
^^^^^^^^^^^^^^^^^

:dp:`fls_4GWgxUjPB5fF`
 A :t:`reference pattern <reference_pattern>` is a :t:`pattern` that dereferences a :t:`pointer` that is being matched.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^


:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_s82y4hsuytiq`
A :dt:`reference` is a :t:`value` of a :t:`reference type`.

.. _fls_1XGsXRZIFnqL:

reference identifier pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.

.. _fls_kiy6b1wbn0a3:

reference pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^


:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reference type (reference_type)

### Before glossary entry (origin/main)

```rst
.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^

:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.

:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_DMoKOdvCRaWZ:

reference type
^^^^^^^^^^^^^^

:dp:`fls_2kzXFQtDiaMk`
 A :t:`reference type <reference_type>` is an :t:`indirection type <indirection_type>` with :t:`ownership`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^


:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.


:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ebshqnhmwgow`
A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer`
that is being matched.


:dp:`fls_rghv5drrqxs1`
See :s:`ReferencePattern`.

.. _fls_uw32xmrfgzcd:

reference type
^^^^^^^^^^^^^^


:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.


:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## referent (referent)

### Before glossary entry (origin/main)

```rst
.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^

:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.
```

### After glossary entry (generated)

```rst
.. _fls_x9uceXl1YpQN:

referent
^^^^^^^^

:dp:`fls_BIPvZj3WOtrv`
 A :t:`referent` is the :t:`value` pointed-to by a :t:`reference`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.


:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_l3knopsdlyf2`
A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.


:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## refutability (refutability)

### Before glossary entry (origin/main)

```rst
.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^

:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_h3Dk1QaFL0Ye:

Refutability
^^^^^^^^^^^^

:dp:`fls_pk13M8gfTOAr`
 :t:`Refutability <refutability>` is a property of :t:`patterns <pattern>` that expresses the ability to match all possible :t:`values <value>` of a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_jzjatdpxqt9u`
See :s:`ReferenceTypeSpecification`.

.. _fls_h8x0u32wfz8v:

referent
^^^^^^^^


:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## refutable constant (refutable_constant)

### Before glossary entry (origin/main)

```rst
.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^

:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.
```

### After glossary entry (generated)

```rst
.. _fls_beGf88c9V3vZ:

refutable constant
^^^^^^^^^^^^^^^^^^

:dp:`fls_WdRLzgWspnoU`
 A :t:`refutable constant <refutable_constant>` is a :t:`constant` of a :t:`refutable type <refutable_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_78ipj8avpwzl`
A :dt:`referent` is the :t:`value` pointed-to by a :t:`reference`.

.. _fls_bkwy183h9ygt:

refutability
^^^^^^^^^^^^


:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## refutable pattern (refutable_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^

:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.
```

### After glossary entry (generated)

```rst
.. _fls_vddlx5Mr7jsu:

refutable pattern
^^^^^^^^^^^^^^^^^

:dp:`fls_M7VURnzdl5d5`
 A :t:`refutable pattern <refutable_pattern>` is a :t:`pattern` that has a possibility of not matching the :t:`value` it is being matched against.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.

.. _fls_v99joc4m6cup:

refutable constant
^^^^^^^^^^^^^^^^^^


:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## refutable type (refutable_type)

### Before glossary entry (origin/main)

```rst
.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^

:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_fiIR4xMBJoGw:

refutable type
^^^^^^^^^^^^^^

:dp:`fls_BTzJ8EudQruc`
 A :t:`refutable type <refutable_type>` is a :t:`type` that has more than one :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mc6hsomq08uu`
A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

.. _fls_srdcx5oi4dcp:

refutable pattern
^^^^^^^^^^^^^^^^^


:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register (register)

### Before glossary entry (origin/main)

```rst
.. _fls_T84qaJMZzMbb:

register
^^^^^^^^

:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.
```

### After glossary entry (generated)

```rst
.. _fls_tjnYo7Ms6wP1:

register
^^^^^^^^

:dp:`fls_UqXE2mWcnQBu`
 A :t:`register` is a hardware component capable of holding data that can be read and written.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_re7qz78koman`
A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
matching the :t:`value` it is being matched against.

.. _fls_dkq1h6p9yaar:

refutable type
^^^^^^^^^^^^^^


:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register argument (register_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^

:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.

:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.
```

### After glossary entry (generated)

```rst
.. _fls_ho5Pt7jLTff3:

register argument
^^^^^^^^^^^^^^^^^

:dp:`fls_fnEodekPhUGt`
 A :t:`register argument <register_argument>` is a :t:`construct` that configures the input and output of a :t:`register`, and optionally binds the configuration to an :t:`identifier`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.

.. _fls_T84qaJMZzMbb:

register
^^^^^^^^


:dp:`fls_fVdSybu8DW8w`
A :dt:`register` is a hardware component capable of holding data that can be
read and written.

.. _fls_ISWWmgKjfYwt:

register argument
^^^^^^^^^^^^^^^^^


:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register class (register_class)

### Before glossary entry (origin/main)

```rst
.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^

:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.
```

### After glossary entry (generated)

```rst
.. _fls_Gm6855dJs2UL:

register class
^^^^^^^^^^^^^^

:dp:`fls_TnBSfItigsxj`
 A :t:`register class <register_class>` represents a set of :t:`registers <register>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_rNoFdCKbVmRC`
A :dt:`register argument` is a :t:`construct` that configures the input
and output of a :t:`register`, and optionally binds the configuration to an
:t:`identifier`.


:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register class argument (register_class_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.
```

### After glossary entry (generated)

```rst
.. _fls_ikZletuAKBWK:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_FOELJpRQK22G`
 A :t:`register class argument <register_class_argument>` is a :t:`register argument <register_argument>` that uses a :t:`register class name <register_class_name>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_aof7O9XREo2S`
See :s:`RegisterArgument`.

.. _fls_2qKUiHcfmZQ6:

register class
^^^^^^^^^^^^^^


:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register class name (register_class_name)

### Before glossary entry (origin/main)

```rst
.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^

:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.

:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.
```

### After glossary entry (generated)

```rst
.. _fls_Chn1QcjUwrMV:

register class name
^^^^^^^^^^^^^^^^^^^

:dp:`fls_R5w8IN9GzWnG`
 A :t:`register class name <register_class_name>` is a target-specific string that identifies a :t:`register class <register_class>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2H0OYS733VJl`
A :dt:`register class` represents a set of :t:`[register]s`.

.. _fls_8gC17CgCS9n1:

register class argument
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ksLXAyPLx9IL`
A :dt:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

.. _fls_xZTkANlRsKRt:

register class name
^^^^^^^^^^^^^^^^^^^


:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register expression (register_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.

:dp:`fls_YEzo09cqWUUy`
See :s:`RegisterExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_swhtqG2ItUBm:

register expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_rnFN5bxuEo9k`
 A :t:`register expression <register_expression>` is either an :t:`input-output register expression <input_output_register_expression>` or a :t:`simple register expression <simple_register_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.


:dp:`fls_YEzo09cqWUUy`
See :s:`RegisterExpression`.

.. _fls_kbBK666iBS2X:

register name
^^^^^^^^^^^^^


:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_QsSFoL0UyRRB`
A :dt:`register class name` is a target-specific string that identifies a
:t:`register class`.


:dp:`fls_Y1ZpiFAV2c1A`
See :s:`RegisterClassName`.

.. _fls_7KIReJZLKdeK:

register expression
^^^^^^^^^^^^^^^^^^^


:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.


:dp:`fls_YEzo09cqWUUy`
See :s:`RegisterExpression`.

.. _fls_kbBK666iBS2X:

register name
^^^^^^^^^^^^^


:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register name (register_name)

### Before glossary entry (origin/main)

```rst
.. _fls_kbBK666iBS2X:

register name
^^^^^^^^^^^^^

:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.

:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.
```

### After glossary entry (generated)

```rst
.. _fls_YRZu0fQaoxqp:

register name
^^^^^^^^^^^^^

:dp:`fls_qFqrdC9OOsZi`
 A :t:`register name <register_name>` is either the :t:`explicit register name <explicit_register_name>` of a :t:`register`, or the :t:`register class name <register_class_name>` of the :t:`register class <register_class>` a :t:`register` belongs to.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.


:dp:`fls_YEzo09cqWUUy`
See :s:`RegisterExpression`.

.. _fls_kbBK666iBS2X:

register name
^^^^^^^^^^^^^


:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.


:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2cVy6XfOQ4QG`
A :dt:`register expression` is either an :t:`input-output register expression`
or a :t:`simple register expression`.


:dp:`fls_YEzo09cqWUUy`
See :s:`RegisterExpression`.

.. _fls_kbBK666iBS2X:

register name
^^^^^^^^^^^^^


:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.


:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register parameter (register_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^

:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.
```

### After glossary entry (generated)

```rst
.. _fls_XYzxieksCT9h:

register parameter
^^^^^^^^^^^^^^^^^^

:dp:`fls_eP9zB23XSQer`
 A :t:`register parameter <register_parameter>` is a substring delimited by characters 0x7B (left curly bracket) and 0x7D (right curly bracket) that is substituted with a :t:`register argument <register_argument>` in an :t:`assembly instruction <assembly_instruction>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.


:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_U5r8Ypnjah5E`
A :dt:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.


:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## register parameter modifier (register_parameter_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.
```

### After glossary entry (generated)

```rst
.. _fls_n7KWzsNpxjjr:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_VN1hpJLI1jib`
 A :t:`register parameter modifier <register_parameter_modifier>` is a substring that starts with character 0x3A (colon), follows a :t:`register parameter <register_parameter>`, and changes the formatting of the related :t:`register parameter <register_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_WeyiFrnGgWPn`
See :s:`RegisterName`.

.. _fls_foh6xELWBsY9:

register parameter
^^^^^^^^^^^^^^^^^^


:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## remainder assignment (remainder_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.
```

### After glossary entry (generated)

```rst
.. _fls_694KnvCsPzua:

remainder assignment
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_9cYc7u0Lcnzt`
 For :t:`remainder assignment <remainder_assignment>`, see :t:`remainder assignment expression <remainder_assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_JicHMIj5dlxJ`
A :dt:`register parameter` is a substring delimited by characters 0x7B (left
curly bracket) and 0x7D (right curly bracket) that is substituted with a
:t:`register argument` in an :t:`assembly instruction`.

.. _fls_NDpKXnlmnN7M:

register parameter modifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## remainder assignment expression (remainder_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.

:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_N0XeJ5WOuNCb:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_3v39fgNnXN53`
 A :t:`remainder assignment expression <remainder_assignment_expression>` is a :t:`compound assignment expression <compound_assignment_expression>` that uses remainder division.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8BdOnxHZS0Qi`
A :dt:`register parameter modifier` is a substring that starts with character
0x3A (colon), follows a :t:`register parameter`, and changes the formatting of
the related :t:`register parameter`.

.. _fls_JnhUWipah0nO:

remainder assignment
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. _fls_mio7pagghcks:

remainder assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## remainder expression (remainder_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.

:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_8RrD7V2Iq4aM:

remainder expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_zpIigRcswcHn`
 A :t:`remainder expression <remainder_expression>` is an :t:`arithmetic expression <arithmetic_expression>` that uses remainder division.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.


:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.

.. _fls_8ibsdx4dx6s7:

renaming
^^^^^^^^


:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.


:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.

.. _fls_f15h4919ln3k:

remainder expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.


:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.

.. _fls_8ibsdx4dx6s7:

renaming
^^^^^^^^


:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## renaming (renaming)

### Before glossary entry (origin/main)

```rst
.. _fls_8ibsdx4dx6s7:

renaming
^^^^^^^^

:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.

:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.
```

### After glossary entry (generated)

```rst
.. _fls_0vC81mi6i1NP:

renaming
^^^^^^^^

:dp:`fls_NpxWcZBHztEV`
 A :t:`renaming` provides an alternative :t:`name` for an existing name.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.


:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.

.. _fls_8ibsdx4dx6s7:

renaming
^^^^^^^^


:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.


:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.

.. _fls_b35oy3nnzixm:

repeat operand
^^^^^^^^^^^^^^


:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.


:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.

.. _fls_8ibsdx4dx6s7:

renaming
^^^^^^^^


:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.


:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.

.. _fls_b35oy3nnzixm:

repeat operand
^^^^^^^^^^^^^^


:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## repeat operand (repeat_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_b35oy3nnzixm:

repeat operand
^^^^^^^^^^^^^^

:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.

:dp:`fls_r4acyux78txu`
See :s:`RepeatOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_xrsq9zFpq9qj:

repeat operand
^^^^^^^^^^^^^^

:dp:`fls_Z2Ox4q5chpPE`
 A :t:`repeat operand <repeat_operand>` is an :t:`operand` that specifies the element being repeated in an :t:`array repetition constructor <array_repetition_constructor>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.


:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.

.. _fls_b35oy3nnzixm:

repeat operand
^^^^^^^^^^^^^^


:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.


:dp:`fls_r4acyux78txu`
See :s:`RepeatOperand`.

.. _fls_r2yjjhrvr9qi:

repetition operator
^^^^^^^^^^^^^^^^^^^


:dp:`fls_67907pk7uogl`
A :dt:`repetition operator` is a :t:`construct` that indicates the number
of times a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription` can be repeated.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.


:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.

.. _fls_b35oy3nnzixm:

repeat operand
^^^^^^^^^^^^^^


:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.


:dp:`fls_r4acyux78txu`
See :s:`RepeatOperand`.

.. _fls_r2yjjhrvr9qi:

repetition operator
^^^^^^^^^^^^^^^^^^^


:dp:`fls_67907pk7uogl`
A :dt:`repetition operator` is a :t:`construct` that indicates the number
of times a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription` can be repeated.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## repetition operator (repetition_operator)

### Before glossary entry (origin/main)

```rst
.. _fls_r2yjjhrvr9qi:

repetition operator
^^^^^^^^^^^^^^^^^^^

:dp:`fls_67907pk7uogl`
A :dt:`repetition operator` is a :t:`construct` that indicates the number
of times a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription` can be repeated.

:dp:`fls_hiasmmpr2jks`
See :s:`MacroRepetitionOperator`.
```

### After glossary entry (generated)

```rst
.. _fls_XKHOIB3JK4iY:

repetition operator
^^^^^^^^^^^^^^^^^^^

:dp:`fls_WDXGL07gXYmW`
 A :t:`repetition operator <repetition_operator>` is a :t:`construct` that indicates the number of times a :t:`macro repetition in matching <macro_repetition_in_matching>` or a :t:`macro repetition in transcription <macro_repetition_in_transcription>` can be repeated.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.


:dp:`fls_r4acyux78txu`
See :s:`RepeatOperand`.

.. _fls_r2yjjhrvr9qi:

repetition operator
^^^^^^^^^^^^^^^^^^^


:dp:`fls_67907pk7uogl`
A :dt:`repetition operator` is a :t:`construct` that indicates the number
of times a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription` can be repeated.


:dp:`fls_hiasmmpr2jks`
See :s:`MacroRepetitionOperator`.

.. _fls_o34kkn5pi0sh:

representation
^^^^^^^^^^^^^^


:dp:`fls_69j7pq2o1iu`
See :t:`type representation`.

.. _fls_TSbBt6WzropN:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ol2y1og2jwss`
A :dt:`repeat operand` is an :t:`operand` that specifies the element being
repeated in an :t:`array repetition constructor`.


:dp:`fls_r4acyux78txu`
See :s:`RepeatOperand`.

.. _fls_r2yjjhrvr9qi:

repetition operator
^^^^^^^^^^^^^^^^^^^


:dp:`fls_67907pk7uogl`
A :dt:`repetition operator` is a :t:`construct` that indicates the number
of times a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription` can be repeated.


:dp:`fls_hiasmmpr2jks`
See :s:`MacroRepetitionOperator`.

.. _fls_o34kkn5pi0sh:

representation
^^^^^^^^^^^^^^


:dp:`fls_69j7pq2o1iu`
See :t:`type representation`.

.. _fls_TSbBt6WzropN:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## representation modifier (representation_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_TSbBt6WzropN:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.

:dp:`fls_TAVyjj66UBUo`
See :s:`Alignment`.
```

### After glossary entry (generated)

```rst
.. _fls_58GoFuHKaz7V:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_RXmRycmPtgBC`
 A :t:`representation modifier <representation_modifier>` is a :t:`construct` that modifies the :t:`alignment` of a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hiasmmpr2jks`
See :s:`MacroRepetitionOperator`.

.. _fls_o34kkn5pi0sh:

representation
^^^^^^^^^^^^^^


:dp:`fls_69j7pq2o1iu`
See :t:`type representation`.

.. _fls_TSbBt6WzropN:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.


:dp:`fls_TAVyjj66UBUo`
See :s:`Alignment`.

.. _fls_x7yd6o4akrrg:

reserved keyword
^^^^^^^^^^^^^^^^


:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hiasmmpr2jks`
See :s:`MacroRepetitionOperator`.

.. _fls_o34kkn5pi0sh:

representation
^^^^^^^^^^^^^^


:dp:`fls_69j7pq2o1iu`
See :t:`type representation`.

.. _fls_TSbBt6WzropN:

representation modifier
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.


:dp:`fls_TAVyjj66UBUo`
See :s:`Alignment`.

.. _fls_x7yd6o4akrrg:

reserved keyword
^^^^^^^^^^^^^^^^


:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## reserved keyword (reserved_keyword)

### Before glossary entry (origin/main)

```rst
.. _fls_x7yd6o4akrrg:

reserved keyword
^^^^^^^^^^^^^^^^

:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.

:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.
```

### After glossary entry (generated)

```rst
.. _fls_REwfORHjuT1Z:

reserved keyword
^^^^^^^^^^^^^^^^

:dp:`fls_gN1AJTTN5s7A`
 A :t:`reserved keyword <reserved_keyword>` is a :t:`keyword` that is not yet in use.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.


:dp:`fls_TAVyjj66UBUo`
See :s:`Alignment`.

.. _fls_x7yd6o4akrrg:

reserved keyword
^^^^^^^^^^^^^^^^


:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.


:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.


:dp:`fls_TAVyjj66UBUo`
See :s:`Alignment`.

.. _fls_x7yd6o4akrrg:

reserved keyword
^^^^^^^^^^^^^^^^


:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.


:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## resolution (resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^

:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.
```

### After glossary entry (generated)

```rst
.. _fls_1mXN4DXfbi35:

Resolution
^^^^^^^^^^

:dp:`fls_J4E19RDS2BOC`
 :t:`Resolution <resolution>` is the process of finding a unique interpretation for a :t:`field access expression <field_access_expression>`, a :t:`method call expression <method_call_expression>`, or a :t:`path`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.


:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^


:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_b67hj7fdbq4s`
A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.


:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^


:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## rest pattern (rest_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^

:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.

:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_qBlY2LsSNgDt:

rest pattern
^^^^^^^^^^^^

:dp:`fls_1ljUu7BekCBT`
 A :t:`rest pattern <rest_pattern>` is a :t:`pattern` that matches zero or more elements that have not already been matched.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^


:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^


:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hp9iqdrkt0cg`
See :s:`ReservedKeyword`.

.. _fls_O5iuGATZgyBu:

resolution
^^^^^^^^^^


:dp:`fls_PQjEvLs5cE4y`
:dt:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, or a :t:`path`.

.. _fls_uuo1qvrz1i0k:

rest pattern
^^^^^^^^^^^^


:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^


:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## return expression (return_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^

:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.

:dp:`fls_phd8zrsyuzu7`
See :s:`ReturnExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_XOhwfvFOy90s:

return expression
^^^^^^^^^^^^^^^^^

:dp:`fls_yVvtyy0m1YIM`
 A :t:`return expression <return_expression>` is an :t:`expression` that optionally yields a :t:`value` and causes control flow to return to the caller.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^


:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.


:dp:`fls_phd8zrsyuzu7`
See :s:`ReturnExpression`.

.. _fls_b8dbm1bs65kw:

return type
^^^^^^^^^^^


:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_xngp3h1znw9o`
A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
have not already been matched.


:dp:`fls_rnmhg04u0oga`
See :s:`RestPattern`.

.. _fls_7tl9qo8yj8xh:

return expression
^^^^^^^^^^^^^^^^^


:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.


:dp:`fls_phd8zrsyuzu7`
See :s:`ReturnExpression`.

.. _fls_b8dbm1bs65kw:

return type
^^^^^^^^^^^


:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## return type (return_type)

### Before glossary entry (origin/main)

```rst
.. _fls_b8dbm1bs65kw:

return type
^^^^^^^^^^^

:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.

:dp:`fls_utuprsem6n58`
See :s:`ReturnType`.
```

### After glossary entry (generated)

```rst
.. _fls_QQ7Y6bDSMP4D:

return type
^^^^^^^^^^^

:dp:`fls_5BG5FGdCjZhn`
 A :t:`return type <return_type>` is the :t:`type` of the result a :t:`function` returns.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.


:dp:`fls_phd8zrsyuzu7`
See :s:`ReturnExpression`.

.. _fls_b8dbm1bs65kw:

return type
^^^^^^^^^^^


:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.


:dp:`fls_utuprsem6n58`
See :s:`ReturnType`.

.. _fls_76o7m8vny72n:

right operand
^^^^^^^^^^^^^


:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vnupfc6s0s7b`
A :dt:`return expression` is an :t:`expression` that optionally yields a
:t:`value` and causes control flow to return to the caller.


:dp:`fls_phd8zrsyuzu7`
See :s:`ReturnExpression`.

.. _fls_b8dbm1bs65kw:

return type
^^^^^^^^^^^


:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.


:dp:`fls_utuprsem6n58`
See :s:`ReturnType`.

.. _fls_76o7m8vny72n:

right operand
^^^^^^^^^^^^^


:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## right operand (right_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_76o7m8vny72n:

right operand
^^^^^^^^^^^^^

:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.

:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_6k83ILy5MQgO:

right operand
^^^^^^^^^^^^^

:dp:`fls_uXBgcB0PrNDZ`
 A :t:`right operand <right_operand>` is an :t:`operand` that appears on the right-hand side of a :t:`binary operator <binary_operator>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.


:dp:`fls_utuprsem6n58`
See :s:`ReturnType`.

.. _fls_76o7m8vny72n:

right operand
^^^^^^^^^^^^^


:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.


:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.

.. _fls_fki32ns69q4j:

rustc
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_cwucgbmmhnnm`
A :dt:`return type` is the :t:`type` of the result a :t:`function` returns.


:dp:`fls_utuprsem6n58`
See :s:`ReturnType`.

.. _fls_76o7m8vny72n:

right operand
^^^^^^^^^^^^^


:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.


:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.

.. _fls_fki32ns69q4j:

rustc
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## rule matching (rule_matching)

### Before glossary entry (origin/main)

```rst
.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^

:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.
```

### After glossary entry (generated)

```rst
.. _fls_A9zs4bUgSuIk:

Rule matching
^^^^^^^^^^^^^

:dp:`fls_SLKAI0V3jhod`
 :t:`Rule matching <rule_matching>` is the process of consuming a :s:`TokenTree <tokentree>` in an attempt to fully satisfy the :t:`macro matcher <macro_matcher>` of a :t:`macro rule <macro_rule>` that belongs to a resolved :t:`declarative macro <declarative_macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.


:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


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

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_e1j9s4odze9b`
A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
a :t:`binary operator`.


:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


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

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## rustc (rustc)

### Before glossary entry (origin/main)

```rst
.. _fls_fki32ns69q4j:

rustc
^^^^^

:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.
```

### After glossary entry (generated)

```rst
.. _fls_uflDvRNtilYm:

rustc
^^^^^

:dp:`fls_4IaYuisiDglF`
 :t:`rustc` is a compiler that implements the FLS.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


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

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hq7x1t5dmdlp`
See :s:`RightOperand`.

.. _fls_9u67noriaxfe:

rule matching
^^^^^^^^^^^^^


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

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
