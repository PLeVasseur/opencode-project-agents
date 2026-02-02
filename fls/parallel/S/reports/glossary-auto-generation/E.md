# Glossary audit E

## Per-letter checklist
- Letter: E
- [x] Reconcile E terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate E terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for E
- [x] Update `migration-checklist.md` for all E terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint E migration`
- [x] Letter complete

## Term checklist
- [x] elaboration (elaboration)
- [x] element type (element_type)
- [x] elided (elided)
- [x] elided lifetime (elided_lifetime)
- [x] else expression (else_expression)
- [x] empty statement (empty_statement)
- [x] entity (entity)
- [x] enum (enum)
- [x] enum field (enum_field)
- [x] enum type (enum_type)
- [x] enum value (enum_value)
- [x] enum variant (enum_variant)
- [x] enum variant value (enum_variant_value)
- [x] equals expression (equals_expression)
- [x] error propagation expression (error_propagation_expression)
- [x] escaped character (escaped_character)
- [x] evaluation (evaluation)
- [x] exclusive range pattern (exclusive_range_pattern)
- [x] execution (execution)
- [x] explicit register argument (explicit_register_argument)
- [x] explicit register name (explicit_register_name)
- [x] explicitly declared entity (explicitly_declared_entity)
- [x] exported function (exported_function)
- [x] exported static (exported_static)
- [x] expression (expression)
- [x] expression statement (expression_statement)
- [x] expression-with-block (expression_with_block)
- [x] expression-without-block (expression_without_block)
- [x] external block (external_block)
- [x] external function (external_function)
- [x] external function item type (external_function_item_type)
- [x] external static (external_static)

## elaboration (elaboration)

### Before glossary entry (origin/main)

```rst
.. _fls_2sja3okj27ne:

elaboration
^^^^^^^^^^^

:dp:`fls_xoahzmwu1std`
:dt:`Elaboration` is the process by which a :t:`declaration` achieves its
runtime effects.
```

### After glossary entry (generated)

```rst
.. _fls_EzGAfQ8lITcz:

Elaboration
^^^^^^^^^^^

:dp:`fls_j3mrLbkgCQ8e`
:t:`Elaboration` is the process by which a :t:`declaration` achieves its runtime
effects.
```

### Before chapter excerpt (origin/main)

```rst
src/items.rst
:dp:`fls_s3b1cba9lfj5`
The :t:`macro expansion` of a :t:`terminated macro invocation` is treated as
zero or more :t:`[item]s` if the :t:`terminated macro invocation` appears as
an :t:`item`.

:dp:`fls_hil5f7y4xdhe`
:t:`Elaboration` is the process by which a :t:`declaration` achieves its runtime
effects.
```

### After chapter excerpt (current)

```rst
src/items.rst
:dp:`fls_s3b1cba9lfj5`
The :t:`macro expansion` of a :t:`terminated macro invocation` is treated as
zero or more :t:`[item]s` if the :t:`terminated macro invocation` appears as
an :t:`item`.

:dp:`fls_hil5f7y4xdhe`
:dt:`Elaboration` is the process by which a :t:`declaration` achieves its runtime
effects.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## element type (element_type)

### Before glossary entry (origin/main)

```rst
.. _fls_bxm4njfo2h58:

element type
^^^^^^^^^^^^

:dp:`fls_3bndijf8g9os`
An :dt:`element type` is the :t:`type` of the elements of an :t:`array type` or
a :t:`slice type`.

:dp:`fls_pvyl887dn016`
See :s:`ElementType`.
```

### After glossary entry (generated)

```rst
.. _fls_otBvEwpBpNWi:

element type
^^^^^^^^^^^^

:dp:`fls_9oXQRTPWRkSQ`
An :t:`element type` is the :t:`type` of the elements of an :t:`array type` or
a :t:`slice type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_fx7b3qv3ghca`.
src/types-and-traits.rst
* - :dp:`fls_fsyt05u9y4sl`
     - **Type**
     - **Minimum**
     - **Maximum**
   * - :dp:`fls_p9ffvtajr832`
     - :c:`i8`
     - \- (2\ :sup:`7`)
     - 2\ :sup:`7` - 1
   * - :dp:`fls_j6xan9f8udw7`
     - :c:`i16`
     - \- (2\ :sup:`15`)
     - 2\ :sup:`15` - 1
   * - :dp:`fls_4t39p3ibkzu7`
     - :c:`i32`
     - \- (2\ :sup:`31`)
     - 2\ :sup:`31` - 1
   * - :dp:`fls_egfoxke0lzje`
     - :c:`i64`
     - \- (2\ :sup:`63`)
     - 2\ :sup:`63` - 1
   * - :dp:`fls_4c4qpel1tbqs`
     - :c:`i128`
     - \- (2\ :sup:`127`)
     - 2\ :sup:`127` - 1

:dp:`fls_t9oyfmgqka6u`
:t:`Type` :c:`isize` has the same number of bits as the platform's
:t:`pointer type`, and is at least 16-bits wide.

:dp:`fls_fx7b3qv3ghca`
An :t:`array type` is a :t:`sequence type` that represents a fixed sequence
of elements.

:dp:`fls_pkts1p2dnxo`
The :t:`element type` shall be a :t:`fixed sized type`.

:dp:`fls_imr2jx6cbuzq`
The :t:`size operand` shall be a :t:`constant expression`
or an :t:`inferred constant`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_fx7b3qv3ghca`
An :dt:`array type` is a :t:`sequence type` that represents a fixed sequence
of elements.

:dp:`fls_xmmgSHsTHDtc`
An :dt:`array` is a :t:`value` of an :t:`array type`.

:dp:`fls_mRbOQQQPbVyU`
An :dt:`element type` is the :t:`type` of the elements of an :t:`array type` or
a :t:`slice type`.

:dp:`fls_pkts1p2dnxo`
The :t:`element type` shall be a :t:`fixed sized type`.

:dp:`fls_imr2jx6cbuzq`
The :t:`size operand` shall be a :t:`constant expression`
or an :t:`inferred constant`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## elided (elided)

### Before glossary entry (origin/main)

```rst
.. _fls_vygjg858yxej:

elided
^^^^^^

:dp:`fls_lo3c3n9wy6qz`
For :dt:`elided`, see :t:`elided lifetime`.
```

### After glossary entry (generated)

```rst
.. _fls_trVQN2ylkjNu:

elided
^^^^^^

:dp:`fls_4KJJN3iRj2IS`
For :t:`elided`, see :t:`elided lifetime`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_9wtuclhm7yz5`.
src/types-and-traits.rst
* :dp:`fls_Uv5CcMHPX79J`
  Other :t:`[expression]s` do not impose any additional :t:`subtyping`
  requirements.

:dp:`fls_LyvV4pOG7E4l`
Any :t:`type coercion` resulting in a :t:`method` invocation imposes the same
:t:`subtyping` requirements as an explicit invocation of that :t:`method` would.

:dp:`fls_9wtuclhm7yz5`
:t:`Lifetime elision` is a set of rules that automatically insert
:t:`[lifetime parameter]s` and/or :t:`[lifetime argument]s` when they are
elided in the source code.

:dp:`fls_JmP6O9zj8fkV`
A :t:`lifetime` may be elided either implicitly or explicitly.

:dp:`fls_5ZAQ9p7jQuc2`
A :t:`lifetime` is elided explicitly if it is the ``'_`` :t:`lifetime`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_LyvV4pOG7E4l`
Any :t:`type coercion` resulting in a :t:`method` invocation imposes the same
:t:`subtyping` requirements as an explicit invocation of that :t:`method` would.

:dp:`fls_9wtuclhm7yz5`
:t:`Lifetime elision` is a set of rules that automatically insert
:t:`[lifetime parameter]s` and/or :t:`[lifetime argument]s` when they are
elided in the source code.

:dp:`fls_HvZUV1WQH4GA`
For :dt:`elided`, see :t:`elided lifetime`.

:dp:`fls_aHW1eUlKeOgr`
An :dt:`elided lifetime` is either an :t:`unnamed lifetime` or a :t:`lifetime`
that has been explicitly omitted from a :t:`function signature` or an
:t:`implementation`.

:dp:`fls_JmP6O9zj8fkV`
A :t:`lifetime` may be elided either implicitly or explicitly.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## elided lifetime (elided_lifetime)

### Before glossary entry (origin/main)

