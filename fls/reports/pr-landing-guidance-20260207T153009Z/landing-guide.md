# PR landing guide (dedupe + tooling + ABI)

## Recommended landing order
- 1) **Dedupe PR first** from `dedupe-paragraph-ids-mainline` (`0165ee6ad6e7e6a54705458d491810b0481b7df4`).
- 2) **Tooling PR second** from `changelog-assistant-paragraph-buckets-inline-tags-on-dedupe-20260207T144017Z` (`0c590c4f6143b958b73fd793d19855f1e53c1880`) on top of assistant stack.
- 3) **ABI docs PR third** from `system-abi-variadic-on-dedupe` (`1d98249e1078b45836a337d18a7df398ca5f72c9`), regenerating changelog with dedupe boundary base.

Why this order:
- Keeps ID-integrity fix separate from ABI language alignment changes.
- Keeps tooling behavior changes reviewable on the tooling branch (not mixed into ABI docs PR).
- Prevents dedupe spillover from appearing in ABI changelog item.

## Branch/PR split to keep
- **PR A (dedupe):** only paragraph ID dedup in `src/glossary.rst`.
- **PR B (tooling):** `tools/changelog_assistant.py` paragraph-bucket rendering + validations.
- **PR C (ABI):** `src/ffi.rst`, `src/glossary.rst` ABI changes and `src/changelog.rst` ABI entry generated with dedupe-base scope.

## Critical generation rule for ABI PR
Use dedupe boundary for assistant base so dedupe fixes do not enter ABI item:

```bash
BASE_REF="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --upstream-pr "https://github.com/rust-lang/rust/pull/145954" \
  --title "Stabilize declaration of C-style variadic functions for the system ABI"
```

This produced the ABI-only set (8 added / 12 changed), excluding dedupe spillover.

## Manual changelog handling for dedupe PR

### Why dedupe should not be bundled under the 1.93 ABI item
- Dedupe is a **historical FLS ID integrity correction**, not a new Rust 1.93 language change.
- The reused IDs were historical collisions:
  - `fls_t4yeovFm83Wo` already used in `src/types-and-traits.rst:652` (discriminant), but had also been used in glossary before dedupe.
  - `fls_I9JaKZelMiby` already used in `src/types-and-traits.rst:2742` (subtrait), but had also been used in glossary before dedupe.
- Dedupe commit moved glossary definitions to unique IDs:
  - `src/glossary.rst:1815` -> `fls_kqdvWGi9cglm` (`discriminant type`)
  - `src/glossary.rst:3938` -> `fls_H5vkbMFvzrFs` (`local trait`)
- Historical origin examples are old maintenance commits (`db1d93f...`, `0975f44...`), not a single current Rust release-note item.

### Recommended placement
Add a small **non-release maintenance** subsection in `src/changelog.rst` (before `Language changes in Rust 1.93.0`) for this one-off correction.

Suggested manual entry:

```rst
FLS maintenance corrections
---------------------------

- Deduplicate historically reused paragraph IDs in the glossary (ID-integrity fix).

  - Corrected glossary `discriminant type` paragraph ID:
    - old reused ID: ``fls_t4yeovFm83Wo``
    - new unique ID: ``fls_kqdvWGi9cglm``
  - Corrected glossary `local trait` paragraph ID:
    - old reused ID: ``fls_I9JaKZelMiby``
    - new unique ID: ``fls_H5vkbMFvzrFs``
  - This is a historical FLS maintenance correction (no Rust language semantics change).
```

### If maintainers require release-only sections
Fallback: place the same text as a dedicated "FLS maintenance correction" bullet at the top of `Language changes in Rust 1.93.0`, explicitly marked as historical correction and not tied to a specific Rust release item.

## Practical landing checklist
- [ ] Open PR A (dedupe) first; keep it tiny and self-contained.
- [ ] Open PR B (tooling) second; include verifier output and assistant behavior checks.
- [ ] Rebase PR C (ABI) after A/B as needed.
- [ ] Re-run changelog assistant for PR C with dedupe-boundary base.
- [ ] Confirm ABI item contains only ABI-scope paragraphs, then merge PR C.

## Notes
- Current integration branch (`b4e9f07813f228541e15a59f67b134d2ec9424d1`) is useful for validation, but for landing upstream, keeping A/B/C split improves reviewability and reduces risk.
