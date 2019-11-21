import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
                                    #CONTENTS
                                    #TEST_REDECLARED-----------(15)
                                    #TEST_UNDECLARED-----------(10)
                                    #TEST_TYPEMISMATCHSTMT-----(15)
                                    #TEST_TYPEMISMATCHEXP------(20)
                                    #TEST_FUNCTIONNOTRETURN----(10)
                                    #TEST_BRKCONTNOTINLOOP-----(05)
                                    #TEST_NOENTRYPOINT---------(05)
                                    #TEST_UNREACHABLEFUNC------(07)
                                    #TEST_NOTLEFTVALUE---------(05)
                                    #TEST_COMBINE--------------(08)
                                    #------------------------------
                                    #TOTAL--------------------(100)

#TEST_REDECLARED-----------------------------------------------------------------------------------(15)

    def test_redeclared_global_variable(self):
        input = """
        int a, b;
        int a;
        void main() {}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_main_local_variable(self):
        input = """
        int a, b;
        void main() {
            int a, b, c;
            int c;
        }"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_function_name(self):
        input = """
        void a() {}
        void a() {}
        void main() {
            a();
        }"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_function_variable_name(self):
        input = """
        boolean x, a;
        void a() {}
        void main() {}"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_block_variable_name(self):
        input = """
        string s;
        void main() {
            int s, t;
            {
                boolean t, u;
                float u;
            }
        }"""
        expect = "Redeclared Variable: u"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_param_name(self):
        input = """
        void foo(int a, int b, int a) {}
        void main() {}"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_var_in_func(self):
        input = """
        float test;
        void __test(int test, int fail) {int fail;}
        void main() {}"""
        expect = "Redeclared Variable: fail"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_block_in_func(self):
        input = """
        void a(int a, int b) {
            int c;
            {
                float a, b, c, d;
                int d;
            }
        }
        int main() {}"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_func(self):
        input = """
        int __init, __str;
        void foo(int __init) {}
        void __str() {}
        void main() {}"""
        expect = "Redeclared Function: __str"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_complex_block(self):
        input = """
        string x, y, z;
        void _x(int x) {
            float _x, y;
            int z;
            {
                int x;
                {
                    int x;
                    {
                        int x;
                    }
                }
            }
            boolean z;
        }
        void main() {}"""
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_param_two_function(self):
        input = """
        void foo(boolean _a, string _b) {}
        void goo(int z, boolean _a, string _b, int z) {}
        void main() {
            foo();
            goo();
        }"""
        expect = "Redeclared Parameter: z"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_arrvar_in_main_func(self):
        input = """
        int a[5], b, c;
        void main() {
            int a, main[10], fail;
            int fail[5];
        }
        string d;"""
        expect = "Redeclared Variable: fail"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_var_after_main_func(self):
        input = """
        int a, b, c;
        float d;
        void main() {
            int a, b, c;
        }
        string d;"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared_func_with_many_var(self):
        input = """
        int a;
        void foo(int a){}
        boolean b;
        void goo(int b){}
        string c;
        float d[3];
        void main() {
            int a, b, c;
            foo(a);
            goo(b);
            a();
        }
        float[] a() {return d;}"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclared_successful_all_scope(self):
        input = """
        int a[5], b[2], c;
        void func(int a, int b) {}
        float d;
        void main() {
            string a[2], b, c[2];
            {
                boolean a, b[2];
                {
                    string a, b, c;
                }
                int c;
            }
            int main;
            func(main, main);
            notFail();
        }
        string success;
        void notFail() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))

#TEST_UNDECLARED-----------------------------------------------------------------------------------(10)

    def test_undeclared_identifier_in_main_simple(self):
        input = """
        int a, b[2], c;
        void main() {
            d;
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_function_in_main_simple(self):
        input = """
        string str, happy;
        void main() {
            int a[5], b, c;
            PPL();
        }"""
        expect = "Undeclared Function: PPL"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_undeclared_id_param_main_simple(self):
        input = """
        int a, b[2], c;
        void foo(int a) {}
        void main() {
            foo(b[0]);
            foo(d);
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_identifier_in_exp(self):
        input = """
        float a;
        int func() {return 1;}
        void main() {
            int a;
            c = 3;
            a = func() + c;
            a + d;
        }
        int c;"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_func_in_exp(self):
        input = """
        int a;
        float b[2];
        void main() {
            foo() + goo();
            notFound(a);
        }
        int foo() {
            return 1;
        }
        float goo() {
            return 2.5;
        }"""
        expect = "Undeclared Function: notFound"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_param_in_callexp(self):
        input = """
        int test(int a, int b) {
            return a + b;
        }
        void main() {
            int a[1], b;
            test(a[0], b);
            test(b, fail);
        }"""
        expect = "Undeclared Identifier: fail"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_identifier_in_func(self):
        input = """
        string sherlock() {
            string ret;
            sher = "sher";
            ret = sher + lock;
            return ret;
        }
        void main() {
            sherlock();
        }
        string sher;"""
        expect = "Undeclared Identifier: lock"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_func_in_func(self):
        input = """
        int plus(int a, int b) {
            return a + b;
        }
        void main() {
            int a, b;
            a = b = 9;
            plus(mul(a, b), div(a, b));
        }
        int mul(int a, int b) {
            return a * b;
        }"""
        expect = "Undeclared Function: div"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_arrcell_index(self):
        input = """
        void main() {
            int index;
            index = 5;
            a[index] + a[9] + a[b];
        }
        int a[10];"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_no_error(self):
        input = """
        float arr[10];
        void main() {
            int a, b, c;
            a = b = c = 100;
            arr[1] = func(a); 
            d = func(b);
            test(c);
        }
        float func(int a) {
            return a * 0.2 - 3;
        }
        float d;
        int test(int a) {
            return a + 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,424))

