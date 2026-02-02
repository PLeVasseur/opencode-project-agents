# Duplicate term definitions

## declarative_macro
- entities-and-resolution.rst:642: A :dt:`declarative macro` is :t:`in scope` after the related :t:`macro`
- macros.rst:74: A :dt:`declarative macro` is a :t:`macro` that associates a :t:`name` with a set
- macros.rst:93: A :dt:`declarative macro` is invoked using a :t:`macro invocation`.

## derive_macro
- macros.rst:387: A :dt:`derive macro` is a :t:`procedural macro` that consumes a stream of
- macros.rst:416: A :dt:`derive macro` is invoked using :t:`attribute` :c:`derive`.

## destructuring_assignment
- expressions.rst:2425: A :dt:`destructuring assignment` is an :t:`assignment expression` where
- expressions.rst:2467: A :dt:`destructuring assignment` is equivalent to a :t:`block expression` of the

## enum_variant
- types-and-traits.rst:659: An :dt:`enum variant` is a :t:`construct` that declares one of the
- types-and-traits.rst:2267: A :dt:`enum variant` is subject to :t:`visible emptiness` when the :t:`type` of at least one of the :t:`enum variant`'s :t:`visible <visibility>` :t:`[field]s` is subject to :t:`visible emptiness`.

## expression
- expressions.rst:78: An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may have
- expressions.rst:279: An :dt:`expression` is not considered a :t:`constant expression` when it

## expression_statement
- statements.rst:25: An :dt:`expression statement` is an :t:`expression` whose result is ignored.
- statements.rst:167: An :dt:`expression statement` is an :t:`expression` whose result is ignored.

## expression_with_block
- entities-and-resolution.rst:572: :dt:`expression-with-block` is :t:`in scope` within the related
- expressions.rst:82: An :dt:`expression-with-block` is an :t:`expression` whose structure involves a

## field_access_expression
- expressions.rst:3658: A :dt:`field access expression` is an :t:`expression` that accesses a :t:`field`
- expressions.rst:3700: A :dt:`field access expression` is subject to :t:`field resolution`.

## function
- functions.rst:52: A :dt:`function` is a :t:`value` of a :t:`function type` that models a behavior.
- types-and-traits.rst:2902: A :dt:`function` is :t:`object safe` when it specifies a

## function_body
- functions.rst:153: A :dt:`function body` is the :t:`block expression` of a :t:`function`.
- functions.rst:160: A :dt:`function body` denotes a :t:`control flow boundary`.

## function_item_type
- types-and-traits.rst:928: A :dt:`function item type` is a unique anonymous :t:`function type` that
- types-and-traits.rst:940: A :dt:`function item type` is coercible to a :t:`function pointer type`.
- types-and-traits.rst:1879: A :dt:`function item type` is unifiable only with another :t:`function item type`

## function_like_macro
- macros.rst:335: A :dt:`function-like macro` is a :t:`procedural macro` that consumes a stream of
- macros.rst:363: A :dt:`function-like macro` is invoked using a :t:`macro invocation`.

## function_parameter
- functions.rst:66: A :dt:`function parameter` is a :t:`construct` that yields a set of
- ownership-and-deconstruction.rst:714: :dt:`function parameter` is :t:`dropped` from right to left as follows:

## function_pointer_type
- types-and-traits.rst:983: A :dt:`function pointer type` is an :t:`indirection type` that refers to a
- types-and-traits.rst:1889: A :dt:`function pointer type` is unifiable only with another

## generic_parameter
- entities-and-resolution.rst:518: A :dt:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.
- entities-and-resolution.rst:557: A :dt:`generic parameter` is not :t:`in scope` within nested :t:`[item]s`,
- generics.rst:50: A :dt:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
- generics.rst:126: A :dt:`generic parameter` is said to :dt:`constrain` an :t:`implementation` if the

## hygiene
- macros.rst:1075: :dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
- macros.rst:1082: :dt:`Hygiene` is categorized as follows:

