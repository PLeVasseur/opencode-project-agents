## Summary
- Deduplicate two reused `:dp:` IDs inherited from mainline by updating glossary entries only.
- Add a standalone `FLS maintenance corrections` changelog section documenting the old->new ID mapping.
- Keep canonical IDs in `src/types-and-traits.rst` unchanged and re-ID the duplicate glossary entries.
- Reduce duplicate paragraph IDs across `src/` from 2 to 0.

## Reference alignment
- No Rust language-rule semantic changes.
- This is historical FLS maintenance (paragraph-ID integrity correction), so it is documented outside the Rust 1.93 language-change item.

## Testing
- `./make.py`
- Duplicate `:dp:` inventory before/after (before: 2 duplicates, after: 0 duplicates)
