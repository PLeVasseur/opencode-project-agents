# Issue 646 report

## Issue
- Title: [Change]: [1.93] Stabilize declaration of C-style variadic functions for the system ABI
- Link: https://github.com/rust-lang/fls/issues/646
- Rust PR: https://github.com/rust-lang/rust/pull/145954
- Reference PR: https://github.com/rust-lang/reference/pull/2069

## Impact assessment
- Added a glossary definition for :t:`calling convention` and referenced it from the ABI section to match the Reference’s ABI intro for the 2021 edition.
- Clarified ``extern "system"`` equivalence on Windows x86_32 with a numbered algorithm, including the variadic exception (``stdcall`` for non-variadic, ``C`` for variadic).
- Added explicit platform availability constraints to the implementation-permissions ABI list (x86_32/x86_64/ARM/UEFI).
- Specified that extern block declarations are introduced into the value namespace.
- Allowed only :s:`ItemSafety` qualifiers on external functions and required them to appear only within unsafe extern blocks.
- Not included: the 2024-edition requirement that extern blocks must be marked ``unsafe`` (out of scope for FLS 2021). Also omitted the Reference’s statement about compiler ABI translation as an implementation detail.

## Spec updates
- Files changed: src/ffi.rst, src/glossary.rst, src/changelog.rst
- Syntax changes: none
- New paragraph IDs: :p:`fls_TmvfmSQP65pA`, :p:`fls_9OFXj6DnKS7W`, :p:`fls_tuP6iLdL6Kx0`, :p:`fls_MpcAsy5zhCeW`, :p:`fls_ZbvI45Ojpte4`, :p:`fls_tZP7xARsjuYv`, :p:`fls_NxhrfQzbxetN`, :p:`fls_yjRmR5F1cL6i`
- Changed paragraph IDs: :p:`fls_dbbfqaqa80r8`, :p:`fls_UippZpUyYpHl`, :p:`fls_36qrs2fxxvi7`, :p:`fls_CIyK8BYzzo26`, :p:`fls_6rtj6rwqxojh`, :p:`fls_d3nmpc5mtg27`, :p:`fls_7t7yxh94wnbl`, :p:`fls_ccFdnlX5HIYk`, :p:`fls_sxj4vy39sj4g`, :p:`fls_tyjs1x4j8ovp`, :p:`fls_xrCRprWS13R1`, :p:`fls_JHlqXjn4Sf07`, :p:`fls_qwchgvvnp0qe`

## Validation
- Snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-646/extern_system_variadic.rs
  - rustc: `rustc +1.93.0 extern_system_variadic.rs`
  - Warnings: dead_code (unused extern fn), improper_ctypes (tuple in extern fn)
- Snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-646/extern_block_qualifiers_positive.rs
  - rustc: `rustc +1.93.0 extern_block_qualifiers_positive.rs`
  - Warnings: dead_code (unused extern fns)
- Snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-646/extern_block_safe_requires_unsafe_negative.rs
  - rustc: `rustc +1.93.0 extern_block_safe_requires_unsafe_negative.rs`
  - Error: safety qualifiers require an unsafe extern block
- Snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-646/extern_block_const_qualifier_negative.rs
  - rustc: `rustc +1.93.0 extern_block_const_qualifier_negative.rs`
  - Error: extern-block functions cannot be `const`
- Snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-646/extern_aapcs_unavailable_negative.rs
  - rustc: `rustc +1.93.0 extern_aapcs_unavailable_negative.rs`
  - Error: E0570 ("aapcs" unsupported ABI for target)
- Note: the Windows x86_32 ``extern "system"`` equivalence (``stdcall`` vs ``C`` for variadics) is target-specific and was not validated on this host.
- Build: `./make.py` (success)

## Reference alignment
- Reference PR: https://github.com/rust-lang/reference/pull/2069
- Reference sections:
  - https://doc.rust-lang.org/reference/items/external-blocks.html#abi
  - https://doc.rust-lang.org/reference/items/external-blocks.html#variadic-functions
  - https://doc.rust-lang.org/reference/items/external-blocks.html#functions
- Alignment: added a numbered ``extern "system"`` ABI mapping rule and calling-convention detail; added platform availability constraints and extern-function qualifier restrictions to match 2021-edition behavior. The 2024 requirement for ``unsafe extern`` blocks is intentionally omitted.
- Note: the Reference ABI list does not include ``vectorcall``; its availability constraint is inferred from the MSVC/clang attribute scope described in FLS.