#TEST_TYPEMISMATCHSTMT-----------------------------------------------------------------------------------(15)

    def test_typemismatchstmt_if_condition(self):
        input = """
        boolean a;
        void main() {
            a = true;
            int a;
            a = 5;
            if (a) {}
        }"""
        expect = "Type Mismatch In Statement: If(Id(a),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_typemismatchstmt_for_expr_no2(self):
        input = """
        void main() {
            putString("LOADING...");
            int i;
            for (i = 0; i = i; i = i + 1) {
                putString("Hello My Luv!");
            }
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),Id(i));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(putString),[StringLiteral(Hello My Luv!)])]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_typemismatchstmt_for_expr_no13(self):
        input = """
        void main() {
            for ("Edogawa"; true; "Conan") {}
        }"""
        expect = "Type Mismatch In Statement: For(StringLiteral(Edogawa);BooleanLiteral(true);StringLiteral(Conan);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_typemismatchstmt_dowhile_condition(self):
        input = """
        void main() {
            do {} while (1);
        }"""
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_typemismatchstmt_return_voidfunc(self):
        input = """
        void foo() {}
        void goo() {
            return;
        }
        void main() {
            foo();
            goo();
            return 0;
        }"""
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_typemismatchstmt_return_floatfunc_coerced_successful(self):
        input = """
        int a;
        float main() {
            float a;
            a = func();
            return a;
        }
        float func() {
            a = 9;
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_typemismatchstmt_return_arrfunc(self):
        input = """
        boolean[] __akiteIru(int a[]) {
            boolean d[5];
            d[1] = true;
            return d;
        }
        int[] main() {
            int a[5];
            return __akiteIru(a);
        }"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(__akiteIru),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_typemismatchstmt_return_stringfunc(self):
        input = """
        string amIStupid(string name) {
            putString("You are so stupid!");
            return "idiot";
        }
        string main() {
            amIStupid("Me");
            return;
        }"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_typemismatchstmt_stmt_combine1(self):
        input = """
        void main() {
            int a, i;
            a = 4;
            if (a > 3) {
                do {
                    a = a / 2;
                } while (a > 3);
            }
            else if (a > 0) {
                for (i = 0; i < 50; i = i + 1) {
                    putIntLn(i * i);
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_typemismatchstmt_stmt_combine2(self):
        input = """
        int func(int a) {
            if (a > 3) return a * 2;
            return a / 2;
        }
        void main() {
            int a[3];
            a[0] = func(3);
            a[1] = func(7);
            for (i = 0; i < 77; i = i * 2) {
                if (true) {
                    a[2] = i;
                }
            }
        }
        int i;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_typemismatchstmt_returnstmtcombine1(self):
        input = """
        int plus(int a, int b) {
            return a + b;
        }
        int minus(float a, float b) {
            return a - b;
        }
        void main() {
            plus(a[0], a[1]) * minus(a[0], a[1]);
        }"""
        expect = "Type Mismatch In Statement: Return(BinaryOp(-,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_typemismatchstmt_returnstmtcombine2(self):
        input = """
        string s;
        void main() {
            s = "Kanashimi";
            s = delete(s);
            return s;
        }
        string delete(string str) {
            return "";
        }"""
        expect = "Type Mismatch In Statement: Return(Id(s))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_typemismatchstmt_dowhile_with_many_block(self):
        input = """
        void main() {
            float i;
            i = 1e-3;
            do {}
            {
                if (true) {
                        boolean flag[2];
                        flag[1] = true;
                    i = i * 10.8;
                    putFloatLn(i);
                }
            }
            do {} while 1; while true;
        }"""
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_typemismatchstmt_no_error1(self):
        input = """
        int plus(int a, int b) {
            return a + b;
        }
        float minus(float a, float b) {
            return a - b;
        }
        float main() {
            int a[2];
            a[0] = 6;
            a[1] = 7;
            return plus(a[0], a[1]) * minus(a[0], a[1]);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_typemismatchstmt_no_error2(self):
        input = """
        void print(int n) {
            int i;
            for (i = 0; i < n; i = i + 1) {
                if (i * i < 10e4) putFloat(i * i);
                else return;
            }
            return;
        }
        void main() {
            print(7);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))

