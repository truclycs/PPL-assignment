##################################
# Ho va ten :   Nguyen Minh Tien #
# MSSV      :   1713484          #
##################################

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        """Test 300"""
        input    = """
        void main(int x, float y, boolean z) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",FloatType()),VarDecl("z",BoolType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_301(self):
        """Test 301"""
        input    = """
        void main() {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_302(self):
        """Test 302"""
        input    = """
        int main() {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_303(self):
        """Test 303"""
        input    = """
        int main;
        """
        expect   = str(Program([VarDecl("main",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_304(self):
        """Test 304"""
        input    = """
        int _int;
        """
        expect   = str(Program([VarDecl("_int",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_305(self):
        """Test 305"""
        input    = """
        float f;
        """
        expect   = str(Program([VarDecl("f",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_306(self):
        """Test 306"""
        input    = """
        string s;
        """
        expect   = str(Program([VarDecl("s",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_307(self):
        """Test 307"""
        input    = """
        boolean b;
        """
        expect   = str(Program([VarDecl("b",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_308(self):
        """Test 308"""
        input    = """
        int a[1];
        """
        expect   = str(Program([VarDecl("a",ArrayType(1,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_309(self):
        """Test 309"""
        input    = """
        int a;
        int b;
        """
        expect   = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_310(self):
        """Test 310"""
        input    = """
        int a[10];
        boolean b;
        float f;
        """
        expect   = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",BoolType()),VarDecl("f",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_311(self):
        """Test 311"""
        input    = """
        boolean isEqual(int a, int b){
            return a == b;
        }
        """
        expect   = str(Program([FuncDecl(Id("isEqual"),[VarDecl("a",IntType()),VarDecl("b",IntType())],BoolType(),Block([Return(BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_312(self):
        """Test 312"""
        input    = """
        int plus(int a, int b) {
            return a + b;
        }
        """
        expect   = str(Program([FuncDecl(Id("plus"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_313(self):
        """Test 313"""
        input    = """
        float delta(int a, int b, int c){
    		return b * b - 4 * a * c;
    	}
        """
        expect   = str(Program([FuncDecl(Id("delta"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],FloatType(),Block([Return(BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_314(self):
        """Test 314"""
        input    = """
        void main() {
            int i;
            float f;
            string s;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("f",FloatType()),VarDecl("s",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_315(self):
        """Test 315"""
        input    = """
        int foo(int a) {
            if (a == 0)
            a = 1;
        }
        """
        expect   = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_316(self):
        """Test 316"""
        input    = """
        int foo2(int a) {
            if (a == 0)
                a = 1;
            else
                a = 2;
        }
        """
        expect   = str(Program([FuncDecl(Id("foo2"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_317(self):
        """Test 317"""
        input    = """
        int f(int a) {
    		do
                decrease(a);
    		while (a > 0);
    	}
        """
        expect   = str(Program([FuncDecl(Id("f"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([CallExpr(Id("decrease"),[Id("a")])],BinaryOp(">",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_318(self):
        """Test 318"""
        input    = """
        int main() {
            int a;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_319(self):
        """Test 319"""
        input    = """
        int main() {
            int a[10];
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_320(self):
        """Test 320"""
        input    = """
        int main() {
            break;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_321(self):
        """Test 321"""
        input    = """
        int main() {
            continue;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_322(self):
        """Test 322"""
        input    = """
        int main() {
            return ret;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(Id("ret"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_323(self):
        """Test 323"""
        input    = """
        void main() {
            return;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_324(self):
        """Test 324"""
        input    = """
        int main() {
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_325(self):
        """Test 325"""
        input    = """
        int main() {
            /*
            Than ham main trong
            */
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_326(self):
        """Test 326"""
        input    = """
        int main() {
            if (x >= y)
                printf(x);
            else
                printf(y);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">=",Id("x"),Id("y")),CallExpr(Id("printf"),[Id("x")]),CallExpr(Id("printf"),[Id("y")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_327(self):
        """Test 327"""
        input    = """
        int main() {
            printf("int main() { printf(\\"Hello World\\");return 0;}");
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("int main() { printf(\\\"Hello World\\\");return 0;}")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_328(self):
        """Test 328"""
        input    = """
        // Khong co gi o day
        int main() {/* Cung khong co gi o day */}
        // Cung khong co gi o day
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_329(self):
        """Test 329"""
        input    = """
        int findMax(int x, int y){
            if (x > y)
                return x;
            else
                return y;
        }
        """
        expect   = str(Program([FuncDecl(Id("findMax"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([If(BinaryOp(">",Id("x"),Id("y")),Return(Id("x")),Return(Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_330(self):
        """Test 330"""
        input    = """
        int findMin(int x, int y){
            if (x < y)
                return x;
            else
                return y;
        }
        """
        expect   = str(Program([FuncDecl(Id("findMin"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([If(BinaryOp("<",Id("x"),Id("y")),Return(Id("x")),Return(Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_331(self):
        """Test 331"""
        input    = """
        int abc_xyz() {
            printf("abc_xyz");
        }
        """
        expect   = str(Program([FuncDecl(Id("abc_xyz"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("abc_xyz")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_332(self):
        """Test 332"""
        input    = """
        string convertIntToStr(int x) {
            string s;
            boolean neg;
            s = "";
            if (x < 0)
                neg = true;
            else
                neg = false;
            do {
                s = s + toChar(x % 10);
                x = x / 10;
            } while (x != 0);
            if (neg) {
                s = "-" + s;
            }
            return s;
        }
        """
        expect   = str(Program([FuncDecl(Id("convertIntToStr"),[VarDecl("x",IntType())],StringType(),Block([VarDecl("s",StringType()),VarDecl("neg",BoolType()),BinaryOp("=",Id("s"),StringLiteral("")),If(BinaryOp("<",Id("x"),IntLiteral(0)),BinaryOp("=",Id("neg"),BooleanLiteral("true")),BinaryOp("=",Id("neg"),BooleanLiteral("false"))),Dowhile([Block([BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),CallExpr(Id("toChar"),[BinaryOp("%",Id("x"),IntLiteral(10))]))),BinaryOp("=",Id("x"),BinaryOp("/",Id("x"),IntLiteral(10)))])],BinaryOp("!=",Id("x"),IntLiteral(0))),If(Id("neg"),Block([BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("-"),Id("s")))])),Return(Id("s"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_333(self):
        """Test 333"""
        input    = """
        boolean isLeapYear(int y) {
            if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0)
                return true;
            else
                return false;
        }
        """
        expect   = str(Program([FuncDecl(Id("isLeapYear"),[VarDecl("y",IntType())],BoolType(),Block([If(BinaryOp("||",BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("y"),IntLiteral(4)),IntLiteral(0)),BinaryOp("!=",BinaryOp("%",Id("y"),IntLiteral(100)),IntLiteral(0))),BinaryOp("==",BinaryOp("%",Id("y"),IntLiteral(400)),IntLiteral(0))),Return(BooleanLiteral("true")),Return(BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_334(self):
        """Test 334"""
        input    = """
        int foo(int a) {
    		do
                decrease(a);
                b = a;
                return a;
    		while (a > 0);
    	}
        """
        expect   = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([CallExpr(Id("decrease"),[Id("a")]),BinaryOp("=",Id("b"),Id("a")),Return(Id("a"))],BinaryOp(">",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_335(self):
        """Test 335"""
        input    = """
        void main() {
            for (i = 0; i; i)
                f;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),Id("i"),Id("i"),Id("f"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_336(self):
        """Test 336"""
        input    = """
        int main() {
            a = b;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_337(self):
        """Test 337"""
        input    = """
        int main() {
            for(i;i;i)
                f();
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("i"),Id("i"),CallExpr(Id("f"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_338(self):
        """Test 338"""
        input    = """
        int main() {
            init(a[10]);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("init"),[ArrayCell(Id("a"),IntLiteral(10))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_339(self):
        """Test 339"""
        input    = """
        int[] a() {}
        """
        expect   = str(Program([FuncDecl(Id("a"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_340(self):
        """Test 340"""
        input    = """
        int[] f(int a[]) {}
        """
        expect   = str(Program([FuncDecl(Id("f"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_341(self):
        """Test 341"""
        input    = """
        int countChar(string s) {
            int x;
            x = 0;
            string c;
            do {
                c = s[x];
                x = x + 1;
            } while (c != "");
            return x;
        }
        """
        expect   = str(Program([FuncDecl(Id("countChar"),[VarDecl("s",StringType())],IntType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(0)),VarDecl("c",StringType()),Dowhile([Block([BinaryOp("=",Id("c"),ArrayCell(Id("s"),Id("x"))),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],BinaryOp("!=",Id("c"),StringLiteral(""))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_342(self):
        """Test 342"""
        input    = """
        int countCharArray(string s[]) {
            int x;
            x = 0;
            string c;
            do {
                c = s[x];
                x = x + 1;
            } while (c != "");
            return x;
        }
        """
        expect   = str(Program([FuncDecl(Id("countCharArray"),[VarDecl("s",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(0)),VarDecl("c",StringType()),Dowhile([Block([BinaryOp("=",Id("c"),ArrayCell(Id("s"),Id("x"))),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],BinaryOp("!=",Id("c"),StringLiteral(""))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_343(self):
        """Test 343"""
        input    = """
        void joke() {
            printf("Error 404: Not found!\\n");
        }
        """
        expect   = str(Program([FuncDecl(Id("joke"),[],VoidType(),Block([CallExpr(Id("printf"),[StringLiteral("Error 404: Not found!\\n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_344(self):
        """Test 344"""
        input    = """
        void joke() {
            perror("Error 404: Not found!\\n");
        }
        """
        expect   = str(Program([FuncDecl(Id("joke"),[],VoidType(),Block([CallExpr(Id("perror"),[StringLiteral("Error 404: Not found!\\n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_345(self):
        """Test 345"""
        input    = """
        int main() {
            int a, b, c;
            return f(a, b, c);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Return(CallExpr(Id("f"),[Id("a"),Id("b"),Id("c")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_346(self):
        """Test 346"""
        input    = """
        int main() {
            string s;
            int i, n;
            for (i = 0; i < n; i = i + 1) {
                printf(s[i]);
            }
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",StringType()),VarDecl("i",IntType()),VarDecl("n",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[ArrayCell(Id("s"),Id("i"))])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_347(self):
        """Test 347"""
        input    = """
        float main() {
            float pi;
            pi = 3.14159;
            return pi;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([VarDecl("pi",FloatType()),BinaryOp("=",Id("pi"),FloatLiteral(3.14159)),Return(Id("pi"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_348(self):
        """Test 348"""
        input    = """
        boolean main() {
            int x, y;
            if (x == y)
                return true;
            else
                return false;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],BoolType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),If(BinaryOp("==",Id("x"),Id("y")),Return(BooleanLiteral("true")),Return(BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_349(self):
        """Test 349"""
        input    = """
        int lcm(int x, int y) {
            int i, min;
            if (x < y)
                min = x;
            else
                min = y;
            for (i = 0; i < min; i = i + 1)
                if (x % i == 0 && y % i == 0)
                    return i;
        }
        """
        expect   = str(Program([FuncDecl(Id("lcm"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([VarDecl("i",IntType()),VarDecl("min",IntType()),If(BinaryOp("<",Id("x"),Id("y")),BinaryOp("=",Id("min"),Id("x")),BinaryOp("=",Id("min"),Id("y"))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("min")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("x"),Id("i")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("y"),Id("i")),IntLiteral(0))),Return(Id("i"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_350(self):
        """Test 350"""
        input    = """
        int gcd(int x, int y) {
            int i, max;
            if (x > y)
                max = x;
            else
                max = y;
            int i;
            for (i = max; i < x * y; i = i + 1)
                if (i % a == 0 && i % b == 0)
                    return i;
        }
        """
        expect   = str(Program([FuncDecl(Id("gcd"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([VarDecl("i",IntType()),VarDecl("max",IntType()),If(BinaryOp(">",Id("x"),Id("y")),BinaryOp("=",Id("max"),Id("x")),BinaryOp("=",Id("max"),Id("y"))),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),Id("max")),BinaryOp("<",Id("i"),BinaryOp("*",Id("x"),Id("y"))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("i"),Id("a")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("i"),Id("b")),IntLiteral(0))),Return(Id("i"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_351(self):
        """Test 351"""
        input    = """
        int gcd(int x, int y) {
            if (y == 0)
                return x;
            else
                return gcd(y, x % y);
        }
        """
        expect   = str(Program([FuncDecl(Id("gcd"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([If(BinaryOp("==",Id("y"),IntLiteral(0)),Return(Id("x")),Return(CallExpr(Id("gcd"),[Id("y"),BinaryOp("%",Id("x"),Id("y"))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_352(self):
        """Test 352"""
        input    = """
        int cntStr(string s) {
            int i;
            i = 0;
            do {
                i = i + 1;
            } while (a[i] != NULL);
            return i;
        }
        """
        expect   = str(Program([FuncDecl(Id("cntStr"),[VarDecl("s",StringType())],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],BinaryOp("!=",ArrayCell(Id("a"),Id("i")),Id("NULL"))),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_353(self):
        """Test 353"""
        input    = """
        int fibo(int n) {
            if (n == 0)
                return 1;
            else
                return fibo(n - 1) * n;
        }
        """
        expect   = str(Program([FuncDecl(Id("fibo"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(0)),Return(IntLiteral(1)),Return(BinaryOp("*",CallExpr(Id("fibo"),[BinaryOp("-",Id("n"),IntLiteral(1))]),Id("n"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_354(self):
        """Test 354"""
        input    = """
        int foo(int i) {
    		do
                for (i = 0; i; i)
                    f;
    		while (i > 0);
    	}
        """
        expect   = str(Program([FuncDecl(Id("foo"),[VarDecl("i",IntType())],IntType(),Block([Dowhile([For(BinaryOp("=",Id("i"),IntLiteral(0)),Id("i"),Id("i"),Id("f"))],BinaryOp(">",Id("i"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_355(self):
        """Test 355"""
        input    = """
        int a, b, c[10]; // Bien toan cuc
        int main() {
            /* phan khai bao */
            float f;
            int a, b, c[10]; // Bien cuc bo
            // Phan thuc thi
            f = 1.0;
            foo(1, 2);
            e + 1;
            10;
        }
        """
        expect   = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("f",FloatType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType())),BinaryOp("=",Id("f"),FloatLiteral(1.0)),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("+",Id("e"),IntLiteral(1)),IntLiteral(10)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_356(self):
        """Test 356"""
        input    = """
        int a, b;
        int main() {
            if (a > b)
                a = a + b;
            else
                b = a + b;
            return (a + b) / 2;
        }
        """
        expect   = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("b"))),BinaryOp("=",Id("b"),BinaryOp("+",Id("a"),Id("b")))),Return(BinaryOp("/",BinaryOp("+",Id("a"),Id("b")),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_357(self):
        """Test 357"""
        input    = """
        int sum(int a, int b) {
            return a + b;
        }
        """
        expect   = str(Program([FuncDecl(Id("sum"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_358(self):
        """Test 358"""
        input    = """
        int sub(int a, int b) {
            return a - b;
        }
        """
        expect   = str(Program([FuncDecl(Id("sub"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("-",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_359(self):
        """Test 359"""
        input    = """
        string main(int a[], boolean b, float c) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",BoolType()),VarDecl("c",FloatType())],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_360(self):
        """Test 360"""
        input    = """
        float mul(int a, int b) {
            return a * b;
        }
        """
        expect   = str(Program([FuncDecl(Id("mul"),[VarDecl("a",IntType()),VarDecl("b",IntType())],FloatType(),Block([Return(BinaryOp("*",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_361(self):
        """Test 361"""
        input    = """
        string s() {
            return "Toi yeu Bach Khoa";
        }
        """
        expect   = str(Program([FuncDecl(Id("s"),[],StringType(),Block([Return(StringLiteral("Toi yeu Bach Khoa"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_362(self):
        """Test 362"""
        input    = """
        void foo() {
            // Than ham rong
            return 0; // Bao loi
        }
        """
        expect   = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_363(self):
        """Test 363"""
        input    = """
        void main() {
            int a, b;
            if (a > b)
                a = a + 1;
            findnumber(a);
            if (a == 1)
                {}
            else if (a == b)
                {}
            else
                {}
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))),CallExpr(Id("findnumber"),[Id("a")]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([]),If(BinaryOp("==",Id("a"),Id("b")),Block([]),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_364(self):
        """Test 364"""
        input    = """
        int foo(int a, int b, int c) {
            a = 10;
            f = 1.1;
            s = "I <3 U";
        }
        """
        expect   = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],IntType(),Block([BinaryOp("=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("f"),FloatLiteral(1.1)),BinaryOp("=",Id("s"),StringLiteral("I <3 U"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_365(self):
        """Test 365"""
        input    = """
        void cuoc_song_lap_trinh() {
            an();
            ngu();
            code();
        }
        """
        expect   = str(Program([FuncDecl(Id("cuoc_song_lap_trinh"),[],VoidType(),Block([CallExpr(Id("an"),[]),CallExpr(Id("ngu"),[]),CallExpr(Id("code"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_366(self):
        """Test 366"""
        input    = """
    	void main() {
       		print("Hello World!\\n");
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Hello World!\\n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_367(self):
        """Test 367"""
        input    = """
        boolean main() {
            int a;
            if (a % 2 == 0)
                return 1;
            else
                return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],BoolType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(2)),IntLiteral(0)),Return(IntLiteral(1)),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_368(self):
        """Test 368"""
        input    = """
        int main() {
            int x;
            x = 0;
            do {
                x = x + 1;
                printf("%d", x);
            } while (x < 10);
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(0)),Dowhile([Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("%d"),Id("x")])])],BinaryOp("<",Id("x"),IntLiteral(10))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_369(self):
        """Test 369"""
        input    = """
        int main() {
            int x;
            x = 0;
            do {
                printf("%d", x);
                x = x + 1;
                if (x >= 10)
                    break;
            } while(true);
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(0)),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("%d"),Id("x")]),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),If(BinaryOp(">=",Id("x"),IntLiteral(10)),Break())])],BooleanLiteral("true")),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_370(self):
        """Test 370"""
        input    = """
        void main() {
            f(a[10]);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("f"),[ArrayCell(Id("a"),IntLiteral(10))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_371(self):
        """Test 371"""
        input    = """
        float main() {
            float f;
            f = 10e10;
            return f;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([VarDecl("f",FloatType()),BinaryOp("=",Id("f"),FloatLiteral(100000000000.0)),Return(Id("f"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_372(self):
        """Test 372"""
        input    = """
        int main() {}
        int a, b;
        void f() {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",IntType()),VarDecl("b",IntType()),FuncDecl(Id("f"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_373(self):
        """Test 373"""
        input    = """
        int main(int a[]) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_374(self):
        """Test 374"""
        input    = """
        void main(int a[], float b[]) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType()))],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_375(self):
        """Test 375"""
        input    = """
        float f() {}
        """
        expect   = str(Program([FuncDecl(Id("f"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_376(self):
        """Test 376"""
        input    = """
        string s() {}
        """
        expect   = str(Program([FuncDecl(Id("s"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_377(self):
        """Test 377"""
        input    = """
        boolean b() {}
        """
        expect   = str(Program([FuncDecl(Id("b"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_378(self):
        """Test 378"""
        input    = """
        int a[10];
        int b;
        int c;
        int main() {
            f(a, b, c);
        }
        """
        expect   = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("f"),[Id("a"),Id("b"),Id("c")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_379(self):
        """Test 379"""
        input    = """
        int main() {
            if (thisIsAProgram())
                return 1;
            else
                return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("thisIsAProgram"),[]),Return(IntLiteral(1)),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_380(self):
        """Test 380"""
        input    = """
        string s;
        int main() {
            s = "Day la chuoi se xuat ra man hinh\\n";
            printf(s);
            return 0;
        }
        """
        expect   = str(Program([VarDecl("s",StringType()),FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("s"),StringLiteral("Day la chuoi se xuat ra man hinh\\n")),CallExpr(Id("printf"),[Id("s")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_381(self):
        """Test 381"""
        input    = """
        float delta(int a, int b, int c) {
            return b*b - 4*a*c;
        }
        """
        expect   = str(Program([FuncDecl(Id("delta"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],FloatType(),Block([Return(BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_382(self):
        """Test 382"""
        input    = """
        float x1(int a, int b, float d) {
            return (-b + sqrt(d)) / (2 * a);
        }
        """
        expect   = str(Program([FuncDecl(Id("x1"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("d",FloatType())],FloatType(),Block([Return(BinaryOp("/",BinaryOp("+",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("d")])),BinaryOp("*",IntLiteral(2),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_383(self):
        """Test 383"""
        input    = """
        float x2(int a, int b, float d) {
            return (-b - sqrt(d)) / (2 * a);
        }
        """
        expect   = str(Program([FuncDecl(Id("x2"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("d",FloatType())],FloatType(),Block([Return(BinaryOp("/",BinaryOp("-",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("d")])),BinaryOp("*",IntLiteral(2),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_384(self):
        """Test 384"""
        input    = """
        int countIsLeapYear(int a, int b) {
            int i;
            int count;
            count = 0;
            for (i = a; i <= b; i = i + 1) {
                if (isLeapYear(i))
                    count = count + 1;
            }
            return count;
        }
        """
        expect   = str(Program([FuncDecl(Id("countIsLeapYear"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([VarDecl("i",IntType()),VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),For(BinaryOp("=",Id("i"),Id("a")),BinaryOp("<=",Id("i"),Id("b")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(CallExpr(Id("isLeapYear"),[Id("i")]),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))))])),Return(Id("count"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_385(self):
        """Test 385"""
        input    = """
        int main() {
            int i;
            int count;
            count = 0;
            for (i = 0; i < 1000; i = i + 1) {
                if (isLeapYear(i))
                    count = count + 1;
            }
            return count;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(1000)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(CallExpr(Id("isLeapYear"),[Id("i")]),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))))])),Return(Id("count"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_386(self):
        """Test 386"""
        input    = """
        void main() {
            int a, b, c;
            a = b = c;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_387(self):
        """Test 387"""
        input    = """
        void main() {
            int a;
            a = 1 + 2 + 3;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_388(self):
        """Test 388"""
        input    = """
        void main() {
            delta = b*b - 4*a*c;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("delta"),BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_389(self):
        """Test 389"""
        input    = """
        void main() {
            x1 = (-b + sqrt(delta)) / (2 * a);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("x1"),BinaryOp("/",BinaryOp("+",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("delta")])),BinaryOp("*",IntLiteral(2),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_390(self):
        """Test 390"""
        input    = """
        void main() {
            x2 = (-b - sqrt(delta)) / (2 * a);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("x2"),BinaryOp("/",BinaryOp("-",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("delta")])),BinaryOp("*",IntLiteral(2),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_391(self):
        """Test 391"""
        input    = """
        int a, arr[10];
        """
        expect   = str(Program([VarDecl("a",IntType()),VarDecl("arr",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_392(self):
        """Test 392"""
        input    = """
        void main() {
            int a;
            a = getIntLn();
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("getIntLn"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_393(self):
        """Test 393"""
        input    = """
        int main() {
            putIntLn(10);
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_394(self):
        """Test 394"""
        input    = """
        int main() {
            int i;
            for (i = 0; i < 10; i = i + 1) {
                printf("Hello World!\\n");
            }
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Hello World!\\n")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_395(self):
        """Test 395"""
        input    = """
        string s;
        int main() {
            printf(s);
            return 0;
        }
        """
        expect   = str(Program([VarDecl("s",StringType()),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[Id("s")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_396(self):
        """Test 396"""
        input    = """
        int main() {
            string s;
            s = "Hello World!";
            printf(s);
            return 0;
        }
        """
        expect   = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("Hello World!")),CallExpr(Id("printf"),[Id("s")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_397(self):
        """Test 397"""
        input    = """
        int main(string args) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("args",StringType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_398(self):
        """Test 398"""
        input    = """
        int main(int x) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_399(self):
        """Test 399"""
        input    = """
        int main(int x, int y) {}
        """
        expect   = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))