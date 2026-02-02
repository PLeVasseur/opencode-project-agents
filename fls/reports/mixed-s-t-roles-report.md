# Mixed :s: and :t: Usage Report

Scope: `/home/pete.levasseur/project/fls/src/**/*.rst` excluding `src/changelog.rst`.

## Category Summary
- **Dynamic semantics rule header**: 2 paragraph(s)
  - Example: `/home/pete.levasseur/project/fls/src/expressions.rst` lines 1275-1277
  - Example: `/home/pete.levasseur/project/fls/src/expressions.rst` lines 1307-1309
- **Glossary definition linking term to syntax**: 14 paragraph(s)
  - Example: `/home/pete.levasseur/project/fls/src/glossary.rst` lines 1035-1037
  - Example: `/home/pete.levasseur/project/fls/src/glossary.rst` lines 1130-1134
- **Legality rule referencing syntax production**: 80 paragraph(s)
  - Example: `/home/pete.levasseur/project/fls/src/associated-items.rst` lines 47-49
  - Example: `/home/pete.levasseur/project/fls/src/attributes.rst` lines 411-413
- **Macro processing rule**: 29 paragraph(s)
  - Example: `/home/pete.levasseur/project/fls/src/macros.rst` lines 185-189
  - Example: `/home/pete.levasseur/project/fls/src/macros.rst` lines 268-271
- **Syntax category definition**: 5 paragraph(s)
  - Example: `/home/pete.levasseur/project/fls/src/lexical-elements.rst` lines 460-462
  - Example: `/home/pete.levasseur/project/fls/src/lexical-elements.rst` lines 1119-1124

## Inferred Heuristics for Mixed :s: and :t: Usage
- :s: names grammar productions or syntactic categories, while :t: names semantic entities, concepts, or roles; mixed usage usually links a syntax fragment to its semantic meaning or constraint.
- Mixed usage appears frequently in Legality Rules to constrain where a syntactic form (e.g., :s:`TypeBoundList`, :s:`FunctionParameterVariadicPart`) is allowed for a semantic construct (e.g., :t:`function`, :t:`associated type`).
- In Syntax sections, :s: supplies the category being defined and :t: supplies the broader lexical/semantic classification (e.g., a lexical element category or keyword class).
- In Glossary entries, :t: defines the term and :s: anchors the definition to a concrete syntax production or token class, bridging terminology to grammar.
- In macro-related rules, :s: is used for token-tree/grammar artifacts and :t: for macro concepts and processing stages, reflecting the translation pipeline from syntax to macro semantics.
- Dynamic Semantics headers mix :t: for the evaluation concept and :s: for the operator grammar, signalling a rule that elaborates operational behavior for a specific syntactic form.

