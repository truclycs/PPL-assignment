# ID: 1710009
# Name: Phan Gia Anh 

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):


#===================================VISIT [PROGRAM]===================================
    # program  : declaration+ EOF ;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        List = []
        for x in ctx.declaration():
            mem = self.visit(x)
            List.extend(mem)
        return Program(List)


    # declaration: vardec | fundec ;
    def visitDeclaration(self,ctx:MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))
#=====================================================================================



#===================================VISIT [DECLARATION]===================================
    # vardec: primitive var(COMMA var)* SEMI ;
    def visitVardec(self,ctx:MCParser.VardecContext):
        if(ctx.getChildCount() == 3):
            Ele = self.visit(ctx.var(0))
            return [VarDecl(Ele[0],self.visit(ctx.primitive()))] if(len(Ele) == 1) else [VarDecl(Ele[0],ArrayType(Ele[1],self.visit(ctx.primitive())))]
        else:
            List = []
            for x in ctx.var():
                Ele = self.visit(x)
                List.append(VarDecl(Ele[0],self.visit(ctx.primitive())) if(len(Ele) == 1) else VarDecl(Ele[0],ArrayType(Ele[1],self.visit(ctx.primitive()))))
            return List


    # var: IDENTIFIER | IDENTIFIER LSQUARE INTLIT RSQUARE ;
    def visitVar(self,ctx:MCParser.VarContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        else:
            return [ctx.IDENTIFIER().getText(),int(ctx.INTLIT().getText())]


    # primitive: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE ;
    def visitPrimitive(self,ctx:MCParser.PrimitiveContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()


    # fundec: funtype IDENTIFIER LBRACKET paralist RBRACKET blockstmt ;
    def visitFundec(self,ctx:MCParser.FundecContext):
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.paralist()),self.visit(ctx.funtype()),self.visit(ctx.blockstmt()))]


    # funtype: primitive | VOIDTYPE | arraypointer ;
    def visitFuntype(self,ctx:MCParser.FuntypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        else:
            return self.visit(ctx.getChild(0))
    

    # arraypointer: (INTTYPE | FLOATTYPE | STRINGTYPE | BOOLTYPE) LSQUARE RSQUARE ;
    def visitArraypointer(self,ctx:MCParser.ArraypointerContext):
        if ctx.INTTYPE():
            return ArrayPointerType(IntType())
        elif ctx.FLOATTYPE():
            return ArrayPointerType(FloatType())
        elif ctx.STRINGTYPE():
            return ArrayPointerType(StringType())
        else:
            return ArrayPointerType(BoolType())
            
    
    # paralist: (paradec(COMMA paradec)*)? ;
    def visitParalist(self,ctx:MCParser.ParalistContext):
        return [self.visit(x) for x in ctx.paradec()]


    # paradec: primitive IDENTIFIER | primitive IDENTIFIER LSQUARE RSQUARE ;
    def visitParadec(self,ctx:MCParser.ParadecContext):
        if(ctx.getChildCount() == 2):
            return VarDecl(ctx.IDENTIFIER().getText(),self.visit(ctx.primitive()))
        else:
            return VarDecl(ctx.IDENTIFIER().getText(),ArrayPointerType(self.visit(ctx.primitive())))
#=========================================================================================



#===================================VISIT [STATEMENT]===================================
    # blockstmt: LPARENTHESIS blockmem* RPARENTHESIS ;
    def visitBlockstmt(self,ctx:MCParser.BlockstmtContext):
        List = []
        for x in ctx.blockmem():
            mem = self.visit(x)
            List.extend(mem)
        return Block(List)


    # blockmem: vardec | stmt ;
    def visitBlockmem(self,ctx:MCParser.BlockmemContext):
        return self.visit(ctx.getChild(0)) if ctx.vardec() else [self.visit(ctx.getChild(0))]
        

    # stmt: blockstmt | ifstmt | whilestmt | forstmt | breakstmt | continuestmt | returnstmt | expstmt ;
    def visitStmt(self,ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # ifstmt: IF LBRACKET exp RBRACKET stmt (ELSE stmt)? ;    
    def visitIfstmt(self,ctx:MCParser.IfstmtContext):
        return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)) if(len(ctx.stmt()) == 2) else None)
    

    # whilestmt: DO stmt+ WHILE exp SEMI ;
    def visitWhilestmt(self,ctx:MCParser.WhilestmtContext):
        return Dowhile([self.visit(x) for x in ctx.stmt()],self.visit(ctx.exp()))


    # forstmt: FOR LBRACKET exp SEMI exp SEMI exp RBRACKET stmt ;
    def visitForstmt(self,ctx:MCParser.ForstmtContext):
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.stmt()))


    # breakstmt: BREAK SEMI ;
    def visitBreakstmt(self,ctx:MCParser.BreakstmtContext):
        return Break()


    # continuestmt: CONTINUE SEMI ;
    def visitContinuestmt(self,ctx:MCParser.ContinuestmtContext):
        return Continue()


    # returnstmt: RETURN (exp)? SEMI ;
    def visitReturnstmt(self,ctx:MCParser.ReturnstmtContext):
        return Return(self.visit(ctx.exp()) if ctx.exp() else None)


    # expstmt: exp SEMI ;
    def visitExpstmt(self,ctx:MCParser.ExpstmtContext):
        return self.visit(ctx.exp())
#=======================================================================================
    


#===================================VISIT [EXPRESSION]===================================
    # exp: exp1 (ASSIGN exp)? | exp8 | exp9 ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp1()),self.visit(ctx.exp()))


    # exp1: exp1 OR exp2 | exp2 ;
    def visitExp1(self,ctx:MCParser.Exp1Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))


    # exp2: exp2 AND exp3 | exp3 ;
    def visitExp2(self,ctx:MCParser.Exp2Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))


    # exp3: exp4 ISEQUAL exp4 | exp4 ;
    def visitExp3(self,ctx:MCParser.Exp3Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))


    # exp4: exp5 COMP exp5 | exp5 COMPEQ exp5 | exp5 ;
    def visitExp4(self,ctx:MCParser.Exp4Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))


    # exp5: exp5 ADD exp6 | exp5 SUB exp6 | exp6 ;
    def visitExp5(self,ctx:MCParser.Exp5Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))


    # exp6: exp6 DIV exp7 | exp6 MUL exp7 | exp6 MOD exp7 | exp7 ;
    def visitExp6(self,ctx:MCParser.Exp6Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))


    # exp7: SUB exp7 | NOT exp7 | exp8 ;
    def visitExp7(self,ctx:MCParser.Exp7Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp7()))


    # exp8: exp9 LSQUARE exp RSQUARE | exp9 ;
    def visitExp8(self,ctx:MCParser.Exp8Context):
        if(ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        else:
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))


    # exp9: LBRACKET exp RBRACKET | funcall | literals | IDENTIFIER ;
    def visitExp9(self,ctx:MCParser.Exp9Context):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif(ctx.getChildCount() != 1):
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.getChild(0))


    # literals: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT ;
    def visitLiterals(self,ctx:MCParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return BooleanLiteral(True) if(ctx.BOOLLIT().getText() == "true") else BooleanLiteral(False)


    # funcall: IDENTIFIER LBRACKET (exp(COMMA exp)*)? RBRACKET ;
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()),[self.visit(x) for x in ctx.exp()])
#========================================================================================