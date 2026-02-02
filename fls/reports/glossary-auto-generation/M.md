# Glossary audit M

## Per-letter checklist
- Letter: M
- [ ] Reconcile M terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate M terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for M
- [ ] Update `migration-checklist.md` for all M terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint M migration`
- [ ] Letter complete

## Term checklist
- [ ] macro (macro)
- [ ] macro expansion (macro_expansion)
- [ ] macro implementation function (macro_implementation_function)
- [ ] macro invocation (macro_invocation)
- [ ] macro match (macro_match)
- [ ] macro matcher (macro_matcher)
- [ ] macro matching (macro_matching)
- [ ] macro repetition (macro_repetition)
- [ ] macro repetition in matching (macro_repetition_in_matching)
- [ ] macro repetition in transcription (macro_repetition_in_transcription)
- [ ] macro rule (macro_rule)
- [ ] macro statement (macro_statement)
- [ ] macro transcriber (macro_transcriber)
- [ ] macro transcription (macro_transcription)
- [ ] main function signature (main_function_signature)
- [ ] match arm (match_arm)
- [ ] match arm body (match_arm_body)
- [ ] match arm guard (match_arm_guard)
- [ ] match arm matcher (match_arm_matcher)
- [ ] match expression (match_expression)
- [ ] metavariable (metavariable)
- [ ] metavariable indication (metavariable_indication)
- [ ] method (method)
- [ ] method call expression (method_call_expression)
- [ ] method operand (method_operand)
- [ ] method resolution (method_resolution)
- [ ] mixed site hygiene (mixed_site_hygiene)
- [ ] modifying operand (modifying_operand)
- [ ] module (module)
- [ ] move type (move_type)
- [ ] multi segment path (multi_segment_path)
- [ ] multiplication assignment (multiplication_assignment)
- [ ] multiplication assignment expression (multiplication_assignment_expression)
- [ ] multiplication expression (multiplication_expression)
- [ ] mutability (mutability)
- [x] mutable (mutable)
- [ ] mutable assignee expression (mutable_assignee_expression)
- [ ] mutable binding (mutable_binding)
- [ ] mutable borrow (mutable_borrow)
- [ ] mutable borrow expression (mutable_borrow_expression)
- [ ] mutable place expression (mutable_place_expression)
- [ ] mutable place expression context (mutable_place_expression_context)
- [ ] mutable raw pointer type (mutable_raw_pointer_type)
- [ ] mutable reference (mutable_reference)
- [ ] mutable reference type (mutable_reference_type)
- [ ] mutable static (mutable_static)
- [ ] mutable variable (mutable_variable)

## macro (macro)

### Before glossary entry (origin/main)

```rst
.. _fls_sdkcn1exc9da:

macro
^^^^^

:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.
```

### After glossary entry (generated)

```rst
.. _fls_y2KjEwMtpv9y:

macro
^^^^^

:dp:`fls_FiXyUJmOWQuh`
 A :t:`macro` is a custom definition that extends Rust by defining callable syntactic transformations.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2yypq3m1kquj`
A :dt:`loop expression` is an :t:`expression` that evaluates a
:t:`block expression` continuously as long as some criterion holds true.


:dp:`fls_o2dyznhq7rez`
See :s:`LoopExpression`.

.. _fls_sdkcn1exc9da:

macro
^^^^^


:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2yypq3m1kquj`
A :dt:`loop expression` is an :t:`expression` that evaluates a
:t:`block expression` continuously as long as some criterion holds true.


:dp:`fls_o2dyznhq7rez`
See :s:`LoopExpression`.

.. _fls_sdkcn1exc9da:

macro
^^^^^


:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro expansion (macro_expansion)

### Before glossary entry (origin/main)

```rst
.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^

:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.
```

### After glossary entry (generated)

```rst
.. _fls_Nxtgv4hJL8YZ:

Macro expansion
^^^^^^^^^^^^^^^

:dp:`fls_wxDF04ySpeEG`
 :t:`Macro expansion <macro_expansion>` is the process of statically executing a :t:`macro invocation <macro_invocation>` and replacing it with the produced output of the :t:`macro invocation <macro_invocation>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_o2dyznhq7rez`
See :s:`LoopExpression`.

.. _fls_sdkcn1exc9da:

macro
^^^^^


:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_o2dyznhq7rez`
See :s:`LoopExpression`.

.. _fls_sdkcn1exc9da:

macro
^^^^^


:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro implementation function (macro_implementation_function)

### Before glossary entry (origin/main)

```rst
.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.
```

### After glossary entry (generated)

```rst
.. _fls_yqcqKYEM7NFh:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_QNiO7eKyJ2Z2`
 A :t:`macro implementation function <macro_implementation_function>` is the :t:`function` that encapsulates the syntactic transformations of a :t:`procedural macro <procedural_macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bt16qi8g2js5`