## Complete Paragraph List
### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/associated-items.rst`
- Lines: 47-49
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_wasocqdnuzd1`
An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
:t:`associated trait type`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 411-413
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_930o6urn669w`
:t:`Attribute` :c:`inline` without an :s:`InlineHint` suggests to a tool that
:t:`inlining` should be performed.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 415-417
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_z7ufiqqujgdh`
:t:`Attribute` :c:`inline` with :s:`InlineHint` ``always`` suggests to a tool
that :t:`inlining` should always be performed.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 419-421
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_f0n4g5uky9tp`
:t:`Attribute` :c:`inline` with :s:`InlineHint` ``never`` suggests to a tool
that :t:`inlining` should never be performed.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 989-993
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_rzw12sagm585`
An :t:`attribute` :c:`cfg_attr` where the related
:t:`configuration predicate` evaluates to ``true`` is replaced with a new
:t:`attribute` for each :s:`AttributeContent` enumerated in the
:t:`[attribute]'s` :s:`AttributeContentList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 1916-1919
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_ir9i4i2x5gyx`
:t:`Attribute` :dc:`proc_macro_derive` turns the related :t:`function` into a
:t:`derive macro`, where :s:`DeriveName` defines the :t:`name` of the
:t:`derive macro` available to :t:`attribute` :c:`derive`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 1921-1923
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_NydVxyb43TH6`
The :s:`HelperAttributeList` declares the :t:`[derive helper attribute]s` of
the :t:`derive macro`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/attributes.rst`
- Lines: 2238-2241
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_bcoq5aus8nkr`
If :s:`ExpectedPanicMessage` is specified, then the related
:t:`testing function` passes only when the :t:`panic` message contains the
:s:`ExpectedPanicMessage`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/entities-and-resolution.rst`
- Lines: 332-336
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_cw006jhlboa`
If a :t:`simple path` appears in a :t:`use import` and starts with a
:t:`path segment` expressed as :t:`keyword` ``self``, then the :t:`path` shall
be part of the :s:`UseImportContent` of a :t:`nesting import` as long as the
:t:`path` is a :t:`single segment path`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/entities-and-resolution.rst`
- Lines: 513-514
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_6o38qhbna46z`
A :t:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/entities-and-resolution.rst`
- Lines: 544-546
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_3qm3vh97bvpb`
A :t:`generic parameter` of a :t:`type bound predicate` is :t:`in scope` within
the related :s:`TypeBoundList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 673-675
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_DfCne8YWevLE`
When the remaining :t:`[lexical element]s` of a :s:`StatementList` match either
an :s:`Expression` or :s:`Statement` they are interpreted as an :s:`Expression`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1248-1251
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_plcut8vzdwox`
The :t:`type` of the :t:`operand` of a :t:`negation expression` with a
:s:`BitwiseNegationOperator` shall implement the :std:`core::ops::Not`
:t:`trait`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1253-1255
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_ohu0kljfexd3`
The :t:`type` of a :t:`negation expression` with a :s:`BitwiseNegationOperator`
is :t:`associated type` :std:`core::ops::Not::Output`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1257-1259
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_ghqvj8q71o97`
The :t:`value` of a :t:`negation expression` with a :s:`BitwiseNegationOperator`
is the result of ``core::ops::Not::not(operand)``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1261-1263
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_3m4mgqnzqhri`
The :t:`type` of the :t:`operand` of a :t:`negation expression` with a
:s:`SignNegationOperator` shall implement the :std:`core::ops::Neg` :t:`trait`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1265-1267
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_u7gzm6n75rzm`
The :t:`type` of a :t:`negation expression` with a :s:`SignNegationOperator`
shall be :t:`associated type` :std:`core::ops::Neg::Output`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1269-1271
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_9rmq7iaf092d`
The :t:`value` of a :t:`negation expression` with a :s:`SignNegationOperator` is
the result of ``core::ops::Neg::neg(operand)``.
```

### Dynamic semantics rule header
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1275-1277
- Context: rubric `Dynamic Semantics`, list item `no`

```rst
:dp:`fls_yzt6pcsvj3a`
The :t:`evaluation` of a :t:`negation expression` with a
:s:`BitwiseNegationOperator` proceeds as follows:
```

### Dynamic semantics rule header
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 1307-1309
- Context: rubric `Dynamic Semantics`, list item `no`

```rst
:dp:`fls_tsou6yz4mfte`
The :t:`evaluation` of a :t:`negation expression` with a
:s:`SignNegationOperator` proceeds as follows:
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 3726-3727
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_af1WL2mBKMfW`
  If the :t:`closure expression` specifies a :s:`ClosureBodyWithReturnType`, then the :t:`return type` is the specified :s:`ReturnTypeWithoutBounds`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/expressions.rst`
