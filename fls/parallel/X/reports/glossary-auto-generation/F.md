# Glossary audit F

## Per-letter checklist
- Letter: F
- [x] Reconcile F terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate F terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for F
- [x] Update `migration-checklist.md` for all F terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint F migration`
- [x] Letter complete

## Term checklist
- [x] f32 (f32)
- [x] f64 (f64)
- [x] fat pointer (fat_pointer)
- [x] fat pointer type (fat_pointer_type)
- [x] FFI (ffi)
- [x] field (field)
- [x] field access expression (field_access_expression)
- [x] field index (field_index)
- [x] field list (field_list)
- [x] field resolution (field_resolution)
- [x] field selector (field_selector)
- [x] final match arm (final_match_arm)
- [x] fixed sized type (fixed_sized_type)
- [x] float literal (float_literal)
- [x] float suffix (float_suffix)
- [x] floating-point type (floating_point_type)
- [x] floating-point type variable (floating_point_type_variable)
- [x] floating-point value (floating_point_value)
- [x] for loop (for_loop)
- [x] for loop expression (for_loop_expression)
- [x] Foreign Function Interface (foreign_function_interface)
- [x] fragment specifier (fragment_specifier)
- [x] full range expression (full_range_expression)
- [x] function (function)
- [x] function body (function_body)
- [x] function item type (function_item_type)
- [x] function lifetime elision (function_lifetime_elision)
- [x] function parameter (function_parameter)
- [x] function pointer type (function_pointer_type)
- [x] function pointer type parameter (function_pointer_type_parameter)
- [x] function qualifier (function_qualifier)
- [x] function signature (function_signature)
- [x] function type (function_type)
- [x] function-like macro (function_like_macro)
- [x] fundamental (fundamental)
- [x] future (future)
- [x] future operand (future_operand)

## f32 (f32)

### Before glossary entry (origin/main)

```rst
.. _fls_4w6garmjhrd9:

f32
^^^

:dp:`fls_4w5rqj7zdemu`
:dc:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_NB5jgWvB0qUm:

f32
^^^

:dp:`fls_cFbbNbScRqSu`
:c:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_vnwbs0exbwcn`
:c:`Char` is a :t:`type` whose :t:`[value]s` are represented as a 32-bit
unsigned word in the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges
of :t:`Unicode`.

:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_30yny2xb9b6b`
:t:`Type` :c:`f32` is equivalent to the IEEE 754-2008 binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:t:`Type` :c:`f64` is equivalent to the IEEE 754-2008 binary64 :t:`type`.

:dp:`fls_nuFAwLHOdQBx`
Operations on values of :t:`[floating point type]s` may not preserve the sign bit in case of the value being a IEEE floating-point ``NaN``.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_xcUkEjuclTjp`
A :dt:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.

:dp:`fls_a5exYaDySck3`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.

:dp:`fls_30yny2xb9b6b`
:dc:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:dc:`f64` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary64 :t:`type`.

:dp:`fls_nuFAwLHOdQBx`
Operations on values of :t:`[floating point type]s` may not preserve the sign bit in case of the value being a IEEE floating-point ``NaN``.
```

### Role classification

dc: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## f64 (f64)

### Before glossary entry (origin/main)

```rst
.. _fls_pj450h99yo28:

f64
^^^

:dp:`fls_ly6p0i6lsibh`
:dc:`f64` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary64 :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_LIgc4CvEd2Dt:

f64
^^^

:dp:`fls_6oGNYTYxB7lh`
:c:`f64` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary64 :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_30yny2xb9b6b`
:t:`Type` :c:`f32` is equivalent to the IEEE 754-2008 binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:t:`Type` :c:`f64` is equivalent to the IEEE 754-2008 binary64 :t:`type`.

:dp:`fls_nuFAwLHOdQBx`
Operations on values of :t:`[floating point type]s` may not preserve the sign bit in case of the value being a IEEE floating-point ``NaN``.

:dp:`fls_cokwseo3nnr`
:t:`[Unsigned integer type]s` define the following inclusive ranges over the
domain of whole numbers:
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_a5exYaDySck3`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.

:dp:`fls_30yny2xb9b6b`
:dc:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:dc:`f64` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary64 :t:`type`.

:dp:`fls_nuFAwLHOdQBx`
Operations on values of :t:`[floating point type]s` may not preserve the sign bit in case of the value being a IEEE floating-point ``NaN``.

:dp:`fls_cokwseo3nnr`
:t:`[Unsigned integer type]s` define the following inclusive ranges over the
domain of whole numbers:
```

### Role classification

dc: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## fat pointer (fat_pointer)

### Before glossary entry (origin/main)

```rst
.. _fls_nkf9z4pqg8x1:

fat pointer
^^^^^^^^^^^

:dp:`fls_knbc2jv5c5ds`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
```

### After glossary entry (generated)

```rst
.. _fls_kqV2r90HxZfB:

fat pointer
^^^^^^^^^^^

:dp:`fls_N3i4mvu5TyLP`
A :t:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_ozYgHEHFTT5c`.
src/types-and-traits.rst
:dp:`fls_kdbq02iguzgl`
All :t:`[value]s` have an :t:`alignment` and a :t:`size`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

:dp:`fls_muxfn9soi47l`
The :t:`alignment` of a :t:`value` specifies which addresses are valid for
storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
address that is a multiple of ``N``.

:dp:`fls_1pbwigq6f3ha`
The :t:`size` of a :t:`type` is the offset in bytes between successive elements
in :t:`array type` ``[T, N]`` where ``T`` is the :t:`type` of the :t:`value`,
including any padding for :t:`alignment`. :t:`Size` is a multiple of the
:t:`alignment`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

:dp:`fls_w1KifBNDp4VE`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.

:dp:`fls_muxfn9soi47l`
The :dt:`alignment` of a :t:`value` specifies which addresses are valid for
storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
address that is a multiple of ``N``.

:dp:`fls_1pbwigq6f3ha`
The :t:`size` of a :t:`type` is the offset in bytes between successive elements
in :t:`array type` ``[T, N]`` where ``T`` is the :t:`type` of the :t:`value`,
including any padding for :t:`alignment`. :t:`Size` is a multiple of the
:t:`alignment`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## fat pointer type (fat_pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_trvkbidlsss8:

fat pointer type
^^^^^^^^^^^^^^^^

:dp:`fls_l8ew6udd79hh`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
```

### After glossary entry (generated)

```rst
.. _fls_kE7O312C49cp:

fat pointer type
^^^^^^^^^^^^^^^^

:dp:`fls_dxT5czMxxnWd`
A :t:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_kdbq02iguzgl`
All :t:`[value]s` have an :t:`alignment` and a :t:`size`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

:dp:`fls_muxfn9soi47l`
The :t:`alignment` of a :t:`value` specifies which addresses are valid for
storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
address that is a multiple of ``N``.

:dp:`fls_1pbwigq6f3ha`
The :t:`size` of a :t:`type` is the offset in bytes between successive elements
in :t:`array type` ``[T, N]`` where ``T`` is the :t:`type` of the :t:`value`,
including any padding for :t:`alignment`. :t:`Size` is a multiple of the
:t:`alignment`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_c6lSeub6RBUV`
A :dt:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

:dp:`fls_w1KifBNDp4VE`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.

:dp:`fls_muxfn9soi47l`
The :dt:`alignment` of a :t:`value` specifies which addresses are valid for
storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
address that is a multiple of ``N``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## FFI (ffi)

### Before glossary entry (origin/main)

```rst
.. _fls_qi21fdknzez6:

FFI
^^^

:dp:`fls_z363fu89mj1c`
For :dt:`FFI`, see :t:`Foreign Function Interface`.
```

### After glossary entry (generated)

```rst
.. _fls_aOt1KdgCBCwd:

FFI
^^^

:dp:`fls_haGaaeJ7w6er`
:t:`FFI` is an abbreviation for :t:`Foreign Function Interface`.
```

### Before chapter excerpt (origin/main)

```rst
src/ffi.rst
:dp:`fls_djlglv2eaihl`
:t:`Foreign Function Interface` or :t:`FFI` employs :t:`ABI`,
:t:`[attribute]s`, :t:`[external block]s`, :t:`[external function]s`, linkage,
and :t:`type` :t:`layout` to interface a Rust program with foreign code.

:dp:`fls_k1hiwghzxtfa`
The following :t:`[attribute]s` affect :t:`FFI`:

* :dp:`fls_3cgtdk4698hm`
  :t:`Attribute` :c:`export_name`.
```

### After chapter excerpt (current)

```rst
src/ffi.rst
:dp:`fls_djlglv2eaihl`
A :dt:`Foreign Function Interface` employs :t:`ABI`, :t:`[attribute]s`,
:t:`[external block]s`, :t:`[external function]s`, linkage, and :t:`type`
:t:`layout` to interface a Rust program with foreign code.

:dp:`fls_JpmkeFXLhQyy`
:dt:`FFI` is an abbreviation for :t:`Foreign Function Interface`.

:dp:`fls_k1hiwghzxtfa`
The following :t:`[attribute]s` affect :t:`FFI`:

* :dp:`fls_3cgtdk4698hm`
  :t:`Attribute` :c:`export_name`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## field (field)

### Before glossary entry (origin/main)

```rst
.. _fls_7gCAbHnGEIl6:

