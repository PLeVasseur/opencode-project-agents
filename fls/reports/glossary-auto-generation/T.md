# Glossary audit T

## Per-letter checklist
- Letter: T
- [ ] Reconcile T terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate T terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for T
- [ ] Update `migration-checklist.md` for all T terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint T migration`
- [ ] Letter complete

## Term checklist
- [ ] tail expression (tail_expression)
- [ ] temporary (temporary)
- [x] terminated (terminated)
- [ ] terminated macro invocation (terminated_macro_invocation)
- [ ] textual macro scope (textual_macro_scope)
- [ ] textual type (textual_type)
- [ ] thin pointer (thin_pointer)
- [ ] thin pointer type (thin_pointer_type)
- [ ] token matching (token_matching)
- [ ] tokens (token)
- [ ] trait (trait)
- [ ] trait body (trait_body)
- [ ] trait bound (trait_bound)
- [ ] trait implementation (trait_implementation)
- [ ] trait object lifetime elision (trait_object_lifetime_elision)
- [ ] trait object type (trait_object_type)
- [ ] trait type (trait_type)
- [ ] transparent representation (transparent_representation)
- [ ] trivial predicate (trivial_predicate)
- [ ] tuple (tuple)
- [ ] tuple enum variant (tuple_enum_variant)
- [ ] tuple enum variant value (tuple_enum_variant_value)
- [ ] tuple expression (tuple_expression)
- [ ] tuple field (tuple_field)
- [ ] tuple initializer (tuple_initializer)
- [ ] tuple pattern (tuple_pattern)
- [ ] tuple struct (tuple_struct)
- [ ] tuple struct call expression (tuple_struct_call_expression)
- [ ] tuple struct field (tuple_struct_field)
- [ ] tuple struct pattern (tuple_struct_pattern)
- [ ] tuple struct type (tuple_struct_type)
- [ ] tuple struct value (tuple_struct_value)
- [ ] tuple type (tuple_type)
- [ ] type (type)
- [ ] type alias (type_alias)
- [ ] type argument (type_argument)
- [ ] type ascription (type_ascription)
- [ ] type bound predicate (type_bound_predicate)
- [ ] type cast expression (type_cast_expression)
- [ ] type coercion (type_coercion)
- [ ] type inference (type_inference)
- [ ] type inference root (type_inference_root)
- [ ] type parameter (type_parameter)
- [ ] type parameter initializer (type_parameter_initializer)
- [ ] type parameter type (type_parameter_type)
- [ ] type path (type_path)
- [ ] type path resolution (type_path_resolution)
- [ ] type representation (type_representation)
- [ ] type specification (type_specification)
- [ ] type unification (type_unification)
- [ ] type variable (type_variable)

## tail expression (tail_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_psd2ll10ixs:

tail expression
^^^^^^^^^^^^^^^

:dp:`fls_6k873f1knasi`
A :dt:`tail expression` is the last :t:`expression` within a
:t:`block expression`.
```

### After glossary entry (generated)

```rst
.. _fls_hRiL9usuZEUm:

tail expression
^^^^^^^^^^^^^^^

:dp:`fls_FZC5FEsWyzdk`
 A :t:`tail expression <tail_expression>` is the last :t:`expression` within a :t:`block expression <block_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## temporary (temporary)

### Before glossary entry (origin/main)

```rst
.. _fls_4omay4i65dwz:

temporary
^^^^^^^^^

:dp:`fls_fathkxu9kxvw`
A :dt:`temporary` is an anonymous :t:`variable` produced by some intermediate
computation.
```

### After glossary entry (generated)

```rst
.. _fls_NHB0j6WayupJ:

temporary
^^^^^^^^^

:dp:`fls_ZmgMfOLzyuvf`
 A :t:`temporary` is an anonymous :t:`variable` produced by some intermediate computation.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## terminated (terminated)

### Before glossary entry (origin/main)

```rst
.. _fls_ihv02usuziw8:

terminated
^^^^^^^^^^

:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
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


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## terminated macro invocation (terminated_macro_invocation)

### Before glossary entry (origin/main)

```rst
.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.

:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.
```

### After glossary entry (generated)

```rst
.. _fls_NLysZvWZticD:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ooUadlpJdeDO`
 A :t:`terminated macro invocation <terminated_macro_invocation>` is a :t:`macro invocation <macro_invocation>` that may be used as a :t:`statement`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_fathkxu9kxvw`
A :dt:`temporary` is an anonymous :t:`variable` produced by some intermediate
computation.

.. _fls_ihv02usuziw8:

terminated
^^^^^^^^^^


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_fathkxu9kxvw`
A :dt:`temporary` is an anonymous :t:`variable` produced by some intermediate
computation.

.. _fls_ihv02usuziw8:

terminated
^^^^^^^^^^


:dp:`fls_med1l8vheb83`
A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
longer evaluated.

.. _fls_ef03n3ehz372:

terminated macro invocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## textual macro scope (textual_macro_scope)

### Before glossary entry (origin/main)

```rst
.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^

:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.
```

### After glossary entry (generated)

