# Context-dependent glossary definitions

The following definition paragraphs include contextual phrasing that may not
read clearly when copied into the generated glossary.

## scoping_construct

Doc: entities-and-resolution.rst
Section: Scope Hierarchy

Definition snippet:

```rst
:dp:`fls_ns4eog3od4kw` A :dt:`scoping construct` is a :t:`construct` that introduces :t:`[scope]s` into the :t:`scope hierarchy`. The following :t:`[construct]s` are :t:`[scoping construct]s`:  * :dp:`fls_kqmykyzdb1k6`   :t:`[Block expression]s`,  * :dp:`fls_g86d5v14sxxv`   :t:`[Closure expression]s`,  * :dp:`fls_ldwencd8zp9a`   :t:`[Declarative macro]s`,  * :dp:`fls_jz7hgkvocc9r`   :t:`Enum type` :t:`[declaration]s`,  * :dp:`fls_p4g8sxba7at9`   :t:`Function` :t:`[declaration]s`,  * :dp:`fls_d1cp5pt5wn0z`   :t:`Function pointer type` :t:`specifications <type specification>`,  * :dp:`fls_ibmm8y748z4`   :t:`[If let expression]s`,  * :dp:`fls_39011vsy2vxx`   :t:`Implementation` :t:`[declaration]s`,  * :dp:`fls_m81hyd154yun`   :t:`[Let statement]s`,  * :dp:`fls_fvgzmsaox4z3`   :t:`[Loop expression]s`,  * :dp:`fls_rj8uld11o1br`   :t:`[Match arm]s`,  * :dp:`fls_hyp4dnpqe620`   :t:`Module` :t:`[declaration]s`,  * :dp:`fls_zgied4qysk2a`   :t:`Struct type` :t:`[declaration]s`,  * :dp:`fls_cn6dzmrxdp1w`   :t:`[Trait bound]s`,  * :dp:`fls_9n7m0tv7w2np`   :t:`Trait` :t:`[declaration]s`,  * :dp:`fls_sj2ivbf2l2dp`   :t:`Type alias` :t:`[declaration]s`,  * :dp:`fls_cejfio3ddy0j`   :t:`[Type bound predicate]s`,  * :dp:`fls_j3rot386teec`   :t:`Union type` :t:`[declaration]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## macro_namespace

Doc: entities-and-resolution.rst
Section: Namespaces

Definition snippet:

```rst
:dp:`fls_crwfafrmydr7` A :dt:`macro namespace` contains the :t:`[name]s` of the following kinds of :t:`entities <entity>`:  * :dp:`fls_t8fcpm8ldv1y`   :t:`[Attribute macro]s`,  * :dp:`fls_7pkex797rkeu`   :t:`[Built-in attribute]s`,  * :dp:`fls_v32f2evgqt5q`   :t:`[Declarative macro]s`,  * :dp:`fls_f6yrzwu6yi30`   :t:`[Derive macro]s`,  * :dp:`fls_nk0swexy2ztm`   :t:`[Function-like macro]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## type_namespace

Doc: entities-and-resolution.rst
Section: Namespaces

Definition snippet:

```rst
:dp:`fls_ckptn88o6lla` A :dt:`type namespace` contains the :t:`[name]s` of the following kinds of :t:`entities <entity>`:  * :dp:`fls_3ma5v1fop98p`   :t:`[Associated type]s`,  * :dp:`fls_nj7sep7ht7lg`   :c:`bool` :t:`[type]s`,  * :dp:`fls_g8h6t5x6yprm`   :t:`[Enum type]s`,  * :dp:`fls_2l1o7vqfr4m7`   :t:`[Enum variant]s`,  * :dp:`fls_6q8rjv1jmu84`   :t:`[Module]s`,  * :dp:`fls_lx2tx1jt8t3a`   :t:`[Numeric type]s`,  * :dp:`fls_mo00df28t7c1`   :c:`Self`,  * :dp:`fls_8o3izim4zf8t`   :t:`[Struct type]s`,  * :dp:`fls_fweohszgbuj4`   :t:`[Textual type]s`,  * :dp:`fls_ry02dzisxz3h`   :t:`[Trait]s`,  * :dp:`fls_dcz1bxjjfsq`   :t:`[Type alias]es`,  * :dp:`fls_wt9kgsi6n6ep`   :t:`[Type parameter]s`,  * :dp:`fls_w29t5njbe46s`   :t:`[Union type]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## value_namespace

Doc: entities-and-resolution.rst
Section: Namespaces

Definition snippet:

```rst
:dp:`fls_u1533bngb0yv` A :dt:`value namespace` contains the :t:`[name]s` of the following kinds of :t:`entities <entity>`:  * :dp:`fls_e8v4g45v5ry2`   :t:`[Associated constant]s`,  * :dp:`fls_pq8bzav84q3z`   :t:`[Associated function]s`,  * :dp:`fls_ttr6v8ca4av0`   :t:`[Binding]s`,  * :dp:`fls_aivi97hhfxy2`   :t:`[Constant]s`,  * :dp:`fls_pie4ltdtzkl3`   :t:`[Constant parameter]s`,  * :dp:`fls_qmf7lk6h96sv`   :t:`Enum variant` constructors,  * :dp:`fls_ufp3btk8pet5`   :t:`[Function]s`,  * :dp:`fls_t3bnpkfazw4z`   :c:`Self` constructors,  * :dp:`fls_y0shlli54n5y`   :t:`[Static]s`,  * :dp:`fls_tghgxcju5u2t`   :t:`Struct` constructors.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## language_prelude

Doc: entities-and-resolution.rst
Section: Preludes

Definition snippet:

```rst
:dp:`fls_pbc7ktlu0pl` The :dt:`language prelude` is a :t:`prelude` that brings :t:`in scope` of every :t:`module` the following :t:`entities <entity>`:  * :dp:`fls_frjv68kqqxfh`   Boolean type :c:`bool`.  * :dp:`fls_rf6a2ae3y7vu`   :t:`[Built-in attribute]s`.  * :dp:`fls_sxnnkzmuvexa`   :t:`[Floating-point type]s` :c:`f32` and :c:`f64`.  * :dp:`fls_qsyorqjkdh2t`   :t:`[Integer type]s` :c:`i8`, :c:`i16`, :c:`i32`, :c:`i64`, :c:`i128`,   :c:`isize`, :c:`u8`, :c:`u16`, :c:`u32`, :c:`u64`, :c:`u128`, and :c:`usize`.  * :dp:`fls_aolj6abvp9sa`   :t:`[Textual type]s` :c:`char` and :c:`str`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## method_resolution_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Method Resolution

Definition snippet:

```rst
:dp:`fls_bb4cbmvui8fk` :dt:`Method resolution implementation candidate lookup` for a :t:`receiver type` proceeds as follows:  #. :dp:`fls_5wny1yxbyuz0`    Perform :t:`method resolution inherent implementation candidate lookup` for    the :t:`receiver type`.  #. :dp:`fls_gsc8pt4tlsqv`    Perform :t:`method resolution trait implementation candidate lookup` for the    :t:`receiver type`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## method_resolution_inherent_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Method Resolution

Definition snippet:

```rst
:dp:`fls_tfglce1wuq5q` :dt:`Method resolution inherent implementation candidate lookup` for a :t:`receiver type` proceeds as follows:  #. :dp:`fls_64bfcn9okeve`    Construct the :t:`dereference type chain` for the :t:`receiver type`.  #. :dp:`fls_om90v9re8b2l`    For each :t:`dereference type` in the :t:`dereference type chain`     #. :dp:`fls_bsf4hy9x7c2e`       For each :t:`inherent implementation` in the set of       :t:`[inherent implementation]s` of the :t:`dereference type` where the       :t:`implementing type` :t:`unifies <unify>` with the       :t:`dereference type`        #. :dp:`fls_cnn5hkf1z5q4`          Try to locate a :t:`candidate method` in the :t:`inherent          implementation`, where the :t:`type` of the :t:`self parameter`          :t:`unifies <unify>` with the :t:`receiver type`.        #. :dp:`fls_j9ho6xc2fj0w`          If such a :t:`candidate method` exists, then the          :t:`method call expression` resolves to that :t:`candidate method` and          :t:`method resolution` stops.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## method_resolution_trait_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Method Resolution

Definition snippet:

```rst
:dp:`fls_1y94elgpg0uk` :dt:`Method resolution trait implementation candidate lookup` for a :t:`receiver type` proceeds as follows:  #. :dp:`fls_npsdxrtcslcf`    Construct the :t:`dereference type chain` for the :t:`receiver type`.  #. :dp:`fls_yv5l823lwdsv`    For each :t:`dereference type` in the :t:`dereference type chain`     #. :dp:`fls_ckdoyvbaybe0`       For each :t:`trait implementation` of the :t:`dereference type` where the       :t:`implemented trait` is :t:`in scope`        #. :dp:`fls_1azkiu20r0e4`          Try to locate a :t:`candidate method` in the          :t:`trait implementation`, where the :t:`type` of the          :t:`self parameter` :t:`unifies <unify>` with the :t:`receiver type`.        #. :dp:`fls_ose5m4bhkg57`          If such a :t:`candidate method` exists, then the          :t:`method call expression` resolves to that :t:`candidate method` and          :t:`method resolution` stops.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## namespace_context

Doc: entities-and-resolution.rst
Section: Path Resolution

Definition snippet:

```rst
:dp:`fls_ec4wo8odusqp` A :dt:`namespace context` is a set of :t:`[namespace]s` where the :t:`[name]s` of :t:`candidate selected entities <candidate selected entity>` reside.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## path_expression_resolution_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Path Expression Resolution

Definition snippet:

