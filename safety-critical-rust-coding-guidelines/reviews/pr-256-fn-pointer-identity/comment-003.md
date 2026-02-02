### Location
File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
Line: 39
Snippet: ``Rust's ``fn`` type is a zero-sized function item promoted to a function pointer``

### Type
Blocking

### Comment
This statement is incorrect. Function items are zero-sized types that *coerce* to function pointers; the ``fn`` type itself is the function pointer type. Please rephrase to reflect that distinction.

```suggestion
      Function items are zero-sized types that coerce to function pointers
      :cite:`gui_QbvIknd9qNF6:RUST-REF-FN-PTR`, whose address is determined by the compiler backend.
```
