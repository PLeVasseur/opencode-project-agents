# Legacy glossary definitions for missing terms

## definition_site_hygiene
Title: definition site hygiene

```rst
:dp:`fls_2Y1Dpw5ZEqT3`
:dt:`Definition site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site. :t:`[Identifier]s` with
:t:`definition site hygiene` cannot reference the environment of the
:s:`MacroRulesDeclaration`, cannot be referenced by the environment of a
:s:`MacroInvocation`, and are considered :t:`hygienic`.
```

## discriminant_type
Title: discriminant type

```rst
:dp:`fls_t4yeovFm83Wo`
A :dt:`discriminant type` is the :t:`type` of a :t:`discriminant`.
```

## division_assignment
Title: division assignment

```rst
:dp:`fls_kvQskrzE1y97`
For :dt:`division assignment`, see :t:`division assignment expression`.
```

## dropping
Title: dropping

```rst
:dp:`fls_k4mguykh8ey`
:dt:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`.
```

## element_type
Title: element type

```rst
:dp:`fls_3bndijf8g9os`
An :dt:`element type` is the :t:`type` of the elements of an :t:`array type` or
a :t:`slice type`.
```

## elided
Title: elided

```rst
:dp:`fls_lo3c3n9wy6qz`
For :dt:`elided`, see :t:`elided lifetime`.
```

## elided_lifetime
Title: elided lifetime

```rst
:dp:`fls_9q28407ev0a6`
An :dt:`elided lifetime` is either an :t:`unnamed lifetime` or a :t:`lifetime`
that has been explicitly omitted from a :t:`function signature` or an
:t:`implementation`.
```

## enum
Title: enum

```rst
:dp:`fls_9o0ig19xh2f5`
An :dt:`enum` is an :t:`item` that declares an :t:`enum type`.
```

## enum_field
Title: enum field

```rst
:dp:`fls_J8udq05QGiEj`
An :dt:`enum field` is a :t:`field` of an :t:`enum variant`.
```

## enum_value
Title: enum value

```rst
:dp:`fls_QdBTdVLB2xHk`
An :dt:`enum value` is a :t:`value` of an :t:`enum type`.
```

## enum_variant_value
Title: enum variant value

```rst
:dp:`fls_VQRqNPFFWmDp`
An :dt:`enum variant value` is the :t:`enum value` of the corresponding
:t:`enum` of the :t:`enum variant`.
```

## escaped_character
Title: escaped character

```rst
:dp:`fls_7yvnbakmo7y5`
An :dt:`escaped character` is the textual representation for a character with
special meaning. An escaped character consists of character 0x5C (reverse
solidus), followed by the single character encoding of the special meaning
character. For example, ``\t`` is the escaped character for 0x09 (horizontal
tabulation).
```

## fat_pointer
Title: fat pointer

```rst
:dp:`fls_knbc2jv5c5ds`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
```

## ffi
Title: FFI

```rst
:dp:`fls_z363fu89mj1c`
For :dt:`FFI`, see :t:`Foreign Function Interface`.
```

## field_index
Title: field index

```rst
:dp:`fls_6061r871qgbj`
A :dt:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
```

## field_list
Title: field list

```rst
:dp:`fls_xMZsrxMc9Cni`
A :dt:`field list` is a :s:`RecordStructFieldList` or :s:`TupleStructFieldList`.
```

## fixed_sized_type
Title: fixed sized type

```rst
:dp:`fls_eadiywl20jo4`
A :dt:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.
```

## floating_point_type
Title: floating-point type

```rst
:dp:`fls_1w5yjiffah1u`
A :dt:`floating-point type` is a :t:`numeric type` whose :t:`[value]s` denote
fractional numbers.
```

## floating_point_value
Title: floating-point value

```rst
:dp:`fls_rx8cvWPlvel5`
A :dt:`floating-point value` is a :t:`value` of a :t:`floating-point type`.
```

## for_loop
Title: for loop

```rst
:dp:`fls_gmhh56arsbw8`
For :dt:`for loop`, see :t:`for loop expression`.
```

## foreign_function_interface
Title: Foreign Function Interface