A :dt:`macro` is a custom definition that extends Rust by defining callable
syntactic transformations.

.. _fls_td4jm76u9m03:

macro expansion
^^^^^^^^^^^^^^^


:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro invocation (macro_invocation)

### Before glossary entry (origin/main)

```rst
.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^

:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.

:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.
```

### After glossary entry (generated)

```rst
.. _fls_xETQrrZ61cyX:

macro invocation
^^^^^^^^^^^^^^^^

:dp:`fls_c6grzxhvgiT0`
 A :t:`macro invocation <macro_invocation>` is a call of a :t:`declarative macro <declarative_macro>` or :t:`function-like macro <function_like_macro>` that is expanded statically and replaced with the result of the :t:`macro`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^


:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_t383uo1l4h8x`
:dt:`Macro expansion` is the process of statically executing a
:t:`macro invocation` and replacing it with the produced output of the
:t:`macro invocation`.

.. _fls_o5jy1u64nyiy:

macro implementation function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_xy4t1suhrn46`
A :dt:`macro implementation function` is the :t:`function` that encapsulates
the syntactic transformations of a :t:`procedural macro`.

.. _fls_20x9eqa7xeui:

macro invocation
^^^^^^^^^^^^^^^^


:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^


:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro match (macro_match)

### Before glossary entry (origin/main)

```rst
.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^

:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.

:dp:`fls_dww6sqbj2vin`
See :s:`MacroMatch`.
```

### After glossary entry (generated)

```rst
.. _fls_OQnZydW4CQDb:

macro match
^^^^^^^^^^^

:dp:`fls_NvajCWS1JPN2`
 A :t:`macro match <macro_match>` is the most basic form of a satisfied :t:`macro matcher <macro_matcher>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^


:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.


:dp:`fls_dww6sqbj2vin`
See :s:`MacroMatch`.

.. _fls_4h4snjd4thsv:

macro matcher
^^^^^^^^^^^^^


:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_5qtwcp5ns5vz`
A :dt:`macro invocation` is a call of a :t:`declarative macro` or
:t:`function-like macro` that is expanded statically and replaced with the
result of the :t:`macro`.


:dp:`fls_IgzL0OJ9Ja7y`
See :s:`MacroInvocation`.

.. _fls_boanb1ipzc9:

macro match
^^^^^^^^^^^


:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.


:dp:`fls_dww6sqbj2vin`
See :s:`MacroMatch`.

.. _fls_4h4snjd4thsv:

macro matcher
^^^^^^^^^^^^^


:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro matcher (macro_matcher)

### Before glossary entry (origin/main)

```rst
.. _fls_4h4snjd4thsv:

macro matcher
^^^^^^^^^^^^^

:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.

:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.
```

### After glossary entry (generated)

```rst
.. _fls_Ad4IUtSl6kFk:

macro matcher
^^^^^^^^^^^^^

:dp:`fls_e5VHnFriEJej`
 A :t:`macro matcher <macro_matcher>` is a :t:`construct` that describes a syntactic pattern that a :t:`macro` must match.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.


:dp:`fls_dww6sqbj2vin`
See :s:`MacroMatch`.

.. _fls_4h4snjd4thsv:

macro matcher
^^^^^^^^^^^^^


:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.


:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q0ve6nd287ta`
A :dt:`macro match` is the most basic form of a satisfied :t:`macro matcher`.


:dp:`fls_dww6sqbj2vin`
See :s:`MacroMatch`.

.. _fls_4h4snjd4thsv:

macro matcher
^^^^^^^^^^^^^


:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.


:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro matching (macro_matching)

### Before glossary entry (origin/main)

```rst
.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^

:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.
```

### After glossary entry (generated)

```rst
.. _fls_Aly65ZTbc2sx:

Macro matching
^^^^^^^^^^^^^^

:dp:`fls_JvA6Lo8O9F9P`
 :t:`Macro matching <macro_matching>` is the process of performing :t:`rule matching <rule_matching>` and :t:`token matching <token_matching>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.


:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_sqncf88chnsy`
A :dt:`macro matcher` is a :t:`construct` that describes a syntactic pattern
that a :t:`macro` must match.


:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro repetition (macro_repetition)

### Before glossary entry (origin/main)

```rst
.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^

:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.
```

### After glossary entry (generated)

```rst
.. _fls_OgkIhPnOHtSq:

macro repetition
^^^^^^^^^^^^^^^^

:dp:`fls_jF3scBCQ01dG`
 A :t:`macro repetition <macro_repetition>` is either a :t:`macro repetition in matching <macro_repetition_in_matching>` or a :t:`macro repetition in transcription <macro_repetition_in_transcription>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ioyegc6ggd7o`
