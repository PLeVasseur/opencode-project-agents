# Missing term definitions (chapter sources)

## definition site hygiene (definition_site_hygiene)
- macros.rst:1085: :t:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
- macros.rst:1086: site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference

## discriminant type (discriminant_type)
- types-and-traits.rst:1608: The :t:`discriminant type` of an :t:`enum type` with :t:`C representation` is
- types-and-traits.rst:1613: The :t:`discriminant type` of an :t:`enum type` with :t:`default representation`
- types-and-traits.rst:1617: The :t:`discriminant type` of an :t:`enum type` with
- types-and-traits.rst:1622: It is a static error if the :t:`discriminant type` cannot hold all the
- types-and-traits.rst:1646: :t:`discriminant type` of the :t:`enum type`.

## division assignment (division_assignment)
- expressions.rst:2672: The :t:`type` of the :t:`assigned operand` of a :t:`division assignment` shall
- expressions.rst:2754: For a :t:`division assignment`,

## dropping (dropping)
- ownership-and-deconstruction.rst:382: :t:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
- ownership-and-deconstruction.rst:391: :t:`Dropping` an :t:`initialized` :t:`variable` proceeds as follows:
- ownership-and-deconstruction.rst:427: Otherwise, :t:`dropping` has no effect.
- ownership-and-deconstruction.rst:465: A :dt:`drop scope` is a region of program text that governs the :t:`dropping` of
- ownership-and-deconstruction.rst:597: associated with a :t:`temporary` to prevent the premature :t:`dropping` of the
- inline-assembly.rst:1507: does not return, preventing the :t:`dropping` of :t:`[variable]s`.

## element type (element_type)
- entities-and-resolution.rst:1372: :t:`slice type` where the :t:`slice type` has the same :t:`element type`
- expressions.rst:2934: :t:`element type` and ``N`` is the size of the array. The :t:`size` of an
- patterns.rst:648: :t:`type` is ``[T; N]`` where ``T`` is the :t:`element type` of the
- types-and-traits.rst:498: The :t:`element type` shall be a :t:`fixed sized type`.
- types-and-traits.rst:535: The :t:`element type` shall be a :t:`fixed sized type`.
- types-and-traits.rst:856: An :t:`array type` whose :t:`element type` is a valid :t:`union field`
- types-and-traits.rst:1485: For :t:`array type` ``[T; N]`` where ``T`` is the :t:`element type` and ``N``
- types-and-traits.rst:1838: The :t:`[element type]s` of both :t:`[array type]s` are unifiable, and
- types-and-traits.rst:1845: :t:`[element type]s` of both :t:`[slice type]s` are unifiable.
- types-and-traits.rst:2204: :t:`[Array type]s` and :t:`[slice type]s`, if the :t:`[element type]` is
- types-and-traits.rst:2264: The :t:`type` is an :t:`array type` with a non-zero :t:`size operand` and an :t:`element type` that is subject to :t:`visible emptiness`.

## elided (elided)
- types-and-traits.rst:3334: Each :t:`elided` :t:`input lifetime` is a distinct :t:`lifetime parameter` in
- types-and-traits.rst:3339: :t:`lifetime` is assigned to all :t:`elided` :t:`[output lifetime]s`.
- types-and-traits.rst:3344: :t:`self input lifetime` is assigned to all :t:`elided`
- types-and-traits.rst:3360: its :t:`lifetime` :t:`elided` form is
- types-and-traits.rst:3378: An :t:`elided` :t:`lifetime` of a :t:`reference type` or :t:`path` in the
- types-and-traits.rst:3384: :t:`elided`.
- types-and-traits.rst:3387: The :t:`lifetime` of an :t:`associated trait constant` shall not be :t:`elided`.
- types-and-traits.rst:3399: its :t:`lifetime` :t:`elided` form is
- types-and-traits.rst:3417: An :t:`elided` :t:`lifetime` of a :t:`trait object type` is inferred as follows:
- types-and-traits.rst:3422: :t:`elided` :t:`lifetime`,
- types-and-traits.rst:3430: :t:`elided` :t:`lifetime`,
- types-and-traits.rst:3442: specified, then the :t:`elided` :t:`lifetime` is the ``'static``
- types-and-traits.rst:3443: :t:`lifetime` unless it is :t:`elided` in :t:`[expression]s` where it is
- types-and-traits.rst:3459: its :t:`lifetime` :t:`elided` form is
- types-and-traits.rst:3501: its :t:`lifetime` :t:`elided` form is

## elided lifetime (elided_lifetime)
- generics.rst:464: either inferred :t:`[lifetime argument]s` or :t:`[elided lifetime]s`,

## enum (enum)
- entities-and-resolution.rst:1062: exported by the :t:`module` or :t:`enum` its :t:`import path prefix` resolves to
- entities-and-resolution.rst:1066: An :t:`import path prefix` shall resolve to a :t:`module` or :t:`enum`.
- entities-and-resolution.rst:1077: If the :t:`import path prefix` resolves to an :t:`enum`, bring the
- entities-and-resolution.rst:1078: :t:`[name]s` of all of the :t:`enum`'s :t:`[enum variant]s` into :t:`scope`.
- exceptions-and-errors.rst:18: A possibly absent :t:`value` is usually represented using :t:`enum`
- exceptions-and-errors.rst:23: :t:`enum` :std:`core::result::Result`.
- exceptions-and-errors.rst:29: :t:`Enum` :std:`core::option::Option` indicates whether a :t:`value` is
- exceptions-and-errors.rst:34: :t:`Enum` :std:`core::result::Result` indicates whether a computation completed
- generics.rst:59: A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.
- types-and-traits.rst:660: possible variations of an :t:`enum`.

## enum field (enum_field)
- entities-and-resolution.rst:924: :t:`[Enum field]s`,

## enum value (enum_value)
- expressions.rst:3185: :t:`enum value`, a :t:`struct value`, or a :t:`union value`.
- expressions.rst:3192: A :dt:`base initializer` is a :t:`construct` that specifies an :t:`enum value`, or
- expressions.rst:3263: The :t:`value` of a :t:`struct expression` is the :t:`enum value`,
- patterns.rst:747: A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a

## enum variant value (enum_variant_value)
- patterns.rst:818: :t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

## escaped character (escaped_character)
- general.rst:290: :t:`escaped character`, for example:
- lexical-elements.rst:702: recognize :t:`[escaped character]s`.
- lexical-elements.rst:809: recognize :t:`[escaped character]s`.
- lexical-elements.rst:1246: recognize :t:`[escaped character]s`.

