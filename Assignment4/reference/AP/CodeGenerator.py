from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import functools

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
        self.curFunc = Symbol("null", MType([], VoidType()), CName("MPClass"))

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)
        
class StringType(Type):
    def __str__(self):
        return "StringType"
    def accept(self, v, c):
       return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, c):
        return None
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, c):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst, isDup = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.isDup = isDup

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.curFunc = Symbol("null", MType([],VoidType()), CName(self.className))
        
    def varGlobal(self, ast, c):
        _ctxt = c
        _name = ast.variable.name
        _type = ast.varType
        self.emit.printout(self.emit.emitATTRIBUTE(_name, _type, False, ""))
        _symbol = Symbol(ast.variable.name, _type, CName(self.className))
        _ctxt.append(_symbol)
        return _ctxt
        
    def funcGlobal(self, ast, c):
        _ctxt = c
        _name = ast.name.name
        _type = MType([x.varType for x in ast.param], ast.returnType)
        _symbol = Symbol(_name, _type, CName(self.className))
        _ctxt.append(_symbol)
        return _ctxt
        
    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        _lsVar = [i for i in ast.decl if type(i) is VarDecl]
        _lsArrayVar = [i for i in _lsVar if type(i.varType) is ArrayType]
        _lsFun = [i for i in ast.decl if type(i) is FuncDecl]

        #functools.reduce(lambda x, y: self.varGlobal(y, x) if type(y) is VarDecl else self.funcGlobal(y, x), ast.decl, self.env if self.env else [])
        for x in ast.decl:
            self.env = self.varGlobal(x, self.env) if type(x) is VarDecl else self.funcGlobal(x, self.env)
        
        #functools.reduce(lambda a, b: self.visit(b, a), _lsFun, SubBody(None, self.env))
        for x in _lsFun:
            self.visit(x, SubBody(None, self.env))
        
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), c, Frame("<init>", VoidType))
        
        if _lsArrayVar:
            self.emit.printout(self.emit.emitCLINIT(self.className, _lsArrayVar, Frame("<clinit>", VoidType())))

        self.emit.emitEPILOG()
        
        return c
        
    def visitVarDecl(self, ast, c):
        _env = c.sym if type(c) is SubBody else []
        _frame = c.frame
        _idx = _frame.getNewIndex()
        _string = self.emit.emitVAR(_idx, ast.variable.name, ast.varType, _frame.getStartLabel(), _frame.getEndLabel(), _frame)
        self.emit.printout(_string)
        
        return SubBody(_frame, [Symbol(ast.variable.name, ast.varType, Index(_idx))] + _env)
        
    def arrayTypeDecl(self, ast, c):
        _sym = c.sym
        _frame = c.frame
        _idx = (self.lookup(ast.variable.name.lower(), _sym, lambda x: x.name.lower())).value.value
        self.emit.printout(self.emit.emitNEWARRAY(ast.varType, _frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.variable.name, ast.varType, _idx, _frame))
        return SubBody(_frame, _sym)
    
    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        
        mtype = MType(intype, returnType)
        
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        
        frame.enterScope(True)
        
        glenv = o
        
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            
        glSubBody = SubBody(frame, glenv)
        if (isMain is False) and (intype != []):
            for x in consdecl.param:
                glSubBody = self.visit(x, glSubBody)

        for x in consdecl.local:
            glSubBody = self.visit(x, glSubBody)
        
        lsArrVarDecl = [i for i in consdecl.local if type(i.varType) is ArrayType]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for x in lsArrVarDecl:
            self.arrayTypeDecl(x, glSubBody)

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        returnStmt = list(filter(lambda x:type(x) is Return, consdecl.body))
        
        [self.visit(x, glSubBody) for x in consdecl.body]
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if (type(returnType) is VoidType) or (not returnStmt):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope()
    
    def visitFuncDecl(self, ast, c):
        _sym = c.sym
        _frame = Frame(ast.name.name, ast.returnType)
        self.curFunc = self.lookup(ast.name.name.lower(), _sym, lambda x: x.name.lower())
        self.genMETHOD(ast, _sym, _frame)
        return c
    
    def genBinExpr(self, frame, resLeft, typeLeft, resRight, typeRight, isFloat = False):
        if type(typeLeft) is FloatType and type(typeRight) is IntType:
            return resLeft + resRight + self.emit.emitI2F(frame), FloatType()
        if type(typeLeft) is IntType and type(typeRight) is FloatType:
            return resLeft + self.emit.emitI2F(frame) + resRight, FloatType()
        if isFloat and type(typeLeft) is IntType:
            return resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitI2F(frame), FloatType()
        return resLeft + resRight, typeLeft
    
    def visitBinaryOp(self, ast, c):
        _frame = c.frame
        _sym = c.sym
        op = ast.op

        (resLeft, typeLeft) = self.visit(ast.left, Access(_frame, _sym, False, True, True))
        (resRight, typeRight) = self.visit(ast.right, Access(_frame, _sym, False, True, True))
        
        if op == "/":
            _exp, _type = self.genBinExpr(_frame, resLeft, typeLeft, resRight, typeRight, True)
            _op = self.emit.emitMULOP(op, FloatType(), _frame)
            _string = _exp + _op
            return _string, _type
            
        _exp, _type = self.genBinExpr(_frame, resLeft, typeLeft, resRight, typeRight)
        if op in ["andthen", "orelse"]: 
            _string = self.emit.emitAND_OR_SHORT_CIRCUIT(op, resLeft, resRight, _frame)
            return _string, _type

        if op in ["+", "-"]:
            _op = self.emit.emitADDOP(op, _type, _frame)
        elif op == "*":
            _op = self.emit.emitMULOP(op, _type, _frame)
        elif op.lower() == "div":
            _op = self.emit.emitMULOP("/", _type, _frame)
        elif op.lower() == "mod":
            _op = self.emit.emitMOD(_frame)
        elif op in ["<", "<=", ">", ">="]:
            _op = self.emit.emitREOP(op, _type, _frame)
            _type = BoolType()
        elif op in ["=", "<>"]:
            _op = self.emit.emitREOP(op, _type, _frame)
            _type = BoolType()
        elif op.lower() == "and":
            _op = self.emit.emitANDOP(_frame)
            _type = BoolType()
        elif op.lower() == "or":
            _op = self.emit.emitOROP(_frame)
            _type = BoolType()
        _string = _exp + _op   

        return _string, _type

    def visitUnaryOp(self, ast, c):
        _frame = c.frame
        _sym = c.sym

        (resExpr, typeExpr) = self.visit(ast.body, Access(_frame, _sym, False, True, True))

        if ast.op == "not":
            return resExpr + self.emit.emitNOT(BoolType(), _frame), BoolType()
        elif ast.op == "-": 
            return resExpr + self.emit.emitNEGOP(typeExpr, _frame), typeExpr

    def visitCallExpr(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        returnType = ctype.rettype

        if ctxt.isLeft and not ctxt.isFirst:
            return self.emit.emitWRITEVAR2(ast.method.name, returnType, frame), returnType

        listParamType = ctype.partype
        checkList = []
        for item in range(len(listParamType)):
            checkList.append((ast.param[item], listParamType[item]))

        in_ = ("", [])

        for x in checkList:
            (str1, typ1) = self.visit(x[0], Access(frame, nenv, False, True, True))
            if type(x[1]) is ArrayType:
                str1 += self.emit.emitCLONE(typ1) + self.emit.emitCHECKCAST(typ1)
            if type(typ1) is IntType and type(x[1]) is FloatType:
                in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
            else:
                in_ = (in_[0] + str1, in_[1] + [typ1])

        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), returnType

    def visitId(self, ast, c):
        if type(c) != SubBody:
            sym = self.lookup(ast.name.lower(), c.sym, lambda x: x.name.lower())
            code = ""
            if c.isLeft is True and c.isFirst is True:
                pass
            elif c.isLeft is True and c.isFirst is False:
                if type(sym.mtype) is ArrayType or type(sym.mtype) is ArrayPointerType:
                    code = self.emit.emitWRITEVAR2(sym.name, sym.mtype, c.frame)
                else:
                    if type(sym.value) is CName:
                        code = self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, c.frame)
                    elif type(sym.value) is Index:
                        code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, c.frame)
            elif c.isLeft is False:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, c.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitREADVAR(ast, sym.mtype, sym.value.value, c.frame)
            return code, sym.mtype
        else:
            sym = self.lookup(ast.name.lower(), c.sym, lambda x: x.name.lower())
            return ("", sym.mtype)
            
    def visitArrayCell(self, ast, c):
        if type(c) != SubBody:
            frame = c.frame
            lsSym = c.sym

            arrt = self.lookup(ast.arr.method.name.lower() if type(ast.arr) is CallExpr else ast.arr.name.lower(), lsSym, lambda x: x.name.lower())
            lw = int(arrt.mtype.rettype.lower) if type(arrt.mtype) is MType else int(arrt.mtype.lower)

            if c.isLeft is True and c.isFirst is True:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
                if lw >= 0:
                    (resIdx, typIdx) = self.visit(BinaryOp("-", ast.idx, IntLiteral(lw)), Access(frame, lsSym, False, True, True))
                else:
                    (resIdx, typIdx) = self.visit(BinaryOp("+", ast.idx, IntLiteral(- lw)), Access(frame, lsSym, False, True, True))
                return (resArr + resIdx, typeArr.eleType)
            
            elif c.isLeft is True and c.isFirst is False:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, True, False, False))
                return (resArr, typeArr)
            
            elif c.isLeft is False:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
                if lw >= 0:
                    (resIdx, typIdx) = self.visit(BinaryOp("-", ast.idx, IntLiteral(lw)), Access(frame, lsSym, False, True, True))
                else:
                    (resIdx, typIdx) = self.visit(BinaryOp("+", ast.idx, IntLiteral(- lw)), Access(frame, lsSym, False, True, True))
                
                if type(typeArr) is ArrayType:
                    arrayType = typeArr.eleType
                    aload = self.emit.emitALOAD(arrayType, frame)
                    return (resArr + resIdx + aload, arrayType)
                elif type(typeArr) is ArrayPointerType:
                    arrayPointerType = typeArr.eleType
                    aload = self.emit.emitALOAD(arrayPointerType, frame)
                    return (resArr + resIdx + aload, arrayPointerType)
        else:
            frame = c.frame
            lsSym = c.sym
            (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
            arrType = typeArr.eleType
            return ("", arrayType)
        return None
    
    def visitAssign(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym
        op_Str = ""
        str_I2f = "" 
        resType = IntType()
        (resLeft1, typeLeft1) = self.visit(ast.lhs, Access(frame, env, True, True))
        (resRight, typeRight) = self.visit(ast.exp,Access(frame, env, False, True))

        if type(typeLeft1) == FloatType and type(typeRight) == IntType:
            str_I2f = self.emit.emitI2F(frame)
        
        (resLeft2, typeLeft2) = self.visit(ast.lhs, Access(frame, env, True, False))
        
        _fcp, _type = self.genBinExpr(frame, resLeft1, typeLeft1, resRight, typeRight)
        _string = _fcp + resLeft2
        
        self.emit.printout(_string)
        return (_string, _type)
    
    def visitWith(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        newEnv = ctxt.sym
        
        frame.enterScope(False)
        
        varEnv = functools.reduce(lambda a, b: self.visit(b, a), ast.decl, SubBody(frame, newEnv))
        
        # list Vardecl
        listVarDecl = ast.decl
        listArrayVarDecl = filter(lambda x: type(x.varType) is ArrayType, listVarDecl)
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        [self.arrayTypeDecl(x, varEnv) for x in listArrayVarDecl]
        [self.visit(x, varEnv) for x in ast.stmt]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return None

    def visitIf(self, ast, c):
        frame = c.frame
        env = c.sym
        (resExpr, typeExpr) = ast.expr.accept(self, Access(frame, env, False, True, True))
        falseLabel = frame.getNewLabel()
        
        self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
        [self.visit(x, c) for x in ast.thenStmt]
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        else:
            trueLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(trueLabel, frame) + self.emit.emitLABEL(falseLabel, frame))
            [self.visit(x, c) for x in ast.elseStmt]
            self.emit.printout(self.emit.emitLABEL(trueLabel, frame))
        return None

    def visitFor(self, ast, c):
        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()

        self.visit(Assign(ast.id, ast.expr1), SubBody(frame, env))
        self.visit(Assign(ast.id, BinaryOp("-", ast.id, IntLiteral(1))), c)
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        self.visit(Assign(ast.id, BinaryOp("+", ast.id, IntLiteral(1))), c)
        (resExpr2, typeExpr2) = self.visit(BinaryOp("<=", ast.id, ast.expr2), Access(frame, env, False, True))
        self.emit.printout(resExpr2)
        self.emit.printout(self.emit.emitIFTRUE(frame.getBreakLabel(), frame))
        (r1, t1) = self.visit(ast.id, Access(frame, env, False, True))
        self.emit.printout(r1)
        (r1, t1) = self.visit(ast.expr2, Access(frame, env, False, True))
        self.emit.printout(r1)
        [self.visit(i, c) for i in ast.loop]
        
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        (r1, t1) = self.visit(ast.expr2, Access(frame, env, True, False))
        self.emit.printout(r1)
        (r1, t1) = self.visit(ast.id, Access(frame, env, True, False))
        self.emit.printout(r1)
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        
        
#        self.visit(Assign(ast.id, ast.expr1), SubBody(frame, env))
#        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
#        if ast.up:
#            (resExpr2, typeExpr2) = self.visit(BinaryOp("<=", ast.id, ast.expr2), Access(frame, env, False, True, False))
#        else:
#            (resExpr2, typeExpr2) = self.visit(BinaryOp(">=", ast.id, ast.expr2), Access(frame, env, False, True, False))
#        self.emit.printout(resExpr2)
#        self.emit.printout(self.emit.emitIFTRUE(frame.getBreakLabel(), frame))
#        [self.visit(i, c) for i in ast.loop]
#        
#        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
#        if ast.up:
#            self.visit(Assign(ast.id, BinaryOp("+", ast.id, IntLiteral(1))), c)
#        else:
#            self.visit(Assign(ast.id, BinaryOp("-", ast.id, IntLiteral(1))), c)
#        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))
#        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        
        frame.exitLoop()
        return None
    
    def visitContinue(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        return None
    
    def visitBreak(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
        return None
    
    def visitReturn(self, ast, c):
        if ast.expr:
            (resExpr, resType) = self.visit(ast.expr, Access(c.frame, c.sym, False, True, True))
            typeFunc = self.curFunc.mtype.rettype
            if type(typeFunc) is FloatType and type(resType) is IntType:
                self.emit.printout(resExpr + self.emit.emitI2F(c.frame) + self.emit.emitRETURN(FloatType(), c.frame))
            else:
                self.emit.printout(resExpr + self.emit.emitRETURN(resType, c.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), c.frame))
        return None

    def visitWhile(self, ast, c):
        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        
        (resExpr, typeExpr) = ast.exp.accept(self, Access(frame, env, False, True, True))
        self.emit.printout(resExpr)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))
        
        [self.visit(x, c) for x in ast.sl]
        
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()
        return None
    
    def visitCallStmt(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype
        
        listParamType = ctype.partype
        checkList = []
        for item in range(len(listParamType)):
            checkList.append((ast.param[item], listParamType[item]))
        
        in_ = ("", list())
        
        for x in checkList:
            (str1, typ1) = self.visit(x[0], Access(frame, nenv, False, True, True))
            if type(x[1]) is ArrayType:
                str1 += self.emit.emitCLONE(typ1) + self.emit.emitCHECKCAST(typ1)
            if type(typ1) is IntType and type(x[1]) is FloatType:
                in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
            else:
                in_ = (in_[0] + str1, in_[1] + [typ1])

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))
        return None
    
    def visitIntLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    
    def visitFloatLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()
    
    def visitStringLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
        