```rst
.. _fls_l2181y5566ck:

elided lifetime
^^^^^^^^^^^^^^^

:dp:`fls_9q28407ev0a6`
An :dt:`elided lifetime` is either an :t:`unnamed lifetime` or a :t:`lifetime`
that has been explicitly omitted from a :t:`function signature` or an
:t:`implementation`.
```

### After glossary entry (generated)

```rst
.. _fls_B1vIcM7rodvm:

elided lifetime
^^^^^^^^^^^^^^^

:dp:`fls_wdmg0BFIJXIL`
An :t:`elided lifetime` is either an :t:`unnamed lifetime` or a :t:`lifetime`
that has been explicitly omitted from a :t:`function signature` or an
:t:`implementation`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_9wtuclhm7yz5`.
src/types-and-traits.rst
* :dp:`fls_Uv5CcMHPX79J`
  Other :t:`[expression]s` do not impose any additional :t:`subtyping`
  requirements.

:dp:`fls_LyvV4pOG7E4l`
Any :t:`type coercion` resulting in a :t:`method` invocation imposes the same
:t:`subtyping` requirements as an explicit invocation of that :t:`method` would.

:dp:`fls_9wtuclhm7yz5`
:t:`Lifetime elision` is a set of rules that automatically insert
:t:`[lifetime parameter]s` and/or :t:`[lifetime argument]s` when they are
elided in the source code.

:dp:`fls_JmP6O9zj8fkV`
A :t:`lifetime` may be elided either implicitly or explicitly.

:dp:`fls_5ZAQ9p7jQuc2`
A :t:`lifetime` is elided explicitly if it is the ``'_`` :t:`lifetime`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_9wtuclhm7yz5`
:t:`Lifetime elision` is a set of rules that automatically insert
:t:`[lifetime parameter]s` and/or :t:`[lifetime argument]s` when they are
elided in the source code.

:dp:`fls_HvZUV1WQH4GA`
For :dt:`elided`, see :t:`elided lifetime`.

:dp:`fls_aHW1eUlKeOgr`
An :dt:`elided lifetime` is either an :t:`unnamed lifetime` or a :t:`lifetime`
that has been explicitly omitted from a :t:`function signature` or an
:t:`implementation`.

:dp:`fls_JmP6O9zj8fkV`
A :t:`lifetime` may be elided either implicitly or explicitly.

:dp:`fls_5ZAQ9p7jQuc2`
A :t:`lifetime` is elided explicitly if it is the ``'_`` :t:`lifetime`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## else expression (else_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_ff5zp7m9d5ot:

else expression
^^^^^^^^^^^^^^^

:dp:`fls_inp7luoqkjc5`
An :dt:`else expression` is an :t:`expression` that represents either a
:t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.

:dp:`fls_2jniy6bkq1hn`
See :s:`ElseExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_m8oqueuEH8e5:

else expression
^^^^^^^^^^^^^^^

:dp:`fls_B6cjHBlEmwSk`
An :t:`else expression` is an :t:`expression` that represents either a
:t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_ehseim1p479z`
The :t:`evaluation` of a :t:`range expression` evaluates its :t:`[operand]s` in
left-to-right order.

:dp:`fls_2i4fbxbbvpf1`
An :t:`if expression` is an :t:`expression` that evaluates either a
:t:`block expression` or an :t:`else expression` depending on the :t:`value` of
its :t:`subject expression`.

:dp:`fls_5azwlk7hav1k`
An :t:`else expression` is an :t:`expression` that represents either a
:t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.

:dp:`fls_r7gzxo16esri`
The :t:`type` of the :t:`subject expression` of an :t:`if expression` shall be
:t:`type` :c:`bool`.

:dp:`fls_iv9t4nfs4f6w`
The :t:`type` of an :t:`if expression` is the :t:`type` of its
:t:`block expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_ehseim1p479z`
The :t:`evaluation` of a :t:`range expression` evaluates its :t:`[operand]s` in
left-to-right order.

:dp:`fls_2i4fbxbbvpf1`
An :t:`if expression` is an :t:`expression` that evaluates either a
:t:`block expression` or an :t:`else expression` depending on the :t:`value` of
its :t:`subject expression`.

:dp:`fls_5azwlk7hav1k`
An :dt:`else expression` is an :t:`expression` that represents either a
:t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.

:dp:`fls_r7gzxo16esri`
The :t:`type` of the :t:`subject expression` of an :t:`if expression` shall be
:t:`type` :c:`bool`.

:dp:`fls_iv9t4nfs4f6w`
The :t:`type` of an :t:`if expression` is the :t:`type` of its
:t:`block expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## empty statement (empty_statement)

### Before glossary entry (origin/main)

```rst
.. _fls_iwed9n4jz6b8:

empty statement
^^^^^^^^^^^^^^^

:dp:`fls_irw5gwuvj3nn`
An :dt:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).
```

### After glossary entry (generated)

```rst
.. _fls_jvcPQf9KZ6LV:

empty statement
^^^^^^^^^^^^^^^

:dp:`fls_kge3PCIPFfoy`
An :t:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).
```

### Before chapter excerpt (origin/main)

```rst
src/statements.rst
:dp:`fls_7zh6ziglo5iy`
An :t:`expression statement` is an :t:`expression` whose result is ignored.

:dp:`fls_kdxe1ukmgl1`
An :t:`item statement` is a :t:`statement` that is expressed as an :t:`item`.

:dp:`fls_fftdnwe22xrb`
An :t:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).

:dp:`fls_or125cqtxg9j`
A :t:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

:dp:`fls_estqu395zxgk`
:t:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.
```

### After chapter excerpt (current)

```rst
src/statements.rst
:dp:`fls_7zh6ziglo5iy`
An :dt:`expression statement` is an :t:`expression` whose result is ignored.

:dp:`fls_kdxe1ukmgl1`
An :t:`item statement` is a :t:`statement` that is expressed as an :t:`item`.

:dp:`fls_fftdnwe22xrb`
An :dt:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).

:dp:`fls_or125cqtxg9j`
A :t:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

:dp:`fls_estqu395zxgk`
:dt:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## entity (entity)

### Before glossary entry (origin/main)

```rst
.. _fls_1qu1t74ga8aa:

entity
^^^^^^

:dp:`fls_mdbck557k8sy`
An :dt:`entity` is a :t:`construct` that can be referred to within program
text, usually via a :t:`field access expression` or a :t:`path`.
```

### After glossary entry (generated)

```rst
.. _fls_C8dKGnbzb3xn:

entity
^^^^^^

:dp:`fls_E5zgv5aviy8g`
An :t:`entity` is a :t:`construct` that can be referred to within program text,
usually via a :t:`field access expression` or a :t:`path`.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_x7j6wcigqt7u`
An :t:`entity` is a :t:`construct` that can be referred to within program text,
usually via a :t:`field access expression` or a :t:`path`.

:dp:`fls_40d2g0hvq2il`
A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

:dp:`fls_lcca91wjwnpx`
A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_t1kEzrZaE1Af`
A :dt:`construct` is a syntactic element of a Rust program defined by this
specification.

:dp:`fls_x7j6wcigqt7u`
An :dt:`entity` is a :t:`construct` that can be referred to within program text,
usually via a :t:`field access expression` or a :t:`path`.

:dp:`fls_40d2g0hvq2il`
A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

:dp:`fls_lcca91wjwnpx`
A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## enum (enum)

### Before glossary entry (origin/main)

```rst
.. _fls_xnhj9fqlfs2p:

enum
^^^^

:dp:`fls_9o0ig19xh2f5`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.
```

### After glossary entry (generated)

```rst
.. _fls_puLl4GDUOuPq:

enum
^^^^

:dp:`fls_XnKg6lAZlH0w`
An :t:`enum` is an :t:`item` that declares an :t:`enum type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_s9a36zsrfqew`.
src/types-and-traits.rst
:dp:`fls_wacoqrtzvrwu`
It is a :t:`safety invariant` for a :t:`value` of :t:`type` :c:`str` to denote
a valid UTF-8 sequence of characters.

:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.

:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_n9HtRM22YEv5`
An :dt:`abstract data type` is a collection of other :t:`[type]s`.

:dp:`fls_74bRiJktNHvk`
A :dt:`field` is an element of an :t:`abstract data type`.

:dp:`fls_9ZleHwO3HlUX`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.

:dp:`fls_gbdd37seqoab`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_v4QIqcZGsG6C`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## enum field (enum_field)

