# Stale branch fix plan - 2026-02-02

## PR 368 - [Coding Guideline] Revise guideline on unsafe code in macros
- URL: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/368
- Head: rcseacord:patch-6 (cross-repo)
- Base: main
- Mergeable: CONFLICTING (DIRTY)
- Failing checks:
  - build (Build workflow)
  - Netlify deploy (Header rules, Pages changed, Redirect rules)
- Planned actions:
  - Rebase on latest main.
  - Inspect build failure log for root error; fix doc/rust example issues as needed.
  - Netlify failures likely downstream of build; re-check after build passes.

## PR 358 - [Coding Rule]: assure visibility of unsafe keyword in unsafe code
- URL: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/358
- Head: rcseacord:guideline/unsafetoken (cross-repo)
- Base: main
- Mergeable: CONFLICTING (DIRTY)
- Failing checks:
  - check_rust_examples / Test Guidelines (Stable)
  - build (Build workflow)
  - Netlify deploy (Header rules, Pages changed, Redirect rules)
- Planned actions:
  - Rebase on latest main.
  - Inspect Test Guidelines (Stable) failure log, fix example issues.
  - Verify build after example fixes; Netlify expected to clear once build is green.

## PR 305 - [Coding Guideline]: Ensure all loops have a termination condition that is provably reachable
- URL: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/305
- Head: rcseacord:guideline/infloop (cross-repo)
- Base: main
- Mergeable: CONFLICTING (DIRTY)
- Failing checks:
  - Netlify deploy (Header rules, Pages changed, Redirect rules)
- Planned actions:
  - Rebase on latest main.
  - Identify source of Netlify failure; likely build or doc header format issue.
  - Run build to confirm and fix any doc header or example issues.

## PR 256 - [Coding Guideline]: Do Not Depend on Function Pointer Identity
- URL: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/256
- Head: rcseacord:feat/fpident (cross-repo)
- Base: main
- Mergeable: CONFLICTING (DIRTY)
- Failing checks:
  - check_rust_examples / Test Guidelines (Stable)
  - Netlify deploy (Header rules, Pages changed, Redirect rules)
- Planned actions:
  - Rebase on latest main.
  - Inspect Test Guidelines (Stable) failure log, fix example issues.
  - Confirm Netlify clears after build/tests pass.
