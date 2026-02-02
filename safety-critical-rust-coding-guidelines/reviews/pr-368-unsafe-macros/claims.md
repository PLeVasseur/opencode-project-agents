# Claims Map

PR: 368
Guideline IDs: gui_FRLaMIMb4t3S
Reviewer: OpenCode
Date: 2026-02-02

## Summary Table
| ID | Status | Type | Location | Source Kind | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Unverified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:11 | Other | Category choice not justified. |
| C-002 | Verified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:12 | Other | New guidelines must be draft per style guide. |
| C-003 | Unverified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:13 | Other | Release applicability not justified. |
| C-004 | Disputed | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:14 | FLS | FLS paragraph is Attribute Macros; content is macro_rules. |
| C-005 | Unverified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:15 | Other | Decidability choice not justified. |
| C-006 | Unverified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:16 | Other | Scope choice not justified. |
| C-007 | Unverified | Field-choice | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:17 | Other | Tag choices not justified. |
| C-008 | Unverified | Normative | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:6 | Other | No sources provided. |
| C-009 | Unverified | Normative | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:19 | Other | No sources provided. |
| C-010 | Unverified | Normative | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:20 | Other | No sources provided. |
| C-011 | Unverified | Rationale | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:26 | Other | No sources provided. |
| C-012 | Unverified | Example-prose | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:32 | Other | No sources provided. |
| C-013 | Unverified | Example-comment | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:38 | Other | No sources provided. |
| C-014 | Unverified | Example-comment | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:48 | Other | No sources provided. |
| C-015 | Unverified | Example-prose | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:56 | Other | No sources provided. |
| C-016 | Unverified | Example-comment | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:63 | Other | No sources provided. |
| C-017 | Unverified | Example-comment | src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst:73 | Other | No sources provided. |

## Legend
- Type: Normative | Rationale | Example-prose | Example-comment | Field-choice
- Source kind: Reference | FLS | UCG | Rustc-dev-guide | Standard (CERT/MISRA/...) | Other
- Status: Verified | Unverified | Disputed

## Claims

### C-001
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 11
- Snippet: ``:category: advisory``

Claim:
- Text: "The guideline category is advisory."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Category values are defined; choice not justified.

Status:
- Unverified

### C-002
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 12
- Snippet: ``:status: draft``

Claim:
- Text: "The guideline status is draft."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: New guidelines must start as draft.

Status:
- Verified

### C-003
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
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
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 14
- Snippet: ``:fls: fls_4vjbkm4ceymk``

Claim:
- Text: "This guideline maps to FLS paragraph fls_4vjbkm4ceymk."
- Type: Field-choice

Source:
- Kind: FLS
- Citation: src/spec.lock (macros.html#attribute-macros)
- Notes: Paragraph is Attribute Macros; guideline covers macro_rules.

Status:
- Disputed

### C-005
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
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
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 16
- Snippet: ``:scope: module``

Claim:
- Text: "The guideline scope is module."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Scope choice not justified.

Status:
- Unverified

### C-007
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 17
- Snippet: ``:tags: safety, reduce-human-error``

Claim:
- Text: "The guideline tags are safety and reduce-human-error."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Tag choices not justified.

Status:
- Unverified

### C-008
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 6
- Snippet: ``Do not hide unsafe code in macros``

Claim:
- Text: "Do not hide unsafe code in macros."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-009
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 19
- Snippet: ``Do not hide unsafe code in macro definitions.``

Claim:
- Text: "Do not hide unsafe code in macro definitions."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-010
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 20
- Snippet: ``Macros that expand to unsafe code should preserve the ``unsafe`` token visibility.``

Claim:
- Text: "Macros that expand to unsafe code should preserve the unsafe token visibility."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-011
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 26
- Snippet: ``Macros that generate unsafe code obscure safety-critical code, making the code more difficult to review and audit.``

Claim:
- Text: "Macros that generate unsafe code obscure safety-critical code and hinder review."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-012
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 32
- Snippet: ``Macros that generate unsafe code without preserving the ``unsafe`` token visibility obscure safety-critical code.``

Claim:
- Text: "Hidden unsafe macro expansions obscure safety-critical code."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-013
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 38
- Snippet: ``// This macro hides the unsafe token from callers - noncompliant``

Claim:
- Text: "The macro hides the unsafe token from callers."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-014
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 48
- Snippet: ``// The unsafe operation is hidden from the caller``

Claim:
- Text: "The unsafe operation is hidden from the caller."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-015
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 56
- Snippet: ``This compliant example requires the caller to wrap the macro invocation in an ``unsafe`` block,``

Claim:
- Text: "Wrapping the macro invocation in an unsafe block makes unsafe use visible."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-016
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 63
- Snippet: ``// This macro requires the caller to acknowledge the unsafe operation - compliant``

Claim:
- Text: "The macro requires callers to acknowledge the unsafe operation."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-017
Location:
- File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
- Line: 73
- Snippet: ``// The unsafe operation is visible at the call site``

Claim:
- Text: "The unsafe operation is visible at the call site."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified
