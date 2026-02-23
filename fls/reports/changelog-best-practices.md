# FLS Changelog Best Practices

## Goal
Keep `src/changelog.rst` an auditable mapping between Rust release language items and FLS spec changes.

## When to update the changelog
- Add a new release section whenever the FLS version advances (see `version.rst`), even if the release has no language changes.
- For every language item in the Rust release notes, add a bullet in the corresponding release section.
  - If the item affects FLS content, record the spec changes (new or changed or removed paragraphs, syntax, sections, glossary entries).
  - If it does not affect FLS, still record it with a concise "No change: reason" line.
- Update the changelog in the same commit as the spec change when possible; otherwise create a focused follow-up commit that explicitly fixes or extends the entry.
- Update the changelog when correcting prior entries (typos, missing IDs, wrong classification) so audit history shows the correction.
- Do not add entries for purely editorial refactors or non-language work unless they correct a release mapping or clarify a language change.

## What counts as an FLS-impacting change
- Added or removed paragraph IDs (referenced as `:p:` in the changelog).
- Paragraph text changed under an existing ID.
- New or changed syntax items (`:s:`), syntax directives, or grammar categories.
- New sections (anchors referenced as `:ref:`) or glossary additions or changes (`:t:`).
- Structural clarifications that change normative meaning (not just wording).

## Recording conventions (quick reminders)
- Keep release sections ordered newest-first and titled "Language changes in Rust X.Y.Z".
- Each bullet includes a link to the upstream Rust PR or release note item.
- Use nested bullets for "New/Changed/Removed paragraph(s)" and similar detail blocks, matching current style in `src/changelog.rst`.

## Examples: changed paragraph text recorded in the changelog

### :p:`fls_3qj3jvmtxvx6` — safe `#[target_feature]` calls (Rust 1.86.0, rust-lang/rust#134090)
Location: `src/attributes.rst`

Before:
```rst
:dp:`fls_3qj3jvmtxvx6`
:t:`Attribute` :c:`target_feature` shall apply to :t:`[unsafe function]s`.
```

After:
```rst
:dp:`fls_3qj3jvmtxvx6`
Safe :t:`[function]s` that are annotated with :c:`[target_feature]s`
can only be called without an :t:`unsafe block` by a caller that is within a function
that enables all the :c:`[target_feature]s` that the callee enables.
```

Essence: expands from a simple restriction (only unsafe functions) to a precise rule
for safe functions, changing the allowed surface and the call-site requirements.

### :p:`fls_SYnFJBhi0IWj` — trait object upcasting rule (Rust 1.84.0, rust-lang/rust#131857)
Location: `src/types-and-traits.rst`

Before:
```rst
:dp:`fls_SYnFJBhi0IWj`
The source :t:`type` is a :t:`trait object type` and the target :t:`type` is a
:t:`trait object type` with the same :t:`[trait bound]s` and additional
:t:`[auto trait]s`.
```

After:
```rst
:dp:`fls_SYnFJBhi0IWj`
The source :t:`type` is a :t:`trait object type` and the target :t:`type` is a :t:`trait object type` with the same or no :t:`[principal trait bound]`, and the target :t:`type` has the same or less non-:t:`principal trait` :t:`[trait bound]s`.
```

Essence: refines the coercion rule from "same bounds + more auto traits" to
explicit principal and non-principal bound constraints, altering which upcasts
are valid.

### :p:`fls_8i4jzksxlrw0` — raw pointer deref exception (Rust 1.84.0, rust-lang/rust#129248)
Location: `src/expressions.rst`

Before:
```rst
:dp:`fls_8i4jzksxlrw0`
Dereferencing a :t:`raw pointer` shall require :t:`unsafe context`.
```

After:
```rst
:dp:`fls_8i4jzksxlrw0`
Dereferencing a :t:`raw pointer` shall require :t:`unsafe context` unless the :t:`dereference expression` is the :t:`operand` of a :t:`raw borrow expression`.
```

Essence: adds a safety exception, so the same operation is now conditionally safe,
which changes the required context for dereferencing.

### :p:`fls_imr2jx6cbuzq` — inferred array size constants (Rust 1.89.0, rust-lang/rust#141610)
Location: `src/types-and-traits.rst`

Before:
```rst
:dp:`fls_imr2jx6cbuzq`
The :t:`size operand` shall be a :t:`constant expression`.
```

After:
```rst
:dp:`fls_imr2jx6cbuzq`
The :t:`size operand` shall be a :t:`constant expression` or an :t:`inferred constant`.
```

Essence: broadens the admissible forms of array sizes to include inferred consts,
which is a semantic expansion of what the language accepts.

