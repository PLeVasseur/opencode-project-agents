# Glossary audit D

## Per-letter checklist
- Letter: D
- [x] Reconcile D terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate D terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for D
- [x] Update `migration-checklist.md` for all D terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint D migration`
- [x] Letter complete

## Term checklist
- [x] dangling (dangling)
- [x] data race (data_race)
- [x] decimal literal (decimal_literal)
- [x] declaration (declaration)
- [x] declarative macro (declarative_macro)
- [x] deconstructee (deconstructee)
- [x] default representation (default_representation)
- [x] definition site hygiene (definition_site_hygiene)
- [x] dereference (dereference)
- [x] dereference expression (dereference_expression)
- [x] dereference type (dereference_type)
- [x] dereference type chain (dereference_type_chain)
- [x] derive macro (derive_macro)
- [x] destruction (destruction)
- [x] destructor (destructor)
- [x] destructuring assignment (destructuring_assignment)
- [x] direction modifier (direction_modifier)
- [x] discriminant (discriminant)
- [x] discriminant initializer (discriminant_initializer)
- [x] discriminant type (discriminant_type)
- [x] diverging expression (diverging_expression)
- [x] diverging type variable (diverging_type_variable)
- [x] division assignment (division_assignment)
- [x] division assignment expression (division_assignment_expression)
- [x] division expression (division_expression)
- [x] doc comment (doc_comment)
- [x] drop construct (drop_construct)
- [x] drop order (drop_order)
- [x] drop scope (drop_scope)
- [x] drop scope extension (drop_scope_extension)
- [x] drop type (drop_type)
- [x] dropping (dropping)
- [x] dynamically sized type (dynamically_sized_type)

## dangling (dangling)

### Before glossary entry (origin/main)

```rst
.. _fls_76cj65bptdpn:

dangling
^^^^^^^^

:dp:`fls_lq2urzh7bzxx`
A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
:c:`null` or not all of the bytes at the referred memory location are part of
the same allocation.
```

### After glossary entry (generated)

```rst
.. _fls_XouWyav9k9ro:

dangling
^^^^^^^^

:dp:`fls_Wa4wIr2dR2jM`
A :t:`value` of an :t:`indirection type` is :t:`dangling` if it is either
:c:`null` or not all of the bytes at the referred memory location are part of
the same allocation.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_eoak5mdl6ma`.
src/values.rst
* :dp:`fls_s231d18x5eay`
  One :t:`value` is of an :t:`abstract data type` and the other denotes a
  :t:`field` of the same :t:`value`, or

* :dp:`fls_dfr4yqo93fsn`
  One :t:`value` denotes an :t:`array` and the other denotes an element of the
  same :t:`value`, or

* :dp:`fls_eoak5mdl6ma`
  Both :t:`[value]s` are elements of the same :t:`array`.

:dp:`fls_6lg0oaaopc26`
It is undefined behavior to create a :t:`value` from uninitialized memory unless
the :t:`type` of the :t:`value` is a :t:`union type`.

:dp:`fls_oqhQ62mDLckN`
It is undefined behavior to create an :t:`allocated object` at :t:`base address`
:c:`null`.
```

### After chapter excerpt (current)

```rst
src/values.rst
* :dp:`fls_dfr4yqo93fsn`
  One :t:`value` denotes an :t:`array` and the other denotes an element of the
  same :t:`value`, or

* :dp:`fls_eoak5mdl6ma`
  Both :t:`[value]s` are elements of the same :t:`array`.

:dp:`fls_649WudgnmRKE`
A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
:c:`null` or not all of the bytes at the referred memory location are part of
the same allocation.

:dp:`fls_6lg0oaaopc26`
It is undefined behavior to create a :t:`value` from uninitialized memory unless
the :t:`type` of the :t:`value` is a :t:`union type`.

:dp:`fls_oqhQ62mDLckN`
It is undefined behavior to create an :t:`allocated object` at :t:`base address`
:c:`null`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## data race (data_race)

### Before glossary entry (origin/main)

```rst
.. _fls_9meaofgcpvx6:

data race
^^^^^^^^^

:dp:`fls_v2s1b57e3r7n`
A :dt:`data race` is a scenario where two or more threads access a shared
memory location concurrently.
```

### After glossary entry (generated)

```rst
.. _fls_KsSH5T6ip3vE:

data race
^^^^^^^^^

:dp:`fls_yx6IwIvBDix9`
A :t:`data race` is a scenario where two or more threads access a shared memory
location concurrently without any synchronization, where one of the accesses is
a modification.
```

### Before chapter excerpt (origin/main)

```rst
src/concurrency.rst
:dp:`fls_opt7v0mopxc8`
The Rust programming language provides features for concurrent programming
without :t:`[data race]s`, whose rules are presented in this chapter.

:dp:`fls_tx4b8r6i93n4`
A :t:`data race` is a scenario where two or more threads access a shared memory
location concurrently without any synchronization, where one of the accesses is
a modification.

:dp:`fls_isypweqewe78`
It is undefined behavior if two or more threads engage in a :t:`data race`.

:dp:`fls_n5l17mlglq11`
The Rust programming language provides the :std:`core::marker::Send` and
:std:`core::marker::Sync` :t:`[trait]s` for preventing data races at the
:t:`type` level.
```

### After chapter excerpt (current)

```rst
src/concurrency.rst
:dp:`fls_opt7v0mopxc8`
The Rust programming language provides features for concurrent programming
without :t:`[data race]s`, whose rules are presented in this chapter.

:dp:`fls_tx4b8r6i93n4`
A :dt:`data race` is a scenario where two or more threads access a shared memory
location concurrently without any synchronization, where one of the accesses is
a modification.

:dp:`fls_isypweqewe78`
It is undefined behavior if two or more threads engage in a :t:`data race`.

:dp:`fls_n5l17mlglq11`
The Rust programming language provides the :std:`core::marker::Send` and
:std:`core::marker::Sync` :t:`[trait]s` for preventing data races at the
:t:`type` level.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## decimal literal (decimal_literal)

### Before glossary entry (origin/main)

```rst
.. _fls_128iunbbiuql:

decimal literal
^^^^^^^^^^^^^^^

:dp:`fls_lwv823lih69m`
A :dt:`decimal literal` is an :t:`integer literal` in base 10.

:dp:`fls_pxiba4se64y4`
See :s:`DecimalLiteral`.
```

### After glossary entry (generated)

```rst
.. _fls_H5NyWQTaOgjc:

decimal literal
^^^^^^^^^^^^^^^

:dp:`fls_9lb9RSnPYL2Q`
A :t:`decimal literal` is an :t:`integer literal` in base 10.
```

### Before chapter excerpt (origin/main)

```rst
src/lexical-elements.rst
:dp:`fls_vkk2krfn93ry`
An :t:`integer literal` is a :t:`numeric literal` that denotes a whole number.

:dp:`fls_nxqncu5yq4eu`
A :t:`binary literal` is an :t:`integer literal` in base 2.

:dp:`fls_rn8xfd66yvst`
A :t:`decimal literal` is an :t:`integer literal` in base 10.

:dp:`fls_2268lchxkzjp`
A :t:`hexadecimal literal` is an :t:`integer literal` in base 16.

:dp:`fls_4v7awnutbpoe`
An :t:`octal literal` is an :t:`integer literal` in base 8.
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
A :t:`hexadecimal literal` is an :t:`integer literal` in base 16.

:dp:`fls_4v7awnutbpoe`
An :t:`octal literal` is an :t:`integer literal` in base 8.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## declaration (declaration)

### Before glossary entry (origin/main)

```rst
.. _fls_9qgy7x6w5ro5:

declaration
^^^^^^^^^^^

:dp:`fls_kct7ducpli6k`
A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.
```

### After glossary entry (generated)

```rst
.. _fls_7KJALZUIfqDB:

