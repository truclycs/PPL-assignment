import unittest
from TestUtils import TestChecker
from AST import *
# 1752282

class CheckSuite(unittest.TestCase):
    def test_undeclared_function_0(self):
        input = """void main(){
            foo();
            return;
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_undeclared_variable_1(self):
        input = """void main(){
            a;
            return;
        }"""
        expect = "Undeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_undeclared_variable_global_simple(self):
        input = """int a;
        float b;
        void main(){
            a;
            b;
            c;
            return;
        }"""
        expect = "Undeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_undeclared_variable_local_simple(self):
        input = """
        void main(){
            int a;
            float b;
            a;
            b;
            c;
            return;
        }
        """
        expect = "Undeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_correct_variable(self):
        """Simple program: int main() {} """
        input = """
        int x;
        float y;
        void main(){
            x;
            y;
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_correct_variable_2(self):
        input="""int x;
        float y;
        string z;
        boolean t;
        void main(){
            x;
            y;
            z;
            t;
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_variable_declared_in_parameter(self):
        input= """int l(int y,float z){
            y;
            z;
            return y;
        }
        void main(){
            l(6,6.5);
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_undeclared_variable_from_parameter(self):
        input="""int l(int y, float z){
            l(x,6.5);
            return 10;
        }
        void main(){
            return ;
        }"""
        expect="Undeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_parameter_overide_global_varialbe(self):
        input="""int x;
        int g(float x){
            return g(6.5);
        }
        void main(){
        return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_parameter_overide_its_function_name(self):
        input="""int g(float g){
                return 5;
        }
        void main(){
            g(6.5);
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_two_global_var_has_same_name(self):
        input = """int x;
        int y;
        float x;
        void main(){return;}
        """
        expect="Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_two_global_var_has_same_name_complex(self):
        input="""int x;
        int a(){}
        float x;
        void main(){}"""
        expect="Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_two_global_var_has_same_name_more_complex(self):
        input="""int x;
        int a(float x){return 6;}
        string x;
        void main(){return;}"""
        expect="Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_local_then_global_variable_declaration(self):
        input="""int l(int x){return x;}
        float x;
        void main(){l(5);return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_two_parameter_has_same_name(self):
        input="""int l(int x,float x){return 5;}
        void main(){l(5,5.5);return;}"""
        expect="Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_function_has_same_name_with_globvar(self):
        input="""int x;
        float x(){return 6.5;}
        void main(){x();return;}"""
        expect="Redeclared Function: x"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_function_has_same_name_with_another_func(self):
        input="""int x(){return 5;}
        float x(){return 6.5;}
        void main(){return;}"""
        expect="Redeclared Function: x"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_function_has_same_name_with_globvar_advance(self):
        input="""int x(){return 5;}
        float x;
        void main(){return;}"""
        expect="Redeclared Function: x"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_function_has_same_name_with_localvar(self):
        input="""int x(){return 5;}
        int y(float x){return 6;}
        void main(){x();y(6.5);return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_function_call_variable_from_local_scope(self):
        input="""int x(float y){return 5;}
        void main(){y;return;}"""
        expect="Undeclared Variable: y"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_function_if(self):
        input="""void main(){int x; if(5){x=5;}return;}"""
        expect="Type Mismatch In Statement: If(IntLiteral(5),Block([BinaryOp(=,Id(x),IntLiteral(5))]))"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_function_if_with_wrong_conditon(self):
        input="""void main(){int x; if(x+5){return;}}"""
        expect="Type Mismatch In Statement: If(BinaryOp(+,Id(x),IntLiteral(5)),Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_function_if_with_float_condition(self):
        input="""void main(){float x; if(x){return;}}"""
        expect="Type Mismatch In Statement: If(Id(x),Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_function_if_with_string_condition(self):
        input="""void main(){string x;if(x)return;}"""
        expect="Type Mismatch In Statement: If(Id(x),Return())"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_function_if_with_boolean_condition(self):
        input="""void main(){boolean x;
        if(x)return;return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_function_if_with_expression(self):
        input="""void main(){int x;
            if(x==5)return;
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_function_if_with_expression_advance_2(self):
        input="""void main(){int x;
            if(x+5)return;
            return;
            }"""
        expect="Type Mismatch In Statement: If(BinaryOp(+,Id(x),IntLiteral(5)),Return())"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_if_conditon_with_typemismatch_in_exp(self):
        input="""void main(){boolean x;
            if(x+5)return;
            return;
        }"""
        expect="Type Mismatch In Expression: BinaryOp(+,Id(x),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_if_condition_with_typemismatch_in_exp(self):
        input="""void main(){if(5)return;
        return;}"""
        expect="Type Mismatch In Statement: If(IntLiteral(5),Return())"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_if_conditon_is_a_function_call(self):
        input="""int a(){return 5;}
        void main(){if(a())return;return;}"""
        expect="Type Mismatch In Statement: If(CallExpr(Id(a),[]),Return())"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_if_condition_is_a_function_call_2(self):
        input="""boolean a(){return true;}
        void main(){if(a())return;return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_for_stmt_with_wrong_simple_expr(self):
        input="""void main(){for(5;true;6){5;}return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_for_stmt_with_the_first_expr_wrong(self):
        input="""void main(){
            for(true;true;6){5;}return;
        }"""
        expect="Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);IntLiteral(6);Block([IntLiteral(5)]))"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_for_stmt_with_the_second_expr_wrong(self):
        input="""void main(){
            int i;
            for(i=5;i=6;i=7){5;}return;
        }"""
        expect="Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(5));BinaryOp(=,Id(i),IntLiteral(6));BinaryOp(=,Id(i),IntLiteral(7));Block([IntLiteral(5)]))"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_for_stmt_with_the_third_expr_wrong(self):
        input="""void main(){
            int i;
            for(i=5;true;false){5;}return;
        }"""
        expect="Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(5));BooleanLiteral(true);BooleanLiteral(false);Block([IntLiteral(5)]))"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_for_stmt_with_more_complex_condition(self):
        input="""void main(){
            int i;
            for(i=5;i==9;i=i+1){}
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_for_stmt_with_function_call_expr(self):
        input="""int a(){return 5;}
        boolean b(){return true;}
        void main(){
            for(a();b();a()+1){
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_for_stmt_with_wrong_position(self):
        input="""int a(){return 5;}
        boolean b(){return true;}
        void main(){
            for(b();b();a()+1){
            }
            return;
        }"""
        expect="Type Mismatch In Statement: For(CallExpr(Id(b),[]);CallExpr(Id(b),[]);BinaryOp(+,CallExpr(Id(a),[]),IntLiteral(1));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_for_stmt_simple_loop(self):
        input="""void main(){
            int i;
            boolean t;
            for(i;t;i){
                int i;
                float i;
            }
            return;
        }"""
        expect="Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_for_stmt_full(self):
        input="""int a(int x,boolean y){
            if(y)return x;
            else return 4;
        }
        void main(){
            int i;
            for(i=0;i==4;i=i+1){
                a(i,i==4);
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_do_while_stmt_simple(self):
        input="""void main(){
         do{
         }
         while(5);
         return;
        }"""
        expect="Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_do_while_stmt_float(self):
        input="""void main(){
            do{}
            while(5.5);
            return;
        }"""
        expect="Type Mismatch In Statement: Dowhile([Block([])],FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_do_while_stmt_string(self):
        input="""void main(){
            do{}
            while("true");
            return;
        }"""
        expect="Type Mismatch In Statement: Dowhile([Block([])],StringLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_do_while_stmt_funcall(self):
        input="""int a(){return 5;}
        void main(){
            do{}
            while(a());
            return;
        }"""
        expect="Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(a),[]))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_do_while_stmt_with_special_op(self):
        input="""int a(){return 5;}
        void main(){
            int i;
            do{}
            while(i==3 && a());
            return;
        }"""
        expect="Type Mismatch In Expression: BinaryOp(&&,BinaryOp(==,Id(i),IntLiteral(3)),CallExpr(Id(a),[]))"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_do_while_stmt_with_special_op_2(self):
        input = """int a(){return 5;}
                void main(){
                    int i;
                    do{}
                    while(i==3 || a());
                    return;
                }"""
        expect="Type Mismatch In Expression: BinaryOp(||,BinaryOp(==,Id(i),IntLiteral(3)),CallExpr(Id(a),[]))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_do_while_correct(self):
        input="""boolean a(){return true;}
        void main(){
            int i;
            do{}
            while(i==3 || a());
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_do_part_in_Dowhile(self):
        input="""void main(){
            do{i=i+1;}
            while(true);
            return;
        }"""
        expect="Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_do_part_funcalll_Dowhile(self):
        input="""int a(){return 5;}
        void main(){
            do{a();b();}
            while(true);
            return;
        }"""
        expect="Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_fully_DoWhile(self):
        input="""boolean a(){return true;}
        void main(){
            int i;
            do{i==3;
            a();}
            while(i==3 || a());
            return;
        } """
        expect=""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_break_stmt(self):
        input="""void main(){
            break;
            return;
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_break_stmt_in_if(self):
        input="""void main(){
            if(true){break;}
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_break_in_for_loop(self):
        input="""void main(){
            for(5;true;6){
             break;
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_break_in_function(self):
        input="""int a(){break;return;}
        void main(){
            a();
            return;
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_break_in_if_in_loop(self):
        input="""void main(){
            for(5;true;6){
                int i;
                if(i==7){break;}
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_break_in_block_in_block(self):
        input="""void main(){
            for(5;true;6){
                {
                    break;
                }
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_break_in_do_while(self):
        input="""void main(){
            do{
                break;
            }
            while(true);
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_break_outside_do_while(self):
        input="""void main(){
            do{}
            while(true);
            break;
            return;
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_break_inside_for_but_doWhile(self):
        input="""void main(){
            do{}
            while(true);
            break;
            for(5;true;6){
                break;
            }
            return;
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_break_outside_for_but_doWhile(self):
        input="""void main(){
            do{break;}
            while(true);
            for(5;true;6){
            }
            break;
            return;
        }"""
        expect="Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_continue_in_main_simple(self):
        input="""void main(){
            continue;
            return;
        }"""
        expect="Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_continue_outside_loop(self):
        input="""void main(){
            do{}
            while(true);
            continue;
            return;
        }"""
        expect="Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_continue_inside_for(self):
        input="""void main(){
            int i;
            for(i;i==7;i=i+1){
                continue;
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_continue_in_if(self):
        input="""void main(){
            int i;
            if(i<7){
                continue;
            }
            return;
        }"""
        expect="Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_continue_in_doWhile_but_for(self):
        input="""void main(){
            int i;
            do{
            continue;}
            while(i<7);
            for(i;true;i=i+1){}
            continue;
            return;
        }"""
        expect="Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_continue_in_For_but_doWhile(self):
        input="""void main(){
            int i;
            do{
            i=i+1;}
            while(i<7);
            continue;
            for(i;true;i=i+1){continue;}
            return;
        }"""
        expect="Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_continue_in_if_in_doWhile(self):
        input="""void main(){
            int i;
            do{
                if(i==5){continue;}
            }
            while(i<7);
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_return_int_stmt(self):
        input="""int a(){return true;}
        void main(){a();return;}"""
        expect="Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_return_boolean_function(self):
        input="""boolean a(){return 5;}
        void main(){a();return;}"""
        expect="Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_return_void_function(self):
        input="""void a(){return 5;}
        void main(){a();return;}"""
        expect="Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_return_int_for_float_function(self):
        input="""float a(){return 5;}
        void main(){a();return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_function_not_return(self):
        input="""int a(){}
        void main(){return;}"""
        expect="Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_function_float_not_return(self):
        input="""float b(){}
        void main(){return;}"""
        expect="Function b Not Return "
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_function_main_not_return(self):
        input="""void main(){int a;}"""
        expect="Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_No_entry_point(self):
        input="int a(){return 1;}"
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_No_entry_point_complex(self):
        input="""int a(){return 1;}
        int b(){return 2;}"""
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_No_entry_point_main(self):
        input="""int a(){return 1;}
        int main(){return 2;}"""
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_CallExpr_simple(self):
        input="""int a(){return 1;}
        void main(){a();return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_Undeclared_Function_complex(self):
        input="""int a(){return 1;}
        void main(){b();return;}"""
        expect="Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_parameter_in_funcCall(self):
        input="""int a(int b){return 1;}
        void main(){a(5.5);return;}"""
        expect="Type Mismatch In Expression: CallExpr(Id(a),[FloatLiteral(5.5)])"
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_parameter_in_funcCall_2(self):
        input="""int a(float b){return 1;}
        void main(){a(5);return;}"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_number_of_parameter_in_fucnCall(self):
        input="""int a(int b,int c){return 1;}
        void main(){a(5);return;}"""
        expect="Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_wrong_type_of_parameter_in_funcall_complex(self):
        input = """int a(int b,int c){return 1;}
                void main(){a(5,5.5);return;}"""
        expect="Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(5),FloatLiteral(5.5)])"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_function_call_functioncall(self):
        input="""int a(){return 1;}
        int b(int c ){return c;}
        void main(){
            b(a());
            b(b(5));
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_no_left_value(self):
        input="""void main(){
            int a;
            int b;
            int c;
            a+b=c;
            return;
        }"""
        expect="Not Left Value: BinaryOp(=,BinaryOp(+,Id(a),Id(b)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_simple_expr(self):
        input="""int a;
        int b;
        void main(){
            a=a+b;
            x=a-b;
            return;
        }"""
        expect="Undeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_function_array_pointer_type(self):
        input="""int[] a(int c[]){int b[5];return b;}
        int f(int g){return 1;}
        void main(){
            int d[5];
            a(d);
            f(d[4]);
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_not_left_value_for_array(self):
        input="""void main(){
            int a[5];
            a[4]=4+5*a[3]-2;
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_complex_expr(self):
        input="""void main(){
            int a[5];
            int b;
            b=4;
            a[4]=4+(6+10/a[4])-b+15*27+a[b];
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_complex_expr_in_stmt(self):
        input="""int[] a(){int b[5];return b;}
        void main(){
            int b[4];
            if(b[3]==2){
                a();
                return ;
            }
            return;
        }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_continue_in_function(self):
        input="""
        int a(int x){int a;return a(5);}
        void main(){return;}"""
        expect="Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_funtion_not_return(self):
        input="""
        void main(){
            int a;
            if(a==5)return;
        }"""
        expect="Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_function_not_return_advance(self):
        input="""void main(){
            int a;
            if(a==5){
                if(a==4){return;}
            }
            else return;
        }"""
        expect="Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_unreachable_function_special(self):
        input="""int a(){return 1;}
        int b(){return 2;}
        void main(){a();
        return;}
        """
        expect="Unreachable Function: b"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_special_functionCall_(self):
        input = """
        int foo1(){foo2();return 1;}
        int foo2(){foo1();return 1;}
        void main(){return;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_special_function_call_and_parameter_same_name(self):
        input = """
        void main(){foo(5);return;}
        int foo(int foo){
            foo(foo);
            return 5;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(foo)])"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_special_unreachable_function(self):
        input="""int a(int x){return 1;}
        void main(){int b;
        if(a(a(a(a(b)))) == 5)
            {b=10;}
            return;
            }"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_special_not_left_value(self):
        input="""int a(){return 1;}
        void main(){
            a()=5+6;
            return;
        }"""
        expect="Not Left Value: BinaryOp(=,CallExpr(Id(a),[]),BinaryOp(+,IntLiteral(5),IntLiteral(6)))"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_buildIn_function(self):
        input="""int a(){return 1;}
        void main(){
            int d;
            string b;
            float c;
            if(c==d){c=d-5;}
            else c=d+5;
            for(c;c!=d;c=d+1){a();getInt();}
            do{putIntLn(b);}while(d-c<0);
            return;
        }"""
        expect="Type Mismatch In Expression: BinaryOp(==,Id(c),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_buildIn_function_2(self):
        input="""int a(){return 1;}
        void main(){
            int d;
            string b;
            int c;
            if(c==d){c=d-5;}
            else c=d+5;
            for(c;c!=d;c=d+1){a();getInt();}
            do{getInt(b);}while(d-c<0);
            return;
        }"""
        expect="Type Mismatch In Expression: CallExpr(Id(getInt),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,499))






