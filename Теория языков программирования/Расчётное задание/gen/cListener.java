// Generated from D:/Git/labs/Теория языков программирования/Расчётное задание\c.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link cParser}.
 */
public interface cListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link cParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(cParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(cParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#genericSelection}.
	 * @param ctx the parse tree
	 */
	void enterGenericSelection(cParser.GenericSelectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#genericSelection}.
	 * @param ctx the parse tree
	 */
	void exitGenericSelection(cParser.GenericSelectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#genericAssocList}.
	 * @param ctx the parse tree
	 */
	void enterGenericAssocList(cParser.GenericAssocListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#genericAssocList}.
	 * @param ctx the parse tree
	 */
	void exitGenericAssocList(cParser.GenericAssocListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#genericAssociation}.
	 * @param ctx the parse tree
	 */
	void enterGenericAssociation(cParser.GenericAssociationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#genericAssociation}.
	 * @param ctx the parse tree
	 */
	void exitGenericAssociation(cParser.GenericAssociationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void enterPostfixExpression(cParser.PostfixExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void exitPostfixExpression(cParser.PostfixExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#argumentExpressionList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentExpressionList(cParser.ArgumentExpressionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#argumentExpressionList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentExpressionList(cParser.ArgumentExpressionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(cParser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(cParser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryOperator(cParser.UnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryOperator(cParser.UnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#castExpression}.
	 * @param ctx the parse tree
	 */
	void enterCastExpression(cParser.CastExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#castExpression}.
	 * @param ctx the parse tree
	 */
	void exitCastExpression(cParser.CastExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(cParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(cParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(cParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(cParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpression(cParser.ShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpression(cParser.ShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(cParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(cParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(cParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(cParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#andExpression}.
	 * @param ctx the parse tree
	 */
	void enterAndExpression(cParser.AndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#andExpression}.
	 * @param ctx the parse tree
	 */
	void exitAndExpression(cParser.AndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#exclusiveOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterExclusiveOrExpression(cParser.ExclusiveOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#exclusiveOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitExclusiveOrExpression(cParser.ExclusiveOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#inclusiveOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterInclusiveOrExpression(cParser.InclusiveOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#inclusiveOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitInclusiveOrExpression(cParser.InclusiveOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpression(cParser.LogicalAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpression(cParser.LogicalAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpression(cParser.LogicalOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpression(cParser.LogicalOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpression(cParser.ConditionalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpression(cParser.ConditionalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(cParser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(cParser.AssignmentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(cParser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(cParser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(cParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(cParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#constantExpression}.
	 * @param ctx the parse tree
	 */
	void enterConstantExpression(cParser.ConstantExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#constantExpression}.
	 * @param ctx the parse tree
	 */
	void exitConstantExpression(cParser.ConstantExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(cParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(cParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declarationSpecifiers}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationSpecifiers(cParser.DeclarationSpecifiersContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declarationSpecifiers}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationSpecifiers(cParser.DeclarationSpecifiersContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declarationSpecifiers2}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationSpecifiers2(cParser.DeclarationSpecifiers2Context ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declarationSpecifiers2}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationSpecifiers2(cParser.DeclarationSpecifiers2Context ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declarationSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationSpecifier(cParser.DeclarationSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declarationSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationSpecifier(cParser.DeclarationSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#initDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void enterInitDeclaratorList(cParser.InitDeclaratorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#initDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void exitInitDeclaratorList(cParser.InitDeclaratorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#initDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterInitDeclarator(cParser.InitDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#initDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitInitDeclarator(cParser.InitDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#storageClassSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterStorageClassSpecifier(cParser.StorageClassSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#storageClassSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitStorageClassSpecifier(cParser.StorageClassSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#typeSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterTypeSpecifier(cParser.TypeSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#typeSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitTypeSpecifier(cParser.TypeSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structOrUnionSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterStructOrUnionSpecifier(cParser.StructOrUnionSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structOrUnionSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitStructOrUnionSpecifier(cParser.StructOrUnionSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structOrUnion}.
	 * @param ctx the parse tree
	 */
	void enterStructOrUnion(cParser.StructOrUnionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structOrUnion}.
	 * @param ctx the parse tree
	 */
	void exitStructOrUnion(cParser.StructOrUnionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structDeclarationList}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclarationList(cParser.StructDeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structDeclarationList}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclarationList(cParser.StructDeclarationListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclaration(cParser.StructDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclaration(cParser.StructDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#specifierQualifierList}.
	 * @param ctx the parse tree
	 */
	void enterSpecifierQualifierList(cParser.SpecifierQualifierListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#specifierQualifierList}.
	 * @param ctx the parse tree
	 */
	void exitSpecifierQualifierList(cParser.SpecifierQualifierListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclaratorList(cParser.StructDeclaratorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclaratorList(cParser.StructDeclaratorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#structDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclarator(cParser.StructDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#structDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclarator(cParser.StructDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#enumSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterEnumSpecifier(cParser.EnumSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#enumSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitEnumSpecifier(cParser.EnumSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#enumeratorList}.
	 * @param ctx the parse tree
	 */
	void enterEnumeratorList(cParser.EnumeratorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#enumeratorList}.
	 * @param ctx the parse tree
	 */
	void exitEnumeratorList(cParser.EnumeratorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#enumerator}.
	 * @param ctx the parse tree
	 */
	void enterEnumerator(cParser.EnumeratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#enumerator}.
	 * @param ctx the parse tree
	 */
	void exitEnumerator(cParser.EnumeratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#enumerationConstant}.
	 * @param ctx the parse tree
	 */
	void enterEnumerationConstant(cParser.EnumerationConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#enumerationConstant}.
	 * @param ctx the parse tree
	 */
	void exitEnumerationConstant(cParser.EnumerationConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#atomicTypeSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterAtomicTypeSpecifier(cParser.AtomicTypeSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#atomicTypeSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitAtomicTypeSpecifier(cParser.AtomicTypeSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#typeQualifier}.
	 * @param ctx the parse tree
	 */
	void enterTypeQualifier(cParser.TypeQualifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#typeQualifier}.
	 * @param ctx the parse tree
	 */
	void exitTypeQualifier(cParser.TypeQualifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#functionSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterFunctionSpecifier(cParser.FunctionSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#functionSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitFunctionSpecifier(cParser.FunctionSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#alignmentSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterAlignmentSpecifier(cParser.AlignmentSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#alignmentSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitAlignmentSpecifier(cParser.AlignmentSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declarator}.
	 * @param ctx the parse tree
	 */
	void enterDeclarator(cParser.DeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declarator}.
	 * @param ctx the parse tree
	 */
	void exitDeclarator(cParser.DeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#directDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterDirectDeclarator(cParser.DirectDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#directDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitDirectDeclarator(cParser.DirectDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#gccDeclaratorExtension}.
	 * @param ctx the parse tree
	 */
	void enterGccDeclaratorExtension(cParser.GccDeclaratorExtensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#gccDeclaratorExtension}.
	 * @param ctx the parse tree
	 */
	void exitGccDeclaratorExtension(cParser.GccDeclaratorExtensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#gccAttributeSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterGccAttributeSpecifier(cParser.GccAttributeSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#gccAttributeSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitGccAttributeSpecifier(cParser.GccAttributeSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#gccAttributeList}.
	 * @param ctx the parse tree
	 */
	void enterGccAttributeList(cParser.GccAttributeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#gccAttributeList}.
	 * @param ctx the parse tree
	 */
	void exitGccAttributeList(cParser.GccAttributeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#gccAttribute}.
	 * @param ctx the parse tree
	 */
	void enterGccAttribute(cParser.GccAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#gccAttribute}.
	 * @param ctx the parse tree
	 */
	void exitGccAttribute(cParser.GccAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#nestedParenthesesBlock}.
	 * @param ctx the parse tree
	 */
	void enterNestedParenthesesBlock(cParser.NestedParenthesesBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#nestedParenthesesBlock}.
	 * @param ctx the parse tree
	 */
	void exitNestedParenthesesBlock(cParser.NestedParenthesesBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#pointer}.
	 * @param ctx the parse tree
	 */
	void enterPointer(cParser.PointerContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#pointer}.
	 * @param ctx the parse tree
	 */
	void exitPointer(cParser.PointerContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#typeQualifierList}.
	 * @param ctx the parse tree
	 */
	void enterTypeQualifierList(cParser.TypeQualifierListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#typeQualifierList}.
	 * @param ctx the parse tree
	 */
	void exitTypeQualifierList(cParser.TypeQualifierListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#parameterTypeList}.
	 * @param ctx the parse tree
	 */
	void enterParameterTypeList(cParser.ParameterTypeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#parameterTypeList}.
	 * @param ctx the parse tree
	 */
	void exitParameterTypeList(cParser.ParameterTypeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(cParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(cParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#parameterDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterParameterDeclaration(cParser.ParameterDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#parameterDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitParameterDeclaration(cParser.ParameterDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#identifierList}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierList(cParser.IdentifierListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#identifierList}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierList(cParser.IdentifierListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#typeName}.
	 * @param ctx the parse tree
	 */
	void enterTypeName(cParser.TypeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#typeName}.
	 * @param ctx the parse tree
	 */
	void exitTypeName(cParser.TypeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#abstractDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterAbstractDeclarator(cParser.AbstractDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#abstractDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitAbstractDeclarator(cParser.AbstractDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#directAbstractDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterDirectAbstractDeclarator(cParser.DirectAbstractDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#directAbstractDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitDirectAbstractDeclarator(cParser.DirectAbstractDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#typedefName}.
	 * @param ctx the parse tree
	 */
	void enterTypedefName(cParser.TypedefNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#typedefName}.
	 * @param ctx the parse tree
	 */
	void exitTypedefName(cParser.TypedefNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#initializer}.
	 * @param ctx the parse tree
	 */
	void enterInitializer(cParser.InitializerContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#initializer}.
	 * @param ctx the parse tree
	 */
	void exitInitializer(cParser.InitializerContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#initializerList}.
	 * @param ctx the parse tree
	 */
	void enterInitializerList(cParser.InitializerListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#initializerList}.
	 * @param ctx the parse tree
	 */
	void exitInitializerList(cParser.InitializerListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#designation}.
	 * @param ctx the parse tree
	 */
	void enterDesignation(cParser.DesignationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#designation}.
	 * @param ctx the parse tree
	 */
	void exitDesignation(cParser.DesignationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#designatorList}.
	 * @param ctx the parse tree
	 */
	void enterDesignatorList(cParser.DesignatorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#designatorList}.
	 * @param ctx the parse tree
	 */
	void exitDesignatorList(cParser.DesignatorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#designator}.
	 * @param ctx the parse tree
	 */
	void enterDesignator(cParser.DesignatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#designator}.
	 * @param ctx the parse tree
	 */
	void exitDesignator(cParser.DesignatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#staticAssertDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterStaticAssertDeclaration(cParser.StaticAssertDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#staticAssertDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitStaticAssertDeclaration(cParser.StaticAssertDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(cParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(cParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#labeledStatement}.
	 * @param ctx the parse tree
	 */
	void enterLabeledStatement(cParser.LabeledStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#labeledStatement}.
	 * @param ctx the parse tree
	 */
	void exitLabeledStatement(cParser.LabeledStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(cParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(cParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#blockItemList}.
	 * @param ctx the parse tree
	 */
	void enterBlockItemList(cParser.BlockItemListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#blockItemList}.
	 * @param ctx the parse tree
	 */
	void exitBlockItemList(cParser.BlockItemListContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#blockItem}.
	 * @param ctx the parse tree
	 */
	void enterBlockItem(cParser.BlockItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#blockItem}.
	 * @param ctx the parse tree
	 */
	void exitBlockItem(cParser.BlockItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(cParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(cParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#selectionStatement}.
	 * @param ctx the parse tree
	 */
	void enterSelectionStatement(cParser.SelectionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#selectionStatement}.
	 * @param ctx the parse tree
	 */
	void exitSelectionStatement(cParser.SelectionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterIterationStatement(cParser.IterationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitIterationStatement(cParser.IterationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#jumpStatement}.
	 * @param ctx the parse tree
	 */
	void enterJumpStatement(cParser.JumpStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#jumpStatement}.
	 * @param ctx the parse tree
	 */
	void exitJumpStatement(cParser.JumpStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(cParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(cParser.CompilationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#translationUnit}.
	 * @param ctx the parse tree
	 */
	void enterTranslationUnit(cParser.TranslationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#translationUnit}.
	 * @param ctx the parse tree
	 */
	void exitTranslationUnit(cParser.TranslationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#externalDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterExternalDeclaration(cParser.ExternalDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#externalDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitExternalDeclaration(cParser.ExternalDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDefinition(cParser.FunctionDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDefinition(cParser.FunctionDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link cParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationList(cParser.DeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link cParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationList(cParser.DeclarationListContext ctx);
}