declaration
^^^^^^^^^^^

:dp:`fls_txD6LRkTzNC9`
A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.
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

:dp:`fls_94l2d7ti0hjw`
An :t:`explicitly declared entity` is an :t:`entity` that has a
:t:`declaration`. The following :t:`entities <entity>` are
:t:`explicitly declared entities <explicitly declared entity>`:

* :dp:`fls_kvdqmo8gmdxi`
  :t:`[Associated item]s`,
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_x7j6wcigqt7u`
An :dt:`entity` is a :t:`construct` that can be referred to within program text,
usually via a :t:`field access expression` or a :t:`path`.

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
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## declarative macro (declarative_macro)

### Before glossary entry (origin/main)

```rst
.. _fls_5944xn0lz8e:

declarative macro
^^^^^^^^^^^^^^^^^

:dp:`fls_pe12lfffaoqt`
A :dt:`declarative macro` is a :t:`macro` that associates a :t:`name` with a
set of syntactic transformation rules.

:dp:`fls_1te2kfi9lt6c`
See :s:`MacroRulesDeclaration`.
```

### After glossary entry (generated)

```rst
.. _fls_yxvN745QrRZH:

declarative macro
^^^^^^^^^^^^^^^^^

:dp:`fls_WXQURYdBunzi`
A :t:`declarative macro` is a :t:`macro` that associates a :t:`name` with a set
of syntactic transformation :t:`[macro rule]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_rnty1c8l5495`
:t:`[Token]s` are a subset of :t:`[lexical element]s` consumed by :t:`[macro]s`.

:dp:`fls_ikzjsq8heyk6`
A :ds:`MacroMatchToken` is any :t:`lexical element` in category
:s:`LexicalElement`, except punctuation ``$`` and category :s:`Delimiter`.

:dp:`fls_w44hav7mw3ao`
A :t:`declarative macro` is a :t:`macro` that associates a :t:`name` with a set
of syntactic transformation :t:`[macro rule]s`.

:dp:`fls_dw1nq4r9ghhd`
A :t:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher` and
a :t:`macro transcriber`.

:dp:`fls_oq4xn8guos8f`
A :t:`macro matcher` is a :t:`construct` that describes a syntactic pattern that
a :t:`macro` must match.
```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_rnty1c8l5495`
:t:`[Token]s` are a subset of :t:`[lexical element]s` consumed by :t:`[macro]s`.

:dp:`fls_ikzjsq8heyk6`
A :ds:`MacroMatchToken` is any :t:`lexical element` in category
:s:`LexicalElement`, except punctuation ``$`` and category :s:`Delimiter`.

:dp:`fls_w44hav7mw3ao`
A :dt:`declarative macro` is a :t:`macro` that associates a :t:`name` with a set
of syntactic transformation :t:`[macro rule]s`.

:dp:`fls_dw1nq4r9ghhd`
A :t:`macro rule` is a :t:`construct` that consists of a :t:`macro matcher` and
a :t:`macro transcriber`.

:dp:`fls_oq4xn8guos8f`
A :t:`macro matcher` is a :t:`construct` that describes a syntactic pattern that
a :t:`macro` must match.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## deconstructee (deconstructee)

### Before glossary entry (origin/main)

```rst
.. _fls_GAlaslkO8gLG:

deconstructee
^^^^^^^^^^^^^

:dp:`fls_QsvWOdoFWtUO`
A :dt:`deconstructee` indicates the :t:`enum variant` or :t:`type` that is
being deconstructed by a :t:`struct pattern`.

:dp:`fls_TkFjmV7AR7lp`
See :s:`Deconstructee`.
```

### After glossary entry (generated)

```rst
.. _fls_iba1bzOr2H6K:

deconstructee
^^^^^^^^^^^^^

:dp:`fls_wh7KJqzpiKsN`
A :t:`deconstructee` indicates the :t:`enum variant` or :t:`type` that is being
deconstructed by a :t:`struct pattern`.
```

### Before chapter excerpt (origin/main)

```rst
src/patterns.rst
:dp:`fls_9yuobz1jsehf`
A slice pattern in the context of a match expression.

:dp:`fls_vjdkpr3zml51`
A :t:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.

:dp:`fls_6o3x101wo478`
A :t:`deconstructee` indicates the :t:`enum variant` or :t:`type` that is being
deconstructed by a :t:`struct pattern`.

:dp:`fls_k9zih9s0oe5h`
A :t:`struct pattern` is interpreted based on the :t:`deconstructee`. It is a
static error if a :t:`struct pattern` cannot be interpreted.

:dp:`fls_r8rat3qmc4hy`
A :t:`struct pattern` is an :t:`irrefutable pattern` if
```

### After chapter excerpt (current)

```rst
src/patterns.rst
:dp:`fls_9yuobz1jsehf`
A slice pattern in the context of a match expression.

:dp:`fls_vjdkpr3zml51`
A :t:`struct pattern` is a :t:`pattern` that matches an :t:`enum value`, a
:t:`struct value`, or a :t:`union value`.

:dp:`fls_6o3x101wo478`
A :dt:`deconstructee` indicates the :t:`enum variant` or :t:`type` that is being
deconstructed by a :t:`struct pattern`.

:dp:`fls_k9zih9s0oe5h`
A :t:`struct pattern` is interpreted based on the :t:`deconstructee`. It is a
static error if a :t:`struct pattern` cannot be interpreted.

:dp:`fls_r8rat3qmc4hy`
A :t:`struct pattern` is an :t:`irrefutable pattern` if
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## default representation (default_representation)

### Before glossary entry (origin/main)

```rst
.. _fls_g9v8ubx8m1sq:

default representation
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_e85fsp10acnh`
:dt:`Default representation` is a :t:`type representation` that does not make
any guarantees about :t:`layout`.
```

### After glossary entry (generated)

```rst
.. _fls_dynjaRnr2bbC:

Default representation
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_d3LisUYr1v8M`
:t:`Default representation` makes no guarantees about the :t:`layout`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
* :dp:`fls_ergdb18tpx25`
  :t:`Transparent representation`.

:dp:`fls_8s1vddh8vdhy`
:t:`C representation` lays out a :t:`type` such that the :t:`type` is
interoperable with the :t:`C` language.

:dp:`fls_b005bktrkrxy`
:t:`Default representation` makes no guarantees about the :t:`layout`.

:dp:`fls_7plbkqlmed0r`
:t:`Primitive representation` is the :t:`type representation` of individual
:t:`[integer type]s`. :t:`Primitive representation` applies only to an
:t:`enum type` that is not a :t:`zero-variant enum type`. It is possible to
combine :t:`C representation` and :t:`primitive representation`.

:dp:`fls_ml4khttq3w5k`
:t:`Transparent representation` applies only to an :t:`enum type` with a
single :t:`enum variant` or a :t:`struct type` where the :t:`struct type` or
:t:`enum variant` has a single :t:`field` of non-zero :t:`size` and any number
of :t:`[field]s` of :t:`size` zero and :t:`alignment` one.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
* :dp:`fls_ergdb18tpx25`
  :t:`Transparent representation`.

:dp:`fls_8s1vddh8vdhy`
:dt:`C representation` lays out a :t:`type` such that the :t:`type` is
interoperable with the :t:`C` language.

:dp:`fls_b005bktrkrxy`
:dt:`Default representation` makes no guarantees about the :t:`layout`.

:dp:`fls_7plbkqlmed0r`
:t:`Primitive representation` is the :t:`type representation` of individual
:t:`[integer type]s`. :t:`Primitive representation` applies only to an
:t:`enum type` that is not a :t:`zero-variant enum type`. It is possible to
combine :t:`C representation` and :t:`primitive representation`.

:dp:`fls_ml4khttq3w5k`
:t:`Transparent representation` applies only to an :t:`enum type` with a
single :t:`enum variant` or a :t:`struct type` where the :t:`struct type` or
:t:`enum variant` has a single :t:`field` of non-zero :t:`size` and any number
of :t:`[field]s` of :t:`size` zero and :t:`alignment` one.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## definition site hygiene (definition_site_hygiene)

### Before glossary entry (origin/main)

```rst
.. _fls_FrfnICpg81sr:

definition site hygiene
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_2Y1Dpw5ZEqT3`
:dt:`Definition site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site. :t:`[Identifier]s` with
:t:`definition site hygiene` cannot reference the environment of the
:s:`MacroRulesDeclaration`, cannot be referenced by the environment of a
:s:`MacroInvocation`, and are considered :t:`hygienic`.
```

### After glossary entry (generated)

```rst
.. _fls_dvTrnUlXDu00:

Definition site hygiene
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_vXzJlnRoiHto`
:t:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference
the environment of the :s:`MacroRulesDeclaration`, cannot be referenced by the
environment of a :s:`MacroInvocation`, and are considered :t:`hygienic`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_7ezc7ncs678f`
:t:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
within them, which aims to eliminate the syntactic interference between a
:t:`macro` and its environment.

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
```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_7ezc7ncs678f`
:t:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
within them, which aims to eliminate the syntactic interference between a
:t:`macro` and its environment.

:dp:`fls_3axjf28xb1nt`
:t:`Hygiene` is categorized as follows:

* :dp:`fls_dz2mvodl818d`
  :dt:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference
  the environment of the :s:`MacroRulesDeclaration`, cannot be referenced by the
  environment of a :s:`MacroInvocation`, and are considered :dt:`hygienic`.

* :dp:`fls_puqhytfzfsg6`
  :dt:`call site hygiene`, which resolves to a :s:`MacroInvocation` site.
  :t:`[Identifier]s` with :t:`call site hygiene` can reference the environment
  of the :s:`MacroRulesDeclaration`, can reference the environment of the
  :s:`MacroInvocation`, and are considered :dt:`unhygienic`.

* :dp:`fls_uyvnq88y9gk3`
  :t:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
  :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
  considered :dt:`partially hygienic`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## dereference (dereference)

### Before glossary entry (origin/main)

```rst
.. _fls_127n1n5ssk2b:

dereference
^^^^^^^^^^^

:dp:`fls_hk97pb1qt04y`
A :dt:`dereference` is the memory location produced by evaluating a
:t:`dereference expression`.
```

### After glossary entry (generated)

```rst
.. _fls_Id4WZ6z7nKqm:

dereference
^^^^^^^^^^^

:dp:`fls_dU9eu8R6EgCc`
A :t:`dereference` is the memory location produced by evaluating a
:t:`dereference expression`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_f6wktzofzdn1`.
src/expressions.rst
:dp:`fls_qQrV8QuGGcVO`
The :t:`evaluation` of a :t:`raw borrow expression` evaluates its :t:`operand`.

:dp:`fls_dTABiwAPGhdZ`
Mutable raw borrow.

:dp:`fls_f6wktzofzdn1`
A :t:`dereference expression` is an :t:`expression` that obtains the pointed-to
memory location of its :t:`operand`.

:dp:`fls_aeh5pzpcjveq`
When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
type`, the :t:`dereference expression` denotes the pointed-to memory location of
the :t:`operand`, or the :t:`dereference` of the :t:`operand`.

:dp:`fls_9cc0ml2sru6x`
The :t:`dereference` is assignable when the :t:`dereference expression` is a
:t:`mutable place expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_dTABiwAPGhdZ`
Mutable raw borrow.

:dp:`fls_f6wktzofzdn1`
A :dt:`dereference expression` is an :t:`expression` that obtains the pointed-to
memory location of its :t:`operand`.

:dp:`fls_aOXtV5sEUGxJ`
A :dt:`dereference` is the memory location produced by evaluating a
:t:`dereference expression`.

:dp:`fls_aeh5pzpcjveq`
When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
type`, the :t:`dereference expression` denotes the pointed-to memory location of
the :t:`operand`, or the :t:`dereference` of the :t:`operand`.

:dp:`fls_9cc0ml2sru6x`
The :t:`dereference` is assignable when the :t:`dereference expression` is a
:t:`mutable place expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## dereference expression (dereference_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_o588wfq878rm:

dereference expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_3cuyhbh2llei`
A :dt:`dereference expression` is an :t:`expression` that obtains the
pointed-to memory location of its :t:`operand`.

:dp:`fls_hx0jwahdb1nf`
See :s:`DereferenceExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_YjDi2UjzsqcW:

dereference expression
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_aMkrupm8NzdQ`
A :t:`dereference expression` is an :t:`expression` that obtains the pointed-to
memory location of its :t:`operand`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_qQrV8QuGGcVO`
The :t:`evaluation` of a :t:`raw borrow expression` evaluates its :t:`operand`.

:dp:`fls_dTABiwAPGhdZ`
Mutable raw borrow.

:dp:`fls_f6wktzofzdn1`
A :t:`dereference expression` is an :t:`expression` that obtains the pointed-to
memory location of its :t:`operand`.

:dp:`fls_aeh5pzpcjveq`
When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
type`, the :t:`dereference expression` denotes the pointed-to memory location of
the :t:`operand`, or the :t:`dereference` of the :t:`operand`.

:dp:`fls_9cc0ml2sru6x`
The :t:`dereference` is assignable when the :t:`dereference expression` is a
:t:`mutable place expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_qQrV8QuGGcVO`
The :t:`evaluation` of a :t:`raw borrow expression` evaluates its :t:`operand`.

:dp:`fls_dTABiwAPGhdZ`
Mutable raw borrow.

:dp:`fls_f6wktzofzdn1`
A :dt:`dereference expression` is an :t:`expression` that obtains the pointed-to
memory location of its :t:`operand`.

:dp:`fls_aOXtV5sEUGxJ`
A :dt:`dereference` is the memory location produced by evaluating a
:t:`dereference expression`.

:dp:`fls_aeh5pzpcjveq`
When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
type`, the :t:`dereference expression` denotes the pointed-to memory location of
the :t:`operand`, or the :t:`dereference` of the :t:`operand`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## dereference type (dereference_type)

### Before glossary entry (origin/main)

```rst
.. _fls_xbN0GtcH8emc:

dereference type
^^^^^^^^^^^^^^^^

:dp:`fls_HfuUQ7IaoI5j`
A :dt:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.
```

### After glossary entry (generated)

```rst
.. _fls_2rTCL5MPsnyl:

dereference type
^^^^^^^^^^^^^^^^

:dp:`fls_3IZ1q2VwfvuJ`
A :t:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_ho4kem1slcxg`
:t:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, a :t:`call
expression` or a :t:`path`.

:dp:`fls_7le2vcdbtxbq`
A :t:`construct` that is being resolved is said to be :t:`under resolution`.

:dp:`fls_x3alg07yd7hx`
A :t:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.

:dp:`fls_4hulwazdu20i`
A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:

* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_ho4kem1slcxg`
:t:`Resolution` is the process of finding a unique interpretation for a
:t:`field access expression`, a :t:`method call expression`, a :t:`call
expression` or a :t:`path`.

:dp:`fls_7le2vcdbtxbq`
A :t:`construct` that is being resolved is said to be :dt:`under resolution`.

:dp:`fls_x3alg07yd7hx`
A :dt:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.

:dp:`fls_4hulwazdu20i`
A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:

* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## dereference type chain (dereference_type_chain)

### Before glossary entry (origin/main)

```rst
.. _fls_T380NdEsFxIp:

dereference type chain
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_kIzoAEf069HE`
A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`.
```

### After glossary entry (generated)