See :s:`MacroMatcher`.

.. _fls_ao7GhE0C8MQO:

macro matching
^^^^^^^^^^^^^^


:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro repetition in matching (macro_repetition_in_matching)

### Before glossary entry (origin/main)

```rst
.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.

:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.
```

### After glossary entry (generated)

```rst
.. _fls_t4LAnuJEtpNT:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_b1JCsjisZRMn`
 A :t:`macro repetition in matching <macro_repetition_in_matching>` allows for a syntactic pattern to be matched zero or multiple times during :t:`macro matching <macro_matching>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_RrDmFXuZrhFT`
:dt:`Macro matching` is the process of performing :t:`rule matching` and
:t:`token matching`.

.. _fls_kddW7EirSn0g:

macro repetition
^^^^^^^^^^^^^^^^


:dp:`fls_sDomcFWIeUAT`
A :dt:`macro repetition` is either a :t:`macro repetition in matching` or a
:t:`macro repetition in transcription`.

.. _fls_a5j2hztrjfv5:

macro repetition in matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro repetition in transcription (macro_repetition_in_transcription)

### Before glossary entry (origin/main)

```rst
.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.

:dp:`fls_5wdiqbwgr9nt`
See :s:`MacroRepetitionTranscriber`.
```

### After glossary entry (generated)

```rst
.. _fls_cnOh7r7jRC1H:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_DRnpQ3oc4RHb`
 A :t:`macro repetition in transcription <macro_repetition_in_transcription>` allows for a syntactic pattern to be transcribed zero or multiple times during :t:`macro transcription <macro_transcription>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.


:dp:`fls_5wdiqbwgr9nt`
See :s:`MacroRepetitionTranscriber`.

.. _fls_gw31cagmzx26:

macro rule
^^^^^^^^^^


:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wio0e9qzstjh`
A :dt:`macro repetition in matching` allows for a syntactic pattern to be
matched zero or multiple times during :t:`macro matching`.


:dp:`fls_potk1y850zer`
See :s:`MacroRepetitionMatch`.

.. _fls_sqv126lwdz23:

macro repetition in transcription
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.


:dp:`fls_5wdiqbwgr9nt`
See :s:`MacroRepetitionTranscriber`.

.. _fls_gw31cagmzx26:

macro rule
^^^^^^^^^^


:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro rule (macro_rule)

### Before glossary entry (origin/main)

```rst
.. _fls_gw31cagmzx26:

macro rule
^^^^^^^^^^

:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.

:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.
```

### After glossary entry (generated)

```rst
.. _fls_U5BzMUarR5Rm:

macro rule
^^^^^^^^^^

:dp:`fls_LmmI6BEjs6ga`
 A :t:`macro rule <macro_rule>` is a :t:`construct` that consists of a :t:`macro matcher <macro_matcher>` and a :t:`macro transcriber <macro_transcriber>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.


:dp:`fls_5wdiqbwgr9nt`
See :s:`MacroRepetitionTranscriber`.

.. _fls_gw31cagmzx26:

macro rule
^^^^^^^^^^


:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.


:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ex9vd3w0t4wo`
A :dt:`macro repetition in transcription` allows for a syntactic pattern to be
transcribed zero or multiple times during :t:`macro transcription`.


:dp:`fls_5wdiqbwgr9nt`
See :s:`MacroRepetitionTranscriber`.

.. _fls_gw31cagmzx26:

macro rule
^^^^^^^^^^


:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.


:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro statement (macro_statement)

### Before glossary entry (origin/main)

```rst
.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^

:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.
```

### After glossary entry (generated)

```rst
.. _fls_OtICfq3nBt0f:

macro statement
^^^^^^^^^^^^^^^

:dp:`fls_gjWAR4gqh1Od`
 A :t:`macro statement <macro_statement>` is a :t:`statement` expressed as a :t:`terminated macro invocation <terminated_macro_invocation>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.


:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^


:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7gfdqggs33id`
A :dt:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher`
and a :t:`macro transcriber`.


:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^


:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro transcriber (macro_transcriber)

### Before glossary entry (origin/main)

```rst
.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^

:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.

:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.
```

### After glossary entry (generated)

```rst
.. _fls_8jouE2nEuuwF:

macro transcriber
^^^^^^^^^^^^^^^^^

:dp:`fls_lpnPH939FXAE`
 A :t:`macro transcriber <macro_transcriber>` is a :t:`construct` that describes the replacement syntax of a :t:`macro`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^


:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_qv68aj43mz5m`
See :s:`MacroRule`.

.. _fls_i4yf4lt8qvkt:

macro statement
^^^^^^^^^^^^^^^


:dp:`fls_yhh9k9epv3g6`
A :dt:`macro statement` is a :t:`statement` expressed as a
:t:`terminated macro invocation`.

.. _fls_76o6rjh6lrqd:

macro transcriber
^^^^^^^^^^^^^^^^^


:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## macro transcription (macro_transcription)

### Before glossary entry (origin/main)

```rst
.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^

:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.
```

### After glossary entry (generated)

```rst
.. _fls_ULZahEOGBaWB:

Macro transcription
^^^^^^^^^^^^^^^^^^^

:dp:`fls_W9QdH1aQUqCv`
 :t:`Macro transcription <macro_transcription>` is the process of producing the expansion of a :t:`declarative macro <declarative_macro>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ug79qf3p693h`
A :dt:`macro transcriber` is a :t:`construct` that describes the replacement
syntax of a :t:`macro`.


:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## main function signature (main_function_signature)

### Before glossary entry (origin/main)

```rst
.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.
```

### After glossary entry (generated)

```rst
.. _fls_mfoD586IaVz1:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_GHVXSFHsFaGp`
 A :t:`main function signature <main_function_signature>` is a :t:`function signature <function_signature>` subject to specific restrictions.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_myubuihvjl4s`
See :s:`MacroTranscriber`.

.. _fls_vdq3cphhpxmg:

macro transcription
^^^^^^^^^^^^^^^^^^^


:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## match arm (match_arm)

### Before glossary entry (origin/main)

```rst
.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^

:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.
```

### After glossary entry (generated)

```rst
.. _fls_Ap4ioNHZNtgO:

match arm
^^^^^^^^^

:dp:`fls_spH2arPeEjIN`
 A :t:`match arm <match_arm>` is a :t:`construct` that consists of a :t:`match arm matcher <match_arm_matcher>` and a :t:`match arm body <match_arm_body>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_nouiggbpipg`
:dt:`Macro transcription` is the process of producing the expansion of a
:t:`declarative macro`.

.. _fls_MJ1YWiOpxAa8:

main function signature
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## match arm body (match_arm_body)

### Before glossary entry (origin/main)

```rst
.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^

:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.
```

### After glossary entry (generated)

```rst
.. _fls_wFcLrtEYz1z3:

match arm body
^^^^^^^^^^^^^^

:dp:`fls_svIeOlRUN1Xx`
 A :t:`match arm body <match_arm_body>` is the :t:`operand` of a :t:`match arm <match_arm>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_QijObGZEIykU`
A :dt:`main function signature` is a :t:`function signature` subject to specific
restrictions.

.. _fls_fizf1byuspv2:

match arm
^^^^^^^^^


:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## match arm guard (match_arm_guard)

### Before glossary entry (origin/main)

```rst
.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^

:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.

:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.
```

### After glossary entry (generated)

```rst
.. _fls_S5pcxJpBJrZO:

match arm guard
^^^^^^^^^^^^^^^

:dp:`fls_s2Z2Kn5DN3NX`
 A :t:`match arm guard <match_arm_guard>` is a :t:`construct` that provides additional filtering to a :t:`match arm matcher <match_arm_matcher>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^


:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_z5qsy5z2zak3`
A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
and a :t:`match arm body`.

.. _fls_q7lcdtxuy1ac:

match arm body
^^^^^^^^^^^^^^


:dp:`fls_33e7oefx0xqm`
A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. _fls_aa1x6ajl4zid:

match arm guard
^^^^^^^^^^^^^^^


:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^


:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## match arm matcher (match_arm_matcher)

### Before glossary entry (origin/main)

```rst
.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^

:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.

:dp:`fls_j7i2bjvzz1tx`
See :s:`MatchArmMatcher`.
```

### After glossary entry (generated)

```rst
.. _fls_FfaYwwPN4ixZ:

match arm matcher
^^^^^^^^^^^^^^^^^

:dp:`fls_tmSEhFuVE9yV`
 A :t:`match arm matcher <match_arm_matcher>` is a :t:`construct` that consists of a :t:`pattern` and a :t:`match arm guard <match_arm_guard>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^


:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.


:dp:`fls_j7i2bjvzz1tx`
See :s:`MatchArmMatcher`.

.. _fls_w15uouo0sjao:

match expression
^^^^^^^^^^^^^^^^


:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_uhn07jmvv9ea`
A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
to a :t:`match arm matcher`.


:dp:`fls_ykf70vbng54n`
See :s:`MatchArmGuard`.

.. _fls_i3omadaygum2:

match arm matcher
^^^^^^^^^^^^^^^^^


:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.


:dp:`fls_j7i2bjvzz1tx`
See :s:`MatchArmMatcher`.

.. _fls_w15uouo0sjao:

match expression
^^^^^^^^^^^^^^^^


:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## match expression (match_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_w15uouo0sjao:

match expression
^^^^^^^^^^^^^^^^

:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.

:dp:`fls_wkalvzkmp95y`
See :s:`MatchExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_VC3GipQnKdYP:

