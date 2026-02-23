# Glossary Missing 7 Resolution Plan

## Purpose

- [ ] Resolve the final 7 missing entries from the legacy glossary to reach full coverage.

## Context

- [ ] Coverage report lists 7 missing entries.
- [ ] Missing entries: `assignment`, `atomic`, `c_signed_int_type`, `evaluated`, `executed`, `range_full_expression`, `representation`.
- [ ] Legacy glossary defines 5 as redirects and 2 as standalone definitions.

## Analysis Summary

- [ ] Redirect-only terms: `assignment`, `atomic`, `evaluated`, `executed`, `representation`.
- [ ] Standalone terms: `c_signed_int_type`, `range_full_expression`.
- [ ] Existing canonical targets:
  - [ ] `assignment expression` covers `assignment`.
  - [ ] `atomic type` covers `atomic`.
  - [ ] `Evaluation` covers `evaluated`.
  - [ ] `type representation` covers `representation`.
  - [ ] `execution` target for `executed` is undecided.

## Tasks

### 1) Redirect-only terms

- [ ] Add alias glossary entries (redirect-style) so these terms appear in the generated glossary.
- [ ] `assignment`: add a `:dt:` entry that points to `:t:`assignment expression`` in `src/expressions.rst` near the canonical definition.
- [ ] `atomic`: add a `:dt:` entry that points to `:t:`atomic type`` in `src/types-and-traits.rst` near the canonical definition.
- [ ] `evaluated`: add a `:dt:` entry that points to `:t:`evaluation`` near the canonical `Evaluation` definition.
- [ ] `executed`: add a `:dt:` entry that points to `:t:`execution`` near the canonical definition.
- [ ] `representation`: add a `:dt:` entry that points to `:t:`type representation`` near the canonical definition.

### 2) Add standalone definitions

- [ ] Add `C signed int type` definition to `src/types-and-traits.rst` (Enum Type Representation, immediately after its first use).
- [ ] Add `full range expression` definition to `src/expressions.rst` (Range Expressions section; ensure term id maps to `range_full_expression`).

### 3) Update reports

- [ ] Regenerate `glossary-coverage-compare.md` and verify 0 missing entries.
- [ ] Update `migration-checklist.md` to check the 7 terms.
- [ ] Update any per-letter audit files if required by policy.

### 4) Validation

- [ ] Run `./make.py --check-generated-glossary`.
- [ ] Confirm `git status -sb` reflects only expected changes.

## Placement Details

- [ ] `assignment`: `src/expressions.rst`, Assignment Expressions section near the canonical `assignment expression` definition.
- [ ] `atomic`: `src/types-and-traits.rst`, Type Representation or Atomic Types section near the canonical `atomic type` definition.
- [ ] `evaluated`: place near the canonical `Evaluation` definition (likely `src/expressions.rst`).
- [ ] `executed`: place near the canonical `Execution` definition (likely `src/statements.rst` or the chapter that defines statement execution).
- [ ] `representation`: `src/types-and-traits.rst`, Type Representation section near the canonical `type representation` definition.
- [ ] `c_signed_int_type`: `src/types-and-traits.rst`, Enum Type Representation section, immediately after the sentence that mentions `c signed int type`.
- [ ] `range_full_expression`: `src/expressions.rst`, Range Expressions section near the existing full range definition; update to include the proper term id.

## Open Decision

- [ ] Whether a canonical `execution` definition already exists; if not, add it before adding the `executed` alias entry.