- Lines: 3753-3754
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_XWJ9SFggdVeH`
  If the :t:`closure parameter` lacks a :s:`TypeSpecification`, the :t:`type` is inferred form the usage of the :t:`closure parameter`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 189-190
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_4XOoiFloXM7t`
  If the :t:`external block` specifies an :s:`AbiKind`, then the :t:`ABI` is the specified :s:`AbiKind`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 220-221
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_l88r9fj82650`
An :t:`external function` shall be invoked from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 223-224
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_qwchgvvnp0qe`
An :t:`external function` shall not specify a :s:`FunctionQualifierList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 230-232
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_m7tu4w4lk8v`
An :t:`external function` shall not specify a :s:`GenericParameterList`
containing :t:`[constant parameter]s` or :t:`[type parameter]s`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 234-235
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_rdu4723vp0oo`
An :t:`external function` shall not specify a :s:`FunctionBody`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 241-243
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_juob30rst11r`
Only the last parameter :s:`FunctionParameter` of an :t:`external function` may
specify a :s:`FunctionParameterVariadicPart`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/ffi.rst`
- Lines: 259-260
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_fo9with6xumo`
An :t:`external static` shall be referenced from an :t:`unsafe context` unless it is defined in an :t:`unsafe external block` and subject to :s:`ItemSafety` with keyword ``safe``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/functions.rst`
- Lines: 81-82
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_PGtp39f6gJwU`
  If the :t:`function parameter` is a :t:`self parameter` without a :s:`TypeSpecification`:
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/functions.rst`
- Lines: 106-108
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_o4uSLPo00KUg`
A :dt:`variadic function` is an :t:`external function` that specifies
:s:`FunctionParameterVariadicPart` as the last :t:`function parameter`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/functions.rst`
- Lines: 146-147
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_C7dvzcXcpQCy`
  If the :s:`FunctionDeclaration` specifies a :s:`ReturnType`, then the :t:`return type` is the specified :s:`ReturnType`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/functions.rst`
- Lines: 203-204
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_7ucwmzqtittv`
An :t:`unsafe function` is a :t:`function` subject to an :s:`ItemSafety` with :t:`keyword` ``unsafe``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/functions.rst`
- Lines: 206-207
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_nUADhgcfvvGC`
A :t:`function` shall only be subject to an :s:`ItemSafety` with :t:`keyword` ``safe`` if it is an :t:`external function` in an :t:`unsafe external block`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/generics.rst`
- Lines: 162-164
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_5r7ontjlmgwj`
  As a :t:`constant argument` of an :t:`[associated type]'s`
  :s:`InitializationType`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 1035-1037
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_my4r1l3ilyt2`
A :dt:`byte string literal` is a :t:`literal` that consists of multiple
:s:`[AsciiCharacter]s`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 1130-1134
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_YTQmXotFOXWU`
:dt:`Call site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroInvocation` site. :t:`[Identifier]s` with :t:`call site hygiene` can
reference the environment of the :s:`MacroRulesDeclaration`, can reference the
environment of the :s:`MacroInvocation`, and are considered :t:`unhygienic`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 1687-1692
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_2Y1Dpw5ZEqT3`
:dt:`Definition site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site. :t:`[Identifier]s` with
:t:`definition site hygiene` cannot reference the environment of the
:s:`MacroRulesDeclaration`, cannot be referenced by the environment of a
:s:`MacroInvocation`, and are considered :t:`hygienic`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 3404-3405
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_tbldwtisl9vc`
An :dt:`inline module` is a :t:`module` with an :s:`InlineModuleSpecification`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 4260-4264
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_hjJpNmKiZxlT`
:dt:`Mixed site hygiene` is a type of :t:`hygiene` which resolves to the
:s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
and is considered :t:`partially hygienic`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 4718-4720
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_wS4EzN0N1GDP`
An :dt:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 4784-4786
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_xhe5gmr0r9zn`
An :dt:`outline module` is a :t:`module` with an
:s:`OutlineModuleSpecification`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 5499-5501
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 5508-5509
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 5900-5903
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_dux9js5oixjd`
:dt:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 6161-6163
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_XpbU4Up0Aza8`
A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
of multiple :s:`[AsciiCharacter]s`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 6733-6736
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_a19q6lhvakcm`
:dt:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 6862-6864
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_eduQhUYBEkVx`
A :dt:`tuple enum variant` is an :t:`enum variant` with a
:s:`TupleStructFieldList`.
```

### Glossary definition linking term to syntax
- File: `/home/pete.levasseur/project/fls/src/glossary.rst`
- Lines: 6919-6920
- Context: rubric `none`, list item `no`

```rst
:dp:`fls_pdcpmapiq491`
A :dt:`tuple struct` is a :t:`struct` with a :s:`TupleStructFieldList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1584-1586
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_h8549stij7pj`
:t:`[Assembly option]s` ``att_syntax`` and ``raw`` shall appear only in
:s:`GlobalAsmArguments`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1628-1631
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_m0SBtonaNppV`
The :s:`AssemblyInstruction`, :s:`RegisterArgument`, :s:`AbiClobber`, and
:s:`AssemblyOption` arguments in :s:`AsmArguments` and :s:`GlobalAsmArguments`
may be preceded by :t:`outer attribute` instances.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1637-1642
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_xzDPz2zfRfoI`
If a :s:`AssemblyInstruction`, :s:`RegisterArgument`, :s:`AbiClobber`, or
:s:`AssemblyOption` is annotated with :c:`cfg` or :c:`cfg_attr` and the related
:t:`configuration predicate` evaluates to ``false``, the annotated argument is
not considered part of the related macro invocation, consistent with
:t:`conditional compilation`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1644-1647
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_cTEiqjf6haEg`
It is a static error for a :s:`RegisterArgument`, :s:`AbiClobber`, or
:s:`AssemblyOption` to appear before the first :s:`AssemblyInstruction`, even if
the argument is ignored by :t:`conditional compilation`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1700-1702
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_1ikzov7cxic1`
When invoking :t:`macro` :std:`core::arch::asm`, the :s:`DelimitedTokenTree` of
the related :t:`macro invocation` shall follow the syntax of :s:`AsmArguments`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/inline-assembly.rst`
- Lines: 1711-1715
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_tgzga1lanfuo`
When invoking :t:`macro` :std:`core::arch::global_asm` and
:t:`macro` :std:`core::arch::naked_asm`, the
:s:`DelimitedTokenTree` of the related :t:`macro invocation` shall follow the
syntax of :s:`GlobalAsmArguments`.
```

### Syntax category definition
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 460-462
- Context: rubric `Syntax`, list item `no`

```rst
:dp:`fls_ls7ymvgd5kfa`
A :ds:`RawIdentifierKeyword` is any :t:`keyword` in category :s:`Keyword`,
except ``crate``, ``self``, ``Self``, and ``super``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 494-496
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_irwcldiotei2`
A :t:`pure identifier` shall be restricted to characters in category
:s:`AsciiCharacter` in the following contexts:
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 622-624
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_t63zfv5JdUhj`
A :t:`byte string literal` is a :t:`literal` that consists of multiple
:s:`[AsciiCharacter]s`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 654-656
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_moe3zfx39ox2`
A :t:`simple byte string literal` is a :t:`byte string literal` that consists of multiple
:s:`[AsciiCharacter]s`.
```

