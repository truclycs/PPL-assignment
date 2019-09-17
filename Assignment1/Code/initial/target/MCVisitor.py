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


    # Visit a parse tree produced by MCParser#variable_declaration.
    def visitVariable_declaration(self, ctx:MCParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#many_variables.
    def visitMany_variables(self, ctx:MCParser.Many_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_declaration.
    def visitFunction_declaration(self, ctx:MCParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_list.
    def visitParameter_list(self, ctx:MCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression1.
    def visitExpression1(self, ctx:MCParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression2.
    def visitExpression2(self, ctx:MCParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression3.
    def visitExpression3(self, ctx:MCParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression4.
    def visitExpression4(self, ctx:MCParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression5.
    def visitExpression5(self, ctx:MCParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression6.
    def visitExpression6(self, ctx:MCParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression7.
    def visitExpression7(self, ctx:MCParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression8.
    def visitExpression8(self, ctx:MCParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_call.
    def visitFunction_call(self, ctx:MCParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_expression.
    def visitList_expression(self, ctx:MCParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
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


    # Visit a parse tree produced by MCParser#expression_statement.
    def visitExpression_statement(self, ctx:MCParser.Expression_statementContext):
        return self.visitChildren(ctx)



del MCParser