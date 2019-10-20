import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
#VARDEC
	def test_vardec_0(self):
		input = """
		int a,b,c;
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	def test_vardec_1(self):
		input = """
		int a,b[5],c;
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	def test_vardec_2(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	def test_vardec_3(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,303))   
	def test_vardec_4(self):
		input = """
        boolean arrBool[5];
		"""
		expect = str(Program([VarDecl("arrBool",ArrayType(5,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,304))    
	def test_vardec_5(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
        boolean t,f,_t,_f;
        boolean arrBool[5];
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),VarDecl("t",BoolType()),VarDecl("f",BoolType()),VarDecl("_t",BoolType()),VarDecl("_f",BoolType()),VarDecl("arrBool",ArrayType(5,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,305))
	def test_vardec_6(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
        bool t,f,_t,_f;
        bool arrBool[5];
        int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
        bool t,f,_t,_f;
        bool arrBool[5];
        int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
        bool t,f,_t,_f;
        bool arrBool[5];
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	def test_vardec_7(self):
		input = """
		int a,b[500000],c;
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(500000,IntType())),VarDecl("c",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,307))

#FUNCDEC
	def test_fundec_1(self):
		input = """
		int main(){}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	def test_fundec_2(self):
		input = """
		int main() {\n fooo(1712281);}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("fooo"),[IntLiteral(1712281)])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,309))
	def test_funcdec_3(self):
		input = """
		void in(){
                fooo(1712281);
            }
            int[] foo(){}
        int main(){
                fooo("This is assigment 1");
            }
		"""
		expect = str(Program([FuncDecl(Id("in"),[],VoidType(),Block([CallExpr(Id("fooo"),[IntLiteral(1712281)])])),FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("fooo"),[StringLiteral("This is assigment 1")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,310))
	def test_funcdec_4(self):
		input = """
		void start(){
                int one;
            }
            boolean _boolVar;
        int main(){
                string str1, str2, str_arr3[5];
            }
		"""
		expect = str(Program([FuncDecl(Id("start"),[],VoidType(),Block([VarDecl("one",IntType())])),VarDecl("_boolVar",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,311))
	def test_funcdec_5(self):
		input = """
		float[] start(){
                int one;
            }
        boolean _boolVar;
        int main(){
                string str1, str2, str_arr3[5];
            }
		"""
		expect = str(Program([FuncDecl(Id("start"),[],ArrayPointerType(FloatType()),Block([VarDecl("one",IntType())])),VarDecl("_boolVar",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,312))
	def test_funcdec_6(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
		void start(){
                int one;
            }
        boolean _boolVar;
        int[] _main(){
                string str1, str2, str_arr3[5];
            }
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("start"),[],VoidType(),Block([VarDecl("one",IntType())])),VarDecl("_boolVar",BoolType()),FuncDecl(Id("_main"),[],ArrayPointerType(IntType()),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,313))   
	def test_funcdec_7(self):
		input = """
        int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
		void start(int a, float c){
                int one;
            }
        boolean _boolVar;
        int[] _main(boolean f){
                string str1, str2, str_arr3[5];
            }
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("start"),[VarDecl("a",IntType()),VarDecl("c",FloatType())],VoidType(),Block([VarDecl("one",IntType())])),VarDecl("_boolVar",BoolType()),FuncDecl(Id("_main"),[VarDecl("f",BoolType())],ArrayPointerType(IntType()),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,314))    
	def test_funcdec_8(self):
		input = """
		int[] _main(boolean f, boolean _id[], float a[]){
                string str1, str2, str_arr3[5];
            }
		"""
		expect = str(Program([FuncDecl(Id("_main"),[VarDecl("f",BoolType()),VarDecl("_id",ArrayPointerType(BoolType())),VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,315))
	def test_funcdec_9(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
        int[] _main(boolean f, boolean _id[], float a[]){
                string str1, str2, str_arr3[5];
				int a,b[5],c;
        		float _vi,_int[6];
        		string str, str[3], str[5], str[2];
            }
		float _vi,_int[6];
        string str, str[3], str[5], str[2];
		void start(int a, float c){
                int one;
            }
        boolean _boolVar;
        int[] main(boolean f){
            }
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("_main"),[VarDecl("f",BoolType()),VarDecl("_id",ArrayPointerType(BoolType())),VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("str1",StringType()),VarDecl("str2",StringType()),VarDecl("str_arr3",ArrayType(5,StringType())),VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType()))])),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("start"),[VarDecl("a",IntType()),VarDecl("c",FloatType())],VoidType(),Block([VarDecl("one",IntType())])),VarDecl("_boolVar",BoolType()),FuncDecl(Id("main"),[VarDecl("f",BoolType())],ArrayPointerType(IntType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,316))

#EXPRESSION IN GENERAL
	def test_exp_1(self):
		input = """
		int main(){
            boolean a;
            a = ("abc" == "ABC")||("abc" + "456" > "abc");
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),BinaryOp("=",Id("a"),BinaryOp("||",BinaryOp("==",StringLiteral("abc"),StringLiteral("ABC")),BinaryOp(">",BinaryOp("+",StringLiteral("abc"),StringLiteral("456")),StringLiteral("abc"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,317))
	def test_exp_2(self):
		input = """
            int foo(){
                return 3;
            }
            int main(){
                boolean b;
                b = x + y > 100 || y <= 10; 
                putInt(foo());
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(3))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp(">",BinaryOp("+",Id("x"),Id("y")),IntLiteral(100)),BinaryOp("<=",Id("y"),IntLiteral(10)))),CallExpr(Id("putInt"),[CallExpr(Id("foo"),[])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,318))
	def test_exp_3(self):
		input = """
            int foo(){
                return 3;
            }
            int main(){
                boolean b;
                b = x + y > 100 || y <= 10; 
                goo(foo());
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(3))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp(">",BinaryOp("+",Id("x"),Id("y")),IntLiteral(100)),BinaryOp("<=",Id("y"),IntLiteral(10)))),CallExpr(Id("goo"),[CallExpr(Id("foo"),[])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,319))

#INDEX EXP
	def test_indexExp_1(self):
		input = """
		int main(){
                abc [ 3 + x ] = -doo[x-5];
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("abc"),BinaryOp("+",IntLiteral(3),Id("x"))),UnaryOp("-",ArrayCell(Id("doo"),BinaryOp("-",Id("x"),IntLiteral(5)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,320))
	def test_indexExp_2(self):
		input = """
		void foo(){
                is = (.1e18[a<=foo(3)] >= 9e7) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",Id("is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,321))
	def test_indexExp_3(self):
		input = """
		boolean foo(){
                foo1[3+x] = goo[(1+a[1])] && doo[x-5] = 5;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],BoolType(),Block([BinaryOp("=",ArrayCell(Id("foo1"),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("=",BinaryOp("&&",ArrayCell(Id("goo"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1)))),ArrayCell(Id("doo"),BinaryOp("-",Id("x"),IntLiteral(5)))),IntLiteral(5)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,322))
	def test_indexExp_4(self):
		input = """
		boolean foo(){
                foo(2)[3+x] = a[b[2]] +3;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],BoolType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,323))   
	def test_indexExp_5(self):
		input = """
        void foo(){
                _is = (.1e18[a<=foo(3)] >= 9e7) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",Id("_is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,324))    
	def test_indexExp_6(self):
		input = """
		int[] _main(boolean f, boolean _id[], float a[]){
                foo(2)[3+x] = a[b[2]] +3;
				_is = (.1e18[a<=foo(3)] >= 9e7) ;
				boolean a[3000];
            }
		"""
		expect = str(Program([FuncDecl(Id("_main"),[VarDecl("f",BoolType()),VarDecl("_id",ArrayPointerType(BoolType())),VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",Id("_is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0))),VarDecl("a",ArrayType(3000,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,325))
	def test_indexExp_7(self):
		input = """
		int[] _main(boolean f, boolean _id[], float a[]){
                foo(2)[3+x] = a[b[2]] +3;
				_is = (.1e18[a<=foo(3)] >= 9e7) ;
				boolean a[3000];
            }
        int main(boolean f){
            }
		int main(){}
		void main(){}
		"""
		expect = str(Program([FuncDecl(Id("_main"),[VarDecl("f",BoolType()),VarDecl("_id",ArrayPointerType(BoolType())),VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",Id("_is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0))),VarDecl("a",ArrayType(3000,BoolType()))])),FuncDecl(Id("main"),[VarDecl("f",BoolType())],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,326))

#INVOC EXP
	def test_invocExp_1(self):
		input = """
		int foo(int arg1, boolean arg2, string arg3){}
            int main(){
                foo(arg1 = .45e-3, (lightSpeed >= 3e8), "This is string");
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl("arg1",IntType()),VarDecl("arg2",BoolType()),VarDecl("arg3",StringType())],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[BinaryOp("=",Id("arg1"),FloatLiteral(0.00045)),BinaryOp(">=",Id("lightSpeed"),FloatLiteral(300000000.0)),StringLiteral("This is string")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,327))
	def test_invocExp_2(self):
		input = """
            int main(){
                a[m+n] = b[m+1] = foo()[m*1] = a[a / 3];
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),BinaryOp("=",ArrayCell(Id("b"),BinaryOp("+",Id("m"),IntLiteral(1))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",Id("m"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,328))
	def test_invocExp_3(self):
		input = """
            int main(){
				foo(foo(foo()));
			}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,329))
	def test_invocExp_4(self):
		input = """
		boolean _boolVar;
        int main() {
            int n3;
            n3 = call();
			is = (.1e18[a<=foo(3)] >= 9e7) ;
        }
		"""
		expect = str(Program([VarDecl("_boolVar",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n3",IntType()),BinaryOp("=",Id("n3"),CallExpr(Id("call"),[])),BinaryOp("=",Id("is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,330))
	def test_invocExp_5(self):
		input = """
		boolean _boolVar;
        int main() {
            int n3;
            n3 = call();
			is = (.1e18[a<=foo(3)] >= 9e7) ;
			res = foo(foo(a+b, foo(5)));
			return res;
        }
		"""
		expect = str(Program([VarDecl("_boolVar",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n3",IntType()),BinaryOp("=",Id("n3"),CallExpr(Id("call"),[])),BinaryOp("=",Id("is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0))),BinaryOp("=",Id("res"),CallExpr(Id("foo"),[CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),CallExpr(Id("foo"),[IntLiteral(5)])])])),Return(Id("res"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,331))
	def test_invocExp_6(self):
		input = """
		int main() {
            int n3;
            n3 = call();
			is = (.1e18[a<=foo(3, "foo(5)")] >= 9e7) ;
			res = (foo(foo(a+b, "foo(5)")));
			return res;
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n3",IntType()),BinaryOp("=",Id("n3"),CallExpr(Id("call"),[])),BinaryOp("=",Id("is"),BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3),StringLiteral("foo(5)")]))),FloatLiteral(90000000.0))),BinaryOp("=",Id("res"),CallExpr(Id("foo"),[CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),StringLiteral("foo(5)")])])),Return(Id("res"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,332))
	def test_invocExp_7(self):
		input = """
		int main() {
            int n3;
            n3 = call();
			res = (foo(foo(a+b, "foo(5)")));
			return res;
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n3",IntType()),BinaryOp("=",Id("n3"),CallExpr(Id("call"),[])),BinaryOp("=",Id("res"),CallExpr(Id("foo"),[CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),StringLiteral("foo(5)")])])),Return(Id("res"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,333))   

#EXP AND PRECEDENCE
	def test_generalExp_precedence_1(self):
		input = """
        int main(){
                (1>=0)[2] = 2+a[1]+c+("abc"< 0);
                (.25+1e3+(1<0))[10] = 4;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(BinaryOp(">=",IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(1))),Id("c")),BinaryOp("<",StringLiteral("abc"),IntLiteral(0)))),BinaryOp("=",ArrayCell(BinaryOp("+",BinaryOp("+",FloatLiteral(0.25),FloatLiteral(1000.0)),BinaryOp("<",IntLiteral(1),IntLiteral(0))),IntLiteral(10)),IntLiteral(4))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,334))    
	def test_generalExp_precedence_2(self):
		input = """
		int main(){
            "a34"[25] =  foo[32] && !in[30] ;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(StringLiteral("a34"),IntLiteral(25)),BinaryOp("&&",ArrayCell(Id("foo"),IntLiteral(32)),UnaryOp("!",ArrayCell(Id("in"),IntLiteral(30)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,335))
	def test_generalExp_precedence_3(self):
		input = """
		boolean foo(){
                me >= 69 == 123 + (1 % 3);
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],BoolType(),Block([BinaryOp("==",BinaryOp(">=",Id("me"),IntLiteral(69)),BinaryOp("+",IntLiteral(123),BinaryOp("%",IntLiteral(1),IntLiteral(3))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,336))
	def test_generalExp_precedence_4(self):
		input = """
		int foo(int arg1, boolean arg2, string arg3){}
        int main(){
            foo(arg1 = .45e-3, (lightSpeed >= 3e8), "This is string");
        }
		boolean foo(int arr[]){
                me >= 69 == 123 + (1 % 3);
				return flag;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl("arg1",IntType()),VarDecl("arg2",BoolType()),VarDecl("arg3",StringType())],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[BinaryOp("=",Id("arg1"),FloatLiteral(0.00045)),BinaryOp(">=",Id("lightSpeed"),FloatLiteral(300000000.0)),StringLiteral("This is string")])])),FuncDecl(Id("foo"),[VarDecl("arr",ArrayPointerType(IntType()))],BoolType(),Block([BinaryOp("==",BinaryOp(">=",Id("me"),IntLiteral(69)),BinaryOp("+",IntLiteral(123),BinaryOp("%",IntLiteral(1),IntLiteral(3)))),Return(Id("flag"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,337))
	def test_generalExp_precedence_5(self):
		input = """
		int main(){
            "a34"[25] =  foo[32] && !in[30] ;
        }
        int[] _main1(){
            a[m+n] = b[m+1] = foo()[m*1] = a[a / 3];
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(StringLiteral("a34"),IntLiteral(25)),BinaryOp("&&",ArrayCell(Id("foo"),IntLiteral(32)),UnaryOp("!",ArrayCell(Id("in"),IntLiteral(30)))))])),FuncDecl(Id("_main1"),[],ArrayPointerType(IntType()),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),BinaryOp("=",ArrayCell(Id("b"),BinaryOp("+",Id("m"),IntLiteral(1))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",Id("m"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,338))
	def test_generalExp_precedence_6(self):
		input = """
            int main(){
				s = -a[m+n*_abc>=9*2&&"abc"];
			}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("s"),UnaryOp("-",ArrayCell(Id("a"),BinaryOp("&&",BinaryOp(">=",BinaryOp("+",Id("m"),BinaryOp("*",Id("n"),Id("_abc"))),BinaryOp("*",IntLiteral(9),IntLiteral(2))),StringLiteral("abc")))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,339))

#IF STATEMENT
	def test_ifStatement_1(self):
		input = """
		int main(){
                if (tryHard) pass = "true";
                else pass = "false";
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("tryHard"),BinaryOp("=",Id("pass"),StringLiteral("true")),BinaryOp("=",Id("pass"),StringLiteral("false")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,340))
	def test_ifStatement_2(self):
		input = """
		int main(){
                if (tryHard) pass = "true";
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("tryHard"),BinaryOp("=",Id("pass"),StringLiteral("true")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,341))
	def test_ifStatement_3(self):
		input = """
		int main(){
                if(a>1) a = 1;
                else
                    if ((1!=2)==(3!=4)) x = 1;
                    else foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(1)),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,342))
	def test_ifStatement_4(self):
		input = """
		int main(){
                if(foo(3,2)) a = a%5;
                if ((1!=2)==(3!=4)) x = 1;
                    else foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(2)]),BinaryOp("=",Id("a"),BinaryOp("%",Id("a"),IntLiteral(5)))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,343))   
	def test_ifStatement_5(self):
		input = """
        int _global;
            int main(){
                if(_global % 5) _global = 3;
                if ((1!=2)==(3!=4)) x = 1;
                    else foo("foo",3);
            }
		"""
		expect = str(Program([VarDecl("_global",IntType()),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("%",Id("_global"),IntLiteral(5)),BinaryOp("=",Id("_global"),IntLiteral(3))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,344))    
	def test_ifStatement_6(self):
		input = """
		int main(){
                if(_global % 5) _global = 3; foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("%",Id("_global"),IntLiteral(5)),BinaryOp("=",Id("_global"),IntLiteral(3))),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,345))
	def test_ifStatement_7(self):
		input = """
		int main(){
                if(true) {}
                else 
                    if(_global % 5) _global = 3;
                if ((1!=2)==(3!=4)) x = 1;
                else foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([]),If(BinaryOp("%",Id("_global"),IntLiteral(5)),BinaryOp("=",Id("_global"),IntLiteral(3)))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	def test_ifStatement_8(self):
		input = """
		int main(){
                if(true) {
					if(a>1) a = 1;
                else
                    if ((1!=2)==(3!=4)) x = 1;
                    else foo("foo",3);
				}
                else 
                    if(_global % 5) _global = 3;
                if ((1!=2)==(3!=4)) x = 1;
                else foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BinaryOp(">",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(1)),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)])))]),If(BinaryOp("%",Id("_global"),IntLiteral(5)),BinaryOp("=",Id("_global"),IntLiteral(3)))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,347))
	def test_ifStatement_9(self):
		input = """
		int main(){
			if(a = 2){}else{}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(2)),Block([]),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,348))
	def test_ifStatement_10(self):
		input = """
        int main(){
			if(a = 2){}else{}
		}
        int main(){
			if(a = 2){}else{}
		}
        int main(){
			if(a = 2){}else{}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(2)),Block([]),Block([]))])),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(2)),Block([]),Block([]))])),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(2)),Block([]),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,349))

