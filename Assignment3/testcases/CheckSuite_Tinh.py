import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    #---Test Redeclared Variable/Function/Parameter
        
    def test0_RedeclaredVariable(self):
        """Redeclared Variable a"""
        input = """
        int main(){
            int a;
            {
                float a;
            }
            boolean a;
            return 0;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test1_RedeclaredVariable(self):
        """Redeclared Variable b"""
        input = """
        void main(float b){
            string b;
            return getInt();
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2_RedeclaredVariable(self):
        """Redeclared Variable main"""
        input = """
        boolean foo(boolean foo){
            return foo;
        }
        void main(){
            return ;
        }
        string main;
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test3_RedeclaredFunction(self):
        """Redeclared Function foo"""
        input = """
        boolean foo;
        int main(){
            return 0;
        }
        int foo(){
            return 0;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test4_RedeclaredFunction(self):
        """Redeclared Function a"""
        input = """
        int a(int b){
            return b;
        }
        string a(string b){
            return b;
        }
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test5_RedeclaredFunction(self):
        """Redeclared Function main"""
        input = """
        int main1, arr[69];
        float f;
        float main;
        string foo2(){ return "surprise";}
        int main(){
            return 0;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test6_RedeclaredFunction(self):
        """Redeclared Function foo2"""
        input = """
        int foo1, a;
        string foo2(){return "surprise";}
        int main(){
            return 0;
        }
        void foo2(){return;}
        """
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test7_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float a){return a+b;}
        int main(){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test8_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float b){return a+b;}
        int main(int a[], float a[]){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test9_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float b){return a+b;}
        int main(int a[], string a){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    #---Test Undeclared Identifier/Function
        
    def test10_UndeclaredIdentifier(self):
        """Undeclared Identifier: temp"""
        input = """
        int a[1], i;
        void main(){
            int i, a;
            for(i=1;i<10;i=i+1)
            {
                if(temp<10)
                    temp=temp+1;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: temp"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test11_UndeclaredIdentifier(self):
        """Undeclared Identifier: res"""
        input = """
        int foo(int a[])
        {
            return a[0];
        }
        float main(){
            int arr[10];
            float f;
            f = 0;
            do f=f+foo(arr); res=f+1; while (foo(arr)+f)<100;
            return f;
            }
        """
        expect = "Undeclared Identifier: res"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12_UndeclaredIdentifier(self):
        """Undeclared Identifier: exp"""
        input = """
        int a;
        float b;
        string c;
        int d[10];
        void main(){
            {
                if(exp)
                    return;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: exp"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test13_UndeclaredIdentifier(self):
        """Undeclared Identifier: somethingjustlikethis"""
        input = """
        void main()
        {
            {
                int a,b;
                boolean c,d;
                a = 10 ;
                b = 5;
                c = true;
                d = c == (a>b);
            }
            {
                somethingjustlikethis = a+b; 
            }
            return;
        }
        """
        expect = "Undeclared Identifier: somethingjustlikethis"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test14_UndeclaredIdentifier(self):
        """Undeclared Identifier: i"""
        input = """
        int[] foo()
        {
            int a[5];
            return a;
        }
        void main()
        {
            do
                foo();
            while i;
            return;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test15_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a, int b){ return a+b;}
        int main(){
                return a+b+foo2();
            }
        int a,b;
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16_UndeclaredFunction(self):
        """Undeclared Function: multi"""
        input = """
        void main(){
            string str;
            str = "Chery Chery Lady\\n";
            int a;
            a = multi(10);
            return;
        }
        """
        expect = "Undeclared Function: multi"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test17_UndeclaredFunction(self):
        """Undeclared Function: foo1"""
        input = """
        int foo()
            {
                return 1;
            }
        int main()
        {
            int a;
            a=foo();
            return foo1();
        }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test18_UndeclaredFunction(self):
        """Undeclared Function: convertBoolean"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(convertBoolean(a))
                return;
            else                
                return;
        }
        """
        expect = "Undeclared Function: convertBoolean"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test19_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a){
            if((a%2)==0)
                a=a+1;
            else
                do 
                    a=a-1;
                while a > 0;
            return a;
        }
        void main(){
            int a,b[10],i;
            a=10;
            for(i=0;i<10;i=i+1)
                b[i]=foo(a)+foo2(a);                
            return;
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,419))

    #---Test Type Mismatch In Statement
        
    def test20_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(a)
                return;
            else                
                return;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Return(),Return())"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test21_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        int foo(int a){
            if((a%2)+1.0)
                a=a+1;
            else
                return a+1;
            return a;
        }
        void main(){              
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,BinaryOp(%,Id(a),IntLiteral(2)),FloatLiteral(1.0)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            float b[10];
            foo(a,b);              
            return;
        }
        int[] foo(int a,float b[]) {
            int c[3];
            if(a*2) foo(a-1,b);
            else return c;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLiteral(2)),CallExpr(Id(foo),[BinaryOp(-,Id(a),IntLiteral(1)),Id(b)]),Return(Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test23_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            float i, temp;
            for(i=1.0;i<10;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),FloatLiteral(1.0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test24_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i=i+1;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i<10;1.1e-1)
                {
                    if(temp<10)
                        temp=temp+1;
                    i=i+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));FloatLiteral(0.11);Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1)))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test26_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Dowhile"""
        input = """
        int foo(int a[])
        {
            return a[0];
        }
        void main(){
            int arr[10];
            float f;
            f = 0;
            do 
                f=f+foo(arr); 
                f=f+1; 
            while (foo(arr)+f);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(f),BinaryOp(+,Id(f),CallExpr(Id(foo),[Id(arr)]))),BinaryOp(=,Id(f),BinaryOp(+,Id(f),IntLiteral(1)))],BinaryOp(+,CallExpr(Id(foo),[Id(arr)]),Id(f)))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test27_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Dowhile"""
        input = """
        int foo(int a){
            if((a%2)==0)
                a=a+1;
            else
                do a=a-1;
                while a = 0;
            return a;
        }
        void main(){
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)))],BinaryOp(=,Id(a),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test28_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Return"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(a==1)
                return true;
            else                
                return;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test29_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Return"""
        input = """
        int[] main(){
            float a[5];
            int b[5];
            if(true)
                return a;
            else
                return b;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,429))

    # ---Test Type Mismatch In Expression
        
    def test30_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        void main(){
            int a,b[10],i;
            a=10;
            for(i=1;i<=10;i=i+1)
                b[i-1.0];                
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(-,Id(i),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test31_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        void main(){
            int a,b[1];
            a=1;
            b[1.0]=a;                
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int foo(){
            return 1;
        }
        void main(){
                foo()[1]+1; 
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test33_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int[] foo(int a[]){
            return a;
        }
        void main(){
                int a[10];
                (foo(a)[1])[2]; 
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(ArrayCell(CallExpr(Id(foo),[Id(a)]),IntLiteral(1)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test34_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: BinaryOp"""
        input = """
        int main(){
            boolean boo; 
            boo=false;
            1-boo;
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),Id(boo))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test35_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: UnaryOp(!,Id(boo))"""
        input = """
        int main(){
            int boo; 
            boo=1;
            (!boo)&&(true);
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(boo))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test36_TypeMismatchInExpression(self):
        """Type Mismatch In Expression:  - boolean"""
        input = """
        int main(){
            boolean c;
            c=true;
            int i,a;
            i=a+3;
            if (i>0){
                int d;
                d=1;
                -c;
                putInt(d);
            }
            return i;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test37_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int[] + 1"""
        input = """
        int[] foo(int a,float b[]) {
                int c[3];
                if(a>0) 
                {
                    foo(a-1,b);
                    return c;
                }
                else return c;
        }
        void main(){
            int a;
            float b[10];
            a= 69;
            foo(a,b)+1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(foo),[Id(a),Id(b)]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test38_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = boolean"""
        input = """
        int main(){
            boolean c;
            int i;
            i=3;
            if (i>0){
                int d;
                d=true;
            }
            return i;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test39_TypeMismatchInExpression(self):
        """no error, test with expression"""
        input = """
        int main(){
            float a[6];
            int b[9];
            int c[69];
            a[1]=foo(2)[3]/(c[b[2]]+3.0);
            return b[0];
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test40_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = float"""
        input = """
        int main(){
            int a;
            float b;
            b = 69;
            a = b;        
        {
            return 0;
        }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test41_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: type of LHS is ArrayType"""
        input = """
        void main(){
            int a[69];
            a = 69;        
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(69))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: need two args in func f"""
        input = """
        int i;
        int f(int a, int b){
            return 200;
        }
        void main(){
            int test;
            test=f(test);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f),[Id(test)])"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test43_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: string hello -> boolean boo"""
        input = """
        int foo(boolean boo){
            return 69;
        }
        int main(){
            string hello;
            return foo(hello);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(hello)])"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test44_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: cann't pass int b[] to float b[]"""
        input = """
        int foo(int a[] , float b[]){
            return a[0]/a[1];
        }
        int main(){
            return foo(a,b);
        }
        int a[5], b[10];
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test45_TypeMismatchInExpression(self):
        """no error"""
        input = """
        int[] foo(int a[]){
            return a;
        }
        int main(){
            int arr[69];
            return foo(foo(foo(arr)))[1]/foo(foo(foo(arr)))[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test46_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: func'name = value"""
        input = """
        int foo(int a){
            return a;
        }
        void main(){
            foo = 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test47_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = void"""
        input = """
        int foo;
        void f(){
            return;
        }
        void main(){
            foo = f();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),CallExpr(Id(f),[]))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test48_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int foo;
        void main(){
            foo[1];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test49_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: float != float"""
        input = """
        void main(){
            int a,b;
            a=b=1;
            boolean boo;
            boo = foo(a,b);
            return;
        }
        boolean foo(float a, float b){
            if (a!=b)
                return true;
            else
                return false;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,449))

    #---Test Break/Continue not in loop
        
    def test50_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test51_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        int foo(){
            if (true)
                break;
            else return 1;
            return 0;
        }
        void main(){}
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        string hello(string str){
            return str;
        }
        int main(){
            hello("Hi");
            {{break;}}
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test53_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        void main(){
            if (true)
                {
                    {
                        if (false)
                            break;
                    }
                }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test54_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        boolean foo(){
            return true;
        }
        int foo1(){
            return 1;
        }
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test55_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test56_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        int foo(){
            if (true)
                continue;
            else return 1;
            return 0;
        }
        void main(){}
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test57_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        string hello(string str){
            return str;
        }
        int main(){
            hello("Hi");
            {{continue;}}
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test58_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            if (true)
                {
                    {
                        if (false)
                            continue;
                    }
                }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test59_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        boolean foo(){
            return true;
        }
        int foo1(){
            return 1;
        }
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))

    #---Test Function not return
        
    def test60_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            int a,b;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test61_FunctionNotReturn(self):
        """Function foo Not Return"""
        input = """
        void main(){}
        int foo(){}
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            if (true)
                return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test63_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            int i;
            for(i=1;i<69;i=i+1)
                return i;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test64_FunctionNotReturn(self):
        """no error"""
        input = """
        int main(){
            if(true)
                if(false)
                    return 1;
                else
                    return 0;
            else return 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    #---Test No Entry Point

    def test65_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int foo(){
            return 0;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int a,b;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test67_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int a;
        float b;
        boolean main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test68_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        void foo(){}
        int main;
        void f(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test69_NoEntryPoint(self):
        """Simple program: int main() {} """
        input = """
        int a;
        float main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,469))

    #---Test Unreachable function
        
    def test70_UnreachableFunction(self):
        """Unreachable Function: foo"""
        input = """
        int foo(){return 0;}
        void main()
        {
            return;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test71_UnreachableFunction(self):
        """Unreachable Function: foo"""
        input = """
        int foo(int a){
            if (a>0)
                return foo(a-1);
            else
                return 0;
        }
        void main()
        {
            return;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72_UnreachableFunction(self):
        """no error"""
        input = """
        int foo1()
        {
            foo2();
            return 1;
        }
        int foo2()
        {
            foo1();
            return 1;
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test73_UnreachableFunction(self):
        """no error"""
        input = """
        void foo1()
        {
            foo2();
        }
        void foo2()
        {
            foo3();
        }
        void foo3()
        {
            foo1();
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test74_UnreachableFunction(self):
        """Unreachable Function: foo1"""
        input = """
        void foo1()
        {
            foo2();
            foo3();
        }
        void foo2(){}
        void foo3(){}
        void main(){}
        """
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 474))

    #---Test Not Left Value

    def test75_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            1+1=2; 
        }
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test76_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(){ 
            return 0; 
        }
        void main(){
            foo()=1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test77_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int x;
        void main(){
            x+1=2;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test78_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            float arr[10];
            arr[0]+arr[1]=arr[2]+3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test79_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(int a){
            return a;
        }
        void main(){
            a+foo(a)=foo(a)+a;
        }
        int a;
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),CallExpr(Id(foo),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,479))

    #---Test More Complex Program
        
    def test80_True(self):
        """no error"""
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int test;
            test=f();
            putIntLn(test);
            {
                int i, test, f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);
            }
            putIntLn(test);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test81_UnreachableFunction(self):
        """Unreachable Function: rescursive"""
        input = """
        int x,y[8];
        int a,b,c;
        void main(){
            y[x+a+b*c];
        }
        void rescursive(int i,float z){
            boolean exp;
            int statement;
            exp =true;
            int x;
            int c;
            if(exp)
                statement;
            else
                return;
        }
        """
        expect = "Unreachable Function: rescursive"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82_MoreDecls(self):
        """no error"""
        input = """
        int main(){
            int a;
            {
                int a;
                {
                    int a;
                    return b;
                }
            }
        }
        int b;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test83(self):
        """int func return with float"""
        input = """
        int a,b,c;
        float d;
        int main(){
            if (a<b) 
                c=a; 
            else 
                if(c<b)
                    c=b;
                else
                    c=b;
            return d=a=b=c;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(=,Id(d),BinaryOp(=,Id(a),BinaryOp(=,Id(b),Id(c)))))"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test84_TypeMismatchInExpression(self):
        """use int in logic exp"""
        input = """
        int main(){
            boolean a,b,d,e,f;
            int c;
            a || b || c || d && e && f;
            return 1; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(||,Id(a),Id(b)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test85_MoreComplexReturn(self):
        """no error"""
        input = """
        int foo(){
            if(true)
            {
                int i;
                for(i=0;i<10;i=i+1)
                {
                    break;
                }
                return 1;
            }
            else
                do
                    if(true)
                        return 2;
                    else
                        return 3;
                while(true);
        }
        float main(){
            return foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test86_TestMoreComplexReturn(self):
        """No return in ThenStm"""
        input = """
        int foo(){
            if(true)
            {
                int i;
                for(i=0;i<10;i=i+1)
                {
                    break;
                }
                return 1;
            }
            else
                do
                    if(true)
                        foo();
                    else
                        return 3;
                while(true);
        }
        float main(){
            return foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test87_NotLeftValue(self):
        """Not Left Value: b+c"""
        input = """
        int foo(){
            return 0;
        }
        int main(){
            int a,b,c;
            return a=b+c=foo();
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test88_TypeMisMatchInExpressionUnaryOp(self):
        """ ! int """
        input = """
        int main()
        {
            int a,b,c;
            a = !b + -a;
            return a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test89_CallMoreFunc(self):
        """no error"""
        input = """
        int main(){
            do
            {
                {
                    if (b>c)
                        return a+1;
                    else
                        return b-1;                    
                }
            }
            {
                a+b;
            }
            while (a<5);
            foo();
            foo();
            foo();
            foo();
            return 1;
        }
        int a,b,c;
        void foo(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test90_ComplexProgram(self):
        """No error"""
        input = """
        int main(){
            return foo(a,b);
        }
        int foo(int a[], float b){
            if (a[0] == 0) 
                return a[0];
            else
            {
                return foo(a,b);
            }
        }
        int a[10];
        float b;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
        
    def test91_complexprogram(self):
        """no error"""
        input = """
        void printf(string str){}
        void scanf(float a){}
        string int2str(int a){ return "Kael99" ;}
        int main()
        {
            int i, n, t1, t2, nextTerm;
            printf("Enter the number of terms: ");
            scanf(n);
            printf("Fibonacci Series: ");
            for (i = 1; i <= n; i=i+1)
            {
                printf(int2str(t1));
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92_CompareWithFloat(self):
        """ number == float """
        input = """
        void printf(string str){}
        void scanf(float a){}
        int main()
        {
            float number;
            printf("Enter a number: ");
            scanf(number);
            if (number <= 0.0)
            {
                if (number == 0.0)
                    printf("You entered 0.");
                else
                    printf("You entered a negative number.");
            }
            else
                printf("You entered a positive number.");
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(number),FloatLiteral(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test93_complexprogram(self):
        """no error"""
        input = """
        int main()
        {
            int low, high, i, flag;
            do
            {
                flag = 0;
                for(i = 2; i <= low/2.0; i=i+1)
                {
                    if(low % i == 0)
                        {
                            flag = 1;
                            break;
                        }
                }
                if (flag == 0)
                    return low;
                low=low+1;
            }
            while (low < high);
            return 0;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
        
    def test94_complexprogram(self):
        """! float"""
        input = """
        int main()
        {   
            do
            {
                if(n1 > n2)
                    n1 = n1 - n2;
                else
                    n2 = n2 - n1;
            }
            while(n1!=n2);
            return foo(1);
        }
        int foo(float a){
            return !a;
        }
        int n1, n2; 
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test95_complexprogram(self):
        """float foo2 can not return in foo1"""
        input = """
        float main()
        {
            int n, i, sum;
            for(i=1; i <= n; i=i+1)
            {
                sum = sum+i;
            }
            return foo1();
        }
        int foo1(){
            return foo2();
        }
        float foo2(){
            return foo1();
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo2),[]))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test96_complexprogram(self):
        """no error"""
        input = """
        void getFibonacii(int a,int b, int n)
        {   
            int sum;
            if(n>0)
            {
                sum=a+b;
                a=b;
                b=sum;
                getFibonacii(a,b,n-1);
            }
        }
        int main()
        {
            n = 10;     
            a=0;        //first term
            b=1;        //second term

            //call function with (n-2) terms
            getFibonacii(a,b,n-2);  
            return 0;
        }
        int a,b,sum,n;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test97_complexprogram(self):
        """ int result = float getPower()"""
        input = """
        float getPower(int b,int p)
        {
            float result;
            if(p==0)
                return result;
            else 
            {
                result=b*(getPower(b,p-1));
                return result;
            }
        }
        int main()
        {
            int base,power;
            int result;     
            result=getPower(base,power);     
            return result;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(result),CallExpr(Id(getPower),[Id(base),Id(power)]))"
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test98_AllBuiltinFunction(self):
        """Simple program: int main() {} """
        input = """
        void main () {
            float a;
            a=getInt();
            putInt(69);
            putIntLn(96);
            a=getFloat();
            putFloat(69);
            putFloatLn(69.96);
            putBool(true&&false);
            putBoolLn(true||false);
            putString("Hello hello, can u hear me?");
            putStringLn("Hello hello, can u hear me?");
            putLn();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test99(self):
        """Type Mismatch In Expression: use var as func"""
        input = """
        int foo;
        void main()
        {
            foo(1);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,499))