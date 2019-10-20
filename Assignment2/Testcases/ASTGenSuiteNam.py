import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_simple_program_2(self):
        input = """void ndhnam(int n, int a, int m){}"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[VarDecl("n",IntType()),VarDecl("a",IntType()),VarDecl("m",IntType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_simple_program_3(self):
        input = """void ndhnam(){}
        int main(){
            int a,b,c, d, e, f;
            a = b = c = 10;
            float f[2];
            if (a == b) f[2] = .1e9;
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(10)))),VarDecl("f",ArrayType(2,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(2)),FloatLiteral(100000000.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_simple_program_4(self):
        input = """boolean TRUEORFALSE(boolean True){True = false;}"""
        expect = str(Program([FuncDecl(Id("TRUEORFALSE"),[VarDecl("True",BoolType())],BoolType(),Block([BinaryOp("=",Id("True"),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_simple_program_5(self):
        input = """string[] main(string main){a = 5;}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("main",StringType())],ArrayPointerType(StringType()),Block([BinaryOp("=",Id("a"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_simple_program_6(self):
        input = """string Ha_Nam(string _30121999){string Hello; Hello = "Happy birthday!" + 30 + 12 + 1999;}"""
        expect = str(Program([FuncDecl(Id("Ha_Nam"),[VarDecl("_30121999",StringType())],StringType(),Block([VarDecl("Hello",StringType()),BinaryOp("=",Id("Hello"),BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("Happy birthday!"),IntLiteral(30)),IntLiteral(12)),IntLiteral(1999)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_simple_program_7(self):
        input = """int main () {
            putttttttIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putttttttIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_program_8(self):
        input = """int main(){
        int c;
        c = 2 + 2;
        if ( c != 4 )
            return;
        else
             b = 5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),BinaryOp("+",IntLiteral(2),IntLiteral(2))),If(BinaryOp("!=",Id("c"),IntLiteral(4)),Return(),BinaryOp("=",Id("b"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_simple_program_9(self):
        input = """void main(){
            int a,b,c, d;
            a = b = c = 10;
            float foo[5];
            if (a == b) foo(2)[n[2]] = .1e9;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(10)))),VarDecl("foo",ArrayType(5,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(Id("n"),IntLiteral(2))),FloatLiteral(100000000.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_simple_program_10(self):
        input = """int[] foo(float a, boolean b[]){
        int c[9];
        if (b != false){
            c[10] = 9;
        }
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",FloatType()),VarDecl("b",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(9,IntType())),If(BinaryOp("!=",Id("b"),BooleanLiteral(False)),Block([BinaryOp("=",ArrayCell(Id("c"),IntLiteral(10)),IntLiteral(9))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_simple_program_11(self):
        input = """int[] a(){}
        boolean b(){}"""
        expect = str(Program([FuncDecl(Id("a"),[],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("b"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_simple_program_12(self):
        input = """void feeder(string player){
            int i;
            i = 0;
            do
                i = i + 1;
                player = "why you always feed," + player + "?";
            while i != 3;
        }"""
        expect = str(Program([FuncDecl(Id("feeder"),[VarDecl("player",StringType())],VoidType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("player"),BinaryOp("+",BinaryOp("+",StringLiteral("why you always feed,"),Id("player")),StringLiteral("?")))],BinaryOp("!=",Id("i"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_simple_program_13(self):
        input = """int main(int a[]){
            int i;
            for (i = 0; i < 5; i = i + 1)
                okay();
            return okay();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("okay"),[])),Return(CallExpr(Id("okay"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_simple_program_14(self):
        input = """int main(float a[]){
        for(a[1] = 8; a[9] < (5 + 6)[5];i = i + 2)
            a[951]*5 = 8 && 2;
            a = 5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(FloatType()))],IntType(),Block([For(BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(8)),BinaryOp("<",ArrayCell(Id("a"),IntLiteral(9)),ArrayCell(BinaryOp("+",IntLiteral(5),IntLiteral(6)),IntLiteral(5))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),BinaryOp("=",BinaryOp("*",ArrayCell(Id("a"),IntLiteral(951)),IntLiteral(5)),BinaryOp("&&",IntLiteral(8),IntLiteral(2)))),BinaryOp("=",Id("a"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_simple_program_15(self):
        input = """int main(int a[], int b){
        string c, d, f, g, h, j, k;
        for(a; a < (5 + 6)[5];i = i + 2)
            if(i == 5) return true; else return hello(a[b]);
            a = 5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],IntType(),Block([VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("f",StringType()),VarDecl("g",StringType()),VarDecl("h",StringType()),VarDecl("j",StringType()),VarDecl("k",StringType()),For(Id("a"),BinaryOp("<",Id("a"),ArrayCell(BinaryOp("+",IntLiteral(5),IntLiteral(6)),IntLiteral(5))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),If(BinaryOp("==",Id("i"),IntLiteral(5)),Return(BooleanLiteral(True)),Return(CallExpr(Id("hello"),[ArrayCell(Id("a"),Id("b"))])))),BinaryOp("=",Id("a"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_simple_program_16(self):
        input = """int[] main(int a[]){
        for(a; a < (5 + 6)[5];i = i + 2)
            if(i == f) return true;
            f = 5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([For(Id("a"),BinaryOp("<",Id("a"),ArrayCell(BinaryOp("+",IntLiteral(5),IntLiteral(6)),IntLiteral(5))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),If(BinaryOp("==",Id("i"),Id("f")),Return(BooleanLiteral(True)))),BinaryOp("=",Id("f"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_simple_program_17(self):
        input = """float main(int a[]){
        return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],FloatType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_simple_program_18(self):
        input = """int hello(string a[]){
        this == b * 5 = a = main(foo, a, b, f, d, h);
        }"""
        expect = str(Program([FuncDecl(Id("hello"),[VarDecl("a",ArrayPointerType(StringType()))],IntType(),Block([BinaryOp("=",BinaryOp("==",Id("this"),BinaryOp("*",Id("b"),IntLiteral(5))),BinaryOp("=",Id("a"),CallExpr(Id("main"),[Id("foo"),Id("a"),Id("b"),Id("f"),Id("d"),Id("h")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_simple_program_19(self):
        input = """int main(string a){
        this / a = main(foo, a, b, f, d, h);
        return d;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",StringType())],IntType(),Block([BinaryOp("=",BinaryOp("/",Id("this"),Id("a")),CallExpr(Id("main"),[Id("foo"),Id("a"),Id("b"),Id("f"),Id("d"),Id("h")])),Return(Id("d"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_simple_program_20(self):
        input = """float ndhnam(){
        float1 = (true || flase)*("ok");
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[],FloatType(),Block([BinaryOp("=",Id("float1"),BinaryOp("*",BinaryOp("||",BooleanLiteral(True),Id("flase")),StringLiteral("ok")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_simple_program_21(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            before = after - present;
            hello = "\\n";
        }"""
        expect = str(Program([FuncDecl(Id("hello"),[VarDecl("hello",IntType()),VarDecl("hello",FloatType()),VarDecl("snsnsn",ArrayPointerType(StringType()))],VoidType(),Block([BinaryOp("=",Id("before"),BinaryOp("-",Id("after"),Id("present"))),BinaryOp("=",Id("hello"),StringLiteral("\\n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_simple_program_22(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            helo = "\\rrqwvdvfsbgnfnfgfrrrrrrrr";
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = str(Program([FuncDecl(Id("hello"),[VarDecl("hello",IntType()),VarDecl("hello",FloatType()),VarDecl("snsnsn",ArrayPointerType(StringType()))],VoidType(),Block([BinaryOp("=",Id("helo"),StringLiteral("\\rrqwvdvfsbgnfnfgfrrrrrrrr")),CallExpr(Id("helo"),[CallExpr(Id("helo"),[CallExpr(Id("helo"),[CallExpr(Id("helo"),[Id("helo"),Id("ola")])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    
    def test_simple_program_23(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            if (helo == 789654123)
                if (ok) return;
                else ok = 8;
            else pass;
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = str(Program([FuncDecl(Id("hello"),[VarDecl("hello",IntType()),VarDecl("hello",FloatType()),VarDecl("snsnsn",ArrayPointerType(StringType()))],VoidType(),Block([If(BinaryOp("==",Id("helo"),IntLiteral(789654123)),If(Id("ok"),Return(),BinaryOp("=",Id("ok"),IntLiteral(8))),Id("pass")),CallExpr(Id("helo"),[CallExpr(Id("helo"),[CallExpr(Id("helo"),[CallExpr(Id("helo"),[Id("helo"),Id("ola")])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_simple_program_24(self):
        input = """void Void(){}
        int main(){LOOOPPPP();}
        string String(string ____){_;}"""
        expect = str(Program([FuncDecl(Id("Void"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("LOOOPPPP"),[])])),FuncDecl(Id("String"),[VarDecl("____",StringType())],StringType(),Block([Id("_")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_simple_program_25(self):
        input = """void Adder(float a, int b){
        c = a + b = b / a = a * a = a / b;
        float c,d,f,g;
        }"""
        expect = str(Program([FuncDecl(Id("Adder"),[VarDecl("a",FloatType()),VarDecl("b",IntType())],VoidType(),Block([BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("=",BinaryOp("/",Id("b"),Id("a")),BinaryOp("=",BinaryOp("*",Id("a"),Id("a")),BinaryOp("/",Id("a"),Id("b")))))),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("f",FloatType()),VarDecl("g",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_simple_program_26(self):
        input = """void Adderrr(int a, int b){
        c = a + b = b / a = a * a = a / b;
        int hhh,hh,jj;
        }
        int Main(int arr[]){
        arr = .1e-5 + 1.e7 * 8;
        Add(5,6,5);
        return;
        }"""
        expect = str(Program([FuncDecl(Id("Adderrr"),[VarDecl("a",IntType()),VarDecl("b",IntType())],VoidType(),Block([BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("=",BinaryOp("/",Id("b"),Id("a")),BinaryOp("=",BinaryOp("*",Id("a"),Id("a")),BinaryOp("/",Id("a"),Id("b")))))),VarDecl("hhh",IntType()),VarDecl("hh",IntType()),VarDecl("jj",IntType())])),FuncDecl(Id("Main"),[VarDecl("arr",ArrayPointerType(IntType()))],IntType(),Block([BinaryOp("=",Id("arr"),BinaryOp("+",FloatLiteral(1e-06),BinaryOp("*",FloatLiteral(10000000.0),IntLiteral(8)))),CallExpr(Id("Add"),[IntLiteral(5),IntLiteral(6),IntLiteral(5)]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_simple_program_27(self):
        input = """int Main(int a, float b, string c, int d[]){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \\r \\\\ t em e n t
        while(ok(ok)[5]);
            run_py(runnnnn);
        }"""
        expect = str(Program([FuncDecl(Id("Main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",ArrayPointerType(IntType()))],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(5)),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),ArrayCell(Id("f"),IntLiteral(5)),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0)))],ArrayCell(CallExpr(Id("ok"),[Id("ok")]),IntLiteral(5))),CallExpr(Id("run_py"),[Id("runnnnn")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_simple_program_28(self):
        input = """int Main(int hhh, float b){
        do
            /*a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \\r \\\\ t em e n t*/
            ok();
        while(ok(ok)[5]);
            run_py(runnnnn);
        }"""
        expect = str(Program([FuncDecl(Id("Main"),[VarDecl("hhh",IntType()),VarDecl("b",FloatType())],IntType(),Block([Dowhile([CallExpr(Id("ok"),[])],ArrayCell(CallExpr(Id("ok"),[Id("ok")]),IntLiteral(5))),CallExpr(Id("run_py"),[Id("runnnnn")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_simple_program_29(self):
        input = """int main() {
        float alpha;
        cin = theta;
        float result; sin(alpha);
        cout(fixed, setprecision(4) , result);
        return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("alpha",FloatType()),BinaryOp("=",Id("cin"),Id("theta")),VarDecl("result",FloatType()),CallExpr(Id("sin"),[Id("alpha")]),CallExpr(Id("cout"),[Id("fixed"),CallExpr(Id("setprecision"),[IntLiteral(4)]),Id("result")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_simple_program_30(self):
        input = """int[] Matrix(int _x, int _y, int _z) {
        x = _x;
        y = _y;
        z = _z;
        mat = inr[x];
        for (i = 0; i < x; i +1 =i) 
            for(j = 0; j < y; j + 1 =j)
                mat[i] && mat[j] = inr[z];
        }"""
        expect = str(Program([FuncDecl(Id("Matrix"),[VarDecl("_x",IntType()),VarDecl("_y",IntType()),VarDecl("_z",IntType())],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("x"),Id("_x")),BinaryOp("=",Id("y"),Id("_y")),BinaryOp("=",Id("z"),Id("_z")),BinaryOp("=",Id("mat"),ArrayCell(Id("inr"),Id("x"))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("x")),BinaryOp("=",BinaryOp("+",Id("i"),IntLiteral(1)),Id("i")),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("y")),BinaryOp("=",BinaryOp("+",Id("j"),IntLiteral(1)),Id("j")),BinaryOp("=",BinaryOp("&&",ArrayCell(Id("mat"),Id("i")),ArrayCell(Id("mat"),Id("j"))),ArrayCell(Id("inr"),Id("z")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_simple_program_31(self):
        input = """int a[11000];
        void tapcon(int k, int i) {
        for (j = 0; j < 5; j = j + 1)
            x[i] = a[j];
            if (i == k - 1) 
                for (j = 0; j < k; j = j * 2)
                    cout(x[j]);
            else tapcon(k, i + 1);
        }"""
        expect = str(Program([VarDecl("a",ArrayType(11000,IntType())),FuncDecl(Id("tapcon"),[VarDecl("k",IntType()),VarDecl("i",IntType())],VoidType(),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),IntLiteral(5)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("x"),Id("i")),ArrayCell(Id("a"),Id("j")))),If(BinaryOp("==",Id("i"),BinaryOp("-",Id("k"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("k")),BinaryOp("=",Id("j"),BinaryOp("*",Id("j"),IntLiteral(2))),CallExpr(Id("cout"),[ArrayCell(Id("x"),Id("j"))])),CallExpr(Id("tapcon"),[Id("k"),BinaryOp("+",Id("i"),IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_simple_program_32(self):
        input = """float a[8];
        void tapcon(int k, int i) {
        for (j = 0; j < 5; j = j + 1)
            // x[i] = a[j];
            if (i == k - 1) 
                for (j = 0; j < k; j = j * 2)
                    cout(x[j]);
            else tapcon(k, i + 1);
        }"""
        expect = str(Program([VarDecl("a",ArrayType(8,FloatType())),FuncDecl(Id("tapcon"),[VarDecl("k",IntType()),VarDecl("i",IntType())],VoidType(),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),IntLiteral(5)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),If(BinaryOp("==",Id("i"),BinaryOp("-",Id("k"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("k")),BinaryOp("=",Id("j"),BinaryOp("*",Id("j"),IntLiteral(2))),CallExpr(Id("cout"),[ArrayCell(Id("x"),Id("j"))])),CallExpr(Id("tapcon"),[Id("k"),BinaryOp("+",Id("i"),IntLiteral(1))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_simple_program_33(self):
        input = """
        void thuc(int thuc) {
        thisthuc = thuc;
        }
        int getthuc() {
            return thuc;
            }
        void setao(int ao) {
            thisao = ao;
            }
        int getao() {
        int a;
            return ao;
        }"""
        expect = str(Program([FuncDecl(Id("thuc"),[VarDecl("thuc",IntType())],VoidType(),Block([BinaryOp("=",Id("thisthuc"),Id("thuc"))])),FuncDecl(Id("getthuc"),[],IntType(),Block([Return(Id("thuc"))])),FuncDecl(Id("setao"),[VarDecl("ao",IntType())],VoidType(),Block([BinaryOp("=",Id("thisao"),Id("ao"))])),FuncDecl(Id("getao"),[],IntType(),Block([VarDecl("a",IntType()),Return(Id("ao"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_simple_program_34(self):
        input = """
        void helloWord(int thuc) {
            print("hello");
        }"""
        expect = str(Program([FuncDecl(Id("helloWord"),[VarDecl("thuc",IntType())],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("hello")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_simple_program_35(self):
        input = """void main() {
        int n;
        cout("ban dang tinh sin(x) voi x -> 0 \\n Hay nhap x ~ 0: ");
        system("pause");
        return;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),CallExpr(Id("cout"),[StringLiteral("ban dang tinh sin(x) voi x -> 0 \\n Hay nhap x ~ 0: ")]),CallExpr(Id("system"),[StringLiteral("pause")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_simple_program_36(self):
        input = """int main() {
        int n;
        cout("ban dang tinh sin(x) voi x -> 0 \\n Hay nhap x ~ 0: ");
        system("pause");
        return k;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("cout"),[StringLiteral("ban dang tinh sin(x) voi x -> 0 \\n Hay nhap x ~ 0: ")]),CallExpr(Id("system"),[StringLiteral("pause")]),Return(Id("k"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_simple_program_37(self):
        input = """int main(string days) {
        int songay, nam, tuan, ngay;
        cout = "Nhap so ngay: ";
        cin = songay;
        nam = songay / 365;
        tuan = (songay % 365) / 7;
        ngay = songay - nam * 365 - tuan * 7;
        cout = songay + " ngay = " + nam + " nam + " + tuan + " tuan + " + ngay + " ngay" + endl;
        system("pause");
        return;}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("days",StringType())],IntType(),Block([VarDecl("songay",IntType()),VarDecl("nam",IntType()),VarDecl("tuan",IntType()),VarDecl("ngay",IntType()),BinaryOp("=",Id("cout"),StringLiteral("Nhap so ngay: ")),BinaryOp("=",Id("cin"),Id("songay")),BinaryOp("=",Id("nam"),BinaryOp("/",Id("songay"),IntLiteral(365))),BinaryOp("=",Id("tuan"),BinaryOp("/",BinaryOp("%",Id("songay"),IntLiteral(365)),IntLiteral(7))),BinaryOp("=",Id("ngay"),BinaryOp("-",BinaryOp("-",Id("songay"),BinaryOp("*",Id("nam"),IntLiteral(365))),BinaryOp("*",Id("tuan"),IntLiteral(7)))),BinaryOp("=",Id("cout"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("songay"),StringLiteral(" ngay = ")),Id("nam")),StringLiteral(" nam + ")),Id("tuan")),StringLiteral(" tuan + ")),Id("ngay")),StringLiteral(" ngay")),Id("endl"))),CallExpr(Id("system"),[StringLiteral("pause")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_simple_program_38(self):
        input = """float main() {
        int soao;
        boolean thoat;
        return true;}"""
        expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([VarDecl("soao",IntType()),VarDecl("thoat",BoolType()),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_simple_program_39(self):
        input = """string[] MMain() {
        return soao;
        break;
        countinue;
        return true;}"""
        expect = str(Program([FuncDecl(Id("MMain"),[],ArrayPointerType(StringType()),Block([Return(Id("soao")),Break(),Id("countinue"),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_simple_program_40(self):
        input = """int main() {
        return soao;
        return true;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(Id("soao")),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))



    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLfffffffffffffffffn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLfffffffffffffffffn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_more_complex_program_2(self):
        input = """int intlit;
        int main() {
        float i, F, F1, F2, k, n;
        F1 = 1;
        F2 = 1;}"""
        expect = str(Program([VarDecl("intlit",IntType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",FloatType()),VarDecl("F",FloatType()),VarDecl("F1",FloatType()),VarDecl("F2",FloatType()),VarDecl("k",FloatType()),VarDecl("n",FloatType()),BinaryOp("=",Id("F1"),IntLiteral(1)),BinaryOp("=",Id("F2"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_more_complex_program_3(self):
        input = """void main() {
        int n;
        cout ("nhap n: ");
        cin (n);
        for ( k = 0; k <= n; k = k + 1) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        pi = 2 * sum;
        system("pause");
        return ok;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),CallExpr(Id("cout"),[StringLiteral("nhap n: ")]),CallExpr(Id("cin"),[Id("n")]),For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<=",Id("k"),Id("n")),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([BinaryOp("=",Id("tuso"),BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("k"),IntLiteral(1)))),BinaryOp("=",Id("mau1"),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),Id("k")))),BinaryOp("=",Id("mau2"),BinaryOp("+",IntLiteral(3),BinaryOp("*",IntLiteral(2),Id("k")))),BinaryOp("=",Id("nhantu"),BinaryOp("/",BinaryOp("*",Id("tuso"),Id("tuso")),BinaryOp("*",Id("mau1"),Id("mau2")))),BinaryOp("=",Id("sum"),BinaryOp("*",Id("sum"),Id("nhantu")))])),BinaryOp("=",Id("pi"),BinaryOp("*",IntLiteral(2),Id("sum"))),CallExpr(Id("system"),[StringLiteral("pause")]),Return(Id("ok"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_more_complex_program_4(self):
        input = """int nguyendanghanam() {
        cin ( n);
        for ( k = 0; k <= n; k = k + 1) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        }"""
        expect = str(Program([FuncDecl(Id("nguyendanghanam"),[],IntType(),Block([CallExpr(Id("cin"),[Id("n")]),For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<=",Id("k"),Id("n")),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([BinaryOp("=",Id("tuso"),BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("k"),IntLiteral(1)))),BinaryOp("=",Id("mau1"),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),Id("k")))),BinaryOp("=",Id("mau2"),BinaryOp("+",IntLiteral(3),BinaryOp("*",IntLiteral(2),Id("k")))),BinaryOp("=",Id("nhantu"),BinaryOp("/",BinaryOp("*",Id("tuso"),Id("tuso")),BinaryOp("*",Id("mau1"),Id("mau2")))),BinaryOp("=",Id("sum"),BinaryOp("*",Id("sum"),Id("nhantu")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_more_complex_program_5(self):
        input = """string Name(string Ho, string Ten){
        Ho = "Nguyen Dang Ha";
        }"""
        expect = str(Program([FuncDecl(Id("Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],StringType(),Block([BinaryOp("=",Id("Ho"),StringLiteral("Nguyen Dang Ha"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_more_complex_program_6(self):
        input = """string Name(string Ho, string Ten){
        Ten = "Nam";
        }"""
        expect = str(Program([FuncDecl(Id("Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],StringType(),Block([BinaryOp("=",Id("Ten"),StringLiteral("Nam"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_more_complex_program_7(self):
        input = """void Name(string Ho, string Ten){
        print("My name is: ", Ho, Ten);
        }"""
        expect = str(Program([FuncDecl(Id("Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("My name is: "),Id("Ho"),Id("Ten")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_more_complex_program_8(self):
        input = """string Name(string Ho, string Ten){
        Myemail = "nam.nguyen999@hcmut.edu.vn" || "ndhnam99@gmail.com";
        }"""
        expect = str(Program([FuncDecl(Id("Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],StringType(),Block([BinaryOp("=",Id("Myemail"),BinaryOp("||",StringLiteral("nam.nguyen999@hcmut.edu.vn"),StringLiteral("ndhnam99@gmail.com")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_more_complex_program_9(self):
        input = """int[] Name(string Ho, string Ten){
        Ho = "Nguyen Dang Ha";
        Ten = "Nam";
        print("My name is: ", Ho, Ten);
        }"""
        expect = str(Program([FuncDecl(Id("Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("Ho"),StringLiteral("Nguyen Dang Ha")),BinaryOp("=",Id("Ten"),StringLiteral("Nam")),CallExpr(Id("print"),[StringLiteral("My name is: "),Id("Ho"),Id("Ten")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_more_complex_program_10(self):
        input = """string NDHNAM_Name(string Ho, string Ten){
        Ho = "Nguyen Dang Ha";
        Ten = "Nam";
        print("My name is: ", Ho, Ten);
        Myemail = "nam.nguyen999@hcmut.edu.vn" || "ndhnam99@gmail.com";
        }"""
        expect = str(Program([FuncDecl(Id("NDHNAM_Name"),[VarDecl("Ho",StringType()),VarDecl("Ten",StringType())],StringType(),Block([BinaryOp("=",Id("Ho"),StringLiteral("Nguyen Dang Ha")),BinaryOp("=",Id("Ten"),StringLiteral("Nam")),CallExpr(Id("print"),[StringLiteral("My name is: "),Id("Ho"),Id("Ten")]),BinaryOp("=",Id("Myemail"),BinaryOp("||",StringLiteral("nam.nguyen999@hcmut.edu.vn"),StringLiteral("ndhnam99@gmail.com")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_more_complex_program_11(self):
        input = """int test1(){}
        float test2(){}
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([])),FuncDecl(Id("test2"),[],FloatType(),Block([])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_more_complex_program_12(self):
        input = """string[] okkk(int a, float g[]){
            cout(1,56, khk);
        }"""
        expect = str(Program([FuncDecl(Id("okkk"),[VarDecl("a",IntType()),VarDecl("g",ArrayPointerType(FloatType()))],ArrayPointerType(StringType()),Block([CallExpr(Id("cout"),[IntLiteral(1),IntLiteral(56),Id("khk")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_more_complex_program_13(self):
        input = """int test1(){}
        float test2(){
            int kko[5550];
            boolean bool;
            kko[5] = 69;
        }
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([])),FuncDecl(Id("test2"),[],FloatType(),Block([VarDecl("kko",ArrayType(5550,IntType())),VarDecl("bool",BoolType()),BinaryOp("=",ArrayCell(Id("kko"),IntLiteral(5)),IntLiteral(69))])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_more_complex_program_14(self):
        input = """int test1(){}
        float test2(boolean trueorfalse){
            do
                okkokokok();
                kokoko();
            while 
                tre == true;
        }
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([])),FuncDecl(Id("test2"),[VarDecl("trueorfalse",BoolType())],FloatType(),Block([Dowhile([CallExpr(Id("okkokokok"),[]),CallExpr(Id("kokoko"),[])],BinaryOp("==",Id("tre"),BooleanLiteral(True)))])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_more_complex_program_15(self):
        input = """int test1(){
            exp = (1 == 2)*(2/5)+(tt / 8)!=(ggg);
        }
        float test2(){}
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([BinaryOp("=",Id("exp"),BinaryOp("!=",BinaryOp("+",BinaryOp("*",BinaryOp("==",IntLiteral(1),IntLiteral(2)),BinaryOp("/",IntLiteral(2),IntLiteral(5))),BinaryOp("/",Id("tt"),IntLiteral(8))),Id("ggg")))])),FuncDecl(Id("test2"),[],FloatType(),Block([])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_more_complex_program_16(self):
        input = """int test1(){
            continue;
        }
        float test2(){
            break;
        }
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([Continue()])),FuncDecl(Id("test2"),[],FloatType(),Block([Break()])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_more_complex_program_17(self):
        input = """void ihhiihihi(){
            _123456 = 123456;
        }"""
        expect = str(Program([FuncDecl(Id("ihhiihihi"),[],VoidType(),Block([BinaryOp("=",Id("_123456"),IntLiteral(123456))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_more_complex_program_18(self):
        input = """float ok(int ok, string type){
            print(type[ok]);
        }"""
        expect = str(Program([FuncDecl(Id("ok"),[VarDecl("ok",IntType()),VarDecl("type",StringType())],FloatType(),Block([CallExpr(Id("print"),[ArrayCell(Id("type"),Id("ok"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_more_complex_program_19(self):
        input = """int test1(){}
        float test2(){}
        void test3(){
            int a, b, d, f, g, t, h;
            float a,f,g,h,e,h;
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([])),FuncDecl(Id("test2"),[],FloatType(),Block([])),FuncDecl(Id("test3"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("d",IntType()),VarDecl("f",IntType()),VarDecl("g",IntType()),VarDecl("t",IntType()),VarDecl("h",IntType()),VarDecl("a",FloatType()),VarDecl("f",FloatType()),VarDecl("g",FloatType()),VarDecl("h",FloatType()),VarDecl("e",FloatType()),VarDecl("h",FloatType()),CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_more_complex_program_20(self):
        input = """int test1(){
            int a[5], g[5],h,j[10],k,r;
            string ffff[7];
            fff = "agbcndsjvhbsjkdjc//nbdgcvsdcjnsjdc";
        }
        float test2(){}
        void test3(){
            hello("vvv");
        }"""
        expect = str(Program([FuncDecl(Id("test1"),[],IntType(),Block([VarDecl("a",ArrayType(5,IntType())),VarDecl("g",ArrayType(5,IntType())),VarDecl("h",IntType()),VarDecl("j",ArrayType(10,IntType())),VarDecl("k",IntType()),VarDecl("r",IntType()),VarDecl("ffff",ArrayType(7,StringType())),BinaryOp("=",Id("fff"),StringLiteral("agbcndsjvhbsjkdjc//nbdgcvsdcjnsjdc"))])),FuncDecl(Id("test2"),[],FloatType(),Block([])),FuncDecl(Id("test3"),[],VoidType(),Block([CallExpr(Id("hello"),[StringLiteral("vvv")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))


    def test_call_without_parameter(self):
        """More complex program"""
        input = """int mmamam () {
            getIn(55);
        }"""
        expect = str(Program([FuncDecl(Id("mmamam"),[],IntType(),Block([CallExpr(Id("getIn"),[IntLiteral(55)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_call_without_parameter_2(self):
        input = """int main(string arg) {
	int t;
	cin(t);
	for (i = 0; i < t; i = i + 1) {
		int a, b, c, d, k;
		cin(k);
		int pen, pencile;
		if (a % c == 0) {
			pen = a / c;
		}
		else {
			pen = a / c + 1;
		}
		if (b % d == 0) {
			pencile = b / d;
		}
		else {
			pencile = b / d + 1;
		}
		if (pen + pencile > k) {
			cout(endl);
		}
		else {
			cout(endl);
		}
	}
	system("pause");
	return a0;
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType())],IntType(),Block([VarDecl("t",IntType()),CallExpr(Id("cin"),[Id("t")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("k",IntType()),CallExpr(Id("cin"),[Id("k")]),VarDecl("pen",IntType()),VarDecl("pencile",IntType()),If(BinaryOp("==",BinaryOp("%",Id("a"),Id("c")),IntLiteral(0)),Block([BinaryOp("=",Id("pen"),BinaryOp("/",Id("a"),Id("c")))]),Block([BinaryOp("=",Id("pen"),BinaryOp("+",BinaryOp("/",Id("a"),Id("c")),IntLiteral(1)))])),If(BinaryOp("==",BinaryOp("%",Id("b"),Id("d")),IntLiteral(0)),Block([BinaryOp("=",Id("pencile"),BinaryOp("/",Id("b"),Id("d")))]),Block([BinaryOp("=",Id("pencile"),BinaryOp("+",BinaryOp("/",Id("b"),Id("d")),IntLiteral(1)))])),If(BinaryOp(">",BinaryOp("+",Id("pen"),Id("pencile")),Id("k")),Block([CallExpr(Id("cout"),[Id("endl")])]),Block([CallExpr(Id("cout"),[Id("endl")])]))])),CallExpr(Id("system"),[StringLiteral("pause")]),Return(Id("a0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_call_without_parameter_3(self):
        input = """int main(string arg[]) {
	int t[595959595959];
	cin(t);
	for (jjj = 0; i < t; i = i + 1) {
		int a, b[5], c, d, k;
		cin(k);
		int pen, pencile;
		if (a % c == 0) {
			pen = a / c;
		}
		else {
			pen = a / c + 1;
		}
		if (b % d == 0) {
			pencile = b / d;
		}
		if (pen + pencile > k) {
			cout(endl);
		}
		else {
			cout(endl);
		}
	}
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("t",ArrayType(595959595959,IntType())),CallExpr(Id("cin"),[Id("t")]),For(BinaryOp("=",Id("jjj"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("k",IntType()),CallExpr(Id("cin"),[Id("k")]),VarDecl("pen",IntType()),VarDecl("pencile",IntType()),If(BinaryOp("==",BinaryOp("%",Id("a"),Id("c")),IntLiteral(0)),Block([BinaryOp("=",Id("pen"),BinaryOp("/",Id("a"),Id("c")))]),Block([BinaryOp("=",Id("pen"),BinaryOp("+",BinaryOp("/",Id("a"),Id("c")),IntLiteral(1)))])),If(BinaryOp("==",BinaryOp("%",Id("b"),Id("d")),IntLiteral(0)),Block([BinaryOp("=",Id("pencile"),BinaryOp("/",Id("b"),Id("d")))])),If(BinaryOp(">",BinaryOp("+",Id("pen"),Id("pencile")),Id("k")),Block([CallExpr(Id("cout"),[Id("endl")])]),Block([CallExpr(Id("cout"),[Id("endl")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_call_without_parameter_4(self):
        input = """int[] main(string arg, int okokokoko[]) {
	int t;
	
	system("pause");
	return a0;
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType()),VarDecl("okokokoko",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("t",IntType()),CallExpr(Id("system"),[StringLiteral("pause")]),Return(Id("a0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_call_without_parameter_5(self):
        input = """int main(string arg) {
	/*int t;
	cin(t);
	for (i = 0; i < t; i = i + 1) {
		int a, b, c, d, k;
		cin(k);
		int pen, pencile;
		if (a % c == 0) {
			pen = a / c;
		}
		else {
			pen = a / c + 1;
		}
		if (b % d == 0) {
			pencile = b / d;
		}
		else {
			pencile = b / d + 1;
		}
		if (pen + pencile > k) {
			cout(endl);
		}
		else {
			cout(endl);
		}
	}
	system("pause");*/
	return a0;
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType())],IntType(),Block([Return(Id("a0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_call_without_parameter_6(self):
        input = """boolean[] main(string arg) {
	//int t;
	//cin(t);
	for (i = 0; i < t; i = i + 1) {
		int a, b, c, d, k;
		cin(k);
		int pen, pencile;
		if (a % c == 0) {
			pen = a / c;
		}
	}
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType())],ArrayPointerType(BoolType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("k",IntType()),CallExpr(Id("cin"),[Id("k")]),VarDecl("pen",IntType()),VarDecl("pencile",IntType()),If(BinaryOp("==",BinaryOp("%",Id("a"),Id("c")),IntLiteral(0)),Block([BinaryOp("=",Id("pen"),BinaryOp("/",Id("a"),Id("c")))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_call_without_parameter_7(self):
        input = """boolean naim(int arg[]) {
	/*for (i = 0; i < t; i = i + 1) {
		int a, b, c, d, k;
		cin(k);
		int pen[951], pencile;
		if (a % c == 0) {
			pen = a / c;
		}
    }*/
	/*	else {
			pen = a / c + 1;
		}*/
		if (b % d == 0) {
			pencile = b / d;
		}
		else {
			pencile = b / d + 1;
		}
		if (pen + pencile > k) {
			cout(endl);
		}
		else {
			//cout(endl);
		}
	system("sytpppp");
	return a0;
}"""
        expect = str(Program([FuncDecl(Id("naim"),[VarDecl("arg",ArrayPointerType(IntType()))],BoolType(),Block([If(BinaryOp("==",BinaryOp("%",Id("b"),Id("d")),IntLiteral(0)),Block([BinaryOp("=",Id("pencile"),BinaryOp("/",Id("b"),Id("d")))]),Block([BinaryOp("=",Id("pencile"),BinaryOp("+",BinaryOp("/",Id("b"),Id("d")),IntLiteral(1)))])),If(BinaryOp(">",BinaryOp("+",Id("pen"),Id("pencile")),Id("k")),Block([CallExpr(Id("cout"),[Id("endl")])]),Block([])),CallExpr(Id("system"),[StringLiteral("sytpppp")]),Return(Id("a0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_call_without_parameter_8(self):
        input = """void mWin(int double, string arg) {
	float nope;
	for (i = 0; i < t; i = i + 1) {
        break;
        continue;
    }
}"""
        expect = str(Program([FuncDecl(Id("mWin"),[VarDecl("double",IntType()),VarDecl("arg",StringType())],VoidType(),Block([VarDecl("nope",FloatType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Break(),Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_call_without_parameter_9(self):
        input = """int main(string arg) {
	int t;
	cin(t);
	for (i = 0; i < t; i = i + 1) {
		string a, b[2], c, d[9], k;
		if (pen + pencile > k) {
			cout(endl);
            int hhh[555];
            hh = -5;
		}
	}
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType())],IntType(),Block([VarDecl("t",IntType()),CallExpr(Id("cin"),[Id("t")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",StringType()),VarDecl("b",ArrayType(2,StringType())),VarDecl("c",StringType()),VarDecl("d",ArrayType(9,StringType())),VarDecl("k",StringType()),If(BinaryOp(">",BinaryOp("+",Id("pen"),Id("pencile")),Id("k")),Block([CallExpr(Id("cout"),[Id("endl")]),VarDecl("hhh",ArrayType(555,IntType())),BinaryOp("=",Id("hh"),UnaryOp("-",IntLiteral(5)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_call_without_parameter_10(self):
        input = """float main(string arg) {
	for (i = 0; i < t; i = i + 1) {
		int a, b, c, d, k;
		cin(k);
		int pen, pencile;
		if (a % c == 0) {
			pen = a / c;
		}
		if (b % d == 0) {
			pencile = b / d;
		}
		if (pen + pencile > k) {
			cout(endl);
		}
	}
}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("arg",StringType())],FloatType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("t")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("k",IntType()),CallExpr(Id("cin"),[Id("k")]),VarDecl("pen",IntType()),VarDecl("pencile",IntType()),If(BinaryOp("==",BinaryOp("%",Id("a"),Id("c")),IntLiteral(0)),Block([BinaryOp("=",Id("pen"),BinaryOp("/",Id("a"),Id("c")))])),If(BinaryOp("==",BinaryOp("%",Id("b"),Id("d")),IntLiteral(0)),Block([BinaryOp("=",Id("pencile"),BinaryOp("/",Id("b"),Id("d")))])),If(BinaryOp(">",BinaryOp("+",Id("pen"),Id("pencile")),Id("k")),Block([CallExpr(Id("cout"),[Id("endl")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_call_without_parameter_11(self):
        input = """
        int a[200001];
        int main(){
	    int n;
	    res = 0;
	    walker = 0;
	    loop = true;
	    for (i = 0; i < n; i = i - 1) {
		    if (loop) {
			    a[i] = 56;
		    }
		    if (a[i] == 1) {
			    walker = false;
		    }
		    else {
			    res = max(res, walker);	
			    walker = 0;
		    }
		    if (loop && (i == n - 1)) {
			    i = -1;
			    loop = false;
		    }
	    }
	    system("pause");
	    return aaa0;
        }"""
        expect = str(Program([VarDecl("a",ArrayType(200001,IntType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),BinaryOp("=",Id("walker"),IntLiteral(0)),BinaryOp("=",Id("loop"),BooleanLiteral(True)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Block([If(Id("loop"),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(56))])),If(BinaryOp("==",ArrayCell(Id("a"),Id("i")),IntLiteral(1)),Block([BinaryOp("=",Id("walker"),BooleanLiteral(False))]),Block([BinaryOp("=",Id("res"),CallExpr(Id("max"),[Id("res"),Id("walker")])),BinaryOp("=",Id("walker"),IntLiteral(0))])),If(BinaryOp("&&",Id("loop"),BinaryOp("==",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1)))),Block([BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("loop"),BooleanLiteral(False))]))])),CallExpr(Id("system"),[StringLiteral("pause")]),Return(Id("aaa0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_call_without_parameter_12(self):
        input = """int a[200001];
        int main(){
	    int n265_6565;
	    res = 0;
	    walker = 0;
	    loop = true;
        }"""
        expect = str(Program([VarDecl("a",ArrayType(200001,IntType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n265_6565",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),BinaryOp("=",Id("walker"),IntLiteral(0)),BinaryOp("=",Id("loop"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_call_without_parameter_13(self):
        input = """string str[200001];
        int[] dev(int io[]){
	    
	    walker = 0;
	    loop = true;
	    
	    return aaa0;
        }"""
        expect = str(Program([VarDecl("str",ArrayType(200001,StringType())),FuncDecl(Id("dev"),[VarDecl("io",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("walker"),IntLiteral(0)),BinaryOp("=",Id("loop"),BooleanLiteral(True)),Return(Id("aaa0"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_call_without_parameter_14(self):
        input = """boolean arr[200001];
        void main(){
	    int n[5];
	    
		    if (loop && (i == n - 1)) {
			    i = -1;
			    loop = false;
		    }
	    
        }"""
        expect = str(Program([VarDecl("arr",ArrayType(200001,BoolType())),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",ArrayType(5,IntType())),If(BinaryOp("&&",Id("loop"),BinaryOp("==",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1)))),Block([BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("loop"),BooleanLiteral(False))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_call_without_parameter_15(self):
        input = """int a[200001];
        int main(){
	    int n;
	    res = 0;
	    walker = 0;
	    loop = true;
	    for (i = 0; i < n; i = i - 1) {
		    break;
	    }
        }"""
        expect = str(Program([VarDecl("a",ArrayType(200001,IntType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),BinaryOp("=",Id("walker"),IntLiteral(0)),BinaryOp("=",Id("loop"),BooleanLiteral(True)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Block([Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_call_without_parameter_16(self):
        input = """int a[200001];
        int main(){
	    int n;
	    res = 0;
	    walker = 0;
	    loop = true;
	    for (i = 0; i < n; i = i - 1) {
		    if (loop) {
			    a[i] = 56;
		    }
		    if (a[i] == 1) {
			    walker = false;
		    }
		    
		    if (loop && (i == n * h - 1)) {
			    i = -1;
			    loop = false;
		    }
	    }
	    system("paussssssssse");
        }"""
        expect = str(Program([VarDecl("a",ArrayType(200001,IntType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),BinaryOp("=",Id("walker"),IntLiteral(0)),BinaryOp("=",Id("loop"),BooleanLiteral(True)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Block([If(Id("loop"),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(56))])),If(BinaryOp("==",ArrayCell(Id("a"),Id("i")),IntLiteral(1)),Block([BinaryOp("=",Id("walker"),BooleanLiteral(False))])),If(BinaryOp("&&",Id("loop"),BinaryOp("==",Id("i"),BinaryOp("-",BinaryOp("*",Id("n"),Id("h")),IntLiteral(1)))),Block([BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("loop"),BooleanLiteral(False))]))])),CallExpr(Id("system"),[StringLiteral("paussssssssse")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_call_without_parameter_17(self):
        input = """int array[59001];
        """
        expect = str(Program([VarDecl("array",ArrayType(59001,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_call_without_parameter_18(self):
        input = """string stringg;
        int intt;
        void oi(){}"""
        expect = str(Program([VarDecl("stringg",StringType()),VarDecl("intt",IntType()),FuncDecl(Id("oi"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_call_without_parameter_19(self):
        input = """void V0(){}
        void V2(int a, int b, int c, int d){}
        int[] I4(int a[], int c[], string c){}"""
        expect = str(Program([FuncDecl(Id("V0"),[],VoidType(),Block([])),FuncDecl(Id("V2"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())],VoidType(),Block([])),FuncDecl(Id("I4"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("c",ArrayPointerType(IntType())),VarDecl("c",StringType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_call_without_parameter_20(self):
        input = """int[] array(int a[], float b[]){
            int a, f, g, h[8];
        }"""
        expect = str(Program([FuncDecl(Id("array"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("f",IntType()),VarDecl("g",IntType()),VarDecl("h",ArrayType(8,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_call_without_parameter_21(self):
        input = """void main(int ii) {
	int n, x;
	for (i = 0; i < n; i = n + x) {
	}
	temp = a[n - 1];
	for (inti = n - 1; i >= 0; i = i- 5 -2) {
		if (temp != a[i]) {
		}
	}
	system("pause");}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("ii",IntType())],VoidType(),Block([VarDecl("n",IntType()),VarDecl("x",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("n"),Id("x"))),Block([])),BinaryOp("=",Id("temp"),ArrayCell(Id("a"),BinaryOp("-",Id("n"),IntLiteral(1)))),For(BinaryOp("=",Id("inti"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("-",Id("i"),IntLiteral(5)),IntLiteral(2))),Block([If(BinaryOp("!=",Id("temp"),ArrayCell(Id("a"),Id("i"))),Block([]))])),CallExpr(Id("system"),[StringLiteral("pause")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_call_without_parameter_22(self):
        input = """float ok(int ii[]) {
	for (i = 0; i < n; i = n + x) {
	}
	for (inti = n - 1; i >= 0; i = i- 5 -2) {
		if (temp != a[i]) {
            break;
		}
        else
            continue;
	}
	system("pause");}"""
        expect = str(Program([FuncDecl(Id("ok"),[VarDecl("ii",ArrayPointerType(IntType()))],FloatType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("n"),Id("x"))),Block([])),For(BinaryOp("=",Id("inti"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("-",Id("i"),IntLiteral(5)),IntLiteral(2))),Block([If(BinaryOp("!=",Id("temp"),ArrayCell(Id("a"),Id("i"))),Block([Break()]),Continue())])),CallExpr(Id("system"),[StringLiteral("pause")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_call_without_parameter_23(self):
        input = """void interface() {
	temp = a[n - 1];
    interfce();
	for (inti = n - 1; i >= 0; i = i- 5 -2) {
		if (temp != a[i]) {
		}
	}}"""
        expect = str(Program([FuncDecl(Id("interface"),[],VoidType(),Block([BinaryOp("=",Id("temp"),ArrayCell(Id("a"),BinaryOp("-",Id("n"),IntLiteral(1)))),CallExpr(Id("interfce"),[]),For(BinaryOp("=",Id("inti"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("-",Id("i"),IntLiteral(5)),IntLiteral(2))),Block([If(BinaryOp("!=",Id("temp"),ArrayCell(Id("a"),Id("i"))),Block([]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_call_without_parameter_24(self):
        input = """int res(int n) {
	    if (n < 10) return max(1,n);
	    return max((n % 10)*res(n / 10), 9 * res((n / 10) - 1));
        }

        int main() {
	        int n;
	        system("pause");
        }"""
        expect = str(Program([FuncDecl(Id("res"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("<",Id("n"),IntLiteral(10)),Return(CallExpr(Id("max"),[IntLiteral(1),Id("n")]))),Return(CallExpr(Id("max"),[BinaryOp("*",BinaryOp("%",Id("n"),IntLiteral(10)),CallExpr(Id("res"),[BinaryOp("/",Id("n"),IntLiteral(10))])),BinaryOp("*",IntLiteral(9),CallExpr(Id("res"),[BinaryOp("-",BinaryOp("/",Id("n"),IntLiteral(10)),IntLiteral(1))]))]))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("system"),[StringLiteral("pause")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_call_without_parameter_25(self):
        input = """int res(int n) {
	    if (n < 10) return max(1,n);
	    return max((n % 10)*res(n / 10), 9 * res((n / 10) - 1));
        do {
	        int n;
	        system("pause");
        }
        while main;
        } """
        expect = str(Program([FuncDecl(Id("res"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("<",Id("n"),IntLiteral(10)),Return(CallExpr(Id("max"),[IntLiteral(1),Id("n")]))),Return(CallExpr(Id("max"),[BinaryOp("*",BinaryOp("%",Id("n"),IntLiteral(10)),CallExpr(Id("res"),[BinaryOp("/",Id("n"),IntLiteral(10))])),BinaryOp("*",IntLiteral(9),CallExpr(Id("res"),[BinaryOp("-",BinaryOp("/",Id("n"),IntLiteral(10)),IntLiteral(1))]))])),Dowhile([Block([VarDecl("n",IntType()),CallExpr(Id("system"),[StringLiteral("pause")])])],Id("main"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    
    def test_call_without_parameter_26(self):
        input = """void main() {
	        int n5555;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n5555",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_call_without_parameter_27(self):
        input = """int main() {
	    float sum;
	    string s;
	    for (i = 0; i < n; i=55) {
		    cin(s);
		    sort(sbegin, send);
		    if (s_length == 1) {
		    }
		    else {
			    for (j = 0; j < slength- 1; j = 5) {
			        if (s[j] != s[j + 1] - 1) {
			        	cout("no");
				        break;
				    }
				    if (j == s_length - 2) {
				    	cout("Yes");
				    }
		        }
            }
	    }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("sum",FloatType()),VarDecl("s",StringType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(55)),Block([CallExpr(Id("cin"),[Id("s")]),CallExpr(Id("sort"),[Id("sbegin"),Id("send")]),If(BinaryOp("==",Id("s_length"),IntLiteral(1)),Block([]),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",Id("slength"),IntLiteral(1))),BinaryOp("=",Id("j"),IntLiteral(5)),Block([If(BinaryOp("!=",ArrayCell(Id("s"),Id("j")),BinaryOp("-",ArrayCell(Id("s"),BinaryOp("+",Id("j"),IntLiteral(1))),IntLiteral(1))),Block([CallExpr(Id("cout"),[StringLiteral("no")]),Break()])),If(BinaryOp("==",Id("j"),BinaryOp("-",Id("s_length"),IntLiteral(2))),Block([CallExpr(Id("cout"),[StringLiteral("Yes")])]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_call_without_parameter_28(self):
        input = """float[] main(float f, int i, int k[]) {
	    for (i = 0; i < n; i=55) {
		    if (true) {
			    for (j = 0; j < s_length() - 1; j = 5) {
			        if (s[j] >= s[j + 1] - 1) {
				    }
		        }
            }
	    }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("f",FloatType()),VarDecl("i",IntType()),VarDecl("k",ArrayPointerType(IntType()))],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(55)),Block([If(BooleanLiteral(True),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",CallExpr(Id("s_length"),[]),IntLiteral(1))),BinaryOp("=",Id("j"),IntLiteral(5)),Block([If(BinaryOp(">=",ArrayCell(Id("s"),Id("j")),BinaryOp("-",ArrayCell(Id("s"),BinaryOp("+",Id("j"),IntLiteral(1))),IntLiteral(1))),Block([]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_call_without_parameter_29(self):
        input = """int main() {
	    float sum;
	    /*string s;
	    for (i = 0; i < n; i=55) {
		    cin(s);
		    sort(sbegin, send);
		    if (s_length == 1) {
		    }
		    else {
			    for (j = 0; j < slength- 1; j = 5) {
			        
				    }
				    if (j == s_length - 2) {
				    	cout("Yes");
				    }
		        }
            }
	    }*/
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("sum",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_call_without_parameter_30(self):
        input = """
        void main(){}
        string[] main(string main[]) {
	    for (i = 0; i < n; i=55) {
			    for (j = 0; j < slength * s() - 1; j = 5) {
			        if (s[j] != s[j + 1] - 1) {
			        	cout("no");
				        break;
				    }
				    if (j == s_length - 2) {
				    	cout("Yes");
				    }
		        }   
	    }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("main"),[VarDecl("main",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(55)),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",BinaryOp("*",Id("slength"),CallExpr(Id("s"),[])),IntLiteral(1))),BinaryOp("=",Id("j"),IntLiteral(5)),Block([If(BinaryOp("!=",ArrayCell(Id("s"),Id("j")),BinaryOp("-",ArrayCell(Id("s"),BinaryOp("+",Id("j"),IntLiteral(1))),IntLiteral(1))),Block([CallExpr(Id("cout"),[StringLiteral("no")]),Break()])),If(BinaryOp("==",Id("j"),BinaryOp("-",Id("s_length"),IntLiteral(2))),Block([CallExpr(Id("cout"),[StringLiteral("Yes")])]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
    def test_call_without_parameter_31(self):
        input = """int main() {
	int a[2001];
	len_a = 0;
	int b[2001];
	len_b = 0;
	int s;
	res = 0;
	for ( i = 0; i < n; i = 9) {
		if (s % 2 == 0) {
			a[len_a] = s;
		}
		else {
			b[len_b = len_b + 5] = s;
		}
	}
	sort(a, a + len_a);
	sort(b, b + len_b);
	if (abs(len_b - len_a) == 1) {
	}
	else if (len_b > len_a) {
		temp = len_b - len_a - 1;
		for (i = 0; i < temp; i = 5) {
			res = b[i];
		}
	}
	else if (len_a > len_b) {
		temp = len_a - len_b - 1;
		for (i = 0; i < temp; i = 1 -2) {
			res = a[i];
		}
	}
	else if (len_a == len_b) {
	}
	else {
		res = min(a[0], b[0]);
		
	}
	system("pause");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(2001,IntType())),BinaryOp("=",Id("len_a"),IntLiteral(0)),VarDecl("b",ArrayType(2001,IntType())),BinaryOp("=",Id("len_b"),IntLiteral(0)),VarDecl("s",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(9)),Block([If(BinaryOp("==",BinaryOp("%",Id("s"),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("a"),Id("len_a")),Id("s"))]),Block([BinaryOp("=",ArrayCell(Id("b"),BinaryOp("=",Id("len_b"),BinaryOp("+",Id("len_b"),IntLiteral(5)))),Id("s"))]))])),CallExpr(Id("sort"),[Id("a"),BinaryOp("+",Id("a"),Id("len_a"))]),CallExpr(Id("sort"),[Id("b"),BinaryOp("+",Id("b"),Id("len_b"))]),If(BinaryOp("==",CallExpr(Id("abs"),[BinaryOp("-",Id("len_b"),Id("len_a"))]),IntLiteral(1)),Block([]),If(BinaryOp(">",Id("len_b"),Id("len_a")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_b"),Id("len_a")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),IntLiteral(5)),Block([BinaryOp("=",Id("res"),ArrayCell(Id("b"),Id("i")))]))]),If(BinaryOp(">",Id("len_a"),Id("len_b")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_a"),Id("len_b")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),Block([BinaryOp("=",Id("res"),ArrayCell(Id("a"),Id("i")))]))]),If(BinaryOp("==",Id("len_a"),Id("len_b")),Block([]),Block([BinaryOp("=",Id("res"),CallExpr(Id("min"),[ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("b"),IntLiteral(0))]))]))))),CallExpr(Id("system"),[StringLiteral("pause")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_call_without_parameter_32(self):
        input = """int main() {
	/*int a[2001];
	len_a = 0;
	int b[2001];
	len_b = 0;
	int s;
	res = 0;*/
	for ( i = 0; i < n; i = 9) {
		if (s % 2 == 0) {
			a[len_a] = s;
		}
		else {
			b[len_b = len_b + 5] = s;
		}
	}
	sort(a, a + len_a);
	sort(b, b + len_b);
	if (abs(len_b - len_a) == 1) {
	}
	else if (len_b > len_a) {
		temp = len_b - len_a - 1;
		for (i = 0; i < temp; i = 5) {
			res = b[i];
		}
	}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(9)),Block([If(BinaryOp("==",BinaryOp("%",Id("s"),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("a"),Id("len_a")),Id("s"))]),Block([BinaryOp("=",ArrayCell(Id("b"),BinaryOp("=",Id("len_b"),BinaryOp("+",Id("len_b"),IntLiteral(5)))),Id("s"))]))])),CallExpr(Id("sort"),[Id("a"),BinaryOp("+",Id("a"),Id("len_a"))]),CallExpr(Id("sort"),[Id("b"),BinaryOp("+",Id("b"),Id("len_b"))]),If(BinaryOp("==",CallExpr(Id("abs"),[BinaryOp("-",Id("len_b"),Id("len_a"))]),IntLiteral(1)),Block([]),If(BinaryOp(">",Id("len_b"),Id("len_a")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_b"),Id("len_a")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),IntLiteral(5)),Block([BinaryOp("=",Id("res"),ArrayCell(Id("b"),Id("i")))]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_call_without_parameter_33(self):
        input = """int[] mn(int o[]) {
	
	if (abs(len_b - len_a) == 1) {
	}
	else if (len_b > len_a) {
		temp = len_b - len_a - 1;
		for (i = 0; i < temp; i = 5) {
			res = b[i];
		}
	}
	else if (len_a > len_b) {
		temp = len_a - len_b - 1;
		for (i = 0; i < temp; i = 1 -2) {
			res = a[i];
		}
	}
	else if (len_a == len_b) {
	}
	else {
		res = min(a[0], b[0]);	
	}
        }"""
        expect = str(Program([FuncDecl(Id("mn"),[VarDecl("o",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([If(BinaryOp("==",CallExpr(Id("abs"),[BinaryOp("-",Id("len_b"),Id("len_a"))]),IntLiteral(1)),Block([]),If(BinaryOp(">",Id("len_b"),Id("len_a")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_b"),Id("len_a")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),IntLiteral(5)),Block([BinaryOp("=",Id("res"),ArrayCell(Id("b"),Id("i")))]))]),If(BinaryOp(">",Id("len_a"),Id("len_b")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_a"),Id("len_b")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),Block([BinaryOp("=",Id("res"),ArrayCell(Id("a"),Id("i")))]))]),If(BinaryOp("==",Id("len_a"),Id("len_b")),Block([]),Block([BinaryOp("=",Id("res"),CallExpr(Id("min"),[ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("b"),IntLiteral(0))]))])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_call_without_parameter_34(self):
        input = """int main() {
	int a[2001];
	int s;
	res = 0;
	for ( i = 0; i < n; i = 9) {
		if (s % 2 == 0) {
			a[len_a] = s;
		}
		else {
			b[len_b = len_b + 5] = s;
		}
	}
	sort(a, a + len_a);
	sort(b, b + len_b);
	if (abs(len_b - len_a) == 1) {
	}
	else if (len_b > len_a) {
		temp = len_b - len_a - 1;
		for (i = 0; i < temp; i = 5) {
			res = b[i];
		}
	}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(2001,IntType())),VarDecl("s",IntType()),BinaryOp("=",Id("res"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),IntLiteral(9)),Block([If(BinaryOp("==",BinaryOp("%",Id("s"),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("a"),Id("len_a")),Id("s"))]),Block([BinaryOp("=",ArrayCell(Id("b"),BinaryOp("=",Id("len_b"),BinaryOp("+",Id("len_b"),IntLiteral(5)))),Id("s"))]))])),CallExpr(Id("sort"),[Id("a"),BinaryOp("+",Id("a"),Id("len_a"))]),CallExpr(Id("sort"),[Id("b"),BinaryOp("+",Id("b"),Id("len_b"))]),If(BinaryOp("==",CallExpr(Id("abs"),[BinaryOp("-",Id("len_b"),Id("len_a"))]),IntLiteral(1)),Block([]),If(BinaryOp(">",Id("len_b"),Id("len_a")),Block([BinaryOp("=",Id("temp"),BinaryOp("-",BinaryOp("-",Id("len_b"),Id("len_a")),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("temp")),BinaryOp("=",Id("i"),IntLiteral(5)),Block([BinaryOp("=",Id("res"),ArrayCell(Id("b"),Id("i")))]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_call_without_parameter_35(self):
        input = """int revire() {
	int a[2001];
	len_a = 0;
	int b[2001];
	
	sort(a, a + len_a);
	sort(b, b + len_b);
    }
	"""
        expect = str(Program([FuncDecl(Id("revire"),[],IntType(),Block([VarDecl("a",ArrayType(2001,IntType())),BinaryOp("=",Id("len_a"),IntLiteral(0)),VarDecl("b",ArrayType(2001,IntType())),CallExpr(Id("sort"),[Id("a"),BinaryOp("+",Id("a"),Id("len_a"))]),CallExpr(Id("sort"),[Id("b"),BinaryOp("+",Id("b"),Id("len_b"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
    def test_call_without_parameter_36(self):
        input = """void ndhnam(){
            int a[16];
	for (i = 0; i < n; i=i+1) {
	}
	/*
	for (i = n; i > 0; i = i/2) {
		for	system("pause");
			}
		}
	}
	*/
	res = 1;
	for (i = 2; i <= n; i = i * 2) {
		for (j = 0; j < n; j = j + i) {
			if (is_sorted(a + j, a + j + i)) {
				res = max(res, i);
			}
		}
	}
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[],VoidType(),Block([VarDecl("a",ArrayType(16,IntType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])),BinaryOp("=",Id("res"),IntLiteral(1)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),Id("i"))),Block([If(CallExpr(Id("is_sorted"),[BinaryOp("+",Id("a"),Id("j")),BinaryOp("+",BinaryOp("+",Id("a"),Id("j")),Id("i"))]),Block([BinaryOp("=",Id("res"),CallExpr(Id("max"),[Id("res"),Id("i")]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_call_without_parameter_37(self):
        input = """void ndhnam(){
            int arrrr[16];
	for (i = 0; i < n; i=i+1) {
	}
	
	for (i = n; i > 0; i = i/2) {
		for (j = 0; j < n; j= j +i) {
			if (is_sorted(a + j, a + j + i)) {
				system("pause");
			}
		}
	}
	res = 1;
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[],VoidType(),Block([VarDecl("arrrr",ArrayType(16,IntType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])),For(BinaryOp("=",Id("i"),Id("n")),BinaryOp(">",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("/",Id("i"),IntLiteral(2))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),Id("i"))),Block([If(CallExpr(Id("is_sorted"),[BinaryOp("+",Id("a"),Id("j")),BinaryOp("+",BinaryOp("+",Id("a"),Id("j")),Id("i"))]),Block([CallExpr(Id("system"),[StringLiteral("pause")])]))]))])),BinaryOp("=",Id("res"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_call_without_parameter_38(self):
        input = """void ndhnam(){
	for (i = n; i > 0; i = i/2) {
		for (j = 0; j < n; j= j +i) {
			if (is_sorted(a + j, a + j + i)) {
				system("pause");
			}
		}
	}
	res = 1;
	for (i = 2; i <= n; i = i * 2) {
		for (j = 0; j < n; j = j + i) {
			if (is_sorted(a + j, a + j + i)) {
				res = max(res, i);
			}
		}
	}
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),Id("n")),BinaryOp(">",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("/",Id("i"),IntLiteral(2))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),Id("i"))),Block([If(CallExpr(Id("is_sorted"),[BinaryOp("+",Id("a"),Id("j")),BinaryOp("+",BinaryOp("+",Id("a"),Id("j")),Id("i"))]),Block([CallExpr(Id("system"),[StringLiteral("pause")])]))]))])),BinaryOp("=",Id("res"),IntLiteral(1)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),Id("i"))),Block([If(CallExpr(Id("is_sorted"),[BinaryOp("+",Id("a"),Id("j")),BinaryOp("+",BinaryOp("+",Id("a"),Id("j")),Id("i"))]),Block([BinaryOp("=",Id("res"),CallExpr(Id("max"),[Id("res"),Id("i")]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_call_without_parameter_39(self):
        input = """string hello(string myname){
            print(myname ,"hello");
        }"""
        expect = str(Program([FuncDecl(Id("hello"),[VarDecl("myname",StringType())],StringType(),Block([CallExpr(Id("print"),[Id("myname"),StringLiteral("hello")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_call_without_parameter_40(self):
        input = """void ndhnam(int birthday, int MSSV){
            ndhnam("NguyenDangHaNam", 1710195);
            print("OKAY");
        }"""
        expect = str(Program([FuncDecl(Id("ndhnam"),[VarDecl("birthday",IntType()),VarDecl("MSSV",IntType())],VoidType(),Block([CallExpr(Id("ndhnam"),[StringLiteral("NguyenDangHaNam"),IntLiteral(1710195)]),CallExpr(Id("print"),[StringLiteral("OKAY")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