match expression
^^^^^^^^^^^^^^^^

:dp:`fls_Tk3BOD77xQhV`
 A :t:`match expression <match_expression>` is an :t:`expression` that tries to match one of its multiple :t:`patterns <pattern>` against its :t:`subject expression <subject_expression>` and if it succeeds, evaluates an :t:`operand`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.


:dp:`fls_j7i2bjvzz1tx`
See :s:`MatchArmMatcher`.

.. _fls_w15uouo0sjao:

match expression
^^^^^^^^^^^^^^^^


:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.


:dp:`fls_wkalvzkmp95y`
See :s:`MatchExpression`.

.. _fls_xo9uyazcfuq3:

metavariable
^^^^^^^^^^^^


:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_paz9358w4cpu`
A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
and a :t:`match arm guard`.


:dp:`fls_j7i2bjvzz1tx`
See :s:`MatchArmMatcher`.

.. _fls_w15uouo0sjao:

match expression
^^^^^^^^^^^^^^^^


:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.


:dp:`fls_wkalvzkmp95y`
See :s:`MatchExpression`.

.. _fls_xo9uyazcfuq3:

metavariable
^^^^^^^^^^^^


:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## metavariable (metavariable)

### Before glossary entry (origin/main)

```rst
.. _fls_xo9uyazcfuq3:

metavariable
^^^^^^^^^^^^

:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.

:dp:`fls_k4xaw93z8x33`
See :s:`MacroMetavariable`.
```

### After glossary entry (generated)

```rst
.. _fls_SrL1S5qgK5Bt:

metavariable
^^^^^^^^^^^^

:dp:`fls_CcJFiO09JEAc`
 A :t:`metavariable` is a :t:`macro match <macro_match>` that describes a :t:`variable`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.


:dp:`fls_wkalvzkmp95y`
See :s:`MatchExpression`.

.. _fls_xo9uyazcfuq3:

metavariable
^^^^^^^^^^^^


:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.


:dp:`fls_k4xaw93z8x33`
See :s:`MacroMetavariable`.

.. _fls_5P2594jy7uDE:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2ohrphptjny6`
A :dt:`match expression` is an :t:`expression` that tries to match one of
its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
succeeds, evaluates an :t:`operand`.


:dp:`fls_wkalvzkmp95y`
See :s:`MatchExpression`.

.. _fls_xo9uyazcfuq3:

metavariable
^^^^^^^^^^^^


:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.


:dp:`fls_k4xaw93z8x33`
See :s:`MacroMetavariable`.

.. _fls_5P2594jy7uDE:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## metavariable indication (metavariable_indication)

### Before glossary entry (origin/main)

```rst
.. _fls_5P2594jy7uDE:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.

:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.
```

### After glossary entry (generated)

```rst
.. _fls_qoTPU6tYh3gi:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NqAPm40noyAb`
 A :t:`metavariable indication <metavariable_indication>` is a :t:`construct` that indicates a :t:`metavariable`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.


:dp:`fls_k4xaw93z8x33`
See :s:`MacroMetavariable`.

.. _fls_5P2594jy7uDE:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.


:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_fu1esz5i9mt`
A :dt:`metavariable` is a :t:`macro match` that describes a :t:`variable`.


:dp:`fls_k4xaw93z8x33`
See :s:`MacroMetavariable`.

.. _fls_5P2594jy7uDE:

metavariable indication
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.


:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## method (method)

### Before glossary entry (origin/main)

```rst
.. _fls_bi3g8xkk9ekf:

method
^^^^^^

:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
```

### After glossary entry (generated)

```rst
.. _fls_MKn1jE3sRTZY:

method
^^^^^^

:dp:`fls_VEhRMX7P5NTN`
 A :t:`method` is an :t:`associated function <associated_function>` with a :t:`self parameter <self_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.


:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_r1FxbWffC9Wt`
A :dt:`metavariable indication` is a :t:`construct` that indicates a
:t:`metavariable`.


:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## method call expression (method_call_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.

:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_XGrzx4ENBbCL:

method call expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_NYIsTpiZK6L5`
 A :t:`method call expression <method_call_expression>` is an :t:`expression` that invokes a :t:`method` of a :t:`variable`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^


:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bcMO2a0e0gXJ`
See :s:`MacroMetavariableIndication`.

.. _fls_bi3g8xkk9ekf:

method
^^^^^^


:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.

.. _fls_l4wel2551cw9:

method call expression
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^


:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## method operand (method_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^

:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.

:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_l4ZTt6Ac7jRx:

method operand
^^^^^^^^^^^^^^

:dp:`fls_Fowb62cBHnfq`
 A :t:`method operand <method_operand>` is an :t:`operand` that denotes the :t:`method` being invoked by a :t:`method call expression <method_call_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^


:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.


:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_367sod24edts`
A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
of a :t:`variable`.


:dp:`fls_ohhcvxcaqv11`
See :s:`MethodCallExpression`.

.. _fls_l6eJxvmplLqQ:

method operand
^^^^^^^^^^^^^^


:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.


:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## method resolution (method_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^

:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.
```

### After glossary entry (generated)

```rst
.. _fls_kuoXxGhTsb14:

Method resolution
^^^^^^^^^^^^^^^^^

:dp:`fls_nVGLmVygM2A4`
 :t:`Method resolution <method_resolution>` is a kind of :t:`resolution` that applies to a :t:`method call expression <method_call_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.


:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_VLLAFjAxCfkE`
A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
invoked by a :t:`method call expression`.


:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mixed site hygiene (mixed_site_hygiene)

### Before glossary entry (origin/main)

```rst
.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^

:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.
```

### After glossary entry (generated)

```rst
.. _fls_prAnJtWWxSFz:

partially hygienic
^^^^^^^^^^^^^^^^^^

:dp:`fls_ArXdnCnPWplc`
 :t:`Mixed site hygiene <mixed_site_hygiene>`, which resolves to a :s:`MacroRulesDeclaration <macrorulesdeclaration>` site for :t:`labels <label>`, :t:`variables <variable>`, and the ``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation <macroinvocation>` site otherwise, and is considered :t:`partially hygienic <partially_hygienic>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Pkgr4fJQZpJ6`
See :s:`MethodOperand`.

.. _fls_05yFh5Ud0YkW:

method resolution
^^^^^^^^^^^^^^^^^


:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## modifying operand (modifying_operand)

### Before glossary entry (origin/main)

```rst
.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^

:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.

:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.
```

### After glossary entry (generated)

```rst
.. _fls_PqkRQJ9GfMbH:

modifying operand
^^^^^^^^^^^^^^^^^

:dp:`fls_2umcwTBFxuLL`
 A :t:`modifying operand <modifying_operand>` is an :t:`operand` that supplies the :t:`value` that is used in the calculation of a :t:`compound assignment expression <compound_assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^


:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_LbW4z6OTuD1l`
:dt:`Method resolution` is a kind of :t:`resolution` that applies to a
:t:`method call expression`.

.. _fls_2FFRdj5cO0ks:

mixed site hygiene
^^^^^^^^^^^^^^^^^^


:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.

.. _fls_5hoe1v960xfi:

modifying operand
^^^^^^^^^^^^^^^^^


:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^


:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## module (module)

### Before glossary entry (origin/main)

```rst
.. _fls_kbxk78vm564e:

module
^^^^^^

:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.

:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_pB5TqwIREtMl:

module
^^^^^^

:dp:`fls_Spp9kSY4Nl2V`
 A :t:`module` is a container for zero or more :t:`items <item>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^


:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.


:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_9wt2l5gg06pb`
A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.


:dp:`fls_qnwbrwdnv7n0`
See :s:`ModifyingOperand`.

.. _fls_kbxk78vm564e:

module
^^^^^^


:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.


:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## move type (move_type)

### Before glossary entry (origin/main)

```rst
.. _fls_gnucgrytswa4:

move type
^^^^^^^^^

:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.
```

### After glossary entry (generated)

```rst
.. _fls_DE8aoCm8mn09:

move type
^^^^^^^^^

:dp:`fls_KQoXpDGyojgN`
 A :t:`move type <move_type>` is a :t:`type` that implements the `core::marker::Sized <https://doc.rust-lang.org/stable/std/?search=core%3A%3Amarker%3A%3ASized>`__ :t:`trait` and that is not a :t:`copy type <copy_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.


:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ujlsg58bskl5`
A :dt:`module` is a container for zero or more :t:`[item]s`.


:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## multi segment path (multi_segment_path)

### Before glossary entry (origin/main)

```rst
.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^

:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.
```

### After glossary entry (generated)

```rst
.. _fls_cmzKhIci8uuJ:

multi segment path
^^^^^^^^^^^^^^^^^^

:dp:`fls_zidEx3ehm0nB`
 A :t:`multi segment path <multi_segment_path>` is a :t:`path` consisting of more than one :t:`path segment <path_segment>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_os60q6vvm71c`
See :s:`ModuleDeclaration`.

.. _fls_gnucgrytswa4:

move type
^^^^^^^^^


:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## multiplication assignment (multiplication_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.
```

### After glossary entry (generated)

```rst
.. _fls_9EJTYuSiJz8E:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_o80e9Sk0r1Qj`
 For :t:`multiplication assignment <multiplication_assignment>`, see :t:`multiplication assignment expression <multiplication_assignment_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_ri37ez31gai8`
A :dt:`move type` is a :t:`type` that implements the :std:`core::marker::Sized`
:t:`trait` and that is not a :t:`copy type`.

.. _fls_iw2vYgmLhlsg:

multi segment path
^^^^^^^^^^^^^^^^^^


:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## multiplication assignment expression (multiplication_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.

:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_vO4ivA7xQ17N:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_s91E157Uebnf`
 A :t:`multiplication assignment expression <multiplication_assignment_expression>` is a :t:`compound assignment expression <compound_assignment_expression>` that uses multiplication.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

.. _fls_lpSCLhnaxeCg:

multiplication assignment
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.

.. _fls_yo4k6lk0tizn:

multiplication assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## multiplication expression (multiplication_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.

:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_9QvGweNm71zj:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_gX1alPeg3tTy`
 A :t:`multiplication expression <multiplication_expression>` is an :t:`arithmetic expression <arithmetic_expression>` that uses multiplication.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.


:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_eo9gx05n5ru3`
A :dt:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.


:dp:`fls_b0dc5lec1mdc`
See :s:`MultiplicationAssignmentExpression`.

.. _fls_bgtznqqgtmd8:

multiplication expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.


:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutability (mutability)

### Before glossary entry (origin/main)

```rst
.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^

:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.
```

### After glossary entry (generated)

```rst
.. _fls_rKbbAudzStc3:

Mutability
^^^^^^^^^^

:dp:`fls_JOvrcyfy5qp7`
 :t:`Mutability <mutability>` determines whether a :t:`construct` can modify a :t:`value`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.


:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_324qh8wz474b`
A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
multiplication.


:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable (mutable)

### Before glossary entry (origin/main)

```rst
.. _fls_wvejcadmzt5p:

mutable
^^^^^^^

:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_34bkl5i75q5`
See :s:`MultiplicationExpression`.

.. _fls_yM11Bcxn4p7c:

mutability
^^^^^^^^^^


:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable assignee expression (mutable_assignee_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.
```

### After glossary entry (generated)

```rst
.. _fls_LXOstwqqxLD5:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_LSLe9Gq5Klud`
 A :t:`mutable assignee expression <mutable_assignee_expression>` is an :t:`assignee expression <assignee_expression>` whose :t:`value` can be modified.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lBrXj9lo4s6o`
:dt:`Mutability` determines whether a :t:`construct` can modify a :t:`value`.

.. _fls_wvejcadmzt5p:

mutable
^^^^^^^


:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable binding (mutable_binding)

### Before glossary entry (origin/main)

```rst
.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^

:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.
```

### After glossary entry (generated)

```rst
.. _fls_pTQNtSsUtJd9:

mutable binding
^^^^^^^^^^^^^^^

:dp:`fls_gTa4qDHvrWbP`
 A :t:`mutable binding <mutable_binding>` is a :t:`binding` whose :t:`value` can be modified.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_dqm58deu1orn`
A :t:`value` is :dt:`mutable` when it can be modified.

.. _fls_TEVPHHiCMByO:

mutable assignee expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable borrow (mutable_borrow)

### Before glossary entry (origin/main)

```rst
.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^

:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.
```

### After glossary entry (generated)

```rst
.. _fls_KSBgoFdljfEp:

mutable borrow
^^^^^^^^^^^^^^

:dp:`fls_4KShNpuwPZK9`
 A :t:`mutable borrow <mutable_borrow>` is a :t:`mutable reference <mutable_reference>` produced by :t:`borrowing`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.

.. _fls_ntaA0NtJ9z5h:

mutable binding
^^^^^^^^^^^^^^^


:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable borrow expression (mutable_borrow_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.
```

### After glossary entry (generated)

```rst
.. _fls_MplnCRyhYNbh:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_okAumAE4XGKn`
 A :t:`mutable borrow expression <mutable_borrow_expression>` is a :t:`borrow expression <borrow_expression>` that has :t:`keyword` ``mut``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_v2pGKVaQjtcl`
A :dt:`mutable binding` is a :t:`binding` whose :t:`value` can be modified.

.. _fls_iku91jwdtdr1:

mutable borrow
^^^^^^^^^^^^^^


:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable place expression (mutable_place_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.
```

### After glossary entry (generated)

```rst
.. _fls_YYim1ASfQjXg:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_J576n0jXDMgN`
 A :t:`mutable place expression <mutable_place_expression>` is a :t:`place expression <place_expression>` whose memory location can be modified.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_5knwbyz4fd9z`
A :dt:`mutable borrow` is a :t:`mutable reference` produced by :t:`borrowing`.

.. _fls_kw3oiotr98tt:

mutable borrow expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable place expression context (mutable_place_expression_context)

### Before glossary entry (origin/main)

```rst
.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.
```

### After glossary entry (generated)

```rst
.. _fls_TmAv7Scy2Tyf:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_KxDZeIrI1XmP`
 A :t:`mutable place expression context <mutable_place_expression_context>` is a :t:`place expression context <place_expression_context>` that may evaluate its :t:`operand` as a mutable memory location.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_80kcc4y21hu6`
A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
:t:`keyword` ``mut``.

.. _fls_7eyza445ew53:

mutable place expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable raw pointer type (mutable_raw_pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.
```

### After glossary entry (generated)

```rst
.. _fls_y207fWYMYL51:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_HkvQndtAhh68`
 A :t:`mutable raw pointer type <mutable_raw_pointer_type>` is a :t:`raw pointer type <raw_pointer_type>` subject to :t:`keyword` ``mut``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_kq877s3vij70`
A :dt:`mutable place expression` is a :t:`place expression` whose memory
location can be modified.

.. _fls_x5BKVLc4KDlK:

mutable place expression context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable reference (mutable_reference)

### Before glossary entry (origin/main)

```rst
.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^

:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.
```

### After glossary entry (generated)

```rst
.. _fls_wS0Yz9s46PLc:

mutable reference
^^^^^^^^^^^^^^^^^

:dp:`fls_12WowB6maEDM`
 A :t:`mutable reference <mutable_reference>` is a :t:`value` of a :t:`mutable reference type <mutable_reference_type>`, and allows the mutation of its :t:`referent`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2ixH8LWGHi3k`
A :dt:`mutable place expression context` is a :t:`place expression context`
that may evaluate its :t:`operand` as a mutable memory location.

.. _fls_wOvlW47jKEWF:

mutable raw pointer type
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable reference type (mutable_reference_type)

### Before glossary entry (origin/main)

```rst
.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.
```

### After glossary entry (generated)

```rst
.. _fls_2qjH9P8estvC:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wUjRfljqgwgv`
 A :t:`mutable reference type <mutable_reference_type>` is a :t:`reference type <reference_type>` subject to :t:`keyword` ``mut``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_86SFxSDRcC06`
A :dt:`mutable raw pointer type` is a :t:`raw pointer type` subject to
:t:`keyword` ``mut``.

.. _fls_jtzj092hyjkz:

mutable reference
^^^^^^^^^^^^^^^^^


:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable static (mutable_static)

### Before glossary entry (origin/main)

```rst
.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^

:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.
```

### After glossary entry (generated)

```rst
.. _fls_Jq3Mbt6Gp6Fy:

mutable static
^^^^^^^^^^^^^^

:dp:`fls_cWH9o2n8SO0c`
 A :t:`mutable static <mutable_static>` is a :t:`static` whose :t:`value` can be modified.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^


:dp:`fls_jjpzrs38vs3y`
A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_wujjrhm1d338`
A :dt:`mutable reference` is a :t:`value` of a :t:`mutable reference type`, and
allows the mutation of its :t:`referent`.

.. _fls_8iq0wcczl465:

mutable reference type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^


:dp:`fls_jjpzrs38vs3y`
A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## mutable variable (mutable_variable)

### Before glossary entry (origin/main)

```rst
.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^

:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.
```

### After glossary entry (generated)

```rst
.. _fls_cqiF4fEjhm4w:

mutable variable
^^^^^^^^^^^^^^^^

:dp:`fls_kH752VkmgA6D`
 A :t:`mutable variable <mutable_variable>` is a :t:`variable` whose :t:`value` can be modified.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^


:dp:`fls_jjpzrs38vs3y`
A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.


:dp:`fls_yrzevg5kd4bi`
See :s:`Name`.

.. _fls_CxzbzLu4pWPY:

named block expression
^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q06p9tclwaaw`
A :dt:`mutable reference type` is a :t:`reference type` subject to :t:`keyword`
``mut``.

.. _fls_omgyj7yxwgua:

mutable static
^^^^^^^^^^^^^^


:dp:`fls_3ss4bokujaby`
A :dt:`mutable static` is a :t:`static` whose :t:`value` can be modified.

.. _fls_n7h4xr40xwgb:

mutable variable
^^^^^^^^^^^^^^^^


:dp:`fls_kjjv9jvdpf2o`
A :dt:`mutable variable` is a :t:`variable` whose :t:`value` can be modified.

.. _fls_kad7fzn94x4d:

name
^^^^


:dp:`fls_jjpzrs38vs3y`
A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.


:dp:`fls_yrzevg5kd4bi`
See :s:`Name`.

.. _fls_CxzbzLu4pWPY:

named block expression
^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
