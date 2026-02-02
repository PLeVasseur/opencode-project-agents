# Issue 649 report

## Issue
- Title: [Change]: [1.93] LUB coercions now correctly handle function item types, and functions with differing safeties
- Link: https://github.com/rust-lang/fls/issues/649
- Rust PR: https://github.com/rust-lang/rust/pull/148602

## Impact assessment
- FLS updated to make LUB selection rules explicit for safe vs unsafe function pointer results, and to define safe/unsafe function signature subtyping for coercion.
- Added a target_feature coercion restriction mirroring the Reference: safe target_feature functions only coerce to safe function pointers in feature-enabled contexts; otherwise only unsafe function pointer coercions are allowed.

## Spec updates
- Files changed: src/attributes.rst, src/types-and-traits.rst, src/changelog.rst
- Syntax changes: none
- New paragraph IDs: :p:`fls_ReYuWzijQ1aL`, :p:`fls_yhtOWsxAcccM`, :p:`fls_rRegjSIudDM1`

## Validation
- Positive snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-649/lub_coercion_safety_positive.rs
  - rustc: `rustc +1.93.0 lub_coercion_safety_positive.rs` (success)
- Negative snippet: /home/pete.levasseur/opencode-project-agents/fls/reports/issue-649/target_feature_coercion_negative.rs
  - rustc: `rustc +1.93.0 target_feature_coercion_negative.rs`
  - Error: E0308 (cannot coerce #[target_feature] function to safe fn pointer)
- Build: `./make.py` (success)

## Reference alignment
- LUB coercions: https://doc.rust-lang.org/reference/type-coercions.html#least-upper-bound-coercions
- target_feature restrictions: https://doc.rust-lang.org/reference/attributes/codegen.html#target_feature
- Alignment: Added explicit safe/unsafe LUB selection and target_feature coercion restriction to match Reference behavior; no deviations recorded.
