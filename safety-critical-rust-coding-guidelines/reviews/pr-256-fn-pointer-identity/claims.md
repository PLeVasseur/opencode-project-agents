# Claims Map

PR: 256
Guideline IDs: gui_QbvIknd9qNF6
Reviewer: OpenCode
Date: 2026-02-02

## Summary Table
| ID | Status | Type | Location | Source Kind | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:11 | Other | Category choice not justified. |
| C-002 | Verified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:12 | Other | New guidelines must be draft. |
| C-003 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:13 | Other | Release applicability not justified. |
| C-004 | Verified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:14 | FLS | FLS paragraph is in Types and Traits. |
| C-005 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:15 | Other | Decidability choice not justified. |
| C-006 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:16 | Other | Scope choice not justified. |
| C-007 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:17 | Other | Tag choice not justified. |
| C-008 | Unverified | Normative | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:6 | Other | No authoritative source cited. |
| C-009 | Unverified | Normative | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:19 | Other | No authoritative source cited. |
| C-010 | Unverified | Normative | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:40 | Other | Indirect comparison list not sourced. |
| C-011 | Disputed | Normative | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:23 | Reference | ``no_mangle`` does not guarantee single instance. |
| C-012 | Disputed | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:30 | Other | "Instantiated every time referenced" not supported. |
| C-013 | Disputed | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:31 | Reference | ``no_mangle`` single instance claim not supported. |
| C-014 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:35 | FLS | FLS cited but does not state address identity rules. |
| C-015 | Disputed | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:39 | Reference | ``fn`` type is not a zero-sized function item. |
| C-016 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:41 | Other | Multiple code instances claim not sourced. |
| C-017 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:45 | Other | Unreliable operations list not sourced. |
| C-018 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:61 | Other | Optimization claims not fully sourced. |
| C-019 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:102 | Other | Deduplication/UB claim not sourced. |
| C-020 | Verified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:307 | Other | Rust issue 117047 cited. |
| C-021 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:311 | Other | Consequence list not sourced. |
| C-022 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:328 | Other | Noncompliant example claim not sourced. |
| C-023 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:382 | Other | Cross-crate comparison claim not sourced. |
| C-024 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:411 | Other | Compliant enum example claim not sourced. |
| C-025 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:440 | Other | HashMap identity claim not sourced. |
| C-026 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:463 | Other | Stable identity wrapper claim not sourced. |
| C-027 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst:498 | Other | Deduplication example claim not sourced. |

## Legend
- Type: Normative | Rationale | Example-prose | Example-comment | Field-choice
- Source kind: Reference | FLS | UCG | Rustc-dev-guide | Standard (CERT/MISRA/...) | Other
- Status: Verified | Unverified | Disputed

## Claims

### C-001
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 11
- Snippet: ``:category: required``

Claim:
- Text: "The guideline category is required."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Category values are defined; choice not justified.

Status:
- Unverified

### C-002
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 12
- Snippet: ``:status: draft``

Claim:
- Text: "The guideline status is draft."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: New guidelines must be draft.

Status:
- Verified

### C-003
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 13
- Snippet: ``:release: unclear-latest``

Claim:
- Text: "The guideline applies from unclear through latest release."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Release applicability not justified.

Status:
- Unverified

### C-004
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 14
- Snippet: ``:fls: fls_1kg1mknf4yx7``

Claim:
- Text: "This guideline maps to FLS paragraph fls_1kg1mknf4yx7."
- Type: Field-choice

