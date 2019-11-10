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
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def checkRedeclared(list_decl, decl, kind):
    if type(kind) in ["Variable", "Parameter"]:
        if any(decl.variable.name == x.name for x in list_decl):
            raise Redeclared(kind, decl.variable.name)
        return Symbol(decl.variable.name, decl.varType)
    
    if any(decl.name.name == x.name for x in list_decl):
        raise Redeclared(kind, decl.name.name)
    return Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType))

def getType(x):
    return Variable(x) if type(x) == VarDecl else Function(x)

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
        reachable_func = {}
        
        for decl in ast.decl:
            environment.append(checkRedeclared(environment, decl, getType(decl)))
            if type(decl) == FuncDecl:
                entry_point = decl if decl.name.name == 'main' else entry_point
                reachable_func[decl.name.name] = decl.name.name == 'main'

        if not entry_point:
            raise NoEntryPoint()

        list(map(lambda x: self.visit(x, (environment, None, False, reachable_func, None)), ast.decl))

        for func in reachable_func:
            if not reachable_func[func]:
                raise Unreachable(func)

        return None