### Syntax category definition
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 1119-1124
- Context: rubric `Syntax`, list item `no`

```rst
:dp:`fls_5v9gx22g5wPm`
A :ds:`UnicodeEscape` starts with a ``\u{`` literal, followed by 1 to 6
instances of a :s:`HexadecimalDigit`, inclusive, followed by a ``}`` character.
It can represent any :t:`Unicode` codepoint between U+00000 and U+10FFFF,
inclusive, except :t:`Unicode` surrogate codepoints, which exist between
the range of U+D800 and U+DFFF, inclusive.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 1549-1551
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_bl55g03jmayf`
Word ``macro_rules`` acts as a :t:`keyword` only when used in the context of a
:s:`MacroRulesDefinition`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 1553-1555
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_c354oryv513p`
Word ``'static`` acts as a :t:`keyword` only when used in the context of a
:s:`LifetimeIndication`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 1557-1559
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_r9fhuiq1ys1p`
Word ``union`` acts as a :t:`keyword` only when used in the context of a
:s:`UnionDeclaration`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/lexical-elements.rst`
- Lines: 1561-1562
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_g0JEluWqBpNc`
Word ``safe`` acts as a :t:`keyword` only when used as a qualifier of :s:`FunctionDeclaration` or :s:`StaticDeclaration` in the context of a :s:`ExternalBlock`.
```

### Syntax category definition
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 67-69
- Context: rubric `Syntax`, list item `no`

```rst
:dp:`fls_ikzjsq8heyk6`
A :ds:`MacroMatchToken` is any :t:`lexical element` in category
:s:`LexicalElement`, except punctuation ``$`` and category :s:`Delimiter`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 185-189
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_NBbygZwUxjFp`
  ``vis`` shall only be followed by ``,``, an :t:`identifier` except for
  ``priv``, any token that may begin a :s:`TypeSpecification`, or a
  :t:`metavariable` with the ``ident``, ``ty`` or ``block``
  :t:`fragment specifier` kind.
```