### Before glossary entry (origin/main)

```rst
.. _fls_zrRydWZgm03k:

enum field
^^^^^^^^^^

:dp:`fls_J8udq05QGiEj`
An :dt:`enum field` is a :t:`field` of an :t:`enum variant`.
```

### After glossary entry (generated)

```rst
.. _fls_oBl4hFoMHsGA:

enum field
^^^^^^^^^^

:dp:`fls_fAJt681TAXVh`
An :t:`enum field` is a :t:`field` of an :t:`enum variant`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_wQTFwl88VujQ`.
src/types-and-traits.rst
:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :dt:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_1PqJYZ5eMNym`
An :dt:`enum field` is a :t:`field` of an :t:`enum variant`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :dt:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## enum type (enum_type)

### Before glossary entry (origin/main)

```rst
.. _fls_grlluqa4ucp3:

enum type
^^^^^^^^^

:dp:`fls_idwrgo87ub3i`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_o6ih6n1z1566`
See :s:`EnumDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_gO9nc1WwbOPO:

enum type
^^^^^^^^^

:dp:`fls_eN8CpX06IyyX`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.

:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_74bRiJktNHvk`
A :dt:`field` is an element of an :t:`abstract data type`.

:dp:`fls_9ZleHwO3HlUX`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.

:dp:`fls_gbdd37seqoab`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_v4QIqcZGsG6C`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.

:dp:`fls_KTzAGty3T5fF`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## enum value (enum_value)

### Before glossary entry (origin/main)

```rst
.. _fls_H6aUAUjNlx6z:

enum value
^^^^^^^^^^

:dp:`fls_QdBTdVLB2xHk`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.
```

### After glossary entry (generated)

```rst
.. _fls_b9aDFIrxcAIz:

enum value
^^^^^^^^^^

:dp:`fls_zE2GcEY0AqK4`
An :t:`enum value` is a :t:`value` of an :t:`enum type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_gbdd37seqoab`.
src/types-and-traits.rst
:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.

:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_9ZleHwO3HlUX`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.

:dp:`fls_gbdd37seqoab`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_v4QIqcZGsG6C`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.

:dp:`fls_KTzAGty3T5fF`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## enum variant (enum_variant)

### Before glossary entry (origin/main)

```rst
.. _fls_klwlx5jixwud:

enum variant
^^^^^^^^^^^^

:dp:`fls_9jq4keg9y94u`
An :dt:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_tj2s55onen6b`
See :s:`EnumVariant`.
```

### After glossary entry (generated)

```rst
.. _fls_N2903zIuXptB:

enum variant
^^^^^^^^^^^^

:dp:`fls_uttxH1RzC9Cr`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_KTzAGty3T5fF`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :dt:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_1PqJYZ5eMNym`
An :dt:`enum field` is a :t:`field` of an :t:`enum variant`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## enum variant value (enum_variant_value)

### Before glossary entry (origin/main)

```rst
.. _fls_mKxBWCojhnWu:

enum variant value
^^^^^^^^^^^^^^^^^^

:dp:`fls_VQRqNPFFWmDp`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.
```

### After glossary entry (generated)

```rst
.. _fls_xpp4j7Lgnd0C:

enum variant value
^^^^^^^^^^^^^^^^^^

:dp:`fls_nonueKnfWmww`
An :t:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_gbdd37seqoab`.
src/types-and-traits.rst
:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.

:dp:`fls_gbdd37seqoab`
An :t:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_gbdd37seqoab`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.

:dp:`fls_v4QIqcZGsG6C`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.

:dp:`fls_KTzAGty3T5fF`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.

:dp:`fls_il9a1olqmu38`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`fls_wQTFwl88VujQ`
An :dt:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## equals expression (equals_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_alifv570nx7q:

equals expression
^^^^^^^^^^^^^^^^^

:dp:`fls_mn1g2hijtd6f`
An :dt:`equals expression` is a :t:`comparison expression` that tests equality.

:dp:`fls_j32l4do0xw4d`
See :s:`EqualsExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_cfzg0wxdgUCe:

equals expression
^^^^^^^^^^^^^^^^^

:dp:`fls_N93p8Vvkpvjn`
An :t:`equals expression` is a :t:`comparison expression` that tests equality.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_asfrqemqviad`
A :t:`comparison expression` implicitly takes :t:`[shared borrow]s` of its
:t:`[operand]s`.

:dp:`fls_9s4re3ujnfis`
The :t:`type` of a :t:`comparison expression` is :t:`type` :c:`bool`.

:dp:`fls_ruyho6cu7rxg`
An :t:`equals expression` is a :t:`comparison expression` that tests equality.

:dp:`fls_8echqk9po1cf`
The :t:`type` of the :t:`left operand` of an :t:`equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_d62qfloqk2ub`
The :t:`value` of an :t:`equals expression` is the result of
``core::cmp::PartialEq::eq(&left_operand, &right_operand)``.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_asfrqemqviad`
A :t:`comparison expression` implicitly takes :t:`[shared borrow]s` of its
:t:`[operand]s`.

:dp:`fls_9s4re3ujnfis`
The :t:`type` of a :t:`comparison expression` is :t:`type` :c:`bool`.

:dp:`fls_ruyho6cu7rxg`
An :dt:`equals expression` is a :t:`comparison expression` that tests equality.

:dp:`fls_8echqk9po1cf`
The :t:`type` of the :t:`left operand` of an :t:`equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_d62qfloqk2ub`
The :t:`value` of an :t:`equals expression` is the result of
``core::cmp::PartialEq::eq(&left_operand, &right_operand)``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## error propagation expression (error_propagation_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_kz7tgpi8xkt4:

error propagation expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_5kebgodxtqqt`
An :dt:`error propagation expression` is an :t:`expression` that either
evaluates to a :t:`value` of its :t:`operand` or returns a value to the next
control flow boundary.

:dp:`fls_agyqvyda3rcj`
See :s:`ErrorPropagationExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_dqwLLMpyyzEl:

error propagation expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_o6LOCqh0V9oy`
An :t:`error propagation expression` is an :t:`expression` that either evaluates
to a :t:`value` of its :t:`operand` or returns a value to the enclosing control
flow boundary.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_9wgldua1u8yt`
It is undefined behavior to dereference a :t:`raw pointer` that is either
:t:`dangling` or unaligned.

:dp:`fls_9ifaterm8nop`
See :p:`fls_350qejoq9i23` for the declaration of ``ref_answer``.

:dp:`fls_8q59wbumrt5s`
An :t:`error propagation expression` is an :t:`expression` that either evaluates
to a :t:`value` of its :t:`operand` or returns a value to the enclosing control
flow boundary.

:dp:`fls_mq2h4seoxah`
An :t:`error propagation expression` shall appear within a :t:`control flow
boundary`.

:dp:`fls_ab4vhq4nwn7f`
The :t:`type` of an :t:`error propagation expression` is :t:`associated type`
:std:`core::ops::Try::Output`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_9wgldua1u8yt`
It is undefined behavior to dereference a :t:`raw pointer` that is either
:t:`dangling` or unaligned.

:dp:`fls_9ifaterm8nop`
See :p:`fls_350qejoq9i23` for the declaration of ``ref_answer``.

:dp:`fls_8q59wbumrt5s`
An :dt:`error propagation expression` is an :t:`expression` that either evaluates
to a :t:`value` of its :t:`operand` or returns a value to the enclosing control
flow boundary.

:dp:`fls_mq2h4seoxah`
An :t:`error propagation expression` shall appear within a :t:`control flow
boundary`.

:dp:`fls_ab4vhq4nwn7f`
The :t:`type` of an :t:`error propagation expression` is :t:`associated type`
:std:`core::ops::Try::Output`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## escaped character (escaped_character)

### Before glossary entry (origin/main)

```rst
.. _fls_9hw559b548m0:

escaped character
^^^^^^^^^^^^^^^^^

:dp:`fls_7yvnbakmo7y5`
An :dt:`escaped character` is the textual representation for a character with
special meaning. An escaped character consists of character 0x5C (reverse
solidus), followed by the single character encoding of the special meaning
character. For example, ``\t`` is the escaped character for 0x09 (horizontal
tabulation).
```

### After glossary entry (generated)

