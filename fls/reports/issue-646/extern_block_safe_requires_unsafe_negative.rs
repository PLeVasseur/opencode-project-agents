extern "C" {
    safe fn safe_api();
}

fn main() {}

// ExternalBlock derivation (src/ffi.rst:172-175):
// - ExternalBlock -> unsafe? extern AbiKind? { InnerAttributeOrDoc* ExternItem* }.
//   - unsafe? -> empty (line 1).
//   - extern (line 1).
//   - AbiKind -> StringLiteral (src/ffi.rst:48-50).
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153-1155).
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175-1176).
//     - Evidence: line 1: "C".
//   - ExternItem -> ExternalItemWithVisibility (src/ffi.rst:177-178).
//   - ExternalItemWithVisibility -> FunctionDeclaration (src/ffi.rst:180-183).
//
// FunctionDeclaration derivation (src/functions.rst:15-16):
// - FunctionDeclaration -> FunctionQualifierList fn Name GenericParameterList? ( FunctionParameterList? ) ReturnType? WhereClause? ( FunctionBody | ; ).
//   - FunctionQualifierList -> const? async? ItemSafety? AbiSpecification? (src/functions.rst:18-19).
//     - ItemSafety -> safe (line 2) (src/items.rst:39-41).
//   - Name -> Identifier (src/entities-and-resolution.rst:20-21).
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
//     - Evidence: line 2: `safe_api`.
//   - FunctionBody | ; -> ; (line 2).
//
// FLS rubric verification:
// - fls_tuP6iLdL6Kx0 — "An external function shall only specify ItemSafety if it is defined in an unsafe external block." (src/ffi.rst:238-239)
//   - Evidence: line 2 specifies ItemSafety without an unsafe external block on line 1.
// - fls_nUADhgcfvvGC — "A function shall only be subject to an ItemSafety with keyword safe if it is an external function in an unsafe external block." (src/functions.rst:206-207)
//   - Evidence: line 2 uses `safe fn` while line 1 lacks `unsafe` on the extern block.
//
// Expected result (negative example): rustc rejects `safe fn` in a non-unsafe extern block.
