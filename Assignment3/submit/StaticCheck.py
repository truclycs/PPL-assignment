#Student ID: 1710187  
#Student name: Nguyen Thi Truc Ly  
              
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
        self.name  = name
        self.mtype = mtype
        self.value = value

def checkRedeclared(list_decl, decl, kind):
    if kind == "Variable" or kind == "Parameter":
        if any(decl.variable == x.name for x in list_decl):
            raise Redeclared(kind, decl.variable)    
        return Symbol(decl.variable, decl.varType)
    else:
        if any(decl.name.name == x.name for x in list_decl):
            raise Redeclared(Function(), decl.name.name)    
        return Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType))

def getType(decl):
    return "Variable" if type(decl) is VarDecl else "Function"

def overrideDeclaration(environment, name):
    [environment.remove(id) for id in environment if id.name == name]

def BinOpType(left, right):
    if (type(left), type(right)) == (IntType, IntType):
        return IntType()
    elif ((type(left), type(right)) == (FloatType, FloatType)) or\
         ((type(left), type(right)) == (FloatType, IntType)) or\
         ((type(left), type(right)) == (IntType, FloatType)): 
        return FloatType()
    return None

def assignRule(left, right):
    if type(left) == VoidType or type(left) == ArrayType:
        return False
    elif ((type(left) == ArrayPointerType and type(right) == ArrayType)) or\
         ((type(left) == ArrayPointerType and type(right) == ArrayPointerType)):
        return eleType(left.eleType, right.eleType)
    elif (type(left), type(right)) == (FloatType, IntType):
        return True 
    else:
        return type(left) == type(right)

def eleType(left, right):
    if ((type(left), type(right)) == (BoolType, BoolType)) or\
       ((type(left), type(right)) == (StringType, StringType)) or\
       ((type(left), type(right)) == (FloatType, FloatType)) or\
       ((type(left), type(right)) == (IntType, IntType)):
        return True
    else:
        return False

def explicitType(left, right):
    if ((type(left), type(right)) == (BoolType, BoolType)) or\
       ((type(left), type(right)) == (StringType, StringType)) or\
       ((type(left), type(right)) == (FloatType, FloatType)) or\
       ((type(left), type(right)) == (IntType, IntType)) or\
       ((type(left), type(right)) == (FloatType, IntType)):
        return True
    else: 
        return False