```rst
.. _fls_fTOq9xkgWnCw:

escaped character
^^^^^^^^^^^^^^^^^

:dp:`fls_w9ZH6q49Svvg`
An :t:`escaped character` is the textual representation for a character with
special meaning. An escaped character consists of character 0x5C (reverse
solidus), followed by the single character encoding of the special meaning
character. For example, ``\t`` is the escaped character for 0x09 (horizontal
tabulation).
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_x2cw7g8g56f8`.
src/lexical-elements.rst
* :dp:`fls_4sxt1ct7fyen`
  If a :t:`floating-point type` can be uniquely determined from the surrounding
  program context, then the :t:`unsuffixed float` has that :t:`type`.

* :dp:`fls_wa72rssp0jnt`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`f64`.

* :dp:`fls_x2cw7g8g56f8`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_j9q9ton57rvl`
A :ds:`CharacterLiteralCharacter` is any :t:`Unicode` character except
characters 0x09 (horizontal tabulation), 0x0A (new line), 0x0D (carriage
return), 0x27 (apostrophe), and 0x5c (reverse solidus).

:dp:`fls_5v9gx22g5wPm`
A :ds:`UnicodeEscape` starts with a ``\u{`` literal, followed by 1 to 6
instances of a :s:`HexadecimalDigit`, inclusive, followed by a ``}`` character.
It can represent any :t:`Unicode` codepoint between U+00000 and U+10FFFF,
inclusive, except :t:`Unicode` surrogate codepoints, which exist between
the range of U+D800 and U+DFFF, inclusive.
```

### After chapter excerpt (current)

```rst
src/lexical-elements.rst
* :dp:`fls_wa72rssp0jnt`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`f64`.

* :dp:`fls_x2cw7g8g56f8`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_TXk2yFGh8at5`
An :dt:`escaped character` is the textual representation for a character with
special meaning. An escaped character consists of character 0x5C (reverse
solidus), followed by the single character encoding of the special meaning
character. For example, ``\t`` is the escaped character for 0x09 (horizontal
tabulation).

:dp:`fls_j9q9ton57rvl`
A :ds:`CharacterLiteralCharacter` is any :t:`Unicode` character except
characters 0x09 (horizontal tabulation), 0x0A (new line), 0x0D (carriage
return), 0x27 (apostrophe), and 0x5c (reverse solidus).

:dp:`fls_5v9gx22g5wPm`
A :ds:`UnicodeEscape` starts with a ``\u{`` literal, followed by 1 to 6
instances of a :s:`HexadecimalDigit`, inclusive, followed by a ``}`` character.
It can represent any :t:`Unicode` codepoint between U+00000 and U+10FFFF,
inclusive, except :t:`Unicode` surrogate codepoints, which exist between
the range of U+D800 and U+DFFF, inclusive.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## evaluation (evaluation)

### Before glossary entry (origin/main)

```rst
.. _fls_p3gre0895k2u:

evaluation
^^^^^^^^^^

:dp:`fls_8zmtio6razl1`
:dt:`Evaluation` is the process by which an :t:`expression` achieves its
runtime effects.
```

### After glossary entry (generated)

```rst
.. _fls_vcXdxrJRH2bf:

Evaluation
^^^^^^^^^^

:dp:`fls_rbA8pxcb4HMl`
:t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
effects.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_2j132xueobfv`
A :t:`subject expression` is an :t:`expression` that controls :t:`[for loop]s`,
:t:`[if expression]s`, and :t:`[match expression]s`.

:dp:`fls_a243nclqqjlu`
A :t:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

:dp:`fls_1223lwh4nq49`
:t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
effects.

:dp:`fls_oqj7s9fi3j3j`
An :t:`assignee expression` is an :t:`expression` that appears as the
:t:`left operand` of an :t:`assignment expression`. The following
:t:`[expression]s` are :t:`[assignee expression]s`:

* :dp:`fls_skopz71arbwa`
  :t:`[Place expression]s`,
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_2j132xueobfv`
A :t:`subject expression` is an :t:`expression` that controls :t:`[for loop]s`,
:t:`[if expression]s`, and :t:`[match expression]s`.

:dp:`fls_a243nclqqjlu`
A :t:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

:dp:`fls_1223lwh4nq49`
:dt:`Evaluation` is the process by which an :t:`expression` achieves its runtime
effects.

:dp:`fls_oqj7s9fi3j3j`
An :dt:`assignee expression` is an :t:`expression` that appears as the
:t:`left operand` of an :t:`assignment expression`. The following
:t:`[expression]s` are :t:`[assignee expression]s`:

* :dp:`fls_skopz71arbwa`
  :t:`[Place expression]s`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## exclusive range pattern (exclusive_range_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_EJSzYb4IxvtR:

exclusive range pattern
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_qxsV6ZxFfDHm`
An :dt:`exclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_kHIWYUPhxikM`
See :s:`ExclusiveRangePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_zCcRqOXtUBy5:

exclusive range pattern
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2E5jWhwio4jr`
An :t:`exclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.
```

### Before chapter excerpt (origin/main)

```rst
src/patterns.rst
:dp:`fls_jhchm7dy927k`
A :t:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.

:dp:`fls_q86j23iiqv8w`
An :t:`inclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_3PyquOKjA7SI`
An :t:`exclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_akf9x5r6e0ta`
An :t:`obsolete range pattern` is a :t:`range pattern` that uses obsolete syntax
to express an :t:`inclusive range pattern`.

:dp:`fls_vrpr6ttpfpal`
A :t:`range pattern bound` is a constraint on the range of a :t:`range pattern`.
```

### After chapter excerpt (current)

```rst
src/patterns.rst
:dp:`fls_jhchm7dy927k`
A :t:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.

:dp:`fls_q86j23iiqv8w`
An :t:`inclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_3PyquOKjA7SI`
An :dt:`exclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_akf9x5r6e0ta`
An :t:`obsolete range pattern` is a :t:`range pattern` that uses obsolete syntax
to express an :t:`inclusive range pattern`.

:dp:`fls_vrpr6ttpfpal`
A :t:`range pattern bound` is a constraint on the range of a :t:`range pattern`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## execution (execution)

### Before glossary entry (origin/main)

```rst
.. _fls_q0ur239s8uv:

execution
^^^^^^^^^

:dp:`fls_e5jbii84hd5g`
:dt:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.
```

### After glossary entry (generated)

```rst
.. _fls_DYeZMWhW6i9s:

Execution
^^^^^^^^^

:dp:`fls_sGEkvucGWVE9`
:t:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.
```

### Before chapter excerpt (origin/main)

```rst
src/statements.rst
:dp:`fls_fftdnwe22xrb`
An :t:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).

:dp:`fls_or125cqtxg9j`
A :t:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

:dp:`fls_estqu395zxgk`
:t:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.

:dp:`fls_dl763ssb54q1`
The :t:`execution` of an :t:`empty statement` has no effect.

:dp:`fls_ct7pp7jnfr86`
A :t:`let statement` is a :t:`statement` that introduces new :t:`[binding]s`
produced by its :t:`pattern-without-alternation` that are optionally
initialized to a :t:`value`.
```

### After chapter excerpt (current)

```rst
src/statements.rst
:dp:`fls_fftdnwe22xrb`
An :dt:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).

:dp:`fls_or125cqtxg9j`
A :t:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

:dp:`fls_estqu395zxgk`
:dt:`Execution` is the process by which a :t:`statement` achieves its runtime
effects.

:dp:`fls_dl763ssb54q1`
The :t:`execution` of an :t:`empty statement` has no effect.

:dp:`fls_ct7pp7jnfr86`
A :t:`let statement` is a :t:`statement` that introduces new :t:`[binding]s`
produced by its :t:`pattern-without-alternation` that are optionally
initialized to a :t:`value`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## explicit register argument (explicit_register_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_B1qkkSvc69J4:

explicit register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2o6S1WGDrMh3`
An :dt:`explicit register argument` is a :t:`register argument` that uses an
:t:`explicit register name`.
```

### After glossary entry (generated)

```rst
.. _fls_NZnpptMspl73:

explicit register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_cr8Iz6xU2otg`
An :t:`explicit register argument` is a :t:`register argument` that uses an
:t:`explicit register name`.
```

### Before chapter excerpt (origin/main)

```rst
src/inline-assembly.rst
:dp:`fls_sqs5to20p0te`
A :t:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

:dp:`fls_dzlycyk24euk`
A :t:`named register argument` shall appear after a
:t:`positional register argument`.

