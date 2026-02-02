# Glossary audit W

## Per-letter checklist
- Letter: W
- [ ] Reconcile W terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate W terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for W
- [ ] Update `migration-checklist.md` for all W terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint W migration`
- [ ] Letter complete

## Term checklist
- [ ] weak keyword (weak_keyword)
- [ ] where clause (where_clause)
- [ ] where clause predicate (where_clause_predicate)
- [ ] while let loop (while_let_loop)
- [ ] while let loop expression (while_let_loop_expression)
- [ ] while loop (while_loop)
- [ ] while loop expression (while_loop_expression)
- [ ] whitespace string (whitespace_string)

## weak keyword (weak_keyword)

### Before glossary entry (origin/main)

```rst
.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^

:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.

:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.
```

### After glossary entry (generated)

```rst
.. _fls_wBlX9VeS3HIS:

weak keyword
^^^^^^^^^^^^

:dp:`fls_NyuPEDifMcq2`
 A :t:`weak keyword <weak_keyword>` is a :t:`keyword` whose special meaning depends on the context.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^


:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_MQiPWNwdk95I`
A :dt:`visible empty enum variant` is an :t:`enum variant` subject to :t:`visible emptiness`.

.. _fls_HYWQ0lJS3TET:

visible empty type
^^^^^^^^^^^^^^^^^^


:dp:`fls_OLVD0u9w68Gl`
A :dt:`visible empty type` is a :t:`type` subject to :t:`visible emptiness`.

.. _fls_iplp3gvfbcpw:

weak keyword
^^^^^^^^^^^^


:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^


:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## where clause (where_clause)

### Before glossary entry (origin/main)

```rst
.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^

:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.

:dp:`fls_k32hnug33eo9`
See :s:`WhereClause`.
```

### After glossary entry (generated)

```rst
.. _fls_eI4FMBgXi1EU:

where clause
^^^^^^^^^^^^

:dp:`fls_BjWDYM9hdW1s`
 A :t:`where clause <where_clause>` is a :t:`construct` that specifies :t:`bounds <bound>` on :t:`lifetime parameters <lifetime_parameter>` and :t:`type parameters <type_parameter>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^


:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.


:dp:`fls_k32hnug33eo9`
See :s:`WhereClause`.

.. _fls_myNeYCm4VI0R:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_4hiznltf5wlu`
A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
context.


:dp:`fls_psah573fsrig`
See :s:`WeakKeyword`.

.. _fls_ew2gsg72rjxk:

where clause
^^^^^^^^^^^^


:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.


:dp:`fls_k32hnug33eo9`
See :s:`WhereClause`.

.. _fls_myNeYCm4VI0R:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## where clause predicate (where_clause_predicate)

### Before glossary entry (origin/main)

```rst
.. _fls_myNeYCm4VI0R:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.

:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.
```

### After glossary entry (generated)

```rst
.. _fls_g9b56wopOrA9:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_JRSubeUv0ACB`
 A :t:`where clause predicate <where_clause_predicate>` is either a :t:`lifetime bound predicate <lifetime_bound_predicate>` or a :t:`type bound predicate <type_bound_predicate>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.


:dp:`fls_k32hnug33eo9`
See :s:`WhereClause`.

.. _fls_myNeYCm4VI0R:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.


:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_prljyrhontzn`
A :dt:`where clause` is a :t:`construct` that specifies :t:`[bound]s` on
:t:`[lifetime parameter]s` and :t:`[type parameter]s`.


:dp:`fls_k32hnug33eo9`
See :s:`WhereClause`.

.. _fls_myNeYCm4VI0R:

where clause predicate
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.


:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

Potential context markers: here.

## while let loop (while_let_loop)

### Before glossary entry (origin/main)

```rst
.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^

:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.
```

### After glossary entry (generated)

```rst
.. _fls_czdPcFLfc7me:

while let loop
^^^^^^^^^^^^^^

:dp:`fls_7d8T1211mprg`
 For :t:`while let loop <while_let_loop>`, see :t:`while let loop expression <while_let_loop_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.


:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_0LACQVmZpDQF`
A :dt:`where clause predicate` is either a :t:`lifetime bound predicate` or a
:t:`type bound predicate`.


:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## while let loop expression (while_let_loop_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.

:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_SFujv0Oo1zBg:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wSK60ZYx6mVw`
 A :t:`while let loop expression <while_let_loop_expression>` is a :t:`loop expression <loop_expression>` that continues to evaluate its :t:`loop body <loop_body>` as long as its :t:`subject let expression <subject_let_expression>` yields a :t:`value` that can be matched against its :t:`pattern`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_Jk7V1SOKE4Gm`
See :s:`WhereClausePredicate`.

.. _fls_8hcsablipi17:

while let loop
^^^^^^^^^^^^^^


:dp:`fls_ovutw52qtx71`
For :dt:`while let loop`, see :t:`while let loop expression`.

.. _fls_gme4odk59x6d:

while let loop expression
^^^^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## while loop (while_loop)

### Before glossary entry (origin/main)

```rst
.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^

:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.
```

### After glossary entry (generated)

```rst
.. _fls_sglvAOKGWieq:

while loop
^^^^^^^^^^

:dp:`fls_zuxptU8XV6eg`
 For :t:`while loop <while_loop>`, see :t:`while loop expression <while_loop_expression>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_g35gn7n88acp`
A :dt:`while let loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
:t:`value` that can be matched against its :t:`pattern`.


:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## while loop expression (while_loop_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.

:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_Kv1RKEtcnFZE:

while loop expression
^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_oWCZG2cmIxNr`
 A :t:`while loop expression <while_loop_expression>` is a :t:`loop expression <loop_expression>` that continues to evaluate its :t:`loop body <loop_body>` as long as its :t:`iteration expression <iteration_expression>` holds true.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^

```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_q3jcb4nodqba`
See :s:`WhileLetLoopExpression`.

.. _fls_od59yim9kasi:

while loop
^^^^^^^^^^


:dp:`fls_ug9cxoml9ged`
For :dt:`while loop`, see :t:`while loop expression`.

.. _fls_1qxi3h3qmgso:

while loop expression
^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^

```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.

## whitespace string (whitespace_string)

### Before glossary entry (origin/main)

```rst
.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^

:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.
```

### After glossary entry (generated)

```rst
.. _fls_I284OkPCF4w1:

whitespace string
^^^^^^^^^^^^^^^^^

:dp:`fls_Om2ImXvFMVnY`
 A :t:`whitespace string <whitespace_string>` is a string that consists of one or more :t:`whitespace characters <whitespace_character>`.
```

### Before chapter excerpt (origin/main)

```rst
glossary.rst
:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### After chapter excerpt (current)

```rst
glossary-definitions.rst
:dp:`fls_fq0zyup4djyh`
A :dt:`while loop expression` is a :t:`loop expression` that continues to
evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
true.


:dp:`fls_7htwpbmyq83u`
See :s:`WhileLoopExpression`.

.. _fls_cxm8nw6qiryr:

whitespace string
^^^^^^^^^^^^^^^^^


:dp:`fls_nljkmadklwdp`
A :dt:`whitespace string` is a string that consists of one or more
:t:`[whitespace character]s`.

.. _fls_a5lrxgucl3be:

zero-sized type
^^^^^^^^^^^^^^^


:dp:`fls_rmd6pearrhr8`
A :dt:`zero-sized type` is a :t:`fixed sized type` with :t:`size` zero.

.. _fls_pix563lfbpm:

zero-variant enum type
^^^^^^^^^^^^^^^^^^^^^^


:dp:`fls_84gqz3vwi5mj`
A :dt:`zero-variant enum type` is an :t:`enum type` without any
:t:`[enum variant]s`.
```

### Role classification

dt: term definitions

### Standalone edits

No stand-alone edits flagged.
