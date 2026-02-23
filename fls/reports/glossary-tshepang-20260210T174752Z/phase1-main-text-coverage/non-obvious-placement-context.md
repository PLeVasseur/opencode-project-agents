# Phase 1 non-obvious placement context

This companion report shows in-file context around each non-obvious term placement
called out in `non-obvious-placement-rationale.md`.

Source inputs:

- Placement map: `phase1-main-text-coverage/term-inventory.json`
- Phase branch content: `/home/pete.levasseur/project/fls-wt/step1/src/*.rst`

## Placement index

| Term | Chapter placement | Glossary line |
| --- | --- | --- |
| `code point` | `src/lexical-elements.rst:34` | `src/glossary.rst:1268` |
| `plane` | `src/lexical-elements.rst:38` | `src/glossary.rst:5043` |
| `constrain` | `src/generics.rst:129` | `src/glossary.rst:1472` |
| `implementation coherence` | `src/implementations.rst:139` | `src/glossary.rst:3103` |
| `fundamental` | `src/implementations.rst:167` | `src/glossary.rst:2618` |
| `unify` | `src/types-and-traits.rst:2047` | `src/glossary.rst:7309` |
| `unifiable type` (`unifiable types`) | `src/types-and-traits.rst:2058` | `src/glossary.rst:7293` |
| `structurally equal` | `src/types-and-traits.rst:2466` | `src/glossary.rst:6495` |
| `object safe` | `src/types-and-traits.rst:3147` | `src/glossary.rst:4652` |
| `terminated` | `src/expressions.rst:3955` | `src/glossary.rst:6675` |

## In-context excerpts

### `code point`, `plane` (`src/lexical-elements.rst`)

```text
00024| :dp:`fls_itcth8292ud6`
00025| The program text of a Rust program is written using the :t:`Unicode` character
00026| set.
00027| 
00028| :dp:`fls_m2v7k1p9t4qa`
00029| :dt:`Unicode` is the universal character encoding standard for written
00030| characters and text described in the Unicode Standard by the Unicode
00031| Consortium.
00032| 
00033| :dp:`fls_4h2v3pk7qz6n`
00034| In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
00035| character.
00036| 
00037| :dp:`fls_6n9y0qb5t2mc`
00038| In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
00039| :t:`[code point]s`.
00040| 
00041| .. rubric:: Syntax
00042| 
00043| :dp:`fls_vfx8byq5zo8t`
00044| A character is defined by this document for each cell in the coding space
00045| described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
00046| character to that cell.
```

### `constrain` (`src/generics.rst`)

```text
00120| :dp:`fls_jzfk9fspzqja`
00121| A :t:`generic struct` shall use all of its :t:`[type parameter]s` and
00122| :t:`[lifetime parameter]s` at least once in at least one of its :t:`[field]s`.
00123| 
00124| :dp:`fls_6j616ydf2mnh`
00125| A :t:`generic union` shall use all of its :t:`[type parameter]s` and
00126| :t:`[lifetime parameter]s` at least once in at least one of its :t:`[field]s`.
00127| 
00128| :dp:`fls_hyi2jnp38v1n`
00129| A :t:`generic parameter` is said to :dt:`constrain` an :t:`implementation` if the
00130| :t:`generic parameter` appears at least once in one of the following:
00131| 
00132| * :dp:`fls_sseo6u6pbcki`
00133|   As a :t:`binding argument` in the :t:`[trait bound]s` of a :t:`type` that
00134|   contains another :t:`generic parameter` that constrains the
00135|   :t:`implementation`, or
00136| 
00137| * :dp:`fls_62b59qvom3nm`
00138|   The :t:`implemented trait`, or
00139| 
00140| * :dp:`fls_oq76uff9gp0k`
00141|   The :t:`implementing type`.
00142| 
00143| :dp:`fls_ua3w16qo9o4`
00144| It is a static error if a :t:`constant parameter` or a :t:`type parameter` of
00145| an :t:`implementation` does not constrain the :t:`implementation`.
```

### `implementation coherence`, `fundamental` (`src/implementations.rst`)