field
^^^^^

:dp:`fls_uAkrgfFTK2YV`
A :dt:`field` is an element of an :t:`abstract data type`.
```

### After glossary entry (generated)

```rst
.. _fls_ZVNPBE8aaxz1:

field
^^^^^

:dp:`fls_WNELHaYnwKaQ`
A :t:`field` is an element of an :t:`abstract data type`.
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
:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.

:dp:`fls_n9HtRM22YEv5`
An :dt:`abstract data type` is a collection of other :t:`[type]s`.

:dp:`fls_74bRiJktNHvk`
A :dt:`field` is an element of an :t:`abstract data type`.

:dp:`fls_9ZleHwO3HlUX`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.

:dp:`fls_gbdd37seqoab`
An :dt:`enum type` is an :t:`abstract data type` that contains
:t:`[enum variant]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## field access expression (field_access_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_yipl7ajrbs6y:

field access expression
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_gdl348a04d15`
A :dt:`field access expression` is an :t:`expression` that accesses a
:t:`field` of a :t:`value`.

:dp:`fls_luetyuwu54d6`
See :s:`FieldAccessExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_F90QfLV0aAyI:

field access expression
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_TEataM5C6gkR`
A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_Gr1ixJ9vFjUm`
The :t:`type` of a :t:`matched argument operand` and the :t:`type` of the
corresponding :t:`function parameter` or :t:`field` shall be :t:`unifiable`.

:dp:`fls_jTMQa6AJSMpE`
The number of :t:`[argument operand]s` shall be equal to the number of
:t:`[field]s` or :t:`[function parameter]s` of the :t:`callee type`.

:dp:`fls_hr8qvwlhd9ts`
A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.

:dp:`fls_s2vpn4ihenpe`
A :t:`container operand` is an :t:`operand` that indicates the :t:`value` whose
:t:`field` is selected in a :t:`field access expression`.

:dp:`fls_yeuayil6uxzx`
A :t:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_Gr1ixJ9vFjUm`
The :t:`type` of a :t:`matched argument operand` and the :t:`type` of the
corresponding :t:`function parameter` or :t:`field` shall be :t:`unifiable`.

:dp:`fls_jTMQa6AJSMpE`
The number of :t:`[argument operand]s` shall be equal to the number of
:t:`[field]s` or :t:`[function parameter]s` of the :t:`callee type`.

:dp:`fls_hr8qvwlhd9ts`
A :dt:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.

:dp:`fls_s2vpn4ihenpe`
A :dt:`container operand` is an :t:`operand` that indicates the :t:`value` whose
:t:`field` is selected in a :t:`field access expression`.

:dp:`fls_yeuayil6uxzx`
A :dt:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## field index (field_index)

### Before glossary entry (origin/main)

```rst
.. _fls_6uwwat9j4x7y:

field index
^^^^^^^^^^^

:dp:`fls_6061r871qgbj`
A :dt:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.

:dp:`fls_IDYKXUIL845x`
See :s:`FieldIndex`.
```

### After glossary entry (generated)

```rst
.. _fls_uB8j6Xytj1sB:

field index
^^^^^^^^^^^

:dp:`fls_jEFI0VYUBa9a`
A :t:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_g1azfj548136`.
src/types-and-traits.rst
:dp:`fls_wqbuof7kxsrg`
It is a static error if the :t:`value` of a :t:`discriminant` exceeds the
maximum :t:`value` of the :t:`type` of the :t:`expression` of a :t:`discriminant
initializer`.

:dp:`fls_f046du2fkgr6`
It is a :t:`validity invariant` for a :t:`value` of an :t:`enum type` to have a
:t:`discriminant` specified by the :t:`enum type`.

:dp:`fls_g1azfj548136`
A :t:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

:dp:`fls_r885av95eivp`
The :t:`name` of a :t:`record struct field` shall be unique within the
related :s:`RecordStructDeclaration`.

:dp:`fls_auurdv1zvzb`
If the :t:`type` of a :t:`record struct field` is a :t:`dynamically sized type`,
then the :t:`record struct field` shall be the last :t:`record struct field` in
the :s:`RecordStructFieldList`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_YERnNZiSdCRn`
A :dt:`field list` is a :s:`RecordStructFieldList` or a
:s:`TupleStructFieldList`.

:dp:`fls_g1azfj548136`
A :t:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

:dp:`fls_3QSa0wGQtbHh`
A :dt:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.

:dp:`fls_r885av95eivp`
The :t:`name` of a :t:`record struct field` shall be unique within the
related :s:`RecordStructDeclaration`.

:dp:`fls_auurdv1zvzb`
If the :t:`type` of a :t:`record struct field` is a :t:`dynamically sized type`,
then the :t:`record struct field` shall be the last :t:`record struct field` in
the :s:`RecordStructFieldList`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## field list (field_list)

### Before glossary entry (origin/main)

```rst
.. _fls_8qLL14WfXXNN:

field list
^^^^^^^^^^

:dp:`fls_xMZsrxMc9Cni`
A :dt:`field list` is a :s:`RecordStructFieldList` or :s:`TupleStructFieldList`.
```

### After glossary entry (generated)

```rst
.. _fls_8zmK6lG5fpzD:

field list
^^^^^^^^^^

:dp:`fls_EKSTwaF2Ta8y`
A :t:`field list` is a :s:`RecordStructFieldList` or a
:s:`TupleStructFieldList`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_f046du2fkgr6`.
src/types-and-traits.rst
:dp:`fls_w9xj26ej869w`
It is a static error if two :t:`[enum variant]s` have :t:`[discriminant]s`
with the same :t:`value`.

:dp:`fls_wqbuof7kxsrg`
It is a static error if the :t:`value` of a :t:`discriminant` exceeds the
maximum :t:`value` of the :t:`type` of the :t:`expression` of a :t:`discriminant
initializer`.

:dp:`fls_f046du2fkgr6`
It is a :t:`validity invariant` for a :t:`value` of an :t:`enum type` to have a
:t:`discriminant` specified by the :t:`enum type`.

:dp:`fls_g1azfj548136`
A :t:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

:dp:`fls_r885av95eivp`
The :t:`name` of a :t:`record struct field` shall be unique within the
related :s:`RecordStructDeclaration`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_wqbuof7kxsrg`
It is a static error if the :t:`value` of a :t:`discriminant` exceeds the
maximum :t:`value` of the :t:`type` of the :t:`expression` of a :t:`discriminant
initializer`.

:dp:`fls_f046du2fkgr6`
It is a :t:`validity invariant` for a :t:`value` of an :t:`enum type` to have a
:t:`discriminant` specified by the :t:`enum type`.

:dp:`fls_YERnNZiSdCRn`
A :dt:`field list` is a :s:`RecordStructFieldList` or a
:s:`TupleStructFieldList`.

:dp:`fls_g1azfj548136`
A :t:`struct type` is an :t:`abstract data type` that is a product of other
:t:`[type]s`.

:dp:`fls_3QSa0wGQtbHh`
A :dt:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## field resolution (field_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_BlZwxp6H62sS:

field resolution
^^^^^^^^^^^^^^^^

:dp:`fls_nL8UuclgxfGL`
:dt:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.
```

### After glossary entry (generated)

```rst
.. _fls_l3vhmdLhcJDD:

Field resolution
^^^^^^^^^^^^^^^^

:dp:`fls_gQ5i1v0G7pOd`
:t:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.

* :dp:`fls_ygam5nisv98c`
  Otherwise the :t:`dereference type chain` continues with :t:`type`
  :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.

:dp:`fls_1nxknwjdp0am`
:t:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.

:dp:`fls_j1bip4w30q8`
A :dt:`candidate container type` is the :t:`type` of the :t:`container operand`
of a :t:`field access expression` :t:`under resolution`.

:dp:`fls_jrk3gzqvqr8e`
A :dt:`candidate container type chain` is a sequence of
:t:`[candidate container type]s`. The :t:`candidate container type chain`
starts with the :t:`type` of the :t:`container operand` of the
:t:`field access expression` :t:`under resolution`. From then on, the
:t:`candidate container type chain` is treated as a
:t:`dereference type chain`.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.

* :dp:`fls_ygam5nisv98c`
  Otherwise the :t:`dereference type chain` continues with :t:`type`
  :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.

:dp:`fls_1nxknwjdp0am`
:dt:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.

:dp:`fls_j1bip4w30q8`
A :dt:`candidate container type` is the :t:`type` of the :t:`container operand`
of a :t:`field access expression` :t:`under resolution`.

:dp:`fls_jrk3gzqvqr8e`
A :dt:`candidate container type chain` is a sequence of
:t:`[candidate container type]s`. The :t:`candidate container type chain`
starts with the :t:`type` of the :t:`container operand` of the
:t:`field access expression` :t:`under resolution`. From then on, the
:t:`candidate container type chain` is treated as a
:t:`dereference type chain`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## field selector (field_selector)

