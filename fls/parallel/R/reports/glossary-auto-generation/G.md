# Glossary audit G

## Per-letter checklist
- Letter: G
- [x] Reconcile G terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate G terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for G
- [x] Update `migration-checklist.md` for all G terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint G migration`
- [x] Letter complete

## Term checklist
- [x] generic argument (generic_argument)
- [x] generic associated type (generic_associated_type)
- [x] generic conformance (generic_conformance)
- [x] generic enum (generic_enum)
- [x] generic function (generic_function)
- [x] generic implementation (generic_implementation)
- [x] generic parameter (generic_parameter)
- [x] generic parameter scope (generic_parameter_scope)
- [x] generic struct (generic_struct)
- [x] generic substitution (generic_substitution)
- [x] generic trait (generic_trait)
- [x] generic type (generic_type)
- [x] generic type alias (generic_type_alias)
- [x] generic union (generic_union)
- [x] glob import (glob_import)
- [x] global path (global_path)
- [x] global type variable (global_type_variable)
- [x] greater-than expression (greater_than_expression)
- [x] greater-than-or-equals expression (greater_than_or_equals_expression)

## generic argument (generic_argument)

### Before glossary entry (origin/main)

```rst
.. _fls_j1cyhud0h65t:

generic argument
^^^^^^^^^^^^^^^^

:dp:`fls_meimxi20p51a`
A :dt:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.

:dp:`fls_8bvdmdgbu17l`
See :s:`GenericArgumentList`.
```

### After glossary entry (generated)

```rst
.. _fls_uwBV6i2TVS7K:

generic argument
^^^^^^^^^^^^^^^^