```rst
:dp:`fls_240yj1kym1kh`
:dt:`Foreign Function Interface` employs :t:`ABI`, :t:`[attribute]s`,
:t:`external block`, :t:`[external function]s`, linkage, and :t:`type`
:t:`layout` to interface a Rust program with foreign code.
```

## full_range_expression
Title: full range expression

```rst
:dp:`fls_NIb9UOIRjMqa`
A :dt:`full range expression` is a :t:`range expression` that covers the full
range of a :t:`type`.
```

## function_pointer_type_parameter
Title: function pointer type parameter

```rst
:dp:`fls_nF1k90JJWq2K`
A :dt:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.
```

## function_type
Title: function type

```rst
:dp:`fls_4e19116glgtv`
A :dt:`function type` is either a :t:`closure type` or a
:t:`function item type`.
```

## generic_argument
Title: generic argument

```rst
:dp:`fls_meimxi20p51a`
A :dt:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.
```

## generic_conformance
Title: generic conformance

```rst
:dp:`fls_PfvELNsNySLT`
:dt:`Generic conformance` measures the compatibility between a set of
:t:`[generic parameter]s` and a set of :t:`[generic argument]s`.
```

## generic_substitution
Title: generic substitution

```rst
:dp:`fls_Led1Nxfcd70K`
A :dt:`generic substitution` is the replacement of a :t:`generic parameter`
with a :t:`generic argument`.
```

## immutable_place_expression_context
Title: immutable place expression context

```rst
:dp:`fls_UvrQ49dSoQGc`
An :dt:`immutable place expression context` is a :t:`place expression context`
whose memory location cannot be modified.
```

## immutable_variable
Title: immutable variable

```rst
:dp:`fls_sdg35i92taip`
An :dt:`immutable variable` is a :t:`variable` whose :t:`value` cannot be
modified.
```

## implementation_conformance
Title: implementation conformance

```rst
:dp:`fls_Gpq4EP1SsYJR`
:dt:`Implementation conformance` measures the compatibility between a
:t:`trait implementation` and the :t:`implemented trait`.
```

## incomplete_associated_constant
Title: incomplete associated constant

```rst
:dp:`fls_bq48gl84bul0`
An :dt:`incomplete associated constant` is an :t:`associated constant` without
a :t:`constant initializer`.
```

## incomplete_associated_function
Title: incomplete associated function

```rst
:dp:`fls_iboondra204w`
An :dt:`incomplete associated function` is an :t:`associated function` without
a :t:`function body`.
```

## incomplete_associated_type
Title: incomplete associated type

```rst
:dp:`fls_tka0gth8rc9x`
An :dt:`incomplete associated type` is an :t:`associated type` without an
:t:`initialization type`.
```

## indexed_field_selector
Title: indexed field selector

```rst
:dp:`fls_u6mh5yediub`
An :dt:`indexed field selector` is a :t:`field selector` where the selected
:t:`field` is indicated by an index.
```

## indirection_type
Title: indirection type

```rst
:dp:`fls_8so1phpdjyk8`
An :dt:`indirection type` is a :t:`type` whose :t:`[value]s` refer to memory
locations.
```

## infinite_loop
Title: infinite loop

```rst
:dp:`fls_xpm53i3rkuu0`
For :dt:`infinite loop`, see :t:`infinite loop expression`.
```

## initialization_expression
Title: initialization expression

```rst
:dp:`fls_KUeiSByPUc4w`
An :dt:`initialization expression` is either a :t:`constant initializer` or a
:t:`static initializer`.
```

## initialization_type
Title: initialization type

```rst
:dp:`fls_crn87nne7k38`
An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
:t:`name` for.
```

## item
Title: item

```rst
:dp:`fls_2ghaujiqkhyy`
An :dt:`item` is the most basic semantic element in program text. An item
defines the compile- and run-time semantics of a program.
```

## layout
Title: layout

```rst
:dp:`fls_qk602dmhc0d6`
:dt:`Layout` specifies the :t:`alignment`, :t:`size`, and the relative offset
of :t:`[field]s` in a :t:`type`.
```

## let_binding
Title: let binding

```rst
:dp:`fls_sw6HrsxsnG2y`
A :dt:`let binding` is the :t:`binding` introduced by a :t:`let statement`, an :t:`if let expression`, or a :t:`while let loop expression`.
```

