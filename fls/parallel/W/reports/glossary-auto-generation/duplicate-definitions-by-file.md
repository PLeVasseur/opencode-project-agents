# Duplicate definitions grouped by file

## associated-items.rst
- 158: method -> A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

## entities-and-resolution.rst
- 292: path -> A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
- 299: path -> A :dt:`path` is subject to :t:`path resolution`.
- 321: simple_path -> A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
- 343: simple_path -> A :dt:`simple path` is subject to :t:`simple path resolution`.
- 357: path_expression -> A :dt:`path expression` is subject to :t:`path expression resolution`.
- 360: type_path -> A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
- 363: type_path -> A :dt:`type path` is subject to :t:`type path resolution`.
- 518: generic_parameter -> A :dt:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.
- 557: generic_parameter -> A :dt:`generic parameter` is not :t:`in scope` within nested :t:`[item]s`,
- 572: expression_with_block -> :dt:`expression-with-block` is :t:`in scope` within the related
- 591: label -> A :dt:`label` is :t:`in scope` within the :t:`block expression` of the related
- 595: label -> A :dt:`label` is not :t:`in scope` within nested :t:`[async block]s`,
- 642: declarative_macro -> A :dt:`declarative macro` is :t:`in scope` after the related :t:`macro`
- 648: module -> :dt:`module` is subject to :t:`attribute` :c:`macro_use`, then the

