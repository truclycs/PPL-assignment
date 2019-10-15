import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """
        int a, b, c;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2(self):
        input = """
        int a, b[10], c;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3(self):
        input = """
        int a[10], b[10],c[10];
        """ 
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4(self):
        input = """
        void foo() {
            int a, b, c;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5(self):
        input = """
        void foo() {
            int a[10], b[10], c[10];
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6(self):

        input = """
        int x, y, z;
        void foo() {
          int a[10], b[10], c[10];
        }
        """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType()),FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_7(self):
        input = """
        int x, y, z[10];
        void foo() {
          int a[10], b[10], c[10];
        }
        """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",ArrayType(10,IntType())),FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8(self):
        input = """       
        string a;
        int b;
        float c;  
        boolean d;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",IntType()),VarDecl("c",FloatType()),VarDecl("d",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9(self):
        input = """
        string foo() {
            int a[10], b[10];
            string s;
            boolean flag;
            float f[10], fl;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],StringType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("s",StringType()),VarDecl("flag",BoolType()),VarDecl("f",ArrayType(10,FloatType())),VarDecl("fl",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_100(self):
        input = """
        int[] foo() {
            int x;
            int a, b, c, d[1000];
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("x",IntType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1000,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_10(self):
        input = """
        int[] foo() {
            int x;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("x",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """
        string s;
        boolean flag, d[100000];
        int a[18], b[2], c[1999];
        float foo() {
            float aa, bb, cc, dd[10000];
            int xx, yy, zz[10000];
            string ss, pp;
        }        
        """
        expect = str(Program([VarDecl("s",StringType()),VarDecl("flag",BoolType()),VarDecl("d",ArrayType(100000,BoolType())),VarDecl("a",ArrayType(18,IntType())),VarDecl("b",ArrayType(2,IntType())),VarDecl("c",ArrayType(1999,IntType())),FuncDecl(Id("foo"),[],FloatType(),Block([VarDecl("aa",FloatType()),VarDecl("bb",FloatType()),VarDecl("cc",FloatType()),VarDecl("dd",ArrayType(10000,FloatType())),VarDecl("xx",IntType()),VarDecl("yy",IntType()),VarDecl("zz",ArrayType(10000,IntType())),VarDecl("ss",StringType()),VarDecl("pp",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
        int main() {}
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
        int main() {
            if (a == b) c = d;
            else c = e;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),Id("d")),BinaryOp("=",Id("c"),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
        void foo(int x, int y, float z, string s, int a[]) {
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",FloatType()),VarDecl("s",StringType()),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
        int h, c, m;
        void foo(int x, int y, float z, string s, int a[]) {
            int f[100], l[999999], p[100000];
        }
        """
        expect = str(Program([VarDecl("h",IntType()),VarDecl("c",IntType()),VarDecl("m",IntType()),FuncDecl(Id("foo"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",FloatType()),VarDecl("s",StringType()),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("f",ArrayType(100,IntType())),VarDecl("l",ArrayType(999999,IntType())),VarDecl("p",ArrayType(100000,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
        void foo(int x, int y, float z, string s, int a[]) {
            x = y + c;
            a[5] = z + x;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",FloatType()),VarDecl("s",StringType()),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("y"),Id("c"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),BinaryOp("+",Id("z"),Id("x")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
        int x, y, z, d;
        float foo(int a, int b) {
            if (a == b)  
                if (a == x) 
                    b = y;
                else
                    c = z;
             else
                c = d;
        }
        """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType()),VarDecl("d",IntType()),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType())],FloatType(),Block([If(BinaryOp("==",Id("a"),Id("b")),If(BinaryOp("==",Id("a"),Id("x")),BinaryOp("=",Id("b"),Id("y")),BinaryOp("=",Id("c"),Id("z"))),BinaryOp("=",Id("c"),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """
        void foo() {}
        int main() {}
        boolean check() {}
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("check"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
        int x;
        int main() {}
        float y;
        float solve() {}
        """
        expect = str(Program([VarDecl("x",IntType()),FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("y",FloatType()),FuncDecl(Id("solve"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        input = """
        int func(int par1, float par2) {
            do a = 1; while a = 1;
            return a = 1;
        }
        void main() {}
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("par1",IntType()),VarDecl("par2",FloatType())],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1))],BinaryOp("=",Id("a"),IntLiteral(1))),Return(BinaryOp("=",Id("a"),IntLiteral(1)))])),FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """
        int func(int a) {
            do a; while a;
            return a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([Id("a")],Id("a")),Return(BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        input = """
        void foo (int i) {
            int i,j,k[5];
            // ABC XYZ
        }

        void main() {
            /*nntl*/
            int abc;
            continue;
            res(i);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("i",IntType())],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",ArrayType(5,IntType()))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("abc",IntType()),Continue(),CallExpr(Id("res"),[Id("i")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        input = """
        boolean OK(int a) {return true;} 
        """
        expect = str(Program([FuncDecl(Id("OK"),[VarDecl("a",IntType())],BoolType(),Block([Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        input = """
        boolean OK(int a) {return true; a(a);}
        """
        expect = str(Program([FuncDecl(Id("OK"),[VarDecl("a",IntType())],BoolType(),Block([Return(BooleanLiteral(True)),CallExpr(Id("a"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    # def test_25(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,325))

    # def test_26(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,326))

    # def test_27(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,327))

    # def test_28(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,328))

    # def test_29(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,329))

    # def test_30(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # def test_31(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,331))

    # def test_32(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # def test_33(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,333))

    # def test_34(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))

    # def test_35(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))

    # def test_36(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,336))

    # def test_37(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,337))

    # def test_38(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,338))

    # def test_39(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,339))

    # def test_40(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,340))

    # def test_41(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,341))

    # def test_42(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,342))

    # def test_43(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,343))

    # def test_44(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,344))

    # def test_45(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,345))

    # def test_46(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,346))

    # def test_47(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,347))

    # def test_48(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,348))

    # def test_49(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,349))

    # def test_50(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,350))

    # def test_51(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,351))

    # def test_52(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,352))

    # def test_53(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,353))

    # def test_54(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,354))

    # def test_55(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,355))

    # def test_56(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,356))

    # def test_57(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,357))

    # def test_58(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,358))

    # def test_59(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,359))

    # def test_60(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,360))

    # def test_61(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,361))

    # def test_62(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,362))

    # def test_63(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,363))

    # def test_64(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,364))

    # def test_65(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,365))

    # def test_66(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,366))

    # def test_67(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,367))

    # def test_68(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,368))

    # def test_69(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,369))

    # def test_70(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,370))

    # def test_71(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,371))

    # def test_72(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,372))

    # def test_73(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,373))

    # def test_74(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,374))

    # def test_75(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))

    # def test_76(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))

    # def test_77(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))

    # def test_78(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))

    # def test_79(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))

    # def test_80(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))

    # def test_81(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))

    # def test_82(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))

    # def test_83(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))

    # def test_84(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))

    # def test_85(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))

    # def test_86(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))

    # def test_87(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))

    # def test_88(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,388))

    # def test_89(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))

    # def test_90(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))

    # def test_91(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,391))

    # def test_92(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,392))

    # def test_93(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,393))

    # def test_94(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))

    # def test_95(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))

    # def test_96(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))

    # def test_97(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))

    # def test_98(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))

    # def test_99(self):
    #     input = """
    #     """
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))