Source:
- Kind: FLS
- Citation: src/spec.lock (types-and-traits.html#fls_1kg1mknf4yx7)
- Notes: Paragraph exists in Types and Traits.

Status:
- Verified

### C-005
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 15
- Snippet: ``:decidability: decidable``

Claim:
- Text: "The guideline is decidable to check automatically."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: No justification provided.

Status:
- Unverified

### C-006
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 16
- Snippet: ``:scope: system``

Claim:
- Text: "The guideline scope is system."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: No justification provided.

Status:
- Unverified

### C-007
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 17
- Snippet: ``:tags: surprising-behavior``

Claim:
- Text: "The guideline tag is surprising-behavior."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Tag choice not justified.

Status:
- Unverified

### C-008
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 6
- Snippet: ``Do not directly or indirectly compare function pointers``

Claim:
- Text: "Function pointers must not be compared directly or indirectly."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-009
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 19
- Snippet: ``Do not *directly* or *indirectly* compare function pointers.``

Claim:
- Text: "Do not directly or indirectly compare function pointers."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-010
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 40
- Snippet: ``The following are all the ways function pointers can be indirectly compared:``

Claim:
- Text: "The listed patterns are all the ways function pointers can be indirectly compared."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: Claim is not supported.

Status:
- Unverified

### C-011
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 23
- Snippet: ````#[no_mangle]`` functions are guaranteed to have a single instance``

Claim:
- Text: "``#[no_mangle]`` functions are guaranteed to have a single instance."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_QbvIknd9qNF6:RUST-REF-NO-MANGLE`
- Notes: Reference does not guarantee single instantiation.

Status:
- Disputed

### C-012
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 30
- Snippet: ``Functions may be instantiated multiple times. They may, for example, be instantiated``

Claim:
- Text: "Functions may be instantiated multiple times, possibly every time referenced."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Disputed

### C-013
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 31
- Snippet: ``Only ``#[no_mangle]`` functions are guaranteed to be instantiated a single time``

Claim:
- Text: "Only ``#[no_mangle]`` functions are guaranteed single instantiation."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_QbvIknd9qNF6:RUST-REF-NO-MANGLE`
- Notes: Reference does not state this guarantee.

Status:
- Disputed

### C-014
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 35
- Snippet: ``Avoid assumptions about low-level metadata (such as symbol addresses) unless``

Claim:
- Text: "Function address identity is not guaranteed by the FLS."
- Type: Rationale

Source:
- Kind: FLS
- Citation: :cite:`gui_QbvIknd9qNF6:FLS`
- Notes: FLS reference does not explicitly state this.

Status:
- Unverified

### C-015
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 39
- Snippet: ``Rust's ``fn`` type is a zero-sized function item promoted to a function pointer``

Claim:
- Text: "The ``fn`` type is a zero-sized function item promoted to a function pointer."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_QbvIknd9qNF6:RUST-REF-FN-PTR`
- Notes: Function items are zero-sized; ``fn`` is the pointer type.

Status:
- Disputed

### C-016
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 41
- Snippet: ``When a function resides in a different crate or codegen-unit partitioning is``

Claim:
- Text: "Compiler may generate multiple code instances or alter addresses across crates/codegen units."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-017
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 45
- Snippet: ``Consequently, the following operations are unreliable for functions which are not``

Claim:
- Text: "Equality, identity keys, and address-based matching are unreliable for non-no_mangle functions."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-018
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 61
- Snippet: ``Compiler optimizations may cause function pointers to lose stable identity``

Claim:
- Text: "Optimizations like inlining or function merging can affect function pointer identity."
- Type: Rationale

Source:
- Kind: Other
- Citation: :cite:`gui_QbvIknd9qNF6:LLVM-LTO`
- Notes: LLVM LTO does not directly state Rust function pointer equality guarantees.

Status:
- Unverified

### C-019
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 102
- Snippet: ``These functions are deduplicated for specific backends and have the same address.``

Claim:
- Text: "The foo/bar functions can be deduplicated and share addresses despite differing UB behavior."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-020
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 307
- Snippet: ``This behavior has resulted in real-world issues, such as the bug reported in``

Claim:
- Text: "Rust issue 117047 reports function pointer comparison failures due to multiple instantiations."
- Type: Rationale

Source:
- Kind: Other
- Citation: :cite:`gui_QbvIknd9qNF6:RUST-ISSUE-117047`
- Notes: Issue provides real-world evidence.

Status:
- Verified

### C-021
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 311
- Snippet: ``Violating this rule may cause:``

Claim:
- Text: "Violating the rule can cause logic failures, security issues, and nondeterminism."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-022
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 328
- Snippet: ``In this noncompliant example, the ``write_first`` and ``write_second`` functions each``

Claim:
- Text: "The example demonstrates unsound behavior when function pointer addresses compare equal."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-023
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 382
- Snippet: ``Due to cross-crate inlining or codegen-unit partitioning, the address of``

Claim:
- Text: "Cross-crate inlining/codegen units can change function pointer addresses."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-024
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 411
- Snippet: ``Replace function pointer comparison with an explicit enumeration type``

Claim:
- Text: "Using an explicit enum identifier is a compliant alternative to function pointer comparisons."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-025
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 440
- Snippet: ``A function pointer used as a key is not guaranteed to have stable identity``

Claim:
- Text: "Function pointers are not guaranteed to have stable identity when used as keys."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-026
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 463
- Snippet: ``This compliant example uses stable identity wrappers as identity keys.``

Claim:
- Text: "Stable, programmer-defined IDs are a compliant alternative."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-027
Location:
- File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
- Line: 498
- Snippet: ``This noncompliant example relies on function pointer identity for deduplication:``

Claim:
- Text: "Deduplicating by function pointer identity is noncompliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified
