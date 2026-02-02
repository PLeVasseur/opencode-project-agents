### Location
File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
Line: 28
Snippet: ``You can access a field of a union even when the backing bytes of that field are uninitialized provided that:``

### Type
Blocking

### Comment
This text is incorrect. The Rust Reference requires values to be valid for their type, and integers must be initialized before being read. Uninitialized bytes are not a valid value even for integer types. Please rewrite this paragraph to require full initialization and validity for the accessed type.

```suggestion
   You may read a union field only when the backing bytes are fully initialized and form a valid value for the field's type
   :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION` :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`.
   Uninitialized bytes are not a valid value for scalar types (including integers), so reading them is undefined behavior even
   when all bit patterns are otherwise valid.
```
