### Location
File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
Line: 74
Snippet: ``The sole exception is that unions work like C unions:``

### Type
Blocking

### Comment
This paragraph is misleading. Unions do not provide a general exception that permits reading fields that were never written; reads are only defined when the bytes form a valid value for the accessed type. Please restate this in terms of validity requirements for union field reads.

```suggestion
   Unions do not track an active field; every field read is a typed read and must satisfy the validity requirements of the
   accessed type :cite:`gui_6JSM7YE7a1KR:RUST-REF-UNION` :cite:`gui_6JSM7YE7a1KR:RUST-REF-UB`.
```
