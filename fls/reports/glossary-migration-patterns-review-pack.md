# Glossary migration pattern review pack

This file is a manual review aid generated from the sampled directives.

## 001 while loop expression (dual)
- File: src/expressions.rst:5352
- Commit: 2dfc847a722423358b918a6836760a3a11b5cb96
- Indent: 0

Current context (10 lines before/after):
```
  5342 | .. syntax::
  5343 | 
  5344 |    WhileLoopExpression ::=
  5345 |        $$while$$ IterationExpression LoopBody
  5346 | 
  5347 |    IterationExpression ::=
  5348 |        SubjectExpression
  5349 | 
  5350 | .. rubric:: Legality Rules
  5351 | 
  5352 | .. glossary-entry:: while loop expression
  5353 |    
  5354 |    :glossary:
  5355 |      :dp:`fls_fq0zyup4djyh`
  5356 |      A :dt:`while loop expression` is a :t:`loop expression` that continues to
  5357 |      evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
  5358 |      true.
  5359 |      
  5360 |      :dp:`fls_7htwpbmyq83u`
  5361 |      See :s:`WhileLoopExpression`.
  5362 |    :chapter:
  5363 |      :dp:`fls_ajby242tnu7c`
  5364 |      A :t:`while loop expression` is a :t:`loop expression` that continues to
  5365 |      evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
  5366 |      true.
  5367 | 
  5368 | .. glossary-entry:: iteration expression
  5369 |    
  5370 |    :glossary:
  5371 |      :dp:`fls_suz163n1x1xm`
  5372 |      An :dt:`iteration expression` is an :t:`expression` that provides the criterion
  5373 |      of a :t:`while loop expression`.
  5374 |      
  5375 |      :dp:`fls_jw5lj2hgjl8v`
  5376 |      See :s:`IterationExpression`.
  5377 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_fq0zyup4djyh`
     A :dt:`while loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
     true.
     
     :dp:`fls_7htwpbmyq83u`
     See :s:`WhileLoopExpression`.
```

Chapter block (current):
```
     :dp:`fls_ajby242tnu7c`
     A :t:`while loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
     true.

```

Static glossary entry:
```

:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.

:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_ajby242tnu7c`
A :t:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.

```

## 002 while let loop expression (dual)
- File: src/expressions.rst:5439
- Commit: 2dfc847a722423358b918a6836760a3a11b5cb96
- Indent: 0

Current context (10 lines before/after):
```
  5429 | 
  5430 | .. rubric:: Syntax
  5431 | 
  5432 | .. syntax::
  5433 | 
  5434 |    WhileLetLoopExpression ::=
  5435 |        $$while$$ $$let$$ Pattern $$=$$ SubjectLetExpression LoopBody
  5436 | 
  5437 | .. rubric:: Legality Rules
  5438 | 
  5439 | .. glossary-entry:: while let loop expression
  5440 |    
  5441 |    :glossary:
  5442 |      :dp:`fls_g35gn7n88acp`
  5443 |      A :dt:`while let loop expression` is a :t:`loop expression` that continues to
  5444 |      evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
  5445 |      :t:`value` that can be matched against its :t:`pattern`.
  5446 |      
  5447 |      :dp:`fls_q3jcb4nodqba`
  5448 |      See :s:`WhileLetLoopExpression`.
  5449 |    :chapter:
  5450 |      :dp:`fls_fmdlyp9r9zl7`
  5451 |      A :t:`while let loop expression` is a :t:`loop expression` that continues to
  5452 |      evaluate its :t:`loop body` as long as its :t:`subject let expression` yields
  5453 |      a :t:`value` that can be matched against its :t:`pattern`.
  5454 | 
  5455 | :dp:`fls_bC60ZSC9yUOI`
  5456 | The :t:`expected type` of the :t:`pattern` is the :t:`type` of the :t:`subject let expression`.
  5457 | 
  5458 | :dp:`fls_gTfSLePwHTES`
  5459 | The :t:`type` of a :t:`while let loop expression` is the :t:`unit type`.
  5460 | 
  5461 | :dp:`fls_pTq4LIGIoAtN`
  5462 | The :t:`value` of a :t:`while let loop expression` is the :t:`unit value`.
  5463 | 
  5464 | .. rubric:: Dynamic Semantics
```

Glossary block (current):
```
     :dp:`fls_g35gn7n88acp`
     A :dt:`while let loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
     :t:`value` that can be matched against its :t:`pattern`.
     
     :dp:`fls_q3jcb4nodqba`
     See :s:`WhileLetLoopExpression`.
```

Chapter block (current):
```
     :dp:`fls_fmdlyp9r9zl7`
     A :t:`while let loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`subject let expression` yields
     a :t:`value` that can be matched against its :t:`pattern`.

```

Static glossary entry:
```

:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.

:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_fmdlyp9r9zl7`
A :t:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields
a :t:`value` that can be matched against its :t:`pattern`.

```

## 003 visibility (dual)
- File: src/entities-and-resolution.rst:173
- Commit: 66a1099560705cbf09a1a0ce96f8eeb318085b76
- Indent: 0

Current context (10 lines before/after):
```
   163 |        $$pub$$ $$($$ $$in$$ SimplePath $$)$$
   164 | 
   165 |    SimplePublicModifier ::=
   166 |        $$pub$$
   167 | 
   168 |    SuperPublicModifier ::=
   169 |        $$pub$$ $$($$ $$super$$ $$)$$
   170 | 
   171 | .. rubric:: Legality Rules
   172 | 
   173 | .. glossary-entry:: visibility
   174 |    
   175 |    :glossary:
   176 |      :dp:`fls_sadmsqhptlho`
   177 |      :dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
   178 |      which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
   179 |    :chapter:
   180 |      :dp:`fls_7kpepal8ghuj`
   181 |      :t:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
   182 |      which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
   183 | 
   184 | .. glossary-entry:: public visibility
   185 |    
   186 |    :glossary:
   187 |      :dp:`fls_6cfxqtl921ko`
   188 |      :dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
   189 |      to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
   190 |      :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
   191 |    :chapter:
   192 |      :dp:`fls_qo0itr5il1kk`
   193 |      :t:`Public visibility` is a kind of :t:`visibility` that allows for a :t:`name`
```

Glossary block (current):
```
     :dp:`fls_sadmsqhptlho`
     :dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
     which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
```

Chapter block (current):
```
     :dp:`fls_7kpepal8ghuj`
     :t:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
     which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

```

Static glossary entry:
```

:dp:`fls_sadmsqhptlho`
:dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_7kpepal8ghuj`
:t:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.

```

## 004 visibility modifier (dual)
- File: src/entities-and-resolution.rst:210
- Commit: 66a1099560705cbf09a1a0ce96f8eeb318085b76
- Indent: 0

Current context (10 lines before/after):
```
   200 |      :dp:`fls_duop22hyaweq`
   201 |      :dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
   202 |      to be referred to only by the current :t:`module` of the :t:`entity`, and its
   203 |      descendant :t:`[module]s`.
   204 |    :chapter:
   205 |      :dp:`fls_knjruq5wppv`
   206 |      :t:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
   207 |      to be referred to only by the current :t:`module` of the :t:`entity`, and its
   208 |      descendant :t:`[module]s`.
   209 | 
   210 | .. glossary-entry:: visibility modifier
   211 |    
   212 |    :glossary:
   213 |      :dp:`fls_ze7befho4jhs`
   214 |      A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
   215 |      :t:`item`.
   216 |    :chapter:
   217 |      :dp:`fls_t7i4n19qdgn4`
   218 |      A :t:`visibility modifier` sets the :t:`visibility` of a :t:`name`.
   219 | 
   220 | .. glossary-entry:: crate public modifier
   221 |    
   222 |    :glossary:
   223 |      :dp:`fls_dj7fmrqhbhsv`
   224 |      A :dt:`crate public modifier` is a :t:`visibility modifier` that grants a
   225 |      :t:`name` :t:`public visibility` within the current :t:`crate` only.
   226 |      
   227 |      :dp:`fls_wjfupeyeczp0`
   228 |      See :s:`CratePublicModifier`.
   229 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_ze7befho4jhs`
     A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
     :t:`item`.
```

Chapter block (current):
```
     :dp:`fls_t7i4n19qdgn4`
     A :t:`visibility modifier` sets the :t:`visibility` of a :t:`name`.

```

Static glossary entry:
```

:dp:`fls_ze7befho4jhs`
A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
:t:`item`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_t7i4n19qdgn4`
A :t:`visibility modifier` sets the :t:`visibility` of a :t:`name`.

```

## 005 unqualified path expression (dual)
- File: src/entities-and-resolution.rst:513
- Commit: 31ccd8534dc29d58e9a37eeb005dace8db822a8d
- Indent: 0

Current context (10 lines before/after):
```
   503 |    
   504 |    :glossary:
   505 |      :dp:`fls_T4Xd6W6EqPSb`
   506 |      A :dt:`multi segment path` is a :t:`path` consisting of more than one
   507 |      :t:`path segment`.
   508 |    :chapter:
   509 |      :dp:`fls_wm61yeclairz`
   510 |      A :t:`multi segment path` is a :t:`path` consisting of more than one
   511 |      :t:`path segment`.
   512 | 
   513 | .. glossary-entry:: unqualified path expression
   514 |    
   515 |    :glossary:
   516 |      :dp:`fls_9xKgP8uVsOaR`
   517 |      An :dt:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   518 |    :chapter:
   519 |      :dp:`fls_nRgjCLYZL3iX`
   520 |      An :t:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   521 | 
   522 | :dp:`fls_tvvycup09b51`
   523 | A :t:`path expression` is subject to :t:`path expression resolution`.
   524 | 
   525 | .. glossary-entry:: type path
   526 |    
   527 |    :glossary:
   528 |      :dp:`fls_UBR5czHrMTrx`
   529 |      A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
   530 |      
   531 |      :dp:`fls_7CbNAZYSZayW`
```

Glossary block (current):
```
     :dp:`fls_9xKgP8uVsOaR`
     An :dt:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
```

Chapter block (current):
```
     :dp:`fls_nRgjCLYZL3iX`
     An :t:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.

```

Static glossary entry:
```

:dp:`fls_9xKgP8uVsOaR`
An :dt:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_nRgjCLYZL3iX`
An :t:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.

```

## 006 unsafe block expression (dual)
- File: src/expressions.rst:1138
- Commit: 31ccd8534dc29d58e9a37eeb005dace8db822a8d
- Indent: 0

Current context (10 lines before/after):
```
  1128 |        $$unsafe$$ BlockExpression
  1129 | 
  1130 | .. rubric:: Legality Rules
  1131 | 
  1132 | .. glossary-entry:: unsafe block
  1133 |    
  1134 |    :glossary:
  1135 |      :dp:`fls_8tkolhmd6xfp`
  1136 |      For :dt:`unsafe block`, see :t:`unsafe block expression`.
  1137 | 
  1138 | .. glossary-entry:: unsafe block expression
  1139 |    
  1140 |    :glossary:
  1141 |      :dp:`fls_et2h89jyivhs`
  1142 |      An :dt:`unsafe block expression` is a :t:`block expression` that is specified
  1143 |      with :t:`keyword` ``unsafe``.
  1144 |      
  1145 |      :dp:`fls_c94rudunhp5b`
  1146 |      See :s:`UnsafeBlockExpression`.
  1147 |    :chapter:
  1148 |      :dp:`fls_2az5huhcxzzy`
  1149 |      An :t:`unsafe block expression` is a :t:`block expression` that is specified
  1150 |      with :t:`keyword` ``unsafe``.
  1151 | 
  1152 | :dp:`fls_5ucvvja4dzoc`
  1153 | An :t:`unsafe block expression` allows :t:`unsafety`.
  1154 | 
  1155 | :dp:`fls_j3mmg317q442`
  1156 | The :t:`type` of the :t:`unsafe block expression` is the :t:`type` of its
  1157 | :t:`block expression`.
  1158 | 
  1159 | :dp:`fls_nygurv3x3wq6`
  1160 | The :t:`value` of the :t:`unsafe block expression` is the :t:`value` of its
  1161 | :t:`block expression`.
```

Glossary block (current):
```
     :dp:`fls_et2h89jyivhs`
     An :dt:`unsafe block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``unsafe``.
     
     :dp:`fls_c94rudunhp5b`
     See :s:`UnsafeBlockExpression`.
```

Chapter block (current):
```
     :dp:`fls_2az5huhcxzzy`
     An :t:`unsafe block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``unsafe``.

```

Static glossary entry:
```

:dp:`fls_et2h89jyivhs`
An :dt:`unsafe block expression` is a :t:`block expression` that is specified
with :t:`keyword` ``unsafe``.

:dp:`fls_c94rudunhp5b`
See :s:`UnsafeBlockExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_2az5huhcxzzy`
An :t:`unsafe block expression` is a :t:`block expression` that is specified
with :t:`keyword` ``unsafe``.

```

## 007 type path resolution (dual)
- File: src/entities-and-resolution.rst:2284
- Commit: ba1d4b9508e877d0bdcb75a99661163a9bffbae2
- Indent: 0

Current context (10 lines before/after):
```
  2274 |       :t:`path segment` resolves to that :t:`constant` or :t:`function` and
  2275 |       :t:`path expression resolution` stops.
  2276 | 
  2277 | .. _fls_1h0olpc7vbui:
  2278 | 
  2279 | Type Path Resolution
  2280 | ^^^^^^^^^^^^^^^^^^^^
  2281 | 
  2282 | .. rubric:: Legality Rules
  2283 | 
  2284 | .. glossary-entry:: type path resolution
  2285 |    
  2286 |    :glossary:
  2287 |      :dp:`fls_Xv6JbfdIyvA3`
  2288 |      :dt:`Type path resolution` is a form of :t:`path resolution` that applies to
  2289 |      a :t:`type path`.
  2290 |    :chapter:
  2291 |      :dp:`fls_2zuncql8ir5k`
  2292 |      :t:`Type path resolution` is a form of :t:`path resolution` that applies to
  2293 |      a :t:`type path`.
  2294 | 
  2295 | :dp:`fls_bv5cj918dqqe`
  2296 | The :t:`namespace context` of :t:`type path resolution` is the
  2297 | :t:`type namespace`.
  2298 | 
  2299 | :dp:`fls_bsakzuteuh5s`
  2300 | The leftmost :t:`path segment` of a :t:`type path` is resolved using general
  2301 | :t:`path resolution`. The remaining :t:`[path segment]s` are resolved in
  2302 | left-to-right order, as follows:
  2303 | 
  2304 | * :dp:`fls_j1ewjisx0mc2`
```

Glossary block (current):
```
     :dp:`fls_Xv6JbfdIyvA3`
     :dt:`Type path resolution` is a form of :t:`path resolution` that applies to
     a :t:`type path`.
```

Chapter block (current):
```
     :dp:`fls_2zuncql8ir5k`
     :t:`Type path resolution` is a form of :t:`path resolution` that applies to
     a :t:`type path`.

```

Static glossary entry:
```

:dp:`fls_Xv6JbfdIyvA3`
:dt:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_2zuncql8ir5k`
:t:`Type path resolution` is a form of :t:`path resolution` that applies to
a :t:`type path`.

```

## 008 union type (dual)
- File: src/types-and-traits.rst:1364
- Commit: ba1d4b9508e877d0bdcb75a99661163a9bffbae2
- Indent: 0

Current context (10 lines before/after):
```
  1354 |        $$union$$ Name GenericParameterList? WhereClause? RecordStructFieldList
  1355 | 
  1356 | .. rubric:: Legality Rules
  1357 | 
  1358 | .. glossary-entry:: union
  1359 |    
  1360 |    :glossary:
  1361 |      :dp:`fls_x3oibk39dvem`
  1362 |      A :dt:`union` is an :t:`item` that declares a :t:`union type`.
  1363 | 
  1364 | .. glossary-entry:: union type
  1365 |    
  1366 |    :glossary:
  1367 |      :dp:`fls_af2sscrep7mc`
  1368 |      A :dt:`union type` is an :t:`abstract data type` similar to a :t:`C`-like union.
  1369 |      
  1370 |      :dp:`fls_fgvjogfz8ink`
  1371 |      See :s:`UnionDeclaration`.
  1372 |    :chapter:
  1373 |      :dp:`fls_nskmnzq95yqm`
  1374 |      A :t:`union type` is an :t:`abstract data type` that is a sum of other
  1375 |      :t:`[type]s`.
  1376 | 
  1377 | .. glossary-entry:: union field
  1378 |    
  1379 |    :glossary:
  1380 |      :dp:`fls_6t2fbnlndz8y`
  1381 |      A :dt:`union field` is a :t:`field` of a :t:`union type`.
  1382 | 
  1383 | .. glossary-entry:: union value
  1384 |    
  1385 |    :glossary:
  1386 |      :dp:`fls_9BPrxky3a4nE`
```

Glossary block (current):
```
     :dp:`fls_af2sscrep7mc`
     A :dt:`union type` is an :t:`abstract data type` similar to a :t:`C`-like union.
     
     :dp:`fls_fgvjogfz8ink`
     See :s:`UnionDeclaration`.
```

Chapter block (current):
```
     :dp:`fls_nskmnzq95yqm`
     A :t:`union type` is an :t:`abstract data type` that is a sum of other
     :t:`[type]s`.

```

Static glossary entry:
```

:dp:`fls_af2sscrep7mc`
A :dt:`union type` is an :t:`abstract data type` similar to a :t:`C`-like union.

:dp:`fls_fgvjogfz8ink`
See :s:`UnionDeclaration`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_nskmnzq95yqm`
A :t:`union type` is an :t:`abstract data type` that is a sum of other
:t:`[type]s`.

```

## 009 type path (dual)
- File: src/entities-and-resolution.rst:525
- Commit: cf11e81e0115b4f4234b6f113802fe2ece9b146e
- Indent: 0

Current context (10 lines before/after):
```
   515 |    :glossary:
   516 |      :dp:`fls_9xKgP8uVsOaR`
   517 |      An :dt:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   518 |    :chapter:
   519 |      :dp:`fls_nRgjCLYZL3iX`
   520 |      An :t:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   521 | 
   522 | :dp:`fls_tvvycup09b51`
   523 | A :t:`path expression` is subject to :t:`path expression resolution`.
   524 | 
   525 | .. glossary-entry:: type path
   526 |    
   527 |    :glossary:
   528 |      :dp:`fls_UBR5czHrMTrx`
   529 |      A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
   530 |      
   531 |      :dp:`fls_7CbNAZYSZayW`
   532 |      See :s:`TypePath`.
   533 |    :chapter:
   534 |      :dp:`fls_h2zikgmazoxx`
   535 |      A :t:`type path` is a :t:`path` that acts as a :t:`type specification`.
   536 | 
   537 | :dp:`fls_nj7s6xmzx55f`
   538 | A :t:`type path` is subject to :t:`type path resolution`.
   539 | 
   540 | .. glossary-entry:: qualifying trait
   541 |    
   542 |    :glossary:
   543 |      :dp:`fls_zKY1dWBMrqXZ`
   544 |      A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
   545 |      :t:`qualified type`.
   546 |      
```

Glossary block (current):
```
     :dp:`fls_UBR5czHrMTrx`
     A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.
     
     :dp:`fls_7CbNAZYSZayW`
     See :s:`TypePath`.
```

Chapter block (current):
```
     :dp:`fls_h2zikgmazoxx`
     A :t:`type path` is a :t:`path` that acts as a :t:`type specification`.

```

Static glossary entry:
```

:dp:`fls_UBR5czHrMTrx`
A :dt:`type path` is a :t:`path` that acts as a :t:`type specification`.

:dp:`fls_7CbNAZYSZayW`
See :s:`TypePath`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_h2zikgmazoxx`
A :t:`type path` is a :t:`path` that acts as a :t:`type specification`.

```

## 010 under resolution (dual)
- File: src/entities-and-resolution.rst:1619
- Commit: cf11e81e0115b4f4234b6f113802fe2ece9b146e
- Indent: 0

Current context (10 lines before/after):
```
  1609 |    :glossary:
  1610 |      :dp:`fls_PQjEvLs5cE4y`
  1611 |      :dt:`Resolution` is the process of finding a unique interpretation for a
  1612 |      :t:`field access expression`, a :t:`method call expression`, or a :t:`path`.
  1613 |    :chapter:
  1614 |      :dp:`fls_ho4kem1slcxg`
  1615 |      :t:`Resolution` is the process of finding a unique interpretation for a
  1616 |      :t:`field access expression`, a :t:`method call expression`, a :t:`call
  1617 |      expression` or a :t:`path`.
  1618 | 
  1619 | .. glossary-entry:: under resolution
  1620 |    
  1621 |    :glossary:
  1622 |      :dp:`fls_BppwXSVUWtEu`
  1623 |      A :t:`construct` that is being resolved is said to be :dt:`under resolution`.
  1624 |    :chapter:
  1625 |      :dp:`fls_7le2vcdbtxbq`
  1626 |      A :t:`construct` that is being resolved is said to be :t:`under resolution`.
  1627 | 
  1628 | .. glossary-entry:: dereference type
  1629 |    
  1630 |    :glossary:
  1631 |      :dp:`fls_HfuUQ7IaoI5j`
  1632 |      A :dt:`dereference type` is either a :t:`reference type` or a :t:`type` that
  1633 |      implements the :std:`core::ops::Deref` :t:`trait`.
  1634 |    :chapter:
  1635 |      :dp:`fls_x3alg07yd7hx`
  1636 |      A :t:`dereference type` is either a :t:`reference type` or a :t:`type` that
  1637 |      implements the :std:`core::ops::Deref` :t:`trait`.
```

Glossary block (current):
```
     :dp:`fls_BppwXSVUWtEu`
     A :t:`construct` that is being resolved is said to be :dt:`under resolution`.
```

Chapter block (current):
```
     :dp:`fls_7le2vcdbtxbq`
     A :t:`construct` that is being resolved is said to be :t:`under resolution`.

```

Static glossary entry:
```

:dp:`fls_BppwXSVUWtEu`
A :t:`construct` that is being resolved is said to be :dt:`under resolution`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_7le2vcdbtxbq`
A :t:`construct` that is being resolved is said to be :t:`under resolution`.

```

## 011 tuple expression (dual)
- File: src/expressions.rst:4073
- Commit: 52d13394ed3976cbeadc5bc15115cd2570586ec3
- Indent: 0

Current context (10 lines before/after):
```
  4063 | .. syntax::
  4064 | 
  4065 |    TupleExpression ::=
  4066 |        $$($$ TupleInitializerList? $$)$$
  4067 | 
  4068 |    TupleInitializerList ::=
  4069 |        ExpressionList
  4070 | 
  4071 | .. rubric:: Legality Rules
  4072 | 
  4073 | .. glossary-entry:: tuple expression
  4074 |    
  4075 |    :glossary:
  4076 |      :dp:`fls_x7m4u1dx4eli`
  4077 |      A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
  4078 |      
  4079 |      :dp:`fls_qawnvcddgyxx`
  4080 |      See :s:`TupleExpression`.
  4081 |    :chapter:
  4082 |      :dp:`fls_87rp1hfwvjel`
  4083 |      A :t:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
  4084 | 
  4085 | .. glossary-entry:: tuple initializer
  4086 |    
  4087 |    :glossary:
  4088 |      :dp:`fls_94hg6re11zl5`
  4089 |      A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
  4090 |      :t:`tuple field` in a :t:`tuple expression`.
  4091 |    :chapter:
  4092 |      :dp:`fls_581y6jq1eyn8`
  4093 |      A :t:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
  4094 |      :t:`tuple field` in a :t:`tuple expression`.
```

Glossary block (current):
```
     :dp:`fls_x7m4u1dx4eli`
     A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
     
     :dp:`fls_qawnvcddgyxx`
     See :s:`TupleExpression`.
```

Chapter block (current):
```
     :dp:`fls_87rp1hfwvjel`
     A :t:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

```

Static glossary entry:
```

:dp:`fls_x7m4u1dx4eli`
A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

:dp:`fls_qawnvcddgyxx`
See :s:`TupleExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_87rp1hfwvjel`
A :t:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

```

## 012 tuple initializer (dual)
- File: src/expressions.rst:4085
- Commit: 52d13394ed3976cbeadc5bc15115cd2570586ec3
- Indent: 0

Current context (10 lines before/after):
```
  4075 |    :glossary:
  4076 |      :dp:`fls_x7m4u1dx4eli`
  4077 |      A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
  4078 |      
  4079 |      :dp:`fls_qawnvcddgyxx`
  4080 |      See :s:`TupleExpression`.
  4081 |    :chapter:
  4082 |      :dp:`fls_87rp1hfwvjel`
  4083 |      A :t:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
  4084 | 
  4085 | .. glossary-entry:: tuple initializer
  4086 |    
  4087 |    :glossary:
  4088 |      :dp:`fls_94hg6re11zl5`
  4089 |      A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
  4090 |      :t:`tuple field` in a :t:`tuple expression`.
  4091 |    :chapter:
  4092 |      :dp:`fls_581y6jq1eyn8`
  4093 |      A :t:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
  4094 |      :t:`tuple field` in a :t:`tuple expression`.
  4095 | 
  4096 | :dp:`fls_ljz3sxmfzflm`
  4097 | The :t:`type` of a :t:`tuple expression` is ``(T1, T2, ..., TN)``, where ``T1``
  4098 | is the :t:`type` of the first :t:`tuple initializer`, ``T2`` is the :t:`type` of
  4099 | the second :t:`tuple initializer`, and ``TN`` is the :t:`type` of the ``N``-th
  4100 | :t:`tuple initializer`.
  4101 | 
  4102 | :dp:`fls_k2aznqo9j49p`
  4103 | The :t:`value` of a :t:`tuple expression` is ``(V1, V2, ..., VN)``, where ``V1``
  4104 | is the :t:`value` of the first :t:`tuple initializer`, ``V2`` is the :t:`value`
  4105 | of the second :t:`tuple initializer`, and ``VN`` is the :t:`value` of the
```

Glossary block (current):
```
     :dp:`fls_94hg6re11zl5`
     A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
     :t:`tuple field` in a :t:`tuple expression`.
```

Chapter block (current):
```
     :dp:`fls_581y6jq1eyn8`
     A :t:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
     :t:`tuple field` in a :t:`tuple expression`.

```

Static glossary entry:
```

:dp:`fls_94hg6re11zl5`
A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_581y6jq1eyn8`
A :t:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
:t:`tuple field` in a :t:`tuple expression`.

```

## 013 sync type (dual)
- File: src/concurrency.rst:66
- Commit: dc774c9d0b2a6ae1dff7a9cd4e1d8a84b3489ceb
- Indent: 0

Current context (10 lines before/after):
```
    56 | 
    57 | :dp:`fls_cax6fe4em23k`
    58 | An :t:`abstract data type` automatically implements the
    59 | :std:`core::marker::Send` :t:`trait` if the :t:`[type]s` of all its
    60 | :t:`[field]s` are :t:`[send type]s`.
    61 | 
    62 | :dp:`fls_4ypqdehn7b0v`
    63 | A :t:`send type` shall have :t:`[value]s` that are safe to transfer across
    64 | thread boundaries.
    65 | 
    66 | .. glossary-entry:: sync type
    67 |    
    68 |    :glossary:
    69 |      :dp:`fls_rpc0c8qx3nbo`
    70 |      A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
    71 |      :t:`trait`.
    72 |    :chapter:
    73 |      :dp:`fls_dekskhk4g895`
    74 |      A :t:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
    75 |      :t:`trait`.
    76 | 
    77 | :dp:`fls_y0iqr5ibnbfe`
    78 | An :t:`abstract data type` automatically implements the
    79 | :std:`core::marker::Sync` :t:`trait` if the :t:`[type]s` of all its
    80 | :t:`[field]s` are :t:`[sync type]s`.
    81 | 
    82 | :dp:`fls_zgemofbs5q2x`
    83 | A :t:`sync type` shall have :t:`[value]s` that are allowed to be shared across
    84 | multiple threads at any given time without incurring data races.
    85 | 
    86 | .. _fls_vyc9vcuamlph:
```

Glossary block (current):
```
     :dp:`fls_rpc0c8qx3nbo`
     A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
     :t:`trait`.
```

Chapter block (current):
```
     :dp:`fls_dekskhk4g895`
     A :t:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
     :t:`trait`.

```

Static glossary entry:
```

:dp:`fls_rpc0c8qx3nbo`
A :dt:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_dekskhk4g895`
A :t:`sync type` is a :t:`type` that implements the :std:`core::marker::Sync`
:t:`trait`.

```

## 014 super public modifier (dual)
- File: src/entities-and-resolution.rst:288
- Commit: dc774c9d0b2a6ae1dff7a9cd4e1d8a84b3489ceb
- Indent: 0

Current context (10 lines before/after):
```
   278 |      A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
   279 |      :t:`name` :t:`public visibility`.
   280 |      
   281 |      :dp:`fls_rd68vm2f2qy5`
   282 |      See :s:`SelfPublicModifier`.
   283 |    :chapter:
   284 |      :dp:`fls_np8aghofjqhm`
   285 |      A :t:`simple public modifier` is a :t:`visibility modifier` that grants a
   286 |      :t:`name` :t:`public visibility`.
   287 | 
   288 | .. glossary-entry:: super public modifier
   289 |    
   290 |    :glossary:
   291 |      :dp:`fls_vry5mhs3a5wv`
   292 |      A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
   293 |      :t:`name` :t:`public visibility` within the parent :t:`module` only.
   294 |      
   295 |      :dp:`fls_4a1s9bcrk5oy`
   296 |      See :s:`SuperPublicModifier`.
   297 |    :chapter:
   298 |      :dp:`fls_quzvhzpr0124`
   299 |      A :t:`super public modifier` is a :t:`visibility modifier` that grants a
   300 |      :t:`name` :t:`public visibility` within the parent :t:`module` only. A
   301 |      :t:`super public modifier` is equivalent to a :t:`simple path public modifier`
   302 |      where the :t:`simple path` denotes :t:`keyword` ``super``.
   303 | 
   304 | :dp:`fls_utgjx6l5zwfl`
   305 | An external :t:`item`, a :t:`field`, or an :t:`item` that appears without a
   306 | :t:`visibility modifier` has :t:`private visibility` by default.
   307 | 
   308 | :dp:`fls_jifg2st5bfd6`
   309 | An :t:`associated item` of a :t:`trait` has the same :t:`visibility` as the
   310 | :t:`trait`.
   311 | 
   312 | :dp:`fls_dm0xr424ine1`
   313 | An :t:`enum variant` and its :t:`[field]s` have the same :t:`visibility` as the
```

Glossary block (current):
```
     :dp:`fls_vry5mhs3a5wv`
     A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility` within the parent :t:`module` only.
     
     :dp:`fls_4a1s9bcrk5oy`
     See :s:`SuperPublicModifier`.
```

Chapter block (current):
```
     :dp:`fls_quzvhzpr0124`
     A :t:`super public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility` within the parent :t:`module` only. A
     :t:`super public modifier` is equivalent to a :t:`simple path public modifier`
     where the :t:`simple path` denotes :t:`keyword` ``super``.

```

Static glossary entry:
```

:dp:`fls_vry5mhs3a5wv`
A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only.

:dp:`fls_4a1s9bcrk5oy`
See :s:`SuperPublicModifier`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_quzvhzpr0124`
A :t:`super public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the parent :t:`module` only. A
:t:`super public modifier` is equivalent to a :t:`simple path public modifier`
where the :t:`simple path` denotes :t:`keyword` ``super``.

```

## 015 subject expression (dual)
- File: src/expressions.rst:67
- Commit: 6f91bcd7e628612db9af159d58fc072e5f1867eb
- Indent: 0

Current context (10 lines before/after):
```
    57 | 
    58 |    Operand ::=
    59 |        Expression
    60 | 
    61 |    LeftOperand ::=
    62 |        Operand
    63 | 
    64 |    RightOperand ::=
    65 |        Operand
    66 | 
    67 | .. glossary-entry:: subject expression
    68 |    
    69 |    :glossary:
    70 |      :dp:`fls_xisqke87ert`
    71 |      A :dt:`subject expression` is an :t:`expression` that controls
    72 |      :t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.
    73 |      
    74 |      :dp:`fls_gph5doham4js`
    75 |      See :s:`SubjectExpression`.
    76 |    :chapter:
    77 |      :dp:`fls_pwut2jbmk66k`
    78 |      A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
    79 |      :s:`StructExpression`.
    80 | 
    81 | .. glossary-entry:: subject let expression
    82 |    
    83 |    :glossary:
    84 |      :dp:`fls_b3ckv6zgnaeb`
    85 |      A :dt:`subject let expression` is an :t:`expression` that controls
    86 |      :t:`[if let expression]s` and :t:`[while let loop]s`.
    87 |      
    88 |      :dp:`fls_vnzaargh5yok`
    89 |      See :s:`SubjectLetExpression`.
    90 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_xisqke87ert`
     A :dt:`subject expression` is an :t:`expression` that controls
     :t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.
     
     :dp:`fls_gph5doham4js`
     See :s:`SubjectExpression`.
```

Chapter block (current):
```
     :dp:`fls_pwut2jbmk66k`
     A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
     :s:`StructExpression`.

```

Static glossary entry:
```

:dp:`fls_xisqke87ert`
A :dt:`subject expression` is an :t:`expression` that controls
:t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.

:dp:`fls_gph5doham4js`
See :s:`SubjectExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_pwut2jbmk66k`
A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
:s:`StructExpression`.

```

## 016 subject let expression (dual)
- File: src/expressions.rst:81
- Commit: 6f91bcd7e628612db9af159d58fc072e5f1867eb
- Indent: 0

Current context (10 lines before/after):
```
    71 |      A :dt:`subject expression` is an :t:`expression` that controls
    72 |      :t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.
    73 |      
    74 |      :dp:`fls_gph5doham4js`
    75 |      See :s:`SubjectExpression`.
    76 |    :chapter:
    77 |      :dp:`fls_pwut2jbmk66k`
    78 |      A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
    79 |      :s:`StructExpression`.
    80 | 
    81 | .. glossary-entry:: subject let expression
    82 |    
    83 |    :glossary:
    84 |      :dp:`fls_b3ckv6zgnaeb`
    85 |      A :dt:`subject let expression` is an :t:`expression` that controls
    86 |      :t:`[if let expression]s` and :t:`[while let loop]s`.
    87 |      
    88 |      :dp:`fls_vnzaargh5yok`
    89 |      See :s:`SubjectLetExpression`.
    90 |    :chapter:
    91 |      :dp:`fls_361q9ljc6ybz`
    92 |      A :ds:`SubjectLetExpression` is any expression in category
    93 |      :s:`SubjectExpression`, except :s:`LazyBooleanExpression`.
    94 | 
    95 | .. glossary-entry:: subexpression
    96 |    
    97 |    :glossary:
    98 |      :dp:`fls_bNSHwD4Kpfm0`
    99 |      A :dt:`subexpression` is an :t:`expression` nested within another
   100 |      :t:`expression`.
   101 | 
   102 | .. rubric:: Legality Rules
   103 | 
   104 | .. glossary-entry:: expression
```

Glossary block (current):
```
     :dp:`fls_b3ckv6zgnaeb`
     A :dt:`subject let expression` is an :t:`expression` that controls
     :t:`[if let expression]s` and :t:`[while let loop]s`.
     
     :dp:`fls_vnzaargh5yok`
     See :s:`SubjectLetExpression`.
```

Chapter block (current):
```
     :dp:`fls_361q9ljc6ybz`
     A :ds:`SubjectLetExpression` is any expression in category
     :s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

```

Static glossary entry:
```

:dp:`fls_b3ckv6zgnaeb`
A :dt:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

:dp:`fls_vnzaargh5yok`
See :s:`SubjectLetExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_361q9ljc6ybz`
A :ds:`SubjectLetExpression` is any expression in category
:s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

```

## 017 simple path public modifier (dual)
- File: src/entities-and-resolution.rst:250
- Commit: 6cc6e9f1f6cb14ffe8cdc156ba852ef171bcc767
- Indent: 0

Current context (10 lines before/after):
```
   240 |      
   241 |      :dp:`fls_21cvbfjpckkt`
   242 |      See :s:`SelfPublicModifier`.
   243 |    :chapter:
   244 |      :dp:`fls_tnh7o3pb4e22`
   245 |      A :t:`self public modifier` is a :t:`visibility modifier` that grants a
   246 |      :t:`name` :t:`private visibility`. A :t:`self public modifier` is equivalent
   247 |      to a :t:`simple path public modifier` where the :t:`simple path` denotes
   248 |      :t:`keyword` ``self``.
   249 | 
   250 | .. glossary-entry:: simple path public modifier
   251 |    
   252 |    :glossary:
   253 |      :dp:`fls_mby9r0jm6uyv`
   254 |      A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
   255 |      :t:`name` :t:`public visibility` within the provided :t:`simple path` only.
   256 |      
   257 |      :dp:`fls_mud4hw74kuh6`
   258 |      See :s:`SimplePathPublicModifier`.
   259 |    :chapter:
   260 |      :dp:`fls_yymgpyi67dty`
   261 |      A :t:`simple path public modifier` is a :t:`visibility modifier` that grants a
   262 |      :t:`name` :t:`public visibility` within the provided :t:`simple path` only.
   263 | 
   264 | :dp:`fls_hc121mxknq03`
   265 | The :t:`simple path` of a :t:`simple path public modifier` shall start
   266 | with a :t:`path segment` expressed by either :t:`keyword` ``crate``,
   267 | :t:`keyword` ``self``, or :t:`keyword` ``super``.
   268 | 
   269 | :dp:`fls_icztzxjpm1du`
   270 | The :t:`simple path` of a :t:`simple path public modifier` shall resolve to
   271 | an ancestor :t:`module` of the current :t:`module` or the current :t:`module`
   272 | itself.
   273 | 
```

Glossary block (current):
```
     :dp:`fls_mby9r0jm6uyv`
     A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility` within the provided :t:`simple path` only.
     
     :dp:`fls_mud4hw74kuh6`
     See :s:`SimplePathPublicModifier`.
```

Chapter block (current):
```
     :dp:`fls_yymgpyi67dty`
     A :t:`simple path public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility` within the provided :t:`simple path` only.

```

Static glossary entry:
```

:dp:`fls_mby9r0jm6uyv`
A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.

:dp:`fls_mud4hw74kuh6`
See :s:`SimplePathPublicModifier`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_yymgpyi67dty`
A :t:`simple path public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility` within the provided :t:`simple path` only.

```

## 018 simple public modifier (dual)
- File: src/entities-and-resolution.rst:274
- Commit: 6cc6e9f1f6cb14ffe8cdc156ba852ef171bcc767
- Indent: 0

Current context (10 lines before/after):
```
   264 | :dp:`fls_hc121mxknq03`
   265 | The :t:`simple path` of a :t:`simple path public modifier` shall start
   266 | with a :t:`path segment` expressed by either :t:`keyword` ``crate``,
   267 | :t:`keyword` ``self``, or :t:`keyword` ``super``.
   268 | 
   269 | :dp:`fls_icztzxjpm1du`
   270 | The :t:`simple path` of a :t:`simple path public modifier` shall resolve to
   271 | an ancestor :t:`module` of the current :t:`module` or the current :t:`module`
   272 | itself.
   273 | 
   274 | .. glossary-entry:: simple public modifier
   275 |    
   276 |    :glossary:
   277 |      :dp:`fls_ce1ounn1g68`
   278 |      A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
   279 |      :t:`name` :t:`public visibility`.
   280 |      
   281 |      :dp:`fls_rd68vm2f2qy5`
   282 |      See :s:`SelfPublicModifier`.
   283 |    :chapter:
   284 |      :dp:`fls_np8aghofjqhm`
   285 |      A :t:`simple public modifier` is a :t:`visibility modifier` that grants a
   286 |      :t:`name` :t:`public visibility`.
   287 | 
   288 | .. glossary-entry:: super public modifier
   289 |    
   290 |    :glossary:
   291 |      :dp:`fls_vry5mhs3a5wv`
   292 |      A :dt:`super public modifier` is a :t:`visibility modifier` that grants a
   293 |      :t:`name` :t:`public visibility` within the parent :t:`module` only.
   294 |      
   295 |      :dp:`fls_4a1s9bcrk5oy`
   296 |      See :s:`SuperPublicModifier`.
   297 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_ce1ounn1g68`
     A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility`.
     
     :dp:`fls_rd68vm2f2qy5`
     See :s:`SelfPublicModifier`.
```

Chapter block (current):
```
     :dp:`fls_np8aghofjqhm`
     A :t:`simple public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`public visibility`.

```

Static glossary entry:
```

:dp:`fls_ce1ounn1g68`
A :dt:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.

:dp:`fls_rd68vm2f2qy5`
See :s:`SelfPublicModifier`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_np8aghofjqhm`
A :t:`simple public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`public visibility`.

```

## 019 send type (dual)
- File: src/concurrency.rst:46
- Commit: bc8919fbbd8d4666fda0758018f0510370466334
- Indent: 0

Current context (10 lines before/after):
```
    36 | Send and Sync
    37 | -------------
    38 | 
    39 | .. rubric:: Legality Rules
    40 | 
    41 | :dp:`fls_n5l17mlglq11`
    42 | The Rust programming language provides the :std:`core::marker::Send` and
    43 | :std:`core::marker::Sync` :t:`[trait]s` for preventing data races at the
    44 | :t:`type` level.
    45 | 
    46 | .. glossary-entry:: send type
    47 |    
    48 |    :glossary:
    49 |      :dp:`fls_qfkng98dw6yy`
    50 |      A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
    51 |      :t:`trait`.
    52 |    :chapter:
    53 |      :dp:`fls_2jujsujpjp3w`
    54 |      A :t:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
    55 |      :t:`trait`.
    56 | 
    57 | :dp:`fls_cax6fe4em23k`
    58 | An :t:`abstract data type` automatically implements the
    59 | :std:`core::marker::Send` :t:`trait` if the :t:`[type]s` of all its
    60 | :t:`[field]s` are :t:`[send type]s`.
    61 | 
    62 | :dp:`fls_4ypqdehn7b0v`
    63 | A :t:`send type` shall have :t:`[value]s` that are safe to transfer across
    64 | thread boundaries.
    65 | 
    66 | .. glossary-entry:: sync type
```

Glossary block (current):
```
     :dp:`fls_qfkng98dw6yy`
     A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
     :t:`trait`.
```

Chapter block (current):
```
     :dp:`fls_2jujsujpjp3w`
     A :t:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
     :t:`trait`.

```

Static glossary entry:
```

:dp:`fls_qfkng98dw6yy`
A :dt:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_2jujsujpjp3w`
A :t:`send type` is a :t:`type` that implements the :std:`core::marker::Send`
:t:`trait`.

```

## 020 simple path (dual)
- File: src/entities-and-resolution.rst:456
- Commit: bc8919fbbd8d4666fda0758018f0510370466334
- Indent: 0

Current context (10 lines before/after):
```
   446 |    
   447 |    :glossary:
   448 |      :dp:`fls_msg8jw9momfw`
   449 |      A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
   450 |      ``::``.
   451 |    :chapter:
   452 |      :dp:`fls_7kb6ltajgiou`
   453 |      A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
   454 |      ``::``.
   455 | 
   456 | .. glossary-entry:: simple path
   457 |    
   458 |    :glossary:
   459 |      :dp:`fls_db91duoug4eb`
   460 |      A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
   461 |      :t:`[identifier]s` or certain :t:`[keyword]s`.
   462 |      
   463 |      :dp:`fls_cm7ysyfrdwom`
   464 |      See :s:`SimplePath`.
   465 |    :chapter:
   466 |      :dp:`fls_n77icl6idazp`
   467 |      A :t:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
   468 |      :t:`[identifier]s` or certain :t:`[keyword]s` as defined in the syntax rules
   469 |      above.
   470 | 
   471 | :dp:`fls_YnUsdSM4x9eq`
   472 | A :dt:`path prefix` is a :t:`path` with its last :t:`path segment` and
   473 | :t:`namespace qualifier` ``::`` stripped.
   474 | 
   475 | :dp:`fls_iuzvtr3oax1o`
   476 | If a :t:`simple path` appears in a :t:`use import` and starts with a
   477 | :t:`path segment` expressed as either :t:`keyword` ``crate``, :t:`keyword`
   478 | ``$crate``, :t:`keyword` ``self``, or :t:`keyword` ``super``, then the
   479 | :t:`path` shall be the :t:`simple path prefix` of a :t:`glob import` or a
   480 | :t:`nesting import`, or the :t:`simple path` of a :t:`simple import`.
```

Glossary block (current):
```
     :dp:`fls_db91duoug4eb`
     A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
     :t:`[identifier]s` or certain :t:`[keyword]s`.
     
     :dp:`fls_cm7ysyfrdwom`
     See :s:`SimplePath`.
```

Chapter block (current):
```
     :dp:`fls_n77icl6idazp`
     A :t:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
     :t:`[identifier]s` or certain :t:`[keyword]s` as defined in the syntax rules
     above.

```

Static glossary entry:
```

:dp:`fls_db91duoug4eb`
A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s`.

:dp:`fls_cm7ysyfrdwom`
See :s:`SimplePath`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_n77icl6idazp`
A :t:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s` as defined in the syntax rules
above.

```

## 021 self public modifier (dual)
- File: src/entities-and-resolution.rst:234
- Commit: 3925cc1fb6bb7f1d87d9b2d6b611be59eab141d8
- Indent: 0

Current context (10 lines before/after):
```
   224 |      A :dt:`crate public modifier` is a :t:`visibility modifier` that grants a
   225 |      :t:`name` :t:`public visibility` within the current :t:`crate` only.
   226 |      
   227 |      :dp:`fls_wjfupeyeczp0`
   228 |      See :s:`CratePublicModifier`.
   229 |    :chapter:
   230 |      :dp:`fls_aa4f3rvir9lm`
   231 |      A :t:`crate public modifier` is a :t:`visibility modifier` that grants a
   232 |      :t:`name` :t:`public visibility` within the current :t:`crate` only.
   233 | 
   234 | .. glossary-entry:: self public modifier
   235 |    
   236 |    :glossary:
   237 |      :dp:`fls_ln3bzqgctfym`
   238 |      A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
   239 |      :t:`name` :t:`private visibility`.
   240 |      
   241 |      :dp:`fls_21cvbfjpckkt`
   242 |      See :s:`SelfPublicModifier`.
   243 |    :chapter:
   244 |      :dp:`fls_tnh7o3pb4e22`
   245 |      A :t:`self public modifier` is a :t:`visibility modifier` that grants a
   246 |      :t:`name` :t:`private visibility`. A :t:`self public modifier` is equivalent
   247 |      to a :t:`simple path public modifier` where the :t:`simple path` denotes
   248 |      :t:`keyword` ``self``.
   249 | 
   250 | .. glossary-entry:: simple path public modifier
   251 |    
   252 |    :glossary:
   253 |      :dp:`fls_mby9r0jm6uyv`
   254 |      A :dt:`simple path public modifier` is a :t:`visibility modifier` that grants a
   255 |      :t:`name` :t:`public visibility` within the provided :t:`simple path` only.
   256 |      
   257 |      :dp:`fls_mud4hw74kuh6`
   258 |      See :s:`SimplePathPublicModifier`.
   259 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_ln3bzqgctfym`
     A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`private visibility`.
     
     :dp:`fls_21cvbfjpckkt`
     See :s:`SelfPublicModifier`.
```

Chapter block (current):
```
     :dp:`fls_tnh7o3pb4e22`
     A :t:`self public modifier` is a :t:`visibility modifier` that grants a
     :t:`name` :t:`private visibility`. A :t:`self public modifier` is equivalent
     to a :t:`simple path public modifier` where the :t:`simple path` denotes
     :t:`keyword` ``self``.

```

Static glossary entry:
```

:dp:`fls_ln3bzqgctfym`
A :dt:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`.

:dp:`fls_21cvbfjpckkt`
See :s:`SelfPublicModifier`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_tnh7o3pb4e22`
A :t:`self public modifier` is a :t:`visibility modifier` that grants a
:t:`name` :t:`private visibility`. A :t:`self public modifier` is equivalent
to a :t:`simple path public modifier` where the :t:`simple path` denotes
:t:`keyword` ``self``.

```

## 022 scope (dual)
- File: src/entities-and-resolution.rst:688
- Commit: 3925cc1fb6bb7f1d87d9b2d6b611be59eab141d8
- Indent: 0

Current context (10 lines before/after):
```
   678 |    type T = <S as T>::Assoc;
   679 | 
   680 | 
   681 | .. _fls_izl8iuhoz9e0:
   682 | 
   683 | Scopes
   684 | ------
   685 | 
   686 | .. rubric:: Legality Rules
   687 | 
   688 | .. glossary-entry:: scope
   689 |    
   690 |    :glossary:
   691 |      :dp:`fls_fachaj550cq1`
   692 |      A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
   693 |    :chapter:
   694 |      :dp:`fls_5x5xykocwyiy`
   695 |      A :t:`scope` is a region of program text where an :t:`entity` can be referred
   696 |      to. An :t:`entity` is :t:`in scope` when it can be referred to.
   697 | 
   698 | .. glossary-entry:: in scope
   699 |    
   700 |    :glossary:
   701 |      :dp:`fls_sy380geqvf2l`
   702 |      A :t:`name` is :dt:`in scope` when it can be referred to.
   703 | 
   704 | .. _fls_6ozthochxz1i:
   705 | 
   706 | Binding Scopes
   707 | ~~~~~~~~~~~~~~
```

Glossary block (current):
```
     :dp:`fls_fachaj550cq1`
     A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
```

Chapter block (current):
```
     :dp:`fls_5x5xykocwyiy`
     A :t:`scope` is a region of program text where an :t:`entity` can be referred
     to. An :t:`entity` is :t:`in scope` when it can be referred to.

```

Static glossary entry:
```

:dp:`fls_fachaj550cq1`
A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_5x5xykocwyiy`
A :t:`scope` is a region of program text where an :t:`entity` can be referred
to. An :t:`entity` is :t:`in scope` when it can be referred to.

```

## 023 remainder expression (dual)
- File: src/expressions.rst:1868
- Commit: e5bd283aaeb404147ba83c2dc3fb49b413e9313f
- Indent: 0

Current context (10 lines before/after):
```
  1858 | :t:`right operand` is the :t:`trait implementation` :t:`type parameter`.
  1859 | 
  1860 | :dp:`fls_ittf4yggk7do`
  1861 | The :t:`type` of a :t:`multiplication expression` is :t:`associated type`
  1862 | :std:`core::ops::Mul::Output`.
  1863 | 
  1864 | :dp:`fls_ylqm6wucq2sw`
  1865 | The :t:`value` of a :t:`multiplication expression` is the result of
  1866 | ``core::ops::Mul::mul(left_operand, right_operand)``.
  1867 | 
  1868 | .. glossary-entry:: remainder expression
  1869 |    
  1870 |    :glossary:
  1871 |      :dp:`fls_l6muwnclm1do`
  1872 |      A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
  1873 |      remainder division.
  1874 |      
  1875 |      :dp:`fls_h98qlby2uiru`
  1876 |      See :s:`RemainderExpression`.
  1877 |    :chapter:
  1878 |      :dp:`fls_3de9ulyzuoa`
  1879 |      A :t:`remainder expression` is an :t:`arithmetic expression` that uses remainder
  1880 |      division.
  1881 | 
  1882 | :dp:`fls_8fbhreyynhid`
  1883 | The :t:`type` of the :t:`left operand` of a :t:`remainder expression` shall
  1884 | implement the :std:`core::ops::Rem` :t:`trait` where the :t:`type` of the
  1885 | :t:`right operand` is the :t:`trait implementation` :t:`type parameter`.
  1886 | 
  1887 | :dp:`fls_u3jwnrqun5kl`
  1888 | The :t:`type` of a :t:`remainder expression` is :t:`associated type`
  1889 | :std:`core::ops::Rem::Output`.
  1890 | 
  1891 | :dp:`fls_2ude3wrxji2p`
```

Glossary block (current):
```
     :dp:`fls_l6muwnclm1do`
     A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
     remainder division.
     
     :dp:`fls_h98qlby2uiru`
     See :s:`RemainderExpression`.
```

Chapter block (current):
```
     :dp:`fls_3de9ulyzuoa`
     A :t:`remainder expression` is an :t:`arithmetic expression` that uses remainder
     division.

```

Static glossary entry:
```

:dp:`fls_l6muwnclm1do`
A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
remainder division.

:dp:`fls_h98qlby2uiru`
See :s:`RemainderExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_3de9ulyzuoa`
A :t:`remainder expression` is an :t:`arithmetic expression` that uses remainder
division.

```

## 024 remainder assignment expression (dual)
- File: src/expressions.rst:3383
- Commit: e5bd283aaeb404147ba83c2dc3fb49b413e9313f
- Indent: 0

Current context (10 lines before/after):
```
  3373 |      :dp:`fls_ndlv3k9uclz2`
  3374 |      A :t:`multiplication assignment expression` is a
  3375 |      :t:`compound assignment expression` that uses multiplication.
  3376 | 
  3377 | .. glossary-entry:: remainder assignment
  3378 |    
  3379 |    :glossary:
  3380 |      :dp:`fls_58eDC2XtQcaR`
  3381 |      For :dt:`remainder assignment`, see :t:`remainder assignment expression`.
  3382 | 
  3383 | .. glossary-entry:: remainder assignment expression
  3384 |    
  3385 |    :glossary:
  3386 |      :dp:`fls_en7ytqvefw7j`
  3387 |      A :dt:`remainder assignment expression` is a
  3388 |      :t:`compound assignment expression` that uses remainder division.
  3389 |      
  3390 |      :dp:`fls_rkk80quk8uzc`
  3391 |      See :s:`RemainderAssignmentExpression`.
  3392 |    :chapter:
  3393 |      :dp:`fls_fbp5dojti27r`
  3394 |      A :t:`remainder assignment expression` is a :t:`compound assignment expression`
  3395 |      that uses remainder division.
  3396 | 
  3397 | .. glossary-entry:: shift left assignment
  3398 |    
  3399 |    :glossary:
  3400 |      :dp:`fls_6adWrtvab6Tw`
  3401 |      For :dt:`shift left assignment`, see :t:`shift left assignment expression`.
  3402 | 
  3403 | .. glossary-entry:: shift left assignment expression
  3404 |    
  3405 |    :glossary:
  3406 |      :dp:`fls_j15ke2p8cjfp`
```

Glossary block (current):
```
     :dp:`fls_en7ytqvefw7j`
     A :dt:`remainder assignment expression` is a
     :t:`compound assignment expression` that uses remainder division.
     
     :dp:`fls_rkk80quk8uzc`
     See :s:`RemainderAssignmentExpression`.
```

Chapter block (current):
```
     :dp:`fls_fbp5dojti27r`
     A :t:`remainder assignment expression` is a :t:`compound assignment expression`
     that uses remainder division.

```

Static glossary entry:
```

:dp:`fls_en7ytqvefw7j`
A :dt:`remainder assignment expression` is a
:t:`compound assignment expression` that uses remainder division.

:dp:`fls_rkk80quk8uzc`
See :s:`RemainderAssignmentExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_fbp5dojti27r`
A :t:`remainder assignment expression` is a :t:`compound assignment expression`
that uses remainder division.

```

## 025 receiver type (dual)
- File: src/entities-and-resolution.rst:1770
- Commit: 3bff43ba3ae891942ed0511e29cd95174c621c92
- Indent: 0

Current context (10 lines before/after):
```
  1760 |    
  1761 |    :glossary:
  1762 |      :dp:`fls_LbW4z6OTuD1l`
  1763 |      :dt:`Method resolution` is a kind of :t:`resolution` that applies to a
  1764 |      :t:`method call expression`.
  1765 |    :chapter:
  1766 |      :dp:`fls_e5a5z5yht26l`
  1767 |      :t:`Method resolution` is a kind of :t:`resolution` that applies to a
  1768 |      :t:`method call expression`.
  1769 | 
  1770 | .. glossary-entry:: receiver type
  1771 |    
  1772 |    :glossary:
  1773 |      :dp:`fls_vgQmMlpFas5t`
  1774 |      A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.
  1775 |    :chapter:
  1776 |      :dp:`fls_mbdS0xiNlj92`
  1777 |      A :dt:`receiver type` is the :t:`type` of the :t:`receiver operand`
  1778 |      of a :t:`method call expression`.
  1779 | 
  1780 | :dp:`fls_z80ylmlu1f3q`
  1781 | A :dt:`candidate receiver type` is the :t:`type` of the :t:`receiver operand`
  1782 | of a :t:`method call expression` :t:`under resolution`.
  1783 | 
  1784 | :dp:`fls_e1029pvq706h`
  1785 | A :dt:`candidate receiver type chain` is a sequence of
  1786 | :t:`[candidate receiver type]s`. The :t:`candidate receiver type chain` starts
  1787 | with the :t:`type` of the :t:`receiver operand` of the
  1788 | :t:`method call expression` :t:`under resolution`. From then on, the
  1789 | :t:`candidate receiver type chain` is treated as a :t:`dereference type chain`.
```

Glossary block (current):
```
     :dp:`fls_vgQmMlpFas5t`
     A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.
```

Chapter block (current):
```
     :dp:`fls_mbdS0xiNlj92`
     A :dt:`receiver type` is the :t:`type` of the :t:`receiver operand`
     of a :t:`method call expression`.

```

Static glossary entry:
```

:dp:`fls_vgQmMlpFas5t`
A :dt:`receiver type` is the :t:`type` of a :t:`receiver operand`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_mbdS0xiNlj92`
A :dt:`receiver type` is the :t:`type` of the :t:`receiver operand`
of a :t:`method call expression`.

```

## 026 raw borrow expression (dual)
- File: src/expressions.rst:1348
- Commit: 3bff43ba3ae891942ed0511e29cd95174c621c92
- Indent: 0

Current context (10 lines before/after):
```
  1338 | 
  1339 | .. rubric:: Syntax
  1340 | 
  1341 | .. syntax::
  1342 | 
  1343 |    RawBorrowExpression ::=
  1344 |        $$&$$ $$raw$$ ($$const$$ | $$mut$$) Operand
  1345 | 
  1346 | .. rubric:: Legality Rules
  1347 | 
  1348 | .. glossary-entry:: raw borrow expression
  1349 |    
  1350 |    :glossary:
  1351 |      :dp:`fls_Fe39wLb0vvEg`
  1352 |      A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
  1353 |      
  1354 |      :dp:`fls_I71jq8BGyLqi`
  1355 |      See :s:`RawBorrowExpression`.
  1356 |    :chapter:
  1357 |      :dp:`fls_TS6DvMon5h27`
  1358 |      A :t:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
  1359 | 
  1360 | :dp:`fls_UtjWrE2qeplQ`
  1361 | An :dt:`immutable raw borrow expression` is a :t:`raw borrow expression` that has :t:`keyword` ``const``.
  1362 | 
  1363 | :dp:`fls_4e7EE4a8Yvmy`
  1364 | A :dt:`mutable raw borrow expression` is a :t:`raw borrow expression` that has :t:`keyword` ``mut``.
  1365 | 
  1366 | :dp:`fls_gOXUWePymgGV`
  1367 | When the :t:`operand` of a :t:`raw borrow expression` is a :t:`place expression`, the :t:`raw borrow expression` produces a :t:`raw pointer` to the memory location indicated by the :t:`operand`.
  1368 | 
  1369 | :dp:`fls_YBC8GrIBzZbi`
```

Glossary block (current):
```
     :dp:`fls_Fe39wLb0vvEg`
     A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
     
     :dp:`fls_I71jq8BGyLqi`
     See :s:`RawBorrowExpression`.
```

Chapter block (current):
```
     :dp:`fls_TS6DvMon5h27`
     A :t:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

```

Static glossary entry:
```

:dp:`fls_Fe39wLb0vvEg`
A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

:dp:`fls_I71jq8BGyLqi`
See :s:`RawBorrowExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_TS6DvMon5h27`
A :t:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

```

## 027 public visibility (dual)
- File: src/entities-and-resolution.rst:184
- Commit: 7f4ea487fa34478672e9c3c7cd6e239c788a1fce
- Indent: 0

Current context (10 lines before/after):
```
   174 |    
   175 |    :glossary:
   176 |      :dp:`fls_sadmsqhptlho`
   177 |      :dt:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
   178 |      which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
   179 |    :chapter:
   180 |      :dp:`fls_7kpepal8ghuj`
   181 |      :t:`Visibility` is a property of :t:`[field]s` and :t:`[item]s` that determines
   182 |      which :t:`[module]s` can refer to the :t:`name` of the :t:`field` or :t:`item`.
   183 | 
   184 | .. glossary-entry:: public visibility
   185 |    
   186 |    :glossary:
   187 |      :dp:`fls_6cfxqtl921ko`
   188 |      :dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
   189 |      to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
   190 |      :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
   191 |    :chapter:
   192 |      :dp:`fls_qo0itr5il1kk`
   193 |      :t:`Public visibility` is a kind of :t:`visibility` that allows for a :t:`name`
   194 |      to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
   195 |      :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
   196 | 
   197 | .. glossary-entry:: private visibility
   198 |    
   199 |    :glossary:
   200 |      :dp:`fls_duop22hyaweq`
   201 |      :dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
   202 |      to be referred to only by the current :t:`module` of the :t:`entity`, and its
   203 |      descendant :t:`[module]s`.
   204 |    :chapter:
   205 |      :dp:`fls_knjruq5wppv`
   206 |      :t:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
```

Glossary block (current):
```
     :dp:`fls_6cfxqtl921ko`
     :dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
     to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
     :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
```

Chapter block (current):
```
     :dp:`fls_qo0itr5il1kk`
     :t:`Public visibility` is a kind of :t:`visibility` that allows for a :t:`name`
     to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
     :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

```

Static glossary entry:
```

:dp:`fls_6cfxqtl921ko`
:dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_qo0itr5il1kk`
:t:`Public visibility` is a kind of :t:`visibility` that allows for a :t:`name`
to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
:t:`[module]s` of the related :t:`entity` can be referred to from ``M``.

```

## 028 qualifying trait (dual)
- File: src/entities-and-resolution.rst:540
- Commit: 7f4ea487fa34478672e9c3c7cd6e239c788a1fce
- Indent: 0

Current context (10 lines before/after):
```
   530 |      
   531 |      :dp:`fls_7CbNAZYSZayW`
   532 |      See :s:`TypePath`.
   533 |    :chapter:
   534 |      :dp:`fls_h2zikgmazoxx`
   535 |      A :t:`type path` is a :t:`path` that acts as a :t:`type specification`.
   536 | 
   537 | :dp:`fls_nj7s6xmzx55f`
   538 | A :t:`type path` is subject to :t:`type path resolution`.
   539 | 
   540 | .. glossary-entry:: qualifying trait
   541 |    
   542 |    :glossary:
   543 |      :dp:`fls_zKY1dWBMrqXZ`
   544 |      A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
   545 |      :t:`qualified type`.
   546 |      
   547 |      :dp:`fls_z6OeUWBnec90`
   548 |      See :s:`QualifyingTrait`.
   549 |    :chapter:
   550 |      :dp:`fls_e65q3iz50j6a`
   551 |      A :t:`qualifying trait` is a :t:`trait` that imposes a restriction on a
   552 |      :t:`qualified type`.
   553 | 
   554 | :dp:`fls_Ai1jN5a8h3Dz`
   555 | A :t:`qualifying trait` shall resolve to a :t:`trait`.
   556 | 
   557 | .. glossary-entry:: qualified type
   558 |    
   559 |    :glossary:
   560 |      :dp:`fls_e7YyZXOFo6ei`
   561 |      A :dt:`qualified type` is a :t:`type` that is restricted to a set of
   562 |      :t:`[implementation]s` that exhibit :t:`implementation conformance` to a
   563 |      :t:`qualifying trait`.
```

Glossary block (current):
```
     :dp:`fls_zKY1dWBMrqXZ`
     A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
     :t:`qualified type`.
     
     :dp:`fls_z6OeUWBnec90`
     See :s:`QualifyingTrait`.
```

Chapter block (current):
```
     :dp:`fls_e65q3iz50j6a`
     A :t:`qualifying trait` is a :t:`trait` that imposes a restriction on a
     :t:`qualified type`.

```

Static glossary entry:
```

:dp:`fls_zKY1dWBMrqXZ`
A :dt:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.

:dp:`fls_z6OeUWBnec90`
See :s:`QualifyingTrait`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_e65q3iz50j6a`
A :t:`qualifying trait` is a :t:`trait` that imposes a restriction on a
:t:`qualified type`.

```

## 029 private visibility (dual)
- File: src/entities-and-resolution.rst:197
- Commit: cf130665cd12450ccfd9e04b533c178a86e2b4f6
- Indent: 0

Current context (10 lines before/after):
```
   187 |      :dp:`fls_6cfxqtl921ko`
   188 |      :dt:`Public visibility` is a kind of :t:`visibility` that allows a :t:`name`
   189 |      to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
   190 |      :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
   191 |    :chapter:
   192 |      :dp:`fls_qo0itr5il1kk`
   193 |      :t:`Public visibility` is a kind of :t:`visibility` that allows for a :t:`name`
   194 |      to be referred to from arbitrary :t:`module` ``M`` as long as the ancestor
   195 |      :t:`[module]s` of the related :t:`entity` can be referred to from ``M``.
   196 | 
   197 | .. glossary-entry:: private visibility
   198 |    
   199 |    :glossary:
   200 |      :dp:`fls_duop22hyaweq`
   201 |      :dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
   202 |      to be referred to only by the current :t:`module` of the :t:`entity`, and its
   203 |      descendant :t:`[module]s`.
   204 |    :chapter:
   205 |      :dp:`fls_knjruq5wppv`
   206 |      :t:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
   207 |      to be referred to only by the current :t:`module` of the :t:`entity`, and its
   208 |      descendant :t:`[module]s`.
   209 | 
   210 | .. glossary-entry:: visibility modifier
   211 |    
   212 |    :glossary:
   213 |      :dp:`fls_ze7befho4jhs`
   214 |      A :dt:`visibility modifier` sets the :t:`visibility` of the :t:`name` of an
   215 |      :t:`item`.
   216 |    :chapter:
   217 |      :dp:`fls_t7i4n19qdgn4`
   218 |      A :t:`visibility modifier` sets the :t:`visibility` of a :t:`name`.
   219 | 
```

Glossary block (current):
```
     :dp:`fls_duop22hyaweq`
     :dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
     to be referred to only by the current :t:`module` of the :t:`entity`, and its
     descendant :t:`[module]s`.
```

Chapter block (current):
```
     :dp:`fls_knjruq5wppv`
     :t:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
     to be referred to only by the current :t:`module` of the :t:`entity`, and its
     descendant :t:`[module]s`.

```

Static glossary entry:
```

:dp:`fls_duop22hyaweq`
:dt:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_knjruq5wppv`
:t:`Private visibility` is a kind of :t:`visibility` that allows a :t:`name`
to be referred to only by the current :t:`module` of the :t:`entity`, and its
descendant :t:`[module]s`.

```

## 030 prelude (dual)
- File: src/entities-and-resolution.rst:1234
- Commit: cf130665cd12450ccfd9e04b533c178a86e2b4f6
- Indent: 0

Current context (10 lines before/after):
```
  1224 | * :dp:`fls_3np518s1su4w`
  1225 |   :t:`[Union field]s`.
  1226 | 
  1227 | .. _fls_ld0ize96cm6m:
  1228 | 
  1229 | Preludes
  1230 | --------
  1231 | 
  1232 | .. rubric:: Legality Rules
  1233 | 
  1234 | .. glossary-entry:: prelude
  1235 |    
  1236 |    :glossary:
  1237 |      :dp:`fls_D0PJioOZjKNN`
  1238 |      A :dt:`prelude` is a collection of :t:`entities <entity>` that are
  1239 |      automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.
  1240 |    :chapter:
  1241 |      :dp:`fls_po4gw6t2ptwu`
  1242 |      A :t:`prelude` is a collection of :t:`entities <entity>` that are automatically
  1243 |      brought :t:`in scope` of every :t:`module` in a :t:`crate`. Such
  1244 |      :t:`entities <entity>` are referred to as
  1245 |      :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
  1246 |      is referred to as a :t:`prelude name`.
  1247 | 
  1248 | .. glossary-entry:: prelude entity
  1249 |    
  1250 |    :glossary:
  1251 |      :dp:`fls_2lU7RUjzFlsz`
  1252 |      A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
  1253 | 
  1254 | .. glossary-entry:: prelude name
  1255 |    
  1256 |    :glossary:
  1257 |      :dp:`fls_6Jk7fUAK122A`
```

Glossary block (current):
```
     :dp:`fls_D0PJioOZjKNN`
     A :dt:`prelude` is a collection of :t:`entities <entity>` that are
     automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.
```

Chapter block (current):
```
     :dp:`fls_po4gw6t2ptwu`
     A :t:`prelude` is a collection of :t:`entities <entity>` that are automatically
     brought :t:`in scope` of every :t:`module` in a :t:`crate`. Such
     :t:`entities <entity>` are referred to as
     :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
     is referred to as a :t:`prelude name`.

```

Static glossary entry:
```

:dp:`fls_D0PJioOZjKNN`
A :dt:`prelude` is a collection of :t:`entities <entity>` that are
automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_po4gw6t2ptwu`
A :t:`prelude` is a collection of :t:`entities <entity>` that are automatically
brought :t:`in scope` of every :t:`module` in a :t:`crate`. Such
:t:`entities <entity>` are referred to as
:t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
is referred to as a :t:`prelude name`.

```

## 031 path (dual)
- File: src/entities-and-resolution.rst:404
- Commit: cee165a9aacc28c14a1f74f573d44a90537d0dab
- Indent: 0

Current context (10 lines before/after):
```
   394 |        PathSegment $$::$$? (GenericArgumentList | QualifiedFnTrait)?
   395 | 
   396 |    QualifiedFnTrait ::=
   397 |        $$($$ TypeSpecificationList? $$)$$ ReturnType?
   398 | 
   399 |    QualifiedTypePath ::=
   400 |        QualifiedType ($$::$$ TypePathSegment)+
   401 | 
   402 | .. rubric:: Legality Rules
   403 | 
   404 | .. glossary-entry:: path
   405 |    
   406 |    :glossary:
   407 |      :dp:`fls_u3jyud6mhy1f`
   408 |      A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
   409 |      :dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
   410 |    :chapter:
   411 |      :dp:`fls_klcltwcwrw6i`
   412 |      A :t:`path` is a sequence of :t:`[path segment]s` logically separated by
   413 |      :t:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
   414 | 
   415 | .. glossary-entry:: path segment
   416 |    
   417 |    :glossary:
   418 |      :dp:`fls_gsumebjc2bsp`
   419 |      A :dt:`path segment` is a constituent of a :t:`path`.
   420 |      
   421 |      :dp:`fls_m067uq7fo66i`
   422 |      See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.
   423 |    :chapter:
   424 |      :dp:`fls_y1z7kougmahd`
```

Glossary block (current):
```
     :dp:`fls_u3jyud6mhy1f`
     A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
     :dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
```

Chapter block (current):
```
     :dp:`fls_klcltwcwrw6i`
     A :t:`path` is a sequence of :t:`[path segment]s` logically separated by
     :t:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

```

Static glossary entry:
```

:dp:`fls_u3jyud6mhy1f`
A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_klcltwcwrw6i`
A :t:`path` is a sequence of :t:`[path segment]s` logically separated by
:t:`namespace qualifier` ``::`` that resolves to an :t:`entity`.

```

## 032 path segment (dual)
- File: src/entities-and-resolution.rst:415
- Commit: cee165a9aacc28c14a1f74f573d44a90537d0dab
- Indent: 0

Current context (10 lines before/after):
```
   405 |    
   406 |    :glossary:
   407 |      :dp:`fls_u3jyud6mhy1f`
   408 |      A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by
   409 |      :dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
   410 |    :chapter:
   411 |      :dp:`fls_klcltwcwrw6i`
   412 |      A :t:`path` is a sequence of :t:`[path segment]s` logically separated by
   413 |      :t:`namespace qualifier` ``::`` that resolves to an :t:`entity`.
   414 | 
   415 | .. glossary-entry:: path segment
   416 |    
   417 |    :glossary:
   418 |      :dp:`fls_gsumebjc2bsp`
   419 |      A :dt:`path segment` is a constituent of a :t:`path`.
   420 |      
   421 |      :dp:`fls_m067uq7fo66i`
   422 |      See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.
   423 |    :chapter:
   424 |      :dp:`fls_y1z7kougmahd`
   425 |      A :t:`path segment` is an element of a :t:`path`.
   426 | 
   427 | :dp:`fls_8q8nqfpSz7Ly`
   428 | A :t:`path` is subject to :t:`path resolution`.
   429 | 
   430 | :dp:`fls_opn5n5t2mo3m`
   431 | If a :t:`path segment` is expressed as either :t:`keyword` ``crate``,
   432 | :t:`keyword` ``$crate``, :t:`keyword` ``self``, or :t:`keyword` ``Self``, then
   433 | the :t:`path segment` shall be the first :t:`path segment` of a :t:`path`.
   434 | 
   435 | :dp:`fls_774uryecc2sx`
   436 | A :t:`path` that starts with a :t:`path segment` that is expressed as
```

Glossary block (current):
```
     :dp:`fls_gsumebjc2bsp`
     A :dt:`path segment` is a constituent of a :t:`path`.
     
     :dp:`fls_m067uq7fo66i`
     See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.
```

Chapter block (current):
```
     :dp:`fls_y1z7kougmahd`
     A :t:`path segment` is an element of a :t:`path`.

```

Static glossary entry:
```

:dp:`fls_gsumebjc2bsp`
A :dt:`path segment` is a constituent of a :t:`path`.

:dp:`fls_m067uq7fo66i`
See :s:`PathSegment`, :s:`SimplePathSegment`, :s:`TypePathSegment`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_y1z7kougmahd`
A :t:`path segment` is an element of a :t:`path`.

```

## 033 outer attribute (dual)
- File: src/attributes.rst:70
- Commit: 6d3a2bc1710e8df4fd2a8737c1b74399bb9226ab
- Indent: 0

Current context (10 lines before/after):
```
    60 |      An :dt:`inner attribute` is an :t:`attribute` that applies to an enclosing
    61 |      :t:`item`.
    62 |      
    63 |      :dp:`fls_umkk8xwktat1`
    64 |      See :s:`InnerAttribute`.
    65 |    :chapter:
    66 |      :dp:`fls_yd0ehw5csaur`
    67 |      An :t:`inner attribute` is an :t:`attribute` that applies to an enclosing
    68 |      :t:`item`.
    69 | 
    70 | .. glossary-entry:: outer attribute
    71 |    
    72 |    :glossary:
    73 |      :dp:`fls_gffxnbilsqly`
    74 |      An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
    75 |      :t:`item`.
    76 |      
    77 |      :dp:`fls_ty6ihy6x3kf`
    78 |      See :s:`OuterAttribute`.
    79 |    :chapter:
    80 |      :dp:`fls_8o6vmzbw1b1j`
    81 |      An :t:`outer attribute` is an :t:`attribute` that applies to a subsequent
    82 |      :t:`item`.
    83 | 
    84 | .. glossary-entry:: attribute content
    85 |    
    86 |    :glossary:
    87 |      :dp:`fls_sn0GvVmM3o38`
    88 |      An :dt:`attribute content` is a :t:`construct` that provides the content of
    89 |      an :t:`attribute`.
    90 |      
    91 |      :dp:`fls_YwyrWC8fcmRm`
    92 |      See :s:`AttributeContent`.
    93 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_gffxnbilsqly`
     An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
     :t:`item`.
     
     :dp:`fls_ty6ihy6x3kf`
     See :s:`OuterAttribute`.
```

Chapter block (current):
```
     :dp:`fls_8o6vmzbw1b1j`
     An :t:`outer attribute` is an :t:`attribute` that applies to a subsequent
     :t:`item`.

```

Static glossary entry:
```

:dp:`fls_gffxnbilsqly`
An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.

:dp:`fls_ty6ihy6x3kf`
See :s:`OuterAttribute`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_8o6vmzbw1b1j`
An :t:`outer attribute` is an :t:`attribute` that applies to a subsequent
:t:`item`.

```

## 034 not configuration predicate (dual)
- File: src/attributes.rst:1052
- Commit: 6d3a2bc1710e8df4fd2a8737c1b74399bb9226ab
- Indent: 0

Current context (10 lines before/after):
```
  1042 |      See :s:`ConfigurationPredicateAny`.
  1043 |    :chapter:
  1044 |      :dp:`fls_Rp73YEE3aFdI`
  1045 |      An :t:`any configuration predicate` is a :t:`configuration predicate` that
  1046 |      models existential quantifier ANY.
  1047 | 
  1048 | :dp:`fls_m0zxktz168e0`
  1049 | An :t:`any configuration predicate` evaluates statically to ``true`` when any
  1050 | nested configuration predicate evaluates to ``true``.
  1051 | 
  1052 | .. glossary-entry:: not configuration predicate
  1053 |    
  1054 |    :glossary:
  1055 |      :dp:`fls_BVMlBterkFYq`
  1056 |      A :dt:`not configuration predicate` is a :t:`configuration predicate` that
  1057 |      negates the Boolean :t:`value` of its nested :t:`configuration predicate`.
  1058 |      
  1059 |      :dp:`fls_9j9AaNcv0VNA`
  1060 |      See :s:`ConfigurationPredicateNot`.
  1061 |    :chapter:
  1062 |      :dp:`fls_XsxeOd32JI8x`
  1063 |      A :t:`not configuration predicate` is a :t:`configuration predicate` that
  1064 |      negates the Boolean :t:`value` of its nested :t:`configuration predicate`.
  1065 | 
  1066 | :dp:`fls_tvsadfy9uibu`
  1067 | A :t:`not configuration predicate` evaluates statically to ``true`` when its
  1068 | nested configuration predicate evaluates to ``false``.
  1069 | 
  1070 | :dp:`fls_JWx8vQwl19Fu`
  1071 | :t:`Configuration predicate` :dc:`true` always evaluates statically to ``true``.
  1072 | 
  1073 | :dp:`fls_SziFAQsio0ab`
  1074 | :t:`Configuration predicate` :dc:`false` always evaluates statically to ``false``.
  1075 | 
```

Glossary block (current):
```
     :dp:`fls_BVMlBterkFYq`
     A :dt:`not configuration predicate` is a :t:`configuration predicate` that
     negates the Boolean :t:`value` of its nested :t:`configuration predicate`.
     
     :dp:`fls_9j9AaNcv0VNA`
     See :s:`ConfigurationPredicateNot`.
```

Chapter block (current):
```
     :dp:`fls_XsxeOd32JI8x`
     A :t:`not configuration predicate` is a :t:`configuration predicate` that
     negates the Boolean :t:`value` of its nested :t:`configuration predicate`.

```

Static glossary entry:
```

:dp:`fls_BVMlBterkFYq`
A :dt:`not configuration predicate` is a :t:`configuration predicate` that
negates the Boolean :t:`value` of its nested :t:`configuration predicate`.

:dp:`fls_9j9AaNcv0VNA`
See :s:`ConfigurationPredicateNot`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_XsxeOd32JI8x`
A :t:`not configuration predicate` is a :t:`configuration predicate` that
negates the Boolean :t:`value` of its nested :t:`configuration predicate`.

```

## 035 name (dual)
- File: src/entities-and-resolution.rst:36
- Commit: ec494261fe9c8659a7414bc1f5810f5381c4b303
- Indent: 0

Current context (10 lines before/after):
```
    26 |    
    27 |    :glossary:
    28 |      :dp:`fls_mdbck557k8sy`
    29 |      An :dt:`entity` is a :t:`construct` that can be referred to within program
    30 |      text, usually via a :t:`field access expression` or a :t:`path`.
    31 |    :chapter:
    32 |      :dp:`fls_x7j6wcigqt7u`
    33 |      An :t:`entity` is a :t:`construct` that can be referred to within program text,
    34 |      usually via a :t:`field access expression` or a :t:`path`.
    35 | 
    36 | .. glossary-entry:: name
    37 |    
    38 |    :glossary:
    39 |      :dp:`fls_jjpzrs38vs3y`
    40 |      A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.
    41 |      
    42 |      :dp:`fls_yrzevg5kd4bi`
    43 |      See :s:`Name`.
    44 |    :chapter:
    45 |      :dp:`fls_40d2g0hvq2il`
    46 |      A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.
    47 | 
    48 | .. glossary-entry:: declaration
    49 |    
    50 |    :glossary:
    51 |      :dp:`fls_kct7ducpli6k`
    52 |      A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
    53 |      :t:`entity`.
    54 |    :chapter:
    55 |      :dp:`fls_lcca91wjwnpx`
    56 |      A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
    57 |      :t:`entity`.
```

Glossary block (current):
```
     :dp:`fls_jjpzrs38vs3y`
     A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.
     
     :dp:`fls_yrzevg5kd4bi`
     See :s:`Name`.
```

Chapter block (current):
```
     :dp:`fls_40d2g0hvq2il`
     A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

```

Static glossary entry:
```

:dp:`fls_jjpzrs38vs3y`
A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.

:dp:`fls_yrzevg5kd4bi`
See :s:`Name`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_40d2g0hvq2il`
A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.

```

## 036 namespace (dual)
- File: src/entities-and-resolution.rst:1094
- Commit: ec494261fe9c8659a7414bc1f5810f5381c4b303
- Indent: 0

Current context (10 lines before/after):
```
  1084 | :t:`generic parameter scope` and a :t:`Self scope` into the
  1085 | :t:`scope hierarchy`.
  1086 | 
  1087 | .. _fls_dq403wq5yrs:
  1088 | 
  1089 | Namespaces
  1090 | ----------
  1091 | 
  1092 | .. rubric:: Legality Rules
  1093 | 
  1094 | .. glossary-entry:: namespace
  1095 |    
  1096 |    :glossary:
  1097 |      :dp:`fls_er8lcvnEqxa5`
  1098 |      A :dt:`namespace` is a logical grouping of :t:`[name]s` such that the
  1099 |      occurrence of a :t:`name` in one :t:`namespace` does not conflict with an
  1100 |      occurrence of the same :t:`name` in another :t:`namespace`.
  1101 |    :chapter:
  1102 |      :dp:`fls_1d4jm61qnt4l`
  1103 |      A :t:`namespace` is a logical grouping of :t:`[name]s` such that the occurrence
  1104 |      of a :t:`name` in one :t:`namespace` does not conflict with an occurrence of
  1105 |      the same :t:`name` in another :t:`namespace`.
  1106 | 
  1107 | :dp:`fls_avsua7bho205`
  1108 | :t:`[Name]s` are segregated into one of five :t:`[namespace]s` based on the
  1109 | kind of :t:`entity` the :t:`name` refers to.
  1110 | 
  1111 | :dp:`fls_9e3xeza853wx`
  1112 | A :dt:`label namespace` contains :t:`[label]s`.
  1113 | 
  1114 | :dp:`fls_w625tk3ogdui`
  1115 | A :dt:`lifetime namespace` contains the :t:`[name]s` of
  1116 | :t:`[lifetime parameter]s`.
```

Glossary block (current):
```
     :dp:`fls_er8lcvnEqxa5`
     A :dt:`namespace` is a logical grouping of :t:`[name]s` such that the
     occurrence of a :t:`name` in one :t:`namespace` does not conflict with an
     occurrence of the same :t:`name` in another :t:`namespace`.
```

Chapter block (current):
```
     :dp:`fls_1d4jm61qnt4l`
     A :t:`namespace` is a logical grouping of :t:`[name]s` such that the occurrence
     of a :t:`name` in one :t:`namespace` does not conflict with an occurrence of
     the same :t:`name` in another :t:`namespace`.

```

Static glossary entry:
```

:dp:`fls_er8lcvnEqxa5`
A :dt:`namespace` is a logical grouping of :t:`[name]s` such that the
occurrence of a :t:`name` in one :t:`namespace` does not conflict with an
occurrence of the same :t:`name` in another :t:`namespace`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_1d4jm61qnt4l`
A :t:`namespace` is a logical grouping of :t:`[name]s` such that the occurrence
of a :t:`name` in one :t:`namespace` does not conflict with an occurrence of
the same :t:`name` in another :t:`namespace`.

```

## 037 method (dual)
- File: src/associated-items.rst:289
- Commit: d6c89e6ea6fc940b9837807548bb9b4e3d8e999b
- Indent: 0

Current context (10 lines before/after):
```
   279 |      :dp:`fls_amWtS80fPtza`
   280 |      An :t:`associated trait implementation function` is an :t:`associated function`
   281 |      that appears within a :t:`trait implementation`.
   282 | 
   283 | :dp:`fls_Cu8FWrisrqz1`
   284 | Every occurrence of an :t:`impl trait type` in the :t:`return type` of an
   285 | :t:`associated trait implementation function` is equivalent to referring to the
   286 | corresponding :t:`associated trait type` of the corresponding :t:`associated
   287 | trait function`.
   288 | 
   289 | .. glossary-entry:: method
   290 |    
   291 |    :glossary:
   292 |      :dp:`fls_n4opbiofu9q6`
   293 |      A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
   294 |    :chapter:
   295 |      :dp:`fls_oy92gzxgc273`
   296 |      A :t:`method` is an :t:`associated function` with a :t:`self parameter`.
   297 | 
   298 | :dp:`fls_WXnCWfJGoQx3`
   299 | The type of a :t:`self parameter` shall be one of the following:
   300 | 
   301 | * :dp:`fls_OaszUw4IFobz`
   302 |   A :t:`type specification` resolving to the :t:`implementing type` of the
   303 |   related :t:`implementation`, or
   304 | 
   305 | * :dp:`fls_Wd2FZRomB5yn`
   306 |   ``&T`` where ``T`` is one of the :t:`[type]s` listed in this enumeration,
   307 |   or
```

Glossary block (current):
```
     :dp:`fls_n4opbiofu9q6`
     A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
```

Chapter block (current):
```
     :dp:`fls_oy92gzxgc273`
     A :t:`method` is an :t:`associated function` with a :t:`self parameter`.

```

Static glossary entry:
```

:dp:`fls_n4opbiofu9q6`
A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_oy92gzxgc273`
A :t:`method` is an :t:`associated function` with a :t:`self parameter`.

```

## 038 multi segment path (dual)
- File: src/entities-and-resolution.rst:502
- Commit: d6c89e6ea6fc940b9837807548bb9b4e3d8e999b
- Indent: 0

Current context (10 lines before/after):
```
   492 |    
   493 |    :glossary:
   494 |      :dp:`fls_Hun5BCZsqd6k`
   495 |      A :dt:`single segment path` is a :t:`path` consisting of exactly one
   496 |      :t:`path segment`.
   497 |    :chapter:
   498 |      :dp:`fls_chtj3hcfe3ap`
   499 |      A :t:`single segment path` is a :t:`path` consisting of exactly one
   500 |      :t:`path segment`.
   501 | 
   502 | .. glossary-entry:: multi segment path
   503 |    
   504 |    :glossary:
   505 |      :dp:`fls_T4Xd6W6EqPSb`
   506 |      A :dt:`multi segment path` is a :t:`path` consisting of more than one
   507 |      :t:`path segment`.
   508 |    :chapter:
   509 |      :dp:`fls_wm61yeclairz`
   510 |      A :t:`multi segment path` is a :t:`path` consisting of more than one
   511 |      :t:`path segment`.
   512 | 
   513 | .. glossary-entry:: unqualified path expression
   514 |    
   515 |    :glossary:
   516 |      :dp:`fls_9xKgP8uVsOaR`
   517 |      An :dt:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   518 |    :chapter:
   519 |      :dp:`fls_nRgjCLYZL3iX`
   520 |      An :t:`unqualified path expression` is a :t:`path expression`  without a :t:`qualified type`.
   521 | 
   522 | :dp:`fls_tvvycup09b51`
```

Glossary block (current):
```
     :dp:`fls_T4Xd6W6EqPSb`
     A :dt:`multi segment path` is a :t:`path` consisting of more than one
     :t:`path segment`.
```

Chapter block (current):
```
     :dp:`fls_wm61yeclairz`
     A :t:`multi segment path` is a :t:`path` consisting of more than one
     :t:`path segment`.

```

Static glossary entry:
```

:dp:`fls_T4Xd6W6EqPSb`
A :dt:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_wm61yeclairz`
A :t:`multi segment path` is a :t:`path` consisting of more than one
:t:`path segment`.

```

## 039 loop expression (dual)
- File: src/expressions.rst:5098
- Commit: 0be1c7edc60b50ad00fc75e381e1185cf41e4d66
- Indent: 0

Current context (10 lines before/after):
```
  5088 |        BlockExpression
  5089 | 
  5090 | .. rubric:: Legality Rules
  5091 | 
  5092 | .. glossary-entry:: loop
  5093 |    
  5094 |    :glossary:
  5095 |      :dp:`fls_omjnvxva07z2`
  5096 |      For :dt:`loop`, see :t:`loop expression`.
  5097 | 
  5098 | .. glossary-entry:: loop expression
  5099 |    
  5100 |    :glossary:
  5101 |      :dp:`fls_2yypq3m1kquj`
  5102 |      A :dt:`loop expression` is an :t:`expression` that evaluates a
  5103 |      :t:`block expression` continuously as long as some criterion holds true.
  5104 |      
  5105 |      :dp:`fls_o2dyznhq7rez`
  5106 |      See :s:`LoopExpression`.
  5107 |    :chapter:
  5108 |      :dp:`fls_y1d8kd1bdlmx`
  5109 |      A :t:`loop expression` is an :t:`expression` that evaluates a :t:`block
  5110 |      expression` continuously as long as some criterion holds true.
  5111 | 
  5112 | .. glossary-entry:: loop body
  5113 |    
  5114 |    :glossary:
  5115 |      :dp:`fls_fRWcWPeKgx9g`
  5116 |      A :dt:`loop body` is the :t:`block expression` of a :t:`loop expression`.
  5117 |      
  5118 |      :dp:`fls_vWuR2TET712r`
  5119 |      See :s:`LoopBody`.
  5120 |    :chapter:
  5121 |      :dp:`fls_BjZjuiFnPtFd`
```

Glossary block (current):
```
     :dp:`fls_2yypq3m1kquj`
     A :dt:`loop expression` is an :t:`expression` that evaluates a
     :t:`block expression` continuously as long as some criterion holds true.
     
     :dp:`fls_o2dyznhq7rez`
     See :s:`LoopExpression`.
```

Chapter block (current):
```
     :dp:`fls_y1d8kd1bdlmx`
     A :t:`loop expression` is an :t:`expression` that evaluates a :t:`block
     expression` continuously as long as some criterion holds true.

```

Static glossary entry:
```

:dp:`fls_2yypq3m1kquj`
A :dt:`loop expression` is an :t:`expression` that evaluates a
:t:`block expression` continuously as long as some criterion holds true.

:dp:`fls_o2dyznhq7rez`
See :s:`LoopExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_y1d8kd1bdlmx`
A :t:`loop expression` is an :t:`expression` that evaluates a :t:`block
expression` continuously as long as some criterion holds true.

```

## 040 loop body (dual)
- File: src/expressions.rst:5112
- Commit: 0be1c7edc60b50ad00fc75e381e1185cf41e4d66
- Indent: 0

Current context (10 lines before/after):
```
  5102 |      A :dt:`loop expression` is an :t:`expression` that evaluates a
  5103 |      :t:`block expression` continuously as long as some criterion holds true.
  5104 |      
  5105 |      :dp:`fls_o2dyznhq7rez`
  5106 |      See :s:`LoopExpression`.
  5107 |    :chapter:
  5108 |      :dp:`fls_y1d8kd1bdlmx`
  5109 |      A :t:`loop expression` is an :t:`expression` that evaluates a :t:`block
  5110 |      expression` continuously as long as some criterion holds true.
  5111 | 
  5112 | .. glossary-entry:: loop body
  5113 |    
  5114 |    :glossary:
  5115 |      :dp:`fls_fRWcWPeKgx9g`
  5116 |      A :dt:`loop body` is the :t:`block expression` of a :t:`loop expression`.
  5117 |      
  5118 |      :dp:`fls_vWuR2TET712r`
  5119 |      See :s:`LoopBody`.
  5120 |    :chapter:
  5121 |      :dp:`fls_BjZjuiFnPtFd`
  5122 |      A :t:`loop body` is the :t:`block expression` of a :t:`loop expression`.
  5123 | 
  5124 | :dp:`fls_XEc0cIkpkyzJ`
  5125 | The :t:`type` of the :t:`loop body` shall be the :t:`unit type`.
  5126 | 
  5127 | .. glossary-entry:: anonymous loop expression
  5128 |    
  5129 |    :glossary:
  5130 |      :dp:`fls_csss2a8yk52k`
  5131 |      An :dt:`anonymous loop expression` is a :t:`loop expression` without a
  5132 |      :t:`label`.
  5133 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_fRWcWPeKgx9g`
     A :dt:`loop body` is the :t:`block expression` of a :t:`loop expression`.
     
     :dp:`fls_vWuR2TET712r`
     See :s:`LoopBody`.
```

Chapter block (current):
```
     :dp:`fls_BjZjuiFnPtFd`
     A :t:`loop body` is the :t:`block expression` of a :t:`loop expression`.

```

Static glossary entry:
```

:dp:`fls_fRWcWPeKgx9g`
A :dt:`loop body` is the :t:`block expression` of a :t:`loop expression`.

:dp:`fls_vWuR2TET712r`
See :s:`LoopBody`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_BjZjuiFnPtFd`
A :t:`loop body` is the :t:`block expression` of a :t:`loop expression`.

```

## 041 literal expression (dual)
- File: src/expressions.rst:773
- Commit: c862c565cd8bd0fdb98c0ceb25de6192c61169dc
- Indent: 0

Current context (10 lines before/after):
```
   763 | 
   764 | .. rubric:: Syntax
   765 | 
   766 | .. syntax::
   767 | 
   768 |    LiteralExpression ::=
   769 |        Literal
   770 | 
   771 | .. rubric:: Legality Rules
   772 | 
   773 | .. glossary-entry:: literal expression
   774 |    
   775 |    :glossary:
   776 |      :dp:`fls_otaauusc24v5`
   777 |      A :dt:`literal expression` is an :t:`expression` that denotes a :t:`literal`.
   778 |      
   779 |      :dp:`fls_7po7zobtlhzn`
   780 |      See :s:`LiteralExpression`.
   781 |    :chapter:
   782 |      :dp:`fls_rbwwczom3agt`
   783 |      A :t:`literal expression` is an :t:`expression` that denotes a :t:`literal`.
   784 | 
   785 | :dp:`fls_w30su9x4q13r`
   786 | The :t:`type` of a :t:`literal expression` is the :t:`type` of the corresponding
   787 | :t:`literal`.
   788 | 
   789 | :dp:`fls_wdpbg5xzgmwu`
   790 | The :t:`value` of a :t:`literal expression` is the :t:`value` of the
   791 | corresponding :t:`literal`.
   792 | 
   793 | .. rubric:: Dynamic Semantics
   794 | 
```

Glossary block (current):
```
     :dp:`fls_otaauusc24v5`
     A :dt:`literal expression` is an :t:`expression` that denotes a :t:`literal`.
     
     :dp:`fls_7po7zobtlhzn`
     See :s:`LiteralExpression`.
```

Chapter block (current):
```
     :dp:`fls_rbwwczom3agt`
     A :t:`literal expression` is an :t:`expression` that denotes a :t:`literal`.

```

Static glossary entry:
```

:dp:`fls_otaauusc24v5`
A :dt:`literal expression` is an :t:`expression` that denotes a :t:`literal`.

:dp:`fls_7po7zobtlhzn`
See :s:`LiteralExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_rbwwczom3agt`
A :t:`literal expression` is an :t:`expression` that denotes a :t:`literal`.

```

## 042 lifetime parameter (dual)
- File: src/generics.rst:167
- Commit: c862c565cd8bd0fdb98c0ceb25de6192c61169dc
- Indent: 0

Current context (10 lines before/after):
```
   157 |      A :t:`constant parameter initializer` is a :t:`construct` that provides the
   158 |      default :t:`value` of its related :t:`constant parameter`.
   159 | 
   160 | :dp:`fls_p4yb8EAXlRU0`
   161 | A :t:`constant parameter initializer` shall be a :t:`constant expression`.
   162 | 
   163 | :dp:`fls_4a2qshaf5se7`
   164 | It is a static error to use a :t:`generic parameter` in the
   165 | :t:`discriminant initializer` of an :t:`enum variant`.
   166 | 
   167 | .. glossary-entry:: lifetime parameter
   168 |    
   169 |    :glossary:
   170 |      :dp:`fls_7g0iu68nrsd4`
   171 |      A :dt:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.
   172 |      
   173 |      :dp:`fls_z1wl2uiwip98`
   174 |      See :s:`LifetimeParameter`.
   175 |    :chapter:
   176 |      :dp:`fls_s0nrjwqg2wox`
   177 |      A :t:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.
   178 | 
   179 | :dp:`fls_2grtygcj8o3`
   180 | A :t:`lifetime parameter` shall not be used within a :t:`constant context`,
   181 | except for the ``'static`` :t:`lifetime`.
   182 | 
   183 | .. glossary-entry:: type parameter
   184 |    
   185 |    :glossary:
   186 |      :dp:`fls_5t6510wkb67x`
   187 |      A :dt:`type parameter` is a :t:`generic parameter` for a :t:`type`.
   188 |      
```

Glossary block (current):
```
     :dp:`fls_7g0iu68nrsd4`
     A :dt:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.
     
     :dp:`fls_z1wl2uiwip98`
     See :s:`LifetimeParameter`.
```

Chapter block (current):
```
     :dp:`fls_s0nrjwqg2wox`
     A :t:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.

```

Static glossary entry:
```

:dp:`fls_7g0iu68nrsd4`
A :dt:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.

:dp:`fls_z1wl2uiwip98`
See :s:`LifetimeParameter`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_s0nrjwqg2wox`
A :t:`lifetime parameter` is a :t:`generic parameter` for a :t:`lifetime`.

```

## 043 item scope (dual)
- File: src/entities-and-resolution.rst:815
- Commit: bc069fd463a2b1db5851cad4c7b9bb28e1eb9e4e
- Indent: 0

Current context (10 lines before/after):
```
   805 | A :t:`generic parameter` is not :t:`in scope` within nested :t:`[item]s`,
   806 | except within :t:`[associated item]s`.
   807 | 
   808 | .. _fls_m0z7omni9hp0:
   809 | 
   810 | Item Scope
   811 | ~~~~~~~~~~
   812 | 
   813 | .. rubric:: Legality Rules
   814 | 
   815 | .. glossary-entry:: item scope
   816 |    
   817 |    :glossary:
   818 |      :dp:`fls_mW7IwWGSjrl2`
   819 |      An :dt:`item scope` is a :t:`scope` for :t:`[item]s`.
   820 |    :chapter:
   821 |      :dp:`fls_p5o243hhe1y3`
   822 |      An :t:`item scope` is a :t:`scope` for :t:`[item]s`.
   823 | 
   824 | :dp:`fls_huvo0mp2i6fb`
   825 | An :t:`item` declared within the :t:`block expression` of an
   826 | :t:`expression-with-block` is :t:`in scope` within the related
   827 | :t:`block expression`.
   828 | 
   829 | :dp:`fls_x8r0oppuc1t6`
   830 | An :t:`item` declared within a :t:`module` is :t:`in scope` within the
   831 | related :t:`module`. Such an :t:`item` is not :t:`in scope` within nested
   832 | :t:`[module]s`.
   833 | 
```

Glossary block (current):
```
     :dp:`fls_mW7IwWGSjrl2`
     An :dt:`item scope` is a :t:`scope` for :t:`[item]s`.
```

Chapter block (current):
```
     :dp:`fls_p5o243hhe1y3`
     An :t:`item scope` is a :t:`scope` for :t:`[item]s`.

```

Static glossary entry:
```

:dp:`fls_mW7IwWGSjrl2`
An :dt:`item scope` is a :t:`scope` for :t:`[item]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_p5o243hhe1y3`
An :t:`item scope` is a :t:`scope` for :t:`[item]s`.

```

## 044 label scope (dual)
- File: src/entities-and-resolution.rst:841
- Commit: bc069fd463a2b1db5851cad4c7b9bb28e1eb9e4e
- Indent: 0

Current context (10 lines before/after):
```
   831 | related :t:`module`. Such an :t:`item` is not :t:`in scope` within nested
   832 | :t:`[module]s`.
   833 | 
   834 | .. _fls_769b4p8v3cwu:
   835 | 
   836 | Label Scope
   837 | ~~~~~~~~~~~
   838 | 
   839 | .. rubric:: Legality Rules
   840 | 
   841 | .. glossary-entry:: label scope
   842 |    
   843 |    :glossary:
   844 |      :dp:`fls_2H6HkQ102hVS`
   845 |      A :dt:`label scope` is a :t:`scope` for :t:`[label]s`.
   846 |    :chapter:
   847 |      :dp:`fls_96kczd4zhpco`
   848 |      A :t:`label scope` is a :t:`scope` for :t:`[label]s`.
   849 | 
   850 | :dp:`fls_8sevg1sa82h4`
   851 | A :t:`label` is :t:`in scope` within the :t:`block expression` of the related
   852 | :t:`loop expression`.
   853 | 
   854 | :dp:`fls_ep5smja1rxdv`
   855 | A :t:`label` is not :t:`in scope` within nested :t:`[async block]s`,
   856 | :t:`[closure expression]s`, :t:`[constant context]s`, and :t:`[item]s`.
   857 | 
   858 | .. glossary-entry:: Self
   859 |    
```

Glossary block (current):
```
     :dp:`fls_2H6HkQ102hVS`
     A :dt:`label scope` is a :t:`scope` for :t:`[label]s`.
```

Chapter block (current):
```
     :dp:`fls_96kczd4zhpco`
     A :t:`label scope` is a :t:`scope` for :t:`[label]s`.

```

Static glossary entry:
```

:dp:`fls_2H6HkQ102hVS`
A :dt:`label scope` is a :t:`scope` for :t:`[label]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_96kczd4zhpco`
A :t:`label scope` is a :t:`scope` for :t:`[label]s`.

```

## 045 inner attribute (dual)
- File: src/attributes.rst:56
- Commit: 59827bd9324eed4f4c29ed86c4861e79c94f3a1a
- Indent: 0

Current context (10 lines before/after):
```
    46 |    
    47 |    :glossary:
    48 |      :dp:`fls_o74rfpe6zo6a`
    49 |      An :dt:`attribute` is a general, free-form metadatum that is interpreted based
    50 |      on its name, convention, language, and tool.
    51 |    :chapter:
    52 |      :dp:`fls_rnzxj1t0hehl`
    53 |      An :t:`attribute` is a general, free-form metadatum that is interpreted based on
    54 |      its :t:`name`, convention, language, and tool.
    55 | 
    56 | .. glossary-entry:: inner attribute
    57 |    
    58 |    :glossary:
    59 |      :dp:`fls_l7kxkav42l5d`
    60 |      An :dt:`inner attribute` is an :t:`attribute` that applies to an enclosing
    61 |      :t:`item`.
    62 |      
    63 |      :dp:`fls_umkk8xwktat1`
    64 |      See :s:`InnerAttribute`.
    65 |    :chapter:
    66 |      :dp:`fls_yd0ehw5csaur`
    67 |      An :t:`inner attribute` is an :t:`attribute` that applies to an enclosing
    68 |      :t:`item`.
    69 | 
    70 | .. glossary-entry:: outer attribute
    71 |    
    72 |    :glossary:
    73 |      :dp:`fls_gffxnbilsqly`
    74 |      An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
    75 |      :t:`item`.
    76 |      
    77 |      :dp:`fls_ty6ihy6x3kf`
    78 |      See :s:`OuterAttribute`.
    79 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_l7kxkav42l5d`
     An :dt:`inner attribute` is an :t:`attribute` that applies to an enclosing
     :t:`item`.
     
     :dp:`fls_umkk8xwktat1`
     See :s:`InnerAttribute`.
```

Chapter block (current):
```
     :dp:`fls_yd0ehw5csaur`
     An :t:`inner attribute` is an :t:`attribute` that applies to an enclosing
     :t:`item`.

```

Static glossary entry:
```

:dp:`fls_l7kxkav42l5d`
An :dt:`inner attribute` is an :t:`attribute` that applies to an enclosing
:t:`item`.

:dp:`fls_umkk8xwktat1`
See :s:`InnerAttribute`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_yd0ehw5csaur`
An :t:`inner attribute` is an :t:`attribute` that applies to an enclosing
:t:`item`.

```

## 046 infinite loop expression (dual)
- File: src/expressions.rst:5272
- Commit: 59827bd9324eed4f4c29ed86c4861e79c94f3a1a
- Indent: 0

Current context (10 lines before/after):
```
  5262 |        $$loop$$ LoopBody
  5263 | 
  5264 | .. rubric:: Legality Rules
  5265 | 
  5266 | .. glossary-entry:: infinite loop
  5267 |    
  5268 |    :glossary:
  5269 |      :dp:`fls_xpm53i3rkuu0`
  5270 |      For :dt:`infinite loop`, see :t:`infinite loop expression`.
  5271 | 
  5272 | .. glossary-entry:: infinite loop expression
  5273 |    
  5274 |    :glossary:
  5275 |      :dp:`fls_mvplpa4t1f2p`
  5276 |      An :dt:`infinite loop expression` is a :t:`loop expression` that continues to
  5277 |      evaluate its :t:`loop body` indefinitely.
  5278 |      
  5279 |      :dp:`fls_2gipk6b62hme`
  5280 |      See :s:`InfiniteLoopExpression`.
  5281 |    :chapter:
  5282 |      :dp:`fls_p11qw6mtxlda`
  5283 |      An :t:`infinite loop expression` is a :t:`loop expression` that continues to
  5284 |      evaluate its :t:`loop body` indefinitely.
  5285 | 
  5286 | :dp:`fls_b314wjbv0zwe`
  5287 | The :t:`type` of an :t:`infinite loop expression` is determined as follows:
  5288 | 
  5289 | * :dp:`fls_rpedapxnv8w3`
  5290 |   If the :t:`infinite loop expression` does not contain a :t:`break expression`,
  5291 |   then the :t:`type` is the :t:`never type`.
  5292 | 
  5293 | * :dp:`fls_wf11yp1jwf53`
  5294 |   If the :t:`infinite loop expression` contains at least one
  5295 |   :t:`break expression`, then the :t:`type` is the :t:`unified type` of the
```

Glossary block (current):
```
     :dp:`fls_mvplpa4t1f2p`
     An :dt:`infinite loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` indefinitely.
     
     :dp:`fls_2gipk6b62hme`
     See :s:`InfiniteLoopExpression`.
```

Chapter block (current):
```
     :dp:`fls_p11qw6mtxlda`
     An :t:`infinite loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` indefinitely.

```

Static glossary entry:
```

:dp:`fls_mvplpa4t1f2p`
An :dt:`infinite loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` indefinitely.

:dp:`fls_2gipk6b62hme`
See :s:`InfiniteLoopExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_p11qw6mtxlda`
An :t:`infinite loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` indefinitely.

```

## 047 inert attribute (dual)
- File: src/attributes.rst:127
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
   117 |    
   118 |    :glossary:
   119 |      :dp:`fls_r8rzj8mtxtp1`
   120 |      An :dt:`active attribute` is an :t:`attribute` that is removed from the
   121 |      :t:`item` it decorates.
   122 |    :chapter:
   123 |      :dp:`fls_p4potvq7x532`
   124 |      An :t:`active attribute` is an :t:`attribute` that is removed from the :t:`item`
   125 |      it decorates.
   126 | 
   127 | .. glossary-entry:: inert attribute
   128 |    
   129 |    :glossary:
   130 |      :dp:`fls_o4e3tyjz7l1h`
   131 |      An :dt:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
   132 |      it decorates.
   133 |    :chapter:
   134 |      :dp:`fls_xk7lb2g02sy7`
   135 |      An :t:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
   136 |      it decorates.
   137 | 
   138 | :dp:`fls_q8wl7pidx2za`
   139 | The following :t:`[attribute]s` are :t:`[active attribute]s`:
   140 | 
   141 | * :dp:`fls_jottio69o9e7`
   142 |   :t:`[Attribute macro]s`.
   143 | 
   144 | * :dp:`fls_gzyx9lfi5pvd`
   145 |   :t:`Attribute` :c:`cfg`.
   146 | 
   147 | * :dp:`fls_elsfqsiqor1y`
```

Glossary block (current):
```
     :dp:`fls_o4e3tyjz7l1h`
     An :dt:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
     it decorates.
```

Chapter block (current):
```
     :dp:`fls_xk7lb2g02sy7`
     An :t:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
     it decorates.

```

Static glossary entry:
```

:dp:`fls_o4e3tyjz7l1h`
An :dt:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
it decorates.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_xk7lb2g02sy7`
An :t:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
it decorates.

```

## 048 implicitly declared entity (dual)
- File: src/entities-and-resolution.rst:122
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
   112 | 
   113 | * :dp:`fls_fup6984lxdfy`
   114 |   :t:`[Trait]s`,
   115 | 
   116 | * :dp:`fls_ji9iem1c7ekq`
   117 |   :t:`[Type alias]es`,
   118 | 
   119 | * :dp:`fls_v7w8ptbyxv9w`
   120 |   :t:`[Union type]s`.
   121 | 
   122 | .. glossary-entry:: implicitly declared entity
   123 |    
   124 |    :glossary:
   125 |      :dp:`fls_VQs1jd4Nx3qR`
   126 |      An :dt:`implicitly declared entity` is an :t:`entity` that lacks an explicit
   127 |      :t:`declaration`.
   128 |    :chapter:
   129 |      :dp:`fls_ig1l38gpy5gy`
   130 |      An :t:`implicitly declared entity` is an :t:`entity` that lacks an explicit
   131 |      :t:`declaration`. The following :t:`entities <entity>` are
   132 |      :t:`implicitly declared entities <implicitly declared entity>`:
   133 | 
   134 | * :dp:`fls_ed0t6u7fo3fi`
   135 |   :t:`[Built-in attribute]s`.
   136 | 
   137 | * :dp:`fls_gjps01c8l6aa`
   138 |   :t:`Language prelude` :t:`entities <entity>`.
   139 | 
   140 | .. _fls_jdknpu3kf865:
   141 | 
   142 | Visibility
   143 | ----------
```

Glossary block (current):
```
     :dp:`fls_VQs1jd4Nx3qR`
     An :dt:`implicitly declared entity` is an :t:`entity` that lacks an explicit
     :t:`declaration`.
```

Chapter block (current):
```
     :dp:`fls_ig1l38gpy5gy`
     An :t:`implicitly declared entity` is an :t:`entity` that lacks an explicit
     :t:`declaration`. The following :t:`entities <entity>` are
     :t:`implicitly declared entities <implicitly declared entity>`:

```

Static glossary entry:
```

:dp:`fls_VQs1jd4Nx3qR`
An :dt:`implicitly declared entity` is an :t:`entity` that lacks an explicit
:t:`declaration`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_ig1l38gpy5gy`
An :t:`implicitly declared entity` is an :t:`entity` that lacks an explicit
:t:`declaration`. The following :t:`entities <entity>` are
:t:`implicitly declared entities <implicitly declared entity>`:

```

## 049 immutable place expression (dual)
- File: src/expressions.rst:607
- Commit: d9a148b646fdf290cf100acab764502eb84d2180
- Indent: 0

Current context (10 lines before/after):
```
   597 | * :dp:`fls_ilaqmj3hc5uv`
   598 |   A :t:`path expression` that resolves to a :t:`mutable static`,
   599 | 
   600 | * :dp:`fls_m0gbw9myylv2`
   601 |   A :t:`path expression` that resolves to a :t:`mutable variable` that is not
   602 |   currently borrowed,
   603 | 
   604 | * :dp:`fls_dcm3yr3y9y0a`
   605 |   A :t:`temporary`.
   606 | 
   607 | .. glossary-entry:: immutable place expression
   608 |    
   609 |    :glossary:
   610 |      :dp:`fls_MXBEZjzBxw5Z`
   611 |      An :dt:`immutable place expression` is a :t:`place expression` whose memory
   612 |      location cannot be modified.
   613 |    :chapter:
   614 |      :dp:`fls_cPEMHZtPkctX`
   615 |      An :t:`immutable place expression` is a :t:`place expression` whose memory
   616 |      location cannot be modified. All :t:`[place expression]s` that are not
   617 |      :t:`[mutable place expression]s` are :t:`[immutable place expression]s`.
   618 | 
   619 | .. glossary-entry:: place expression context
   620 |    
   621 |    :glossary:
   622 |      :dp:`fls_fqcx8suiy5k`
   623 |      A :dt:`place expression context` is a :t:`construct` that may evaluate its
   624 |      operand as a memory location.
   625 |    :chapter:
   626 |      :dp:`fls_4vxi1ji93dxb`
   627 |      A :t:`place expression context` is a :t:`construct` that may evaluate its
   628 |      :t:`operand` as a memory location.
```

Glossary block (current):
```
     :dp:`fls_MXBEZjzBxw5Z`
     An :dt:`immutable place expression` is a :t:`place expression` whose memory
     location cannot be modified.
```

Chapter block (current):
```
     :dp:`fls_cPEMHZtPkctX`
     An :t:`immutable place expression` is a :t:`place expression` whose memory
     location cannot be modified. All :t:`[place expression]s` that are not
     :t:`[mutable place expression]s` are :t:`[immutable place expression]s`.

```

Static glossary entry:
```

:dp:`fls_MXBEZjzBxw5Z`
An :dt:`immutable place expression` is a :t:`place expression` whose memory
location cannot be modified.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_cPEMHZtPkctX`
An :t:`immutable place expression` is a :t:`place expression` whose memory
location cannot be modified. All :t:`[place expression]s` that are not
:t:`[mutable place expression]s` are :t:`[immutable place expression]s`.

```

## 050 immutable borrow expression (dual)
- File: src/expressions.rst:1255
- Commit: d9a148b646fdf290cf100acab764502eb84d2180
- Indent: 0

Current context (10 lines before/after):
```
  1245 |      operand.
  1246 |      
  1247 |      :dp:`fls_c3hydbp2exok`
  1248 |      See :s:`BorrowExpression`.
  1249 |    :chapter:
  1250 |      :dp:`fls_nnqfkl228hjx`
  1251 |      A :t:`borrow expression` is an :t:`expression` that borrows the :t:`value` of
  1252 |      its :t:`operand` and creates a :t:`reference` to the memory location of its
  1253 |      :t:`operand`.
  1254 | 
  1255 | .. glossary-entry:: immutable borrow expression
  1256 |    
  1257 |    :glossary:
  1258 |      :dp:`fls_dojod5pg4r7l`
  1259 |      An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1260 |      :t:`keyword` ``mut``.
  1261 |    :chapter:
  1262 |      :dp:`fls_r7ix8webgqlm`
  1263 |      An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1264 |      :t:`keyword` ``mut``.
  1265 | 
  1266 | .. glossary-entry:: shared borrow
  1267 |    
  1268 |    :glossary:
  1269 |      :dp:`fls_gmbskxin90zi`
  1270 |      A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
  1271 |      :t:`immutable borrow expression`.
  1272 | 
  1273 | .. glossary-entry:: mutable borrow expression
  1274 |    
  1275 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_dojod5pg4r7l`
     An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
     :t:`keyword` ``mut``.
```

Chapter block (current):
```
     :dp:`fls_r7ix8webgqlm`
     An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
     :t:`keyword` ``mut``.

```

Static glossary entry:
```

:dp:`fls_dojod5pg4r7l`
An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
:t:`keyword` ``mut``.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_r7ix8webgqlm`
An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
:t:`keyword` ``mut``.

```

## 051 global path (dual)
- File: src/entities-and-resolution.rst:445
- Commit: 90e13856aa69709b8d3aee337224a1893ce13c47
- Indent: 0

Current context (10 lines before/after):
```
   435 | :dp:`fls_774uryecc2sx`
   436 | A :t:`path` that starts with a :t:`path segment` that is expressed as
   437 | :t:`keyword` ``$crate`` shall appear only within a :t:`macro transcriber`.
   438 | 
   439 | :dp:`fls_7k88ypcgaoff`
   440 | If a :t:`path segment` is expressed as :t:`keyword` ``super``, then the
   441 | :t:`path segment` shall either be the first :t:`path segment` of a :t:`path`,
   442 | or the previous :t:`path segment` of the :t:`path` shall also be expressed as
   443 | :t:`keyword` ``super``.
   444 | 
   445 | .. glossary-entry:: global path
   446 |    
   447 |    :glossary:
   448 |      :dp:`fls_msg8jw9momfw`
   449 |      A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
   450 |      ``::``.
   451 |    :chapter:
   452 |      :dp:`fls_7kb6ltajgiou`
   453 |      A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
   454 |      ``::``.
   455 | 
   456 | .. glossary-entry:: simple path
   457 |    
   458 |    :glossary:
   459 |      :dp:`fls_db91duoug4eb`
   460 |      A :dt:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
   461 |      :t:`[identifier]s` or certain :t:`[keyword]s`.
   462 |      
   463 |      :dp:`fls_cm7ysyfrdwom`
   464 |      See :s:`SimplePath`.
   465 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_msg8jw9momfw`
     A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
     ``::``.
```

Chapter block (current):
```
     :dp:`fls_7kb6ltajgiou`
     A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
     ``::``.

```

Static glossary entry:
```

:dp:`fls_msg8jw9momfw`
A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_7kb6ltajgiou`
A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.

```

## 052 generic parameter scope (dual)
- File: src/entities-and-resolution.rst:756
- Commit: 90e13856aa69709b8d3aee337224a1893ce13c47
- Indent: 0

Current context (10 lines before/after):
```
   746 | A :t:`binding` declared outside of a :t:`const block expression` is not :t:`in
   747 | scope` within such a :t:`const block expression`.
   748 | 
   749 | .. _fls_ftphlagzd2te:
   750 | 
   751 | Generic Parameter Scope
   752 | ~~~~~~~~~~~~~~~~~~~~~~~
   753 | 
   754 | .. rubric:: Legality Rules
   755 | 
   756 | .. glossary-entry:: generic parameter scope
   757 |    
   758 |    :glossary:
   759 |      :dp:`fls_e2tICijmLkj4`
   760 |      A :dt:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
   761 |    :chapter:
   762 |      :dp:`fls_amoh8r4gghyj`
   763 |      A :t:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
   764 | 
   765 | :dp:`fls_6o38qhbna46z`
   766 | A :t:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.
   767 | 
   768 | :dp:`fls_jqevvpndxzdz`
   769 | A :t:`generic parameter` of an :t:`enum type` is :t:`in scope` within the
   770 | related :t:`[enum variant]s` and :t:`where clause`.
   771 | 
   772 | :dp:`fls_t9ztg017itkp`
   773 | A :t:`generic parameter` of a :t:`function pointer type` is :t:`in scope`
   774 | within the related :t:`type specification`.
```

Glossary block (current):
```
     :dp:`fls_e2tICijmLkj4`
     A :dt:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
```

Chapter block (current):
```
     :dp:`fls_amoh8r4gghyj`
     A :t:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.

```

Static glossary entry:
```

:dp:`fls_e2tICijmLkj4`
A :dt:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_amoh8r4gghyj`
A :t:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.

```

## 053 generic associated type (dual)
- File: src/associated-items.rst:113
- Commit: 5c37a4870b5bc04d6efb8b8ae2509a2fe02424ba
- Indent: 0

Current context (10 lines before/after):
```
   103 |      See :s:`InitializationType`.
   104 | 
   105 | :dp:`fls_w8nu8suy7t5`
   106 | An :t:`associated type` shall not be used in the :t:`path expression` of a
   107 | :t:`struct expression`.
   108 | 
   109 | :dp:`fls_wasocqdnuzd1`
   110 | An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
   111 | :t:`associated trait type`.
   112 | 
   113 | .. glossary-entry:: generic associated type
   114 |    
   115 |    :glossary:
   116 |      :dp:`fls_O4wckPZPmree`
   117 |      A :dt:`generic associated type` is an :t:`associated type` with
   118 |      :t:`[generic parameter]s`.
   119 |    :chapter:
   120 |      :dp:`fls_PeD0DzjK57be`
   121 |      A :t:`generic associated type` is an :t:`associated type` with
   122 |      :t:`[generic parameter]s`.
   123 | 
   124 | :dp:`fls_3foYUch29ZtF`
   125 | A :t:`lifetime parameter` of a :t:`generic associated type` requires a
   126 | :t:`bound` of the form ``T: 'lifetime``, where ``T`` is a :t:`type parameter`
   127 | or :c:`Self` and ``'lifetime`` is the :t:`lifetime parameter`, when
   128 | 
   129 | * :dp:`fls_SnQc0zZS57Cz`
   130 |   The :t:`generic associated type` is used in an :t:`associated function` of
   131 |   the same :t:`trait`, and
   132 | 
   133 | * :dp:`fls_6Z05BK2JSzpP`
```

Glossary block (current):
```
     :dp:`fls_O4wckPZPmree`
     A :dt:`generic associated type` is an :t:`associated type` with
     :t:`[generic parameter]s`.
```

Chapter block (current):
```
     :dp:`fls_PeD0DzjK57be`
     A :t:`generic associated type` is an :t:`associated type` with
     :t:`[generic parameter]s`.

```

Static glossary entry:
```

:dp:`fls_O4wckPZPmree`
A :dt:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_PeD0DzjK57be`
A :t:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.

```

## 054 future (dual)
- File: src/concurrency.rst:167
- Commit: 5c37a4870b5bc04d6efb8b8ae2509a2fe02424ba
- Indent: 0

Current context (10 lines before/after):
```
   157 | 
   158 | Asynchronous Computation
   159 | ------------------------
   160 | 
   161 | .. rubric:: Legality Rules
   162 | 
   163 | :dp:`fls_g40xp4andj5g`
   164 | The Rust programming language provides asynchronous computation through
   165 | :t:`module` :std:`core::task` and the :std:`core::future::Future` :t:`trait`.
   166 | 
   167 | .. glossary-entry:: future
   168 |    
   169 |    :glossary:
   170 |      :dp:`fls_pvigospl4n3g`
   171 |      A :dt:`future` represents a :t:`value` of a :t:`type` that implements the
   172 |      :std:`core::future::Future` :t:`trait` which may not have finished computing
   173 |      yet.
   174 |    :chapter:
   175 |      :dp:`fls_fte085hi1yqj`
   176 |      A :t:`future` represents a :t:`value` of a :t:`type` that implements the
   177 |      :std:`core::future::Future` :t:`trait` which may not have finished computing
   178 |      yet.
   179 | 
   180 | :dp:`fls_7muubin2wn1v`
   181 | The computed :t:`value` of a :t:`future` is obtained by using an
   182 | :t:`await expression` or by invoking :std:`core::future::Future::poll`.
   183 | 
   184 | :dp:`fls_ftzey2156ha`
   185 | :std:`core::future::Future::poll` shall not be invoked on a :t:`future` that has
   186 | already returned :std:`core::task::Poll::Ready`.
```

Glossary block (current):
```
     :dp:`fls_pvigospl4n3g`
     A :dt:`future` represents a :t:`value` of a :t:`type` that implements the
     :std:`core::future::Future` :t:`trait` which may not have finished computing
     yet.
```

Chapter block (current):
```
     :dp:`fls_fte085hi1yqj`
     A :t:`future` represents a :t:`value` of a :t:`type` that implements the
     :std:`core::future::Future` :t:`trait` which may not have finished computing
     yet.

```

Static glossary entry:
```

:dp:`fls_pvigospl4n3g`
A :dt:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_fte085hi1yqj`
A :t:`future` represents a :t:`value` of a :t:`type` that implements the
:std:`core::future::Future` :t:`trait` which may not have finished computing
yet.

```

## 055 field resolution (dual)
- File: src/entities-and-resolution.rst:1666
- Commit: 200bda31f096cf2c311953ddbd51a7cbd2957307
- Indent: 0

Current context (10 lines before/after):
```
  1656 |   Otherwise the :t:`dereference type chain` continues with :t:`type`
  1657 |   :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.
  1658 | 
  1659 | .. _fls_xcwfotmq2e5d:
  1660 | 
  1661 | Field Resolution
  1662 | ~~~~~~~~~~~~~~~~
  1663 | 
  1664 | .. rubric:: Legality Rules
  1665 | 
  1666 | .. glossary-entry:: field resolution
  1667 |    
  1668 |    :glossary:
  1669 |      :dp:`fls_nL8UuclgxfGL`
  1670 |      :dt:`Field resolution` is a form of :t:`resolution` that applies to a
  1671 |      :t:`field access expression`.
  1672 |    :chapter:
  1673 |      :dp:`fls_1nxknwjdp0am`
  1674 |      :t:`Field resolution` is a form of :t:`resolution` that applies to a
  1675 |      :t:`field access expression`.
  1676 | 
  1677 | :dp:`fls_j1bip4w30q8`
  1678 | A :dt:`candidate container type` is the :t:`type` of the :t:`container operand`
  1679 | of a :t:`field access expression` :t:`under resolution`.
  1680 | 
  1681 | :dp:`fls_jrk3gzqvqr8e`
  1682 | A :dt:`candidate container type chain` is a sequence of
  1683 | :t:`[candidate container type]s`. The :t:`candidate container type chain`
  1684 | starts with the :t:`type` of the :t:`container operand` of the
  1685 | :t:`field access expression` :t:`under resolution`. From then on, the
  1686 | :t:`candidate container type chain` is treated as a
```

Glossary block (current):
```
     :dp:`fls_nL8UuclgxfGL`
     :dt:`Field resolution` is a form of :t:`resolution` that applies to a
     :t:`field access expression`.
```

Chapter block (current):
```
     :dp:`fls_1nxknwjdp0am`
     :t:`Field resolution` is a form of :t:`resolution` that applies to a
     :t:`field access expression`.

```

Static glossary entry:
```

:dp:`fls_nL8UuclgxfGL`
:dt:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_1nxknwjdp0am`
:t:`Field resolution` is a form of :t:`resolution` that applies to a
:t:`field access expression`.

```

## 056 field access expression (dual)
- File: src/expressions.rst:4775
- Commit: 200bda31f096cf2c311953ddbd51a7cbd2957307
- Indent: 0

Current context (10 lines before/after):
```
  4765 |      | NamedFieldSelector
  4766 | 
  4767 |    IndexedFieldSelector ::=
  4768 |        DecimalLiteral
  4769 | 
  4770 |    NamedFieldSelector ::=
  4771 |        Identifier
  4772 | 
  4773 | .. rubric:: Legality Rules
  4774 | 
  4775 | .. glossary-entry:: field access expression
  4776 |    
  4777 |    :glossary:
  4778 |      :dp:`fls_gdl348a04d15`
  4779 |      A :dt:`field access expression` is an :t:`expression` that accesses a
  4780 |      :t:`field` of a :t:`value`.
  4781 |      
  4782 |      :dp:`fls_luetyuwu54d6`
  4783 |      See :s:`FieldAccessExpression`.
  4784 |    :chapter:
  4785 |      :dp:`fls_hr8qvwlhd9ts`
  4786 |      A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
  4787 |      of a :t:`value`.
  4788 | 
  4789 | .. glossary-entry:: container operand
  4790 |    
  4791 |    :glossary:
  4792 |      :dp:`fls_stjmobac6wyd`
  4793 |      A :dt:`container operand` is an :t:`operand` that indicates the :t:`value`
  4794 |      whose :t:`field` is selected in a :t:`field access expression`.
  4795 |      
  4796 |      :dp:`fls_hgm1ssicc8j4`
  4797 |      See :s:`ContainerOperand`.
  4798 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_gdl348a04d15`
     A :dt:`field access expression` is an :t:`expression` that accesses a
     :t:`field` of a :t:`value`.
     
     :dp:`fls_luetyuwu54d6`
     See :s:`FieldAccessExpression`.
```

Chapter block (current):
```
     :dp:`fls_hr8qvwlhd9ts`
     A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
     of a :t:`value`.

```

Static glossary entry:
```

:dp:`fls_gdl348a04d15`
A :dt:`field access expression` is an :t:`expression` that accesses a
:t:`field` of a :t:`value`.

:dp:`fls_luetyuwu54d6`
See :s:`FieldAccessExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_hr8qvwlhd9ts`
A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
of a :t:`value`.

```

## 057 exported function (dual)
- File: src/attributes.rst:1601
- Commit: 862a461cc68af536cc2c77e242b5ceb330e641c2
- Indent: 0

Current context (10 lines before/after):
```
  1591 | 
  1592 | :dp:`fls_esaew4fqk8mm`
  1593 | :t:`Attribute` :dc:`no_mangle` indicates that the :t:`name` of the related
  1594 | :t:`function` or :t:`static` will be used as the symbol for that :t:`function`
  1595 | or :t:`static`.
  1596 | 
  1597 | :dp:`fls_lvnclpxbye9u`
  1598 | :t:`Attribute` :c:`no_mangle` causes the related :t:`function` or :t:`static` to
  1599 | be publicly exported from the produced library or object file.
  1600 | 
  1601 | .. glossary-entry:: exported function
  1602 |    
  1603 |    :glossary:
  1604 |      :dp:`fls_QotMF1iaEYod`
  1605 |      An :dt:`exported function` is an export of a :t:`function`.
  1606 |    :chapter:
  1607 |      :dp:`fls_VKuSiswPMll7`
  1608 |      An :t:`exported function` is a :t:`function` subject to :t:`attribute`
  1609 |      :c:`no_mangle`.
  1610 | 
  1611 | .. glossary-entry:: exported static
  1612 |    
  1613 |    :glossary:
  1614 |      :dp:`fls_aolCSvb349ZU`
  1615 |      An :dt:`exported static` is an export of a :t:`static`.
  1616 |    :chapter:
  1617 |      :dp:`fls_I029Rvr5BX5P`
  1618 |      An :t:`exported static` is a :t:`static` subject to :t:`attribute`
  1619 |      :c:`no_mangle`.
  1620 | 
```

Glossary block (current):
```
     :dp:`fls_QotMF1iaEYod`
     An :dt:`exported function` is an export of a :t:`function`.
```

Chapter block (current):
```
     :dp:`fls_VKuSiswPMll7`
     An :t:`exported function` is a :t:`function` subject to :t:`attribute`
     :c:`no_mangle`.

```

Static glossary entry:
```

:dp:`fls_QotMF1iaEYod`
An :dt:`exported function` is an export of a :t:`function`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_VKuSiswPMll7`
An :t:`exported function` is a :t:`function` subject to :t:`attribute`
:c:`no_mangle`.

```

## 058 exported static (dual)
- File: src/attributes.rst:1611
- Commit: 862a461cc68af536cc2c77e242b5ceb330e641c2
- Indent: 0

Current context (10 lines before/after):
```
  1601 | .. glossary-entry:: exported function
  1602 |    
  1603 |    :glossary:
  1604 |      :dp:`fls_QotMF1iaEYod`
  1605 |      An :dt:`exported function` is an export of a :t:`function`.
  1606 |    :chapter:
  1607 |      :dp:`fls_VKuSiswPMll7`
  1608 |      An :t:`exported function` is a :t:`function` subject to :t:`attribute`
  1609 |      :c:`no_mangle`.
  1610 | 
  1611 | .. glossary-entry:: exported static
  1612 |    
  1613 |    :glossary:
  1614 |      :dp:`fls_aolCSvb349ZU`
  1615 |      An :dt:`exported static` is an export of a :t:`static`.
  1616 |    :chapter:
  1617 |      :dp:`fls_I029Rvr5BX5P`
  1618 |      An :t:`exported static` is a :t:`static` subject to :t:`attribute`
  1619 |      :c:`no_mangle`.
  1620 | 
  1621 | .. rubric:: Examples
  1622 | 
  1623 | .. code-block:: rust
  1624 | 
  1625 |    #[no_mangle]
  1626 |    pub fn symbol_name() {}
  1627 | 
  1628 | .. _fls_aibb2quva4mn:
  1629 | 
  1630 | Attribute ``repr``
```

Glossary block (current):
```
     :dp:`fls_aolCSvb349ZU`
     An :dt:`exported static` is an export of a :t:`static`.
```

Chapter block (current):
```
     :dp:`fls_I029Rvr5BX5P`
     An :t:`exported static` is a :t:`static` subject to :t:`attribute`
     :c:`no_mangle`.

```

Static glossary entry:
```

:dp:`fls_aolCSvb349ZU`
An :dt:`exported static` is an export of a :t:`static`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_I029Rvr5BX5P`
An :t:`exported static` is a :t:`static` subject to :t:`attribute`
:c:`no_mangle`.

```

## 059 entity (dual)
- File: src/entities-and-resolution.rst:25
- Commit: 9a978c3837abf7f7ac0c77834d8f0ae4e52e11a5
- Indent: 0

Current context (10 lines before/after):
```
    15 | 
    16 | .. rubric:: Syntax
    17 | 
    18 | .. syntax::
    19 | 
    20 |    Name ::=
    21 |        Identifier
    22 | 
    23 | .. rubric:: Legality Rules
    24 | 
    25 | .. glossary-entry:: entity
    26 |    
    27 |    :glossary:
    28 |      :dp:`fls_mdbck557k8sy`
    29 |      An :dt:`entity` is a :t:`construct` that can be referred to within program
    30 |      text, usually via a :t:`field access expression` or a :t:`path`.
    31 |    :chapter:
    32 |      :dp:`fls_x7j6wcigqt7u`
    33 |      An :t:`entity` is a :t:`construct` that can be referred to within program text,
    34 |      usually via a :t:`field access expression` or a :t:`path`.
    35 | 
    36 | .. glossary-entry:: name
    37 |    
    38 |    :glossary:
    39 |      :dp:`fls_jjpzrs38vs3y`
    40 |      A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.
    41 |      
    42 |      :dp:`fls_yrzevg5kd4bi`
    43 |      See :s:`Name`.
    44 |    :chapter:
    45 |      :dp:`fls_40d2g0hvq2il`
```

Glossary block (current):
```
     :dp:`fls_mdbck557k8sy`
     An :dt:`entity` is a :t:`construct` that can be referred to within program
     text, usually via a :t:`field access expression` or a :t:`path`.
```

Chapter block (current):
```
     :dp:`fls_x7j6wcigqt7u`
     An :t:`entity` is a :t:`construct` that can be referred to within program text,
     usually via a :t:`field access expression` or a :t:`path`.

```

Static glossary entry:
```

:dp:`fls_mdbck557k8sy`
An :dt:`entity` is a :t:`construct` that can be referred to within program
text, usually via a :t:`field access expression` or a :t:`path`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_x7j6wcigqt7u`
An :t:`entity` is a :t:`construct` that can be referred to within program text,
usually via a :t:`field access expression` or a :t:`path`.

```

## 060 evaluation (dual)
- File: src/expressions.rst:202
- Commit: 9a978c3837abf7f7ac0c77834d8f0ae4e52e11a5
- Indent: 0

Current context (10 lines before/after):
```
   192 | :dp:`fls_2j132xueobfv`
   193 | A :t:`subject expression` is an :t:`expression` that controls :t:`[for loop]s`,
   194 | :t:`[if expression]s`, and :t:`[match expression]s`.
   195 | 
   196 | :dp:`fls_a243nclqqjlu`
   197 | A :t:`subject let expression` is an :t:`expression` that controls
   198 | :t:`[if let expression]s` and :t:`[while let loop]s`.
   199 | 
   200 | .. rubric:: Dynamic Semantics
   201 | 
   202 | .. glossary-entry:: evaluation
   203 |    
   204 |    :glossary:
   205 |      :dp:`fls_8zmtio6razl1`
   206 |      :dt:`Evaluation` is the process by which an :t:`expression` achieves its
   207 |      runtime effects.
   208 |    :chapter:
   209 |      :dp:`fls_1223lwh4nq49`
   210 |      :t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
   211 |      effects.
   212 | 
   213 | .. glossary-entry:: evaluated
   214 |    
   215 |    :glossary:
   216 |      :dp:`fls_769tm6hn9g5e`
   217 |      See :t:`evaluation`.
   218 | 
   219 | .. _fls_isyftqu120l:
   220 | 
   221 | Expression Classification
   222 | -------------------------
```

Glossary block (current):
```
     :dp:`fls_8zmtio6razl1`
     :dt:`Evaluation` is the process by which an :t:`expression` achieves its
     runtime effects.
```

Chapter block (current):
```
     :dp:`fls_1223lwh4nq49`
     :t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
     effects.

```

Static glossary entry:
```

:dp:`fls_8zmtio6razl1`
:dt:`Evaluation` is the process by which an :t:`expression` achieves its
runtime effects.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_1223lwh4nq49`
:t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
effects.

```

## 061 dereference type chain (dual)
- File: src/entities-and-resolution.rst:1639
- Commit: 869af9cc64a5433bcd5231e13ad53210e88a97ff
- Indent: 0

Current context (10 lines before/after):
```
  1629 |    
  1630 |    :glossary:
  1631 |      :dp:`fls_HfuUQ7IaoI5j`
  1632 |      A :dt:`dereference type` is either a :t:`reference type` or a :t:`type` that
  1633 |      implements the :std:`core::ops::Deref` :t:`trait`.
  1634 |    :chapter:
  1635 |      :dp:`fls_x3alg07yd7hx`
  1636 |      A :t:`dereference type` is either a :t:`reference type` or a :t:`type` that
  1637 |      implements the :std:`core::ops::Deref` :t:`trait`.
  1638 | 
  1639 | .. glossary-entry:: dereference type chain
  1640 |    
  1641 |    :glossary:
  1642 |      :dp:`fls_kIzoAEf069HE`
  1643 |      A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`.
  1644 |    :chapter:
  1645 |      :dp:`fls_4hulwazdu20i`
  1646 |      A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
  1647 |      :t:`dereference type chain` starts with an initial :t:`dereference type`. From
  1648 |      then on, the :t:`dereference type chain` continues as follows:
  1649 | 
  1650 | * :dp:`fls_ptocwx5p25lj`
  1651 |   If the previous :t:`dereference type` is a :t:`reference type`, then the
  1652 |   :t:`dereference type chain` continues with the inner :t:`type` of the
  1653 |   previous :t:`dereference type`.
  1654 | 
  1655 | * :dp:`fls_ygam5nisv98c`
  1656 |   Otherwise the :t:`dereference type chain` continues with :t:`type`
  1657 |   :std:`core::ops::Deref::Target` of the previous :t:`dereference type`.
  1658 | 
  1659 | .. _fls_xcwfotmq2e5d:
```

Glossary block (current):
```
     :dp:`fls_kIzoAEf069HE`
     A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`.
```

Chapter block (current):
```
     :dp:`fls_4hulwazdu20i`
     A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
     :t:`dereference type chain` starts with an initial :t:`dereference type`. From
     then on, the :t:`dereference type chain` continues as follows:

```

Static glossary entry:
```

:dp:`fls_kIzoAEf069HE`
A :dt:`dereference type chain` is a sequence of :t:`[dereference type]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_4hulwazdu20i`
A :t:`dereference type chain` is a sequence of :t:`[dereference type]s`. A
:t:`dereference type chain` starts with an initial :t:`dereference type`. From
then on, the :t:`dereference type chain` continues as follows:

```

## 062 diverging expression (dual)
- File: src/expressions.rst:483
- Commit: 869af9cc64a5433bcd5231e13ad53210e88a97ff
- Indent: 0

Current context (10 lines before/after):
```
   473 | The invocation of a :t:`constant function` follows the dynamic semantics of a
   474 | :t:`non-[constant function]` invocation.
   475 | 
   476 | .. _fls_zJOAmSr3Dbqk:
   477 | 
   478 | Diverging Expressions
   479 | ~~~~~~~~~~~~~~~~~~~~~
   480 | 
   481 | .. rubric:: Legality Rules
   482 | 
   483 | .. glossary-entry:: diverging expression
   484 |    
   485 |    :glossary:
   486 |      :dp:`fls_fLlNzmB34cj9`
   487 |      A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
   488 |      program flow to diverge from the normal :t:`evaluation` order.
   489 |    :chapter:
   490 |      :dp:`fls_oth9vFtcb9l4`
   491 |      A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
   492 |      program flow to diverge from the normal :t:`evaluation` order.
   493 | 
   494 | :dp:`fls_cmBVodJMjZi7`
   495 | :t:`[Diverging expression]s` are:
   496 | 
   497 | * :dp:`fls_xsOgdiIzysP1`
   498 |   :t:`[Break expression]s`,
   499 | 
   500 | * :dp:`fls_xqxdHziqgWf5`
   501 |   :t:`[Return expression]s`,
   502 | 
   503 | * :dp:`fls_fU91m6DCB0ip`
```

Glossary block (current):
```
     :dp:`fls_fLlNzmB34cj9`
     A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
     program flow to diverge from the normal :t:`evaluation` order.
```

Chapter block (current):
```
     :dp:`fls_oth9vFtcb9l4`
     A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
     program flow to diverge from the normal :t:`evaluation` order.

```

Static glossary entry:
```

:dp:`fls_fLlNzmB34cj9`
A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_oth9vFtcb9l4`
A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
program flow to diverge from the normal :t:`evaluation` order.

```

## 063 data race (dual)
- File: src/concurrency.rst:17
- Commit: 441f3fd3c0241e9e5d92b270603f7d9aa8e30195
- Indent: 0

Current context (10 lines before/after):
```
     7 | 
     8 | Concurrency
     9 | ===========
    10 | 
    11 | :dp:`fls_opt7v0mopxc8`
    12 | The Rust programming language provides features for concurrent programming
    13 | without :t:`[data race]s`, whose rules are presented in this chapter.
    14 | 
    15 | .. rubric:: Legality Rules
    16 | 
    17 | .. glossary-entry:: data race
    18 |    
    19 |    :glossary:
    20 |      :dp:`fls_v2s1b57e3r7n`
    21 |      A :dt:`data race` is a scenario where two or more threads access a shared
    22 |      memory location concurrently.
    23 |    :chapter:
    24 |      :dp:`fls_tx4b8r6i93n4`
    25 |      A :t:`data race` is a scenario where two or more threads access a shared memory
    26 |      location concurrently without any synchronization, where one of the accesses is
    27 |      a modification.
    28 |      
    29 |      .. rubric:: Undefined Behavior
    30 | 
    31 | :dp:`fls_isypweqewe78`
    32 | It is undefined behavior if two or more threads engage in a :t:`data race`.
    33 | 
    34 | .. _fls_eiw4by8z75di:
    35 | 
    36 | Send and Sync
    37 | -------------
    38 | 
    39 | .. rubric:: Legality Rules
    40 | 
```

Glossary block (current):
```
     :dp:`fls_v2s1b57e3r7n`
     A :dt:`data race` is a scenario where two or more threads access a shared
     memory location concurrently.
```

Chapter block (current):
```
     :dp:`fls_tx4b8r6i93n4`
     A :t:`data race` is a scenario where two or more threads access a shared memory
     location concurrently without any synchronization, where one of the accesses is
     a modification.
     
     .. rubric:: Undefined Behavior

```

Static glossary entry:
```

:dp:`fls_v2s1b57e3r7n`
A :dt:`data race` is a scenario where two or more threads access a shared
memory location concurrently.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_tx4b8r6i93n4`
A :t:`data race` is a scenario where two or more threads access a shared memory
location concurrently without any synchronization, where one of the accesses is
a modification.

.. rubric:: Undefined Behavior

```

## 064 declaration (dual)
- File: src/entities-and-resolution.rst:48
- Commit: 441f3fd3c0241e9e5d92b270603f7d9aa8e30195
- Indent: 0

Current context (10 lines before/after):
```
    38 |    :glossary:
    39 |      :dp:`fls_jjpzrs38vs3y`
    40 |      A :dt:`name` is an :t:`identifier` that refers to an :t:`entity`.
    41 |      
    42 |      :dp:`fls_yrzevg5kd4bi`
    43 |      See :s:`Name`.
    44 |    :chapter:
    45 |      :dp:`fls_40d2g0hvq2il`
    46 |      A :t:`name` is an :t:`identifier` that refers to an :t:`entity`.
    47 | 
    48 | .. glossary-entry:: declaration
    49 |    
    50 |    :glossary:
    51 |      :dp:`fls_kct7ducpli6k`
    52 |      A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
    53 |      :t:`entity`.
    54 |    :chapter:
    55 |      :dp:`fls_lcca91wjwnpx`
    56 |      A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
    57 |      :t:`entity`.
    58 | 
    59 | .. glossary-entry:: explicitly declared entity
    60 |    
    61 |    :glossary:
    62 |      :dp:`fls_shpNJ0JCSCwa`
    63 |      An :dt:`explicitly declared entity` is an :t:`entity` that has a
    64 |      :t:`declaration`.
    65 |    :chapter:
    66 |      :dp:`fls_94l2d7ti0hjw`
    67 |      An :t:`explicitly declared entity` is an :t:`entity` that has a
    68 |      :t:`declaration`. The following :t:`entities <entity>` are
```

Glossary block (current):
```
     :dp:`fls_kct7ducpli6k`
     A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
     :t:`entity`.
```

Chapter block (current):
```
     :dp:`fls_lcca91wjwnpx`
     A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
     :t:`entity`.

```

Static glossary entry:
```

:dp:`fls_kct7ducpli6k`
A :dt:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_lcca91wjwnpx`
A :t:`declaration` is a :t:`construct` that introduces a :t:`name` for an
:t:`entity`.

```

## 065 configuration predicate (dual)
- File: src/attributes.rst:1001
- Commit: 7a54fff856ad2552c39e0671562f762f893cbbde
- Indent: 0

Current context (10 lines before/after):
```
   991 |        $$not$$ $$($$ ConfigurationPredicate $$)$$
   992 | 
   993 |    ConfigurationPredicateList ::=
   994 |        ConfigurationPredicate ($$,$$ ConfigurationPredicate)* $$,$$?
   995 | 
   996 | .. rubric:: Legality Rules
   997 | 
   998 | :dp:`fls_xrjp7xw9jutz`
   999 | :t:`Attribute` :dc:`cfg` enables :t:`conditional compilation`.
  1000 | 
  1001 | .. glossary-entry:: configuration predicate
  1002 |    
  1003 |    :glossary:
  1004 |      :dp:`fls_TyKIUQMxO9Si`
  1005 |      A :dt:`configuration predicate` is a :t:`construct` that evaluates statically
  1006 |      to either ``true`` or ``false``, and controls :t:`conditional compilation`.
  1007 |      
  1008 |      :dp:`fls_99ioki0M64fD`
  1009 |      See :s:`ConfigurationPredicate`.
  1010 |    :chapter:
  1011 |      :dp:`fls_l96kyix5xsof`
  1012 |      A :t:`configuration predicate` is a :t:`construct` that evaluates statically
  1013 |      to either ``true`` or ``false``, and controls :t:`conditional compilation`.
  1014 | 
  1015 | .. glossary-entry:: all configuration predicate
  1016 |    
  1017 |    :glossary:
  1018 |      :dp:`fls_IyMZWiTnkYPv`
  1019 |      An :dt:`all configuration predicate` is a :t:`configuration predicate` that
  1020 |      models existential quantifier ALL.
  1021 |      
  1022 |      :dp:`fls_0fEw9Bx8xX8q`
  1023 |      See :s:`ConfigurationPredicateAll`.
  1024 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_TyKIUQMxO9Si`
     A :dt:`configuration predicate` is a :t:`construct` that evaluates statically
     to either ``true`` or ``false``, and controls :t:`conditional compilation`.
     
     :dp:`fls_99ioki0M64fD`
     See :s:`ConfigurationPredicate`.
```

Chapter block (current):
```
     :dp:`fls_l96kyix5xsof`
     A :t:`configuration predicate` is a :t:`construct` that evaluates statically
     to either ``true`` or ``false``, and controls :t:`conditional compilation`.

```

Static glossary entry:
```

:dp:`fls_TyKIUQMxO9Si`
A :dt:`configuration predicate` is a :t:`construct` that evaluates statically
to either ``true`` or ``false``, and controls :t:`conditional compilation`.

:dp:`fls_99ioki0M64fD`
See :s:`ConfigurationPredicate`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_l96kyix5xsof`
A :t:`configuration predicate` is a :t:`construct` that evaluates statically
to either ``true`` or ``false``, and controls :t:`conditional compilation`.

```

## 066 constant expression (dual)
- File: src/expressions.rst:272
- Commit: 7a54fff856ad2552c39e0671562f762f893cbbde
- Indent: 0

Current context (10 lines before/after):
```
   262 | :t:`[Parenthesized expression]s` are allowed to appear anywhere in
   263 | :t:`[assignee expression]s`.
   264 | 
   265 | .. _fls_66m4rnbssgig:
   266 | 
   267 | Constant Expressions
   268 | ~~~~~~~~~~~~~~~~~~~~
   269 | 
   270 | .. rubric:: Legality Rules
   271 | 
   272 | .. glossary-entry:: constant expression
   273 |    
   274 |    :glossary:
   275 |      :dp:`fls_rmn8w4rh3juf`
   276 |      A :dt:`constant expression` is an :t:`expression` that can be evaluated
   277 |      statically.
   278 |    :chapter:
   279 |      :dp:`fls_1ji7368ieg0b`
   280 |      A :t:`constant expression` is an :t:`expression` that can be evaluated
   281 |      statically. The following :t:`[construct]s` are :t:`[constant expression]s` as
   282 |      long as their :t:`[operand]s` are also :t:`[constant expression]s` and do not
   283 |      involve :t:`[type]s` that require :t:`destruction`:
   284 | 
   285 | * :dp:`fls_y6ore0iwx7e0`
   286 |   :t:`[Arithmetic expression]s` of :t:`[scalar type]s`,
   287 | 
   288 | * :dp:`fls_xguga84v3j8u`
   289 |   :t:`[Array expression]s`,
   290 | 
   291 | * :dp:`fls_idxf02p7jogu`
   292 |   :t:`[Assignment expression]s`,
   293 | 
   294 | * :dp:`fls_6z45ss502alt`
```

Glossary block (current):
```
     :dp:`fls_rmn8w4rh3juf`
     A :dt:`constant expression` is an :t:`expression` that can be evaluated
     statically.
```

Chapter block (current):
```
     :dp:`fls_1ji7368ieg0b`
     A :t:`constant expression` is an :t:`expression` that can be evaluated
     statically. The following :t:`[construct]s` are :t:`[constant expression]s` as
     long as their :t:`[operand]s` are also :t:`[constant expression]s` and do not
     involve :t:`[type]s` that require :t:`destruction`:

```

Static glossary entry:
```

:dp:`fls_rmn8w4rh3juf`
A :dt:`constant expression` is an :t:`expression` that can be evaluated
statically.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_1ji7368ieg0b`
A :t:`constant expression` is an :t:`expression` that can be evaluated
statically. The following :t:`[construct]s` are :t:`[constant expression]s` as
long as their :t:`[operand]s` are also :t:`[constant expression]s` and do not
involve :t:`[type]s` that require :t:`destruction`:

```

## 067 call resolution (dual)
- File: src/entities-and-resolution.rst:1901
- Commit: 00dc1831813a3212fa587b2ab379dae2b23ed81a
- Indent: 0

Current context (10 lines before/after):
```
  1891 | :dp:`fls_jw2yv23cduu4`
  1892 | A :t:`method call expression` shall resolve to exactly one :t:`method`.
  1893 | 
  1894 | .. _fls_TelBKNKodx3d:
  1895 | 
  1896 | Call Resolution
  1897 | ~~~~~~~~~~~~~~~
  1898 | 
  1899 | .. rubric:: Legality Rules
  1900 | 
  1901 | .. glossary-entry:: call resolution
  1902 |    
  1903 |    :glossary:
  1904 |      :dp:`fls_fS1ZjGGypvbn`
  1905 |      :dt:`Call resolution` is a kind of :t:`resolution` that applies to a
  1906 |      :t:`call expression`.
  1907 |    :chapter:
  1908 |      :dp:`fls_ZjJ7y9r6QQMW`
  1909 |      :t:`Call resolution` is a form of :t:`resolution` that applies to a
  1910 |      :t:`call expression`.
  1911 | 
  1912 | :dp:`fls_zBSloU2Gjv7x`
  1913 | A :dt:`candidate callee type` is the :t:`type` of the :t:`call operand`
  1914 | of a :t:`call expression` :t:`under resolution`.
  1915 | 
  1916 | :dp:`fls_XBakDylF7aOG`
  1917 | A :dt:`candidate callee type chain` is a sequence of :t:`[candidate callee type]s`.
  1918 | The :t:`candidate callee type chain` starts with the :t:`type` of the :t:`call
  1919 | operand` of the:t:`call expression` :t:`under resolution`. From then on, the
  1920 | :t:`candidate callee type chain` is treated as a :t:`dereference type chain`.
  1921 | 
```

Glossary block (current):
```
     :dp:`fls_fS1ZjGGypvbn`
     :dt:`Call resolution` is a kind of :t:`resolution` that applies to a
     :t:`call expression`.
```

Chapter block (current):
```
     :dp:`fls_ZjJ7y9r6QQMW`
     :t:`Call resolution` is a form of :t:`resolution` that applies to a
     :t:`call expression`.

```

Static glossary entry:
```

:dp:`fls_fS1ZjGGypvbn`
:dt:`Call resolution` is a kind of :t:`resolution` that applies to a
:t:`call expression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_ZjJ7y9r6QQMW`
:t:`Call resolution` is a form of :t:`resolution` that applies to a
:t:`call expression`.

```

## 068 comparison expression (dual)
- File: src/expressions.rst:2369
- Commit: 00dc1831813a3212fa587b2ab379dae2b23ed81a
- Indent: 0

Current context (10 lines before/after):
```
  2359 |        LeftOperand $$<$$ RightOperand
  2360 | 
  2361 |    LessThanOrEqualsExpression ::=
  2362 |        LeftOperand $$<=$$ RightOperand
  2363 | 
  2364 |    NotEqualsExpression ::=
  2365 |        LeftOperand $$!=$$ RightOperand
  2366 | 
  2367 | .. rubric:: Legality Rules
  2368 | 
  2369 | .. glossary-entry:: comparison expression
  2370 |    
  2371 |    :glossary:
  2372 |      :dp:`fls_394p7gdruvk7`
  2373 |      A :dt:`comparison expression` is an :t:`expression` that compares the
  2374 |      :t:`[value]s` of two :t:`[operand]s`.
  2375 |      
  2376 |      :dp:`fls_1jk0s7389mt0`
  2377 |      See :s:`ComparisonExpression`.
  2378 |    :chapter:
  2379 |      :dp:`fls_yzuceqx6nxwa`
  2380 |      A :t:`comparison expression` is an :t:`expression` that compares the
  2381 |      :t:`[value]s` of two :t:`[operand]s`.
  2382 | 
  2383 | :dp:`fls_asfrqemqviad`
  2384 | A :t:`comparison expression` implicitly takes :t:`[shared borrow]s` of its
  2385 | :t:`[operand]s`.
  2386 | 
  2387 | :dp:`fls_9s4re3ujnfis`
  2388 | The :t:`type` of a :t:`comparison expression` is :t:`type` :c:`bool`.
  2389 | 
  2390 | .. glossary-entry:: equals expression
  2391 |    
  2392 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_394p7gdruvk7`
     A :dt:`comparison expression` is an :t:`expression` that compares the
     :t:`[value]s` of two :t:`[operand]s`.
     
     :dp:`fls_1jk0s7389mt0`
     See :s:`ComparisonExpression`.
```

Chapter block (current):
```
     :dp:`fls_yzuceqx6nxwa`
     A :t:`comparison expression` is an :t:`expression` that compares the
     :t:`[value]s` of two :t:`[operand]s`.

```

Static glossary entry:
```

:dp:`fls_394p7gdruvk7`
A :dt:`comparison expression` is an :t:`expression` that compares the
:t:`[value]s` of two :t:`[operand]s`.

:dp:`fls_1jk0s7389mt0`
See :s:`ComparisonExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_yzuceqx6nxwa`
A :t:`comparison expression` is an :t:`expression` that compares the
:t:`[value]s` of two :t:`[operand]s`.

```

## 069 built-in attribute (dual)
- File: src/attributes.rst:218
- Commit: 98e97a8daf186436df9b7b6622aab89132b9697a
- Indent: 0

Current context (10 lines before/after):
```
   208 |      | TargetFeatureContent
   209 |      | TestContent
   210 |      | TrackCallerContent
   211 |      | TypeLengthLimitContent
   212 |      | UnsafeContent
   213 |      | UsedContent
   214 |      | WindowsSubsystemContent
   215 | 
   216 | .. rubric:: Legality Rules
   217 | 
   218 | .. glossary-entry:: built-in attribute
   219 |    
   220 |    :glossary:
   221 |      :dp:`fls_a40rclur4orm`
   222 |      A :dt:`built-in attribute` is a language-defined :t:`attribute`.
   223 |      
   224 |      :dp:`fls_ooq5g8zffyfb`
   225 |      See :s:`InnerBuiltinAttribute`, :s:`OuterBuiltinAttribute`.
   226 |    :chapter:
   227 |      :dp:`fls_92tqo8uas8kd`
   228 |      A :t:`built-in attribute` is a language-defined :t:`attribute`.
   229 | 
   230 | :dp:`fls_bxucstrfcco8`
   231 | The following :t:`[built-in attribute]s` are :dt:`[code generation attribute]s`:
   232 | 
   233 | * :dp:`fls_wle815gb9ai2`
   234 |   :t:`Attribute` :c:`cold`.
   235 | 
   236 | * :dp:`fls_tvn08dtuilue`
   237 |   :t:`Attribute` :c:`inline`.
   238 | 
   239 | * :dp:`fls_eOJS3mxa9xgu`
```

Glossary block (current):
```
     :dp:`fls_a40rclur4orm`
     A :dt:`built-in attribute` is a language-defined :t:`attribute`.
     
     :dp:`fls_ooq5g8zffyfb`
     See :s:`InnerBuiltinAttribute`, :s:`OuterBuiltinAttribute`.
```

Chapter block (current):
```
     :dp:`fls_92tqo8uas8kd`
     A :t:`built-in attribute` is a language-defined :t:`attribute`.

```

Static glossary entry:
```

:dp:`fls_a40rclur4orm`
A :dt:`built-in attribute` is a language-defined :t:`attribute`.

:dp:`fls_ooq5g8zffyfb`
See :s:`InnerBuiltinAttribute`, :s:`OuterBuiltinAttribute`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_92tqo8uas8kd`
A :t:`built-in attribute` is a language-defined :t:`attribute`.

```

## 070 borrow expression (dual)
- File: src/expressions.rst:1239
- Commit: 98e97a8daf186436df9b7b6622aab89132b9697a
- Indent: 0

Current context (10 lines before/after):
```
  1229 | 
  1230 | .. rubric:: Syntax
  1231 | 
  1232 | .. syntax::
  1233 | 
  1234 |    BorrowExpression ::=
  1235 |        $$&$$ $$mut$$? Operand
  1236 | 
  1237 | .. rubric:: Legality Rules
  1238 | 
  1239 | .. glossary-entry:: borrow expression
  1240 |    
  1241 |    :glossary:
  1242 |      :dp:`fls_2f55piwg78ru`
  1243 |      A :dt:`borrow expression` is an :t:`expression` that borrows the :t:`value`
  1244 |      of its :t:`operand` and creates a :t:`reference` to the memory location of its
  1245 |      operand.
  1246 |      
  1247 |      :dp:`fls_c3hydbp2exok`
  1248 |      See :s:`BorrowExpression`.
  1249 |    :chapter:
  1250 |      :dp:`fls_nnqfkl228hjx`
  1251 |      A :t:`borrow expression` is an :t:`expression` that borrows the :t:`value` of
  1252 |      its :t:`operand` and creates a :t:`reference` to the memory location of its
  1253 |      :t:`operand`.
  1254 | 
  1255 | .. glossary-entry:: immutable borrow expression
  1256 |    
  1257 |    :glossary:
  1258 |      :dp:`fls_dojod5pg4r7l`
  1259 |      An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1260 |      :t:`keyword` ``mut``.
  1261 |    :chapter:
  1262 |      :dp:`fls_r7ix8webgqlm`
  1263 |      An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1264 |      :t:`keyword` ``mut``.
```

Glossary block (current):
```
     :dp:`fls_2f55piwg78ru`
     A :dt:`borrow expression` is an :t:`expression` that borrows the :t:`value`
     of its :t:`operand` and creates a :t:`reference` to the memory location of its
     operand.
     
     :dp:`fls_c3hydbp2exok`
     See :s:`BorrowExpression`.
```

Chapter block (current):
```
     :dp:`fls_nnqfkl228hjx`
     A :t:`borrow expression` is an :t:`expression` that borrows the :t:`value` of
     its :t:`operand` and creates a :t:`reference` to the memory location of its
     :t:`operand`.

```

Static glossary entry:
```

:dp:`fls_2f55piwg78ru`
A :dt:`borrow expression` is an :t:`expression` that borrows the :t:`value`
of its :t:`operand` and creates a :t:`reference` to the memory location of its
operand.

:dp:`fls_c3hydbp2exok`
See :s:`BorrowExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_nnqfkl228hjx`
A :t:`borrow expression` is an :t:`expression` that borrows the :t:`value` of
its :t:`operand` and creates a :t:`reference` to the memory location of its
:t:`operand`.

```

## 071 binding scope (dual)
- File: src/entities-and-resolution.rst:711
- Commit: 48ae27979c3ba216ba39d0e1bd634784063db0d2
- Indent: 0

Current context (10 lines before/after):
```
   701 |      :dp:`fls_sy380geqvf2l`
   702 |      A :t:`name` is :dt:`in scope` when it can be referred to.
   703 | 
   704 | .. _fls_6ozthochxz1i:
   705 | 
   706 | Binding Scopes
   707 | ~~~~~~~~~~~~~~
   708 | 
   709 | .. rubric:: Legality Rules
   710 | 
   711 | .. glossary-entry:: binding scope
   712 |    
   713 |    :glossary:
   714 |      :dp:`fls_6qPYH5NJ8usI`
   715 |      A :dt:`binding scope` is a :t:`scope` for :t:`[binding]s`.
   716 |    :chapter:
   717 |      :dp:`fls_ncg9etb3x7k0`
   718 |      A :t:`binding scope` is a :t:`scope` for :t:`[binding]s`.
   719 | 
   720 | :dp:`fls_u52mx4xw8zod`
   721 | The :t:`binding` of a :t:`closure parameter` is :t:`in scope` within the
   722 | related :t:`closure body`.
   723 | 
   724 | :dp:`fls_t9mk8kasobea`
   725 | The :t:`binding` of a :t:`function parameter` is :t:`in scope` within the
   726 | related :t:`function body`.
   727 | 
   728 | :dp:`fls_h9cvs854ae34`
   729 | The :t:`binding` of a :t:`for loop` or a :t:`while let loop` is :t:`in scope`
```

Glossary block (current):
```
     :dp:`fls_6qPYH5NJ8usI`
     A :dt:`binding scope` is a :t:`scope` for :t:`[binding]s`.
```

Chapter block (current):
```
     :dp:`fls_ncg9etb3x7k0`
     A :t:`binding scope` is a :t:`scope` for :t:`[binding]s`.

```

Static glossary entry:
```

:dp:`fls_6qPYH5NJ8usI`
A :dt:`binding scope` is a :t:`scope` for :t:`[binding]s`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_ncg9etb3x7k0`
A :t:`binding scope` is a :t:`scope` for :t:`[binding]s`.

```

## 072 block expression (dual)
- File: src/expressions.rst:877
- Commit: 48ae27979c3ba216ba39d0e1bd634784063db0d2
- Indent: 0

Current context (10 lines before/after):
```
   867 |        $${$$
   868 |          InnerAttributeOrDoc*
   869 |          StatementList
   870 |        $$}$$
   871 | 
   872 |    StatementList ::=
   873 |        Statement* Expression?
   874 | 
   875 | .. rubric:: Legality Rules
   876 | 
   877 | .. glossary-entry:: block expression
   878 |    
   879 |    :glossary:
   880 |      :dp:`fls_gvjvzxi2xps4`
   881 |      A :dt:`block expression` is an :t:`expression` that sequences expressions and
   882 |      :t:`[statement]s`.
   883 |      
   884 |      :dp:`fls_h8j9t2xq2i1u`
   885 |      See :s:`BlockExpression`.
   886 |    :chapter:
   887 |      :dp:`fls_nf65p0l0v0gr`
   888 |      A :t:`block expression` is an :t:`expression` that sequences :t:`[expression]s`
   889 |      and :t:`[statement]s`.
   890 | 
   891 | .. glossary-entry:: tail expression
   892 |    
   893 |    :glossary:
   894 |      :dp:`fls_6k873f1knasi`
   895 |      A :dt:`tail expression` is the last :t:`expression` within a
   896 |      :t:`block expression`.
   897 |    :chapter:
   898 |      :dp:`fls_tn3hj7k2lliu`
   899 |      A :t:`tail expression` is the last :t:`expression` within a :t:`block
   900 |      expression`.
```

Glossary block (current):
```
     :dp:`fls_gvjvzxi2xps4`
     A :dt:`block expression` is an :t:`expression` that sequences expressions and
     :t:`[statement]s`.
     
     :dp:`fls_h8j9t2xq2i1u`
     See :s:`BlockExpression`.
```

Chapter block (current):
```
     :dp:`fls_nf65p0l0v0gr`
     A :t:`block expression` is an :t:`expression` that sequences :t:`[expression]s`
     and :t:`[statement]s`.

```

Static glossary entry:
```

:dp:`fls_gvjvzxi2xps4`
A :dt:`block expression` is an :t:`expression` that sequences expressions and
:t:`[statement]s`.

:dp:`fls_h8j9t2xq2i1u`
See :s:`BlockExpression`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_nf65p0l0v0gr`
A :t:`block expression` is an :t:`expression` that sequences :t:`[expression]s`
and :t:`[statement]s`.

```

## 073 attribute (dual)
- File: src/attributes.rst:45
- Commit: 1e900d9c4d1925a2ffb01e7d179e5a657c5a4015
- Indent: 0

Current context (10 lines before/after):
```
    35 | 
    36 |    AttributeInput ::=
    37 |        $$($$ TokenTree* $$)$$
    38 |      | $$=$$ Expression
    39 | 
    40 |    AttributeContentList ::=
    41 |        AttributeContent ($$,$$ AttributeContent)* $$,$$?
    42 | 
    43 | .. rubric:: Legality Rules
    44 | 
    45 | .. glossary-entry:: attribute
    46 |    
    47 |    :glossary:
    48 |      :dp:`fls_o74rfpe6zo6a`
    49 |      An :dt:`attribute` is a general, free-form metadatum that is interpreted based
    50 |      on its name, convention, language, and tool.
    51 |    :chapter:
    52 |      :dp:`fls_rnzxj1t0hehl`
    53 |      An :t:`attribute` is a general, free-form metadatum that is interpreted based on
    54 |      its :t:`name`, convention, language, and tool.
    55 | 
    56 | .. glossary-entry:: inner attribute
    57 |    
    58 |    :glossary:
    59 |      :dp:`fls_l7kxkav42l5d`
    60 |      An :dt:`inner attribute` is an :t:`attribute` that applies to an enclosing
    61 |      :t:`item`.
    62 |      
    63 |      :dp:`fls_umkk8xwktat1`
    64 |      See :s:`InnerAttribute`.
    65 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_o74rfpe6zo6a`
     An :dt:`attribute` is a general, free-form metadatum that is interpreted based
     on its name, convention, language, and tool.
```

Chapter block (current):
```
     :dp:`fls_rnzxj1t0hehl`
     An :t:`attribute` is a general, free-form metadatum that is interpreted based on
     its :t:`name`, convention, language, and tool.

```

Static glossary entry:
```

:dp:`fls_o74rfpe6zo6a`
An :dt:`attribute` is a general, free-form metadatum that is interpreted based
on its name, convention, language, and tool.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_rnzxj1t0hehl`
An :t:`attribute` is a general, free-form metadatum that is interpreted based on
its :t:`name`, convention, language, and tool.

```

## 074 attribute content (dual)
- File: src/attributes.rst:84
- Commit: 1e900d9c4d1925a2ffb01e7d179e5a657c5a4015
- Indent: 0

Current context (10 lines before/after):
```
    74 |      An :dt:`outer attribute` is an :t:`attribute` that applies to a subsequent
    75 |      :t:`item`.
    76 |      
    77 |      :dp:`fls_ty6ihy6x3kf`
    78 |      See :s:`OuterAttribute`.
    79 |    :chapter:
    80 |      :dp:`fls_8o6vmzbw1b1j`
    81 |      An :t:`outer attribute` is an :t:`attribute` that applies to a subsequent
    82 |      :t:`item`.
    83 | 
    84 | .. glossary-entry:: attribute content
    85 |    
    86 |    :glossary:
    87 |      :dp:`fls_sn0GvVmM3o38`
    88 |      An :dt:`attribute content` is a :t:`construct` that provides the content of
    89 |      an :t:`attribute`.
    90 |      
    91 |      :dp:`fls_YwyrWC8fcmRm`
    92 |      See :s:`AttributeContent`.
    93 |    :chapter:
    94 |      :dp:`fls_9TMRVlQwAdTB`
    95 |      An :t:`attribute content` is a :t:`construct` that provides the content of
    96 |      an :t:`attribute`.
    97 | 
    98 | .. rubric:: Examples
    99 | 
   100 | .. code-block:: rust
   101 | 
   102 |    #[cfg(target_os = "linux")]
   103 |    fn linux_only_function() {
   104 |        #![allow(unused_variables)]
   105 | 
   106 |        let unused = ();
   107 |    }
```

Glossary block (current):
```
     :dp:`fls_sn0GvVmM3o38`
     An :dt:`attribute content` is a :t:`construct` that provides the content of
     an :t:`attribute`.
     
     :dp:`fls_YwyrWC8fcmRm`
     See :s:`AttributeContent`.
```

Chapter block (current):
```
     :dp:`fls_9TMRVlQwAdTB`
     An :t:`attribute content` is a :t:`construct` that provides the content of
     an :t:`attribute`.

```

Static glossary entry:
```

:dp:`fls_sn0GvVmM3o38`
An :dt:`attribute content` is a :t:`construct` that provides the content of
an :t:`attribute`.

:dp:`fls_YwyrWC8fcmRm`
See :s:`AttributeContent`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_9TMRVlQwAdTB`
An :t:`attribute content` is a :t:`construct` that provides the content of
an :t:`attribute`.

```

## 075 associated item (dual)
- File: src/associated-items.rst:27
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
    17 | 
    18 |    AssociatedItemWithVisibility ::=
    19 |        VisibilityModifier? (
    20 |            ConstantDeclaration
    21 |          | FunctionDeclaration
    22 |          | TypeAliasDeclaration
    23 |        )
    24 | 
    25 | .. rubric:: Legality Rules
    26 | 
    27 | .. glossary-entry:: associated item
    28 |    
    29 |    :glossary:
    30 |      :dp:`fls_o5ysjk7l91ni`
    31 |      An :dt:`associated item` is an :t:`item` that appears within an
    32 |      :t:`implementation` or a :t:`trait`.
    33 |      
    34 |      :dp:`fls_44vtqu7tvhi2`
    35 |      See :s:`AssociatedItem`.
    36 |    :chapter:
    37 |      :dp:`fls_ckzd25qd213t`
    38 |      An :t:`associated item` is an :t:`item` that appears within an
    39 |      :t:`implementation` or a :t:`trait`.
    40 | 
    41 | .. glossary-entry:: associated constant
    42 |    
    43 |    :glossary:
    44 |      :dp:`fls_hi9qa0k2nujb`
    45 |      An :dt:`associated constant` is a :t:`constant` that appears as an
    46 |      :t:`associated item`.
    47 |    :chapter:
    48 |      :dp:`fls_5y6ae0xqux57`
    49 |      An :t:`associated constant` is a :t:`constant` that appears as an
    50 |      :t:`associated item`.
```

Glossary block (current):
```
     :dp:`fls_o5ysjk7l91ni`
     An :dt:`associated item` is an :t:`item` that appears within an
     :t:`implementation` or a :t:`trait`.
     
     :dp:`fls_44vtqu7tvhi2`
     See :s:`AssociatedItem`.
```

Chapter block (current):
```
     :dp:`fls_ckzd25qd213t`
     An :t:`associated item` is an :t:`item` that appears within an
     :t:`implementation` or a :t:`trait`.

```

Static glossary entry:
```

:dp:`fls_o5ysjk7l91ni`
An :dt:`associated item` is an :t:`item` that appears within an
:t:`implementation` or a :t:`trait`.

:dp:`fls_44vtqu7tvhi2`
See :s:`AssociatedItem`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_ckzd25qd213t`
An :t:`associated item` is an :t:`item` that appears within an
:t:`implementation` or a :t:`trait`.

```

## 076 associated constant (dual)
- File: src/associated-items.rst:41
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
    31 |      An :dt:`associated item` is an :t:`item` that appears within an
    32 |      :t:`implementation` or a :t:`trait`.
    33 |      
    34 |      :dp:`fls_44vtqu7tvhi2`
    35 |      See :s:`AssociatedItem`.
    36 |    :chapter:
    37 |      :dp:`fls_ckzd25qd213t`
    38 |      An :t:`associated item` is an :t:`item` that appears within an
    39 |      :t:`implementation` or a :t:`trait`.
    40 | 
    41 | .. glossary-entry:: associated constant
    42 |    
    43 |    :glossary:
    44 |      :dp:`fls_hi9qa0k2nujb`
    45 |      An :dt:`associated constant` is a :t:`constant` that appears as an
    46 |      :t:`associated item`.
    47 |    :chapter:
    48 |      :dp:`fls_5y6ae0xqux57`
    49 |      An :t:`associated constant` is a :t:`constant` that appears as an
    50 |      :t:`associated item`.
    51 | 
    52 | .. glossary-entry:: incomplete associated constant
    53 |    
    54 |    :glossary:
    55 |      :dp:`fls_bq48gl84bul0`
    56 |      An :dt:`incomplete associated constant` is an :t:`associated constant` without
    57 |      a :t:`constant initializer`.
    58 | 
    59 | .. glossary-entry:: associated function
    60 |    
    61 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_hi9qa0k2nujb`
     An :dt:`associated constant` is a :t:`constant` that appears as an
     :t:`associated item`.
```

Chapter block (current):
```
     :dp:`fls_5y6ae0xqux57`
     An :t:`associated constant` is a :t:`constant` that appears as an
     :t:`associated item`.

```

Static glossary entry:
```

:dp:`fls_hi9qa0k2nujb`
An :dt:`associated constant` is a :t:`constant` that appears as an
:t:`associated item`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_5y6ae0xqux57`
An :t:`associated constant` is a :t:`constant` that appears as an
:t:`associated item`.

```

## 077 active attribute (dual)
- File: src/attributes.rst:116
- Commit: 290841f2052b17e4a95428886ad4c10ccf097483
- Indent: 0

Current context (10 lines before/after):
```
   106 |        let unused = ();
   107 |    }
   108 | 
   109 | .. _fls_i52cujixq9qs:
   110 | 
   111 | Attribute Properties
   112 | --------------------
   113 | 
   114 | .. rubric:: Legality Rules
   115 | 
   116 | .. glossary-entry:: active attribute
   117 |    
   118 |    :glossary:
   119 |      :dp:`fls_r8rzj8mtxtp1`
   120 |      An :dt:`active attribute` is an :t:`attribute` that is removed from the
   121 |      :t:`item` it decorates.
   122 |    :chapter:
   123 |      :dp:`fls_p4potvq7x532`
   124 |      An :t:`active attribute` is an :t:`attribute` that is removed from the :t:`item`
   125 |      it decorates.
   126 | 
   127 | .. glossary-entry:: inert attribute
   128 |    
   129 |    :glossary:
   130 |      :dp:`fls_o4e3tyjz7l1h`
   131 |      An :dt:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
   132 |      it decorates.
   133 |    :chapter:
   134 |      :dp:`fls_xk7lb2g02sy7`
   135 |      An :t:`inert attribute` is an :t:`attribute` that remains with the :t:`item`
   136 |      it decorates.
```

Glossary block (current):
```
     :dp:`fls_r8rzj8mtxtp1`
     An :dt:`active attribute` is an :t:`attribute` that is removed from the
     :t:`item` it decorates.
```

Chapter block (current):
```
     :dp:`fls_p4potvq7x532`
     An :t:`active attribute` is an :t:`attribute` that is removed from the :t:`item`
     it decorates.

```

Static glossary entry:
```

:dp:`fls_r8rzj8mtxtp1`
An :dt:`active attribute` is an :t:`attribute` that is removed from the
:t:`item` it decorates.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_p4potvq7x532`
An :t:`active attribute` is an :t:`attribute` that is removed from the :t:`item`
it decorates.

```

## 078 all configuration predicate (dual)
- File: src/attributes.rst:1015
- Commit: 290841f2052b17e4a95428886ad4c10ccf097483
- Indent: 0

Current context (10 lines before/after):
```
  1005 |      A :dt:`configuration predicate` is a :t:`construct` that evaluates statically
  1006 |      to either ``true`` or ``false``, and controls :t:`conditional compilation`.
  1007 |      
  1008 |      :dp:`fls_99ioki0M64fD`
  1009 |      See :s:`ConfigurationPredicate`.
  1010 |    :chapter:
  1011 |      :dp:`fls_l96kyix5xsof`
  1012 |      A :t:`configuration predicate` is a :t:`construct` that evaluates statically
  1013 |      to either ``true`` or ``false``, and controls :t:`conditional compilation`.
  1014 | 
  1015 | .. glossary-entry:: all configuration predicate
  1016 |    
  1017 |    :glossary:
  1018 |      :dp:`fls_IyMZWiTnkYPv`
  1019 |      An :dt:`all configuration predicate` is a :t:`configuration predicate` that
  1020 |      models existential quantifier ALL.
  1021 |      
  1022 |      :dp:`fls_0fEw9Bx8xX8q`
  1023 |      See :s:`ConfigurationPredicateAll`.
  1024 |    :chapter:
  1025 |      :dp:`fls_y1MUhnKCxK6T`
  1026 |      An :t:`all configuration predicate` is a :t:`configuration predicate` that
  1027 |      models existential quantifier ALL.
  1028 | 
  1029 | :dp:`fls_tncxxsyutppf`
  1030 | An :t:`all configuration predicate` evaluates statically to ``true`` when either
  1031 | all nested configuration predicates evaluate to ``true``, or there are no nested
  1032 | configuration predicates.
  1033 | 
  1034 | .. glossary-entry:: any configuration predicate
  1035 |    
  1036 |    :glossary:
  1037 |      :dp:`fls_0nWHML8eoozG`
  1038 |      An :dt:`any configuration predicate` is a :t:`configuration predicate` that
```

Glossary block (current):
```
     :dp:`fls_IyMZWiTnkYPv`
     An :dt:`all configuration predicate` is a :t:`configuration predicate` that
     models existential quantifier ALL.
     
     :dp:`fls_0fEw9Bx8xX8q`
     See :s:`ConfigurationPredicateAll`.
```

Chapter block (current):
```
     :dp:`fls_y1MUhnKCxK6T`
     An :t:`all configuration predicate` is a :t:`configuration predicate` that
     models existential quantifier ALL.

```

Static glossary entry:
```

:dp:`fls_IyMZWiTnkYPv`
An :dt:`all configuration predicate` is a :t:`configuration predicate` that
models existential quantifier ALL.

:dp:`fls_0fEw9Bx8xX8q`
See :s:`ConfigurationPredicateAll`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_y1MUhnKCxK6T`
An :t:`all configuration predicate` is a :t:`configuration predicate` that
models existential quantifier ALL.

```

## 079 associated function (dual)
- File: src/associated-items.rst:59
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
    49 |      An :t:`associated constant` is a :t:`constant` that appears as an
    50 |      :t:`associated item`.
    51 | 
    52 | .. glossary-entry:: incomplete associated constant
    53 |    
    54 |    :glossary:
    55 |      :dp:`fls_bq48gl84bul0`
    56 |      An :dt:`incomplete associated constant` is an :t:`associated constant` without
    57 |      a :t:`constant initializer`.
    58 | 
    59 | .. glossary-entry:: associated function
    60 |    
    61 |    :glossary:
    62 |      :dp:`fls_zcy5pat39bq7`
    63 |      An :dt:`associated function` is a :t:`function` that appears as an
    64 |      :t:`associated item`.
    65 |    :chapter:
    66 |      :dp:`fls_lj7492aq7fzo`
    67 |      An :t:`associated function` is a :t:`function` that appears as an
    68 |      :t:`associated item`.
    69 | 
    70 | .. glossary-entry:: incomplete associated function
    71 |    
    72 |    :glossary:
    73 |      :dp:`fls_iboondra204w`
    74 |      An :dt:`incomplete associated function` is an :t:`associated function` without
    75 |      a :t:`function body`.
    76 | 
    77 | .. glossary-entry:: associated type
    78 |    
    79 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_zcy5pat39bq7`
     An :dt:`associated function` is a :t:`function` that appears as an
     :t:`associated item`.
```

Chapter block (current):
```
     :dp:`fls_lj7492aq7fzo`
     An :t:`associated function` is a :t:`function` that appears as an
     :t:`associated item`.

```

Static glossary entry:
```

:dp:`fls_zcy5pat39bq7`
An :dt:`associated function` is a :t:`function` that appears as an
:t:`associated item`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_lj7492aq7fzo`
An :t:`associated function` is a :t:`function` that appears as an
:t:`associated item`.

```

## 080 associated type (dual)
- File: src/associated-items.rst:77
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
    67 |      An :t:`associated function` is a :t:`function` that appears as an
    68 |      :t:`associated item`.
    69 | 
    70 | .. glossary-entry:: incomplete associated function
    71 |    
    72 |    :glossary:
    73 |      :dp:`fls_iboondra204w`
    74 |      An :dt:`incomplete associated function` is an :t:`associated function` without
    75 |      a :t:`function body`.
    76 | 
    77 | .. glossary-entry:: associated type
    78 |    
    79 |    :glossary:
    80 |      :dp:`fls_rs0n72c2d8f`
    81 |      An :dt:`associated type` is a :t:`type alias` that appears as an
    82 |      :t:`associated item`.
    83 |    :chapter:
    84 |      :dp:`fls_8cz4rdrklaj4`
    85 |      An :t:`associated type` is a :t:`type alias` that appears as an
    86 |      :t:`associated item`.
    87 | 
    88 | .. glossary-entry:: incomplete associated type
    89 |    
    90 |    :glossary:
    91 |      :dp:`fls_tka0gth8rc9x`
    92 |      An :dt:`incomplete associated type` is an :t:`associated type` without an
    93 |      :t:`initialization type`.
    94 | 
    95 | .. glossary-entry:: initialization type
    96 |    
    97 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_rs0n72c2d8f`
     An :dt:`associated type` is a :t:`type alias` that appears as an
     :t:`associated item`.
```

Chapter block (current):
```
     :dp:`fls_8cz4rdrklaj4`
     An :t:`associated type` is a :t:`type alias` that appears as an
     :t:`associated item`.

```

Static glossary entry:
```

:dp:`fls_rs0n72c2d8f`
An :dt:`associated type` is a :t:`type alias` that appears as an
:t:`associated item`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_8cz4rdrklaj4`
An :t:`associated type` is a :t:`type alias` that appears as an
:t:`associated item`.

```

## 081 associated implementation constant (dual)
- File: src/associated-items.rst:141
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
   131 |   the same :t:`trait`, and
   132 | 
   133 | * :dp:`fls_6Z05BK2JSzpP`
   134 |   The corresponding :t:`lifetime argument` in the use is not the ``'static``
   135 |   :t:`lifetime` and has either an explicit :t:`bound` or an :t:`implied bound`
   136 |   that constrains the :t:`type parameter`, and
   137 | 
   138 | * :dp:`fls_AtItgS1UvwiX`
   139 |   The intersection of all such uses is not empty.
   140 | 
   141 | .. glossary-entry:: associated implementation constant
   142 |    
   143 |    :glossary:
   144 |      :dp:`fls_rfaxcrrrb5q9`
   145 |      An :dt:`associated implementation constant` is an :t:`associated constant` that
   146 |      appears within an :t:`implementation`.
   147 |    :chapter:
   148 |      :dp:`fls_l3iwn56n1uz8`
   149 |      An :t:`associated implementation constant` is an :t:`associated constant` that
   150 |      appears within an :t:`implementation`.
   151 | 
   152 | :dp:`fls_4ftfefcotb4g`
   153 | An :t:`associated implementation constant` shall have a :t:`constant
   154 | initializer`.
   155 | 
   156 | .. glossary-entry:: associated implementation function
   157 |    
   158 |    :glossary:
   159 |      :dp:`fls_7xbmvl3jrc27`
   160 |      An :dt:`associated implementation function` is an :t:`associated function` that
   161 |      appears within an :t:`implementation`.
```

Glossary block (current):
```
     :dp:`fls_rfaxcrrrb5q9`
     An :dt:`associated implementation constant` is an :t:`associated constant` that
     appears within an :t:`implementation`.
```

Chapter block (current):
```
     :dp:`fls_l3iwn56n1uz8`
     An :t:`associated implementation constant` is an :t:`associated constant` that
     appears within an :t:`implementation`.

```

Static glossary entry:
```

:dp:`fls_rfaxcrrrb5q9`
An :dt:`associated implementation constant` is an :t:`associated constant` that
appears within an :t:`implementation`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_l3iwn56n1uz8`
An :t:`associated implementation constant` is an :t:`associated constant` that
appears within an :t:`implementation`.

```

## 082 associated implementation function (dual)
- File: src/associated-items.rst:156
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
   146 |      appears within an :t:`implementation`.
   147 |    :chapter:
   148 |      :dp:`fls_l3iwn56n1uz8`
   149 |      An :t:`associated implementation constant` is an :t:`associated constant` that
   150 |      appears within an :t:`implementation`.
   151 | 
   152 | :dp:`fls_4ftfefcotb4g`
   153 | An :t:`associated implementation constant` shall have a :t:`constant
   154 | initializer`.
   155 | 
   156 | .. glossary-entry:: associated implementation function
   157 |    
   158 |    :glossary:
   159 |      :dp:`fls_7xbmvl3jrc27`
   160 |      An :dt:`associated implementation function` is an :t:`associated function` that
   161 |      appears within an :t:`implementation`.
   162 |    :chapter:
   163 |      :dp:`fls_qb5qpfe0uwk`
   164 |      An :t:`associated implementation function` is an :t:`associated function` that
   165 |      appears within an :t:`implementation`.
   166 | 
   167 | :dp:`fls_1zlkeb6fz10j`
   168 | An :t:`associated implementation function` shall have a :t:`function body`.
   169 | 
   170 | .. glossary-entry:: associated implementation type
   171 |    
   172 |    :glossary:
   173 |      :dp:`fls_6g5t81gx9ayx`
   174 |      An :dt:`associated implementation type` is an :t:`associated type` that appears
   175 |      within an :t:`implementation`.
   176 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_7xbmvl3jrc27`
     An :dt:`associated implementation function` is an :t:`associated function` that
     appears within an :t:`implementation`.
```

Chapter block (current):
```
     :dp:`fls_qb5qpfe0uwk`
     An :t:`associated implementation function` is an :t:`associated function` that
     appears within an :t:`implementation`.

```

Static glossary entry:
```

:dp:`fls_7xbmvl3jrc27`
An :dt:`associated implementation function` is an :t:`associated function` that
appears within an :t:`implementation`.
```

Pre-migration chapter snippet (from commit parent):
```
:dp:`fls_qb5qpfe0uwk`
An :t:`associated implementation function` is an :t:`associated function` that
appears within an :t:`implementation`.

```

## 083 while loop (glossary-only)
- File: src/expressions.rst:5334
- Commit: 2dfc847a722423358b918a6836760a3a11b5cb96
- Indent: 0

Current context (10 lines before/after):
```
  5324 | 
  5325 |    loop {
  5326 |        println!("I am alive!");
  5327 |    }
  5328 | 
  5329 | .. _fls_5jjm1kt43axd:
  5330 | 
  5331 | While Loops
  5332 | ~~~~~~~~~~~
  5333 | 
  5334 | .. glossary-entry:: while loop
  5335 |    
  5336 |    :glossary:
  5337 |      :dp:`fls_ug9cxoml9ged`
  5338 |      For :dt:`while loop`, see :t:`while loop expression`.
  5339 | 
  5340 | .. rubric:: Syntax
  5341 | 
  5342 | .. syntax::
  5343 | 
  5344 |    WhileLoopExpression ::=
  5345 |        $$while$$ IterationExpression LoopBody
  5346 | 
  5347 |    IterationExpression ::=
  5348 |        SubjectExpression
  5349 | 
```

Glossary block (current):
```
     :dp:`fls_ug9cxoml9ged`
     For :dt:`while loop`, see :t:`while loop expression`.

```

Static glossary entry:
```

:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.
```

## 084 while let loop (glossary-only)
- File: src/expressions.rst:5424
- Commit: 2dfc847a722423358b918a6836760a3a11b5cb96
- Indent: 0

Current context (10 lines before/after):
```
  5414 |    while counter < 5 {
  5415 |        counter += 1;
  5416 |        println("iteration {}", counter);
  5417 |    }
  5418 | 
  5419 | .. _fls_m6kd5i9dy8dx:
  5420 | 
  5421 | While Let Loops
  5422 | ~~~~~~~~~~~~~~~
  5423 | 
  5424 | .. glossary-entry:: while let loop
  5425 |    
  5426 |    :glossary:
  5427 |      :dp:`fls_ovutw52qtx71`
  5428 |      For :dt:`while let loop`, see :t:`while let loop expression`.
  5429 | 
  5430 | .. rubric:: Syntax
  5431 | 
  5432 | .. syntax::
  5433 | 
  5434 |    WhileLetLoopExpression ::=
  5435 |        $$while$$ $$let$$ Pattern $$=$$ SubjectLetExpression LoopBody
  5436 | 
  5437 | .. rubric:: Legality Rules
  5438 | 
  5439 | .. glossary-entry:: while let loop expression
```

Glossary block (current):
```
     :dp:`fls_ovutw52qtx71`
     For :dt:`while let loop`, see :t:`while let loop expression`.

```

Static glossary entry:
```

:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.
```

## 085 validity invariant (glossary-only)
- File: src/types-and-traits.rst:393
- Commit: 66a1099560705cbf09a1a0ce96f8eeb318085b76
- Indent: 0

Current context (10 lines before/after):
```
   383 | Operation ``a >= b`` is equivalent to ``a == b | a > b``.
   384 | 
   385 | :dp:`fls_2j659ns8wop4`
   386 | Operation ``a < b`` is equivalent to ``!(a >= b)``.
   387 | 
   388 | :dp:`fls_d09l2rl0161l`
   389 | Operation ``a <= b`` is equivalent to ``a == b | a < b``.
   390 | 
   391 | .. rubric:: Undefined Behavior
   392 | 
   393 | .. glossary-entry:: validity invariant
   394 |    
   395 |    :glossary:
   396 |      :dp:`fls_3ebC3l839ajF`
   397 |      A :dt:`validity invariant` is an invariant that when violated results in
   398 |      immediate :t:`undefined behavior`.
   399 | 
   400 | :dp:`fls_2sd39mj05mb9`
   401 | It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`bool` to have
   402 | a bit pattern of ``0x00`` and ``0x01``.
   403 | 
   404 | .. _fls_wrvjizrqf3po:
   405 | 
   406 | Char Type
   407 | ~~~~~~~~~
   408 | 
   409 | .. rubric:: Legality Rules
```

Glossary block (current):
```
     :dp:`fls_3ebC3l839ajF`
     A :dt:`validity invariant` is an invariant that when violated results in
     immediate :t:`undefined behavior`.

```

Static glossary entry:
```

:dp:`fls_3ebC3l839ajF`
A :dt:`validity invariant` is an invariant that when violated results in
immediate :t:`undefined behavior`.
```

## 086 unsized type (glossary-only)
- File: src/types-and-traits.rst:3078
- Commit: 66a1099560705cbf09a1a0ce96f8eeb318085b76
- Indent: 0

Current context (10 lines before/after):
```
  3068 |   The source :t:`type` is a :t:`trait object type` with some :t:`principal trait` ``T``
  3069 |   and the target :t:`type` is a :t:`trait object type` with some :t:`principal trait` ``U``,
  3070 |   where ``U`` is a :t:`supertrait` of ``T``.
  3071 | 
  3072 | .. glossary-entry:: sized type
  3073 |    
  3074 |    :glossary:
  3075 |      :dp:`fls_pwcgsRCNSwKn`
  3076 |      A :dt:`sized type` is a :t:`type` with statically known size.
  3077 | 
  3078 | .. glossary-entry:: unsized type
  3079 |    
  3080 |    :glossary:
  3081 |      :dp:`fls_M9NpzBH8Wf4z`
  3082 |      An :dt:`unsized type` is a :t:`type` with statically unknown size.
  3083 | 
  3084 | .. glossary-entry:: unsized coercion
  3085 |    
  3086 |    :glossary:
  3087 |      :dp:`fls_olt5qhyvhmtq`
  3088 |      An :dt:`unsized coercion` is a :t:`type coercion` that converts a
  3089 |      :t:`sized type` into an :t:`unsized type`.
  3090 |    :chapter:
  3091 |      :dp:`fls_iiiu2q7pym4p`
  3092 |      An :t:`unsized coercion` is a :t:`type coercion` that converts a :t:`sized type`
  3093 |      into an :t:`unsized type`. :t:`Unsized coercion` from a source :t:`type` to a
```

Glossary block (current):
```
     :dp:`fls_M9NpzBH8Wf4z`
     An :dt:`unsized type` is a :t:`type` with statically unknown size.

```

Static glossary entry:
```

:dp:`fls_M9NpzBH8Wf4z`
An :dt:`unsized type` is a :t:`type` with statically unknown size.
```

## 087 unsafe block (glossary-only)
- File: src/expressions.rst:1132
- Commit: 31ccd8534dc29d58e9a37eeb005dace8db822a8d
- Indent: 0

Current context (10 lines before/after):
```
  1122 | 
  1123 | .. rubric:: Syntax
  1124 | 
  1125 | .. syntax::
  1126 | 
  1127 |    UnsafeBlockExpression ::=
  1128 |        $$unsafe$$ BlockExpression
  1129 | 
  1130 | .. rubric:: Legality Rules
  1131 | 
  1132 | .. glossary-entry:: unsafe block
  1133 |    
  1134 |    :glossary:
  1135 |      :dp:`fls_8tkolhmd6xfp`
  1136 |      For :dt:`unsafe block`, see :t:`unsafe block expression`.
  1137 | 
  1138 | .. glossary-entry:: unsafe block expression
  1139 |    
  1140 |    :glossary:
  1141 |      :dp:`fls_et2h89jyivhs`
  1142 |      An :dt:`unsafe block expression` is a :t:`block expression` that is specified
  1143 |      with :t:`keyword` ``unsafe``.
  1144 |      
  1145 |      :dp:`fls_c94rudunhp5b`
  1146 |      See :s:`UnsafeBlockExpression`.
  1147 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_8tkolhmd6xfp`
     For :dt:`unsafe block`, see :t:`unsafe block expression`.

```

Static glossary entry:
```

:dp:`fls_8tkolhmd6xfp`
For :dt:`unsafe block`, see :t:`unsafe block expression`.
```

## 088 unsigned integer type (glossary-only)
- File: src/types-and-traits.rst:499
- Commit: 31ccd8534dc29d58e9a37eeb005dace8db822a8d
- Indent: 0

Current context (10 lines before/after):
```
   489 | 
   490 | .. rubric:: Legality Rules
   491 | 
   492 | .. glossary-entry:: integer type
   493 |    
   494 |    :glossary:
   495 |      :dp:`fls_nhfqdhf26ym3`
   496 |      An :dt:`integer type` is a :t:`numeric type` whose :t:`[value]s` denote whole
   497 |      numbers.
   498 | 
   499 | .. glossary-entry:: unsigned integer type
   500 |    
   501 |    :glossary:
   502 |      :dp:`fls_dxnf79qemlg6`
   503 |      An :dt:`unsigned integer type` is an :t:`integer type` whose :t:`[value]s`
   504 |      denote zero and positive whole numbers.
   505 | 
   506 | :dp:`fls_cokwseo3nnr`
   507 | :t:`[Unsigned integer type]s` define the following inclusive ranges over the
   508 | domain of whole numbers:
   509 | 
   510 | .. list-table::
   511 | 
   512 |    * - :dp:`fls_vk1skn6ek36u`
   513 |      - **Type**
   514 |      - **Minimum**
   515 |      - **Maximum**
```

Glossary block (current):
```
     :dp:`fls_dxnf79qemlg6`
     An :dt:`unsigned integer type` is an :t:`integer type` whose :t:`[value]s`
     denote zero and positive whole numbers.

```

Static glossary entry:
```

:dp:`fls_dxnf79qemlg6`
An :dt:`unsigned integer type` is an :t:`integer type` whose :t:`[value]s`
denote zero and positive whole numbers.
```

## 089 unique immutable reference (glossary-only)
- File: src/expressions.rst:6857
- Commit: ba1d4b9508e877d0bdcb75a99661163a9bffbae2
- Indent: 0

Current context (10 lines before/after):
```
  6847 | :dt:`by mutable reference capture` binds a :t:`mutable reference` to the
  6848 | :t:`capture target` and passes the :t:`mutable reference` into the
  6849 | :t:`capturing environment`.
  6850 | 
  6851 | :dp:`fls_8HLaLAIZgYfs`
  6852 | A :t:`captured` :t:`capture target` with :t:`capture mode`
  6853 | :dt:`by unique immutable reference capture` binds a
  6854 | :t:`unique immutable reference` to the :t:`capture target` and passes the
  6855 | :t:`mutable reference` into the :t:`capturing environment`.
  6856 | 
  6857 | .. glossary-entry:: unique immutable reference
  6858 |    
  6859 |    :glossary:
  6860 |      :dp:`fls_eXrivAmNxzmv`
  6861 |      A :dt:`unique immutable reference` is an :t:`immutable reference` produced by
  6862 |      :t:`capturing` what is asserted to be the only live :t:`reference` to a
  6863 |      :t:`value` while the :t:`reference` exists.
  6864 | 
  6865 | :dp:`fls_t695ps4lfh6z`
  6866 | The :t:`capture mode` is determined based on the use of the :t:`capture target`
  6867 | within the :t:`capturing expression`, as follows:
  6868 | 
  6869 | #. :dp:`fls_6j8cr7d5zs1l`
  6870 |    If the :t:`capturing expression` is subject to :t:`keyword` ``move``, then
  6871 |    the :t:`capture mode` is :t:`by value capture`.
  6872 | 
  6873 | #. :dp:`fls_l8e98pyhm08g`
  6874 |    Otherwise the :t:`capture mode` is determined based on the following
```

Glossary block (current):
```
     :dp:`fls_eXrivAmNxzmv`
     A :dt:`unique immutable reference` is an :t:`immutable reference` produced by
     :t:`capturing` what is asserted to be the only live :t:`reference` to a
     :t:`value` while the :t:`reference` exists.

```

Static glossary entry:
```

:dp:`fls_eXrivAmNxzmv`
A :dt:`unique immutable reference` is an :t:`immutable reference` produced by
:t:`capturing` what is asserted to be the only live :t:`reference` to a
:t:`value` while the :t:`reference` exists.
```

## 090 u8 (glossary-only)
- File: src/types-and-traits.rst:537
- Commit: ba1d4b9508e877d0bdcb75a99661163a9bffbae2
- Indent: 0

Current context (10 lines before/after):
```
   527 |      - 2\ :sup:`32` - 1
   528 |    * - :dp:`fls_q9f95uet7gq4`
   529 |      - :c:`u64`
   530 |      - 0
   531 |      - 2\ :sup:`64` - 1
   532 |    * - :dp:`fls_yjb3kzijd19v`
   533 |      - :c:`u128`
   534 |      - 0
   535 |      - 2\ :sup:`128` - 1
   536 | 
   537 | .. glossary-entry:: u8
   538 |    
   539 |    :glossary:
   540 |      :dp:`fls_umf9zfeghy6`
   541 |      :dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
   542 |      2\ :sup:`8` - 1, all inclusive.
   543 | 
   544 | .. glossary-entry:: u16
   545 |    
   546 |    :glossary:
   547 |      :dp:`fls_8vi7bm2895y0`
   548 |      :dc:`u16` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
   549 |      2\ :sup:`16` - 1, all inclusive.
   550 | 
   551 | .. glossary-entry:: u32
   552 |    
   553 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_umf9zfeghy6`
     :dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
     2\ :sup:`8` - 1, all inclusive.

```

Static glossary entry:
```

:dp:`fls_umf9zfeghy6`
:dc:`u8` is an :t:`unsigned integer type` whose :t:`[value]s` range from 0 to
2\ :sup:`8` - 1, all inclusive.
```

## 091 unary operator (glossary-only)
- File: src/expressions.rst:1214
- Commit: cf11e81e0115b4f4234b6f113802fe2ece9b146e
- Indent: 0

Current context (10 lines before/after):
```
  1204 |    :glossary:
  1205 |      :dp:`fls_6ev01xwcfow1`
  1206 |      An :dt:`operator expression` is an :t:`expression` that involves an operator.
  1207 |      
  1208 |      :dp:`fls_qdszbyeuo7w1`
  1209 |      See :s:`OperatorExpression`.
  1210 |    :chapter:
  1211 |      :dp:`fls_ursc5ynymoy`
  1212 |      An :t:`operator expression` is an :t:`expression` that involves an operator.
  1213 | 
  1214 | .. glossary-entry:: unary operator
  1215 |    
  1216 |    :glossary:
  1217 |      :dp:`fls_p6mk2zrwgwem`
  1218 |      A :dt:`unary operator` operates on one :t:`operand`.
  1219 | 
  1220 | .. rubric:: Dynamic Semantics
  1221 | 
  1222 | :dp:`fls_lSxXWxJn0vMO`
  1223 | An :t:`operator expression` that operates with :t:`[floating-point value]s` run as a :t:`constant expression` is allowed to yield different :t:`[value]s` compared to when run as a non-:t:`constant expression`.
  1224 | 
  1225 | .. _fls_qztk0bkju9u:
  1226 | 
  1227 | Borrow Expression
  1228 | ~~~~~~~~~~~~~~~~~
  1229 | 
```

Glossary block (current):
```
     :dp:`fls_p6mk2zrwgwem`
     A :dt:`unary operator` operates on one :t:`operand`.

```

Static glossary entry:
```

:dp:`fls_p6mk2zrwgwem`
A :dt:`unary operator` operates on one :t:`operand`.
```

## 092 Unicode (glossary-only)
- File: src/lexical-elements.rst:28
- Commit: cf11e81e0115b4f4234b6f113802fe2ece9b146e
- Indent: 0

Current context (10 lines before/after):
```
    18 | 
    19 | .. _fls_2i089jvv8j5g:
    20 | 
    21 | Character Set
    22 | -------------
    23 | 
    24 | :dp:`fls_itcth8292ud6`
    25 | The program text of a Rust program is written using the :t:`Unicode` character
    26 | set.
    27 | 
    28 | .. glossary-entry:: Unicode
    29 |    
    30 |    :glossary:
    31 |      :dp:`fls_y7gwku7pe1f4`
    32 |      :dt:`Unicode` is the universal character encoding standard for written
    33 |      characters and text described in the Unicode® Standard by the Unicode
    34 |      Consortium.
    35 | 
    36 | .. rubric:: Syntax
    37 | 
    38 | :dp:`fls_vfx8byq5zo8t`
    39 | A character is defined by this document for each cell in the coding space
    40 | described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
    41 | character to that cell.
    42 | 
    43 | .. glossary-entry:: code point
    44 |    
    45 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_y7gwku7pe1f4`
     :dt:`Unicode` is the universal character encoding standard for written
     characters and text described in the Unicode® Standard by the Unicode
     Consortium.

```

Static glossary entry:
```

:dp:`fls_y7gwku7pe1f4`
:dt:`Unicode` is the universal character encoding standard for written
characters and text described in the Unicode® Standard by the Unicode
Consortium.
```

## 093 tuple (glossary-only)
- File: src/types-and-traits.rst:859
- Commit: 52d13394ed3976cbeadc5bc15115cd2570586ec3
- Indent: 0

Current context (10 lines before/after):
```
   849 |        $$($$ TupleFieldList? $$)$$
   850 | 
   851 |    TupleFieldList ::=
   852 |        TupleField ($$,$$ TupleField)* $$,$$?
   853 | 
   854 |    TupleField ::=
   855 |        TypeSpecification
   856 | 
   857 | .. rubric:: Legality Rules
   858 | 
   859 | .. glossary-entry:: tuple
   860 |    
   861 |    :glossary:
   862 |      :dp:`fls_yhcfqz6p0059`
   863 |      A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.
   864 | 
   865 | .. glossary-entry:: tuple type
   866 |    
   867 |    :glossary:
   868 |      :dp:`fls_q0ulqfvnxwni`
   869 |      A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
   870 |      of other :t:`[type]s`.
   871 |      
   872 |      :dp:`fls_rkugxsau1w78`
   873 |      See :s:`TupleTypeSpecification`.
   874 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_yhcfqz6p0059`
     A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.

```

Static glossary entry:
```

:dp:`fls_yhcfqz6p0059`
A :dt:`tuple` is a :t:`value` of a :t:`tuple type`.
```

## 094 tuple field (glossary-only)
- File: src/types-and-traits.rst:879
- Commit: 52d13394ed3976cbeadc5bc15115cd2570586ec3
- Indent: 0

Current context (10 lines before/after):
```
   869 |      A :dt:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
   870 |      of other :t:`[type]s`.
   871 |      
   872 |      :dp:`fls_rkugxsau1w78`
   873 |      See :s:`TupleTypeSpecification`.
   874 |    :chapter:
   875 |      :dp:`fls_bn7wmf681ngt`
   876 |      A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
   877 |      of other :t:`[type]s`.
   878 | 
   879 | .. glossary-entry:: tuple field
   880 |    
   881 |    :glossary:
   882 |      :dp:`fls_8rq1gbzij5tk`
   883 |      A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.
   884 | 
   885 | .. glossary-entry:: arity
   886 |    
   887 |    :glossary:
   888 |      :dp:`fls_dl2gkip00bua`
   889 |      An :dt:`arity` is the number of :t:`[tuple field]s` in a :t:`tuple type`.
   890 | 
   891 | .. glossary-entry:: unit type
   892 |    
   893 |    :glossary:
   894 |      :dp:`fls_jtdtv3q2ls05`
```

Glossary block (current):
```
     :dp:`fls_8rq1gbzij5tk`
     A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.

```

Static glossary entry:
```

:dp:`fls_8rq1gbzij5tk`
A :dt:`tuple field` is a :t:`field` of a :t:`tuple type`.
```

## 095 syntactic category (glossary-only)
- File: src/general.rst:268
- Commit: dc774c9d0b2a6ae1dff7a9cd4e1d8a84b3489ceb
- Indent: 0

Current context (10 lines before/after):
```
   258 | together with context-dependent requirements expressed by narrative rules.
   259 | 
   260 | :dp:`fls_ioyp4wux6skt`
   261 | The semantic meaning of a Rust program is described by means of narrative rules defining
   262 | both the effects of each construct and the composition rules for constructs.
   263 | 
   264 | :dp:`fls_jsflt7691ye4`
   265 | The context-free syntax of Rust is described using a simple variant of the
   266 | Backus-Naur form. In particular:
   267 | 
   268 | .. glossary-entry:: syntactic category
   269 |    
   270 |    :glossary:
   271 |      :dp:`fls_f981e3m7kq50`
   272 |      A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
   273 |      definition of the Rust programming language.
   274 | 
   275 | .. glossary-entry:: escaped character
   276 |    
   277 |    :glossary:
   278 |      :dp:`fls_7yvnbakmo7y5`
   279 |      An :dt:`escaped character` is the textual representation for a character with
   280 |      special meaning. An escaped character consists of character 0x5C (reverse
   281 |      solidus), followed by the single character encoding of the special meaning
   282 |      character. For example, ``\t`` is the escaped character for 0x09 (horizontal
   283 |      tabulation).
   284 | 
```

Glossary block (current):
```
     :dp:`fls_f981e3m7kq50`
     A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
     definition of the Rust programming language.

```

Static glossary entry:
```

:dp:`fls_f981e3m7kq50`
A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
definition of the Rust programming language.
```

## 096 textual type (glossary-only)
- File: src/types-and-traits.rst:198
- Commit: dc774c9d0b2a6ae1dff7a9cd4e1d8a84b3489ceb
- Indent: 0

Current context (10 lines before/after):
```
   188 | Scalar Types
   189 | ------------
   190 | 
   191 | .. glossary-entry:: scalar type
   192 |    
   193 |    :glossary:
   194 |      :dp:`fls_GgBqFW2NywoA`
   195 |      A :dt:`scalar type` is either a :c:`bool` :t:`type`, a :c:`char` :t:`type`, or
   196 |      a :t:`numeric type`.
   197 | 
   198 | .. glossary-entry:: textual type
   199 |    
   200 |    :glossary:
   201 |      :dp:`fls_lv1pdtzf6f58`
   202 |      A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
   203 |      :c:`str`.
   204 | 
   205 | .. _fls_tiqp1gxf116z:
   206 | 
   207 | Bool Type
   208 | ~~~~~~~~~
   209 | 
   210 | .. rubric:: Legality Rules
   211 | 
   212 | .. glossary-entry:: bool
   213 |    
   214 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_lv1pdtzf6f58`
     A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
     :c:`str`.

```

Static glossary entry:
```

:dp:`fls_lv1pdtzf6f58`
A :dt:`textual type` is a :t:`type` class that includes type :c:`char` and type
:c:`str`.
```

## 097 subexpression (glossary-only)
- File: src/expressions.rst:95
- Commit: 6f91bcd7e628612db9af159d58fc072e5f1867eb
- Indent: 0

Current context (10 lines before/after):
```
    85 |      A :dt:`subject let expression` is an :t:`expression` that controls
    86 |      :t:`[if let expression]s` and :t:`[while let loop]s`.
    87 |      
    88 |      :dp:`fls_vnzaargh5yok`
    89 |      See :s:`SubjectLetExpression`.
    90 |    :chapter:
    91 |      :dp:`fls_361q9ljc6ybz`
    92 |      A :ds:`SubjectLetExpression` is any expression in category
    93 |      :s:`SubjectExpression`, except :s:`LazyBooleanExpression`.
    94 | 
    95 | .. glossary-entry:: subexpression
    96 |    
    97 |    :glossary:
    98 |      :dp:`fls_bNSHwD4Kpfm0`
    99 |      A :dt:`subexpression` is an :t:`expression` nested within another
   100 |      :t:`expression`.
   101 | 
   102 | .. rubric:: Legality Rules
   103 | 
   104 | .. glossary-entry:: expression
   105 |    
   106 |    :glossary:
   107 |      :dp:`fls_f7iuwgbs1lql`
   108 |      An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may
   109 |      have side effects at run-time.
   110 |      
   111 |      :dp:`fls_8l9hru1x586q`
```

Glossary block (current):
```
     :dp:`fls_bNSHwD4Kpfm0`
     A :dt:`subexpression` is an :t:`expression` nested within another
     :t:`expression`.

```

Static glossary entry:
```

:dp:`fls_bNSHwD4Kpfm0`
A :dt:`subexpression` is an :t:`expression` nested within another
:t:`expression`.
```

## 098 subtraction assignment (glossary-only)
- File: src/expressions.rst:3437
- Commit: 6f91bcd7e628612db9af159d58fc072e5f1867eb
- Indent: 0

Current context (10 lines before/after):
```
  3427 |      A :dt:`shift right assignment expression` is a
  3428 |      :t:`compound assignment expression` that uses bit shift right arithmetic.
  3429 |      
  3430 |      :dp:`fls_naqzlebew1uf`
  3431 |      See :s:`ShiftRightAssignmentExpression`.
  3432 |    :chapter:
  3433 |      :dp:`fls_s7rey2bndfei`
  3434 |      A :t:`shift right assignment expression` is a
  3435 |      :t:`compound assignment expression` that uses bit shift right arithmetic.
  3436 | 
  3437 | .. glossary-entry:: subtraction assignment
  3438 |    
  3439 |    :glossary:
  3440 |      :dp:`fls_75Eyk2YXO2j4`
  3441 |      For :dt:`subtraction assignment`, see :t:`subtraction assignment`.
  3442 | 
  3443 | .. glossary-entry:: subtraction assignment expression
  3444 |    
  3445 |    :glossary:
  3446 |      :dp:`fls_4pb85nl4r7vs`
  3447 |      A :dt:`subtraction assignment expression` is a
  3448 |      :t:`compound assignment expression` that uses subtraction.
  3449 |      
  3450 |      :dp:`fls_mye9yj5tc8hr`
  3451 |      See :s:`SubtractionAssignmentExpression`.
  3452 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_75Eyk2YXO2j4`
     For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

```

Static glossary entry:
```

:dp:`fls_75Eyk2YXO2j4`
For :dt:`subtraction assignment`, see :t:`subtraction assignment`.
```

## 099 statement (glossary-only)
- File: src/statements.rst:11
- Commit: 6cc6e9f1f6cb14ffe8cdc156ba852ef171bcc767
- Indent: 0

Current context (10 lines before/after):
```
     1 | .. SPDX-License-Identifier: MIT OR Apache-2.0
     2 |    SPDX-FileCopyrightText: The Ferrocene Developers
     3 | 
     4 | .. default-domain:: spec
     5 | 
     6 | .. _fls_wdicg3sqa98e:
     7 | 
     8 | Statements
     9 | ==========
    10 | 
    11 | .. glossary-entry:: statement
    12 |    
    13 |    :glossary:
    14 |      :dp:`fls_faijgwg4lhp9`
    15 |      A :dt:`statement` is a component of a block expression.
    16 |      
    17 |      :dp:`fls_th7edvxml3mn`
    18 |      See :s:`Statement`.
    19 | 
    20 | .. rubric:: Syntax
    21 | 
    22 | .. syntax::
    23 | 
    24 |    Statement ::=
    25 |        ExpressionStatement
    26 |      | Item
    27 |      | LetStatement
    28 |      | TerminatedMacroInvocation
    29 |      | $$;$$
```

Glossary block (current):
```
     :dp:`fls_faijgwg4lhp9`
     A :dt:`statement` is a component of a block expression.
     
     :dp:`fls_th7edvxml3mn`
     See :s:`Statement`.

```

Static glossary entry:
```

:dp:`fls_faijgwg4lhp9`
A :dt:`statement` is a component of a block expression.

:dp:`fls_th7edvxml3mn`
See :s:`Statement`.
```

## 100 slice (glossary-only)
- File: src/types-and-traits.rst:756
- Commit: 6cc6e9f1f6cb14ffe8cdc156ba852ef171bcc767
- Indent: 0

Current context (10 lines before/after):
```
   746 | 
   747 | .. code-block:: rust
   748 | 
   749 |    let array: [i32; 3] = [1, 2, 3];
   750 | 
   751 | .. _fls_vpbikb73dw4k:
   752 | 
   753 | Slice Types
   754 | ~~~~~~~~~~~
   755 | 
   756 | .. glossary-entry:: slice
   757 |    
   758 |    :glossary:
   759 |      :dp:`fls_p1sv01ml2ark`
   760 |      A :dt:`slice` is a :t:`value` of a :t:`slice type`.
   761 | 
   762 | .. rubric:: Syntax
   763 | 
   764 | .. syntax::
   765 | 
   766 |    SliceTypeSpecification ::=
   767 |        $$[$$ ElementType $$]$$
   768 | 
   769 | .. rubric:: Legality Rules
   770 | 
   771 | .. glossary-entry:: slice type
```

Glossary block (current):
```
     :dp:`fls_p1sv01ml2ark`
     A :dt:`slice` is a :t:`value` of a :t:`slice type`.

```

Static glossary entry:
```

:dp:`fls_p1sv01ml2ark`
A :dt:`slice` is a :t:`value` of a :t:`slice type`.
```

## 101 shared borrow (glossary-only)
- File: src/expressions.rst:1266
- Commit: bc8919fbbd8d4666fda0758018f0510370466334
- Indent: 0

Current context (10 lines before/after):
```
  1256 |    
  1257 |    :glossary:
  1258 |      :dp:`fls_dojod5pg4r7l`
  1259 |      An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1260 |      :t:`keyword` ``mut``.
  1261 |    :chapter:
  1262 |      :dp:`fls_r7ix8webgqlm`
  1263 |      An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
  1264 |      :t:`keyword` ``mut``.
  1265 | 
  1266 | .. glossary-entry:: shared borrow
  1267 |    
  1268 |    :glossary:
  1269 |      :dp:`fls_gmbskxin90zi`
  1270 |      A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
  1271 |      :t:`immutable borrow expression`.
  1272 | 
  1273 | .. glossary-entry:: mutable borrow expression
  1274 |    
  1275 |    :glossary:
  1276 |      :dp:`fls_80kcc4y21hu6`
  1277 |      A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
  1278 |      :t:`keyword` ``mut``.
  1279 |    :chapter:
  1280 |      :dp:`fls_50j167r4v61b`
  1281 |      A :t:`mutable borrow expression` is a :t:`borrow expression` that has
  1282 |      :t:`keyword` ``mut``.
```

Glossary block (current):
```
     :dp:`fls_gmbskxin90zi`
     A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
     :t:`immutable borrow expression`.

```

Static glossary entry:
```

:dp:`fls_gmbskxin90zi`
A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
:t:`immutable borrow expression`.
```

## 102 shift left assignment (glossary-only)
- File: src/expressions.rst:3397
- Commit: bc8919fbbd8d4666fda0758018f0510370466334
- Indent: 0

Current context (10 lines before/after):
```
  3387 |      A :dt:`remainder assignment expression` is a
  3388 |      :t:`compound assignment expression` that uses remainder division.
  3389 |      
  3390 |      :dp:`fls_rkk80quk8uzc`
  3391 |      See :s:`RemainderAssignmentExpression`.
  3392 |    :chapter:
  3393 |      :dp:`fls_fbp5dojti27r`
  3394 |      A :t:`remainder assignment expression` is a :t:`compound assignment expression`
  3395 |      that uses remainder division.
  3396 | 
  3397 | .. glossary-entry:: shift left assignment
  3398 |    
  3399 |    :glossary:
  3400 |      :dp:`fls_6adWrtvab6Tw`
  3401 |      For :dt:`shift left assignment`, see :t:`shift left assignment expression`.
  3402 | 
  3403 | .. glossary-entry:: shift left assignment expression
  3404 |    
  3405 |    :glossary:
  3406 |      :dp:`fls_j15ke2p8cjfp`
  3407 |      A :dt:`shift left assignment expression` is a
  3408 |      :t:`compound assignment expression` that uses bit shift left arithmetic.
  3409 |      
  3410 |      :dp:`fls_ozu74fsakomn`
  3411 |      See :s:`ShiftLeftAssignmentExpression`.
  3412 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_6adWrtvab6Tw`
     For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

```

Static glossary entry:
```

:dp:`fls_6adWrtvab6Tw`
For :dt:`shift left assignment`, see :t:`shift left assignment expression`.
```

## 103 Self (glossary-only)
- File: src/entities-and-resolution.rst:858
- Commit: 3925cc1fb6bb7f1d87d9b2d6b611be59eab141d8
- Indent: 0

Current context (10 lines before/after):
```
   848 |      A :t:`label scope` is a :t:`scope` for :t:`[label]s`.
   849 | 
   850 | :dp:`fls_8sevg1sa82h4`
   851 | A :t:`label` is :t:`in scope` within the :t:`block expression` of the related
   852 | :t:`loop expression`.
   853 | 
   854 | :dp:`fls_ep5smja1rxdv`
   855 | A :t:`label` is not :t:`in scope` within nested :t:`[async block]s`,
   856 | :t:`[closure expression]s`, :t:`[constant context]s`, and :t:`[item]s`.
   857 | 
   858 | .. glossary-entry:: Self
   859 |    
   860 |    :glossary:
   861 |      :dp:`fls_q6whqbfusswf`
   862 |      :dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
   863 |      implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
   864 |      :t:`type` that implements a :t:`trait`.
   865 | 
   866 | .. _fls_kgbi26212eof:
   867 | 
   868 | Self Scope
   869 | ~~~~~~~~~~
   870 | 
   871 | .. rubric:: Legality Rules
   872 | 
   873 | .. glossary-entry:: Self scope
   874 |    
   875 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_q6whqbfusswf`
     :dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
     implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
     :t:`type` that implements a :t:`trait`.

```

Static glossary entry:
```

:dp:`fls_q6whqbfusswf`
:dc:`Self` is either an implicit :t:`type parameter` in :t:`[trait]s` or an
implicit :t:`type alias` in :t:`[implementation]s`. :c:`Self` refers to the
:t:`type` that implements a :t:`trait`.
```

## 104 rustc (glossary-only)
- File: src/general.rst:57
- Commit: 3925cc1fb6bb7f1d87d9b2d6b611be59eab141d8
- Indent: 0

Current context (10 lines before/after):
```
    47 | -----
    48 | 
    49 | :dp:`fls_srdq4mota5pr`
    50 | This document specifies the form and meaning of programs written in the 2021 Edition of the
    51 | Rust programming language, as implemented by the Rust compiler (:t:`rustc`),
    52 | version |spec_version|.
    53 | It documents the current understanding for the purposes of
    54 | compiler validation. As such, given any doubt, it prefers documenting behavior
    55 | of :t:`rustc` over claiming correctness as a specification.
    56 | 
    57 | .. glossary-entry:: rustc
    58 |    
    59 |    :glossary:
    60 |      :dp:`fls_zdgbeixirjfm`
    61 |      :dt:`rustc` is a compiler that implements the FLS.
    62 | 
    63 | :dp:`fls_dv1qish8svc`
    64 | This document is made available for contribution and review,
    65 | and can be a place of shared understanding. It
    66 | is not intended as a discussion ground for language evolution. It is also not
    67 | intended as a document enabling conformance between compilers.
    68 | 
    69 | .. _fls_10yukmkhl0ng:
    70 | 
    71 | Extent
    72 | ~~~~~~
```

Glossary block (current):
```
     :dp:`fls_zdgbeixirjfm`
     :dt:`rustc` is a compiler that implements the FLS.

```

Static glossary entry:
```

:dp:`fls_zdgbeixirjfm`
:dt:`rustc` is a compiler that implements the FLS.
```

## 105 refutability (glossary-only)
- File: src/patterns.rst:155
- Commit: 764f095e70e4cf8836ffda3ed3f8e5f78f685ad5
- Indent: 0

Current context (10 lines before/after):
```
   145 | .. glossary-entry:: irrefutable pattern
   146 |    
   147 |    :glossary:
   148 |      :dp:`fls_y421hdrbs6ak`
   149 |      An :dt:`irrefutable pattern` is a :t:`pattern` that always matches the
   150 |      :t:`value` it is being matched against.
   151 |    :chapter:
   152 |      :dp:`fls_9fjspnefoyvz`
   153 |      An :t:`irrefutable pattern` is a :t:`pattern` that always matches any :t:`value` of its :t:`type`.
   154 | 
   155 | .. glossary-entry:: refutability
   156 |    
   157 |    :glossary:
   158 |      :dp:`fls_gzjrfx19fg40`
   159 |      :dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
   160 |      to match all possible :t:`[value]s` of a :t:`type`.
   161 | 
   162 | .. glossary-entry:: refutable pattern
   163 |    
   164 |    :glossary:
   165 |      :dp:`fls_re7qz78koman`
   166 |      A :dt:`refutable pattern` is a :t:`pattern` that has a possibility of not
   167 |      matching the :t:`value` it is being matched against.
   168 |    :chapter:
   169 |      :dp:`fls_uq7ftuuq1sig`
   170 |      A :t:`refutable pattern` is a :t:`pattern` that has a possibility of not
   171 |      matching a :t:`value` of its :t:`type`
```

Glossary block (current):
```
     :dp:`fls_gzjrfx19fg40`
     :dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
     to match all possible :t:`[value]s` of a :t:`type`.

```

Static glossary entry:
```

:dp:`fls_gzjrfx19fg40`
:dt:`Refutability` is a property of :t:`[pattern]s` that expresses the ability
to match all possible :t:`[value]s` of a :t:`type`.
```

## 106 renaming (glossary-only)
- File: src/entities-and-resolution.rst:1390
- Commit: e5bd283aaeb404147ba83c2dc3fb49b413e9313f
- Indent: 0

Current context (10 lines before/after):
```
  1380 |    * :dp:`fls_irdKqoYzBM0M`
  1381 |      If the :t:`use import` is a :t:`nesting import` then start with the
  1382 |      :t:`[path segment]s` of the :t:`nesting import`'s :t:`simple path prefix`.
  1383 | 
  1384 | #. :dp:`fls_gAWsqibl4GLq`
  1385 |    Then if the current :t:`use import` is the child of a :t:`nesting import`,
  1386 |    prepend the :t:`nesting import`'s :t:`simple path prefix` to the
  1387 |    :t:`import path prefix`. Repeat this step with the :t:`nesting import` as
  1388 |    the current :t:`use import`.
  1389 | 
  1390 | .. glossary-entry:: renaming
  1391 |    
  1392 |    :glossary:
  1393 |      :dp:`fls_cp8u9kq44o8a`
  1394 |      A :dt:`renaming` provides an alternative :t:`name` for an existing name.
  1395 |      
  1396 |      :dp:`fls_8inznqig2ibr`
  1397 |      See :s:`Renaming`.
  1398 | 
  1399 | .. glossary-entry:: simple import
  1400 |    
  1401 |    :glossary:
  1402 |      :dp:`fls_jrlzpoauui9g`
  1403 |      A :dt:`simple import` is a :t:`use import` that binds a :t:`simple path` to a
  1404 |      local :t:`name` by using an optional :t:`renaming`.
  1405 |      
  1406 |      :dp:`fls_ta5t4h25unsw`
  1407 |      See :s:`SimpleImport`.
  1408 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_cp8u9kq44o8a`
     A :dt:`renaming` provides an alternative :t:`name` for an existing name.
     
     :dp:`fls_8inznqig2ibr`
     See :s:`Renaming`.

```

Static glossary entry:
```

:dp:`fls_cp8u9kq44o8a`
A :dt:`renaming` provides an alternative :t:`name` for an existing name.

:dp:`fls_8inznqig2ibr`
See :s:`Renaming`.
```

## 107 remainder assignment (glossary-only)
- File: src/expressions.rst:3377
- Commit: e5bd283aaeb404147ba83c2dc3fb49b413e9313f
- Indent: 0

Current context (10 lines before/after):
```
  3367 |      A :dt:`multiplication assignment expression` is a
  3368 |      :t:`compound assignment expression` that uses multiplication.
  3369 |      
  3370 |      :dp:`fls_b0dc5lec1mdc`
  3371 |      See :s:`MultiplicationAssignmentExpression`.
  3372 |    :chapter:
  3373 |      :dp:`fls_ndlv3k9uclz2`
  3374 |      A :t:`multiplication assignment expression` is a
  3375 |      :t:`compound assignment expression` that uses multiplication.
  3376 | 
  3377 | .. glossary-entry:: remainder assignment
  3378 |    
  3379 |    :glossary:
  3380 |      :dp:`fls_58eDC2XtQcaR`
  3381 |      For :dt:`remainder assignment`, see :t:`remainder assignment expression`.
  3382 | 
  3383 | .. glossary-entry:: remainder assignment expression
  3384 |    
  3385 |    :glossary:
  3386 |      :dp:`fls_en7ytqvefw7j`
  3387 |      A :dt:`remainder assignment expression` is a
  3388 |      :t:`compound assignment expression` that uses remainder division.
  3389 |      
  3390 |      :dp:`fls_rkk80quk8uzc`
  3391 |      See :s:`RemainderAssignmentExpression`.
  3392 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_58eDC2XtQcaR`
     For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

```

Static glossary entry:
```

:dp:`fls_58eDC2XtQcaR`
For :dt:`remainder assignment`, see :t:`remainder assignment expression`.
```

## 108 record enum variant (glossary-only)
- File: src/types-and-traits.rst:1005
- Commit: 3bff43ba3ae891942ed0511e29cd95174c621c92
- Indent: 0

Current context (10 lines before/after):
```
   995 |      An :dt:`enum variant` is a :t:`construct` that declares one of the
   996 |      possible variations of an :t:`enum`.
   997 |      
   998 |      :dp:`fls_tj2s55onen6b`
   999 |      See :s:`EnumVariant`.
  1000 |    :chapter:
  1001 |      :dp:`fls_wQTFwl88VujQ`
  1002 |      An :t:`enum variant` is a :t:`construct` that declares one of the
  1003 |      possible variations of an :t:`enum`.
  1004 | 
  1005 | .. glossary-entry:: record enum variant
  1006 |    
  1007 |    :glossary:
  1008 |      :dp:`fls_NWyvPQmOIjo2`
  1009 |      A :dt:`record enum variant` is an :t:`enum variant` with a
  1010 |      :s:`RecordStructFieldList`.
  1011 | 
  1012 | .. glossary-entry:: tuple enum variant
  1013 |    
  1014 |    :glossary:
  1015 |      :dp:`fls_eduQhUYBEkVx`
  1016 |      A :dt:`tuple enum variant` is an :t:`enum variant` with a
  1017 |      :s:`TupleStructFieldList`.
  1018 | 
  1019 | .. glossary-entry:: unit enum variant
  1020 |    
  1021 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_NWyvPQmOIjo2`
     A :dt:`record enum variant` is an :t:`enum variant` with a
     :s:`RecordStructFieldList`.

```

Static glossary entry:
```

:dp:`fls_NWyvPQmOIjo2`
A :dt:`record enum variant` is an :t:`enum variant` with a
:s:`RecordStructFieldList`.
```

## 109 record struct (glossary-only)
- File: src/types-and-traits.rst:1184
- Commit: 3bff43ba3ae891942ed0511e29cd95174c621c92
- Indent: 0

Current context (10 lines before/after):
```
  1174 | 
  1175 |    TupleStructFieldList ::=
  1176 |        $$($$ (TupleStructField ($$,$$ TupleStructField)* $$,$$?)? $$)$$
  1177 | 
  1178 |    TupleStructField ::=
  1179 |        OuterAttributeOrDoc* VisibilityModifier? TypeSpecification
  1180 | 
  1181 |    UnitStructDeclaration ::=
  1182 |        $$struct$$ Name GenericParameterList? WhereClause? $$;$$
  1183 | 
  1184 | .. glossary-entry:: record struct
  1185 |    
  1186 |    :glossary:
  1187 |      :dp:`fls_qyd7kqnpjs2`
  1188 |      A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.
  1189 |      
  1190 |      :dp:`fls_rqs5rdnhkwnx`
  1191 |      See :s:`RecordStructDeclaration`.
  1192 | 
  1193 | .. glossary-entry:: record struct type
  1194 |    
  1195 |    :glossary:
  1196 |      :dp:`fls_mgrz3o51gbis`
  1197 |      A :dt:`record struct type` is the :t:`type` of a :t:`record struct`.
  1198 | 
  1199 | .. glossary-entry:: record struct field
  1200 |    
  1201 |    :glossary:
  1202 |      :dp:`fls_lb0t10evec6z`
```

Glossary block (current):
```
     :dp:`fls_qyd7kqnpjs2`
     A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.
     
     :dp:`fls_rqs5rdnhkwnx`
     See :s:`RecordStructDeclaration`.

```

Static glossary entry:
```

:dp:`fls_qyd7kqnpjs2`
A :dt:`record struct` is a :t:`struct` with a :s:`RecordStructFieldList`.

:dp:`fls_rqs5rdnhkwnx`
See :s:`RecordStructDeclaration`.
```

## 110 punctuator (glossary-only)
- File: src/lexical-elements.rst:229
- Commit: 7f4ea487fa34478672e9c3c7cd6e239c788a1fce
- Indent: 0

Current context (10 lines before/after):
```
   219 |    
   220 |    :glossary:
   221 |      :dp:`fls_128xny4qfcj5`
   222 |      A :dt:`separator` is a character or a string that separates adjacent
   223 |      :t:`[lexical element]s`.
   224 |    :chapter:
   225 |      :dp:`fls_a6t53o8h1vdk`
   226 |      A :t:`separator` is a character or a string that separates adjacent :t:`[lexical
   227 |      element]s`. A :t:`whitespace string` is a :t:`separator`.
   228 | 
   229 | .. glossary-entry:: punctuator
   230 |    
   231 |    :glossary:
   232 |      :dp:`fls_gwqgi0b7jxmu`
   233 |      A :dt:`punctuator` is a character or a sequence of characters in category
   234 |      :s:`Punctuation`.
   235 | 
   236 | :dp:`fls_8fv63w6f4udl`
   237 | A :dt:`simple punctuator` is one of the following special characters:
   238 | 
   239 | .. syntax::
   240 | 
   241 |    $$+$$
   242 |    $$-$$
   243 |    $$*$$
   244 |    $$/$$
   245 |    $$%$$
```

Glossary block (current):
```
     :dp:`fls_gwqgi0b7jxmu`
     A :dt:`punctuator` is a character or a sequence of characters in category
     :s:`Punctuation`.

```

Static glossary entry:
```

:dp:`fls_gwqgi0b7jxmu`
A :dt:`punctuator` is a character or a sequence of characters in category
:s:`Punctuation`.
```

## 111 prelude entity (glossary-only)
- File: src/entities-and-resolution.rst:1248
- Commit: cf130665cd12450ccfd9e04b533c178a86e2b4f6
- Indent: 0

Current context (10 lines before/after):
```
  1238 |      A :dt:`prelude` is a collection of :t:`entities <entity>` that are
  1239 |      automatically brought :t:`in scope` of every :t:`module` in a :t:`crate`.
  1240 |    :chapter:
  1241 |      :dp:`fls_po4gw6t2ptwu`
  1242 |      A :t:`prelude` is a collection of :t:`entities <entity>` that are automatically
  1243 |      brought :t:`in scope` of every :t:`module` in a :t:`crate`. Such
  1244 |      :t:`entities <entity>` are referred to as
  1245 |      :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
  1246 |      is referred to as a :t:`prelude name`.
  1247 | 
  1248 | .. glossary-entry:: prelude entity
  1249 |    
  1250 |    :glossary:
  1251 |      :dp:`fls_2lU7RUjzFlsz`
  1252 |      A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
  1253 | 
  1254 | .. glossary-entry:: prelude name
  1255 |    
  1256 |    :glossary:
  1257 |      :dp:`fls_6Jk7fUAK122A`
  1258 |      A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.
  1259 | 
  1260 | :dp:`fls_n4102qskkmz2`
  1261 | The :dt:`core prelude` is a :t:`prelude` that brings :t:`in scope` of every
  1262 | :t:`module` all re-exported :t:`entities <entity>` from the
  1263 | :std:`core::prelude::rust_2021` :t:`module`.
```

Glossary block (current):
```
     :dp:`fls_2lU7RUjzFlsz`
     A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.

```

Static glossary entry:
```

:dp:`fls_2lU7RUjzFlsz`
A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
```

## 112 prelude name (glossary-only)
- File: src/entities-and-resolution.rst:1254
- Commit: cf130665cd12450ccfd9e04b533c178a86e2b4f6
- Indent: 0

Current context (10 lines before/after):
```
  1244 |      :t:`entities <entity>` are referred to as
  1245 |      :t:`prelude entities <prelude entity>`. The :t:`name` of a :t:`prelude entity`
  1246 |      is referred to as a :t:`prelude name`.
  1247 | 
  1248 | .. glossary-entry:: prelude entity
  1249 |    
  1250 |    :glossary:
  1251 |      :dp:`fls_2lU7RUjzFlsz`
  1252 |      A :dt:`prelude entity` is an :t:`entity` declared in a :t:`prelude`.
  1253 | 
  1254 | .. glossary-entry:: prelude name
  1255 |    
  1256 |    :glossary:
  1257 |      :dp:`fls_6Jk7fUAK122A`
  1258 |      A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.
  1259 | 
  1260 | :dp:`fls_n4102qskkmz2`
  1261 | The :dt:`core prelude` is a :t:`prelude` that brings :t:`in scope` of every
  1262 | :t:`module` all re-exported :t:`entities <entity>` from the
  1263 | :std:`core::prelude::rust_2021` :t:`module`.
  1264 | 
  1265 | :dp:`fls_atvnwly4w8g2`
  1266 | An :dt:`external prelude` is a :t:`prelude` that brings :t:`in scope` of the
  1267 | :t:`crate root module` the :t:`entities <entity>` of the :t:`[crate]s` imported
  1268 | using external :t:`[crate import]s` or supplied by a tool. If the external
  1269 | :t:`crate import` uses a :t:`renaming`, then the :t:`identifier` of the
```

Glossary block (current):
```
     :dp:`fls_6Jk7fUAK122A`
     A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.

```

Static glossary entry:
```

:dp:`fls_6Jk7fUAK122A`
A :dt:`prelude name` is a :t:`name` of a :t:`prelude entity`.
```

## 113 partially hygienic (glossary-only)
- File: src/macros.rst:1379
- Commit: cee165a9aacc28c14a1f74f573d44a90537d0dab
- Indent: 0

Current context (10 lines before/after):
```
  1369 |        :s:`MacroRulesDeclaration` site for :t:`[variable]s`, :t:`[label]s`, and the
  1370 |        ``$crate`` :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise,
  1371 |        and is considered :t:`partially hygienic`.
  1372 |      :chapter:
  1373 |        * :dp:`fls_uyvnq88y9gk3`
  1374 |          :t:`Mixed site hygiene`, which resolves to a :s:`MacroRulesDeclaration`
  1375 |          site for :t:`[label]s`, :t:`[variable]s`, and the ``$crate``
  1376 |          :t:`metavariable`, and to the :s:`MacroInvocation` site otherwise, and is
  1377 |          considered :dt:`partially hygienic`.
  1378 | 
  1379 | .. glossary-entry:: partially hygienic
  1380 |    
  1381 |    :glossary:
  1382 |      :dp:`fls_Qh8V0Y08dNoa`
  1383 |      An :t:`identifier` is :dt:`partially hygienic` when it has
  1384 |      :t:`mixed site hygiene`.
  1385 | 
  1386 | :dp:`fls_yxqcr19dig18`
  1387 | Every :t:`macro` has associated :t:`hygiene` that depends on its kind:
  1388 | 
  1389 | * :dp:`fls_kx25olky1jov`
  1390 |   :t:`[Declarative macro]s` have :t:`mixed site hygiene`.
  1391 | 
  1392 | * :dp:`fls_v46v0t2vh6x4`
  1393 |   :t:`[Procedural macro]s` have :t:`call site hygiene` and
  1394 |   :t:`mixed site hygiene` depending on the implementation of the
  1395 |   :t:`procedural macro`.
```

Glossary block (current):
```
     :dp:`fls_Qh8V0Y08dNoa`
     An :t:`identifier` is :dt:`partially hygienic` when it has
     :t:`mixed site hygiene`.

```

Static glossary entry:
```

:dp:`fls_Qh8V0Y08dNoa`
An :t:`identifier` is :dt:`partially hygienic` when it has
:t:`mixed site hygiene`.
```

## 114 numeric type (glossary-only)
- File: src/types-and-traits.rst:434
- Commit: 6d3a2bc1710e8df4fd2a8737c1b74399bb9226ab
- Indent: 0

Current context (10 lines before/after):
```
   424 | :dp:`fls_juysxea25owj`
   425 | It is a :t:`validity invariant` for a :t:`value` of :t:`type` :c:`char` to be
   426 | inside the 0x000 - 0xD7FF or the 0xE000 - 0x10FFFF inclusive ranges of
   427 | :t:`Unicode`.
   428 | 
   429 | .. _fls_qwljwqr07slp:
   430 | 
   431 | Numeric Types
   432 | ~~~~~~~~~~~~~
   433 | 
   434 | .. glossary-entry:: numeric type
   435 |    
   436 |    :glossary:
   437 |      :dp:`fls_cpdsj94l57af`
   438 |      A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.
   439 | 
   440 | .. _fls_b4xporvr64s:
   441 | 
   442 | Floating Point Types
   443 | ^^^^^^^^^^^^^^^^^^^^
   444 | 
   445 | .. rubric:: Legality Rules
   446 | 
   447 | .. glossary-entry:: floating-point type
   448 |    
   449 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_cpdsj94l57af`
     A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.

```

Static glossary entry:
```

:dp:`fls_cpdsj94l57af`
A :dt:`numeric type` is a :t:`type` whose :t:`[value]s` denote numbers.
```

## 115 object safety (glossary-only)
- File: src/types-and-traits.rst:4019
- Commit: 6d3a2bc1710e8df4fd2a8737c1b74399bb9226ab
- Indent: 0

Current context (10 lines before/after):
```
  4009 | 
  4010 |    trait Circle: Shape {
  4011 |        fn radius(&self) -> f64;
  4012 |    }
  4013 | 
  4014 | .. _fls_4ikc07mfrez5:
  4015 | 
  4016 | Object Safety
  4017 | ~~~~~~~~~~~~~
  4018 | 
  4019 | .. glossary-entry:: object safety
  4020 |    
  4021 |    :glossary:
  4022 |      :dp:`fls_vqmng1l9ab8a`
  4023 |      :dt:`Object safety` is the process of determining whether a :t:`trait` can be
  4024 |      used as a :t:`trait object type`.
  4025 | 
  4026 | .. rubric:: Legality Rules
  4027 | 
  4028 | .. glossary-entry:: object safe
  4029 |    
  4030 |    :glossary:
  4031 |      :dp:`fls_oa2jiklr5nl2`
  4032 |      A :t:`trait` is :dt:`object safe` when it can be used as a
  4033 |      :t:`trait object type`.
  4034 |    :chapter:
  4035 |      :dp:`fls_lrdki56hpc3k`
```

Glossary block (current):
```
     :dp:`fls_vqmng1l9ab8a`
     :dt:`Object safety` is the process of determining whether a :t:`trait` can be
     used as a :t:`trait object type`.

```

Static glossary entry:
```

:dp:`fls_vqmng1l9ab8a`
:dt:`Object safety` is the process of determining whether a :t:`trait` can be
used as a :t:`trait object type`.
```

## 116 named field selector (glossary-only)
- File: src/entities-and-resolution.rst:1721
- Commit: ec494261fe9c8659a7414bc1f5810f5381c4b303
- Indent: 0

Current context (10 lines before/after):
```
  1711 |    #. :dp:`fls_s14fegwhwnc8`
  1712 |       Try to locate a :t:`candidate indexed field` of the
  1713 |       :t:`candidate container type`.
  1714 | 
  1715 |    #. :dp:`fls_tfjm27ydiake`
  1716 |       If such a :t:`candidate indexed field` exists and is visible at the point
  1717 |       of the :t:`field access expression`, then the :t:`field access expression`
  1718 |       resolves to that :t:`candidate indexed field` and :t:`field resolution`
  1719 |       stops.
  1720 | 
  1721 | .. glossary-entry:: named field selector
  1722 |    
  1723 |    :glossary:
  1724 |      :dp:`fls_cczpgxqdyh1e`
  1725 |      A :dt:`named field selector` is a :t:`field selector` where the selected
  1726 |      :t:`field` is indicated by an :t:`identifier`.
  1727 |      
  1728 |      :dp:`fls_hpw0n89ez5nw`
  1729 |      See :s:`NamedFieldSelector`.
  1730 | 
  1731 | :dp:`fls_p6hgoqo0kcx`
  1732 | :t:`Field resolution` of a :t:`field access expression` with a
  1733 | :t:`named field selector` proceeds as follows:
  1734 | 
  1735 | #. :dp:`fls_e7sj392ohvbd`
  1736 |    For each :t:`candidate container type` of the
  1737 |    :t:`candidate container type chain`
  1738 | 
  1739 |    #. :dp:`fls_z6qt9obbhhcg`
  1740 |       Try to locate a :t:`candidate named field` of the
```

Glossary block (current):
```
     :dp:`fls_cczpgxqdyh1e`
     A :dt:`named field selector` is a :t:`field selector` where the selected
     :t:`field` is indicated by an :t:`identifier`.
     
     :dp:`fls_hpw0n89ez5nw`
     See :s:`NamedFieldSelector`.

```

Static glossary entry:
```

:dp:`fls_cczpgxqdyh1e`
A :dt:`named field selector` is a :t:`field selector` where the selected
:t:`field` is indicated by an :t:`identifier`.

:dp:`fls_hpw0n89ez5nw`
See :s:`NamedFieldSelector`.
```

## 117 NaN-boxing (glossary-only)
- File: src/inline-assembly.rst:661
- Commit: ec494261fe9c8659a7414bc1f5810f5381c4b303
- Indent: 0

Current context (10 lines before/after):
```
   651 |   ``freg``, then :c:`f32` :t:`[value]s` are :t:`NaN-boxed <NaN-boxing>`. in a
   652 |   :c:`f64` :t:`value`.
   653 | 
   654 | * :dp:`fls_78gb8z1fyluc`
   655 |   Otherwise, for an :t:`input register`, the upper bits of the :t:`register`
   656 |   have an undefined :t:`value`.
   657 | 
   658 | * :dp:`fls_7dii7lee457t`
   659 |   Otherwise, for an :t:`output register`, the upper bits are ignored.
   660 | 
   661 | .. glossary-entry:: NaN-boxing
   662 |    
   663 |    :glossary:
   664 |      :dp:`fls_s956sJGwOa6z`
   665 |      :dt:`NaN-boxing` is a technique for encoding :t:`[value]s` using the low order
   666 |      bits of the mantissa of a 64-bit IEEE floating-point ``NaN``.
   667 | 
   668 | :dp:`fls_ujhjocg1361b`
   669 | If a :t:`register argument` has :t:`direction modifier` ``inout`` and an
   670 | :t:`input-output register expression`, then the :t:`input register expression`
   671 | and the :t:`output register expression` shall have the same :t:`type`.
   672 | 
   673 | .. _fls_hejgghwzblf:
   674 | 
   675 | Register Arguments
   676 | ------------------
   677 | 
```

Glossary block (current):
```
     :dp:`fls_s956sJGwOa6z`
     :dt:`NaN-boxing` is a technique for encoding :t:`[value]s` using the low order
     bits of the mantissa of a 64-bit IEEE floating-point ``NaN``.

```

Static glossary entry:
```

:dp:`fls_s956sJGwOa6z`
:dt:`NaN-boxing` is a technique for encoding :t:`[value]s` using the low order
bits of the mantissa of a 64-bit IEEE floating-point ``NaN``.
```

## 118 multiplication assignment (glossary-only)
- File: src/expressions.rst:3356
- Commit: d6c89e6ea6fc940b9837807548bb9b4e3d8e999b
- Indent: 0

Current context (10 lines before/after):
```
  3346 |      A :dt:`division assignment expression` is a :t:`compound assignment expression`
  3347 |      that uses division.
  3348 |      
  3349 |      :dp:`fls_cdxt76aqwtkq`
  3350 |      See :s:`DivisionAssignmentExpression`.
  3351 |    :chapter:
  3352 |      :dp:`fls_pkzj0uigfcgm`
  3353 |      A :t:`division assignment expression` is a :t:`compound assignment expression`
  3354 |      that uses division.
  3355 | 
  3356 | .. glossary-entry:: multiplication assignment
  3357 |    
  3358 |    :glossary:
  3359 |      :dp:`fls_llUb5VHKjwW4`
  3360 |      For :dt:`multiplication assignment`, see
  3361 |      :t:`multiplication assignment expression`.
  3362 | 
  3363 | .. glossary-entry:: multiplication assignment expression
  3364 |    
  3365 |    :glossary:
  3366 |      :dp:`fls_eo9gx05n5ru3`
  3367 |      A :dt:`multiplication assignment expression` is a
  3368 |      :t:`compound assignment expression` that uses multiplication.
  3369 |      
  3370 |      :dp:`fls_b0dc5lec1mdc`
  3371 |      See :s:`MultiplicationAssignmentExpression`.
  3372 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_llUb5VHKjwW4`
     For :dt:`multiplication assignment`, see
     :t:`multiplication assignment expression`.

```

Static glossary entry:
```

:dp:`fls_llUb5VHKjwW4`
For :dt:`multiplication assignment`, see
:t:`multiplication assignment expression`.
```

## 119 mutable assignee expression (glossary-only)
- File: src/expressions.rst:3485
- Commit: d6c89e6ea6fc940b9837807548bb9b4e3d8e999b
- Indent: 0

Current context (10 lines before/after):
```
  3475 |      A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
  3476 |      is used in the calculation of a :t:`compound assignment expression`.
  3477 |      
  3478 |      :dp:`fls_qnwbrwdnv7n0`
  3479 |      See :s:`ModifyingOperand`.
  3480 |    :chapter:
  3481 |      :dp:`fls_9v09ayi2azpe`
  3482 |      A :t:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
  3483 |      is used in the calculation of a :t:`compound assignment expression`.
  3484 | 
  3485 | .. glossary-entry:: mutable assignee expression
  3486 |    
  3487 |    :glossary:
  3488 |      :dp:`fls_0RSlFbwrB3gp`
  3489 |      A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
  3490 |      :t:`value` can be modified.
  3491 | 
  3492 | :dp:`fls_row7saf53vwd`
  3493 | An :t:`assigned operand` shall denote a :t:`mutable assignee expression`.
  3494 | 
  3495 | :dp:`fls_xmgcdw9yhb55`
  3496 | The :t:`type` of a :t:`compound assignment` is the :t:`unit type`.
  3497 | 
  3498 | :dp:`fls_yeh6mvyvb4dp`
  3499 | The :t:`value` of a :t:`compound assignment` is the :t:`unit value`.
  3500 | 
  3501 | :dp:`fls_657knnsobdyu`
```

Glossary block (current):
```
     :dp:`fls_0RSlFbwrB3gp`
     A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
     :t:`value` can be modified.

```

Static glossary entry:
```

:dp:`fls_0RSlFbwrB3gp`
A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
:t:`value` can be modified.
```

## 120 loop (glossary-only)
- File: src/expressions.rst:5092
- Commit: 0be1c7edc60b50ad00fc75e381e1185cf41e4d66
- Indent: 0

Current context (10 lines before/after):
```
  5082 |        ForLoopExpression
  5083 |      | InfiniteLoopExpression
  5084 |      | WhileLetLoopExpression
  5085 |      | WhileLoopExpression
  5086 | 
  5087 |    LoopBody ::=
  5088 |        BlockExpression
  5089 | 
  5090 | .. rubric:: Legality Rules
  5091 | 
  5092 | .. glossary-entry:: loop
  5093 |    
  5094 |    :glossary:
  5095 |      :dp:`fls_omjnvxva07z2`
  5096 |      For :dt:`loop`, see :t:`loop expression`.
  5097 | 
  5098 | .. glossary-entry:: loop expression
  5099 |    
  5100 |    :glossary:
  5101 |      :dp:`fls_2yypq3m1kquj`
  5102 |      A :dt:`loop expression` is an :t:`expression` that evaluates a
  5103 |      :t:`block expression` continuously as long as some criterion holds true.
  5104 |      
  5105 |      :dp:`fls_o2dyznhq7rez`
  5106 |      See :s:`LoopExpression`.
  5107 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_omjnvxva07z2`
     For :dt:`loop`, see :t:`loop expression`.

```

Static glossary entry:
```

:dp:`fls_omjnvxva07z2`
For :dt:`loop`, see :t:`loop expression`.
```

## 121 layout (glossary-only)
- File: src/types-and-traits.rst:2337
- Commit: c862c565cd8bd0fdb98c0ceb25de6192c61169dc
- Indent: 0

Current context (10 lines before/after):
```
  2327 |      - :c:`f64`
  2328 |      - 8
  2329 |    * - :dp:`fls_nyxnnlwmt5gu`
  2330 |      - :c:`char`
  2331 |      - 4
  2332 | 
  2333 | :dp:`fls_lwmrljw9m0pb`
  2334 | Types :c:`usize` and :c:`isize` have :t:`size` big enough to contain every
  2335 | address on the target platform.
  2336 | 
  2337 | .. glossary-entry:: layout
  2338 |    
  2339 |    :glossary:
  2340 |      :dp:`fls_qk602dmhc0d6`
  2341 |      :dt:`Layout` specifies the :t:`alignment`, :t:`size`, and the relative offset
  2342 |      of :t:`[field]s` in a :t:`type`.
  2343 | 
  2344 | :dp:`fls_pzi6izljfv0f`
  2345 | For :t:`type` :c:`str`, the :t:`layout` is that of :t:`slice type`
  2346 | ``[u8]``.
  2347 | 
  2348 | :dp:`fls_7cjbxleo998q`
  2349 | For :t:`array type` ``[T; N]`` where ``T`` is the :t:`element type` and ``N``
  2350 | is :t:`size operand`, the :t:`alignment` is that of ``T``, and the :t:`size` is
  2351 | calculated as ``core::mem::size_of::<T>() * N``.
  2352 | 
  2353 | :dp:`fls_veotnstzigw2`
```

Glossary block (current):
```
     :dp:`fls_qk602dmhc0d6`
     :dt:`Layout` specifies the :t:`alignment`, :t:`size`, and the relative offset
     of :t:`[field]s` in a :t:`type`.

```

Static glossary entry:
```

:dp:`fls_qk602dmhc0d6`
:dt:`Layout` specifies the :t:`alignment`, :t:`size`, and the relative offset
of :t:`[field]s` in a :t:`type`.
```

## 122 local variable (glossary-only)
- File: src/values.rst:350
- Commit: c862c565cd8bd0fdb98c0ceb25de6192c61169dc
- Indent: 0

Current context (10 lines before/after):
```
   340 |    
   341 |    :glossary:
   342 |      :dp:`fls_9ab12k4vwsio`
   343 |      A :dt:`variable` is a placeholder for a :t:`value` that is allocated on the
   344 |      stack.
   345 |    :chapter:
   346 |      :dp:`fls_hl5tnd9yy252`
   347 |      A :t:`variable` is a placeholder for a :t:`value` that is allocated on the
   348 |      stack.
   349 | 
   350 | .. glossary-entry:: local variable
   351 |    
   352 |    :glossary:
   353 |      :dp:`fls_3inlcyi6444u`
   354 |      For :dt:`local variable`, see :t:`variable`.
   355 | 
   356 | .. glossary-entry:: immutable variable
   357 |    
   358 |    :glossary:
   359 |      :dp:`fls_sdg35i92taip`
   360 |      An :dt:`immutable variable` is a :t:`variable` whose :t:`value` cannot be
   361 |      modified.
   362 | 
   363 | .. glossary-entry:: mutable variable
   364 |    
   365 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_3inlcyi6444u`
     For :dt:`local variable`, see :t:`variable`.

```

Static glossary entry:
```

:dp:`fls_3inlcyi6444u`
For :dt:`local variable`, see :t:`variable`.
```

## 123 label (glossary-only)
- File: src/expressions.rst:5511
- Commit: bc069fd463a2b1db5851cad4c7b9bb28e1eb9e4e
- Indent: 0

Current context (10 lines before/after):
```
  5501 | 
  5502 | .. rubric:: Syntax
  5503 | 
  5504 | .. syntax::
  5505 | 
  5506 |    LabelIndication ::=
  5507 |        $$'$$ NonKeywordIdentifier
  5508 | 
  5509 | .. rubric:: Legality Rules
  5510 | 
  5511 | .. glossary-entry:: label
  5512 |    
  5513 |    :glossary:
  5514 |      :dp:`fls_iAAf2rLmgmGQ`
  5515 |      A :dt:`label` is the :t:`name` of a :t:`loop expression`.
  5516 |      
  5517 |      :dp:`fls_HicurdHIiLX2`
  5518 |      See :s:`Label`.
  5519 | 
  5520 | .. glossary-entry:: label indication
  5521 |    
  5522 |    :glossary:
  5523 |      :dp:`fls_sso322p7adt0`
  5524 |      A :dt:`label indication` is a :t:`construct` that indicates a :t:`label`.
  5525 |      
  5526 |      :dp:`fls_g6iqfqooz8th`
  5527 |      See :s:`LabelIndication`.
  5528 |    :chapter:
  5529 |      :dp:`fls_tx5u743391h7`
```

Glossary block (current):
```
     :dp:`fls_iAAf2rLmgmGQ`
     A :dt:`label` is the :t:`name` of a :t:`loop expression`.
     
     :dp:`fls_HicurdHIiLX2`
     See :s:`Label`.

```

Static glossary entry:
```

:dp:`fls_iAAf2rLmgmGQ`
A :dt:`label` is the :t:`name` of a :t:`loop expression`.

:dp:`fls_HicurdHIiLX2`
See :s:`Label`.
```

## 124 item (glossary-only)
- File: src/items.rst:43
- Commit: bc069fd463a2b1db5851cad4c7b9bb28e1eb9e4e
- Indent: 0

Current context (10 lines before/after):
```
    33 |        )
    34 | 
    35 |    MacroItem ::=
    36 |        MacroRulesDeclaration
    37 |      | TerminatedMacroInvocation
    38 | 
    39 |    ItemSafety ::=
    40 |        $$unsafe$$
    41 |      | $$safe$$
    42 | 
    43 | .. glossary-entry:: item
    44 |    
    45 |    :glossary:
    46 |      :dp:`fls_2ghaujiqkhyy`
    47 |      An :dt:`item` is the most basic semantic element in program text. An item
    48 |      defines the compile- and run-time semantics of a program.
    49 |      
    50 |      :dp:`fls_xd997kd2i73a`
    51 |      See :s:`Item`.
    52 | 
    53 | .. rubric:: Legality Rules
    54 | 
    55 | :dp:`fls_s3b1cba9lfj5`
    56 | The :t:`macro expansion` of a :t:`terminated macro invocation` is treated as
    57 | zero or more :t:`[item]s` if the :t:`terminated macro invocation` appears as
    58 | an :t:`item`.
    59 | 
    60 | .. rubric:: Dynamic Semantics
    61 | 
    62 | :dp:`fls_hil5f7y4xdhe`
```

Glossary block (current):
```
     :dp:`fls_2ghaujiqkhyy`
     An :dt:`item` is the most basic semantic element in program text. An item
     defines the compile- and run-time semantics of a program.
     
     :dp:`fls_xd997kd2i73a`
     See :s:`Item`.

```

Static glossary entry:
```

:dp:`fls_2ghaujiqkhyy`
An :dt:`item` is the most basic semantic element in program text. An item
defines the compile- and run-time semantics of a program.

:dp:`fls_xd997kd2i73a`
See :s:`Item`.
```

## 125 initialization type (glossary-only)
- File: src/associated-items.rst:95
- Commit: 59827bd9324eed4f4c29ed86c4861e79c94f3a1a
- Indent: 0

Current context (10 lines before/after):
```
    85 |      An :t:`associated type` is a :t:`type alias` that appears as an
    86 |      :t:`associated item`.
    87 | 
    88 | .. glossary-entry:: incomplete associated type
    89 |    
    90 |    :glossary:
    91 |      :dp:`fls_tka0gth8rc9x`
    92 |      An :dt:`incomplete associated type` is an :t:`associated type` without an
    93 |      :t:`initialization type`.
    94 | 
    95 | .. glossary-entry:: initialization type
    96 |    
    97 |    :glossary:
    98 |      :dp:`fls_crn87nne7k38`
    99 |      An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
   100 |      :t:`name` for.
   101 |      
   102 |      :dp:`fls_3r85y1lh1oxo`
   103 |      See :s:`InitializationType`.
   104 | 
   105 | :dp:`fls_w8nu8suy7t5`
   106 | An :t:`associated type` shall not be used in the :t:`path expression` of a
   107 | :t:`struct expression`.
   108 | 
   109 | :dp:`fls_wasocqdnuzd1`
   110 | An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
   111 | :t:`associated trait type`.
   112 | 
   113 | .. glossary-entry:: generic associated type
   114 |    
```

Glossary block (current):
```
     :dp:`fls_crn87nne7k38`
     An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
     :t:`name` for.
     
     :dp:`fls_3r85y1lh1oxo`
     See :s:`InitializationType`.

```

Static glossary entry:
```

:dp:`fls_crn87nne7k38`
An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
:t:`name` for.

:dp:`fls_3r85y1lh1oxo`
See :s:`InitializationType`.
```

## 126 initialization expression (glossary-only)
- File: src/expressions.rst:3127
- Commit: 59827bd9324eed4f4c29ed86c4861e79c94f3a1a
- Indent: 0

Current context (10 lines before/after):
```
  3117 |   An :t:`underscore expression` corresponds to an :t:`underscore pattern`.
  3118 | 
  3119 | :dp:`fls_4bb07tn28ivw`
  3120 | The :t:`pattern` that corresponds to a :t:`destructuring assignment` shall be
  3121 | an :t:`irrefutable pattern`.
  3122 | 
  3123 | :dp:`fls_g80a92tr2ser`
  3124 | A :t:`destructuring assignment` is equivalent to a :t:`block expression` of the
  3125 | following form:
  3126 | 
  3127 | .. glossary-entry:: initialization expression
  3128 |    
  3129 |    :glossary:
  3130 |      :dp:`fls_KUeiSByPUc4w`
  3131 |      An :dt:`initialization expression` is either a :t:`constant initializer` or a
  3132 |      :t:`static initializer`.
  3133 | 
  3134 | * :dp:`fls_u0iqhbw37xvq`
  3135 |   The first :t:`statement` is a :t:`let statement` with its :t:`pattern`
  3136 |   equivalent to the lowered :t:`assignee pattern` and its
  3137 |   :t:`initialization expression` equivalent to the :t:`value operand`.
  3138 | 
  3139 | * :dp:`fls_wsfhd3udt6fq`
  3140 |   Then each bound :t:`identifier` of the :t:`assignee pattern` is an
  3141 |   :t:`assignment expression` used as a :t:`statement`, as follows:
  3142 | 
  3143 | * :dp:`fls_ll6h6qcaos65`
```

Glossary block (current):
```
     :dp:`fls_KUeiSByPUc4w`
     An :dt:`initialization expression` is either a :t:`constant initializer` or a
     :t:`static initializer`.

```

Static glossary entry:
```

:dp:`fls_KUeiSByPUc4w`
An :dt:`initialization expression` is either a :t:`constant initializer` or a
:t:`static initializer`.
```

## 127 incomplete associated constant (glossary-only)
- File: src/associated-items.rst:52
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
    42 |    
    43 |    :glossary:
    44 |      :dp:`fls_hi9qa0k2nujb`
    45 |      An :dt:`associated constant` is a :t:`constant` that appears as an
    46 |      :t:`associated item`.
    47 |    :chapter:
    48 |      :dp:`fls_5y6ae0xqux57`
    49 |      An :t:`associated constant` is a :t:`constant` that appears as an
    50 |      :t:`associated item`.
    51 | 
    52 | .. glossary-entry:: incomplete associated constant
    53 |    
    54 |    :glossary:
    55 |      :dp:`fls_bq48gl84bul0`
    56 |      An :dt:`incomplete associated constant` is an :t:`associated constant` without
    57 |      a :t:`constant initializer`.
    58 | 
    59 | .. glossary-entry:: associated function
    60 |    
    61 |    :glossary:
    62 |      :dp:`fls_zcy5pat39bq7`
    63 |      An :dt:`associated function` is a :t:`function` that appears as an
    64 |      :t:`associated item`.
    65 |    :chapter:
    66 |      :dp:`fls_lj7492aq7fzo`
    67 |      An :t:`associated function` is a :t:`function` that appears as an
    68 |      :t:`associated item`.
```

Glossary block (current):
```
     :dp:`fls_bq48gl84bul0`
     An :dt:`incomplete associated constant` is an :t:`associated constant` without
     a :t:`constant initializer`.

```

Static glossary entry:
```

:dp:`fls_bq48gl84bul0`
An :dt:`incomplete associated constant` is an :t:`associated constant` without
a :t:`constant initializer`.
```

## 128 incomplete associated function (glossary-only)
- File: src/associated-items.rst:70
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
    60 |    
    61 |    :glossary:
    62 |      :dp:`fls_zcy5pat39bq7`
    63 |      An :dt:`associated function` is a :t:`function` that appears as an
    64 |      :t:`associated item`.
    65 |    :chapter:
    66 |      :dp:`fls_lj7492aq7fzo`
    67 |      An :t:`associated function` is a :t:`function` that appears as an
    68 |      :t:`associated item`.
    69 | 
    70 | .. glossary-entry:: incomplete associated function
    71 |    
    72 |    :glossary:
    73 |      :dp:`fls_iboondra204w`
    74 |      An :dt:`incomplete associated function` is an :t:`associated function` without
    75 |      a :t:`function body`.
    76 | 
    77 | .. glossary-entry:: associated type
    78 |    
    79 |    :glossary:
    80 |      :dp:`fls_rs0n72c2d8f`
    81 |      An :dt:`associated type` is a :t:`type alias` that appears as an
    82 |      :t:`associated item`.
    83 |    :chapter:
    84 |      :dp:`fls_8cz4rdrklaj4`
    85 |      An :t:`associated type` is a :t:`type alias` that appears as an
    86 |      :t:`associated item`.
```

Glossary block (current):
```
     :dp:`fls_iboondra204w`
     An :dt:`incomplete associated function` is an :t:`associated function` without
     a :t:`function body`.

```

Static glossary entry:
```

:dp:`fls_iboondra204w`
An :dt:`incomplete associated function` is an :t:`associated function` without
a :t:`function body`.
```

## 129 immutable place expression context (glossary-only)
- File: src/expressions.rst:668
- Commit: d9a148b646fdf290cf100acab764502eb84d2180
- Indent: 0

Current context (10 lines before/after):
```
   658 | * :dp:`fls_5yXuTLQOQ3cc`
   659 |   The :t:`subject let expression` of an :t:`if let expression` or a
   660 |   :t:`while let loop expression`,
   661 | 
   662 | * :dp:`fls_nman7mJVSQlm`
   663 |   The :t:`subject expression` of a :t:`match expression`,
   664 | 
   665 | * :dp:`fls_JBfZuFDQg3mU`
   666 |   The :t:`base initializer` of a :t:`struct expression`.
   667 | 
   668 | .. glossary-entry:: immutable place expression context
   669 |    
   670 |    :glossary:
   671 |      :dp:`fls_UvrQ49dSoQGc`
   672 |      An :dt:`immutable place expression context` is a :t:`place expression context`
   673 |      whose memory location cannot be modified.
   674 | 
   675 | .. glossary-entry:: mutable place expression context
   676 |    
   677 |    :glossary:
   678 |      :dp:`fls_2ixH8LWGHi3k`
   679 |      A :dt:`mutable place expression context` is a :t:`place expression context`
   680 |      that may evaluate its :t:`operand` as a mutable memory location.
   681 |    :chapter:
   682 |      :dp:`fls_wxGAOWEVT77u`
   683 |      A :t:`mutable place expression context` is a :t:`place expression context` that
   684 |      may evaluate its :t:`operand` as a mutable memory location. The following
```

Glossary block (current):
```
     :dp:`fls_UvrQ49dSoQGc`
     An :dt:`immutable place expression context` is a :t:`place expression context`
     whose memory location cannot be modified.

```

Static glossary entry:
```

:dp:`fls_UvrQ49dSoQGc`
An :dt:`immutable place expression context` is a :t:`place expression context`
whose memory location cannot be modified.
```

## 130 i64 (glossary-only)
- File: src/types-and-traits.rst:642
- Commit: d9a148b646fdf290cf100acab764502eb84d2180
- Indent: 0

Current context (10 lines before/after):
```
   632 |      :dc:`i16` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
   633 |      :sup:`15`) to 2\ :sup:`15` - 1, all inclusive.
   634 | 
   635 | .. glossary-entry:: i32
   636 |    
   637 |    :glossary:
   638 |      :dp:`fls_yh8wzhhso4xc`
   639 |      :dc:`i32` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
   640 |      :sup:`31`) to 2\ :sup:`31` - 1, all inclusive.
   641 | 
   642 | .. glossary-entry:: i64
   643 |    
   644 |    :glossary:
   645 |      :dp:`fls_4bpatxp8yelv`
   646 |      :dc:`i64` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
   647 |      :sup:`63`) to 2\ :sup:`63` - 1, all inclusive.
   648 | 
   649 | .. glossary-entry:: i128
   650 |    
   651 |    :glossary:
   652 |      :dp:`fls_p75kpbtonb8z`
   653 |      :dc:`i128` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
   654 |      :sup:`127`) to 2\ :sup:`127` - 1, all inclusive.
   655 | 
   656 | .. glossary-entry:: isize
   657 |    
   658 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_4bpatxp8yelv`
     :dc:`i64` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
     :sup:`63`) to 2\ :sup:`63` - 1, all inclusive.

```

Static glossary entry:
```

:dp:`fls_4bpatxp8yelv`
:dc:`i64` is a :t:`signed integer type` whose :t:`[value]s` range from - (2\
:sup:`63`) to 2\ :sup:`63` - 1, all inclusive.
```

## 131 hygiene (glossary-only)
- File: src/macros.rst:1307
- Commit: 90e13856aa69709b8d3aee337224a1893ce13c47
- Indent: 0

Current context (10 lines before/after):
```
  1297 | Hygiene
  1298 | -------
  1299 | 
  1300 | :dp:`fls_7ezc7ncs678f`
  1301 | :t:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s` that appear
  1302 | within them, which aims to eliminate the syntactic interference between a
  1303 | :t:`macro` and its environment.
  1304 | 
  1305 | .. rubric:: Legality Rules
  1306 | 
  1307 | .. glossary-entry:: hygiene
  1308 |    
  1309 |    :glossary:
  1310 |      :dp:`fls_AQg0MqAQZqkz`
  1311 |      :dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
  1312 |      appear within them, which aims to eliminate the syntactic interference between
  1313 |      a :t:`macro` and its environment.
  1314 | 
  1315 | .. glossary-entry:: hygienic
  1316 |    
  1317 |    :glossary:
  1318 |      :dp:`fls_hiDddAkNH5Ms`
  1319 |      An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.
  1320 | 
  1321 | .. glossary-entry:: unhygienic
  1322 |    
  1323 |    :glossary:
  1324 |      :dp:`fls_0t4lFZLkNieR`
```

Glossary block (current):
```
     :dp:`fls_AQg0MqAQZqkz`
     :dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
     appear within them, which aims to eliminate the syntactic interference between
     a :t:`macro` and its environment.

```

Static glossary entry:
```

:dp:`fls_AQg0MqAQZqkz`
:dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
appear within them, which aims to eliminate the syntactic interference between
a :t:`macro` and its environment.
```

## 132 hygienic (glossary-only)
- File: src/macros.rst:1315
- Commit: 90e13856aa69709b8d3aee337224a1893ce13c47
- Indent: 0

Current context (10 lines before/after):
```
  1305 | .. rubric:: Legality Rules
  1306 | 
  1307 | .. glossary-entry:: hygiene
  1308 |    
  1309 |    :glossary:
  1310 |      :dp:`fls_AQg0MqAQZqkz`
  1311 |      :dt:`Hygiene` is a property of :t:`[macro]s` and :t:`[identifier]s`` that
  1312 |      appear within them, which aims to eliminate the syntactic interference between
  1313 |      a :t:`macro` and its environment.
  1314 | 
  1315 | .. glossary-entry:: hygienic
  1316 |    
  1317 |    :glossary:
  1318 |      :dp:`fls_hiDddAkNH5Ms`
  1319 |      An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.
  1320 | 
  1321 | .. glossary-entry:: unhygienic
  1322 |    
  1323 |    :glossary:
  1324 |      :dp:`fls_0t4lFZLkNieR`
  1325 |      An :t:`identifier` is :dt:`unhygienic` when it has :t:`call site hygiene`.
  1326 | 
  1327 | :dp:`fls_3axjf28xb1nt`
  1328 | :t:`Hygiene` is categorized as follows:
  1329 | 
  1330 | *
```

Glossary block (current):
```
     :dp:`fls_hiDddAkNH5Ms`
     An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.

```

Static glossary entry:
```

:dp:`fls_hiDddAkNH5Ms`
An :t:`identifier` is :dt:`hygienic` when it has :t:`definition site hygiene`.
```

## 133 function type (glossary-only)
- File: src/types-and-traits.rst:1432
- Commit: 5c37a4870b5bc04d6efb8b8ae2509a2fe02424ba
- Indent: 0

Current context (10 lines before/after):
```
  1422 |        int: i32,
  1423 |        float: f32,
  1424 |        double: f64
  1425 |    }
  1426 | 
  1427 | .. _fls_hbbek3z4wtcs:
  1428 | 
  1429 | Function Types
  1430 | --------------
  1431 | 
  1432 | .. glossary-entry:: function type
  1433 |    
  1434 |    :glossary:
  1435 |      :dp:`fls_4e19116glgtv`
  1436 |      A :dt:`function type` is either a :t:`closure type` or a
  1437 |      :t:`function item type`.
  1438 | 
  1439 | .. _fls_xd2oxlebhs14:
  1440 | 
  1441 | Closure Types
  1442 | ~~~~~~~~~~~~~
  1443 | 
  1444 | .. rubric:: Legality Rules
  1445 | 
  1446 | .. glossary-entry:: closure type
  1447 |    
  1448 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_4e19116glgtv`
     A :dt:`function type` is either a :t:`closure type` or a
     :t:`function item type`.

```

Static glossary entry:
```

:dp:`fls_4e19116glgtv`
A :dt:`function type` is either a :t:`closure type` or a
:t:`function item type`.
```

## 134 function pointer type parameter (glossary-only)
- File: src/types-and-traits.rst:1592
- Commit: 5c37a4870b5bc04d6efb8b8ae2509a2fe02424ba
- Indent: 0

Current context (10 lines before/after):
```
  1582 |    FunctionPointerTypeParameterList ::=
  1583 |        FunctionPointerTypeParameter ($$,$$ FunctionPointerTypeParameter)*
  1584 |          ($$,$$ VariadicPart | $$,$$?)
  1585 | 
  1586 |    VariadicPart ::=
  1587 |        OuterAttributeOrDoc* $$...$$
  1588 | 
  1589 |    FunctionPointerTypeParameter ::=
  1590 |        OuterAttributeOrDoc* (IdentifierOrUnderscore $$:$$)? TypeSpecification
  1591 | 
  1592 | .. glossary-entry:: function pointer type parameter
  1593 |    
  1594 |    :glossary:
  1595 |      :dp:`fls_nF1k90JJWq2K`
  1596 |      A :dt:`function pointer type parameter` is a :t:`function parameter` of a
  1597 |      :t:`function pointer type`.
  1598 |      
  1599 |      :dp:`fls_vvy6qogy0xnb`
  1600 |      See :s:`FunctionPointerTypeParameter`.
  1601 | 
  1602 | .. rubric:: Legality Rules
  1603 | 
  1604 | .. glossary-entry:: function pointer type
  1605 |    
  1606 |    :glossary:
  1607 |      :dp:`fls_lcawg25xhblx`
  1608 |      A :dt:`function pointer type` is an :t:`indirection type` that refers to a
  1609 |      :t:`function`.
  1610 |      
  1611 |      :dp:`fls_t50umpk5abjy`
```

Glossary block (current):
```
     :dp:`fls_nF1k90JJWq2K`
     A :dt:`function pointer type parameter` is a :t:`function parameter` of a
     :t:`function pointer type`.
     
     :dp:`fls_vvy6qogy0xnb`
     See :s:`FunctionPointerTypeParameter`.

```

Static glossary entry:
```

:dp:`fls_nF1k90JJWq2K`
A :dt:`function pointer type parameter` is a :t:`function parameter` of a
:t:`function pointer type`.

:dp:`fls_vvy6qogy0xnb`
See :s:`FunctionPointerTypeParameter`.
```

## 135 field index (glossary-only)
- File: src/expressions.rst:4827
- Commit: 200bda31f096cf2c311953ddbd51a7cbd2957307
- Indent: 0

Current context (10 lines before/after):
```
  4817 | .. glossary-entry:: indexed field selector
  4818 |    
  4819 |    :glossary:
  4820 |      :dp:`fls_u6mh5yediub`
  4821 |      An :dt:`indexed field selector` is a :t:`field selector` where the selected
  4822 |      :t:`field` is indicated by an index.
  4823 |      
  4824 |      :dp:`fls_wbbyf2szc8a7`
  4825 |      See :s:`IndexedFieldSelector`.
  4826 | 
  4827 | .. glossary-entry:: field index
  4828 |    
  4829 |    :glossary:
  4830 |      :dp:`fls_6061r871qgbj`
  4831 |      A :dt:`field index` is the position of a :t:`field` within a
  4832 |      :t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
  4833 |      :t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
  4834 |      
  4835 |      :dp:`fls_IDYKXUIL845x`
  4836 |      See :s:`FieldIndex`.
  4837 | 
  4838 | .. glossary-entry:: selected field
  4839 |    
  4840 |    :glossary:
  4841 |      :dp:`fls_8otlvwlqrd4e`
  4842 |      A :dt:`selected field` is a :t:`field` that is selected by a
  4843 |      :t:`field access expression`.
  4844 |    :chapter:
  4845 |      :dp:`fls_qqrconpa92i3`
  4846 |      A :t:`selected field` is a :t:`field` that is selected by a
  4847 |      :t:`field access expression`.
```

Glossary block (current):
```
     :dp:`fls_6061r871qgbj`
     A :dt:`field index` is the position of a :t:`field` within a
     :t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
     :t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
     
     :dp:`fls_IDYKXUIL845x`
     See :s:`FieldIndex`.

```

Static glossary entry:
```

:dp:`fls_6061r871qgbj`
A :dt:`field index` is the position of a :t:`field` within a
:t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
:t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.

:dp:`fls_IDYKXUIL845x`
See :s:`FieldIndex`.
```

## 136 for loop (glossary-only)
- File: src/expressions.rst:5174
- Commit: 200bda31f096cf2c311953ddbd51a7cbd2957307
- Indent: 0

Current context (10 lines before/after):
```
  5164 | 
  5165 | .. rubric:: Syntax
  5166 | 
  5167 | .. syntax::
  5168 | 
  5169 |    ForLoopExpression ::=
  5170 |        $$for$$ Pattern $$in$$ SubjectExpression LoopBody
  5171 | 
  5172 | .. rubric:: Legality Rules
  5173 | 
  5174 | .. glossary-entry:: for loop
  5175 |    
  5176 |    :glossary:
  5177 |      :dp:`fls_gmhh56arsbw8`
  5178 |      For :dt:`for loop`, see :t:`for loop expression`.
  5179 | 
  5180 | .. glossary-entry:: for loop expression
  5181 |    
  5182 |    :glossary:
  5183 |      :dp:`fls_f0gp7qxoc4o4`
  5184 |      A :dt:`for loop expression` is a :t:`loop expression` that continues to
  5185 |      evaluate its :t:`loop body` as long as its :t:`subject expression` yields a
  5186 |      :t:`value`.
  5187 |      
  5188 |      :dp:`fls_yn4d35pvmn87`
  5189 |      See :s:`ForLoopExpression`.
```

Glossary block (current):
```
     :dp:`fls_gmhh56arsbw8`
     For :dt:`for loop`, see :t:`for loop expression`.

```

Static glossary entry:
```

:dp:`fls_gmhh56arsbw8`
For :dt:`for loop`, see :t:`for loop expression`.
```

## 137 executed (glossary-only)
- File: src/statements.rst:80
- Commit: 862a461cc68af536cc2c77e242b5ceb330e641c2
- Indent: 0

Current context (10 lines before/after):
```
    70 |    
    71 |    :glossary:
    72 |      :dp:`fls_e5jbii84hd5g`
    73 |      :dt:`Execution` is the process by which a :t:`statement` achieves its runtime
    74 |      effects.
    75 |    :chapter:
    76 |      :dp:`fls_estqu395zxgk`
    77 |      :t:`Execution` is the process by which a :t:`statement` achieves its runtime
    78 |      effects.
    79 | 
    80 | .. glossary-entry:: executed
    81 |    
    82 |    :glossary:
    83 |      :dp:`fls_kelmsc68lyf7`
    84 |      See :t:`execution`.
    85 | 
    86 | :dp:`fls_dl763ssb54q1`
    87 | The :t:`execution` of an :t:`empty statement` has no effect.
    88 | 
    89 | .. _fls_yivm43r5wnp1:
    90 | 
    91 | Let Statements
    92 | --------------
    93 | 
    94 | .. rubric:: Syntax
    95 | 
```

Glossary block (current):
```
     :dp:`fls_kelmsc68lyf7`
     See :t:`execution`.

```

Static glossary entry:
```

:dp:`fls_kelmsc68lyf7`
See :t:`execution`.
```

## 138 fat pointer (glossary-only)
- File: src/types-and-traits.rst:2255
- Commit: 862a461cc68af536cc2c77e242b5ceb330e641c2
- Indent: 0

Current context (10 lines before/after):
```
  2245 |      :dp:`fls_i2j0u4v5o1bs`
  2246 |      A :dt:`thin pointer` is a :t:`value` of a :t:`thin pointer type`.
  2247 | 
  2248 | .. glossary-entry:: thin pointer type
  2249 |    
  2250 |    :glossary:
  2251 |      :dp:`fls_33rka3kyxgrk`
  2252 |      A :dt:`thin pointer type` is an :t:`indirection type` that refers to a
  2253 |      :t:`fixed sized type`.
  2254 | 
  2255 | .. glossary-entry:: fat pointer
  2256 |    
  2257 |    :glossary:
  2258 |      :dp:`fls_knbc2jv5c5ds`
  2259 |      A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
  2260 | 
  2261 | .. glossary-entry:: fat pointer type
  2262 |    
  2263 |    :glossary:
  2264 |      :dp:`fls_l8ew6udd79hh`
  2265 |      A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
  2266 |    :chapter:
  2267 |      :dp:`fls_ozYgHEHFTT5c`
  2268 |      A :dt:`fat pointer type` is an :t:`indirection type` whose contained :t:`type specification` is a :t:`dynamically sized type`.
  2269 | 
  2270 | .. glossary-entry:: alignment
```

Glossary block (current):
```
     :dp:`fls_knbc2jv5c5ds`
     A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.

```

Static glossary entry:
```

:dp:`fls_knbc2jv5c5ds`
A :dt:`fat pointer` is a :t:`value` of a :t:`fat pointer type`.
```

## 139 evaluated (glossary-only)
- File: src/expressions.rst:213
- Commit: 9a978c3837abf7f7ac0c77834d8f0ae4e52e11a5
- Indent: 0

Current context (10 lines before/after):
```
   203 |    
   204 |    :glossary:
   205 |      :dp:`fls_8zmtio6razl1`
   206 |      :dt:`Evaluation` is the process by which an :t:`expression` achieves its
   207 |      runtime effects.
   208 |    :chapter:
   209 |      :dp:`fls_1223lwh4nq49`
   210 |      :t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
   211 |      effects.
   212 | 
   213 | .. glossary-entry:: evaluated
   214 |    
   215 |    :glossary:
   216 |      :dp:`fls_769tm6hn9g5e`
   217 |      See :t:`evaluation`.
   218 | 
   219 | .. _fls_isyftqu120l:
   220 | 
   221 | Expression Classification
   222 | -------------------------
   223 | 
   224 | .. _fls_3ut3biyra4r9:
   225 | 
   226 | Assignee Expressions
   227 | ~~~~~~~~~~~~~~~~~~~~
   228 | 
```

Glossary block (current):
```
     :dp:`fls_769tm6hn9g5e`
     See :t:`evaluation`.

```

Static glossary entry:
```

:dp:`fls_769tm6hn9g5e`
See :t:`evaluation`.
```

## 140 escaped character (glossary-only)
- File: src/general.rst:275
- Commit: 9a978c3837abf7f7ac0c77834d8f0ae4e52e11a5
- Indent: 0

Current context (10 lines before/after):
```
   265 | The context-free syntax of Rust is described using a simple variant of the
   266 | Backus-Naur form. In particular:
   267 | 
   268 | .. glossary-entry:: syntactic category
   269 |    
   270 |    :glossary:
   271 |      :dp:`fls_f981e3m7kq50`
   272 |      A :dt:`syntactic category` is a nonterminal in the Backus-Naur Form grammar
   273 |      definition of the Rust programming language.
   274 | 
   275 | .. glossary-entry:: escaped character
   276 |    
   277 |    :glossary:
   278 |      :dp:`fls_7yvnbakmo7y5`
   279 |      An :dt:`escaped character` is the textual representation for a character with
   280 |      special meaning. An escaped character consists of character 0x5C (reverse
   281 |      solidus), followed by the single character encoding of the special meaning
   282 |      character. For example, ``\t`` is the escaped character for 0x09 (horizontal
   283 |      tabulation).
   284 | 
   285 | * :dp:`fls_98fm7z04lq9`
   286 |   A ``monospaced`` font is used to denote Rust syntax.
   287 | 
   288 | * :dp:`fls_ceb5a8t6cakr`
   289 |   Words in PascalCase font are used to denote a syntactic category, for example:
   290 | 
   291 | .. syntax::
   292 | 
   293 |    FloatExponent
   294 | 
```

Glossary block (current):
```
     :dp:`fls_7yvnbakmo7y5`
     An :dt:`escaped character` is the textual representation for a character with
     special meaning. An escaped character consists of character 0x5C (reverse
     solidus), followed by the single character encoding of the special meaning
     character. For example, ``\t`` is the escaped character for 0x09 (horizontal
     tabulation).

```

Static glossary entry:
```

:dp:`fls_7yvnbakmo7y5`
An :dt:`escaped character` is the textual representation for a character with
special meaning. An escaped character consists of character 0x5C (reverse
solidus), followed by the single character encoding of the special meaning
character. For example, ``\t`` is the escaped character for 0x09 (horizontal
tabulation).
```

## 141 division assignment (glossary-only)
- File: src/expressions.rst:3336
- Commit: 869af9cc64a5433bcd5231e13ad53210e88a97ff
- Indent: 0

Current context (10 lines before/after):
```
  3326 |      A :dt:`bit xor assignment expression` is a :t:`compound assignment expression`
  3327 |      that uses bit exclusive or arithmetic.
  3328 |      
  3329 |      :dp:`fls_lcrd0birf0un`
  3330 |      See :s:`BitXorAssignmentExpression`.
  3331 |    :chapter:
  3332 |      :dp:`fls_lkjwyy78m2vx`
  3333 |      A :t:`bit xor assignment expression` is a :t:`compound assignment expression`
  3334 |      that uses bit exclusive or arithmetic.
  3335 | 
  3336 | .. glossary-entry:: division assignment
  3337 |    
  3338 |    :glossary:
  3339 |      :dp:`fls_kvQskrzE1y97`
  3340 |      For :dt:`division assignment`, see :t:`division assignment expression`.
  3341 | 
  3342 | .. glossary-entry:: division assignment expression
  3343 |    
  3344 |    :glossary:
  3345 |      :dp:`fls_lzuz5fkveikk`
  3346 |      A :dt:`division assignment expression` is a :t:`compound assignment expression`
  3347 |      that uses division.
  3348 |      
  3349 |      :dp:`fls_cdxt76aqwtkq`
  3350 |      See :s:`DivisionAssignmentExpression`.
  3351 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_kvQskrzE1y97`
     For :dt:`division assignment`, see :t:`division assignment expression`.

```

Static glossary entry:
```

:dp:`fls_kvQskrzE1y97`
For :dt:`division assignment`, see :t:`division assignment expression`.
```

## 142 discriminant initializer (glossary-only)
- File: src/types-and-traits.rst:1063
- Commit: 869af9cc64a5433bcd5231e13ad53210e88a97ff
- Indent: 0

Current context (10 lines before/after):
```
  1053 | 
  1054 | .. glossary-entry:: discriminant
  1055 |    
  1056 |    :glossary:
  1057 |      :dp:`fls_dfegy9y6awx`
  1058 |      A :dt:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
  1059 |    :chapter:
  1060 |      :dp:`fls_t4yeovFm83Wo`
  1061 |      A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.
  1062 | 
  1063 | .. glossary-entry:: discriminant initializer
  1064 |    
  1065 |    :glossary:
  1066 |      :dp:`fls_o7hihgcqmnyc`
  1067 |      A :dt:`discriminant initializer` provides the :t:`value` of a :t:`discriminant`.
  1068 |      
  1069 |      :dp:`fls_g5obc23vigng`
  1070 |      See :s:`DiscriminantInitializer`.
  1071 | 
  1072 | :dp:`fls_hp5frc752dam`
  1073 | A :t:`discriminant initializer` shall be specified only when all :t:`[enum
  1074 | variant]s` appear without an :s:`EnumVariantKind`.
  1075 | 
  1076 | :dp:`fls_pijczoq4k9ij`
  1077 | The :t:`type` of the :t:`expression` of a :t:`discriminant initializer` shall
  1078 | be either:
  1079 | 
  1080 | * :dp:`fls_x7nh42on06bg`
  1081 |   The :t:`type` of the :t:`primitive representation` specified by :t:`attribute`
```

Glossary block (current):
```
     :dp:`fls_o7hihgcqmnyc`
     A :dt:`discriminant initializer` provides the :t:`value` of a :t:`discriminant`.
     
     :dp:`fls_g5obc23vigng`
     See :s:`DiscriminantInitializer`.

```

Static glossary entry:
```

:dp:`fls_o7hihgcqmnyc`
A :dt:`discriminant initializer` provides the :t:`value` of a :t:`discriminant`.

:dp:`fls_g5obc23vigng`
See :s:`DiscriminantInitializer`.
```

## 143 dereference (glossary-only)
- File: src/expressions.rst:1430
- Commit: 441f3fd3c0241e9e5d92b270603f7d9aa8e30195
- Indent: 0

Current context (10 lines before/after):
```
  1420 |      A :dt:`dereference expression` is an :t:`expression` that obtains the
  1421 |      pointed-to memory location of its :t:`operand`.
  1422 |      
  1423 |      :dp:`fls_hx0jwahdb1nf`
  1424 |      See :s:`DereferenceExpression`.
  1425 |    :chapter:
  1426 |      :dp:`fls_f6wktzofzdn1`
  1427 |      A :t:`dereference expression` is an :t:`expression` that obtains the pointed-to
  1428 |      memory location of its :t:`operand`.
  1429 | 
  1430 | .. glossary-entry:: dereference
  1431 |    
  1432 |    :glossary:
  1433 |      :dp:`fls_hk97pb1qt04y`
  1434 |      A :dt:`dereference` is the memory location produced by evaluating a
  1435 |      :t:`dereference expression`.
  1436 | 
  1437 | :dp:`fls_aeh5pzpcjveq`
  1438 | When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
  1439 | type`, the :t:`dereference expression` denotes the pointed-to memory location of
  1440 | the :t:`operand`, or the :t:`dereference` of the :t:`operand`.
  1441 | 
  1442 | :dp:`fls_9cc0ml2sru6x`
  1443 | The :t:`dereference` is assignable when the :t:`dereference expression` is a
  1444 | :t:`mutable place expression`.
  1445 | 
  1446 | :dp:`fls_8i4jzksxlrw0`
```

Glossary block (current):
```
     :dp:`fls_hk97pb1qt04y`
     A :dt:`dereference` is the memory location produced by evaluating a
     :t:`dereference expression`.

```

Static glossary entry:
```

:dp:`fls_hk97pb1qt04y`
A :dt:`dereference` is the memory location produced by evaluating a
:t:`dereference expression`.
```

## 144 dangling (glossary-only)
- File: src/expressions.rst:1488
- Commit: 441f3fd3c0241e9e5d92b270603f7d9aa8e30195
- Indent: 0

Current context (10 lines before/after):
```
  1478 | * :dp:`fls_fyend8kkpqq4`
  1479 |   Otherwise the :t:`value` is the result of evaluating :t:`expression`
  1480 |   ``*core::ops::Deref::deref(&operand)`` or :t:`expression`
  1481 |   ``*core::ops::DerefMut::deref_mut(&mut operand)`` respectively.
  1482 | 
  1483 | .. rubric:: Dynamic Semantics
  1484 | 
  1485 | :dp:`fls_72bpdsxxbgeq`
  1486 | The :t:`evaluation` of a :t:`dereference expression` evaluates its :t:`operand`.
  1487 | 
  1488 | .. glossary-entry:: dangling
  1489 |    
  1490 |    :glossary:
  1491 |      :dp:`fls_lq2urzh7bzxx`
  1492 |      A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
  1493 |      :c:`null` or not all of the bytes at the referred memory location are part of
  1494 |      the same allocation.
  1495 | 
  1496 | .. rubric:: Undefined Behavior
  1497 | 
  1498 | :dp:`fls_9wgldua1u8yt`
  1499 | It is undefined behavior to dereference a :t:`raw pointer` that is either
  1500 | :t:`dangling` or unaligned.
  1501 | 
  1502 | .. rubric:: Examples
  1503 | 
  1504 | :dp:`fls_9ifaterm8nop`
  1505 | See :p:`fls_350qejoq9i23` for the declaration of ``ref_answer``.
```

Glossary block (current):
```
     :dp:`fls_lq2urzh7bzxx`
     A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
     :c:`null` or not all of the bytes at the referred memory location are part of
     the same allocation.

```

Static glossary entry:
```

:dp:`fls_lq2urzh7bzxx`
A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
:c:`null` or not all of the bytes at the referred memory location are part of
the same allocation.
```

## 145 conditional compilation (glossary-only)
- File: src/attributes.rst:941
- Commit: 7a54fff856ad2552c39e0671562f762f893cbbde
- Indent: 0

Current context (10 lines before/after):
```
   931 | It is a :t:`safety invariant` for the :t:`function body` to respect the :t:`ABI` of the function.
   932 | 
   933 | :dp:`fls_wGbJrz4OpKKb`
   934 | It is a :t:`safety invariant` for the :t:`function body` to :t:`diverge <diverging expression>`.
   935 | 
   936 | .. _fls_cdx9zb1yxcc8:
   937 | 
   938 | Conditional Compilation Attributes
   939 | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   940 | 
   941 | .. glossary-entry:: conditional compilation
   942 |    
   943 |    :glossary:
   944 |      :dp:`fls_xymops69eer3`
   945 |      :dt:`Conditional compilation` is the process of compiling
   946 |      :t:`conditionally-compiled source code`.
   947 | 
   948 | .. glossary-entry:: conditionally-compiled source code
   949 |    
   950 |    :glossary:
   951 |      :dp:`fls_hs4lnrdxpj2g`
   952 |      :dt:`Conditionally-compiled source code` is source code that may or may not be
   953 |      considered a part of a Rust program depending on certain conditions.
   954 | 
   955 | .. _fls_fymvsy6ig99a:
   956 | 
   957 | Attribute ``cfg``
```

Glossary block (current):
```
     :dp:`fls_xymops69eer3`
     :dt:`Conditional compilation` is the process of compiling
     :t:`conditionally-compiled source code`.

```

Static glossary entry:
```

:dp:`fls_xymops69eer3`
:dt:`Conditional compilation` is the process of compiling
:t:`conditionally-compiled source code`.
```

## 146 conditionally-compiled source code (glossary-only)
- File: src/attributes.rst:948
- Commit: 7a54fff856ad2552c39e0671562f762f893cbbde
- Indent: 0

Current context (10 lines before/after):
```
   938 | Conditional Compilation Attributes
   939 | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   940 | 
   941 | .. glossary-entry:: conditional compilation
   942 |    
   943 |    :glossary:
   944 |      :dp:`fls_xymops69eer3`
   945 |      :dt:`Conditional compilation` is the process of compiling
   946 |      :t:`conditionally-compiled source code`.
   947 | 
   948 | .. glossary-entry:: conditionally-compiled source code
   949 |    
   950 |    :glossary:
   951 |      :dp:`fls_hs4lnrdxpj2g`
   952 |      :dt:`Conditionally-compiled source code` is source code that may or may not be
   953 |      considered a part of a Rust program depending on certain conditions.
   954 | 
   955 | .. _fls_fymvsy6ig99a:
   956 | 
   957 | Attribute ``cfg``
   958 | ^^^^^^^^^^^^^^^^^
   959 | 
   960 | .. rubric:: Syntax
   961 | 
   962 | .. syntax::
   963 | 
   964 |    CfgContent ::=
```

Glossary block (current):
```
     :dp:`fls_hs4lnrdxpj2g`
     :dt:`Conditionally-compiled source code` is source code that may or may not be
     considered a part of a Rust program depending on certain conditions.

```

Static glossary entry:
```

:dp:`fls_hs4lnrdxpj2g`
:dt:`Conditionally-compiled source code` is source code that may or may not be
considered a part of a Rust program depending on certain conditions.
```

## 147 compound assignment (glossary-only)
- File: src/expressions.rst:3270
- Commit: 00dc1831813a3212fa587b2ab379dae2b23ed81a
- Indent: 0

Current context (10 lines before/after):
```
  3260 |    :glossary:
  3261 |      :dp:`fls_21iFIDCu7Pk4`
  3262 |      For :dt:`bit or assignment`, see :t:`bit or assignment expression`.
  3263 | 
  3264 | .. glossary-entry:: bit xor assignment
  3265 |    
  3266 |    :glossary:
  3267 |      :dp:`fls_VJpCPVCuszs1`
  3268 |      For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.
  3269 | 
  3270 | .. glossary-entry:: compound assignment
  3271 |    
  3272 |    :glossary:
  3273 |      :dp:`fls_lGV9QvCmYGcH`
  3274 |      For :dt:`compound assignment`, see :t:`compound assignment expression`.
  3275 | 
  3276 | .. rubric:: Legality Rules
  3277 | 
  3278 | .. glossary-entry:: compound assignment expression
  3279 |    
  3280 |    :glossary:
  3281 |      :dp:`fls_mkxpk2jhe5s0`
  3282 |      A :dt:`compound assignment expression` is an expression that first computes
  3283 |      a :t:`value` from two :t:`[operand]s` and then assigns the value to an
  3284 |      :t:`assigned operand`.
  3285 |      
```

Glossary block (current):
```
     :dp:`fls_lGV9QvCmYGcH`
     For :dt:`compound assignment`, see :t:`compound assignment expression`.

```

Static glossary entry:
```

:dp:`fls_lGV9QvCmYGcH`
For :dt:`compound assignment`, see :t:`compound assignment expression`.
```

## 148 code point (glossary-only)
- File: src/lexical-elements.rst:43
- Commit: 00dc1831813a3212fa587b2ab379dae2b23ed81a
- Indent: 0

Current context (10 lines before/after):
```
    33 |      characters and text described in the Unicode® Standard by the Unicode
    34 |      Consortium.
    35 | 
    36 | .. rubric:: Syntax
    37 | 
    38 | :dp:`fls_vfx8byq5zo8t`
    39 | A character is defined by this document for each cell in the coding space
    40 | described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
    41 | character to that cell.
    42 | 
    43 | .. glossary-entry:: code point
    44 |    
    45 |    :glossary:
    46 |      :dp:`fls_6xw8jtiomc2n`
    47 |      In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
    48 |      character.
    49 | 
    50 | .. glossary-entry:: plane
    51 |    
    52 |    :glossary:
    53 |      :dp:`fls_x1wbguoqdsf9`
    54 |      In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
    55 |      :t:`[code point]s`.
    56 | 
    57 | :dp:`fls_pvslhm3chtlb`
    58 | A :dt:`whitespace character` is one of the following characters:
    59 | 
```

Glossary block (current):
```
     :dp:`fls_6xw8jtiomc2n`
     In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
     character.

```

Static glossary entry:
```

:dp:`fls_6xw8jtiomc2n`
In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
character.
```

## 149 borrowed (glossary-only)
- File: src/expressions.rst:1290
- Commit: 98e97a8daf186436df9b7b6622aab89132b9697a
- Indent: 0

Current context (10 lines before/after):
```
  1280 |      :dp:`fls_50j167r4v61b`
  1281 |      A :t:`mutable borrow expression` is a :t:`borrow expression` that has
  1282 |      :t:`keyword` ``mut``.
  1283 | 
  1284 | :dp:`fls_ya77l2zgtilp`
  1285 | When the :t:`operand` of a :t:`borrow expression` is a :t:`place expression`,
  1286 | the :t:`borrow expression` produces a :t:`reference` to the memory location
  1287 | indicated by the :t:`operand`. The memory location is placed in a borrowed
  1288 | state, or simply :t:`borrowed`.
  1289 | 
  1290 | .. glossary-entry:: borrowed
  1291 |    
  1292 |    :glossary:
  1293 |      :dp:`fls_3gnps2s95ck4`
  1294 |      A memory location is :dt:`borrowed` when a :t:`reference` pointing to it is
  1295 |      :t:`active`.
  1296 | 
  1297 | :dp:`fls_chr03xll75d`
  1298 | The :t:`type` of a :t:`borrow expression` is determined as follows:
  1299 | 
  1300 | * :dp:`fls_5b2x5ri2w54r`
  1301 |   If the :t:`borrow expression` denotes an :t:`immutable borrow expression`, then the
  1302 |   :t:`type` is ``&T``, where ``T`` is the :t:`type` of the :t:`operand`.
  1303 | 
  1304 | * :dp:`fls_agl09ia869rk`
  1305 |   If the :t:`borrow expression` denotes a :t:`mutable borrow expression`, then the
  1306 |   :t:`type` is ``&mut T``, where ``T`` is the :t:`type` of the :t:`operand`.
```

Glossary block (current):
```
     :dp:`fls_3gnps2s95ck4`
     A memory location is :dt:`borrowed` when a :t:`reference` pointing to it is
     :t:`active`.

```

Static glossary entry:
```

:dp:`fls_3gnps2s95ck4`
A memory location is :dt:`borrowed` when a :t:`reference` pointing to it is
:t:`active`.
```

## 150 Call conformance (glossary-only)
- File: src/expressions.rst:4480
- Commit: 98e97a8daf186436df9b7b6622aab89132b9697a
- Indent: 0

Current context (10 lines before/after):
```
  4470 |      :t:`call expression`.
  4471 |      
  4472 |      :dp:`fls_w6wu4wi6srjj`
  4473 |      See :s:`CallOperand`.
  4474 |    :chapter:
  4475 |      :dp:`fls_7ql1c71eidg8`
  4476 |      A :t:`call operand` is the :t:`function` being invoked or the
  4477 |      :t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
  4478 |      by a :t:`call expression`.
  4479 | 
  4480 | .. glossary-entry:: Call conformance
  4481 |    
  4482 |    :glossary:
  4483 |      :dp:`fls_Jr1gUX7Ju4Oh`
  4484 |      :dt:`Call conformance` measures the compatibility between a set of
  4485 |      :t:`[argument operand]s` and a set if :t:`[function parameter]s` or
  4486 |      :t:`[field]s`.
  4487 | 
  4488 | .. glossary-entry:: adjusted call operand
  4489 |    
  4490 |    :glossary:
  4491 |      :dp:`fls_mchqbc64iu0u`
  4492 |      An :dt:`adjusted call operand` is a :t:`call operand` adjusted with inserted :t:`[borrow expression]s` and :t:`[dereference expression]s`.
  4493 | 
  4494 | .. glossary-entry:: tuple struct call expression
  4495 |    
  4496 |    :glossary:
  4497 |      :dp:`fls_DQaCUkskfXzk`
```

Glossary block (current):
```
     :dp:`fls_Jr1gUX7Ju4Oh`
     :dt:`Call conformance` measures the compatibility between a set of
     :t:`[argument operand]s` and a set if :t:`[function parameter]s` or
     :t:`[field]s`.

```

Static glossary entry:
```

:dp:`fls_Jr1gUX7Ju4Oh`
:dt:`Call conformance` measures the compatibility between a set of
:t:`[argument operand]s` and a set if :t:`[function parameter]s` or
:t:`[field]s`.
```

## 151 bit and assignment (glossary-only)
- File: src/expressions.rst:3252
- Commit: 48ae27979c3ba216ba39d0e1bd634784063db0d2
- Indent: 0

Current context (10 lines before/after):
```
  3242 | .. glossary-entry:: addition assignment expression
  3243 |    
  3244 |    :glossary:
  3245 |      :dp:`fls_w83tf9m7vu67`
  3246 |      An :dt:`addition assignment expression` is a
  3247 |      :t:`compound assignment expression` that uses addition.
  3248 |      
  3249 |      :dp:`fls_hihh97p0rnt8`
  3250 |      See :s:`AdditionAssignmentExpression`.
  3251 | 
  3252 | .. glossary-entry:: bit and assignment
  3253 |    
  3254 |    :glossary:
  3255 |      :dp:`fls_wIl0K7O6lTXJ`
  3256 |      For :dt:`bit and assignment`, see :t:`bit and assignment expression`.
  3257 | 
  3258 | .. glossary-entry:: bit or assignment
  3259 |    
  3260 |    :glossary:
  3261 |      :dp:`fls_21iFIDCu7Pk4`
  3262 |      For :dt:`bit or assignment`, see :t:`bit or assignment expression`.
  3263 | 
  3264 | .. glossary-entry:: bit xor assignment
  3265 |    
  3266 |    :glossary:
  3267 |      :dp:`fls_VJpCPVCuszs1`
```

Glossary block (current):
```
     :dp:`fls_wIl0K7O6lTXJ`
     For :dt:`bit and assignment`, see :t:`bit and assignment expression`.

```

Static glossary entry:
```

:dp:`fls_wIl0K7O6lTXJ`
For :dt:`bit and assignment`, see :t:`bit and assignment expression`.
```

## 152 bit or assignment (glossary-only)
- File: src/expressions.rst:3258
- Commit: 48ae27979c3ba216ba39d0e1bd634784063db0d2
- Indent: 0

Current context (10 lines before/after):
```
  3248 |      
  3249 |      :dp:`fls_hihh97p0rnt8`
  3250 |      See :s:`AdditionAssignmentExpression`.
  3251 | 
  3252 | .. glossary-entry:: bit and assignment
  3253 |    
  3254 |    :glossary:
  3255 |      :dp:`fls_wIl0K7O6lTXJ`
  3256 |      For :dt:`bit and assignment`, see :t:`bit and assignment expression`.
  3257 | 
  3258 | .. glossary-entry:: bit or assignment
  3259 |    
  3260 |    :glossary:
  3261 |      :dp:`fls_21iFIDCu7Pk4`
  3262 |      For :dt:`bit or assignment`, see :t:`bit or assignment expression`.
  3263 | 
  3264 | .. glossary-entry:: bit xor assignment
  3265 |    
  3266 |    :glossary:
  3267 |      :dp:`fls_VJpCPVCuszs1`
  3268 |      For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.
  3269 | 
  3270 | .. glossary-entry:: compound assignment
  3271 |    
  3272 |    :glossary:
  3273 |      :dp:`fls_lGV9QvCmYGcH`
```

Glossary block (current):
```
     :dp:`fls_21iFIDCu7Pk4`
     For :dt:`bit or assignment`, see :t:`bit or assignment expression`.

```

Static glossary entry:
```

:dp:`fls_21iFIDCu7Pk4`
For :dt:`bit or assignment`, see :t:`bit or assignment expression`.
```

## 153 atomic (glossary-only)
- File: src/concurrency.rst:93
- Commit: 1e900d9c4d1925a2ffb01e7d179e5a657c5a4015
- Indent: 0

Current context (10 lines before/after):
```
    83 | A :t:`sync type` shall have :t:`[value]s` that are allowed to be shared across
    84 | multiple threads at any given time without incurring data races.
    85 | 
    86 | .. _fls_vyc9vcuamlph:
    87 | 
    88 | Atomics
    89 | -------
    90 | 
    91 | .. rubric:: Legality Rules
    92 | 
    93 | .. glossary-entry:: atomic
    94 |    
    95 |    :glossary:
    96 |      :dp:`fls_9xd3m2qvqzk`
    97 |      See :t:`atomic type`.
    98 | 
    99 | .. glossary-entry:: atomic type
   100 |    
   101 |    :glossary:
   102 |      :dp:`fls_cycpv4fopgx2`
   103 |      An :dt:`atomic type` is a :t:`type` defined in :t:`module`
   104 |      :std:`core::sync::atomic`.
   105 |    :chapter:
   106 |      :dp:`fls_3pjla9s93mhd`
   107 |      An :t:`atomic type` is a :t:`type` defined in :t:`module`
   108 |      :std:`core::sync::atomic`. :t:`[Atomic type]s` provide primitive shared-memory
```

Glossary block (current):
```
     :dp:`fls_9xd3m2qvqzk`
     See :t:`atomic type`.

```

Static glossary entry:
```

:dp:`fls_9xd3m2qvqzk`
See :t:`atomic type`.
```

## 154 binary operator (glossary-only)
- File: src/expressions.rst:158
- Commit: 1e900d9c4d1925a2ffb01e7d179e5a657c5a4015
- Indent: 0

Current context (10 lines before/after):
```
   148 |    :glossary:
   149 |      :dp:`fls_3mnn1au9ob6q`
   150 |      An :dt:`operand` is an :t:`expression` nested within an expression.
   151 |      
   152 |      :dp:`fls_8299xfhdsd1`
   153 |      See :s:`Operand`.
   154 |    :chapter:
   155 |      :dp:`fls_gwgttltgjma4`
   156 |      An :t:`operand` is an :t:`expression` nested within an :t:`expression`.
   157 | 
   158 | .. glossary-entry:: binary operator
   159 |    
   160 |    :glossary:
   161 |      :dp:`fls_v0he0zp9ph7a`
   162 |      A :dt:`binary operator` is an operator that operates on two :t:`[operand]s`.
   163 | 
   164 | .. glossary-entry:: left operand
   165 |    
   166 |    :glossary:
   167 |      :dp:`fls_m821x5195ac9`
   168 |      A :dt:`left operand` is an :t:`operand` that appears on the left-hand side of a
   169 |      :t:`binary operator`.
   170 |      
   171 |      :dp:`fls_ghlbsklg7wdb`
   172 |      See :s:`LeftOperand`.
   173 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_v0he0zp9ph7a`
     A :dt:`binary operator` is an operator that operates on two :t:`[operand]s`.

```

Static glossary entry:
```

:dp:`fls_v0he0zp9ph7a`
A :dt:`binary operator` is an operator that operates on two :t:`[operand]s`.
```

## 155 assignment (glossary-only)
- File: src/expressions.rst:2953
- Commit: 73607e097ae56fe9f9e53a1b59f40bad73e0dc4a
- Indent: 0

Current context (10 lines before/after):
```
  2943 | 
  2944 | .. code-block:: rust
  2945 | 
  2946 |    answer as f64
  2947 | 
  2948 | .. _fls_y4by2i8dl05o:
  2949 | 
  2950 | Assignment Expressions
  2951 | ~~~~~~~~~~~~~~~~~~~~~~
  2952 | 
  2953 | .. glossary-entry:: assignment
  2954 |    
  2955 |    :glossary:
  2956 |      :dp:`fls_j9pyuucyplmi`
  2957 |      See :t:`assignment expression`.
  2958 | 
  2959 | .. rubric:: Syntax
  2960 | 
  2961 | .. syntax::
  2962 | 
  2963 |    AssignmentExpression ::=
  2964 |        AssigneeOperand $$=$$ ValueOperand
  2965 | 
  2966 |    AssigneeOperand ::=
  2967 |        Operand
  2968 | 
```

Glossary block (current):
```
     :dp:`fls_j9pyuucyplmi`
     See :t:`assignment expression`.

```

Static glossary entry:
```

:dp:`fls_j9pyuucyplmi`
See :t:`assignment expression`.
```

## 156 arithmetic operator (glossary-only)
- File: src/expressions.rst:1770
- Commit: e090b1deb8cce93cfb34507604463c588bb2b7c2
- Indent: 0

Current context (10 lines before/after):
```
  1760 |        LeftOperand $$*$$ RightOperand
  1761 | 
  1762 |    RemainderExpression ::=
  1763 |        LeftOperand $$%$$ RightOperand
  1764 | 
  1765 |    SubtractionExpression ::=
  1766 |        LeftOperand $$-$$ RightOperand
  1767 | 
  1768 | .. rubric:: Legality Rules
  1769 | 
  1770 | .. glossary-entry:: arithmetic operator
  1771 |    
  1772 |    :glossary:
  1773 |      :dp:`fls_Qf7DckakqvRq`
  1774 |      An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.
  1775 | 
  1776 | .. glossary-entry:: arithmetic expression
  1777 |    
  1778 |    :glossary:
  1779 |      :dp:`fls_u3z2r1fw89xo`
  1780 |      An :dt:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
  1781 |      from two :t:`[operand]s` using arithmetic.
  1782 |      
  1783 |      :dp:`fls_in59ccg4g3we`
  1784 |      See :s:`ArithmeticExpression`.
  1785 |    :chapter:
```

Glossary block (current):
```
     :dp:`fls_Qf7DckakqvRq`
     An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.

```

Static glossary entry:
```

:dp:`fls_Qf7DckakqvRq`
An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.
```

## 157 addition assignment (glossary-only)
- File: src/expressions.rst:3236
- Commit: e090b1deb8cce93cfb34507604463c588bb2b7c2
- Indent: 0

Current context (10 lines before/after):
```
  3226 | 
  3227 |    SubtractionAssignmentExpression ::=
  3228 |        AssignedOperand $$-=$$ ModifyingOperand
  3229 | 
  3230 |    AssignedOperand ::=
  3231 |        Operand
  3232 | 
  3233 |    ModifyingOperand ::=
  3234 |        Operand
  3235 | 
  3236 | .. glossary-entry:: addition assignment
  3237 |    
  3238 |    :glossary:
  3239 |      :dp:`fls_FVgKeCXlmuPe`
  3240 |      For :dt:`addition assignment`, see :t:`addition assignment expression`.
  3241 | 
  3242 | .. glossary-entry:: addition assignment expression
  3243 |    
  3244 |    :glossary:
  3245 |      :dp:`fls_w83tf9m7vu67`
  3246 |      An :dt:`addition assignment expression` is a
  3247 |      :t:`compound assignment expression` that uses addition.
  3248 |      
  3249 |      :dp:`fls_hihh97p0rnt8`
  3250 |      See :s:`AdditionAssignmentExpression`.
  3251 | 
```

Glossary block (current):
```
     :dp:`fls_FVgKeCXlmuPe`
     For :dt:`addition assignment`, see :t:`addition assignment expression`.

```

Static glossary entry:
```

:dp:`fls_FVgKeCXlmuPe`
For :dt:`addition assignment`, see :t:`addition assignment expression`.
```

## 158 incomplete associated type (glossary-only)
- File: src/associated-items.rst:88
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
    78 |    
    79 |    :glossary:
    80 |      :dp:`fls_rs0n72c2d8f`
    81 |      An :dt:`associated type` is a :t:`type alias` that appears as an
    82 |      :t:`associated item`.
    83 |    :chapter:
    84 |      :dp:`fls_8cz4rdrklaj4`
    85 |      An :t:`associated type` is a :t:`type alias` that appears as an
    86 |      :t:`associated item`.
    87 | 
    88 | .. glossary-entry:: incomplete associated type
    89 |    
    90 |    :glossary:
    91 |      :dp:`fls_tka0gth8rc9x`
    92 |      An :dt:`incomplete associated type` is an :t:`associated type` without an
    93 |      :t:`initialization type`.
    94 | 
    95 | .. glossary-entry:: initialization type
    96 |    
    97 |    :glossary:
    98 |      :dp:`fls_crn87nne7k38`
    99 |      An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
   100 |      :t:`name` for.
   101 |      
   102 |      :dp:`fls_3r85y1lh1oxo`
   103 |      See :s:`InitializationType`.
   104 | 
```

Glossary block (current):
```
     :dp:`fls_tka0gth8rc9x`
     An :dt:`incomplete associated type` is an :t:`associated type` without an
     :t:`initialization type`.

```

Static glossary entry:
```

:dp:`fls_tka0gth8rc9x`
An :dt:`incomplete associated type` is an :t:`associated type` without an
:t:`initialization type`.
```

## 159 concrete type (glossary-only)
- File: src/attributes.rst:1825
- Commit: 7a54fff856ad2552c39e0671562f762f893cbbde
- Indent: 0

Current context (10 lines before/after):
```
  1815 | 
  1816 | :dp:`fls_dfnkzj8ob3uq`
  1817 | :t:`Attribute` :c:`type_length_limit` shall apply to the
  1818 | :t:`crate root module`.
  1819 | 
  1820 | :dp:`fls_61vt1r8g51nh`
  1821 | :t:`Attribute` :dc:`type_length_limit` sets the maximum number of
  1822 | :t:`[generic substitution]s` for :t:`[type parameter]s` when constructing a
  1823 | :t:`concrete type`.
  1824 | 
  1825 | .. glossary-entry:: concrete type
  1826 |    
  1827 |    :glossary:
  1828 |      :dp:`fls_l0lr3ybgccjc`
  1829 |      A :dt:`concrete type` is a :t:`type` described by a :t:`type specification`.
  1830 | 
  1831 | .. rubric:: Examples
  1832 | 
  1833 | .. code-block:: rust
  1834 | 
  1835 |    #![type_length_limit = "42"]
  1836 | 
  1837 | .. _fls_2084b06dr0wz:
  1838 | 
  1839 | Macros Attributes
  1840 | ~~~~~~~~~~~~~~~~~
```

Glossary block (current):
```
     :dp:`fls_l0lr3ybgccjc`
     A :dt:`concrete type` is a :t:`type` described by a :t:`type specification`.

```

Static glossary entry:
```

:dp:`fls_l0lr3ybgccjc`
A :dt:`concrete type` is a :t:`type` described by a :t:`type specification`.
```

## 160 in scope (glossary-only)
- File: src/entities-and-resolution.rst:698
- Commit: 2cd6855f0662e0356bc09075d2967bc0a7ab724d
- Indent: 0

Current context (10 lines before/after):
```
   688 | .. glossary-entry:: scope
   689 |    
   690 |    :glossary:
   691 |      :dp:`fls_fachaj550cq1`
   692 |      A :dt:`scope` is a region of program text where a :t:`name` can be referred to.
   693 |    :chapter:
   694 |      :dp:`fls_5x5xykocwyiy`
   695 |      A :t:`scope` is a region of program text where an :t:`entity` can be referred
   696 |      to. An :t:`entity` is :t:`in scope` when it can be referred to.
   697 | 
   698 | .. glossary-entry:: in scope
   699 |    
   700 |    :glossary:
   701 |      :dp:`fls_sy380geqvf2l`
   702 |      A :t:`name` is :dt:`in scope` when it can be referred to.
   703 | 
   704 | .. _fls_6ozthochxz1i:
   705 | 
   706 | Binding Scopes
   707 | ~~~~~~~~~~~~~~
   708 | 
   709 | .. rubric:: Legality Rules
   710 | 
   711 | .. glossary-entry:: binding scope
   712 |    
   713 |    :glossary:
```

Glossary block (current):
```
     :dp:`fls_sy380geqvf2l`
     A :t:`name` is :dt:`in scope` when it can be referred to.

```

Static glossary entry:
```

:dp:`fls_sy380geqvf2l`
A :t:`name` is :dt:`in scope` when it can be referred to.
```

## 161 place (glossary-only)
- File: src/expressions.rst:525
- Commit: cf130665cd12450ccfd9e04b533c178a86e2b4f6
- Indent: 0

Current context (10 lines before/after):
```
   515 |   Any :t:`expression` whose :t:`evaluation` requires the :t:`evaluation` of a
   516 |   diverging :t:`subexpression` on all reachable control flow paths.
   517 | 
   518 | .. _fls_6ydylimiv553:
   519 | 
   520 | Place Expressions
   521 | ~~~~~~~~~~~~~~~~~
   522 | 
   523 | .. rubric:: Legality Rules
   524 | 
   525 | .. glossary-entry:: place
   526 |    
   527 |    :glossary:
   528 |      :dp:`fls_uCTiUBWHMPY9`
   529 |      A :dt:`place` is a location where a :t:`value` resides.
   530 | 
   531 | .. glossary-entry:: place expression
   532 |    
   533 |    :glossary:
   534 |      :dp:`fls_z6mgu2mk142r`
   535 |      A :dt:`place expression` is an :t:`expression` that represents a memory
   536 |      location.
   537 |    :chapter:
   538 |      :dp:`fls_qbrcg3cl9td`
   539 |      A :t:`place expression` is an :t:`expression` that represents a memory
   540 |      location. The following :t:`[expression]s` are :t:`[place expression]s`:
```

Glossary block (current):
```
     :dp:`fls_uCTiUBWHMPY9`
     A :dt:`place` is a location where a :t:`value` resides.

```

Static glossary entry:
```

:dp:`fls_uCTiUBWHMPY9`
A :dt:`place` is a location where a :t:`value` resides.
```

## 162 async block (glossary-only)
- File: src/expressions.rst:977
- Commit: 1e900d9c4d1925a2ffb01e7d179e5a657c5a4015
- Indent: 0

Current context (10 lines before/after):
```
   967 | 
   968 | .. rubric:: Syntax
   969 | 
   970 | .. syntax::
   971 | 
   972 |    AsyncBlockExpression ::=
   973 |        $$async$$ $$move$$? BlockExpression
   974 | 
   975 | .. rubric:: Legality Rules
   976 | 
   977 | .. glossary-entry:: async block
   978 |    
   979 |    :glossary:
   980 |      :dp:`fls_pf6lrmcjywoj`
   981 |      For :dt:`async block`, see :t:`async block expression`.
   982 | 
   983 | .. glossary-entry:: async block expression
   984 |    
   985 |    :glossary:
   986 |      :dp:`fls_p6nvfs7bfoxd`
   987 |      An :dt:`async block expression` is a :t:`block expression` that is specified
   988 |      with :t:`keyword` ``async`` and encapsulates behavior which is executed in
   989 |      an asynchronous manner.
   990 |      
   991 |      :dp:`fls_je689rormhd6`
   992 |      See :s:`AsyncBlockExpression`.
```

Glossary block (current):
```
     :dp:`fls_pf6lrmcjywoj`
     For :dt:`async block`, see :t:`async block expression`.

```

Static glossary entry:
```

:dp:`fls_pf6lrmcjywoj`
For :dt:`async block`, see :t:`async block expression`.
```

## 163 addition assignment expression (glossary-only)
- File: src/expressions.rst:3242
- Commit: e090b1deb8cce93cfb34507604463c588bb2b7c2
- Indent: 0

Current context (10 lines before/after):
```
  3232 | 
  3233 |    ModifyingOperand ::=
  3234 |        Operand
  3235 | 
  3236 | .. glossary-entry:: addition assignment
  3237 |    
  3238 |    :glossary:
  3239 |      :dp:`fls_FVgKeCXlmuPe`
  3240 |      For :dt:`addition assignment`, see :t:`addition assignment expression`.
  3241 | 
  3242 | .. glossary-entry:: addition assignment expression
  3243 |    
  3244 |    :glossary:
  3245 |      :dp:`fls_w83tf9m7vu67`
  3246 |      An :dt:`addition assignment expression` is a
  3247 |      :t:`compound assignment expression` that uses addition.
  3248 |      
  3249 |      :dp:`fls_hihh97p0rnt8`
  3250 |      See :s:`AdditionAssignmentExpression`.
  3251 | 
  3252 | .. glossary-entry:: bit and assignment
  3253 |    
  3254 |    :glossary:
  3255 |      :dp:`fls_wIl0K7O6lTXJ`
  3256 |      For :dt:`bit and assignment`, see :t:`bit and assignment expression`.
  3257 | 
  3258 | .. glossary-entry:: bit or assignment
  3259 |    
  3260 |    :glossary:
  3261 |      :dp:`fls_21iFIDCu7Pk4`
```

Glossary block (current):
```
     :dp:`fls_w83tf9m7vu67`
     An :dt:`addition assignment expression` is a
     :t:`compound assignment expression` that uses addition.
     
     :dp:`fls_hihh97p0rnt8`
     See :s:`AdditionAssignmentExpression`.

```

Static glossary entry:
```

:dp:`fls_w83tf9m7vu67`
An :dt:`addition assignment expression` is a
:t:`compound assignment expression` that uses addition.

:dp:`fls_hihh97p0rnt8`
See :s:`AdditionAssignmentExpression`.
```

## 164 bit xor assignment (glossary-only)
- File: src/expressions.rst:3264
- Commit: 48ae27979c3ba216ba39d0e1bd634784063db0d2
- Indent: 0

Current context (10 lines before/after):
```
  3254 |    :glossary:
  3255 |      :dp:`fls_wIl0K7O6lTXJ`
  3256 |      For :dt:`bit and assignment`, see :t:`bit and assignment expression`.
  3257 | 
  3258 | .. glossary-entry:: bit or assignment
  3259 |    
  3260 |    :glossary:
  3261 |      :dp:`fls_21iFIDCu7Pk4`
  3262 |      For :dt:`bit or assignment`, see :t:`bit or assignment expression`.
  3263 | 
  3264 | .. glossary-entry:: bit xor assignment
  3265 |    
  3266 |    :glossary:
  3267 |      :dp:`fls_VJpCPVCuszs1`
  3268 |      For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.
  3269 | 
  3270 | .. glossary-entry:: compound assignment
  3271 |    
  3272 |    :glossary:
  3273 |      :dp:`fls_lGV9QvCmYGcH`
  3274 |      For :dt:`compound assignment`, see :t:`compound assignment expression`.
  3275 | 
  3276 | .. rubric:: Legality Rules
  3277 | 
  3278 | .. glossary-entry:: compound assignment expression
  3279 |    
```

Glossary block (current):
```
     :dp:`fls_VJpCPVCuszs1`
     For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.

```

Static glossary entry:
```

:dp:`fls_VJpCPVCuszs1`
For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.
```

