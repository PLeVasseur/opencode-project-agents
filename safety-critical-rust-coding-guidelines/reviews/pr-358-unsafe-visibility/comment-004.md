### Location
File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
Line: 124
Snippet: ``An ``extern`` block is unsafe because undefined behavior can occur if types or functions are``

### Type
Blocking

### Comment
The statement "This is true even if the declarations are not used" is not supported; UB stems from *using* incorrect declarations (e.g., calling with the wrong ABI/signature). Please narrow the claim and cite the external blocks or unsafe keyword reference.

```suggestion
      An ``extern`` block is unsafe because undefined behavior can occur if types or functions are misdeclared and
      then used. This noncompliant example requires Rust Edition 2021 or earlier to compile.
```