:dp:`fls_ics6gdzww1p`
An :t:`explicit register argument` is a :t:`register argument` that uses an
:t:`explicit register name`.

:dp:`fls_mmc1w8jjr55r`
An :t:`explicit register argument` shall appear after a
:t:`named register argument`.

:dp:`fls_9hhtcey2d4t6`
A :t:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.
```

### After chapter excerpt (current)

```rst
src/inline-assembly.rst
:dp:`fls_sqs5to20p0te`
A :t:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

:dp:`fls_dzlycyk24euk`
A :t:`named register argument` shall appear after a
:t:`positional register argument`.

:dp:`fls_ics6gdzww1p`
An :dt:`explicit register argument` is a :t:`register argument` that uses an
:t:`explicit register name`.

:dp:`fls_mmc1w8jjr55r`
An :t:`explicit register argument` shall appear after a
:t:`named register argument`.

:dp:`fls_9hhtcey2d4t6`
A :t:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## explicit register name (explicit_register_name)

### Before glossary entry (origin/main)

```rst
.. _fls_uc7PnSbVVd9X:

explicit register name
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_UcMk6RRLrkB5`
An :dt:`explicit register name` is a target-specific string that identifies
a :t:`register`.

:dp:`fls_Z3WDh75VpSUU`
See :s:`ExplicitRegisterName`.
```

### After glossary entry (generated)

```rst
.. _fls_zs3JRHsBt9CJ:

explicit register name
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_LlASxHzyYpfL`
An :t:`explicit register name` is a target-specific string that identifies
a :t:`register`.
```

### Before chapter excerpt (origin/main)

```rst
src/inline-assembly.rst
:dp:`fls_HV3Y1A2xn0zr`
A :t:`register` that is not specified as an :t:`output register` shall have the
same :t:`value` upon exit from an :t:`assembly code block` as it did upon entry
into the :t:`assembly code block`.

:dp:`fls_vesfzh8h6qzu`
A :t:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.

:dp:`fls_ffwqxlh60i5w`
An :t:`explicit register name` is a target-specific string that identifies
a :t:`register`.

:dp:`fls_3p8akc7gcsnx`
An :t:`explicit register name` may be aliased as follows:

   * - :dp:`fls_7dlx7nt77xk`
     - **Architecture**
     - **Explicit register name**
     - **Aliases**
   * - :dp:`fls_w4z7yh5qyyed`
     - AArch64
     - ``sp``
     - ``wsp``
   * - :dp:`fls_rzp8eg6z6x3q`
     - AArch64
     - ``v[0-31]``
     - ``b[0-31]``, ``d[0-31]``, ``h[0-31]``, ``q[0-31]``, ``s[0-31]``
   * - :dp:`fls_e1w41918j49`
     - AArch64
     - ``x[0-30]``
     - ``w[0-30]``
   * - :dp:`fls_q0s90h7xmnn4`
     - AArch64
     - ``x29``
     - ``fp``
   * - :dp:`fls_3pt63w76isay`
     - AArch64
     - ``x30``
     - ``lr``
   * - :dp:`fls_f3clxd3vidhh`
     - AArch64
     - ``xzr``
     - ``wzr``
   * - :dp:`fls_vyeczg1cjxys`
     - ARM
     - ``r[0-3]``
     - ``a[1-4]``
   * - :dp:`fls_h5t153uhzoq3`
     - ARM
     - ``r[4-9]``
     - ``v[1-6]``
   * - :dp:`fls_jhph577nqds1`
     - ARM
     - ``r9``
     - ``rfp``
   * - :dp:`fls_mobj1y67vxvb`
     - ARM
     - ``r10``
     - ``sl``
   * - :dp:`fls_9ke412je1hqn`
     - ARM
     - ``r11``
     - ``fp``
   * - :dp:`fls_hndlas58937e`
     - ARM
     - ``r12``
     - ``ip``
   * - :dp:`fls_5x0yvjil3z8p`
     - ARM
     - ``r13``
     - ``sp``
   * - :dp:`fls_gxvlvnqs436h`
     - ARM
     - ``r14``
     - ``lr``
   * - :dp:`fls_mra7zuu7uzmb`
     - ARM
     - ``r15``
     - ``pc``
   * - :dp:`fls_maa7w0jwvat2`
     - RISC-V
     - ``f[0-7]``
     - ``ft[0-7]``
   * - :dp:`fls_az7kcaq70h4d`
     - RISC-V
     - ``f[8-9]``
     - ``fs[0-1]``
   * - :dp:`fls_xudmsflrhvo3`
     - RISC-V
     - ``f[10-17]``
     - ``fa[0-7]``
   * - :dp:`fls_px77cr1k8coy`
     - RISC-V
     - ``f[18-27]``
     - ``fs[2-11]``
   * - :dp:`fls_y1m7tlqk2dv7`
     - RISC-V
     - ``f[28-31]``
     - ``ft[8-11]``
   * - :dp:`fls_3dqq9319okv5`
     - RISC-V
     - ``x0``
     - ``zero``
   * - :dp:`fls_5l9qo5c0gek8`
     - RISC-V
     - ``x1``
     - ``ra``
   * - :dp:`fls_1m68zqsxjuyp`
     - RISC-V
     - ``x2``
     - ``sp``
   * - :dp:`fls_bck9slu4hsn1`
     - RISC-V
     - ``x3``
     - ``gp``
   * - :dp:`fls_3x72q39c8iwt`
     - RISC-V
     - ``x4``
     - ``tp``
   * - :dp:`fls_yfbrla8c801g`
     - RISC-V
     - ``x[5-7]``
     - ``t[0-2]``
   * - :dp:`fls_3nuf1gcldamv`
     - RISC-V
     - ``x8``
     - ``fp``, ``s0``
   * - :dp:`fls_nquf1uaoezx6`
     - RISC-V
     - ``x9``
     - ``s1``
   * - :dp:`fls_91oeyxc75vu5`
     - RISC-V
     - ``x[10-17]``
     - ``a[0-7]``
   * - :dp:`fls_r5btazdpwqtw`
     - RISC-V
     - ``x[18-27]``
     - ``s[2-11]``
   * - :dp:`fls_vpibsan8aful`
     - RISC-V
     - ``x[28-31]``
     - ``t[3-6]``
   * - :dp:`fls_lj6xcaaecokk`
     - x86
     - ``ax``
     - ``eax``, ``rax``
   * - :dp:`fls_bb1qjfin4zjc`
     - x86
     - ``bp``
     - ``bpl``, ``ebp``, ``rbp``
   * - :dp:`fls_7qj6pxuq2x9e`
     - x86
     - ``bx``
     - ``ebx``, ``rbx``
   * - :dp:`fls_2xkw4nqt1s5a`
     - x86
     - ``cx``
     - ``ecx``, ``rcx``
   * - :dp:`fls_dpzi4ygox7jw`
     - x86
     - ``di``
     - ``edi``, ``rdi``
   * - :dp:`fls_yr5ztipvgezk`
     - x86
     - ``dx``
     - ``edx``, ``rdx``
   * - :dp:`fls_n8ccafjut1yd`
     - x86
     - ``ip``
     - ``eip``, ``rip``
   * - :dp:`fls_iv23mcgw6l3r`
     - x86
     - ``r[8-15]``
     - ``r[8-15]b``, ``r[8-15]d``, ``r[8-15]w``
   * - :dp:`fls_yr7bac5k3uk7`
     - x86
     - ``si``
     - ``esi``, ``rsi``
   * - :dp:`fls_gvb2zcrseqci`
     - x86
     - ``sp``
     - ``esp``, ``rsp``, ``spl``
   * - :dp:`fls_z1b9nf49nbjh`
     - x86
     - ``st(0)``
     - ``st``
   * - :dp:`fls_etfkcesnrlwt`
     - x86
     - ``xmm[0-31]``
     - ``ymm[0-31]``, ``zmm[0-31]``
```

### After chapter excerpt (current)