#DOWHILE STATEMENT
	def test_doWhileStatement_1(self):
		input = """
		int foo(){
                do 
                    a=30 ;
                    if(true) a= b[1];
                    else b=a[1]= 30;
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(30)),If(BooleanLiteral(True),BinaryOp("=",Id("a"),ArrayCell(Id("b"),IntLiteral(1))),BinaryOp("=",Id("b"),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(30))))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,350))
	def test_doWhileStatement_2(self):
		input = """
		int foo(){
                do 
                    a = a-1;
                    do f = sqrt(a*a + b*b + c*c);
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,351))
	def test_doWhileStatement_3(self):
		input = """
		int foo(){
                do 
                    return f[23]%50;
                while (1);
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([Return(BinaryOp("%",ArrayCell(Id("f"),IntLiteral(23)),IntLiteral(50)))],IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,352))
	def test_doWhileStatement_4(self):
		input = """
		int main(){
                if(foo(3,2)) a = a%5;
                if ((1!=2)==(3!=4)) x = 1;
                    else foo("foo",3);
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(2)]),BinaryOp("=",Id("a"),BinaryOp("%",Id("a"),IntLiteral(5)))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,353))   
	def test_doWhileStatement_5(self):
		input = """
        int foo(){
                do 
                    a = a-1;
                    do f = sqrt(a*a + b*b + c*c);
                        if (true) {}
                        else {}
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BooleanLiteral(True),Block([]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,354))    
	def test_doWhileStatement_6(self):
		input = """
		int foo(){
                do 
                    a = a-1;
                    break;
                    do f = sqrt(a*a + b*b + c*c);
                        if (true) { break; }
                        else {}
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Break(),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BooleanLiteral(True),Block([Break()]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,355))
	def test_doWhileStatement_7(self):
		input = """
		int main(){
			do 1; do 1; do 1; while 3; do 1; while 3; do 1; while 3; do 1; while 3; while 3; while 3;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([IntLiteral(1),Dowhile([IntLiteral(1),Dowhile([IntLiteral(1)],IntLiteral(3)),Dowhile([IntLiteral(1)],IntLiteral(3)),Dowhile([IntLiteral(1)],IntLiteral(3)),Dowhile([IntLiteral(1)],IntLiteral(3))],IntLiteral(3))],IntLiteral(3))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,356))
	def test_doWhileStatement_8(self):
		input = """
		int main(){
			do{
                if(true) {
					if(a>1) a = 1;
                	else{
                    	if ((1!=2)==(3!=4)) x = 1;
                    	else foo("foo",3);
					}
				}
                else {
                    if(_global % 5) _global = 3;
                	if ((1!=2)==(3!=4)) x = 1;
                	else foo("foo",3);
            	}
			}
			while("abc");
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BooleanLiteral(True),Block([If(BinaryOp(">",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(1)),Block([If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))]),Block([If(BinaryOp("%",Id("_global"),IntLiteral(5)),BinaryOp("=",Id("_global"),IntLiteral(3))),If(BinaryOp("==",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("x"),IntLiteral(1)),CallExpr(Id("foo"),[StringLiteral("foo"),IntLiteral(3)]))]))])],StringLiteral("abc"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,357))
	def test_doWhileStatement_9(self):
		input = """
		int main(){
			do{}{}{}{}a=3;while (.1e18[a<=foo(3)] >= 9e7);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),BinaryOp("=",Id("a"),IntLiteral(3))],BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,358))
	def test_doWhileStatement_10(self):
		input = """
        int main(){
			do{}{}{}{}a=3;while (.1e18[a<=foo(3)] >= 9e7);
		}
		int main(){
			do{}{}{}{}a=3;while (.1e18[a<=foo(3)] >= 9e7);
		}
		int main(){
			do{}{}{}{}a=3;while (.1e18[a<=foo(3)] >= 9e7);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),BinaryOp("=",Id("a"),IntLiteral(3))],BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))])),FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),BinaryOp("=",Id("a"),IntLiteral(3))],BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))])),FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),BinaryOp("=",Id("a"),IntLiteral(3))],BinaryOp(">=",ArrayCell(FloatLiteral(1e+17),BinaryOp("<=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))),FloatLiteral(90000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,359))

#FOR STATEMENT
	def test_forStatement_1(self):
		input = """
		int main(){
                for (i=1; i<=5; i=i+1)
                    s = s+i;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),Id("i"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,360))
	def test_forStatement_2(self):
		input = """
		int foo(){
            for (i=1; i<m+10; i= i+1) 
                for (j=1; j>m+10; j= j-1)
                    s = s + 1;
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp(">",Id("j"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,361))
	def test_forStatement_3(self):
		input = """
		int foo(){
            for (i = -20 ;i<=0; i= i + 1) 
                for (j=1; j>m+10; j= j-1){
                    s = s + 1;
                    break;
                }
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(20))),BinaryOp("<=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp(">",Id("j"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),Break()])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,362))
	def test_forStatement_4(self):
		input = """
		int foo(){
            for (i = -20 ;i<=0; i= i + 1) 
                for (j=1; j>m+10; j= j-1){
                    s = s + 1;
                    if (s > 0) break;
                    else continue;
                }
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(20))),BinaryOp("<=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp(">",Id("j"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),If(BinaryOp(">",Id("s"),IntLiteral(0)),Break(),Continue())])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,363))   
	def test_forStatement_5(self):
		input = """
        int foo(){
            for (i = -20 ;i<=0; i= i + 1) 
                for (j=1; j>m+10; j= j-1){
                    s = s + 1;
                    if (s > 0) break;
                    else continue;
                }
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(20))),BinaryOp("<=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp(">",Id("j"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),If(BinaryOp(">",Id("s"),IntLiteral(0)),Break(),Continue())])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,364))    
	def test_forStatement_6(self):
		input = """
		int foo(){
            for (i = -20 ;i<=0; i= i + 1) 
                for (j=1; j>m+10; j= j-1){
                    s = s + 1;
                    if (s > 0) break;
                }
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),UnaryOp("-",IntLiteral(20))),BinaryOp("<=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp(">",Id("j"),BinaryOp("+",Id("m"),IntLiteral(10))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),If(BinaryOp(">",Id("s"),IntLiteral(0)),Break())])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,365))
	def test_forStatement_7(self):
		input = """
		float[] foo(){
           for (i = 0;"abc"; i = i-1)
                do 
                continue;
                while i>1 ;
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),StringLiteral("abc"),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Dowhile([Continue()],BinaryOp(">",Id("i"),IntLiteral(1))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,366))
	def test_forStatement_8(self):
		input = """
		int main(){
                for ("1";"1";"1")
                    s = "Fighting!";
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(StringLiteral("1"),StringLiteral("1"),StringLiteral("1"),BinaryOp("=",Id("s"),StringLiteral("Fighting!")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,367))
	def test_forStatement_9(self):
		input = """
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
		int main(){
                for ("1";"1";"1")
                    s = "Fighting!";
            }
		int a,b[5],c;
        float _vi,_int[6];
        string str, str[3], str[5], str[2];
		int main(){
                for ("1";"1";"1")
                    s = "Fighting!";
            }
		int main(){
                for ("1";"1";"1")
                    s = "Fighting!";
            }
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("main"),[],IntType(),Block([For(StringLiteral("1"),StringLiteral("1"),StringLiteral("1"),BinaryOp("=",Id("s"),StringLiteral("Fighting!")))])),VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType()),VarDecl("_vi",FloatType()),VarDecl("_int",ArrayType(6,FloatType())),VarDecl("str",StringType()),VarDecl("str",ArrayType(3,StringType())),VarDecl("str",ArrayType(5,StringType())),VarDecl("str",ArrayType(2,StringType())),FuncDecl(Id("main"),[],IntType(),Block([For(StringLiteral("1"),StringLiteral("1"),StringLiteral("1"),BinaryOp("=",Id("s"),StringLiteral("Fighting!")))])),FuncDecl(Id("main"),[],IntType(),Block([For(StringLiteral("1"),StringLiteral("1"),StringLiteral("1"),BinaryOp("=",Id("s"),StringLiteral("Fighting!")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,368))
	def test_forStatement_10(self):
		input = """
        int main(){
    		for (1;1;1){{{{{}}}}}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([Block([Block([Block([Block([])])])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
#BREAK STATEMENT
	def test_break_1(self):
		input = """
		float[] foo(){
           do {
			   a = a+1;
			   if ("abc") break;
		   }  
		   while(true);
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(FloatType()),Block([Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),If(StringLiteral("abc"),Break())])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,370))
	def test_break_2(self):
		input = """
		float[] foo(){
           for (i = 0; i <= 5; i = i-1)
                if (a == 3) break;   
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("a"),IntLiteral(3)),Break()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,371))
	def test_break_3(self):
		input = """
		float[] foo(){
           for (i = 0; i <= 5; i = i-1)
                if (a == 3) bReAk;    
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("a"),IntLiteral(3)),Id("bReAk")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,372))

#CONTINUE STATEMENT
	def test_continue_1(self):
		input = """
		int main () {
            int a;
            a = 10;
             do {
                if( a == 15) {
                    a = a + 1;
                    continue;
                }
                foo(a);
                a= a+1;
            } while( a < 20 );
            return 0;   
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Dowhile([Block([If(BinaryOp("==",Id("a"),IntLiteral(15)),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()])),CallExpr(Id("foo"),[Id("a")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("<",Id("a"),IntLiteral(20))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,373))   
	def test_continue_2(self):
		input = """
        int main () {
            int a;
            a = 10;
            for(1;1;1) {
                if( a == 15) {
                    a = a + 1;
                    continue;
                }
                foo(a);
                a= a+1;
			}  
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([If(BinaryOp("==",Id("a"),IntLiteral(15)),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()])),CallExpr(Id("foo"),[Id("a")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,374))    
	def test_continue_3(self):
		input = """
		int foo(){
            for(1;1;1){continue;}
        }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([Continue()]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,375))

#RETURN STATEMENT
	def test_return_1(self):
		input = """
		int main () {
             return 1;   
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,376))
	def test_return_2(self):
		input = """
		int main () {
             return arr[3];   
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(ArrayCell(Id("arr"),IntLiteral(3)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,377))
	def test_return_3(self):
		input = """
		int main () {
             return foo(2,3%5);   
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(CallExpr(Id("foo"),[IntLiteral(2),BinaryOp("%",IntLiteral(3),IntLiteral(5))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,378))

#EXP STATEMENT
	def test_expStatement_1(self):
		input = """
        int main () {
             1.68e-32;
             abcd;
             arr[7] == 3e8;
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([FloatLiteral(1.68e-32),Id("abcd"),BinaryOp("==",ArrayCell(Id("arr"),IntLiteral(7)),FloatLiteral(300000000.0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,379))
	def test_expStatement_2(self):
		input = """
		int goo () { 
            int a,b;
            (ab==c) && (!true);
        }
		"""
		expect = str(Program([FuncDecl(Id("goo"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("&&",BinaryOp("==",Id("ab"),Id("c")),UnaryOp("!",BooleanLiteral(True)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,380))

#BLOCK STATEMENT
	def test_blockStatement_1(self):
		input = """
		int main () { 
            int a ,b, c ; 
            a=b=c=5; 
            float f [ 5 ] ; 
            if (a==b) f [0] = 1.0; 
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),VarDecl("f",ArrayType(5,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,381))
	def test_blockStatement_2(self):
		input = """
		int main(){{}{}{}{}{}{}{}{}{}}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,382))
	def test_blockStatement_3(self):
		input = """
		int main(){{{{{{{{{{}}}}}}}}}}  
        
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,383)) 

#COMMENT  
	def test_comment_1(self):
		input = """
        void function_name(int a) 
            { 
                {}  //Function Body 
                return;  //Function execution would get terminated 
            } 
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([Block([]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,384))    
	def test_comment_2(self):
		input = """
		void function_name(int a) 
            { 
                /*
                {foo
                foo
                foo
                foo
                } */ //Function Body 
                return;  //Function execution would get terminated 
            }  
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,385))
	def test_comment_3(self):
		input = """
		void function_name(int a) 
            { 
                int\ta;
                // Function Body 
                return;  //Function execution would get terminated 
            }  
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("a",IntType()),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,386))
	def test_comment_4(self):
		input = """
		void function_name(int a) 
            { 
                {int foo\n;
                }
            }
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([Block([VarDecl("foo",IntType())])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,387))

#MIX AND COMPLEX PROG
	def test_mix_1(self):
		input = """
		int main(){
                 a[b[2]] = 10;
                 name();
                 return;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(10)),CallExpr(Id("name"),[]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,388))
	def test_mix_2(self):
		input = """
        float[] nah(){
				int s;
                {
                    if (s > 10) break;
					else do
                        a = a + 1;
                        while(true);
                }
            }
		"""
		expect = str(Program([FuncDecl(Id("nah"),[],ArrayPointerType(FloatType()),Block([VarDecl("s",IntType()),Block([If(BinaryOp(">",Id("s"),IntLiteral(10)),Break(),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BooleanLiteral(True)))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,389))
	def test_complexProg_1(self):
		input = """
		int main(){
                 a[b[2]] = 10;
                 name();
                 return;
            }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(10)),CallExpr(Id("name"),[]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,390))
	def test_complexProg_2(self):
		input = """
		int foo(){
                do 
                    a = a-1;
                    break;
                    do f = sqrt(a*a + b*b + c*c);
                        if ((1>=0)[2] = 2+a[1]+c+("abc"< 0)) { break; }
                        else {}
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Break(),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BinaryOp("=",ArrayCell(BinaryOp(">=",IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(1))),Id("c")),BinaryOp("<",StringLiteral("abc"),IntLiteral(0)))),Block([Break()]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,391))
	def test_complexProg_3(self):
		input = """
		int main () {
            int a;
            a = 10;
             do {
                if( a == 15) {
                    a = a + 1;
                    coNtInuE;
                }
                foo(a);
                a= a+1;
            } while( a < 20 );
            return 0;   
        }
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Dowhile([Block([If(BinaryOp("==",Id("a"),IntLiteral(15)),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Id("coNtInuE")])),CallExpr(Id("foo"),[Id("a")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("<",Id("a"),IntLiteral(20))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,392))
	def test_complexProg_4(self):
		input = """
		int foo(){
                do 
                    a = a-1;
					//Fighting!!
                    break;
                    do f = sqrt(a*a + b*b + c*c);
                        if ((1>=0)[2] = 2+a[1]+c+("abc"< 0)) { break; }
                        else {}
                    while (a>0);
					//?/@!$$%**())
                while (a!=b) ;
            } 
        
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Break(),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BinaryOp("=",ArrayCell(BinaryOp(">=",IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(1))),Id("c")),BinaryOp("<",StringLiteral("abc"),IntLiteral(0)))),Block([Break()]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,393))   
	def test_complexProg_5(self):
		input = """
        void function_name(int a) 
            { 
                {}  //Function Body 
                return;  //Function execution would get terminated 
            } 
		int GT(int num){
            int t,s;
            t = 0; s = 0;
            for(i=0;i<=n;i=i+1)
                t=t+i;
            for(j=1;j<=t;j=j+1)
                gt=gt*j;
                s=s+gt;
        }
		int foo(){
                do 
                    a = a-1;
                    break;
                    do f = sqrt(a*a + b*b + c*c);
                        if ((1>=0)[2] = 2+a[1]+c+("abc"< 0)) { break; }
                        else {}
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([Block([]),Return()])),FuncDecl(Id("GT"),[VarDecl("num",IntType())],IntType(),Block([VarDecl("t",IntType()),VarDecl("s",IntType()),BinaryOp("=",Id("t"),IntLiteral(0)),BinaryOp("=",Id("s"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("t"),BinaryOp("+",Id("t"),Id("i")))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("t")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("=",Id("gt"),BinaryOp("*",Id("gt"),Id("j")))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),Id("gt")))])),FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Break(),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BinaryOp("=",ArrayCell(BinaryOp(">=",IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(1))),Id("c")),BinaryOp("<",StringLiteral("abc"),IntLiteral(0)))),Block([Break()]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,394))    
	def test_complexProg_6(self):
		input = """
		void function_name(int a) 
            { 
                /*
                {foo
                foo
                foo
                foo
                } */ //Function Body 
                return;  //Function execution would get terminated 
            }  
			int foo(){
                do 
                    a = a-1;
                    break;
                    do f = sqrt(a*a + b*b + c*c);
                        if ((1>=0)[2] = 2+a[1]+c+("abc"< 0)) { break; }
                        else {}
                    while (a>0);
                while (a!=b) ;
            }
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([Return()])),FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Break(),Dowhile([BinaryOp("=",Id("f"),CallExpr(Id("sqrt"),[BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c")))])),If(BinaryOp("=",ArrayCell(BinaryOp(">=",IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),IntLiteral(1))),Id("c")),BinaryOp("<",StringLiteral("abc"),IntLiteral(0)))),Block([Break()]),Block([]))],BinaryOp(">",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,395))
	def test_complexProg_7(self):
		input = """
		void function_name(int a) 
            { 
                int\ta;
                // Function Body 
                return;  //Function execution would get terminated 
            }  
		int[] GT(int num){
            int t,s;
            t = 0; s = 0;
            for(i=0;i<=n;i=i+1)
                t=t+i;
            for(j=1;j<=t;j=j+1)
                gt=gt*j;
                s=s+gt;
			return;
        }
		"""
		expect = str(Program([FuncDecl(Id("function_name"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("a",IntType()),Return()])),FuncDecl(Id("GT"),[VarDecl("num",IntType())],ArrayPointerType(IntType()),Block([VarDecl("t",IntType()),VarDecl("s",IntType()),BinaryOp("=",Id("t"),IntLiteral(0)),BinaryOp("=",Id("s"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("t"),BinaryOp("+",Id("t"),Id("i")))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("t")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("=",Id("gt"),BinaryOp("*",Id("gt"),Id("j")))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),Id("gt"))),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,396))
	def test_complexProg_8(self):
		input = """
		float[] nah(){
				int s;
                {
                    if (s > 10) break;
					else do{{
                        a = a + 1;
						for (1;1;1) put(3);}}
                        while(true);
                }
            }
		"""
		expect = str(Program([FuncDecl(Id("nah"),[],ArrayPointerType(FloatType()),Block([VarDecl("s",IntType()),Block([If(BinaryOp(">",Id("s"),IntLiteral(10)),Break(),Dowhile([Block([Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),CallExpr(Id("put"),[IntLiteral(3)]))])])],BooleanLiteral(True)))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,397))
	def test_complexProg_9(self):
		input = """
		int GT(int num){
            int t,s;
            t = 0; s = 0;
            for(i=0;i<=n;i=i+1)
                t=t+i;
            for(j=1;j<=t;j=j+1)
                gt=gt*j;
                s=s+gt;
        }
		float[] nah(){
				int s;
                {
                    if (s > 10) break;
					else do{{
                        a = a + 1;
						for (1;1;1) put(3);}}
                        while(true);
                }
            }
		"""
		expect = str(Program([FuncDecl(Id("GT"),[VarDecl("num",IntType())],IntType(),Block([VarDecl("t",IntType()),VarDecl("s",IntType()),BinaryOp("=",Id("t"),IntLiteral(0)),BinaryOp("=",Id("s"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("t"),BinaryOp("+",Id("t"),Id("i")))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("t")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("=",Id("gt"),BinaryOp("*",Id("gt"),Id("j")))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),Id("gt")))])),FuncDecl(Id("nah"),[],ArrayPointerType(FloatType()),Block([VarDecl("s",IntType()),Block([If(BinaryOp(">",Id("s"),IntLiteral(10)),Break(),Dowhile([Block([Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),CallExpr(Id("put"),[IntLiteral(3)]))])])],BooleanLiteral(True)))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,398))
	def test_complexProg_10(self):
		input = """
		int main(){
			if(foo(3)){
				if(a[m+n] = b[m+1] = foo()[m*1] = a[a / 3]){
					a=4;
				}
			}
			else{
				if(a[m+n] = b[m+1] = foo()[m*1] = a[a / 3]){
					a=4;
					}
				else{
					do{
						do{
							for(a[3];1;1){
								a[m+n];
							}
						}while(true);

					} while (a[m+n] = b[m+1] = foo()[m*1] = a[a / 3]);
				}
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("foo"),[IntLiteral(3)]),Block([If(BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),BinaryOp("=",ArrayCell(Id("b"),BinaryOp("+",Id("m"),IntLiteral(1))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",Id("m"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))))),Block([BinaryOp("=",Id("a"),IntLiteral(4))]))]),Block([If(BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),BinaryOp("=",ArrayCell(Id("b"),BinaryOp("+",Id("m"),IntLiteral(1))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",Id("m"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))))),Block([BinaryOp("=",Id("a"),IntLiteral(4))]),Block([Dowhile([Block([Dowhile([Block([For(ArrayCell(Id("a"),IntLiteral(3)),IntLiteral(1),IntLiteral(1),Block([ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n")))]))])],BooleanLiteral(True))])],BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),BinaryOp("=",ArrayCell(Id("b"),BinaryOp("+",Id("m"),IntLiteral(1))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",Id("m"),IntLiteral(1))),ArrayCell(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))))))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,399))

	
    