```rst
.. _fls_XC8qChaURmeT:

dereference type chain
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_4GSjPDGBdmka`
A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_7le2vcdbtxbq`
A :t:`construct` that is being resolved is said to be :t:`under resolution`.

:dp:`fls_x3alg07yd7hx`
A :t:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.

:dp:`fls_4hulwazdu20i`
A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:

* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.

* :dp:`fls_ygam5nisv98c`
  Otherwise the :t:`dereference type chain` continues with :t:`type`
  :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_7le2vcdbtxbq`
A :t:`construct` that is being resolved is said to be :dt:`under resolution`.

:dp:`fls_x3alg07yd7hx`
A :dt:`dereference type` is either a :t:`reference type` or a :t:`type` that
implements the :std:`core::ops::Deref` :t:`trait`.

:dp:`fls_4hulwazdu20i`
A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:

* :dp:`fls_ptocwx5p25lj`
  If the previous :t:`dereference type` is a :t:`reference type`, then the
  :t:`dereference type chain` continues with the inner :t:`type` of the
  previous :t:`dereference type`.

* :dp:`fls_ygam5nisv98c`
  Otherwise the :t:`dereference type chain` continues with :t:`type`
  :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## derive macro (derive_macro)

### Before glossary entry (origin/main)

```rst
.. _fls_7ipdj78o7ln:

derive macro
^^^^^^^^^^^^

:dp:`fls_jrrjhl9hocrm`
A :dt:`derive macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of tokens, and is invoked via attribute
:c:`derive`.
```

### After glossary entry (generated)

```rst
.. _fls_120cLedTXcyi:

derive macro
^^^^^^^^^^^^

:dp:`fls_hvWwvn6zMcqp`
A :t:`derive macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`. :t:`[Derive macro]s` are
used to construct new syntax for :t:`[abstract data type]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/macros.rst
:dp:`fls_lfmb22bfnrye`
A :t:`function-like macro` is invoked using a :t:`macro invocation`.

:dp:`fls_fbgal48cgj44`
The sole parameter of the :t:`macro implementation function` captures the
:t:`token` stream produced from the :s:`DelimitedTokenTree` of the
:t:`macro invocation`, excluding outer :s:`[Delimiter]s`.

:dp:`fls_e5x92q2rq8a0`
A :t:`derive macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`. :t:`[Derive macro]s` are
used to construct new syntax for :t:`[abstract data type]s`.

:dp:`fls_ldw75sy5uj7p`
The :t:`macro implementation function` of a :t:`derive macro` shall be subject
to the following restrictions:

* :dp:`fls_7gcnui9beky`
  It shall be subject to :t:`attribute` :c:`proc_macro_derive`,
```

### After chapter excerpt (current)

```rst
src/macros.rst
:dp:`fls_lfmb22bfnrye`
A :t:`function-like macro` is invoked using a :t:`macro invocation`.

:dp:`fls_fbgal48cgj44`
The sole parameter of the :t:`macro implementation function` captures the
:t:`token` stream produced from the :s:`DelimitedTokenTree` of the
:t:`macro invocation`, excluding outer :s:`[Delimiter]s`.

:dp:`fls_e5x92q2rq8a0`
A :dt:`derive macro` is a :t:`procedural macro` that consumes a stream of
:t:`[token]s` and produces a stream of :t:`[token]s`. :t:`[Derive macro]s` are
used to construct new syntax for :t:`[abstract data type]s`.

:dp:`fls_ldw75sy5uj7p`
The :t:`macro implementation function` of a :t:`derive macro` shall be subject
to the following restrictions:

* :dp:`fls_7gcnui9beky`
  It shall be subject to :t:`attribute` :c:`proc_macro_derive`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## destruction (destruction)

### Before glossary entry (origin/main)

```rst
.. _fls_7b3fsp356e9l:

destruction
^^^^^^^^^^^

:dp:`fls_58i2nfhxze3j`
:dt:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.
```

### After glossary entry (generated)

```rst
.. _fls_FX0j0nSO2EWV:

Destruction
^^^^^^^^^^^

:dp:`fls_Cm05pJzfy6RD`
:t:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_7tadh1zel0fc`
Type ``i32`` is a copy type. By the end of the second let statement, ``x`` is
the owner of the original ``42`` and ``y`` is the owner of a cloned ``42``.

:dp:`fls_ywt328hcieka`
Type :std:`core::sync::atomic::AtomicI32` is a move type. By the end of the
second let statement, ``x`` is uninitialized and ``y`` is the sole owner of the
atomic ``42``.

:dp:`fls_e7ucq87s806d`
:t:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :t:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :t:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_7tadh1zel0fc`
Type ``i32`` is a copy type. By the end of the second let statement, ``x`` is
the owner of the original ``42`` and ``y`` is the owner of a cloned ``42``.

:dp:`fls_ywt328hcieka`
Type :std:`core::sync::atomic::AtomicI32` is a move type. By the end of the
second let statement, ``x`` is uninitialized and ``y`` is the sole owner of the
atomic ``42``.

:dp:`fls_e7ucq87s806d`
:dt:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :dt:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :dt:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## destructor (destructor)

### Before glossary entry (origin/main)

```rst
.. _fls_kwxpy451gtc:

destructor
^^^^^^^^^^

:dp:`fls_79pp7o1xooja`
A :dt:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.
```

### After glossary entry (generated)

```rst
.. _fls_oFNOm69cenuL:

destructor
^^^^^^^^^^

:dp:`fls_nUTtnR12Tok2`
A :t:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_e7ucq87s806d`
:t:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :t:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :t:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:t:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`. Such an object is said to be :dt:`dropped`.

:dp:`fls_gfvm70iqu1l4`
An :t:`uninitialized` :t:`variable` is not :t:`dropped`.
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_e7ucq87s806d`
:dt:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :dt:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :dt:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:dt:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`. Such an object is said to be :dt:`dropped`.

:dp:`fls_gfvm70iqu1l4`
An :t:`uninitialized` :t:`variable` is not :t:`dropped`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## destructuring assignment (destructuring_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_2fuu3zr9rn2q:

destructuring assignment
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_7jienn9uzn5k`
A :dt:`destructuring assignment` is an :t:`assignment expression` where
the :t:`assignee operand` is either an :t:`array expression`, a
:t:`struct expression`, or a :t:`tuple expression`.
```

### After glossary entry (generated)

```rst
.. _fls_ugW1VJ0NEIi9:

destructuring assignment
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_iZQg27MOakvI`
A :t:`destructuring assignment` is an :t:`assignment expression` where
the :t:`assignee operand` is either an :t:`array expression`, a :t:`struct
expression`, a :t:`tuple expression` or a :t:`tuple struct call expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
#. :dp:`fls_9i0ctuo099bp`
   The :t:`value` denoted by the :t:`assignee operand` is :t:`dropped`, unless
   the :t:`assignee operand` denotes an uninitialized :t:`variable` or an
   uninitialized :t:`field` of a :t:`variable`.

#. :dp:`fls_hc01gtvlxba`
   The :t:`value` of the :t:`value operand` is :t:`passed <passing convention>`
   into the :t:`place` of the :t:`assignee operand`.

:dp:`fls_2eheo4yo2orm`
A :t:`destructuring assignment` is an :t:`assignment expression` where
the :t:`assignee operand` is either an :t:`array expression`, a :t:`struct
expression`, a :t:`tuple expression` or a :t:`tuple struct call expression`.

:dp:`fls_z8c3b9s9de3x`
The :t:`assignee operand` of a :t:`destructuring assignment` is treated as an
:dt:`assignee pattern` depending on its kind, as follows:

* :dp:`fls_vqb89rkkjw81`
  An :t:`array expression` corresponds to a :t:`slice pattern` with all the
  :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