#TEST_TYPEMISMATCHEXP------------------------------------------------------------------------------------(20)

    def test_typemismatchexp_arrcell_not_an_arr(self):
        input = """
        int a;
        void main() {
            a = 3;
            a[3];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_typemismatchexp_index_not_an_integer(self):
        input = """
        int main() {
            int c;
            c = 0;
            float b, a[4];
            b = 9e-3;
            a[c];
            a[b];
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_typemismatchexp_add_on_string(self):
        input = """
        void main() {
            string C, M, theBest;
            C = "Conan";
            M = "Mai-K";
            theBest = C + M;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(C),Id(M))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_typemismatchexp_arrcell_exp_with_int(self):
        input = """
        int main() {
            int a, b, c[3];
            a = b = 5;
            if (a > 3) {
                c[0] = -(a * b / 3); 
            }
            else if (a == 3) c[1] = a % b;
            else if (a != 1) c[2] = a = b + 3 - a;
            else putInt(-a);
            a && b;
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_typemismatchexp_arrcell_exp_with_boolean(self):
        input = """
        void main() {
            boolean a, b, flag[3];
            a = b = true;
            if (!!a) flag[0] = a || b && (a != b);
            else if (a == b) {
                flag[1] = flag[2] = !(3 > 4);
            }
            else putBoolLn(a);
            -(a || b);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(||,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_typemismatchexp_exp_with_float(self):
        input = """
        void main() {
            float a, b, f[2];
            a = 1e-3;
            b = 2e-6 * 1000 / 1.2;
            if ((a >= b) && (a + 2*b < 1e6)) {
                f[0] = -(-a * -b) + 3;
            }
            else f[1] = a / -b - 3.5 * (b + 2);
            if (f[0] != f[1]) {}
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,ArrayCell(Id(f),IntLiteral(0)),ArrayCell(Id(f),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_typemismatchexp_exp_with_string(self):
        input = """
        string str;
        int main(float a) {
            str = "Are u happy?";
            putString(str);
            string s;
            s = str = "Yup!!!";
            putString(s);
            if (s == str) {}
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(s),Id(str))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_typemismatchexp_exp_with_array(self):
        input = """
        float[] nothing() {
            a[0] = 1;
            a[1] = -2.5e3;
            a[2] = 5E1;
            return a;
        }
        int main(float a) {
            putFloat(nothing()[1]);
            int arr;
            arr = nothing();
            return 0;
        }
        float a[3];
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),CallExpr(Id(nothing),[]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_typemismatchexp_exp_error_float_to_int(self):
        input = """
        int main() {
            float a;
            int i;
            a = i = -(-3 * 4 - 7);
            i = a;
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_typemismatchexp_error_boolean_to_int(self):
        input = """
        void main() {
            boolean a;
            a = true;
            int i;
            i = - 9;
            i = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_typemismatchexp_assign_value_to_arr(self):
        input = """
        boolean a[4];
        void main() {
            a[1] = true;
            a[2] = false || (4 > 3.5);
            a = a[1] && a[2];
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(&&,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(a),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_typemismatchexp_callexp_builtin_diff_numofparam(self):
        input = """
        void main() {
            int str;
            str = getInt();
            putIntLn();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_typemismatchexp_callexp_userdef_diff_numofparam(self):
        input = """
        void main() {
            int a;
            a = 100;
            def(a, a);
            def(a);
        }
        void def(int a, int b) {
            putInt(a);
            putIntLn(b);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(def),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_typemismatchexp_nested_callexp_diff_numofparam(self):
        input = """
        void main() {
            putIntLn(getInt(4));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_typemismatchexp_callexp_wrong_paramtype(self):
        input = """
        boolean a;
        void main() {
            int a;
            a = getInt();
            putInt(a);
            putBool(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putBool),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_typemismatchexp_usedefin_callexp_wrong_paramtype(self):
        input = """
        int func1(int a[]) {
            return a[0] + a[1];
        }
        void main() {
            int main[2], a;
            a = 3;
            func1(main);
            func2(a);
        }
        int func2(int a[]) {
            return a[0] * a[1];
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func2),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_typemismatchexp_combine_exp(self):
        input = """
        int a[5];
        float b;
        boolean c;
        string str[5];
        string[] __str(boolean f[]) {return str;}
        void main() {
            string str;
            boolean flag[2];
            {
                int i, c;
                c = 5;
                for (i = 0; i < c; i = i + 1) {
                    a[i] = i * 2;
                    putIntLn(a[i]);
                } 
            }
            c = true;
            putBool(c);
            {
                b = a[2] + a[1];
            }
            str = "Shinjitsu wa Itsumo Hitotsu";
            putString(str);
            int a[5];
            __str(flag);                            //Okay
            __str(a);                               //Fail
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(__str),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_typemismatchexp_complex_exp(self):
        input = """
        float[] func(float a[], int n) {
            int i;
            for (i = 0; i < n; i = i + 1) {
                int j;
                j = getInt();
                a[i] = j * a[i];
                putFloat(a[i]);
            }
            return a;
        }
        void main() {
            int num;
            num = getInt();
            float arr[2];
            arr[0] = arr[1] = -----5;
            arr[0] = func(arr, num)[0];
            arr = func(arr, num);
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),CallExpr(Id(func),[Id(arr),Id(num)]))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_typemismatchexp_not_error(self):
        input = """
        int main() {
            num = getInt();
            int a[3], ind;
            float b[2];
            ind = getInt();
            float result;
            result = -(getFloat() + 5) * b[ind] / a[num];
            b[0] = b[1] = a[1] + a[2] * num % 4;
            return 0; 
        }
        int num;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_typemismatchexp_more_complex_not_error(self):
        input = """
        int a[2];
        void main() {
            a[0] = a[1] = 3;
            float val;
            boolean b;
            b = (7.7 > 7) || (double(a)[1] - 1 >= 5);
            if (b) {
                val = (double(a)[1] * 7) % double(a)[0];
                putFloat(val);
            }
            else putBoolLn(b);
        }
        int[] double(int arr[]) {
            arr[0] = arr[0] * 2;
            arr[1] = arr[1] * 2;
            putFloatLn(arr[0] + arr[1]);
            return arr;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,459))

#TEST_FUNCTIONNOTRETURN------------------------------------------------------------------------------------(10)

    def test_funcnotreturn_int_main_notret(self):
        input = """
        int main() {
            putFloat(1.5);
            putString("Hello World!");
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_funcnotreturn_userdef_func_notret(self):
        input = """
        int main() {
            func(1, 2, 3);
            return 0;
        }
        float func(float a, float b, float c) {
            float sum;
            sum = a + b + c;
            putFloatLn(sum);
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_funcnotreturn_return_in_one_branch(self):
        input = """
        int testIQ(int IQ) {
            if (IQ > 150) {
                putString("Woww");
                return IQ;
            }
            else
                putString("Meh");
        }
        void main() {
            testIQ(100);
            return;
        }"""
        expect = "Function testIQ Not Return "
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_funcnotreturn_return_in_nestedblock(self):
        input = """
        int main() {
            {
                {
                    {
                        return 0; //Are u okay?
                    }
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_funcnotreturn_return_in_dowhile(self):
        input = """
        int main() {
            int a;
            do {
                a = getInt();
            }
            putInt(a + 1);
            a = a * 2;
            putIntLn(a + 1);
            a = a * a;
            {
                putFloatLn(a + 7);
                {
                    return 0;
                }
            } while true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_funcnotreturn_ifstmt_return_two_branch(self):
        input = """
        int main() {
            float a;
            a = getFloat();
            {
                if (a > 5) {
                    {
                        return 0;
                    }
                }
                else {
                    return 1;
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_funcnotreturn_return_in_for(self):
        input = """
        int main() {
            do {
                int i;
                for (i = 55; i <= 180; i = i + 5) {
                    putBoolLn(JLPT(i));
                    return 0;
                }
            } while true;
        }
        boolean JLPT(int point) {
            if (point >= 90) return true;
            else return false;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_funcnotreturn_void_func(self):
        input = """
        void foo() {goo();}
        int main() {
            goo();
            return 0;
        }
        void goo() {foo();}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_funcnotreturn_void_func_with_return(self):
        input = """
        void notReturnStmt() {
            if (7.5 < 1e2) {
                putString("(y)");
            }
        }
        int main() {
            returnStmt();
            return 0;
        }
        void returnStmt() {
            notReturnStmt();
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_funcnotreturn_combine_return_func(self):
        input = """
        int f1() {
            if (true) return 9;
            else return 10; 
        }
        float f2() {
            if (true) return f1();
            return 200;
        }
        int main() {
            a[0] = a[1] = 5;
            int temp;
            temp = arr(a)[0];
            putString(g2());
            return 0;
        }
        int a[2];
        int[] arr(int a[]) {
            f2();
            return a;
        }
        boolean g1() {
            return 2 * 3 < 18 * 9;
        }
        string g2() {
            if (g1()) return "Yes";
            do return "No";
            while !g1();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

#TEST_BRKCONTNOTINLOOP-----------------------------------------------------------------------------------(05)

    def test_brkcontnotinloop_brk_not_in_loop(self):
        input = """
        void main() {
            break;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_brkcontnotinloop_cont_not_in_loop(self):
        input = """
        void main() {
            {
                {
                    continue;
                }
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_brkcontnotinloop_brk_in_ifstmt(self):
        input = """
        void main() {
            int a;
            a = 5 * -6;
            if (a < -29) {
                break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_brkcontnotinloop_if_in_nested_forloop(self):
        input = """
        void main() {
            int i;
            for (i = 0; i < 100; i = i + 2) {
                int a;
                a = 5;
                if (i * i > 1e3) {
                    break;
                }
                if (i * i < 5e2) {
                    continue;
                }
                for (a = 0; a < 12; a = a + 1) {
                    do {} while true;
                    continue;
                }
                break;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_brkcontnotinloop_brk_continue_in_dowhile(self):
        input = """
        void main() {
            do {
                if (!true) break;
            }
            if (false) continue;
            {
                {{{break;}}}
            }
            while true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,474))

#TEST_NOENTRYPOINT--------------------------------------------------------------------------------------(05)

    def test_noentrypoint_all_vardecl(self):
        input = """
        int a, b, c, d[100];
        float e, f, g[50];
        boolean flag;
        string str;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_noentrypoint_all_funcdecl(self):
        input = """
        void func1() {__func2();}
        void __func2() {mainfunc();}
        void mainfunc() {__main();}
        void __main() {func1();}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_noentrypoint_main_variable(self):
        input = """
        int a, b, c;
        boolean main;
        string str;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_noentrypoint_func_vardecl_not_include_main_func(self):
        input = """
        int a[10], m[100];
        float _main(int a) {
            __main(2);
            return a * 2;
        }
        float main;
        boolean __main(int a) {
            _main(2);
            return a == 100;
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_noentrypoint_no_err(self):
        input = """
        int a, b, c;
        float __main;
        int main(string argv) {
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,479))

#TEST_UNREACHABLEFUNC--------------------------------------------------------------------------------------(07)

    def test_unreachablefunc_foo(self):
        input = """
        int foo(int a) {
            return a*2;
        }
        int main() {
            return 0;
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_unreachablefunc_goo_after_mainfunc(self):
        input = """
        void foo() {}
        int main() {
            foo();
            return 0;
        }
        void goo() {foo();}"""
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_unreachablefunc_recursivefunc(self):
        input = """
        void foo() {foo();}
        int main() {
            goo();
            return 0;
        }
        void goo() {}"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachablefunc_goo_not_invoke(self):
        input = """
        int main() {
            foo();
            return 0;
        }
        void foo() {hoo(100);}
        void goo() {foo();}
        int hoo(int a) {
            return a % 2;
        }"""
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachablefunc_noneed_invoke_main(self):
        input = """
        int a, b;
        int main() {
            a = b = 3;
            foo(b);
            return 0;
        }
        void foo(int a) {putIntLn(a);}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachablefunc_no_err(self):
        input = """
        int a;
        int foo() {
            a = hoo();
            return a;
        }
        float goo() {
            a = foo();
            return a * 8;
        }
        void main() {
            goo();
            return;
        }
        int hoo() {
            goo();
            return 100;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_unreachablefunc_main_is_invoked(self):
        input = """
        int foo() {
            if (true) return main();
            return 3;
        }
        int main() {
            int a;
            a = foo();
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))

#TEST_NOTLEFTVALUE--------------------------------------------------------------------------------------(05)
    
    def test_notleftvalue_assign_to_literal(self):
        input = """
        int main() {
            int a;
            7 = a = 8;
            return 0;
        }
        void goo() {foo();}"""
        expect = "Not Left Value: IntLiteral(7)"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_test_notleftvalue_assign_to_callexpr(self):
        input = """
        int foo() {return 0;}
        int main() {
            foo() = 22/12/1999;
            return 0;
        }"""
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_notleftvalue_assign_to_biexpr(self):
        input = """
        boolean b[5];
        int main() {
            b[2] = ret(b)[0];
            true && (3 > 4) = b[2];
            return 0;
        }
        boolean[] ret(boolean b[]) {
            b[0] = true;
            return b;
        }"""
        expect = "Not Left Value: BinaryOp(&&,BooleanLiteral(true),BinaryOp(>,IntLiteral(3),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_notleftvalue_assign_to_unexpr(self):
        input = """
        int main() {
            n = getInt();
            a = -b = -(5 - 6 * n);
            return 0;
        }
        int a, b, n;"""
        expect = "Not Left Value: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_notleftvalue_no_err(self):
        input = """
        int[] func() {
            return a;
        }
        int main() {
            int a[5];
            a[2] = 9;
            a[4] = 12;
            float b;
            a[1] = a[2] * a[4];
            b = a[1] * 9.5;
            a[3] = a[4] = -(9 * 8 + 5) * 5;
            func()[2] = 1;
            return a[2] % a[3];
        }
        int a[3];"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))

#TEST_COMBINE--------------------------------------------------------------------------------------------(08)

    def test_combine_complex_scope(self):
        input = """
        int i;
        int f() {
            return 200;
        }
        void main(){
            int main;
            main = f();
            putIntLn(main);
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
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_combine_enter_and_print_arr(self):
        input = """
        /*Enter and print an array of integers*/
		int main() {
			enter(a, 10);
			print(a, 10);
			return 0;
		}
        int a[10], b;
		void enter(int a[], int n) {
			int i, j[2];
			for (i = 0; i < n; i = i + 1) {
				putString("Enter an integer: ");
            	a[i] = getInt();
			}
		}
        void print(int a[], int n) {
			int i;
			for (i = 0; i < n; i = i + 1) putIntLn(a[i]);
		}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_combine_find_largest_element(self):
        input = """
        int main()
		{
    		int i, n;
    		float arr[100];
    		putString("Enter total number of elements(1 to 100): ");
    		n = getInt();
    		putString("\\n");
    		//Stores number entered by the user
    		for (i = 0; i < n; i = i + 1)
    		{
       			putString("Enter Number: ");
       			arr[i] = getInt();
    		}
    		//Loop to store largest number to arr[0]
    		for (i = 1; i < n; i = i + 1)
    		{
       			if (arr[0] < arr[i])					//Change < to > if you want to find the smallest element
           			arr[0] = arr[i];
    		}
    		putString("Largest element = ");
            putFloatLn(arr[0]);
    		return 0;
		}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_combine_convert_binary_to_octal(self):
        input = """
        /*Function convert binary to Octal */
		int convertBinarytoOctal(int binaryNumber)
		{
    		int octalNumber, decimalNumber, i;
			octalNumber = decimalNumber = i = 0;
			do {
        		decimalNumber = decimalNumber + (binaryNumber%10) * pow(2,i);
        		i = i + 1;
        		binaryNumber = binaryNumber / 10;
    		}
    		while (binaryNumber != 0);
    		i = 1;
			do {
        		octalNumber = octalNumber + (decimalNumber % 8) * i;
        		decimalNumber = decimalNumber / 8;
        		i = i * 10;
    		}
    		while (decimalNumber != 0);
    
    		return octalNumber;
		}
        void main() {
            putIntLn(convertBinarytoOctal(100000000111110));
            return;
        }
        int pow(int a, int b) {
            int i, result;
            result = 1;
            for (i = 0; i < b; i = i + 1)
                result = result*a;
            return result;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_combine_check_year(self):
        input = """
        int main()
		{
    		int year;
    		putString("Enter a year: ");
    		year = getInt();
    		if (year % 4 == 0)
    		{
        		if (year % 100 == 0)
        		{
            	//Year is divisible by 400, hence the year is a leap year
            	if (year % 400 == 0)
                	putString("Leap year.");
            	else
                	putString("Not leap year.");
        		}
        		else
            		putString("Leap year.");
    		}
    		else
        		putString("Not leap year.");
    
    		return 0;
		}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))


    def test_combine_check_palindrome(self):
        input = """
        int main()
		{
    		int n, reversedInteger, remainder, originalInteger;
			reversedInteger = 0;
    		putString("Enter an integer: ");
    		n = getInt();
    		originalInteger = n;
    		//reversed integer is stored in variable 
			do
        		remainder = n%10;
        		reversedInteger = reversedInteger*10 + remainder;
        		n = n / 10;
    		while (n != 0);
    		
    		//palindrome if orignalInteger and reversedInteger are equal
    		if (originalInteger == reversedInteger)
        		putString("Is a palindrome.");
    		else
        		putString("Is not a palindrome.");
    
    		return 0;
		}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_combine_check_prime_number(self):
        input = """
        //Check if a number is prime number

		boolean isPrime(int n)
        {
            boolean flag;
            flag = true;
            int j;
            for (j = 2; j <= n/2; j = j + 1)
            {
                if (n % j == 0)
                {
                    flag = false;
                    break;
                }
            }
            return flag;
        }

		int main() {
			int n;
			n = getInt();
			if (isPrime(n)) {
                putInt(n);
                putString(" is a prime number.");
            }
			else {
                putInt(n);
                putString(" is not a prime number.");
            }
			return 0;
		}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_funcnotreturn_find_root(self):
        input = """
        int main()
		{
    		float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    		putString("Enter coefficients a, b and c: ");
    		a = getFloat();
            b = getFloat();
            c = getFloat();
    		discriminant = b*b - 4*a*c;
    		//condition for real and different roots
    		if (discriminant > 0)
    		{
    			//sqrt() function returns square root
        		root1 = (-b+sqrt(discriminant))/(2*a);
        		root2 = (-b-sqrt(discriminant))/(2*a);
        		putFloatLn(root1);
                putFloatLn(root2);
    		}
    		//condition for real and equal roots
    		else if (discriminant <= 0)
    		{
        		root1 = root2 = -b/(2*a);
        		putString("root1 = root2 = ");
                putFloatLn(root1);
    		}
    		//if roots are not real 
    		else
    		{
        		realPart = -b/(2*a);
        		imaginaryPart = sqrt(-discriminant)/(2*a);
        		putFloat(realPart);
                putString("+-");
                putFloat(imaginaryPart);
                putString("i");
    		}
    		return 0;
		}
        float sqrt(float sqrt) {
            return 1.1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))
