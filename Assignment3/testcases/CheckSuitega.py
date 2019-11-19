import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):


    def test_Redeclared_Variable_1(self):
        input = """
                int something;
                float anything;
                void main(){return;}
                boolean main;
                """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_Redeclared_Variable_2(self):
        input = """
                int anything[999];
                float anything;
                void main(string main[]){
                    // Nothing
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: anything"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Redeclared_Variable_3(self):
        input = """
                int something;
                float anything;
                void main(int same[]){
                    float same;
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: same"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_Redeclared_Variable_4(self):
        input = """
                int something[999];
                float anything[999];
                void main(string main[]){
                    int scope;
                    float scope1;
                    {
                        string scope;
                        {
                            boolean scope;
                        }
                    }
                    boolean scope1;
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: scope1"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_Redeclared_Function_1(self):
        input = """
                int someone;
                float anyone;
                boolean main;
                void main(){}
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclared_Function_2(self):
        input = """
                int someone;
                float anyone;
                boolean same;
                void main(){}

                int main(string d[]){}
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclared_Parameter(self):
        input = """
                int One;
                float Two;
                string Three;
                boolean Four;
                void Five(int One, float Two, string Three, boolean Four, int One[]){}
                int main(){return 1;}
                """
        expect = "Redeclared Parameter: One"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_No_Entry_Point_1(self):
        input = """
                int someone;
                string anyone;
                boolean main;
                float something;
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_No_Entry_Point_2(self):
        input = """
                int someone;
                string anyone;
                boolean main[999];
                float something;
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Mismatch_Statement_If_1(self):
        input = """
                float many[99];
                boolean condition[99];
                int main(int argc){
                    if(true){
                        if(condition[0]){
                            // Just empty
                            return argc;
                        }
                    }else{
                        if(many[98] + 3){
                            // We have a exception
                            return argc + 3;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,ArrayCell(Id(many),IntLiteral(98)),IntLiteral(3)),Block([Return(BinaryOp(+,Id(argc),IntLiteral(3)))]))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Mismatch_Statement_If_2(self):
        input = """
                int many[99];
                boolean condition[99];
                int main(int argc){
                    if(true){
                        if((many[98] <= 3) && (argc == argc + 1)){
                            // Just empty
                            return argc;
                        }
                    }else{
                        if(many[99] = 3){
                            // We have a exception
                            return argc;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,ArrayCell(Id(many),IntLiteral(99)),IntLiteral(3)),Block([Return(Id(argc))]))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_Mismatch_Statement_If_3(self):
        input = """
                int many[99];
                boolean condition[99];
                int main(int argc){
                    if(BooleanFunction()){
                        if((many[98] <= 3) && (argc == argc + 1)){
                            return argc;
                        }
                    }else{
                        if(ArrayFunction()){
                            return argc + 3;
                        }
                    }
                }
                boolean BooleanFunction(){return true;}
                void ArrayFunction(){return;}
                """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(ArrayFunction),[]),Block([Return(BinaryOp(+,Id(argc),IntLiteral(3)))]))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Mismatch_Statement_For_1(self):
        input = """
                float many;
                string main(int man){
                    for(man = 0; many <= man; man = man + 1){
                        for(true; true; true){
                            print("Upin Ipin >.<");
                        }
                    }
                    return "Nothing";
                }

                void print(string str){
                    print(str);
                }
                """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);BooleanLiteral(true);Block([CallExpr(Id(print),[StringLiteral(Upin Ipin >.<)])]))"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_Mismatch_Statement_For_2(self):
        input = """
                float many;
                string main(int man){
                    for(man = 0; many <= man; man = man + 1){
                        for(man; wrong(); man){
                            print("Upin Ipin >.<");
                        }

                        for(1; 2; 3){
                            print("It's wrong");
                        }
                    }
                    return "Nothing";
                }

                void print(string str){
                    print(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(3);Block([CallExpr(Id(print),[StringLiteral(It's wrong)])]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Mismatch_Statement_DoWhile_1(self):
        input = """
                string str;
                boolean bool[99];
                boolean[] main(){
                    for(3; wrong(); 3){
                        do
                            str = "ABC";
                            print(str);
                        while(bool);
                        return bool;
                    }
                }
                void print(string str){
                    print(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(str),StringLiteral(ABC)),CallExpr(Id(print),[Id(str)])],Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_Mismatch_Statement_DoWhile_2(self):
        input = """
                string str;
                boolean bool[99];
                boolean[] main(boolean input[]){
                    do
                        do 
                        {
                            return input;
                        }
                        while(bool[0] && true || false);
                    while(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([Dowhile([Block([Return(Id(input))])],BinaryOp(||,BinaryOp(&&,ArrayCell(Id(bool),IntLiteral(0)),BooleanLiteral(true)),BooleanLiteral(false)))],Id(str))"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_Mismatch_Statement_Return_1(self):
        input = """
                string str;
                boolean bool[99];
                void main(int para){
                    {
                        {
                            return para;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(para))"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_Mismatch_Statement_Return_2(self):
        input = """
                string str;
                boolean bool[99];
                float main(int para){
                    if(true){
                        return para;
                    }
                    else{
                        if(false){
                            return 3.;
                        }
                    }
                    return str;
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(str))"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_Mismatch_Statement_Return_3(self):
        input = """
                string str[999];
                boolean bool[99];
                string[] main(string char[]){
                    if(false){
                        return str;
                    }
                    else{
                        if(bool[98]){
                            return char;
                        }
                        else{
                            return bool[98];
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(bool),IntLiteral(98)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    # def test_ex(self):
    #     input = """
    #             string str[999];
    #             boolean bool[99];
    #             string[] main(string char[]){
    #                 if(false){
    #                     return str;
    #                 }
    #                 else{
    #                     if(bool[98]){
    #                         return char;
    #                     }
    #                     else{
    #                         return bool[98];
    #                     }
    #                 }
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return(ArrayCell(Id(bool),IntLiteral(98)))"
    #     self.assertTrue(TestChecker.test(input,expect,410))





    