class StaticChecker(BaseVisitor, Utils):
    global_envi =  [Symbol("getInt", MType([], IntType())),
                    Symbol("putInt", MType([IntType()], VoidType())),
                    Symbol("putIntLn", MType([IntType()], VoidType())),
                    Symbol("getFloat", MType([], FloatType())),
                    Symbol("putFloat", MType([FloatType()], VoidType())),
                    Symbol("putFloatLn", MType([FloatType()], VoidType())),
                    Symbol("putBool", MType([BoolType()], VoidType())),
                    Symbol("putBoolLn", MType([BoolType()], VoidType())),
                    Symbol("putString", MType([StringType()], VoidType())),
                    Symbol("putStringLn", MType([StringType()], VoidType())),
                    Symbol("putLn", MType([], VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        environment = c.copy()  
        return_type = None
        entry_point = 0
        is_loop = False
        list_para = None
        reachable_func = {}
        main_call = None
        
        for decl in ast.decl:
            environment.append(checkRedeclared(environment, decl, getType(decl)))
            if type(decl) is FuncDecl:
                entry_point = decl.name.name == 'main' or entry_point
                reachable_func[decl.name.name] = decl.name.name == 'main'

        if not entry_point: 
            raise NoEntryPoint()

        for decl in ast.decl:
            if type(decl) is FuncDecl:
                self.visit(decl, (environment, return_type, is_loop, list_para, reachable_func, main_call))

        for func in reachable_func:
            if reachable_func[func] == 0:
                raise UnreachableFunction(func)
        
        return None

    def visitFuncDecl(self, ast, c): 
        environment = c[0].copy()
        list_para = []

        for para in ast.param:
            list_para.append(checkRedeclared(list_para, para, "Parameter"))

        environment += list_para
        
        is_return = self.visit(ast.body, (environment, ast.returnType, False, list_para, c[4], ast.name.name))
       
        if not is_return and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)

    def visitBlock(self, ast, c):      
        environment = c[0].copy() 
        list_para = c[3]
        end = False    

        for mem in ast.member:  
            if type(mem) is VarDecl:    
                list_para.append(checkRedeclared(list_para, mem, "Variable"))
                overrideDeclaration(environment, mem.variable)
            else:
                environment += list_para
                end = self.visit(mem, (environment, c[1], c[2], [], c[4], c[5]))
                
        environment += list_para
        return end if end is True or end is "BC" else False   

    def visitIf(self, ast, c):
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
        environment = c[0].copy()
        ex1 = self.visit(ast.expr1,(environment,c[1],False,[],c[4],c[5]))
        ex2 = self.visit(ast.expr2,(environment,c[1],False,[],c[4],c[5]))
        ex3 = self.visit(ast.expr3,(environment,c[1],False,[],c[4],c[5]))
        if type(ex1) is not IntType or\
           type(ex2) is not BoolType or\
           type(ex3) is not IntType:
            raise TypeMismatchInStatement(ast)
    
        self.visit(ast.loop,(environment,c[1],True,[],c[4],c[5]))
        
    def visitDowhile(self, ast, c):
        environment = c[0].copy()
        end = False 
        for st in ast.sl:
            if end is True or end is "BC":
                raise UnreachableStatement(st)
            end = self.visit(st,(environment,c[1],True,[],c[4],c[5]))
        if type(self.visit(ast.exp,(environment,c[1],False,[],c[4],c[5]))) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return True if end is True else None

    def visitBinaryOp(self, ast, c):
        environment = c[0].copy() if c[0] is not None else []
        left  = self.visit(ast.left,(environment,c[1],c[2],[],c[4],c[5]))
        right  = self.visit(ast.right,(environment,c[1],c[2],[],c[4],c[5]))
        op  = ast.op

        if op == "+" or op == "-" or op == "*" or op == "/":
            rtype = BinOpType(left,right)
            if rtype is not None:
                return rtype
            raise TypeMismatchInExpression(ast)
        elif op == "<" or op == "<=" or op == ">" or op == ">=":
            rtype = BinOpType(left,right)
            if rtype is not None:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "==" or op == "!=":
            if (type(left),type(right)) == (IntType,IntType):
                return BoolType()
            elif (type(left),type(right)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "%":
            if (type(left),type(right)) == (IntType,IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
        elif op == "&&" or op == "||":
            if (type(left), type(right)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "=":
            if explicitType(left, right): 
                if type(ast.left) not in [Id, ArrayCell]:
                    raise NotLeftValue(ast.left)
                return left
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        environment = c[0].copy()
        rtype  = self.visit(ast.body,(environment,c[1],c[2],[],c[4],c[5]))
        if ast.op is "!":
            if type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast) 
            return BoolType()
        if (type(rtype) is not IntType) and (type(rtype) is not FloatType):
            raise TypeMismatchInExpression(ast) 
        return rtype 

    def visitCallExpr(self, ast, c): 
        environment = c[0].copy() 

        res = self.lookup(ast.method.name, environment, lambda x: x.name)

        if (res in StaticChecker.global_envi):
            c[4][res.name] = 1
            
        list_para = [self.visit(x, (environment, c[1], c[2], [], c[4], c[5])) for x in ast.param]
        
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(list_para):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(list_para)):
                if assignRule(res.mtype.partype[i],list_para[i]) is False:
                    raise TypeMismatchInExpression(ast)

            if ast.method.name != c[5]:
                c[4][ast.method.name] += 1

            return res.mtype.rettype

    def visitId(self, ast, c):
        environment = c[0].copy()
        id = self.lookup(ast.name, environment, lambda x: x.name)
        if id is None:
            raise Undeclared(Identifier(), ast.name) 
        return id.mtype 

    def visitArrayCell(self, ast, c):
        environment = c[0].copy()
        if type(self.visit(ast.idx,(environment,c[1],c[2],[],c[4],c[5]))) is not IntType:
            raise TypeMismatchInExpression(ast)
        else:
            arr = self.visit(ast.arr,(environment,c[1],c[2],[],c[4],c[5]))
            if type(arr) is (ArrayType or ArrayPointerType):
                return arr.eleType
            else:
                raise TypeMismatchInExpression(ast)

    def visitBreak(self, ast, c):
        if c[2] == False:
            raise BreakNotInLoop()
        return "BC"

    def visitContinue(self, ast, c):
        if c[2] == False:
            raise ContinueNotInLoop()
        return "BC"

    def visitReturn(self, ast, c):        
        environment = c[0].copy()
        rtype = c[1]
        if ast.expr is None:
            if type(rtype) is VoidType:
                return True
            else:
                raise TypeMismatchInStatement(ast)
        elif assignRule(rtype, self.visit(ast.expr,(environment,None, False,[],c[4],c[5]))) is False:
            raise TypeMismatchInStatement(ast)
        return True 
      
    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        return ast.eleType

    def visitArrayPointerType(self, ast, c):
        return ast.eleType

    def visitIntLiteral(self, ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c): 
        return FloatType()

    def visitStringLiteral(self, ast, c): 
        return StringType()

    def visitBooleanLiteral(self, ast, c): 
        return BoolType()