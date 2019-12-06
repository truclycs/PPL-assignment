from Utils import *
from StaticCheck import *
from StaticError import *
from MachineCode import JasminCode
from CodeGenError import *
import CodeGenerator as cgen
import functools

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()
        
    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is cgen.StringType or typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is cgen.ArrayPointerType or typeIn is ArrayType:
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + (self.getJVMType(inType.rettype))
        elif typeIn is cgen.ClassType:
            return "L" + inType.cname + ";"
        else:
            return ""
            
    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is cgen.StringType or typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
            
    def emitPUSHICONST(self, in_, frame):

        frame.push();
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(""+str(i)) 
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(1 if in_ is "True" else 0, frame)
                
                
    def emitPUSHFCONST(self, in_, frame):
    
        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(str(in_))   
            
    def emitPUSHCONST(self, in_, typ, frame):

        if type(typ) is IntType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(1 if in_ is True else 0, frame)
        elif type(typ) is cgen.StringType:
            frame.push()
            return self.jvm.emitLDC("\"" + in_ + "\"")
        else:
            raise IllegalOperandException(in_)
            
    def emitALOAD(self, in_, frame):

        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        if type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        if type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is cgen.StringType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))
            
    def emitASTORE(self, in_, frame):

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        if type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is cgen.StringType or type(in_) is ArrayType or type(in_) is StringType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))
            
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)
        
    def emitREADVAR(self, name, inType, index, frame):

        frame.push()
        if type(inType) is IntType:
            return self.jvm.emitILOAD(index)
        if type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        if type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is cgen.StringType or type(inType) is ArrayType or type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)
            
    def emitREADVAR2(self, name, typ, frame):

        if type(typ) is ArrayType:
            emitALOAD(typ.eleType, frame)
        raise IllegalOperandException(name)
        
    def emitWRITEVAR(self, name, inType, index, frame):
        frame.pop()

        if type(inType) is IntType:
            return self.jvm.emitISTORE(index)
        if type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        if type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif (type(inType) is cgen.ArrayPointerType) or (type(inType) is cgen.ClassType) or (type(inType) is cgen.StringType) or (type(inType) is ArrayType) or (type(inType)) is StringType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)
            
    def emitWRITEVAR2(self, name, typ, frame):

        if type(typ) is ArrayType or type(typ) is cgen.ArrayPointerType:
            return self.emitASTORE(typ.eleType,frame)
        raise IllegalOperandException(name)
        
    def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
    
        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)
        
    def emitGETSTATIC(self, lexeme, in_, frame):
    
        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))
        
    def emitPUTSTATIC(self, lexeme, in_, frame):

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))
        
    def emitGETFIELD(self, lexeme, in_, frame):

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))
        
    def emitPUTFIELD(self, lexeme, in_, frame):

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))
        
    def emitINVOKESTATIC(self, lexeme, in_, frame):
    
        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))
        
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()
        
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))
        
    def emitNEGOP(self, in_, frame):

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()
            
    def emitNOT(self, in_, frame):

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE2(label1, frame))
        result.append(self.emitPUSHCONST(True, in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST(False, in_, frame))
        result.append(self.emitLABEL(label2, frame))

        return ''.join(result)
        
    def emitADDOP(self, lexeme, in_, frame):

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()
                
    def emitMULOP(self, lexeme, in_, frame):

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()
                
    def emitDIV(self, frame):

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):

        frame.pop()
        return self.jvm.emitIREM()
        
    def emitANDOP(self, frame):

        frame.pop()
        return self.jvm.emitIAND()
        
    def emitOROP(self, frame):

        frame.pop()
        return self.jvm.emitIOR()
        
    def emitAND_OR_SHORT_CIRCUIT(self,op,left,right,frame):
        result = []
        labelX = frame.getNewLabel()
        labelY = frame.getNewLabel()
        
        if op == "orelse":
            result.append(left)
            result.append(self.jvm.emitIFGT(labelX))
            frame.pop()
            result.append(right)
            result.append(self.jvm.emitIFGT(labelX))
            frame.pop()
            result.append(self.emitPUSHCONST(0, IntType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelY,frame))
            result.append(self.emitLABEL(labelX,frame))
            result.append(self.emitPUSHCONST(1, IntType(), frame))
            result.append(self.emitLABEL(labelY,frame))
        elif op == "andthen":
            result.append(left)
            result.append(self.jvm.emitIFLE(labelX))
            frame.pop()
            result.append(right)
            result.append(self.jvm.emitIFLE(labelX))
            frame.pop()
            result.append(self.emitPUSHCONST(1, IntType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelY,frame))
            result.append(self.emitLABEL(labelX,frame))
            result.append(self.emitPUSHCONST(0, IntType(), frame))
            result.append(self.emitLABEL(labelY,frame))

            
        return ''.join(result)

    def emitREOP(self, op, in_, frame):
    
        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if op == ">":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLE(labelF))
            else:
                result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLT(labelF))
            else:
                result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGE(labelF))
            else:
                result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGT(labelF))
            else:
                result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "<>":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFEQ(labelF))
            elif (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is cgen.StringType) or (type(in_) is cgen.ArrayPointerType):
                result.append(self.jvm.emitIFACMPEQ(labelF))
            else:
                result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFNE(labelF))
            elif (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is cgen.StringType) or (type(in_) is cgen.ArrayPointerType):
                result.append(self.jvm.emitIFACMPNE(labelF))
            else:
                result.append(self.jvm.emitIFICMPNE(labelF))

        result.append(self.emitPUSHCONST(1, IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(str(labelO), frame))
        result.append(self.emitLABEL(str(labelF), frame))
        result.append(self.emitPUSHCONST(0, IntType(), frame))
        result.append(self.emitLABEL(str(labelO), frame))

        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):

        result = [] 

        frame.pop()
        frame.pop()
        if op == ">":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPLE(falseLabel))
                result.append(self.jvm.emitGOTO(trueLabel))

        elif op == ">=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLT(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPLT(falseLabel))

        elif op == "<":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPGE(falseLabel))

        elif op == "<=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGT(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPGT(falseLabel))

        elif op == "!=":
            if (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is cgen.StringType) or (type(in_) is cgen.ArrayPointerType):
                result.append(self.jvm.emitIFACMPEQ(falseLabel))
            elif type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFEQ(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPEQ(falseLabel))

        elif op == "==":
            if (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is cgen.StringType) or (type(in_) is cgen.ArrayPointerType):
                result.append(self.jvm.emitIFACMPNE(falseLabel))
            elif type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFNE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPNE(falseLabel))

        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    def emitMETHOD(self, lexeme, in_, isStatic, frame):

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)
        
    def emitENDMETHOD(self, frame):

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)
        
    def emitNEWARRAY(self,in_,frame):

        buffer = []
        buffer.append(self.emitPUSHICONST(int(in_.upper) - int(in_.lower) + 1, frame))
        if type(in_.eleType) is cgen.StringType or type(in_.eleType) is StringType:
            buffer.append(self.jvm.emitANEWARRAY(self.getFullType(in_.eleType)))
        elif (type(in_.eleType) is IntType) or (type(in_.eleType) is FloatType) or (type(in_.eleType) is BoolType):
            buffer.append(self.jvm.emitNEWARRAY(self.getFullType(in_.eleType)))
        
        return ''.join(buffer)
        
    def emitNEW(self,in_,frame):

        buffer = []
        buffer.append(self.jvm.emitNEW(in_.cname))
        frame.push()
        buffer.append(self.jvm.emitDUP)
        frame.push()
        return ''.join(buffer)
        
    def emitINITGLOBALARRAY(self,lexeme,in_,frame):

        buffer = []
        buffer.append(self.emitNEWARRAY(in_, frame))
        frame.pop()
        buffer.append(self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_)))
        return ''.join(buffer)
        
    def emitCLINIT(self,classname,in_,frame):

        result          = []
        initGlobalArray = []
        tmp = MType([],VoidType())
        
        frame.enterScope(True)
        result.append(self.emitMETHOD("<clinit>", tmp, True, frame))
        
        for x in in_:
            initGlobalArray.append(self.emitINITGLOBALARRAY(classname+"."+x.variable.name,x.varType,frame))

        result.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        result.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        result.append(''.join(initGlobalArray))
        result.append(self.emitRETURN(VoidType(), frame))
        result.append(self.jvm.emitENDMETHOD())
        frame.exitScope()
        
        return ''.join(result)
        
    def getConst(self, ast):

        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())
        elif type(ast) is BooleanLiteral:
            return (str(ast.value), BoolType())
        elif type(ast) is FloatLiteral:
            return (str(ast.value), FloatType())
        elif type(ast) is StringLiteral:
            return (str(ast.value), cgen.StringType())
            
    def emitIFTRUE(self, label, frame):
    
        frame.pop()
        return self.jvm.emitIFEQ(label)
    
    def emitIFTRUE2(self,label,frame):
    
        frame.pop()
        return self.jvm.emitIFNE(label)
        
    def emitIFFALSE(self, label, frame):

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):

        frame.pop()
        return self.jvm.emitIFICMPLT(label)
        
    def emitDUP(self, frame):

        frame.push()
        return self.jvm.emitDUP()

    def emitDUP_X2(self,frame):
    
        frame.push()
        return self.jvm.emitDUPX2()

    def emitPOP(self, frame):

        frame.pop()
        return self.jvm.emitPOP()
        
    def emitI2F(self, frame):

        return self.jvm.emitI2F()
        
    def emitRETURN(self, in_, frame):

        if type(in_) is IntType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif (type(in_) is cgen.StringType) or (type(in_) is ArrayType) or (type(in_) is cgen.ArrayPointerType) or (type(in_) is StringType):
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        elif type(in_) is cgen.ClassType:
            frame.pop()
            return self.jvm.emitARETURN()
        else:
            pass
            
    def emitLABEL(self, label, frame):

        return self.jvm.emitLABEL(label)
        
    def emitGOTO(self, label, frame):

        return self.jvm.emitGOTO(str(label))
        
    def emitPROLOG(self, name, parent):

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)
        
    def emitLIMITSTACK(self, num):

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()
        
    def printout(self, in_ ,fl=False):

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()
        
    def emitCLONE(self, type_):
        return self.jvm.INDENT + "invokevirtual " + self.getJVMType(type_) + "/clone()Ljava/lang/Object;\n"
        
    def emitCHECKCAST(self, type_):
        return self.jvm.INDENT + "checkcast " + self.getJVMType(type_) + "\n"