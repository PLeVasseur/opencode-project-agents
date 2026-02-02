#![allow(dead_code)]

#[cfg(any(target_arch = "x86_64", target_arch = "x86"))]
pub unsafe fn asm_cfg_negative() {
    core::arch::asm!(
        #[cfg(false)]
        in(reg) 0_u32,
        "",
    );
}

#[cfg(not(any(target_arch = "x86_64", target_arch = "x86")))]
pub fn asm_cfg_negative() {}

// Argument indices are comma-separated positions inside `asm!(...)`.
// Attributes belong to the following argument.
//
// Argument index map:
// - arg[1] (lines 6-7): AssemblyAttributeRegisterArgument -> #[cfg(false)] in(reg) 0_u32.
// - arg[2] (line 8): AssemblyTemplate -> "".
//
// arg[1] expansion:
// - AssemblyAttributeRegisterArgument -> OuterAttribute* RegisterArgument (src/inline-assembly.rst:1636)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 6): false.
//   - RegisterArgument -> (Identifier =)? ( DirectionModifier ( RegisterName ) )? RegisterExpression (src/inline-assembly.rst:608)
//     - DirectionModifier -> in (src/inline-assembly.rst:611)
//     - RegisterName -> RegisterClassName -> reg (src/inline-assembly.rst:50, 418)
//     - RegisterExpression -> SimpleRegisterExpression -> Expression (src/inline-assembly.rst:618, 634)
//       - Expression -> ExpressionWithoutBlock -> LiteralExpression (src/expressions.rst:15, 32, 42)
//       - LiteralExpression -> Literal (src/expressions.rst:574)
//       - Literal -> NumericLiteral (src/lexical-elements.rst:546)
//         - NumericLiteral -> IntegerLiteral (src/lexical-elements.rst:824)
//           - IntegerLiteral -> IntegerContent IntegerSuffix? (src/lexical-elements.rst:842)
//             - IntegerContent -> DecimalLiteral (src/lexical-elements.rst:861)
//               - DecimalLiteral -> DecimalDigit DecimalDigitOrUnderscore* (src/lexical-elements.rst:861, 864, 868)
//             - IntegerSuffix -> UnsignedIntegerSuffix -> u32 (src/lexical-elements.rst:891, 903)
//   - Evidence:
//     - Line 6: `#[cfg(false)]`.
//     - Line 7: `in(reg) 0_u32`.
//
// arg[2] expansion:
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> empty.
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 8: "".
//
// Ordering violation:
// - AsmArguments -> ( AssemblyCodeBlock , AssemblyAttributeRegisterArgument* , AssemblyAttributeAbiClobber* , AssemblyAttributeAssemblyOption* ) (src/inline-assembly.rst:1630)
// - AssemblyCodeBlock -> AssemblyTemplate ( , AssemblyTemplate )* (src/inline-assembly.rst:965)
// - The first argument is a RegisterArgument, not an AssemblyInstruction.
//   - Evidence:
//     - Lines 6-7: register argument before any template.
//     - Line 8: first template appears after the operand.
//
// FLS rubric verification (Attributes):
// - fls_cTEiqjf6haEg — "It is a static error for a :t:`register argument`, :t:`ABI clobber`, or :t:`assembly option` to appear before the first :t:`assembly instruction`, even if the argument is ignored by :t:`conditional compilation`." (src/inline-assembly.rst:1665)
//   - Evidence:
//     - Lines 6-7: register argument before any template.
//     - Line 8: first template appears after the operand.
//     - rustc 1.93.0 error points at line 7: `expected expression, found keyword 'in'`.
