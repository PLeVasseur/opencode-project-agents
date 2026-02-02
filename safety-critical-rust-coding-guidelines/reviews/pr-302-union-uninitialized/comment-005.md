### Location
File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
Line: 106
Snippet: ``.. non_compliant_example::``

### Type
Blocking

### Comment
The prose and ``rust-example`` block are not indented under the ``non_compliant_example`` directive, so the directive has no content. This breaks the required structure. Indent the prose and code block to be children of the directive.

```suggestion
   .. non_compliant_example::
      :id: non_compl_ex_gE095eyVJizR
      :status: draft

      This noncompliant example assumes prior initialization is preserved after reassignment.

      .. rust-example::
         :miri: expect_ub

         union Data {
             uninit: (),
             init: (u8, u8),
         }

         fn reassign(d: &mut Data) {
             // Reassignment invalidates all prior initialization
             *d = Data { uninit: () };
         }

         fn foo() {
             let mut d = Data { init: (0, 0) };
             reassign(&mut d);
             
             // 'init' is uninitialized after reassignment
             println!("{}", unsafe { d.init.1 });  // noncompliant
         }

         fn main() {
             foo();
         }
```