### Syntax category definition
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 229-232
- Context: rubric `Syntax`, list item `no`

```rst
:dp:`fls_4ps4x4513xau`
A :ds:`MacroRepetitionSeparator` is any :t:`lexical element` in category
:s:`LexicalElement`, except punctuation ``+``, ``*``, ``?``, and category
:s:`Delimiter`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 268-271
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_Sm4qVsHKYLY2`
  If the :t:`macro repetition` has a :t:`separator`, the :t:`separator` shall
  be allowed by the :s:`MacroRepetitionMatchContent`'s
  :t:`[fragment specifier restriction]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 273-277
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_Rdvs8Dz6OUU7`
  If the :t:`repetition operator` is ``*`` or ``+``, then the
  possible beginnings of the :s:`MacroRepetitionMatchContent` shall be allowed
  by its :s:`MacroRepetitionMatchContent`'s
  :t:`[fragment specifier restriction]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 279-282
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_UIlj6Csow81w`
  If the :t:`repetition operator` is ``?`` or ``*``, then the succeeding
  :s:`MacroMatch` must be allowed by the preceding :s:`MacroMatch`'s
  :t:`[fragment specifier restriction]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 284-287
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_yp2XxDv4DzEi`
  The possible beginnings of the :s:`MacroRepetitionMatchContent` must be
  allowed by the preceding :s:`MacroMatch`'s
  :t:`[fragment specifier restriction]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 289-291
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_n5TkJKWiDhCD`
  The succeeding :s:`MacroMatch` must be allowed by the possible endings of the
  :s:`MacroRepetitionMatchContent`'s :t:`[fragment specifier restriction]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 365-368
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_fbgal48cgj44`
The sole parameter of the :t:`macro implementation function` captures the
:t:`token` stream produced from the :s:`DelimitedTokenTree` of the
:t:`macro invocation`, excluding outer :s:`[Delimiter]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 418-421
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_caa16usjxryg`
The sole parameter of the :t:`macro implementation function` captures
the :t:`token` stream produced from the related :s:`EnumDeclaration`,
:s:`StructDeclaration`, or :s:`UnionDeclaration`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 488-493
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_fku5beu3mr4c`
The first :t:`function parameter` of the :t:`macro implementation function`
captures the :t:`token` stream produced from the :s:`DelimitedTokenTree`
of the invoking :t:`attribute`, excluding outer :s:`[Delimiter]s`. If no
:s:`DelimitedTokenTree` is provided, then the :t:`token` stream is considered
empty.
```

### Syntax category definition
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 539-541
- Context: rubric `Syntax`, list item `no`

```rst
:dp:`fls_wushtmw9qt3y`
A :ds:`NonDelimitedToken` is any :t:`lexical element` in category
:s:`LexicalElement`, except category :s:`Delimiter`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 617-620
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_40xq8Ri1OMZZ`
   The :s:`TokenTree` of the :t:`macro invocation` has all
   :t:`[outer block doc]s` and :t:`[outer line doc]s` contained within replaced
   by their equivalent :t:`attribute` :c:`doc` representation.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 622-626
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_76prdp6k1fga`
   The :s:`TokenTree` of the :t:`macro invocation` is matched against the
   :t:`[macro rule]s` of the resolved :t:`macro` by considering individual
   :t:`[macro matcher]s`. It is a static error if no :t:`macro matcher` is
   satisfied.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 667-670
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_nNrs4EC3ff5T`
   The :s:`TokenTree` of the :t:`macro invocation` has all :t:`[outer block
   doc]s` and :t:`[outer line doc]s` contained within replaced by their
   equivalent :t:`attribute` :c:`doc` representation.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 672-674
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_srtqkdceaz5t`
   The :s:`TokenTree` of the :t:`macro invocation` is transformed into a
   corresponding :std:`proc_macro::TokenStream`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 732-738
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_my93neopj9x0`
   The returned :std:`proc_macro::TokenStream` of the
   :t:`macro implementation function` call is appended to the enclosing
   :t:`block expression` or :t:`module` where the related :s:`EnumDeclaration`,
   :s:`StructDeclaration`, or :s:`UnionDeclaration` resides. It is a static
   error if the output :std:`proc_macro::TokenStream` does not constitute zero
   or more :t:`[item]s`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 743-749
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_tjn92evtlflq`
   The :s:`DelimitedTokenTree` of the invoking :t:`attribute macro` is
   transformed into a corresponding :std:`proc_macro::TokenStream` without
   the outer :s:`[Delimiter]s`. If no :s:`DelimitedTokenTree` is provided,
   and empty :std:`proc_macro::TokenStream` is used. This
   :std:`proc_macro::TokenStream` constitutes the first :t:`function parameter`
   of the :t:`macro implementation function`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 791-794
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_77ucvwu6idms`
:t:`Rule matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy the :t:`macro matcher` of a :t:`macro rule` that belongs to a
resolved :t:`declarative macro`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 799-803
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_r6i1ykrhb49j`
   The :t:`[macro matcher]s` of all :t:`[macro rule]s` that belong to a resolved
   :t:`macro` are tried against the :s:`TokenTree` of the :t:`macro invocation`,
   in declarative order. In the event of a static error, no further attempts at
   selecting a subsequent :t:`macro matcher` are made.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 805-812
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_3qzes4lr8yuv`
   The :t:`macro match` of a candidate :t:`macro matcher` is tried against
   the :s:`TokenTree` of the :t:`macro invocation` by matching individual
   :t:`[token]s`, in left-to-right order. Matching does not employ lookahead.
   It is a static error if matching a candidate :t:`macro matcher` is ambiguous.
   Matching does not employ backtracking. It is a static error if matching a
   candidate :t:`macro matcher` fails while parsing into a :t:`metavariable` and
   having consumed at least one :t:`token` while parsing the :t:`metavariable`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 824-827
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_k6a24sbon5v9`
:t:`Token matching` is the process of consuming a :s:`TokenTree` in an attempt
to fully satisfy a :t:`macro match` of a selected :t:`macro matcher` that
belongs to a resolved :t:`declarative macro`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 832-834
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_g1rml9tavh8v`
The outer :s:`[Delimiter]s` of a :t:`macro matcher` match any outer
:s:`[Delimiter]s` in the :t:`macro invocation`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 879-880
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_xbuixjt9pum6`
  :t:`Fragment specifier` **tt** requires a :s:`TokenTree`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 892-895
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_ghqjk6xj85ng`
Repetition in a :t:`macro matcher` is matched based on how many times the
:t:`pattern` appears consecutively optionally separated by a :t:`separator` in
the :s:`TokenTree` of the :t:`macro invocation`, as follows:
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 934-936
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_rb1tu4e7dpma`
Any other :t:`token` in a :t:`macro matcher` is matched literally against the
:s:`TokenTree` of the :t:`macro invocation`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 938-940
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_c76sdvos5xeo`
It is a static error if the :s:`TokenTree` of the :t:`macro invocation` contains
leftover :t:`[token]s` after :t:`macro matching`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 956-959
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_iw7322ycvhkc`
Every :t:`metavariable indication` found in the :s:`DelimitedTokenTree` of the
:t:`macro transcriber` that belongs to a matched :t:`macro rule` is replaced by
the matched sequence of :t:`[token]s` of the :t:`metavariable`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 965-968
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_ihcwl6taptas`
Every :t:`macro repetition in transcription` found in the
:s:`DelimitedTokenTree` of the :t:`macro transcriber` shall be transcribed by
repeatedly transcribing the :t:`[token]s` inside of it.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 1084-1088
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_dz2mvodl818d`
  :t:`Definition site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site. :t:`[Identifier]s` with :t:`definition site hygiene` cannot reference
  the environment of the :s:`MacroRulesDeclaration`, cannot be referenced by the
  environment of a :s:`MacroInvocation`, and are considered :t:`hygienic`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 1090-1094
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_puqhytfzfsg6`
  :t:`Call site hygiene`, which resolves to a :s:`MacroInvocation` site.
  :t:`[Identifier]s` with :t:`call site hygiene` can reference the environment
  of the :s:`MacroRulesDeclaration`, can reference the environment of the
  :s:`MacroInvocation`, and are considered :t:`unhygienic`.
```

