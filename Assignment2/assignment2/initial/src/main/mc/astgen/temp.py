from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx:MPParser.ProgramContext):
        _many_declarations = self.visit(ctx.many_declarations())
#        print(_many_declarations)
        return Program(_many_declarations)
    
    def visitMany_declarations(self, ctx:MPParser.Many_declarationsContext):
        if ctx.many_declarations():
            return self.visit(ctx.many_declarations()) + self.visit(ctx.declaration())
        else:
            return self.visit(ctx.declaration())
        
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        if ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        if ctx.procedure_declaration():
            return self.visit(ctx.procedure_declaration())
        
    def visitVariable_declaration(self, ctx:MPParser.Variable_declarationContext):
#        print(str(self.visit(ctx.list_declarations())[0]))
        return self.visit(ctx.list_declarations())
    
    def visitList_declarations(self, ctx:MPParser.List_declarationsContext):
        if ctx.list_declarations():
            return self.visit(ctx.list_declarations()) + self.visit(ctx.v_declaration())
        else:
            return self.visit(ctx.v_declaration())
    
    def visitV_declaration(self, ctx:MPParser.V_declarationContext):
        _list_identifiers = self.visit(ctx.list_identifiers())
        _returnType = self.visit(ctx.types())
        
        return [VarDecl(_id, _returnType) for _id in _list_identifiers]
        
    def visitList_identifiers(self, ctx:MPParser.List_identifiersContext):
        if ctx.list_identifiers():
            return self.visit(ctx.list_identifiers()) + [Id(ctx.IDENTIFIER().getText())]
        else:
            return [Id(ctx.IDENTIFIER().getText())]
    def visitFunction_declaration(self, ctx:MPParser.Function_declarationContext):
        _name = Id(ctx.IDENTIFIER().getText())
        _param = self.visit(ctx.list_parameters())
        if ctx.variable_declaration():
            _local = self.visit(ctx.variable_declaration())
        else:
            _local = []
        _body = self.visit(ctx.compound_statement())
        _returnType = self.visit(ctx.types())
        return [FuncDecl(_name, _param, _local, _body, _returnType)]

    def visitList_parameters(self, ctx:MPParser.List_parametersContext):
        if ctx.not_null_list_parameters():
            return self.visit(ctx.not_null_list_parameters())
        else:
            return []
        
    def visitNot_null_list_parameters(self, ctx:MPParser.Not_null_list_parametersContext):
        if ctx.not_null_list_parameters():
            return self.visit(ctx.not_null_list_parameters()) + self.visit(ctx.parameter_declaration())
        else:
            return self.visit(ctx.parameter_declaration())
        
    def visitParameter_declaration(self, ctx:MPParser.Parameter_declarationContext):
        _list_identifiers = self.visit(ctx.list_identifiers())
        _returnType = self.visit(ctx.types())
        return [VarDecl(_id, _returnType) for _id in _list_identifiers]
        
    def visitProcedure_declaration(self, ctx:MPParser.Procedure_declarationContext):
        _name = Id(ctx.IDENTIFIER().getText())
        _param = self.visit(ctx.list_parameters())
        if ctx.variable_declaration():
            _local = self.visit(ctx.variable_declaration())
        else:
            _local = []
        _body = self.visit(ctx.compound_statement())
        return [FuncDecl(_name, _param, _local, _body)]
        
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            _value = int(ctx.INTEGER_LITERAL().getText())
            return IntLiteral(_value)
        elif ctx.REAL_LITERAL():
            _value = float(ctx.REAL_LITERAL().getText())
            return FloatLiteral(_value)
        elif ctx.TRUE():
            _value = bool(True)
            return BooleanLiteral(_value)
        elif ctx.FALSE():
            _value = bool(False)
            return BooleanLiteral(_value)
        elif ctx.STRING_LITERAL():
            _value = str(ctx.STRING_LITERAL().getText())
            return StringLiteral(_value)
    
    def visitTypes(self, ctx:MPParser.TypesContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.compound_type())
            
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.INTEGER():
            return IntType()
        if ctx.REAL():
            return FloatType()
        if ctx.STRING():
            return StringType()
    
    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        return self.visit(ctx.array_type())
    
    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        _lower = int(ctx.INTEGER_LITERAL(0).getText())
        if ctx.getChild(2).getText() == "-":
            _lower = - _lower
        _upper = int(ctx.INTEGER_LITERAL(1).getText())
        if ctx.getChild(4).getText() == "-" or ctx.getChild(5).getText() == "-":
            _upper = - _upper
        _eleType = self.visit(ctx.primitive_type())
        return ArrayType(_lower, _upper, _eleType)
        
    def visitOperand(self, ctx:MPParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.func_call():
            return self.visit(ctx.func_call())
    
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        if ctx.AND():
            _op = "andthen"
            _left = self.visit(ctx.expression())
            _right = self.visit(ctx.expression_1())
            return BinaryOp(_op, _left, _right)
        if ctx.OR():
            _op = "orelse"
            _left = self.visit(ctx.expression())
            _right = self.visit(ctx.expression_1())
            return BinaryOp(_op, _left, _right)
        if ctx.expression_1():
            return self.visit(ctx.expression_1())
        
    def visitExpression_1(self, ctx:MPParser.Expression_1Context):
        if ctx.EQUAL():
            _op = str(ctx.EQUAL())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        if ctx.NOTEQUAL():
            _op = str(ctx.NOTEQUAL())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        if ctx.LESSTHAN():
            _op = str(ctx.LESSTHAN())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        if ctx.GREATERTHAN():
            _op = str(ctx.GREATERTHAN())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        if ctx.LESSEQUAL():
            _op = str(ctx.LESSEQUAL())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        if ctx.GREATEREQUAL():
            _op = str(ctx.GREATEREQUAL())
            _left = self.visit(ctx.expression_2(0))
            _right = self.visit(ctx.expression_2(1))
            return BinaryOp(_op, _left, _right)
        else:
            return self.visit(ctx.expression_2(0))
            
    def visitExpression_2(self, ctx:MPParser.Expression_2Context):
        if ctx.ADD():
            _op = str(ctx.ADD())
            _left = self.visit(ctx.expression_2())
            _right = self.visit(ctx.expression_3())
            return BinaryOp(_op, _left, _right)
        if ctx.SUB():
            _op = str(ctx.SUB())
            _left = self.visit(ctx.expression_2())
            _right = self.visit(ctx.expression_3())
            return BinaryOp(_op, _left, _right)
        if ctx.OR():
            _op = str(ctx.OR())
            _left = self.visit(ctx.expression_2())
            _right = self.visit(ctx.expression_3())
            return BinaryOp(_op, _left, _right)
        else:
            return self.visit(ctx.expression_3())
    
    def visitExpression_3(self, ctx:MPParser.Expression_3Context):
        if ctx.DIV_F():
            _op = str(ctx.DIV_F())
            _left = self.visit(ctx.expression_3())
            _right = self.visit(ctx.expression_4())
            return BinaryOp(_op, _left, _right)
        if ctx.MUL():
            _op = str(ctx.MUL())
            _left = self.visit(ctx.expression_3())
            _right = self.visit(ctx.expression_4())
            return BinaryOp(_op, _left, _right)
        if ctx.DIV():
            _op = str(ctx.DIV())
            _left = self.visit(ctx.expression_3())
            _right = self.visit(ctx.expression_4())
            return BinaryOp(_op, _left, _right)
        if ctx.MOD():
            _op = str(ctx.MOD())
            _left = self.visit(ctx.expression_3())
            _right = self.visit(ctx.expression_4())
            return BinaryOp(_op, _left, _right)
        if ctx.AND():
            _op = str(ctx.AND())
            _left = self.visit(ctx.expression_3())
            _right = self.visit(ctx.expression_4())
            return BinaryOp(_op, _left, _right)
        else:
            return self.visit(ctx.expression_4())
            
    def visitExpression_4(self, ctx:MPParser.Expression_4Context):
        if ctx.SUB():
            _op = str(ctx.SUB())
            _body = self.visit(ctx.expression_4())
            return UnaryOp(_op, _body)
        if ctx.NOT():
            _op = str(ctx.NOT())
            _body = self.visit(ctx.expression_4())
            return UnaryOp(_op, _body)
        else:
            return self.visit(ctx.expression_5())
        
    def visitExpression_5(self, ctx:MPParser.Expression_5Context):
        if ctx.expression_5():
            _arr = self.visit(ctx.expression_5())
            _idx = self.visit(ctx.expression())
            return ArrayCell(_arr, _idx)
        else:
            return self.visit(ctx.expression_6())

    def visitExpression_6(self, ctx:MPParser.Expression_6Context):
        if ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.operand())
            
    def visitArr_element(self, ctx:MPParser.Arr_elementContext):
        _arr = self.visit(ctx.expression_5())
        _idx = self.visit(ctx.expression())
        return ArrayCell(_arr, _idx)
        
    def visitFunc_call(self, ctx:MPParser.Func_callContext):
        _method = Id(ctx.IDENTIFIER().getText())
        _param = self.visit(ctx.list_expression())
        return CallExpr(_method, _param)
        
    def visitList_expression(self, ctx:MPParser.List_expressionContext):
        if ctx.not_null_list_expression():
            return self.visit(ctx.not_null_list_expression())
        else:
            return []
    
    def visitNot_null_list_expression(self, ctx:MPParser.Not_null_list_expressionContext):
        if ctx.not_null_list_expression():
            return self.visit(ctx.not_null_list_expression()) + [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())]
        
    def visitStatement(self, ctx:MPParser.StatementContext):
        if ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.while_statement():
            return self.visit(ctx.while_statement())
        if ctx.for_statement():
            return self.visit(ctx.for_statement())
        if ctx.break_statement():
            return self.visit(ctx.break_statement())
        if ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        if ctx.return_statement():
            return self.visit(ctx.return_statement())
        if ctx.compound_statement():
            return self.visit(ctx.compound_statement())
        if ctx.with_statement():
            return self.visit(ctx.with_statement())
        if ctx.call_statement():
            return self.visit(ctx.call_statement())
            
    def visitAssignment_statement(self, ctx:MPParser.Assignment_statementContext):
        if ctx.assignment_statement():
            if ctx.IDENTIFIER():
                _lhs = Id(ctx.IDENTIFIER().getText())
            else:
                _lhs = self.visit(ctx.arr_element())
            _list_assignment = self.visit(ctx.assignment_statement())
            _exp = _list_assignment[-1].lhs
            return _list_assignment + [Assign(_lhs, _exp)]
        else:
            if ctx.IDENTIFIER():
                _lhs = Id(ctx.IDENTIFIER().getText())
            else:
                _lhs = self.visit(ctx.arr_element())
            _exp = self.visit(ctx.expression())
            return [Assign(_lhs, _exp)]
            
    def visitIf_statement(self, ctx:MPParser.If_statementContext):
        _expr = self.visit(ctx.expression())
        if ctx.ELSE():
            _thenStmt = self.visit(ctx.statement(0))
            _elseStmt = self.visit(ctx.statement(1))
        else:
            _thenStmt = self.visit(ctx.statement(0))
            _elseStmt = []
        return [If(_expr, _thenStmt, _elseStmt)]
        
    def visitWhile_statement(self, ctx:MPParser.While_statementContext):
        _exp = self.visit(ctx.expression())
        _sl = self.visit(ctx.statement())
        return [While(_exp, _sl)]
        
    def visitFor_statement(self, ctx:MPParser.For_statementContext):
        _id = Id(ctx.IDENTIFIER().getText())
        _expr1 = self.visit(ctx.expression(0))
        _expr2 = self.visit(ctx.expression(1))
        _loop = self.visit(ctx.statement())
        if ctx.DOWNTO():
            _up = False
        else:
            _up = True
        return [For(_id, _expr1, _expr2, _up, _loop)]

    def visitBreak_statement(self, ctx:MPParser.Break_statementContext):
        return [Break()]
        
    def visitContinue_statement(self, ctx:MPParser.Continue_statementContext):
        return [Continue()]
        
    def visitReturn_statement(self, ctx:MPParser.Return_statementContext):
        if ctx.expression():
            _expr = self.visit(ctx.expression())
            return [Return(_expr)]
        return [Return()]
        
    def visitCompound_statement(self, ctx:MPParser.Compound_statementContext):
        return self.visit(ctx.list_statements())
    
    def visitList_statements(self, ctx:MPParser.List_statementsContext):
        if ctx.not_null_list_statements():
            return self.visit(ctx.not_null_list_statements())
        else:
            return []
            
    def visitNot_null_list_statements(self, ctx:MPParser.Not_null_list_statementsContext):
        if ctx.not_null_list_statements():
            return self.visit(ctx.not_null_list_statements()) + self.visit(ctx.statement())
        else:
            return self.visit(ctx.statement())
            
    def visitWith_statement(self, ctx:MPParser.With_statementContext):
        _decl = self.visit(ctx.list_declarations())
        _stmt = self.visit(ctx.statement())
        return [With(_decl, _stmt)]
        
    def visitCall_statement(self, ctx:MPParser.Call_statementContext):
        _func_call = self.visit(ctx.func_call())
        _method = _func_call.method
        _param = _func_call.param
        return [CallStmt(_method, _param)]
       
