### Location
File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
Line: 103
Snippet: ``NOTE: This code can still have undefined behavior if the ``convert`` function symbol is``

### Type
Non-blocking

### Comment
``:miri: skip`` is used in this example (and others) without a justification. Please add a brief note explaining why Miri is skipped (e.g., link-time attributes/FFI not supported by Miri).

```suggestion
      NOTE: Miri is skipped here because link-time attributes like ``no_mangle`` are not supported by Miri.
```