```rst
.. _fls_9zM2c1wktHQt:

textual macro scope
^^^^^^^^^^^^^^^^^^^

:dp:`fls_rYXEOMxwWN5B`
 A :t:`textual macro scope <textual_macro_scope>` is a :t:`scope` for :t:`declarative macros <declarative_macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_542es82wfzco`
A :dt:`terminated macro invocation` is a :t:`macro invocation` that may be used
as a :t:`statement`.


:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## textual type (textual_type)

### Before glossary entry (origin/main)

```rst
.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^

:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.
```

### After glossary entry (generated)

```rst
.. _fls_Im8AUtciRNcY:

textual type
^^^^^^^^^^^^

:dp:`fls_RuyrFkkVb0ox`
 A :t:`textual type <textual_type>` is a :t:`type` class that includes type :c:`char` and type :c:`str`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_tcvfi2zgdm58`
See :s:`TerminatedMacroInvocation`.

.. _fls_AVZGZPd6WXXO:

textual macro scope
^^^^^^^^^^^^^^^^^^^


:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## thin pointer (thin_pointer)

### Before glossary entry (origin/main)

```rst
.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^

:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.
```

### After glossary entry (generated)

```rst
.. _fls_QyAIRudSxJo3:

thin pointer
^^^^^^^^^^^^

:dp:`fls_WBlJB9LvjfKP`
 A :t:`thin pointer <thin_pointer>` is a :t:`value` of a :t:`thin pointer type <thin_pointer_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_xyeYk6vrmlWp`
A :dt:`textual macro scope` is a :t:`scope` for :t:`[declarative macro]s`.

.. _fls_mdcbhy96hrau:

textual type
^^^^^^^^^^^^


:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## thin pointer type (thin_pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^

:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.
```

### After glossary entry (generated)

```rst
.. _fls_wjxeVq7ofQhB:

thin pointer type
^^^^^^^^^^^^^^^^^

:dp:`fls_KahaVA0Z6u9r`
 A :t:`thin pointer type <thin_pointer_type>` is an :t:`indirection type <indirection_type>` that refers to a :t:`fixed sized type <fixed_sized_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.

.. _fls_lfsgf6u142yb:

thin pointer
^^^^^^^^^^^^


:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## token matching (token_matching)

### Before glossary entry (origin/main)

```rst
.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^

:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.
```

### After glossary entry (generated)

```rst
.. _fls_G7lCR67pmf7x:

Token matching
^^^^^^^^^^^^^^

:dp:`fls_f54Sy3RlyOCG`
 :t:`Token matching <token_matching>` is the process of consuming a :s:`TokenTree <tokentree>` in an attempt to fully satisfy a :t:`macro match <macro_match>` of a selected :t:`macro matcher <macro_matcher>` that belongs to a resolved :t:`declarative macro <declarative_macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_i2j0u4v5o1bs`
A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.

.. _fls_7ksqpi9j8ba9:

thin pointer type
^^^^^^^^^^^^^^^^^


:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tokens (token)

### Before glossary entry (origin/main)

```rst
.. _fls_ma3vs7yoj285:

tokens
^^^^^^

:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.
```

### After glossary entry (generated)

```rst
.. _fls_0UBCKbcExyJn:

Tokens
^^^^^^

:dp:`fls_BTaRLF95JJgX`
 :t:`Tokens <token>` are a subset of :t:`lexical elements <lexical_element>` consumed by :t:`macros <macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_33rka3kyxgrk`
A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
:t:`fixed sized type`.

.. _fls_tzoko74t5t6n:

token matching
^^^^^^^^^^^^^^


:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait (trait)

### Before glossary entry (origin/main)

```rst
.. _fls_cad25qns4164:

trait
^^^^^

:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.

:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_TgzSUlvYp1Mj:

trait
^^^^^

:dp:`fls_YXk7NxcmfgSu`
 A :t:`trait` is an :t:`item` that describes an interface a :t:`type` can implement.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^


:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.

.. _fls_ma3vs7yoj285:

tokens
^^^^^^


:dp:`fls_v23kqvyvscd7`
:dt:`[Token]s` are a subset of :t:`[lexical element]s` consumed by
:t:`[macro]s`.

.. _fls_cad25qns4164:

trait
^^^^^


:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^


:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait body (trait_body)

### Before glossary entry (origin/main)

```rst
.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^

:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.

:dp:`fls_dITFx04TB4h0`
See :s:`TraitBody`.
```

### After glossary entry (generated)

```rst
.. _fls_R1xnrs8mn1gd:

trait body
^^^^^^^^^^

:dp:`fls_1cwOx21Y38es`
 A :t:`trait body <trait_body>` is a :t:`construct` that encapsulates the :t:`associated items <associated_item>`, :t:`inner attributes <inner_attribute>`, and :t:`inner doc comments <inner_doc_comment>` of a :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^


:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.


:dp:`fls_dITFx04TB4h0`
See :s:`TraitBody`.

.. _fls_868cgnb1soeh:

trait bound
^^^^^^^^^^^


:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mf4x9g70o5z6`
A :dt:`trait` is an :t:`item` that describes an interface a :t:`type` can
implement.


:dp:`fls_ypjhwvuyrns`
See :s:`TraitDeclaration`.

.. _fls_5hNydsQDrICq:

trait body
^^^^^^^^^^


:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.


:dp:`fls_dITFx04TB4h0`
See :s:`TraitBody`.

.. _fls_868cgnb1soeh:

trait bound
^^^^^^^^^^^


:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait bound (trait_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_868cgnb1soeh:

trait bound
^^^^^^^^^^^

:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.

:dp:`fls_bkbym8v4t6oh`
See :s:`TraitBound`.
```

### After glossary entry (generated)

```rst
.. _fls_5SfhRajzjNL4:

trait bound
^^^^^^^^^^^

:dp:`fls_hptoKbFik1bP`
 A :t:`trait bound <trait_bound>` is a :t:`bound` that imposes a constraint on the :t:`traits <trait>` of :t:`generic parameters <generic_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.


:dp:`fls_dITFx04TB4h0`
See :s:`TraitBody`.

.. _fls_868cgnb1soeh:

trait bound
^^^^^^^^^^^


:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.


:dp:`fls_bkbym8v4t6oh`
See :s:`TraitBound`.

.. _fls_kflieu6uottg:

trait implementation
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_u221Me58aZmY`
A :dt:`trait body` is a :t:`construct` that encapsulates the
:t:`[associated item]s`, :t:`[inner attribute]s`, and
:t:`[inner doc comment]s` of a :t:`trait`.


:dp:`fls_dITFx04TB4h0`
See :s:`TraitBody`.

.. _fls_868cgnb1soeh:

trait bound
^^^^^^^^^^^


:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.


:dp:`fls_bkbym8v4t6oh`
See :s:`TraitBound`.

.. _fls_kflieu6uottg:

trait implementation
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait implementation (trait_implementation)

### Before glossary entry (origin/main)

```rst
.. _fls_kflieu6uottg:

trait implementation
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.

:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.
```

### After glossary entry (generated)

```rst
.. _fls_JMpJwqqmtrma:

trait implementation
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tPK7rbbVqgjq`
 A :t:`trait implementation <trait_implementation>` is an :t:`implementation` that adds functionality specified by a :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.


:dp:`fls_bkbym8v4t6oh`
See :s:`TraitBound`.

.. _fls_kflieu6uottg:

trait implementation
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.


:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_95zx8unuxxpq`
A :dt:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.


:dp:`fls_bkbym8v4t6oh`
See :s:`TraitBound`.

.. _fls_kflieu6uottg:

trait implementation
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.


:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait object lifetime elision (trait_object_lifetime_elision)

### Before glossary entry (origin/main)

```rst
.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.
```

### After glossary entry (generated)

```rst
.. _fls_E2vWzorRAEhw:

Trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_SAyoFpWzGJM4`
 :t:`Trait object lifetime elision <trait_object_lifetime_elision>` is a form of :t:`lifetime elision <lifetime_elision>` that applies to :t:`trait object types <trait_object_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.


:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^


:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_5v7kbg144pr8`
A :dt:`trait implementation` is an :t:`implementation` that adds functionality
specified by a :t:`trait`.


:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^


:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## trait object type (trait_object_type)

### Before glossary entry (origin/main)

```rst
.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^

:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.

:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.
```

### After glossary entry (generated)

```rst
.. _fls_IJDDyZ02BjiF:

trait object type
^^^^^^^^^^^^^^^^^

:dp:`fls_hsWylz6Qgwdm`
 A :t:`trait object type <trait_object_type>` is a :t:`type` that implements a :t:`trait`, where the :t:`type` is not known at compile time.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^


:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_rytylyyxh27f`
See :s:`TraitImplementation`.

.. _fls_TCIzYoMeGtub:

trait object lifetime elision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_rALP9b6qjlp9`
:dt:`Trait object lifetime elision` is a form of :t:`lifetime elision` that
applies to :t:`[trait object type]s`.

.. _fls_7qtbro7ipndr:

trait object type
^^^^^^^^^^^^^^^^^


:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## trait type (trait_type)

### Before glossary entry (origin/main)

```rst
.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^

:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.
```

### After glossary entry (generated)

```rst
.. _fls_763BStLVfJAJ:

trait type
^^^^^^^^^^

:dp:`fls_vsttUZ5MpUaQ`
 A :t:`trait type <trait_type>` is either an :t:`impl trait type <impl_trait_type>` or a :t:`trait object type <trait_object_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lo2fzzdwxy1l`
A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where
the :t:`type` is not known at compile time.


:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## transparent representation (transparent_representation)

### Before glossary entry (origin/main)

```rst
.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.
```

### After glossary entry (generated)

```rst
.. _fls_xypPJh3PD9s3:

Transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_UV5YAhCzjgj5`
 :t:`Transparent representation <transparent_representation>` is a :t:`type representation <type_representation>` that applies only to an :t:`enum type <enum_type>` with a single :t:`enum variant <enum_variant>` or a :t:`struct type <struct_type>` where the :t:`struct type <struct_type>` or :t:`enum variant <enum_variant>` has a single :t:`field` of non-zero :t:`size` and any number of :t:`fields <field>` of :t:`size` zero and :t:`alignment` one.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_d632mc5c8qwt`
See :s:`TraitObjectTypeSpecification`,
:s:`TraitObjectTypeSpecificationOneBound`.

.. _fls_nfdfeFVZRC5F:

trait type
^^^^^^^^^^


:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## trivial predicate (trivial_predicate)

### Before glossary entry (origin/main)

```rst
.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^

:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.
```

### After glossary entry (generated)

```rst
.. _fls_z5yeSprZqAZP:

trivial predicate
^^^^^^^^^^^^^^^^^

:dp:`fls_eb8d0Ljc2xCm`
 A :t:`trivial predicate <trivial_predicate>` is a :t:`where clause predicate <where_clause_predicate>` that does not use the :t:`generic parameters <generic_parameter>` or :t:`higher-ranked trait bounds <higher_ranked_trait_bound>` of the related :t:`construct`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_JQsQnQ0dTHlS`
A :dt:`trait type` is either an :t:`impl trait type` or a
:t:`trait object type`.

.. _fls_sl62718i1kkn:

transparent representation
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## tuple (tuple)

### Before glossary entry (origin/main)

```rst
.. _fls_si70t19ox07e:

tuple
^^^^^

:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.
```

### After glossary entry (generated)

```rst
.. _fls_MDjRKF8703K7:

tuple
^^^^^

:dp:`fls_m4Kw80MMl9im`
 A :t:`tuple` is a :t:`value` of a :t:`tuple type <tuple_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hb3e72rhzpnv`
:dt:`Transparent representation` is a :t:`type representation` that applies
only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type`
where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of
non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and
:t:`alignment` one.

.. _fls_soqkluvirlsd:

trivial predicate
^^^^^^^^^^^^^^^^^


:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple enum variant (tuple_enum_variant)

### Before glossary entry (origin/main)

```rst
.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^

:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.
```

### After glossary entry (generated)

```rst
.. _fls_IMKC2UgD0Isr:

tuple enum variant
^^^^^^^^^^^^^^^^^^

:dp:`fls_6xhqFkWOY4rT`
 A :t:`tuple enum variant <tuple_enum_variant>` is an :t:`enum variant <enum_variant>` with a :s:`TupleStructFieldList <tuplestructfieldlist>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_db5njwrjolhs`
A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

.. _fls_si70t19ox07e:

tuple
^^^^^


:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple enum variant value (tuple_enum_variant_value)

### Before glossary entry (origin/main)

```rst
.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.
```

### After glossary entry (generated)

```rst
.. _fls_TAGgFDpRGqTs:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_MKaaDdbMU3Ao`
 A :t:`tuple enum variant value <tuple_enum_variant_value>` is a :t:`value` of a :t:`tuple enum variant <tuple_enum_variant>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

.. _fls_1XEHpJOK9DKB:

tuple enum variant
^^^^^^^^^^^^^^^^^^


:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple expression (tuple_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^

:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_JgOyqa7OBVEa:

tuple expression
^^^^^^^^^^^^^^^^

:dp:`fls_4J9cbin0wNtv`
 A :t:`tuple expression <tuple_expression>` is an :t:`expression` that constructs a :t:`tuple`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.

.. _fls_sP7uHoLxGfRO:

tuple enum variant value
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ORURxipGqNrZ`
A :dt:`tuple enum variant value` is a :t:`value` of a :t:`tuple enum variant`.

.. _fls_udl6ujjg1jae:

tuple expression
^^^^^^^^^^^^^^^^


:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple field (tuple_field)

### Before glossary entry (origin/main)

```rst
.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^

:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.
```

### After glossary entry (generated)

```rst
.. _fls_BGaw65jXs2kG:

tuple field
^^^^^^^^^^^

:dp:`fls_RfTKdInsUUeF`
 A :t:`tuple field <tuple_field>` is a :t:`field` of a :t:`tuple type <tuple_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.


:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple initializer (tuple_initializer)

### Before glossary entry (origin/main)

```rst
.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^

:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.
```

### After glossary entry (generated)

```rst
.. _fls_bqSjsBOchFtD:

tuple initializer
^^^^^^^^^^^^^^^^^

:dp:`fls_hSyG6rhhaInN`
 A :t:`tuple initializer <tuple_initializer>` is an :t:`operand` that provides the :t:`value` of a :t:`tuple field <tuple_field>` in a :t:`tuple expression <tuple_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.

.. _fls_bf1v4e1s5xj6:

tuple field
^^^^^^^^^^^


:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple pattern (tuple_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^

:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.

:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_OOhSEQkljg12:

tuple pattern
^^^^^^^^^^^^^

:dp:`fls_5dA8YTauGjc5`
 A :t:`tuple pattern <tuple_pattern>` is a :t:`pattern` that matches a :t:`tuple` which satisfies all criteria defined by its :t:`subpatterns <subpattern>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^


:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

.. _fls_zfvvbf7ncrhj:

tuple initializer
^^^^^^^^^^^^^^^^^


:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

.. _fls_7f2sx37kg4ca:

tuple pattern
^^^^^^^^^^^^^


:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^


:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple struct (tuple_struct)

### Before glossary entry (origin/main)

```rst
.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^

:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.

:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_JD95vPwYY1WV:

tuple struct
^^^^^^^^^^^^

:dp:`fls_UKflCLSQjXAM`
 A :t:`tuple struct <tuple_struct>` is a :t:`struct` with a :s:`TupleStructFieldList <tuplestructfieldlist>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^


:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.


:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_al2q3vh1rg6e`
A :dt:`tuple pattern` is a :t:`pattern` that matches a :t:`tuple` which
satisfies all criteria defined by its :t:`[subpattern]s`.


:dp:`fls_bevmt5t0238j`
See :s:`TuplePattern`.

.. _fls_245idp9hpqf6:

tuple struct
^^^^^^^^^^^^


:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.


:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple struct call expression (tuple_struct_call_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.
```

### After glossary entry (generated)

```rst
.. _fls_PeCupBQaMGqB:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_5WpYoqa7dOuj`
 A :t:`tuple struct call expression <tuple_struct_call_expression>` is a :t:`call expression <call_expression>` where the :t:`call operand <call_operand>` resolves to a :t:`tuple struct <tuple_struct>` or a :t:`tuple enum variant <tuple_enum_variant>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.


:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^


:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.


:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^


:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## tuple struct field (tuple_struct_field)

### Before glossary entry (origin/main)

```rst
.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^

:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.

:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.
```

### After glossary entry (generated)

```rst
.. _fls_iksdACRQGB4q:

tuple struct field
^^^^^^^^^^^^^^^^^^

:dp:`fls_MCsj885jpWvj`
 A :t:`tuple struct field <tuple_struct_field>` is a :t:`field` of a :t:`tuple struct type <tuple_struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^


:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_1tj4p05m4wdf`
See :s:`TupleStructDeclaration`.

.. _fls_UYCpeq4Z87My:

tuple struct call expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_DQaCUkskfXzk`
A :dt:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.

.. _fls_xx4slbg8s63e:

tuple struct field
^^^^^^^^^^^^^^^^^^


:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple struct pattern (tuple_struct_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.

:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_ER9oMR1F4Wmt:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_TAiXWOAJEQNu`
 A :t:`tuple struct pattern <tuple_struct_pattern>` is a :t:`pattern` that matches a :t:`tuple enum variant value <tuple_enum_variant_value>` or a :t:`tuple struct value <tuple_struct_value>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.


:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ndeb1a2hm9d8`
A :dt:`tuple struct field` is a :t:`field` of a :t:`tuple struct type`.


:dp:`fls_v4eq8xg608d5`
See :s:`TupleStructField`.

.. _fls_u2j18nl1t12f:

tuple struct pattern
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.


:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple struct type (tuple_struct_type)

### Before glossary entry (origin/main)

```rst
.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^

:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.
```

### After glossary entry (generated)

```rst
.. _fls_hBLkC606WkLP:

tuple struct type
^^^^^^^^^^^^^^^^^

:dp:`fls_JEhJSFc3TSgS`
 A :t:`tuple struct type <tuple_struct_type>` is the :t:`type` of a :t:`tuple struct <tuple_struct>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.


:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gu1mfurivnfz`
A :dt:`tuple struct pattern` is a :t:`pattern` that matches a
:t:`tuple enum variant value` or a :t:`tuple struct value`.


:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple struct value (tuple_struct_value)

### Before glossary entry (origin/main)

```rst
.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^

:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.
```

### After glossary entry (generated)

```rst
.. _fls_wrxSspY2v61q:

tuple struct value
^^^^^^^^^^^^^^^^^^

:dp:`fls_Y3Bc7PzlSdkX`
 A :t:`tuple struct value <tuple_struct_value>` is a :t:`value` of a :t:`tuple struct type <tuple_struct_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_3jx5683mdm10`
See :s:`TupleStructPattern`.

.. _fls_qx8j2lvqigqk:

tuple struct type
^^^^^^^^^^^^^^^^^


:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## tuple type (tuple_type)

### Before glossary entry (origin/main)

```rst
.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^

:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_cRa2SFVso95i:

tuple type
^^^^^^^^^^

:dp:`fls_k4Y8FuF39mzV`
 A :t:`tuple type <tuple_type>` is a :t:`sequence type <sequence_type>` that represents a heterogeneous list of other :t:`types <type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_hhikx5ajx3bl`
A :dt:`tuple struct type` is the :t:`type` of a :t:`tuple struct`.

.. _fls_x4ALCJKhVDZF:

tuple struct value
^^^^^^^^^^^^^^^^^^


:dp:`fls_xz1p4pss2Ocn`
A :dt:`tuple struct value` is a :t:`value` of a :t:`tuple struct type`.

.. _fls_k4yz7i2pf9wp:

tuple type
^^^^^^^^^^


:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type (type)

### Before glossary entry (origin/main)

```rst
.. _fls_wzupssn435n:

type
^^^^

:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.
```

### After glossary entry (generated)

```rst
.. _fls_7uno69pLEDiH:

unify
^^^^^

:dp:`fls_37YhwbveUi0j`
 A :t:`type` is said to :t:`unify` with another type when the domains, ranges, and structures of both :t:`types <type>` are compatible.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^


:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q0ulqfvnxwni`
A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.


:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^


:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type alias (type_alias)

### Before glossary entry (origin/main)

```rst
.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^

:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.

:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_eh8ZvV5lM2xj:

type alias
^^^^^^^^^^

:dp:`fls_BKVHfysP2gdS`
 A :t:`type alias <type_alias>` is an :t:`item` that defines a :t:`name` for a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^


:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^


:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_rkugxsau1w78`
See :s:`TupleTypeSpecification`.

.. _fls_wzupssn435n:

type
^^^^


:dp:`fls_nhlh7vvgsbwo`
A :dt:`type` defines a set of :t:`[value]s` and a set of operations that act on
those :t:`[value]s`.

.. _fls_vaklivoy2ix2:

type alias
^^^^^^^^^^


:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^


:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type argument (type_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^

:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.

:dp:`fls_91tqk65qiygf`
See :s:`TypeArgument`.
```

### After glossary entry (generated)

```rst
.. _fls_5LES25NX0CKc:

type argument
^^^^^^^^^^^^^

:dp:`fls_2mStRbKPIVFl`
 A :t:`type argument <type_argument>` is a :t:`generic argument <generic_argument>` that supplies the :t:`value` of a :t:`type parameter <type_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^


:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.


:dp:`fls_91tqk65qiygf`
See :s:`TypeArgument`.

.. _fls_1n50v16et5e6:

type ascription
^^^^^^^^^^^^^^^


:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_8pcsxodv1xp5`
A :dt:`type alias` is an :t:`item` that defines a :t:`name` for a :t:`type`.


:dp:`fls_qfzskp1t3h5w`
See :s:`TypeAliasDeclaration`.

.. _fls_89ollsdjx3uy:

type argument
^^^^^^^^^^^^^


:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.


:dp:`fls_91tqk65qiygf`
See :s:`TypeArgument`.

.. _fls_1n50v16et5e6:

type ascription
^^^^^^^^^^^^^^^


:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type ascription (type_ascription)

### Before glossary entry (origin/main)

```rst
.. _fls_1n50v16et5e6:

type ascription
^^^^^^^^^^^^^^^

:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.

:dp:`fls_c3xtiputfxea`
See :s:`TypeAscription`.
```

### After glossary entry (generated)

```rst
.. _fls_vGDM8G262WfN:

type ascription
^^^^^^^^^^^^^^^

:dp:`fls_OZm5cLAYYScs`
 A :t:`type ascription <type_ascription>` specifies the :t:`type` of a :t:`construct`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.


:dp:`fls_91tqk65qiygf`
See :s:`TypeArgument`.

.. _fls_1n50v16et5e6:

type ascription
^^^^^^^^^^^^^^^


:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.


:dp:`fls_c3xtiputfxea`
See :s:`TypeAscription`.

.. _fls_zDdXv5I4bW9H:

type bound predicate
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_152lk7hrtd11`
A :dt:`type argument` is a :t:`generic argument` that supplies the :t:`value`
of a :t:`type parameter`.


:dp:`fls_91tqk65qiygf`
See :s:`TypeArgument`.

.. _fls_1n50v16et5e6:

type ascription
^^^^^^^^^^^^^^^


:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.


:dp:`fls_c3xtiputfxea`
See :s:`TypeAscription`.

.. _fls_zDdXv5I4bW9H:

type bound predicate
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type bound predicate (type_bound_predicate)

### Before glossary entry (origin/main)

```rst
.. _fls_zDdXv5I4bW9H:

type bound predicate
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.

:dp:`fls_oMlPNgoDjnoW`
See :s:`TypeBoundPredicate`.
```

### After glossary entry (generated)

```rst
.. _fls_icX9npVuu6xe:

type bound predicate
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_UAKg6dC4YPbd`
 A :t:`type bound predicate <type_bound_predicate>` is a :t:`construct` that specifies :t:`lifetime bounds <lifetime_bound>` and :t:`trait bounds <trait_bound>` on a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.


:dp:`fls_c3xtiputfxea`
See :s:`TypeAscription`.

.. _fls_zDdXv5I4bW9H:

type bound predicate
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.


:dp:`fls_oMlPNgoDjnoW`
See :s:`TypeBoundPredicate`.

.. _fls_k24jb967nu1q:

type cast expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_pm5jytclqn7y`
A :dt:`type ascription` specifies the :t:`type` of a :t:`construct`.


:dp:`fls_c3xtiputfxea`
See :s:`TypeAscription`.

.. _fls_zDdXv5I4bW9H:

type bound predicate
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.


:dp:`fls_oMlPNgoDjnoW`
See :s:`TypeBoundPredicate`.

.. _fls_k24jb967nu1q:

type cast expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type cast expression (type_cast_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_k24jb967nu1q:

type cast expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.

:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_Yhz2noyHXaim:

type cast expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Vhp7Gpqjp286`
 A :t:`type cast expression <type_cast_expression>` is an :t:`expression` that changes the :t:`type` of an :t:`operand`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.


:dp:`fls_oMlPNgoDjnoW`
See :s:`TypeBoundPredicate`.

.. _fls_k24jb967nu1q:

type cast expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.


:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_j6WKoybB4cep`
A :dt:`type bound predicate` is a :t:`construct` that specifies
:t:`[lifetime bound]s` and :t:`[trait bound]s` on a :t:`type`.


:dp:`fls_oMlPNgoDjnoW`
See :s:`TypeBoundPredicate`.

.. _fls_k24jb967nu1q:

type cast expression
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.


:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type coercion (type_coercion)

### Before glossary entry (origin/main)

```rst
.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^

:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_0zrl1OsTVUsj:

Type coercion
^^^^^^^^^^^^^

:dp:`fls_769PxmMn7tY9`
 :t:`Type coercion <type_coercion>` is an implicit operation that changes the :t:`type` of a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.


:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_j6zo3rir1x76`
A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
of an :t:`operand`.


:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type inference (type_inference)

### Before glossary entry (origin/main)

```rst
.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^

:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_H5WfGrGEsaeJ:

Type inference
^^^^^^^^^^^^^^

:dp:`fls_SNlK25LLTexY`
 :t:`Type inference <type_inference>` is the process of deducing the expected :t:`type` of an arbitrary :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_dvh1xy9w74ch`
See :s:`TypeCastExpression`.

.. _fls_6j08yuafv0vl:

type coercion
^^^^^^^^^^^^^


:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type inference root (type_inference_root)

### Before glossary entry (origin/main)

```rst
.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^

:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.
```

### After glossary entry (generated)

```rst
.. _fls_BFCkeJnCQAnY:

type inference root
^^^^^^^^^^^^^^^^^^^

:dp:`fls_4mZI0aAn1s6U`
 A :t:`type inference root <type_inference_root>` is a :t:`construct` whose inner :t:`expressions <expression>` and :t:`patterns <pattern>` are subject to :t:`type inference <type_inference>` independently of other :t:`type inference roots <type_inference_root>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_mt36qehtqova`
:dt:`Type coercion` is an implicit operation that changes the :t:`type` of
a :t:`value`.

.. _fls_7fpvb2gvqng8:

type inference
^^^^^^^^^^^^^^


:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type parameter (type_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^

:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.

:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.
```

### After glossary entry (generated)

```rst
.. _fls_3T9WnFygNAt7:

type parameter
^^^^^^^^^^^^^^

:dp:`fls_mRrXwJT7AU6D`
 A :t:`type parameter <type_parameter>` is a :t:`generic parameter <generic_parameter>` for a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ky8epvf9834e`
:dt:`Type inference` is the process of deducing the expected :t:`type` of an
arbitrary :t:`value`.

.. _fls_0jri0m3F1fAT:

type inference root
^^^^^^^^^^^^^^^^^^^


:dp:`fls_hLI7lCixs48z`
A :dt:`type inference root` is a :t:`construct` whose inner :t:`[expression]s`
and :t:`[pattern]s` are subject to :t:`type inference` independently of other
:t:`[type inference root]s`.

.. _fls_uv2damik654e:

type parameter
^^^^^^^^^^^^^^


:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type parameter initializer (type_parameter_initializer)

### Before glossary entry (origin/main)

```rst
.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.

:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.
```

### After glossary entry (generated)

```rst
.. _fls_MGIzShK42HHg:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_faR4X7M1TMGP`
 A :t:`type parameter initializer <type_parameter_initializer>` is a :t:`construct` that provides the default :t:`value` of its related :t:`type parameter <type_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.


:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_5t6510wkb67x`
A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.


:dp:`fls_vquy0tsvd93x`
See :s:`TypeParameter`.

.. _fls_Fq2zTHYRpK2V:

type parameter initializer
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.


:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type parameter type (type_parameter_type)

### Before glossary entry (origin/main)

```rst
.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.
```

### After glossary entry (generated)

```rst
.. _fls_8jY8qxR5oddE:

type parameter type
^^^^^^^^^^^^^^^^^^^

:dp:`fls_GLZrePgUn4NY`
 A :t:`type parameter type <type_parameter_type>` is a placeholder :t:`type` of a :t:`type parameter <type_parameter>` to be substituted by :t:`generic substitution <generic_substitution>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.


:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^


:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Xpz47JLNsOXI`
A :dt:`type parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`type parameter`.


:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^


:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type path (type_path)

### Before glossary entry (origin/main)

```rst
.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^

:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.

:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.
```

### After glossary entry (generated)

```rst
.. _fls_EEFRSmbdU3sN:

type path
^^^^^^^^^

:dp:`fls_ybYrp4TXV9MM`
 A :t:`type path <type_path>` is a :t:`path` that acts as a :t:`type specification <type_specification>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^


:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6Ap26AcSadP8`
See :s:`TypeParameterInitializer`.

.. _fls_HghjWqvyj5bN:

type parameter type
^^^^^^^^^^^^^^^^^^^


:dp:`fls_EuHHxwHd0RHV`
A :dt:`type parameter type` is a placeholder :t:`type` of a :t:`type parameter`
to be substituted by :t:`generic substitution`.

.. _fls_QDCiXh7uSj9r:

type path
^^^^^^^^^


:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type path resolution (type_path_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.
```

### After glossary entry (generated)

```rst
.. _fls_8VINhH9Nzh3w:

Type path resolution
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ALbzfo1B4yzW`
 :t:`Type path resolution <type_path_resolution>` is a form of :t:`path resolution <path_resolution>` that applies to a :t:`type path <type_path>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.


:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type representation (type_representation)

### Before glossary entry (origin/main)

```rst
.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^

:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.
```

### After glossary entry (generated)

```rst
.. _fls_MXVIcy3gcEW3:

Type representation
^^^^^^^^^^^^^^^^^^^

:dp:`fls_OKkhLMl2wZse`
 :t:`Type representation <type_representation>` specifies the :t:`layout` of :t:`fields <field>` of :t:`abstract data types <abstract_data_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.

.. _fls_wa3biT0rQ102:

type path resolution
^^^^^^^^^^^^^^^^^^^^


:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type specification (type_specification)

### Before glossary entry (origin/main)

```rst
.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^

:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.

:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_oetTL5abqLbl:

type specification
^^^^^^^^^^^^^^^^^^

:dp:`fls_CiiDTd5PHbkT`
 A :t:`type specification <type_specification>` describes the structure of a :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

.. _fls_u1zkh2m8p92:

type representation
^^^^^^^^^^^^^^^^^^^


:dp:`fls_rv80nyxwj2z8`
:dt:`Type representation` specifies the :t:`layout` of :t:`[field]s` of
:t:`[abstract data type]s`.

.. _fls_ukua6gbye6ot:

type specification
^^^^^^^^^^^^^^^^^^


:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type unification (type_unification)

### Before glossary entry (origin/main)

```rst
.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^

:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.
```

### After glossary entry (generated)

```rst
.. _fls_hAKXyvEsYgxp:

Type unification
^^^^^^^^^^^^^^^^

:dp:`fls_VvJuL2Ke4N8S`
 :t:`Type unification <type_unification>` is the process by which :t:`type inference <type_inference>` propagates known :t:`types <type>` across the :t:`type inference root <type_inference_root>` and assigns concrete :t:`types <type>` to :t:`type variables <type_variable>`, as well as a general mechanism to check for compatibility between two :t:`types <type>` during :t:`method resolution <method_resolution>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^


:dp:`fls_j9eusnwze4rz`
A :dt:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

.. _fls_44uvj9l7q98z:

u8
^^


:dp:`fls_umf9zfeghy6`
:dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`8` - 1, all inclusive.

.. _fls_eh24kdjdze5j:

u16
^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_tdjhjg9zhnv5`
A :dt:`type specification` describes the structure of a :t:`type`.


:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^


:dp:`fls_j9eusnwze4rz`
A :dt:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

.. _fls_44uvj9l7q98z:

u8
^^


:dp:`fls_umf9zfeghy6`
:dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`8` - 1, all inclusive.

.. _fls_eh24kdjdze5j:

u16
^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## type variable (type_variable)

### Before glossary entry (origin/main)

```rst
.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^

:dp:`fls_j9eusnwze4rz`
A :dt:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.
```

### After glossary entry (generated)

```rst
.. _fls_KqgAxA81Vbpk:

type variable
^^^^^^^^^^^^^

:dp:`fls_LXNRu789xXm1`
 A :t:`type variable <type_variable>` is a placeholder used during :t:`type inference <type_inference>` to stand in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^


:dp:`fls_j9eusnwze4rz`
A :dt:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

.. _fls_44uvj9l7q98z:

u8
^^


:dp:`fls_umf9zfeghy6`
:dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`8` - 1, all inclusive.

.. _fls_eh24kdjdze5j:

u16
^^^


:dp:`fls_8vi7bm2895y0`
:dc:`u16` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`16` - 1, all inclusive.

.. _fls_jybcgdujzpqy:

u32
^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_a3sqjp1l8po6`
See :s:`TypeSpecification`.

.. _fls_qoehu9p00q56:

type unification
^^^^^^^^^^^^^^^^


:dp:`fls_3vyodut341b5`
:dt:`Type unification` is the process by which :t:`type inference` propagates
known :t:`[type]s` across the :t:`type inference root` and assigns concrete
:t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
for compatibility between two :t:`[type]s` during :t:`method resolution`.

.. _fls_6zhffgxtytku:

type variable
^^^^^^^^^^^^^


:dp:`fls_j9eusnwze4rz`
A :dt:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

.. _fls_44uvj9l7q98z:

u8
^^


:dp:`fls_umf9zfeghy6`
:dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`8` - 1, all inclusive.

.. _fls_eh24kdjdze5j:

u16
^^^


:dp:`fls_8vi7bm2895y0`
:dc:`u16` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`16` - 1, all inclusive.

.. _fls_jybcgdujzpqy:

u32
^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
