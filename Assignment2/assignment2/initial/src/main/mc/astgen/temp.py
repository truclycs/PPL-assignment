# program: many_declarations EOF;

# many_declarations:
#     many_declarations declaration
#     | declaration
#     ;

# declaration:
#     variable_declaration
#     | function_declaration
#     | procedure_declaration
#     ;

# // 2.1
# variable_declaration:
#     VAR list_declarations
#     ;

# list_declarations:
#     list_declarations v_declaration
#     | v_declaration
#     ;

# v_declaration:
#     list_identifiers COLON types SEMI
#     ;

# list_identifiers:
#     list_identifiers COMMA IDENTIFIER
#     | IDENTIFIER
#     ;

# // 2.2
# function_declaration:
#     FUNCTION IDENTIFIER LB list_parameters RB COLON types SEMI variable_declaration? compound_statement
#     ;

# list_parameters:
#     not_null_list_parameters
#     |
#     ;

# not_null_list_parameters:
#     not_null_list_parameters SEMI parameter_declaration
#     | parameter_declaration
#     ;
    
# parameter_declaration:
#     list_identifiers COLON types
#     ;

# // 2.3

# procedure_declaration:
#     PROCEDURE IDENTIFIER LB list_parameters RB SEMI variable_declaration? compound_statement
# //    | main_procedure

# types:
#     primitive_type
#     | compound_type
#     ;

# primitive_type:
#     BOOLEAN
#     | INTEGER
#     | REAL
#     | STRING
#     ;

# compound_type:
#     array_type
#     ;

# array_type:
#     ARRAY LSB SUB? INTEGER_LITERAL DDOT SUB? INTEGER_LITERAL RSB OF primitive_type
#     ;

# // 5. Expressions

# operand:
#     literal
#     | IDENTIFIER
# //    | arr_element
#     | func_call
#     ;

# expression:
#     expression AND THEN expression_1
#     | expression OR ELSE expression_1
# //    expression_1 AND THEN expression
# //    | expression_1 OR ELSE expression
#     | expression_1
# //    | operand
#     ;

# expression_1:
#     expression_2 EQUAL expression_2
#     | expression_2 NOTEQUAL expression_2
#     | expression_2 LESSTHAN expression_2
#     | expression_2 GREATERTHAN expression_2
#     | expression_2 LESSEQUAL expression_2
#     | expression_2 GREATEREQUAL expression_2
#     | expression_2
#     ;

# expression_2:
#     expression_2 ADD expression_3
#     | expression_2 SUB expression_3
#     | expression_2 OR expression_3
#     | expression_3
#     ;

# expression_3:
#     expression_3 DIV_F expression_4
#     | expression_3 MUL expression_4
#     | expression_3 DIV expression_4
#     | expression_3 MOD expression_4
#     | expression_3 AND expression_4
#     | expression_4
#     ;

# expression_4:
#     SUB expression_4
#     | NOT expression_4
#     | expression_5
#     ;

# expression_5:
#     expression_5 LSB expression RSB
#     | expression_6
#     ;
    
# expression_6:
#     LB expression RB
#     | operand
#     ;


# // 5.3: Index Expression
# arr_element:
#     expression_5 LSB expression RSB
#     ;

# // 5.4: Invocation Expression
# func_call:
#     IDENTIFIER LB list_expression RB
#     ;

# list_expression:
#     not_null_list_expression
#     |
#     ;
    
# not_null_list_expression:
#     not_null_list_expression COMMA expression
#     | expression
#     ;

# // 6. Statements and Control Flow

# statement:
#     assignment_statement
#     | if_statement
#     | while_statement
#     | for_statement
#     | break_statement
#     | continue_statement
#     | return_statement
#     | compound_statement
#     | with_statement
#     | call_statement
#     ;

# // 6.1 Assignment Statement
# assignment_statement:
#     (IDENTIFIER | arr_element) ASSIGN assignment_statement
#     | (IDENTIFIER | arr_element) ASSIGN expression SEMI
#     ;

# list_var_idx_ass:
#     list_var_idx_ass ASSIGN IDENTIFIER
#     | list_var_idx_ass ASSIGN arr_element
#     | IDENTIFIER
#     | arr_element
#     ;

# // 6.2 If Statement

# if_statement:
#     IF expression THEN statement (ELSE statement)?
#     ;

# // 6.3 While Statement
# 
# 
# 
# tement:
#     WHILE expression DO statement
#     ;

# // 6.4 For Statement
# for_statement:
#     FOR IDENTIFIER ASSIGN expression (TO | DOWNTO) expression DO statement
#     ;


# // 6.7 Return Statement
# return_statement:
#     RETURN expression? SEMI
#     ;

# // 6.8 Compound Statement
# compound_statement:
#     BEGIN list_statements END
#     ;

# list_statements:
#     not_null_list_statements
#     |
#     ;

# not_null_list_statements:
#     not_null_list_statements statement
#     | statement
#     ;

# // 6.9 With Statement
# with_statement:
#     WITH list_declarations DO statement
#     ;

# // 6.10 Call Statement
# call_statement:
#     func_call SEMI
#     ;

# // 9. The main function
# /*main_procedure:
#     PROCEDURE MAIN LB RB SEMI variable_declaration? compound_statement
#     ;

class ASTGeneration(MPVisitor):
    
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

    
    def visitTypes(self, ctx:MPParser.TypesContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.compound_type())
    
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
       
