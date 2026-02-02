# Claims Map

PR: 302
Guideline IDs: gui_6JSM7YE7a1KR
Reviewer: OpenCode
Date: 2026-02-02

## Summary Table
| ID | Status | Type | Location | Source Kind | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:8 | Other | Category choice not justified. |
| C-002 | Verified | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:9 | Other | New guidelines must be draft per style guide. |
| C-003 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:10 | Other | Release applicability not justified. |
| C-004 | Disputed | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:11 | FLS | FLS paragraph is in Values chapter; chapter mismatch. |
| C-005 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:12 | Other | Decidability choice not justified. |
| C-006 | Disputed | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:13 | Other | ``expression`` is not an allowed scope value. |
| C-007 | Unverified | Field-choice | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:14 | Other | Tag choices not justified. |
| C-008 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:6 | Reference | Union reads must be valid; uninitialized bytes are invalid. |
| C-009 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:16 | Reference | Invalid values are UB; union reads require validity. |
| C-010 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:17 | Reference | Uninitialized bytes are invalid values. |
| C-011 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:22 | Reference | Union reads must be valid at field type. |
| C-012 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:23 | Reference | Unions share storage; writing one field overwrites others. |
| C-013 | Unverified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:24 | Other | Reassignment semantics not cited. |
| C-014 | Unverified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:25 | Other | Recommendation to prefer ``MaybeUninit`` not cited. |
| C-015 | Disputed | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:28 | Reference | Uninitialized bytes are invalid for scalar types. |
| C-016 | Verified | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:31 | Reference | Union reads must be valid for the field type. |
| C-017 | Disputed | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:34 | Reference | Integers must be initialized before being read. |
| C-018 | Disputed | Normative | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:74 | Reference | Union reads are only valid when bytes form a valid value. |
| C-019 | Verified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:41 | Reference | Unions share common storage. |
| C-020 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:42 | Other | Partial initialization effects not cited. |
| C-021 | Verified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:44 | Reference | Reading uninitialized bytes is UB. |
| C-022 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:48 | Other | Silent data corruption claim not sourced. |
| C-023 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:51 | Other | Function merging/UB interaction not sourced. |
| C-024 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:61 | Other | Reassignment resets initialization not sourced. |
| C-025 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:65 | Other | Compiler warning behavior not sourced. |
| C-026 | Unverified | Rationale | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:70 | Other | Raw pointer access/typed read requirement not sourced. |
| C-027 | Verified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:83 | Reference | Partial initialization leads to UB on read. |
| C-028 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:96 | Reference | Only first byte initialized. |
| C-029 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:98 | Reference | Reading uninitialized value is UB. |
| C-030 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:110 | Other | Reassignment preserves init claim not sourced. |
| C-031 | Unverified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:121 | Other | Reassignment invalidates init not sourced. |
| C-032 | Unverified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:129 | Other | ``init`` uninitialized after reassignment not sourced. |
| C-033 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:41 | Other | Function pointer comparison + optimization claim not sourced. |
| C-034 | Verified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:82 | Reference | Fully initializing before read avoids UB. |
| C-035 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:95 | Reference | Initializes all bytes. |
| C-036 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:102 | Reference | Both bytes initialized. |
| C-037 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:210 | Other | ``MaybeUninit`` guidance not cited. |
| C-038 | Verified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:238 | Reference | Full-field initialization is valid. |
| C-039 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:49 | Reference | Initialize entire field at once. |
| C-040 | Verified | Example-comment | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:57 | Reference | All bytes initialized. |
| C-041 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:65 | Other | Function pointer comparison avoidance not sourced. |
| C-042 | Unverified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:314 | Other | Bit-pattern claim not cited. |
| C-043 | Verified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:334 | Reference | Union field reads allowed if valid. |
| C-044 | Verified | Example-prose | src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc:53 | Reference | Unions do not relax type validity. |

## Legend
- Type: Normative | Rationale | Example-prose | Example-comment | Field-choice
- Source kind: Reference | FLS | UCG | Rustc-dev-guide | Standard (CERT/MISRA/...) | Other
- Status: Verified | Unverified | Disputed

## Claims

### C-001
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 8
- Snippet: ``:category: required``

Claim:
- Text: "The guideline category is required."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Category is a required field with allowed values.

Status:
- Unverified

### C-002
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 9
- Snippet: ``:status: draft``

Claim:
- Text: "The guideline status is draft."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: New guidelines must be marked draft initially.

Status:
- Verified

### C-003
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 10
- Snippet: ``:release: 1.85.0``

Claim:
- Text: "The guideline applies starting in Rust 1.85.0."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: No evidence provided for release applicability.

Status:
- Unverified

### C-004
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 11
- Snippet: ``:fls: fls_6lg0oaaopc26``

Claim:
- Text: "This guideline maps to FLS paragraph fls_6lg0oaaopc26."
- Type: Field-choice