## local_variable
Title: local variable

```rst
:dp:`fls_3inlcyi6444u`
For :dt:`local variable`, see :t:`variable`.
```

## loop
Title: loop

```rst
:dp:`fls_omjnvxva07z2`
For :dt:`loop`, see :t:`loop expression`.
```

## macro_repetition_in_matching
Title: macro repetition in matching

```rst
:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.
```

## mixed_site_hygiene
Title: mixed site hygiene

```rst
:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.
```

## multiplication_assignment
Title: multiplication assignment

```rst
:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.
```

## mutable_assignee_expression
Title: mutable assignee expression

```rst
:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.
```

## mutable_binding
Title: mutable binding

```rst
:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.
```

## mutable_variable
Title: mutable variable

```rst
:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.
```

## named_field_selector
Title: named field selector

```rst
:dp:`fls_cczpgxqdyh1e`
A :dt:`named field selector` is a :t:`field selector` where the selected
:t:`field` is indicated by an :t:`identifier`.
```

## nan_boxing
Title: NaN-boxing

```rst
:dp:`fls_s956sJGwOa6z`
:dt:`NaN-boxing` is a technique for encoding :t:`[value]s` using the low order
bits of the mantissa of a 64-bit IEEE floating-point ``NaN``.
```

## numeric_type
Title: numeric type

```rst
:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.
```

## object_safety
Title: object safety

```rst
:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.
```

## place
Title: place

```rst
:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.
```

## pointer
Title: pointer

```rst
:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.
```

## pointer_type
Title: pointer type

```rst
:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.
```

## prelude_entity
Title: prelude entity

```rst
:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
```

## prelude_name
Title: prelude name

```rst
:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.
```

## principal_trait
Title: principal trait

```rst
:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.
```

## punctuator
Title: punctuator

```rst
:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.
```

## raw_pointer
Title: raw pointer

```rst
:dp:`fls_rbdilcmt2cns`
A :dt:`raw pointer` is a pointer of a :t:`raw pointer type`.
```

## reachable_control_flow_path
Title: reachable control flow path

```rst
:dp:`fls_IxrvzuBg8j3E`
A :dt:`reachable control flow path` is a control flow path that can be
taken by the execution of a program between two given points in the program.
```

## record_enum_variant
Title: record enum variant

```rst
:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.
```

## record_struct
Title: record struct

```rst
:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.
```

## record_struct_field
Title: record struct field

```rst
:dp:`fls_lb0t10evec6z`
A :dt:`record struct field` is a :t:`field` of a :t:`record struct type`.
```

## record_struct_type
Title: record struct type

```rst
:dp:`fls_mgrz3o51gbis`
A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.
```

## record_struct_value
Title: record struct value

```rst
:dp:`fls_SMBIc0JMck1H`
A :dt:`record struct value` is a :t:`value` of a :t:`record struct type`.
```

## reference_identifier_pattern
Title: reference identifier pattern

```rst
:dp:`fls_jQs6oJ4RFBPN`
A :dt:`reference identifier pattern` is an :t:`identifier pattern` with
:t:`keyword` ``ref``.
```

## refutable_type
Title: refutable type

```rst
:dp:`fls_l2yz6jeehm52`
A :dt:`refutable type` is a :t:`type` that has more than one :t:`value`.
```

## remainder_assignment
Title: remainder assignment

```rst
:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.
```

## representation_modifier
Title: representation modifier

```rst
:dp:`fls_BCvXL7HkXqdZ`
A :dt:`representation modifier` is a :t:`construct` that modifies the
:t:`alignment` of a :t:`type`.
```

## rustc
Title: rustc

```rst
:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.
```

## safety_invariant
Title: safety invariant

```rst
:dp:`fls_wRZfAmTmMGTX`
A :dt:`safety invariant` is an invariant that when violated may result in
:t:`undefined behavior`.
```

## scope_hierarchy
Title: scope hierarchy

```rst
:dp:`fls_Spcc3L9X939d`
The :dt:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
by :t:`[scoping construct]s`.
```

## sequence_type
Title: sequence type

```rst
:dp:`fls_lk1oslxh8h9p`
A :dt:`sequence type` represents a sequence of elements.
```

