# Glossary audit H

## Per-letter checklist
- Letter: H
- [x] Reconcile H terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate H terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for H
- [x] Update `migration-checklist.md` for all H terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint H migration`
- [x] Letter complete

## Term checklist
- [x] half-open range pattern (half_open_range_pattern)
- [x] hexadecimal literal (hexadecimal_literal)
- [x] higher-ranked trait bound (higher_ranked_trait_bound)
- [x] hygiene (hygiene)
- [x] hygienic (hygienic)

## half-open range pattern (half_open_range_pattern)

### Before glossary entry (origin/main)

```rst
.. _fls_fquvoglio1jz:

half-open range pattern
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_tymjispfgp7u`
A :dt:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.

:dp:`fls_evm3nxwswk00`
See :s:`HalfOpenRangePattern`.
```

### After glossary entry (generated)

```rst
.. _fls_8kCJArEO6Brq:

half-open range pattern
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_IDs7d4q0hTKY`
A :t:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_wvspqc2otn6v`
A :dt:`greater-than-or-equals expression` is a :t:`comparison expression` that
tests for a greater-than-or-equals relationship.


:dp:`fls_9azbvj9xux6y`
See :s:`GreaterThanOrEqualsExpression`.

.. _fls_fquvoglio1jz:

half-open range pattern
^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_tymjispfgp7u`
A :dt:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.


:dp:`fls_evm3nxwswk00`
See :s:`HalfOpenRangePattern`.

.. _fls_5uiij8eqln5g:

hexadecimal literal
^^^^^^^^^^^^^^^^^^^


:dp:`fls_8b6njsi8g68i`
A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.

```

### After chapter excerpt (current)

```rst
src/patterns.rst
:dp:`fls_okupyoav13rm`
A :t:`range pattern` is a :t:`pattern` that matches :t:`[value]s` which fall
within a range.

:dp:`fls_jhchm7dy927k`
A :dt:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.

:dp:`fls_q86j23iiqv8w`
An :t:`inclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.

:dp:`fls_3PyquOKjA7SI`
An :dt:`exclusive range pattern` is a :t:`range pattern` with both a
:t:`range pattern low bound` and a :t:`range pattern high bound`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## hexadecimal literal (hexadecimal_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_5uiij8eqln5g:

hexadecimal literal
^^^^^^^^^^^^^^^^^^^

:dp:`fls_8b6njsi8g68i`
A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.

:dp:`fls_vssa4z5wcgaa`
See :s:`HexadecimalLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_L8UKXWni9Mp3:

hexadecimal literal
^^^^^^^^^^^^^^^^^^^

:dp:`fls_a9Y7Dmxhklvi`
A :t:`hexadecimal literal` is an :t:`integer literal` in base 16.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_tymjispfgp7u`
A :dt:`half-open range pattern` is a :t:`range pattern` with only a
:t:`range pattern low bound`.


:dp:`fls_evm3nxwswk00`
See :s:`HalfOpenRangePattern`.

.. _fls_5uiij8eqln5g:

hexadecimal literal
^^^^^^^^^^^^^^^^^^^


:dp:`fls_8b6njsi8g68i`
A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.


:dp:`fls_vssa4z5wcgaa`
See :s:`HexadecimalLiteral`.

.. _fls_h87i5nbeuxky:

higher-ranked trait bound
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_lpyc4omcthv`
A :dt:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s`.

```

### After chapter excerpt (current)

```rst
src/lexical-elements.rst
:dp:`fls_vkk2krfn93ry`
An :t:`integer literal` is a :t:`numeric literal` that denotes a whole number.

:dp:`fls_nxqncu5yq4eu`
A :dt:`binary literal` is an :t:`integer literal` in base 2.

:dp:`fls_rn8xfd66yvst`
A :dt:`decimal literal` is an :t:`integer literal` in base 10.

:dp:`fls_2268lchxkzjp`
A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.

:dp:`fls_4v7awnutbpoe`
An :t:`octal literal` is an :t:`integer literal` in base 8.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## higher-ranked trait bound (higher_ranked_trait_bound)

### Before glossary entry (origin/main)

```rst
.. _fls_h87i5nbeuxky:

higher-ranked trait bound
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_lpyc4omcthv`
A :dt:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s`.

:dp:`fls_m3nrsdvxxg6j`
See :s:`ForGenericParameterList`.
```

### After glossary entry (generated)

```rst
.. _fls_3G3Rhb4VrasL:

higher-ranked trait bound
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_jRyNOQj78VdQ`
A :t:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s` specified by the
:s:`ForGenericParameterList`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_8b6njsi8g68i`
A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.


:dp:`fls_vssa4z5wcgaa`
See :s:`HexadecimalLiteral`.

.. _fls_h87i5nbeuxky:

higher-ranked trait bound
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_lpyc4omcthv`
A :dt:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s`.


:dp:`fls_m3nrsdvxxg6j`
See :s:`ForGenericParameterList`.

.. _fls_GuMMjhEMMLvF:

hygiene
^^^^^^^


:dp:`fls_AQg0MqAQZqkz`
:dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
appear within them, which aims to eliminate the syntactic interference between
a :t:`macro` and its environment.

.. _fls_95h0aWZ7xx6U:

hygienic
^^^^^^^^

```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_5g508z6c7q5f`
A :dt:`bound` imposes a constraint on a :t:`generic parameter` by limiting the
set of possible :t:`[generic substitution]s`.

:dp:`fls_grby8tmmd8sb`
A :t:`lifetime bound` is a :t:`bound` that imposes a constraint on the
:t:`[lifetime]s` of :t:`[generic parameter]s`.

:dp:`fls_knut10hoz6wc`
A :t:`trait bound` is a :t:`bound` that imposes a constraint on the
:t:`[trait]s` of :t:`[generic parameter]s`.

:dp:`fls_vujl3fblz6x2`
A :dt:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s` specified by the
:s:`ForGenericParameterList`.

:dp:`fls_AzuZmR9DXSQh`
An :t:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## hygiene (hygiene)

### Before glossary entry (origin/main)

```rst
.. _fls_GuMMjhEMMLvF:

hygiene
^^^^^^^

:dp:`fls_AQg0MqAQZqkz`
:dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
appear within them, which aims to eliminate the syntactic interference between
a :t:`macro` and its environment.
```

### After glossary entry (generated)

```rst
.. _fls_QdQUOu1mfrBi:

hygiene
^^^^^^^

:dp:`fls_p9n8MVOSafZq`
The :t:`hygiene` of :t:`[macro]s` and :t:`[identifier]s` that appear within
them is a property that aims to eliminate the syntactic interference between a
:t:`macro` and its environment.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_lpyc4omcthv`
A :dt:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s`.


:dp:`fls_m3nrsdvxxg6j`
See :s:`ForGenericParameterList`.

.. _fls_GuMMjhEMMLvF:

hygiene
^^^^^^^


:dp:`fls_AQg0MqAQZqkz`
:dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
appear within them, which aims to eliminate the syntactic interference between
a :t:`macro` and its environment.

.. _fls_95h0aWZ7xx6U:

hygienic
^^^^^^^^


:dp:`fls_hiDddAkNH5Ms`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.

.. _fls_obiv2a6ywfhh:

i8
^^


:dp:`fls_1y9ulxnz8qba`
:dc:`i8` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
:sup:`7`) to 2\ :sup:`7` - 1, all inclusive.

.. _fls_rvcjp656gzlm:

i16
^^^

```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_7ezc7ncs678f`
The :dt:`hygiene` of :t:`[macro]s` and :t:`[identifier]s` that appear within
them is a property that aims to eliminate the syntactic interference between a
:t:`macro` and its environment.

:dp:`fls_3axjf28xb1nt`
:t:`hygiene` is categorized as follows:

* :dp:`fls_dz2mvodl818d`
  :dt:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference
  the environment of the :s:`MacroRulesDeclaration`, cannot be referenced by the
  environment of a :s:`MacroInvocation`, and are considered :t:`hygienic`.

* :dp:`fls_puqhytfzfsg6`
  :dt:`call site hygiene`, which resolves to a :s:`MacroInvocation` site.
  :t:`[Identifier]s` with :t:`call site hygiene` can reference the environment
  of the :s:`MacroRulesDeclaration`, can reference the environment of the
  :s:`MacroInvocation`, and are considered :t:`unhygienic`.

* :dp:`fls_uyvnq88y9gk3`
  :dt:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
  :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
  considered :t:`partially hygienic`.

:dp:`fls_4bTKuwDSu5FJ`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## hygienic (hygienic)

### Before glossary entry (origin/main)

```rst
.. _fls_95h0aWZ7xx6U:

hygienic
^^^^^^^^

:dp:`fls_hiDddAkNH5Ms`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.
```

### After glossary entry (generated)

```rst
.. _fls_lRkd2mTlrCub:

hygienic
^^^^^^^^

:dp:`fls_5PGvpfBe234J`
An :t:`identifier` is :t:`hygienic` when it has :t:`definition site hygiene`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_m3nrsdvxxg6j`
See :s:`ForGenericParameterList`.

.. _fls_GuMMjhEMMLvF:

hygiene
^^^^^^^


:dp:`fls_AQg0MqAQZqkz`
:dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
appear within them, which aims to eliminate the syntactic interference between
a :t:`macro` and its environment.

.. _fls_95h0aWZ7xx6U:

hygienic
^^^^^^^^


:dp:`fls_hiDddAkNH5Ms`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.

.. _fls_obiv2a6ywfhh:

i8
^^


:dp:`fls_1y9ulxnz8qba`
:dc:`i8` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
:sup:`7`) to 2\ :sup:`7` - 1, all inclusive.

.. _fls_rvcjp656gzlm:

i16
^^^


:dp:`fls_ci9jl55wxwdg`
:dc:`i16` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
:sup:`15`) to 2\ :sup:`15` - 1, all inclusive.

.. _fls_l1h9g4ntf3c:

i32
^^^

```

### After chapter excerpt (current)

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

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
