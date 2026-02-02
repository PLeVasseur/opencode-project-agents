### Location
File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
Line: 180
Snippet: ``The ``#[export_name]`` and ``#[link_section]`` attributes can cause undefined behavior if``

### Type
Blocking

### Comment
The Rust Reference classifies these as unsafe attributes, but it does not state that misuse is necessarily UB. Please rephrase to match the reference (extra safety conditions that must be upheld) and cite ``RUST-REF-UNSAFE-ATTR``.

```suggestion
      The ``#[export_name]`` and ``#[link_section]`` attributes are unsafe because they impose extra safety conditions
      the compiler cannot verify :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`. Misuse can lead to incorrect linkage or
      platform-specific behavior, and the hazards are not visible without an ``unsafe`` wrapper.
```
