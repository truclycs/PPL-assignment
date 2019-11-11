"""
 * @author nhphung
 * @StudentName: Nguyen Thi Truc Ly 
 * @StudentID 1710187
"""

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import functools

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def checkRedeclared(list_decl, decl, kind):
    if kind == "Variable" or kind == "Parameter":
        if any(decl.variable.name == x.name for x in list_decl):
            raise Redeclared(kind, decl.variable.name)    
        return Symbol(decl.variable.name, decl.varType)

    else:
        if any(decl.name.name == x.name for x in list_decl):
            raise Redeclared(Function(), decl.name.name)    
        return Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType))

def getType(decl):
    return "Variable" if type(decl) is VarDecl else "Function"

def overrideDeclaration(environment, name):
    [environment.remove(id) for id in environment if id.name == name]

def BinOpType(l,r):
    if (type(l),type(r)) == (IntType,IntType):
        return IntType()
    elif ((type(l),type(r)) == (FloatType,FloatType)) or\
         ((type(l),type(r)) == (FloatType,IntType)) or\
         ((type(l),type(r)) == (IntType,FloatType)): 
        return FloatType()
    return None


def AssignmentRule(l,r):
    if type(l) == VoidType or type(l) == ArrayType:
        return False
    elif ((type(l) == ArrayPointerType and type(r) == ArrayType)) or\
         ((type(l) == ArrayPointerType and type(r) == ArrayPointerType)):
        return assE(l.eleType,r.eleType)
    elif (type(l), type(r)) == (FloatType,IntType):
        return True 
    else:
        return type(l)==type(r)


def assE(l,r):
    if ((type(l),type(r)) == (BoolType,BoolType)) or\
       ((type(l),type(r)) == (StringType,StringType)) or\
       ((type(l),type(r)) == (FloatType,FloatType)) or\
       ((type(l),type(r)) == (IntType,IntType)):
        return True
    else:
        return False


def assignExplicitType(l,r):
    if ((type(l),type(r)) == (BoolType,BoolType)) or\
       ((type(l),type(r)) == (StringType,StringType)) or\
       ((type(l),type(r)) == (FloatType,FloatType)) or\
       ((type(l),type(r)) == (IntType,IntType)) or\
       ((type(l),type(r)) == (FloatType,IntType)):
        return True
    else: 
        return False

