const DATA: u8 = 0;

const PTR_BYTES: [u8; 8] =
    unsafe { core::mem::transmute::<*const u8, [u8; 8]>(&DATA as *const u8) };

const PTR_RESTORED: *const u8 = unsafe { core::mem::transmute::<[u8; 8], *const u8>(PTR_BYTES) };

fn main() {
    let _ = PTR_RESTORED as usize;
}

// Argument index map (CallExpression in line 4):
// - arg[1] (line 4): ArgumentOperand -> `&DATA as *const u8`.
//
// Argument index map (CallExpression in line 8):
// - arg[1] (line 8): ArgumentOperand -> `PTR_BYTES`.
//
// UnsafeBlockExpression derivation (src/expressions.rst:867-868, 654-658):
// - UnsafeBlockExpression -> unsafe BlockExpression.
// - BlockExpression -> { InnerAttributeOrDoc* StatementList }.
//   - StatementList -> Statement* Expression? (src/expressions.rst:660-662).
//   - Evidence: lines 3-5 and 7-9.
//
// CallExpression derivation (src/expressions.rst:3353-3360):
// - CallExpression -> CallOperand ( ArgumentOperandList? ).
// - CallOperand -> Operand -> Expression (src/expressions.rst:56-60).
// - ArgumentOperandList -> ExpressionList (src/expressions.rst:55-56).
// - Evidence: lines 4 and 8.
//
// PathExpression derivation for `core::mem::transmute` (src/expressions.rst:612-614, entities-and-resolution.rst:260-267, 244-245, lexical-elements.rst:435-450):
// - PathExpression -> UnqualifiedPathExpression -> PathExpressionSegment (:: PathExpressionSegment )*.
// - PathExpressionSegment -> PathSegment -> SimplePathSegment -> Identifier.
// - Evidence: lines 4 and 8: `core::mem::transmute`.
//
// TypeCastExpression derivation (src/expressions.rst:2125-2126):
// - TypeCastExpression -> Operand as TypeSpecificationWithoutBounds.
// - Evidence: line 4: `&DATA as *const u8`.
//
// BorrowExpression derivation (src/expressions.rst:943-944):
// - BorrowExpression -> & mut? Operand.
// - Evidence: line 4: `&DATA`.
//
// PathExpression derivation for DATA (src/expressions.rst:612-614, entities-and-resolution.rst:260-267, 20-21, lexical-elements.rst:435-450):
// - PathExpression -> UnqualifiedPathExpression.
// - UnqualifiedPathExpression -> PathExpressionSegment ( :: PathExpressionSegment )*.
// - PathExpressionSegment -> PathSegment ( :: GenericArgumentList )?.
// - PathSegment -> SimplePathSegment.
// - SimplePathSegment -> Identifier -> NonKeywordIdentifier -> PureIdentifier.
// - Evidence: line 4: `DATA`.
//
// Constant expression rubric verification (src/expressions.rst:160-266):
// - fls_1ji7368ieg0b — Constant expressions include unsafe block expressions and call expressions where the callee is a constant function.
//   - Evidence: lines 3-5 and 7-9 are unsafe block expressions whose tail expressions are call expressions to `core::mem::transmute`.
//
// Expected result (negative example): rustc rejects the const evaluation because it depends on the raw bytes of a pointer value.