#. :dp:`fls_9i0ctuo099bp`
   The :t:`value` denoted by the :t:`assignee operand` is :t:`dropped`, unless
   the :t:`assignee operand` denotes an uninitialized :t:`variable` or an
   uninitialized :t:`field` of a :t:`variable`.

#. :dp:`fls_hc01gtvlxba`
   The :t:`value` of the :t:`value operand` is :t:`passed <passing convention>`
   into the :t:`place` of the :t:`assignee operand`.

:dp:`fls_2eheo4yo2orm`
A :dt:`destructuring assignment` is an :t:`assignment expression` where
the :t:`assignee operand` is either an :t:`array expression`, a :t:`struct
expression`, a :t:`tuple expression` or a :t:`tuple struct call expression`.

:dp:`fls_z8c3b9s9de3x`
The :t:`assignee operand` of a :t:`destructuring assignment` is treated as an
:dt:`assignee pattern` depending on its kind, as follows:

* :dp:`fls_vqb89rkkjw81`
  An :t:`array expression` corresponds to a :t:`slice pattern` with all the
  :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## direction modifier (direction_modifier)

### Before glossary entry (origin/main)

```rst
.. _fls_ugIFZlAzDK6H:

direction modifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_8DY7xPVX4nXx`
A :dt:`direction modifier` is a :t:`construct` that indicates whether a
:t:`register argument` initializes a :t:`register`, assigns the :t:`value` of a
:t:`register` to an :t:`expression`, or both.

:dp:`fls_lRKEzY3fQ3B2`
See :s:`DirectionModifier`.
```

### After glossary entry (generated)

```rst
.. _fls_8NzXt5T0QNLN:

direction modifier
^^^^^^^^^^^^^^^^^^

:dp:`fls_EoxPcojMyrUK`
A :t:`direction modifier` is a :t:`construct` that indicates whether a
:t:`register argument` initializes a :t:`register`, assigns the :t:`value` of a
:t:`register` to an :t:`expression`, or both.
```

### Before chapter excerpt (origin/main)

```rst
src/inline-assembly.rst
:dp:`fls_9hhtcey2d4t6`
A :t:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

:dp:`fls_8aynifgq02gt`
A :t:`register class argument` causes an assembler to select a suitable
:t:`register` from the related :t:`register class`.

:dp:`fls_5a3vfresnv5z`
A :t:`direction modifier` is a :t:`construct` that indicates whether a
:t:`register argument` initializes a :t:`register`, assigns the :t:`value` of a
:t:`register` to an :t:`expression`, or both.

:dp:`fls_fta1gb5tzi3a`
An :t:`input register expression` is an :t:`expression` that provides the
initial :t:`value` of a :t:`register`.

:dp:`fls_sopiivuae0x7`
An :t:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.
```

### After chapter excerpt (current)

```rst
src/inline-assembly.rst
:dp:`fls_9hhtcey2d4t6`
A :t:`register class argument` is a :t:`register argument` that uses a
:t:`register class name`.

:dp:`fls_8aynifgq02gt`
A :t:`register class argument` causes an assembler to select a suitable
:t:`register` from the related :t:`register class`.

:dp:`fls_5a3vfresnv5z`
A :dt:`direction modifier` is a :t:`construct` that indicates whether a
:t:`register argument` initializes a :t:`register`, assigns the :t:`value` of a
:t:`register` to an :t:`expression`, or both.

:dp:`fls_fta1gb5tzi3a`
An :t:`input register expression` is an :t:`expression` that provides the
initial :t:`value` of a :t:`register`.

:dp:`fls_sopiivuae0x7`
An :t:`output register expression` is an :t:`expression` that is assigned the
:t:`value` of a :t:`register`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## discriminant (discriminant)

### Before glossary entry (origin/main)

```rst
.. _fls_7vg56eeo0zlg:

discriminant
^^^^^^^^^^^^

:dp:`fls_dfegy9y6awx`
A :dt:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
```

### After glossary entry (generated)

```rst
.. _fls_xGWjLvqLYgJY:

discriminant
^^^^^^^^^^^^

:dp:`fls_KIp8jL1DU6yt`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.

:dp:`fls_hp5frc752dam`
A :t:`discriminant initializer` shall be specified only when all :t:`[enum
variant]s` appear without an :s:`EnumVariantKind`.

:dp:`fls_pijczoq4k9ij`
The :t:`type` of the :t:`expression` of a :t:`discriminant initializer` shall
be either:
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_1PqJYZ5eMNym`
An :dt:`enum field` is a :t:`field` of an :t:`enum variant`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :dt:`discriminant` is an opaque integer that identifies an :t:`enum variant`.

:dp:`fls_IhqHv2D1nuXj`
A :dt:`discriminant initializer` provides the :t:`value` of a
:t:`discriminant`.

:dp:`fls_hp5frc752dam`
A :t:`discriminant initializer` shall be specified only when all :t:`[enum
variant]s` appear without an :s:`EnumVariantKind`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## discriminant initializer (discriminant_initializer)

### Before glossary entry (origin/main)

```rst
.. _fls_xayj37ocbqjn:

discriminant initializer
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_o7hihgcqmnyc`
A :dt:`discriminant initializer` provides the :t:`value` of a :t:`discriminant`.

:dp:`fls_g5obc23vigng`
See :s:`DiscriminantInitializer`.
```

### After glossary entry (generated)

```rst
.. _fls_lMCVp0bVkNQI:

discriminant initializer
^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_8eIreK4vRzTC`
A :t:`discriminant initializer` provides the :t:`value` of a
:t:`discriminant`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_t4yeovFm83Wo`.
src/types-and-traits.rst
:dp:`fls_wQTFwl88VujQ`
An :t:`enum variant` is a :t:`construct` that declares one of the
possible variations of an :t:`enum`.

:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.

:dp:`fls_hp5frc752dam`
A :t:`discriminant initializer` shall be specified only when all :t:`[enum
variant]s` appear without an :s:`EnumVariantKind`.

:dp:`fls_pijczoq4k9ij`
The :t:`type` of the :t:`expression` of a :t:`discriminant initializer` shall
be either:
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.

:dp:`fls_t4yeovFm83Wo`
A :dt:`discriminant` is an opaque integer that identifies an :t:`enum variant`.

:dp:`fls_IhqHv2D1nuXj`
A :dt:`discriminant initializer` provides the :t:`value` of a
:t:`discriminant`.

:dp:`fls_hp5frc752dam`
A :t:`discriminant initializer` shall be specified only when all :t:`[enum
variant]s` appear without an :s:`EnumVariantKind`.

:dp:`fls_pijczoq4k9ij`
The :t:`type` of the :t:`expression` of a :t:`discriminant initializer` shall
be either:
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## discriminant type (discriminant_type)

### Before glossary entry (origin/main)

```rst
.. _fls_a0ezuPLtENme:

discriminant type
^^^^^^^^^^^^^^^^^

:dp:`fls_t4yeovFm83Wo`
A :dt:`discriminant type` is the :t:`type` of a :t:`discriminant`.
```

### After glossary entry (generated)

```rst
.. _fls_ENiFfesicTaA:

discriminant type
^^^^^^^^^^^^^^^^^

:dp:`fls_4AQGFRlK9olK`
A :t:`discriminant type` is the :t:`type` of a :t:`discriminant`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_p0c62ejo1u1t`.
src/types-and-traits.rst
:dp:`fls_fsbf6ist38ix`
:t:`Type representation` may be specified using :t:`attribute` :c:`repr`. An
:t:`enum type`, a :t:`struct type`, or a :t:`union type` that is not subject to
:t:`attribute` :c:`repr` has :t:`default representation`.

:dp:`fls_qkkc8x2oghst`
:t:`Type representation` may be specified using :t:`attribute` :c:`[repr]` and
modified further using :t:`attribute` :c:`[repr]`'s :s:`Alignment`
:t:`[representation modifier]s`. A :t:`representation modifier` shall apply only
to a :t:`struct type` or a :t:`union type` subject to :t:`C representation` or
:t:`default representation`.

