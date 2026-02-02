### Location
File: src/coding-guidelines/attributes/gui_ZDLZzjeOwLSU.rst
Line: 22
Snippet: ``The following constructs require explicit ``unsafe`` visibility:``

### Type
Blocking

### Comment
These normative requirements need citations. Please cite the Rust Reference sections for unsafe extern blocks and unsafe attributes (and the Rust 2024 edition guide if the requirement is edition-specific).

```suggestion
   The following constructs require explicit ``unsafe`` visibility:

   * ``extern`` blocks must be declared as ``unsafe extern`` :cite:`gui_ZDLZzjeOwLSU:RUST-REF-EXTERN`
   * The ``#[no_mangle]`` attribute must be written as ``#[unsafe(no_mangle)]`` :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
   * The ``#[export_name]`` attribute must be written as ``#[unsafe(export_name)]`` :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
   * The ``#[link_section]`` attribute must be written as ``#[unsafe(link_section)]`` :cite:`gui_ZDLZzjeOwLSU:RUST-REF-UNSAFE-ATTR`
```
