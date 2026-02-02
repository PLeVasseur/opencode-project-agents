# Glossary audit V

## Per-letter checklist
- Letter: V
- [ ] Reconcile V terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate V terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for V
- [ ] Update `migration-checklist.md` for all V terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint V migration`
- [ ] Letter complete

## Term checklist
- [ ] validity invariant (validity_invariant)
- [ ] value (value)
- [ ] value expression (value_expression)
- [ ] value expression context (value_expression_context)
- [ ] value operand (value_operand)
- [ ] variable (variable)
- [ ] variadic part (variadic_part)
- [ ] variance (variance)
- [ ] visibility (visibility)
- [ ] visibility modifier (visibility_modifier)
- [ ] visible emptiness (visible_emptiness)
- [ ] visible empty enum variant (visible_empty_enum_variant)
- [ ] visible empty type (visible_empty_type)

## validity invariant (validity_invariant)

### Before glossary entry (origin/main)

```rst
.. _fls_A5K8aOBsI3BG:

validity invariant
^^^^^^^^^^^^^^^^^^

:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.
```

### After glossary entry (generated)

```rst
.. _fls_W8dzo2Uic5ID:

validity invariant
^^^^^^^^^^^^^^^^^^

:dp:`fls_ldy8zytsZQPi`
 A :t:`validity invariant <validity_invariant>` is an invariant that when violated results in immediate :t:`undefined behavior <undefined_behavior>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ib5wf62j4uhr`
See :s:`UseImport`.

.. _fls_gvjm5mms9ahz:

usize
^^^^^


:dp:`fls_r22k1l8799k6`
:dc:`usize` is an :t:`unsigned integer type` with the same number of bits as
the platform's :t:`pointer type`, and is at least 16-bits wide.

.. _fls_A5K8aOBsI3BG:

validity invariant
^^^^^^^^^^^^^^^^^^


:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ib5wf62j4uhr`
See :s:`UseImport`.

.. _fls_gvjm5mms9ahz:

usize
^^^^^


:dp:`fls_r22k1l8799k6`
:dc:`usize` is an :t:`unsigned integer type` with the same number of bits as
the platform's :t:`pointer type`, and is at least 16-bits wide.

.. _fls_A5K8aOBsI3BG:

validity invariant
^^^^^^^^^^^^^^^^^^


:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## value (value)

### Before glossary entry (origin/main)

```rst
.. _fls_tg866bc926ms:

value
^^^^^

:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_BO5FARqmzotQ:

value
^^^^^

:dp:`fls_286G8BuNIkfJ`
 A :t:`value` is either a :t:`literal` or the result of a computation, that may be stored in a memory location, and interpreted based on some :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_r22k1l8799k6`
:dc:`usize` is an :t:`unsigned integer type` with the same number of bits as
the platform's :t:`pointer type`, and is at least 16-bits wide.

.. _fls_A5K8aOBsI3BG:

validity invariant
^^^^^^^^^^^^^^^^^^


:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_r22k1l8799k6`
:dc:`usize` is an :t:`unsigned integer type` with the same number of bits as
the platform's :t:`pointer type`, and is at least 16-bits wide.

.. _fls_A5K8aOBsI3BG:

validity invariant
^^^^^^^^^^^^^^^^^^


:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## value expression (value_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^

:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_3s83aDUNEjCG:

value expression
^^^^^^^^^^^^^^^^

:dp:`fls_oUtMDbu6C6j5`
 A :t:`value expression <value_expression>` is an :t:`expression` that represents a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.

.. _fls_tg866bc926ms:

value
^^^^^


:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## value expression context (value_expression_context)

### Before glossary entry (origin/main)

```rst
.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.
```

### After glossary entry (generated)

```rst
.. _fls_osVXQPtkYbSf:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_PC84lVuT3vZh`
 A :t:`value expression context <value_expression_context>` is an expression context that is not a :t:`place expression context <place_expression_context>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_h8jn338b51yu`
A :dt:`value` is either a :t:`literal` or the result of a computation, that may
be stored in a memory location, and interpreted based on some :t:`type`.

.. _fls_h03noz6jzpyl:

value expression
^^^^^^^^^^^^^^^^


:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## value operand (value_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^

:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.

:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_2d8t0OWM8jFl:

value operand
^^^^^^^^^^^^^

:dp:`fls_ZsudiKcvG2gW`
 A :t:`value operand <value_operand>` is an :t:`operand` that supplies the :t:`value` that is assigned to an :t:`assignee operand <assignee_operand>` by an :t:`assignment expression <assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mn6tcuz5j3p`
A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.

.. _fls_7xiaXXSwy4GP:

value expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_NGGZEbmoLRbD`
A :dt:`value expression context` is an expression context that is not a
:t:`place expression context`.

.. _fls_a5xof9jlpc2e:

value operand
^^^^^^^^^^^^^


:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## variable (variable)

### Before glossary entry (origin/main)

```rst
.. _fls_donq6w1906lw:

