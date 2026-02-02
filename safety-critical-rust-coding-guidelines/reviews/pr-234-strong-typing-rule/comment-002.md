### Location
File: src/coding-guidelines/types-and-traits/gui_xztNdXA2oFNC.rst.inc
Line: 132
Snippet: `println!("Speed: {} m/s", result.0);  // Access the inner value`

### Type
Non-blocking

### Comment
Add a bibliography entry for the new Rust Reference citation so the guideline remains self-contained and traceable.

```suggestion
          println!("Speed: {} m/s", result.0);  // Access the inner value
       }

   .. bibliography::
      :id: bib_xztNdXA2oFNC
      :status: draft

      .. list-table::
         :header-rows: 0
         :widths: auto
         :class: bibliography-table

         * - :bibentry:`gui_xztNdXA2oFNC:RUST-REF-TYPE-ALIASES`
           - The Rust Reference. "Type aliases." https://doc.rust-lang.org/reference/items/type-aliases.html
```