```rst
src/inline-assembly.rst
:dp:`fls_HV3Y1A2xn0zr`
A :t:`register` that is not specified as an :t:`output register` shall have the
same :t:`value` upon exit from an :t:`assembly code block` as it did upon entry
into the :t:`assembly code block`.

:dp:`fls_vesfzh8h6qzu`
A :t:`register name` is either the :t:`explicit register name` of a
:t:`register`, or the :t:`register class name` of the :t:`register class` a
:t:`register` belongs to.

:dp:`fls_ffwqxlh60i5w`
An :dt:`explicit register name` is a target-specific string that identifies
a :t:`register`.

:dp:`fls_3p8akc7gcsnx`
An :t:`explicit register name` may be aliased as follows:

   * - :dp:`fls_7dlx7nt77xk`
     - **Architecture**
     - **Explicit register name**
     - **Aliases**
   * - :dp:`fls_w4z7yh5qyyed`
     - AArch64
     - ``sp``
     - ``wsp``
   * - :dp:`fls_rzp8eg6z6x3q`
     - AArch64
     - ``v[0-31]``
     - ``b[0-31]``, ``d[0-31]``, ``h[0-31]``, ``q[0-31]``, ``s[0-31]``
   * - :dp:`fls_e1w41918j49`
     - AArch64
     - ``x[0-30]``
     - ``w[0-30]``
   * - :dp:`fls_q0s90h7xmnn4`
     - AArch64
     - ``x29``
     - ``fp``
   * - :dp:`fls_3pt63w76isay`
     - AArch64
     - ``x30``
     - ``lr``
   * - :dp:`fls_f3clxd3vidhh`
     - AArch64
     - ``xzr``
     - ``wzr``
   * - :dp:`fls_vyeczg1cjxys`
     - ARM
     - ``r[0-3]``
     - ``a[1-4]``
   * - :dp:`fls_h5t153uhzoq3`
     - ARM
     - ``r[4-9]``
     - ``v[1-6]``
   * - :dp:`fls_jhph577nqds1`
     - ARM
     - ``r9``
     - ``rfp``
   * - :dp:`fls_mobj1y67vxvb`
     - ARM
     - ``r10``
     - ``sl``
   * - :dp:`fls_9ke412je1hqn`
     - ARM
     - ``r11``
     - ``fp``
   * - :dp:`fls_hndlas58937e`
     - ARM
     - ``r12``
     - ``ip``
   * - :dp:`fls_5x0yvjil3z8p`
     - ARM
     - ``r13``
     - ``sp``
   * - :dp:`fls_gxvlvnqs436h`
     - ARM
     - ``r14``
     - ``lr``
   * - :dp:`fls_mra7zuu7uzmb`
     - ARM
     - ``r15``
     - ``pc``
   * - :dp:`fls_maa7w0jwvat2`
     - RISC-V
     - ``f[0-7]``
     - ``ft[0-7]``
   * - :dp:`fls_az7kcaq70h4d`
     - RISC-V
     - ``f[8-9]``
     - ``fs[0-1]``
   * - :dp:`fls_xudmsflrhvo3`
     - RISC-V
     - ``f[10-17]``
     - ``fa[0-7]``
   * - :dp:`fls_px77cr1k8coy`
     - RISC-V
     - ``f[18-27]``
     - ``fs[2-11]``
   * - :dp:`fls_y1m7tlqk2dv7`
     - RISC-V
     - ``f[28-31]``
     - ``ft[8-11]``
   * - :dp:`fls_3dqq9319okv5`
     - RISC-V
     - ``x0``
     - ``zero``
   * - :dp:`fls_5l9qo5c0gek8`
     - RISC-V
     - ``x1``
     - ``ra``
   * - :dp:`fls_1m68zqsxjuyp`
     - RISC-V
     - ``x2``
     - ``sp``
   * - :dp:`fls_bck9slu4hsn1`
     - RISC-V
     - ``x3``
     - ``gp``
   * - :dp:`fls_3x72q39c8iwt`
     - RISC-V
     - ``x4``
     - ``tp``
   * - :dp:`fls_yfbrla8c801g`
     - RISC-V
     - ``x[5-7]``
     - ``t[0-2]``
   * - :dp:`fls_3nuf1gcldamv`
     - RISC-V
     - ``x8``
     - ``fp``, ``s0``
   * - :dp:`fls_nquf1uaoezx6`
     - RISC-V
     - ``x9``
     - ``s1``
   * - :dp:`fls_91oeyxc75vu5`
     - RISC-V
     - ``x[10-17]``
     - ``a[0-7]``
   * - :dp:`fls_r5btazdpwqtw`
     - RISC-V
     - ``x[18-27]``
     - ``s[2-11]``
   * - :dp:`fls_vpibsan8aful`
     - RISC-V
     - ``x[28-31]``
     - ``t[3-6]``
   * - :dp:`fls_lj6xcaaecokk`
     - x86
     - ``ax``
     - ``eax``, ``rax``
   * - :dp:`fls_bb1qjfin4zjc`
     - x86
     - ``bp``
     - ``bpl``, ``ebp``, ``rbp``
   * - :dp:`fls_7qj6pxuq2x9e`
     - x86
     - ``bx``
     - ``ebx``, ``rbx``
   * - :dp:`fls_2xkw4nqt1s5a`
     - x86
     - ``cx``
     - ``ecx``, ``rcx``
   * - :dp:`fls_dpzi4ygox7jw`
     - x86
     - ``di``
     - ``edi``, ``rdi``
   * - :dp:`fls_yr5ztipvgezk`
     - x86
     - ``dx``
     - ``edx``, ``rdx``
   * - :dp:`fls_n8ccafjut1yd`
     - x86
     - ``ip``
     - ``eip``, ``rip``
   * - :dp:`fls_iv23mcgw6l3r`
     - x86
     - ``r[8-15]``
     - ``r[8-15]b``, ``r[8-15]d``, ``r[8-15]w``
   * - :dp:`fls_yr7bac5k3uk7`
     - x86
     - ``si``
     - ``esi``, ``rsi``
   * - :dp:`fls_gvb2zcrseqci`
     - x86
     - ``sp``
     - ``esp``, ``rsp``, ``spl``
   * - :dp:`fls_z1b9nf49nbjh`
     - x86
     - ``st(0)``
     - ``st``
   * - :dp:`fls_etfkcesnrlwt`
     - x86
     - ``xmm[0-31]``
     - ``ymm[0-31]``, ``zmm[0-31]``
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## explicitly declared entity (explicitly_declared_entity)

### Before glossary entry (origin/main)

```rst
.. _fls_lqxcnZqvwcsH:

explicitly declared entity
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_shpNJ0JCSCwa`
An :dt:`explicitly declared entity` is an :t:`entity` that has a
:t:`declaration`.
```

### After glossary entry (generated)

```rst
.. _fls_HwVAdB20j1dE:

explicitly declared entity
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_TQdCw2PkpM5F`
An :t:`explicitly declared entity` is an :t:`entity` that has a
:t:`declaration`. The following :t:`entities <entity>` are
:t:`explicitly declared entities <explicitly declared entity>`:
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_40d2g0hvq2il`
A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

:dp:`fls_lcca91wjwnpx`
A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.

:dp:`fls_94l2d7ti0hjw`
An :t:`explicitly declared entity` is an :t:`entity` that has a
:t:`declaration`. The following :t:`entities <entity>` are
:t:`explicitly declared entities <explicitly declared entity>`:

* :dp:`fls_kvdqmo8gmdxi`
  :t:`[Associated item]s`,

* :dp:`fls_b3cdg74utyvo`
  :t:`[Binding]s`,
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_40d2g0hvq2il`
A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

:dp:`fls_lcca91wjwnpx`
A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.

:dp:`fls_94l2d7ti0hjw`
An :dt:`explicitly declared entity` is an :t:`entity` that has a
:t:`declaration`. The following :t:`entities <entity>` are
:t:`explicitly declared entities <explicitly declared entity>`:

* :dp:`fls_kvdqmo8gmdxi`
  :t:`[Associated item]s`,

* :dp:`fls_b3cdg74utyvo`
  :t:`[Binding]s`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## exported function (exported_function)

### Before glossary entry (origin/main)

```rst
.. _fls_5oQllRM7Wjsg:

exported function
^^^^^^^^^^^^^^^^^

:dp:`fls_QotMF1iaEYod`
An :dt:`exported function` is an export of a :t:`function`.
```

### After glossary entry (generated)

```rst
.. _fls_05XsUAj1jF2O:

exported function
^^^^^^^^^^^^^^^^^

:dp:`fls_rSFSR17DYDmh`
An :t:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.
```

### Before chapter excerpt (origin/main)