variable
^^^^^^^^

:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.
```

### After glossary entry (generated)

```rst
.. _fls_i1Z90ltAL14P:

variable
^^^^^^^^

:dp:`fls_jNtou5RduDeg`
 A :t:`variable` is a placeholder for a :t:`value` that is allocated on the stack.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^


:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_x4seemjknk2z`
A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
assigned to an :t:`assignee operand` by an :t:`assignment expression`.


:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^


:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## variadic part (variadic_part)

### Before glossary entry (origin/main)

```rst
.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^

:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.

:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.
```

### After glossary entry (generated)

```rst
.. _fls_sfSFLJ3gmCkb:

variadic part
^^^^^^^^^^^^^

:dp:`fls_XTEndu0sdbhm`
 A :t:`variadic part <variadic_part>` indicates the presence of :t:`C <c>`-like optional parameters.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^


:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_cl4fakfkpscp`
See :s:`ValueOperand`.

.. _fls_donq6w1906lw:

variable
^^^^^^^^


:dp:`fls_9ab12k4vwsio`
A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
stack.

.. _fls_RIe80XOF8VlA:

variadic part
^^^^^^^^^^^^^


:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## variance (variance)

### Before glossary entry (origin/main)

```rst
.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^

:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.
```

### After glossary entry (generated)

```rst
.. _fls_Ji7Tc6rWA1VF:

Variance
^^^^^^^^

:dp:`fls_2wRAOZnAjJiA`
 :t:`Variance <variance>` is a property of :t:`lifetime parameters <lifetime_parameter>` and :t:`type parameters <type_parameter>` that describes the circumstances under which a :t:`generic type <generic_type>` is a :t:`subtype` of an instantiation of itself with different :t:`generic arguments <generic_argument>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ePnTyLoqJ1i7`
A :dt:`variadic part` indicates the presence of :t:`C`-like optional
parameters.


:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## visibility (visibility)

### Before glossary entry (origin/main)

```rst
.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^

:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
```

### After glossary entry (generated)

```rst
.. _fls_LRIB3VGRFCIT:

Visibility
^^^^^^^^^^

:dp:`fls_UVry1fScaPr0`
 :t:`Visibility <visibility>` is a property of :t:`fields <field>` and :t:`items <item>` that determines which :t:`modules <module>` can refer to the :t:`name` of the :t:`field` or :t:`item`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_z9D86gBFbKB5`
See :s:`VariadicPart`.

.. _fls_q0xplb4tbzpq:

variance
^^^^^^^^


:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## visibility modifier (visibility_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^

:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.
```

### After glossary entry (generated)

```rst
.. _fls_sGD4Q4kduLDr:

visibility modifier
^^^^^^^^^^^^^^^^^^^

:dp:`fls_9WnQaZnaizLK`
 A :t:`visibility modifier <visibility_modifier>` sets the :t:`visibility` of the :t:`name` of an :t:`item`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_il0krrsf09f8`
:dt:`Variance` is a property of :t:`[lifetime parameter]s` and
:t:`[type parameter]s` that describes the circumstances under which a
:t:`generic type` is a :t:`subtype` of an instantiation of itself with
different :t:`[generic argument]s`.

.. _fls_svx87y4p8fdx:

visibility
^^^^^^^^^^


:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## visible emptiness (visible_emptiness)

### Before glossary entry (origin/main)

```rst
.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^

:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.
```

### After glossary entry (generated)

```rst
.. _fls_C0YWJAAJjFeQ:

Visible emptiness
^^^^^^^^^^^^^^^^^

:dp:`fls_CkxkU4fJXlYT`
 :t:`Visible emptiness <visible_emptiness>` is a property of :t:`types <type>` and :t:`enum variants <enum_variant>` that have no :t:`values <value>` that are fully observable.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

.. _fls_xqjk8avt7t51:

visibility modifier
^^^^^^^^^^^^^^^^^^^


:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## visible empty enum variant (visible_empty_enum_variant)

### Before glossary entry (origin/main)

```rst
.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.
```

### After glossary entry (generated)

```rst
.. _fls_DYxnoZjoD5gG:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_DoWx0M3Sugjq`
 A :t:`visible empty enum variant <visible_empty_enum_variant>` is an :t:`enum variant <enum_variant>` subject to :t:`visible emptiness <visible_emptiness>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.

.. _fls_dLlUt8PrXAls:

visible emptiness
^^^^^^^^^^^^^^^^^


:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## visible empty type (visible_empty_type)

### Before glossary entry (origin/main)

```rst
.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^

:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.
```

### After glossary entry (generated)

```rst
.. _fls_3dEOU0MKZSc6:

visible empty type
^^^^^^^^^^^^^^^^^^

:dp:`fls_aZpwzUaBTscN`
 A :t:`visible empty type <visible_empty_type>` is a :t:`type` subject to :t:`visible emptiness <visible_emptiness>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.

.. _fls_EnT5zRuwviWM:

visible empty enum variant
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
