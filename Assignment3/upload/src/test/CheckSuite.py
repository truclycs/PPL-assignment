import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

#================Redeclared Variable/Function/Parameter==============
    def testRedeclaredVariableGlobal(self):
        input = """
        int a;
        int a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def testRedeclaredbGlobal(self):  
        input = """
        int b;
        float b;
        void main() {}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,401))

    def testRedeclaredcGlobal(self):  
        input = """
        int c;
        void main() {
            putString("...");
        }
        string c[10];
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,402))

    def testRedeclaredVariable(self):  
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

#================Undeclared Identifier/Function==============

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
        string getString() {
            string s;
            s = "string";
            return s;
        }
        int func(int n) {
            getString();
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

#================Function not return==============

    def testFuntionNotReturn1(self):
        input = """ 
        int x;
        void funcVoid() {
            int a, b;
            x = a + b;
        }
        int getSum(int a, int b) {
            return a + b;
        }
        boolean check(int a, int b) {
            if (getSum(a, b) == 10) {
                return true;
            }
        }
        void getRes(int a, int b) {
            funcVoid();
            x = getSum(a, b) - x;
            check(a, b);
        }
        void main() {
            int a, b;
            getRes(a, b);
        }
        """
        expect = "Function check Not Return "
        self.assertTrue(TestChecker.test(input,expect,431))

    def testFuntionNotReturn2(self):
        input = """ 
        boolean foo(int a, int b) {
            a = b;
        }
        int main() {
            int a, b;
            foo(a, b);
            return 0;
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,432))

    def testFunctionNotReturn3(self):
        input = """ 
        int main() {
            int a;
            if (a == 1) {
                return 0;
            }
            else {
                a = 1;  
            }
        }        
        """
        expect = "Function main Not Return " 
        self.assertTrue(TestChecker.test(input,expect,433))

    def testFunctionNotReturn4(self):
        input = """ 
        int main() {
            int a;
            if (a == 1) {
                a = 10;
            }
            else {
                return 0;
            }
        }        
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,434))

    def testNotFailFunctionNotReturn1(self):
        input = """
        void main() {
            int n;
            n = 10;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def testNotFailFunctionNotReturn2(self):
        input = """
        int main(int n) {
            if (n == 1) {
                return 1;
            }
            else {
                return 0;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,436))

#================Break/Continue not in loop==============

    def testBreakNotInLoop1(self):
        input = """ 
        int main() {
            int i, n;
            for (i = 0; i < n; i = i + 1) {
                if (n % i == 0) {
                    break;
                }
                else {
                    {
                        break;
                    }
                }
            }
            do {
                i = i + 1;
                break;
            } while (i <= n);
            break; //Here
            return 0;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))

    def testBreakNotInLoop2(self):
        input = """ 
        int main() {
            int x;
            if (x > 10) {
                break;
            }
            return 0;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))

    def testContinueNotInLoop1(self):
        input = """ 
        int main() {
            int i, n;
            for (i = 0; i < n; i = i + 1) {
                if (n % i == 0) {
                    continue;
                }
                else {
                    {
                        continue;
                    }
                }
            }
            do {
                i = i + 1;
                continue;
            } while (i <= n);
            continue; //Here
            return 0;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))

    def testContinueNotInLoop2(self):
        input = """ 
        void main() {
            int check_con;
            check_con = 10000;
            if (check_con < 100) {
                check_con = 10;
            }
            else {
                continue;
            }
            return;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,440))

    def testBreakAndContinueInLoop(self):
        input = """ 
        void main() {
            int i, n, res;
            res = 1;
            for (i = 0; i < n; i = i + 1) {
                if (n % i == 0) {
                    res = res * i;
                    continue;
                }
                else {
                    if (n % i == 1) {
                        break;
                    }
                    else {
                        res = res + i;
                    }
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))

#================No Entry Point==============

    def testNoEntryPoint1(self):
        input = """ 
        int x;
        void funcVoid() {
            int a, b;
            x = a + b;
        }
        int getSum(int a, int b) {
            return a + b;
        }
        boolean check(int a, int b) {
            if (getSum(a, b) == 10) {
                return true;
            }
        }
        float getRes(int a, int b) {
            funcVoid();
            x = getSum(a, b) / x;
            check(a, b);
            return 10.0;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,442))

    def testNoEntryPoint2(self):
        input = """ 
        int getMax(int n, int a[]) {
            int i;
            int main;
            main = a[0];
            for (i = 0; i < n; i = i + 1) {
                if (a[i] > main) {
                    main = a[i];
                }
            }
            return main;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,443))

    def testNoEntryPoint3(self):
        input = """
        void foo(int main) {
            putStringLn("No Entry Point");
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,444))

#================Unreachable function==============

    def testUnreachableFunction1(self):
        input = """ 
        int foo1() {
            return 1;
        }
        
        int foo2() {
            foo1();
            return 2;
        }
        int foo3() {
            foo2();
            return 3;
        }
        void main(){}
        """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def testUnreachableFunction2(self):
        input = """ 
        int getMax(int n) {
            int i, a[10];
            int max;
            max = a[0];
            for (i = 0; i < n; i = i + 1) {
                if (a[i] > max) {
                    max = a[i];
                }
            }
            return max;
        }
        void main() {
            int n;
            n = 10;
        }
        """
        expect = "Unreachable Function: getMax"
        self.assertTrue(TestChecker.test(input,expect,446))


    def testUnreachableFunction3(self):
        input = """ 
        void foo(){}
        void main(){}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,447))

    def testUnreachableFunction4(self):
        input = """ 
        void foo() {
            foo();
        }
        void main(){}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,448))

    def testUnreachableFunction5(self):
        input = """ 
        void main() {
            foo1();
        }
        void foo1() {
            foo2();
        }
        void foo2() {
            foo1();
        }
        void foo3(){}
        """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,449))

    def testReachableFunction(self):
        input = """ 
        void main() {
            foo1();
            foo3();
        }
        void foo1() {
            foo2();
        }
        void foo2() {
            foo1();
        }
        void foo3(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

#================Type Mismatch In Statement==============

    def testNoTypeMismatchInStatementIf(self):
        input = """
        int main(){
            if (true) {
                return 1;
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def testTypeMismatchInStatementIf1(self):
        input = """
        void main(){
            if (10.5) {
                int i;
                i = i * i;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(FloatLiteral(10.5),Block([VarDecl(i,IntType),BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)))]))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def testTypeMismatchInStatementIf2(self):
        input = """
        void main(){
            int n;
            if ("true"){
                n = 0;
            }
        }
        """ 
        expect = "Type Mismatch In Statement: If(StringLiteral(true),Block([BinaryOp(=,Id(n),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def testTypeMismatchInStatementIf3(self):
        input = """
        void main(){
            int n;
            if (n == 10){
                n = 1;
            }
            else {
                if (n = n + 1) {
                    n = 0;
                }
            }
        }
        """ 
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1))),Block([BinaryOp(=,Id(n),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def testNoTypeMismatchInStatementFor(self):
        input = """ 
        int main() {
            int i, n;
            int a[10];
            for (i = 0; i < n; i = i + 1) {
                a[i] = 0;
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))

    def testTypeMismatchInStatementFor1(self):
        input = """ 
        int main() {
            int i, n;
            int a[10];
            for (i == 0; i < n; i = i + 1) {
                a[i] = 0;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def testTypeMismatchInStatementFor2(self):
        input = """ 
        int main() {
            int i, n;
            int a[10];
            for (i = 0; i < n; i == i + 1) {
                a[i] = 0;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(==,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def testTypeMismatchInStatementFor3(self):
        input = """ 
        int main() {
            int i, n;
            int a[10];
            for (i = 0; i = n; i = i + 1) {
                a[i] = 0;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def testTypeMismatchInStatementDoWhile1(self):
        input = """ 
        int main() {
            int n;
            do {
                n = n + 1;
            }
            while (n = 10);
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1)))])],BinaryOp(=,Id(n),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def testTypeMismatchInStatementDoWhile2(self):
        input = """ 
        int main() {
            int n;
            do {
                n = n + 1;
            }
            while (4.4);
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1)))])],FloatLiteral(4.4))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def testNoTypeMismatchInStatementDoWhile(self):
        input = """ 
        int main() {
            int n;
            do {
                n = n + 1;
            }
            while (true);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def testNoTypeMismatchInStatementReturn1(self):
        input = """ 
        void main() {
            string s;
            s = "checkReturn";
            return ;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))

    def testNoTypeMismatchInStatementReturn2(self):
        input = """ 
        int main() {
            int a[10];
            a[7] = 15;
            return a[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def testReturnValueInVoidFunc(self):
        input = """ 
        void main() {
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def testReturnFloatInIntFunc(self):
        input = """ 
        int main() {
            return 1.16;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.16))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def testReturnBoolInFloatFunc(self):
        input = """ 
        float foo(int x, int y, int z) {
            if (x == y) {
                return 10.0;
            }
            else {
                return true;
            }
        }
        void main() {
            int x, y, z;
            foo(x, y, z);
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def testReturnZeroInBoolFunc(self):
        input = """ 
        boolean checkPrime(int n) {
            if (n < 2) {
                return false;
            } 
            int i;
            for (i = 2; i * i <= n ; i = i + 1) {
                if (n % i == 0) {
                    return 0;
                }
            }
            return true;
        }
        void main() {
            int n;
            checkPrime(n);
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def testReturnBoolFuncInIntFunc(self):
        input = """ 
        boolean checkPrime(int n) {
            if (n < 2) {
                return false;
            } 
            int i;
            for (i = 2; i * i <= n ; i = i + 1) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
        int get(int n) {
            return checkPrime(n);
        }
        void main() {
            int n;
            get(n);
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(checkPrime),[Id(n)]))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def testTypeMismatchInStatementReturn(self):
        input = """ 
        int[] main() {
            int a[10];
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

    def testTypeMismatchInStatementReturn7(self):
        input = """ 
        int[] main() {
            int a[10];
            return a[0];
        }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,470))