```rst
src/attributes.rst
:dp:`fls_esaew4fqk8mm`
:t:`Attribute` :dc:`no_mangle` indicates that the :t:`name` of the related
:t:`function` or :t:`static` will be used as the symbol for that :t:`function`
or :t:`static`.

:dp:`fls_lvnclpxbye9u`
:t:`Attribute` :c:`no_mangle` causes the related :t:`function` or :t:`static` to
be publicly exported from the produced library or object file.

:dp:`fls_VKuSiswPMll7`
An :t:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_I029Rvr5BX5P`
An :t:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_vetjq9sw84qc`
:t:`Attribute` :c:`repr` shall apply to :t:`[abstract data type]s`.
```

### After chapter excerpt (current)

```rst
src/attributes.rst
:dp:`fls_esaew4fqk8mm`
:t:`Attribute` :dc:`no_mangle` indicates that the :t:`name` of the related
:t:`function` or :t:`static` will be used as the symbol for that :t:`function`
or :t:`static`.

:dp:`fls_lvnclpxbye9u`
:t:`Attribute` :c:`no_mangle` causes the related :t:`function` or :t:`static` to
be publicly exported from the produced library or object file.

:dp:`fls_VKuSiswPMll7`
An :dt:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_I029Rvr5BX5P`
An :dt:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_vetjq9sw84qc`
:t:`Attribute` :c:`repr` shall apply to :t:`[abstract data type]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## exported static (exported_static)

### Before glossary entry (origin/main)

```rst
.. _fls_zkq5ZkJwsyoD:

exported static
^^^^^^^^^^^^^^^^^

:dp:`fls_aolCSvb349ZU`
An :dt:`exported static` is an export of a :t:`static`.
```

### After glossary entry (generated)

```rst
.. _fls_bPdLcDwO8iJ7:

exported static
^^^^^^^^^^^^^^^

:dp:`fls_aGylWf382nr7`
An :t:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.
```

### Before chapter excerpt (origin/main)

```rst
src/attributes.rst
:dp:`fls_lvnclpxbye9u`
:t:`Attribute` :c:`no_mangle` causes the related :t:`function` or :t:`static` to
be publicly exported from the produced library or object file.

:dp:`fls_VKuSiswPMll7`
An :t:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_I029Rvr5BX5P`
An :t:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_vetjq9sw84qc`
:t:`Attribute` :c:`repr` shall apply to :t:`[abstract data type]s`.

:dp:`fls_is2esjz1sy36`
:t:`Attribute` :dc:`repr` shall indicate the :t:`type representation` of the
related :t:`type`.
```

### After chapter excerpt (current)

```rst
src/attributes.rst
:dp:`fls_lvnclpxbye9u`
:t:`Attribute` :c:`no_mangle` causes the related :t:`function` or :t:`static` to
be publicly exported from the produced library or object file.

:dp:`fls_VKuSiswPMll7`
An :dt:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_I029Rvr5BX5P`
An :dt:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.

:dp:`fls_vetjq9sw84qc`
:t:`Attribute` :c:`repr` shall apply to :t:`[abstract data type]s`.

:dp:`fls_is2esjz1sy36`
:t:`Attribute` :dc:`repr` shall indicate the :t:`type representation` of the
related :t:`type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## expression (expression)

### Before glossary entry (origin/main)

```rst
.. _fls_q8ofwncggngd:

expression
^^^^^^^^^^

:dp:`fls_f7iuwgbs1lql`
An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may
have side effects at run-time.

:dp:`fls_8l9hru1x586q`
See :s:`Expression`.
```

### After glossary entry (generated)

```rst
.. _fls_kb7hUVXn5C04:

expression
^^^^^^^^^^

:dp:`fls_OVdKljqmP0w4`
An :t:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_pwut2jbmk66k`
A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
:s:`StructExpression`.

:dp:`fls_361q9ljc6ybz`
A :ds:`SubjectLetExpression` is any expression in category
:s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

:dp:`fls_h5o6tgul4yor`
An :t:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :t:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :t:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_pwut2jbmk66k`
A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
:s:`StructExpression`.

:dp:`fls_361q9ljc6ybz`
A :ds:`SubjectLetExpression` is any expression in category
:s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

:dp:`fls_h5o6tgul4yor`
An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :dt:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## expression statement (expression_statement)

### Before glossary entry (origin/main)

```rst
.. _fls_a1rorkjt3vpc:

expression statement
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ds0pspiqk4am`
An :dt:`expression statement` is an :t:`expression` whose result is ignored.

:dp:`fls_41jt1h3audzv`
See :s:`ExpressionStatement`.
```

### After glossary entry (generated)

```rst
.. _fls_vPM6HY3vOD9b:

expression statement
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_iFm4FN5RnQo9`
An :t:`expression statement` is an :t:`expression` whose result is ignored.
```

### Before chapter excerpt (origin/main)

```rst
src/statements.rst
:dp:`fls_7zh6ziglo5iy`
An :t:`expression statement` is an :t:`expression` whose result is ignored.

:dp:`fls_kdxe1ukmgl1`
An :t:`item statement` is a :t:`statement` that is expressed as an :t:`item`.

:dp:`fls_fftdnwe22xrb`
An :t:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).
```

### After chapter excerpt (current)

```rst
src/statements.rst
:dp:`fls_7zh6ziglo5iy`
An :dt:`expression statement` is an :t:`expression` whose result is ignored.

:dp:`fls_kdxe1ukmgl1`
An :t:`item statement` is a :t:`statement` that is expressed as an :t:`item`.

:dp:`fls_fftdnwe22xrb`
An :dt:`empty statement` is a :t:`statement` expressed as character 0x3B
(semicolon).
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## expression-with-block (expression_with_block)

### Before glossary entry (origin/main)

```rst
.. _fls_u6huewic8650:

expression-with-block
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ujlm50le5dnj`
An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_iwheys965ml3`
See :s:`ExpressionWithBlock`.
```

### After glossary entry (generated)

```rst
.. _fls_8wRQZGUul4VX:

expression-with-block
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_t6VnXOzLIqZt`
An :t:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_361q9ljc6ybz`
A :ds:`SubjectLetExpression` is any expression in category
:s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

:dp:`fls_h5o6tgul4yor`
An :t:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :t:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :t:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.

:dp:`fls_gwgttltgjma4`
An :t:`operand` is an :t:`expression` nested within an :t:`expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_361q9ljc6ybz`
A :ds:`SubjectLetExpression` is any expression in category
:s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

:dp:`fls_h5o6tgul4yor`
An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :dt:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.

:dp:`fls_gwgttltgjma4`
An :t:`operand` is an :t:`expression` nested within an :t:`expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## expression-without-block (expression_without_block)

### Before glossary entry (origin/main)

```rst
.. _fls_378e2xhxzk26:

expression-without-block
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_xfh9xmsphzqb`
An :dt:`expression-without-block` is an :t:`expression` whose structure does
not involve a :t:`block expression`.

:dp:`fls_miaphjnikd51`
See :s:`ExpressionWithoutBlock`.
```

### After glossary entry (generated)

```rst
.. _fls_28glTnQMa7wb:

expression-without-block
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8mLpxkQtlRei`
An :t:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_h5o6tgul4yor`
An :t:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :t:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :t:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.

:dp:`fls_gwgttltgjma4`
An :t:`operand` is an :t:`expression` nested within an :t:`expression`.

:dp:`fls_1r29rtnjlkql`
A :t:`left operand` is an :t:`operand` that appears on the left-hand side of a
:t:`binary operator`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_h5o6tgul4yor`
An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may have
side effects at run-time.

:dp:`fls_xmklb3070sp`
An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
:t:`block expression`.

:dp:`fls_p15oeage4j0e`
An :dt:`expression-without-block` is an :t:`expression` whose structure does not
involve a :t:`block expression`.

:dp:`fls_gwgttltgjma4`
An :t:`operand` is an :t:`expression` nested within an :t:`expression`.

:dp:`fls_1r29rtnjlkql`
A :t:`left operand` is an :t:`operand` that appears on the left-hand side of a
:t:`binary operator`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## external block (external_block)

### Before glossary entry (origin/main)

```rst
.. _fls_9k6jcsljghab:

external block
^^^^^^^^^^^^^^

:dp:`fls_z2ebcp7kjpuy`
An :dt:`external block` is a :t:`construct` that provides the declarations of
foreign :t:`[function]s` as unchecked imports.

:dp:`fls_dm2wz1th2haz`
See :s:`ExternalBlock`.
```

