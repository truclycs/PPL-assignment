#    **************************************
#    * Student name: Nguyen Thi Truc Ly   *
#    * Student ID: 1710187                *
#    ************************************** 
import sys
sys.setrecursionlimit(10**6)

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
# program: decls EOF;
    def visitProgram(self, ctx:MCParser.ProgramContext):       
        return Program(self.visit(ctx.decls())) 

# decls: (var_decl | func_decl)+;
    def visitDecls(self, ctx:MCParser.DeclsContext):
        decl = []        
        for x in ctx.getChildren():
            decl += self.visit(x)
        return decl

# var_decl: primitive_type var (COMMA var)* SEMI;
# var: ID (LSB INTLIT RSB)?;
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        res = []
        for x in ctx.var():
            if x.INTLIT():
                res.append(VarDecl(x.ID().getText(), ArrayType(int(x.INTLIT().getText()), self.visit(ctx.primitive_type()))))
            else:
                res.append(VarDecl(x.ID().getText(), self.visit(ctx.primitive_type())))
        return res

# func_decl: types ID LB para_list? RB block_stmt;
# para_list: para_decl (COMMA para_decl)*;
    def visitFunc_decl(self, ctx:MCParser.Func_declContext): 
        name = ctx.ID().getText()
        para = ([self.visit(x) for x in ctx.para_list().para_decl()] if ctx.para_list() else [])
        return_type = self.visit(ctx.types())
        body = self.visit(ctx.block_stmt())
        return [FuncDecl(Id(name), para, return_type, body)]

# para_decl: primitive_type ID (LSB RSB)?;
    def visitPara_decl(self, ctx:MCParser.Para_declContext): 
        if ctx.LSB():
            return VarDecl(ctx.ID().getText(), ArrayPointerType(self.visit(ctx.primitive_type())))
        else:
            return VarDecl(ctx.ID().getText(), self.visit(ctx.primitive_type()))

# types   : primitive_type | array_pointer_type | VOID; 
    def visitTypes(self, ctx:MCParser.TypesContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.array_pointer_type())

# primitive_type: BOOL | INT | FLOAT | STRING;
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()        

# array_pointer_type: primitive_type ID? LSB RSB;
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        if ctx.LSB():
            return ArrayPointerType(self.visit(ctx.primitive_type()))

# exp : exp1 ASSIGN exp | exp1;
    def visitExp(self, ctx:MCParser.ExpContext): 
        if ctx.ASSIGN():
            return BinaryOp('=', self.visit(ctx.exp1()), self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp1())

# exp1: exp1 OR exp2 | exp2;
    def visitExp1(self, ctx:MCParser.Exp1Context): 
        if ctx.OR():
            return BinaryOp("||",  self.visit(ctx.exp1()), self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())

# exp2: exp2 AND exp3 | exp3;
    def visitExp2(self, ctx:MCParser.Exp2Context): 
        if ctx.AND():
            return BinaryOp("&&", self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

# exp3: exp4 (EQUAL | NOT_EQUAL) exp4 | exp4;
    def visitExp3(self, ctx:MCParser.Exp3Context): 
        if ctx.EQUAL():
            return BinaryOp("==", self.visit(ctx.exp4(0)), self.visit(ctx.exp4(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp("!=", self.visit(ctx.exp4(0)), self.visit(ctx.exp4(1)))
        else:
            return self.visit(ctx.exp4(0))

# exp4: exp5 (LESS| GREATER | LESS_EQUAL | GREATER_EQUAL) exp5 | exp5;
    def visitExp4(self, ctx:MCParser.Exp4Context): 
        if ctx.LESS():
            return BinaryOp("<", self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
        elif ctx.GREATER():
            return BinaryOp(">", self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
        elif ctx.LESS_EQUAL():
            return BinaryOp("<=", self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
        elif ctx.GREATER_EQUAL():
            return BinaryOp(">=", self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
        else:
            return self.visit(ctx.exp5(0))

# exp5: exp5 (ADD | SUB) exp6 | exp6;
    def visitExp5(self, ctx:MCParser.Exp5Context): 
        if ctx.ADD():
            return BinaryOp("+", self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        elif ctx.SUB():
            return BinaryOp("-", self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())

# exp6: exp6 (DIV | MUL | MOD) exp7 | exp7;
    def visitExp6(self, ctx:MCParser.Exp6Context): 
        if ctx.DIV():
            return BinaryOp("/", self.visit(ctx.exp6()), self.visit(ctx.exp7()))
        if ctx.MUL():
            return BinaryOp("*", self.visit(ctx.exp6()), self.visit(ctx.exp7()))
        if ctx.MOD():
            return BinaryOp("%", self.visit(ctx.exp6()), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp7())

# exp7: (SUB | NOT) exp7 |exp8;
    def visitExp7(self, ctx:MCParser.Exp7Context): 
        if ctx.SUB():
            return UnaryOp("-", self.visit(ctx.exp7()))
        elif ctx.NOT():
            return UnaryOp("!", self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())

# exp8: operand LSB exp RSB | operand;
    def visitExp8(self, ctx:MCParser.Exp8Context): 
        if ctx.exp():
            arr = self.visit(ctx.operand())
            idx = self.visit(ctx.exp())
            return ArrayCell(arr, idx)
        else:
            return self.visit(ctx.operand())

# operand : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB exp RB | func_call | ID;
    def visitOperand(self, ctx:MCParser.OperandContext): 
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(bool(True) if ctx.BOOLLIT().getText() == "true" else bool(False))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        else:
            return Id(ctx.ID().getText())
 
# func_call: ID LB list_exp? RB;
# list_exp : exp (COMMA exp)*;
    def visitFunc_call(self, ctx:MCParser.Func_callContext): 
        method = Id(ctx.ID().getText())
        param = [self.visit(x) for x in ctx.list_exp().exp()] if ctx.list_exp() else []
        return CallExpr(method, param)

# stmt: if_stmt | for_stmt | while_stmt | break_stmt | continue_stmt | return_stmt | exp_stmt | block_stmt;
    def visitStmt(self, ctx:MCParser.StmtContext):
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.exp_stmt():
            return self.visit(ctx.exp_stmt())
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())

# if_stmt: IF LB exp RB stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext): 
        expr = self.visit(ctx.exp())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = None
        if ctx.stmt(1):
            else_stmt = self.visit(ctx.stmt(1))
        return If(expr, then_stmt, else_stmt)

# while_stmt: DO stmt+ WHILE exp SEMI;
    def visitWhile_stmt(self, ctx:MCParser.While_stmtContext): 
        sl  = [self.visit(x) for x in ctx.stmt()]
        exp = self.visit(ctx.exp())
        return Dowhile(sl, exp)

# for_stmt: FOR LB exp SEMI exp SEMI exp RB stmt;
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext): 
        e1, e2, e3 = [self.visit(x) for x in ctx.exp()]
        loop = self.visit(ctx.stmt())
        return For(e1, e2, e3, loop)

# break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext): 
        return Break()

# continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext): 
        return Continue()

# return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()

# exp_stmt: exp SEMI;
    def visitExp_stmt(self, ctx:MCParser.Exp_stmtContext): 
        return self.visit(ctx.exp())

# block_stmt: LP body_block RP;
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext): 
        if ctx.body_block():
            return Block(self.visit(ctx.body_block()))

# body_block: (var_decl | stmt)*;
    def visitBody_block(self, ctx:MCParser.Body_blockContext): 
        member = []
        if ctx.getChildren():      
            for x in ctx.getChildren():
                if x.getChildCount() == 1:
                    member.append(self.visit(x))
                else:
                    member += self.visit(x)
        return member