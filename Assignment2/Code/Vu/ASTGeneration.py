from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    # program : decls EOF;
    def visitProgram(self, ctx:MCParser.ProgramContext):
       return Program(self.visit(ctx.decls()))
    #decl: (func|var_stmt)+
    def visitDecls(self,ctx:MCParser.DeclsContext):
        decl= []
        for x in ctx.getChildren():
            decl.append(self.visit(x))
        return decl
    # var_stmt: var_dec | stmt
    def visitVar_stmt(self,ctx:MCParser.Var_stmtContext):
        if ctx.var_dec(): 
            return self.visit(ctx.var_dec())
        else:
            return self.visit(ctx.stmt())
    # func: func: (VOIDTYPE|mctype) (ID|'main') paradec blockstate;
    def visitFunc(self,ctx:MCParser.FuncContext):
    #return Program([FuncDecl(Id("main"),[],self.visit(ctx.mctype()),Block([self.visit(ctx.body())] if ctx.body() else []))])
        name=""
        if ctx.ID():
            name=ctx.ID().getText()
        else: name="main"
        if ctx.VOIDTYPE():
            return FuncDecl(Id(name),self.visit(ctx.paradec()),VoidType,self.visit(ctx.blockstate()))
        else:
            return FuncDecl(Id(name),self.visit(ctx.paradec()),self.visit(ctx.mctype()),self.visit(ctx.blockstate()))
    # var_dec: mctype listID SM;
    def visitVar_dec(self,ctx:MCParser.Var_decContext):
        return [VarDecl(i,self.visit(ctx.mctype())) for i in self.visit(ctx.listID())]
    # listID: varid (CM varid)* ;
    def visitListID(self,ctx:MCParser.ListIDContext):
        return list(map(lambda x: self.visit(x),ctx.varid()))
    #varid: ID LV INTLIT RV | ID
    def visitVarid(self,ctx:MCParser.VaridContext):
        if ctx.INTLIT():
            return ArrayCell(Id(ctx.ID().getText()),IntLiteral(int(ctx.INTLIT().getText())))
        else:
            return Id(ctx.ID().getText())
    # stmt: (BREAK | CONTINUE | RETURN expr? | call | expr) SM | ifstate | whilestate | forstate | blockstate ;
    def visitStmt(self,ctx:MCParser.StmtContext):
        if ctx.BREAK():
            return Break
        elif ctx.CONTINUE():
            return Continue
        elif ctx.RETURN():
            return Return
        elif ctx.call():
            return self.visit(ctx.call())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ifstate():
            return self.visit(ctx.ifstate())
        elif ctx.whilestate():
            return self.visit(ctx.whilestate())
        elif ctx.forstate():
            return self.visit(ctx.forstate())
        else:
            return self.visit(ctx.blockstate())
    # call: ID LB explist? RB
    def visitCall(self,ctx:MCParser.CallContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.explist()) if ctx.explist() else [])
    # explist: explist: expr (CM expr)*;
    def visitExplist(self,ctx:MCParser.ExplistContext):
        return list(map(lambda x: self.visit(x),ctx.expr()))
    # expr: expr ASSIGN expr1 | expr1
    def visitExpr(self,ctx:MCParser.ExprContext):
        if ctx.ASSIGN():
            return BinaryOp('=',self.visit(ctx.expr()),self.visit(ctx.expr1()))
        else:
            return self.visit(ctx.expr1())
    # expr1: expr2 LOGICOR expr1 | expr2
    def visitExpr1(self,ctx:MCParser.Expr1Context):
        if ctx.LOGICOR():
            return BinaryOp("||",self.visit(ctx.expr2()),self.visit(ctx.expr1()))
        else:
            return self.visit(ctx.expr2())
    # expr2: expr3 LOGICAND expr2 | expr3
    def visitExpr2(self,ctx:MCParser.Expr2Context):
        if ctx.LOGICAND():
            return BinaryOp("&&",self.visit(ctx.expr3()),self.visit(ctx.expr2()))
        else:
            return self.visit(ctx.expr3())
    # expr3: expr4 EQ expr4 | expr4 NEQ expr4 | expr4;
    def visitExpr3(self,ctx:MCParser.Expr3Context):
        if ctx.EQ():
            return BinaryOp("==",self.visit(ctx.expr4(0)),self.visit(ctx.expr4(1)))
        elif ctx.NEQ():
            return BinaryOp("!=",self.visit(ctx.expr4(0)),self.visit(ctx.expr4(1)))
        else:
            return self.visit(ctx.expr4(0))
    # expr4: expr5 LESS expr5 | expr5 LESSEQ expr5 | expr5 GREATER expr5 | expr5 GREATEREQ expr5 | expr5;
    def visitExpr4(self,ctx:MCParser.Expr4Context):
        if ctx.LESS():
            return BinaryOp('<',self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        elif ctx.LESSEQ():
            return BinaryOp("<=",self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        elif ctx.GREATER():
            return BinaryOp('>',self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        elif ctx.GREATEREQ():
            return BinaryOp(">=",self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        else:
            return self.visit(ctx.expr5(0))
    # expr5: expr6 ADD expr5 | expr6 SUBNEG expr5 | expr6
    def visitExpr5(self,ctx:MCParser.Expr5Context):
        if ctx.ADD():
            return BinaryOp('+',self.visit(ctx.expr6()),self.visit(ctx.expr5()))
        elif ctx.SUBNEG():
            return BinaryOp('-',self.visit(ctx.expr6()),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
    # expr6: expr7 DIV expr6 | expr7 MUL expr6 | expr7 MOD expr6 | expr7;
    def visitExpr6(self,ctx:MCParser.Expr6Context):
        if ctx.DIV():
            return BinaryOp('/',self.visit(ctx.expr7()),self.visit(ctx.expr6()))
        if ctx.MUL():
            return BinaryOp('*',self.visit(ctx.expr7()),self.visit(ctx.expr6()))
        if ctx.MOD():
            return BinaryOp('%',self.visit(ctx.expr7()),self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
    # expr7: SUBNEG expr8 | LOGICNOT expr8 | expr8;
    def visitExpr7(self,ctx:MCParser.Expr7Context):
        if ctx.SUBNEG():
            return UnaryOp('-',self.visit(ctx.expr8()))
        elif ctx.LOGICNOT():
            return UnaryOp('!',self.visit(ctx.expr8()))
        else: 
            return self.visit(ctx.expr8())
    #expr8: expr9 LV RV | expr9;
    def visitExpr8(self,ctx:MCParser.Expr8Context):
        if ctx.getChildCount()==3:
            return UnaryOp("[]",self.visit(expr9()))
        else: 
            return self.visit(ctx.expr9())
    # expr9: call|LB expr RB| varid | FLOATLIT | INTLIT | STRINGLIT | BOOLEANLIT ;
    def visitExpr9(self,ctx:MCParser.Expr9Context):
        if ctx.call():
            return self.visit(ctx.call())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.varid():
            return self.visit(ctx.varid())
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return BooleanLiteral(bool(ctx.BOOLEANLIT().getText()))
    # ifstate: IF LB expb? RB EOF? stmt EOF? (SM ELSE EOF? stmt)? ;
    def visitIfstate(self,ctx:MCParser.IfstateContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.expr()),self.visit(ctx.stmt(0)))
        else:
            return If(self.visit(ctx.expr()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)))
    # whilestate: DO (stmt SM)* WHILE  expb 
    def visitWhilestate(self,ctx:MCParser.WhilestateContext):
        return Dowhile(list(map(lambda x: self.visit(x),ctx.stmt())),ctx.expr())
    # forstate: FOR LB assign SM expb SM assign RB stmt 
    def visitForstate(self,ctx:MCParser.ForstateContext):
        return For(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.expr(2)),self.visit(ctx.stmt())) 
    # blockstate: LP var_stmt* RP;
    def visitBlockstate(self,ctx:MCParser.BlockstateContext):
        return Block(list(map(lambda x: self.visit(x),ctx.var_stmt())))
    #paradec: LB paralist? RB
    def visitParadec(self,ctx:MCParser.ParadecContext):
        if ctx.paralist():
            return self.visit(ctx.paralist())
        else:
            return []
    #paralist: para (SM para)*
    def visitParalist(self,ctx:MCParser.ParalistContext):
        return list(map(lambda x: self.visit(x),ctx.para()))
    #para: mctype ID
    def visitPara(self,ctx:MCParser.ParaContext):
        return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.mctype()))
    # mctype: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType
        elif ctx.FLOATLIT():
            return FloatType
        elif ctx.STRINGLIT():
            return StringType
        else:
            return BoolType