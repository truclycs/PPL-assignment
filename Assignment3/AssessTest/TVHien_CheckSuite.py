import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_main_1(self):
        input = """void main() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_main_2(self):
        input = Program([VarDecl("a",IntType())])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_main_3(self):
        input = """void main (int a){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_main_func(self):
        input = """int main (){return 1;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_main_func1(self):
        input = """
        int a, a, c;
        void main (){}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_main_func2(self):
        input = """
        int a, c;
        int foo(){return 0;}
        int foo(){return 0;}
        void main (){}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redecl_1(self):
        input = """
        int foo, c;
        int foo(){return 0;}
        void main (){}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_return_1(self):
        input = """
        int foo(){}
        void main (){
            if (1) a();
        }
        int foo2(){ return 0;}"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_return_2(self):
        input = """
        int foo(){return 0;}
        void main (){
        }
        int foo2(){}"""
        expect = "Function foo2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redecl_2(self):
        input = """
        int foo(int a,int a){return 0;}
        void main (){
          foo(1,2);  
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redecl_3(self):
        input = """
        int foo(){
        int foo;
        return 0;}
        void main (){
            
        }
        int foo(){ return 0;}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redecl_34(self):
        input = """
        int foo(){
        int foo;
        return 0;}
        void main (){
            int foo; 
        }
        int foo2(int foo){ 
        return 0;}
        int foo2(int foo){ 
        return 0;}"""
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_return_2(self):
        input = """
        int foo(){
        return 1.0;}
        void main (){
            
        }
        int foo2(){ return 0;}"""
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_return_3(self):
        input = """
        void foo(){
                return 1;}
        void main (){
            
        }"""
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_return_4(self):
        input = """
        int foo(){
        int a;
        return a;}
        void main (){
            
        }
        string foo2(){ return 0;}"""
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_return_5(self):
        input = """
        int foo(){
        float a;
        return a;}
        void main (){
            
        }
        int foo2(){ return 0;}"""
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_vardecl_1(self):
        input = """
        int foo(){
            boolean a;

        return 1;}
        void main (){
            foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_vardecl_2(self):
        input = """
        int foo(){
            a;
        return 1;}
        void main (){
            
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_redeclared1(self):
        input="""int foo(){}
        int foo(){}
        void main(){}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_redeclared_param(self):
        input="""
            int x;
            int y;
            int swap(int a,int b, boolean a){
                return 1;
            }
            void main(){
                swap(1,2,true);
            }
         """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_redeclared2(self):
        input="""int a;
        int b;
        
        void main(){
            int x;
            x=a+b;
        }
        int c;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_typeMis_match(self):
        input="void main(){} int foo(){putIntLn(getInt(4));}"
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_Undeclared_Identifier_d(self):
        input = """ void main(){}
                    void foo(int a){
                        int z;
                            d;
                            } 
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_Undeclared_Identifier_d1(self):
        input = """ void main(){}
                    void foo(int a){
                            d;
                            } 
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_Mismatch_Stmt_If_expr_is_Integer(self):
        input = """ void main(){} 
                    void foo(int a){
                        int b;
                        if(10)
                        a = 2;
                        } 
                """
        expected = """Type Mismatch In Statement: If(IntLiteral(10),BinaryOp(=,Id(a),IntLiteral(2)))"""
        self.assertTrue(TestChecker.test(input,expected,423))

    def test_undeclared_function_01(self):
        input = """
        	int main() {foo();}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_undeclared_function_02(self):
        input = """
        	void main () {writeIntLn(3);}
        """
        expect = "Undeclared Function: writeIntLn"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_undeclared_function_03(self):
        input = """
        int a[10],c;
        int m(int size, int arr[]){
            foo();
        }
        void main(){
            int a[1];
            m(10,a);
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_mismatch_condition_ifstmt1(self):
        """ Mismatch Condition(Void) If Statement """
        input = """
        void main(){
            if (div(5,2)){}
            else {}
        }
        void print(){}
        """
        expect = "Undeclared Function: div"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_function_04(self):
        input = """
	        int a[10],c;
	        void m(int size, int arr[]){
	            {complex(10);}
	        }
	        void main(){
	            int a[1];
	            m(10,a);
        }
        """
        expect = "Undeclared Function: complex"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_undeclared_function_05(self):
        input = """
	        int a[10],c;
	        void main(){
	            int size;
	            int i;
	            if(true)
	                size = i;
	            
	            else{
	                complex(10);
	            }
        }
        """
        expect = "Undeclared Function: complex"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_undeclared_function_06(self):
        input = """
	        int a[10],c;
	        void main(){
	            int size;
	            int i;
	            for(i = 0; i < 100; i = i + 1){
	                foo();
	            }
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_undeclared_function_07(self):
        input = """
        int a[10],c;
        void main(){
            int size;
            size = c+1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_breakNotLoop_01(self):
        inp = """
        void main(){
            foo();
        }
        void foo(){
            do{
                2;
            } while (true);
            break;
        }
        """
        out = "Break Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,432))
    def test_breakNotLoop_02(self):
        inp = """
        void main(){
            for(1;true;1) 1;
            break;
            return;
        }"""
        out = "Break Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,433))        



	# ContinueNotInLoop
    def test_conNotLoop_01(self):
        inp = """
        void main() {
            int i;
            for (i; i < 5; i = i + 2) {
              i = i + 1;
            }
            continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,434))
    def test_conNotLoop_02(self):
        inp = """
        void main(){
            continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,435))      
    def test_conNotLoop_03(self):
        inp = """
        void main(){
            for(1;true;1){if(true) continue;}
            if(true) { 
                for(1;true;1){ 
                    if(true) break; 
                } 
                continue;
            } 
            else { }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,436))
    def test_conNotLoop_04(self):
        inp = """
        void main(){
            if(true) { 
                for(1;true;1) { continue; } 
                if(false) { continue;} 
            }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,437))
    def test_conNotLoop_05(self):
        inp = """
        void main(){
            for(1;true;1) { 
                if(true) continue; 
            }
            do 
                if(true) continue; 
                else { continue;} 
            while(true);
            if(false) {} 
            else continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,438))
    def test_conNotLoop_06(self):
        inp = """
        void main(){
            for(1;true;1) { 
                do if(true) break; else {continue;} while(true); if(true) continue; }
                do if(true) continue; else {continue;} while(true);
                if(false) { } 
                else { { 
                    { 
                        { 
                            { int a; continue; } 
                        } 
                    } 
                } 
            }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,439))
    def test_conNotLoop_07(self):
        inp = """
         void main(){
          do if(true) break; else {continue;} while(true);
          for(1;true;1) { if(true) continue; }
          do if(false) break; else {} while(true);
          continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,440))




	# NoEntryPoint
    def test_NoEntryPoint_01(self):
        inp = "int m(){ }"
        out = "No Entry Point"
        self.assertTrue(TestChecker.test(inp,out,441))
    def test_NoEntryPoint_02(self):
        inp = """
        int mn(){
            int i; 
            if(i==5) return 1; 
            else return 1; 
            i=1+i;
        }
        """
        out = "No Entry Point"
        self.assertTrue(TestChecker.test(inp,out,442))
    def test_NoEntryPoint_03(self):
        inp = "float min(int a){ }"
        out = "No Entry Point"
        self.assertTrue(TestChecker.test(inp,out,443))
    def test_NoEntryPoint_04(self):
        inp = "boolean man(int a, int b){ int c; man();}"
        out = "No Entry Point"
        self.assertTrue(TestChecker.test(inp,out,444))



	# UnreachableFunction
    def test_unReach_Func_01(self):
        inp = """
        void foo(){ }
        void main(){ }
        """
        out = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(inp,out,445))
    def test_unReach_Func_02(self):
        inp = """
        void foo(){
            foo();
        }
        void main(){ }
        """
        out = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(inp,out,446))
    def test_unReach_Func_03(self):
        inp = """
        void foo(){
            foo();
        }

        void foo1(){
            foo();
        }
        void main(){ }
        """
        out = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(inp,out,447))
    def test_unReach_Func_04(self):
        inp = """
        void foo(){
            foo1();
        }

        void foo1(){
            foo();
        }

        void foo2(){
            foo();
            foo1();
        }

        void main(){ }
        """
        out = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(inp,out,448))




	# NotLeftValue
    # Index
    # Uninitialize

	# UnreachableStatement
    def test_unReach_Stat_01(self):
        inp = """
        void main(){
            return;
            0;
        }
        """
        out = "Unreachable Statement: " + str(IntLiteral(0))
        self.assertTrue(TestChecker.test(inp,out,449))
    def test_unReach_Stat_02(self):
        inp = """
        void main(){
            for(1;true;1){
                break;
                continue;
                2;
            }
            return;
        }"""
        out = "Unreachable Statement: " + str(Continue())
        self.assertTrue(TestChecker.test(inp,out,450))
    def test_unReach_Stat_03(self):
        inp = """
        void main(){ }
        int static_void_main(){
            int a,b;
            float result;
            if(a>b) a;
            else return a;
            do
                continue;
                if(a>1) return a; 
                else return b;
            while (true);
            return 1;
        }
        """
        out = "Unreachable Statement: " + str(If(BinaryOp(">",Id("a"),IntLiteral(1)),Return(Id("a")),Return(Id("b"))))
        self.assertTrue(TestChecker.test(inp,out,451))
    def test_unReach_Stat_04(self):
        inp = """
        void main(){
            do
                {continue;}
                {1;}
            while(true);
            return;
        }
        """
        out = "Unreachable Statement: "+str(Block([IntLiteral(1)]))
        self.assertTrue(TestChecker.test(inp,out,452))
    def test_unReach_Stat_05(self):
        inp = """
        void main(){ }
        float f;
        int checkOddNumber(int n){
            if(n%2==0)
                return n;
            else
                return checkOddNumber(n+1);
            n=1%n;
        }
        """
        out = "Unreachable Statement: "+str(BinaryOp("=",Id("n"),BinaryOp("%",IntLiteral(1),Id("n"))))
        self.assertTrue(TestChecker.test(inp,out,453))

    def test_typeMis_Exp_08(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[isTrue];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,454))
    def test_typeMis_Exp_09(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr["isTrue"];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),StringLiteral("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,455))
    def test_typeMis_Exp_10(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[foo()];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,456))
    def test_typeMis_Exp_11(self):
        inp = """
        int a[10];
        void main(){
            int a;
            a[10];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,457))
    def test_typeMis_Exp_12(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            string a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,458))
    def test_typeMis_Exp_13(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            float a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,459))
    def test_typeMis_Exp_14(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            boolean a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,460))
    def test_typeMis_Exp_15(self):
        inp = """
        int a[10],c;
        int foo(){
            int a;
            return a;
        }
        void main(){
            boolean a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            foo()[10];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,461)) 
    def test_typeMis_Exp_16(self):
        inp = """
        int a[10],b,arr;
        void main(){
            int iNum;
            float fNum;
            fNum = 1;
            iNum = fNum;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("iNum"),Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,462))
    def test_typeMis_Exp_17(self):
        inp =  """
        int a[10],b,arr;
        void main(){
            int iNum;
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("fNum"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,463))
    def test_typeMis_Exp_18(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            float fNum;
            boolean isTrue;
            isTrue = true;
            str = isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("str"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,464))
    def test_typeMis_Exp_19(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            a=arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("a"),Id("arr")))
        self.assertTrue(TestChecker.test(inp,out,465))
    def test_typeMis_Exp_20(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            arr = foo(iNum);
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("arr"),CallExpr(Id("foo"),[Id("iNum")])))
        self.assertTrue(TestChecker.test(inp,out,466))


 


    # Error: TypeMismatchInStatement
    def test_typeMis_Stat_01(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if(i){
                i = 0;
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(If(Id("i"),Block([BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,467)) 
    def test_typeMis_Stat_02(self):
        inp = """int a[10],c;
         void main(){
            int size;
            int i;
            if(10.5){
                i = 0;
            }
         }
        """
        out = "Type Mismatch In Statement: " + str(If(FloatLiteral(float(10.5)),Block([BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,468))
    def test_typeMis_Stat_03(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if("true"){
                i = 0;
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(If(StringLiteral("true"),Block([BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,469))
    def test_typeMis_Stat_04(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            for(true; i< 10; i= i+1){
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BooleanLiteral(True),BinaryOp("<",Id("i"),IntLiteral(int(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])))
        self.assertTrue(TestChecker.test(inp,out,470))
    def test_typeMis_Stat_05(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(j = 14.3; i< 10; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("j"),FloatLiteral(float(14.3))),BinaryOp("<",Id("i"),IntLiteral(int(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(int(1)))),Block([])))
        self.assertTrue(TestChecker.test(inp,out,471))
    def test_typeMis_Stat_06(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(i=1; i = size +10; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("size"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])))
        self.assertTrue(TestChecker.test(inp,out,472))
    def test_typeMis_Stat_07(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
        for(i=1; j = 10.5; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("j"),FloatLiteral(float(10.5))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])))
        self.assertTrue(TestChecker.test(inp,out,473))
    def test_typeMis_Stat_08(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(i=1; i < 10; 14.3){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),FloatLiteral(float(14.3)),Block([])))
        self.assertTrue(TestChecker.test(inp,out,474))
    def test_typeMis_Stat_09(self):
        inp = """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        do{
         i = i + 1;
        }while(i);
        }
        """
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],Id("i")))
        self.assertTrue(TestChecker.test(inp,out,475))
    def test_typeMis_Stat_10(self):
        inp = """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        do{
         i = i + 1;
        }while("false");
        }"""
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],StringLiteral("false")))
        self.assertTrue(TestChecker.test(inp,out,476))
    def test_typeMis_Stat_11(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            do{
                i = i + 1;
            }while(15.10);
        }
        """
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],FloatLiteral(float(15.1))))
        self.assertTrue(TestChecker.test(inp,out,477))
    def test_typeMis_Stat_12(self):
        inp =  """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        return i;
        }"""
        out = "Type Mismatch In Statement: " + str(Return(Id("i")))
        self.assertTrue(TestChecker.test(inp,out,478))
    def test_typeMis_Stat_13(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            return "void";
        }
        """
        out = "Type Mismatch In Statement: " + str(Return(StringLiteral("void")))
        self.assertTrue(TestChecker.test(inp,out,479))
    def test_typeMis_Stat_14(self):
        inp =  """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return 10.6;
        }
        void main(){}
        """
        out = "Type Mismatch In Statement: " + str(Return(FloatLiteral(float(10.6))))
        self.assertTrue(TestChecker.test(inp,out,480))
    def test_typeMis_Stat_15(self):
        inp = """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return true;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(BooleanLiteral(True)))
        self.assertTrue(TestChecker.test(inp,out,481))
    def test_typeMis_Stat_16(self):
        inp = """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return;
        }
        void main(){ complex();}
      """
        out = "Type Mismatch In Statement: " + str(Return(None))
        self.assertTrue(TestChecker.test(inp,out,482))





	# FunctionNotReturn
    def test_notRet_Func_01(self):
        inp = """
        void main(){ foo(1); }
        int foo(int a){ }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,483))
    def test_notRet_Func_02(self):
        inp = """
        void main(){ foo(1,1); }
        int foo(int a,float b){
            if(true){ } 
            else {
                return 2;
            } 
        }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,484)) 
    def test_notRet_Func_03(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            int x;
            do
                x=0;
            while(true);
        }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,485))
    def test_notRet_Func_04(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) return 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,486))
    def test_notRet_Func_05(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) 1; 
            else return 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,487))
    def test_notRet_Func_06(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) 1; 
            else 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,488))
    def test_notRet_Func_07(self):
        inp = """
        void main(){ foo(3); }
        int foo(int b){
            for(1;true;1) return 1;
        }
        """
        out =  "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,489))
    def test_notRet_Func_08(self):
        inp =  """
        void main(){ foo(2); }
        int foo(int a){
            a = 1;
        }
        """  
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,490))
    def test_notRet_Func_09(self):
        inp = """
        string getString(){return "Abc";}
        void func(){ }
        void main(){
            func();
            getString();
            haha();
        }
        boolean haha(){ }
        """
        out = "Function haha Not Return "
        self.assertTrue(TestChecker.test(inp,out,491))

    def test_typeMis_Exp_01(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_typeMis_Exp_02(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_typeMis_Exp_03(self):
       """More complex program"""
       input = """void main () {
           putIntLn();
        }"""
       expect = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"),[]))
       self.assertTrue(TestChecker.test(input,expect,494))  
    def test_typeMis_Exp_04(self):
       """More complex program"""
       input = """void main () {
           putIntLn(getInt(4));
       }"""
       expect = "Type Mismatch In Expression: " + str(CallExpr(Id("getInt"),[IntLiteral(4)]))
       self.assertTrue(TestChecker.test(input,expect,495)) 
    def test_typeMis_Exp_05(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("getInt"),[IntLiteral(4)]))
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_typeMis_Exp_06(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"),[]))
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_typeMis_Exp_07(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[fNum];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,498))

    def test_break_not_in_loop1(self):
        """ Break Not In Loop """
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,499))

    