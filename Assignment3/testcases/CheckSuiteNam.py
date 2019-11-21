import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """int foo(){return 0;}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point_more(self):
        input = """int Main(int main){return 1710195;}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_simple_program_no_entry_point(self):
        input = """int test;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_function_main(self):
        input = """int main(){return 0;}
        void main(int a){}"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_function_foo(self):
        input = """int main(){
            int MSSV;
            MSSV = 1710195;
            if(MSSV == 1710195){
                return MSSV;
            }
            return 1;
        }
        void foo(){}
        float foo(int a){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_params_func(self):
        input = """
        int s;
        void d(int c){}
        int t;
        int main(int t, float t[]){
            float a;
            a = 1;
            s = 2;
            f = 2;
            d(2);
            //g();
            return 0;
        }
        int f;"""
        expect = "Redeclared Parameter: t"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_params_func_2(self):
        input = """
        int s;
        void main(){
            return;
        } 
        boolean True(int s, int s){return true;}"""
        expect = "Redeclared Parameter: s"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable_block(self):
        input = """
        int test;
        float main(int test){
            boolean test;
            test = true;
            return 0.0005;
        }"""
        expect = "Redeclared Variable: test"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_variable_block_2(self):
        input = """
        boolean main(int arg){
            return true;
        }
        int Main(int arg){
            int True;
            boolean True;
            True = 2;
            return 0;
        }"""
        expect = "Redeclared Variable: True"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_variable_string(self):
        input = """ 
        void main(){}
        void Main(string k){
            int k[6];
            return;
        }"""
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_variable_block_if(self):
        input = """ 
        int main(){
            int a;
            a = 5;
            boolean b;
            b = true;
            if(b){
                float a;
                int a;
            }
            return -1;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_variable_block_elif(self):
        input = """
        void main(){
            int a;
            a = 5;
            boolean b;
            b = true;
            if(b){
                a = 1;
            }
            else{
                float b;
                int b;
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_variable_block_for_expr(self):
        input = """
        float main(int min, int max){
            float f;
            for (min; min < 5; max = max + 1){
                float f;
                f = 6.6;
                int g;
                boolean g;
                break;
            }
            return f;
        }
        """
        expect = "Redeclared Variable: g"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared_variable_block_for_if(self):
        input = """
        string str;
        int a;
        string main(int c){
            int b;
            b = 666666666;
            a = 0;
            int l;
            for(a = 5; a == 0; a = a - 1){
                if(a == 0){
                    float f;
                }
                if(a != 0){
                    string b;
                    float b;
                }
            }
            return str;
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclared_variable_for_for(self):
        input = """
        string str;
        int a;
        string main(int c){
            int b;
            for(a = 5; a == 0; a = a - 1){
                if(a == 0){
                    float f;
                }
                if(a != 0){
                    boolean b;
                }
                for(b = 1; b == 5; b = 1 + 1){
                    int f; 
                    float b;
                    string c;
                    string c;
                }
            }
            return str;
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_redeclared_variable_if_for(self):
        input = """
        void main(int arg[]){
            if(true){
                int a;
                a = 1;
            }
            else{
                int i;
                for (i = 0; i < 100; i = i + 1){
                    int j;
                    float j;
                    j = 1.5;
                }
                return;
            }
        }
        """
        expect = "Redeclared Variable: j"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_redeclared_variable_block_if_if(self):
        input = """void main(int arg[]){
            if(true){
                int a;
                a = 1;
                if(a == 1){
                    arg[2] = a;
                }
                string a;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclare_function_foo(self):
        input = """
        int main(int a, int b, int c){
            foo();
            return 0;
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclare_function_test(self):
        input = """
        void foo(int a){ a = a + 1; test();}
        int main(int a, int b, int c){
            foo(a);
            return 0;
        }"""
        expect = "Undeclared Function: test"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclare_function_sum(self):
        input = """
        int mul(int l, int r){
            int res;
            res = l*r;
            return res;
        }
        void main(int arg[]){
            int res;
            int a, b, c;
            res = a*b + b*c + c*b + mul(c,a);
            res = res + sum(res);
            return;
        }
        """
        expect = "Undeclared Function: sum"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclare_function_in_ifexp(self):
        input = """
        boolean main(int a){
            boolean b, c, d;
            if(bool(a, b, c, d)){
                return true;
            }
            return false;
        }"""
        expect = "Undeclared Function: bool"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_function_in_ifstmt(self):
        input = """
        int foo(int a){
            if (a > 0){
                return 1;
            }
            return foo(a + 1);
        }
        void main(){
            int res, test;
            test = -1000;
            res = foo(test);
            if(res > 0){
                Main();
                return;
            }
        }"""
        expect = "Undeclared Function: Main"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_function_in_doWhilestmt(self):
        input = """
        int main(){
            boolean main;
            main = true;
            if(main){
                do 
                    main = res();
                while main;
            }
            return 0;
        }
        """
        expect = "Undeclared Function: res"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_function_in_Forexp(self):
        input = """
        string str;
        int a;
        string main(int c){
            int b;
            for(a = 5; ok(a); a = a - 1){
                for(b = 1; b == 5; b = 1 + 1){
                    int f; 
                    float b;
                    string c;
                }
            }
            return str;
        }"""
        expect = "Undeclared Function: ok"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_function_in_Ifexp(self):
        input = """
        int main(int arg[], int b){
            if(undeclare(b)){
                return b;
            }
            return 0;
        }"""
        expect = "Undeclared Function: undeclare"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function_in_whileexp(self):
        input = """
        int main(int arg[], int b){
            do{
                return arg;
            }
            while foo(arg[1], b);
            return arg;
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_redeclared_variable_global(self):
        input = """int c;
        float c;
        int main(){return;}"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_variable_global(self):
        input = """int c;
        void main(){
            b = 5;
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_identifier_in_return(self):
        input = """
        string main(){
            d = 5;
            return c;
        }
        int d;"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_identifier_call(self):
        input = """
        int test;
        void main(){
            test = 0;
            foo(test);
            foo(a);
        }
        int foo(int test){return 0 + 1;}
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_identifier_return(self):
        input = """
        int test;
        void main(){
            foo(test);
            foo1();
        }
        void foo1(){
            return;
        }
        float foo(int a){
            test = 5;
            return b;
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_identifier_expIF(self):
        input = """
        int test;
        void main(){
            test = 0;
            foo(test);
        }
        int foo(int test){
            if(b == 0){
                test = test / 5;
            }
            return 0 + 1;
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undeclared_identifier_exp(self):
        input = """
        int main(){
            return a + 1;
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_identifier_exp2(self):
        input = """
        int main(){
            int a, b, c, d;
            a = b + 5 / d * 5 - e;
            return 0;
        }
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMismatchInStatement_if_exp(self):
        input = """
        void main(int arg[], int c){
            string name;
            name  = "Nguyen Dang Ha Nam";
            putString(name);
            int len;
            len = 10;
            if(putInt(len)){
                return;
            }
        }"""
        expect = "Type Mismatch In Statement: If(CallExpr(Id(putInt),[Id(len)]),Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_TypeMismatchInStatement_for_exp1(self):
        input = """
        void main(int arg[], int c){
            string name;
            name  = "Nguyen Dang Ha Nam";
            putString(name);
            int len;
            len = 10;
            if(len > 0){
                return;
            }
            for (name = "Nam"; len != 10; len = len - 1){
                return;
            }
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(name),StringLiteral(Nam));BinaryOp(!=,Id(len),IntLiteral(10));BinaryOp(=,Id(len),BinaryOp(-,Id(len),IntLiteral(1)));Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMismatchInStatement_for_exp2(self):
        input = """
        void foo(int arg[], float c){
            string name;
            name  = "Nguyen Dang Ha Nam";
            putString(name);
            int len;
            len = 10;
            if(len > 0){
                return;
            }
            for (arg[5] = 4; name = "Name"; len = len - 1){
                return;
            }
        }
        int a[5];
        int main(){
            foo(a, c);
            return -1;
        }
        float c;"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,ArrayCell(Id(arg),IntLiteral(5)),IntLiteral(4));BinaryOp(=,Id(name),StringLiteral(Name));BinaryOp(=,Id(len),BinaryOp(-,Id(len),IntLiteral(1)));Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_TypeMismatchInStatement_for_exp3(self):
        input = """
        
        int main(){
            foo(a, c);
            return -1;
        }
        void foo(int arg[], float c){
            string name;
            name  = "Nguyen Dang Ha Nam";
            int len;
            len = 0;
            for (arg[5] = 4; len != arg[5]; c = len - 1){
                return;
            }
        }
        int a[5];
        float c;
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,ArrayCell(Id(arg),IntLiteral(5)),IntLiteral(4));BinaryOp(!=,Id(len),ArrayCell(Id(arg),IntLiteral(5)));BinaryOp(=,Id(c),BinaryOp(-,Id(len),IntLiteral(1)));Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMismatchInStatement_while(self):
        input = """
        int c;
        int main(){
            float c;
            foo(a, c);
            return -1;
        }
        void foo(int arg[], float c){
            string name;
            name  = "Nguyen Dang Ha Nam";
            int len;
            len = 0;
            do{
                len = len + 1;
            }
            while 1;
        }
        int a[5];
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(len),BinaryOp(+,Id(len),IntLiteral(1)))])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_TypeMismatchInStatement_return_void(self):
        input = """
        void main(){
            return 1;
        }"""
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_TypeMismatchInStatement_return_int(self):
        input = """
        float Return(){return foo();}
        int foo(){return main();}
        int main(){return 1.2;}"""
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_TypeMismatchInStatement_return_float(self):
        input = """
        float Return(){return foo();}
        void foo(){return;}
        float main(){return 1.2;}"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_TypeMismatchInStatement_return_boolean(self):
        input = """
        boolean a;
        boolean c;
        boolean main(boolean b){
            int c;
            a = false;
            if(a != b){
                return c;
            }
            return true;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_TypeMismatchInStatement_return_string(self):
        input = """boolean a;
        boolean c;
        string main(boolean b){
            int c;
            a = false;
            if(a != b){
                return c;
            }
            string str;
            return str;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_redeclared_foo(self):
        input = """
        int foo;
            void foo(){return;} 
            void main() {
                return;
            }
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_TypeMismatchInStatement_return_void_2(self):
        input = """
        void R(int a){
            a = a + 1;
        }
        int param;
        void main(){
            param  = 1;
            R(param + 1);
            return param;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(param))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_TypeMismatchInStatement_return_array_poiter(self):
        input = """
        int[] main(){
            int a;
            return a;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_TypeMismatchInStatement_return_array_poiter_2(self):
        input = """
        int[] foo(){
            int a[10];
            a[1] = 2;
            return a;
        }
        int[] main(){
            boolean b;
            b = true;
            foo();
            return b;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_TypeMismatchInStatement_return_array_type(self):
        input = """
        int[] main(){
            boolean b;
            b = true;
            int param[5];
            foo(param[5]);
            return b;
        }
        int[] foo(int a[]){
            return a[3];
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(param),IntLiteral(5))])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_TypeMismatchInStatement_return_string_2(self):
        input = """
        string main(int a, float b){
            return b = a;
        }"""
        expect = "Type Mismatch In Statement: Return(BinaryOp(=,Id(b),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_TypeMismatchInStatement_return_void_3(self):
        input = """
        int foo(){return 0;}
        float main(){return 0;}
        void Main(){return foo();}"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_TypeMismatchInExpression_array_subcripting(self):
        input = """
        int main(){
            int a;
            float b;
            a = 1;
            b = 1.01;
            int a2[1];
            float b2[51];
            return 55.02;
        }"""
        expect = "Type Mismatch In Statement: Return(FloatLiteral(55.02))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_TypeMismatchInExpression_binary_more(self):
        input = """
        int main(){
            int a;
            a = 5;
            int b;
            b = 6;
            string c;
            c = "hello";
            a > b;
            c > a;
            return -1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_TypeMismatchInExpression_binary_modul(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            a >= b;
            a % c;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchInExpression_binary_equal(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            boolean bool;
            bool = a == b;
            bool = a == c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_typemismatch_block(self):
        input = """
        int main(){
            int d[5];
            d = 5;
        } """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TypeMismatchInExpression_binary_less(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "Nguyen Dang Ha Nam";
            boolean bool;
            bool = a <= b;
            bool = a <= c;
            bool = a >= s;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchInExpression_binary_add_add(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "1710195";
            a = a + b + b +a +a+ b+a;
            a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_TypeMismatchInExpression_binary_add_sub_mul_div(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "1710195";
            c = a + b*a/c + b -c*c+a +a+ b+a;
            b = a + b*a/c + b -c*c+a +a+ b+a;
            //a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(a)),Id(c))),Id(b)),BinaryOp(*,Id(c),Id(c))),Id(a)),Id(a)),Id(b)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_TypeMismatchInExpression_binary_operator(self):
        input = """
        float foo(int a, float b){
            return a + b;
        }
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "1710195";
            c = a + b*a/c + b -c*c+a +a+ b+a;
            c = a + b*a/c + b -c*c+a +a+ b+a - foo(a, c);
            c =  foo(b, c) % a;
            //a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,CallExpr(Id(foo),[Id(b),Id(c)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_unreach_function(self):
        input = """
        int a;
        void foo2(){}
        int main(){
            int a;
            foo();
            return 1;}
        int foo(){return a + 1;}"""
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_TypeMismatchInExpression_binary_not(self):
        input = """
        float foo(int a, float b){
            return a + b;
        }
        void main(){
            int a;
            a = 5;
            boolean bool;
            !bool;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            c =  foo(b, c) - c;
            !a;
            //a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_TypeMismatchInExpression_binary_and(self):
        input = """
        boolean and(boolean a, boolean b){
            return a && b;
        }

        boolean main(boolean a, boolean b){
            return and(a, b);
        }

        boolean andInt(int a, int b){
            andInt(a, b);
            return a && b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_TypeMismatchInExpression_binary_or(self):
        input = """
        boolean or(boolean a, boolean b){
            return a || b;
        }

        boolean main(boolean a, boolean b){
            return or(a, b);
        }

        boolean orInt(int c, int b){
            orInt(c, b);
            return c || b;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_TypeMismatchInExpression_binary_not_equal(self):
        input = """
        boolean notEqual(boolean a, boolean b){
            return a != b;
        }

        boolean notEqualInt(int a, int b, int c){
            return a != c || b != c;
        }

        boolean main(boolean a, boolean b){
            return notEqual(a, b);
        }

        boolean notEqualFloat(int d, int e, float f, float g){
            notEqualInt(d, e, e);
            notEqualFloat(d, e, f, g);
            return f != g;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(f),Id(g))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_TypeMismatchInExpression_binary_assign(self):
        input = """
        boolean notEqual(boolean a, boolean b){
            return a != b;
        }

        boolean notEqualInt(int a, int b, int c){
            return a != c || b != c;
        }

        boolean main(boolean a, boolean b){
            return notEqual(a, b);
        }

        boolean notEqualFloat(int d, int e, float f, float g){
            notEqualInt(d, e, e);
            notEqualFloat(d, e, f, g);
            string s1, s2;
            s1 = s2;
            d = e;
            f = d;
            boolean a, b;
            a = true;
            b = false;
            a = b;
            d =b;
            return e != e;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_TypeMismatchInExpression_binary_assign_2(self):
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "1710195";
            a = a + b + b +a +a+ b+a;
            s = s + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(s),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_TypeMismatchInExpression_binary_2(self):
        input = """
        void foo(){
            foo();
        }

        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "1710195";
            a = a + b + b +a +a+ b+a;
            int man;
            man = main();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(man),CallExpr(Id(main),[]))"
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_TypeMismatchInExpression_unary(self):
        input = """
        float main(){
            int a;
            a = 5;
            -foo();
            return -a;
        }
        boolean foo(){
            return true;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_TypeMismatchInExpression_unary_2(self):
        input = """
        float main(){
            int a;
            a = 5;
            -foo();
            return -main();
        }
        float foo(){
            return -13.5;
        }
        void wrong(){
            -wrong();
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,CallExpr(Id(wrong),[]))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_notleftvalue_int(self):
        input = """int main(){
            int LHS;
            1 = LHS;
            return 1;
        }"""
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_notleftvalue_void(self):
        input = """
        void foo(){
            return;
        }
        int main(){
            int LHS;
            LHS = 3;
            LHS + 1 = 5;
            return 1;
        }"""
        expect = "Not Left Value: BinaryOp(+,Id(LHS),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_complete_program(self):
        input = """void main(){
            foo1();
            int a;
            for(a = 1; a < 32; a = a + a){
                break;
                continue;
                if(a > 0){
                break;
            }
            }
            
            //continue;
        }

        void foo1(){
            putString("hello world");
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_break_not_in_loop(self):
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_continue_not_in_loop(self):
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_break_not_in_loop_2(self):
        input = """
         float main(int min, int max){
            float f;
            for (min; min < 5; max = max + 1){
                float f;
                f = 6.6;
                int g;
                break;
            }
            break;
            return f;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_break_not_in_loop_3(self):
        input = """
         float main(int min, int max){
            float f;
            for (min; min < 5; max = max + 1){
                float f;
                f = 6.6;
                int g;
                break;
                if(!(min == 66)){
                    break;
                }
            }
            continue;
            return f;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_continues_not_in_loop_2(self):
        input = """
         float main(int min, int max){
            float f;
            for (min; min < 5; max = max + 1){
                float f;
                f = 6.6;
                int g;
                continue;
            }
            continue;
            return f;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_Continue_not_in_loop_3(self):
        input = """
         float main(int min, int max){
            float f;
            for (min; min < 5; max = max + 1){
                float f;
                f = 6.6;
                int g;
                continue;
                if(!(min == 66)){
                    continue;
                }
            }
            break;
            return f;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_Break_Continue_not_in_loop(self):
        input = """
        void main(int a, int b, int c){
            do{
                a = a - 2;
                if (a == b){
                    break;
                }
            }while(c != b);

            do{
                a = a - 2;
                if(a == b){
                    if(a == c){
                        continue;
                    }
                }
                if(a==b){
                    if(a!=c){
                        break;
                    }
                }
            }
            while(a != b && !(a==c));
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_No_Entry_Point_2(self):
        input = """
        int foo;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_No_Entry_Point_3(self):
        input = """
        int ain;
        int main;
        void Main(){

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_No_Entry_Point_4(self):
        input = """
        void foo(){
            foo();
            foo2();
        }
        void foo2(){
            int main;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachable_function(self):
        input = """
        void main(){
            return;
        }
        string foo(){
            return "ndhnam";
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachable_function_2(self):
        input = """
        int foo3;
        void foo2(){
            foo();
        }

        void main(){
            return;
        }
        string foo(){
            foo3 = 5;
            foo();
            return "ndhnam";
        }

        """
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachable_function_3(self):
        input = """
        
        string hello(){
            return "?";
        }

        string main(){
            hello();
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_not_left_value(self):
        input = """
        void main(int a[]){
            int ab;
            ab = 5;
            5 = ab;
            return;
        }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_not_left_value_2(self):
        input = """
        void main(int g){
            int ma;
            float array[5];
            array[4] = 0;
            ma = array[4];
            
            ma = main;
            return;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(ma),ArrayCell(Id(array),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_not_left_value_3(self):
        input = """
        void main(int g){
            float array[5];
            array[4] = 0;
            4 > 5 = array[4];
            return;
        }
        """
        expect = "Not Left Value: BinaryOp(>,IntLiteral(4),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_not_left_value_4(self):
        input = """
        void main(int g){
            float array[5];
            array[4] = 0;
            4 > 5 + g = array[4];
            return;
        }
        """
        expect = "Not Left Value: BinaryOp(>,IntLiteral(4),BinaryOp(+,IntLiteral(5),Id(g)))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_typemismatch_array_pointer(self):
        input = """
        int[] getArr(int a[]){
            int b[10];
            if (b[0] < 10){
                return b;
            }
            else{
                return a;
            }
            return a;
        }
        void main(int b[]){
            int a[10];
            b = getArr(a);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(getArr),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_function_not_return_1(self):
        input = """
        int main(){
            foo();
            if(true){
                return 0;
            }
            else{
                return 0;
            }
        }

        int foo(){

        }

        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_function_not_return_2(self):
        input = """
        int main(){
            if(true){
                if (true){
                    return 0;
                }
                else{
                    return 0;
                }
            }
            else{
                return 0;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_typemismatch_float_div_float_ret_int(self):
        input = """
        int main(float a, float b){
            return b/a;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(b),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_typemismatch_int_div_float_ret_float(self):
        input = """
        float main(int a, float b){
            return b/a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_typemismatch_int_div_float_ret_int(self):
        input = """

        int foo(int a, float b){
            return a/b;
        }

        float main(int c, float d){
            return div(a, b);
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_function_not_return_ok(self):
        input = """
        float main(){
            if(true){
                if (true){
                    if (true){
                        return 0;
                    }
                    else{
                        return 0;
                    }
                }
                else{
                    return 0;
                }
            }
            else{
                if (true){
                    return 0;
                }
                else{
                    if (true){
                        return 0;
                    }
                    else{
                        return 0;
                    }
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_function_not_return_failer(self):
        input = """
        float main(){
            if(true){
                if (true){
                    if (true){
                        return 0;
                    }
                    else{
                        int a;
                        float b;
                        string c;
                        boolean d;
                        int e[5];
                        a = 5;
                        b = 5.1;
                        c = "Nam";
                        d = true;
                    }
                }
                else{
                    return 0;
                }
            }
            else{
                if (true){
                    return 0;
                }
                else{
                    if (true){
                        return 0;
                    }
                    else{
                        return 0;
                    }
                }
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_redeclared_(self):
        input = """
        float main(){
            if(true){
                if (true){
                    if (true){
                        return 0;
                    }
                }
                else{
                    return 0;
                }
            }
            else{
                if (true){
                    return 0;
                }
                else{
                    if (true){
                        return 0;
                    }
                    else{
                        return 0;
                    }
                }
            }
            return -1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_completed_program(self):
        input = """
        void Nguyen(){
        }

        string Dang(){
            return "Dang";
        }

        boolean Ha(){
            return true;
        }

        int Nam(){
            return 1;
        }

        float MSSV(){
            return 1710195;
        }

        int main(){
            Nguyen();
            Dang();
            Ha();
            Nam();
            MSSV();
            return Nam();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))

   