:dp:`fls_p0c62ejo1u1t`
:t:`[Zero-variant enum type]s` shall not be subject to :t:`C representation`.

:dp:`fls_efp1kfgkpba8`
The :t:`size` and :t:`alignment` of an :t:`enum type` without :t:`[field]s`
subject to :t:`C representation`, :t:`default representation`, or
:t:`primitive representation` are those of its :t:`discriminant`.

:dp:`fls_s9c0a0lg6c0p`
The :t:`discriminant type` of an :t:`enum type` with :t:`C representation` is
the corresponding :t:`c signed int type` for the target platform's :t:`C`
:t:`ABI`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_qkkc8x2oghst`
:t:`Type representation` may be specified using :t:`attribute` :c:`[repr]` and
modified further using :t:`attribute` :c:`[repr]`'s :s:`Alignment`
:t:`[representation modifier]s`. A :t:`representation modifier` shall apply only
to a :t:`struct type` or a :t:`union type` subject to :t:`C representation` or
:t:`default representation`.

:dp:`fls_p0c62ejo1u1t`
:t:`[Zero-variant enum type]s` shall not be subject to :t:`C representation`.

:dp:`fls_pwtzoGxdQk3U`
A :dt:`discriminant type` is the :t:`type` of a :t:`discriminant`.

:dp:`fls_efp1kfgkpba8`
The :t:`size` and :t:`alignment` of an :t:`enum type` without :t:`[field]s`
subject to :t:`C representation`, :t:`default representation`, or
:t:`primitive representation` are those of its :t:`discriminant`.

:dp:`fls_s9c0a0lg6c0p`
The :t:`discriminant type` of an :t:`enum type` with :t:`C representation` is
the corresponding :t:`c signed int type` for the target platform's :t:`C`
:t:`ABI`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## diverging expression (diverging_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_gDFsAj1Bvx7A:

diverging expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_fLlNzmB34cj9`
A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.
```

### After glossary entry (generated)

```rst
.. _fls_fGxmaZLYc1uN:

diverging expression
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_dNZAyCGxtzzw`
A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_XopG4yS9Q4q1`
It is a static error if the evaluation of a :t:`constant expression` results in
a :t:`value` that is unaligned.

:dp:`fls_tg0kya5125jt`
The invocation of a :t:`constant function` follows the dynamic semantics of a
:t:`non-[constant function]` invocation.

:dp:`fls_oth9vFtcb9l4`
A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.

:dp:`fls_cmBVodJMjZi7`
:t:`[Diverging expression]s` are:

* :dp:`fls_xsOgdiIzysP1`
  :t:`[Break expression]s`,
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_XopG4yS9Q4q1`
It is a static error if the evaluation of a :t:`constant expression` results in
a :t:`value` that is unaligned.

:dp:`fls_tg0kya5125jt`
The invocation of a :t:`constant function` follows the dynamic semantics of a
:t:`non-[constant function]` invocation.

:dp:`fls_oth9vFtcb9l4`
A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.

:dp:`fls_cmBVodJMjZi7`
:t:`[Diverging expression]s` are:

* :dp:`fls_xsOgdiIzysP1`
  :t:`[Break expression]s`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## diverging type variable (diverging_type_variable)

### Before glossary entry (origin/main)

```rst
.. _fls_9DuaIn6cRbXf:

diverging type variable
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_sxyL7yOp3H9s`
A :dt:`diverging type variable` is a :t:`type variable` that can refer to any
:t:`type` and originates from a :t:`diverging expression`.
```

### After glossary entry (generated)

```rst
.. _fls_a6Wz7wsl7Q92:

diverging type variable
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_7GHjdwfrt23j`
A :t:`diverging type variable` is a :t:`type variable` that can refer to any
:t:`type` and originates from a :t:`diverging expression`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
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

:dp:`fls_rvj3XspFZ1u3`
The :t:`type inference` algorithm uses :t:`type unification` to propagate known
:t:`[type]s` of :t:`[expression]s` and :t:`[pattern]s` across the
:t:`type inference root` being inferred. In the rules detailed below, a static
error occurs when :t:`type unification` fails.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
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

:dp:`fls_rvj3XspFZ1u3`
The :t:`type inference` algorithm uses :t:`type unification` to propagate known
:t:`[type]s` of :t:`[expression]s` and :t:`[pattern]s` across the
:t:`type inference root` being inferred. In the rules detailed below, a static
error occurs when :t:`type unification` fails.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## division assignment (division_assignment)

### Before glossary entry (origin/main)

```rst
.. _fls_0lpT9Ncj7S9X:

division assignment
^^^^^^^^^^^^^^^^^^^

:dp:`fls_kvQskrzE1y97`
For :dt:`division assignment`, see :t:`division assignment expression`.
```

### After glossary entry (generated)

```rst
.. _fls_PadcNeQ2wFTt:

division assignment
^^^^^^^^^^^^^^^^^^^

:dp:`fls_mo94ifeZThwX`
A :t:`division assignment` is a :t:`division assignment expression`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_dvy201zd6oym`.
src/expressions.rst
:dp:`fls_s7rey2bndfei`
A :t:`shift right assignment expression` is a
:t:`compound assignment expression` that uses bit shift right arithmetic.

:dp:`fls_7l7v7vigw3fu`
A :t:`subtraction assignment expression` is a
:t:`compound assignment expression` that uses subtraction.

:dp:`fls_dvy201zd6oym`
An :t:`assigned operand` is the target :t:`operand` of a
:t:`compound assignment expression`.

:dp:`fls_9v09ayi2azpe`
A :t:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.

:dp:`fls_row7saf53vwd`
An :t:`assigned operand` shall denote a :t:`mutable assignee expression`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_JxiaXUUJY7lz`
An :dt:`bit or assignment` is a :t:`bit or assignment expression`.

:dp:`fls_0PENxft8n4Vz`
An :dt:`bit xor assignment` is a :t:`bit xor assignment expression`.

:dp:`fls_YUraJ9uJt34w`
A :dt:`division assignment` is a :t:`division assignment expression`.

:dp:`fls_9v09ayi2azpe`
A :t:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
is used in the calculation of a :t:`compound assignment expression`.

:dp:`fls_row7saf53vwd`
An :t:`assigned operand` shall denote a :t:`mutable assignee expression`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## division assignment expression (division_assignment_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_ccv27fji08ou:

division assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_lzuz5fkveikk`
A :dt:`division assignment expression` is a :t:`compound assignment expression`
that uses division.

:dp:`fls_cdxt76aqwtkq`
See :s:`DivisionAssignmentExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_KMnfarVyqSsv:

division assignment expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_JugMAgYJn6mW`
A :t:`division assignment expression` is a :t:`compound assignment expression`
that uses division.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_ak4g5112jkl`
A :t:`bit or assignment expression` is a :t:`compound assignment expression`
that uses bit or arithmetic.

:dp:`fls_lkjwyy78m2vx`
A :t:`bit xor assignment expression` is a :t:`compound assignment expression`
that uses bit exclusive or arithmetic.

:dp:`fls_pkzj0uigfcgm`
A :t:`division assignment expression` is a :t:`compound assignment expression`
that uses division.

:dp:`fls_ndlv3k9uclz2`
A :t:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.

:dp:`fls_fbp5dojti27r`
A :t:`remainder assignment expression` is a :t:`compound assignment expression`
that uses remainder division.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_ak4g5112jkl`
A :dt:`bit or assignment expression` is a :t:`compound assignment expression`
that uses bit or arithmetic.

:dp:`fls_lkjwyy78m2vx`
A :dt:`bit xor assignment expression` is a :t:`compound assignment expression`
that uses bit exclusive or arithmetic.