## shared_borrow
Title: shared borrow

```rst
:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.
```

## shared_reference
Title: shared reference

```rst
:dp:`fls_cspa4c5mscnw`
A :dt:`shared reference` is a :t:`value` of a :t:`shared reference type`.
```

## shift_left_assignment
Title: shift left assignment

```rst
:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.
```

## shift_right_assignment
Title: shift right assignment

```rst
:dp:`fls_XuwcHjwHdyA8`
For :dt:`shift right assignment`, see :t:`shift right assignment expression`.
```

## signed_integer_type
Title: signed integer type

```rst
:dp:`fls_vcronf7l2bhy`
A :dt:`signed integer type` is an :t:`integer type` whose :t:`[value]s` denote
negative whole numbers, zero, and positive whole numbers.
```

## sized_type
Title: sized type

```rst
:dp:`fls_pwcgsRCNSwKn`
A :dt:`sized type` is a :t:`type` with statically known size.
```

## slice
Title: slice

```rst
:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.
```

## statement
Title: statement

```rst
:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.
```

## struct
Title: struct

```rst
:dp:`fls_rufylj7qxs1w`
A :dt:`struct` is an :t:`item` that declares a :t:`struct type`.
```

## struct_field
Title: struct field

```rst
:dp:`fls_8Z9YWMnrHXJS`
A :dt:`struct field` is a :t:`field` of a :t:`struct type`.
```

## struct_value
Title: struct value

```rst
:dp:`fls_YmZfW9kWlbIX`
A :dt:`struct value` is a :t:`value` of a :t:`struct type`.
```

## subexpression
Title: subexpression

```rst
:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.
```

## subtraction_assignment
Title: subtraction assignment

```rst
:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.
```

## subtype
Title: subtype

```rst
:dp:`fls_pmkjOWsieQog`
A :dt:`subtype` is a :t:`type` with additional constraints.
```

## syntactic_category
Title: syntactic category

```rst
:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.
```

## textual_type
Title: textual type

```rst
:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.
```

## thin_pointer
Title: thin pointer

```rst
:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.
```

## thin_pointer_type
Title: thin pointer type

```rst
:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.
```

## token
- Not found in legacy glossary.

## trait_type
Title: trait type

```rst
:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.
```

## tuple
Title: tuple

```rst
:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.
```

## tuple_enum_variant
Title: tuple enum variant

```rst
:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.
```

## tuple_enum_variant_value
Title: tuple enum variant value

```rst
:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.
```

## tuple_field
Title: tuple field

```rst
:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.
```

## tuple_struct
Title: tuple struct

```rst
:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.
```

## tuple_struct_field
Title: tuple struct field

```rst
:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.
```

## tuple_struct_type
Title: tuple struct type

```rst
:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.
```

## tuple_struct_value
Title: tuple struct value

```rst
:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.
```

## type_ascription
Title: type ascription

```rst
:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.
```

## type_specification
Title: type specification

```rst
:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.
```

## unary_operator
Title: unary operator

```rst
:dp:`fls_p6mk2zrwgwem`
A :dt:`unary operator` operates on one :t:`operand`.
```

## undefined_behavior
Title: undefined behavior

```rst
:dp:`fls_WpwmltUMQGZa`
:dt:`Undefined behavior` is a situation that results in an unbounded error.
```

## unicode
Title: Unicode

```rst
:dp:`fls_y7gwku7pe1f4`
:dt:`Unicode` is the universal character encoding standard for written
characters and text described in the Unicode® Standard by the Unicode
Consortium.
```

## unifiable
Title: unifiable

```rst
:dp:`fls_01BNTCL4u8Gn`
For :dt:`unifiable`, see :t:`unify`.
```

## unified_type
Title: unified type

```rst
:dp:`fls_tqRwIe6z3a4j`
A :dt:`unified type` is a :t:`type` produced by :t:`type unification`.
```

## union
Title: union

```rst
:dp:`fls_x3oibk39dvem`
A :dt:`union` is an :t:`item` that declares a :t:`union type`.
```

## union_field
Title: union field

```rst
:dp:`fls_6t2fbnlndz8y`
A :dt:`union field` is a :t:`field` of a :t:`union type`.
```

