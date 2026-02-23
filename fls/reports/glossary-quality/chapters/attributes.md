# Chapter: Attributes (`src/attributes.rst`)

Conventions
- Headings: alphabetical by term
- Coverage: expected 64 / found 64
Rating rubric (0-5): 5=Clear, scoped, standalone definition; no ambiguity; adds discriminators and context. 4=Mostly clear; minor missing detail or slight reliance on other terms but still useful. 3=Adequate but vague; relies on multiple other terms or lacks scope/edge cases. 2=Low signal; largely tautological, circular, or too abstract; hard to apply. 1=Bare alias, link-only "See ...", or fragment; not independently useful. 0=Missing definition or nonsensical/incoherent text.
Issue tags: missing, link-only, alias-only, tautological, circular, truncated, fragment, list-leadin-without-list, missing-scope, missing-discriminator, low-signal, regression-vs-legacy, inconsistent-term, editorial-noise, wrong-domain, missing-see-line, definition-same-role-change-expected
Legacy policy: legacy link-only/alias-only definitions are intentional; if generated expands them, mark as regression-vs-legacy and set `Legacy: better`.
Overrides: if legacy vs generated differs only by :dt: vs :t:, rate 5 and tag definition-same-role-change-expected (override all other criteria). If legacy had a "See ..." line and generated lacks it, rate 3 and tag missing-see-line; include the missing "See ..." line in Notes.

Checklist
- [ ] Read chapter/appendix and generated glossary terms linked to this file.
- [ ] Compare each term to the legacy glossary.
- [ ] Flag missing/red terms or missing definitions.
- [ ] Flag regressions vs legacy definition quality.
- [ ] Ensure `## <term>` headings are alphabetical and match mapping (expected <count> / found <count>).
- [ ] Note definition issues: list lead-ins without lists, truncated/dangling sentences, alias-only definitions, circular term chains, sentence fragments, tautologies, link-only "See ..." definitions, missing scope/discriminators, low-signal definitions, editorial noise/typos/spacing.

Per-term template (copy for each term in this file):
```text
## <term>
Rating: <0-5> (<label>)
Issues: <tags>
Notes: <why helpful/unhelpful>
Legacy: <better/worse + brief reason>
```

## active attribute
## all configuration predicate
## any configuration predicate
## attribute
## attribute content
## automatically_derived
## built-in attribute
## cfg
## cfg_attr
## cold
## collapse_debuginfo
## configuration predicate
## crate_name
## crate_type
## derive
## doc
## export_name
## exported function
## exported static
## false
## global_allocator
## ignore
## inert attribute
## inline
## inlined
## inlining
## inner attribute
## link
## link_name
## link_ordinal
## link_section
## macro_export
## macro_use
## module path
## naked
## no_builtins
## no_implicit_prelude
## no_link
## no_main
## no_mangle
## no_std
## non-exhaustive type
## non-exhaustive variant
## non_exhaustive
## not configuration predicate
## outer attribute
## panic_handler
## path attribute
## proc_macro
## proc_macro_attribute
## proc_macro_derive
## recursion_limit
## repr
## representation modifier
## should_panic
## target_feature
## test
## testing function
## track_caller
## true
## type_length_limit
## unsafe
## used
## windows_subsystem