#================ Type Mismatch In Expression===============

    def testDiffNumofparamStmt(self):
        input = """
        void main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def testDiffNumofparamExpr(self):
        input = """
        void main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def testOverrideFuncFooByVarFoo(self):
        input = """
        int foo() {
            return 0;
        }

        void foo2() {
            foo();
        }

        void main(){
            int foo;
            foo = 5;
            foo2();
            foo();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def testUnary(self):
        input = """
        void main() {
            boolean flag;
            !flag;
            int a;
            !a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def testTypeMismatchInExp(self):
        input = """
        void main(){
            string str;
            int num;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = 15;
            num = 15;
            num && fNum;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(num),Id(fNum))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def testTypeMismatchInGetInt(self):
        input = """ 
        int main() {
            return getInt(5);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,476))

    def testTypeMismatchInPutInt(self):
        input = """ 
        void main() {
            putInt("input");
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putInt),[StringLiteral(input)])"
        self.assertTrue(TestChecker.test(input,expect,477))

    def testTypeMismatchInGetFloat(self):
        input = """ 
        float main() {
            return getFloat(1.53);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getFloat),[FloatLiteral(1.53)])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def testTypeMismatchInPutFloat(self):
        input = """ 
        void main() {
            getFloat(putInt(18));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getFloat),[CallExpr(Id(putInt),[IntLiteral(18)])])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def testTypeMismatchInPutBool(self):
        input = """ 
        void main() {
            putBool("true");
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putBool),[StringLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def testTypeMismatchInPutString(self):
        input = """ 
        void main() {
            putString(false);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putString),[BooleanLiteral(false)])"
        self.assertTrue(TestChecker.test(input,expect,481))

    def testBuiltIn(self):
        input = """ 
        void main() {
            int a;
            a = getInt();
            putIntLn(4);
            putFloat(4.4);
            putFloatLn(4.4);
            putBool(true);
            putBoolLn(false);
            putString("Built-in");
            putStringLn("Built-in");
            putLn();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def testTypeMismatchInArray(self):
        input = """
        void main(){
            int arr[10];
            float num;
            num = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[num];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),Id(num))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def testTypeMismatchBinaryOp(self):
        input = """ 
        void main() {
            int a;
            float b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def testConditionIfByFloat(self):
        input = """ 
        void main() {
            float a;
            if (a != 4.4) {
                a = 4;
            }
            else {
                a = 2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),FloatLiteral(4.4))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def testCorrectInExp(self):
        input = """ 
        int foo(int x) {
            return x * x;
        }

        int[] main(int a[]) {
            int b[10];
            int x;
            x = 10;
            if (foo(x) == 100) {
                return a;
            }
            else {
                return b;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))

    def testTypeMismatchWithFloat(self):
        input = """ 
        void main() {
            float f;
            f = f % 10;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(f),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def testTypeMismatchWithBoolean(self):
        input = """ 
        void main() {
            boolean flag;
            if (flag <= true) {
                flag = false;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(flag),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def testPlusBooleanWithFloat(self):
        input = """ 
        void main() {
            boolean flag;
            flag = true;
            float f;
            f = 4.4;
            f = f + flag;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(f),Id(flag))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def testAssignInArrayPointerType(self):
        input = """
        int[] getArr(int a[]) {
            int b[10];
            if (b[0] < 10) {
                return b;
            }
            else {
                return a;
            }
        }

        void main(int b[]) {
            int a[10];
            b = getArr(a);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(getArr),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def testTypeMatch(self):
        input = """ 
        void main(){
            int n;
            foo(complex(n));
        }
        int foo(int a[]){
            int arr;
            return arr;
        }
        int[] complex(int a){
            int f[10];
            return f;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))

    def testTypeMismacthPara(self):
        input = """ 
        void main(){
            int n;
            foo(complex(n));
        }
        int foo(int a[]){
            int arr;
            return arr;
        }
        float[] complex(int a){
            float f[10];
            return f;
        }        
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(complex),[Id(n)])])"
        self.assertTrue(TestChecker.test(input,expect,492))

    def testTypeMismacthWithFunc(self):
        input = """ 
        int foo(int x) {
            if (x == 0) {
                return 1;
            }
            return foo(x - 1) * x;
        }

        void main() {
            foo();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def testDivFloatValue(self):
        input = """ 
        void main() {
            int a, b, c;
            float d;
            b = d / c + a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(+,BinaryOp(/,Id(d),Id(c)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,494))

#================ Not Left Value ===============

    def testLiteralInLeftExp(self):
        input = """ 
        void main() {
            int a;
            10 = a;   
        }
        """
        expect = "Not Left Value: IntLiteral(10)"
        self.assertTrue(TestChecker.test(input,expect,495))

    def testNotLeftValue(self):
        input = """
        void main() {
            int a;
            a + 1 = 10;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def testLeftExpIsFunc(self):
        input = """ 
        int foo(int x) {
            return x;
        }

        void main() {
            int n;
            foo(n) = n;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[Id(n)])"
        self.assertTrue(TestChecker.test(input,expect,497))

    def testLeftExpIsBool(self):
        input = """
        void main() {
            boolean flag;
            true = flag;
        }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,498))

#================CORRECR TEST===============

    def testCorrect(self):
        input = """ 
        int n, m;

        float F(int x) {
            float f;
            return f;
        }

        int I(boolean b) {
            int i;
            return i;
        }

        boolean B() {
            boolean b;
            return b;
        }

        void total() {
            F(I(B()));
        }
 
        int checkReturn(int a[], int x) {
            if (x + 10 > 20) {
                if (true) {
                    if (true) {
                        return 1;
                    }
                    else {
                        return 0;
                    }
                }
                return 1;
            }
            return x * x * x;
        }

        float checkFloat(float f) {
            float a, b, c, d;
            f = (a * b + c) + checkFloat(d);
            return f;
        }

        int[] arr(){
            int a [20]; 
            return a;
        }

        int main() {
            int a[10], x;
            float f;
            n = checkReturn(a, x);
            f = checkFloat(f);
            a[0] = a[1];

            int i;
            for (i = 0; i < n; i = i + 1) {
                if (a[i] % 2 == 0) {
                    a[i] = a[i] * 2; 
                }
                else {
                    break;
                }
            }
            arr()[10] = 10;
            total();
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))    