```rst
:dp:`fls_utfpnwlo0v99` :dt:`Path expression resolution implementation candidate lookup` for a :t:`path segment` and a :t:`trait` or :t:`type` proceeds as follows:  #. :dp:`fls_1p8ocf1w5bp4`    Perform    :t:`path expression resolution inherent implementation candidate lookup` for    the :t:`path segment` and the :t:`trait` or :t:`type`.  #. :dp:`fls_qb5yo7j5gnvf`    Perform    :t:`path expression resolution trait implementation candidate lookup` for    the :t:`path segment` and the :t:`trait` or :t:`type`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## path_expression_resolution_inherent_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Path Expression Resolution

Definition snippet:

```rst
:dp:`fls_o1g0forw6xw` :dt:`Path expression resolution inherent implementation candidate lookup` for a :t:`path segment` and a :t:`trait` or :t:`type` proceeds as follows:  #. :dp:`fls_bcqe13q696zg`    For each :t:`inherent implementation` in the set of    :t:`[inherent implementation]s` of the :t:`trait` or :t:`type` where the    :t:`implementing type` :t:`unifies <unify>` with the :t:`trait` or :t:`type`     #. :dp:`fls_3sceutaqpqha`       Try to locate a visible :t:`constant` or a visible :t:`function` in the       :t:`inherent implementation` whose :t:`name` matches the characters of       the :t:`path segment`.     #. :dp:`fls_6q9cwqlvxmd1`       If such a :t:`constant` or :t:`function` exists, then the       :t:`path segment` resolves to that :t:`constant` or :t:`function` and       :t:`path expression resolution` stops.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## path_expression_resolution_trait_implementation_candidate_lookup

Doc: entities-and-resolution.rst
Section: Path Expression Resolution

Definition snippet:

```rst
:dp:`fls_qeym3vbi36iv` :dt:`Path expression resolution trait implementation candidate lookup` for a :t:`path segment` and a :t:`trait` or :t:`type` proceeds as follows:  #. :dp:`fls_8x0pqwpm80sj`    For each :t:`trait implementation` of the :t:`trait` or :t:`type` where the    :t:`implemented trait` is :t:`in scope`     #. :dp:`fls_pp09gmrnasjp`       Try to locate a visible :t:`constant` or a visible :t:`function` in the       :t:`trait implementation` whose :t:`name` matches the characters of the       :t:`path segment`.     #. :dp:`fls_q0jt6n2j1hsx`       If such a :t:`constant` or :t:`function` exists, then the       :t:`path segment` resolves to that :t:`constant` or :t:`function` and       :t:`path expression resolution` stops.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## fragment_specifier_restriction

Doc: macros.rst
Section: Metavariables

Definition snippet:

```rst
:dp:`fls_8o9mcV2KrKac` :t:`Fragment specifier` kinds impose the following :dt:`[fragment specifier restriction]s` on the :t:`[token]s` that follow them:  * :dp:`fls_PxR9vNHsaFnI`   ``expr`` and ``expr_2021`` shall only be followed by ``=>``, ``,``, or ``;``.  * :dp:`fls_ePyoTeJJ11N0`   ``pat`` shall only be followed by ``=>``, ``,``, ``=``, ``|``, ``if``, or   ``in``.  * :dp:`fls_0j7VOV4ewfeY`   ``path`` shall only be followed by ``=>``, ``,``, ``=``, ``|``, ``;``, ``:``,   ``>``, ``>>``, ``[``, ``{``, ``as``, ``where``, or a :t:`metavariable` with   the ``block`` :t:`fragment specifier` kind.  * :dp:`fls_80cOMpIMU2gx`   ``pat_param`` shall only be followed by ``=>``, ``,``, ``=``, ``|``, ``if``,   or ``in``.  * :dp:`fls_DFMRwsWI8e5z`   ``stmt`` shall only be followed by ``=>``, ``,``, or ``;``.  * :dp:`fls_BoIGgrFdyhwH`   ``ty`` shall only be followed by ``=>``, ``,``, ``=``, ``|``, ``;``, ``:``,   ``>``, ``>>``, ``[``, ``{``, ``as``, ``where``, or a :t:`metavariable` with   the ``block`` :t:`fragment specifier` kind.  * :dp:`fls_NBbygZwUxjFp`   ``vis`` shall only be followed by ``,``, an :t:`identifier` except for   ``priv``, any token that may begin a :s:`TypeSpecification`, or a   :t:`metavariable` with the ``ident``, ``ty`` or ``block``   :t:`fragment specifier` kind.  * :dp:`fls_lZ8F1zUJju33`   Any other kind may be followed by any token.
```

Context note: following, here
Reason: contains contextual phrasing that may require manual rewrite.

## specialized_cast

Doc: expressions.rst
Section: Type Cast Expressions

Definition snippet:

```rst
:dp:`fls_otaxe9okhdr1` A :t:`type cast expression` with the following characteristics performs a :dt:`specialized cast`:  * :dp:`fls_4s69s9pcvbn7`   An :t:`operand` of a :t:`numeric type` and a target :t:`numeric type` perform   a :t:`numeric cast`.  * :dp:`fls_le6bchl25ewz`   An :t:`operand` of an :t:`enum type` and a target :t:`integer type`   perform :t:`enum cast`. An :dt:`enum cast` converts the :t:`operand` to its   :t:`discriminant`, followed by a :t:`numeric cast`.  * :dp:`fls_pcromhosmnf0`   An operand of :t:`type` :c:`bool` or :t:`type` :c:`char` and a   target :t:`integer type` perform :t:`primitive-to-integer cast`. A   :dt:`primitive-to-integer cast`    * :dp:`fls_al9f1t7vlsxi`     Converts an :t:`operand` of :t:`type` :c:`bool` with :t:`value` ``false``     to zero.    * :dp:`fls_jea17f39fmsg`     Converts an :t:`operand` of :t:`type` :c:`bool` with :t:`value` ``true``     to one.    * :dp:`fls_eb00s8fxlvjb`     Convert an :t:`operand` of :t:`type` :c:`char` to the :t:`value` of the     corresponding :t:`code point`, followed by a :t:`numeric cast`.  * :dp:`fls_qk5trk8wkvxb`   An :t:`operand` of :t:`type` :c:`u8` and a target :t:`type` :c:`char` performs   :t:`u8-to-char cast`. A :dt:`u8-to-char cast` converts an :t:`operand` of   :t:`type` :c:`u8` to the :t:`value` of the corresponding :t:`code point`.  * :dp:`fls_t16yzaxro5ew`   An :t:`operand` of :t:`type` ``*const T`` or ``*mut T`` and a   :t:`target type` ``*const V`` or ``*mut V`` where ``V`` implements the   :std:`core::marker::Sized` :t:`trait` performs pointer-to-pointer cast.  * :dp:`fls_i4zsbbmfa2fl`   An :t:`operand` of :t:`type` ``*const T`` or ``*mut T`` where ``T`` implements   the :std:`core::marker::Sized` :t:`trait` and a target :t:`integer type`   perform :t:`pointer-to-address cast`. A :dt:`pointer-to-address cast` produces   an integer that represents the machine address of the referenced memory. If   the :t:`integer type` is smaller than the :t:`type` of the :t:`operand`, the   address is truncated.  * :dp:`fls_59mpteeczzo`   An :t:`operand` of :t:`integer type` and :t:`target type` ``*const V`` or   ``*mut V`` where ``V`` implements the :std:`core::marker::Sized` :t:`trait`   perform :t:`address-to-pointer cast`. An :dt:`address-to-pointer cast`   produces a :t:`pointer` that interprets the integer as a machine address.  * :dp:`fls_8ccwlliqw9jx`   An :t:`operand` of :t:`type` ``&mut [T; N]`` and a :t:`target type`   ``*const T`` perform array-to-pointer cast.  * :dp:`fls_i8txki3htx92`   An :t:`operand` of a :t:`function item type` and a :t:`target type`   ``*const V`` or ``*mut V`` where ``V`` implements the   :std:`core::marker::Sized` :t:`trait` perform function-item-to-pointer cast.  * :dp:`fls_6hbkvbb1c8aj`   An :t:`operand` of a :t:`function item type` and a target :t:`integer type`   perform function-to-address cast.  * :dp:`fls_133j6xw8k4qe`   An :t:`operand` of a :t:`function pointer type` and a :t:`target type`   ``*const V`` or ``*mut V`` where ``V`` implements the   :std:`core::marker::Sized` :t:`trait` perform   :dt:`function-pointer-to-pointer cast`.  * :dp:`fls_bhw2j9wjpf2x`   An :t:`operand` of a :t:`function pointer type` and a target :t:`integer type`   perform :t:`function-pointer-to-address cast`. A   :dt:`function-pointer-to-address cast` produces an integer that represents the   machine address of the referenced :t:`function`. If the :t:`integer type` is   smaller than the size of the :t:`function pointer type`, the address is   truncated.
```

Context note: following, here
Reason: contains contextual phrasing that may require manual rewrite.

## whitespace_character

Doc: lexical-elements.rst
Section: Character Set

Definition snippet:

```rst
:dp:`fls_pvslhm3chtlb` A :dt:`whitespace character` is one of the following characters:  * :dp:`fls_a5ec9cpn4sc8`   0x09 (horizontal tabulation)  * :dp:`fls_dgyrj49y3c7c`   0x0A (new line)  * :dp:`fls_5ocmngyur7by`   0x0B (vertical tabulation)  * :dp:`fls_1aj0rgi9kpib`   0x0C (form feed)  * :dp:`fls_bfzdxsbq2c2q`   0x0D (carriage return)  * :dp:`fls_vw0kq2y1o63m`   0x20 (space)  * :dp:`fls_ao296bmamwzh`   0x85 (next line)  * :dp:`fls_6kymhq7embdh`   0x200E (left-to-right mark)  * :dp:`fls_8mxmrxvhn3by`   0x200F (right-to-left mark)  * :dp:`fls_bc6D1ATvmJJr`   0x2028 (line separator)  * :dp:`fls_zfs15iel08y0`   0x2029 (paragraph separator)
```

Context note: following, next
Reason: contains contextual phrasing that may require manual rewrite.

## simple_punctuator

Doc: lexical-elements.rst
Section: Lexical Elements, Separators, and Punctuation

Definition snippet:

```rst
:dp:`fls_8fv63w6f4udl` A :dt:`simple punctuator` is one of the following special characters:  .. syntax::     $$+$$    $$-$$    $$*$$    $$/$$    $$%$$    $$^$$    $$!$$    $$&$$    $$|$$    $$=$$    $$>$$    $$<$$    $$@$$    $$_$$    $$.$$    $$,$$    $$;$$    $$:$$    $$#$$    $$$$$    $$?$$    $${$$    $$}$$    $$[$$    $$]$$    $$($$    $$)$$
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## compound_punctuator

Doc: lexical-elements.rst
Section: Lexical Elements, Separators, and Punctuation

Definition snippet:

```rst
:dp:`fls_es0tz1q9cmoo` A :dt:`compound punctuator` is one of the following two or more adjacent special characters:  .. syntax::     $$&&$$    $$||$$    $$<<$$    $$>>$$    $$+=$$    $$-=$$    $$*=$$    $$/=$$    $$%=$$    $$^=$$    $$&=$$    $$|=$$    $$<<=$$    $$>>=$$    $$==$$    $$!=$$    $$>=$$    $$<=$$    $$..$$    $$...$$    $$..=$$    $$::$$    $$->$$    $$=>$$
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## flexible_compound_punctuator

Doc: lexical-elements.rst
Section: Lexical Elements, Separators, and Punctuation

Definition snippet:

```rst
:dp:`fls_vm86olkeecer` The following :t:`[compound punctuator]s` are :dt:`[flexible compound punctuator]s`.  .. syntax::     $$&&$$    $$||$$    $$<<$$    $$>>$$
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## base_address

Doc: values.rst
Section: Values

Definition snippet:

```rst
:dp:`fls_kaomYy0Ml4Nh` The :dt:`base address` of an :t:`allocated object` is the memory address where the object is stored.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## code_generation_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_bxucstrfcco8` The following :t:`[built-in attribute]s` are :dt:`[code generation attribute]s`:  * :dp:`fls_wle815gb9ai2`   :t:`Attribute` :c:`cold`.  * :dp:`fls_tvn08dtuilue`   :t:`Attribute` :c:`inline`.  * :dp:`fls_eOJS3mxa9xgu`   :t:`Attribute` :c:`naked`.  * :dp:`fls_q4c023zdsfgn`   :t:`Attribute` :c:`no_builtins`.  * :dp:`fls_xtu3p0kzwn7b`   :t:`Attribute` :c:`target_feature`.  * :dp:`fls_gxxbf6eag3et`   :t:`Attribute` :c:`track_caller`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## conditional_compilation_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_87o6n9et9jio` The following :t:`[built-in attribute]s` are :dt:`[conditional compilation attribute]s`:  * :dp:`fls_ui0i3rpt5v5u`   :t:`Attribute` :c:`cfg`.  * :dp:`fls_6utorag4adlv`   :t:`Attribute` :c:`cfg_attr`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## derivation_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_d8spdkjzp496` The following :t:`[built-in attribute]s` are :dt:`[derivation attribute]s`:  * :dp:`fls_vidbcv25dyud`   :t:`Attribute` :c:`automatically_derived`.  * :dp:`fls_d0298bmlyuu4`   :t:`Attribute` :c:`derive`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## diagnostics_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_dtb3t5ht5ngf` The following :t:`[built-in attribute]s` are :dt:`[diagnostics attribute]s`:  * :dp:`fls_c5n4gzgs79vv`   :t:`Attribute` ``allow``.  * :dp:`fls_xheohvupr8kb`   :t:`Attribute` ``deny``.  * :dp:`fls_s5z2q5pl14p4`   :t:`Attribute` ``deprecated``.  * :dp:`fls_NrTL2FruARAv`   :t:`Attribute` ``expect``.  * :dp:`fls_5ko0q9jnxv5a`   :t:`Attribute` ``forbid``.  * :dp:`fls_rgjf5ibhurda`   :t:`Attribute` ``must_use``.  * :dp:`fls_4d2ArC50kNWL`   :t:`Attribute` ``unsafe``.  * :dp:`fls_29y8icoou1gx`   :t:`Attribute` ``warn``.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## documentation_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_3fxhz0olhbcy` The following :t:`[built-in attribute]s` are :dt:`[documentation attribute]s`:  * :dp:`fls_oexj0952o05u`   :t:`Attribute` :c:`doc`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## foreign_function_interface_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_q579e97n1m8j` The following :t:`[built-in attribute]s` are :dt:`[foreign function interface attribute]s`:  * :dp:`fls_sn43rofpq6ld`   :t:`Attribute` :c:`crate_name`.  * :dp:`fls_56d70gkmin4p`   :t:`Attribute` :c:`crate_type`.  * :dp:`fls_mgb1xipm0qwo`   :t:`Attribute` :c:`export_name`.  * :dp:`fls_rmhlssasdtkj`   :t:`Attribute` :c:`link`.  * :dp:`fls_josaywt6g3rq`   :t:`Attribute` :c:`link_name`.  * :dp:`fls_qk4vkn42c2jh`   :t:`Attribute` :c:`link_section`.  * :dp:`fls_f21azsygoovw`   :t:`Attribute` :c:`no_link`.  * :dp:`fls_4d31lwzblg91`   :t:`Attribute` :c:`no_main`.  * :dp:`fls_muucfla1s8yn`   :t:`Attribute` :c:`no_mangle`.  * :dp:`fls_wbdtpntjr95w`   :t:`Attribute` :c:`repr`.  * :dp:`fls_lglwcbsvi9yj`   :t:`Attribute` :c:`used`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## limits_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_1gyg8hfb13n7` The following :t:`[built-in attribute]s` are :dt:`[limits attribute]s`:  * :dp:`fls_6005g57evfbp`   :t:`Attribute` :c:`recursion_limit`.  * :dp:`fls_3y4o8kq58dt8`   :t:`Attribute` :c:`type_length_limit`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## macro_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_vsix3pqf519x` The following :t:`[built-in attribute]s` are :dt:`[macro attribute]s`:  * :dp:`fls_c8uqw8p0qrh5`   :t:`Attribute` :c:`macro_export`.  * :dp:`fls_b3jobjxmqppy`   :t:`Attribute` :c:`macro_use`.  * :dp:`fls_xyhoxm30i7wn`   :t:`Attribute` :c:`proc_macro`.  * :dp:`fls_nowfw1ffhupd`   :t:`Attribute` :c:`proc_macro_attribute`.  * :dp:`fls_5i27houut1mu`   :t:`Attribute` :c:`proc_macro_derive`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## modules_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_1v9p4vr1nszn` The following :t:`[built-in attribute]s` are :dt:`[modules attribute]s`:  * :dp:`fls_jvkgtnulrqgh`   :t:`Attribute` :c:`path`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## prelude_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_k9p2xrs3dotn` The following :t:`[built-in attribute]s` are :dt:`[prelude attribute]s`:  * :dp:`fls_73n30xdcx8e`   :t:`Attribute` :c:`no_implicit_prelude`.  * :dp:`fls_e7zusnfka5dt`   :t:`Attribute` :c:`no_std`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## runtime_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_85ul6x76ew9` The following :t:`[built-in attribute]s` are :dt:`[runtime attribute]s`:  * :dp:`fls_xkhm1sht2ju5`   :t:`Attribute` :c:`global_allocator`.  * :dp:`fls_w9za4moh6gb3`   :t:`Attribute` :c:`panic_handler`.  * :dp:`fls_3vubhygy9jje`   :t:`Attribute` :c:`windows_subsystem`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## testing_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_mhaplbf40j02` The following :t:`[built-in attribute]s` are :dt:`[testing attribute]s`:  * :dp:`fls_23huzf3c4arx`   :t:`Attribute` :c:`ignore`.  * :dp:`fls_i63y9xnnwq2z`   :t:`Attribute` :c:`should_panic`.  * :dp:`fls_yic8ksed28no`   :t:`Attribute` :c:`test`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## type_attribute

Doc: attributes.rst
Section: Built-in Attributes

Definition snippet:

```rst
:dp:`fls_p1ugiol1e5v5` The following :t:`[built-in attribute]s` are :dt:`[type attribute]s`:  * :dp:`fls_7xh2iphiteam`   :t:`Attribute` :c:`non_exhaustive`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## coercion_site

Doc: types-and-traits.rst
Section: Type Coercion

Definition snippet:

```rst
:dp:`fls_j3kbaf43sgpj` The following :t:`[construct]s` constitute a :dt:`coercion site`:  * :dp:`fls_wxrugvlazy6v`   The :t:`[argument operand]s` of a :t:`call expression` or a   :t:`method call expression`.  * :dp:`fls_bhzmble1itog`   A :t:`constant` declaration.  * :dp:`fls_eu4bt3dw1b8c`   A :t:`field` of an :t:`abstract data type`.  * :dp:`fls_apstt4elv2k7`   A :t:`function` result.  * :dp:`fls_sp794uzfiofr`   A :t:`let statement` with an explicit :t:`type specification`.  * :dp:`fls_xfqny6bwzsu9`   A :t:`static` declaration.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## coercion_propagating_expression

Doc: types-and-traits.rst
Section: Type Coercion

Definition snippet:

```rst
:dp:`fls_u0e42y7nvn7e` The following :t:`[expression]s` constitute a :dt:`coercion-propagating expression`:  * :dp:`fls_p8hp5y506nam`   Each :t:`operand` of an :t:`array expression`.  * :dp:`fls_fjc9xev8rcu6`   The :t:`tail expression` of a :t:`block expression`.  * :dp:`fls_n1kh3z8d4q8y`   The :t:`operand` of a :t:`parenthesized expression`.  * :dp:`fls_dgoypa3hcxc0`   Each :t:`operand` of a :t:`tuple expression`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## least_upper_bound_coercion

Doc: types-and-traits.rst
Section: Type Coercion

Definition snippet:

```rst
:dp:`fls_da4w32rsrwxc` :dt:`Least upper bound coercion` is a :t:`multi-[type coercion]` that is used in the following scenarios:  * :dp:`fls_zi5311z1w7re`   To find the common :t:`type` of multiple :t:`if expression` branches.  * :dp:`fls_zst5pa29rpt`   To find the common :t:`type` of multiple :t:`if let expression` branches.  * :dp:`fls_agw1aej616vf`   To find the common :t:`type` for multiple :t:`match expression`   :t:`[match arm]s`.  * :dp:`fls_tnbga5dl4gz8`   To find the common :t:`type` of :t:`array expression` :t:`[operand]s`.  * :dp:`fls_yoreux8tn65x`   To find the :t:`return type` of a :t:`closure expression` with multiple   :t:`[return expression]s`.  * :dp:`fls_r11shke69uu6`   To find the :t:`return type` of a :t:`function` with multiple   :t:`[return expression]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## obligation

Doc: types-and-traits.rst
Section: Type Inference

Definition snippet:

```rst
:dp:`fls_6GrNr2izovRN` Performing :t:`type inference` may introduce a requirement that some :t:`type` must implement a :t:`trait`, or that a :t:`type` or :t:`lifetime` must outlive some other :t:`lifetime`. Such requirements are referred to as :dt:`[obligation]s` and are detailed in the inference rules below.
```

Context note: below
Reason: contains contextual phrasing that may require manual rewrite.

## input_lifetime

Doc: types-and-traits.rst
Section: Function Lifetime Elision

Definition snippet:

```rst
:dp:`fls_dpudys82dhdc` An :dt:`input lifetime` is one of the following :t:`[lifetime]s`:  * :dp:`fls_pjil71kk0r25`   Any :t:`lifetime` related to a :t:`function parameter`.  * :dp:`fls_1jnn9bsb71k7`   Any :t:`lifetime` related to a :t:`function pointer type parameter`.  * :dp:`fls_2p29p1fvi182`   Any :t:`lifetime` related to the :t:`[function parameter]s` of the   :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and :std:`core::ops::FnOnce`   :t:`[trait]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## output_lifetime

Doc: types-and-traits.rst
Section: Function Lifetime Elision

Definition snippet:

```rst
:dp:`fls_hsg9kfyvh35m` An :dt:`output lifetime` is one of the following :t:`[lifetime]s`:  * :dp:`fls_ofqy10q4a9jk`   Any :t:`lifetime` related to the :t:`return type` of a :t:`function`.  * :dp:`fls_yofbo96tjppf`   Any :t:`lifetime` related to the :t:`return type` of a   :t:`function pointer type`.  * :dp:`fls_vf7cxiir91ps`   Any :t:`lifetime` related to the :t:`[return type]s` of the   :std:`core::ops::Fn`, :std:`core::ops::FnMut`, and :std:`core::ops::FnOnce`   :t:`[trait]s`.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## extern_c_abi

Doc: ffi.rst
Section: ABI

Definition snippet:

```rst
:dp:`fls_9zitf1fvvfk8` The following :t:`[ABI]s` are supported:  * :dp:`fls_x7ct9k82fpgn`   ``extern "C"`` - The default :t:`ABI` of :t:`C` code, referred to as   :dt:`extern C ABI`.  * :dp:`fls_LfjvLXvI6TFL`   ``extern "C-unwind"`` - The same as ``extern "C"`` with the addition that   unwinding across FFI is permitted.  * :dp:`fls_a2d8ltpgtvn6`   ``extern "Rust"`` - The default :t:`ABI` of a Rust program, referred to as   :dt:`Rust ABI`.  * :dp:`fls_8m7pc3riokst`   ``extern "system"`` - The operating system-dependent :t:`ABI`.  * :dp:`fls_NQAzj5ai1La5`   ``extern "system-unwind"`` - The same as ``extern "system"`` with the   addition that unwinding across FFI is permitted.
```

Context note: following
Reason: contains contextual phrasing that may require manual rewrite.

## associated_type_projection

Doc: glossary-definitions.rst
Section: associated type projection

Definition snippet:

```rst
:dp:`fls_4moFUY6epk0v` An :dt:`associated type projection` is a :t:`qualified type path` of the form ``<type as trait>::associated_type``, where ``type`` is a :t:`type`, ``trait`` is a :t:`qualifying trait`, and ``associated type`` is an :t:`associated type`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## data_race

Doc: glossary-definitions.rst
Section: data race

Definition snippet:

```rst
:dp:`fls_v2s1b57e3r7n` A :dt:`data race` is a scenario where two or more threads access a shared memory location concurrently.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## destructuring_assignment

Doc: glossary-definitions.rst
Section: destructuring assignment

Definition snippet:

```rst
:dp:`fls_7jienn9uzn5k` A :dt:`destructuring assignment` is an :t:`assignment expression` where the :t:`assignee operand` is either an :t:`array expression`, a :t:`struct expression`, or a :t:`tuple expression`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## error_propagation_expression

Doc: glossary-definitions.rst
Section: error propagation expression

Definition snippet:

```rst
:dp:`fls_5kebgodxtqqt` An :dt:`error propagation expression` is an :t:`expression` that either evaluates to a :t:`value` of its :t:`operand` or returns a value to the next control flow boundary.
```

Context note: next
Reason: contains contextual phrasing that may require manual rewrite.

## external_function_item_type

Doc: glossary-definitions.rst
Section: external function item type

Definition snippet:

```rst
:dp:`fls_dwlovqly44dj` An :dt:`external function item type` is a :t:`function item type` where the related :t:`function` is an :t:`external function`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## function_signature

Doc: glossary-definitions.rst
Section: function signature

Definition snippet:

```rst
:dp:`fls_ndld48kg6o8d` A :dt:`function signature` is a unique identification of a :t:`function` that encompasses of its :t:`[function qualifier]s`, :t:`name`, :t:`[generic parameter]s`, :t:`[function parameter]s`, :t:`return type`, and :t:`where clause`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## fundamental

Doc: glossary-definitions.rst
Section: fundamental

Definition snippet:

```rst
:dp:`fls_e0dRD4NTE0UP` A :t:`trait` or :t:`type` is :dt:`fundamental` when its :t:`implementation coherence` rules are relaxed and the :t:`trait` or :t:`type` is always treated as if it was a :t:`local trait` or a :t:`local type`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## impl_trait_type

Doc: glossary-definitions.rst
Section: impl trait type

Definition snippet:

```rst
:dp:`fls_rdctgmnfncnd` An :dt:`impl trait type` is a :t:`type` that implements a :t:`trait`, where the :t:`type` is known at compile time.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## implementation_coherence

Doc: glossary-definitions.rst
Section: implementation coherence

Definition snippet:

```rst
:dp:`fls_hAmKcuYT9hHi` A :t:`trait implementation` exhibits :dt:`implementation coherence` when it is valid and does not overlap with another :t:`trait implementation`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## indexed_field_selector

Doc: glossary-definitions.rst
Section: indexed field selector

Definition snippet:

```rst
:dp:`fls_u6mh5yediub` An :dt:`indexed field selector` is a :t:`field selector` where the selected :t:`field` is indicated by an index.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## inherent_implementation

Doc: glossary-definitions.rst
Section: inherent implementation

Definition snippet:

```rst
:dp:`fls_6fpicw8ss4h3` An :dt:`inherent implementation` is an :t:`implementation` that adds direct functionality.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## named_field_selector

Doc: glossary-definitions.rst
Section: named field selector

Definition snippet:

```rst
:dp:`fls_cczpgxqdyh1e` A :dt:`named field selector` is a :t:`field selector` where the selected :t:`field` is indicated by an :t:`identifier`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## place

Doc: glossary-definitions.rst
Section: place

Definition snippet:

```rst
:dp:`fls_uCTiUBWHMPY9` A :dt:`place` is a location where a :t:`value` resides.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## scope

Doc: glossary-definitions.rst
Section: scope

Definition snippet:

```rst
:dp:`fls_fachaj550cq1` A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## simple_string_literal

Doc: glossary-definitions.rst
Section: simple string literal

Definition snippet:

```rst
:dp:`fls_p6qyyptz8w8w` A :dt:`simple string literal` is a :t:`string literal` where the characters are :t:`Unicode` characters.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## subtyping

Doc: glossary-definitions.rst
Section: subtyping

Definition snippet:

```rst
:dp:`fls_bo5xzjsdd3lj` :dt:`Subtyping` is a property of :t:`[type]s`, allowing one :t:`type` to be used where another :t:`type` is expected.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## trait_object_type

Doc: glossary-definitions.rst
Section: trait object type

Definition snippet:

```rst
:dp:`fls_lo2fzzdwxy1l` A :dt:`trait object type` is a :t:`type` that implements a :t:`trait`, where the :t:`type` is not known at compile time.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## transparent_representation

Doc: glossary-definitions.rst
Section: transparent representation

Definition snippet:

```rst
:dp:`fls_hb3e72rhzpnv` :dt:`Transparent representation` is a :t:`type representation` that applies only to an :t:`enum type` with a single :t:`enum variant` or a :t:`struct type` where the :t:`struct type` or :t:`enum variant` has a single :t:`field` of non-zero :t:`size` and any number of :t:`[field]s` of :t:`size` zero and :t:`alignment` one.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## trivial_predicate

Doc: glossary-definitions.rst
Section: trivial predicate

Definition snippet:

```rst
:dp:`fls_db5njwrjolhs` A :dt:`trivial predicate` is a :t:`where clause predicate` that does not use the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related :t:`construct`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## tuple_struct_call_expression

Doc: glossary-definitions.rst
Section: tuple struct call expression

Definition snippet:

```rst
:dp:`fls_DQaCUkskfXzk` A :dt:`tuple struct call expression` is a :t:`call expression` where the :t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## unsafe_function_item_type

Doc: glossary-definitions.rst
Section: unsafe function item type

Definition snippet:

```rst
:dp:`fls_r91tuwi55nu7` An :dt:`unsafe function item type` is a :t:`function item type` where the related :t:`function` is an :t:`unsafe function`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## use_import

Doc: glossary-definitions.rst
Section: use import

Definition snippet:

```rst
:dp:`fls_uccv9zthh5vt` A :dt:`use import` brings :t:`entities <entity>` :t:`in scope` within the :t:`block expression` of an :t:`expression-with-block` or :t:`module` where the :t:`use import` resides.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## where_clause

Doc: glossary-definitions.rst
Section: where clause

Definition snippet:

```rst
:dp:`fls_prljyrhontzn` A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on :t:`[lifetime parameter]s` and :t:`[type parameter]s`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

## where_clause_predicate

Doc: glossary-definitions.rst
Section: where clause predicate

Definition snippet:

```rst
:dp:`fls_0LACQVmZpDQF` A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a :t:`type bound predicate`.
```

Context note: here
Reason: contains contextual phrasing that may require manual rewrite.