### Macro processing rule
- File: `/home/pete.levasseur/project/fls/src/macros.rst`
- Lines: 1096-1100
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_uyvnq88y9gk3`
  :t:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
  :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
  considered :dt:`partially hygienic`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 65-69
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_TUanRT7WU14E`
It is a static error when :t:`[lexical element]s` match multiple alternations
of a :t:`pattern-without-range`, except for when the :t:`pattern` is ``&mut``
:s:`Identifier`. Such a :t:`pattern` is interpreted as a :t:`reference pattern`
with :t:`keyword` ``mut`` containing an :t:`identifier pattern`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 590-594
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_30u9ij164ww3`
  If the :t:`reference pattern` appears with :t:`keyword` ``mut``,
  then the :t:`type` is ``&mut pattern_without_range_type``,
  where ``pattern_without_range_type`` is the :t:`type` of the
  :s:`PatternWithoutRange`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 596-600
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_d1kc73hpncpo`
  If the :t:`reference pattern` appears without :t:`keyword`
  ``mut``, then the :t:`type` is ``& pattern_without_range_type``,
  where ``pattern_without_range_type`` is the :t:`type` of the
  :s:`PatternWithoutRange`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 704-707
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_r78zzw7yyg34`
  A :t:`slice`, where the :s:`PatternList` consists of a single
  :t:`rest pattern`, or a single possibly nested :t:`identifier pattern` whose
  last :t:`bound pattern` is a :t:`rest pattern`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 897-899
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_f0u0j4q90lpl`
  A :s:`RecordStructRestPattern` is allowed even if all :t:`[field]s` of the
  :t:`deconstructee` have been matched.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 915-917
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_brhtaaxt1s3s`
  A :s:`RecordStructRestPattern` is allowed even if all :t:`[field]s` of the
  :t:`deconstructee` have been matched.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 923-925
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_pfz8xlwezbw1`
  The :s:`RecordStructPatternContent` of the :t:`record struct
  pattern` shall contain exactly one :s:`FieldDeconstructor`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 927-929
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_XFKBJZe6k1o2`
  The :t:`record struct pattern` shall not contain a
  :s:`RecordStructRestPattern`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 944-947
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_9y1gbv47z23o`
If the :t:`deconstructee` of a :t:`record struct pattern` is a
:t:`unit enum variant` or a :t:`unit struct`, then the
:t:`record struct pattern` shall have at most one :s:`RecordStructRestPattern`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1045-1046
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_5lo1hs8wzz0t`
  If the :t:`tuple struct pattern` has a :s:`RecordStructRestPattern`, then
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1048-1051
- Context: rubric `Legality Rules`, list item `yes`

```rst
  * :dp:`fls_gwuc2xffosu`
    If the :t:`subpattern` precedes the :s:`RecordStructRestPattern`, then its
    position is the position within the :s:`PatternList` in left-to-right order,
    starting from zero.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1053-1056
- Context: rubric `Legality Rules`, list item `yes`

```rst
  * :dp:`fls_w369n8lmwr7g`
    If the :t:`subpattern` succeeds the :s:`RecordStructRestPattern`, then its
    position is the position within the :s:`PatternList` list in right-to-left
    order, starting from the :t:`arity` of the :t:`deconstructee` minus one.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1076-1078
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_qgilaqy5zx7q`
A :s:`RecordStructRestPattern` is allowed even if all :t:`[field]s` of the
:t:`deconstructee` have been matched.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1131-1132
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_KmIHFxlBYelZ`
  If the :t:`tuple pattern` has a :s:`RestPattern`, then
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1134-1137
- Context: rubric `Legality Rules`, list item `yes`

```rst
  * :dp:`fls_5bXqIaKiFcLg`
    If the :t:`subpattern` precedes the :s:`RestPattern`, then its
    position is the position within the :s:`PatternList` in left-to-right order,
    starting from zero.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1139-1142
- Context: rubric `Legality Rules`, list item `yes`

```rst
  * :dp:`fls_soHCAVfGlv5f`
    If the :t:`subpattern` succeeds the :s:`RestPattern`, then its
    position is the position within the :s:`PatternList` list in right-to-left
    order, starting from the :t:`arity` of the :t:`tuple type` minus one.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/patterns.rst`