### Before glossary entry (origin/main)

```rst
.. _fls_kqbata8slp1y:

field selector
^^^^^^^^^^^^^^

:dp:`fls_aq1yg9cp1uof`
A :dt:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.

:dp:`fls_x8swot8e1j32`
See :s:`FieldSelector`.
```

### After glossary entry (generated)

```rst
.. _fls_bGhvuhuYJwYx:

field selector
^^^^^^^^^^^^^^

:dp:`fls_RgZKjdSaWC6n`
A :t:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_hr8qvwlhd9ts`
A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.

:dp:`fls_s2vpn4ihenpe`
A :t:`container operand` is an :t:`operand` that indicates the :t:`value` whose
:t:`field` is selected in a :t:`field access expression`.

:dp:`fls_yeuayil6uxzx`
A :t:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.

:dp:`fls_qqrconpa92i3`
A :t:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

:dp:`fls_fovs9il2h9xg`
The :t:`type` of a :t:`field access expression` is the :t:`type` of the
:t:`selected field`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_hr8qvwlhd9ts`
A :dt:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.

:dp:`fls_s2vpn4ihenpe`
A :dt:`container operand` is an :t:`operand` that indicates the :t:`value` whose
:t:`field` is selected in a :t:`field access expression`.

:dp:`fls_yeuayil6uxzx`
A :dt:`field selector` is a :t:`construct` that selects the :t:`field` to be
accessed in a :t:`field access expression`.

:dp:`fls_qqrconpa92i3`
A :t:`selected field` is a :t:`field` that is selected by a
:t:`field access expression`.

:dp:`fls_fovs9il2h9xg`
The :t:`type` of a :t:`field access expression` is the :t:`type` of the
:t:`selected field`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## final match arm (final_match_arm)

### Before glossary entry (origin/main)

```rst
.. _fls_mj9mmkar8c6f:

final match arm
^^^^^^^^^^^^^^^

:dp:`fls_btoz8jioisx9`
A :dt:`final match arm` is the last :t:`match arm` of a :t:`match expression`.

:dp:`fls_v7ockjwbeel1`
See :s:`FinalMatchArm`.
```

### After glossary entry (generated)

```rst
.. _fls_2EkPDO7hAMas:

final match arm
^^^^^^^^^^^^^^^

:dp:`fls_AHTeXVaj4PsJ`
A :t:`final match arm` is the last :t:`match arm` of a :t:`match expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_l45i24ikfavm`
A :t:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

:dp:`fls_d9gerg12hm2d`
An :t:`intermediate match arm` is any :t:`non-[final match arm]` of a
:t:`match expression`.

:dp:`fls_oj8dg28xw5yp`
A :t:`final match arm` is the last :t:`match arm` of a :t:`match expression`.

:dp:`fls_lrdrtedyz28i`
A :t:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern` and
a :t:`match arm guard`.

:dp:`fls_zJQ4LecT1HYd`
The :t:`expected type` of the :t:`pattern` of the :t:`match arm matcher` is the :t:`type` of the :t:`subject expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_l45i24ikfavm`
A :t:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

:dp:`fls_d9gerg12hm2d`
An :t:`intermediate match arm` is any :t:`non-[final match arm]` of a
:t:`match expression`.

:dp:`fls_oj8dg28xw5yp`
A :dt:`final match arm` is the last :t:`match arm` of a :t:`match expression`.

:dp:`fls_lrdrtedyz28i`
A :t:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern` and
a :t:`match arm guard`.

:dp:`fls_zJQ4LecT1HYd`
The :t:`expected type` of the :t:`pattern` of the :t:`match arm matcher` is the :t:`type` of the :t:`subject expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## fixed sized type (fixed_sized_type)

### Before glossary entry (origin/main)

```rst
.. _fls_rljxa45tleq3:

fixed sized type
^^^^^^^^^^^^^^^^

:dp:`fls_eadiywl20jo4`
A :dt:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.
```

### After glossary entry (generated)

```rst
.. _fls_Vg4UE7EYsdQC:

fixed sized type
^^^^^^^^^^^^^^^^

:dp:`fls_WCaRnM6JJBLI`
A :t:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_kdbq02iguzgl`.
src/types-and-traits.rst
:dp:`fls_rosdkeck5ax2`
A :t:`type alias` shall not have a :s:`TypeBoundList` unless it is an
:t:`associated item`.

:dp:`fls_drxl7u3etfp9`
The last :t:`where clause` is rejected, but may still be consumed by
:t:`[macro]s`.

:dp:`fls_kdbq02iguzgl`
All :t:`[value]s` have an :t:`alignment` and a :t:`size`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_drxl7u3etfp9`
The last :t:`where clause` is rejected, but may still be consumed by
:t:`[macro]s`.

:dp:`fls_kdbq02iguzgl`
All :t:`[value]s` have an :t:`alignment` and a :t:`size`.

:dp:`fls_c6lSeub6RBUV`
A :dt:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## float literal (float_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_achdyw3nbme3:

float literal
^^^^^^^^^^^^^

:dp:`fls_53o8dio9vpjh`
A :dt:`float literal` is a :t:`numeric literal` that denotes a fractional
number.

:dp:`fls_hqeaakhsqxok`
See :s:`FloatLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_iTtZR85kwpdq:

float literal
^^^^^^^^^^^^^

:dp:`fls_GXlf4cIP11Zg`
A :t:`float literal` is a :t:`numeric literal` that denotes a fractional number.
```

### Before chapter excerpt (origin/main)

```rst
src/lexical-elements.rst
* :dp:`fls_qqrqyc6uhol`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`i32`.

* :dp:`fls_pexi5jazthq6`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_rzi7oeqokd6e`
A :t:`float literal` is a :t:`numeric literal` that denotes a fractional number.

:dp:`fls_2ru1zyrykd37`
A :t:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.

:dp:`fls_21mhnhplzam7`
A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.
```

### After chapter excerpt (current)

```rst
src/lexical-elements.rst
* :dp:`fls_qqrqyc6uhol`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`i32`.

* :dp:`fls_pexi5jazthq6`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_rzi7oeqokd6e`
A :dt:`float literal` is a :t:`numeric literal` that denotes a fractional number.

:dp:`fls_2ru1zyrykd37`
A :dt:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.

:dp:`fls_21mhnhplzam7`
A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## float suffix (float_suffix)

### Before glossary entry (origin/main)

```rst
.. _fls_wgylj1n4wrqe:

float suffix
^^^^^^^^^^^^

:dp:`fls_vka2z7frq9j8`
A :dt:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.

:dp:`fls_2k1ddqhsgxqk`
See :s:`FloatSuffix`.
```

### After glossary entry (generated)

```rst
.. _fls_SJSSli5CnhM0:

float suffix
^^^^^^^^^^^^

:dp:`fls_RFEyYkz2298e`
A :t:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.
```

### Before chapter excerpt (origin/main)

```rst
src/lexical-elements.rst
* :dp:`fls_pexi5jazthq6`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_rzi7oeqokd6e`
A :t:`float literal` is a :t:`numeric literal` that denotes a fractional number.

:dp:`fls_2ru1zyrykd37`
A :t:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.

:dp:`fls_21mhnhplzam7`
A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

:dp:`fls_drqh80k0sfkb`
An :t:`unsuffixed float` is a :t:`float literal` without a :t:`float suffix`.
```

### After chapter excerpt (current)

```rst
src/lexical-elements.rst
* :dp:`fls_pexi5jazthq6`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

:dp:`fls_rzi7oeqokd6e`
A :dt:`float literal` is a :t:`numeric literal` that denotes a fractional number.

:dp:`fls_2ru1zyrykd37`
A :dt:`float suffix` is a component of a :t:`float literal` that specifies an
explicit :t:`floating-point type`.

:dp:`fls_21mhnhplzam7`
A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

:dp:`fls_drqh80k0sfkb`
An :t:`unsuffixed float` is a :t:`float literal` without a :t:`float suffix`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## floating-point type (floating_point_type)

### Before glossary entry (origin/main)

```rst
.. _fls_k32g8cd9friu:

floating-point type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_1w5yjiffah1u`
A :dt:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.
```

### After glossary entry (generated)

```rst
.. _fls_cSn1u8tiuTyr:

floating-point type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_kyrLZFRvkacu`
A :t:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_juysxea25owj`.
src/types-and-traits.rst
:dp:`fls_2sd39mj05mb9`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`bool` to have
a bit pattern of ``0x00`` and ``0x01``.

:dp:`fls_vnwbs0exbwcn`
:c:`Char` is a :t:`type` whose :t:`[value]s` are represented as a 32-bit
unsigned word in the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges
of :t:`Unicode`.

:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_30yny2xb9b6b`
:t:`Type` :c:`f32` is equivalent to the IEEE 754-2008 binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:t:`Type` :c:`f64` is equivalent to the IEEE 754-2008 binary64 :t:`type`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_vnwbs0exbwcn`
A :dt:`char` is a :t:`type` whose :t:`[value]s` are represented as a 32-bit
unsigned word in the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges
of :t:`Unicode`.

:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_xcUkEjuclTjp`
A :dt:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.

