# Glossary audit P

## Per-letter checklist
- Letter: P
- [ ] Reconcile P terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate P terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for P
- [ ] Update `migration-checklist.md` for all P terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint P migration`
- [ ] Letter complete

## Term checklist
- [ ] panic (panic)
- [ ] parenthesized expression (parenthesized_expression)
- [ ] parenthesized pattern (parenthesized_pattern)
- [ ] parenthesized type (parenthesized_type)
- [x] partially hygienic (partially_hygienic)
- [ ] passing convention (passing_convention)
- [ ] path (path)
- [ ] path expression (path_expression)
- [ ] path expression resolution (path_expression_resolution)
- [ ] path pattern (path_pattern)
- [ ] path resolution (path_resolution)
- [ ] path segment (path_segment)
- [ ] pattern (pattern)
- [ ] pattern-without-alternation (pattern_without_alternation)
- [ ] pattern-without-range (pattern_without_range)
- [ ] place (place)
- [ ] place expression (place_expression)
- [ ] place expression context (place_expression_context)
- [x] plane (plane)
- [ ] pointer (pointer)
- [ ] pointer type (pointer_type)
- [ ] positional register argument (positional_register_argument)
- [ ] precedence (precedence)
- [ ] prelude (prelude)
- [ ] prelude entity (prelude_entity)
- [ ] prelude name (prelude_name)
- [ ] primitive representation (primitive_representation)
- [ ] principal trait (principal_trait)
- [ ] private visibility (private_visibility)
- [ ] procedural macro (procedural_macro)
- [ ] program entry point (program_entry_point)
- [ ] public visibility (public_visibility)
- [ ] punctuator (punctuator)
- [ ] pure identifier (pure_identifier)

## panic (panic)

### Before glossary entry (origin/main)

```rst
.. _fls_wzpivxkhpln:

panic
^^^^^

:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.
```

### After glossary entry (generated)

```rst
.. _fls_IArY7olaohcR:

panic
^^^^^

:dp:`fls_Pa7Kel2B6MsU`
 A :t:`panic` is an abnormal program state caused by invoking :t:`macro` `core::panic <https://doc.rust-lang.org/stable/std/?search=core%3A%3Apanic>`__.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7vwwhberexeb`
An :dt:`owner` is a :t:`variable` that holds a :t:`value`.

.. _fls_1gmetz8qtr0l:

ownership
^^^^^^^^^


:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## parenthesized expression (parenthesized_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.

:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_mWvbwxpDBekw:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_1Hs78ulU2bT5`
 A :t:`parenthesized expression <parenthesized_expression>` is an :t:`expression` that groups other expressions.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_tu4zt8twucsz`
:dt:`Ownership` is a property of :t:`[value]s` that is central to the resource
management model of Rust.

.. _fls_wzpivxkhpln:

panic
^^^^^


:dp:`fls_t3kpbnmohtp6`
A :dt:`panic` is an abnormal program state caused by invoking :t:`macro`
:std:`core::panic`.

.. _fls_fl56jfxbj0f:

parenthesized expression
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## parenthesized pattern (parenthesized_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.

:dp:`fls_rwt31e8m694i`
See :s:`ParenthesizedPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_HErxqr7VzzuF:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tLDjaibdHvre`
 A :t:`parenthesized pattern <parenthesized_pattern>` is a :t:`pattern` that controls the precedence of its :t:`subpatterns <subpattern>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.


:dp:`fls_rwt31e8m694i`
See :s:`ParenthesizedPattern`.

.. _fls_gilx8zikdq9k:

parenthesized type
^^^^^^^^^^^^^^^^^^


:dp:`fls_pamypc7t7l5n`
A :dt:`parenthesized type` is a :t:`type` that disambiguates the interpretation
of :t:`[lexical element]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_yu1x2rr7cewa`
A :dt:`parenthesized expression` is an :t:`expression` that groups other
expressions.


:dp:`fls_p9exa6fpplfu`
See :s:`ParenthesizedExpression`.

.. _fls_ww6nyinsw1lr:

parenthesized pattern
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.


:dp:`fls_rwt31e8m694i`
See :s:`ParenthesizedPattern`.

.. _fls_gilx8zikdq9k:

parenthesized type
^^^^^^^^^^^^^^^^^^


