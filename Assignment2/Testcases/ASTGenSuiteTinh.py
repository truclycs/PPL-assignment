import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_var_decl_1(self):        
        input = """int a,b[10];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_decl_2(self):        
        input = """int a,b,c,d,e[10];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl_3(self):        
        input = """
        int a;
        float b;
        string c;
        boolean d;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl_4(self):        
        input = """
        int a[10];
        float b,c[5];
        string d[10];
        """
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",FloatType()),VarDecl("c",ArrayType(5,FloatType())),VarDecl("d",ArrayType(10,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_func_decl_1(self):        
        input = """int foo() {}"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_decl_2(self):        
        input = """int foo(int a, float b) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_func_decl_3(self):        
        input = """int foo(int a, float b[]) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_func_decl_4(self):        
        input = """int[] foo(int a, float b) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_func_decl_5(self):        
        input = """int[] foo(int a, float b[]) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_func_decl_6(self):        
        input = """int foo(int a, float b) {
            int c,d;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_func_decl_7(self):        
        input = """int foo(int a, float b) {
            int c[5];
            float d;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([VarDecl("c",ArrayType(5,IntType())),VarDecl("d",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_func_decl_8(self):        
        input = """int foo(int a, float b) {
            return;
            break;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([Return(),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_func_decl_9(self):        
        input = """int foo(int a, float b) {
            a = b;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_func_decl_10(self):        
        input = """int foo(int a, float b) {
            return a + b;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_func_decl_11(self):
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_func_decl_12(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_func_decl_13(self):
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_func_decl_14(self):
        input = """
            int[] foo(int a, float b[]) {
                int c[3];
                if (a>0) foo(a-1,b);
                return c; 
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_func_decl_15(self):        
        input = """
            int main()
            {
                // printf() displays the string inside quotation
                printf("Hello, World!");
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Hello, World!")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_func_decl_16(self):        
        input = """
            int main() {
            boolean boo[2];
            boo[1] = true;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("boo",ArrayType(2,BoolType())),BinaryOp("=",ArrayCell(Id("boo"),IntLiteral(1)),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_decl_17(self):        
        input = """
            int foo (int a , float b[])
        {
            boolean c ;
            int i ;
            i = a + 3 ;
            if (i > 0) {
                int d ;
                d = i + 3 ;
                putInt(d) ;
            }
            return i ;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_func_decl_18(self):        
        input = """
            string name() {
                return "name";
            }
        """
        expect = str(Program([FuncDecl(Id("name"),[],StringType(),Block([Return(StringLiteral("name"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_func_decl_19(self):        
        input = """
            boolean isFalse(boolean a) {
                if (a == true) {return false;}
            }
        """
        expect = str(Program([FuncDecl(Id("isFalse"),[VarDecl("a",BoolType())],BoolType(),Block([If(BinaryOp("==",Id("a"),BooleanLiteral(True)),Block([Return(BooleanLiteral(False))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_decl_20(self):        
        input = """
            float[] add(float a, float b[]) {
                for (i = 0; i >= 0; i = i + 1) {
                    b[i] = a + b[i];
                }
                return b;
            }
        """
        expect = str(Program([FuncDecl(Id("add"),[VarDecl("a",FloatType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("b"),Id("i")),BinaryOp("+",Id("a"),ArrayCell(Id("b"),Id("i"))))])),Return(Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_func_decl_21(self):        
        input = """
            string[] school(string a, string b, string c) {}
        """
        expect = str(Program([FuncDecl(Id("school"),[VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_expression_1(self):        
        input = """
            int main() {
            a = !b + -a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",UnaryOp("!",Id("b")),UnaryOp("-",Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_expression_2(self):        
        input = """
            int main() {
            a = b / c % d * e;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("*",BinaryOp("%",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_expression_3(self):        
        input = """
             int main() {
            a = b + c - -d * e[a];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",UnaryOp("-",Id("d")),ArrayCell(Id("e"),Id("a")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_expression_4(self):        
        input = """
            int main() {
            a = b < (c > d);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("<",Id("b"),BinaryOp(">",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_expression_5(self):        
        input = """
            int main() {
            a = b < c + d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("<",Id("b"),BinaryOp("+",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_expression_6(self):        
        input = """
            int main() {
            a = b < c == d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("<",Id("b"),Id("c")),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_expression_7(self):        
        input = """
            int main() {
            a = b && c == d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("&&",Id("b"),BinaryOp("==",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_expression_8(self):        
        input = """
            int main() {
            a = b || c && d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("||",Id("b"),BinaryOp("&&",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_expression_9(self):        
        input = """
        int main() {
            a = b+c*d/e-f<g==h;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("<",BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("/",BinaryOp("*",Id("c"),Id("d")),Id("e"))),Id("f")),Id("g")),Id("h")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_expression_10(self):        
        input = """
            int main() {
            12 = 5 * 9 / 10 + 15 % 8 && 1 < 10;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",IntLiteral(12),BinaryOp("&&",BinaryOp("+",BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(9)),IntLiteral(10)),BinaryOp("%",IntLiteral(15),IntLiteral(8))),BinaryOp("<",IntLiteral(1),IntLiteral(10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_expression_11(self):        
        input = """
            int main() {
            a = b + foo(5) - (foo() % 1);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),CallExpr(Id("foo"),[IntLiteral(5)])),BinaryOp("%",CallExpr(Id("foo"),[]),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_expression_12(self):        
        input = """
            int main() {
            foo(2)[3+x] = a[b[2]] +3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_expression_13(self):        
        input = """
        void foo (float a[]) {}
        void goo (float x[]) {
            float y[10];
            int z[10];
            foo(x); 
            foo(y); 
            foo(z); 
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(FloatType()))],VoidType(),Block([])),FuncDecl(Id("goo"),[VarDecl("x",ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl("y",ArrayType(10,FloatType())),VarDecl("z",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("x")]),CallExpr(Id("foo"),[Id("y")]),CallExpr(Id("foo"),[Id("z")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_expression_14(self):        
        input = """
            void foo ( ) {
            if(a<b) return ; 
            else return 2; 
        }       
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("<",Id("a"),Id("b")),Return(),Return(IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_expression_15(self):        
        input = """
            int[] foo (int b[]){
                int a [1];
                if (b>c) return a;
                else return b;
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(1,IntType())),If(BinaryOp(">",Id("b"),Id("c")),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_statement_1(self):        
        input = """
        int main() {
            if (a>b) a=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_statement_2(self):        
        input = """
            int main() {
            if (a>b) a=1; else a=0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_statement_3(self):        
        input = """
        int main() {
            if (a>b) {
                int c[5];
                c[2] = b + a * 10 % c[d[e[t+m+5]]];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Block([VarDecl("c",ArrayType(5,IntType())),BinaryOp("=",ArrayCell(Id("c"),IntLiteral(2)),BinaryOp("+",Id("b"),BinaryOp("%",BinaryOp("*",Id("a"),IntLiteral(10)),ArrayCell(Id("c"),ArrayCell(Id("d"),ArrayCell(Id("e"),BinaryOp("+",BinaryOp("+",Id("t"),Id("m")),IntLiteral(5))))))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_statement_4(self):        
        input = """
        int main(){
            do {
                int a[2];
            }
            {
                a+b;
            }
            while (a<5);
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",ArrayType(2,IntType()))]),Block([BinaryOp("+",Id("a"),Id("b"))])],BinaryOp("<",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_statement_5(self):        
        input = """
        int main(){
            do {
                int a[2];
            }
            {
                a+b;
            }
            while a<5==9%7;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",ArrayType(2,IntType()))]),Block([BinaryOp("+",Id("a"),Id("b"))])],BinaryOp("==",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp("%",IntLiteral(9),IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_statement_6(self):        
        input = """
        int main(){
            do {
                foo(5);
            }
            while (a<5);
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("foo"),[IntLiteral(5)])])],BinaryOp("<",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_statement_7(self):        
        input = """
        int main(){
            for(i = 0; i < 10; i=i+1) {
                putIntLn("Hello world!\\n");
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[StringLiteral("Hello world!\\n")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_statement_8(self):        
        input = """
        int main(){
            for(i = 0; i < foo(2)[foo(4)[a+b+c]]; i = i + 1) {
                putIntLn("Hello world!\\n");
            }
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(CallExpr(Id("foo"),[IntLiteral(4)]),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[StringLiteral("Hello world!\\n")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_statement_9(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                printf("Hello world!\\n");
            }
            {

            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Hello world!\\n")])])),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_statement_10(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                for (j = 10; j >= 0; j = j - 1) {
                    if (i == j) putIntLn("i");
                }
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(10)),BinaryOp(">=",Id("j"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),Id("j")),CallExpr(Id("putIntLn"),[StringLiteral("i")]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_statement_11(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                for (j = 10; j >= 0; j = j - 1) {
                    if (i == j) return 0;
                    else return 1;
                }
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(10)),BinaryOp(">=",Id("j"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),Id("j")),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_statement_12(self):        
        input = """
            int main(){
            for (i = 0; i < 10; i = i + 1){
                if (i == a % foo(2)[i]) break;
                else continue;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),BinaryOp("%",Id("a"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),Id("i")))),Break(),Continue())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_statement_13(self):        
        input = """
        int i;
        int f() {
            return 200;
        }
        void main () {
            int main ;
            main = f();
            putIntLn (main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
                putIntLn(main);
        }    
        """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_all_1(self):        
        input = """
        int[] foo(boolean a, float b){}
        int main() {
            putIntLn(foo(a>=b,00.E2019)[10]);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",BoolType()),VarDecl("b",FloatType())],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[ArrayCell(CallExpr(Id("foo"),[BinaryOp(">=",Id("a"),Id("b")),FloatLiteral(0.0)]),IntLiteral(10))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_all_2(self):        
        input = """
        /* this is a comment */ 
        void foo() {if (a==0) {b = a+c;}}
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Block([BinaryOp("=",Id("b"),BinaryOp("+",Id("a"),Id("c")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_all_3(self):        
        input = """
        int main() {
            foo(2)[3+x] = a[b[2]] +3;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_all_4(self):        
        input = """
        int main() {
            int a,b[10];
            a = b[1] = foo()[3] = x = 1 ;    
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),BinaryOp("=",Id("a"),BinaryOp("=",ArrayCell(Id("b"),IntLiteral(1)),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),BinaryOp("=",Id("x"),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_all_5(self):        
        input = """
        int main() {
            a[(123)];
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),IntLiteral(123))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_all_6(self):        
        input = """
        int main() {
            (-12.25e-12);
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("-",FloatLiteral(1.225e-11))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_all_7(self):        
        input = """
        int main() {
            a = false;
            do {
                if (b) a; 
                continue;
            } while !a;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BooleanLiteral(False)),Dowhile([Block([If(Id("b"),Id("a")),Continue()])],UnaryOp("!",Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_all_8(self):        
        input = """
        int main() {
            if (a) 
                do
                    continue;
                while b;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),Dowhile([Continue()],Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_all_9(self):        
        input = """
        int main() {
            return;
            break;
            continue;
            {}
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(),Break(),Continue(),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_all_10(self):        
        input = """
        int main() {
            if (a == b) {} else if (a > b) {} else {}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([]),If(BinaryOp(">",Id("a"),Id("b")),Block([]),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_all_11(self):        
        input = """
        int main() {
             if (a) if (b) b; else c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),If(Id("b"),Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_all_12(self):        
        input = """
        int main() {
            do 
                do
                {}
                while (a);
            while(b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Dowhile([Block([])],Id("a"))],Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_all_13(self):        
        input = """
        int main() {{{{{{{{{}}}}}}}}}
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_all_14(self):        
        input = """
        boolean IsPrime(int number)
        {
            for (i = 2; i < number; i = i + 1)
            {
                if (number % i == 0 && i != number)
                    return false;
            }
            return true;
        }
        """
        expect = str(Program([FuncDecl(Id("IsPrime"),[VarDecl("number",IntType())],BoolType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),Id("number")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("number"),Id("i")),IntLiteral(0)),BinaryOp("!=",Id("i"),Id("number"))),Return(BooleanLiteral(False)))])),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_all_15(self):        
        input = """
        int main() {
            if (a == f[0]) print(a);
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),ArrayCell(Id("f"),IntLiteral(0))),CallExpr(Id("print"),[Id("a")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_all_16(self):        
        input = """
        int main() {
            for(a;a;a) return;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("a"),Id("a"),Id("a"),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_all_17(self):        
        input = """
        int main() {
            printf("Error char: ~`$^.@");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Error char: ~`$^.@")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_all_18(self):        
        input = """
        int main() {
            // final /*...........\\n...........\\r...*/ \\n int a = 5;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_all_19(self):        
        input = """
        int main()
        {
            float a,b,c,d;
            printf("Nhap vao 3 so a, b, c: ");
            scanf("%f%f%f",a,b,c);
            if(a==0)
            {
                if(b==0)
                    {
                        if(c==0)
                            printf("Phuong trinh co vo so nghiem!");
                        else
                            printf("Phuong trinh vo nghiem!");
                    }
                else
                    printf("Phuong trinh co nghiem duy nhat la: %f",-c/b);
            }
            else
            {
                d=b*b-4*a*c;
                if (d<0)
                    printf("Phuong trinh vo nghiem!!!");
                else if (d==0)
                    printf("Phuong trinh co nghiem kep la: %f",-b/(2*a));
                else
                    printf("Phuong trinh co 2 nghiem phan biet la: %f,%f",(-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a));    
            }    
        
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),CallExpr(Id("printf"),[StringLiteral("Nhap vao 3 so a, b, c: ")]),CallExpr(Id("scanf"),[StringLiteral("%f%f%f"),Id("a"),Id("b"),Id("c")]),If(BinaryOp("==",Id("a"),IntLiteral(0)),Block([If(BinaryOp("==",Id("b"),IntLiteral(0)),Block([If(BinaryOp("==",Id("c"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Phuong trinh co vo so nghiem!")]),CallExpr(Id("printf"),[StringLiteral("Phuong trinh vo nghiem!")]))]),CallExpr(Id("printf"),[StringLiteral("Phuong trinh co nghiem duy nhat la: %f"),BinaryOp("/",UnaryOp("-",Id("c")),Id("b"))]))]),Block([BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c")))),If(BinaryOp("<",Id("d"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Phuong trinh vo nghiem!!!")]),If(BinaryOp("==",Id("d"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Phuong trinh co nghiem kep la: %f"),BinaryOp("/",UnaryOp("-",Id("b")),BinaryOp("*",IntLiteral(2),Id("a")))]),CallExpr(Id("printf"),[StringLiteral("Phuong trinh co 2 nghiem phan biet la: %f,%f"),BinaryOp("/",BinaryOp("+",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("d")])),BinaryOp("*",IntLiteral(2),Id("a"))),BinaryOp("/",BinaryOp("-",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("d")])),BinaryOp("*",IntLiteral(2),Id("a")))])))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_all_20(self):        
        input = """
        int main() {
        int array[10];
        int loop;
        printf("In tat ca phan tu cua mang: \\n\\n");
        for(loop = 0; loop < 10; loop = loop + 1)
            printf("%d ", array[loop]);            
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(10,IntType())),VarDecl("loop",IntType()),CallExpr(Id("printf"),[StringLiteral("In tat ca phan tu cua mang: \\n\\n")]),For(BinaryOp("=",Id("loop"),IntLiteral(0)),BinaryOp("<",Id("loop"),IntLiteral(10)),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("%d "),ArrayCell(Id("array"),Id("loop"))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_all_21(self):        
        input = """
        int main() {
            int array[10];
            int sum, loop;
            sum = 0;        
            printf("Chuong trinh tinh tong gia tri cac phan tu mang: \\n\\n");
            for(loop = 9; loop >= 0; loop = loop - 1) {
                sum = sum + array[loop];      
            }
            printf("Tong gia tri cua mang la: %d.", sum);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(10,IntType())),VarDecl("sum",IntType()),VarDecl("loop",IntType()),BinaryOp("=",Id("sum"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Chuong trinh tinh tong gia tri cac phan tu mang: \\n\\n")]),For(BinaryOp("=",Id("loop"),IntLiteral(9)),BinaryOp(">=",Id("loop"),IntLiteral(0)),BinaryOp("=",Id("loop"),BinaryOp("-",Id("loop"),IntLiteral(1))),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("array"),Id("loop"))))])),CallExpr(Id("printf"),[StringLiteral("Tong gia tri cua mang la: %d."),Id("sum")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_all_22(self):        
        input = """
        int main() {
        int array[10];
        int loop, largest;
        largest = array[0];        
        printf("Chuong trinh tim phan tu lon nhat cua mang:\\n\\n"); 
        for(loop = 1; loop < 10; loop = loop + 1) {
            if( largest < array[loop] ) 
                largest = array[loop];
        }        
        printf("Phan tu lon nhat cua mang la: %d", largest);       
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(10,IntType())),VarDecl("loop",IntType()),VarDecl("largest",IntType()),BinaryOp("=",Id("largest"),ArrayCell(Id("array"),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("Chuong trinh tim phan tu lon nhat cua mang:\\n\\n")]),For(BinaryOp("=",Id("loop"),IntLiteral(1)),BinaryOp("<",Id("loop"),IntLiteral(10)),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),Block([If(BinaryOp("<",Id("largest"),ArrayCell(Id("array"),Id("loop"))),BinaryOp("=",Id("largest"),ArrayCell(Id("array"),Id("loop"))))])),CallExpr(Id("printf"),[StringLiteral("Phan tu lon nhat cua mang la: %d"),Id("largest")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_all_23(self):        
        input = """
        int main() { 
            int loop, number;
            int prime;
            
            number;

            for(loop = 2; loop < number; loop = loop + 1) {
                if((number % loop) == 0) {
                    prime = 0;
                }
            }

            if (prime == 1)
                printf("So %d la so nguyen to.", number);
            else
                printf("So %d khong phai la so nguyen to.", number);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("loop",IntType()),VarDecl("number",IntType()),VarDecl("prime",IntType()),Id("number"),For(BinaryOp("=",Id("loop"),IntLiteral(2)),BinaryOp("<",Id("loop"),Id("number")),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("number"),Id("loop")),IntLiteral(0)),Block([BinaryOp("=",Id("prime"),IntLiteral(0))]))])),If(BinaryOp("==",Id("prime"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("So %d la so nguyen to."),Id("number")]),CallExpr(Id("printf"),[StringLiteral("So %d khong phai la so nguyen to."),Id("number")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_all_24(self):        
        input = """
        int main() {
            int a, b, c, i, n;
            n = 6;
            a = b = 1;
            printf("In day Fibonacci:\\n");
            printf("%d %d ",a,b);
            for(i = 1; i <= n-2; i = i + 1) {
                c = a + b;
                printf("%d ", c);
                
                a = b;
                b = c;
            }
            
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("i",IntType()),VarDecl("n",IntType()),BinaryOp("=",Id("n"),IntLiteral(6)),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("In day Fibonacci:\\n")]),CallExpr(Id("printf"),[StringLiteral("%d %d "),Id("a"),Id("b")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),BinaryOp("-",Id("n"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),Id("b"))),CallExpr(Id("printf"),[StringLiteral("%d "),Id("c")]),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("c"))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_all_25(self):        
        input = """
        int main() {
        int loop;
        int factorial;
        int number;

        for(loop = 1; loop<=number; loop = loop + 1) {
            factorial = factorial * loop;
        }

        printf("Giai thua cua %d = %d \\n", number, factorial);

        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("loop",IntType()),VarDecl("factorial",IntType()),VarDecl("number",IntType()),For(BinaryOp("=",Id("loop"),IntLiteral(1)),BinaryOp("<=",Id("loop"),Id("number")),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),Block([BinaryOp("=",Id("factorial"),BinaryOp("*",Id("factorial"),Id("loop")))])),CallExpr(Id("printf"),[StringLiteral("Giai thua cua %d = %d \\n"),Id("number"),Id("factorial")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_all_26(self):        
        input = """
        int main() {
            int a, b, i, hcf;

            a = 12;
            b = 16;

            for(i = 1; i <= a || i <= b; i = i + 1) {
            if( a%i == 0 && b%i == 0 )
                hcf = i;
            }

            printf("USCLN = %d", hcf);
            
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("i",IntType()),VarDecl("hcf",IntType()),BinaryOp("=",Id("a"),IntLiteral(12)),BinaryOp("=",Id("b"),IntLiteral(16)),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("||",BinaryOp("<=",Id("i"),Id("a")),BinaryOp("<=",Id("i"),Id("b"))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("a"),Id("i")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("b"),Id("i")),IntLiteral(0))),BinaryOp("=",Id("hcf"),Id("i")))])),CallExpr(Id("printf"),[StringLiteral("USCLN = %d"),Id("hcf")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_all_27(self):        
        input = """
        int main() {
        int a, b, max, step, lcm;

        a   = 3;
        b   = 4;
        lcm = 0;

        if(a > b)
            max = step = a;
        else
            max = step = b;

        do {
            if(max%a == 0 && max%b == 0) {
                lcm = max;
                break;    
            }

            max = max + step;
        } while(1);

        printf("BSCNN = %d", lcm);
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("max",IntType()),VarDecl("step",IntType()),VarDecl("lcm",IntType()),BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp("=",Id("b"),IntLiteral(4)),BinaryOp("=",Id("lcm"),IntLiteral(0)),If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("max"),BinaryOp("=",Id("step"),Id("a"))),BinaryOp("=",Id("max"),BinaryOp("=",Id("step"),Id("b")))),Dowhile([Block([If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("max"),Id("a")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("max"),Id("b")),IntLiteral(0))),Block([BinaryOp("=",Id("lcm"),Id("max")),Break()])),BinaryOp("=",Id("max"),BinaryOp("+",Id("max"),Id("step")))])],IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("BSCNN = %d"),Id("lcm")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_all_28(self):        
        input = """
        int day_fibonaci(int i)
        {
        if(i == 0)
        {
            return 0;
        }
        if(i == 1)
        {
            return 1;
        }
        return day_fibonaci(i-1) + day_fibonaci(i-2);
        }

        int  main()
        {
            int i;
            for (i = 0; i < 10; i=i+1)
            {
            printf("%d  %n", day_fibonaci(i));
            }      
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("day_fibonaci"),[VarDecl("i",IntType())],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(0)),Block([Return(IntLiteral(0))])),If(BinaryOp("==",Id("i"),IntLiteral(1)),Block([Return(IntLiteral(1))])),Return(BinaryOp("+",CallExpr(Id("day_fibonaci"),[BinaryOp("-",Id("i"),IntLiteral(1))]),CallExpr(Id("day_fibonaci"),[BinaryOp("-",Id("i"),IntLiteral(2))])))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("%d  %n"),CallExpr(Id("day_fibonaci"),[Id("i")])])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_all_29(self):        
        input = """
        int main() {
        int i, num;
        int result;

        printf("Nhap mot so bat ky: ");
        scanf("%d", num);

        result = calculateSum(num);
        printf("Tong cac so tu 1 toi %d la: %d", num, result);

        return (0);
        }

        int calculateSum(int num) {
        int res;
        if (num == 1) {
            return (1);
        } else {
            res = num + calculateSum(num - 1);
        }
        return (res);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("num",IntType()),VarDecl("result",IntType()),CallExpr(Id("printf"),[StringLiteral("Nhap mot so bat ky: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("num")]),BinaryOp("=",Id("result"),CallExpr(Id("calculateSum"),[Id("num")])),CallExpr(Id("printf"),[StringLiteral("Tong cac so tu 1 toi %d la: %d"),Id("num"),Id("result")]),Return(IntLiteral(0))])),FuncDecl(Id("calculateSum"),[VarDecl("num",IntType())],IntType(),Block([VarDecl("res",IntType()),If(BinaryOp("==",Id("num"),IntLiteral(1)),Block([Return(IntLiteral(1))]),Block([BinaryOp("=",Id("res"),BinaryOp("+",Id("num"),CallExpr(Id("calculateSum"),[BinaryOp("-",Id("num"),IntLiteral(1))])))])),Return(Id("res"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_all_30(self):        
        input = """
        int tinhgiaithua(int i)
        {
        if(i <= 1)
        {
            return 1;
        }
        return i * tinhgiaithua(i - 1);
        }
        int  main()
        {
            int i;
            i = 10;
            printf("Gia tri giai thua cua %d la %d\\n", i, tinhgiaithua(i));
        
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("tinhgiaithua"),[VarDecl("i",IntType())],IntType(),Block([If(BinaryOp("<=",Id("i"),IntLiteral(1)),Block([Return(IntLiteral(1))])),Return(BinaryOp("*",Id("i"),CallExpr(Id("tinhgiaithua"),[BinaryOp("-",Id("i"),IntLiteral(1))])))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(10)),CallExpr(Id("printf"),[StringLiteral("Gia tri giai thua cua %d la %d\\n"),Id("i"),CallExpr(Id("tinhgiaithua"),[Id("i")])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_all_31(self):        
        input = """
        int main() {
        int year;
        year = 2016;
        
        if (((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0))
            printf("%d la mot nam nhuan", year);
        else
            printf("%d khong phai la nam nhuan", year);
            
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("year",IntType()),BinaryOp("=",Id("year"),IntLiteral(2016)),If(BinaryOp("||",BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(4)),IntLiteral(0)),BinaryOp("!=",BinaryOp("%",Id("year"),IntLiteral(100)),IntLiteral(0))),BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(400)),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("%d la mot nam nhuan"),Id("year")]),CallExpr(Id("printf"),[StringLiteral("%d khong phai la nam nhuan"),Id("year")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_all_32(self):        
        input = """
        int main() {
        int i, j, count;
        int start, end;

        start = 2; end = 10;

        printf("In bang cuu chuong rut gon:\\n");
        for(i = start; i <= end; i=i+1) {
            count = i;

            for(j = 1; j <= 10; j=j+1) {
                printf(" %3d", count*j);
            }

            printf("\\n");
        }

        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("count",IntType()),VarDecl("start",IntType()),VarDecl("end",IntType()),BinaryOp("=",Id("start"),IntLiteral(2)),BinaryOp("=",Id("end"),IntLiteral(10)),CallExpr(Id("printf"),[StringLiteral("In bang cuu chuong rut gon:\\n")]),For(BinaryOp("=",Id("i"),Id("start")),BinaryOp("<=",Id("i"),Id("end")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("count"),Id("i")),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),IntLiteral(10)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral(" %3d"),BinaryOp("*",Id("count"),Id("j"))])])),CallExpr(Id("printf"),[StringLiteral("\\n")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_all_33(self):        
        input = """
        int main() {
        int i;

        printf("In cac so chan:\\n");
        for(i = 1; i <= 10; i=i+1) {
            if(i%2 == 0)
                printf(" %2d\\n", i);
        }
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("In cac so chan:\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral(" %2d\\n"),Id("i")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_all_34(self):        
        input = """
        int main() {
        int i;

        printf("In cac so le:\\n");
        for(i = 1; i <= 10; i=i+1) {
            if(i%2 != 0)
                printf("%d\\n", i);
        }
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("In cac so le:\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d\\n"),Id("i")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_all_35(self):        
        input = """
        int main() {
        int n,i,j;

        n = 5;   // khai bao so hang.

        printf("Ve tam giac sao deu:\\n\\n");
        for(i = 1; i <= n; i=i+1) {
            for(j = 1; j <= n-i; j=j+1)
                printf(" ");

            for(j = 1; j <= i; j=j+1)
                printf("* ");

            printf("\\n");
        }
        return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("j",IntType()),BinaryOp("=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("Ve tam giac sao deu:\\n\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),BinaryOp("-",Id("n"),Id("i"))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral(" ")])),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("* ")])),CallExpr(Id("printf"),[StringLiteral("\\n")])])),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_all_36(self):        
        input = """
        int main() {
        int n,i,j;

        n = 5;

        printf("Ve tam giac sao vuong can:");
        for(i = 1; i <= n; i=i+1) {
            for(j = 1; j <= i; j=j+1)
                printf("* ");

            printf("\\n");
        }
        return 0;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("j",IntType()),BinaryOp("=",Id("n"),IntLiteral(5)),CallExpr(Id("printf"),[StringLiteral("Ve tam giac sao vuong can:")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("* ")])),CallExpr(Id("printf"),[StringLiteral("\\n")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_all_37(self):        
        input = """
        int main() {
        float percentage;
        int total_marks; total_marks = 86;
        int scored; scored = 50;

        percentage = scored / total_marks * 100.0;

        printf("Gia tri phan tram = %.2f%%", percentage);

        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("percentage",FloatType()),VarDecl("total_marks",IntType()),BinaryOp("=",Id("total_marks"),IntLiteral(86)),VarDecl("scored",IntType()),BinaryOp("=",Id("scored"),IntLiteral(50)),BinaryOp("=",Id("percentage"),BinaryOp("*",BinaryOp("/",Id("scored"),Id("total_marks")),FloatLiteral(100.0))),CallExpr(Id("printf"),[StringLiteral("Gia tri phan tram = %.2f%%"),Id("percentage")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_all_38(self):        
        input = """
        int factorial(int n) {
            int f;

            for(f = 1; n > 1; n = n - 1)
                f = f* n;

            return f;
        }

        int npr(int n,int r) {
            return factorial(n)/factorial(n-r);
        }

        int main() {
            int n, r;

            n = 4;
            r = 3;
            
            printf("Tinh hoan vi:");
            printf("%dp%d = %d \\n", n, r, npr(n,r));

            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("factorial"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("f",IntType()),For(BinaryOp("=",Id("f"),IntLiteral(1)),BinaryOp(">",Id("n"),IntLiteral(1)),BinaryOp("=",Id("n"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("=",Id("f"),BinaryOp("*",Id("f"),Id("n")))),Return(Id("f"))])),FuncDecl(Id("npr"),[VarDecl("n",IntType()),VarDecl("r",IntType())],IntType(),Block([Return(BinaryOp("/",CallExpr(Id("factorial"),[Id("n")]),CallExpr(Id("factorial"),[BinaryOp("-",Id("n"),Id("r"))])))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("r",IntType()),BinaryOp("=",Id("n"),IntLiteral(4)),BinaryOp("=",Id("r"),IntLiteral(3)),CallExpr(Id("printf"),[StringLiteral("Tinh hoan vi:")]),CallExpr(Id("printf"),[StringLiteral("%dp%d = %d \\n"),Id("n"),Id("r"),CallExpr(Id("npr"),[Id("n"),Id("r")])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_all_39(self):        
        input = """
        int main() {
            int num;
            printf("Nhap so dia:");
            scanf("%d", num);

            TOH(num - 1, "A", "B", "C");
            return (0);
        }

        void TOH(int num, string x, string y, string z) {
            if (num > 0) {
                TOH(num - 1, x, z, y);
                printf("%c -> %c", x, y);
                TOH(num - 1, z, y, x);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("num",IntType()),CallExpr(Id("printf"),[StringLiteral("Nhap so dia:")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("num")]),CallExpr(Id("TOH"),[BinaryOp("-",Id("num"),IntLiteral(1)),StringLiteral("A"),StringLiteral("B"),StringLiteral("C")]),Return(IntLiteral(0))])),FuncDecl(Id("TOH"),[VarDecl("num",IntType()),VarDecl("x",StringType()),VarDecl("y",StringType()),VarDecl("z",StringType())],VoidType(),Block([If(BinaryOp(">",Id("num"),IntLiteral(0)),Block([CallExpr(Id("TOH"),[BinaryOp("-",Id("num"),IntLiteral(1)),Id("x"),Id("z"),Id("y")]),CallExpr(Id("printf"),[StringLiteral("%c -> %c"),Id("x"),Id("y")]),CallExpr(Id("TOH"),[BinaryOp("-",Id("num"),IntLiteral(1)),Id("z"),Id("y"),Id("x")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_all_40(self):        
        input = """
        int main() {
        int n;n = 6;

        printf("Gia tri lap phuong cua %d = %d", n, (n*n*n));

        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("n"),IntLiteral(6)),CallExpr(Id("printf"),[StringLiteral("Gia tri lap phuong cua %d = %d"),Id("n"),BinaryOp("*",BinaryOp("*",Id("n"),Id("n")),Id("n"))]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_all_41(self):        
        input = """
        int main() {
        int arms;arms = 153; 
        int check, rem,sum; sum = 0;

        check = arms;

        do {
            rem = check % 10;
            sum = sum + (rem * rem * rem);
            check = check / 10;
        }while(check != 0);

        if(sum == arms) 
            printf("So %d la mot so armstrong.", arms);
        else 
            printf("So %d khong phai la so armstrong.", arms);

        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("arms",IntType()),BinaryOp("=",Id("arms"),IntLiteral(153)),VarDecl("check",IntType()),VarDecl("rem",IntType()),VarDecl("sum",IntType()),BinaryOp("=",Id("sum"),IntLiteral(0)),BinaryOp("=",Id("check"),Id("arms")),Dowhile([Block([BinaryOp("=",Id("rem"),BinaryOp("%",Id("check"),IntLiteral(10))),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),BinaryOp("*",BinaryOp("*",Id("rem"),Id("rem")),Id("rem")))),BinaryOp("=",Id("check"),BinaryOp("/",Id("check"),IntLiteral(10)))])],BinaryOp("!=",Id("check"),IntLiteral(0))),If(BinaryOp("==",Id("sum"),Id("arms")),CallExpr(Id("printf"),[StringLiteral("So %d la mot so armstrong."),Id("arms")]),CallExpr(Id("printf"),[StringLiteral("So %d khong phai la so armstrong."),Id("arms")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_all_42(self):        
        input = """
        int main() {
        int original[10];
        int copied[10];
        int loop;
        
        for(loop = 0; loop < 10; loop = loop+1) {
            copied[loop] = original[loop];
        }
        printf("Sao chep mang trong C:");
        printf("Mang ban dau -> Mang sao chep ");
        
        for(loop = 0; loop < 10; loop = loop+1) {
            printf("    %2d          %2d\\n", original[loop], copied[loop]);
        }

        
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("original",ArrayType(10,IntType())),VarDecl("copied",ArrayType(10,IntType())),VarDecl("loop",IntType()),For(BinaryOp("=",Id("loop"),IntLiteral(0)),BinaryOp("<",Id("loop"),IntLiteral(10)),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("copied"),Id("loop")),ArrayCell(Id("original"),Id("loop")))])),CallExpr(Id("printf"),[StringLiteral("Sao chep mang trong C:")]),CallExpr(Id("printf"),[StringLiteral("Mang ban dau -> Mang sao chep ")]),For(BinaryOp("=",Id("loop"),IntLiteral(0)),BinaryOp("<",Id("loop"),IntLiteral(10)),BinaryOp("=",Id("loop"),BinaryOp("+",Id("loop"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("    %2d          %2d\\n"),ArrayCell(Id("original"),Id("loop")),ArrayCell(Id("copied"),Id("loop"))])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_all_43(self):        
        input = """
        void main()
        {
            int num, binary_val, decimal_val, base, rem;
            decimal_val = 0; base = 1;
            printf("Nhap so nhi phan(1 & 0): ");
            scanf("%d", num); /* maximum five digits */
            binary_val = num;
            do
            {
                rem = num % 10;
                decimal_val = decimal_val + rem * base;
                num = num / 10 ;
                base = base * 2;
            } while (num > 0);
            printf("So nhi phan = %d ", binary_val);
            printf("Gia tri he thap phan = %d ", decimal_val);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("num",IntType()),VarDecl("binary_val",IntType()),VarDecl("decimal_val",IntType()),VarDecl("base",IntType()),VarDecl("rem",IntType()),BinaryOp("=",Id("decimal_val"),IntLiteral(0)),BinaryOp("=",Id("base"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("Nhap so nhi phan(1 & 0): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("num")]),BinaryOp("=",Id("binary_val"),Id("num")),Dowhile([Block([BinaryOp("=",Id("rem"),BinaryOp("%",Id("num"),IntLiteral(10))),BinaryOp("=",Id("decimal_val"),BinaryOp("+",Id("decimal_val"),BinaryOp("*",Id("rem"),Id("base")))),BinaryOp("=",Id("num"),BinaryOp("/",Id("num"),IntLiteral(10))),BinaryOp("=",Id("base"),BinaryOp("*",Id("base"),IntLiteral(2)))])],BinaryOp(">",Id("num"),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("So nhi phan = %d "),Id("binary_val")]),CallExpr(Id("printf"),[StringLiteral("Gia tri he thap phan = %d "),Id("decimal_val")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_all_44(self):        
        input = """
        void main()
        {
            int n;
            float a, b, c ;
            float R;
            float P;
            float S;
            do
            {
                printf("Nhap cac canh cua tam giac:");
                scanf("%f %f %f", a, b, c);
            }
            while(a < 0 || b < 0 || c < 0 || (a + b) <= c || (a + c) <= b || (b + c) <= a);
            P = (a + b + c);
            S = sqrt(P*(P/2 - a)*(P/2 - b)*(P/2 - c)/2);
            printf("Chu vi tam giac : %f dvdd", P);
            printf("Dien tich tam giac : %f dvdt", S);
            break;                
            getch();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("R",FloatType()),VarDecl("P",FloatType()),VarDecl("S",FloatType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap cac canh cua tam giac:")]),CallExpr(Id("scanf"),[StringLiteral("%f %f %f"),Id("a"),Id("b"),Id("c")])])],BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("<",Id("b"),IntLiteral(0))),BinaryOp("<",Id("c"),IntLiteral(0))),BinaryOp("<=",BinaryOp("+",Id("a"),Id("b")),Id("c"))),BinaryOp("<=",BinaryOp("+",Id("a"),Id("c")),Id("b"))),BinaryOp("<=",BinaryOp("+",Id("b"),Id("c")),Id("a")))),BinaryOp("=",Id("P"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))),BinaryOp("=",Id("S"),CallExpr(Id("sqrt"),[BinaryOp("/",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("P"),BinaryOp("-",BinaryOp("/",Id("P"),IntLiteral(2)),Id("a"))),BinaryOp("-",BinaryOp("/",Id("P"),IntLiteral(2)),Id("b"))),BinaryOp("-",BinaryOp("/",Id("P"),IntLiteral(2)),Id("c"))),IntLiteral(2))])),CallExpr(Id("printf"),[StringLiteral("Chu vi tam giac : %f dvdd"),Id("P")]),CallExpr(Id("printf"),[StringLiteral("Dien tich tam giac : %f dvdt"),Id("S")]),Break(),CallExpr(Id("getch"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_all_45(self):        
        input = """
        void main()
        {
            int n;
            float a, b, c ;
            float R;
            float P;
            float S;
            do
            {
                printf("Nhap chieu rong hcn: ");
                scanf("%f", a);
                printf("Nhap chieu dai hcn: ");
                scanf("%f", b);
            }
            while(a < 0 || b < 0);
            P = (a + b)*2;
            S = a * b;
            printf("Chu vi hinh vuong : %f dvdd", P);
            printf("Dien tich hinh vuong: %f dvdt", S);
            break;                
            getch();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("R",FloatType()),VarDecl("P",FloatType()),VarDecl("S",FloatType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap chieu rong hcn: ")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("a")]),CallExpr(Id("printf"),[StringLiteral("Nhap chieu dai hcn: ")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("b")])])],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("<",Id("b"),IntLiteral(0)))),BinaryOp("=",Id("P"),BinaryOp("*",BinaryOp("+",Id("a"),Id("b")),IntLiteral(2))),BinaryOp("=",Id("S"),BinaryOp("*",Id("a"),Id("b"))),CallExpr(Id("printf"),[StringLiteral("Chu vi hinh vuong : %f dvdd"),Id("P")]),CallExpr(Id("printf"),[StringLiteral("Dien tich hinh vuong: %f dvdt"),Id("S")]),Break(),CallExpr(Id("getch"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_all_46(self):        
        input = """
        void main()
        {
            int n;
            float a, b, c ;
            float R;
            float P;
            float S;
            do
            {
                printf("Nhap ban kinh duong tron:");
                scanf("%f", R);
            }
            while(R <= 0);
            P = 2 * PI * R;
            S = PI * R * R;
            printf("Chu vi hinh tron : %f dvdd", P);
            printf("Dien tich hinh tron : %f dvdt", S);
            break;               
            getch();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("R",FloatType()),VarDecl("P",FloatType()),VarDecl("S",FloatType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap ban kinh duong tron:")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("R")])])],BinaryOp("<=",Id("R"),IntLiteral(0))),BinaryOp("=",Id("P"),BinaryOp("*",BinaryOp("*",IntLiteral(2),Id("PI")),Id("R"))),BinaryOp("=",Id("S"),BinaryOp("*",BinaryOp("*",Id("PI"),Id("R")),Id("R"))),CallExpr(Id("printf"),[StringLiteral("Chu vi hinh tron : %f dvdd"),Id("P")]),CallExpr(Id("printf"),[StringLiteral("Dien tich hinh tron : %f dvdt"),Id("S")]),Break(),CallExpr(Id("getch"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_all_47(self):        
        input = """
        void main()
        {
            float C;C = 0;
            float F;
            printf("Nhap vao nhiet do F = ");
            scanf("%f", F);
            C = 5*(F - 32)/9.0;
            printf("Nhieu do Celcius = %f oC", C);
            getch();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("C",FloatType()),BinaryOp("=",Id("C"),IntLiteral(0)),VarDecl("F",FloatType()),CallExpr(Id("printf"),[StringLiteral("Nhap vao nhiet do F = ")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("F")]),BinaryOp("=",Id("C"),BinaryOp("/",BinaryOp("*",IntLiteral(5),BinaryOp("-",Id("F"),IntLiteral(32))),FloatLiteral(9.0))),CallExpr(Id("printf"),[StringLiteral("Nhieu do Celcius = %f oC"),Id("C")]),CallExpr(Id("getch"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))


    