:dp:`fls_a5exYaDySck3`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.

:dp:`fls_30yny2xb9b6b`
:dc:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## floating-point type variable (floating_point_type_variable)

### Before glossary entry (origin/main)

```rst
.. _fls_8ih3gh6hoy78:

floating-point type variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ls41emhkrxdi`
A :dt:`floating-point type variable` is a :t:`type variable` that can refer
only to :t:`[floating-point type]s`.
```

### After glossary entry (generated)

```rst
.. _fls_K7aO0SvS1gqP:

floating-point type variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_SzwQJDyK0n8N`
A :t:`floating-point type variable` is a :t:`type variable` that can refer only
to :t:`[floating-point type]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_gDalJm1XS0mi`
A :t:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.

:dp:`fls_7ov36fpd9mwe`
An :t:`integer type variable` is a :t:`type variable` that can refer only to
:t:`[integer type]s`.

:dp:`fls_3hv3wxkhjjp1`
A :t:`floating-point type variable` is a :t:`type variable` that can refer only
to :t:`[floating-point type]s`.

:dp:`fls_bXQ63GYYDuMp`
A :t:`diverging type variable` is a :t:`type variable` that can refer to any
:t:`type` and originates from a :t:`diverging expression`.

:dp:`fls_JryXiKBIFvF3`
A :dt:`lifetime variable` is a placeholder used during :t:`type inference` to
stand in for an undetermined :t:`lifetime` of a :t:`type`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_gDalJm1XS0mi`
A :t:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.

:dp:`fls_7ov36fpd9mwe`
An :t:`integer type variable` is a :t:`type variable` that can refer only to
:t:`[integer type]s`.

:dp:`fls_3hv3wxkhjjp1`
A :dt:`floating-point type variable` is a :t:`type variable` that can refer only
to :t:`[floating-point type]s`.

:dp:`fls_bXQ63GYYDuMp`
A :dt:`diverging type variable` is a :t:`type variable` that can refer to any
:t:`type` and originates from a :t:`diverging expression`.

:dp:`fls_JryXiKBIFvF3`
A :dt:`lifetime variable` is a placeholder used during :t:`type inference` to
stand in for an undetermined :t:`lifetime` of a :t:`type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## floating-point value (floating_point_value)

### Before glossary entry (origin/main)

```rst
.. _fls_nE6SWuVH7X68:

floating-point value
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_rx8cvWPlvel5`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.
```

### After glossary entry (generated)

```rst
.. _fls_KgGjbsHntJV9:

floating-point value
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_SVbWErcybuzw`
A :t:`floating-point value` is a :t:`value` of a :t:`floating-point type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_juysxea25owj`.
src/types-and-traits.rst
:dp:`fls_2sd39mj05mb9`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`bool` to have
a bit pattern of ``0x00`` and ``0x01``.

:dp:`fls_vnwbs0exbwcn`
:c:`Char` is a :t:`type` whose :t:`[value]s` are represented as a 32-bit
unsigned word in the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges
of :t:`Unicode`.

:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_30yny2xb9b6b`
:t:`Type` :c:`f32` is equivalent to the IEEE 754-2008 binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:t:`Type` :c:`f64` is equivalent to the IEEE 754-2008 binary64 :t:`type`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_juysxea25owj`
It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
:t:`Unicode`.

:dp:`fls_xcUkEjuclTjp`
A :dt:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.

:dp:`fls_a5exYaDySck3`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.

:dp:`fls_30yny2xb9b6b`
:dc:`f32` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary32 :t:`type`.

:dp:`fls_yqflrq9s6p6n`
:dc:`f64` is a :t:`floating-point type` equivalent to the IEEE 754-2008
binary64 :t:`type`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## for loop (for_loop)

### Before glossary entry (origin/main)

```rst
.. _fls_dwnvkq8n94h1:

for loop
^^^^^^^^

:dp:`fls_gmhh56arsbw8`
For :dt:`for loop`, see :t:`for loop expression`.
```

### After glossary entry (generated)

```rst
.. _fls_A0W0M0Jo4kq7:

for loop
^^^^^^^^

:dp:`fls_1L0vG35K9N1C`
For :t:`for loop`, see :t:`for loop expression`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_aw6qczl4zpko`.
src/expressions.rst
:dp:`fls_eg93m93gvwal`
An :t:`anonymous loop expression` is a :t:`loop expression` without a
:t:`label`.

:dp:`fls_phpoq9ho8f1v`
A :t:`named loop expression` is a :t:`loop expression` with a :t:`label`.

:dp:`fls_aw6qczl4zpko`
A :t:`loop expression` is :t:`terminated` when its :t:`block expression` is no
longer evaluated.

:dp:`fls_1bh2alh37frz`
A :t:`for loop expression` is a :t:`loop expression` that continues to evaluate
its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.

:dp:`fls_fkgbin6ydkm4`
The :t:`type` of a :t:`subject expression` shall implement the
:std:`core::iter::IntoIterator` :t:`trait`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_phpoq9ho8f1v`
A :t:`named loop expression` is a :t:`loop expression` with a :t:`label`.

:dp:`fls_aw6qczl4zpko`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

:dp:`fls_RPflON3LZDnO`
For :dt:`for loop`, see :t:`for loop expression`.

:dp:`fls_1bh2alh37frz`
A :dt:`for loop expression` is a :t:`loop expression` that continues to evaluate
its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.

:dp:`fls_fkgbin6ydkm4`
The :t:`type` of a :t:`subject expression` shall implement the
:std:`core::iter::IntoIterator` :t:`trait`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## for loop expression (for_loop_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_vfkqbovqbw86:

for loop expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_f0gp7qxoc4o4`
A :dt:`for loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject expression` yields a
:t:`value`.

:dp:`fls_yn4d35pvmn87`
See :s:`ForLoopExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_4iWpUkbACvQj:

for loop expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_Vlhb5uyp5u5M`
A :t:`for loop expression` is a :t:`loop expression` that continues to evaluate
its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_phpoq9ho8f1v`
A :t:`named loop expression` is a :t:`loop expression` with a :t:`label`.

:dp:`fls_aw6qczl4zpko`
A :t:`loop expression` is :t:`terminated` when its :t:`block expression` is no
longer evaluated.

:dp:`fls_1bh2alh37frz`
A :t:`for loop expression` is a :t:`loop expression` that continues to evaluate
its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.

:dp:`fls_fkgbin6ydkm4`
The :t:`type` of a :t:`subject expression` shall implement the
:std:`core::iter::IntoIterator` :t:`trait`.

:dp:`fls_fo6Aa6Td6rMA`
The :t:`expected type` of the :t:`pattern` is the :t:`associated type` :std:`core::iter::IntoIterator::Item` of the :t:`subject expression`'s :std:`core::iter::IntoIterator` implementation.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_aw6qczl4zpko`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

:dp:`fls_RPflON3LZDnO`
For :dt:`for loop`, see :t:`for loop expression`.

:dp:`fls_1bh2alh37frz`
A :dt:`for loop expression` is a :t:`loop expression` that continues to evaluate
its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.

:dp:`fls_fkgbin6ydkm4`
The :t:`type` of a :t:`subject expression` shall implement the
:std:`core::iter::IntoIterator` :t:`trait`.

:dp:`fls_fo6Aa6Td6rMA`
The :t:`expected type` of the :t:`pattern` is the :t:`associated type` :std:`core::iter::IntoIterator::Item` of the :t:`subject expression`'s :std:`core::iter::IntoIterator` implementation.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## Foreign Function Interface (foreign_function_interface)

### Before glossary entry (origin/main)

```rst
.. _fls_fo7vyxs4l3yh:

Foreign Function Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_240yj1kym1kh`
:dt:`Foreign Function Interface` employs :t:`ABI`, :t:`[attribute]s`,
:t:`external block`, :t:`[external function]s`, linkage, and :t:`type`
:t:`layout` to interface a Rust program with foreign code.
```

### After glossary entry (generated)

```rst
.. _fls_CNLDjP7iISn7:

Foreign Function Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_kazSoDDUbfiM`
A :t:`Foreign Function Interface` employs :t:`ABI`, :t:`[attribute]s`,
:t:`[external block]s`, :t:`[external function]s`, linkage, and :t:`type`
:t:`layout` to interface a Rust program with foreign code.
```

### Before chapter excerpt (origin/main)

```rst
src/ffi.rst
:dp:`fls_djlglv2eaihl`
:t:`Foreign Function Interface` or :t:`FFI` employs :t:`ABI`,
:t:`[attribute]s`, :t:`[external block]s`, :t:`[external function]s`, linkage,
and :t:`type` :t:`layout` to interface a Rust program with foreign code.

:dp:`fls_k1hiwghzxtfa`
The following :t:`[attribute]s` affect :t:`FFI`:

* :dp:`fls_3cgtdk4698hm`
  :t:`Attribute` :c:`export_name`.
```

### After chapter excerpt (current)

