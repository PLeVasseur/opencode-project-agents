# Claims Map

PR: 305
Guideline IDs: gui_Ncdb5PhhiZyX
Reviewer: OpenCode
Date: 2026-02-02

## Summary Table
| ID | Status | Type | Location | Source Kind | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Unverified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:11 | Other | Category choice not justified. |
| C-002 | Verified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:12 | Other | New guidelines must be draft. |
| C-003 | Unverified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:13 | Other | Release applicability not justified. |
| C-004 | Verified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:14 | FLS | FLS paragraph exists in expressions. |
| C-005 | Unverified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:15 | Other | Decidability choice not justified. |
| C-006 | Disputed | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:16 | Other | ``function`` is not an allowed scope value. |
| C-007 | Unverified | Field-choice | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:17 | Other | Tag choice not justified. |
| C-008 | Unverified | Normative | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:6 | Other | No authoritative source cited. |
| C-009 | Unverified | Normative | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:19 | Standard | Termination requirement not cited in amplification. |
| C-010 | Verified | Normative | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:22 | FLS | FLS definition of infinite loops and never type. |
| C-011 | Unverified | Normative | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:27 | Other | Exception for main control loops not sourced. |
| C-012 | Unverified | Normative | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:32 | Other | Loop-variant conditions not sourced. |
| C-013 | Unverified | Rationale | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:42 | Other | System availability risk not sourced. |
| C-014 | Unverified | Rationale | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:56 | Standard | Standards coverage claim not verified. |
| C-015 | Unverified | Rationale | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:62 | Other | Claim about UB not cited. |
| C-016 | Unverified | Rationale | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:66 | Other | Halting problem claim not sourced. |
| C-017 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:74 | Other | Example classification not sourced. |
| C-018 | Unverified | Example-comment | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:85 | Other | Noncompliant comment not sourced. |
| C-019 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:98 | Other | External input loop claim not sourced. |
| C-020 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:130 | Other | Overflow termination claim not sourced. |
| C-021 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:160 | Other | Progress claim not sourced. |
| C-022 | Disputed | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:184 | Other | Main control loop compliance contradicts guidance. |
| C-023 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:243 | Other | Bounded for-loop claim not sourced. |
| C-024 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:267 | Other | Max retries claim not sourced. |
| C-025 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:315 | Other | Timeout mechanism claim not sourced. |
| C-026 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:363 | Other | Loop variant claim not sourced. |
| C-027 | Unverified | Example-prose | src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst:404 | Other | Iterator boundedness claim not sourced. |

## Legend
- Type: Normative | Rationale | Example-prose | Example-comment | Field-choice
- Source kind: Reference | FLS | UCG | Rustc-dev-guide | Standard (CERT/MISRA/...) | Other
- Status: Verified | Unverified | Disputed

## Claims

### C-001
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
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
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
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
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 13
- Snippet: ``:release: unknown``

Claim:
- Text: "The guideline applies to an unknown set of releases."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Release applicability not justified.

Status:
- Unverified

### C-004
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 14
- Snippet: ``:fls: fls_sf4qnd43z2wc``

Claim:
- Text: "This guideline maps to FLS paragraph fls_sf4qnd43z2wc."
- Type: Field-choice

Source:
- Kind: FLS
- Citation: :cite:`gui_Ncdb5PhhiZyX:FLS-LOOPS`
- Notes: FLS paragraph is the infinite-loops section.

Status:
- Verified

### C-005
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 15
- Snippet: ``:decidability: undecidable``

Claim:
- Text: "The guideline is undecidable to check automatically."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: No justification provided.

Status:
- Unverified

### C-006
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 16
- Snippet: ``:scope: function``

Claim:
- Text: "The guideline scope is function."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: ``function`` is not an allowed scope value.

Status:
- Disputed

### C-007
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 17
- Snippet: ``:tags: safety``

Claim:
- Text: "The guideline tag is safety."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Tag choice not justified.

Status:
- Unverified

### C-008
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 6
- Snippet: ``Ensure all loops have a termination condition that is provably reachable``

Claim:
- Text: "All loops must have a provably reachable termination condition."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-009
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 19
- Snippet: ``All loops shall have a termination condition that can be demonstrated to be reachable``

Claim:
- Text: "All loops must have a demonstrably reachable termination condition under all valid execution paths."
- Type: Normative

