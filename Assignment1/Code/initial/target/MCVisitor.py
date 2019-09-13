# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#many_declarations.
    def visitMany_declarations(self, ctx:MCParser.Many_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable_declaration.
    def visitVariable_declaration(self, ctx:MCParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_declarations.
    def visitList_declarations(self, ctx:MCParser.List_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#v_declaration.
    def visitV_declaration(self, ctx:MCParser.V_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_identifiers.
    def visitList_identifiers(self, ctx:MCParser.List_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_declaration.
    def visitFunction_declaration(self, ctx:MCParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_parameters.
    def visitList_parameters(self, ctx:MCParser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#not_null_list_parameters.
    def visitNot_null_list_parameters(self, ctx:MCParser.Not_null_list_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:MCParser.Procedure_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#compound_type.
    def visitCompound_type(self, ctx:MCParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_type.
    def visitArray_type(self, ctx:MCParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_1.
    def visitExpression_1(self, ctx:MCParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_2.
    def visitExpression_2(self, ctx:MCParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_3.
    def visitExpression_3(self, ctx:MCParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_4.
    def visitExpression_4(self, ctx:MCParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_5.
    def visitExpression_5(self, ctx:MCParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_6.
    def visitExpression_6(self, ctx:MCParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arr_element.
    def visitArr_element(self, ctx:MCParser.Arr_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_expression.
    def visitList_expression(self, ctx:MCParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#not_null_list_expression.
    def visitNot_null_list_expression(self, ctx:MCParser.Not_null_list_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MCParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_var_idx_ass.
    def visitList_var_idx_ass(self, ctx:MCParser.List_var_idx_assContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#while_statement.
    def visitWhile_statement(self, ctx:MCParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#compound_statement.
    def visitCompound_statement(self, ctx:MCParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_statements.
    def visitList_statements(self, ctx:MCParser.List_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#not_null_list_statements.
    def visitNot_null_list_statements(self, ctx:MCParser.Not_null_list_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#with_statement.
    def visitWith_statement(self, ctx:MCParser.With_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#call_statement.
    def visitCall_statement(self, ctx:MCParser.Call_statementContext):
        return self.visitChildren(ctx)



del MCParser