## union_value
Title: union value

```rst
:dp:`fls_9BPrxky3a4nE`
A :dt:`union value` is a :t:`value` of a :t:`union type`.
```

## unique_immutable_reference
Title: unique immutable reference

```rst
:dp:`fls_eXrivAmNxzmv`
A :dt:`unique immutable reference` is an :t:`immutable reference` produced by
:t:`capturing` what is asserted to be the only live :t:`reference` to a
:t:`value` while the :t:`reference` exists.
```

## unit_enum_variant
Title: unit enum variant

```rst
:dp:`fls_y6fI5L3Tghie`
A :dt:`unit enum variant` is an :t:`enum variant` without a :t:`field list`.
```

## unit_struct
Title: unit struct

```rst
:dp:`fls_9t7fu8fcak6k`
A :dt:`unit struct` is a :t:`struct` without a :t:`field list`.
```

## unit_struct_constant
Title: unit struct constant

```rst
:dp:`fls_lLGn4JqddeAg`:
A :dt:`unit struct constant` is a :t:`constant` implicitly created by a
:t:`unit struct`.
```

## unit_struct_type
Title: unit struct type

```rst
:dp:`fls_oIzmvACNeQpE`
A :dt:`unit struct type` is the :t:`type` of a :t:`unit struct`.
```

## unit_struct_value
Title: unit struct value

```rst
:dp:`fls_Kr9nGIjx3N4R`
A :dt:`unit struct value` is a :t:`value` of a :t:`unit struct type`.
```

## unit_tuple
Title: unit tuple

```rst
:dp:`fls_vo1jw6rmu4yy`
A :dt:`unit tuple` is a :t:`value` of the :t:`unit type`.
```

## unit_type
Title: unit type

```rst
:dp:`fls_jtdtv3q2ls05`
The :dt:`unit type` is a :t:`tuple type` of zero :t:`arity`.
```

## unit_value
Title: unit value

```rst
:dp:`fls_ycdv4nvsdyx`
The :dt:`unit value` is the :t:`value` of a :t:`unit type`.
```

## unnamed_lifetime
Title: unnamed lifetime

```rst
:dp:`fls_4iy6zpq66mit`
An :dt:`unnamed lifetime` is a :t:`lifetime` declared with character 0x5F (low
line).
```

## unsafe_block
Title: unsafe block

```rst
:dp:`fls_8tkolhmd6xfp`
For :dt:`unsafe block`, see :t:`unsafe block expression`.
```

## unsafe_rust
Title: unsafe Rust

```rst
:dp:`fls_30asi010yf1a`
For :dt:`unsafe Rust`, see :t:`[unsafe operation]s`.
```

## unsafe_trait
Title: unsafe trait

```rst
:dp:`fls_w6zlsf2ye457`
An :dt:`unsafe trait` is a :t:`trait` subject to :t:`keyword` ``unsafe``
```

## unsigned_integer_type
Title: unsigned integer type

```rst
:dp:`fls_dxnf79qemlg6`
An :dt:`unsigned integer type` is an :t:`integer type` whose :t:`[value]s`
denote zero and positive whole numbers.
```

## unsized_type
Title: unsized type

```rst
:dp:`fls_M9NpzBH8Wf4z`
An :dt:`unsized type` is a :t:`type` with statically unknown size.
```

## use_import
Title: use import

```rst
:dp:`fls_uccv9zthh5vt`
A :dt:`use import` brings :t:`entities <entity>` :t:`in scope` within the
:t:`block expression` of an :t:`expression-with-block` or :t:`module` where the
:t:`use import` resides.
```

## validity_invariant
Title: validity invariant

```rst
:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.
```

## visibility_modifier
Title: visibility modifier

```rst
:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.
```

## visible_emptiness
Title: visible emptiness

```rst
:dp:`fls_shXDYqnUy2Pb`
:dt:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.
```

## while_let_loop
Title: while let loop

```rst
:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.
```

## while_loop
Title: while loop

```rst
:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.
```

## zero_sized_type
Title: zero-sized type

```rst
:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.
```

## zero_variant_enum_type
Title: zero-variant enum type

```rst
:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