## identifier_pattern
- patterns.rst:154: An :dt:`identifier pattern` is a :t:`pattern` that binds the :t:`value` it
- patterns.rst:162: An :dt:`identifier pattern` yields a :t:`binding`. An :t:`identifier pattern`
- patterns.rst:184: An :dt:`identifier pattern` is an :t:`irrefutable pattern` when:

## impl_trait_type
- types-and-traits.rst:1148: An :dt:`impl trait type` is a :t:`type` that implements a :t:`trait`, where the
- types-and-traits.rst:1944: An :dt:`impl trait type` is unifiable only with itself.

## index_expression
- expressions.rst:3014: An :dt:`index expression` is an :t:`expression` that indexes into a :t:`value`
- expressions.rst:3026: An :dt:`index expression` is a :t:`constant expression` if the

## inline_assembly
- inline-assembly.rst:16: :dt:`Inline assembly` is hand-written assembly code that is integrated into a
- inline-assembly.rst:20: :dt:`Inline assembly` is written as an :t:`assembly code block` that is
- inline-assembly.rst:27: :dt:`Inline assembly` is available on the following architectures:

## label
- entities-and-resolution.rst:591: A :dt:`label` is :t:`in scope` within the :t:`block expression` of the related
- entities-and-resolution.rst:595: A :dt:`label` is not :t:`in scope` within nested :t:`[async block]s`,

## lifetime
- types-and-traits.rst:3034: A :dt:`lifetime` specifies the expected longevity of a :t:`value`.
- types-and-traits.rst:3258: A :dt:`lifetime` is elided explicitly if it is the ``'_`` :t:`lifetime`.
- types-and-traits.rst:3261: A :dt:`lifetime` is elided implicitly if it is absent.

## lifetime_argument
- generics.rst:390: A :dt:`lifetime argument` is a :t:`generic argument` that supplies the
- generics.rst:444: A :dt:`lifetime argument` is conformant with a :t:`lifetime parameter` when it