## expressions.rst
- 78: expression -> An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may have
- 82: expression_with_block -> An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
- 279: expression -> An :dt:`expression` is not considered a :t:`constant expression` when it
- 623: path_expression -> A :dt:`path expression` is an :t:`expression` that denotes a :t:`path`.
- 2425: destructuring_assignment -> A :dt:`destructuring assignment` is an :t:`assignment expression` where
- 2467: destructuring_assignment -> A :dt:`destructuring assignment` is equivalent to a :t:`block expression` of the
- 3014: index_expression -> An :dt:`index expression` is an :t:`expression` that indexes into a :t:`value`
- 3026: index_expression -> An :dt:`index expression` is a :t:`constant expression` if the
- 3237: shorthand_initializer -> A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
- 3241: shorthand_initializer -> A :dt:`shorthand initializer` is equivalent to a :t:`named initializer` where
- 3551: method_call_expression -> A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
- 3556: method -> :dt:`method` is being invoked by a :t:`method call expression`.
- 3571: method_call_expression -> A :dt:`method call expression` is subject to :t:`method resolution`.
- 3612: method_call_expression -> A :dt:`method call expression` is equivalent to a :t:`call expression` where the
- 3658: field_access_expression -> A :dt:`field access expression` is an :t:`expression` that accesses a :t:`field`
- 3700: field_access_expression -> A :dt:`field access expression` is subject to :t:`field resolution`.
- 3874: loop_expression -> A :dt:`loop expression` is an :t:`expression` that evaluates a :t:`block
- 3893: loop_expression -> A :dt:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
- 4712: match_arm -> A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
- 4757: match_arm -> A :dt:`match arm` is selected when its :t:`pattern` matches the

## functions.rst
- 52: function -> A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.
- 66: function_parameter -> A :dt:`function parameter` is a :t:`construct` that yields a set of
- 153: function_body -> A :dt:`function body` is the :t:`block expression` of a :t:`function`.
- 160: function_body -> A :dt:`function body` denotes a :t:`control flow boundary`.

## generics.rst
- 50: generic_parameter -> A :dt:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
- 126: generic_parameter -> A :dt:`generic parameter` is said to :dt:`constrain` an :t:`implementation` if the
- 390: lifetime_argument -> A :dt:`lifetime argument` is a :t:`generic argument` that supplies the
- 394: type_argument -> A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`type` of
- 444: lifetime_argument -> A :dt:`lifetime argument` is conformant with a :t:`lifetime parameter` when it
- 448: type_argument -> A :dt:`type argument` is conformant with a :t:`type parameter` when the

## implementations.rst
- 65: trait_implementation -> A :dt:`trait implementation` is an :t:`implementation` that adds functionality
- 250: trait_implementation -> A :dt:`trait implementation` is conformant with an :t:`implemented trait` when:

## inline-assembly.rst
- 16: inline_assembly -> :dt:`Inline assembly` is hand-written assembly code that is integrated into a
- 20: inline_assembly -> :dt:`Inline assembly` is written as an :t:`assembly code block` that is
- 27: inline_assembly -> :dt:`Inline assembly` is available on the following architectures:

## lexical-elements.rst
- 758: simple_c_string_literal -> A :dt:`simple c string literal` is any :t:`Unicode` character except characters
- 765: simple_c_string_literal -> A :dt:`simple c string literal` is a :t:`c string literal` where the characters are

## macros.rst
- 74: declarative_macro -> A :dt:`declarative macro` is a :t:`macro` that associates a :t:`name` with a set
- 93: declarative_macro -> A :dt:`declarative macro` is invoked using a :t:`macro invocation`.
- 147: metavariable -> A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.
- 150: metavariable -> A :dt:`metavariable` is visible in the :t:`macro transcriber` of the
- 335: function_like_macro -> A :dt:`function-like macro` is a :t:`procedural macro` that consumes a stream of
- 363: function_like_macro -> A :dt:`function-like macro` is invoked using a :t:`macro invocation`.
- 387: derive_macro -> A :dt:`derive macro` is a :t:`procedural macro` that consumes a stream of
- 416: derive_macro -> A :dt:`derive macro` is invoked using :t:`attribute` :c:`derive`.
- 1075: hygiene -> :dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
- 1082: hygiene -> :dt:`Hygiene` is categorized as follows:

## ownership-and-deconstruction.rst
- 93: reference -> A :dt:`reference` is a :t:`value` of a :t:`reference type`. A :t:`reference`
- 108: reference -> A :dt:`reference` is :dt:`active` from the point of obtaining its :t:`referent`
- 165: value -> A :dt:`value` is :dt:`borrowed` when it is associated with an active
- 714: function_parameter -> :dt:`function parameter` is :t:`dropped` from right to left as follows:

## patterns.rst
- 154: identifier_pattern -> An :dt:`identifier pattern` is a :t:`pattern` that binds the :t:`value` it
- 162: identifier_pattern -> An :dt:`identifier pattern` yields a :t:`binding`. An :t:`identifier pattern`
- 184: identifier_pattern -> An :dt:`identifier pattern` is an :t:`irrefutable pattern` when:
- 318: parenthesized_pattern -> A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
- 322: parenthesized_pattern -> A :dt:`parenthesized pattern` is an :t:`irrefutable pattern` when its nested
- 365: path_pattern -> A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
- 399: path_pattern -> A :dt:`path pattern` is an :t:`irrefutable pattern` when it refers to:
- 479: range_pattern -> A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
- 495: obsolete_range_pattern -> An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete syntax
- 522: obsolete_range_pattern -> An :dt:`obsolete range pattern` is equivalent to an :t:`inclusive range pattern`.
- 525: range_pattern -> A :dt:`range pattern` is an :t:`irrefutable pattern` only when it spans the
- 581: reference_pattern -> A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer` that
- 585: reference_pattern -> A :dt:`reference pattern` is an :t:`irrefutable pattern` when its nested :t:`pattern` itself is an :t:`irrefutable pattern`.
- 630: rest_pattern -> A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
- 639: rest_pattern -> A :dt:`rest pattern` is an :t:`irrefutable pattern`.
- 695: slice_pattern -> A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed size
- 699: slice_pattern -> A :dt:`slice pattern` is an :t:`irrefutable pattern` when it refers to:
- 747: struct_pattern -> A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
- 755: struct_pattern -> A :dt:`struct pattern` is interpreted based on the :t:`deconstructee`. It is a
- 759: struct_pattern -> A :dt:`struct pattern` is an :t:`irrefutable pattern` if
- 852: shorthand_deconstructor -> A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
- 866: shorthand_deconstructor -> A :dt:`shorthand deconstructor` is equivalent to a :t:`named deconstructor` where
- 1111: tuple_pattern -> A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which satisfies
- 1115: tuple_pattern -> A :dt:`tuple pattern` is an :t:`irrefutable pattern` when all of its
- 1191: underscore_pattern -> An :dt:`underscore pattern` is a :t:`pattern` that matches any single :t:`value`.
- 1194: underscore_pattern -> An :dt:`underscore pattern` is an :t:`irrefutable pattern`.

## program-structure-and-compilation.rst
- 73: module -> A :dt:`module` is a container for zero or more :t:`[item]s`.

## statements.rst
- 25: expression_statement -> An :dt:`expression statement` is an :t:`expression` whose result is ignored.
- 167: expression_statement -> An :dt:`expression statement` is an :t:`expression` whose result is ignored.

## types-and-traits.rst
- 531: slice_type -> A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
- 538: slice_type -> A :dt:`slice type` is a :t:`dynamically sized type`.
- 595: tuple_type -> A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
- 659: enum_variant -> An :dt:`enum variant` is a :t:`construct` that declares one of the
- 928: function_item_type -> A :dt:`function item type` is a unique anonymous :t:`function type` that
- 940: function_item_type -> A :dt:`function item type` is coercible to a :t:`function pointer type`.
- 983: function_pointer_type -> A :dt:`function pointer type` is an :t:`indirection type` that refers to a
- 1033: raw_pointer_type -> A :dt:`raw pointer type` is an :t:`indirection type` without validity guarantees.
- 1073: reference_type -> A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.
- 1148: impl_trait_type -> An :dt:`impl trait type` is a :t:`type` that implements a :t:`trait`, where the
- 1213: trait_object_type -> A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where the
- 1220: trait -> A :dt:`trait` is :dt:`object safe` when it can be used as a
- 1236: trait_object_type -> A :dt:`trait object type` is a :t:`dynamically sized type`. A
- 1331: never_type -> The :dt:`never type` is a :t:`type` that represents the result of a computation
- 1391: type_alias -> A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.
- 1536: type_representation -> :dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
- 1542: type_representation -> :dt:`Type representation` is classified into:
- 1605: primitive_representation -> :dt:`primitive representation` are those of its :t:`discriminant`.
- 1618: primitive_representation -> :dt:`primitive representation` is the :t:`integer type` specified by the
- 1769: type_unification -> :dt:`Type unification` is the process by which :t:`type inference` propagates
- 1775: type -> A :dt:`type` is said to :dt:`unify` with another :t:`type` when the domains,
- 1783: type_unification -> :dt:`Type unification` is a symmetric operation. If :t:`type` ``A`` unifies
- 1832: never_type -> The :dt:`never type` is unifiable with any other :t:`type`.
- 1844: slice_type -> A :dt:`slice type` is unifiable only with another :t:`slice type` when the
- 1851: tuple_type -> A :dt:`tuple type` is unifiable only with another :t:`tuple type` when:
- 1879: function_item_type -> A :dt:`function item type` is unifiable only with another :t:`function item type`
- 1889: function_pointer_type -> A :dt:`function pointer type` is unifiable only with another
- 1896: unsafety -> The :dt:`unsafety` is the same, and
- 1915: raw_pointer_type -> A :dt:`raw pointer type` is unifiable only with another :t:`raw pointer type`
- 1919: mutability -> The :dt:`mutability` is the same, and
- 1925: reference_type -> A :dt:`reference type` is unifiable only with another :t:`reference type` when:
- 1928: mutability -> The :dt:`mutability` is the same, and
- 1944: impl_trait_type -> An :dt:`impl trait type` is unifiable only with itself.
- 1947: trait_object_type -> A :dt:`trait object type` is unifiable only with another :t:`trait object type`
- 1957: type_alias -> A :dt:`type alias` is unifiable with another :t:`type` when the aliased :t:`type`
- 2188: type -> A :dt:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
- 2226: type -> A :dt:`type` is subject to :t:`interior mutability` when it contains a
- 2246: type -> A :dt:`type` is subject to :t:`visible emptiness` as follows:
- 2267: enum_variant -> A :dt:`enum variant` is subject to :t:`visible emptiness` when the :t:`type` of at least one of the :t:`enum variant`'s :t:`visible <visibility>` :t:`[field]s` is subject to :t:`visible emptiness`.
- 2749: trait -> A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
- 2861: trait -> A :dt:`trait` is :t:`object safe` when:
- 2902: function -> A :dt:`function` is :t:`object safe` when it specifies a
- 3034: lifetime -> A :dt:`lifetime` specifies the expected longevity of a :t:`value`.
- 3061: variance -> :dt:`Variance` is a property of :t:`[lifetime parameter]s` and
- 3067: type -> A :dt:`type` is its own :t:`subtype`.
- 3084: variance -> :dt:`Variance` is determined as follows:
- 3142: trait -> A :dt:`trait` is :t:`invariant` in all inputs, including the :c:`Self` parameter.
- 3258: lifetime -> A :dt:`lifetime` is elided explicitly if it is the ``'_`` :t:`lifetime`.
- 3261: lifetime -> A :dt:`lifetime` is elided implicitly if it is absent.

## unsafety.rst
- 14: unsafety -> :dt:`Unsafety` is the presence of :t:`[unsafe operation]s` and :t:`[unsafe trait

## values.rst
- 14: value -> A :dt:`value` is either a :t:`literal` or the result of a computation, that may
- 18: value -> A :dt:`value` is :dt:`immutable` when it cannot be modified.
- 21: value -> A :dt:`value` is :dt:`mutable` when it can be modified.
- 158: static -> A :dt:`static` is a :t:`value` that is associated with a specific memory
- 215: static -> A :dt:`static` is not :t:`dropped` during :t:`destruction`.
- 252: variable -> A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
- 271: variable -> A :dt:`variable` is not initialized when allocated.

