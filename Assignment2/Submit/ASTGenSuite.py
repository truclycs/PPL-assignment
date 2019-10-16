import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """
        int a, b, c;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

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

    def test_25(self):
        input = """
        boolean OK(int a) {return true;}
        """
        expect = str(Program([FuncDecl(Id("OK"),[VarDecl("a",IntType())],BoolType(),Block([Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_26(self):
        input = """
        int foo() {
            x = 1;
            y = x + 2;
            if (a < b && b > c || d >= e || e <= f) a = e;
            else a = c;
            return foo();
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("y"),BinaryOp("+",Id("x"),IntLiteral(2))),If(BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),Id("b")),BinaryOp(">",Id("b"),Id("c"))),BinaryOp(">=",Id("d"),Id("e"))),BinaryOp("<=",Id("e"),Id("f"))),BinaryOp("=",Id("a"),Id("e")),BinaryOp("=",Id("a"),Id("c"))),Return(CallExpr(Id("foo"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_27(self):
        input = """
        boolean abc() {
            return;
            coninue;
            break;
            return 8;
        }
        """
        expect = str(Program([FuncDecl(Id("abc"),[],BoolType(),Block([Return(),Id("coninue"),Break(),Return(IntLiteral(8))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_28(self):
        input = """
        int can11 (int TL) {
            int i;
            for (i = 0; i < n; i = i + 1) TL = TL + 1;
            if (TL != oo) can11(TL);
            else break;
        }
        """
        expect = str(Program([FuncDecl(Id("can11"),[VarDecl("TL",IntType())],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("TL"),BinaryOp("+",Id("TL"),IntLiteral(1)))),If(BinaryOp("!=",Id("TL"),Id("oo")),CallExpr(Id("can11"),[Id("TL")]),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_29(self):
        input = """
        void foo () {
            int i, j, k[5];
            float arr[5];
            i = (j + i) /(j + k[arr[1]]) + 1999;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",ArrayType(5,IntType())),VarDecl("arr",ArrayType(5,FloatType())),BinaryOp("=",Id("i"),BinaryOp("+",BinaryOp("/",BinaryOp("+",Id("j"),Id("i")),BinaryOp("+",Id("j"),ArrayCell(Id("k"),ArrayCell(Id("arr"),IntLiteral(1))))),IntLiteral(1999)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_30(self):
        input = """
        int cal(int a, int b, int c) {
            a = (b + c % a /b - c * a) - e;
        }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("/",BinaryOp("%",Id("c"),Id("a")),Id("b"))),BinaryOp("*",Id("c"),Id("a"))),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_31(self):
        input = """
        /*NGUYEN THI TRUC LY*/
        // truclybk.cs@gmail.com
        int a;
        """
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_32(self):
        input = """
        int tl;
        /*NGUYEN THI TRUC LY*/// truclybk.cs@gmail.com
        """
        expect = str(Program([VarDecl("tl",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_33(self):
        input = """
        int cal(int a, int b, int c) {
            a = (b + c % a /b - c * a) - e;
            a = b = c = 10;
            res =((a * b) / d + (f % 7) - 4);
        }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("/",BinaryOp("%",Id("c"),Id("a")),Id("b"))),BinaryOp("*",Id("c"),Id("a"))),Id("e"))),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(10)))),BinaryOp("=",Id("res"),BinaryOp("-",BinaryOp("+",BinaryOp("/",BinaryOp("*",Id("a"),Id("b")),Id("d")),BinaryOp("%",Id("f"),IntLiteral(7))),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_34(self):
        input = """ 
        int cal(int a, int b, int c) {
            res = !((a * b) / d + (-f % 7 - 4));
        }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],IntType(),Block([BinaryOp("=",Id("res"),UnaryOp("!",BinaryOp("+",BinaryOp("/",BinaryOp("*",Id("a"),Id("b")),Id("d")),BinaryOp("-",BinaryOp("%",UnaryOp("-",Id("f")),IntLiteral(7)),IntLiteral(4)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_35(self):
        input = """
        int cal(int a, int b, int c) {
            res != ((a * b) / d ) && (-f % 7 - 4);
        }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],IntType(),Block([BinaryOp("&&",BinaryOp("!=",Id("res"),BinaryOp("/",BinaryOp("*",Id("a"),Id("b")),Id("d"))),BinaryOp("-",BinaryOp("%",UnaryOp("-",Id("f")),IntLiteral(7)),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_36(self):
        input = """int cal(int a) {
                        return;
                    }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_37(self):
        input = """int cal(int a) {
                        if (a) print("OK");
                    }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],IntType(),Block([If(Id("a"),CallExpr(Id("print"),[StringLiteral("OK")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_38(self):
        input = """int cal(int a) {
                        do res = 1 + 1; while 1 + 1 == 2;
                    }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([BinaryOp("=",Id("res"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))],BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_39(self):
        input = """int cal(int a) {
                        cal((a + 3) % 2 * 8);
                    }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],IntType(),Block([CallExpr(Id("cal"),[BinaryOp("*",BinaryOp("%",BinaryOp("+",Id("a"),IntLiteral(3)),IntLiteral(2)),IntLiteral(8))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_40(self):
        input = """int cal(int a) {
                        cal((a + 3) % 2 * 8 = b == c);
                    }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],IntType(),Block([CallExpr(Id("cal"),[BinaryOp("=",BinaryOp("*",BinaryOp("%",BinaryOp("+",Id("a"),IntLiteral(3)),IntLiteral(2)),IntLiteral(8)),BinaryOp("==",Id("b"),Id("c")))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_41(self):
        input = """int a[4]; 
                    void main() {
                        a[3] = 1;
                        a[2 + a[5]] = 6;
                    }
        """
        expect = str(Program([VarDecl("a",ArrayType(4,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(3)),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(5)))),IntLiteral(6))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_42(self):
        input = """ void main() {
                        i = 1;
                        foo (1 ,2);
                        i + 2;
                        100;
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),IntLiteral(1)),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("+",Id("i"),IntLiteral(2)),IntLiteral(100)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_43(self):
        input = """ void main() {
                        float a[10];
                        a[0] = 1.5;
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,FloatType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),FloatLiteral(1.5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_44(self):
        input = """int func(int a, float b){
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
                continue;
                }
                void main() {}"""
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(10)),BinaryOp("<",Id("a"),IntLiteral(20)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))),Continue()])),FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_45(self):
        input = """int main() {
                    if (h > c) x = min(p, b / 2);
                    else (h * x + c * min(f, (b - x * 2) / 2));
                    cexpect(h * min(p, (b - x * 2) / 2) + c * x);
                    return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("h"),Id("c")),BinaryOp("=",Id("x"),CallExpr(Id("min"),[Id("p"),BinaryOp("/",Id("b"),IntLiteral(2))])),BinaryOp("+",BinaryOp("*",Id("h"),Id("x")),BinaryOp("*",Id("c"),CallExpr(Id("min"),[Id("f"),BinaryOp("/",BinaryOp("-",Id("b"),BinaryOp("*",Id("x"),IntLiteral(2))),IntLiteral(2))])))),CallExpr(Id("cexpect"),[BinaryOp("+",BinaryOp("*",Id("h"),CallExpr(Id("min"),[Id("p"),BinaryOp("/",BinaryOp("-",Id("b"),BinaryOp("*",Id("x"),IntLiteral(2))),IntLiteral(2))])),BinaryOp("*",Id("c"),Id("x")))]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_46(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i) sort(x, x + n);                    
                        for (i = 0; i < n; i) {
                            if (x[i] >= s) {
                                return 0;
                            }
                        }                    
                        return 0;
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",IntType()),VarDecl("n",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),CallExpr(Id("sort"),[Id("x"),BinaryOp("+",Id("x"),Id("n"))])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),Block([If(BinaryOp(">=",ArrayCell(Id("x"),Id("i")),Id("s")),Block([Return(IntLiteral(0))]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_47(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i) sort(x, x + n);                    
                        for (i = 0; i < n; i) {
                            if (x[i] >= s) {
                                a = a + 1;
                                return 0;
                            }
                            b = b + 1;
                        }                    
                        return 0;
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",IntType()),VarDecl("n",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),CallExpr(Id("sort"),[Id("x"),BinaryOp("+",Id("x"),Id("n"))])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),Block([If(BinaryOp(">=",ArrayCell(Id("x"),Id("i")),Id("s")),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(IntLiteral(0))])),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_48(self):
        input = """int main() {
                    int n;
                    for (i = 0; i < n; i) {
                        cin(a[i]);
                    }                
                    sort(a, a + n);             
                    for (i = 0; i < n; i) {
                        if (!d[i]) {
                            res;
                            for (j = i + 1; j < n; j) {
                                if (a[j] % a[i] == 0) {
                                    d[j] = true;
                                }
                            }
                        }
                    }
                    return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),Block([CallExpr(Id("cin"),[ArrayCell(Id("a"),Id("i"))])])),CallExpr(Id("sort"),[Id("a"),BinaryOp("+",Id("a"),Id("n"))]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),Block([If(UnaryOp("!",ArrayCell(Id("d"),Id("i"))),Block([Id("res"),For(BinaryOp("=",Id("j"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("<",Id("j"),Id("n")),Id("j"),Block([If(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),Id("j")),ArrayCell(Id("a"),Id("i"))),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("d"),Id("j")),BooleanLiteral(True))]))]))]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_49(self):
        input = """  int main() {
                //  freopen("in.inp", "r", stdin);
                //    freopen("in.expect", "w", stdexpect);
                    int n, m;
                    string s;
                    for (i = 0; i < n; i) {
                        cins[i];
                    }
                    int a[10];
                    for (i = 0; i < m; i) {
                        cina[i];
                    }
                
                   /* int res = 0;
                    for (int i = 0; i < m; i++) {
                        int A = 0, B = 0, C = 0, D = 0, E = 0;
                        for (int j = 0; j < n; j++) {
                            if (s[j][i] == 'A') {
                                A++;
                            }
                            if (s[j][i] == 'B') {
                                B++;
                            }
                            if (s[j][i] == 'C') {
                                C++;
                            }
                            if (s[j][i] == 'D') {
                                D++;
                            }
                            if (s[j][i] == 'E') {
                                E++;
                            }
                        }
                        res += max(max(max(max(A, B), C), D), E) * a[i];
                    }
                
                    cexpect << res;
                    return 0;*/
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("m",IntType()),VarDecl("s",StringType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),Id("i"),Block([ArrayCell(Id("cins"),Id("i"))])),VarDecl("a",ArrayType(10,IntType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("m")),Id("i"),Block([ArrayCell(Id("cina"),Id("i"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_50(self):
        input = """  int main() {                
                    int res;
                    for (i = 0; i < m; i) {
                        int A , B, B, C, D, E;
                        for (j = 0; j < n; j) {
                            if (s[j] == A) {
                                A;
                            }
                        }
                        res = max(max(max(max(A, B), C), D), E) * a[i];
                    }
                    return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("res",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("m")),Id("i"),Block([VarDecl("A",IntType()),VarDecl("B",IntType()),VarDecl("B",IntType()),VarDecl("C",IntType()),VarDecl("D",IntType()),VarDecl("E",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),Id("j"),Block([If(BinaryOp("==",ArrayCell(Id("s"),Id("j")),Id("A")),Block([Id("A")]))])),BinaryOp("=",Id("res"),BinaryOp("*",CallExpr(Id("max"),[CallExpr(Id("max"),[CallExpr(Id("max"),[CallExpr(Id("max"),[Id("A"),Id("B")]),Id("C")]),Id("D")]),Id("E")]),ArrayCell(Id("a"),Id("i"))))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_51(self):
        input = """  int main() {                
                    if (a=b=c=d=e=f=d=f=e||1){
                        break;
                    }
                    return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",Id("d"),BinaryOp("=",Id("e"),BinaryOp("=",Id("f"),BinaryOp("=",Id("d"),BinaryOp("=",Id("f"),BinaryOp("||",Id("e"),IntLiteral(1)))))))))),Block([Break()])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_52(self):
        input = """  int main() {                
                    if (a=b=c=d=e=f=d=f=e||1){
                        break;
                    }
                    else {
                        continue;
                    }
                    return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",Id("d"),BinaryOp("=",Id("e"),BinaryOp("=",Id("f"),BinaryOp("=",Id("d"),BinaryOp("=",Id("f"),BinaryOp("||",Id("e"),IntLiteral(1)))))))))),Block([Break()]),Block([Continue()])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_53(self):
        input = """int abc, xyz;
            int f(boolean bl) {
                x = false;
                do abc = abc + 1;
                while xyz != false;
                return 0;
            }
            float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }"""
        expect = str(Program([VarDecl("abc",IntType()),VarDecl("xyz",IntType()),FuncDecl(Id("f"),[VarDecl("bl",BoolType())],IntType(),Block([BinaryOp("=",Id("x"),BooleanLiteral(False)),Dowhile([BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1)))],BinaryOp("!=",Id("xyz"),BooleanLiteral(False))),Return(IntLiteral(0))])),FuncDecl(Id("foo"),[VarDecl("x",FloatType()),VarDecl("y",FloatType())],FloatType(),Block([Id("x"),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),Id("y"))]),Id("y")])),FuncDecl(Id("check"),[],BoolType(),Block([If(BinaryOp(">",Id("a"),Id("x")),Return(Id("a")),If(BinaryOp("!=",Id("a"),IntLiteral(1)),For(BinaryOp("=",Id("a"),IntLiteral(10)),BinaryOp("<",Id("a"),IntLiteral(20)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))),For(BinaryOp("=",Id("abc"),IntLiteral(1)),BinaryOp("==",Id("xyz"),BooleanLiteral(True)),BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1))),If(BinaryOp("==",Id("abc"),IntLiteral(1)),BinaryOp("=",Id("abc"),IntLiteral(0)),Dowhile([BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1)))],BinaryOp("!=",Id("xyz"),BooleanLiteral(False)))))))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("abc",IntType()),VarDecl("x",IntType()),VarDecl("y",IntType()),For(BinaryOp("=",Id("abc"),IntLiteral(1)),BinaryOp("==",Id("xyz"),BooleanLiteral(True)),BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1))),If(BinaryOp("==",Id("abc"),IntLiteral(1)),BinaryOp("=",Id("abc"),IntLiteral(0)),Dowhile([BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1)))],BinaryOp("!=",Id("xyz"),BooleanLiteral(False))))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_54(self):
        input = """int [ ] foo ( int b [ ] ) {
                    if (ABC ) return a ;
                    else return b ;
            }
            void main() {
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([If(Id("ABC"),Return(Id("a")),Return(Id("b")))])),FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("abc"),IntLiteral(1)),BinaryOp("==",Id("xyz"),BooleanLiteral(True)),BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1))),If(BinaryOp("==",Id("abc"),IntLiteral(1)),BinaryOp("=",Id("abc"),IntLiteral(0)),Dowhile([BinaryOp("=",Id("abc"),BinaryOp("+",Id("abc"),IntLiteral(1)))],BinaryOp("!=",Id("xyz"),BooleanLiteral(False)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_55(self):
        input = """float foo(){
                i=2;
                foo(1.2);
                foo(3*4);
                100;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([BinaryOp("=",Id("i"),IntLiteral(2)),CallExpr(Id("foo"),[FloatLiteral(1.2)]),CallExpr(Id("foo"),[BinaryOp("*",IntLiteral(3),IntLiteral(4))]),IntLiteral(100)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_56(self):
        input ="""float foo(){
                return x;
            }
            float foo(){
                y = y * 13.7878;
                return y;
            }
            """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Return(Id("x"))])),FuncDecl(Id("foo"),[],FloatType(),Block([BinaryOp("=",Id("y"),BinaryOp("*",Id("y"),FloatLiteral(13.7878))),Return(Id("y"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_57(self):
        input = """float foo(){
                foo(x);
                return x;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([CallExpr(Id("foo"),[Id("x")]),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_58(self):
        input = """ int x; 
                    int foo() {
                        a[a[a[a[a[a[a]]]]]];
                    } """
        expect = str(Program([VarDecl("x",IntType()),FuncDecl(Id("foo"),[],IntType(),Block([ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),Id("a")))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_59(self):
        input = """ int foo() {
                    a[((((0.0))))];
                    } """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([ArrayCell(Id("a"),FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_60(self):
        input = """ int foo() {
                        return (-1+2*3+4/5%6)[2];
                    } """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(ArrayCell(BinaryOp("+",BinaryOp("+",UnaryOp("-",IntLiteral(1)),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("%",BinaryOp("/",IntLiteral(4),IntLiteral(5)),IntLiteral(6))),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_61(self):
        input = """int foo() {
                    a(-1+2*3+4/5%6)[2];
                    } """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([ArrayCell(CallExpr(Id("a"),[BinaryOp("+",BinaryOp("+",UnaryOp("-",IntLiteral(1)),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("%",BinaryOp("/",IntLiteral(4),IntLiteral(5)),IntLiteral(6)))]),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_62(self):
        input = """int foo() {
                    (-1+2*3+4/5%6)[2];
                    }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([ArrayCell(BinaryOp("+",BinaryOp("+",UnaryOp("-",IntLiteral(1)),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("%",BinaryOp("/",IntLiteral(4),IntLiteral(5)),IntLiteral(6))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_63(self):
        input = """int[] func() {
                        int a, b, c, x[10];
                        if (flag == true) a = x[1];
                        else break;
                        continue;
                        do (x[2] = 1); while a = b;
                        x[3] = a * b - c + d / f % g;
                        return a[1];
                        return x;
                        return;     
                }   
        """
        expect = str(Program([FuncDecl(Id("func"),[],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",ArrayType(10,IntType())),If(BinaryOp("==",Id("flag"),BooleanLiteral(True)),BinaryOp("=",Id("a"),ArrayCell(Id("x"),IntLiteral(1))),Break()),Continue(),Dowhile([BinaryOp("=",ArrayCell(Id("x"),IntLiteral(2)),IntLiteral(1))],BinaryOp("=",Id("a"),Id("b"))),BinaryOp("=",ArrayCell(Id("x"),IntLiteral(3)),BinaryOp("+",BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),Id("c")),BinaryOp("%",BinaryOp("/",Id("d"),Id("f")),Id("g")))),Return(ArrayCell(Id("a"),IntLiteral(1))),Return(Id("x")),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_64(self):
        input = """
        void kmpPreprocess(string p, int kmp[]) {
            kmp[0] = 0;
            int m;
            int j0;
            int i;
            for (i = 0; i < m; i = i + 1) {
                if (p[i] == p[j]) 
                    j = j + 1;
                    kmp[i] = j;
                    i = i + 1;
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("kmpPreprocess"),[VarDecl("p",StringType()),VarDecl("kmp",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",ArrayCell(Id("kmp"),IntLiteral(0)),IntLiteral(0)),VarDecl("m",IntType()),VarDecl("j0",IntType()),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("m")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",ArrayCell(Id("p"),Id("i")),ArrayCell(Id("p"),Id("j"))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("kmp"),Id("i")),Id("j")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_65(self):
        input = """
        void process() {
			if (i < n && p[j] != t[i]) {
				if (j != 0) {
					j = kmp[j - 1];
				}
				else {
					i = i + 1;
				}
			}
        }
        """
        expect = str(Program([FuncDecl(Id("process"),[],VoidType(),Block([If(BinaryOp("&&",BinaryOp("<",Id("i"),Id("n")),BinaryOp("!=",ArrayCell(Id("p"),Id("j")),ArrayCell(Id("t"),Id("i")))),Block([If(BinaryOp("!=",Id("j"),IntLiteral(0)),Block([BinaryOp("=",Id("j"),ArrayCell(Id("kmp"),BinaryOp("-",Id("j"),IntLiteral(1))))]),Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_66(self):
        input = """
        int main() {
            int x;
            cin(x);
            n = x % 4;
            if (n == 1) {
                cout("0 A");
            }
            else {
                cout("1 B");
            }
            if (n == 3) {
                cout ("2 A");
            }
            else {
                cout = "1 A";
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),CallExpr(Id("cin"),[Id("x")]),BinaryOp("=",Id("n"),BinaryOp("%",Id("x"),IntLiteral(4))),If(BinaryOp("==",Id("n"),IntLiteral(1)),Block([CallExpr(Id("cout"),[StringLiteral("0 A")])]),Block([CallExpr(Id("cout"),[StringLiteral("1 B")])])),If(BinaryOp("==",Id("n"),IntLiteral(3)),Block([CallExpr(Id("cout"),[StringLiteral("2 A")])]),Block([BinaryOp("=",Id("cout"),StringLiteral("1 A"))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_67(self):
        input = """
        void foo() {
            for(i = 0; i < n; i = i + 1)
			if(s[i] == "1"){
				num_rooms = 2*max(i+1, n-i);
				mx = max(mx, num_rooms);
			}
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("num_rooms"),BinaryOp("*",IntLiteral(2),CallExpr(Id("max"),[BinaryOp("+",Id("i"),IntLiteral(1)),BinaryOp("-",Id("n"),Id("i"))]))),BinaryOp("=",Id("mx"),CallExpr(Id("max"),[Id("mx"),Id("num_rooms")]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_68(self):
        input = """
        void foo() {
            for(i = 0; i < n; i = i + 1)
			if(s[i] == "1"){
				num_rooms = 2*max(i+1, n-i);
				mx = max(mx, num_rooms);
			}
        }
        void foo() {
            for(i = 0; i < n; i = i + 1)
			if(s[i] == "1"){
				num_rooms = 2*max(i+1, n-i);
				mx = max(mx, num_rooms);
			}
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("num_rooms"),BinaryOp("*",IntLiteral(2),CallExpr(Id("max"),[BinaryOp("+",Id("i"),IntLiteral(1)),BinaryOp("-",Id("n"),Id("i"))]))),BinaryOp("=",Id("mx"),CallExpr(Id("max"),[Id("mx"),Id("num_rooms")]))])))])),FuncDecl(Id("foo"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("num_rooms"),BinaryOp("*",IntLiteral(2),CallExpr(Id("max"),[BinaryOp("+",Id("i"),IntLiteral(1)),BinaryOp("-",Id("n"),Id("i"))]))),BinaryOp("=",Id("mx"),CallExpr(Id("max"),[Id("mx"),Id("num_rooms")]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_69(self):
        input = """
        int dfs(int x1,int fa) {
            int max1;
            int sum;
            for (j=0; j < l; j = j + 1){
                if(l[x1]!=fa){
                    sum = dfs(l[j],x1);
                }
            }
            if(l[x1]==1)
                return 1;
            else
                return max1;
        }
        """
        expect = str(Program([FuncDecl(Id("dfs"),[VarDecl("x1",IntType()),VarDecl("fa",IntType())],IntType(),Block([VarDecl("max1",IntType()),VarDecl("sum",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("l")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("l"),Id("x1")),Id("fa")),Block([BinaryOp("=",Id("sum"),CallExpr(Id("dfs"),[ArrayCell(Id("l"),Id("j")),Id("x1")]))]))])),If(BinaryOp("==",ArrayCell(Id("l"),Id("x1")),IntLiteral(1)),Return(IntLiteral(1)),Return(Id("max1")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_70(self):
        input = """
        int main ()  {
            int n, x1, x2, x3, x4, x5;
            scanf(n);
            if (n <= 5)
                printf ("1");
            else {
                x1 = n / 5;
                x2 = n % 5 / 4;
                x3 = n % 5 % 4 / 3;
                x4 = n % 5 % 4 % 3 / 2;
                x5 = n % 5 % 4 % 3 % 2 / 1;
                printf(x1 + x2 + x3 + x4 + x5);
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("x1",IntType()),VarDecl("x2",IntType()),VarDecl("x3",IntType()),VarDecl("x4",IntType()),VarDecl("x5",IntType()),CallExpr(Id("scanf"),[Id("n")]),If(BinaryOp("<=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("1")]),Block([BinaryOp("=",Id("x1"),BinaryOp("/",Id("n"),IntLiteral(5))),BinaryOp("=",Id("x2"),BinaryOp("/",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4))),BinaryOp("=",Id("x3"),BinaryOp("/",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3))),BinaryOp("=",Id("x4"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2))),BinaryOp("=",Id("x5"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2)),IntLiteral(1))),CallExpr(Id("printf"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x1"),Id("x2")),Id("x3")),Id("x4")),Id("x5"))])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_71(self):
        input = """
                int main ()  {
            int n, x1, x2, x3, x4, x5;
            scanf(n);
            if (n <= 5)
                printf ("1");
            else {
                x1 = n / 5;
                x2 = n % 5 / 4;
                x3 = n % 5 % 4 / 3;
                x4 = n % 5 % 4 % 3 / 2;
                x5 = n % 5 % 4 % 3 % 2 / 1;
                printf(x1 + x2 + x3 + x4 + x5);
            }
            return 0;
        }
        int main ()  {
            int n, x1, x2, x3, x4, x5;
            scanf(n);
            if (n <= 5)
                printf ("1");
            else {
                x1 = n / 5;
                x2 = n % 5 / 4;
                x3 = n % 5 % 4 / 3;
                x4 = n % 5 % 4 % 3 / 2;
                x5 = n % 5 % 4 % 3 % 2 / 1;
                printf(x1 + x2 + x3 + x4 + x5);
            }
            return 0;
        }
        int main ()  {
            int n, x1, x2, x3, x4, x5;
            scanf(n);
            if (n <= 5)
                printf ("1");
            else {
                x1 = n / 5;
                x2 = n % 5 / 4;
                x3 = n % 5 % 4 / 3;
                x4 = n % 5 % 4 % 3 / 2;
                x5 = n % 5 % 4 % 3 % 2 / 1;
                printf(x1 + x2 + x3 + x4 + x5);
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("x1",IntType()),VarDecl("x2",IntType()),VarDecl("x3",IntType()),VarDecl("x4",IntType()),VarDecl("x5",IntType()),CallExpr(Id("scanf"),[Id("n")]),If(BinaryOp("<=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("1")]),Block([BinaryOp("=",Id("x1"),BinaryOp("/",Id("n"),IntLiteral(5))),BinaryOp("=",Id("x2"),BinaryOp("/",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4))),BinaryOp("=",Id("x3"),BinaryOp("/",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3))),BinaryOp("=",Id("x4"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2))),BinaryOp("=",Id("x5"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2)),IntLiteral(1))),CallExpr(Id("printf"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x1"),Id("x2")),Id("x3")),Id("x4")),Id("x5"))])])),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("x1",IntType()),VarDecl("x2",IntType()),VarDecl("x3",IntType()),VarDecl("x4",IntType()),VarDecl("x5",IntType()),CallExpr(Id("scanf"),[Id("n")]),If(BinaryOp("<=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("1")]),Block([BinaryOp("=",Id("x1"),BinaryOp("/",Id("n"),IntLiteral(5))),BinaryOp("=",Id("x2"),BinaryOp("/",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4))),BinaryOp("=",Id("x3"),BinaryOp("/",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3))),BinaryOp("=",Id("x4"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2))),BinaryOp("=",Id("x5"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2)),IntLiteral(1))),CallExpr(Id("printf"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x1"),Id("x2")),Id("x3")),Id("x4")),Id("x5"))])])),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("x1",IntType()),VarDecl("x2",IntType()),VarDecl("x3",IntType()),VarDecl("x4",IntType()),VarDecl("x5",IntType()),CallExpr(Id("scanf"),[Id("n")]),If(BinaryOp("<=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("1")]),Block([BinaryOp("=",Id("x1"),BinaryOp("/",Id("n"),IntLiteral(5))),BinaryOp("=",Id("x2"),BinaryOp("/",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4))),BinaryOp("=",Id("x3"),BinaryOp("/",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3))),BinaryOp("=",Id("x4"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2))),BinaryOp("=",Id("x5"),BinaryOp("/",BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("n"),IntLiteral(5)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2)),IntLiteral(1))),CallExpr(Id("printf"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x1"),Id("x2")),Id("x3")),Id("x4")),Id("x5"))])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_72(self):
        input = """
        int dfs(int x1,int fa) {
            int max1;
            int sum;
            for (j=0; j < l; j = j + 1){
                if(l[x1]!=fa){
                    sum = dfs(l[j],x1);
                }
            }
            if(l[x1]==1)
                return 1;
            else
                return max1;
            int max1;
            int sum;
            for (j=0; j < l; j = j + 1){
                if(l[x1]!=fa){
                    sum = dfs(l[j],x1);
                }
            }
            if(l[x1]==1)
                return 1;
            else
                return max1;
            int max1;
            int sum;
            for (j=0; j < l; j = j + 1){
                if(l[x1]!=fa){
                    sum = dfs(l[j],x1);
                }
            }
            if(l[x1]==1)
                return 1;
            else
                return max1;
        }
        """
        expect = str(Program([FuncDecl(Id("dfs"),[VarDecl("x1",IntType()),VarDecl("fa",IntType())],IntType(),Block([VarDecl("max1",IntType()),VarDecl("sum",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("l")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("l"),Id("x1")),Id("fa")),Block([BinaryOp("=",Id("sum"),CallExpr(Id("dfs"),[ArrayCell(Id("l"),Id("j")),Id("x1")]))]))])),If(BinaryOp("==",ArrayCell(Id("l"),Id("x1")),IntLiteral(1)),Return(IntLiteral(1)),Return(Id("max1"))),VarDecl("max1",IntType()),VarDecl("sum",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("l")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("l"),Id("x1")),Id("fa")),Block([BinaryOp("=",Id("sum"),CallExpr(Id("dfs"),[ArrayCell(Id("l"),Id("j")),Id("x1")]))]))])),If(BinaryOp("==",ArrayCell(Id("l"),Id("x1")),IntLiteral(1)),Return(IntLiteral(1)),Return(Id("max1"))),VarDecl("max1",IntType()),VarDecl("sum",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("l")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("l"),Id("x1")),Id("fa")),Block([BinaryOp("=",Id("sum"),CallExpr(Id("dfs"),[ArrayCell(Id("l"),Id("j")),Id("x1")]))]))])),If(BinaryOp("==",ArrayCell(Id("l"),Id("x1")),IntLiteral(1)),Return(IntLiteral(1)),Return(Id("max1")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_73(self):
        input = """
        int lca(int u, int v) {
            // Root node at lvl 0 and lvls increase towards leaf.
            if (lvl[v] > lvl[u]) swap(u, v);
            res = 0;
            for (i = logLvl; i >= 0; i = i-1) {
                if (lvl) {
                    if (res < weights[u]) res = weights;
                    u = parent[u];
                }
            }
            if (lvl[v] != lvl[u]) printf("Something is wrong.");
            if (v == u) return res;
            for (i = logLvl; i >= 0; i - 1) {
                if (parent[v] != parent[i]) {
                    res = max(weights[u], res);
                    res = max(weights[v], res);
                    u = parent[u];
                    v = parent[v];
                }        
            }
            res = max(weights[u], res);
            res = max(weights[v], res);
            return res;
        }
            """
        expect = str(Program([FuncDecl(Id("lca"),[VarDecl("u",IntType()),VarDecl("v",IntType())],IntType(),Block([If(BinaryOp(">",ArrayCell(Id("lvl"),Id("v")),ArrayCell(Id("lvl"),Id("u"))),CallExpr(Id("swap"),[Id("u"),Id("v")])),BinaryOp("=",Id("res"),IntLiteral(0)),For(BinaryOp("=",Id("i"),Id("logLvl")),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Block([If(Id("lvl"),Block([If(BinaryOp("<",Id("res"),ArrayCell(Id("weights"),Id("u"))),BinaryOp("=",Id("res"),Id("weights"))),BinaryOp("=",Id("u"),ArrayCell(Id("parent"),Id("u")))]))])),If(BinaryOp("!=",ArrayCell(Id("lvl"),Id("v")),ArrayCell(Id("lvl"),Id("u"))),CallExpr(Id("printf"),[StringLiteral("Something is wrong.")])),If(BinaryOp("==",Id("v"),Id("u")),Return(Id("res"))),For(BinaryOp("=",Id("i"),Id("logLvl")),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("-",Id("i"),IntLiteral(1)),Block([If(BinaryOp("!=",ArrayCell(Id("parent"),Id("v")),ArrayCell(Id("parent"),Id("i"))),Block([BinaryOp("=",Id("res"),CallExpr(Id("max"),[ArrayCell(Id("weights"),Id("u")),Id("res")])),BinaryOp("=",Id("res"),CallExpr(Id("max"),[ArrayCell(Id("weights"),Id("v")),Id("res")])),BinaryOp("=",Id("u"),ArrayCell(Id("parent"),Id("u"))),BinaryOp("=",Id("v"),ArrayCell(Id("parent"),Id("v")))]))])),BinaryOp("=",Id("res"),CallExpr(Id("max"),[ArrayCell(Id("weights"),Id("u")),Id("res")])),BinaryOp("=",Id("res"),CallExpr(Id("max"),[ArrayCell(Id("weights"),Id("v")),Id("res")])),Return(Id("res"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_74(self):
        input = """
        int main(){
        cnt = 0;
		for (i = 0; i < 200; i + 1)
		{
			if (ind[i] != -1)
			{
				//cout << ind[i] << ' ';
				cnt = cnt + 1;
			}
			if (cnt == k)
				break;
		}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("cnt"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(200)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("!=",ArrayCell(Id("ind"),Id("i")),UnaryOp("-",IntLiteral(1))),Block([BinaryOp("=",Id("cnt"),BinaryOp("+",Id("cnt"),IntLiteral(1)))])),If(BinaryOp("==",Id("cnt"),Id("k")),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_75(self):
        input = """
        int main() {
            int n,k;
            //cin>>n>>k;
        
            //vector<int> v(n,0);
            count=0;
        
            for(i=0;i<n;i+1) {
                //cin>>v[i];
                    if(i<=k-1&&v[i]!=0)
                        count = count+1;        
                    else
                    {
                        if(i>k-1&& v[i]==v[k-1]&&v[i]!=0)
                            count = ct;
                    }
            }
                //cout<<count<<endl;        
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("&&",BinaryOp("<=",Id("i"),BinaryOp("-",Id("k"),IntLiteral(1))),BinaryOp("!=",ArrayCell(Id("v"),Id("i")),IntLiteral(0))),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))),Block([If(BinaryOp("&&",BinaryOp("&&",BinaryOp(">",Id("i"),BinaryOp("-",Id("k"),IntLiteral(1))),BinaryOp("==",ArrayCell(Id("v"),Id("i")),ArrayCell(Id("v"),BinaryOp("-",Id("k"),IntLiteral(1))))),BinaryOp("!=",ArrayCell(Id("v"),Id("i")),IntLiteral(0))),BinaryOp("=",Id("count"),Id("ct")))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_76(self):
        input = """
        int gcd(int a, int b) 
        { 
            if (a == 0) 
                return b; 
            return gcd(b % a, a); 
        } 
        """
        expect = str(Program([FuncDecl(Id("gcd"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Return(Id("b"))),Return(CallExpr(Id("gcd"),[BinaryOp("%",Id("b"),Id("a")),Id("a")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_77(self):
        input = """ 
        void solve()
        {
            //cin >> m;
            if (m == 1)
            {
              //  cout << 1;
                return ;
            }
            for (i = 1; i < n; i+1)
            {
                x = (i * (i + 1)) / 2;
        
                if (x >= m)
                {
                    j = i - 1;
                    x = (j * (j + 1)) / 2;
               //     cout << m - x;
                    return ;
                }
            }
        
        }
        """
        expect = str(Program([FuncDecl(Id("solve"),[],VoidType(),Block([If(BinaryOp("==",Id("m"),IntLiteral(1)),Block([Return()])),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("x"),BinaryOp("/",BinaryOp("*",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),IntLiteral(2))),If(BinaryOp(">=",Id("x"),Id("m")),Block([BinaryOp("=",Id("j"),BinaryOp("-",Id("i"),IntLiteral(1))),BinaryOp("=",Id("x"),BinaryOp("/",BinaryOp("*",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),IntLiteral(2))),Return()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_78(self):
        input = """
        int main() {
            for(i=1;i<=n;i+1) {
                if(!vis[i])
                {
                    ans[i]=1;
                    temp+1;
                    for(j=0;j<size;j+1)
                    {
                        //vis[v[i][j]]=true;
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(UnaryOp("!",ArrayCell(Id("vis"),Id("i"))),Block([BinaryOp("=",ArrayCell(Id("ans"),Id("i")),IntLiteral(1)),BinaryOp("+",Id("temp"),IntLiteral(1)),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("size")),BinaryOp("+",Id("j"),IntLiteral(1)),Block([]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_79(self):
        input = """
        int main() {
            // your code goes here
            int m,n;
            mul=m*n;
            tot=mul/2;
            //cout<<tot;
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("m",IntType()),VarDecl("n",IntType()),BinaryOp("=",Id("mul"),BinaryOp("*",Id("m"),Id("n"))),BinaryOp("=",Id("tot"),BinaryOp("/",Id("mul"),IntLiteral(2))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_80(self):
        input = """
        int main()
        {
            int n,m;//cin>>n>>m;
            day=1;
            nextDay=m;
            for(i=1;i<10000;i+1){
                n-1;
                if(i==nextDay)
                {
                    n+1;
                    day+1;
                    nextDay=m*day;
        
                }
                if(n==0)
                {
                    //cout<<i;
                    break;
                }
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("m",IntType()),BinaryOp("=",Id("day"),IntLiteral(1)),BinaryOp("=",Id("nextDay"),Id("m")),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10000)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("-",Id("n"),IntLiteral(1)),If(BinaryOp("==",Id("i"),Id("nextDay")),Block([BinaryOp("+",Id("n"),IntLiteral(1)),BinaryOp("+",Id("day"),IntLiteral(1)),BinaryOp("=",Id("nextDay"),BinaryOp("*",Id("m"),Id("day")))])),If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([Break()]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_81(self):
        input = """
        int max(string floor, int it)
        {
            if (it > (floorsize() - it))
            {
                return (it + 1) * 2;
            }
            else
            {
                return (floorsize() - it) * 2;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("max"),[VarDecl("floor",StringType()),VarDecl("it",IntType())],IntType(),Block([If(BinaryOp(">",Id("it"),BinaryOp("-",CallExpr(Id("floorsize"),[]),Id("it"))),Block([Return(BinaryOp("*",BinaryOp("+",Id("it"),IntLiteral(1)),IntLiteral(2)))]),Block([Return(BinaryOp("*",BinaryOp("-",CallExpr(Id("floorsize"),[]),Id("it")),IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_82(self):
        input = """
        void foo() {
            if (it_first == it_last)
                    {
                        if ((it_first + 1) > (floorsize() - it_first))
                        {
                            cout =(it_first + 1) * 2;
                        }
                        else
                        {
                            cout =(floorsize() - it_first) * 2;
                        }
                    }
                    else
                    {
                        int max1, max2;
                        max1 = max(floor, it_first);
                        max2 = max(floor, it_last);
            
                        if (max1 >= max2)
                        {
                            cout = max1 = endl;
                        }
                        else
                        {
                            cout = max2 = endl;
                        }        
                    }
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("==",Id("it_first"),Id("it_last")),Block([If(BinaryOp(">",BinaryOp("+",Id("it_first"),IntLiteral(1)),BinaryOp("-",CallExpr(Id("floorsize"),[]),Id("it_first"))),Block([BinaryOp("=",Id("cout"),BinaryOp("*",BinaryOp("+",Id("it_first"),IntLiteral(1)),IntLiteral(2)))]),Block([BinaryOp("=",Id("cout"),BinaryOp("*",BinaryOp("-",CallExpr(Id("floorsize"),[]),Id("it_first")),IntLiteral(2)))]))]),Block([VarDecl("max1",IntType()),VarDecl("max2",IntType()),BinaryOp("=",Id("max1"),CallExpr(Id("max"),[Id("floor"),Id("it_first")])),BinaryOp("=",Id("max2"),CallExpr(Id("max"),[Id("floor"),Id("it_last")])),If(BinaryOp(">=",Id("max1"),Id("max2")),Block([BinaryOp("=",Id("cout"),BinaryOp("=",Id("max1"),Id("endl")))]),Block([BinaryOp("=",Id("cout"),BinaryOp("=",Id("max2"),Id("endl")))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_83(self):
        input = """
        int main(){
            "ios_base::sync_with_stdio(false);";
            "cin.tie(0);";
            "cout.tie(0);"  ;          
            int n; //cin >> n;            
            //vector<int> a(n);
            for(i = 0; i < n; i + 1) { cin = a[i];}
            
            //vector<int> ms(n, 1e9 + 7);
            ms[n - 1] = a[n - 1];
            
            for(i = n - 2; i >= 0; i-1){
                if(ms[i + 1] < a[i]) ms[i] = ms[i + 1];
                else ms[i] = a[i];
            }
            
            //for(int i = 0; i < n; i++) cout << ms[i] << " ";
            //cout << endl << endl;            
            for(i = 0; i < n; i+1){
                //vector<int>::iterator it = lower_bound(ms.begin() , ms.end(), a[i]);                
                if(it == msbegin()){
                  //  "cout << -1 << " ";"
                    continue;
                }          
                
                ind = it - msbegin();
                
                if(ind < i){
                    //cout << -1 << " ";
                    continue;
                }
                //else cout << ind - i - 1 << " ";
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([StringLiteral("ios_base::sync_with_stdio(false);"),StringLiteral("cin.tie(0);"),StringLiteral("cout.tie(0);"),VarDecl("n",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("cin"),ArrayCell(Id("a"),Id("i")))])),BinaryOp("=",ArrayCell(Id("ms"),BinaryOp("-",Id("n"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("-",Id("n"),IntLiteral(1)))),For(BinaryOp("=",Id("i"),BinaryOp("-",Id("n"),IntLiteral(2))),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("-",Id("i"),IntLiteral(1)),Block([If(BinaryOp("<",ArrayCell(Id("ms"),BinaryOp("+",Id("i"),IntLiteral(1))),ArrayCell(Id("a"),Id("i"))),BinaryOp("=",ArrayCell(Id("ms"),Id("i")),ArrayCell(Id("ms"),BinaryOp("+",Id("i"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("ms"),Id("i")),ArrayCell(Id("a"),Id("i"))))])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",Id("it"),CallExpr(Id("msbegin"),[])),Block([Continue()])),BinaryOp("=",Id("ind"),BinaryOp("-",Id("it"),CallExpr(Id("msbegin"),[]))),If(BinaryOp("<",Id("ind"),Id("i")),Block([Continue()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_84(self):
        input = """
        int main() {
        int n,i,j,k; pos1=0;pos=-1;
        cin  = n;
        string s;
        sclear();
        for(i=0;i<n;i+1)
        {
            if(s[i]=="1" && pos==-1)
            {
                pos=i;
                pos1=i;
            }
            if(s[i]=="1")
            {
                pos1=i;
            }
        }
       // cout<<pos<<" --"<<pos1<<endl;
        if(pos1==0 && pos==-1)
        {
            "cout<<n<<endl;";
        }
        else if(pos==pos1)
        {
            k=max(pos+1,n-pos);
            //cout<<2*k<<endl;
        }
        else
        {
            cout==max(2*(pos1+1),2*(n-pos));
        }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("pos1"),IntLiteral(0)),BinaryOp("=",Id("pos"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("cin"),Id("n")),VarDecl("s",StringType()),CallExpr(Id("sclear"),[]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),BinaryOp("==",Id("pos"),UnaryOp("-",IntLiteral(1)))),Block([BinaryOp("=",Id("pos"),Id("i")),BinaryOp("=",Id("pos1"),Id("i"))])),If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("pos1"),Id("i"))]))])),If(BinaryOp("&&",BinaryOp("==",Id("pos1"),IntLiteral(0)),BinaryOp("==",Id("pos"),UnaryOp("-",IntLiteral(1)))),Block([StringLiteral("cout<<n<<endl;")]),If(BinaryOp("==",Id("pos"),Id("pos1")),Block([BinaryOp("=",Id("k"),CallExpr(Id("max"),[BinaryOp("+",Id("pos"),IntLiteral(1)),BinaryOp("-",Id("n"),Id("pos"))]))]),Block([BinaryOp("==",Id("cout"),CallExpr(Id("max"),[BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("pos1"),IntLiteral(1))),BinaryOp("*",IntLiteral(2),BinaryOp("-",Id("n"),Id("pos")))]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_85(self):
        input = """
        void foo() {
            {{{{}}}}
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Block([Block([Block([Block([])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_86(self):
        input = """
        int main() {
            int n;
            printf(n);
            {{{{{{{{{{{{{}}}}}}}}}}}}}
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[Id("n")]),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])])])])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_87(self):
        input = """
        int NOP,h,PH;
        int main()
        {cin=NOP;
        cin=h;
        w=0;
        for(i=0;i!=NOP;i+1)
        {cin=PH;
        if (PH>h)
        {
            w=w+2;
        }
        else
            w=w+1;
        }
        cout=w;
            return 0;
        }
        """
        expect = str(Program([VarDecl("NOP",IntType()),VarDecl("h",IntType()),VarDecl("PH",IntType()),FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("cin"),Id("NOP")),BinaryOp("=",Id("cin"),Id("h")),BinaryOp("=",Id("w"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("!=",Id("i"),Id("NOP")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("cin"),Id("PH")),If(BinaryOp(">",Id("PH"),Id("h")),Block([BinaryOp("=",Id("w"),BinaryOp("+",Id("w"),IntLiteral(2)))]),BinaryOp("=",Id("w"),BinaryOp("+",Id("w"),IntLiteral(1))))])),BinaryOp("=",Id("cout"),Id("w")),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_88(self):
        input = """
        int string_sum(string s)
        {
            int b;
            b = 0;
            int k;
            k =ssize();
                for(j=0; j<k; j = j + 1)
                {
                    b = b + (s[j]-48);
                }
            return b;
        }
        """
        expect = str(Program([FuncDecl(Id("string_sum"),[VarDecl("s",StringType())],IntType(),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),IntLiteral(0)),VarDecl("k",IntType()),BinaryOp("=",Id("k"),CallExpr(Id("ssize"),[])),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("k")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),BinaryOp("-",ArrayCell(Id("s"),Id("j")),IntLiteral(48))))])),Return(Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_89(self):
        input = """
        void solve() {
                int a;
                a = 0;
                for(i=0; i<=1200050; i+1)
                {
                // cout << 19+9*i <<" ";
                    a = ((19+9*i));
                    
                    if(string_sum(to_string(a))==10)b+1;
                    if(b==n){
                        cout = a = endl;
                        break;
                    }                    
                }
            }
                    """
        expect = str(Program([FuncDecl(Id("solve"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(1200050)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(19),BinaryOp("*",IntLiteral(9),Id("i")))),If(BinaryOp("==",CallExpr(Id("string_sum"),[CallExpr(Id("to_string"),[Id("a")])]),IntLiteral(10)),BinaryOp("+",Id("b"),IntLiteral(1))),If(BinaryOp("==",Id("b"),Id("n")),Block([BinaryOp("=",Id("cout"),BinaryOp("=",Id("a"),Id("endl"))),Break()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_90(self):
        input = """
        boolean isPrime(int n) {
            if (i < 2) {
                return false;
            }
            for (i = 2; i <= sqrtm; i = i + 1) {
                return false;
            }
            return true;
        }

        int main() {
            int n;
            n = 10;
            if (isPrime(n) == true) {
                n = 1934823904;
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("isPrime"),[VarDecl("n",IntType())],BoolType(),Block([If(BinaryOp("<",Id("i"),IntLiteral(2)),Block([Return(BooleanLiteral(False))])),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),Id("sqrtm")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(BooleanLiteral(False))])),Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("n"),IntLiteral(10)),If(BinaryOp("==",CallExpr(Id("isPrime"),[Id("n")]),BooleanLiteral(True)),Block([BinaryOp("=",Id("n"),IntLiteral(1934823904))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_91(self):
        input = """
        int solution(){
            int n,q1;
            "cin>>n>>q1";
            int a[10],c[200005],d[200005];
            
               if(c[a[i]]==0)
                {
                    c[a[i]]=i+1;
                }

                if(c[a[i]]==i+1)
                {
                    vpb(d[a[i]],c[a[i]],m[a[i]]);
                }      
            ans=0;
            sort(all(v));
            g=sz(v);
            b=-1;temp=0;
                j=g-i-1;
                //cnt=v[j].S.S,f=v[j].S.F,s=v[j].F;
            
                if(s<b)
                {        
                    ans=temp;
                    b=f;
                    temp=cnt;
                    if(s-f+1==cnt)
                    {
                        ans=cnt;
                        temp=0;
                        b=-1;
                    }        
                }
                else
                {
                    b=min(f,b);
                    temp=max(temp,cnt);
                    if(j==0)
                    {
                        ans=temp;
                    }
                }
        //    cout<<n-ans;
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("solution"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("q1",IntType()),StringLiteral("cin>>n>>q1"),VarDecl("a",ArrayType(10,IntType())),VarDecl("c",ArrayType(200005,IntType())),VarDecl("d",ArrayType(200005,IntType())),If(BinaryOp("==",ArrayCell(Id("c"),ArrayCell(Id("a"),Id("i"))),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("c"),ArrayCell(Id("a"),Id("i"))),BinaryOp("+",Id("i"),IntLiteral(1)))])),If(BinaryOp("==",ArrayCell(Id("c"),ArrayCell(Id("a"),Id("i"))),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("vpb"),[ArrayCell(Id("d"),ArrayCell(Id("a"),Id("i"))),ArrayCell(Id("c"),ArrayCell(Id("a"),Id("i"))),ArrayCell(Id("m"),ArrayCell(Id("a"),Id("i")))])])),BinaryOp("=",Id("ans"),IntLiteral(0)),CallExpr(Id("sort"),[CallExpr(Id("all"),[Id("v")])]),BinaryOp("=",Id("g"),CallExpr(Id("sz"),[Id("v")])),BinaryOp("=",Id("b"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("temp"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("-",BinaryOp("-",Id("g"),Id("i")),IntLiteral(1))),If(BinaryOp("<",Id("s"),Id("b")),Block([BinaryOp("=",Id("ans"),Id("temp")),BinaryOp("=",Id("b"),Id("f")),BinaryOp("=",Id("temp"),Id("cnt")),If(BinaryOp("==",BinaryOp("+",BinaryOp("-",Id("s"),Id("f")),IntLiteral(1)),Id("cnt")),Block([BinaryOp("=",Id("ans"),Id("cnt")),BinaryOp("=",Id("temp"),IntLiteral(0)),BinaryOp("=",Id("b"),UnaryOp("-",IntLiteral(1)))]))]),Block([BinaryOp("=",Id("b"),CallExpr(Id("min"),[Id("f"),Id("b")])),BinaryOp("=",Id("temp"),CallExpr(Id("max"),[Id("temp"),Id("cnt")])),If(BinaryOp("==",Id("j"),IntLiteral(0)),Block([BinaryOp("=",Id("ans"),Id("temp"))]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_92(self):
        input = """
        void zzz(int zzz) {
            for(i=0;i<n-1;i+1)
            {
                for(j = i+1;j<n;j+1)
                {
                    if(a[i]>a[j])
                    {
                        temp=a[i];
                        a[i] = a[j];
                        a[j] = temp;
                    }
                }
            }
            }
        """
        expect = str(Program([FuncDecl(Id("zzz"),[VarDecl("zzz",IntType())],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("+",Id("i"),IntLiteral(1)),Block([For(BinaryOp("=",Id("j"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("<",Id("j"),Id("n")),BinaryOp("+",Id("j"),IntLiteral(1)),Block([If(BinaryOp(">",ArrayCell(Id("a"),Id("i")),ArrayCell(Id("a"),Id("j"))),Block([BinaryOp("=",Id("temp"),ArrayCell(Id("a"),Id("i"))),BinaryOp("=",ArrayCell(Id("a"),Id("i")),ArrayCell(Id("a"),Id("j"))),BinaryOp("=",ArrayCell(Id("a"),Id("j")),Id("temp"))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_93(self):
        input = """
        void func(int a, int b[]){
            float d[4], c[5];{string c[5];}
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("d",ArrayType(4,FloatType())),VarDecl("c",ArrayType(5,FloatType())),Block([VarDecl("c",ArrayType(5,StringType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_94(self):
        input = """
        int main(){
        // ios_base::sync_with_stdio(false),cin.tie(0);
        int prefix[305];
        int ar[305];
            string s;
            //cin>>s;
            mx = 0;
            for(i = 0;i<slength;i+1){
                if(s[i] == "+"){
                    ar[i] = 1;
                } else {
                    ar[i] = -1;
                }
            }
            sum = 0;
            prefix[0] = 0;
            for(i = 0;i<slength;i+1){
                sum= ar[i];
                prefix[i+1] = sum;
            }
        
            for(i = 0;i<slength + 1;i+1){
                for(j = i+1;j<slength1;j+1){
                        mx = max(abs(prefix[j]-prefix[i]),mx);
                }
            }
            //cout<<mx<<;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("prefix",ArrayType(305,IntType())),VarDecl("ar",ArrayType(305,IntType())),VarDecl("s",StringType()),BinaryOp("=",Id("mx"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("slength")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("+")),Block([BinaryOp("=",ArrayCell(Id("ar"),Id("i")),IntLiteral(1))]),Block([BinaryOp("=",ArrayCell(Id("ar"),Id("i")),UnaryOp("-",IntLiteral(1)))]))])),BinaryOp("=",Id("sum"),IntLiteral(0)),BinaryOp("=",ArrayCell(Id("prefix"),IntLiteral(0)),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("slength")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("sum"),ArrayCell(Id("ar"),Id("i"))),BinaryOp("=",ArrayCell(Id("prefix"),BinaryOp("+",Id("i"),IntLiteral(1))),Id("sum"))])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("+",Id("slength"),IntLiteral(1))),BinaryOp("+",Id("i"),IntLiteral(1)),Block([For(BinaryOp("=",Id("j"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("<",Id("j"),Id("slength1")),BinaryOp("+",Id("j"),IntLiteral(1)),Block([BinaryOp("=",Id("mx"),CallExpr(Id("max"),[CallExpr(Id("abs"),[BinaryOp("-",ArrayCell(Id("prefix"),Id("j")),ArrayCell(Id("prefix"),Id("i")))]),Id("mx")]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_95(self):
        input = """
        int main(){
            do{
                abc = 456;
                if (x || y || z) return 0;
                else if (1 + 2 + 3 == m) return 0;
            } while (flag = true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("abc"),IntLiteral(456)),If(BinaryOp("||",BinaryOp("||",Id("x"),Id("y")),Id("z")),Return(IntLiteral(0)),If(BinaryOp("==",BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Id("m")),Return(IntLiteral(0))))])],BinaryOp("=",Id("flag"),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_96(self):
        input = """
        void print(string s) {
            s = "zzzzzzzzzzzzzzzzzzzz";
            "zzzzzzzzzzzzZZZZZZZZZZZZZZ";
        }
        """
        expect = str(Program([FuncDecl(Id("print"),[VarDecl("s",StringType())],VoidType(),Block([BinaryOp("=",Id("s"),StringLiteral("zzzzzzzzzzzzzzzzzzzz")),StringLiteral("zzzzzzzzzzzzZZZZZZZZZZZZZZ")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_97(self):
        input = """
        string getTime() {
            return "1:10AM - 16-10-2019";
        }
        """
        expect = str(Program([FuncDecl(Id("getTime"),[],StringType(),Block([Return(StringLiteral("1:10AM - 16-10-2019"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_98(self):
        input = """
        int main(){
            "ios_base::sync_with_stdio(false)";
            "cin.tie(NULL)";
            "cout.tie(NULL)";
            int t;
            //cin>>t;
            int n;
            for (T = 0; T < t; T = T + 1)
            {
                //cin>>n;
                string s;
                //cin>>s;
                //ll left=-1,right=-1;
                for(i=0;i<n;i+1)
                {
                    if(s[i]=="1")
                    {
                        left=i;
                        break;	
                    }
                }
                for(i=n-1;i>=0;i-1)
                {
                    if(s[i]=="1")
                    {
                        right=i;
                        break;
                    }
                }
                maxm=n;
                if(left!=-1 && right!=-1) 
                {
                    temp=max(right+1,n-left);
                    maxm=max(maxm,2*temp);
                }
                //cout<<maxm<<endl;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([StringLiteral("ios_base::sync_with_stdio(false)"),StringLiteral("cin.tie(NULL)"),StringLiteral("cout.tie(NULL)"),VarDecl("t",IntType()),VarDecl("n",IntType()),For(BinaryOp("=",Id("T"),IntLiteral(0)),BinaryOp("<",Id("T"),Id("t")),BinaryOp("=",Id("T"),BinaryOp("+",Id("T"),IntLiteral(1))),Block([VarDecl("s",StringType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("left"),Id("i")),Break()]))])),For(BinaryOp("=",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("-",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",ArrayCell(Id("s"),Id("i")),StringLiteral("1")),Block([BinaryOp("=",Id("right"),Id("i")),Break()]))])),BinaryOp("=",Id("maxm"),Id("n")),If(BinaryOp("&&",BinaryOp("!=",Id("left"),UnaryOp("-",IntLiteral(1))),BinaryOp("!=",Id("right"),UnaryOp("-",IntLiteral(1)))),Block([BinaryOp("=",Id("temp"),CallExpr(Id("max"),[BinaryOp("+",Id("right"),IntLiteral(1)),BinaryOp("-",Id("n"),Id("left"))])),BinaryOp("=",Id("maxm"),CallExpr(Id("max"),[Id("maxm"),BinaryOp("*",IntLiteral(2),Id("temp"))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_99(self):
        input = """void funcEnd() {print("END!");}"""
        expect = str(Program([FuncDecl(Id("funcEnd"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("END!")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
