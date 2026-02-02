extern "system" {
    fn variadic(arg: (), ...);
}

fn main() {}

// Argument index map (FunctionParameterList in line 2):
// - arg[1] (line 2): FunctionParameterPattern -> `arg: ()`.
// - arg[2] (line 2): FunctionParameterVariadicPart -> `...`.
//
// ExternalBlock derivation (src/ffi.rst:172-175):
// - ExternalBlock -> unsafe? extern AbiKind? { InnerAttributeOrDoc* ExternItem* }.
//   - unsafe? -> empty (line 1).
//   - extern (line 1).
//   - AbiKind -> StringLiteral (src/ffi.rst:48-50).
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153-1155).
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175-1176).
//     - Evidence: line 1: "system".
//   - ExternItem -> ExternalItemWithVisibility (src/ffi.rst:177-178).
//   - ExternalItemWithVisibility -> FunctionDeclaration (src/ffi.rst:180-183).
//
// FunctionDeclaration derivation (src/functions.rst:15-16):
// - FunctionDeclaration -> FunctionQualifierList fn Name GenericParameterList? ( FunctionParameterList? ) ReturnType? WhereClause? ( FunctionBody | ; ).
//   - FunctionQualifierList -> const? async? ItemSafety? AbiSpecification? (src/functions.rst:18-19).
//     - all empty (line 2).
//   - Name -> Identifier (src/entities-and-resolution.rst:20-21).
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
//     - Evidence: line 2: `variadic`.
//   - FunctionParameterList -> ( FunctionParameter (, FunctionParameter)* ,? ) (src/functions.rst:21-23).
//   - FunctionBody | ; -> ; (line 2).
//
// FunctionParameterList expansion (src/functions.rst:21-26):
// - FunctionParameter -> OuterAttributeOrDoc* (FunctionParameterPattern | FunctionParameterVariadicPart | TypeSpecification) (src/functions.rst:25-26).
//
// arg[1] (line 2): FunctionParameterPattern:
// - FunctionParameterPattern -> PatternWithoutAlternation ( TypeAscription | ( : FunctionParameterVariadicPart ) ) (src/functions.rst:28-29).
// - PatternWithoutAlternation -> PatternWithoutRange (src/patterns.rst:21-23).
// - PatternWithoutRange -> IdentifierPattern (src/patterns.rst:25-36).
// - IdentifierPattern -> ref? mut? Binding BoundPattern? (src/patterns.rst:145-146).
// - Binding -> Name (src/patterns.rst:1219-1220).
// - Name -> Identifier (src/entities-and-resolution.rst:20-21).
// - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
// - TypeAscription -> : TypeSpecification (src/types-and-traits.rst:44-45).
// - TypeSpecification -> TypeSpecificationWithoutBounds (src/types-and-traits.rst:20-23).
// - TypeSpecificationWithoutBounds -> TupleTypeSpecification (src/types-and-traits.rst:28-42).
// - TupleTypeSpecification -> ( TupleFieldList? ) (src/types-and-traits.rst:76-77).
//   - TupleFieldList? -> empty (line 2).
// - Evidence: line 2: `arg: ()`.
//
// arg[2] (line 2): FunctionParameterVariadicPart:
// - FunctionParameterVariadicPart -> ... (src/functions.rst:31-32).
// - Evidence: line 2: `...`.
//
// FLS rubric verification:
// - fls_w00qi1gx204e — "An external function inherits the ABI of its enclosing external block." (src/ffi.rst:241-243)
//   - Evidence: line 1: extern "system" block; line 2: function declaration has no ABI qualifier.
// - fls_o4uSLPo00KUg — "A variadic function is an external function that specifies FunctionParameterVariadicPart as the last function parameter." (src/functions.rst:106-108)
//   - Evidence: line 2: function is in extern block and ends with `...`.
// - fls_juob30rst11r — "Only the last parameter FunctionParameter of an external function may specify a FunctionParameterVariadicPart." (src/ffi.rst:256-258)
//
// - fls_ZbvI45Ojpte4 + fls_yjRmR5F1cL6i — "The ABI of a function ... whose AbiKind is \"system\" is determined as follows: ... Otherwise, the ABI is extern \"C\"." (src/ffi.rst:86-96)
//   - Evidence: line 1 uses AbiKind "system"; for non-Windows targets, the final step applies.
//   - Evidence: line 2: `...` is the final parameter.
// - fls_icdzs1mjh0n4 + fls_6urL6fZ5cpaA — "A variadic function shall specify one of the following ABIs: ... extern \"system\"." (src/functions.rst:110-128)
//   - Evidence: line 1: extern "system".
