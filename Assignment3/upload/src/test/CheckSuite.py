import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def testRedeclaredVariable1(self):
        input = """
        int a;
        int a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def testRedeclaredVariable2(self):  
        input = """
        int b;
        float b;
        void main() {}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,401))

    def testRedeclaredVariable3(self):  
        input = """
        int c;
        void main() {
            putString("...");
        }
        string c[10];
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,402))

    def testRedeclaredVariable4(self):  
        input = """
        int a, b, c, d, a;
        void main() {
            putStringLn("...");
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def testRedeclaredFunction1(self):  
        input = """
        int foo() {
            return 0;
        }
        float foo() {
            return 4.4;
        }
        int main() {
            foo();
            return 0;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,404))

    def testRedeclaredFunction2(self):  
        input = """
        string foo(){
            return "foo";
        }
        string foo(){
            return "redeclared";
        }
        int main() {
            foo();
            return 0;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,405))

    def testRedeclaredFunction3(self):  
        input = """
        void foo(){}
        void main() {
            foo();
        }
        float foo(){
            return 17.11;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,406))

    def testRedeclaredParameter1(self):
        input = """
        int main(int a, int a){
            return 0;
        } 
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def testRedeclaredParameter2(self):
        input = """
        int main(string x, int a[], float a){
            return 0;
        } """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def testRedeclaredParameter3(self):
        input = """
        void main(string x, boolean x, int x, float x){
            return;
        } """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,409))

    def testRedeclaredVarInFunc1(self):
        input = """
        int main() {
            int a;
            int a;
            return 0;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def testRedeclaredVarInFunc2(self):
        input = """
        void main() {
            int a;
            string a[10];
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def testRedeclaredVarInFunc3(self):
        input = """
        int main() {
            int a;
            string b;
            float c;
            boolean b[10];
            return 0;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,412))

    def testRedeclaredVarInFunc4(self):
        input = """
        void main() {
            boolean x, x;
        }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,413))

    def testRedeclaredVarInFunc5(self):
        input = """
        int foo() {
            int a, a;
            return 10;
        }
        void main() {
            foo();
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def testRedeclaredVarInFunc6(self):
        input = """
        void foo() {
            string arr[10];
            boolean arr[10];
        }
        void main() {
            foo();
        }
        """
        expect = "Redeclared Variable: arr"
        self.assertTrue(TestChecker.test(input,expect,415))

    def testRedeclaredVarInScope1(self):
        input = """
        int foo() {
            int a;
            {
                int a;
                {
                    int c, c;
                }
            }
            return 0;
        }
        void main() {
            foo();
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,416))

    def testRedeclaredVarInScope2(self):
        input = """
        int foo() {
            int a;
            {
                int here;
                {
                    int scope; 
                    boolean a;
                }
                float here;
            }
            return 0;
        }
        int main() {
            foo();
            return 0;
        }
        """
        expect = "Redeclared Variable: here"
        self.assertTrue(TestChecker.test(input,expect,417))

    def testUndeclaredID1(self):
        input = """ 
        int main() {
            a = 1;
            return 0;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def testUndeclaredID2(self):
        input = """ 
        float foo(int a) {
            a = 1;
            b = 2;
            return 4.7;
        }

        int main() {
            int a;
            foo(a);
            return 0;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,419))

    def testUndeclaredID3(self):
        input = """ 
        int foo() {
            int b;
            a = 1;
            b = 2;
            return b;
        }

        int main() {
            return foo();
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,420))

    def testUndeclaredID4(self):
        input = """ 
        int n;

        int foo() {
            n = 1;
            m = 2;
            return m;
        }

        void main() {
            foo();
        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,421))

    def testUndeclaredID5(self):
        input = """ 
        void foo() {
            n = 1;
            x = n;
        }
        int n;
        void main() {
            putFloat(11.34);
            foo();
            return;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,422))

    def testUndeclaredIDinScope1(self):
        input = """ 
        int main() {
            n = 1;
            int n;
            n = 2;
            return 0;
        }
        """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,423))

    def testUndeclaredIDinScope2(self):
        input = """ 
        int n;
        void main() {
            n = 1;
            int n;
            why = 2;
        }
        """
        expect = "Undeclared Identifier: why"
        self.assertTrue(TestChecker.test(input,expect,424))

    def testUndeclaredIDinScope3(self):
        input = """ 
        int n;
        void main() {
            n = 1;
            y[18] = 2;
        }
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def testUndeclaredFunction1(self):
        input = """
        void main() {
            foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,426))

    def testUndeclaredFunction2(self):
        input = """ 
        void main() {
            int func;
            func = 10;
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,427))

    def testUndeclaredFunction3(self):
        input = """ 
        int func(int n) {
            return n * func(n - 1);
        }

        void main() {
            int n;
            n = 10;
            func(n);
            abc();
        }
        """
        expect = "Undeclared Function: abc"
        self.assertTrue(TestChecker.test(input,expect,428))

    def testUndeclaredFunctionUseAst(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))

    def testCorrectDeclared(self):
        input = """ 
        float foo(float a, float b) {
            return a * b;
        }

        int main() {
            float a, b;
            foo(a, b);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    # def test_diff_numofparam_stmt(self):
    #     input = """void main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     input = """void main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_expr_use_ast(self):
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    


    # def testNoTypeMismatchInStatementIf(self):
    #     input = """
    #     void main(){
    #         int n;
    #         if (true){
    #             n = 0;
    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def testTypeMismatchInStatementIf(self):
    #     input = """
    #     void main(){
    #         int i;
    #         if (10.5){
    #             i = 0;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: If(FloatLiteral(10.5),Block([BinaryOp(=,Id(i),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def testTypeMismatchInStatementIf1(self):
    #     input = """
    #     void main(){
    #         int n;
    #         if ("true"){
    #             n = 0;
    #         }
    #     }
    #     """ 
    #     expect = "Type Mismatch In Statement: If(StringLiteral(true),Block([BinaryOp(=,Id(n),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def testTypeMismatchInStatementIf2(self):
    #     input = """
    #     void main(){
    #         int n;
    #         if (n == 10){
    #             n = 1;
    #         }
    #         else {
    #             if (4.4) {
    #                 n = 0;
    #             }
    #         }
    #     }
    #     """ 
    #     expect = "Type Mismatch In Statement: If(FloatLiteral(4.4),Block([BinaryOp(=,Id(n),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def testNoTypeMismatchInStatementFor(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         int a[10];
    #         for (i = 0; i < n; i = i + 1) {
    #             a[i] = 0;
    #         }
    #         return 0;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,439))

    # def testTypeMismatchInStatementFor1(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         int a[10];
    #         for (i == 0; i < n; i = i + 1) {
    #             a[i] = 0;
    #         }
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,440))

    # def testTypeMismatchInStatementFor2(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         int a[10];
    #         for (i = 0; i < n; i == i + 1) {
    #             a[i] = 0;
    #         }
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(==,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,441))

    # def testTypeMismatchInStatementFor3(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         int a[10];
    #         for (i = 0; i = n; i = i + 1) {
    #             a[i] = 0;
    #         }
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
    #     self.assertTrue(TestChecker.test(input,expect,442))

    # def testTypeMismatchInStatementDoWhile(self):
    #     input = """ 
    #     int main() {
    #         int n;
    #         do {
    #             n = n + 1;
    #         }
    #         while (n = 10);
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1)))])],BinaryOp(=,Id(n),IntLiteral(10)))"
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def testTypeMismatchInStatementDoWhile1(self):
    #     input = """ 
    #     int main() {
    #         int n;
    #         do {
    #             n = n + 1;
    #         }
    #         while (4.4);
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1)))])],FloatLiteral(4.4))"
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def testNoTypeMismatchInStatementReturn(self):
    #     input = """ 
    #     void main() {
    #         string s;
    #         s = "checkReturn";
    #         return ;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def testTypeMismatchInStatementReturn(self):
    #     input = """ 
    #     void main() {
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # def testTypeMismatchInStatementReturn1(self):
    #     input = """ 
    #     int[] main() {
    #         int a[10];
    #         return;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return()"
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # def testTypeMismatchInStatementReturn2(self):
    #     input = """ 
    #     float foo(int x, int y, int z) {
    #         if (x == y) {
    #             return 10.0;
    #         }
    #         else {
    #             return true;
    #         }
    #     }

    #     void main() {
    #         int x, y, z;
    #         foo(x, y, z);
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def testTypeMismatchInStatementReturn3(self):
    #     input = """ 
    #     boolean checkPrime(int n) {
    #         if (n < 2) {
    #             return false;
    #         } 
    #         int i;
    #         for (i = 2; i * i <= n ; i = i + 1) {
    #             if (n % i == 0) {
    #                 return 0;
    #             }
    #         }
    #         return true;
    #     }

    #     void main() {
    #         int n;
    #         checkPrime(n);
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
    #     self.assertTrue(TestChecker.test(input,expect,449))

    # def testFuntionNotReturn0(self):
    #     input = """ 
    #     int x;

    #     void funcVoid() {
    #         int a, b;
    #         x = a + b;
    #     }

    #     int getSum(int a, int b) {
    #         return a + b;
    #     }

    #     boolean check(int a, int b) {
    #         if (getSum(a, b) == 10) {
    #             return true;
    #         }
    #     }

    #     float getRes(int a, int b) {
    #         funcVoid();
    #         x = getSum(a, b) / x;
    #         check(a, b);
    #         // must return in this Block
    #     }

    #     void main() {
    #         int a, b;
    #         getRes(a, b);
    #     }
    #     """
    #     expect = "Function check Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def testNotFailFunctionNotReturn(self):
    #     input = """
    #     void main() {
    #         int n;
    #         n = 10;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def testFuntionNotReturn(self):
    #     input = """ 
    #     boolean foo(int a, int b) {
    #         a = b;
    #     }

    #     int main() {
    #         int a, b;
    #         foo(a, b);
    #         return 0;
    #     }
    #     """
    #     expect = "Function foo Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def testBreakNotInLoop(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         for (i = 0; i < n; i = i + 1) {
    #             if (n % i == 0) {
    #                 break;
    #             }
    #             else {
    #                 {
    #                     break;
    #                 }
    #             }
    #         }

    #         do {
    #             i = i + 1;
    #             break;
    #         } while (i <= n);

    #         break; //Here

    #         return 0;
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,453))

    # def testContinueNotInLoop(self):
    #     input = """ 
    #     int main() {
    #         int i, n;
    #         for (i = 0; i < n; i = i + 1) {
    #             if (n % i == 0) {
    #                 continue;
    #             }
    #             else {
    #                 {
    #                     continue;
    #                 }
    #             }
    #         }

    #         do {
    #             i = i + 1;
    #             continue;
    #         } while (i <= n);

    #         continue; //Here

    #         return 0;
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,454))

    # def testNoEntryPoint(self):
    #     input = """ 
    #     int x;

    #     void funcVoid() {
    #         int a, b;
    #         x = a + b;
    #     }

    #     int getSum(int a, int b) {
    #         return a + b;
    #     }

    #     boolean check(int a, int b) {
    #         if (getSum(a, b) == 10) {
    #             return true;
    #         }
    #     }

    #     float getRes(int a, int b) {
    #         funcVoid();
    #         x = getSum(a, b) / x;
    #         check(a, b);
    #         return 10.0;
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def testNoEntryPoint1(self):
    #     input = """ 
    #     int getMax(int n, int a[]) {
    #         int i;
    #         int main;
    #         main = a[0];
    #         for (i = 0; i < n; i = i + 1) {
    #             if (a[i] > main) {
    #                 main = a[i];
    #             }
    #         }
    #         return main;
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def testUnreachableFunction(self):
    #     input = """ 
    #     int getMax(int n) {
    #         int i, a[10];
    #         int max;
    #         max = a[0];
    #         for (i = 0; i < n; i = i + 1) {
    #             if (a[i] > max) {
    #                 max = a[i];
    #             }
    #         }
    #         return max;
    #     }

    #     void main() {
    #         int n;
    #         n = 10;
    #     }
    #     """
    #     expect = "Unreachable Function: getMax"
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def testBreakNotInLoop1(self):
    #     input = """ 
    #     int main() {
    #         int x;
    #         if (x > 10) {
    #             break;
    #         }
    #         return 0;
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,458))

    # def testContinueNotInLoop1(self):
    #     input = """ 
    #     void main() {
    #         int check_con;
    #         check_con = 10000;
    #         if (check_con < 100) {
    #             check_con = 10;
    #         }
    #         else {
    #             continue;
    #         }
    #         return;
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def testUnreachableFunction1(self):
    #     input = """ 
    #     void foo(){}
    #     void main(){}
    #     """
    #     expect = "Unreachable Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,460))

    # def testUnreachableFunction2(self):
    #     input = """ 
    #     void foo() {
    #         foo();
    #     }
    #     void main(){}
    #     """
    #     expect = "Unreachable Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,461))

    # def testFunctionNotReturn1(self):
    #     input = """ 
    #     int main() {
    #         int a;
    #         if (a == 1) {
    #             return 0;
    #         }
    #         else {
    #             a = 1;  
    #         }
    #     }        
    #     """
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,462))

    # def testFunctionNotReturn2(self):
    #     input = """ 
    #     int main() {
    #         int a;
    #         if (a == 1) {
    #             a = 10;
    #         }
    #         else {
    #             return 0;
    #         }
    #     }        
    #     """
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,463))

    # def test(self):
    #     input = """ 
    #     void main(){
    #         foo1() ;
    #     }

    #     void foo1(){
    #         putString("hello world");
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def testFunctionNotReturn3(self):
    #     input = """ 
    #     int foo1() {
    #         return 1;
    #     }
        
    #     int foo2() {
    #         foo1();
    #         return 2;
    #     }

    #     int foo3() {
    #         foo2();
    #         return 3;
    #     }

    #     void main(){}
    #     """
    #     expect = "Unreachable Function: foo3"
    #     self.assertTrue(TestChecker.test(input,expect,465))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,466))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,467))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,468))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,470))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,471))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,472))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,473))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,474))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,476))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,477))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,478))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,479))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,481))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,482))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,483))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,484))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,485))
    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,486))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,487))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,488))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,489))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,490))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,491))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,492))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,493))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,494))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,495))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,496))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,497))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,498))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,499))    


    # int func() {
    #         return 0;
    #     }

    #     void main() {
    #         int func;
    #         func = 15;
    #         func();
    #         abc();
    #     }