## fat pointer (fat_pointer)
- No :t: references found in src/*.rst

## FFI (ffi)
- ffi.rst:14: :t:`Foreign Function Interface` or :t:`FFI` employs :t:`ABI`,
- ffi.rst:19: The following :t:`[attribute]s` affect :t:`FFI`:

## field index (field_index)
- expressions.rst:3207: when the :t:`field index` of the :t:`indexed initializer` resolves to a valid
- patterns.rst:830: when its :t:`field index` and the position of the :t:`field` in the

## field list (field_list)
- No :t: references found in src/*.rst

## fixed sized type (fixed_sized_type)
- types-and-traits.rst:498: The :t:`element type` shall be a :t:`fixed sized type`.
- types-and-traits.rst:535: The :t:`element type` shall be a :t:`fixed sized type`.

## floating-point type (floating_point_type)
- entities-and-resolution.rst:971: :t:`[Floating-point type]s` :c:`f32` and :c:`f64`.
- expressions.rst:1338: If the type of the :t:`operand` is a :t:`floating-point type`, then the
- expressions.rst:1344: :t:`floating-point type`, then ``core::ops::Neg::neg(operand)`` is invoked.
- expressions.rst:1505: :t:`floating-point type`, then the :t:`addition expression` evaluates to the
- expressions.rst:1509: :t:`[floating-point type]s`. If unsigned integer addition or two's
- expressions.rst:1527: :t:`floating-point type`, then the :t:`division expression` evaluates to the
- expressions.rst:1531: :t:`[floating-point type]s`.
- expressions.rst:1556: :t:`floating-point type`, then the :t:`multiplication expression` evaluates
- expressions.rst:1560: multiplication for :t:`[floating-point type]s`. If unsigned integer
- expressions.rst:1578: :t:`floating-point type`, then the :t:`remainder expression` evaluates to
- expressions.rst:1583: :t:`[floating-point type]s`.
- expressions.rst:1608: :t:`floating-point type`, then the :t:`subtraction expression` evaluates to
- expressions.rst:1612: for :t:`[floating-point type]s`. If unsigned integer subtraction or two's
- expressions.rst:2280: Casting an :t:`operand` of a :t:`floating-point type` to a target
- expressions.rst:2302: :t:`floating-point type` produces the closest possible floating-point
- expressions.rst:2710: If the :t:`[type]s` of both :t:`[operand]s` are :t:`[integer type]s` or :t:`[floating-point type]s`, then
- lexical-elements.rst:1052: explicit :t:`floating-point type`.
- lexical-elements.rst:1075: If a :t:`floating-point type` can be uniquely determined from the surrounding
- types-and-traits.rst:85: :t:`Floating-point type`
- types-and-traits.rst:389: Operations on values of :t:`[floating point type]s` may not preserve the sign bit in case of the value being a IEEE floating-point ``NaN``.
- types-and-traits.rst:1817: If ``U`` is a :t:`floating-point type` or an
- types-and-traits.rst:2364: to :t:`[floating-point type]s`.
- types-and-traits.rst:2419: been unified with a concrete :t:`floating-point type`, perform floating-point

## floating-point value (floating_point_value)
- expressions.rst:948: An :t:`operator expression` that operates with :t:`[floating-point value]s` run as a :t:`constant expression` is allowed to yield different :t:`[value]s` compared to when run as a non-:t:`constant expression`.

## for loop (for_loop)
- entities-and-resolution.rst:487: The :t:`binding` of a :t:`for loop` or a :t:`while let loop` is :t:`in scope`
- expressions.rst:105: A :dt:`subject expression` is an :t:`expression` that controls :t:`[for loop]s`,

## Foreign Function Interface (foreign_function_interface)
- ffi.rst:14: :t:`Foreign Function Interface` or :t:`FFI` employs :t:`ABI`,
- ffi.rst:150: :t:`foreign function interface` boundary with an :t:`ABI` that does not end in

## full range expression (full_range_expression)
- expressions.rst:2438: A :t:`full range expression` corresponds to a :t:`rest pattern` if inside an

## function pointer type parameter (function_pointer_type_parameter)
- types-and-traits.rst:3289: to :t:`[function]s`, :t:`[function pointer type parameter]s`, and :t:`[path]s`
- types-and-traits.rst:3300: Any :t:`lifetime` related to a :t:`function pointer type parameter`.

## function type (function_type)
- functions.rst:52: A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.
- types-and-traits.rst:118: :t:`[Function type]s`
- types-and-traits.rst:882: A :dt:`closure type` is a unique anonymous :t:`function type` that encapsulates
- types-and-traits.rst:928: A :dt:`function item type` is a unique anonymous :t:`function type` that

## generic argument (generic_argument)
- generics.rst:52: statically by a :t:`generic argument`.
- generics.rst:202: If the :t:`type parameter` is used as a :t:`generic argument` of an
- generics.rst:205: the :t:`generic argument`.
- generics.rst:218: If the :t:`type parameter` is used as a :t:`generic argument` of an
- generics.rst:221: the :t:`generic argument`.
- generics.rst:296: true for the supplied :t:`[generic argument]s`.
- generics.rst:353: A :t:`generic argument` supplies a static input for an
- generics.rst:367: A :dt:`binding argument` is a :t:`generic argument` that supplies the :t:`type`
- generics.rst:371: A :dt:`binding bound argument` is a :t:`generic argument` that further imposes
- generics.rst:381: A :dt:`constant argument` is a :t:`generic argument` that supplies the
- generics.rst:390: A :dt:`lifetime argument` is a :t:`generic argument` that supplies the
- generics.rst:394: A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`type` of
- generics.rst:398: :t:`[Generic argument]s` are subject to :t:`generic conformance`.
- generics.rst:431: :t:`[generic parameter]s` and a set of :t:`[generic argument]s`.
- generics.rst:453: :t:`[Generic argument]s` are conformant with :t:`[generic parameter]s` when
- generics.rst:456: The :t:`[generic argument]s` consist only of conformant
- generics.rst:462: :t:`[generic argument]s` are :t:`[constant parameter]s` with
- generics.rst:478: :t:`[Generic argument]s` shall be conformant.
- types-and-traits.rst:58: :t:`[constant parameter]s` have been substituted with :t:`[generic argument]s`.
- types-and-traits.rst:3064: different :t:`[generic argument]s`.
- types-and-traits.rst:3425: If the :t:`trait object type` is used as a :t:`generic argument` and

## generic conformance (generic_conformance)
- generics.rst:398: :t:`[Generic argument]s` are subject to :t:`generic conformance`.
- generics.rst:430: :t:`Generic conformance` measures the compatibility between a set of

## generic substitution (generic_substitution)
- attributes.rst:1696: :t:`[generic substitution]s` for :t:`[type parameter]s` when constructing a
- types-and-traits.rst:1308: to be substituted by :t:`generic substitution`.
- types-and-traits.rst:1867: The corresponding :t:`[generic substitution]s` are unifiable.
- types-and-traits.rst:1876: The corresponding :t:`[generic substitution]s` are unifiable.
- types-and-traits.rst:1886: The corresponding :t:`[generic substitution]s` are unifiable.
- types-and-traits.rst:2945: set of possible :t:`[generic substitution]s`.

## immutable place expression context (immutable_place_expression_context)
- expressions.rst:1111: :t:`immutable place expression context`, then the :t:`dereference expression`

## immutable variable (immutable_variable)
- No :t: references found in src/*.rst

## implementation conformance (implementation_conformance)
- entities-and-resolution.rst:374: :t:`[implementation]s` that exhibit :t:`implementation conformance` to a
- implementations.rst:85: :t:`implementation conformance`.
- implementations.rst:209: A :t:`trait implementation` exhibits :t:`implementation conformance` when it

## incomplete associated constant (incomplete_associated_constant)
- No :t: references found in src/*.rst

## incomplete associated function (incomplete_associated_function)
- No :t: references found in src/*.rst

## incomplete associated type (incomplete_associated_type)
- No :t: references found in src/*.rst

## indexed field selector (indexed_field_selector)
- entities-and-resolution.rst:1282: :t:`indexed field selector`.
- entities-and-resolution.rst:1290: :t:`indexed field selector` proceeds as follows:

## indirection type (indirection_type)
- values.rst:52: A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
- types-and-traits.rst:127: :t:`[Indirection type]s`
- types-and-traits.rst:983: A :dt:`function pointer type` is an :t:`indirection type` that refers to a
- types-and-traits.rst:1033: A :dt:`raw pointer type` is an :t:`indirection type` without validity guarantees.
- types-and-traits.rst:1073: A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.
- types-and-traits.rst:1426: A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

## infinite loop (infinite_loop)
- expressions.rst:4135: shall be equivalent to the :t:`evaluation` the following :t:`infinite loop`:
- expressions.rst:4222: with an :t:`infinite loop`.

## initialization expression (initialization_expression)
- expressions.rst:2473: :t:`initialization expression` equivalent to the :t:`value operand`.

## initialization type (initialization_type)
- associated-items.rst:92: An :t:`associated implementation type` shall have an :t:`initialization type`.
- associated-items.rst:123: An :t:`associated trait type` shall not have an :t:`initialization type`.
- entities-and-resolution.rst:546: related :t:`initialization type` and :t:`where clause`.

## item (item)
- associated-items.rst:28: An :dt:`associated item` is an :t:`item` that appears within an
- entities-and-resolution.rst:141: :dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
- entities-and-resolution.rst:142: which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
- entities-and-resolution.rst:192: An external :t:`item`, a :t:`field`, or an :t:`item` that appears without a
- entities-and-resolution.rst:192: An external :t:`item`, a :t:`field`, or an :t:`item` that appears without a
- entities-and-resolution.rst:557: A :dt:`generic parameter` is not :t:`in scope` within nested :t:`[item]s`,
- entities-and-resolution.rst:568: An :dt:`item scope` is a :t:`scope` for :t:`[item]s`.
- entities-and-resolution.rst:571: An :t:`item` declared within the :t:`block expression` of an
- entities-and-resolution.rst:576: An :t:`item` declared within a :t:`module` is :t:`in scope` within the
- entities-and-resolution.rst:577: related :t:`module`. Such an :t:`item` is not :t:`in scope` within nested
- entities-and-resolution.rst:596: :t:`[closure expression]s`, :t:`[constant context]s`, and :t:`[item]s`.
- generics.rst:157: :t:`item`.
- generics.rst:177: An :t:`inferred constant` cannot be used in :t:`item` signatures.
- implementations.rst:40: An :dt:`implementation` is an :t:`item` that supplements an
- items.rst:47: zero or more :t:`[item]s` if the :t:`terminated macro invocation` appears as
- items.rst:48: an :t:`item`.
- macros.rst:451: new :t:`outer attribute` that can be attached to :t:`[item]s`.
- macros.rst:452: :t:`[Attribute macro]s` are used to replace :t:`[item]s` with other
- macros.rst:453: :t:`[item]s`.
- macros.rst:497: captures the :t:`token` stream produced from the related :t:`item`, including
- macros.rst:498: all :t:`[outer attribute]s` that apply to that :t:`item`.
- macros.rst:641: an :t:`item` within an :t:`external block`, or another
- macros.rst:643: :t:`[item]s`.
- macros.rst:690: an :t:`item` within an :t:`external block`, or another
- macros.rst:692: :t:`[item]s`.
- macros.rst:717: The :t:`item` subject to the :t:`derive macro` has all
- macros.rst:722: The :t:`item` subject to the :t:`derive macro` is transformed into a
- macros.rst:738: or more :t:`[item]s`.
- macros.rst:752: The :t:`item` subject to the :t:`attribute macro` has all
- macros.rst:757: The :t:`item` subject to the :t:`attribute macro` is transformed into a
- macros.rst:768: The :t:`item` subject to the :t:`attribute macro` is replaced with the
- macros.rst:771: :std:`proc_macro::TokenStream` does not constitute zero or more :t:`[item]s`.
- macros.rst:850: :t:`Fragment specifier` **item** requires an :t:`item`.
- macros.rst:876: character 0x3B (semicolon), excluding :t:`[item]s` that require character
- program-structure-and-compilation.rst:39: attribute]s`, :t:`[inner doc comment]s`, and :t:`[item]s`. The location of a
- program-structure-and-compilation.rst:73: A :dt:`module` is a container for zero or more :t:`[item]s`.
- program-structure-and-compilation.rst:149: A :t:`proc-macro crate` shall not declare :t:`[item]s` in its :t:`crate root
- program-structure-and-compilation.rst:150: module` with  :t:`public visibility` unless the :t:`item` is a :t:`procedural
- statements.rst:28: An :dt:`item statement` is a :t:`statement` that is expressed as an :t:`item`.
- lexical-elements.rst:517: :t:`[Name]s` of :t:`[item]s` that are subject to :t:`attribute`
- lexical-elements.rst:521: :t:`[Name]s` of :t:`[item]s` within :t:`[external block]s`.
- ownership-and-deconstruction.rst:221: :t:`by move` passing within the enclosing :t:`item`.
- ownership-and-deconstruction.rst:243: :t:`by move` passing within the enclosing :t:`item`.
- attributes.rst:51: :t:`item`.
- attributes.rst:55: :t:`item`.
- attributes.rst:80: An :dt:`active attribute` is an :t:`attribute` that is removed from the :t:`item`
- attributes.rst:84: An :dt:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
- attributes.rst:1635: :t:`[item]s` in the :t:`crate`.
- types-and-traits.rst:1391: A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.
- types-and-traits.rst:2749: A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can

## layout (layout)
- types-and-traits.rst:1481: For :t:`type` :c:`str`, the :t:`layout` is that of :t:`slice type`
- types-and-traits.rst:1490: For a :t:`slice type`, the :t:`layout` is that of the :t:`array type` it slices.
- types-and-traits.rst:1493: For a :t:`tuple type`, the :t:`layout` is tool-defined. For a :t:`unit tuple`,
- types-and-traits.rst:1497: For a :t:`closure type`, the :t:`layout` is tool-defined.
- types-and-traits.rst:1513: For a :t:`trait object type`, the :t:`layout` is the same as the :t:`value`
- types-and-traits.rst:1536: :dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
- types-and-traits.rst:1539: does not change the :t:`layout` of the :t:`[field]s` themselves.
- types-and-traits.rst:1561: :dt:`Default representation` makes no guarantees about the :t:`layout`.
- ffi.rst:16: and :t:`type` :t:`layout` to interface a Rust program with foreign code.

## let binding (let_binding)
- patterns.rst:73: :t:`closure parameter`, a :t:`function parameter`, or a :t:`let binding`.

## local variable (local_variable)
- No :t: references found in src/*.rst

## loop (loop)
- No :t: references found in src/*.rst

## macro repetition in matching (macro_repetition_in_matching)
- macros.rst:237: A :t:`macro repetition in matching` allows for a syntactic pattern to be matched
- macros.rst:245: A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
- macros.rst:250: of times a :t:`macro repetition in matching` or a
- macros.rst:931: Each matched :t:`metavariable` in a :t:`macro repetition in matching` is bound
- macros.rst:1061: where the :t:`metavariable` of the :t:`macro repetition in matching` are
- macros.rst:1066: :t:`macro repetition in matching`, the second :t:`metavariable` argument with

## mixed site hygiene (mixed_site_hygiene)
- macros.rst:1097: :t:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
- macros.rst:1106: :t:`[Declarative macro]s` have :t:`mixed site hygiene`.
- macros.rst:1110: :t:`mixed site hygiene` depending on the implementation of the

## multiplication assignment (multiplication_assignment)
- expressions.rst:2677: The :t:`type` of the :t:`assigned operand` of a :t:`multiplication assignment`
- expressions.rst:2759: For a :t:`multiplication assignment`,

## mutable assignee expression (mutable_assignee_expression)
- expressions.rst:2643: An :t:`assigned operand` shall denote a :t:`mutable assignee expression`.

## mutable binding (mutable_binding)
- patterns.rst:163: with :t:`keyword` ``mut`` yields a :t:`mutable binding`.
- patterns.rst:858: :t:`mutable binding`.

## mutable variable (mutable_variable)
- expressions.rst:452: A :t:`path expression` that resolves to a :t:`mutable variable` that is not

## named field selector (named_field_selector)
- entities-and-resolution.rst:1286: the characters of a :t:`named field selector`.
- entities-and-resolution.rst:1308: :t:`named field selector` proceeds as follows:

## NaN-boxing (nan_boxing)
- inline-assembly.rst:584: ``freg``, then :c:`f32` :t:`[value]s` are :t:`NaN-boxed <NaN-boxing>`. in a

## numeric type (numeric_type)
- entities-and-resolution.rst:862: :t:`[Numeric type]s`,
- expressions.rst:2165: An :t:`operand` of a :t:`numeric type` and a target :t:`numeric type` perform
- expressions.rst:2165: An :t:`operand` of a :t:`numeric type` and a target :t:`numeric type` perform
- types-and-traits.rst:82: :t:`[Numeric type]s`
- types-and-traits.rst:2622: :t:`numeric type`, :t:`unify` the :t:`[type]s` of both :t:`[operand]s` with

## object safety (object_safety)
- No :t: references found in src/*.rst

## place (place)
- expressions.rst:2409: into the :t:`place` of the :t:`assignee operand`.
- expressions.rst:2507: into the :t:`place` of the :t:`assignee operand`.
- ownership-and-deconstruction.rst:268: transferred between :t:`[place]s`.
- ownership-and-deconstruction.rst:308: shall not be :t:`passed <passing convention>` between :t:`[place]s`.
- patterns.rst:1238: :t:`value` by :t:`passing <passing convention>` the :t:`value` to the :t:`place`

## pointer (pointer)
- expressions.rst:2212: produces a :t:`pointer` that interprets the integer as a machine address.
- patterns.rst:581: A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer` that

## pointer type (pointer_type)
- types-and-traits.rst:431: :t:`pointer type`, and is at least 16-bits wide.
- types-and-traits.rst:466: :t:`pointer type`, and is at least 16-bits wide.

## prelude entity (prelude_entity)
- entities-and-resolution.rst:943: :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
- entities-and-resolution.rst:943: :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`

## prelude name (prelude_name)
- entities-and-resolution.rst:944: is referred to as a :t:`prelude name`.
- entities-and-resolution.rst:1190: :t:`[Prelude name]s`,
- entities-and-resolution.rst:1199: A :t:`prelude name` shadows other :t:`[prelude name]s` depending on which
- entities-and-resolution.rst:1199: A :t:`prelude name` shadows other :t:`[prelude name]s` depending on which
- entities-and-resolution.rst:1201: follows, where a later :t:`prelude name` shadows earlier :t:`prelude name`:
- entities-and-resolution.rst:1201: follows, where a later :t:`prelude name` shadows earlier :t:`prelude name`:
- entities-and-resolution.rst:1204: :t:`Language prelude` :t:`names <prelude name>`.
- entities-and-resolution.rst:1207: Standard library :t:`prelude` :t:`names <prelude name>`.
- entities-and-resolution.rst:1210: :t:`macro_use prelude` :t:`names <prelude name>`.
- entities-and-resolution.rst:1213: Tool :t:`prelude` :t:`names <prelude name>`.
- entities-and-resolution.rst:1216: :t:`External prelude` :t:`names <prelude name>`.

## principal trait (principal_trait)
- types-and-traits.rst:1217: The :t:`principal trait` of :t:`trait object type` is the first :t:`trait bound`.
- types-and-traits.rst:1224: The :t:`principal trait` shall denote an :t:`object safe` :t:`trait`.
- types-and-traits.rst:1227: All non-:t:`principal trait` :t:`[trait bound]s` shall denote :t:`[auto trait]s`.
- types-and-traits.rst:2068: The source :t:`type` is a :t:`trait object type` and the target :t:`type` is a :t:`trait object type` with the same or no :t:`principal trait`, and the target :t:`type` has the same or less non-:t:`principal trait` :t:`[trait bound]s`.
- types-and-traits.rst:2068: The source :t:`type` is a :t:`trait object type` and the target :t:`type` is a :t:`trait object type` with the same or no :t:`principal trait`, and the target :t:`type` has the same or less non-:t:`principal trait` :t:`[trait bound]s`.
- types-and-traits.rst:2071: The source :t:`type` is a :t:`trait object type` with some :t:`principal trait` ``T``
- types-and-traits.rst:2072: and the target :t:`type` is a :t:`trait object type` with some :t:`principal trait` ``U``,

## punctuator (punctuator)
- lexical-elements.rst:267: Each of the special characters listed for single character :t:`punctuator`
- lexical-elements.rst:273: The following names are used when referring to :t:`[punctuator]s`:

## raw pointer (raw_pointer)
- expressions.rst:1035: A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
- expressions.rst:1044: When the :t:`operand` of a :t:`raw borrow expression` is a :t:`place expression`, the :t:`raw borrow expression` produces a :t:`raw pointer` to the memory location indicated by the :t:`operand`.
- expressions.rst:1107: Dereferencing a :t:`raw pointer` shall require :t:`unsafe context` unless the :t:`dereference expression` is the :t:`operand` of a :t:`raw borrow expression`.
- expressions.rst:1151: It is undefined behavior to dereference a :t:`raw pointer` that is either

## reachable control flow path (reachable_control_flow_path)
- values.rst:266: :t:`[reachable control flow path]s` up to the point of its usage.

## record enum variant (record_enum_variant)
- expressions.rst:3267: If the :t:`constructee` is a :t:`record enum variant` or a :t:`record struct`,
- patterns.rst:882: :t:`record enum variant` or a :t:`record struct`, then

## record struct (record_struct)
- expressions.rst:3267: If the :t:`constructee` is a :t:`record enum variant` or a :t:`record struct`,
- patterns.rst:882: :t:`record enum variant` or a :t:`record struct`, then

## record struct field (record_struct_field)
- types-and-traits.rst:782: The :t:`name` of a :t:`record struct field` shall be unique within the
- types-and-traits.rst:786: If the :t:`type` of a :t:`record struct field` is a :t:`dynamically sized type`,
- types-and-traits.rst:787: then the :t:`record struct field` shall be the last :t:`record struct field` in
- types-and-traits.rst:787: then the :t:`record struct field` shall be the last :t:`record struct field` in

## record struct type (record_struct_type)
- No :t: references found in src/*.rst

## record struct value (record_struct_value)
- No :t: references found in src/*.rst

## reference identifier pattern (reference_identifier_pattern)
- ownership-and-deconstruction.rst:604: A :t:`reference identifier pattern`, or
- patterns.rst:167: :t:`reference identifier pattern`.

## refutable type (refutable_type)
- patterns.rst:117: A :dt:`refutable constant` is a :t:`constant` of a :t:`refutable type`.

## remainder assignment (remainder_assignment)
- expressions.rst:2683: The :t:`type` of the :t:`assigned operand` of a :t:`remainder assignment` shall
- expressions.rst:2764: For a :t:`remainder assignment`,

## representation modifier (representation_modifier)
- types-and-traits.rst:1588: :t:`[representation modifier]s`. A :t:`representation modifier` shall apply only
- types-and-traits.rst:1588: :t:`[representation modifier]s`. A :t:`representation modifier` shall apply only

## rustc (rustc)
- general.rst:51: Rust programming language, as implemented by the Rust compiler (:t:`rustc`),
- general.rst:55: of :t:`rustc` over claiming correctness as a specification.

## safety invariant (safety_invariant)
- attributes.rst:871: It is a :t:`safety invariant` for the :t:`function body` to respect the :t:`ABI` of the function.
- attributes.rst:874: It is a :t:`safety invariant` for the :t:`function body` to :t:`diverge <diverging expression>`.
- types-and-traits.rst:571: It is a :t:`safety invariant` for a :t:`value` of :t:`type` :c:`str` to denote

## scope hierarchy (scope_hierarchy)
- entities-and-resolution.rst:660: The :t:`scope hierarchy` reflects the nesting of :t:`[scope]s` as introduced
- entities-and-resolution.rst:667: into the :t:`scope hierarchy`. The following :t:`[construct]s` are
- entities-and-resolution.rst:726: :t:`scope hierarchy`.
- entities-and-resolution.rst:730: :t:`scope hierarchy`.
- entities-and-resolution.rst:735: :t:`scope hierarchy`.
- entities-and-resolution.rst:739: :t:`generic parameter scope` into the :t:`scope hierarchy`.
- entities-and-resolution.rst:743: :t:`generic parameter scope` into the :t:`scope hierarchy`.
- entities-and-resolution.rst:747: :t:`scope hierarchy`.
- entities-and-resolution.rst:752: :t:`scope hierarchy`.
- entities-and-resolution.rst:756: :t:`scope hierarchy`.
- entities-and-resolution.rst:760: :t:`binding scope` and a :t:`label scope` into the :t:`scope hierarchy`.
- entities-and-resolution.rst:764: :t:`label scope` into the :t:`scope hierarchy`.
- entities-and-resolution.rst:768: :t:`scope hierarchy`.
- entities-and-resolution.rst:772: :t:`scope hierarchy`.
- entities-and-resolution.rst:777: :t:`scope hierarchy`.
- entities-and-resolution.rst:781: and a :t:`Self scope` into the :t:`scope hierarchy`.
- entities-and-resolution.rst:785: :t:`scope hierarchy`.
- entities-and-resolution.rst:793: :t:`scope hierarchy`.
- entities-and-resolution.rst:798: :t:`scope hierarchy`.
- entities-and-resolution.rst:1509: :t:`[textual macro scope]s`, followed by examining the :t:`scope hierarchy`

## sequence type (sequence_type)
- types-and-traits.rst:91: :t:`[Sequence type]s`
- types-and-traits.rst:491: An :dt:`array type` is a :t:`sequence type` that represents a fixed sequence
- types-and-traits.rst:531: A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
- types-and-traits.rst:558: :c:`Str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit unsigned
- types-and-traits.rst:595: A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list

## shared borrow (shared_borrow)
- expressions.rst:1885: A :t:`comparison expression` implicitly takes :t:`[shared borrow]s` of its

## shared reference (shared_reference)
- types-and-traits.rst:1085: :t:`trait`. Copying a :t:`shared reference` performs a shallow copy.
- types-and-traits.rst:1088: Releasing a :t:`shared reference` has no effect on the :t:`value` it refers to.

## shift left assignment (shift_left_assignment)
- expressions.rst:2688: The :t:`type` of the :t:`assigned operand` of a :t:`shift left assignment` shall
- expressions.rst:2769: For a :t:`shift left assignment`,

## shift right assignment (shift_right_assignment)
- expressions.rst:2693: The :t:`type` of the :t:`assigned operand` of a :t:`shift right assignment`
- expressions.rst:2774: For a :t:`shift right assignment`,

## signed integer type (signed_integer_type)
- expressions.rst:1508: :t:`[signed integer type]s`, or floating-point addition for
- expressions.rst:1530: :t:`[signed integer type]s`, or floating-point division for
- expressions.rst:1559: multiplication for :t:`[signed integer type]s`, or floating-point
- expressions.rst:1582: :t:`[signed integer type]s`, or floating-point division for
- expressions.rst:1611: subtraction for :t:`[signed integer type]s`, or floating-point subtraction
- expressions.rst:1823: :t:`signed integer type` and is negative, then vacated bits are filled
- types-and-traits.rst:434: :t:`[Signed integer type]s` define the following inclusive ranges over the

## sized type (sized_type)
- types-and-traits.rst:2076: An :dt:`unsized coercion` is a :t:`type coercion` that converts a :t:`sized type`

## slice (slice)
- patterns.rst:696: and :t:`[slice]s` of dynamic size.
- patterns.rst:705: A :t:`slice`, where the :s:`PatternList` consists of a single
- types-and-traits.rst:558: :c:`Str` is a :t:`sequence type` that represents a :t:`slice` of 8-bit unsigned
- types-and-traits.rst:1510: For a :t:`fat pointer type` whose contained :t:`type` is that of a :t:`slice` or :t:`trait object type` the :t:`size` is that of two times the size of :t:`type` :c:`usize` and the :t:`alignment` is that of :t:`type` :c:`usize`.

## statement (statement)
- macros.rst:552: as a :t:`statement`.
- macros.rst:656: If the :t:`macro invocation` appears as part of a :t:`statement`, the
- macros.rst:657: output is required to constitute zero or more :t:`[statement]s`.
- macros.rst:705: If the :t:`macro invocation` appears as part of a :t:`statement`, the
- macros.rst:706: output is required to constitute zero or more :t:`[statement]s`.
- macros.rst:875: :t:`Fragment specifier` **stmt** requires a :t:`statement` without trailing
- statements.rst:28: An :dt:`item statement` is a :t:`statement` that is expressed as an :t:`item`.
- statements.rst:31: An :dt:`empty statement` is a :t:`statement` expressed as character 0x3B
- statements.rst:35: A :dt:`macro statement` is a :t:`statement` expressed as a
- statements.rst:41: :dt:`Execution` is the process by which a :t:`statement` achieves its runtime
- statements.rst:65: A :dt:`let statement` is a :t:`statement` that introduces new :t:`[binding]s`
- expressions.rst:671: and :t:`[statement]s`.
- expressions.rst:724: Each :t:`statement` is executed in declarative order.
- expressions.rst:2471: The first :t:`statement` is a :t:`let statement` with its :t:`pattern`
- expressions.rst:2477: :t:`assignment expression` used as a :t:`statement`, as follows:
- ownership-and-deconstruction.rst:484: :t:`[Statement]s`.
- ownership-and-deconstruction.rst:505: The parent :t:`drop scope` of a :t:`statement` is the :t:`drop scope` of the
- ownership-and-deconstruction.rst:506: :t:`block expression` that contains the :t:`statement`.
- ownership-and-deconstruction.rst:562: The :t:`drop scope` of a :t:`statement`.
- inline-assembly.rst:1746: A :t:`label block` does not propagate its :t:`[unsafe context]` to its contained :t:`[statement]s`.
- types-and-traits.rst:2403: Recursively process all :t:`[expression]s` and :t:`[statement]s` in the
- types-and-traits.rst:2407: For each :t:`statement`, apply the :t:`statement` inference rules outlined below.
- types-and-traits.rst:2407: For each :t:`statement`, apply the :t:`statement` inference rules outlined below.
- types-and-traits.rst:2435: The :t:`type inference` rules for :t:`[statement]s` are as follows:
- types-and-traits.rst:3177: :t:`[Expression]s` and :t:`[statement]s` may impose :t:`subtyping` requirements
- types-and-traits.rst:3186: The :t:`subtyping` requirements for :t:`[statement]s` are as follows:

## struct (struct)
- entities-and-resolution.rst:917: :t:`Struct` constructors.
- generics.rst:69: A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.
- expressions.rst:3188: A :dt:`constructee` indicates the :t:`enum variant`, :t:`struct`, or :t:`union`
- patterns.rst:408: A :t:`struct` where the :t:`[type]s` of all :t:`[field]s` are
- types-and-traits.rst:1641: Each :t:`enum variant` corresponds to a :t:`struct` whose :t:`struct type` is

## struct field (struct_field)
- entities-and-resolution.rst:927: :t:`[Struct field]s`,
- types-and-traits.rst:2108: ``last_field`` is a :t:`struct field` of ``S``,
- types-and-traits.rst:2116: ``T`` is not part of any other :t:`struct field` of ``S``.

## struct value (struct_value)
- expressions.rst:3185: :t:`enum value`, a :t:`struct value`, or a :t:`union value`.
- expressions.rst:3193: a :t:`struct value` to be used as a base for
- expressions.rst:3264: :t:`struct value`, or :t:`union value` in construction.
- patterns.rst:748: :t:`struct value`, or a :t:`union value`.
- patterns.rst:818: :t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

## subexpression (subexpression)
- expressions.rst:387: diverging :t:`subexpression` on all reachable control flow paths.
- expressions.rst:2435: :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.
- expressions.rst:2448: :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.
- expressions.rst:2452: :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.
- expressions.rst:2456: :t:`tuple struct pattern` with all the :t:`[subexpression]s` lowered to their
- types-and-traits.rst:3178: on their :t:`[subexpression]s`. Such requirements are applied after

## subtraction assignment (subtraction_assignment)
- expressions.rst:2699: The :t:`type` of the :t:`assigned operand` of a :t:`subtraction assignment`
- expressions.rst:2779: For a :t:`subtraction assignment`,

## subtype (subtype)
- implementations.rst:221: :t:`subtype` of the :t:`type` of the :t:`associated trait constant`.
- implementations.rst:229: :t:`implemented trait` is a :t:`subtype` of the :t:`function signature` of
- types-and-traits.rst:2019: The source :t:`type` is a :t:`subtype` of the target :t:`type`.
- types-and-traits.rst:2057: a :t:`function pointer type` and the source's :t:`function signature` is a :t:`subtype` of the target's :t:`function signature`.
- types-and-traits.rst:2061: :t:`type` is a :t:`function pointer type` and the source's :t:`function signature` is a :t:`subtype` of the target's :t:`function signature`.
- types-and-traits.rst:3063: :dt:`generic type` is a :t:`subtype` of an instantiation of itself with
- types-and-traits.rst:3067: A :dt:`type` is its own :t:`subtype`.
- types-and-traits.rst:3073: :dt:`Covariant` over ``T``, when ``T`` being a :t:`subtype` of ``U`` implies
- types-and-traits.rst:3074: that ``F<T>`` is a :t:`subtype` of ``F<U>``, or
- types-and-traits.rst:3077: :dt:`Contravariant` over ``T``, when ``T`` being a :t:`subtype` of ``U``
- types-and-traits.rst:3078: implies that ``F<U>`` is a :t:`subtype` of ``F<T>``, or
- types-and-traits.rst:3193: :t:`let initializer` (if any) is a :t:`subtype` of the :t:`type` of the
- types-and-traits.rst:3212: :t:`value operand` is a :t:`subtype` of the :t:`type` of its
- types-and-traits.rst:3217: a :t:`subtype` of its :t:`target type`.
- types-and-traits.rst:3221: :t:`[type]s` of its :t:`[argument operand]s` are :t:`[subtype]s` of the
- types-and-traits.rst:3226: a :t:`subtype` of the :t:`return type` of the containing :t:`function` or
- types-and-traits.rst:3230: A :t:`break expression` requires that its :t:`break type` is a :t:`subtype` of

## syntactic category (syntactic_category)
- No :t: references found in src/*.rst

## textual type (textual_type)
- entities-and-resolution.rst:871: :t:`[Textual type]s`,
- entities-and-resolution.rst:978: :t:`[Textual type]s` :c:`char` and :c:`str`.

## thin pointer (thin_pointer)
- types-and-traits.rst:1500: For a :t:`thin pointer`, the :t:`size` and :t:`alignment` are those of :t:`type`
- types-and-traits.rst:1505: a :t:`thin pointer`.
- types-and-traits.rst:1509: are at least those of a :t:`thin pointer`.

## thin pointer type (thin_pointer_type)
- No :t: references found in src/*.rst

## tokens (token)
- macros.rst:28: :t:`[Token]s` are a subset of :t:`[lexical element]s` consumed by :t:`[macro]s`.
- macros.rst:142: :t:`[Declarative macro]s` employ :t:`[metavariable]s` to match a :t:`token` of
- macros.rst:159: :dt:`[fragment specifier restriction]s` on the :t:`[token]s` that follow them:
- macros.rst:313: streams of :t:`[token]s` and produce a stream of :t:`[token]s`.
- macros.rst:313: streams of :t:`[token]s` and produce a stream of :t:`[token]s`.
- macros.rst:336: :t:`[token]s` and produces a stream of :t:`[token]s`.
- macros.rst:336: :t:`[token]s` and produces a stream of :t:`[token]s`.
- macros.rst:367: :t:`token` stream produced from the :s:`DelimitedTokenTree` of the
- macros.rst:388: :t:`[token]s` and produces a stream of :t:`[token]s`. :t:`[Derive macro]s` are
- macros.rst:388: :t:`[token]s` and produces a stream of :t:`[token]s`. :t:`[Derive macro]s` are
- macros.rst:420: the :t:`token` stream produced from the related :s:`EnumDeclaration`,
- macros.rst:450: of :t:`[token]s` to produce a single stream of :t:`[token]s`, and defines a
- macros.rst:450: of :t:`[token]s` to produce a single stream of :t:`[token]s`, and defines a
- macros.rst:490: captures the :t:`token` stream produced from the :s:`DelimitedTokenTree`
- macros.rst:492: :s:`DelimitedTokenTree` is provided, then the :t:`token` stream is considered
- macros.rst:497: captures the :t:`token` stream produced from the related :t:`item`, including
- macros.rst:808: :t:`[token]s`, in left-to-right order. Matching does not employ lookahead.
- macros.rst:812: having consumed at least one :t:`token` while parsing the :t:`metavariable`.
- macros.rst:838: :t:`[token]s` in the :t:`macro invocation` based on its :t:`fragment specifier`:
- macros.rst:889: Once a :t:`metavariable` is matched, the matching sequence of :t:`[token]s` is
- macros.rst:920: Once a :t:`metavariable` is matched, the matching sequence of :t:`[token]s` is
- macros.rst:924: The matching sequence of :t:`[token]s` is stored in an ordered collection at
- macros.rst:935: Any other :t:`token` in a :t:`macro matcher` is matched literally against the
- macros.rst:940: leftover :t:`[token]s` after :t:`macro matching`.
- macros.rst:959: the matched sequence of :t:`[token]s` of the :t:`metavariable`.
- macros.rst:962: Unresolved :t:`[metavariable indication]s` are kept as :t:`[token]s` in the
- macros.rst:968: repeatedly transcribing the :t:`[token]s` inside of it.
- macros.rst:1009: replaced with the matched sequence of :t:`[token]s` of the corresponding
- macros.rst:1014: be transcribed to the matched :t:`[token]s` in order, as follows:

## trait type (trait_type)
- types-and-traits.rst:139: :t:`[Trait type]s`

## tuple (tuple)
- expressions.rst:3110: A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
- expressions.rst:3459: ``argument_operand_tuple`` is a :t:`tuple` that wraps the
- expressions.rst:3467: ``argument_operand_tuple`` is a :t:`tuple` that wraps the
- expressions.rst:3475: ``argument_operand_tuple`` is a :t:`tuple` that wraps the
- patterns.rst:1111: A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which satisfies
- patterns.rst:1119: The :t:`type` of a :t:`tuple pattern` is the :t:`type` of the :t:`tuple` being

## tuple enum variant (tuple_enum_variant)
- expressions.rst:627: :t:`constant`, a :t:`function`, a :t:`static`, a :t:`tuple enum variant`, a
- expressions.rst:3288: If the :t:`constructee` is a :t:`tuple enum variant` or a :t:`tuple struct`,
- expressions.rst:3424: :t:`function pointer type`, a :t:`tuple enum variant`, a
- expressions.rst:3431: :t:`function`, the :t:`type` of the :t:`tuple enum variant` or the
- expressions.rst:3449: If the :t:`callee type` is a :t:`tuple enum variant` or a
- expressions.rst:3451: the :t:`tuple enum variant` or the :t:`tuple struct` with the
- patterns.rst:181: to a :t:`tuple struct` or a :t:`tuple enum variant`.
- patterns.rst:903: :t:`tuple enum variant` or a :t:`tuple struct type`, then
- patterns.rst:1034: :t:`tuple enum variant` or a :t:`tuple struct type`.

## tuple enum variant value (tuple_enum_variant_value)
- expressions.rst:3403: constructs a :t:`tuple enum variant value` or a :t:`tuple struct value`.
- expressions.rst:3411: :t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
- patterns.rst:1030: :t:`tuple enum variant value`, or a :t:`tuple struct value`.

## tuple field (tuple_field)
- expressions.rst:3114: :t:`tuple field` in a :t:`tuple expression`.
- patterns.rst:1123: A :t:`subpattern` of a :t:`tuple pattern` matches a :t:`tuple field` of the
- patterns.rst:1124: :t:`tuple type` when its position and the position of the :t:`tuple field` in
- patterns.rst:1150: :t:`type` of the matched :t:`tuple field` shall be :t:`unifiable`.
- patterns.rst:1153: For each :t:`tuple field` of the :t:`tuple type`, the :t:`tuple pattern` shall
- patterns.rst:1163: A :s:`RestPattern` is allowed even if all :t:`[tuple field]s` of the
- types-and-traits.rst:599: The :dt:`arity` of a :t:`tuple type` is the number of :t:`[tuple field]s` in its
- types-and-traits.rst:603: If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
- types-and-traits.rst:604: the :t:`tuple field` shall be the last :t:`tuple field` in the
- types-and-traits.rst:604: the :t:`tuple field` shall be the last :t:`tuple field` in the
- types-and-traits.rst:852: A :t:`tuple type` whose :t:`[tuple field]s`' :t:`[type]s` are all valid
- types-and-traits.rst:1857: The :t:`[type]s` of the corresponding :t:`[tuple field]s` are unifiable.
- types-and-traits.rst:2211: :t:`[Tuple type]s`, if the :t:`[type]s` of the :t:`[tuple field]s` are

## tuple struct (tuple_struct)
- expressions.rst:247: :t:`[static]s`, :t:`[tuple struct]s`, and  :t:`[unit struct]s`,
- expressions.rst:628: :t:`tuple struct`, a :t:`unit enum variant`, a :t:`unit struct`, or a
- expressions.rst:3288: If the :t:`constructee` is a :t:`tuple enum variant` or a :t:`tuple struct`,
- expressions.rst:3420: :t:`call operand` resolves to a :t:`tuple struct`.
- expressions.rst:3432: :t:`tuple struct` being constructed, or :t:`associated type`
- expressions.rst:3451: the :t:`tuple enum variant` or the :t:`tuple struct` with the
- patterns.rst:181: to a :t:`tuple struct` or a :t:`tuple enum variant`.

## tuple struct field (tuple_struct_field)
- types-and-traits.rst:791: If the :t:`type` of a :t:`tuple struct field` is a :t:`dynamically sized type`,
- types-and-traits.rst:792: then the :t:`tuple struct field` shall be the last :t:`tuple struct field` in
- types-and-traits.rst:792: then the :t:`tuple struct field` shall be the last :t:`tuple struct field` in

## tuple struct type (tuple_struct_type)
- expressions.rst:3425: :t:`tuple struct type`, or a :t:`type` that implements any of the
- expressions.rst:3450: :t:`tuple struct type`, then the :t:`value` is the result of constructing
- patterns.rst:903: :t:`tuple enum variant` or a :t:`tuple struct type`, then
- patterns.rst:1034: :t:`tuple enum variant` or a :t:`tuple struct type`.

## tuple struct value (tuple_struct_value)
- expressions.rst:3403: constructs a :t:`tuple enum variant value` or a :t:`tuple struct value`.
- expressions.rst:3411: :t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
- patterns.rst:1030: :t:`tuple enum variant value`, or a :t:`tuple struct value`.

## type ascription (type_ascription)
- statements.rst:87: If the :t:`let statement` lacks a :t:`type ascription` and a :t:`let initializer`, then the :t:`expected type` is the :t:`inferred type`.
- statements.rst:90: If the :t:`let statement` lacks a :t:`type ascription`, then the :t:`expected type` is the :t:`type` of the :t:`let initializer`.
- statements.rst:93: Otherwise the :t:`expected type` is the :t:`type` specified by the :t:`type ascription`.
- statements.rst:100: If the :t:`let statement` appears with a :t:`type ascription`, then the
- statements.rst:101: :t:`type` is the :t:`type` specified by the :t:`type ascription`.
- statements.rst:104: If the :t:`let statement` lacks a :t:`type ascription`, then the :t:`type` is
- types-and-traits.rst:2317: The :t:`expected type` of a :t:`constant argument` is the :t:`type ascription`
- types-and-traits.rst:2322: is the :t:`type` specified by the :t:`type ascription` of the related
- types-and-traits.rst:2327: the :t:`type` specified by the :t:`type ascription` of the related
- types-and-traits.rst:2450: If the :t:`let statement` has a :t:`type ascription`, :t:`unify` that
- types-and-traits.rst:2697: :t:`[pattern]s` and :t:`[type ascription]s` and return :t:`type`, and then
- types-and-traits.rst:3375: the :t:`type ascription` of :t:`[constant]s` and :t:`[static]s`.

## type specification (type_specification)
- associated-items.rst:164: A :t:`type specification` resolving to the :t:`implementing type` of the
- entities-and-resolution.rst:360: A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
- entities-and-resolution.rst:526: within the related :t:`type specification`.
- entities-and-resolution.rst:686: :t:`Function pointer type` :t:`specifications <type specification>`,
- entities-and-resolution.rst:742: The :t:`type specification` of a :t:`function pointer type` introduces a
- implementations.rst:245: The :t:`type specification` of the :t:`associated type` of the
- macros.rst:355: It shall have a single :t:`function parameter` whose :t:`type specification`
- macros.rst:359: It shall have a :t:`return type` whose :t:`type specification` indicates
- macros.rst:408: It shall have a single :t:`function parameter` whose :t:`type specification`
- macros.rst:412: It shall have a :t:`return type` whose :t:`type specification` indicates
- macros.rst:472: It shall have two :t:`[function parameter]s` whose :t:`[type specification]s`
- macros.rst:476: It shall have a :t:`return type` whose :t:`type specification` indicates type
- macros.rst:661: :t:`type specification` without :t:`[bound]s`, the output is required to
- macros.rst:710: :t:`type specification` without :t:`[bound]s`, the output is required to
- macros.rst:883: :t:`Fragment specifier` **ty** requires a :t:`type specification`.
- values.rst:102: The :t:`type specification` of a :t:`constant` shall have ``'static``
- values.rst:166: The :t:`type specification` of a :t:`static` shall have ``'static``
- types-and-traits.rst:1426: A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
- types-and-traits.rst:1993: A :t:`let statement` with an explicit :t:`type specification`.
- types-and-traits.rst:3379: :t:`type specification` of a :t:`constant` or :t:`static` is inferred to be the
- types-and-traits.rst:3420: If the :t:`trait object type` is used as the :t:`type specification` of a

## unary operator (unary_operator)
- No :t: references found in src/*.rst

## undefined behavior (undefined_behavior)
- unsafety.rst:19: :t:`undefined behavior` that is not diagnosed as a static error.

## Unicode (unicode)
- lexical-elements.rst:25: The program text of a Rust program is written using the :t:`Unicode` character
- lexical-elements.rst:32: described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
- lexical-elements.rst:32: described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
- lexical-elements.rst:36: In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
- lexical-elements.rst:40: In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
- lexical-elements.rst:84: An :ds:`AsciiCharacter` is any :t:`Unicode` character in the range 0x00 - 0x7F, both inclusive.
- lexical-elements.rst:487: #31 for :t:`Unicode` version 16.0, with the following profile:
- lexical-elements.rst:758: A :dt:`simple c string literal` is any :t:`Unicode` character except characters
- lexical-elements.rst:766: :t:`Unicode` characters.
- lexical-elements.rst:1123: A :ds:`CharacterLiteralCharacter` is any :t:`Unicode` character except
- lexical-elements.rst:1130: It can represent any :t:`Unicode` codepoint between U+00000 and U+10FFFF,
- lexical-elements.rst:1131: inclusive, except :t:`Unicode` surrogate codepoints, which exist between
- lexical-elements.rst:1137: A :dt:`character literal` is a :t:`literal` that denotes a fixed :t:`Unicode`
- lexical-elements.rst:1193: A :ds:`SimpleStringCharacter` is any :t:`Unicode` character except characters
- lexical-elements.rst:1204: :t:`Unicode` characters.
- types-and-traits.rst:359: of :t:`Unicode`.
- types-and-traits.rst:366: :t:`Unicode`.

## unifiable (unifiable)
- generics.rst:441: are :t:`unifiable`.
- expressions.rst:2921: shall be :t:`unifiable`.
- expressions.rst:3213: :t:`type` of the matched :t:`field` shall be :t:`unifiable`.
- expressions.rst:3230: :t:`field` shall be :t:`unifiable`.
- expressions.rst:3252: :t:`field` shall be :t:`unifiable`.
- expressions.rst:3624: corresponding :t:`function parameter` or :t:`field` shall be :t:`unifiable`.
- expressions.rst:4409: :t:`[operand]s` shall be :t:`unifiable`.
- expressions.rst:4549: :t:`else expression` shall be :t:`unifiable`.
- expressions.rst:4619: :t:`else expression` shall be :t:`unifiable`.
- expressions.rst:4742: :t:`[pattern]s` of all :t:`[match arm matcher]s` shall be :t:`unifiable`.
- expressions.rst:4750: :t:`unifiable`.
- patterns.rst:81: :t:`unifiable`.
- patterns.rst:530: :t:`range pattern high bound` of a :t:`range pattern` shall be :t:`unifiable`.
- patterns.rst:836: matched :t:`field` shall be :t:`unifiable`.
- patterns.rst:849: matched :t:`field` shall be :t:`unifiable`.
- patterns.rst:878: matched :t:`field` shall be :t:`unifiable`.
- patterns.rst:1064: :t:`type` of the matched :t:`field` shall be :t:`unifiable`.
- patterns.rst:1150: :t:`type` of the matched :t:`tuple field` shall be :t:`unifiable`.

## unified type (unified_type)
- expressions.rst:686: has a :t:`tail expression`, then the :t:`type` is the :t:`unified type` of
- expressions.rst:692: :t:`break expression`, then the :t:`type` is the :t:`unified type` of the
- expressions.rst:3998: :t:`break expression`, then the :t:`type` is the :t:`unified type` of the
- expressions.rst:4753: The :t:`type` of a :t:`match expression` is the :t:`unified type` of the
- patterns.rst:538: :t:`type` is the :t:`unified type` of the :t:`[type]s` of the

## union (union)
- generics.rst:78: A :dt:`generic union` is a :t:`union` with :t:`[generic parameter]s`.
- unsafety.rst:35: Accessing a :t:`field` of a :t:`union`, other than to assign to it.
- expressions.rst:3188: A :dt:`constructee` indicates the :t:`enum variant`, :t:`struct`, or :t:`union`
- expressions.rst:3682: Reading the :t:`selected field` of a :t:`union` shall require
- expressions.rst:3686: Writing to the :t:`selected field` of a :t:`union` where the :t:`type` of the
- expressions.rst:3691: Writing to and then reading from the :t:`selected field` of a :t:`union`
- types-and-traits.rst:832: A :t:`union` without any :t:`[union field]s` is rejected, but may still be consumed by

## union field (union_field)
- entities-and-resolution.rst:930: :t:`[Union field]s`.
- types-and-traits.rst:832: A :t:`union` without any :t:`[union field]s` is rejected, but may still be consumed by
- types-and-traits.rst:836: The :t:`name` of a :t:`union field` shall be unique within the related
- types-and-traits.rst:840: The :t:`type` of a :t:`union field` shall be either:
- types-and-traits.rst:853: :t:`union field` :t:`[type]s`, or
- types-and-traits.rst:856: An :t:`array type` whose :t:`element type` is a valid :t:`union field`
- types-and-traits.rst:1522: :t:`union type` is subject to :t:`attribute` :c:`repr`. All :t:`[union field]s`

## union value (union_value)
- expressions.rst:3185: :t:`enum value`, a :t:`struct value`, or a :t:`union value`.
- expressions.rst:3264: :t:`struct value`, or :t:`union value` in construction.
- patterns.rst:748: :t:`struct value`, or a :t:`union value`.
- patterns.rst:818: :t:`enum variant value`, a :t:`struct value`, or a :t:`union value`.

## unique immutable reference (unique_immutable_reference)
- expressions.rst:5194: :t:`unique immutable reference` to the :t:`capture target` and passes the

## unit enum variant (unit_enum_variant)
- expressions.rst:628: :t:`tuple struct`, a :t:`unit enum variant`, a :t:`unit struct`, or a
- expressions.rst:3322: If the :t:`constructee` is a :t:`unit enum variant` or a :t:`unit struct`, then
- patterns.rst:172: :t:`unit struct constant` or a :t:`unit enum variant`.
- patterns.rst:177: :t:`unit struct constant`, or a :t:`unit enum variant`.
- patterns.rst:196: a :t:`constant`, a :t:`unit struct constant`, or a :t:`unit enum variant`.
- patterns.rst:366: :t:`unit enum variant`, or a :t:`unit struct constant` indicated by a :t:`path`.
- patterns.rst:413: :t:`unit enum variant`, or :t:`unit struct constant` the :t:`path` resolved to.
- patterns.rst:863: :t:`constant`, a :t:`unit enum variant`, or a :t:`unit struct constant`.
- patterns.rst:946: :t:`unit enum variant` or a :t:`unit struct`, then the
- patterns.rst:1431: If the :t:`constant`, :t:`unit enum variant` or :t:`unit struct` the

## unit struct (unit_struct)
- expressions.rst:247: :t:`[static]s`, :t:`[tuple struct]s`, and  :t:`[unit struct]s`,
- expressions.rst:628: :t:`tuple struct`, a :t:`unit enum variant`, a :t:`unit struct`, or a
- expressions.rst:3322: If the :t:`constructee` is a :t:`unit enum variant` or a :t:`unit struct`, then
- patterns.rst:946: :t:`unit enum variant` or a :t:`unit struct`, then the
- patterns.rst:1431: If the :t:`constant`, :t:`unit enum variant` or :t:`unit struct` the

## unit struct constant (unit_struct_constant)
- patterns.rst:172: :t:`unit struct constant` or a :t:`unit enum variant`.
- patterns.rst:177: :t:`unit struct constant`, or a :t:`unit enum variant`.
- patterns.rst:196: a :t:`constant`, a :t:`unit struct constant`, or a :t:`unit enum variant`.
- patterns.rst:366: :t:`unit enum variant`, or a :t:`unit struct constant` indicated by a :t:`path`.
- patterns.rst:413: :t:`unit enum variant`, or :t:`unit struct constant` the :t:`path` resolved to.
- patterns.rst:863: :t:`constant`, a :t:`unit enum variant`, or a :t:`unit struct constant`.

## unit struct type (unit_struct_type)
- No :t: references found in src/*.rst

## unit struct value (unit_struct_value)
- No :t: references found in src/*.rst

## unit tuple (unit_tuple)
- types-and-traits.rst:1493: For a :t:`tuple type`, the :t:`layout` is tool-defined. For a :t:`unit tuple`,

## unit type (unit_type)
- statements.rst:171: (semicolon) is the :t:`unit type`.
- expressions.rst:700: Otherwise the :t:`type` is the :t:`unit type`.
- expressions.rst:2375: The :t:`type` of an :t:`assignment expression` is the :t:`unit type`.
- expressions.rst:2646: The :t:`type` of a :t:`compound assignment` is the :t:`unit type`.
- expressions.rst:3881: The :t:`type` of the :t:`loop body` shall be the :t:`unit type`.
- expressions.rst:3922: The :t:`type` of a :t:`for loop expression` is the :t:`unit type`.
- expressions.rst:4062: The :t:`type` of a :t:`while loop expression` is the :t:`unit type`.
- expressions.rst:4118: The :t:`type` of a :t:`while let loop expression` is the :t:`unit type`.
- expressions.rst:4235: is the :t:`unit type`.
- functions.rst:150: Otherwise the :t:`return type` is the :t:`unit type`.
- inline-assembly.rst:1743: The type of the :t:`label block` must be :t:`unit type` or :t:`never type`.
- attributes.rst:2287: A :t:`testing function` that returns the :t:`unit type` passes when it
- types-and-traits.rst:1004: Otherwise the :t:`return type` is the :t:`unit type`.
- types-and-traits.rst:2424: unified with a concrete :t:`type`, unify them with the :t:`unit type`.
- types-and-traits.rst:2443: :t:`unit type` if the :t:`expression statement` lacks the character 0x3B
- types-and-traits.rst:2681: The :t:`type` of the :t:`expression` is the :t:`unit type`.

## unit value (unit_value)
- expressions.rst:716: Otherwise the :t:`value` is the :t:`unit value`.
- expressions.rst:2378: The :t:`value` of an :t:`assignment expression` is the :t:`unit value`.
- expressions.rst:2649: The :t:`value` of a :t:`compound assignment` is the :t:`unit value`.
- expressions.rst:3925: The :t:`value` of a :t:`for loop expression` is the :t:`unit value`.
- expressions.rst:4006: then the :t:`value` is the :t:`unit value`.
- expressions.rst:4065: The :t:`value` of a :t:`while loop expression` is the :t:`unit value`.
- expressions.rst:4121: The :t:`value` of a :t:`while let loop expression` is the :t:`unit value`.
- expressions.rst:4250: is the :t:`unit value`.
- expressions.rst:4876: :t:`value` is the :t:`unit value`.

## unnamed lifetime (unnamed_lifetime)
- No :t: references found in src/*.rst

## unsafe block (unsafe_block)
- unsafety.rst:44: An :dt:`unsafe context` is either an :t:`unsafe block` or an
- attributes.rst:540: can only be called without an :t:`unsafe block` by a caller that is within a function

## unsafe Rust (unsafe_rust)
- unsafety.rst:20: :t:`[Unsafe operation]s` are referred to as :t:`unsafe Rust`.

## unsafe trait (unsafe_trait)
- implementations.rst:81: only if it implements an :t:`unsafe trait`.

## unsigned integer type (unsigned_integer_type)
- expressions.rst:1507: for :t:`[unsigned integer type]s`, two's complement addition for
- expressions.rst:1529: division for :t:`[unsigned integer type]s`, two's complement division for
- expressions.rst:1558: integer multiplication for :t:`[unsigned integer type]s`, two's complement
- expressions.rst:1581: :t:`[unsigned integer type]s`, two's complement division for
- expressions.rst:1610: integer subtraction for :t:`[unsigned integer type]s`, two's complement
- types-and-traits.rst:399: :t:`[Unsigned integer type]s` define the following inclusive ranges over the

## unsized type (unsized_type)
- types-and-traits.rst:2077: into an :t:`unsized type`. :t:`Unsized coercion` from a source :t:`type` to a

## use import (use_import)
- entities-and-resolution.rst:330: If a :t:`simple path` appears in a :t:`use import` and starts with a
- entities-and-resolution.rst:337: If a :t:`simple path` appears in a :t:`use import` and starts with a
- entities-and-resolution.rst:1020: A :t:`use import` brings :t:`entities <entity>` :t:`in scope` within the
- entities-and-resolution.rst:1022: :t:`use import` resides.
- entities-and-resolution.rst:1030: :t:`use import`. An :t:`import path prefix` for a given
- entities-and-resolution.rst:1037: If the :t:`use import` is a :t:`simple import` then start with the
- entities-and-resolution.rst:1042: If the :t:`use import` is a :t:`glob import` then start with the
- entities-and-resolution.rst:1046: If the :t:`use import` is a :t:`nesting import` then start with the
- entities-and-resolution.rst:1050: Then if the current :t:`use import` is the child of a :t:`nesting import`,
- entities-and-resolution.rst:1053: the current :t:`use import`.
- entities-and-resolution.rst:1056: A :dt:`simple import` is a :t:`use import` that brings all :t:`entities <entity>`
- entities-and-resolution.rst:1061: A :dt:`glob import` is a :t:`use import` that brings all :t:`entities <entity>`
- entities-and-resolution.rst:1115: A :dt:`nesting import` is a :t:`use import` that provides a common
- entities-and-resolution.rst:1116: :t:`simple path prefix` for its nested :t:`[use import]s`.
- entities-and-resolution.rst:1650: If the :t:`simple path` is part of a :t:`use import`, then the

## validity invariant (validity_invariant)
- types-and-traits.rst:346: It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`bool` to have
- types-and-traits.rst:364: It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
- types-and-traits.rst:716: It is a :t:`validity invariant` for a :t:`value` of an :t:`enum type` to have a
- types-and-traits.rst:1009: It is a :t:`validity invariant` for a :t:`value` of a :t:`function pointer type`
- types-and-traits.rst:1105: It is :t:`validity invariant` for a :t:`value` of a :t:`reference type` to be
- types-and-traits.rst:1340: It is :t:`validity invariant` to not have a :t:`value` of the :t:`never type`.

## visibility modifier (visibility_modifier)
- associated-items.rst:180: The :t:`visibility modifier` of an :t:`associated trait item` or :t:`associated
- entities-and-resolution.rst:155: A :t:`visibility modifier` sets the :t:`visibility` of a :t:`name`.
- entities-and-resolution.rst:158: A :dt:`crate public modifier` is a :t:`visibility modifier` that grants a
- entities-and-resolution.rst:162: A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
- entities-and-resolution.rst:168: A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
- entities-and-resolution.rst:182: A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
- entities-and-resolution.rst:186: A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
- entities-and-resolution.rst:193: :t:`visibility modifier` has :t:`private visibility` by default.
- entities-and-resolution.rst:1655: If the :t:`simple path` is part of a :t:`visibility modifier`, then the
- macros.rst:346: It shall be subject to :t:`visibility modifier` ``pub``,
- macros.rst:399: It shall be subject to :t:`visibility modifier` ``pub``,
- macros.rst:463: It shall be subject to :t:`visibility modifier` ``pub``,

## visible emptiness (visible_emptiness)
- patterns.rst:405: An :t:`enum variant` of an :t:`enum type` with zero or more :t:`[visible empty enum variant]s` and one non-:t:`visible empty enum variant` where the :t:`[type]s` of all :t:`[field]s` are not subject to :t:`visible emptiness`
- patterns.rst:771: An :t:`enum variant` of an :t:`enum type` with zero or more :t:`[visible empty enum variant]s` and one non-:t:`visible empty enum variant` where the :t:`[type]s` of all :t:`[field]s` are not subject to :t:`visible emptiness`.
- types-and-traits.rst:2237: :t:`Visible emptiness <visible emptiness>` is a property of :t:`[type]s` and :t:`[enum variant]s` that have no :t:`[value]s` that are fully observable.
- types-and-traits.rst:2240: A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.
- types-and-traits.rst:2243: A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.
- types-and-traits.rst:2246: A :dt:`type` is subject to :t:`visible emptiness` as follows:
- types-and-traits.rst:2255: The :t:`type` is an :t:`enum type` not subject to :t:`attribute` :c:`non_exhaustive` where all :t:`[enum variant]s` are subject to :t:`visible emptiness`.
- types-and-traits.rst:2258: The :t:`type` is a :t:`struct type` with at least one :t:`visible <visibility>` :t:`field` whose :t:`type` is subject to :t:`visible emptiness`.
- types-and-traits.rst:2261: The :t:`type` is a :t:`tuple type` with at least one of the contained :t:`[type]s` is subject to :t:`visible emptiness`.
- types-and-traits.rst:2264: The :t:`type` is an :t:`array type` with a non-zero :t:`size operand` and an :t:`element type` that is subject to :t:`visible emptiness`.
- types-and-traits.rst:2267: A :dt:`enum variant` is subject to :t:`visible emptiness` when the :t:`type` of at least one of the :t:`enum variant`'s :t:`visible <visibility>` :t:`[field]s` is subject to :t:`visible emptiness`.
- types-and-traits.rst:2267: A :dt:`enum variant` is subject to :t:`visible emptiness` when the :t:`type` of at least one of the :t:`enum variant`'s :t:`visible <visibility>` :t:`[field]s` is subject to :t:`visible emptiness`.

## while let loop (while_let_loop)
- entities-and-resolution.rst:487: The :t:`binding` of a :t:`for loop` or a :t:`while let loop` is :t:`in scope`
- expressions.rst:110: :t:`[if let expression]s` and :t:`[while let loop]s`.

## while loop (while_loop)
- No :t: references found in src/*.rst

## zero-sized type (zero_sized_type)
- No :t: references found in src/*.rst

## zero-variant enum type (zero_variant_enum_type)
- types-and-traits.rst:656: A :t:`zero-variant enum type` has no :t:`[value]s`.
- types-and-traits.rst:1566: :t:`enum type` that is not a :t:`zero-variant enum type`. It is possible to
- types-and-traits.rst:1600: :t:`[Zero-variant enum type]s` shall not be subject to :t:`C representation`.
- types-and-traits.rst:2252: The :t:`type` is a :t:`zero-variant enum type`.