Source:
- Kind: Standard
- Citation: :cite:`gui_Ncdb5PhhiZyX:DO-178C`, :cite:`gui_Ncdb5PhhiZyX:ISO-26262`
- Notes: Standards cited in rationale, not amplification.

Status:
- Unverified

### C-010
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 22
- Snippet: ``According to the Rust FLS, an ``infinite loop expression`` is a ``loop expression````

Claim:
- Text: "An infinite loop expression evaluates its body indefinitely and has never type if no break."
- Type: Normative

Source:
- Kind: FLS
- Citation: :cite:`gui_Ncdb5PhhiZyX:FLS-LOOPS`
- Notes: FLS defines infinite loops and their type.

Status:
- Verified

### C-011
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 27
- Snippet: ``Unbounded or potentially infinite loops are prohibited unless they serve as the main``

Claim:
- Text: "Unbounded loops are prohibited unless they are main control loops with external termination."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-012
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 32
- Snippet: ``* Have a compile-time bounded iteration count``

Claim:
- Text: "Loops must satisfy one of the listed termination conditions (bounded count, loop variant, or external termination)."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source cited.

Status:
- Unverified

### C-013
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 42
- Snippet: ``* **System availability**: A non-terminating loop can cause the system to become``

Claim:
- Text: "Non-terminating loops can cause system unavailability and safety-function failure."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-014
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 56
- Snippet: ``* **Certification requirements**: Standards such as DO-178C, ISO 26262, IEC 61508,``

Claim:
- Text: "DO-178C, ISO 26262, IEC 61508, and MISRA C require termination evidence."
- Type: Rationale

Source:
- Kind: Standard
- Citation: :cite:`gui_Ncdb5PhhiZyX:DO-178C`, :cite:`gui_Ncdb5PhhiZyX:ISO-26262`, :cite:`gui_Ncdb5PhhiZyX:IEC-61508`, :cite:`gui_Ncdb5PhhiZyX:MISRA-C-2012`
- Notes: Standard requirements not verified.

Status:
- Unverified

### C-015
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 62
- Snippet: ``Rust does not consider empty infinite loops to be undefined behavior.``

Claim:
- Text: "Empty infinite loops are not undefined behavior in Rust."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No reference cited.

Status:
- Unverified

### C-016
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 66
- Snippet: ``Loop termination is generally undecidable (the halting problem)``

Claim:
- Text: "Loop termination is generally undecidable (halting problem)."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source cited.

Status:
- Unverified

### C-017
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 74
- Snippet: ``An unconditional infinite loop with no termination mechanism.``

Claim:
- Text: "The example is an unconditional infinite loop with no termination mechanism."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-018
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 85
- Snippet: ``// Non-compliant: no termination condition``

Claim:
- Text: "The loop has no termination condition."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-019
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 98
- Snippet: ``This noncompliant example contains a loop whose termination depends on external input``

Claim:
- Text: "The loop termination depends on external input that may never arrive."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-020
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 130
- Snippet: ``This noncompliant example contains a loop with a termination condition that may never be``

Claim:
- Text: "Termination may never be satisfied due to integer overflow/wrapping."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-021
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 160
- Snippet: ``This noncompliant example contains a loop that depends on a condition modified by``

Claim:
- Text: "Loop termination depends on another thread without guaranteed progress."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-022
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 184
- Snippet: ``This noncompliant solution contains a main control loop with documented external termination.``

Claim:
- Text: "A main control loop with external termination must still be treated as noncompliant and requires deviation."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Contradicts earlier allowance in guideline.

Status:
- Disputed

### C-023
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 243
- Snippet: ``This compliant solution contains a simple ``for`` loop with a compile-time bounded iteration count.``

Claim:
- Text: "A compile-time bounded for-loop is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-024
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 267
- Snippet: ``This compliant example contains a loop with an explicit maximum iteration bound.``

Claim:
- Text: "A loop bounded by a fixed max retry count is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-025
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 315
- Snippet: ``This compliant example contains a loop with a timeout mechanism.``

Claim:
- Text: "A timeout-bounded loop is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-026
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 363
- Snippet: ``This compliant example contains a loop with a provable loop variant``

Claim:
- Text: "A loop with a provable variant is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified

### C-027
Location:
- File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
- Line: 404
- Snippet: ``This compliant example contains an iterator-based loop with bounded collection size.``

Claim:
- Text: "Iterator-based loops bounded by collection size are compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: Illustrative example.

Status:
- Unverified