class StaticChecker(BaseVisitor, Utils):
    global_envi =   [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([StringType()],VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        environment = c.copy()  
        entry_point = None
        return_type = None
        is_loop = False
        main_call = None
        reachable_func = {}
        
        for decl in ast.decl:
            environment.append(checkRedeclared(environment, decl, getType(decl)))
            if type(decl) == FuncDecl:
                entry_point = decl if decl.name.name == 'main' else entry_point
                reachable_func[decl.name.name] = decl.name.name == 'main'

        if not entry_point:
            raise NoEntryPoint()

        for decl in ast.decl:
            if not type(decl) is VarDecl:
                self.visit(decl, (environment, return_type, is_loop, reachable_func, main_call))
                
        # list(map(lambda x: self.visit(x, (environment, None, False, reachable_func, None)), ast.decl))

        # for func in reachable_func:
        #     if not reachable_func[func]:
        #         raise Unreachable(func)
        return None

    def visitFuncDecl(self, ast, c): 
        environment = c[0].copy()
        para = []
    
        for p in ast.param:
            para.append(checkRedeclared(para, p, "Parameter"))
        
        is_return = self.visitBlock(ast.body, (environment, ast.returnType, False, para, c[4], ast.name.name))
        if is_return is False and type(ast.returnType) != VoidType:
            raise FunctionNotReturn(ast.name.name)

    def visitBlock(self, ast, c):        
        environment = c[0].copy()
        # c[3]: list param
        lsP = c[3] if c[3] else []
        isRet = []
        isEnd = False     

        # find and override all vardecl
        for vd in ast.member:
            if vd is VarDecl:
                lsP.append(checkRedeclared(lsP,vd,"Variable"))
                overrideDeclaration(environment,vd.variable.name)
            else:
                if isEnd is True or isEnd is "BC":
                    raise UnreachableStatement(st)
                isEnd = self.visit(vd,(environment,c[1],c[2],[],c[4],c[5]))
                isRet.append(isEnd)

        environment += lsP
        return isEnd if isEnd is True or isEnd is "BC" else False



    def visitVarDecl(self, ast, c):
        local = c[0]
        type = c[1]
        environment = c[2]
        local.append(checkRedeclared(local, ast, c[1]))
        overrideDeclaration(environment, ast.variable.name)

    def visitIf(self,ast,c):
        """
        #expr:Expr
        #thenStmt:Stmt
        #elseStmt:Stmt
        """
        environment = c[0].copy()

        if type(self.visit(ast.expr,(environment,c[1],c[2],None,c[4],c[5]))) != BoolType:
            raise TypeMismatchInStatement(ast)

        ts = self.visit(ast.thenStmt,(environment,c[1],c[2],[],c[4],c[5]))
        es = self.visit(ast.elseStmt,(environment,c[1],c[2],[],c[4],c[5])) if ast.elseStmt else None
        
        if ts is True and es is True:
            return True
        elif ts is "BC" and es is "BC" or\
             ts is "BC" and es is True or\
             ts is True and es is "BC":
            return "BC"

    def visitFor(self,ast,c):
        """
        expr1,expr2,expr3: Expr
        loop: Stmt
        """
        environment = c[0].copy()

        ex1 = self.visit(ast.expr1,(environment,c[1],False,[],c[4],c[5]))
        ex2 = self.visit(ast.expr2,(environment,c[1],False,[],c[4],c[5]))
        ex3 = self.visit(ast.expr3,(environment,c[1],False,[],c[4],c[5]))
        if type(ex1) is not IntType or\
           type(ex2) is not BoolType or\
           type(ex3) is not IntType:
            raise TypeMismatchInStatement(ast)
        # visit all block 
        self.visit(ast.loop,(environment,c[1],True,[],c[4],c[5]))
        

    def visitDowhile(self,ast,c):
        """
        sl:  list(Stmt)
        exp: Expr
        """
        environment = c[0].copy()
        isEnd = False 
        for st in ast.sl:
            if isEnd is True or isEnd is "BC":
                raise UnreachableStatement(st)
            isEnd = self.visit(st,(environment,c[1],True,[],c[4],c[5]))
        if type(self.visit(ast.exp,(environment,c[1],False,[],c[4],c[5]))) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return True if isEnd is True else None


    def visitBinaryOp(self,ast,c):
        """
        #op:string
        #left:Expr
        #right:Expr
        """
        environment = c[0].copy() if c[0] is not None else []
        le  = self.visit(ast.left,(environment,c[1],c[2],[],c[4],c[5]))
        ri  = self.visit(ast.right,(environment,c[1],c[2],[],c[4],c[5]))
        op  = ast.op

        if op == "+" or op == "-" or op == "*" or op == "/":
            rtype = BinOpType(le,ri)
            if rtype is not None:
                return rtype
            raise TypeMismatchInExpression(ast)
        elif op == "<" or op == "<=" or op == ">" or op ==">=":
            rtype = BinOpType(le,ri)
            if rtype is not None:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "==" or op == "!=":
            if (type(le),type(ri)) == (IntType,IntType):
                return BoolType()
            elif (type(le),type(ri)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "%":
            if (type(le),type(ri)) == (IntType,IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
        elif op == "&&" or op == "||":
            if (type(le),type(ri)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "=":
            if assignExplicitType(le,ri): 
                return le
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        """
        op: String
        body: Expr  
        """
        environment = c[0].copy()
        rtype  = self.visit(ast.body,(environment,c[1],c[2],[],c[4],c[5]))
        if ast.op is "!":
            if type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast) 
            return BoolType()
        if (type(rtype) is not IntType) and (type(rtype) is not FloatType):
            raise TypeMismatchInExpression(ast) 
        return rtype


    def visitId(self,ast,c):
        """ 
        name:string 
        """
        environment = c[0].copy() if c[0] is not None else []
        res = self.lookup(ast.name, environment, lambda x:x.name)
        if res is None or type(res.MType) is MType :
            raise Undeclared(Identifier(),ast.name) 
        elif type(res) is Symbol:
            return res.mtype 
        else:
            raise Undeclared(Identifier(),ast.name)     

    def visitCallExpr(self, ast, c): 
        environment = c[0].copy() 
        res = self.lookup(ast.method.name,environment, lambda x: x.name)
        lsp = [self.visit(x,(environment,c[1],c[2],[],c[4],c[5])) for x in ast.param]
      
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(lsp):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(lsp)):
                if AssignmentRule(res.mtype.partype[i],lsp[i]) is False:
                    raise TypeMismatchInExpression(ast)
            # some magic here :v 
            if ast.method.name != c[5]:
                c[4][ast.method.name] += 1

            return res.mtype.rettype


    def visitArrayCell(self,ast,c):
        environment = c[0].copy()
        if type(self.visit(ast.idx,(environment,c[1],c[2],[],c[4],c[5]))) is not IntType:
            raise TypeMismatchInExpression(ast)
        else:
            arr = self.visit(ast.arr,(environment,c[1],c[2],[],c[4],c[5]))
            if type(arr) is (ArrayType or ArrayPointerType):
                return arr.eleType
            else:
                raise TypeMismatchInExpression(ast)


    def visitBreak(self,ast,c):
        if c[2] == False:
            raise BreakNotInLoop()
        return "BC"

    def visitContinue(self,ast,c):
        if c[2] == False:
            raise ContinueNotInLoop()
        return "BC"

    def visitReturn(self,ast,c):
        """
        expr: Expr
        """
        environment   = c[0].copy()
        rtype = c[1]
        if ast.expr is None and type(rtype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        elif ast.expr is None and type(rtype) is VoidType:
            return True
        elif AssignmentRule(rtype,self.visit(ast.expr,(environment,None, False,[],c[4],c[5]))) is False:
            raise TypeMismatchInStatement(ast)

        return True 

    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitVoidType(self,ast,c):
        return VoidType()

    def visitArrayType(self,ast,c):
        return ast.eleType 

    def visitArrayPointerType(self,ast,c):
        return ast.eleType

    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self,ast, c): 
        return FloatType()

    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
   