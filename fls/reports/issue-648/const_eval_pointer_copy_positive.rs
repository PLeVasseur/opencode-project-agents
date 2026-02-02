const DATA: u8 = 0;
const PTR: *const u8 = &DATA as *const u8;

fn main() {
    let _ = PTR as usize;
}

// Argument index map (TypeCastExpression in line 2):
// - arg[1] (line 2): Operand -> `&DATA`.
//
// BorrowExpression derivation (src/expressions.rst:943-944):
// - BorrowExpression -> & mut? Operand.
// - Evidence: line 2: `&DATA`.
//
// TypeCastExpression derivation (src/expressions.rst:2125-2126):
// - TypeCastExpression -> Operand as TypeSpecificationWithoutBounds.
// - Evidence: line 2: `&DATA as *const u8`.
//
// RawPointerTypeSpecification derivation for `*const u8` (src/types-and-traits.rst:1013-1014, 28-42, entities-and-resolution.rst:273-277, 244-245, lexical-elements.rst:435-450):
// - TypeSpecificationWithoutBounds -> RawPointerTypeSpecification.
// - RawPointerTypeSpecification -> * const TypeSpecificationWithoutBounds.
// - TypeSpecificationWithoutBounds -> TypePath -> TypePathSegment -> PathSegment -> SimplePathSegment -> Identifier -> NonKeywordIdentifier -> PureIdentifier.
// - Evidence: line 2: `*const u8`.
//
// PathExpression derivation for DATA (src/expressions.rst:612-614, entities-and-resolution.rst:260-267, 20-21, lexical-elements.rst:435-450):
// - PathExpression -> UnqualifiedPathExpression -> PathExpressionSegment ( :: PathExpressionSegment )*.
// - PathExpressionSegment -> PathSegment ( :: GenericArgumentList )?.
// - PathSegment -> SimplePathSegment -> Identifier -> NonKeywordIdentifier -> PureIdentifier.
// - Evidence: line 2: `DATA`.
//
// Constant expression rubric verification (src/expressions.rst:160-266):
// - fls_1ji7368ieg0b — Constant expressions include borrow expressions and type cast expressions.
//   - Evidence: line 2 uses a borrow expression and a type cast expression as a const initializer.