```rst
src/ffi.rst
:dp:`fls_djlglv2eaihl`
A :dt:`Foreign Function Interface` employs :t:`ABI`, :t:`[attribute]s`,
:t:`[external block]s`, :t:`[external function]s`, linkage, and :t:`type`
:t:`layout` to interface a Rust program with foreign code.

:dp:`fls_JpmkeFXLhQyy`
:dt:`FFI` is an abbreviation for :t:`Foreign Function Interface`.

:dp:`fls_k1hiwghzxtfa`
The following :t:`[attribute]s` affect :t:`FFI`:

* :dp:`fls_3cgtdk4698hm`
  :t:`Attribute` :c:`export_name`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## fragment specifier (fragment_specifier)

### Before glossary entry (origin/main)

```rst
.. _fls_pi7j0t7h1y86:

fragment specifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_6lhwep7ulpr0`
A :dt:`fragment specifier` is a :t:`construct` that indicates the :t:`type` of
a :t:`metavariable`.

:dp:`fls_drfn9yqrihgx`
See ``MacroFragmentSpecifier``.
```

### After glossary entry (generated)

```rst
.. _fls_tbP1Z2l9mazx:

fragment specifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_rEESjlLD0ULj`
A :t:`fragment specifier` is a :t:`construct` that indicates the :t:`type` of
a :t:`metavariable`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_4zdait30exvn`
A :t:`metavariable` is a :t:`macro match` that describes a :t:`variable`.

:dp:`fls_2HguXbL7DjKH`
A :t:`metavariable` is visible in the :t:`macro transcriber` of the
:t:`macro rule` of the :t:`macro matcher` it is declared in.

:dp:`fls_8zypylq60zba`
A :t:`fragment specifier` is a :t:`construct` that indicates the :t:`type` of
a :t:`metavariable`.

:dp:`fls_8o9mcV2KrKac`
:t:`Fragment specifier` kinds impose the following
:dt:`[fragment specifier restriction]s` on the :t:`[token]s` that follow them:

* :dp:`fls_PxR9vNHsaFnI`
  ``expr`` and ``expr_2021`` shall only be followed by ``=>``, ``,``, or ``;``.
```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_4zdait30exvn`
A :t:`metavariable` is a :t:`macro match` that describes a :t:`variable`.

:dp:`fls_2HguXbL7DjKH`
A :t:`metavariable` is visible in the :t:`macro transcriber` of the
:t:`macro rule` of the :t:`macro matcher` it is declared in.

:dp:`fls_8zypylq60zba`
A :dt:`fragment specifier` is a :t:`construct` that indicates the :t:`type` of
a :t:`metavariable`.

:dp:`fls_8o9mcV2KrKac`
:t:`Fragment specifier` kinds impose the following
:dt:`[fragment specifier restriction]s` on the :t:`[token]s` that follow them:

* :dp:`fls_PxR9vNHsaFnI`
  ``expr`` and ``expr_2021`` shall only be followed by ``=>``, ``,``, or ``;``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## full range expression (full_range_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_tWp1PLe8m83K:

full range expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NIb9UOIRjMqa`
A :dt:`full range expression` is a :t:`range expression` that covers the full
range of a :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_LtJ8IZs2QG9G:

full range expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_cxgTUJygiLl8`
A :t:`full range expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_ke2fpgodq84u`
The :t:`type` of a :t:`range-from-to expression` is :std:`core::ops::Range`.

:dp:`fls_zb6jk6qykun6`
The :t:`value` of a :t:`range-from-to expression` is
``core::ops::Range { start: range_expression_low_bound, end: range_expression_high_bound }``.

:dp:`fls_x67xo25n0qlz`
A :t:`range-full expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.

:dp:`fls_m6n0gvg3ct1b`
The :t:`type` of a :t:`range-full expression` is :std:`core::ops::RangeFull`.

:dp:`fls_yvh5cdgzevni`
The :t:`value` of a :t:`range-full expression` is ``core::ops::RangeFull {}``.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_ke2fpgodq84u`
The :t:`type` of a :t:`range-from-to expression` is :std:`core::ops::Range`.

:dp:`fls_zb6jk6qykun6`
The :t:`value` of a :t:`range-from-to expression` is
``core::ops::Range { start: range_expression_low_bound, end: range_expression_high_bound }``.

:dp:`fls_x67xo25n0qlz`
A :dt:`full range expression` is a :t:`range expression` that covers the whole
range of a :t:`type`.

:dp:`fls_m6n0gvg3ct1b`
The :t:`type` of a :t:`full range expression` is :std:`core::ops::RangeFull`.

:dp:`fls_yvh5cdgzevni`
The :t:`value` of a :t:`full range expression` is ``core::ops::RangeFull {}``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function (function)

### Before glossary entry (origin/main)

```rst
.. _fls_yllg093syzdi:

function
^^^^^^^^

:dp:`fls_ni14pcm4ap9l`
A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.

:dp:`fls_hn01vvw2fx9m`
See :s:`FunctionDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_OZIr0DdzPIkJ:

function
^^^^^^^^

:dp:`fls_1mIouS9FT93o`
A :t:`function` is a :t:`value` of a :t:`function type` that models a behavior.
```

### Before chapter excerpt (origin/main)

```rst
src/functions.rst
:dp:`fls_gn1ngtx2tp2s`
A :t:`function` is a :t:`value` of a :t:`function type` that models a behavior.

:dp:`fls_bdx9gnnjxru3`
A :t:`function` declares a unique :t:`function item type` for itself.

:dp:`fls_87jnkimc15gi`
A :t:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.
```

### After chapter excerpt (current)

```rst
src/functions.rst
:dp:`fls_gn1ngtx2tp2s`
A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.

:dp:`fls_bdx9gnnjxru3`
A :t:`function` declares a unique :t:`function item type` for itself.

:dp:`fls_87jnkimc15gi`
A :dt:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function body (function_body)

### Before glossary entry (origin/main)

```rst
.. _fls_vjgkg8kfi93:

function body
^^^^^^^^^^^^^

:dp:`fls_y5ha4123alik`
A :dt:`function body` is the :t:`block expression` of a :t:`function`.

:dp:`fls_r0g0i730x6x4`
See :s:`FunctionBody`.
```

### After glossary entry (generated)

```rst
.. _fls_PnXFizKDuhHU:

function body
^^^^^^^^^^^^^

:dp:`fls_7VKiBF2QlzTX`
A :t:`function body` is the :t:`block expression` of a :t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
src/functions.rst
* :dp:`fls_C7dvzcXcpQCy`
  If the :s:`FunctionDeclaration` specifies a :s:`ReturnType`, then the :t:`return type` is the specified :s:`ReturnType`.

* :dp:`fls_J8X8ahnJLrMo`
  Otherwise the :t:`return type` is the :t:`unit type`.

:dp:`fls_927nfm5mkbsp`
A :t:`function body` is the :t:`block expression` of a :t:`function`.

:dp:`fls_yfm0jh62oaxr`
A :t:`function` shall have a :t:`function body` unless it is an
:t:`associated trait function` or an :t:`external function`.

:dp:`fls_bHwy8FLzEUi3`
A :t:`function body` denotes a :t:`control flow boundary`.
```

### After chapter excerpt (current)

```rst
src/functions.rst
* :dp:`fls_C7dvzcXcpQCy`
  If the :s:`FunctionDeclaration` specifies a :s:`ReturnType`, then the :t:`return type` is the specified :s:`ReturnType`.

* :dp:`fls_J8X8ahnJLrMo`
  Otherwise the :t:`return type` is the :t:`unit type`.

:dp:`fls_927nfm5mkbsp`
A :dt:`function body` is the :t:`block expression` of a :t:`function`.

:dp:`fls_yfm0jh62oaxr`
A :t:`function` shall have a :t:`function body` unless it is an
:t:`associated trait function` or an :t:`external function`.

:dp:`fls_bHwy8FLzEUi3`
A :t:`function body` denotes a :t:`control flow boundary`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function item type (function_item_type)

### Before glossary entry (origin/main)

```rst
.. _fls_ayuia853po0a:

function item type
^^^^^^^^^^^^^^^^^^

:dp:`fls_rfvfo8x42dh8`
A :dt:`function item type` is a unique anonymous :t:`function type` that
identifies a :t:`function`.
```

### After glossary entry (generated)

```rst
.. _fls_88gcnYlJ1gkv:

function item type
^^^^^^^^^^^^^^^^^^

:dp:`fls_7SKB4LCJumeH`
A :t:`function item type` is a unique anonymous :t:`function type` that
identifies a :t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_2nuhy0ujgq18`
A :t:`closure type` implicitly implements the :std:`core::marker::Send`
:t:`trait` if all the :t:`[type]s` of the :t:`[value]s` of the
:t:`capturing environment` implement the :std:`core::marker::Send` :t:`trait`.

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
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_2nuhy0ujgq18`
A :t:`closure type` implicitly implements the :std:`core::marker::Send`
:t:`trait` if all the :t:`[type]s` of the :t:`[value]s` of the
:t:`capturing environment` implement the :std:`core::marker::Send` :t:`trait`.

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
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function lifetime elision (function_lifetime_elision)

### Before glossary entry (origin/main)

```rst
.. _fls_WMaE58yv1joW:

function lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tZMmRHua1S8K`
:dt:`Function lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[function]s`, :t:`[function pointer type parameter]s` and :t:`[path]s`
resolving to one of the :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and
:std:`core::ops::FnOnce` :t:`[trait]s`.
```

### After glossary entry (generated)

```rst
.. _fls_fAX5XPRKHjpn:

Function lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tb6DUOqIpwCv`
:t:`Function lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[function]s`, :t:`[function pointer type parameter]s`, and :t:`[path]s`
that resolve to one of the :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and
:std:`core::ops::FnOnce` :t:`[trait]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_cD0ZYi23VqWg`
It is a static error to elide a :t:`lifetime` in a position where no
:t:`lifetime elision` rules are active.

:dp:`fls_sA4Lqc5o6cX3`
:t:`[Lifetime]s` cannot be implicitly elided within :t:`[impl trait type]s`.
If no :t:`lifetime bound` is present, the :t:`impl trait type` is not considered
to be bound by any :t:`lifetime`.

:dp:`fls_lAdIRCFFlydD`
:t:`Function lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[function]s`, :t:`[function pointer type parameter]s`, and :t:`[path]s`
that resolve to one of the :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and
:std:`core::ops::FnOnce` :t:`[trait]s`.

:dp:`fls_dpudys82dhdc`
An :dt:`input lifetime` is one of the following :t:`[lifetime]s`:

* :dp:`fls_pjil71kk0r25`
  Any :t:`lifetime` related to a :t:`function parameter`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_cD0ZYi23VqWg`
It is a static error to elide a :t:`lifetime` in a position where no
:t:`lifetime elision` rules are active.

:dp:`fls_sA4Lqc5o6cX3`
:t:`[Lifetime]s` cannot be implicitly elided within :t:`[impl trait type]s`.
If no :t:`lifetime bound` is present, the :t:`impl trait type` is not considered
to be bound by any :t:`lifetime`.

:dp:`fls_lAdIRCFFlydD`
:dt:`Function lifetime elision` is a form of :t:`lifetime elision` that applies
to :t:`[function]s`, :t:`[function pointer type parameter]s`, and :t:`[path]s`
that resolve to one of the :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and
:std:`core::ops::FnOnce` :t:`[trait]s`.

:dp:`fls_dpudys82dhdc`
An :dt:`input lifetime` is one of the following :t:`[lifetime]s`:

* :dp:`fls_pjil71kk0r25`
  Any :t:`lifetime` related to a :t:`function parameter`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function parameter (function_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_xn800gcjnln1:

function parameter
^^^^^^^^^^^^^^^^^^

:dp:`fls_2feq1ky9pla1`
A :dt:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.

:dp:`fls_4tf20svi3rjx`
See :s:`FunctionParameter`.
```

### After glossary entry (generated)

```rst
.. _fls_AfoMHqfx40pf:

function parameter
^^^^^^^^^^^^^^^^^^

:dp:`fls_zdzpGHhLVUjT`
A :t:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/functions.rst
:dp:`fls_87jnkimc15gi`
A :t:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.

:dp:`fls_nwywh1vjt6rr`
A :t:`function` shall not be subject to both :t:`keyword` ``async`` and
:t:`keyword` ``const``.

:dp:`fls_uwuthzfgslif`
A :t:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.

:dp:`fls_ymeo93t4mz4`
A :t:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

:dp:`fls_ijbt4tgnl95n`
A :t:`function` shall not specify a :t:`self parameter` unless it is an
:t:`associated function`.
```

### After chapter excerpt (current)

```rst
src/functions.rst
:dp:`fls_87jnkimc15gi`
A :dt:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.

:dp:`fls_nwywh1vjt6rr`
A :t:`function` shall not be subject to both :t:`keyword` ``async`` and
:t:`keyword` ``const``.

:dp:`fls_uwuthzfgslif`
A :dt:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.

:dp:`fls_ymeo93t4mz4`
A :t:`self parameter` is a :t:`function parameter` expressed by :t:`keyword`
``self``.

:dp:`fls_ijbt4tgnl95n`
A :t:`function` shall not specify a :t:`self parameter` unless it is an
:t:`associated function`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function pointer type (function_pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_fqwzlg78k503:

function pointer type
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_lcawg25xhblx`
A :dt:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.

:dp:`fls_t50umpk5abjy`
See :s:`FunctionPointerTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_ypF5Ofkg1x3n:

function pointer type
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_UD4nEcoL8Qqf`
A :t:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_e9x4f7qxvvjv`
A :t:`function item type` is coercible to a :t:`function pointer type`.

:dp:`fls_1941wid94hlg`
A :t:`function item type` implements the :std:`core::clone::Clone` :t:`trait`,
the :std:`core::marker::Copy` :t:`trait`, the :std:`core::ops::Fn` :t:`trait`,
the :std:`core::ops::FnMut` :t:`trait`, the :std:`core::ops::FnOnce` :t:`trait`,
the :std:`core::marker::Send` :t:`trait`, and the :std:`core::marker::Sync`
:t:`trait`.

:dp:`fls_v2wrytr3t04h`
A :t:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.

:dp:`fls_5dd7icjcl3nt`
An :t:`unsafe function pointer type` is a function pointer type subject to
:t:`keyword` ``unsafe``.

:dp:`fls_B0SMXRqQMS1E`
A :t:`variadic part` indicates the presence of :t:`C`-like optional
parameters.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_e9x4f7qxvvjv`
A :t:`function item type` is coercible to a :t:`function pointer type`.

:dp:`fls_1941wid94hlg`
A :t:`function item type` implements the :std:`core::clone::Clone` :t:`trait`,
the :std:`core::marker::Copy` :t:`trait`, the :std:`core::ops::Fn` :t:`trait`,
the :std:`core::ops::FnMut` :t:`trait`, the :std:`core::ops::FnOnce` :t:`trait`,
the :std:`core::marker::Send` :t:`trait`, and the :std:`core::marker::Sync`
:t:`trait`.

:dp:`fls_v2wrytr3t04h`
A :dt:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.

:dp:`fls_aXhHQFNr7kaf`
A :dt:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.

