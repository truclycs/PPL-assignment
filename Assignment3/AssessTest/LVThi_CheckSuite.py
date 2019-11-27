import unittest
from TestUtils import TestChecker
from AST import *
#1613289 - Lê Văn Thi
class CheckSuite(unittest.TestCase):
    def test_func_1(self):
        """Simple program: int main() {} """
        input = """void main() {} int main1(){}"""
        expect = "Function main1 Not Return "
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_func_2(self):
        """More complex program"""
        input = """void main () {
            int c,b;
            int c;
        }"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_func_3(self):
        """More complex program"""
        input = """void main () {
            int a;
        }
        int foo(){float a;}"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_func_4(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_func_5(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_func_6(self):
        """More complex program""" 
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_func_7(self):
        """More complex program"""
        input = """void main () {
            foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_func_8(self):
        """More complex program"""
        input = """void main () {
            bar();
        }
        int a,b;"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_func9(self):
        """More complex program"""
        input = """void main () {
            int x;
            foo5(x);
        }
        int foo5(){return 0;}"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo5),[Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_func_10(self):
        """More complex program"""
        input = """int a;
        void main () {
            int a,b;
            a = foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_func_redecl(self):
        """More complex program"""
        input = """int foo10;
        void foo10(){}
        void main () {
            int a,b;
            foo10();
        }"""
        expect = "Redeclared Function: foo10"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_func_11(self):
        """More complex program"""
        input = """int foo(int a){return 0;}
        void main () {
            int a,b;
            string str;
            foo();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_func_12(self):
        """More complex program"""
        input = """//int a;
        void main () {
            
        }
        int foo(){return;}
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_func_13(self):
        """More complex program"""
        input = """//int a;
        void main () {
            return ;
            foo_(3);
            getInt();
        }
        int foo_(int a){return a;}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_func_14(self):
        """More complex program"""
        input = """//int a;
        void main () {
            return ;
        }
        int foo(){return 0;}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_func_15(self):
        """More complex program"""
        input = """//int a;
        void main () {
            return ;
        }
        int foo(){return 0;}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_var_1(self):
        """More complex program"""
        input = """int a;
        void main () {
            int e, f;
            string str;
            float f;
        }
        """
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_var_2(self):
        """More complex program"""
        input = """int a;
        void main () {
            int a, b;
        }
        void foo(int a, int b){int b;}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_var_3(self):
        """More complex program"""
        input = """
        void main () {
            string a, b;
        }
        int foo(int a){ return b;}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_var_4(self):
        """More complex program"""
        input = """void foo(int a){ }
        void main () {
            return ;
        }
        int foo;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_ifStmt(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            if (a = 0) b = 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(b),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_ifStmt_1(self):
        """More complex program"""
        input = """
        void main () {
            int a;
            if (b == 0) a = 0;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_ifStmt_2(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            if (a != b) doSomeThing();
        }
        """
        expect = "Undeclared Function: doSomeThing"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_ifStmt_3(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            if (a != b) {
                a = b;
                if (b > 0) b = 0;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_ifStmt_4(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            if (a + b) a = 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),BinaryOp(=,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_ifStmt_5(self):
        """More complex program"""
        input = """
        int foo(int a){
            if (a == 0) return 0;
            if (a > 0) return 1;
            return 2;
        }
        void main () {
            float x;
            x = foo(3);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_forStmt_1(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            for (a = 0; a == 2; a < 10){
                b = b + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(0));BinaryOp(==,Id(a),IntLiteral(2));BinaryOp(<,Id(a),IntLiteral(10));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_forStmt_2(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            for (a < 0; a == 2; a = a +1 ) b = 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(<,Id(a),IntLiteral(0));BinaryOp(==,Id(a),IntLiteral(2));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(b),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_forStmt_3(self):
        """More complex program"""
        input = """void foo(){}
        void main () {
            int a, b;
            for (a = 1; a < 10; a = a + 2) b = b + a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_forStmt_4(self):
        """More complex program"""
        input = """
        void main () {
            for (a = 0; a < 10; a + 1) a = 2;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_forStmt_0(self):
        """More complex program"""
        input = """
        void main (int a) {
            a = b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_doWhile_1(self):
        """More complex program"""
        input = """
        void main () {
            do foo31(); while(i > 0);
        }
        void foo31(){}
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_doWhile_2(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            do {
                foo();
            } while(i);
        }
        void foo(){}
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(foo),[])])],Id(i))"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_doWhile_3(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            do {
                
            } while (foo2());
        }
        float foo2(){return 1.0;}
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(foo2),[]))"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_doWhile_4(self):
        """More complex program"""
        input = """int a;
        void main () {
            do {
                a = foo(b);
            } while (true);
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_doWhile_5(self):
        """More complex program"""
        input = """int a;
        void main () {
            do {
                int a;
                string a;
            } while (a == 0);
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_param_1(self):
        """More complex program"""
        input = """int a;
        void main () {
            
        }
        int foo(int foo, int i){
            int i;
            return 0;
        }
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_param_2(self):
        """More complex program"""
        input = """int a;
        void main () {
            int foo;
            foo(foo, a);
        }
        int foo(int foo, int n){return (foo + n);}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_param_3(self):
        """More complex program"""
        input = """int a;
        void main (int main) {
            main = 2;
            foo(a);

        }
        int foo(){return 0;}
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_param_4(self):
        """More complex program"""
        input = """int a;
        void main (int main) {
            main = 2;
            foo(a);

        }
        int foo(){return 0;}
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_build_in_func_1(self):
        """More complex program"""
        input = """int a;
        void main () {
            getFloat();
            putIntLn();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_build_in_func_2(self):
        """More complex program"""
        input = """string a;
        void main () {
            putString(a) + 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(putString),[Id(a)]),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_build_in_func_3(self):
        """More complex program"""
        input = """int a;
        void main () {
            putLn(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_build_in_func_4(self):
        """More complex program"""
        input = """
        void main () {
            float a;
            a = getFloat();
            putIntLn(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_build_in_func_5(self):
        """More complex program"""
        input = """
        void main () {
            putFloat(getFloat(putLn()));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getFloat),[CallExpr(Id(putLn),[])])"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_invalid_assign_1(self):
        """More complex program"""
        input = """int a;
        void main () {
            a = "String";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(String))"
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_invalid_assign_2(self):
        """More complex program"""
        input = """int a;
        void main () {
            a = 10.5;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(10.5))"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_invalid_assign_3(self):
        """More complex program"""
        input = """int a;
        float f;
        void main () {
            f = a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_invalid_assign_4(self):
        """More complex program"""
        input = """
        void main () {
            string s;
            s = "String";
            s1 = s;
        }
        """
        expect = "Undeclared Identifier: s1"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_invalid_assign_5(self):
        """More complex program"""
        input = """
        void main () {
            boolean b;
            b = true;
            b = 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_invalid_assign_6(self):
        """More complex program"""
        input = """
        int foo() {return 2;}
        void main () {
            boolean b;
            b = foo();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_invalid_assign_7(self):
        """More complex program"""
        input = """
        void main () {
            string s;
            s = foo();
        }
        void foo(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(s),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_invalid_assign_8(self):
        """More complex program"""
        input = """
        void main () {
            float f;
            f = foo();
        }
        int foo(int i){
            return i + i;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_invalid_assign_9(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            float f;
            a = b + f;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(f))"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_invalid_assign_10(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            float f;
            boolean b;
            b = i > f;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(i),Id(f))"
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_not_left_value_1(self):
        """More complex program"""
        input = """
        void foo(){}
        void main () {
            foo() = 3;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_not_left_value_2(self):
        """More complex program"""
        input = """
        void main () {
            3 = 3;
        }
        """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_not_left_value_3(self):
        """More complex program"""
        input = """
        int a;
        void main () {
            2 = a + a;
        }
        """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_not_left_value_4(self):
        """More complex program"""
        input = """
        float f;
        void main () {
            f + 3.3 = 9.3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(f),FloatLiteral(3.3))"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_not_left_value_5(self):
        """More complex program"""
        input = """
        int foo(){return 2;}
        void main () {
            int y;
            y * 2 = foo();
        }
        """
        expect = "Not Left Value: BinaryOp(*,Id(y),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_break_continue_in_loop_1(self):
        """More complex program"""
        input = """
        int foo(){return 2;}
        void main () {
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_break_continue_in_loop_2(self):
        """More complex program"""
        input = """
        int foo(){return 2;}
        void main () {
            {{continue;}}
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_break_continue_in_loop_3(self):
        """More complex program"""
        input = """
        void main () {
            int i, a;
            for (i = 0; i < 10; i = i + 2){
                if (i == 4) continue;
                else a = a + i;
            }
            print(a);
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_break_continue_in_loop_4(self):
        """More complex program"""
        input = """
        void main () {
            int x;
            x = 10;
            do {
                if(x < 0) break;
                x = x - 1;
            } while (true);
            putInt(x);
            return x;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(x))"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_break_continue_in_loop_5(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            do{
                int x;
                {
                    if (true) {
                        x = 2;
                        break;
                    }
                }
            }while(i < 0);
            x = 0;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_break_continue_in_loop_6(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            for(i = 0; i < 6; i = i + 1){
                int x;
                {
                    if (true) {
                        break;
                    }
                    x = 3;
                }
            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_break_continue_in_loop_7(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            {
                int x,y;
                int z;
                {
                    {
                        continue;
                        i = i + 1;
                        z = x + y;
                    }
                }
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_combine_1(self):
        input = """
        void main () {
            int x;
            int arr[5];
            arr[2] = x;
            arr[x] + x = 10; 
        }
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(arr),Id(x)),Id(x))"
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_combine_2(self):
        input = """
        void main () {
            boolean b;
            int x;
            if (b == true){
                x = x + 1;
            } else{
                x = b;
            }
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_combine_3(self):
        input = """
        int foo(){return 1;}
        void main (int x) {
            int foo;
            foo = 2;
            foo(foo);
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_combine_4(self):
        input = """
        void main () {
            int x;
            do{
                x = x + 1;
            } while(foo(x) == false);
        }
        int foo(int x){return x;}
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(foo),[Id(x)]),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_combine_5(self):
        input = """
        void main () {
            float x;
            x = 2;
            {
                if (x == 2) x = 3;
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_combine_6(self):
        input = """
        void main () {
            int f,z;
            for(f = 2; f < 3; f){
                z = z  + f;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_combine_7(self):
        input = """
        void main () {
            {
                int i;
                float f;
                string s;
            }
            i = f;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_combine_8(self):
        input = """
        void main () {
            int x;
            float f;
            foo(x);
            foo(f);

        }
        void foo(int x){
        }
        void foo(float x){

        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_combine_9(self):
        input = """
        int i;
        void main () {
            if (i < 0 || i > 10){
                putString("OK");
            } else{
                putString("Not OK");
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_combine_10(self):
        input = """
        void main () {
            float f;
            f = -2.2 + 1;
            int i;
            i = foo(f);
        }
        int foo(float f){return f;}
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,UnaryOp(-,FloatLiteral(2.2)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_combine_11(self):
        input = """
        void main () {
            int a,b,c;
            a = getInt();
            b = getInt();
            c = getInt();
            if (a > b) putString("a > b");
            else if (a < b) putString("a < b");
            else putString("a = b");
        }
        boolean foo(int x){}
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_combine_12(self):
        input = """
        int main () {

            return 0;
            return 0;
        }
        void main(){
            return;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_combine_13(self):
        input = """
        int n;
        float f;
        void main () {
            putString("enter a number");
            n = getInt();
            if (n/2 == 0) putStringLn("So da nhap la so chan");
            else putStringLn("So da nhap la so le");
            putString("Press anykey to end!");
            getString();
            return;
        }
        """
        expect = "Undeclared Function: getString"
        self.assertTrue(TestChecker.test(input,expect,479))
	def test_all_1(self):
		"""More complex program"""
        input = """
        int foo(){return 2;}
        void main () {
            int a;
            a * 2 = foo();
        }
        """
        expect = "Not Left Value: BinaryOp(*,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,480))
	def test_all_2(self):
		"""More complex program"""
        input = """
        float f;
        void main () {
            f + 2.3 = 10.3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(f),FloatLiteral(2.3))"
		self.assertTrue(TestChecker.test(input,expect,481))
	def test_all_3(self):
        """More complex program"""
        input = """
        float f;
        void main () {
            f + 4.3 = 9.3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(f),FloatLiteral(4.3))"
        self.assertTrue(TestChecker.test(input,expect,482))
	def test_all_4(self):
        """More complex program"""
        input = """
        void main () {
            10 = 10;
        }
        """
        expect = "Not Left Value: IntLiteral(10)"
        self.assertTrue(TestChecker.test(input,expect,483))
	def test_all_5(self):
        """More complex program"""
        input = """
        void foo(){}
        void main () {
            foo() = 4;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,484))
	def test_all_6(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            float f;
            boolean b;
            b = i > f;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(i),Id(f))"
        self.assertTrue(TestChecker.test(input,expect,485))
	def test_all_7(self):
        """More complex program"""
        input = """
        void main () {
            int a, b;
            float f;
            a = b + f;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(f))"
        self.assertTrue(TestChecker.test(input,expect,486))
	def test_all_8(self):
        """More complex program"""
        input = """
        void main () {
            float f;
            f = foo();
        }
        int foo(int i){
            return i + i;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,487))
	def test_all_9(self):
        """More complex program"""
        input = """
        int foo() {return 2;}
        void main () {
            boolean b;
            b = foo();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,488))
	def test_all_10(self):
        """More complex program"""
        input = """
        void main () {
            boolean b;
            b = true;
            b = 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,489))
	def test_all_11(self):
        """More complex program"""
        input = """
        void main () {
            string s;
            s = "String";
            s1 = s;
        }
        """
        expect = "Undeclared Identifier: s1"
        self.assertTrue(TestChecker.test(input,expect,490))
	def test_all_12(self):
        """More complex program"""
        input = """int a;
        float f;
        void main () {
            f = a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))
	def test_all_13(self):
        """More complex program"""
        input = """int a;
        void main () {
            a = 2.2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(2.2))"
        self.assertTrue(TestChecker.test(input,expect,492))
	def test_all_14(self):
        """More complex program"""
        input = """int a;
        void main () {
            a = "String";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(String))"
        self.assertTrue(TestChecker.test(input,expect,493))
	def test_all_15(self):
        """More complex program"""
        input = """
        void main () {
            putFloat(getFloat(putLn()));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getFloat),[CallExpr(Id(putLn),[])])"
        self.assertTrue(TestChecker.test(input,expect,494))
	def test_all_16(self):
        """More complex program"""
        input = """
        void main () {
            float a;
            a = getFloat();
            putIntLn(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,495))
	def test_all_17(self):
        """More complex program"""
        input = """int a;
        void main () {
            putLn(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,496))
	def test_all_18(self):
        """More complex program"""
        input = """string a;
        void main () {
            putString(a) + 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(putString),[Id(a)]),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,497))
	def test_all_19(self):
        """More complex program"""
        input = """int a;
        void main () {
            getFloat();
            putIntLn();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,498))
	def test_all_20(self):
        """More complex program"""
        input = """int a;
        void main (int main) {
            main = 2;
            foo(a);

        }
        int foo(){return 0;}
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,499))
	
		
		