```text
00133| Implementation Coherence
00134| ------------------------
00135| 
00136| .. rubric:: Legality Rules
00137| 
00138| :dp:`fls_fv1l4yjuut7p`
00139| A :t:`trait implementation` exhibits :dt:`implementation coherence` when it is
00140| valid and does not overlap with another :t:`trait implementation`.
00141| 
00142| :dp:`fls_swdusjwzgksx`
00143| Two :t:`[trait implementation]s` of the same :t:`implemented trait` overlap when
00144| the intersection of the :t:`[implementing type]s` is non-empty.
00145| 
00146| :dp:`fls_ir7hp941ky8t`
00147| Given :t:`trait implementation`
00148| ``impl<P1, P2, .., PN> Trait<T1, T2, .., TN> for T0``, the
00149| :t:`trait implementation` is considered valid when
00150| 
00151| * :dp:`fls_3tbm20k2ixol`
00152|   ``Trait`` is :t:`fundamental` or a :t:`local trait`, or
00153| 
00154| * :dp:`fls_lscc9ileg3gm`
00155|   All of
00156| 
00157|   * :dp:`fls_9klwbsh3vlxu`
00158|     At least one of :t:`[type]s` ``T0, T1, .., TN`` is :T:`fundamental` or a
00159|     :t:`local type`, and
00160| 
00161|   * :dp:`fls_9gmc1tcscq9v`
00162|     No :t:`type parameter` of ``P1, P2, .., PN`` that is not used in another
00163|     :t:`type` may appear in the :t:`non-[local type]s` and
00164|     :t:`non-[fundamental]` :t:`[type]s` of ``T0, T1, .., TN``.
00165| 
00166| :dp:`fls_UkQhjEWSJpDq`
00167| A :t:`trait` or :t:`type` is :dt:`fundamental` when its
00168| :t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type`
00169| is always treated as if it was a :t:`local trait` or a :t:`local type`.
00170| 
00171| :dp:`fls_fSybUG40hA5r`
00172| The following :t:`[type]s` are :t:`fundamental`:
```

### `unify`, `unifiable type` (`src/types-and-traits.rst`)

```text
02041| :dt:`Type unification` is the process by which :t:`type inference` propagates
02042| known :t:`[type]s` across the :t:`type inference root` and assigns concrete
02043| :t:`[type]s` to :t:`[type variable]s`, as well as a general mechanism to check
02044| for compatibility between two :t:`[type]s` during :t:`method resolution`.
02045| 
02046| :dp:`fls_67VZrx6dw68H`
02047| A :t:`type` is said to :dt:`unify` with another :t:`type` when the domains,
02048| ranges, and structures of both :t:`[type]s` are compatible according to the
02049| rules detailed below.
02050| 
02051| :dp:`fls_m4p8k1v7t2qa`
02052| Two :t:`[type]s` are :dt:`unifiable` when they :t:`unify`.
02053| 
02054| :dp:`fls_v7k2m9p1t4qa`
02055| A :dt:`unified type` is a :t:`type` produced by :t:`type unification`.
02056| 
02057| :dp:`fls_aie0tr62vhw5`
02058| Two types that :t:`unify` are said to be :dt:`[unifiable type]s`.
02059| 
02060| :dp:`fls_3U7Ue6Xzuv9M`
02061| :t:`Type unification` is a symmetric operation. If :t:`type` ``A`` unifies
02062| with :t:`type` ``B``, then ``B`` also unifies with ``A`` and such
02063| :t:`type unification` results in the same observable effects.
```

### `structurally equal` (`src/types-and-traits.rst`)

```text
02460| Structural Equality
02461| ~~~~~~~~~~~~~~~~~~~
02462| 
02463| .. rubric:: Legality Rules
02464| 
02465| :dp:`fls_uVTpA7gbLCYX`
02466| A :t:`type` is :dt:`structurally equal` when its :t:`[value]s` can be compared
02467| for equality by structure.
02468| 
02469| :dp:`fls_2DZAP6JJjJ9h`
02470| The following :t:`[type]s` are :t:`structurally equal`:
02471| 
02472| * :dp:`fls_emcNJzl2tHSA`
02473|   :c:`Bool`, :c:`char`, :t:`[function pointer type]s`, :t:`[integer type]s`,
02474|   :c:`str`,  and :t:`[raw pointer type]s`.
```

### `object safe` (`src/types-and-traits.rst`)

```text
03142| :dp:`fls_aG0l4OGm8sMG`
03143| :dt:`Object safety` is the process of determining whether a :t:`trait` can be used
03144| as a :t:`trait object type`.
03145| 
03146| :dp:`fls_lrdki56hpc3k`
03147| A :t:`trait` is :dt:`object safe` when:
03148| 
03149| * :dp:`fls_5wlltclogfkw`
03150|   Its :t:`[supertrait]s` are :t:`object safe`, and
03151| 
03152| * :dp:`fls_droy0w5gtqaw`
03153|   :std:`core::marker::Sized` is not a :t:`supertrait`, and
03154| 
03155| * :dp:`fls_46gd1q80c6bn`
03156|   It lacks :t:`[associated constant]s`, and
03157| 
03158| * :dp:`fls_kwo4cknx0yat`
03159|   Its :t:`[associated function]s` are :t:`object safe`, and
```

### `terminated` (`src/expressions.rst`)

```text
03952| .. rubric:: Dynamic Semantics
03953| 
03954| :dp:`fls_aw6qczl4zpko`
03955| A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
03956| longer evaluated.
03957| 
03958| .. _fls_onfyolkcbeh3:
03959| 
03960| For Loops
03961| ~~~~~~~~~
03962| 
03963| .. rubric:: Syntax
03964| 
03965| .. syntax::
03966| 
03967|    ForLoopExpression ::=
03968|        $$for$$ Pattern $$in$$ SubjectExpression LoopBody
```

## Notes

- `unifiable type` appears in source as list-role form: `:dt:`[unifiable type]s``.
- The contextual excerpts are snapshots from phase-1 branch content and are intended
  as reviewer evidence, not normative source files.