- Lines: 1162-1164
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_cC6ohNuiltfL`
A :s:`RestPattern` is allowed even if all :t:`[tuple field]s` of the
:t:`tuple type` have been matched.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/program-structure-and-compilation.rst`
- Lines: 79-80
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_qypjjpcf8uwq`
An :t:`inline module` is a :t:`module` with an :s:`InlineModuleSpecification`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/program-structure-and-compilation.rst`
- Lines: 82-83
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_cavwpr1ybk37`
An :t:`outline module` is a :t:`module` with an :s:`OutlineModuleSpecification`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/statements.rst`
- Lines: 78-81
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_1s1UikGU5YQb`
If a :t:`let statement` has a :t:`block expression`, then the :s:`Expression` of
the :s:`LetInitializer` shall not be a :s:`LazyBooleanExpression` or end with
token ``}``.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 591-594
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 648-650
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_g5qle7xzaoif`
The :t:`name` of an :t:`enum variant` shall be unique within the related
:s:`EnumDeclaration`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 655-657
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_hp5frc752dam`
A :t:`discriminant initializer` shall be specified only when all :t:`[enum
variant]s` appear without an :s:`EnumVariantKind`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 682-684
- Context: rubric `Legality Rules`, list item `yes`

```rst
#. :dp:`fls_t36rk3wikq28`
   Otherwise, if the :t:`enum variant` is the first :t:`enum variant` in the
   :s:`EnumVariantList`, then the :t:`value` is zero.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 767-769
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_r885av95eivp`
The :t:`name` of a :t:`record struct field` shall be unique within the
related :s:`RecordStructDeclaration`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 771-774
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_auurdv1zvzb`
If the :t:`type` of a :t:`record struct field` is a :t:`dynamically sized type`,
then the :t:`record struct field` shall be the last :t:`record struct field` in
the :s:`RecordStructFieldList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 776-779
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_vce7w0904du5`
If the :t:`type` of a :t:`tuple struct field` is a :t:`dynamically sized type`,
then the :t:`tuple struct field` shall be the last :t:`tuple struct field` in
the :s:`TupleStructFieldList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 821-823
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_1caus8ybmfli`
The :t:`name` of a :t:`union field` shall be unique within the related
:s:`RecordStructDeclaration`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 986-987
- Context: rubric `Legality Rules`, list item `yes`

```rst
* :dp:`fls_8gpvNJfVlyaD`
  If the :t:`function pointer type` specifies a :s:`ReturnTypeWithoutBounds`, then the :t:`return type` is the specified :s:`ReturnTypeWithoutBounds`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 1371-1373
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_rosdkeck5ax2`
A :t:`type alias` shall not have a :s:`TypeBoundList` unless it is an
:t:`associated item`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 1563-1568
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_qkkc8x2oghst`
:t:`Type representation` may be specified using :t:`attribute` :c:`[repr]` and
modified further using :t:`attribute` :c:`[repr]`'s :s:`Alignment`
:t:`[representation modifier]s`. A :t:`representation modifier` shall apply only
to a :t:`struct type` or a :t:`union type` subject to :t:`C representation` or
:t:`default representation`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 2937-2940
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_vujl3fblz6x2`
A :t:`higher-ranked trait bound` is a :t:`bound` that specifies an infinite
list of :t:`[bound]s` for all possible :t:`[lifetime]s` specified by the
:s:`ForGenericParameterList`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/types-and-traits.rst`
- Lines: 2942-2944
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_AzuZmR9DXSQh`
An :t:`opt-out trait bound` is a :t:`trait bound` with :s:`Punctuation` ``?``
that nullifies an implicitly added :t:`trait bound`.
```

### Legality rule referencing syntax production
- File: `/home/pete.levasseur/project/fls/src/values.rst`
- Lines: 162-163
- Context: rubric `Legality Rules`, list item `no`

```rst
:dp:`fls_WRpcVF1fLEpr`
A :t:`static` shall only be subject to an :s:`ItemSafety` if it is an :t:`external static` in an :t:`unsafe external block`.
```