:dp:`fls_pkzj0uigfcgm`
A :dt:`division assignment expression` is a :t:`compound assignment expression`
that uses division.

:dp:`fls_ndlv3k9uclz2`
A :t:`multiplication assignment expression` is a
:t:`compound assignment expression` that uses multiplication.

:dp:`fls_fbp5dojti27r`
A :t:`remainder assignment expression` is a :t:`compound assignment expression`
that uses remainder division.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## division expression (division_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_vxd5q8nekkn0:

division expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_du05yp205f4y`
A :dt:`division expression` is an :t:`arithmetic expression` that uses division.

:dp:`fls_d3vwk4autyd`
See :s:`DivisionExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_tWA6R9fPcfF9:

division expression
^^^^^^^^^^^^^^^^^^^

:dp:`fls_U07WKFlMFRUA`
A :t:`division expression` is an :t:`arithmetic expression` that uses division.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_vk17mfv47wk9`
The :t:`type` of an :t:`addition expression` is :t:`associated type`
:std:`core::ops::Add::Output`.

:dp:`fls_ryzhdpxgm7ii`
The :t:`value` of an :t:`addition expression` is the result of
``core::ops::Add::add(left_operand, right_operand)``.

:dp:`fls_dstca76y08ge`
A :t:`division expression` is an :t:`arithmetic expression` that uses division.

:dp:`fls_f1puss9t4btz`
The :t:`type` of the :t:`left operand` of a :t:`division expression` shall
implement the :std:`core::ops::Div` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_5rdrkvspw57z`
The :t:`type` of a :t:`division expression` is :t:`associated type`
:std:`core::ops::Div::Output`.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_vk17mfv47wk9`
The :t:`type` of an :t:`addition expression` is :t:`associated type`
:std:`core::ops::Add::Output`.

:dp:`fls_ryzhdpxgm7ii`
The :t:`value` of an :t:`addition expression` is the result of
``core::ops::Add::add(left_operand, right_operand)``.

:dp:`fls_dstca76y08ge`
A :dt:`division expression` is an :t:`arithmetic expression` that uses division.

:dp:`fls_f1puss9t4btz`
The :t:`type` of the :t:`left operand` of a :t:`division expression` shall
implement the :std:`core::ops::Div` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_5rdrkvspw57z`
The :t:`type` of a :t:`division expression` is :t:`associated type`
:std:`core::ops::Div::Output`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## doc comment (doc_comment)

### Before glossary entry (origin/main)

