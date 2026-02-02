# Issue 648 report

## Issue
- Title: [Change]: [1.93] During const-evaluation, support copying pointers byte-by-byte
- Link: https://github.com/rust-lang/fls/issues/648
- Rust PR: https://github.com/rust-lang/rust/pull/148259

## Impact assessment
- No FLS text change applied. The FLS defines which constructs are constant expressions and the high-level static-error conditions (src/expressions.rst:160-342), but it does not define a byte-level const-eval memory model, pointer provenance, or pointer representation in memory.
- The constant-expression list explicitly excludes pointer-to-address and function-pointer-to-address casts (src/expressions.rst:254-256), reinforcing that raw pointer byte representations are outside the specified const-eval surface.
- Raw pointer types are defined in terms of type properties (src/types-and-traits.rst:1006-1029) without specifying representation or provenance rules; the change in rust-lang/rust#148259 is about interpreter-level pointer fragment tracking.
- Precedent in the FLS changelog treats similar const-eval pointer behavior as out-of-scope (Rust 1.86 entry: “More pointers are now detected as definitely not-null based on their alignment in const eval” with “No change: The concrete semantics of constant evaluation is not described within the FLS” in src/changelog.rst:412-414).
- Capturing this change normatively would require a broader const-eval memory/provenance specification; a one-off rule would be incomplete and inconsistent with existing FLS scope.

## Evidence excerpts
- `src/expressions.rst:254-257`
  ```
  * :dp:`fls_e0a1e8ddph7`
    :t:`[Type cast expression]s` that are not :t:`[pointer-to-address cast]s`,
    :t:`[function-pointer-to-address cast]s`, and :t:`[unsized coercion]s` that
    involve a :t:`trait object type`,
  ```
- `src/types-and-traits.rst:1018-1019`
  ```
  :dp:`fls_rpbhr0xukbx9`
  A :t:`raw pointer type` is an :t:`indirection type` without validity guarantees.
  ```
- `src/changelog.rst:419-421`
  ```
  - `More pointers are now detected as definitely not-null based on their alignment in const eval. <https://github.com/rust-lang/rust/pull/133700>`_

    - No change: The concrete semantics of constant evaluation is not described within the FLS
  ```

## Spec updates
- Files changed: src/changelog.rst
- Syntax changes: none
- Paragraph IDs: none

## Validation
- Positive snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-648/const_eval_pointer_copy_positive.rs
  - rustc: `rustc +1.93.0 const_eval_pointer_copy_positive.rs` (success)
- Negative snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-648/const_eval_pointer_copy_negative.rs
  - rustc: `rustc +1.93.0 const_eval_pointer_copy_negative.rs`
  - Error: E0080 (const-eval rejected use of pointer byte representation; “absolute address of a pointer is not known at compile-time”)
- Build: `./make.py` (success)

## Reference alignment
- No Rust Reference PR was linked from rust-lang/rust#148259. The Reference does not currently specify const-eval pointer provenance or byte-level pointer copying semantics, so no alignment updates were made.

## Non-normative references
- rustc-dev-guide (const-eval overview): https://rustc-dev-guide.rust-lang.org/const-eval.html
  - Context for CTFE as an interpreter over MIR; describes evaluation stages but is not a language specification.
- rustc-dev-guide (CTFE interpreter memory model): https://rustc-dev-guide.rust-lang.org/const-eval/interpret.html
  - Explains virtual memory, allocation IDs, and pointer storage during const evaluation, which is the implementation layer affected by rust-lang/rust#148259.
- Miri (implementation reference): https://github.com/rust-lang/miri
  - Miri shares the CTFE interpreter and documents that it approximates Rust UB and is updated with the compiler; useful context for pointer/provenance behavior but non-normative.

### Excerpts
- rustc-dev-guide `const-eval/interpret.html#memory`
  ```
  Such an `Allocation` is basically just a sequence of `u8` storing the value of each byte in this allocation.
  ... a `Pointer` consists of a pair of an `AllocId` ... and an offset into the allocation.
  ... we want to store a `Pointer` into an `Allocation`: ... the `relocation` field ... stores the byte offset
  as a bunch of `u8`, while its `AllocId` gets stored out-of-band.
  ```
- UCG glossary `glossary.html#abstract-byte`
  ```
  Another piece of shadow state is pointer provenance ... implies that abstract bytes must be able to carry provenance.
  ... Init(u8, Option<Provenance>)
  ```
- UCG glossary `glossary.html#pointer-provenance`
  ```
  The provenance of a pointer is used to distinguish pointers that point to the same memory address ...
  ```