### :p:`fls_hbn1l42xmr3h` — variadic ABI allowance expansion (Rust 1.91.0, rust-lang/rust#144066)
Location: `src/types-and-traits.rst`

Before:
```rst
:dp:`fls_hbn1l42xmr3h`
A :t:`variadic part` shall be specified only when the :t:`ABI` of the
:t:`function pointer type` is either ``extern "C"`` or ``extern "cdecl"``.
```

After:
```rst
:dp:`fls_hbn1l42xmr3h`
A :t:`variadic part` shall be specified only when the :t:`ABI` of the
:t:`function pointer type` is one of the following:

* :dp:`fls_OR85NVifPwjr`
  ``extern "C"``
* :dp:`fls_4s2IdfYDzPrX`
  ``extern "C-unwind"``
* :dp:`fls_ZJJppPfiJRou`
  ``extern "aapcs"``
* :dp:`fls_jOyZh9ujWWHQ`
  ``extern "aapcs-unwind"``
* :dp:`fls_Xdr0bFwxhWiB`
  ``extern "cdecl"``
* :dp:`fls_DpTFEHZAABdD`
  ``extern "cdecl-unwind"``
* :dp:`fls_eHPWHrvs7ETl`
  ``extern "sysv64"``
* :dp:`fls_mjCrvmikm58M`
  ``extern "sysv64-unwind"``
* :dp:`fls_4EUb9zFatZ97`
  ``extern "win64"``
* :dp:`fls_4B4B5FIqAes9`
  ``extern "win64-unwind"``
* :dp:`fls_b7FTlWfnX2OI`
  ``extern "efiapi"``
```

Essence: replaces a two-ABI restriction with an explicit whitelist of supported
variadic ABIs, materially changing what is accepted and requiring a changelog note.

## Examples: paragraph text changes without changelog entries

### :p:`fls_IKSPR7ZQMErU` — remove duplicated word (commit 38f4ce0)
Location: `src/associated-items.rst`

Before:
```rst
:dp:`fls_IKSPR7ZQMErU`
:std:`core::pin::Pin<T> <core::pin::Pin>` where ``T`` is one of the the :t:`[type]s` listed in this
enumeration.
```

After:
```rst
:dp:`fls_IKSPR7ZQMErU`
:std:`core::pin::Pin<T> <core::pin::Pin>` where ``T`` is one of the :t:`[type]s` listed in this
enumeration.
```

Essence: removes a duplicated word; pure editorial cleanup with no semantic or
release‑mapped impact.

### :p:`fls_icdzs1mjh0n4` — normative wording tightened (commit 686f9d0)
Location: `src/functions.rst`

Before:
```rst
:dp:`fls_icdzs1mjh0n4`
A :t:`variadic function` can only be used with one of the following :t:`[ABI]s`:
```

After:
```rst
:dp:`fls_icdzs1mjh0n4`
A :t:`variadic function` shall specify one of the following :t:`[ABI]s`:
```

Essence: shifts to explicit requirement language without changing the allowed
set; treated as wording precision, not a new release-mapped rule.

### :p:`fls_VhzGfnWg7YrG` — missing case added to list (commit cd68c9e)
Location: `src/values.rst`

Before:
```rst
:dp:`fls_VhzGfnWg7YrG`
The :t:`mutable reference` is contained within a :t:`mutable static`, or
```

After:
```rst
:dp:`fls_VhzGfnWg7YrG`
The :t:`mutable reference` is contained within a :t:`mutable static`
or a :t:`static` whose type is subject to :t:`interior mutability`, or
```

Essence: completeness fix in an existing rule list; fills an omission but doesn’t
track a specific Rust release note item.

### :p:`fls_zyuxqty09SDO` — stronger phrasing in constant context rule (commit 08395fc)
Location: `src/expressions.rst`

Before:
```rst
:dp:`fls_zyuxqty09SDO`
All forms of :t:`[borrow]s` except those of expressions that would be subject to
```

After:
```rst
:dp:`fls_zyuxqty09SDO`
All forms of :t:`[borrow]s` except those of expressions that are subject to
```

Essence: wording tightened while preserving meaning; an editorial refinement,
so no changelog entry.

### :p:`fls_8m7pc3riokst` — remove unused term (commit 7f4881c)
Location: `src/ffi.rst`

Before:
```rst
:dp:`fls_8m7pc3riokst`
``extern "system"`` - The operating system-dependent :t:`ABI`, referred to as
:dt:`external system ABI`.
```

After:
```rst
:dp:`fls_8m7pc3riokst`
``extern "system"`` - The operating system-dependent :t:`ABI`.
```

Essence: removes a locally unused term without changing the ABI definition;
considered editorial cleanup rather than a release-triggered change.