:dp:`fls_ZR7SkI4bkCmf`
A :t:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_1xgw1dq60quz`
A :t:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

:dp:`fls_47s8i7pzb9gg`
It is a static error to create a :t:`trivial predicate` that does not hold.

:dp:`fls_3x6qd8vt5uus`
A :t:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.

:dp:`fls_ky39fb2vcom6`
A :s:`BindingArgument` shall follow :s:`[ConstantArgument]s`,
:s:`[LifetimeArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.

:dp:`fls_9n1ejjili06h`
A :s:`LifetimeArgument` shall precede :s:`[BindingArgument]s`,
:s:`[ConstantArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_1xgw1dq60quz`
A :t:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

:dp:`fls_47s8i7pzb9gg`
It is a static error to create a :t:`trivial predicate` that does not hold.

:dp:`fls_3x6qd8vt5uus`
A :dt:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.

:dp:`fls_8j3ARLPm65vI`
A :dt:`generic substitution` is the replacement of a :t:`generic parameter`
with a :t:`generic argument`.

:dp:`fls_ky39fb2vcom6`
A :s:`BindingArgument` shall follow :s:`[ConstantArgument]s`,
:s:`[LifetimeArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic associated type (generic_associated_type)

### Before glossary entry (origin/main)

```rst
.. _fls_nooYIxMnV8Ps:

generic associated type
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_O4wckPZPmree`
A :dt:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_g14815RAlpOc:

generic associated type
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_jW4hglE5v8CQ`
A :t:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/associated-items.rst
:dp:`fls_w8nu8suy7t5`
An :t:`associated type` shall not be used in the :t:`path expression` of a
:t:`struct expression`.

:dp:`fls_wasocqdnuzd1`
An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
:t:`associated trait type`.

:dp:`fls_PeD0DzjK57be`
A :t:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.

:dp:`fls_3foYUch29ZtF`
A :t:`lifetime parameter` of a :t:`generic associated type` requires a
:t:`bound` of the form ``T: 'lifetime``, where ``T`` is a :t:`type parameter`
or :c:`Self` and ``'lifetime`` is the :t:`lifetime parameter`, when

* :dp:`fls_SnQc0zZS57Cz`
  The :t:`generic associated type` is used in an :t:`associated function` of
  the same :t:`trait`, and
```

### After chapter excerpt (current)

```rst
src/associated-items.rst
:dp:`fls_w8nu8suy7t5`
An :t:`associated type` shall not be used in the :t:`path expression` of a
:t:`struct expression`.

:dp:`fls_wasocqdnuzd1`
An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
:t:`associated trait type`.

:dp:`fls_PeD0DzjK57be`
A :dt:`generic associated type` is an :t:`associated type` with
:t:`[generic parameter]s`.

:dp:`fls_3foYUch29ZtF`
A :t:`lifetime parameter` of a :t:`generic associated type` requires a
:t:`bound` of the form ``T: 'lifetime``, where ``T`` is a :t:`type parameter`
or :c:`Self` and ``'lifetime`` is the :t:`lifetime parameter`, when

* :dp:`fls_SnQc0zZS57Cz`
  The :t:`generic associated type` is used in an :t:`associated function` of
  the same :t:`trait`, and
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic conformance (generic_conformance)

### Before glossary entry (origin/main)

```rst
.. _fls_3uFg0NK5fYQ6:

generic conformance
^^^^^^^^^^^^^^^^^^^

:dp:`fls_PfvELNsNySLT`
:dt:`Generic conformance` measures the compatibility between a set of
:t:`[generic parameter]s` and a set of :t:`[generic argument]s`.
```

### After glossary entry (generated)

```rst
.. _fls_DXgj93rs1Vn3:

Generic conformance
^^^^^^^^^^^^^^^^^^^

:dp:`fls_mBW36aqgDdfg`
:t:`Generic conformance` measures the compatibility between a set of
:t:`[generic parameter]s` and a set of :t:`[generic argument]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_l88o2snx9qbt`
The following is a generic function with a binding argument.

:dp:`fls_thpj9io9tyuy`
The following are generic arguments for ``func``.

:dp:`fls_CBWyxBJeYeb2`
:t:`Generic conformance` measures the compatibility between a set of
:t:`[generic parameter]s` and a set of :t:`[generic argument]s`.

:dp:`fls_ltch5eivxgaa`
A :t:`binding argument` is conformant with an :t:`associated type` when the
supplied :t:`type` of the :t:`binding argument` fulfills the required
:t:`[trait bound]s` of the :t:`associated type`.

:dp:`fls_gb3mpt5rxjoa`
A :t:`constant argument` is conformant with a :t:`constant parameter` when
the :t:`[type]s` of the :t:`constant argument` and the :t:`constant parameter`
are :t:`unifiable`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_l88o2snx9qbt`
The following is a generic function with a binding argument.

:dp:`fls_thpj9io9tyuy`
The following are generic arguments for ``func``.

:dp:`fls_CBWyxBJeYeb2`
:dt:`Generic conformance` measures the compatibility between a set of
:t:`[generic parameter]s` and a set of :t:`[generic argument]s`.

:dp:`fls_ltch5eivxgaa`
A :t:`binding argument` is conformant with an :t:`associated type` when the
supplied :t:`type` of the :t:`binding argument` fulfills the required
:t:`[trait bound]s` of the :t:`associated type`.

:dp:`fls_gb3mpt5rxjoa`
A :t:`constant argument` is conformant with a :t:`constant parameter` when
the :t:`[type]s` of the :t:`constant argument` and the :t:`constant parameter`
are :t:`unifiable`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic enum (generic_enum)

### Before glossary entry (origin/main)

```rst
.. _fls_3tj3i83eoi36:

generic enum
^^^^^^^^^^^^

:dp:`fls_pnu8w26uexaq`
A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_gmTwf3F7ddwC:

generic enum
^^^^^^^^^^^^

:dp:`fls_CZR4W5QgnjD4`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_sye3d17l9bf5`
A :t:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
or a :t:`type`, whose :t:`constant`, :t:`lifetime`, or :t:`type` is supplied
statically by a :t:`generic argument`.

:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_sye3d17l9bf5`
A :dt:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
or a :t:`type`, whose :t:`constant`, :t:`lifetime`, or :t:`type` is supplied
statically by a :t:`generic argument`.

:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :dt:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic function (generic_function)

### Before glossary entry (origin/main)

```rst
.. _fls_votx8gvy5utg:

generic function
^^^^^^^^^^^^^^^^

:dp:`fls_rfkbc967d48h`
A :dt:`generic function` is a :t:`function` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_O8khqn9exrqJ:

generic function
^^^^^^^^^^^^^^^^

:dp:`fls_RkvxPLAUQoq4`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :dt:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_0GhOR32Z4j7M`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic implementation (generic_implementation)

### Before glossary entry (origin/main)

```rst
.. _fls_1xjbrp376niw:

generic implementation
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_jic937ujpnar`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_XWVQ5UR3Bqqe:

generic implementation
^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_vZGltxP4zHY4`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_pi6eukz7kc99`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_pi6eukz7kc99`
A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :dt:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_0GhOR32Z4j7M`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.

:dp:`fls_wmcp0n36jlbr`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic parameter (generic_parameter)

### Before glossary entry (origin/main)

```rst
.. _fls_s2syghgn74e2:

generic parameter
^^^^^^^^^^^^^^^^^

:dp:`fls_61e6br8jy1v2`
A :dt:`generic parameter` is a placeholder for a :t:`constant`, a
:t:`lifetime`, or a :t:`type` whose :t:`value` is supplied statically by a
:t:`generic argument`.

:dp:`fls_jvxpoob39632`
See :s:`GenericParameterList`.
```

### After glossary entry (generated)

```rst
.. _fls_esMUsWwWw24o:

generic parameter
^^^^^^^^^^^^^^^^^

:dp:`fls_TdAfW2HIMB3h`
A :t:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
or a :t:`type`, whose :t:`constant`, :t:`lifetime`, or :t:`type` is supplied
statically by a :t:`generic argument`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_sye3d17l9bf5`
A :t:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
or a :t:`type`, whose :t:`constant`, :t:`lifetime`, or :t:`type` is supplied
statically by a :t:`generic argument`.

:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_sye3d17l9bf5`
A :dt:`generic parameter` is a placeholder for a :t:`constant`, a :t:`lifetime`,
or a :t:`type`, whose :t:`constant`, :t:`lifetime`, or :t:`type` is supplied
statically by a :t:`generic argument`.

:dp:`fls_dalqke3rznrb`
All :s:`[LifetimeParameter]s` in a :s:`GenericParameterList` shall precede all
:s:`[ConstantParameter]s` and :s:`[TypeParameter]s`.

:dp:`fls_pi6eukz7kc99`
A :dt:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic parameter scope (generic_parameter_scope)

### Before glossary entry (origin/main)

```rst
.. _fls_CzudKdaYbfBF:

generic parameter scope
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_e2tICijmLkj4`
A :dt:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_UmKMwZZd79UL:

generic parameter scope
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_hjI4qretenqm`
A :t:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_xbnki64un70v`
The :t:`binding` of a :t:`match arm` is :t:`in scope` within its related
:t:`[expression]s` and related :t:`match arm guard`.

:dp:`fls_eBacCVlDaKYK`
A :t:`binding` declared outside of a :t:`const block expression` is not :t:`in
scope` within such a :t:`const block expression`.

:dp:`fls_amoh8r4gghyj`
A :t:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.

:dp:`fls_6o38qhbna46z`
A :t:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.

:dp:`fls_jqevvpndxzdz`
A :t:`generic parameter` of an :t:`enum type` is :t:`in scope` within the
related :t:`[enum variant]s` and :t:`where clause`.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_xbnki64un70v`
The :t:`binding` of a :t:`match arm` is :t:`in scope` within its related
:t:`[expression]s` and related :t:`match arm guard`.

:dp:`fls_eBacCVlDaKYK`
A :t:`binding` declared outside of a :t:`const block expression` is not :t:`in
scope` within such a :t:`const block expression`.

:dp:`fls_amoh8r4gghyj`
A :dt:`generic parameter scope` is a :t:`scope` for :t:`[generic parameter]s`.

:dp:`fls_6o38qhbna46z`
A :t:`generic parameter` is :t:`in scope` of a :s:`GenericParameterList`.

:dp:`fls_jqevvpndxzdz`
A :t:`generic parameter` of an :t:`enum type` is :t:`in scope` within the
related :t:`[enum variant]s` and :t:`where clause`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic struct (generic_struct)

### Before glossary entry (origin/main)

```rst
.. _fls_cgtu4v2vxvh:

generic struct
^^^^^^^^^^^^^^

:dp:`fls_mcb2mlklith8`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_l4M70VESIh4F:

generic struct
^^^^^^^^^^^^^^

:dp:`fls_0ZpXXpNfeUDK`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_ixmgqupxvf73`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :t:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_z311nxou9yi3`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_0GhOR32Z4j7M`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.

:dp:`fls_wmcp0n36jlbr`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :dt:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic substitution (generic_substitution)

### Before glossary entry (origin/main)

```rst
.. _fls_VBEBshUrAOKE:

generic substitution
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_Led1Nxfcd70K`
A :dt:`generic substitution` is the replacement of a :t:`generic parameter`
with a :t:`generic argument`.
```

### After glossary entry (generated)

```rst
.. _fls_49ipA9mqWx3q:

generic substitution
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_9c2Flqt5TnqL`
A :t:`generic substitution` is the replacement of a :t:`generic parameter`
with a :t:`generic argument`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_3x6qd8vt5uus`.
src/generics.rst
:dp:`fls_1xgw1dq60quz`
A :t:`trivial predicate` is a :t:`where clause predicate` that does not use
the :t:`[generic parameter]s` or :t:`[higher-ranked trait bound]s` of the related
:t:`construct`.

:dp:`fls_47s8i7pzb9gg`
It is a static error to create a :t:`trivial predicate` that does not hold.

:dp:`fls_3x6qd8vt5uus`
A :t:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.

:dp:`fls_ky39fb2vcom6`
A :s:`BindingArgument` shall follow :s:`[ConstantArgument]s`,
:s:`[LifetimeArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.

:dp:`fls_9n1ejjili06h`
A :s:`LifetimeArgument` shall precede :s:`[BindingArgument]s`,
:s:`[ConstantArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_47s8i7pzb9gg`
It is a static error to create a :t:`trivial predicate` that does not hold.

:dp:`fls_3x6qd8vt5uus`
A :dt:`generic argument` supplies a static input for an
:t:`associated trait type` or a :t:`generic parameter`.

:dp:`fls_8j3ARLPm65vI`
A :dt:`generic substitution` is the replacement of a :t:`generic parameter`
with a :t:`generic argument`.

:dp:`fls_ky39fb2vcom6`
A :s:`BindingArgument` shall follow :s:`[ConstantArgument]s`,
:s:`[LifetimeArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.

:dp:`fls_9n1ejjili06h`
A :s:`LifetimeArgument` shall precede :s:`[BindingArgument]s`,
:s:`[ConstantArgument]s`, and :s:`[TypeArgument]s` in a
:s:`GenericArgumentList`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## generic trait (generic_trait)

### Before glossary entry (origin/main)

```rst
.. _fls_hppo1v3ia4wu:

generic trait
^^^^^^^^^^^^^

:dp:`fls_h515f11akr91`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_uml6nAJDdkxB:

generic trait
^^^^^^^^^^^^^

:dp:`fls_Pvs8PtQYhJBI`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :t:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :t:`generic union` is a :t:`union` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_0GhOR32Z4j7M`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.

:dp:`fls_wmcp0n36jlbr`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :dt:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :dt:`generic union` is a :t:`union` with :t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic type (generic_type)

### Before glossary entry (origin/main)

```rst
.. _fls_3Ss6jDgtF1of:

generic type
^^^^^^^^^^^^

:dp:`fls_Zn2pIsMZoTry`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.
```

### After glossary entry (generated)

```rst
.. _fls_crw3zVrauFo6:

generic type
^^^^^^^^^^^^

:dp:`fls_Co56UEIIrwgA`
A :t:`generic type` is a :t:`type` with a :t:`generic parameter`.
```

### Before chapter excerpt (origin/main)

```rst
Definition did not exist in origin/main chapters. Context near :dp:`fls_z311nxou9yi3`.
src/generics.rst
:dp:`fls_pi6eukz7kc99`
A :t:`generic enum` is an :t:`enum` with :t:`[generic parameter]s`.

:dp:`fls_ixmgqupxvf73`
A :t:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :t:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_ixmgqupxvf73`
A :dt:`generic function` is a :t:`function` with :t:`[generic parameter]s`.

:dp:`fls_z311nxou9yi3`
A :dt:`generic implementation` is an :t:`implementation` with
:t:`[generic parameter]s`.

:dp:`fls_0GhOR32Z4j7M`
A :dt:`generic type` is a :t:`type` with a :t:`generic parameter`.

:dp:`fls_wmcp0n36jlbr`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Added definition paragraph for standalone glossary use.

## generic type alias (generic_type_alias)

### Before glossary entry (origin/main)

```rst
.. _fls_18ow0q8at1pi:

generic type alias
^^^^^^^^^^^^^^^^^^

:dp:`fls_zgxsqq4vu7e3`
A :dt:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_PU4WFp9TlivE:

generic type alias
^^^^^^^^^^^^^^^^^^

:dp:`fls_X4a4XIcbLaJl`
A :t:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_wmcp0n36jlbr`
A :t:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :t:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :t:`generic union` is a :t:`union` with :t:`[generic parameter]s`.

:dp:`fls_vpcqgec83ybt`
A :t:`constant parameter` is a :t:`generic parameter` for a :t:`constant`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_wmcp0n36jlbr`
A :dt:`generic struct` is a :t:`struct` with :t:`[generic parameter]s`.

:dp:`fls_h42kg56vsefx`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :dt:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :dt:`generic union` is a :t:`union` with :t:`[generic parameter]s`.

:dp:`fls_vpcqgec83ybt`
A :dt:`constant parameter` is a :t:`generic parameter` for a :t:`constant`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## generic union (generic_union)

### Before glossary entry (origin/main)

```rst
.. _fls_xn9mla1vm6iv:

generic union
^^^^^^^^^^^^^

:dp:`fls_93rxr0yjx1e7`
A :dt:`generic union` is a :t:`union` with :t:`[generic parameter]s`.
```

### After glossary entry (generated)

```rst
.. _fls_rt3aHTa4SCKQ:

generic union
^^^^^^^^^^^^^

:dp:`fls_shHyRIbqNOu5`
A :t:`generic union` is a :t:`union` with :t:`[generic parameter]s`.
```

### Before chapter excerpt (origin/main)

```rst
src/generics.rst
:dp:`fls_h42kg56vsefx`
A :t:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :t:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :t:`generic union` is a :t:`union` with :t:`[generic parameter]s`.

:dp:`fls_vpcqgec83ybt`
A :t:`constant parameter` is a :t:`generic parameter` for a :t:`constant`.

:dp:`fls_3SjMBlc0b7qo`
A :t:`constant parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`constant parameter`.
```

### After chapter excerpt (current)

```rst
src/generics.rst
:dp:`fls_h42kg56vsefx`
A :dt:`generic trait` is a :t:`trait` with :t:`[generic parameter]s`.

:dp:`fls_372h3oevejih`
A :dt:`generic type alias` is a :t:`type alias` with :t:`[generic parameter]s`.

:dp:`fls_u8mqct93yimd`
A :dt:`generic union` is a :t:`union` with :t:`[generic parameter]s`.

:dp:`fls_vpcqgec83ybt`
A :dt:`constant parameter` is a :t:`generic parameter` for a :t:`constant`.

:dp:`fls_3SjMBlc0b7qo`
A :dt:`constant parameter initializer` is a :t:`construct` that provides the
default :t:`value` of its related :t:`constant parameter`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## glob import (glob_import)

### Before glossary entry (origin/main)

```rst
.. _fls_euukteybsbi:

glob import
^^^^^^^^^^^

:dp:`fls_90qsib7g8e9j`
A :dt:`glob import` is a :t:`use import` that brings all :t:`[name]s` with
:t:`public visibility` prefixed by its :t:`path` prefix into :t:`scope`.

:dp:`fls_n4plc55cij0j`
See :s:`GlobImport`.
```

### After glossary entry (generated)

```rst
.. _fls_LaaA2WaEF9Gn:

glob import
^^^^^^^^^^^

:dp:`fls_l9Dpzf97t4SU`
A :t:`glob import` is a :t:`use import` that brings all :t:`entities <entity>`
exported by the :t:`module` or :t:`enum` its :t:`import path prefix` resolves to
into :t:`scope`.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
#. :dp:`fls_gAWsqibl4GLq`
   Then if the current :t:`use import` is the child of a :t:`nesting import`,
   prepend the :t:`nesting import`'s :t:`simple path prefix` to the
   :t:`import path prefix`. Repeat this step with the :t:`nesting import` as
   the current :t:`use import`.

:dp:`fls_2bkcn83smy2y`
A :t:`simple import` is a :t:`use import` that brings all :t:`entities <entity>`
it refers to into scope, optionally with a different
:t:`name` than they are declared with by using a :t:`renaming`.

:dp:`fls_v3a6y2ze44v2`
A :t:`glob import` is a :t:`use import` that brings all :t:`entities <entity>`
exported by the :t:`module` or :t:`enum` its :t:`import path prefix` resolves to
into :t:`scope`.

:dp:`fls_JHU0ersYB6eL`
An :t:`import path prefix` shall resolve to a :t:`module` or :t:`enum`.

:dp:`fls_jlNKxkuhsvX4`
A :t:`glob import` brings :t:`[name]s` into :t:`scope` as follows:
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
#. :dp:`fls_gAWsqibl4GLq`
   Then if the current :t:`use import` is the child of a :t:`nesting import`,
   prepend the :t:`nesting import`'s :t:`simple path prefix` to the
   :t:`import path prefix`. Repeat this step with the :t:`nesting import` as
   the current :t:`use import`.

:dp:`fls_2bkcn83smy2y`
A :t:`simple import` is a :t:`use import` that brings all :t:`entities <entity>`
it refers to into scope, optionally with a different
:t:`name` than they are declared with by using a :t:`renaming`.

:dp:`fls_v3a6y2ze44v2`
A :dt:`glob import` is a :t:`use import` that brings all :t:`entities <entity>`
exported by the :t:`module` or :t:`enum` its :t:`import path prefix` resolves to
into :t:`scope`.

:dp:`fls_JHU0ersYB6eL`
An :t:`import path prefix` shall resolve to a :t:`module` or :t:`enum`.

:dp:`fls_jlNKxkuhsvX4`
A :t:`glob import` brings :t:`[name]s` into :t:`scope` as follows:
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## global path (global_path)

### Before glossary entry (origin/main)

```rst
.. _fls_g6g8c58bilen:

global path
^^^^^^^^^^^

:dp:`fls_msg8jw9momfw`
A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.
```

### After glossary entry (generated)

```rst
.. _fls_OF6HhKA2Yikt:

global path
^^^^^^^^^^^

:dp:`fls_kTH8DGA1Yb0W`
A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.
```

### Before chapter excerpt (origin/main)

```rst
src/entities-and-resolution.rst
:dp:`fls_774uryecc2sx`
A :t:`path` that starts with a :t:`path segment` that is expressed as
:t:`keyword` ``$crate`` shall appear only within a :t:`macro transcriber`.

:dp:`fls_7k88ypcgaoff`
If a :t:`path segment` is expressed as :t:`keyword` ``super``, then the
:t:`path segment` shall either be the first :t:`path segment` of a :t:`path`,
or the previous :t:`path segment` of the :t:`path` shall also be expressed as
:t:`keyword` ``super``.

:dp:`fls_7kb6ltajgiou`
A :t:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.

:dp:`fls_n77icl6idazp`
A :t:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s` as defined in the syntax rules
above.

:dp:`fls_YnUsdSM4x9eq`
A :dt:`path prefix` is a :t:`path` with its last :t:`path segment` and
:t:`namespace qualifier` ``::`` stripped.
```

### After chapter excerpt (current)

```rst
src/entities-and-resolution.rst
:dp:`fls_774uryecc2sx`
A :t:`path` that starts with a :t:`path segment` that is expressed as
:t:`keyword` ``$crate`` shall appear only within a :t:`macro transcriber`.

:dp:`fls_7k88ypcgaoff`
If a :t:`path segment` is expressed as :t:`keyword` ``super``, then the
:t:`path segment` shall either be the first :t:`path segment` of a :t:`path`,
or the previous :t:`path segment` of the :t:`path` shall also be expressed as
:t:`keyword` ``super``.

:dp:`fls_7kb6ltajgiou`
A :dt:`global path` is a :t:`path` that starts with :t:`namespace qualifier`
``::``.

:dp:`fls_n77icl6idazp`
A :t:`simple path` is a :t:`path` whose :t:`[path segment]s` consist of either
:t:`[identifier]s` or certain :t:`[keyword]s` as defined in the syntax rules
above.

:dp:`fls_YnUsdSM4x9eq`
A :dt:`path prefix` is a :t:`path` with its last :t:`path segment` and
:t:`namespace qualifier` ``::`` stripped.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## global type variable (global_type_variable)

### Before glossary entry (origin/main)

```rst
.. _fls_hy1clqvaewnp:

global type variable
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_pvt4nayq006s`
A :dt:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.
```

### After glossary entry (generated)

```rst
.. _fls_u2jM5vHu4txL:

global type variable
^^^^^^^^^^^^^^^^^^^^

:dp:`fls_70hDvosf3sWK`
A :t:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.
```

### Before chapter excerpt (origin/main)

```rst
src/types-and-traits.rst
* :dp:`fls_veG2D64fIXvo`
  The :t:`expected type` of a :t:`size operand` of an :t:`array expression` or
  an :t:`array type` is :c:`usize`.

:dp:`fls_uvvn4usfsbhr`
A :t:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

:dp:`fls_gDalJm1XS0mi`
A :t:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.

:dp:`fls_7ov36fpd9mwe`
An :t:`integer type variable` is a :t:`type variable` that can refer only to
:t:`[integer type]s`.

:dp:`fls_3hv3wxkhjjp1`
A :t:`floating-point type variable` is a :t:`type variable` that can refer only
to :t:`[floating-point type]s`.
```

### After chapter excerpt (current)

```rst
src/types-and-traits.rst
* :dp:`fls_veG2D64fIXvo`
  The :t:`expected type` of a :t:`size operand` of an :t:`array expression` or
  an :t:`array type` is :c:`usize`.

:dp:`fls_uvvn4usfsbhr`
A :t:`type variable` is a placeholder used during :t:`type inference` to stand
in for an undetermined :t:`type` of an :t:`expression` or a :t:`pattern`.

:dp:`fls_gDalJm1XS0mi`
A :dt:`global type variable` is a :t:`type variable` that can refer to any
:t:`type`.

:dp:`fls_7ov36fpd9mwe`
An :t:`integer type variable` is a :t:`type variable` that can refer only to
:t:`[integer type]s`.

:dp:`fls_3hv3wxkhjjp1`
A :dt:`floating-point type variable` is a :t:`type variable` that can refer only
to :t:`[floating-point type]s`.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## greater-than expression (greater_than_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_g4n20dy3utzy:

greater-than expression
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_j7x5qii6rhwj`
A :dt:`greater-than expression` is a :t:`comparison expression` that tests for
a greater-than relationship.

:dp:`fls_yni50ba3ufvs`
See :s:`GreaterThanExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_yv3zdxiOMII5:

greater-than expression
^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_uydEPBHolg8p`
A :t:`greater-than expression` is a :t:`comparison expression` that tests for a
greater-than relationship.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_8echqk9po1cf`
The :t:`type` of the :t:`left operand` of an :t:`equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_d62qfloqk2ub`
The :t:`value` of an :t:`equals expression` is the result of
``core::cmp::PartialEq::eq(&left_operand, &right_operand)``.

:dp:`fls_wapl0ir7uvbp`
A :t:`greater-than expression` is a :t:`comparison expression` that tests for a
greater-than relationship.

:dp:`fls_x2s6ydvj5zyd`
The :t:`type` of the :t:`left operand` of a :t:`greater-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pso38dowbk91`
The :t:`value` of a :t:`greater-than expression` is the result of
``core::cmp::PartialOrd::gt(&left_operand, &right_operand)``.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_8echqk9po1cf`
The :t:`type` of the :t:`left operand` of an :t:`equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_d62qfloqk2ub`
The :t:`value` of an :t:`equals expression` is the result of
``core::cmp::PartialEq::eq(&left_operand, &right_operand)``.

:dp:`fls_wapl0ir7uvbp`
A :dt:`greater-than expression` is a :t:`comparison expression` that tests for a
greater-than relationship.

:dp:`fls_x2s6ydvj5zyd`
The :t:`type` of the :t:`left operand` of a :t:`greater-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pso38dowbk91`
The :t:`value` of a :t:`greater-than expression` is the result of
``core::cmp::PartialOrd::gt(&left_operand, &right_operand)``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.

## greater-than-or-equals expression (greater_than_or_equals_expression)

### Before glossary entry (origin/main)

```rst
.. _fls_mxz589rq4hiy:

greater-than-or-equals expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wvspqc2otn6v`
A :dt:`greater-than-or-equals expression` is a :t:`comparison expression` that
tests for a greater-than-or-equals relationship.

:dp:`fls_9azbvj9xux6y`
See :s:`GreaterThanOrEqualsExpression`.
```

### After glossary entry (generated)

```rst
.. _fls_6mTalGRiqIOC:

greater-than-or-equals expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:dp:`fls_wvuZjHKG3hcf`
A :t:`greater-than-or-equals expression` is a :t:`comparison expression` that
tests for a greater-than-or-equals relationship.
```

### Before chapter excerpt (origin/main)

```rst
src/expressions.rst
:dp:`fls_x2s6ydvj5zyd`
The :t:`type` of the :t:`left operand` of a :t:`greater-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pso38dowbk91`
The :t:`value` of a :t:`greater-than expression` is the result of
``core::cmp::PartialOrd::gt(&left_operand, &right_operand)``.

:dp:`fls_7n5gol6a8lod`
A :t:`greater-than-or-equals expression` is a :t:`comparison expression` that
tests for a greater-than-or-equals relationship.

:dp:`fls_hholzcbp5u3n`
The :t:`type` of the :t:`left operand` of a
:t:`greater-than-or-equals expression` shall implement the
:std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_wytygse41vzm`
The :t:`value` of a :t:`greater-than-or-equals expression` is the result of
``core::cmp::PartialOrd::ge(&left_operand, &right_operand)``.
```

### After chapter excerpt (current)

```rst
src/expressions.rst
:dp:`fls_x2s6ydvj5zyd`
The :t:`type` of the :t:`left operand` of a :t:`greater-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pso38dowbk91`
The :t:`value` of a :t:`greater-than expression` is the result of
``core::cmp::PartialOrd::gt(&left_operand, &right_operand)``.

:dp:`fls_7n5gol6a8lod`
A :dt:`greater-than-or-equals expression` is a :t:`comparison expression` that
tests for a greater-than-or-equals relationship.

:dp:`fls_hholzcbp5u3n`
The :t:`type` of the :t:`left operand` of a
:t:`greater-than-or-equals expression` shall implement the
:std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_wytygse41vzm`
The :t:`value` of a :t:`greater-than-or-equals expression` is the result of
``core::cmp::PartialOrd::ge(&left_operand, &right_operand)``.
```

### Role classification

dt: term definition role

### Standalone edits

Upgraded definition role to :dt:; no text changes noted.
