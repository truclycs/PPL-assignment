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

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_vardecl_3(self):
        input = """
        int a;
        """
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_vardecl_4(self):
        input = """
        float a,b,c[10];
        """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",ArrayType(10,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_vardecl_5(self):
        input = """
        float a,test[4],b;
        string a[1], d[34], c[3];
        """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("test",ArrayType(4,FloatType())),VarDecl("b",FloatType()),VarDecl("a",ArrayType(1,StringType())),VarDecl("d",ArrayType(34,StringType())),VarDecl("c",ArrayType(3,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_vardecl_6(self):
        input = """
        boolean t[5];
        int main(){
            string type;
        }
        """
        expect = str(Program([VarDecl("t",ArrayType(5,BoolType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("type",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
   
    def test_vardecl_7(self):
        input = """
        void func(int a, int b[]){
            float d[4], c[5];
            {
                string c[5];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("d",ArrayType(4,FloatType())),VarDecl("c",ArrayType(5,FloatType())),Block([VarDecl("c",ArrayType(5,StringType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_funcdecl_1(self):
        input = """
        int main(){
            int var[4];
        }
        void func(int a[], string arr){
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("var",ArrayType(4,IntType()))])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("arr",StringType())],VoidType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_funcdecl_2(self):
        input = """
        void main(int argc){
        }
        float exe(string input, boolean flag){
            return 0;
        }
        int test(float input[], int a, string c[], boolean d){
            int a, b[3], c, d[4];
            // Comment
            // int c;
            return a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",IntType())],VoidType(),Block([])),FuncDecl(Id("exe"),[VarDecl("input",StringType()),VarDecl("flag",BoolType())],FloatType(),Block([Return(IntLiteral(0))])),FuncDecl(Id("test"),[VarDecl("input",ArrayPointerType(FloatType())),VarDecl("a",IntType()),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",BoolType())],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(3,IntType())),VarDecl("c",IntType()),VarDecl("d",ArrayType(4,IntType())),Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_funcdecl_3(self):
        input = """
        int main(){
        }
        void func(int a[], string arr){
        }
        int[] calc(int a){
        }
        string[] mult(float arr[]){
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("arr",StringType())],VoidType(),Block([])),FuncDecl(Id("calc"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("mult"),[VarDecl("arr",ArrayPointerType(FloatType()))],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcdecl_4(self):
        input = """
        int[] main(){
        }
        float[] func(int a[], string arr){
        }
        string[] foo(int p[], int v[]){
        }
        boolean[] bool(boolean c[], int d[]){
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("arr",StringType())],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("foo"),[VarDecl("p",ArrayPointerType(IntType())),VarDecl("v",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([])),FuncDecl(Id("bool"),[VarDecl("c",ArrayPointerType(BoolType())),VarDecl("d",ArrayPointerType(IntType()))],ArrayPointerType(BoolType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_blockstmt_1(self):
        input = """
        int main(){
            int a[3], n, b[3];
            1 + 2 = 3;
            {
                int c;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(3,IntType())),VarDecl("n",IntType()),VarDecl("b",ArrayType(3,IntType())),BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Block([VarDecl("c",IntType())])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_blockstmt_2(self):
        input = """
        int val;
        int main(){
            float k;
            {
                float k[3];
                {
                    int t;
                }
            }
            {
                string a[3];
            }
            {
            }
        }
        """
        expect = str(Program([VarDecl("val",IntType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("k",FloatType()),Block([VarDecl("k",ArrayType(3,FloatType())),Block([VarDecl("t",IntType())])]),Block([VarDecl("a",ArrayType(3,StringType()))]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_blockstmt_3(self):
        input = """
        int main(){
            {
                {
                    {
                        {
                            {
                                int t;
                                {
                                    return 0;
                                }
                                1 + 1 = 2;
                            }
                        }
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Block([Block([VarDecl("t",IntType()),Block([Return(IntLiteral(0))]),BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2))])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_blockstmt_4(self):
        input = """
        int main(){
            {
                int c[3];
            }
        }
        float a[4];
        float foo(int c){
            string c[3];
            {
                string d[3];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl("c",ArrayType(3,IntType()))])])),VarDecl("a",ArrayType(4,FloatType())),FuncDecl(Id("foo"),[VarDecl("c",IntType())],FloatType(),Block([VarDecl("c",ArrayType(3,StringType())),Block([VarDecl("d",ArrayType(3,StringType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_blockstmt_5(self):
        input = """
        int main(){
            {
                int y;
            }
            int arr[3], b, lst[3];
            {
                int x;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl("y",IntType())]),VarDecl("arr",ArrayType(3,IntType())),VarDecl("b",IntType()),VarDecl("lst",ArrayType(3,IntType())),Block([VarDecl("x",IntType())])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_ifstmt_1(self):
        input = """
        int main(){
            if (a == 0)
                return 0;
            else
                return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    def test_ifstmt_2(self):
        input = """
        int main(){
            if (1 + 1){
                int c[3];
            }
            else{
                return 0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("+",IntLiteral(1),IntLiteral(1)),Block([VarDecl("c",ArrayType(3,IntType()))]),Block([Return(IntLiteral(0))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_ifstmt_3(self):
        input = """
        int main(){
            if (a + 4){
                if (a == 2) 
                    return 0;
            }
            else
            {
                int t[2];
                if (b == 3)
                    return 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("+",Id("a"),IntLiteral(4)),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),Return(IntLiteral(0)))]),Block([VarDecl("t",ArrayType(2,IntType())),If(BinaryOp("==",Id("b"),IntLiteral(3)),Return(IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_ifstmt_4(self):
        input = """
        int foo(int t[]){
            if (c == 0){
                return 1;
            }
            if (d == 0){
                return 2;
            }
            else
                return 3;
            if (e == 0){
                return 0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("t",ArrayPointerType(IntType()))],IntType(),Block([If(BinaryOp("==",Id("c"),IntLiteral(0)),Block([Return(IntLiteral(1))])),If(BinaryOp("==",Id("d"),IntLiteral(0)),Block([Return(IntLiteral(2))]),Return(IntLiteral(3))),If(BinaryOp("==",Id("e"),IntLiteral(0)),Block([Return(IntLiteral(0))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_ifstmt_5(self):
        input = """
        int foo(int t){
            if (a + 3 = 1 + 2)  
                if (t == 2)
                    if (n - 1)
                        return 1;
                else
                    if (n + 1)
                        return 0;
        }           
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("t",IntType())],IntType(),Block([If(BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(1),IntLiteral(2))),If(BinaryOp("==",Id("t"),IntLiteral(2)),If(BinaryOp("-",Id("n"),IntLiteral(1)),Return(IntLiteral(1)),If(BinaryOp("+",Id("n"),IntLiteral(1)),Return(IntLiteral(0))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_ifstmt_6(self):
        input = """
        int main(int c){
            if (c == 3){
                arr = x + 3;
                c = 1 + 3;
                int c[4], a;
            }
            else
                return 1;

            if (test == fail){
                arr = x + 3;
                x = x * 2;
                if (1)
                    return 0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("c",IntType())],IntType(),Block([If(BinaryOp("==",Id("c"),IntLiteral(3)),Block([BinaryOp("=",Id("arr"),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("=",Id("c"),BinaryOp("+",IntLiteral(1),IntLiteral(3))),VarDecl("c",ArrayType(4,IntType())),VarDecl("a",IntType())]),Return(IntLiteral(1))),If(BinaryOp("==",Id("test"),Id("fail")),Block([BinaryOp("=",Id("arr"),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("=",Id("x"),BinaryOp("*",Id("x"),IntLiteral(2))),If(IntLiteral(1),Return(IntLiteral(0)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_ifstmt_7(self):
        input = """
        int main(boolean c){
            if (0)
                return 0;
        }
        void test(int c[]){
            if (1)
                return 1;
        }
        string[] foo(int a, float b[]){
            if (2)
                return 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("c",BoolType())],IntType(),Block([If(IntLiteral(0),Return(IntLiteral(0)))])),FuncDecl(Id("test"),[VarDecl("c",ArrayPointerType(IntType()))],VoidType(),Block([If(IntLiteral(1),Return(IntLiteral(1)))])),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(StringType()),Block([If(IntLiteral(2),Return(IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_dowhilestmt_1(self):
        input = """
        int main(){
            int c[3];
            do{
                x = 1;
            } while (c == true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",ArrayType(3,IntType())),Dowhile([Block([BinaryOp("=",Id("x"),IntLiteral(1))])],BinaryOp("==",Id("c"),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_dowhilestmt_2(self):
        input = """
        int main(){
            do{
                int c, d[3], e;
            }
            while (x < 3);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("c",IntType()),VarDecl("d",ArrayType(3,IntType())),VarDecl("e",IntType())])],BinaryOp("<",Id("x"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_dowhilestmt_3(self):
        input = """
        int main(){
            int c,d[4],e;
            do{
                1 + 1 = 2;
                x + 3 > 4;
                string c[3];
            } while (x < 10 + 3);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",IntType()),VarDecl("d",ArrayType(4,IntType())),VarDecl("e",IntType()),Dowhile([Block([BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)),BinaryOp(">",BinaryOp("+",Id("x"),IntLiteral(3)),IntLiteral(4)),VarDecl("c",ArrayType(3,StringType()))])],BinaryOp("<",Id("x"),BinaryOp("+",IntLiteral(10),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_dowhilestmt_4(self):
        input = """
        int main(){
            int a,c,d;
            do{
                float a[5];
                float b[5];
                float c[6];
            } while (1);
            string b,c,d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),Dowhile([Block([VarDecl("a",ArrayType(5,FloatType())),VarDecl("b",ArrayType(5,FloatType())),VarDecl("c",ArrayType(6,FloatType()))])],IntLiteral(1)),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_dowhilestmt_5(self):
        input = """
        int main(){
            int k,c[4];
            do{
                do{
                    int c[3];
                } while (x < 4);
            } while (k == 0);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("k",IntType()),VarDecl("c",ArrayType(4,IntType())),Dowhile([Block([Dowhile([Block([VarDecl("c",ArrayType(3,IntType()))])],BinaryOp("<",Id("x"),IntLiteral(4)))])],BinaryOp("==",Id("k"),IntLiteral(0))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_dowhilestmt_6(self):
        input = """
        int main(){
            do{
                do{
                } while (x = 3);
                do{
                } while (0);
            } while (y < 2);
            do{
            }while (x + 1 > 2);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Dowhile([Block([])],BinaryOp("=",Id("x"),IntLiteral(3))),Dowhile([Block([])],IntLiteral(0))])],BinaryOp("<",Id("y"),IntLiteral(2))),Dowhile([Block([])],BinaryOp(">",BinaryOp("+",Id("x"),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_dowhilestmt_7(self):
        input = """
        int main(){
            do{
                1 + 1 = 3;
                int foo[3];
                do 
                    do
                        do
                            x = x + 1;
                        while (9);
                    while (x + 1 > 0);
                while (x = 3);
            } while (z < -3);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(3)),VarDecl("foo",ArrayType(3,IntType())),Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))],IntLiteral(9))],BinaryOp(">",BinaryOp("+",Id("x"),IntLiteral(1)),IntLiteral(0)))],BinaryOp("=",Id("x"),IntLiteral(3)))])],BinaryOp("<",Id("z"),UnaryOp("-",IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_dowhilestmt_8(self):
        input = """
        int main(){
            do {
                do
                    do{
                        do
                            1 + 1 = 0;
                        while (y < 9);
                    }while (x > 0);
                while (0);
            } while (x - x);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Dowhile([Dowhile([Block([Dowhile([BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(0))],BinaryOp("<",Id("y"),IntLiteral(9)))])],BinaryOp(">",Id("x"),IntLiteral(0)))],IntLiteral(0))])],BinaryOp("-",Id("x"),Id("x")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_dowhilestmt_9(self):
        input = """
        int main(){
            do{
                int c[3];
                if (x == 0)
                    c[3] = 10;
                if (7 == y)
                    return 0;
            } while (z < 10);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp("==",Id("x"),IntLiteral(0)),BinaryOp("=",ArrayCell(Id("c"),IntLiteral(3)),IntLiteral(10))),If(BinaryOp("==",IntLiteral(7),Id("y")),Return(IntLiteral(0)))])],BinaryOp("<",Id("z"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_dowhilestmt_10(self):
        input = """
        int main(){
            do
                if (x == 0)
                    return 0;
                else
                    return 1;
            while (x > 10);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([If(BinaryOp("==",Id("x"),IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(1)))],BinaryOp(">",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_dowhilestmt_11(self):
        input = """
        int main(){
            if (x == 10)
                do {
                    int c[5];
                }
                while (x > 10);
            else
                if (x == 11)
                    return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("x"),IntLiteral(10)),Dowhile([Block([VarDecl("c",ArrayType(5,IntType()))])],BinaryOp(">",Id("x"),IntLiteral(10))),If(BinaryOp("==",Id("x"),IntLiteral(11)),Return(IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_dowhilestmt_12(self):
        input = """
        int main(){
            if (z == 1 + 3){
                int m[5];
                do{
                    if (1 + 1 == 10)
                        return 0;
                }while (y - 3 < 10);
            }
            else{
                return 0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("z"),BinaryOp("+",IntLiteral(1),IntLiteral(3))),Block([VarDecl("m",ArrayType(5,IntType())),Dowhile([Block([If(BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(10)),Return(IntLiteral(0)))])],BinaryOp("<",BinaryOp("-",Id("y"),IntLiteral(3)),IntLiteral(10)))]),Block([Return(IntLiteral(0))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_dowhilestmt_13(self):
        input = """
        int main(){
            do {
                int c[3];
                if (1 == 2){
                    do 
                        if (1 + 1)  
                            return 1;
                        else
                            return 2;
                    while (1 > x);
                }
            } while (!y);
            return 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([Dowhile([If(BinaryOp("+",IntLiteral(1),IntLiteral(1)),Return(IntLiteral(1)),Return(IntLiteral(2)))],BinaryOp(">",IntLiteral(1),Id("x")))]))])],UnaryOp("!",Id("y"))),Return(IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_dowhilestmt_14(self):
        input = """
        int main(){
            do{
                if (1 + 1 == 0)
                    return 0;
                int m[9];
                if (1 + 2 == 3)
                    return 1;
                float t, l[5];
                if (1 + 1 == 11)
                    return 9;
                else
                    return 10;
            } while (x != 10);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(0)),Return(IntLiteral(0))),VarDecl("m",ArrayType(9,IntType())),If(BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Return(IntLiteral(1))),VarDecl("t",FloatType()),VarDecl("l",ArrayType(5,FloatType())),If(BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(11)),Return(IntLiteral(9)),Return(IntLiteral(10)))])],BinaryOp("!=",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_dowhilestmt_15(self):
        input = """
        int main(){
            if (2 == 3)
                do 
                    if (1 + 1)
                    {
                        int a[3];
                    }
                while (1 > 3);
            else
                do 
                    if (0)
                    {
                        int d[4];
                    }
                while (1 < 5);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",IntLiteral(2),IntLiteral(3)),Dowhile([If(BinaryOp("+",IntLiteral(1),IntLiteral(1)),Block([VarDecl("a",ArrayType(3,IntType()))]))],BinaryOp(">",IntLiteral(1),IntLiteral(3))),Dowhile([If(IntLiteral(0),Block([VarDecl("d",ArrayType(4,IntType()))]))],BinaryOp("<",IntLiteral(1),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_dowhilestmt_16(self):
        input = """
        int main(){
            do{
                if (c == 3)
                    return 0;
            } while (x > 3);
        }
        void foo(int c){
            if (d == 10){
                do
                    c = x + 1;
                while (true);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",Id("c"),IntLiteral(3)),Return(IntLiteral(0)))])],BinaryOp(">",Id("x"),IntLiteral(3)))])),FuncDecl(Id("foo"),[VarDecl("c",IntType())],VoidType(),Block([If(BinaryOp("==",Id("d"),IntLiteral(10)),Block([Dowhile([BinaryOp("=",Id("c"),BinaryOp("+",Id("x"),IntLiteral(1)))],BooleanLiteral(True))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_dowhilestmt_17(self):
        input = """
        int main(){
            int c[3],a;
            do{
                int c;
            } while (FALSE);
            int b,c;
            do{
                float k;
            } while(true);
            if (c == 0)
                return 0;
            else
                return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",ArrayType(3,IntType())),VarDecl("a",IntType()),Dowhile([Block([VarDecl("c",IntType())])],Id("FALSE")),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([Block([VarDecl("k",FloatType())])],BooleanLiteral(True)),If(BinaryOp("==",Id("c"),IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_dowhilestmt_18(self):
        input = """
        int main(){
            do {
                int arr[4], arr;
                if (x > 3){
                }
                else{
                    int arr[4], a;
                    do {
                        return 0;
                    }while(1 = true);
                }
            } while(true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("arr",ArrayType(4,IntType())),VarDecl("arr",IntType()),If(BinaryOp(">",Id("x"),IntLiteral(3)),Block([]),Block([VarDecl("arr",ArrayType(4,IntType())),VarDecl("a",IntType()),Dowhile([Block([Return(IntLiteral(0))])],BinaryOp("=",IntLiteral(1),BooleanLiteral(True)))]))])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_dowhilestmt_19(self):
        input = """
        int main(){
            do {
                do{
                    int var[3],b,a;
                    if (b == 0)
                        break;
                    b = b + 1;
                } while (b != 0);
                if (c == 0)
                    break;
                else
                    continue;
            } while (true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Dowhile([Block([VarDecl("var",ArrayType(3,IntType())),VarDecl("b",IntType()),VarDecl("a",IntType()),If(BinaryOp("==",Id("b"),IntLiteral(0)),Break()),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],BinaryOp("!=",Id("b"),IntLiteral(0))),If(BinaryOp("==",Id("c"),IntLiteral(0)),Break(),Continue())])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_dowhilestmt_20(self):
        input = """
        int main(){
            int var[4], t[2], b;
            if (b)
                do{
                    string arr[2];
                    if (t * 2 = 4 * d){
                        break;
                    }
                } while (b != 0);
            else
                return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("var",ArrayType(4,IntType())),VarDecl("t",ArrayType(2,IntType())),VarDecl("b",IntType()),If(Id("b"),Dowhile([Block([VarDecl("arr",ArrayType(2,StringType())),If(BinaryOp("=",BinaryOp("*",Id("t"),IntLiteral(2)),BinaryOp("*",IntLiteral(4),Id("d"))),Block([Break()]))])],BinaryOp("!=",Id("b"),IntLiteral(0))),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_dowhilestmt_21(self):
        input = """
        int main(){
            if (a){
                int a[4], b, c[7];
                continue;
            }
            do{
            } while (true);
            if (b){
                int arr[4];
                int b[5];
            }
            else
                return 0;
            do{
            }while (FALSE);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("b",IntType()),VarDecl("c",ArrayType(7,IntType())),Continue()])),Dowhile([Block([])],BooleanLiteral(True)),If(Id("b"),Block([VarDecl("arr",ArrayType(4,IntType())),VarDecl("b",ArrayType(5,IntType()))]),Return(IntLiteral(0))),Dowhile([Block([])],Id("FALSE"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_dowhilestmt_22(self):
        input = """
        float[] main(int v[], string arr[]){
            do{
                if (FALSE)
                    if (b)
                        return 0;
            } while (a * b > 4 + 3);
            if (a + 8 > 45)
                break;
            else
                continue;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("v",ArrayPointerType(IntType())),VarDecl("arr",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([Dowhile([Block([If(Id("FALSE"),If(Id("b"),Return(IntLiteral(0))))])],BinaryOp(">",BinaryOp("*",Id("a"),Id("b")),BinaryOp("+",IntLiteral(4),IntLiteral(3)))),If(BinaryOp(">",BinaryOp("+",Id("a"),IntLiteral(8)),IntLiteral(45)),Break(),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_dowhilestmt_23(self):
        input = """
        float main(int v[], string arr[]){
            if (1 + 3 >= -3 + 2){
                do {
                    x = x + 2 / 3;
                    y = -y + 1;
                } while (1.3e-3 > 0.1 + x);
            }
        }
        int foo(float arr[]){
            do{
                if (1 >= 9 * x / 2)
                    return 0;
                else
                    if (y != 0)
                        return 0;
                    else
                        return 1;
            } while (x * y % 3 == 0);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("v",ArrayPointerType(IntType())),VarDecl("arr",ArrayPointerType(StringType()))],FloatType(),Block([If(BinaryOp(">=",BinaryOp("+",IntLiteral(1),IntLiteral(3)),BinaryOp("+",UnaryOp("-",IntLiteral(3)),IntLiteral(2))),Block([Dowhile([Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),BinaryOp("/",IntLiteral(2),IntLiteral(3)))),BinaryOp("=",Id("y"),BinaryOp("+",UnaryOp("-",Id("y")),IntLiteral(1)))])],BinaryOp(">",FloatLiteral("1.3e-3"),BinaryOp("+",FloatLiteral(0.1),Id("x"))))]))])),FuncDecl(Id("foo"),[VarDecl("arr",ArrayPointerType(FloatType()))],IntType(),Block([Dowhile([Block([If(BinaryOp(">=",IntLiteral(1),BinaryOp("/",BinaryOp("*",IntLiteral(9),Id("x")),IntLiteral(2))),Return(IntLiteral(0)),If(BinaryOp("!=",Id("y"),IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(1))))])],BinaryOp("==",BinaryOp("%",BinaryOp("*",Id("x"),Id("y")),IntLiteral(3)),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_forstmt_1(self):
        input = """
        int main(){
            int a[4], a;
            for(i;j;k){
                if (a == 0)
                    return 1;
                if (b == 0)
                    return 2;
                if (c == 0)
                    return 3;
                if (d == 0)
                    return 4;
            }
            int a, b[4];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("a",IntType()),For(Id("i"),Id("j"),Id("k"),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Return(IntLiteral(1))),If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(IntLiteral(2))),If(BinaryOp("==",Id("c"),IntLiteral(0)),Return(IntLiteral(3))),If(BinaryOp("==",Id("d"),IntLiteral(0)),Return(IntLiteral(4)))])),VarDecl("a",IntType()),VarDecl("b",ArrayType(4,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_forstmt_2(self):
        input = """
        int main(){
            if (1){
                for(i;j;k){
                    int a[5],c;
                    int c, d[2];
                }
            }
            else{
                for(i;j;k){
                    string a[5], c;
                    return 0;
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([For(Id("i"),Id("j"),Id("k"),Block([VarDecl("a",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(2,IntType()))]))]),Block([For(Id("i"),Id("j"),Id("k"),Block([VarDecl("a",ArrayType(5,StringType())),VarDecl("c",StringType()),Return(IntLiteral(0))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_forstmt_3(self):
        input = """
        int main(){
            for(i;j;k){
                if (a)
                    return 0;
                else
                    do
                        x = 1;
                    while (x < 3);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("j"),Id("k"),Block([If(Id("a"),Return(IntLiteral(0)),Dowhile([BinaryOp("=",Id("x"),IntLiteral(1))],BinaryOp("<",Id("x"),IntLiteral(3))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_forstmt_4(self):
        input = """
        int main(){
            do{
                int i,j,k;
                for (i;j;k){
                    boolean a[3];
                    return 0;
                }
            } while (x < true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",IntType()),For(Id("i"),Id("j"),Id("k"),Block([VarDecl("a",ArrayType(3,BoolType())),Return(IntLiteral(0))]))])],BinaryOp("<",Id("x"),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_forstmt_5(self):
        input = """
        int main(){
            for(i;j;k){
                do
                    x = 1;
                while (x > 1);
                do 
                    x = 2;
                while (x == 1);
                do
                    x = 3;
                while (x < 1);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("j"),Id("k"),Block([Dowhile([BinaryOp("=",Id("x"),IntLiteral(1))],BinaryOp(">",Id("x"),IntLiteral(1))),Dowhile([BinaryOp("=",Id("x"),IntLiteral(2))],BinaryOp("==",Id("x"),IntLiteral(1))),Dowhile([BinaryOp("=",Id("x"),IntLiteral(3))],BinaryOp("<",Id("x"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_forstmt_6(self):
        input = """
        int main(){
            do {
                int a[4], b;
                for(i;j;k){
                    int b[3], d;
                    float d;
                }
            } while (true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("b",IntType()),For(Id("i"),Id("j"),Id("k"),Block([VarDecl("b",ArrayType(3,IntType())),VarDecl("d",IntType()),VarDecl("d",FloatType())]))])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_forstmt_7(self):
        input = """
        int main(){
            if (a > 0){
                do
                    for(i;j;k){
                        int a,b,c[5];
                    }
                while (a == 0);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(0)),Block([Dowhile([For(Id("i"),Id("j"),Id("k"),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(5,IntType()))]))],BinaryOp("==",Id("a"),IntLiteral(0)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_forstmt_8(self):
        input = """
        int main(){
            do{
                for(i;j;k){
                    if (true)
                        return 0;
                }
                for(m;n;o){
                    if (true)
                        return 1;
                }
                for(d;e;f){
                    if (FALSE)
                        return 2;
                }
            } while (z > 0);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([For(Id("i"),Id("j"),Id("k"),Block([If(BooleanLiteral(True),Return(IntLiteral(0)))])),For(Id("m"),Id("n"),Id("o"),Block([If(BooleanLiteral(True),Return(IntLiteral(1)))])),For(Id("d"),Id("e"),Id("f"),Block([If(Id("FALSE"),Return(IntLiteral(2)))]))])],BinaryOp(">",Id("z"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_forstmt_9(self):
        input = """
        int main(){
            if (a){
                do{
                    int a[5], c, b[6];
                    return 1;
                } while(x > 3);
                for(i;j;k){
                    if (a)
                        return 1;
                    else
                        return 2;
                }
            }
            for(m;n;o){
                return 2;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),Block([Dowhile([Block([VarDecl("a",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("b",ArrayType(6,IntType())),Return(IntLiteral(1))])],BinaryOp(">",Id("x"),IntLiteral(3))),For(Id("i"),Id("j"),Id("k"),Block([If(Id("a"),Return(IntLiteral(1)),Return(IntLiteral(2)))]))])),For(Id("m"),Id("n"),Id("o"),Block([Return(IntLiteral(2))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_forstmt_10(self):
        input = """
        int main(){
            for(i = 0; i < 10; i){
                if (a == 0){
                    break;
                }
                else{
                    continue;
                }
                return 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Id("i"),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Block([Break()]),Block([Continue()])),Return(IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_forstmt_11(self):
        input = """
        int main(){
            for(i;j;k){
                for(m;n;o){
                    if (!a)
                        break;
                }
                for(d;e;f){
                    if (!b)
                        break;
                }
            }
            do{
                int arr[3], b;
                x = x + 1;
            }while (x < 76);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("j"),Id("k"),Block([For(Id("m"),Id("n"),Id("o"),Block([If(UnaryOp("!",Id("a")),Break())])),For(Id("d"),Id("e"),Id("f"),Block([If(UnaryOp("!",Id("b")),Break())]))])),Dowhile([Block([VarDecl("arr",ArrayType(3,IntType())),VarDecl("b",IntType()),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],BinaryOp("<",Id("x"),IntLiteral(76)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_forstmt_12(self):
        input = """
        int[] main(int argc){
            int arr[3];
            int y;
            y = 0;
            if (argc == 1){
                for(x = 1; x < 10; x = x + 1){
                    y = y * 2;
                    if (y > 50)
                        break;
                }
            }
            return y;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",IntType())],ArrayPointerType(IntType()),Block([VarDecl("arr",ArrayType(3,IntType())),VarDecl("y",IntType()),BinaryOp("=",Id("y"),IntLiteral(0)),If(BinaryOp("==",Id("argc"),IntLiteral(1)),Block([For(BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Block([BinaryOp("=",Id("y"),BinaryOp("*",Id("y"),IntLiteral(2))),If(BinaryOp(">",Id("y"),IntLiteral(50)),Break())]))])),Return(Id("y"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_expression_1(self):
        input = """
        int main() {
            int a;
            a = 1 + 2;
            c = b + d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),BinaryOp("=",Id("c"),BinaryOp("+",Id("b"),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_expression_2(self):
        input = """
        float[] cal(int a){
            return a + 3 * 4;
        }
        int main() {
            int local_var;
            3 + 4 = 2 * 6 + (1 - 3);
            return local_var + 1;
        }
        """
        expect = str(Program([FuncDecl(Id("cal"),[VarDecl("a",IntType())],ArrayPointerType(FloatType()),Block([Return(BinaryOp("+",Id("a"),BinaryOp("*",IntLiteral(3),IntLiteral(4))))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",IntType()),BinaryOp("=",BinaryOp("+",IntLiteral(3),IntLiteral(4)),BinaryOp("+",BinaryOp("*",IntLiteral(2),IntLiteral(6)),BinaryOp("-",IntLiteral(1),IntLiteral(3)))),Return(BinaryOp("+",Id("local_var"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_expression_3(self):
        input = """
        int main() {
            int local_var;
            local_var = local[1 + x] - 4 * 5;
            min == 15 >= 123 + (1 + 3);
            return local_var + 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",IntType()),BinaryOp("=",Id("local_var"),BinaryOp("-",ArrayCell(Id("local"),BinaryOp("+",IntLiteral(1),Id("x"))),BinaryOp("*",IntLiteral(4),IntLiteral(5)))),BinaryOp("==",Id("min"),BinaryOp(">=",IntLiteral(15),BinaryOp("+",IntLiteral(123),BinaryOp("+",IntLiteral(1),IntLiteral(3))))),Return(BinaryOp("+",Id("local_var"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_expression_4(self):
        input = """
        int main() {
            int local_var;
            local_var = -56 + 49 % 23 * 4;
            str = 1 || 8 != 2 && (3 / 19);
            return _local && 34;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",IntType()),BinaryOp("=",Id("local_var"),BinaryOp("+",UnaryOp("-",IntLiteral(56)),BinaryOp("*",BinaryOp("%",IntLiteral(49),IntLiteral(23)),IntLiteral(4)))),BinaryOp("=",Id("str"),BinaryOp("||",IntLiteral(1),BinaryOp("&&",BinaryOp("!=",IntLiteral(8),IntLiteral(2)),BinaryOp("/",IntLiteral(3),IntLiteral(19))))),Return(BinaryOp("&&",Id("_local"),IntLiteral(34)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_expression_5(self):
        input = """
        int main() {
            int local_var;
            local = 1 * 4 - 3 - (45 = 34);
            return local_var + 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",IntType()),BinaryOp("=",Id("local"),BinaryOp("-",BinaryOp("-",BinaryOp("*",IntLiteral(1),IntLiteral(4)),IntLiteral(3)),BinaryOp("=",IntLiteral(45),IntLiteral(34)))),Return(BinaryOp("+",Id("local_var"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_expression_6(self):
        input = """
        int main() {
            int local_var;
            a = !abc + -45 && arr == (3 != 5) > !out;
            return local_var >= 6;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",IntType()),BinaryOp("=",Id("a"),BinaryOp("&&",BinaryOp("+",UnaryOp("!",Id("abc")),UnaryOp("-",IntLiteral(45))),BinaryOp("==",Id("arr"),BinaryOp(">",BinaryOp("!=",IntLiteral(3),IntLiteral(5)),UnaryOp("!",Id("out")))))),Return(BinaryOp(">=",Id("local_var"),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_expression_7(self):
        input = """
        int main() {
            (a + b) = !!--!!34 + -!-!(a + b);
            return -local_var;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("-",UnaryOp("!",UnaryOp("!",IntLiteral(34))))))),UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",BinaryOp("+",Id("a"),Id("b")))))))),Return(UnaryOp("-",Id("local_var")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_expression_8(self):
        input = """
        int main() {
            int local_var[5];
            a >= 3 = 5;
            return --1 = local_var[3];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("local_var",ArrayType(5,IntType())),BinaryOp("=",BinaryOp(">=",Id("a"),IntLiteral(3)),IntLiteral(5)),Return(BinaryOp("=",UnaryOp("-",UnaryOp("-",IntLiteral(1))),ArrayCell(Id("local_var"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_expression_9(self):
        input = """
        int main() {
            -abc = 12 + true*2 - false % 4;
            return func(12 + 1) >= -!local_var ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id("abc")),BinaryOp("-",BinaryOp("+",IntLiteral(12),BinaryOp("*",BooleanLiteral(True),IntLiteral(2))),BinaryOp("%",BooleanLiteral(False),IntLiteral(4)))),Return(BinaryOp(">=",CallExpr(Id("func"),[BinaryOp("+",IntLiteral(12),IntLiteral(1))]),UnaryOp("-",UnaryOp("!",Id("local_var")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_expression_10(self):
        input = """
        int main() {
            -123 > !(-1 >= 789) == 456;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("==",BinaryOp(">",UnaryOp("-",IntLiteral(123)),UnaryOp("!",BinaryOp(">=",UnaryOp("-",IntLiteral(1)),IntLiteral(789)))),IntLiteral(456))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_expression_11(self):
        input = """
        int main() {
            int a,c,d[3];
            d[-1 * 34 >= (1 && 1)] == 1;
            return func(12, 4 + 1) >= a[4] ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(3,IntType())),BinaryOp("==",ArrayCell(Id("d"),BinaryOp(">=",BinaryOp("*",UnaryOp("-",IntLiteral(1)),IntLiteral(34)),BinaryOp("&&",IntLiteral(1),IntLiteral(1)))),IntLiteral(1)),Return(BinaryOp(">=",CallExpr(Id("func"),[IntLiteral(12),BinaryOp("+",IntLiteral(4),IntLiteral(1))]),ArrayCell(Id("a"),IntLiteral(4))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_expression_12(self):
        input = """
        int main() {
            int abd123;
            (1 && 33) != -45 + (false == 19);
            return func(12, 4 + 1) >= a[4];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("abd123",IntType()),BinaryOp("!=",BinaryOp("&&",IntLiteral(1),IntLiteral(33)),BinaryOp("+",UnaryOp("-",IntLiteral(45)),BinaryOp("==",BooleanLiteral(False),IntLiteral(19)))),Return(BinaryOp(">=",CallExpr(Id("func"),[IntLiteral(12),BinaryOp("+",IntLiteral(4),IntLiteral(1))]),ArrayCell(Id("a"),IntLiteral(4))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_index_1(self):
        input = """
        int main() {
            a[1*-3 == 3] = 1 >= !abc[-10];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("==",BinaryOp("*",IntLiteral(1),UnaryOp("-",IntLiteral(3))),IntLiteral(3))),BinaryOp(">=",IntLiteral(1),UnaryOp("!",ArrayCell(Id("abc"),UnaryOp("-",IntLiteral(10))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_index_2(self):
        input = """
        int main() {
            foo(2)[3+x] = a[b[2]] + 3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_index_3(self):
        input = """
        int main() {
            sum = foo()[5 * foo()] - !tran(5,4)[5 % tran()] + -foo(a[3*b[c]]);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("sum"),BinaryOp("+",BinaryOp("-",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",IntLiteral(5),CallExpr(Id("foo"),[]))),UnaryOp("!",ArrayCell(CallExpr(Id("tran"),[IntLiteral(5),IntLiteral(4)]),BinaryOp("%",IntLiteral(5),CallExpr(Id("tran"),[]))))),UnaryOp("-",CallExpr(Id("foo"),[ArrayCell(Id("a"),BinaryOp("*",IntLiteral(3),ArrayCell(Id("b"),Id("c"))))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_index_4(self):
        input = """
        int main() {
            test = arr[1 + foo()] - arr[1 + arr[1]];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("test"),BinaryOp("-",ArrayCell(Id("arr"),BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[]))),ArrayCell(Id("arr"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("arr"),IntLiteral(1))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_index_5(self):
        input = """
        int main() {
            test[1 + 4*a[3]] - 1 = 3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",BinaryOp("-",ArrayCell(Id("test"),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(4),ArrayCell(Id("a"),IntLiteral(3))))),IntLiteral(1)),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_index_6(self):
        input = """
        int main() {
            float t;
            t = (a + b)[1 + 3];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("t",FloatType()),BinaryOp("=",Id("t"),ArrayCell(BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",IntLiteral(1),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_index_7(self):
        input = """
        int main() {
            string trend; 
            trend = (foo(1) + foo(2))[1 + 9];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("trend",StringType()),BinaryOp("=",Id("trend"),ArrayCell(BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),BinaryOp("+",IntLiteral(1),IntLiteral(9))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_index_8(self):
        input = """
        int main() {
            float n[6];
            n = foo(foo(1)[-3]);
            continue;
            break;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",ArrayType(6,FloatType())),BinaryOp("=",Id("n"),CallExpr(Id("foo"),[ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),UnaryOp("-",IntLiteral(3)))])),Continue(),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_invocation_1(self):
        input = """
        int main() {
            b = poor(-3, a, 1 + b[6]);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("b"),CallExpr(Id("poor"),[UnaryOp("-",IntLiteral(3)),Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("b"),IntLiteral(6)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_invocation_2(self):
        input = """
        int main() {
            d = poor(-1) + poor()[1 / 3];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("d"),BinaryOp("+",CallExpr(Id("poor"),[UnaryOp("-",IntLiteral(1))]),ArrayCell(CallExpr(Id("poor"),[]),BinaryOp("/",IntLiteral(1),IntLiteral(3)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_invocation_3(self):
        input = """
        string name(int a, float c){
        }
        int main() {
            name(1, 4 + 3.5) = main(1);
            return name(1 + b[4])[9];
        }
        """
        expect = str(Program([FuncDecl(Id("name"),[VarDecl("a",IntType()),VarDecl("c",FloatType())],StringType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",CallExpr(Id("name"),[IntLiteral(1),BinaryOp("+",IntLiteral(4),FloatLiteral(3.5))]),CallExpr(Id("main"),[IntLiteral(1)])),Return(ArrayCell(CallExpr(Id("name"),[BinaryOp("+",IntLiteral(1),ArrayCell(Id("b"),IntLiteral(4)))]),IntLiteral(9)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_invocation_4(self):
        input = """
        string call(int a, float c){
        }
        int main() {
            // test call
            call(1, -3, "string", a);
            return "string";
        }
        """
        expect = str(Program([FuncDecl(Id("call"),[VarDecl("a",IntType()),VarDecl("c",FloatType())],StringType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("call"),[IntLiteral(1),UnaryOp("-",IntLiteral(3)),StringLiteral("string"),Id("a")]),Return(StringLiteral("string"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_invocation_5(self):
        input = """
        float[] float_lit(int a[], string k){
        }
        int main() {
            int c;
            c = call(4.5, "string", 1 == 3);
            return main(1, call());
        }
        """
        expect = str(Program([FuncDecl(Id("float_lit"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("k",StringType())],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),CallExpr(Id("call"),[FloatLiteral(4.5),StringLiteral("string"),BinaryOp("==",IntLiteral(1),IntLiteral(3))])),Return(CallExpr(Id("main"),[IntLiteral(1),CallExpr(Id("call"),[])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_invocation_6(self):
        input = """
        int main(){
            int arr[4],b,c[3];
            call(1,2,3) + foo() >= foo(1);
            if (foo())
                return 0;
            else
                return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("arr",ArrayType(4,IntType())),VarDecl("b",IntType()),VarDecl("c",ArrayType(3,IntType())),BinaryOp(">=",BinaryOp("+",CallExpr(Id("call"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),CallExpr(Id("foo"),[])),CallExpr(Id("foo"),[IntLiteral(1)])),If(CallExpr(Id("foo"),[]),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_invocation_7(self):
        input = """
        int main(){
            foo(foo(foo(foo(), foo(1 + 2))));
            for(foo(1); foo(2); foo(3)){
                if (foo(1))
                    return 1;
                else
                    return 2;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(1),IntLiteral(2))])])])]),For(CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)]),CallExpr(Id("foo"),[IntLiteral(3)]),Block([If(CallExpr(Id("foo"),[IntLiteral(1)]),Return(IntLiteral(1)),Return(IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_invocation_8(self):
        input = """
        int main(){
            do{
                foo(1) + foo(2) = foo(3);
                if (x >= foo(4))
                    return 0;
                else
                    if (a(1 + a()))
                        return 0;
            } while (foo() == 1);
        }
        
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),If(BinaryOp(">=",Id("x"),CallExpr(Id("foo"),[IntLiteral(4)])),Return(IntLiteral(0)),If(CallExpr(Id("a"),[BinaryOp("+",IntLiteral(1),CallExpr(Id("a"),[]))]),Return(IntLiteral(0))))])],BinaryOp("==",CallExpr(Id("foo"),[]),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_invocation_9(self):
        input = """
        int main(){
            if (foo(1, foo(2)))
            {
                for (x1; x2; x3){
                    caller(x2, x3);
                    main(lst);
                }
            }
            else{
                return main(1 + 2);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("foo"),[IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(2)])]),Block([For(Id("x1"),Id("x2"),Id("x3"),Block([CallExpr(Id("caller"),[Id("x2"),Id("x3")]),CallExpr(Id("main"),[Id("lst")])]))]),Block([Return(CallExpr(Id("main"),[BinaryOp("+",IntLiteral(1),IntLiteral(2))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_complex_program_1(self):
        input = """
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a + 3;
            if (i > 0){
                int d;
                d = i + 3;
                putInt(d);
            }
            return i;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_complex_program_2(self):
        input = """
        void foo(float a[]){
        }
        void goo(float x[]){
            float y[10];
            int z[10];
            foo(x);
            foo(y);
            foo(z);
            do 
                if (1 > 3) 
                    foo(x) = 1 || 3;
                else
                    for (i = 0; i = 0; i = 1)
                        return main();
            while (1);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(FloatType()))],VoidType(),Block([])),FuncDecl(Id("goo"),[VarDecl("x",ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl("y",ArrayType(10,FloatType())),VarDecl("z",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("x")]),CallExpr(Id("foo"),[Id("y")]),CallExpr(Id("foo"),[Id("z")]),Dowhile([If(BinaryOp(">",IntLiteral(1),IntLiteral(3)),BinaryOp("=",CallExpr(Id("foo"),[Id("x")]),BinaryOp("||",IntLiteral(1),IntLiteral(3))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),IntLiteral(1)),Return(CallExpr(Id("main"),[]))))],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_complex_program_3(self):
        input = """
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a + 3;
            if (i > 0){
                int d;
                d = i + 3;
                putInt(d);
            }
            return i;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_complex_program_4(self):
        input = """
        int global;
        int f(){
            return 200;
        }
        int foo(){
            return global;
        }
        int print(int local){
            // comment
            return local;
        }
        void main(){
            for (i = 0; i < 10; i = i + 1){
                int arr[10];
                arr[i] = arr[i] + 1;
            }
            do {
                print(arr[i]);
            } while (arr[i] % 2 == 0);
            return 0;
        }
        """
        expect = str(Program([VarDecl("global",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("foo"),[],IntType(),Block([Return(Id("global"))])),FuncDecl(Id("print"),[VarDecl("local",IntType())],IntType(),Block([Return(Id("local"))])),FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("arr",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("arr"),Id("i")),BinaryOp("+",ArrayCell(Id("arr"),Id("i")),IntLiteral(1)))])),Dowhile([Block([CallExpr(Id("print"),[ArrayCell(Id("arr"),Id("i"))])])],BinaryOp("==",BinaryOp("%",ArrayCell(Id("arr"),Id("i")),IntLiteral(2)),IntLiteral(0))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_complex_program_5(self):
        input = """
        int arr[10];
        float arr_float[20];
        string[] text(string ch, string arr_char[]){
            return arr_char;
        }
        void main(){
            int i;
            for (i = 0; i < 10; i = i + 1){
                arr_float[i] = arr[i] * 1;
                if (arr_float[i] == 0){
                    arr_float[i] = 0;
                    break;
                }
            }
            do
                arr_float[i] = 0;
                i = i + 1;
            while i < 10;
        }
        """
        expect = str(Program([VarDecl("arr",ArrayType(10,IntType())),VarDecl("arr_float",ArrayType(20,FloatType())),FuncDecl(Id("text"),[VarDecl("ch",StringType()),VarDecl("arr_char",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([Return(Id("arr_char"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("arr_float"),Id("i")),BinaryOp("*",ArrayCell(Id("arr"),Id("i")),IntLiteral(1))),If(BinaryOp("==",ArrayCell(Id("arr_float"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",ArrayCell(Id("arr_float"),Id("i")),IntLiteral(0)),Break()]))])),Dowhile([BinaryOp("=",ArrayCell(Id("arr_float"),Id("i")),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_complex_program_6(self):
        input = """
        int main(){
            int a;
            for (a = 0; a < 10; a = a + 1)
                return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    

    def test_complex_program_7(self):
        input = """
        int main(){
            int a,b[3],c;
            for(i = true; i < 10; i = i + 3){
                int a[3],c,b[3];
                float c;
                return 0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(3,IntType())),VarDecl("c",IntType()),For(BinaryOp("=",Id("i"),BooleanLiteral(True)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(3))),Block([VarDecl("a",ArrayType(3,IntType())),VarDecl("c",IntType()),VarDecl("b",ArrayType(3,IntType())),VarDecl("c",FloatType()),Return(IntLiteral(0))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_complex_program_8(self):
        input = """
        int main(){
            for(i = 0; i <= 10; i - 3){
                for(i = 0; i < 10; i){
                    x = x + 1;
                }
                int c, c[4], d, e[5];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("-",Id("i"),IntLiteral(3)),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Id("i"),Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])),VarDecl("c",IntType()),VarDecl("c",ArrayType(4,IntType())),VarDecl("d",IntType()),VarDecl("e",ArrayType(5,IntType()))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_complex_program_9(self):
        input = """
        int main(){
            int c[4], d;
            for(i;j;k)
                for(m;n;o)
                    return 1;
                for(i;j;k)
                    x = 1;
            for(h;k;i)
                g = 3;
            float d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",ArrayType(4,IntType())),VarDecl("d",IntType()),For(Id("i"),Id("j"),Id("k"),For(Id("m"),Id("n"),Id("o"),Return(IntLiteral(1)))),For(Id("i"),Id("j"),Id("k"),BinaryOp("=",Id("x"),IntLiteral(1))),For(Id("h"),Id("k"),Id("i"),BinaryOp("=",Id("g"),IntLiteral(3))),VarDecl("d",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_complex_program_10(self):
        input = """
        int main(){
            for(i;j;k){
                int a, b, c[3];
                if (b)
                    x = 1;
                else
                    x = 2;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("j"),Id("k"),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(3,IntType())),If(Id("b"),BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("x"),IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_complex_program_11(self):
        input = """
        int main(int a, int v){
            if (a + b < 1 * 3 / 7){
                int c[4], a;
                if (!(a - b))
                    return 0;
                else{
                }
            }
            else
                return 10;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("v",IntType())],IntType(),Block([If(BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("/",BinaryOp("*",IntLiteral(1),IntLiteral(3)),IntLiteral(7))),Block([VarDecl("c",ArrayType(4,IntType())),VarDecl("a",IntType()),If(UnaryOp("!",BinaryOp("-",Id("a"),Id("b"))),Return(IntLiteral(0)),Block([]))]),Return(IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_complex_program_12(self):
        input = """
        int[] test(){
            int a,b[3];
        }
        int a[4], b[3], f, c[2], d[1];
        string foo(int val[], boolean val){
            return 4;
        }
        float b[10];
        """
        expect = str(Program([FuncDecl(Id("test"),[],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(3,IntType()))])),VarDecl("a",ArrayType(4,IntType())),VarDecl("b",ArrayType(3,IntType())),VarDecl("f",IntType()),VarDecl("c",ArrayType(2,IntType())),VarDecl("d",ArrayType(1,IntType())),FuncDecl(Id("foo"),[VarDecl("val",ArrayPointerType(IntType())),VarDecl("val",BoolType())],StringType(),Block([Return(IntLiteral(4))])),VarDecl("b",ArrayType(10,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    