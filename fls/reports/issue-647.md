# Issue 647 report: asm_cfg

## Impact assessment
- Stabilizes `asm_cfg`, allowing `#[cfg]` and `#[cfg_attr]` on inline assembly templates and operands.
- Requires FLS updates in inline-assembly grammar and legality rules.

## Spec changes
- Files updated: `src/inline-assembly.rst`, `src/changelog.rst`.
- Syntax changes:
  - Changed: :s:`AssemblyCodeBlock`, :s:`AsmArguments`, :s:`GlobalAsmArguments`.
- New: :s:`AssemblyTemplate`, :s:`AssemblyAttributeRegisterArgument`, :s:`AssemblyAttributeAbiClobber`, :s:`AssemblyAttributeAssemblyOption`.
- New paragraphs: :p:`fls_m0SBtonaNppV`, :p:`fls_nLBhw2w6uznH`, :p:`fls_xzDPz2zfRfoI`, :p:`fls_cTEiqjf6haEg`.

## Rationale
- Matches rust-lang/reference#2063 and rust-lang/rust#147736 by documenting attribute placement on inline assembly arguments and the template-first constraint.

## Reference alignment
- Reference PR: https://github.com/rust-lang/reference/pull/2063
- Reference sections: https://doc.rust-lang.org/reference/inline-assembly.html#syntax, https://doc.rust-lang.org/reference/inline-assembly.html#attributes
- Grammar alignment:
  - Reference adds `AsmAttrFormatString` and `AsmAttrOperand` to accept outer attributes on templates/operands.
  - FLS mirrors this by introducing `AssemblyTemplate` and `AssemblyAttribute*` wrappers, splitting operands into `RegisterArgument`, `AbiClobber`, and `AssemblyOption`.
- Legality rules alignment:
  - Only `cfg`/`cfg_attr` accepted and template-first requirement match the Reference Attributes section.
  - FLS states cfg-false arguments are not part of the macro invocation, consistent with conditional compilation semantics in `src/program-structure-and-compilation.rst:233`.
- Reference note about rustc’s attribute handling is not included because it is implementation detail without semantic effect.

## Grammar and rubric notes
- `reports/issue-647/asm_cfg_positive.rs:23` contains the grammar derivation and rubric verification with line-numbered evidence.
- `reports/issue-647/global_asm_cfg_positive.rs:15` contains the grammar derivation and rubric verification with line-numbered evidence.
- `reports/issue-647/asm_cfg_negative.rs:15` contains the grammar derivation and rubric verification with line-numbered evidence.

## Validation
- Build: `./make.py` (success; clean rebuild with `./make.py -c`; re-run after moving attribute rules under macros, removing linewraps, and renaming grammar categories).
- Grammar-driven compilation (rustc 1.93.0 via rustup; re-run after glossary-term update, section move, linewrap cleanup, and grammar rename):
  - Command template: `rustc +1.93.0 --edition 2021 --crate-type=lib --out-dir reports/issue-647 <file>`.
  - `reports/issue-647/asm_cfg_positive.rs`: success.
  - `reports/issue-647/global_asm_cfg_positive.rs`: success.
  - `reports/issue-647/asm_cfg_negative.rs`: expected failure (`expected expression, found keyword 'in'` at line 7).

## Artifacts
- `reports/issue-647/asm_cfg_positive.rs`
- `reports/issue-647/global_asm_cfg_positive.rs`
- `reports/issue-647/asm_cfg_negative.rs`
