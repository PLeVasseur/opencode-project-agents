# Claims Map

PR: 358
Guideline IDs: gui_ZDLZzjeOwLSU
Reviewer: OpenCode
Date: 2026-02-02

## Summary Table
| ID | Status | Type | Location | Source Kind | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Unverified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:11 | Other | Category choice not justified. |
| C-002 | Verified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:12 | Other | New guidelines must be draft. |
| C-003 | Unverified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:13 | Other | Release applicability not justified. |
| C-004 | Disputed | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:14 | FLS | FLS paragraph is in Unsafety; chapter mismatch. |
| C-005 | Unverified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:15 | Other | Decidability choice not justified. |
| C-006 | Unverified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:16 | Other | Scope choice not justified. |
| C-007 | Unverified | Field-choice | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:17 | Other | Tag choices not justified. |
| C-008 | Unverified | Normative | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:19 | Reference | Broad claim not directly supported by reference. |
| C-009 | Verified | Normative | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:24 | Reference | ``unsafe extern`` required. |
| C-010 | Verified | Normative | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:25 | Reference | Unsafe attributes require ``unsafe(..)`` wrapper. |
| C-011 | Verified | Normative | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:26 | Reference | Unsafe attributes require ``unsafe(..)`` wrapper. |
| C-012 | Verified | Normative | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:27 | Reference | Unsafe attributes require ``unsafe(..)`` wrapper. |
| C-013 | Verified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:31 | Reference | 2024 Edition requires ``unsafe`` for extern blocks/unsafe attributes. |
| C-014 | Unverified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:42 | Other | Auditability claim not sourced. |
| C-015 | Unverified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:44 | Standard | ISO/DO-178C traceability claim not verified. |
| C-016 | Unverified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:47 | Standard | Coverage claim not verified. |
| C-017 | Unverified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:52 | Other | Responsibility signal claim not sourced. |
| C-018 | Unverified | Rationale | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:59 | Other | Tooling claim references uncited tools. |
| C-019 | Disputed | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:76 | Reference | UB claim for symbol conflicts not supported. |
| C-020 | Verified | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:100 | Reference | Rust 2024 requires unsafe wrapper for unsafe attributes. |
| C-021 | Disputed | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:124 | Reference | UB claim even if unused is overstated. |
| C-022 | Verified | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:147 | Reference | Rust 2024 requires unsafe extern blocks. |
| C-023 | Disputed | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:180 | Reference | UB claim for unsafe attributes not stated by reference. |
| C-024 | Verified | Example-prose | src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst:215 | Reference | Unsafe attributes must use ``unsafe(..)`` wrapper. |

## Legend
- Type: Normative | Rationale | Example-prose | Example-comment | Field-choice
- Source kind: Reference | FLS | UCG | Rustc-dev-guide | Standard (CERT/MISRA/...) | Other
- Status: Verified | Unverified | Disputed

## Claims

### C-001
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
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
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
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
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 13
- Snippet: ``:release: 1.85-latest``

Claim:
- Text: "The guideline applies starting in Rust 1.85 through latest."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Release applicability not justified.

Status:
- Unverified

### C-004
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 14
- Snippet: ``:fls: fls_8kqo952gjhaf``

Claim:
- Text: "This guideline maps to FLS paragraph fls_8kqo952gjhaf."
- Type: Field-choice