```rst
.. _fls_4nm1r57ntecm:

doc comment
^^^^^^^^^^^

:dp:`fls_wkc1w2xk7ebh`
A :dt:`doc comment` is a :t:`comment` class that includes
:t:`[inner block doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`,
and :t:`[outer line doc]s`.
```

### After glossary entry (generated)

```rst
.. _fls_SWLN0INaLNor:

doc comment
^^^^^^^^^^^

:dp:`fls_zdO4u2uzogqy`
A :t:`doc comment` is a :t:`comment` class that includes :t:`[inner block
doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`, and :t:`[outer line
doc]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/lexical-elements.rst
:dp:`fls_scko7crha0um`
An :t:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

:dp:`fls_RYVL9KgaxKvl`
An :t:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

:dp:`fls_7n6d3jx61ose`
A :t:`doc comment` is a :t:`comment` class that includes :t:`[inner block
doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`, and :t:`[outer line
doc]s`.

:dp:`fls_6fxcs17n4kw`
Character 0x0D (carriage return) shall not appear in a :t:`comment`.

:dp:`fls_uze7l7cxonk1`
:t:`[Block comment]s`, :t:`[inner block doc]s`, and :t:`[outer block doc]s`
shall extend one or more :t:`[line]s`.
```

### After chapter excerpt (current)

```rst
src/lexical-elements.rst
:dp:`fls_scko7crha0um`
An :t:`outer line doc` is a :t:`line comment` that applies to a subsequent
:t:`non-[comment]` :t:`construct`.

:dp:`fls_RYVL9KgaxKvl`
An :t:`outer doc comment` is either an :t:`outer block doc` or an
:t:`outer line doc`.

:dp:`fls_7n6d3jx61ose`
A :dt:`doc comment` is a :t:`comment` class that includes :t:`[inner block
doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`, and :t:`[outer line
doc]s`.

:dp:`fls_6fxcs17n4kw`
Character 0x0D (carriage return) shall not appear in a :t:`comment`.

:dp:`fls_uze7l7cxonk1`
:t:`[Block comment]s`, :t:`[inner block doc]s`, and :t:`[outer block doc]s`
shall extend one or more :t:`[line]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## drop construct (drop_construct)

### Before glossary entry (origin/main)

```rst
.. _fls_nw0qr4xy3zxq:

drop construct
^^^^^^^^^^^^^^

:dp:`fls_odg2asgj28m`
A :dt:`drop construct` is a :t:`construct` that employs a :t:`drop scope`.
```

### After glossary entry (generated)

```rst
.. _fls_VL5OZ6vgSnqO:

drop construct
^^^^^^^^^^^^^^

:dp:`fls_ux2FRaJidyB1`
A :t:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_fmn33zhorkf`
Object ``uninitialized`` is not dropped.

:dp:`fls_7uav7vkcv4pz`
A :t:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_txvxrn6wbyql`
A :t:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:

* :dp:`fls_n6y6brm6pghr`
  :t:`[Expression]s`,

* :dp:`fls_gdh6wwvi7ci6`
  :t:`[Function]s`,
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_7uav7vkcv4pz`
A :dt:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_vWILlWIfhB69`
:dt:`Drop order` is the order by which :t:`[value]s` are :t:`dropped` when a
:t:`drop scope` is left.

:dp:`fls_txvxrn6wbyql`
A :dt:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:

* :dp:`fls_n6y6brm6pghr`
  :t:`[Expression]s`,

* :dp:`fls_gdh6wwvi7ci6`
  :t:`[Function]s`,
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## drop order (drop_order)

### Before glossary entry (origin/main)

```rst
.. _fls_j12e358828h:

drop order
^^^^^^^^^^

:dp:`fls_qddkiabu6swt`
:dt:`Drop order` is the order by which :t:`[value]s` are :t:`dropped` when a
:t:`drop scope` is left.
```

### After glossary entry (generated)

```rst
.. _fls_0kaWQcu21weZ:

Drop order
^^^^^^^^^^

:dp:`fls_ocP3Xa8f898n`
:t:`Drop order` is the order by which :t:`[value]s` are :t:`dropped` when a
:t:`drop scope` is left.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_7uav7vkcv4pz`.
src/ownership-and-deconstruction.rst
:dp:`fls_tw36n3g32a0y`
When object ``array`` is dropped, its destructor drops the first element, then
the second element.

:dp:`fls_fmn33zhorkf`
Object ``uninitialized`` is not dropped.

:dp:`fls_7uav7vkcv4pz`
A :t:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_txvxrn6wbyql`
A :t:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:

* :dp:`fls_n6y6brm6pghr`
  :t:`[Expression]s`,
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_fmn33zhorkf`
Object ``uninitialized`` is not dropped.

:dp:`fls_7uav7vkcv4pz`
A :dt:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_vWILlWIfhB69`
:dt:`Drop order` is the order by which :t:`[value]s` are :t:`dropped` when a
:t:`drop scope` is left.

:dp:`fls_txvxrn6wbyql`
A :dt:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:

* :dp:`fls_n6y6brm6pghr`
  :t:`[Expression]s`,
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## drop scope (drop_scope)

### Before glossary entry (origin/main)

```rst
.. _fls_foszri7hdym0:

drop scope
^^^^^^^^^^

:dp:`fls_6bu8x0g9q0er`
A :dt:`drop scope` is a region of program text that governs the :t:`dropping`
of :t:`[value]s`.
```

### After glossary entry (generated)

```rst
.. _fls_8ZpdSrrSHB0p:

drop scope
^^^^^^^^^^

:dp:`fls_cpDpc19gUG69`
A :t:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_tw36n3g32a0y`
When object ``array`` is dropped, its destructor drops the first element, then
the second element.

:dp:`fls_fmn33zhorkf`
Object ``uninitialized`` is not dropped.

:dp:`fls_7uav7vkcv4pz`
A :t:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_txvxrn6wbyql`
A :t:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:

* :dp:`fls_n6y6brm6pghr`
  :t:`[Expression]s`,
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_tw36n3g32a0y`
When object ``array`` is dropped, its destructor drops the first element, then
the second element.

:dp:`fls_fmn33zhorkf`
Object ``uninitialized`` is not dropped.

:dp:`fls_7uav7vkcv4pz`
A :dt:`drop scope` is a region of program text that governs the :t:`dropping` of
:t:`[value]s`. When control flow leaves a :t:`drop scope`, all :t:`[value]s`
associated with that :t:`drop scope` are :t:`dropped` based on a
:t:`drop order`.

:dp:`fls_vWILlWIfhB69`
:dt:`Drop order` is the order by which :t:`[value]s` are :t:`dropped` when a
:t:`drop scope` is left.

:dp:`fls_txvxrn6wbyql`
A :dt:`drop construct` is a :t:`construct` that employs a :t:`drop scope`. The
following :t:`[construct]s` are :t:`[drop construct]s`:
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## drop scope extension (drop_scope_extension)

### Before glossary entry (origin/main)

```rst
.. _fls_qp3ksd2lxm8:

drop scope extension
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_pmdh8kkrwkd0`
:dt:`Drop scope extension` is the process of extending a :t:`drop scope`
associated with a :t:`temporary` to prevent the premature :t:`dropping` of the
:t:`temporary`.
```

### After glossary entry (generated)

```rst
.. _fls_Z9RvUDTTEuTA:

Drop scope extension
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_O33fjlx3UK7T`
:t:`Drop scope extension` is the process of extending a :t:`drop scope`
associated with a :t:`temporary` to prevent the premature :t:`dropping` of the
:t:`temporary`.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
* :dp:`fls_ptk6yibqyfzi`
  The :t:`drop scope` of the :t:`operand` of a :t:`match arm guard`.

* :dp:`fls_dltmd8e8c5ia`
  The :t:`drop scope` of the :t:`right operand` of a
  :t:`lazy boolean expression`.

:dp:`fls_kflqez2mtbit`
:t:`Drop scope extension` is the process of extending a :t:`drop scope`
associated with a :t:`temporary` to prevent the premature :t:`dropping` of the
:t:`temporary`.

:dp:`fls_xjw82bujm148`
An :dt:`extending pattern` is either

* :dp:`fls_965wt48ooqyw`
  A :t:`reference identifier pattern`, or
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
* :dp:`fls_ptk6yibqyfzi`
  The :t:`drop scope` of the :t:`operand` of a :t:`match arm guard`.

* :dp:`fls_dltmd8e8c5ia`
  The :t:`drop scope` of the :t:`right operand` of a
  :t:`lazy boolean expression`.

:dp:`fls_kflqez2mtbit`
:dt:`Drop scope extension` is the process of extending a :t:`drop scope`
associated with a :t:`temporary` to prevent the premature :t:`dropping` of the
:t:`temporary`.

:dp:`fls_xjw82bujm148`
An :dt:`extending pattern` is either

* :dp:`fls_965wt48ooqyw`
  A :t:`reference identifier pattern`, or
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## drop type (drop_type)

### Before glossary entry (origin/main)

```rst
.. _fls_4v6vsuw4g89l:

drop type
^^^^^^^^^

:dp:`fls_ot3e31kwixil`
A :dt:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`destructor`.
```

### After glossary entry (generated)

```rst
.. _fls_glGzLftzcljz:

drop type
^^^^^^^^^

:dp:`fls_DoxWFDRKCt9B`
A :t:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_ywt328hcieka`
Type :std:`core::sync::atomic::AtomicI32` is a move type. By the end of the
second let statement, ``x`` is uninitialized and ``y`` is the sole owner of the
atomic ``42``.

:dp:`fls_e7ucq87s806d`
:t:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :t:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :t:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:t:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`. Such an object is said to be :dt:`dropped`.
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_ywt328hcieka`
Type :std:`core::sync::atomic::AtomicI32` is a move type. By the end of the
second let statement, ``x`` is uninitialized and ``y`` is the sole owner of the
atomic ``42``.

:dp:`fls_e7ucq87s806d`
:dt:`Destruction` is the process of recovering resources associated with a
:t:`value` as it goes out of scope.

:dp:`fls_9m0gszdle0qb`
A :dt:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :dt:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:dt:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`. Such an object is said to be :dt:`dropped`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## dropping (dropping)

### Before glossary entry (origin/main)

```rst
.. _fls_68cl4paduzx2:

dropping
^^^^^^^^

:dp:`fls_k4mguykh8ey`
:dt:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_inMQwxJa0ZTS:

Dropping
^^^^^^^^

:dp:`fls_xNJ5zm7GRf8H`
:t:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_9m0gszdle0qb`
A :t:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :t:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:t:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`. Such an object is said to be :dt:`dropped`.

:dp:`fls_gfvm70iqu1l4`
An :t:`uninitialized` :t:`variable` is not :t:`dropped`.

:dp:`fls_l2xkdjeydqtx`
:t:`Dropping` an :t:`initialized` :t:`variable` proceeds as follows:
```

### After chapter excerpt (current)

```rst
src/ownership-and-deconstruction.rst
:dp:`fls_9m0gszdle0qb`
A :dt:`drop type` is a :t:`type` that implements the :std:`core::ops::Drop`
:t:`trait` or contains a :t:`field` that has a :t:`drop type`.

:dp:`fls_4nkzidytpi6`
A :dt:`destructor` is a :t:`function` that is invoked immediately before the
:t:`destruction` of a :t:`value` of a :t:`drop type`.

:dp:`fls_wzuwapjqtyyy`
:dt:`Dropping` a :t:`value` is the act of invoking the :t:`destructor` of the
related :t:`type`.

:dp:`fls_8U45VMMfCU7F`
A :t:`value` is :dt:`dropped` when its :t:`destructor` is invoked.

:dp:`fls_gfvm70iqu1l4`
An :t:`uninitialized` :t:`variable` is not :t:`dropped`.

:dp:`fls_l2xkdjeydqtx`
:t:`Dropping` an :t:`initialized` :t:`variable` proceeds as follows:
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## dynamically sized type (dynamically_sized_type)

### Before glossary entry (origin/main)

```rst
.. _fls_6uovyjjzh6km:

dynamically sized type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_eeyxu730z2pw`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the
:std:`core::marker::Sized` :t:`trait`.
```

### After glossary entry (generated)

```rst
.. _fls_vDrmsJuJffOt:

dynamically sized type
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_QJIacxuPC9CL`
A :t:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
:dp:`fls_drxl7u3etfp9`
The last :t:`where clause` is rejected, but may still be consumed by
:t:`[macro]s`.

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
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
:dp:`fls_kdbq02iguzgl`
All :t:`[value]s` have an :t:`alignment` and a :t:`size`.

:dp:`fls_c6lSeub6RBUV`
A :dt:`fixed sized type` is a :t:`type` that implements the
:std:`core::marker::Sized` :t:`trait`.

:dp:`fls_26Xgem831Nqg`
A :dt:`dynamically sized type` is a :t:`type` that does not implement the :std:`core::marker::Sized` :t:`trait`.

:dp:`fls_ozYgHEHFTT5c`
A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.

:dp:`fls_w1KifBNDp4VE`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.
