fn safe_fn() {}
unsafe fn unsafe_fn() {}

fn main() {
    let cond = true;
    let f = if cond { safe_fn } else { unsafe_fn };
    let _fp: unsafe fn() = f;
    unsafe {
        _fp();
    }
}

// Index map (IfExpression branches in line 6):
// - branch[1] (line 6): `safe_fn`.
// - branch[2] (line 6): `unsafe_fn`.
//
// IfExpression derivation (src/expressions.rst:4457-4461, 654-658):
// - IfExpression -> if SubjectExpression BlockExpression ElseExpression?.
// - ElseExpression -> else (BlockExpression | IfExpression | IfLetExpression).
// - BlockExpression -> { InnerAttributeOrDoc* StatementList }.
// - Evidence: line 6 uses `if` with two block expressions.
//
// LUB coercion rubric verification:
// - fls_zi5311z1w7re — LUB coercion finds the common type of multiple if-expression branches (src/types-and-traits.rst:2103-2105).
//   - Evidence: line 6 uses an if-expression with differing branch types.
// - fls_rRegjSIudDM1 — When selecting a function pointer type for LUB, choose a non-unsafe pointer only if each source can coerce to a non-unsafe pointer; otherwise select an unsafe function pointer type (src/types-and-traits.rst:2144-2150).
//   - Evidence: line 6 combines a safe and an unsafe function item type; line 7 assigns to `unsafe fn()`.