Source:
- Kind: FLS
- Citation: src/spec.lock (values.html#fls_6lg0oaaopc26)
- Notes: Paragraph is in Values chapter, mismatching placement.

Status:
- Disputed

### C-005
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 12
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
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 13
- Snippet: ``:scope: expression``

Claim:
- Text: "The guideline scope is expression."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: ``expression`` is not an allowed scope value.

Status:
- Disputed

### C-007
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 14
- Snippet: ``:tags: unions, initialization, undefined-behavior``

Claim:
- Text: "The guideline tags are unions, initialization, undefined-behavior."
- Type: Field-choice

Source:
- Kind: Other
- Citation: src/process/style-guideline.rst
- Notes: Tag choices not justified.

Status:
- Unverified

### C-008
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 6
- Snippet: ``Do not read from union fields that may contain uninitialized bytes``

Claim:
- Text: "Do not read from union fields that may contain uninitialized bytes."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Reading uninitialized bytes produces invalid values (UB).

Status:
- Verified

### C-009
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 16
- Snippet: ``Do not read from a union field unless all bytes of that field have been explicitly initialized.``

Claim:
- Text: "Do not read from a union field unless all bytes of that field have been explicitly initialized."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Scalars must be initialized before being read.

Status:
- Verified

### C-010
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 17
- Snippet: ``Partial initialization of a union's composite field leaves some bytes in an uninitialized state,``

Claim:
- Text: "Partial initialization leaves some bytes uninitialized; reading those bytes is undefined behavior."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Uninitialized bytes are invalid values.

Status:
- Verified

### C-011
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 22
- Snippet: ``* Initialize all bytes of a field before reading from it``

Claim:
- Text: "Initialize all bytes of a field before reading from it."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Uninitialized bytes are invalid for scalars.

Status:
- Verified

### C-012
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 23
- Snippet: ``* Do not assume that initializing one variant preserves the initialized state of another``

Claim:
- Text: "Initializing one union variant does not preserve the initialized state of another."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Unions share storage; writes overwrite other fields.

Status:
- Verified

### C-013
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 24
- Snippet: ``* Do not rely on prior initialization of a union before reassignment``

Claim:
- Text: "Prior initialization cannot be relied on after reassignment."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: No authoritative source provided.

Status:
- Unverified

### C-014
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 25
- Snippet: ``* Use ``MaybeUninit`` with proper initialization patterns rather than custom unions for``

Claim:
- Text: "Use MaybeUninit rather than custom unions to manage uninitialized memory."
- Type: Normative

Source:
- Kind: Other
- Citation: None
- Notes: Recommendation not sourced.

Status:
- Unverified

### C-015
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 28
- Snippet: ``You can access a field of a union even when the backing bytes of that field are uninitialized provided that:``

Claim:
- Text: "You can access a union field even when its backing bytes are uninitialized if the resulting value has a well-defined bit pattern."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Uninitialized bytes are invalid for scalar values.

Status:
- Disputed

### C-016
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 31
- Snippet: ``Interpreting that value must still comply with the requirements of the accessed type``

Claim:
- Text: "Union field reads must comply with the validity requirements of the accessed type."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Union reads must be valid for the field type.

Status:
- Verified

### C-017
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 34
- Snippet: ``For example, reading an uninitialized ``u32`` field of a union is allowed;``

Claim:
- Text: "Reading an uninitialized u32 field of a union is allowed; reading an uninitialized bool is disallowed."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Integers must be initialized; uninitialized u32 is invalid.

Status:
- Disputed

### C-018
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 74
- Snippet: ``The sole exception is that unions work like C unions:``

Claim:
- Text: "Any union field may be read even if never written, provided the bytes form a valid representation."
- Type: Normative

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Union reads are only defined when the value is valid; no general exception.

Status:
- Disputed

### C-019
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 41
- Snippet: ``Unions in Rust allow multiple fields to share the same memory.``

Claim:
- Text: "Unions allow multiple fields to share the same memory."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Union fields share common storage.

Status:
- Verified

### C-020
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 42
- Snippet: ``When a union field is a composite type (tuple, struct, array),``

Claim:
- Text: "Partial initialization of composite union fields leaves remaining bytes indeterminate."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No citation provided.

Status:
- Unverified

### C-021
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 44
- Snippet: ``Reading these uninitialized bytes is undefined behavior``

Claim:
- Text: "Reading uninitialized bytes is undefined behavior."
- Type: Rationale

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Uninitialized values are invalid.

Status:
- Verified

### C-022
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 48
- Snippet: ``* **Silent data corruption**: The program may appear to work, reading stale``

Claim:
- Text: "Partial initialization can lead to silent data corruption in testing."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-023
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 51
- Snippet: ``* **Optimization interactions**: The compiler may merge, inline, or deduplicate``

Claim:
- Text: "Compiler optimizations (merging/inlining) can make partially-initialized code paths execute and introduce UB."
- Type: Rationale

Source:
- Kind: Other
- Citation: :cite:`gui_6JSM7YE7a1KR:LLVM-MERGE`
- Notes: LLVM merge documentation does not directly establish UB claim.

Status:
- Unverified

### C-024
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 61
- Snippet: ``* **Reassignment resets initialization**: Assigning a new value to a union``

Claim:
- Text: "Assigning a new value to a union does not preserve initialization of other fields."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-025
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 65
- Snippet: ``* **Nested partial initialization**: When a union variant contains a``

Claim:
- Text: "Partial initialization of nested structs leaves other fields uninitialized, and the compiler does not warn."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-026
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 70
- Snippet: ``Fields of a struct can be individually accessed using a raw pointer.``

Claim:
- Text: "Reading a struct value or forming a reference requires all fields to be initialized before a typed read."
- Type: Rationale

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-027
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 83
- Snippet: ``This noncompliant example partially initializes a tuple field, leaving the second element uninitialized.``

Claim:
- Text: "The example partially initializes a tuple field, leaving a byte uninitialized."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Reading uninitialized bytes is UB.

Status:
- Verified

### C-028
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 96
- Snippet: ``a.init.0 = 1; // Only initializes the first byte``

Claim:
- Text: "Only the first byte is initialized."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Initialization of one field does not initialize others.

Status:
- Verified

### C-029
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 98
- Snippet: ``// Undefined behavior reading uninitialized value``

Claim:
- Text: "Reading the uninitialized value is undefined behavior."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Uninitialized values are invalid.

Status:
- Verified

### C-030
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 110
- Snippet: ``This noncompliant example assumes prior initialization is preserved after reassignment.``

Claim:
- Text: "Prior initialization is preserved after reassignment."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-031
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 121
- Snippet: ``// Reassignment invalidates all prior initialization``

Claim:
- Text: "Reassignment invalidates all prior initialization."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-032
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 129
- Snippet: ``// 'init' is uninitialized after reassignment``

Claim:
- Text: "The ``init`` field is uninitialized after reassignment."
- Type: Example-comment

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-033
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 41
- Snippet: ``This noncompliant example combines function pointer comparison with partial initialization,``

Claim:
- Text: "Function pointer comparison combined with partial initialization can introduce UB via optimization."
- Type: Example-prose

Source:
- Kind: Other
- Citation: :cite:`gui_6JSM7YE7a1KR:LLVM-MERGE`
- Notes: No direct support for UB claim.

Status:
- Unverified

### C-034
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 82
- Snippet: ``This compliant examples initializes all bytes of the field before reading.``

Claim:
- Text: "Initializing all bytes before reading is compliant."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Full initialization avoids invalid values.

Status:
- Verified

### C-035
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 95
- Snippet: ``a.init.1 = 2;  // Initialize all bytes``

Claim:
- Text: "The second byte is initialized; all bytes are initialized."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Initialization required before read.

Status:
- Verified

### C-036
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 102
- Snippet: ``// Both bytes are initialized``

Claim:
- Text: "Both bytes are initialized."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Initialization required for validity.

Status:
- Verified

### C-037
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 210
- Snippet: ``This compliant example uses ``MaybeUninit`` with proper initialization patterns.``

Claim:
- Text: "Using ``MaybeUninit`` with proper initialization is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-038
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 238
- Snippet: ``This compliant example initializes through the composite field directly.``

Claim:
- Text: "Initializing the entire composite field at once is compliant."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Full initialization avoids invalid values.

Status:
- Verified

### C-039
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 49
- Snippet: ``//  Initialize entire field at once``

Claim:
- Text: "The entire field is initialized at once."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Full initialization is required before read.

Status:
- Verified

### C-040
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 57
- Snippet: ``// All bytes in 'd' are initialized``

Claim:
- Text: "All bytes in ``d`` are initialized."
- Type: Example-comment

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Full initialization required.

Status:
- Verified

### C-041
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 65
- Snippet: ``This compliant example avoids relying on function pointer comparisons.``

Claim:
- Text: "Avoiding function pointer comparisons is compliant."
- Type: Example-prose

Source:
- Kind: Other
- Citation: None
- Notes: No source provided.

Status:
- Unverified

### C-042
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 314
- Snippet: ``Types such as ``u8``, ``u16``, ``u32``, and ``i128`` allow all possible bit patterns.``

Claim:
- Text: "Integer types allow all possible bit patterns; if memory is initialized there is no UB."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`
- Notes: Bit-pattern validity for integers not cited in text.

Status:
- Unverified

### C-043
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 334
- Snippet: ``The following code reads a union field:``

Claim:
- Text: "Union field reads are allowed when the value is valid."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Union reads are allowed in unsafe with valid values.

Status:
- Verified

### C-044
Location:
- File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
- Line: 53
- Snippet: ``Even though unions allow reads of any field, not all bit patterns are valid for a ``bool``.``

Claim:
- Text: "Unions do not relax type validity requirements; invalid bool values are UB."
- Type: Example-prose

Source:
- Kind: Reference
- Citation: :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION`
- Notes: Union reads must be valid for the field type.

Status:
- Verified