:dp:`fls_5dd7icjcl3nt`
An :t:`unsafe function pointer type` is a function pointer type subject to
:t:`keyword` ``unsafe``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function pointer type parameter (function_pointer_type_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_v3V6K4S5UhIF:

function pointer type parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_nF1k90JJWq2K`
A :dt:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.

:dp:`fls_vvy6qogy0xnb`
See :s:`FunctionPointerTypeParameter`.
```

### After glossary entry (generated)

```rst
.. _fls_f2LvcvrqIwLU:

function pointer type parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8o1Eka7XdxnY`
A :t:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_v2wrytr3t04h`.
src/types-and-traits.rst
:dp:`fls_e9x4f7qxvvjv`
A :t:`function item type` is coercible to a :t:`function pointer type`.

:dp:`fls_1941wid94hlg`
A :t:`function item type` implements the :std:`core::clone::Clone` :t:`trait`,
the :std:`core::marker::Copy` :t:`trait`, the :std:`core::ops::Fn` :t:`trait`,
the :std:`core::ops::FnMut` :t:`trait`, the :std:`core::ops::FnOnce` :t:`trait`,
the :std:`core::marker::Send` :t:`trait`, and the :std:`core::marker::Sync`
:t:`trait`.

:dp:`fls_v2wrytr3t04h`
A :t:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.

:dp:`fls_5dd7icjcl3nt`
An :t:`unsafe function pointer type` is a function pointer type subject to
:t:`keyword` ``unsafe``.

:dp:`fls_B0SMXRqQMS1E`
A :t:`variadic part` indicates the presence of :t:`C`-like optional
parameters.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_1941wid94hlg`
A :t:`function item type` implements the :std:`core::clone::Clone` :t:`trait`,
the :std:`core::marker::Copy` :t:`trait`, the :std:`core::ops::Fn` :t:`trait`,
the :std:`core::ops::FnMut` :t:`trait`, the :std:`core::ops::FnOnce` :t:`trait`,
the :std:`core::marker::Send` :t:`trait`, and the :std:`core::marker::Sync`
:t:`trait`.

:dp:`fls_v2wrytr3t04h`
A :dt:`function pointer type` is an :t:`indirection type` that refers to a
:t:`function`.

:dp:`fls_aXhHQFNr7kaf`
A :dt:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.

:dp:`fls_5dd7icjcl3nt`
An :t:`unsafe function pointer type` is a function pointer type subject to
:t:`keyword` ``unsafe``.

:dp:`fls_B0SMXRqQMS1E`
A :t:`variadic part` indicates the presence of :t:`C`-like optional
parameters.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## function qualifier (function_qualifier)

### Before glossary entry (origin/main)

```rst
.. _fls_2uvom1x42dcs:

function qualifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_8cux22275v8r`
A :dt:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.

:dp:`fls_3td9tztnj2jq`
See :s:`FunctionQualifierList`.
```

### After glossary entry (generated)

```rst
.. _fls_vWFtqA2ofpD5:

function qualifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_YQaonxGrYKpL`
A :t:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
src/functions.rst
:dp:`fls_gn1ngtx2tp2s`
A :t:`function` is a :t:`value` of a :t:`function type` that models a behavior.

:dp:`fls_bdx9gnnjxru3`
A :t:`function` declares a unique :t:`function item type` for itself.

:dp:`fls_87jnkimc15gi`
A :t:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.

:dp:`fls_nwywh1vjt6rr`
A :t:`function` shall not be subject to both :t:`keyword` ``async`` and
:t:`keyword` ``const``.

:dp:`fls_uwuthzfgslif`
A :t:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.
```

### After chapter excerpt (current)

```rst
src/functions.rst
:dp:`fls_gn1ngtx2tp2s`
A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.

:dp:`fls_bdx9gnnjxru3`
A :t:`function` declares a unique :t:`function item type` for itself.

:dp:`fls_87jnkimc15gi`
A :dt:`function qualifier` is a :t:`construct` that determines the role of
a :t:`function`.

:dp:`fls_nwywh1vjt6rr`
A :t:`function` shall not be subject to both :t:`keyword` ``async`` and
:t:`keyword` ``const``.

:dp:`fls_uwuthzfgslif`
A :dt:`function parameter` is a :t:`construct` that yields a set of
:t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
site of a :t:`call expression` or a :t:`method call expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function signature (function_signature)

### Before glossary entry (origin/main)

```rst
.. _fls_hz3zunp8lrfl:

function signature
^^^^^^^^^^^^^^^^^^

:dp:`fls_ndld48kg6o8d`
A :dt:`function signature` is a unique identification of a :t:`function`
that encompasses of its :t:`[function qualifier]s`, :t:`name`,
:t:`[generic parameter]s`, :t:`[function parameter]s`, :t:`return type`, and
:t:`where clause`.
```

### After glossary entry (generated)

```rst
.. _fls_1jHZyYiJSLsV:

function signature
^^^^^^^^^^^^^^^^^^

:dp:`fls_EIbiHyCE04Qh`
A :t:`function signature` is a unique identification of a :t:`function`
that encompasses of its :t:`[function qualifier]s`, :t:`name`,
:t:`[generic parameter]s`, :t:`[function parameter]s`, :t:`return type`, and
:t:`where clause`.
```

### Before chapter excerpt (origin/main)

```rst
src/functions.rst
:dp:`fls_bHwy8FLzEUi3`
A :t:`function body` denotes a :t:`control flow boundary`.

:dp:`fls_5Q861wb08DU3`
A :t:`function body` of an :t:`async function` denotes an
:t:`async control flow boundary`.

:dp:`fls_owdlsaaygtho`
A :t:`function signature` is a unique identification of a :t:`function`
that encompasses of its :t:`[function qualifier]s`, :t:`name`,
:t:`[generic parameter]s`, :t:`[function parameter]s`, :t:`return type`, and
:t:`where clause`.

:dp:`fls_2049qu3ji5x7`
A :t:`constant function` is a :t:`function` subject to :t:`keyword` ``const``.

:dp:`fls_7mlanuh5mvpn`
The :t:`function body` of a :t:`constant function` shall be a
:t:`constant expression`.
```

### After chapter excerpt (current)

```rst
src/functions.rst
:dp:`fls_bHwy8FLzEUi3`
A :t:`function body` denotes a :t:`control flow boundary`.

:dp:`fls_5Q861wb08DU3`
A :t:`function body` of an :t:`async function` denotes an
:t:`async control flow boundary`.

:dp:`fls_owdlsaaygtho`
A :dt:`function signature` is a unique identification of a :t:`function`
that encompasses of its :t:`[function qualifier]s`, :t:`name`,
:t:`[generic parameter]s`, :t:`[function parameter]s`, :t:`return type`, and
:t:`where clause`.

:dp:`fls_2049qu3ji5x7`
A :dt:`constant function` is a :t:`function` subject to :t:`keyword` ``const``.

:dp:`fls_7mlanuh5mvpn`
The :t:`function body` of a :t:`constant function` shall be a
:t:`constant expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## function type (function_type)

### Before glossary entry (origin/main)

```rst
.. _fls_yo2x1llt9ejy:

function type
^^^^^^^^^^^^^

:dp:`fls_4e19116glgtv`
A :dt:`function type` is either a :t:`closure type` or a
:t:`function item type`.
```

### After glossary entry (generated)

```rst
.. _fls_Srbu7Il8d5uE:

function type
^^^^^^^^^^^^^

:dp:`fls_QTuGTOgECCHj`
A :t:`function type` is either a :t:`closure type` or a
:t:`function item type`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_bQhh3zHAKjSu`.
src/types-and-traits.rst
* :dp:`fls_sXZknxozJxtC`
  :std:`core::mem::ManuallyDrop`, or

* :dp:`fls_vgNK01SXacnx`
  A :t:`tuple type` whose :t:`[tuple field]s`' :t:`[type]s` are all valid
  :t:`union field` :t:`[type]s`, or

* :dp:`fls_bQhh3zHAKjSu`
  An :t:`array type` whose :t:`element type` is a valid :t:`union field`
  :t:`[type]s`.

:dp:`fls_bsykgnbatpmi`
A :t:`closure type` is a unique anonymous :t:`function type` that encapsulates
all :t:`[capture target]s` of a :t:`closure expression`.

:dp:`fls_zfj4l8bigdg0`
A :t:`closure type` implements the :std:`core::ops::FnOnce` :t:`trait`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
* :dp:`fls_vgNK01SXacnx`
  A :t:`tuple type` whose :t:`[tuple field]s`' :t:`[type]s` are all valid
  :t:`union field` :t:`[type]s`, or

* :dp:`fls_bQhh3zHAKjSu`
  An :t:`array type` whose :t:`element type` is a valid :t:`union field`
  :t:`[type]s`.

:dp:`fls_P5PFddyptGec`
A :dt:`function type` is either a :t:`closure type` or a
:t:`function item type`.

:dp:`fls_bsykgnbatpmi`
A :dt:`closure type` is a unique anonymous :t:`function type` that encapsulates
all :t:`[capture target]s` of a :t:`closure expression`.

:dp:`fls_zfj4l8bigdg0`
A :t:`closure type` implements the :std:`core::ops::FnOnce` :t:`trait`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## function-like macro (function_like_macro)

### Before glossary entry (origin/main)

```rst
.. _fls_gzybxk1gosm6:

function-like macro
^^^^^^^^^^^^^^^^^^^

:dp:`fls_psnab9cuq4bu`
A :dt:`function-like macro` is a :t:`procedural macro` that consumes a stream
of :t:`[token]s` and produces a stream of tokens, and is invoked directly.
```

### After glossary entry (generated)

```rst
.. _fls_4N5RB21tO9kg:

function-like macro
^^^^^^^^^^^^^^^^^^^

:dp:`fls_CWSL7RPgrU4X`
A :t:`function-like macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_vtzuplb1p3s`
A :t:`macro implementation function` is the :t:`function` that encapsulates the
syntactic transformations of a :t:`procedural macro`.

:dp:`fls_mewfehvgm16r`
A :t:`macro implementation function` enters the :t:`name` of the
:t:`procedural macro` into the :t:`macro namespace`.

:dp:`fls_utd3zqczix`
A :t:`function-like macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`.

:dp:`fls_ojr30lf6jfx0`
The :t:`macro implementation function` of a :t:`function-like macro` shall be
subject to the following restrictions:

* :dp:`fls_ljkjmegynhiy`
  It shall be subject to :t:`attribute` :c:`proc_macro`,
```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_vtzuplb1p3s`
A :t:`macro implementation function` is the :t:`function` that encapsulates the
syntactic transformations of a :t:`procedural macro`.

:dp:`fls_mewfehvgm16r`
A :t:`macro implementation function` enters the :t:`name` of the
:t:`procedural macro` into the :t:`macro namespace`.

:dp:`fls_utd3zqczix`
A :dt:`function-like macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`.

:dp:`fls_ojr30lf6jfx0`
The :t:`macro implementation function` of a :t:`function-like macro` shall be
subject to the following restrictions:

* :dp:`fls_ljkjmegynhiy`
  It shall be subject to :t:`attribute` :c:`proc_macro`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## fundamental (fundamental)

### Before glossary entry (origin/main)

```rst
.. _fls_OFMoUA3eFtuC:

fundamental
^^^^^^^^^^^

:dp:`fls_e0dRD4NTE0UP`
A :t:`trait` or :t:`type` is :dt:`fundamental` when its
:t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type`
is always treated as if it was a :t:`local trait` or a :t:`local type`.
```

### After glossary entry (generated)

```rst
.. _fls_zJIIt555AtUi:

fundamental
^^^^^^^^^^^

:dp:`fls_0CF4zxTkIsx9`
A :t:`trait` or :t:`type` is :t:`fundamental` when its
:t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type`
is always treated as if it was a :t:`local trait` or a :t:`local type`.
```

### Before chapter excerpt (origin/main)

```rst
src/implementations.rst
* :dp:`fls_9klwbsh3vlxu`
    At least one of :t:`[type]s` ``T0, T1, .., TN`` is :T:`fundamental` or a
    :t:`local type`, and

  * :dp:`fls_9gmc1tcscq9v`
    No :t:`type parameter` of ``P1, P2, .., PN`` that is not used in another
    :t:`type` may appear in the :t:`non-[local type]s` and
    :t:`non-[fundamental]` :t:`[type]s` of ``T0, T1, .., TN``.

:dp:`fls_UkQhjEWSJpDq`
A :t:`trait` or :t:`type` is :t:`fundamental` when its
:t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type`
is always treated as if it was a :t:`local trait` or a :t:`local type`.

:dp:`fls_fSybUG40hA5r`
The following :t:`[type]s` are :t:`fundamental`:

* :dp:`fls_z8APl0CEF7a0`
  :t:`[reference type]s`
```

### After chapter excerpt (current)

```rst
src/implementations.rst
* :dp:`fls_9klwbsh3vlxu`
    At least one of :t:`[type]s` ``T0, T1, .., TN`` is :T:`fundamental` or a
    :t:`local type`, and

  * :dp:`fls_9gmc1tcscq9v`
    No :t:`type parameter` of ``P1, P2, .., PN`` that is not used in another
    :t:`type` may appear in the :t:`non-[local type]s` and
    :t:`non-[fundamental]` :t:`[type]s` of ``T0, T1, .., TN``.

:dp:`fls_UkQhjEWSJpDq`
A :t:`trait` or :t:`type` is :dt:`fundamental` when its
:t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type`
is always treated as if it was a :t:`local trait` or a :t:`local type`.

:dp:`fls_fSybUG40hA5r`
The following :t:`[type]s` are :t:`fundamental`:

* :dp:`fls_z8APl0CEF7a0`
  :t:`[reference type]s`
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## future (future)

### Before glossary entry (origin/main)

```rst
.. _fls_yxzpexco8ag3:

future
^^^^^^

:dp:`fls_pvigospl4n3g`
A :dt:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.
```

### After glossary entry (generated)

```rst
.. _fls_bk4rJUKr5te0:

future
^^^^^^

:dp:`fls_1IH023jEq7wQ`
A :t:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.
```

### Before chapter excerpt (origin/main)

```rst
src/concurrency.rst
* - :dp:`fls_q7mn6pdd8bix`
     - **Type**
     - **Atomic Type**
   * - :dp:`fls_jx0784jzxy00`
     - :c:`bool`
     - :std:`core::sync::atomic::AtomicBool`
   * - :dp:`fls_vzuwnpx7mt08`
     - :c:`i8`
     - :std:`core::sync::atomic::AtomicI8`
   * - :dp:`fls_cpcd0vexfbhj`
     - :c:`i16`
     - :std:`core::sync::atomic::AtomicI16`
   * - :dp:`fls_jt7rfq9atbiv`
     - :c:`i32`
     - :std:`core::sync::atomic::AtomicI32`
   * - :dp:`fls_2hqmfwswc6k`
     - :c:`i64`
     - :std:`core::sync::atomic::AtomicI64`
   * - :dp:`fls_5ab2sw3gwmt3`
     - :c:`isize`
     - :std:`core::sync::atomic::AtomicIsize`
   * - :dp:`fls_w2mw833g28eb`
     - ``*mut T``
     - :std:`core::sync::atomic::AtomicPtr`
   * - :dp:`fls_mjq1l1y0vmz4`
     - :c:`u8`
     - :std:`core::sync::atomic::AtomicU8`
   * - :dp:`fls_906978wtss6n`
     - :c:`u16`
     - :std:`core::sync::atomic::AtomicU16`
   * - :dp:`fls_4urmnh4mfehl`
     - :c:`u32`
     - :std:`core::sync::atomic::AtomicU32`
   * - :dp:`fls_2qkrcd5eovpe`
     - :c:`u64`
     - :std:`core::sync::atomic::AtomicU64`
   * - :dp:`fls_cry1e78gp19q`
     - :c:`usize`
     - :std:`core::sync::atomic::AtomicUsize`

:dp:`fls_g40xp4andj5g`
The Rust programming language provides asynchronous computation through
:t:`module` :std:`core::task` and the :std:`core::future::Future` :t:`trait`.

:dp:`fls_fte085hi1yqj`
A :t:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.

:dp:`fls_7muubin2wn1v`
The computed :t:`value` of a :t:`future` is obtained by using an
:t:`await expression` or by invoking :std:`core::future::Future::poll`.

:dp:`fls_ftzey2156ha`
:std:`core::future::Future::poll` shall not be invoked on a :t:`future` that has
already returned :std:`core::task::Poll::Ready`.
```

### After chapter excerpt (current)

```rst
src/concurrency.rst
* - :dp:`fls_q7mn6pdd8bix`
     - **Type**
     - **Atomic Type**
   * - :dp:`fls_jx0784jzxy00`
     - :c:`bool`
     - :std:`core::sync::atomic::AtomicBool`
   * - :dp:`fls_vzuwnpx7mt08`
     - :c:`i8`
     - :std:`core::sync::atomic::AtomicI8`
   * - :dp:`fls_cpcd0vexfbhj`
     - :c:`i16`
     - :std:`core::sync::atomic::AtomicI16`
   * - :dp:`fls_jt7rfq9atbiv`
     - :c:`i32`
     - :std:`core::sync::atomic::AtomicI32`
   * - :dp:`fls_2hqmfwswc6k`
     - :c:`i64`
     - :std:`core::sync::atomic::AtomicI64`
   * - :dp:`fls_5ab2sw3gwmt3`
     - :c:`isize`
     - :std:`core::sync::atomic::AtomicIsize`
   * - :dp:`fls_w2mw833g28eb`
     - ``*mut T``
     - :std:`core::sync::atomic::AtomicPtr`
   * - :dp:`fls_mjq1l1y0vmz4`
     - :c:`u8`
     - :std:`core::sync::atomic::AtomicU8`
   * - :dp:`fls_906978wtss6n`
     - :c:`u16`
     - :std:`core::sync::atomic::AtomicU16`
   * - :dp:`fls_4urmnh4mfehl`
     - :c:`u32`
     - :std:`core::sync::atomic::AtomicU32`
   * - :dp:`fls_2qkrcd5eovpe`
     - :c:`u64`
     - :std:`core::sync::atomic::AtomicU64`
   * - :dp:`fls_cry1e78gp19q`
     - :c:`usize`
     - :std:`core::sync::atomic::AtomicUsize`

:dp:`fls_g40xp4andj5g`
The Rust programming language provides asynchronous computation through
:t:`module` :std:`core::task` and the :std:`core::future::Future` :t:`trait`.

:dp:`fls_fte085hi1yqj`
A :dt:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.

:dp:`fls_7muubin2wn1v`
The computed :t:`value` of a :t:`future` is obtained by using an
:t:`await expression` or by invoking :std:`core::future::Future::poll`.

:dp:`fls_ftzey2156ha`
:std:`core::future::Future::poll` shall not be invoked on a :t:`future` that has
already returned :std:`core::task::Poll::Ready`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## future operand (future_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_dvk8ccb46abk:

future operand
^^^^^^^^^^^^^^

:dp:`fls_fold1inh5jev`
A :dt:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
an :t:`await expression`.

:dp:`fls_tbfpowv90u5w`
See :s:`FutureOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_af03aQc8San7:

future operand
^^^^^^^^^^^^^^

:dp:`fls_HueUEPQagLDX`
A :t:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
an :t:`await expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
#. :dp:`fls_ubwj8uj6sbgt`
   Control is transferred to the caller frame.

:dp:`fls_sjz5s71hwm7l`
An :t:`await expression` is an :t:`expression` that polls a :t:`future`,
suspending the :t:`execution` of the :t:`future` until the :t:`future` is ready.

:dp:`fls_vhchgab59jvd`
A :t:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
an :t:`await expression`.

:dp:`fls_k9pncajmhgk1`
An :t:`await expression` shall appear within an
:t:`async control flow boundary`. Only the innermost :t:`control flow boundary`
shall be considered.

:dp:`fls_9uw5pd7kbrx3`
The :t:`type` of a :t:`future operand` shall implement the
:std:`core::future::IntoFuture` :t:`trait`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
#. :dp:`fls_ubwj8uj6sbgt`
   Control is transferred to the caller frame.

:dp:`fls_sjz5s71hwm7l`
An :dt:`await expression` is an :t:`expression` that polls a :t:`future`,
suspending the :t:`execution` of the :t:`future` until the :t:`future` is ready.

:dp:`fls_vhchgab59jvd`
A :dt:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
an :t:`await expression`.

:dp:`fls_k9pncajmhgk1`
An :t:`await expression` shall appear within an
:t:`async control flow boundary`. Only the innermost :t:`control flow boundary`
shall be considered.

:dp:`fls_9uw5pd7kbrx3`
The :t:`type` of a :t:`future operand` shall implement the
:std:`core::future::IntoFuture` :t:`trait`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.
