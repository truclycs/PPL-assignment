import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program"""
        input = r"""int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program2(self):
        """Simple program"""
        input = r"""int main(){
                   int a;
                   }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_simple_program3(self):
        """Simple program"""
        input = r"""
                    float a;
                    int b;
                    boolean d;
                    string e;
                """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",IntType()),VarDecl("d",BoolType()),VarDecl("e",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_simple_program4(self):
        """Simple program"""
        input = r"""
                    int a[5];
                    float b[5];
                    string c[5];
                    boolean d[5];
                """
        expect = str(Program([VarDecl("a",ArrayType(5,IntType())),VarDecl("b",ArrayType(5,FloatType())),VarDecl("c",ArrayType(5,StringType())),VarDecl("d",ArrayType(5,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_simple_program5(self):
        """Simple program"""
        input = r"""
                    int main(){}
                    float main(){}
                    void main(){}
                    boolean main(){}
                    string main(){}
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("main"),[],FloatType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],BoolType(),Block([])),FuncDecl(Id("main"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_var_decl1(self):
        """ Test Variable Declare """
        input = r"""int[] main(){}
                    float[] main(){}
                    string[] main(){}
                    boolean[] main(){}
        """
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("main"),[],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("main"),[],ArrayPointerType(StringType()),Block([])),FuncDecl(Id("main"),[],ArrayPointerType(BoolType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_var_decl2(self):
        """ Test Variable Declare """
        input = r"""
                    int a[5],b[5],c[5];
        """
        expect = str(Program([VarDecl("a",ArrayType(5,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(5,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_var_decl3(self):
        """ Test Variable Declare """
        input = r"""int a,b[5];
                   float c,d[5];
                   """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",FloatType()),VarDecl("d",ArrayType(5,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_var_decl4(self):
        """ Test Variable Declare """
        input = r"""float a[1], b[2], c[3], d[4];"""
        expect = str(Program([VarDecl("a",ArrayType(1,FloatType())),VarDecl("b",ArrayType(2,FloatType())),VarDecl("c",ArrayType(3,FloatType())),VarDecl("d",ArrayType(4,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_var_decl5(self):
        """ Test Variable Declare """
        input = r"""int a,b,c,d;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    
    def test_var_decl6(self):
        """ Test Variable Declare """
        input = r"""int a[5], b[5], c[5], d[5];
        """
        expect = str(Program([VarDecl("a",ArrayType(5,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(5,IntType())),VarDecl("d",ArrayType(5,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_function_decl1(self):
        """ Test Function Declare """
        input = r"""int main(int a){

        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    
    def test_function_decl2(self):
        """ Test Function Declare """
        input = r"""int main(int a, float b){

        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_function_decl3(self):
        """ Test Function Declare """
        input = r"""int main(int a[]){

        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_function_decl4(self):
        """ Test Function Declare """
        input = r"""int main(int a[],int b[]){

        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(IntType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_function_decl5(self):
        """ Test Function Declare """
        input = r"""int main(int a[]){
            int a,b,c;
        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType))],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    def test_function_decl6(self):
        """ Test Function Declare """
        input = r"""int[] main(int a, float b){
            int a;
            float b;
            string c;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],ArrayTypePointer(IntType),Block([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,StringType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_function_decl7(self):
        """ Test Function Declare """
        input = r"""float[] main(string a, boolean b){
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,StringType),VarDecl(b,BoolType)],ArrayTypePointer(FloatType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    
    def test_function_decl8(self):
        """ Test Function Declare """
        input = r"""string[] main(string a, string b[]){
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,StringType),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(StringType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    
    def test_If_stm_1(self):
        """ Test If Statement """
        input = r"""int main(){
            if (a==b) return 1;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(a),Id(b)),Return(IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_If_stm_2(self):
        """ Test If Statement """
        input = r"""int main(){
            if(a==b) return 1; else return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(a),Id(b)),Return(IntLiteral(1)),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_If_stm_3(self):
        """ Test If Statement """
        input = r"""int main(){
            if(a==b){
                if(a>c){                 
                }
            }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(a),Id(b)),Block([If(BinaryOp(>,Id(a),Id(c)),Block([]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_If_stm_4(self):
        """ Test If Statement """
        input = r"""int main(){
            if(x==y){
                x=x+1;
            }
            else
            {
                if(x==2) return 0;
            }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(x),Id(y)),Block([BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)))]),Block([If(BinaryOp(==,Id(x),IntLiteral(2)),Return(IntLiteral(0)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_do_while_1(self):
        """ Test Dowhile statement """
        input = r"""int main(){
            do a=2; while a>1;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(a),IntLiteral(2))],BinaryOp(>,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_Continue_1(self):
        """ Test Continue"""
        input = r"""int main(){
            continue;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_Break_1(self):
        """ Test Break """
        input = r"""int main(){break;}
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_return_1(self):
        """ Test return """
        input = r"""int main(){
            return;}
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_return_2(self):
        """ Test return """
        input = r"""int main(){
            return x;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(Id(x))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_return_3(self):
        """ Test return"""
        input = r"""int main(){
            return 5;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_return_4(self):
        """ Test return """
        input = r"""int main(){
            return x();
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(CallExpr(Id(x),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_return_5(self):
        """ Test return """
        input = r"""int main(){
            return x%2;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(%,Id(x),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_For_1(self):
        """ Test For Statement """
        input = r"""int main(){
            for(i=0;i<10;i=i+1)
                continue;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_For_2(self):
        """ Test For Statement """
        input = r"""int main(){
            for(x;y;z) {
                x=y;
            }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(Id(x);Id(y);Id(z);Block([BinaryOp(=,Id(x),Id(y))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_For_3(self):
        """ Test For Statement """
        input = r"""int main(){
            for(i=0;i<10;i=i+1){
                if(i%2==0) result=1;
            }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(result),IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_For_4(self):
        """ Test For Statement """
        input = r"""int main(){
            for(x;y;z)
                for(a;b;c){
                }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(Id(x);Id(y);Id(z);For(Id(a);Id(b);Id(c);Block([])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_For_5(self):
        """ Test For Statement """
        input = r"""int main(){
            for(i=0;i<10;i=i+1)
                for(j=0;j<10;j=j+1)
                    for(k=0;k<10;k=k+1)
                        r=r+1;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(10));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));For(BinaryOp(=,Id(k),IntLiteral(0));BinaryOp(<,Id(k),IntLiteral(10));BinaryOp(=,Id(k),BinaryOp(+,Id(k),IntLiteral(1)));BinaryOp(=,Id(r),BinaryOp(+,Id(r),IntLiteral(1))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_For_6(self):
        """ Test For Statement """
        input = r"""
            void main(){
            int x,y;
            for (x=0; x < 10; x=x+1)
                y = y + 1;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(x,IntType),VarDecl(y,IntType),For(BinaryOp(=,Id(x),IntLiteral(0));BinaryOp(<,Id(x),IntLiteral(10));BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)));BinaryOp(=,Id(y),BinaryOp(+,Id(y),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_For_7(self):
        """ Test For Statement """
        input = r"""
            int main(){
                int d;
                d=0;
                for (i=1; i < 10; a=a+1){
                    if (i%2==0){
                        d=d+1;
                    }
                }
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(d,IntType),BinaryOp(=,Id(d),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_Exp_1(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
               x=x+1;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_Exp_2(self):
        """ Test Exp Statement """
        input = r"""
                int main(){
                   x=x%2;
                }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(x),BinaryOp(%,Id(x),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_Exp_3(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                int a;
                a=a-1;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_Exp_4(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                int a;
                a=a%1;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(%,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_Exp_5(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                int a;
                a=a || true;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(||,Id(a),BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_Exp_6(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                int a;
                int b;
                a=a*b;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),BinaryOp(=,Id(a),BinaryOp(*,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_Exp_7(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                a==b;
                c!=d;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(d))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_Exp_8(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                a*b;
                c/d;
                e%f;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(*,Id(a),Id(b)),BinaryOp(/,Id(c),Id(d)),BinaryOp(%,Id(e),Id(f))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_Exp_9(self):
        """ Test Exp Statement """
        input = r"""
            int main(){
                -a;
                !b;
                c [5];
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([UnaryOp(-,Id(a)),UnaryOp(!,Id(b)),ArrayCell(Id(c),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_Func_call_1(self):
        """ Test Func call Statement """
        input = r"""
            int main(){
                a(b(c()));
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(a),[CallExpr(Id(b),[CallExpr(Id(c),[])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_Func_call_2(self):
        """ Test For Statement """
        input = r"""
            int main(){
                a(1,2,3,4);
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(a),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_Func_call_3(self):
        """ Test For Statement """
        input = r"""
            int main(){
                a(1.5,true,false);
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(a),[FloatLiteral(1.5),BooleanLiteral(true),BooleanLiteral(false)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_Exp_10(self):
        """ Test For Statement """
        input = r"""
            int main(){
                a=(b+a)*(b-a);
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(*,BinaryOp(+,Id(b),Id(a)),BinaryOp(-,Id(b),Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_Exp_11(self):
        """ Test Expr Statement """
        input = r"""
            int main(){
                a=(a||b)&&c||d;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(||,Id(a),Id(b)),Id(c)),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_Dowhile_2(self):
        """ Test Do-while Statement """
        input = r"""int main(){
            do 
                if (x%2==0) a=a+1;
                if (b==10) break;
            while(true);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([If(BinaryOp(==,BinaryOp(%,Id(x),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),If(BinaryOp(==,Id(b),IntLiteral(10)),Break())],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_Do_while_3(self):
        """ Test Do-while Statement """
        input = r"""
            int main(){
                do
                    for(x;y;z) continue;
                while true;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([For(Id(x);Id(y);Id(z);Continue())],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_Do_while_4(self):
        """ Test Do-while Statement """
        input = r"""
            int main(){
                do
                    for(x;y;z) if(x==1) continue;
                    if(x==2) return;
                while true;
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([For(Id(x);Id(y);Id(z);If(BinaryOp(==,Id(x),IntLiteral(1)),Continue())),If(BinaryOp(==,Id(x),IntLiteral(2)),Return())],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_Break_2(self):
        """ Test Break Statement """
        input = r"""void main() {
            for(i=0;i<10;i = i*2) break;
            }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2)));Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_Continue_(self):
        """ Test Continue Statement """
        input = r"""int main() {          
                for (x;y;z){
                    if(a==10) continue;
                }
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(Id(x);Id(y);Id(z);Block([If(BinaryOp(==,Id(a),IntLiteral(10)),Continue())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_return_7(self):
        """ Test Return Statement """
        input = r"""int main(){
            int x;
            x=3;
            if(x==3)
            return "123";
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,IntType),BinaryOp(=,Id(x),IntLiteral(3)),If(BinaryOp(==,Id(x),IntLiteral(3)),Return(StringLiteral(123)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_Expr(self):
        """ Test Expr Statement """
        input = r"""int main(){
              a=a+1;
              b=b+2;
              c=c+3;
              a=a*b*(c+123)/2;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2))),BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(3))),BinaryOp(=,Id(a),BinaryOp(/,BinaryOp(*,BinaryOp(*,Id(a),Id(b)),BinaryOp(+,Id(c),IntLiteral(123))),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_Stm1(self):
        """ Test Expr Statement """
        input = r"""int main(){
              do 
                if(x%2==0)
                    for(i=0;i<10;i=i+1){}
              while (x>10);
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([If(BinaryOp(==,BinaryOp(%,Id(x),IntLiteral(2)),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([])))],BinaryOp(>,Id(x),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    def test_stm2(self):
        """ Test Expression """
        input = r"""int main(){
            do
                do x=x+1;
                while true;
            while true;

        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Dowhile([BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)))],BooleanLiteral(true))],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_stm3(self):
        """ Test statement """
        input = r"""int main(int c){
            for(a;b;c)
            for(x;y;z)
            for(j;q;k){}
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(c,IntType)],IntType,Block([For(Id(a);Id(b);Id(c);For(Id(x);Id(y);Id(z);For(Id(j);Id(q);Id(k);Block([]))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_stm4(self):
        """ Test statement """
        input = r"""int main(){
               do for(i=5;i<10;i=i+1){
                   if(i%2==0) x=x+1;
               }
               while (x>0);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([For(BinaryOp(=,Id(i),IntLiteral(5));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1))))]))],BinaryOp(>,Id(x),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_stm5(self):
        """ Test statement """
        input = r"""int main(){
            for(i=0;i<1;i=i+1){

                do if(x!=0) x=x+1;
                while x<10;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([Dowhile([If(BinaryOp(!=,Id(x),IntLiteral(0)),BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1))))],BinaryOp(<,Id(x),IntLiteral(10)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_exp(self):
        """ Test Expression """
        input = r"""int main(){
            int x;
            x=(1-5)+((3/4)+(5+6));
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,IntType),BinaryOp(=,Id(x),BinaryOp(+,BinaryOp(-,IntLiteral(1),IntLiteral(5)),BinaryOp(+,BinaryOp(/,IntLiteral(3),IntLiteral(4)),BinaryOp(+,IntLiteral(5),IntLiteral(6))))),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_exp0(self):
        """ Test Expression """
        input = r"""int main(){
            a = (a||b)*((a||c)+(a&&c));
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(*,BinaryOp(||,Id(a),Id(b)),BinaryOp(+,BinaryOp(||,Id(a),Id(c)),BinaryOp(&&,Id(a),Id(c)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_exp1(self):
        """ Test Expression """
        input = r"""int main(){
            s=(a+b)*(-c*(d-e));
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(s),BinaryOp(*,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,UnaryOp(-,Id(c)),BinaryOp(-,Id(d),Id(e)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_exp2(self):
        """ Test Expression """
        input = r"""void main(){
            s= true&&true||false;
            prinf(a);
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(s),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(true)),BooleanLiteral(false))),CallExpr(Id(prinf),[Id(a)]),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_exp3(self):
        """ Test Expression """
        input = r"""int main(){
            int a[5];
            prinf(a[2+1]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,5)),CallExpr(Id(prinf),[ArrayCell(Id(a),BinaryOp(+,IntLiteral(2),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_exp4(self):
        """ Test Expression """
        input = r"""int main(){
            x[x];
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(x),Id(x))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
    def test_exp5(self):
        """ Test Expression """
        input = r"""int main(){
            x[x[5+1]];
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(x),ArrayCell(Id(x),BinaryOp(+,IntLiteral(5),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    
    def test_exp6(self):
        """ Test Expression """
        input = r"""int main(){
            float a,b;
            x=a+b/2*5-3;
            y=x+a*b/5||0;
            return (x+y);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,Id(a),BinaryOp(*,BinaryOp(/,Id(b),IntLiteral(2)),IntLiteral(5))),IntLiteral(3))),BinaryOp(=,Id(y),BinaryOp(||,BinaryOp(+,Id(x),BinaryOp(/,BinaryOp(*,Id(a),Id(b)),IntLiteral(5))),IntLiteral(0))),Return(BinaryOp(+,Id(x),Id(y)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    
    def test_exp7(self):
        """ Test Expression """
        input = r"""void main(){
            string a,b,c;
            a= "1";
            b="2222";
            c="3333";
            printf (a);
            printf (b);
            printf (c);
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(c,StringType),BinaryOp(=,Id(a),StringLiteral(1)),BinaryOp(=,Id(b),StringLiteral(2222)),BinaryOp(=,Id(c),StringLiteral(3333)),CallExpr(Id(printf),[Id(a)]),CallExpr(Id(printf),[Id(b)]),CallExpr(Id(printf),[Id(c)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    def test_exp8(self):
        """ Test Expression """
        input = r"""void main(){
            boolean a,b,c;
            printf(a[2]+a[1]+q());
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,BoolType),VarDecl(b,BoolType),VarDecl(c,BoolType),CallExpr(Id(printf),[BinaryOp(+,BinaryOp(+,ArrayCell(Id(a),IntLiteral(2)),ArrayCell(Id(a),IntLiteral(1))),CallExpr(Id(q),[]))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_exp9(self):
        """ Test Expression """
        input = r"""int main(){
            (a/2)*5%3&&32+2343242;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(&&,BinaryOp(%,BinaryOp(*,BinaryOp(/,Id(a),IntLiteral(2)),IntLiteral(5)),IntLiteral(3)),BinaryOp(+,IntLiteral(32),IntLiteral(2343242)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_exp10(self):
        """ Test Expression """
        input = r"""int main(){
            a[2]/q(30)+s(50)*a[5];
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,BinaryOp(/,ArrayCell(Id(a),IntLiteral(2)),CallExpr(Id(q),[IntLiteral(30)])),BinaryOp(*,CallExpr(Id(s),[IntLiteral(50)]),ArrayCell(Id(a),IntLiteral(5))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_complex(self):
        """ Test Complex """
        input = r"""void main(){
            int a;
            int b;
            return(a+b);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),Return(BinaryOp(+,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    
    def test_complex_1(self):
        """ Test complex """
        input = r"""int main(int a,int b){
           return abc();
        }
        void abc(){
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,IntType)],IntType,Block([Return(CallExpr(Id(abc),[]))])),FuncDecl(Id(abc),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    def test_complex_2(self):
        """ Test complex """
        input = r"""int main () {
            int a,b,c;
            a=b+c;
            b=c+a;
            c=b+a;
            return q(a,b,c);
        }
        int q(){}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c))),BinaryOp(=,Id(b),BinaryOp(+,Id(c),Id(a))),BinaryOp(=,Id(c),BinaryOp(+,Id(b),Id(a))),Return(CallExpr(Id(q),[Id(a),Id(b),Id(c)]))])),FuncDecl(Id(q),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    def test_complex_3(self):
        """ Test complex """
        input = r"""void main(){
            float a,b;
            string a[5];
            if(a==1) return b;
            if(b==2) return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(a,ArrayType(StringType,5)),If(BinaryOp(==,Id(a),IntLiteral(1)),Return(Id(b))),If(BinaryOp(==,Id(b),IntLiteral(2)),Return(Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    def test_complex_4(self):
        """ Test complex """
        input = r"""int main(){
            int x;
            print("string");
            do 
                print("x");
            while (i!=0);
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,IntType),CallExpr(Id(print),[StringLiteral(string)]),Dowhile([CallExpr(Id(print),[StringLiteral(x)])],BinaryOp(!=,Id(i),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_complex_5(self):
        """ Test complex """
        input = r"""int main(){
            int i;
            i=0;
            if (i == 0)
                return 1;
            else
                return f(x);
        }
        int f(){
            int i;i=0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0)),If(BinaryOp(==,Id(i),IntLiteral(0)),Return(IntLiteral(1)),Return(CallExpr(Id(f),[Id(x)])))])),FuncDecl(Id(f),[],IntType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    def test_complex_6(self):
        """ Test complex """
        input = r"""int main(){
            a();
            b();
            c();
        }
        int a(){
        }
        int b(){
        }
        int c(){
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(a),[]),CallExpr(Id(b),[]),CallExpr(Id(c),[])])),FuncDecl(Id(a),[],IntType,Block([])),FuncDecl(Id(b),[],IntType,Block([])),FuncDecl(Id(c),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    
    def test_complex_7(self):
        """ Test complex"""
        input = r"""
        int main(){
            a(b);
            b(a);
        }
        int a(int b){}
        int b(int a){}
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(a),[Id(b)]),CallExpr(Id(b),[Id(a)])])),FuncDecl(Id(a),[VarDecl(b,IntType)],IntType,Block([])),FuncDecl(Id(b),[VarDecl(a,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    
    def test_complex_8(self):
        """ Test complex """
        input = r"""void main(){
            int a,b;
            if(a==0) return q(b);
            else return q(a);
            }        
        int q(boolean x){
            if(x==0) return 1;
            if(x==1) return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),If(BinaryOp(==,Id(a),IntLiteral(0)),Return(CallExpr(Id(q),[Id(b)])),Return(CallExpr(Id(q),[Id(a)])))])),FuncDecl(Id(q),[VarDecl(x,BoolType)],IntType,Block([If(BinaryOp(==,Id(x),IntLiteral(0)),Return(IntLiteral(1))),If(BinaryOp(==,Id(x),IntLiteral(1)),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    
    def test_complex_9(self):
        """ Test complex """
        input = r"""int main()
        {
            int a,b,c,d;
            do 
                a=0;
                b=1;
                c=2;
            while (d==0);
            if(a==0) 
            return true;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(d,IntType),Dowhile([BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(b),IntLiteral(1)),BinaryOp(=,Id(c),IntLiteral(2))],BinaryOp(==,Id(d),IntLiteral(0))),If(BinaryOp(==,Id(a),IntLiteral(0)),Return(BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_complex10(self):
        """ Test complex """
        input = r"""int main()
            {
                int d;
                for(i=0;i<10;i=i+1)
                for(j=0;j<10;j=j+1)
                for(k=0;k<10;k=k+1)
                d=d+1;
                return 0;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(d,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(10));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));For(BinaryOp(=,Id(k),IntLiteral(0));BinaryOp(<,Id(k),IntLiteral(10));BinaryOp(=,Id(k),BinaryOp(+,Id(k),IntLiteral(1)));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)))))),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_complex11(self):
        """ Test complex """
        input = r"""int main()
            {
                if(a==0)
                if(b==0)
                if(c==0) return 1;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(0)),If(BinaryOp(==,Id(b),IntLiteral(0)),If(BinaryOp(==,Id(c),IntLiteral(0)),Return(IntLiteral(1)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    
    def test_complex12(self):
        """ Test complex """
        input = r"""int main()
            {
                float a,b,c,d;
                float result;
                result=1;
                do {
                    result=result+1;
                }while (result<10);
                return function(result);
            }
            int function(int a){
                a=a+1;
                return a;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(d,FloatType),VarDecl(result,FloatType),BinaryOp(=,Id(result),IntLiteral(1)),Dowhile([Block([BinaryOp(=,Id(result),BinaryOp(+,Id(result),IntLiteral(1)))])],BinaryOp(<,Id(result),IntLiteral(10))),Return(CallExpr(Id(function),[Id(result)]))])),FuncDecl(Id(function),[VarDecl(a,IntType)],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    
    def test_complex13(self):
        """ Test complex """
        input = r"""int[] main()
            {
                for(i=0;i<10;i=i+1){
                    int x;x=1;
                    do x=x+1;
                    while (x<10);
                }
            }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([VarDecl(x,IntType),BinaryOp(=,Id(x),IntLiteral(1)),Dowhile([BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)))],BinaryOp(<,Id(x),IntLiteral(10)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    
    def test_complex14(self):
        """ Test complex """
        input = r"""
            int recurse(int x){
                if(x!=0) return 1+recurse(x-1); else return 0;
            }"""
        expect = "Program([FuncDecl(Id(recurse),[VarDecl(x,IntType)],IntType,Block([If(BinaryOp(!=,Id(x),IntLiteral(0)),Return(BinaryOp(+,IntLiteral(1),CallExpr(Id(recurse),[BinaryOp(-,Id(x),IntLiteral(1))]))),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_complex15(self):
        """ Test complex """
        input = r"""
            int main(){
                int x;
                x=10;
                if(x!=0)
                return recurse(x);
            }
            int recurse(int x){
                if(x!=0) return 1+recurse(x-1); else return 0;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,IntType),BinaryOp(=,Id(x),IntLiteral(10)),If(BinaryOp(!=,Id(x),IntLiteral(0)),Return(CallExpr(Id(recurse),[Id(x)])))])),FuncDecl(Id(recurse),[VarDecl(x,IntType)],IntType,Block([If(BinaryOp(!=,Id(x),IntLiteral(0)),Return(BinaryOp(+,IntLiteral(1),CallExpr(Id(recurse),[BinaryOp(-,Id(x),IntLiteral(1))]))),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    
    def test_complex16(self):
        """ Test complex """
        input = r"""
            int main(){
                for(i=1;i<10;i=i+1){
                    int x;
                    x=recurse(i);
                }
            }
            int recurse(int x){
                if(x!=0) return 1+recurse(x-1); else return 0;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([VarDecl(x,IntType),BinaryOp(=,Id(x),CallExpr(Id(recurse),[Id(i)]))]))])),FuncDecl(Id(recurse),[VarDecl(x,IntType)],IntType,Block([If(BinaryOp(!=,Id(x),IntLiteral(0)),Return(BinaryOp(+,IntLiteral(1),CallExpr(Id(recurse),[BinaryOp(-,Id(x),IntLiteral(1))]))),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    
    def test_complex17(self):
        """ Test complex """
        input = r"""
            int main(){
                for(i=1;i<10;i=i+1){
                    int x;
                    x=recurse1(i);
                }
            }
            int recurse1(int x){
                if(x!=0) return 1+recurse1(x-1); else return 0;
            }
            int recurse2(int x){
                if(x!=1) return 2+recurse2(x-2); else return 1;
            }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([VarDecl(x,IntType),BinaryOp(=,Id(x),CallExpr(Id(recurse1),[Id(i)]))]))])),FuncDecl(Id(recurse1),[VarDecl(x,IntType)],IntType,Block([If(BinaryOp(!=,Id(x),IntLiteral(0)),Return(BinaryOp(+,IntLiteral(1),CallExpr(Id(recurse1),[BinaryOp(-,Id(x),IntLiteral(1))]))),Return(IntLiteral(0)))])),FuncDecl(Id(recurse2),[VarDecl(x,IntType)],IntType,Block([If(BinaryOp(!=,Id(x),IntLiteral(1)),Return(BinaryOp(+,IntLiteral(2),CallExpr(Id(recurse2),[BinaryOp(-,Id(x),IntLiteral(2))]))),Return(IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    
    def test_complex18(self):
        """ Test complex """
        input = r"""
        int main(){
            q(a());
            for(i=0;i<10;i=i+1){
                x=x*5+(4-1);
                y=y*4*4*3/2;
            }
        }

        void a(){
            return 1;
        }

        int q(){
            return 1;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(q),[CallExpr(Id(a),[])]),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(x),BinaryOp(+,BinaryOp(*,Id(x),IntLiteral(5)),BinaryOp(-,IntLiteral(4),IntLiteral(1)))),BinaryOp(=,Id(y),BinaryOp(/,BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(y),IntLiteral(4)),IntLiteral(4)),IntLiteral(3)),IntLiteral(2)))]))])),FuncDecl(Id(a),[],VoidType,Block([Return(IntLiteral(1))])),FuncDecl(Id(q),[],IntType,Block([Return(IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    
    def test_complex19(self):
        """ Test complex """
        input = r"""
        int main() {
            int i,j;
            for(i = 1; i <= 10; i = i + 1) {
                for(j=1;j <= 10; j = j + 1)
                    printf(j);
                printf(i);
            }
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),IntLiteral(10));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));CallExpr(Id(printf),[Id(j)])),CallExpr(Id(printf),[Id(i)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
    def test_complex20(self):
        """ Test complex """
        input = r"""
        int main() {
            if(x<=y){
                x=x*2;
            }
            else{
                if(x>=z){
                    x=x-2;
                }
                else{
                    if(x<=10){
                        x=x+1;
                    }
                }
            }
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<=,Id(x),Id(y)),Block([BinaryOp(=,Id(x),BinaryOp(*,Id(x),IntLiteral(2)))]),Block([If(BinaryOp(>=,Id(x),Id(z)),Block([BinaryOp(=,Id(x),BinaryOp(-,Id(x),IntLiteral(2)))]),Block([If(BinaryOp(<=,Id(x),IntLiteral(10)),Block([BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)))]))]))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_complex21(self):
        """ Test complex """
        input = r"""
        int main() {
            int a,b;
            do a=a+b; while (a<100);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(b)))],BinaryOp(<,Id(a),IntLiteral(100)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    
    def test_complex22(self):
        """ Test complex """
        input = r"""
        int main() { 
            for(i=0;i<10;i=i+1)
                if(i%2==0) printf(i);
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),CallExpr(Id(printf),[Id(i)]))),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    
    def test_complex23(self):
        """ Test complex """
        input = r"""
        int main() {
            int a,b;
            a=1;b=2;
            if(a<b)
                for(i=0;a<=b;i=i+1){
                    a=a+1;
                }
            else{
                for(i=0;b<=a;i=i+1){
                    a=a-1;
                }
            }
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),IntLiteral(2)),If(BinaryOp(<,Id(a),Id(b)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(a),Id(b));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])),Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(b),Id(a));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)))]))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
