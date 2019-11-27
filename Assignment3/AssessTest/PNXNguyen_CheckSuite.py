"""
    Name: Pham Nguyen Xuan Nguyen
    ID: 1712393
"""
import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    #Redeclared Error
    def test_redeclared_global_variable(self):
        input = """
        int a; 
        int a; 
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_function(self):
        input = """
        int main; 
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_local_variable(self):
        input = """
        int b; 
        void main(){
            int a;
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_function(self):
        input = """
        int a(){
            return 1;
        }
        void a(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_parameter(self):
        input = """
        void main(int c, int c){}"""
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_parameter_local_variable(self):
        input = """ 
        void main(int a){
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_block_variable(self):
        input = """
        void main(){
            {
                int a;
                int a;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_block_block_variable(self):
        input = """ 
        void main(){
            int a;
            {
                int a;
                {
                    int b;
                    int b;
                }
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_arraytype(self):
        input = """
        void main(){
            int a[5];
            int a[3];
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_variable_arraytype(self):
        input = """
        void main(){
            int a;
            int a[10];
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    #Undeclared Error
    def test_undeclared_global_variable(self):
        input = """
        int a;  
        void main(){
            b = 5;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_ifstmt_expr(self):
        input = """
        void main(){
            int b;
            if (a > 5) b = 5;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_forstmt_expr(self):
        input = """
        void main(){
            int b;
            for (i; i < 10; i = i + 1){
                b = b + 1;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_dowhilestmt_expr(self):
        input = """
        void main(){
            int b;
            do a = 5; b = b + 1; while(b == 0);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_returnstmt_expr(self):
        input = """
        void main(){
            return a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_undeclared_function_priority(self):
        input = """
        void main(){
            foo();
        }
        void fo(){
            f();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_function_binaryop_expr(self):
        input = """
        void main(){
            int a;
            a = foo(3)[3];
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_function_infunction(self):
        input = """
        int foo(int a){
            return 1;
        }
        void main(){
            int a;
            a = foo(fo(1));
        }
        """
        expect = "Undeclared Function: fo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_identifier_function_priority(self):
        input = """
        void main(){
            a = foo();
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_function_identifier_priority(self):
        input = """
        void main(){
            foo() = a;
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_typemismatchstatement_ifstmt(self):
        input = """
        void main(){
            int a;
            if (a) a = 2;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_typemismatchstatement_forstmt_expr2(self):
        input = """
        void main(){
            int a;
            for (a; a+1; a = a + 1){
                a = 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(+,Id(a),IntLiteral(1));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_typemismatchstatement_forstmt_expr1(self):
        input = """
        void main(){
            int a;
            for (a/1.0; a > 10; a = a + 1){
                a = 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(/,Id(a),FloatLiteral(1.0));BinaryOp(>,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_typemismatchstatement_forstmt_expr3(self):
        input = """
        void main(){
            int a;
            for (a/1; a > 10; a == a + 1){
                a = 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(/,Id(a),IntLiteral(1));BinaryOp(>,Id(a),IntLiteral(10));BinaryOp(==,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_typemismatchstatement_dowhilestmt_expr(self):
        input = """
        void main(){
            int a;
            do a = 3; while(a);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),IntLiteral(3))],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_typemismatchstatement_returnstmt_voidtype(self):
        input = """
        void main(){
            int a;
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_typemismatchstatement_returnstmt_inttype(self):
        input = """
        float foo(){
            return 1;
        }
        int main(){
            float a;
            return foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_typemismatchstatement_returnstmt_string_arraypointertype(self):
        input = """
        string[] SO(string a[]){
            string b;
            return b;
        }
        void main(){
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_typemismatchstatement_returnstmt_string_arraytype(self):
        input = """
        boolean S(string a[]){
            boolean b[5];
            return b;
        }
        void main(){
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_typemismatchstatement_binaryop_forstmt(self):
        input = """
        void main(){
            int a;
            for (a = 1; a > 10; --a){
                if (a) a = 0;
                else a = 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,429))

    #TypeMismatchExpression Error
    def test_typemismatchexpress_arraytype_E1(self):
        input = """
        void main(){
            int a;
            a[2] = 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_typemismatchexpress_arraytype_E2(self):
        input = """
        void main(){
            int a[1];
            a[a] = 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_typemismatchexpress_arraypointertype(self):
        input = """
        int foo(int a[]){
            a = 0;
            return a[1];
        }
        void main(){
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_typemismatchexpress_binaryexpression_arraypointertype(self):
        input = """
        void main(int b[]){
            int a;
            b = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_typemismatchexpress_binaryexpression_arraytype(self):
        input = """
        void main(){
            int a[1];
            a = 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_typemismatchexpress_binaryexpression_booltype(self):
        input = """
        void main(){
            boolean a;
            int b;
            b = a + 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_typemismatchexpress_binaryexpression_booltype_ifstmt(self):
        input = """
        void main(){
            boolean a;
            int b;
            if (a + 1) b = 1;
            else b = 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_typemismatchexpress_binaryexpression_inttype(self):
        input = """
        void main(){
            int a;
            int b;
            b = b == a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(==,Id(b),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_typemismatchexpress_binaryexpression_inttype_ifstmt(self):
        input = """
        void main(){
            int a;
            float b;
            if(b == a) a = 1;
            else a = 0; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_typemismatchexpress_binaryexpression_floattype(self):
        input = """
        void main(){
            float a;
            float b;
            boolean c;
            c = b == a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_typemismatchexpress_binaryexpression_floattype_ifstmt(self):
        input = """
        void main(){
            float a;
            float b;
            if(b == a) a = 1;
            else a = 0; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_typemismatchexpress_binaryexpression_floattype_unaryop(self):
        input = """
        void main(){
            int a;
            float b;
            a = -b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),UnaryOp(-,Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_typemismatchexpress_binaryexpression_stringtype(self):
        input = """
        void main(){
            string a;
            string b;
            a = a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_typemismatchexpress_binaryexpression_stringtype_ifstmt(self):
        input = """
        void main(){
            string a;
            string b;
            if (a == b) a == "a";
            else a == "b";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_typemismatchexpress_functioncall_notparam(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            int a;
            a = foo(2);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_typemismatchexpress_functioncall_notparamtype(self):
        input = """
        int foo(int a){
            return 1;
        }
        void main(){
            int a;
            float b;
            a = foo(b);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_typemismatchexpress_functioncall_notparamtype_arraypointertype(self):
        input = """
        int foo(int a[]){
            return 1;
        }
        void main(){
            int a;
            int b[1];
            a = foo(b[1]);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(b),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_typemismatchexpress_functioncall_notparamtype_arraytype(self):
        input = """
        int foo(int a[]){
            return 1;
        }
        void main(){
            int a;
            int b[1];
            b[1] = foo(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_typemismatchexpress_binaryop_mod(self):
        input = """
        void main(){
            float a;
            int b;
            b = a % b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_typemismatchexpress_binaryop_div(self):
        input = """
        void main(){
            float a;
            int b;
            b = a / b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(/,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,449))

    #Functionnotreturn Error
    def test_functionnotreturn(self):
        input = """
        int main(){
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_functionnotreturn_function(self):
        input = """
        int foo(){
        }
        void main(){
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_functionnotreturn_ifstmt_noelsestmt(self):
        input = """
        int main(){
            int a;
            if (true) return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_functionnotreturn_ifstmt_elsestmt(self):
        input = """
        int main(){
            int a;
            if (true) return 1;
            else a = 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_functionnotreturn_noifstmt_elsestmt(self):
        input = """
        int main(){
            int a;
            if (true) a = 1;
            else return a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_functionnotreturn_forstmt(self):
        input = """
        int main(){
            int a;
            for (a = 1; a > 10; --a) return a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_functionnotreturn_forstmt_block(self):
        input = """
        int main(){
            int a;
            for (a = 1; a > 10; --a) {
                if (a == 1) return 1;
                else return 2;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_functionnotreturn_dowhilestmt(self):
        input = """
        int main(){
            int a;
            do a = 1; while(a != 1);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_functionnotreturn_dowhilestmt_block(self):
        input = """
        int main(){
            int a;
            do {
                for (a = 1; a < 0; a = a + 1) return 1;
            } while(a != 1);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_functionnotreturn_dowhilestmt_block_ifstmt(self):
        input = """
        int main(){
            int a;
            do {
                for (a = 1; a < 0; a = a + 1) return 1;
            } while(a != 1);
            if (a == 1) return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_breaknotinloop_dowhilestmt(self):
        input = """
        int main(){
            int a;
            do {
                for (a = 1; a < 0; a = a + 1) return 1;
                return 2;
            } while(a != 1);
            break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_breaknotinloop(self):
        input = """
        int main(){
            break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_breaknotinloop_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_breaknotinloop_forstmt_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) {
                for (a = 1; a < 10; --a) {
                    a = a + 1;
                }
                break;
            }
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_breaknotinloop_dowhilestmt_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) {
                do a = a + 1; while (a < 10);
                break;
            }
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_continuenotinloop_dowhilestmt(self):
        input = """
        int main(){
            int a;
            do {
                for (a = 1; a < 0; a = a + 1) return 1;
                return 2;
            } while(a != 1);
            continue;
            return 1;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_continuenotinloop(self):
        input = """
        int main(){
            continue;
            return 1;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_continuenotinloop_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) continue;
            return 1;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_continuenotinloop_forstmt_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) {
                for (a = 1; a < 10; --a) {
                    a = a + 1;
                    break;
                }
                continue;
            }
            return 1;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_continuenotinloop_dowhilestmt_ifstmt(self):
        input = """
        int main(){
            int a;
            if (a == 1) {
                do a = a + 1; break; while (a < 10);
                continue;
            }
            return 1;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    #Noentrypoint Error
    def test_noentrypoint(self):
        input = """
        int foo(){
            return 1;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_noentrypoint_global_variable(self):
        input = """
        int main;
        int noentrypoint(){
            return main;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_noentrypoint_global_variable_main(self):
        input = """
        int main;
        int mai(){
            int main;
            return 1;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_noentrypoint_local_variable_main(self):
        input = """
        int foo(){
            int main;
            return 1;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_noentrypoint_local_variable_main_thisis(self):
        input = """
        int thisisnotmain(){
            int thisismainvariable;
            return thisismainvariable;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,474))

    #Unreachablefunction Error
    def test_unreachablefunction(self):
        input = """
        int foo(int a){
            fo();
            return 1;
        }
        void fo(){}
        void main(){
            int a;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_unreachablefunction_priority(self):
        input = """
        int foo(){
            return 1;
        }
        void fo(){}
        void main(){
            int a;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_unreachablefunction_priority_aftermainfunction(self):
        input = """
        void main(){
            int a;
        }
        int foo(){
            return 1;
        }
        void fo(){}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_unreachablefunction_priority_global_variable(self):
        input = """
        void main(){
            int a;
        }
        int b;
        void foo(){
            b = 2;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_unreachablefunction_priority_global_variable_priority(self):
        input = """
        void fo(){
        }
        void main(){
            int a;
        }
        int b;
        void foo(){
            b = 2;
        }
        """
        expect = "Unreachable Function: fo"
        self.assertTrue(TestChecker.test(input,expect,479))

    #Noleftvalue
    def test_noleftvalue_inttype(self):
        input = """
        void main(){
            int a;
            2 = a;
        }
        """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_noleftvalue_floattype(self):
        input = """
        void main(){
            float a[4];
            26.9 = a[2];
        }
        """
        expect = "Not Left Value: FloatLiteral(26.9)"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_noleftvalue_stringtype(self):
        input = """
        void main(){
            string a;
            "a" = a;
        }
        """
        expect = "Not Left Value: StringLiteral(a)"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_noleftvalue_booltype(self):
        input = """
        void main(){
            boolean a[3];
            true = a[1];
        }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_noleftvalue_random(self):
        input = """
        void main(int a[]){
            int b;
            28.8 = b;
        }
        """
        expect = "Not Left Value: FloatLiteral(28.8)"
        self.assertTrue(TestChecker.test(input,expect,484))

    #Random Error
    def test_random_dowhilestmt(self):
        input ="""void main(){
            int a;
            int b;
            a = 1;
            b = 0;
            do {a = a + 1.0; b = b - 1;
            } while a <= 10 && b > -10 ;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_random_forstmt(self):
        input = """int main(){
            int i, a[5];
            int i, j, a[5];
            for (i = 10; i > 0; --i) {
                for (j = 0; j < i; j = j + 1) 
                    a[i] = j; a[0] = 0;
            }
            return i;
        }"""
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_ifstmt_10(self):
        input = """int main(){
            string a;
            boolean b;
            if (a == "a") b = true;
            else {
                if (a == "b") b = false;
                else {a = "c";
                }
            }
            return 1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_random_breakstmt(self):
        input = """int main(){
            float i;
            i = 0.0;
            for (i;i < 10.0;i = i + 1.0) 
                if (i == 5) break;
            return 1;
        }"""
        expect = "Type Mismatch In Statement: For(Id(i);BinaryOp(<,Id(i),FloatLiteral(10.0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),FloatLiteral(1.0)));If(BinaryOp(==,Id(i),IntLiteral(5)),Break()))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_random_continuestmt(self):
        input = """int main(){
            boolean b;
            int i, j;
            j = 10;
            for (i = 0; i < 10; i = i + 1) {
                b = i > 5; 
                if (b == true) continue;
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_random_returnstmt(self):
        input = """int main(){
            float y, i;
            y = 0;
            for (i = 0; i < 10; i = i + 1) {
                y = y + 1;
                if (y > 3) {
                    y = 0;
                    break;
                } 
            }
            return y;
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(y),BinaryOp(+,Id(y),IntLiteral(1))),If(BinaryOp(>,Id(y),IntLiteral(3)),Block([BinaryOp(=,Id(y),IntLiteral(0)),Break()]))]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_random_funccall(self):
        input = """int[] ntt(int n[], int t[]){
            return n[t]+t[n];
        }
        int main(){
            int n[4], t[4];
            if (ntt(n[3],t[0]) != 0) return ntt(n[3],t[3]);
            return n[1];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(n),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_random_expression(self):
        input = """int main(){
            boolean a,b,c;
            int d;
            a = b && c || d;
            return d;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(&&,Id(b),Id(c)),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_random_recursion(self):
        input = """
        int foo(int a){
            return a + foo(--a);
        }
        int main(){
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_random_recursion_false(self):
        input = """int ntt(int n, int t){
            return n+t;
        }
        int main(){
            if (ntt(3,0) != 0) return ntt(3,3);
            return ntt(3);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(ntt),[IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_random_return_false(self):
        input = """int main(int args){
            int x,y,z[3];
            for(i=5;i>0;--i) x=y;
            return args;
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_random_ifstmt_false(self):
        input = """void main(){
            int a;
            if (a == 5) a = a + 1.0;
            else a = a + 0.2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_forstmt_ifstmt(self):
        input = """int main(){
            int i, j, a[5];
            for (i = 10; i > 0; --i) 
                for (j = 0; j < i; j = j + 1) 
                    a[i] = j; 
            a[0] = 0;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_breakstmt_forstmt(self):
        input = """void main(){
            int i;
            i = 0;
            string s;
            s = "";
            for (i;i < 10;i = i + 1) 
                if (i == 5) break; 
                else s = s + "t";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(s),StringLiteral(t))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_returnstmt_forstmt_ifstmt(self):
        input = """int main(){
            int y, i;
            y = 0;
            for (i = 0; i < 10; i = i + 1) {
                y = y + 1;
                if (y < 3) return y; 
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,499))