### After glossary entry (generated)

```rst
.. _fls_uJ3GZXJkxNLr:

external block
^^^^^^^^^^^^^^

:dp:`fls_xznrqItwdEur`
An :t:`external block` is a :t:`construct` that provides the declarations of
:t:`[external function]s` and :t:`[external static]s` as unchecked imports.
```

### Before chapter excerpt (origin/main)

```rst
src/ffi.rst
* :dp:`fls_JHlqXjn4Sf07`
  ``extern "efiapi"`` - The :t:`ABI` for `UEFI <https://uefi.org/specifications>`_.

:dp:`fls_M4LqHf8hbPA8`
It is undefined behavior when a foreign exception crosses a
:t:`foreign function interface` boundary with an :t:`ABI` that does not end in
``-unwind``.

:dp:`fls_4dje9t5y2dia`
An :t:`external block` is a :t:`construct` that provides the declarations of
:t:`[external function]s` and :t:`[external static]s` as unchecked imports.

:dp:`fls_8ltVLtAfvy0m`
An :t:`unsafe external block` is an :t:`external block` subject to keyword ``unsafe``.

:dp:`fls_Nz0l16hMxqTd`
The :t:`ABI` of an :t:`external block` is determined as follows:
```

### After chapter excerpt (current)

```rst
src/ffi.rst
* :dp:`fls_JHlqXjn4Sf07`
  ``extern "efiapi"`` - The :t:`ABI` for `UEFI <https://uefi.org/specifications>`_.

:dp:`fls_M4LqHf8hbPA8`
It is undefined behavior when a foreign exception crosses a
:t:`foreign function interface` boundary with an :t:`ABI` that does not end in
``-unwind``.

:dp:`fls_4dje9t5y2dia`
An :dt:`external block` is a :t:`construct` that provides the declarations of
:t:`[external function]s` and :t:`[external static]s` as unchecked imports.

:dp:`fls_8ltVLtAfvy0m`
An :t:`unsafe external block` is an :t:`external block` subject to keyword ``unsafe``.

:dp:`fls_Nz0l16hMxqTd`
The :t:`ABI` of an :t:`external block` is determined as follows:
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## external function (external_function)

### Before glossary entry (origin/main)

```rst
.. _fls_8ffbgzkbsf9r:

external function
^^^^^^^^^^^^^^^^^

:dp:`fls_ngz5fqwrf86e`
An :dt:`external function` is an unchecked import of a foreign :t:`function`.
```

### After glossary entry (generated)

```rst
.. _fls_EgPr77nR1v2a:

external function
^^^^^^^^^^^^^^^^^

:dp:`fls_m55gK20CbEJC`
An :t:`external function` is an unchecked import of a foreign :t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
src/ffi.rst
* :dp:`fls_4XOoiFloXM7t`
  If the :t:`external block` specifies an :s:`AbiKind`, then the :t:`ABI` is the specified :s:`AbiKind`.

* :dp:`fls_PBsepNHImJKH`
  Otherwise the :t:`ABI` is the :t:`extern C ABI`.

:dp:`fls_v24ino4hix3m`
An :t:`external function` is an unchecked import of a foreign :t:`function`.

:dp:`fls_l88r9fj82650`
An :t:`external function` shall be invoked from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.

:dp:`fls_qwchgvvnp0qe`
An :t:`external function` shall not specify a :s:`FunctionQualifierList`.
```

### After chapter excerpt (current)

```rst
src/ffi.rst
* :dp:`fls_4XOoiFloXM7t`
  If the :t:`external block` specifies an :s:`AbiKind`, then the :t:`ABI` is the specified :s:`AbiKind`.

* :dp:`fls_PBsepNHImJKH`
  Otherwise the :t:`ABI` is the :t:`extern C ABI`.

:dp:`fls_v24ino4hix3m`
An :dt:`external function` is an unchecked import of a foreign :t:`function`.

:dp:`fls_l88r9fj82650`
An :t:`external function` shall be invoked from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.

:dp:`fls_qwchgvvnp0qe`
An :t:`external function` shall not specify a :s:`FunctionQualifierList`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## external function item type (external_function_item_type)

### Before glossary entry (origin/main)

```rst
.. _fls_ug2kags0o6is:

external function item type
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_dwlovqly44dj`
An :dt:`external function item type` is a :t:`function item type` where the
related :t:`function` is an :t:`external function`.
```

### After glossary entry (generated)

```rst
.. _fls_TifsqKL1ceDm:

external function item type
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_o7kQWmRRlNiJ`
An :t:`external function item type` is a :t:`function item type` where the
related :t:`function` is an :t:`external function`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_5jh07heok8sy`
A :t:`closure type` implicitly implements the :std:`core::marker::Sync`
:t:`trait` if all the :t:`[type]s` of the :t:`[value]s` of the :t:`capturing
environment` implement the :std:`core::marker::Send` :t:`trait`.

:dp:`fls_t24iojx7yc23`
A :t:`function item type` is a unique anonymous :t:`function type` that
identifies a :t:`function`.

:dp:`fls_sas3ahcshnrh`
An :t:`external function item type` is a :t:`function item type` where the
related :t:`function` is an :t:`external function`.

:dp:`fls_liwnzwu1el1i`
An :t:`unsafe function item type` is a :t:`function item type` where the related
:t:`function` is an :t:`unsafe function`.

:dp:`fls_e9x4f7qxvvjv`
A :t:`function item type` is coercible to a :t:`function pointer type`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_5jh07heok8sy`
A :t:`closure type` implicitly implements the :std:`core::marker::Sync`
:t:`trait` if all the :t:`[type]s` of the :t:`[value]s` of the :t:`capturing
environment` implement the :std:`core::marker::Send` :t:`trait`.

:dp:`fls_t24iojx7yc23`
A :dt:`function item type` is a unique anonymous :t:`function type` that
identifies a :t:`function`.

:dp:`fls_sas3ahcshnrh`
An :dt:`external function item type` is a :t:`function item type` where the
related :t:`function` is an :t:`external function`.

:dp:`fls_liwnzwu1el1i`
An :t:`unsafe function item type` is a :t:`function item type` where the related
:t:`function` is an :t:`unsafe function`.

:dp:`fls_e9x4f7qxvvjv`
A :t:`function item type` is coercible to a :t:`function pointer type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## external static (external_static)

### Before glossary entry (origin/main)

```rst
.. _fls_c89migfc2m6e:

external static
^^^^^^^^^^^^^^^

:dp:`fls_bqq6cncstzeg`
An :dt:`external static` is an import of a foreign :t:`variable`.
```

### After glossary entry (generated)

```rst
.. _fls_3FTpQFPlvj34:

external static
^^^^^^^^^^^^^^^

:dp:`fls_ZByvDfKTh1Eh`
An :t:`external static` is an import of a foreign :t:`variable`.
```

### Before chapter excerpt (origin/main)

```rst
src/ffi.rst
:dp:`fls_9div9yusw64h`
An :t:`external function` shall not specify :t:`[pattern]s` other than
:t:`[identifier pattern]s` and :t:`[underscore pattern]s`.

:dp:`fls_juob30rst11r`
Only the last parameter :s:`FunctionParameter` of an :t:`external function` may
specify a :s:`FunctionParameterVariadicPart`.

:dp:`fls_8ddsytjr4il6`
An :t:`external static` is an import of a foreign :t:`variable`.

:dp:`fls_H0cg9XMaGz0y`
An :t:`external static` inherits the :t:`ABI` of its enclosing
:t:`external block`.

:dp:`fls_fo9with6xumo`
An :t:`external static` shall be referenced from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.
```

### After chapter excerpt (current)

```rst
src/ffi.rst
:dp:`fls_9div9yusw64h`
An :t:`external function` shall not specify :t:`[pattern]s` other than
:t:`[identifier pattern]s` and :t:`[underscore pattern]s`.

:dp:`fls_juob30rst11r`
Only the last parameter :s:`FunctionParameter` of an :t:`external function` may
specify a :s:`FunctionParameterVariadicPart`.

:dp:`fls_8ddsytjr4il6`
An :dt:`external static` is an import of a foreign :t:`variable`.

:dp:`fls_H0cg9XMaGz0y`
An :t:`external static` inherits the :t:`ABI` of its enclosing
:t:`external block`.

:dp:`fls_fo9with6xumo`
An :t:`external static` shall be referenced from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.