:dp:`fls_pamypc7t7l5n`
A :dt:`parenthesized type` is a :t:`type` that disambiguates the interpretation
of :t:`[lexical element]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## parenthesized type (parenthesized_type)

### Before glossary entry (origin/main)

```rst
.. _fls_gilx8zikdq9k:

parenthesized type
^^^^^^^^^^^^^^^^^^

:dp:`fls_pamypc7t7l5n`
A :dt:`parenthesized type` is a :t:`type` that disambiguates the interpretation
of :t:`[lexical element]s`.

:dp:`fls_lovkvqoni3xs`
See :s:`ParenthesizedTypeSpecification`.
```

### After glossary entry (generated)

```rst
.. _fls_mZZICUliBBgH:

parenthesized type
^^^^^^^^^^^^^^^^^^

:dp:`fls_7AWoyQyQ8Xje`
 A :t:`parenthesized type <parenthesized_type>` is a :t:`type` that disambiguates the interpretation of :t:`lexical elements <lexical_element>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.


:dp:`fls_rwt31e8m694i`
See :s:`ParenthesizedPattern`.

.. _fls_gilx8zikdq9k:

parenthesized type
^^^^^^^^^^^^^^^^^^


:dp:`fls_pamypc7t7l5n`
A :dt:`parenthesized type` is a :t:`type` that disambiguates the interpretation
of :t:`[lexical element]s`.


:dp:`fls_lovkvqoni3xs`
See :s:`ParenthesizedTypeSpecification`.

.. _fls_fULM1oCKSakS:

partially hygienic
^^^^^^^^^^^^^^^^^^


:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_7j12dwsx9ghg`
A :dt:`parenthesized pattern` is a :t:`pattern` that controls the precedence of
its :t:`[subpattern]s`.


:dp:`fls_rwt31e8m694i`
See :s:`ParenthesizedPattern`.

.. _fls_gilx8zikdq9k:

parenthesized type
^^^^^^^^^^^^^^^^^^


:dp:`fls_pamypc7t7l5n`
A :dt:`parenthesized type` is a :t:`type` that disambiguates the interpretation
of :t:`[lexical element]s`.


:dp:`fls_lovkvqoni3xs`
See :s:`ParenthesizedTypeSpecification`.

.. _fls_fULM1oCKSakS:

partially hygienic
^^^^^^^^^^^^^^^^^^


:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :t:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## partially hygienic (partially_hygienic)

### Before glossary entry (origin/main)

```rst
.. _fls_fULM1oCKSakS:

partially hygienic
^^^^^^^^^^^^^^^^^^

:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.
```

### After glossary entry (generated)

```rst
.. _fls_prAnJtWWxSFz:

partially hygienic
^^^^^^^^^^^^^^^^^^

:dp:`fls_ArXdnCnPWplc`
An :t:`identifier` is :t:`partially hygienic` when it has
:t:`mixed site hygiene`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_uyvnq88y9gk3`
:dt:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
:t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
considered :t:`partially hygienic`.

:dp:`fls_4bTKuwDSu5FJ`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.

:dp:`fls_94TOYfoplm4f`
An :t:`identifier` is :dt:`unhygienic` when it has :t:`call site hygiene`.

:dp:`fls_jGq0s5E0T9fd`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.
```

### After chapter excerpt (current)

```rst
macros.rst
:dp:`fls_o9rwz9z0a2h4`
where the :t:`metavariable` of the :t:`macro repetition in matching` are
repeated ``N`` times, and the :t:`[metavariable indication]s` of the
:t:`macro repetition in transcription` are repeated ``N`` times. Invoking such
a :t:`macro` relates the first :t:`metavariable` argument of the
:t:`macro invocation` with the first :t:`metavariable` of the
:t:`macro repetition in matching`, the second :t:`metavariable` argument with
the second :t:`metavariable`, and so on.

.. _fls_xlfo7di0gsqz:

Hygiene
-------


:dp:`fls_7ezc7ncs678f`
:t:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
within them, which aims to eliminate the syntactic interference between a
:t:`macro` and its environment.

.. rubric:: Legality Rules


:dp:`fls_3axjf28xb1nt`
:t:`Hygiene` is categorized as follows:

* :dp:`fls_dz2mvodl818d`
  :t:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference
  the environment of the :s:`MacroRulesDeclaration`, cannot be referenced by the
  environment of a :s:`MacroInvocation`, and are considered :t:`hygienic`.

