### Location
File: src/coding-guidelines/types-and-traits/gui_xztNdXA2oFNC.rst.inc
Line: 45
Snippet: `Aliases cannot do this, because they are not distinct types.`

### Type
Non-blocking

### Comment
This is a factual claim about type aliases not creating distinct types. Please back it with a Rust Reference citation so readers can verify semantics in a safety-critical context. Reference: https://doc.rust-lang.org/reference/items/type-aliases.html

```suggestion
Aliases cannot do this, because they are not distinct types :cite:`gui_xztNdXA2oFNC:RUST-REF-TYPE-ALIASES`.
```
