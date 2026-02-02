#![allow(dead_code, unused_variables)]

#[cfg(any(target_arch = "x86_64", target_arch = "x86"))]
pub unsafe fn asm_cfg_example() {
    core::arch::asm!(
        "nop",
        #[cfg_attr(target_feature = "sse2", cfg(target_feature = "sse2"))]
        "nop",
        #[cfg(target_feature = "sse2")]
        "/* {value:e} */",
        #[cfg(target_feature = "sse2")]
        value = in(reg) 0_u32,
        #[cfg(target_feature = "sse2")]
        clobber_abi("C"),
        #[cfg(target_feature = "sse2")]
        options(nomem, nostack),
    );
}

#[cfg(not(any(target_arch = "x86_64", target_arch = "x86")))]
pub fn asm_cfg_example() {}

// Argument indices are comma-separated positions inside `asm!(...)`.
// Attributes belong to the following argument.
//
// Argument index map:
// - arg[1] (line 6): AssemblyTemplate -> "nop".
// - arg[2] (lines 7-8): AssemblyTemplate -> #[cfg_attr(...)] "nop".
// - arg[3] (lines 9-10): AssemblyTemplate -> #[cfg(...)] "/* {value:e} */".
// - arg[4] (lines 11-12): AssemblyAttributeRegisterArgument -> #[cfg(...)] value = in(reg) 0_u32.
// - arg[5] (lines 13-14): AssemblyAttributeAbiClobber -> #[cfg(...)] clobber_abi("C").
// - arg[6] (lines 15-16): AssemblyAttributeAssemblyOption -> #[cfg(...)] options(nomem, nostack).
//
// arg[1] expansion:
// - AsmArguments -> ( AssemblyCodeBlock , AssemblyAttributeRegisterArgument* , AssemblyAttributeAbiClobber* , AssemblyAttributeAssemblyOption* ) (src/inline-assembly.rst:1630)
//   - Evidence: line 5.
// - AssemblyCodeBlock -> AssemblyTemplate ( , AssemblyTemplate )* (src/inline-assembly.rst:965)
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> empty.
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 6: "nop".
//
// arg[2] expansion:
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment (src/entities-and-resolution.rst:241)
//         - SimplePathSegment -> Identifier (src/entities-and-resolution.rst:244)
//           - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 7): target_feature = "sse2" , cfg ( target_feature = "sse2" ).
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 7: `#[cfg_attr(target_feature = "sse2", cfg(target_feature = "sse2"))]`.
//     - Line 8: "nop".
//
// arg[3] expansion:
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 9): target_feature = "sse2".
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 9: `#[cfg(target_feature = "sse2")]`.
//     - Line 10: "/* {value:e} */".
//
// arg[4] expansion:
// - AssemblyAttributeRegisterArgument -> OuterAttribute* RegisterArgument (src/inline-assembly.rst:1636)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 11): target_feature = "sse2".
//   - RegisterArgument -> (Identifier =)? ( DirectionModifier ( RegisterName ) )? RegisterExpression (src/inline-assembly.rst:608)
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
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
//     - Line 11: `#[cfg(target_feature = "sse2")]`.
//     - Line 12: `value = in(reg) 0_u32`.
//
// arg[5] expansion:
// - AssemblyAttributeAbiClobber -> OuterAttribute* AbiClobber (src/inline-assembly.rst:1639)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 13): target_feature = "sse2".
//   - AbiClobber -> clobber_abi ( AbiKindList ) (src/inline-assembly.rst:1393)
//     - AbiKindList -> AbiKind ( , AbiKind )* (src/inline-assembly.rst:1396)
//       - AbiKind -> StringLiteral (src/ffi.rst:48)
//         - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//         - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 13: `#[cfg(target_feature = "sse2")]`.
//     - Line 14: `clobber_abi("C")`.
//
// arg[6] expansion:
// - AssemblyAttributeAssemblyOption -> OuterAttribute* AssemblyOption (src/inline-assembly.rst:1642)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 15): target_feature = "sse2".
//   - AssemblyOption -> options ( OptionList ) (src/inline-assembly.rst:1477)
//     - OptionList -> Option ( , Option )* (src/inline-assembly.rst:1480)
//       - Option -> nomem | nostack (src/inline-assembly.rst:1483)
//   - Evidence:
//     - Line 15: `#[cfg(target_feature = "sse2")]`.
//     - Line 16: `options(nomem, nostack)`.
//
// FLS rubric verification (Attributes):
// - fls_m0SBtonaNppV — "The :t:`[assembly instruction]s`, :t:`[register argument]s`, :t:`[ABI clobber]s`, and :t:`[assembly option]s` in :s:`AsmArguments` and :s:`GlobalAsmArguments` may be preceded by :t:`outer attribute` instances." (src/inline-assembly.rst:1656)
//   - Evidence:
//     - Lines 7-10: attributes on templates.
//     - Lines 11-12: attribute on register argument.
//     - Lines 13-14: attribute on clobber.
//     - Lines 15-16: attribute on options.
// - fls_nLBhw2w6uznH — "Only the :t:`attribute` :c:`cfg` and the :t:`attribute` :c:`cfg_attr` are accepted on inline assembly arguments. All other attributes are rejected." (src/inline-assembly.rst:1659)
//   - Evidence:
//     - Line 7: `#[cfg_attr(...)]`.
//     - Lines 9, 11, 13, 15: `#[cfg(...)]`.
// - fls_xzDPz2zfRfoI — "If a :t:`assembly instruction`, :t:`register argument`, :t:`ABI clobber`, or :t:`assembly option` is annotated with :c:`cfg` or :c:`cfg_attr` and the related :t:`configuration predicate` evaluates to ``false``, the annotated argument is not considered part of the related macro invocation, consistent with :t:`conditional compilation`." (src/inline-assembly.rst:1662)
//   - Evidence:
//     - Lines 7-16: arguments gated by `#[cfg(target_feature = "sse2")]` compile when false.
// - fls_cTEiqjf6haEg — "It is a static error for a :t:`register argument`, :t:`ABI clobber`, or :t:`assembly option` to appear before the first :t:`assembly instruction`, even if the argument is ignored by :t:`conditional compilation`." (src/inline-assembly.rst:1665)
//   - Evidence:
//     - Line 6: first argument is the template string "nop".