Source:
- Kind: FLS
- Citation: src/spec.lock (unsafety.html#fls_8kqo952gjhaf)
- Notes: Paragraph is in Unsafety chapter; chapter mismatch.

Status:
- Disputed

### C-005
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
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
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 16
- Snippet: ``:scope: crate``

Claim:
- Text: "The guideline scope is crate."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: No justification provided.

Status:
- Unverified

### C-007
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 17
- Snippet: ``:tags: readability, reduce-human-error``

Claim:
- Text: "The guideline tags are readability and reduce-human-error."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Tag choices not justified.

Status:
- Unverified

### C-008
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 19
- Snippet: ``Mark all code that may violate safety guarantees with a visible ``unsafe`` keyword``

Claim:
- Text: "All code that may violate safety guarantees must be marked with a visible unsafe keyword."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-KEYWORD`
- Notes: The reference describes unsafe contexts but does not mandate this broader rule.

Status:
- Unverified

### C-009
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 24
- Snippet: ``* ``extern`` blocks must be declared as ``unsafe extern````

Claim:
- Text: "Extern blocks must be declared as unsafe extern."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-EXTERN`
- Notes: Reference requires unsafe extern, with 2024 edition differences.

Status:
- Verified

### C-010
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 25
- Snippet: ``* The ``#[no_mangle]`` attribute must be written as ``#[unsafe(no_mangle)]````

Claim:
- Text: "The no_mangle attribute must be wrapped in unsafe(..)."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Unsafe attributes require unsafe wrapper.

Status:
- Verified

### C-011
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 26
- Snippet: ``* The ``#[export_name]`` attribute must be written as ``#[unsafe(export_name)]````

Claim:
- Text: "The export_name attribute must be wrapped in unsafe(..)."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Unsafe attributes require unsafe wrapper.

Status:
- Verified

### C-012
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 27
- Snippet: ``* The ``#[link_section]`` attribute must be written as ``#[unsafe(link_section)]````

Claim:
- Text: "The link_section attribute must be wrapped in unsafe(..)."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Unsafe attributes require unsafe wrapper.

Status:
- Verified

### C-013
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 31
- Snippet: ``Starting with Rust Edition 2024, the use of ``unsafe`` is required in these contexts.``

Claim:
- Text: "Rust Edition 2024 requires unsafe for these contexts."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-KEYWORD`
- Notes: Reference includes 2024 edition differences.

Status:
- Verified

### C-014
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 42
- Snippet: ``* ``unsafe`` blocks create clear audit boundaries``

Claim:
- Text: "Unsafe blocks create clear audit boundaries for reviewers."
- Type: Rationale

Source:
- Kind: Other
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUSTNOMICON-MEET-SAFE`
- Notes: Nomicon discusses unsafe but does not assert audit boundary claim.

Status:
- Unverified

### C-015
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 44
- Snippet: ``Safety-critical standards like ISO 26262``

Claim:
- Text: "ISO 26262 and DO-178C require traceability of hazardous operations."
- Type: Rationale

Source:
- Kind: Standard
- Citation: :cite:`gui_ZDLZzjeOwLSU:ISO-26262`, :cite:`gui_ZDLZzjeOwLSU:DO-178C`
- Notes: Standard requirements not verified.

Status:
- Unverified

### C-016
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 47
- Snippet: ``* Satisfies ISO 26262 Part 6, Table 1, objective 1c``

Claim:
- Text: "This guideline satisfies ISO 26262 Part 6, Table 1, objective 1c."
- Type: Rationale

Source:
- Kind: Standard
- Citation: :cite:`gui_ZDLZzjeOwLSU:ISO-26262`
- Notes: Coverage claim not verified.

Status:
- Unverified

### C-017
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 52
- Snippet: ``* The ``unsafe`` keyword signals that the programmer is taking responsibility``

Claim:
- Text: "The unsafe keyword signals programmer responsibility for invariants."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-KEYWORD`
- Notes: Reference describes unsafe obligations; specific wording not cited.

Status:
- Unverified

### C-018
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 59
- Snippet: ``* Tools like ``cargo-geiger`` :cite:`gui_ZDLZzjeOwLSU:CARGO-GEIGER`, ``unsafe-inspect``,`

Claim:
- Text: "Tools like cargo-geiger, unsafe-inspect, and custom linters can locate and count unsafe blocks."
- Type: Rationale

Source:
- Kind: Other
- Citation: :cite:`gui_ZDLZzjeOwLSU:CARGO-GEIGER`
- Notes: ``unsafe-inspect`` is uncited.

Status:
- Unverified

### C-019
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 76
- Snippet: ``The ``#[no_mangle]`` attribute is unsafe because it can be used to declare a function``

Claim:
- Text: "Symbol conflicts from no_mangle can cause undefined behavior."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Reference does not classify symbol conflicts as UB.

Status:
- Disputed

### C-020
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 100
- Snippet: ``Rust Edition 2024 enforces that the ``no_mangle`` attribute requires an ``unsafe`` keyword``

Claim:
- Text: "Rust Edition 2024 requires unsafe wrapper for no_mangle."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Unsafe attributes require unsafe wrapper.

Status:
- Verified

### C-021
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 124
- Snippet: ``An ``extern`` block is unsafe because undefined behavior can occur if types or functions are``

Claim:
- Text: "Extern misdeclarations cause UB even if declarations are unused."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-EXTERN`
- Notes: UB arises from use; unused declarations do not cause UB.

Status:
- Disputed

### C-022
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 147
- Snippet: ``Rust Edition 2024 enforces that ``extern "C"`` blocks require an ``unsafe`` keyword``

Claim:
- Text: "Rust Edition 2024 requires unsafe extern blocks."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-EXTERN`
- Notes: Reference documents 2024 edition requirement.

Status:
- Verified

### C-023
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 180
- Snippet: ``The ``#[export_name]`` and ``#[link_section]`` attributes can cause undefined behavior if``

Claim:
- Text: "Misuse of export_name/link_section causes undefined behavior."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Reference does not state misuse is UB.

Status:
- Disputed

### C-024
Location:
- File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
- Line: 215
- Snippet: ``The ``#[export_name]`` and ``#[link_section]`` attributes must use the ``unsafe()`` wrapper``

Claim:
- Text: "export_name and link_section must use unsafe(..) wrapper."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
- Notes: Unsafe attributes require unsafe wrapper.

Status:
- Verified