* :dp:`fls_puqhytfzfsg6`
  :t:`Call site hygiene`, which resolves to a :s:`MacroInvocation` site.
  :t:`[Identifier]s` with :t:`call site hygiene` can reference the environment
  of the :s:`MacroRulesDeclaration`, can reference the environment of the
  :s:`MacroInvocation`, and are considered :t:`unhygienic`.

* :dp:`fls_uyvnq88y9gk3`
  :t:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
  :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
  considered :dt:`partially hygienic`.


:dp:`fls_yxqcr19dig18`
Every :t:`macro` has associated :t:`hygiene` that depends on its kind:

* :dp:`fls_kx25olky1jov`
  :t:`[Declarative macro]s` have :t:`mixed site hygiene`.

* :dp:`fls_v46v0t2vh6x4`
  :t:`[Procedural macro]s` have :t:`call site hygiene` and
  :t:`mixed site hygiene` depending on the implementation of the
  :t:`procedural macro`.


:dp:`fls_7eqqk2cj0clr`
The :t:`metavariable` ``$crate`` in a :t:`declarative macro`'s expansion refers
to the crate the :t:`declarative macro` was declared in.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## passing convention (passing_convention)

### Before glossary entry (origin/main)

```rst
.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^

:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.
```

### After glossary entry (generated)

```rst
.. _fls_LpAx96MeiSW9:

passing convention
^^^^^^^^^^^^^^^^^^

:dp:`fls_rWTdObVaf2st`
 A :t:`passing convention <passing_convention>` is the mechanism that defines how a :t:`value` is transferred between :t:`places <place>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lovkvqoni3xs`
See :s:`ParenthesizedTypeSpecification`.

.. _fls_fULM1oCKSakS:

partially hygienic
^^^^^^^^^^^^^^^^^^


:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^


:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_lovkvqoni3xs`
See :s:`ParenthesizedTypeSpecification`.

.. _fls_fULM1oCKSakS:

partially hygienic
^^^^^^^^^^^^^^^^^^


:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :t:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^


:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path (path)

### Before glossary entry (origin/main)

```rst
.. _fls_9zl72vtkgkuo:

path
^^^^

:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
```

### After glossary entry (generated)

```rst
.. _fls_G7oDed7dZx63:

path
^^^^

:dp:`fls_W9gDfIROE1xZ`
 A :t:`path` is a sequence of :t:`path segments <path_segment>` logically separated by :t:`namespace qualifier <namespace_qualifier>` ``::`` that resolves to an :t:`entity`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^


:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :t:`partially hygienic` when it has
:t:`mixed site hygiene`.

.. _fls_wqbd5lxki2al:

passing convention
^^^^^^^^^^^^^^^^^^


:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path expression (path_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^

:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.

:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_vOfiBeBQcxmL:

path expression
^^^^^^^^^^^^^^^

:dp:`fls_Nf0bwm2gbf6j`
 A :t:`path expression <path_expression>` is a :t:`path` that acts as an :t:`expression`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_eqgsg8j9btic`
A :dt:`passing convention` is the mechanism that defines how a :t:`value` is
transferred between :t:`[place]s`.

.. _fls_9zl72vtkgkuo:

path
^^^^


:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

.. _fls_1xdj34py8zc3:

path expression
^^^^^^^^^^^^^^^


:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path expression resolution (path_expression_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.
```

### After glossary entry (generated)

```rst
.. _fls_a7EAmoX3wMuL:

Path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_02a6uu0HBkE0`
 :t:`Path expression resolution <path_expression_resolution>` is a form of :t:`path resolution <path_resolution>` that applies to a :t:`path expression <path_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^


:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4ik66nmvx5hn`
A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.


:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^


:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path pattern (path_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^

:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.

:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.
```

### After glossary entry (generated)

```rst
.. _fls_CWtOsMm86Xci:

path pattern
^^^^^^^^^^^^

:dp:`fls_ECRc7zFHnMGh`
 A :t:`path pattern <path_pattern>` is a :t:`pattern` that matches a :t:`constant`, a :t:`unit enum variant <unit_enum_variant>`, or a :t:`unit struct constant <unit_struct_constant>` indicated by a :t:`path`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^


:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_3qjpjqm0legc`
See :s:`PathExpression`.

.. _fls_EIFtIeLGZNy5:

path expression resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_WYcEVyc3SHuK`
:dt:`Path expression resolution` is a form of :t:`path resolution` that applies
to a :t:`path expression`.

.. _fls_ptikwcw3b20l:

path pattern
^^^^^^^^^^^^


:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path resolution (path_resolution)

### Before glossary entry (origin/main)

```rst
.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^

:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.
```

### After glossary entry (generated)

```rst
.. _fls_JNNJNcZjkNvz:

Path resolution
^^^^^^^^^^^^^^^

:dp:`fls_u7trwGQsHYdW`
 :t:`Path resolution <path_resolution>` is a form of :t:`resolution` that applies to a :t:`path`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^


:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_vacvk3t26ctg`
A :dt:`path pattern` is a :t:`pattern` that matches a :t:`constant`, a
:t:`unit enum variant`, or a :t:`unit struct constant` indicated by a
:t:`path`.


:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^


:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## path segment (path_segment)

### Before glossary entry (origin/main)

```rst
.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^

:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.

:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.
```

### After glossary entry (generated)

```rst
.. _fls_VbHN3JHp4p0O:

path segment
^^^^^^^^^^^^

:dp:`fls_EB0o2LCTqCdv`
 A :t:`path segment <path_segment>` is a constituent of a :t:`path`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^


:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^


:dp:`fls_9wwt9k1xlm6n`
A :dt:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies
all the criteria of the pattern.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_9fudbxoyq8k4`
See :s:`PathPattern`.

.. _fls_J8kiBhcawvnj:

path resolution
^^^^^^^^^^^^^^^


:dp:`fls_uy9Ai9vwTkjB`
:dt:`Path resolution` is a form of :t:`resolution` that applies to a :t:`path`.

.. _fls_xb54s9cs7h08:

path segment
^^^^^^^^^^^^


:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^


:dp:`fls_9wwt9k1xlm6n`
A :dt:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies
all the criteria of the pattern.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pattern (pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_uj1o721im5lb:

pattern
^^^^^^^

:dp:`fls_9wwt9k1xlm6n`
A :dt:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies
all the criteria of the pattern.

:dp:`fls_9va04w9jgdyp`
See :s:`Pattern`.
```

### After glossary entry (generated)

```rst
.. _fls_6jaoCsYpsMGa:

pattern
^^^^^^^

:dp:`fls_PTBj7Lh1utVo`
 A :t:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies all the criteria of the pattern.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^


:dp:`fls_9wwt9k1xlm6n`
A :dt:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies
all the criteria of the pattern.


:dp:`fls_9va04w9jgdyp`
See :s:`Pattern`.

.. _fls_48mv0zecb0un:

pattern matching
^^^^^^^^^^^^^^^^


:dp:`fls_y3oputy9e0sz`
:t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.

.. _fls_cptagvgpgnze:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.


:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.

.. _fls_uj1o721im5lb:

pattern
^^^^^^^


:dp:`fls_9wwt9k1xlm6n`
A :dt:`pattern` is a :t:`construct` that matches a :t:`value` which satisfies
all the criteria of the pattern.


:dp:`fls_9va04w9jgdyp`
See :s:`Pattern`.

.. _fls_48mv0zecb0un:

pattern matching
^^^^^^^^^^^^^^^^


:dp:`fls_y3oputy9e0sz`
:t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.

.. _fls_cptagvgpgnze:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pattern-without-alternation (pattern_without_alternation)

### Before glossary entry (origin/main)

```rst
.. _fls_cptagvgpgnze:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_brussjs3wo6r`
A :dt:`pattern-without-alternation` is a :t:`pattern` that cannot be alternated.

:dp:`fls_fmysn3eezr54`
See :s:`PatternWithoutAlternation`.
```

### After glossary entry (generated)

```rst
.. _fls_ybhZy2Pi1uSr:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_6WLGQ6Wt2pI2`
 A :t:`pattern-without-alternation <pattern_without_alternation>` is a :t:`pattern` that cannot be alternated.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_9va04w9jgdyp`
See :s:`Pattern`.

.. _fls_48mv0zecb0un:

pattern matching
^^^^^^^^^^^^^^^^


:dp:`fls_y3oputy9e0sz`
:t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.

.. _fls_cptagvgpgnze:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_brussjs3wo6r`
A :dt:`pattern-without-alternation` is a :t:`pattern` that cannot be alternated.


:dp:`fls_fmysn3eezr54`
See :s:`PatternWithoutAlternation`.

.. _fls_yeQOZKPoNzw3:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_9va04w9jgdyp`
See :s:`Pattern`.

.. _fls_48mv0zecb0un:

pattern matching
^^^^^^^^^^^^^^^^


:dp:`fls_y3oputy9e0sz`
:t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.

.. _fls_cptagvgpgnze:

pattern-without-alternation
^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_brussjs3wo6r`
A :dt:`pattern-without-alternation` is a :t:`pattern` that cannot be alternated.


:dp:`fls_fmysn3eezr54`
See :s:`PatternWithoutAlternation`.

.. _fls_yeQOZKPoNzw3:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pattern-without-range (pattern_without_range)

### Before glossary entry (origin/main)

```rst
.. _fls_yeQOZKPoNzw3:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.

:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.
```

### After glossary entry (generated)

```rst
.. _fls_w5lLwO4eA9bq:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_ylrji1wnRh6c`
 A :t:`pattern-without-range <pattern_without_range>` is a :t:`pattern-without-alternation <pattern_without_alternation>` that excludes :t:`range patterns <range_pattern>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_brussjs3wo6r`
A :dt:`pattern-without-alternation` is a :t:`pattern` that cannot be alternated.


:dp:`fls_fmysn3eezr54`
See :s:`PatternWithoutAlternation`.

.. _fls_yeQOZKPoNzw3:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.


:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_brussjs3wo6r`
A :dt:`pattern-without-alternation` is a :t:`pattern` that cannot be alternated.


:dp:`fls_fmysn3eezr54`
See :s:`PatternWithoutAlternation`.

.. _fls_yeQOZKPoNzw3:

pattern-without-range
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.


:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## place (place)

### Before glossary entry (origin/main)

```rst
.. _fls_5zjHBZMsCqJZ:

place
^^^^^

:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.
```

### After glossary entry (generated)

```rst
.. _fls_pNYa29Im0Gkn:

place
^^^^^

:dp:`fls_x0XtOMuma2bB`
 A :t:`place` is a location where a :t:`value` resides.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.


:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_LSEOvAwUM7g6`
A :dt:`pattern-without-range` is a :t:`pattern-without-alternation` that
excludes :t:`[range pattern]s`.


:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## place expression (place_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^

:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.
```

### After glossary entry (generated)

```rst
.. _fls_LIMtpIzHntv1:

place expression
^^^^^^^^^^^^^^^^

:dp:`fls_tlGj5nrhvTex`
 A :t:`place expression <place_expression>` is an :t:`expression` that represents a memory location.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Rj8ir4k0K811`
See :s:`PatternWithoutRange`.

.. _fls_5zjHBZMsCqJZ:

place
^^^^^


:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## place expression context (place_expression_context)

### Before glossary entry (origin/main)

```rst
.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.
```

### After glossary entry (generated)

```rst
.. _fls_tbFfPq5gN1et:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_dgXQEvt2i6mY`
 A :t:`place expression context <place_expression_context>` is a :t:`construct` that may evaluate its operand as a memory location.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.

.. _fls_7x6jhh0sz2f:

place expression
^^^^^^^^^^^^^^^^


:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## plane (plane)

### Before glossary entry (origin/main)

```rst
.. _fls_dr6wbsqjd2qm:

plane
^^^^^

:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.
```

### After glossary entry (generated)

```rst
(missing)
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_z6mgu2mk142r`
A :dt:`place expression` is an :t:`expression` that represents a memory
location.

.. _fls_tshbqttxdox1:

place expression context
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pointer (pointer)

### Before glossary entry (origin/main)

```rst
.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^

:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.
```

### After glossary entry (generated)

```rst
.. _fls_PgiAvvc5gYq3:

pointer
^^^^^^^

:dp:`fls_FwT0aFAS2g4N`
 A :t:`pointer` is a :t:`value` of a :t:`pointer type <pointer_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_fqcx8suiy5k`
A :dt:`place expression context` is a :t:`construct` that may evaluate its
operand as a memory location.

.. _fls_dr6wbsqjd2qm:

plane
^^^^^


:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pointer type (pointer_type)

### Before glossary entry (origin/main)

```rst
.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^

:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.
```

### After glossary entry (generated)

```rst
.. _fls_NiKkdVomblHe:

pointer type
^^^^^^^^^^^^

:dp:`fls_UUXawTOQ8LcY`
 A :t:`pointer type <pointer_type>` is a :t:`type` whose values indicate memory locations.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_x1wbguoqdsf9`
In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
:t:`[code point]s`.

.. _fls_HnJEHyUiTpb1:

pointer
^^^^^^^


:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## positional register argument (positional_register_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.
```

### After glossary entry (generated)

```rst
.. _fls_rZuXhxJrio0y:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_CJedoocqicRk`
 A :t:`positional register argument <positional_register_argument>` is a :t:`register argument <register_argument>` whose configuration is not bound to an :t:`identifier`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_DRjhMWo9mjoF`
A :dt:`pointer` is a :t:`value` of a :t:`pointer type`.

.. _fls_o5o1ssqqD7Jg:

pointer type
^^^^^^^^^^^^


:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## precedence (precedence)

### Before glossary entry (origin/main)

```rst
.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^

:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.
```

### After glossary entry (generated)

```rst
.. _fls_exAMjxWALDQ6:

Precedence
^^^^^^^^^^

:dp:`fls_IPHc5UNMCkhf`
 :t:`Precedence <precedence>` is the order by which :t:`expressions <expression>` are evaluated in the presence of other expressions.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_F2dUxEa4nheL`
A :dt:`pointer type` is a :t:`type` whose values indicate memory locations.

.. _fls_Q0r8JkqAP6Of:

positional register argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## prelude (prelude)

### Before glossary entry (origin/main)

```rst
.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^

:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.
```

### After glossary entry (generated)

```rst
.. _fls_64TdwAx43ZIi:

prelude
^^^^^^^

:dp:`fls_yf2iyYaabJic`
 A :t:`prelude` is a collection of :t:`entities <entity>` that are automatically brought :t:`in scope <in_scope>` of every :t:`module` in a :t:`crate`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_GJd6i52P3KM3`
A :dt:`positional register argument` is a :t:`register argument` whose
configuration is not bound to an :t:`identifier`.

.. _fls_ukvdoqo68y5b:

precedence
^^^^^^^^^^


:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## prelude entity (prelude_entity)

### Before glossary entry (origin/main)

```rst
.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^

:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
```

### After glossary entry (generated)

```rst
.. _fls_Xwjz8xfHdZFt:

prelude entity
^^^^^^^^^^^^^^

:dp:`fls_ckQF2iG6VWWq`
 A :t:`prelude entity <prelude_entity>` is an :t:`entity` declared in a :t:`prelude`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_sz93844rqc4r`
:dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
presence of other expressions.

.. _fls_8Gn72FJBarfb:

prelude
^^^^^^^


:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## prelude name (prelude_name)

### Before glossary entry (origin/main)

```rst
.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^

:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.
```

### After glossary entry (generated)

```rst
.. _fls_vWTXeFIQB8vw:

prelude name
^^^^^^^^^^^^

:dp:`fls_BxDWViOwqE3g`
 A :t:`prelude name <prelude_name>` is a :t:`name` of a :t:`prelude entity <prelude_entity>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.

.. _fls_AWySDxPgypiw:

prelude entity
^^^^^^^^^^^^^^


:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## primitive representation (primitive_representation)

### Before glossary entry (origin/main)

```rst
.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.
```

### After glossary entry (generated)

```rst
.. _fls_YDjIcMMLz9ib:

Primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_u2ZBeRlr147N`
 :t:`Primitive representation <primitive_representation>` is the :t:`type representation <type_representation>` of :t:`integer types <integer_type>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

.. _fls_FYn5JqPOhiIs:

prelude name
^^^^^^^^^^^^


:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## principal trait (principal_trait)

### Before glossary entry (origin/main)

```rst
.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^

:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.
```

### After glossary entry (generated)

```rst
.. _fls_za4c8UTDt4Dq:

principal trait
^^^^^^^^^^^^^^^

:dp:`fls_nZaSSZRev8aX`
 The :t:`principal trait <principal_trait>` of :t:`trait object type <trait_object_type>` is its first :t:`trait bound <trait_bound>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

.. _fls_fikexts17v7a:

primitive representation
^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## private visibility (private_visibility)

### Before glossary entry (origin/main)

```rst
.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^

:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.
```

### After glossary entry (generated)

```rst
.. _fls_ixCxFlcolsnU:

Private visibility
^^^^^^^^^^^^^^^^^^

:dp:`fls_ObvRDkJG1Zcx`
 :t:`Private visibility <private_visibility>` is a kind of :t:`visibility` that allows a :t:`name` to be referred to only by the current :t:`module` of the :t:`entity`, and its descendant :t:`modules <module>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_bydly1rt63pf`
:dt:`Primitive representation` is the :t:`type representation` of
:t:`[integer type]s`.

.. _fls_mk3sa7OvtJvB:

principal trait
^^^^^^^^^^^^^^^


:dp:`fls_YtYOHoPaMPFX`
The :dt:`principal trait` of :t:`trait object type` is its first :t:`trait bound`.

.. _fls_v1u1mevpj0kj:

private visibility
^^^^^^^^^^^^^^^^^^


:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## procedural macro (procedural_macro)

### Before glossary entry (origin/main)

```rst
.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^

:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.
```

### After glossary entry (generated)

```rst
.. _fls_Ni0of9RgPNWd:

procedural macro
^^^^^^^^^^^^^^^^

:dp:`fls_koH6PM3zzYHT`
 A :t:`procedural macro <procedural_macro>` is a :t:`macro` that encapsulates syntactic transformations in a :t:`function`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

.. _fls_kCA6SW8bUq5x:

proc-macro crate
^^^^^^^^^^^^^^^^

.. _fls_AjjdLZWiL9Tq:


:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## program entry point (program_entry_point)

### Before glossary entry (origin/main)

```rst
.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^

:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.
```

### After glossary entry (generated)

```rst
.. _fls_eF68JaOonPbw:

program entry point
^^^^^^^^^^^^^^^^^^^

:dp:`fls_cK38726ac6sd`
 A :t:`program entry point <program_entry_point>` is a :t:`function` that is invoked at the start of a Rust program.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_DfTszT1PjV7o`
A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

.. _fls_sp5wdsxwmxf:

procedural macro
^^^^^^^^^^^^^^^^


:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## public visibility (public_visibility)

### Before glossary entry (origin/main)

```rst
.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^

:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
```

### After glossary entry (generated)

```rst
.. _fls_2oyNo8lkK61u:

Public visibility
^^^^^^^^^^^^^^^^^

:dp:`fls_mIfEQINVMIk5`
 :t:`Public visibility <public_visibility>` is a kind of :t:`visibility` that allows a :t:`name` to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor :t:`modules <module>` of the related :t:`entity` can be referred to from ``M``.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_u4utpx4zgund`
A :dt:`procedural macro` is a :t:`macro` that encapsulates syntactic
transformations in a :t:`function`.

.. _fls_SIFecOZqloyx:

program entry point
^^^^^^^^^^^^^^^^^^^


:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## punctuator (punctuator)

### Before glossary entry (origin/main)

```rst
.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^

:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.
```

### After glossary entry (generated)

```rst
.. _fls_mJzv2rGvkGUN:

punctuator
^^^^^^^^^^

:dp:`fls_EBlcWXQQslqz`
 A :t:`punctuator` is a character or a sequence of characters in category :s:`Punctuation <punctuation>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_9m37hN9zgEQf`
A :dt:`program entry point` is a :t:`function` that is invoked at the start of
a Rust program.

.. _fls_v2rjlovqsdyr:

public visibility
^^^^^^^^^^^^^^^^^


:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## pure identifier (pure_identifier)

### Before glossary entry (origin/main)

```rst
.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^

:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.
```

### After glossary entry (generated)

```rst
.. _fls_HLrv0yvksHgE:

pure identifier
^^^^^^^^^^^^^^^

:dp:`fls_DkxPUDiLBFOx`
 A :t:`pure identifier <pure_identifier>` is an :t:`identifier` that does not include :t:`weak keywords <weak_keyword>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

.. _fls_hdwmw3jbwefi:

punctuator
^^^^^^^^^^


:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.

.. _fls_sgwvmnoio1ql:

pure identifier
^^^^^^^^^^^^^^^


:dp:`fls_6pez8fyiew0k`
A :dt:`pure identifier` is an :t:`identifier` that does not include
:t:`[weak keyword]s`.

.. _fls_O6CFtnpN3UEE:

qualified path expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_wKAS6FxqGmTf`
A :dt:`qualified path expression` is a :t:`path expression` that resolves
through a :t:`qualified type`.


:dp:`fls_MXxJn64eJpC5`
See :s:`QualifiedPathExpression`.

.. _fls_Qv0UvhSfwBuM:

qualified type
^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