## loop_expression
- expressions.rst:3874: A :dt:`loop expression` is an :t:`expression` that evaluates a :t:`block
- expressions.rst:3893: A :dt:`loop expression` is :dt:`terminated` when its :t:`block expression` is no

## match_arm
- expressions.rst:4712: A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
- expressions.rst:4757: A :dt:`match arm` is selected when its :t:`pattern` matches the

## metavariable
- macros.rst:147: A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.
- macros.rst:150: A :dt:`metavariable` is visible in the :t:`macro transcriber` of the

## method
- associated-items.rst:158: A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
- expressions.rst:3556: :dt:`method` is being invoked by a :t:`method call expression`.

## method_call_expression
- expressions.rst:3551: A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
- expressions.rst:3571: A :dt:`method call expression` is subject to :t:`method resolution`.
- expressions.rst:3612: A :dt:`method call expression` is equivalent to a :t:`call expression` where the

## module
- entities-and-resolution.rst:648: :dt:`module` is subject to :t:`attribute` :c:`macro_use`, then the
- program-structure-and-compilation.rst:73: A :dt:`module` is a container for zero or more :t:`[item]s`.

## mutability
- types-and-traits.rst:1919: The :dt:`mutability` is the same, and
- types-and-traits.rst:1928: The :dt:`mutability` is the same, and

## never_type
- types-and-traits.rst:1331: The :dt:`never type` is a :t:`type` that represents the result of a computation
- types-and-traits.rst:1832: The :dt:`never type` is unifiable with any other :t:`type`.

## obsolete_range_pattern
- patterns.rst:495: An :dt:`obsolete range pattern` is a :t:`range pattern` that uses obsolete syntax
- patterns.rst:522: An :dt:`obsolete range pattern` is equivalent to an :t:`inclusive range pattern`.

## parenthesized_pattern
- patterns.rst:318: A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
- patterns.rst:322: A :dt:`parenthesized pattern` is an :t:`irrefutable pattern` when its nested

## path
- entities-and-resolution.rst:292: A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
- entities-and-resolution.rst:299: A :dt:`path` is subject to :t:`path resolution`.

## path_expression
- entities-and-resolution.rst:357: A :dt:`path expression` is subject to :t:`path expression resolution`.
- expressions.rst:623: A :dt:`path expression` is an :t:`expression` that denotes a :t:`path`.

## path_pattern
- patterns.rst:365: A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
- patterns.rst:399: A :dt:`path pattern` is an :t:`irrefutable pattern` when it refers to:

## primitive_representation
- types-and-traits.rst:1605: :dt:`primitive representation` are those of its :t:`discriminant`.
- types-and-traits.rst:1618: :dt:`primitive representation` is the :t:`integer type` specified by the

## range_pattern
- patterns.rst:479: A :dt:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
- patterns.rst:525: A :dt:`range pattern` is an :t:`irrefutable pattern` only when it spans the

## raw_pointer_type
- types-and-traits.rst:1033: A :dt:`raw pointer type` is an :t:`indirection type` without validity guarantees.
- types-and-traits.rst:1915: A :dt:`raw pointer type` is unifiable only with another :t:`raw pointer type`

## reference
- ownership-and-deconstruction.rst:93: A :dt:`reference` is a :t:`value` of a :t:`reference type`. A :t:`reference`
- ownership-and-deconstruction.rst:108: A :dt:`reference` is :dt:`active` from the point of obtaining its :t:`referent`

## reference_pattern
- patterns.rst:581: A :dt:`reference pattern` is a :t:`pattern` that dereferences a :t:`pointer` that
- patterns.rst:585: A :dt:`reference pattern` is an :t:`irrefutable pattern` when its nested :t:`pattern` itself is an :t:`irrefutable pattern`.

## reference_type
- types-and-traits.rst:1073: A :dt:`reference type` is an :t:`indirection type` with :t:`ownership`.
- types-and-traits.rst:1925: A :dt:`reference type` is unifiable only with another :t:`reference type` when:

## rest_pattern
- patterns.rst:630: A :dt:`rest pattern` is a :t:`pattern` that matches zero or more elements that
- patterns.rst:639: A :dt:`rest pattern` is an :t:`irrefutable pattern`.

## shorthand_deconstructor
- patterns.rst:852: A :dt:`shorthand deconstructor` is a :t:`construct` that matches the :t:`name`
- patterns.rst:866: A :dt:`shorthand deconstructor` is equivalent to a :t:`named deconstructor` where

## shorthand_initializer
- expressions.rst:3237: A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
- expressions.rst:3241: A :dt:`shorthand initializer` is equivalent to a :t:`named initializer` where

## simple_c_string_literal
- lexical-elements.rst:758: A :dt:`simple c string literal` is any :t:`Unicode` character except characters
- lexical-elements.rst:765: A :dt:`simple c string literal` is a :t:`c string literal` where the characters are

## simple_path
- entities-and-resolution.rst:321: A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
- entities-and-resolution.rst:343: A :dt:`simple path` is subject to :t:`simple path resolution`.

## slice_pattern
- patterns.rst:695: A :dt:`slice pattern` is a :t:`pattern` that matches :t:`[array]s` of fixed size
- patterns.rst:699: A :dt:`slice pattern` is an :t:`irrefutable pattern` when it refers to:

## slice_type
- types-and-traits.rst:531: A :dt:`slice type` is a :t:`sequence type` that provides a view into a sequence
- types-and-traits.rst:538: A :dt:`slice type` is a :t:`dynamically sized type`.
- types-and-traits.rst:1844: A :dt:`slice type` is unifiable only with another :t:`slice type` when the

## static
- values.rst:158: A :dt:`static` is a :t:`value` that is associated with a specific memory
- values.rst:215: A :dt:`static` is not :t:`dropped` during :t:`destruction`.

## struct_pattern
- patterns.rst:747: A :dt:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
- patterns.rst:755: A :dt:`struct pattern` is interpreted based on the :t:`deconstructee`. It is a
- patterns.rst:759: A :dt:`struct pattern` is an :t:`irrefutable pattern` if

## trait
- types-and-traits.rst:1220: A :dt:`trait` is :dt:`object safe` when it can be used as a
- types-and-traits.rst:2749: A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
- types-and-traits.rst:2861: A :dt:`trait` is :t:`object safe` when:
- types-and-traits.rst:3142: A :dt:`trait` is :t:`invariant` in all inputs, including the :c:`Self` parameter.

## trait_implementation
- implementations.rst:65: A :dt:`trait implementation` is an :t:`implementation` that adds functionality
- implementations.rst:250: A :dt:`trait implementation` is conformant with an :t:`implemented trait` when:

## trait_object_type
- types-and-traits.rst:1213: A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where the
- types-and-traits.rst:1236: A :dt:`trait object type` is a :t:`dynamically sized type`. A
- types-and-traits.rst:1947: A :dt:`trait object type` is unifiable only with another :t:`trait object type`

## tuple_pattern
- patterns.rst:1111: A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which satisfies
- patterns.rst:1115: A :dt:`tuple pattern` is an :t:`irrefutable pattern` when all of its

## tuple_type
- types-and-traits.rst:595: A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
- types-and-traits.rst:1851: A :dt:`tuple type` is unifiable only with another :t:`tuple type` when:

## type
- types-and-traits.rst:1775: A :dt:`type` is said to :dt:`unify` with another :t:`type` when the domains,
- types-and-traits.rst:2188: A :dt:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
- types-and-traits.rst:2226: A :dt:`type` is subject to :t:`interior mutability` when it contains a
- types-and-traits.rst:2246: A :dt:`type` is subject to :t:`visible emptiness` as follows:
- types-and-traits.rst:3067: A :dt:`type` is its own :t:`subtype`.

## type_alias
- types-and-traits.rst:1391: A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.
- types-and-traits.rst:1957: A :dt:`type alias` is unifiable with another :t:`type` when the aliased :t:`type`

## type_argument
- generics.rst:394: A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`type` of
- generics.rst:448: A :dt:`type argument` is conformant with a :t:`type parameter` when the

## type_path
- entities-and-resolution.rst:360: A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
- entities-and-resolution.rst:363: A :dt:`type path` is subject to :t:`type path resolution`.

## type_representation
- types-and-traits.rst:1536: :dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
- types-and-traits.rst:1542: :dt:`Type representation` is classified into:

## type_unification
- types-and-traits.rst:1769: :dt:`Type unification` is the process by which :t:`type inference` propagates
- types-and-traits.rst:1783: :dt:`Type unification` is a symmetric operation. If :t:`type` ``A`` unifies

## underscore_pattern
- patterns.rst:1191: An :dt:`underscore pattern` is a :t:`pattern` that matches any single :t:`value`.
- patterns.rst:1194: An :dt:`underscore pattern` is an :t:`irrefutable pattern`.

## unsafety
- unsafety.rst:14: :dt:`Unsafety` is the presence of :t:`[unsafe operation]s` and :t:`[unsafe trait
- types-and-traits.rst:1896: The :dt:`unsafety` is the same, and

## value
- ownership-and-deconstruction.rst:165: A :dt:`value` is :dt:`borrowed` when it is associated with an active
- values.rst:14: A :dt:`value` is either a :t:`literal` or the result of a computation, that may
- values.rst:18: A :dt:`value` is :dt:`immutable` when it cannot be modified.
- values.rst:21: A :dt:`value` is :dt:`mutable` when it can be modified.

## variable
- values.rst:252: A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
- values.rst:271: A :dt:`variable` is not initialized when allocated.

## variance
- types-and-traits.rst:3061: :dt:`Variance` is a property of :t:`[lifetime parameter]s` and
- types-and-traits.rst:3084: :dt:`Variance` is determined as follows:

