### Location
File: src/coding-guidelines/expressions/gui_kMbiWbn8Z6g5.rst.inc
Line: 55
Snippet: `:compile_fail:`

### Type
Blocking

### Comment
This example demonstrates a runtime panic (division by zero), not a compile-time error. Please use `:should_panic:` so the example aligns with the Rust Reference semantics for integer division. Reference: https://doc.rust-lang.org/reference/expressions/operator-expr.html#arithmetic-operators

```suggestion
          :should_panic:
```
