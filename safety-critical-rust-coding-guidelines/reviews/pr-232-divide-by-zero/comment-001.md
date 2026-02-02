### Location
File: src/coding-guidelines/expressions/gui_7y0GAMmtMhch.rst.inc
Line: 48
Snippet: `:compile_fail:`

### Type
Blocking

### Comment
Division by zero on integer types is a runtime panic, not a compile-time error. `:compile_fail:` expects a compile error and may silently pass if the compiler doesn't emit an unconditional_panic warning in this context. Please mark this example as `:should_panic:` so it tests the intended runtime behavior. Reference: https://doc.rust-lang.org/reference/expressions/operator-expr.html#arithmetic-operators

```suggestion
          :should_panic:
```
