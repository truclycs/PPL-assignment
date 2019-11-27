import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    

    def test_Redeclared_Var_in_main(self):
        input = """
            void main(){
                int nezuko;
                float nezuko;
            }
        """
        expect = "Redeclared Variable: nezuko"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_Redeclared_Var_in_Gobal(self):
        input = """
            int nezuko;
            string nezuko;
            void main(){
            }
        """
        expect = "Redeclared Variable: nezuko"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_Redeclared_Var_in_Fuction(self):
        input = """
            int foo(){
                int tanjiro;
                float tanjiro;
            }
            void main(){
            }
        """
        expect = "Redeclared Variable: tanjiro"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Redeclared_Var_in_Fuction_haveParam(self):
        input = """
            int foo(float tanjiro){
                int tanjiro;

            }
            void main(){
            }
        """
        expect = "Redeclared Variable: tanjiro"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_Redeclared_Param_in_Fuction_haveParam(self):
        input = """
            int foo(float tanjiro,int tanjiro){
               

            }
            void main(){
            }
        """
        expect = "Redeclared Parameter: tanjiro"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_2_function_no_return_with_if1(self):
        input = """
            int sunny2(){
                if(5<4){
                    return sunny2();
                }
            }
            int sunny(){

            }
            void main(){
               sunny2();
            }
        """
        expect = "Function sunny Not Return "
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_Redeclared_Param2_in_Fuction_haveParam(self):
        input = """
            int foo(string nobita,int nobita){
               

            }
            void main(){
            }
        """
        expect = "Redeclared Parameter: nobita"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclared_Param2_in_Fuction_haveMutilParam(self):
        input = """
            int foo(string nobita,int nobita,float nobita){
            }
            void main(){
            }
        """
        expect = "Redeclared Parameter: nobita"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclared_Fuction(self):
        input = """
            int luffy(){
               return 0;

            }
            float luffy(){
                return 0;
            }
            void main(){
                luffy();
            }
        """
        expect = "Redeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_Redeclared_Fuction_with_param(self):
        input = """
            int luffy1(int a){
               return 5;

            }
            float luffy1(int b){
                return 5;
            }
            void main(){
                luffy1(5);
            }
        """
        expect = "Redeclared Function: luffy1"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_Redeclared_Fuction_with_different_param(self):
        input = """
            int luffy1(int iu,float jisoo){
               return 0;

            }
            float luffy1(int jisoo){
                return 0;
            }
            void main(){
                luffy1(0);
            }
        """
        expect = "Redeclared Function: luffy1"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Undeclared_Identiﬁer(self):
        input = """
            void main(){
                jisoo = 5;
            }
        """
        expect = "Undeclared Identifier: jisoo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Undeclared_Identiﬁer_in_if(self):
        input = """
            void main(){
                if(jenie<5){
                    luffy();
                }
            }
        """
        expect = "Undeclared Identifier: jenie"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_Undeclared_Identiﬁer_in_for(self):
        input = """
            void main(){
                for(jenie;jenie<5;6){
                    break;
                }
            }
        """
        expect = "Undeclared Identifier: jenie"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Undeclared_Identiﬁer_in_doWhile(self):
        input = """
            void main(){
                do{
                    continue;
                }
                while(rose<5);
            }
        """
        expect = "Undeclared Identifier: rose"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_Undeclared_Identiﬁer_in_funcall(self):
        input = """
            int luffy(int rose){
                return rose;
            }
            void main(){
                luffy(a);
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Undeclared_Identiﬁer_in_return(self):
        input = """
            int luffy(){
                return lisa;
            }
            void main(){
                luffy();
            }
        """
        expect = "Undeclared Identifier: lisa"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_Undeclared_Identiﬁer_in_expression(self):
        input = """
            void main(){
                int a;
                a = 1+lisa;
            }
        """
        expect = "Undeclared Identifier: lisa"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_Undeclared_Function(self):
        input = """
            void main(){
                luffy();
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_Undeclared_Function_in_for(self):
        input = """
            void main(){
                for(1;true;2){
                    luffy();
                }
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_Type_Mismatch_In_epression_funcall(self):
        input = """
            int robin(int c,float e){
                return c;
            }
            void main(){
               robin(true,5);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(robin),[BooleanLiteral(true),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_Type_Mismatch_In_epression_funcall1(self):
        input = """
            int robin(string d){
                return 5;
            }
            void main(){
               robin(5);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(robin),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_Type_Mismatch_In_epression_int(self):
        input = """
            void main(){
               string a;
               a = 5+5.6;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(5),FloatLiteral(5.6)))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_Type_Mismatch_In_epression_float(self):
        input = """
            void main(){
               float a;
               a = true;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_Type_Mismatch_In_epression_string(self):
        input = """
            void main(){
               string a;
               a = true;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_Type_Mismatch_In_epression_boolean(self):
        input = """
            void main(){
               boolean a;
               a = "blueming";
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(blueming))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_Type_Mismatch_In_epression1(self):
        input = """
            void main(){
               float a;
               if(5>true){
                   chopper();
               }
            }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(>,IntLiteral(5),BooleanLiteral(true)),Block([CallExpr(Id(chopper),[])]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_Type_Mismatch_In_epression2(self):
        input = """
            void main(){
               float a;
               if(5>true){
                   chopper();
               }
            }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(>,IntLiteral(5),BooleanLiteral(true)),Block([CallExpr(Id(chopper),[])]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_function_no_return(self):
        input = """
            int chopper(){

            }
            void main(){
               chopper();
            }
        """
        expect = "Function chopper Not Return "
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_2_function_no_return(self):
        input = """
            int franky2(){
                return 5;
            }
            int franky(){

            }
            void main(){
               franky2();
            }
        """
        expect = "Function franky Not Return "
        self.assertTrue(TestChecker.test(input,expect,429))


    def test_2_function_no_return_with_doWhile(self):
        input = """
            int franky2(){
                do{
                    return 5;
                }
                while(5<3);
            }
            int franky(){
                
            }
            void main(){
               franky2();
               franky();
            }
        """
        expect = "Function franky Not Return "
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_2_function_no_return_with_if(self):
        input = """
            int franky2(){
                if(5<4){
                    franky2();
                }
                else{
                    return 5;
                }
            }
            int franky(){

            }
            void main(){
               franky2();
               franky();
            }
        """
        expect = "Function franky Not Return "
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_break_not_in_for(self):
        input = """
            void main(){
               break;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_break_not_in_for1(self):
        input = """
            void main(){
                for(5;4<5;4){

                }
               break;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_break_not_in_for2(self):
        input = """
            void main(){
                for(5;4<5;4){
                    break;
                }
               break;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_break_not_in_for2(self):
        input = """
            void main(){
                break;
                for(5;4<5;4){
                    break;
                }
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_break_not_in_for3(self):
        input = """
            int brook(){
                for(5;4<4;4){

                }
                break;
            }
            void main(){
                for(5;4<5;4){
                    break;
                }
                brook();
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_break_not_in_for4(self):
        input = """
            int brook(){
                break;
                for(5;4<4;4){

                }
                
            }
            void main(){
                for(5;4<5;4){
                   brook();
                }
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_break_not_in_while(self):
        input = """
            void main(){
                break;
                do{
                    int a;
                }
                while(5<4);
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_break_not_in_while1(self):
        input = """
            void main(){
                
                do{
                    int a;
                    break;
                }
                while(5<4);
                break;
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_Undeclared_Function_in_doWhile(self):
        input = """
            void main(){
                do{
                    luffy();
                }
                while(1<2);
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_Undeclared_Function_in_If(self):
        input = """
            void main(){
                if(5<6){
                    for(4;false;3){
                        luffy();
                    }
                }
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_Undeclared_Function_in_Else(self):
        input = """
            void main(){
                if(true){
                    int luffy;
                }
                else{
                    luffy();
                }
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_Undeclared_Function_in_return(self):
        input = """
            int zoro1(){
                return zoro();
            }
            void main(){
                zoro1();
            }
        """
        expect = "Undeclared Function: zoro"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_Undeclared_Function_in_expression(self):
        input = """
            void main(){
                int a;
                a = 2 + zoro();
            }
        """
        expect = "Undeclared Function: zoro"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_Type_Mismatch_In_If(self):
        input = """
            void main(){
               if(0){
                   zoro();
               }
            }
        """
        expect = "Type Mismatch In Statement: If(IntLiteral(0),Block([CallExpr(Id(zoro),[])]))"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_Type_Mismatch_In_If1(self):
        input = """
            void main(){
               if("saitama"){
                   zoro();
               }
            }
        """
        expect = "Type Mismatch In Statement: If(StringLiteral(saitama),Block([CallExpr(Id(zoro),[])]))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_Type_Mismatch_In_Midfor(self):
        input = """
            void main(){
               for(5;"test";5){
                   zoro();
               }
            }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(5);StringLiteral(test);IntLiteral(5);Block([CallExpr(Id(zoro),[])]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_Type_Mismatch_In_Firstfor(self):
        input = """
            void main(){
               for(true;5>6;5){
                   sanji();
               }
            }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BinaryOp(>,IntLiteral(5),IntLiteral(6));IntLiteral(5);Block([CallExpr(Id(sanji),[])]))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_Type_Mismatch_In_Thirdfor(self):
        input = """
            void main(){
               for(4;5>6;false){
                   sanji();
               }
            }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(4);BinaryOp(>,IntLiteral(5),IntLiteral(6));BooleanLiteral(false);Block([CallExpr(Id(sanji),[])]))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_Type_Mismatch_In_doWhile(self):
        input = """
            void main(){
               do{
                   sanji();
               }
               while("test");
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(sanji),[])])],StringLiteral(test))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_Type_Mismatch_In_doWhile1(self):
        input = """
            void main(){
                int a;
                a = 6;
               do{
                   nami();
               }
               while(a);
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(nami),[])])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_Type_Mismatch_In_doWhile2(self):
        input = """
            void main(){
                int a;
                a = 6;
               do{
                   nami();
               }
               while(a+5);
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(nami),[])])],BinaryOp(+,Id(a),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_Type_Mismatch_In_return(self):
        input = """
            void main(){
               return 5;
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_Type_Mismatch_In_return1(self):
        input = """
            int nami(){
                return true;
            }
            void main(){
               nami();
            }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_Type_Mismatch_In_return2(self):
        input = """
            int nami(string c){
                return c;
            }
            void main(){
               nami("akame");
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_Type_Mismatch_In_return3(self):
        input = """
            int nami(string c,float e){
                return e;
            }
            void main(){
               nami("akame",1.5);
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(e))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_Type_Mismatch_In_return_void(self):
        input = """
            void nami(string c,float e){
                return 5;
            }
            void main(){
               nami("akame",1.5);
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_Type_Mismatch_In_return_string(self):
        input = """
            string robin(string c,float e){
                return e;
            }
            void main(){
               robin("akame",1.5);
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(e))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_Type_Mismatch_In_return_boolean(self):
        input = """
            boolean robin(string c,float e){
                return e;
            }
            void main(){
               
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(e))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_break_not_in_while2(self):
        input = """
            float brook(){
                break;
                return 5;
            }
            void main(){
                
                do{
                    brook();
                    break;
                }
                while(5<4);
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_continue_not_in_for(self):
        input = """
            void main(){
                
                continue;
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_continue_not_in_for1(self):
        input = """
            void main(){
                for(5;4<3;5){}
                continue;
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_continue_not_in_for2(self):
        input = """
            void main(){
                continue;
                for(5;4<3;5){continue;}
                
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_continue_not_in_for3(self):
        input = """
            void main(){
                
                for(5;4<3;5){continue;}
                continue;
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_continue_not_in_for4(self):
        input = """
            int brook(){
                continue;
                return brook();
            }
            void main(){
                
                for(5;4<3;5){continue;}
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_continue_not_in_doWhile(self):
        input = """
            void main(){
                do{
                    break;
                }while(5<3);
                continue;
                
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_continue_not_in_doWhile1(self):
        input = """
            void main(){
                continue;
                do{
                    continue;
                }while(5<3);
                
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_continue_not_in_doWhile2(self):
        input = """
            int brook(){
                continue;
                return brook();
            }
            void main(){
                do{
                    continue;
                }while(5<3);
                
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_continue_not_in_Loop(self):
        input = """
            void main(){
               if(true){
                   continue;
               }
                
               
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_break_not_in_Loop(self):
        input = """
            void main(){
               if(true){
                   break;
               }
                
               
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_No_entry_point(self):
        input = """
            int main1(){
               if(true){
                   break;
               }
                
               
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_No_entry_point2(self):
        input = """
            int main1(){
               if(true){
                   break;
               }
                
               
            }
            float main2(){
                return 5.5;
            }
            string main3(){
                return "saitama";
            }
            boolean main4(){
                return true;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,472))


    def test_No_entry_point3(self):
        input = """
            void main3(int a){

            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_Unreachable_function(self):
        input = """
            int nobita(){
                return 5;
            }
            void main(){

            }
        """
        expect = "Unreachable Function: nobita"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_Unreachable_function1(self):
        input = """
            int nobita(){
                return 5;
            }
            int sasuke(int a){
                return a;
            }
            void main(){
                nobita();
            }
        """
        expect = "Unreachable Function: sasuke"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_Unreachable_function2(self):
        input = """
            int nobita1(){
                return 5;
            }
            int sasuke(int a){
                return sasuke(5);
            }
            void main(){
                
            }
        """
        expect = "Unreachable Function: nobita1"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_Unreachable_function3(self):
        input = """
            int nobita2(){
                return nobita2();
            }
            int sasuke1(int a){
                return a;
            }
            void main(){
                
            }
        """
        expect = "Unreachable Function: sasuke1"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_Complex_Break_not_in_loop(self):
        input = """
            int robin(){
                for(5;true;5){
                    do{
                        if(true){
                            for(5;true;5){
                                do{
                                    return robin();
                                    break;
                                }
                                while(true);
                            }
                        }
                    }while(5<3);
                }
                break;
            }
            void main(){
                
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_Complex_Continue_not_in_loop(self):
        input = """
            int robin(){
                for(5;true;5){
                    do{
                        if(true){
                            for(5;true;5){
                                do{
                                    return robin();
                                    break;
                                }
                                while(true);
                            }
                        }
                    }while(5<3);
                }
                continue;
            }
            void main(){
                
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_Undeclared_Identiﬁer_in_if(self):
        input = """
            void main(){
                if(jenie<5){
                    luffy();
                }
            }
        """
        expect = "Undeclared Identifier: jenie"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_Undeclared_Identiﬁer_in_for2(self):
        input = """
            void main(){
                for(jenie;jenie<5;6){
                    break;
                }
            }
        """
        expect = "Undeclared Identifier: jenie"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_Undeclared_Identiﬁer_in_doWhile2(self):
        input = """
            void main(){
                do{
                    continue;
                }
                while(rose<5);
            }
        """
        expect = "Undeclared Identifier: rose"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_Undeclared_Identiﬁer_in_funcall2(self):
        input = """
            int luffy(int rose){
                return rose;
            }
            void main(){
                luffy(a);
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_Undeclared_Identiﬁer_in_return2(self):
        input = """
            int luffy(){
                return lisa;
            }
            void main(){
                luffy();
            }
        """
        expect = "Undeclared Identifier: lisa"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_Undeclared_Identiﬁer_in_expression2(self):
        input = """
            void main(){
                int a;
                a = 1+lisa;
            }
        """
        expect = "Undeclared Identifier: lisa"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_Undeclared_Function2(self):
        input = """
            void main(){
                luffy();
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_Undeclared_Function_in_for2(self):
        input = """
            void main(){
                for(1;true;2){
                    luffy();
                }
            }
        """
        expect = "Undeclared Function: luffy"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_Type_Mismatch_In_epression_funcall2(self):
        input = """
            int robin(int c,float e){
                return c;
            }
            void main(){
               robin(true,5);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(robin),[BooleanLiteral(true),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_Complex_return(self):
        input = """
            int test23(){
                do{
                    if(true){
                        for(5;true;5){
                            if(true){
                                do{
                                  if(true){
                                        test23();
                                    }
                                    else{
                                        return test23();
                                    }  
                                }while(true);
                            }
                        }
                    }
                }
                while(5<3);
                test24();
            }
            void main(){
            }
        """
        expect = "Undeclared Function: test24"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_Unreachable_statement_for(self):
        input = """
            void main(){
                5 = 6+8;
            }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_Unreachable_statement_for1(self):
        input = """
            void main(){
                main() = "saitama";
            }
        """
        expect = "Not Left Value: CallExpr(Id(main),[])"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_Unreachable_statement_for2(self):
        input = """
            void main(){
                true = false;
            }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_Unreachable_statement_if(self):
        input = """
            void main(){
                "saitama" = 6;
            }
        """
        expect = "Not Left Value: StringLiteral(saitama)"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_Unreachable_statement_if1(self):
        input = """
            void main(){
                int a;
                int b;
                a+6 = b+5;
            }
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(6))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_Unreachable_statement_if2(self):
        input = """
            void main(){
                int a;
                int b;
                5= a-b;
            }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_Unreachable_statement_if3(self):
        input = """
            void main(){
                int a;
                int b;
                true = a/b;
            }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_Unreachable_statement_if4(self):
        input = """
            void main(){
                main() = true;
            }
        """
        expect = "Not Left Value: CallExpr(Id(main),[])"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_Index_out_of_range(self):
        input = """
            void main(){
                5-3 = true && true ;
            }
        """
        expect = "Not Left Value: BinaryOp(-,IntLiteral(5),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_Type_Mismatch_In_return_boolean2(self):
        input = """
            boolean robin(string c,float e){
                return e;
            }
            void main(){
               robin("saitama",1.5);
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(e))"
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_2_function_no_return_with_for(self):
        input = """
            int sunny2(){
                for(5;5<34;4){
                    return 5;
                }
            }
            int sunny(){

            }
            void main(){
               sunny2();
               sunny();
            }
        """
        expect = "Function sunny Not Return "
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_No_entry_point4(self):
        input = """
            void main3(int a){

            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,500))