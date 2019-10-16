import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
							#CONTENTS:
							#TEST_DECL 			- 10
							#TEST_EXP 			- 15
							#TEST_IFSTMT 		- 05
							#TEST_FORSTMT 		- 05
							#TEST_BLOCKSTMT 	- 05
							#TEST_DOWHILESTMT 	- 05
							#TEST_OTHERSTMT		- 10
							#TEST_STMTEXPCOMBINE- 15
							#TEST_ALL			- 10
							#TEST_SIMPLEPROGRAM	- 10
							#TEST_COMPLEXPROGRAM- 10
							#========================
							#TOTAL				- 100


#TEST_DECL==========================================================================================(10)
	def test_decl_0(self):
		input = """int a[10];"""
		expect = str(Program([VarDecl("a",ArrayType(10,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	
	def test_decl_1(self):
		input = """float a, b, c;
					boolean flag[5], t; """
		expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("flag",ArrayType(5,BoolType())),VarDecl("t",BoolType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	
	def test_decl_2(self):
		input = """int main(){}
				"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	
	def test_decl_3(self):
		input = """int a, b[7];
				float[] foo(int a, float b[], boolean f){}"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(7,IntType())),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],ArrayPointerType(FloatType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,303))
	
	def test_decl_4(self):
		input = """float f1[9];
				string merge(string a, string b){}"""
		expect = str(Program([VarDecl("f1",ArrayType(9,FloatType())),FuncDecl(Id("merge"),[VarDecl("a",StringType()),VarDecl("b",StringType())],StringType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,304))

	def test_decl_5(self):
		input = """int i;
				//main function here!
				void main(){
					{
						float j;
					}
				}"""
		expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl("j",FloatType())])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,305))

	def test_decl_6(self):
		input = """int goo(){
			{
				float a[10], b;
				{
					string str;
					boolean p[3], q; 
				} 
			}
		}"""
		expect = str(Program([FuncDecl(Id("goo"),[],IntType(),Block([Block([VarDecl("a",ArrayType(10,FloatType())),VarDecl("b",FloatType()),Block([VarDecl("str",StringType()),VarDecl("p",ArrayType(3,BoolType())),VarDecl("q",BoolType())])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	
	def test_decl_7(self):
		input = """void swap(int a, int b){}
				int a[10], b[12], c[16];"""
		expect = str(Program([FuncDecl(Id("swap"),[VarDecl("a",IntType()),VarDecl("b",IntType())],VoidType(),Block([])),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(12,IntType())),VarDecl("c",ArrayType(16,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,307))
	
	def test_sidecl_8(self):
		input = """int main(){
					{
						{
							{
								int i, j, k;
								float c[10];
							}
						}
					}
					{
						string d;
					}
				}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",IntType()),VarDecl("c",ArrayType(10,FloatType()))])])]),Block([VarDecl("d",StringType())])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	
	def test_decl_9(self):
		input = """int a[10], b, c[12], d;
				int[] __nothing(int a[], int b[], int c[], int d){}
				float _sum(float a[]){}"""
		expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),VarDecl("c",ArrayType(12,IntType())),VarDecl("d",IntType()),FuncDecl(Id("__nothing"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(IntType())),VarDecl("c",ArrayPointerType(IntType())),VarDecl("d",IntType())],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("_sum"),[VarDecl("a",ArrayPointerType(FloatType()))],FloatType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,309))

#TEST_EXP===========================================================================================(15)

	def test_exp_0(self):
		input = """int main(){
			a = b + c - d + 5.5;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("-",BinaryOp("+",Id("b"),Id("c")),Id("d")),FloatLiteral(5.5)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,310))

	def test_exp_1(self):
		input = """int sub(){
			result = this*that - that/this%thatthis;
		}"""
		expect = str(Program([FuncDecl(Id("sub"),[],IntType(),Block([BinaryOp("=",Id("result"),BinaryOp("-",BinaryOp("*",Id("this"),Id("that")),BinaryOp("%",BinaryOp("/",Id("that"),Id("this")),Id("thatthis"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,311))

	def test_exp_2(self):
		input = """void main(){
			x = (-!-!--y + y)*z;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("x"),BinaryOp("*",BinaryOp("+",UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("-",Id("y"))))))),Id("y")),Id("z")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,312))

	def test_exp_3(self):
		input = """void __Sherlock(){
			str1 = "The" + " Sign" + " Of" + " Three";
			str2 = "Crossroad in the Ancient" + " Capital";
			APTX = 48*100 + 69;
		}"""
		expect = str(Program([FuncDecl(Id("__Sherlock"),[],VoidType(),Block([BinaryOp("=",Id("str1"),BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("The"),StringLiteral(" Sign")),StringLiteral(" Of")),StringLiteral(" Three"))),BinaryOp("=",Id("str2"),BinaryOp("+",StringLiteral("Crossroad in the Ancient"),StringLiteral(" Capital"))),BinaryOp("=",Id("APTX"),BinaryOp("+",BinaryOp("*",IntLiteral(48),IntLiteral(100)),IntLiteral(69)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,313))

	def test_exp_4(self):
		input = """void _hoo(){
			flag = (a + b >= 12 + c) && (a > b);
			boo = flag || ((a <= 100 - c) && (b < 10)); 
		}"""
		expect = str(Program([FuncDecl(Id("_hoo"),[],VoidType(),Block([BinaryOp("=",Id("flag"),BinaryOp("&&",BinaryOp(">=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",IntLiteral(12),Id("c"))),BinaryOp(">",Id("a"),Id("b")))),BinaryOp("=",Id("boo"),BinaryOp("||",Id("flag"),BinaryOp("&&",BinaryOp("<=",Id("a"),BinaryOp("-",IntLiteral(100),Id("c"))),BinaryOp("<",Id("b"),IntLiteral(10)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,314))

	def test_exp_5(self):
		input = """void main(){
			a = random(0, 48);
			b = random(0, 69);
			sum = sum(a, b);
			printf("sum = ", sum);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),CallExpr(Id("random"),[IntLiteral(0),IntLiteral(48)])),BinaryOp("=",Id("b"),CallExpr(Id("random"),[IntLiteral(0),IntLiteral(69)])),BinaryOp("=",Id("sum"),CallExpr(Id("sum"),[Id("a"),Id("b")])),CallExpr(Id("printf"),[StringLiteral("sum = "),Id("sum")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,315))

	def test_exp_6(self):
		input = """void main(){
			i = j = .77e-3;
            i = j + foo()[2]*i;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),FloatLiteral(0.00077))),BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),BinaryOp("*",ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(2)),Id("i"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,316))

	def test_exp_7(self):
		input = """void main(){
			flag = (a == b + c) || (flag != true + false);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("flag"),BinaryOp("||",BinaryOp("==",Id("a"),BinaryOp("+",Id("b"),Id("c"))),BinaryOp("!=",Id("flag"),BinaryOp("+",BooleanLiteral(True),BooleanLiteral(False)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,317))

	def test_exp_8(self):
		input = """void main(){
			_a = goo(5-b) - foo(5.e-5,4-b)*b/8;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("_a"),BinaryOp("-",CallExpr(Id("goo"),[BinaryOp("-",IntLiteral(5),Id("b"))]),BinaryOp("/",BinaryOp("*",CallExpr(Id("foo"),[FloatLiteral(5e-05),BinaryOp("-",IntLiteral(4),Id("b"))]),Id("b")),IntLiteral(8))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,318))

	def test_exp_9(self):
		input = """void main(){
			result = g[a[10] + a[0]]*(a[5] + a[7]) - !!!a[1] ----4/((a[10] >= x) + 1);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("result"),BinaryOp("-",BinaryOp("-",BinaryOp("*",ArrayCell(Id("g"),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(10)),ArrayCell(Id("a"),IntLiteral(0)))),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(5)),ArrayCell(Id("a"),IntLiteral(7)))),UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(Id("a"),IntLiteral(1)))))),BinaryOp("/",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(4)))),BinaryOp("+",BinaryOp(">=",ArrayCell(Id("a"),IntLiteral(10)),Id("x")),IntLiteral(1)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,319))

	def test_exp_10(self):
		input = """float sum(float a, float b){
			return a + b;
		} //sum func
		float mul(float a, float b){
			return a * b;
		}
		/*
		create andThen func
		*/
		float sumAndThenmul(float a[]){
			return mul(sum(a[0], a[1]), a[2]);
		}"""
		expect = str(Program([FuncDecl(Id("sum"),[VarDecl("a",FloatType()),VarDecl("b",FloatType())],FloatType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("mul"),[VarDecl("a",FloatType()),VarDecl("b",FloatType())],FloatType(),Block([Return(BinaryOp("*",Id("a"),Id("b")))])),FuncDecl(Id("sumAndThenmul"),[VarDecl("a",ArrayPointerType(FloatType()))],FloatType(),Block([Return(CallExpr(Id("mul"),[CallExpr(Id("sum"),[ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("a"),IntLiteral(1))]),ArrayCell(Id("a"),IntLiteral(2))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,320))

	def test_exp_11(self):
		input = """int main(){
			c = .5e-9;
			{
				a = b = d = 9 * c;
				{
					a = foo(c*5 + b)[goo(c*5 + d)];
				}
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("c"),FloatLiteral(5e-10)),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("d"),BinaryOp("*",IntLiteral(9),Id("c"))))),Block([BinaryOp("=",Id("a"),ArrayCell(CallExpr(Id("foo"),[BinaryOp("+",BinaryOp("*",Id("c"),IntLiteral(5)),Id("b"))]),CallExpr(Id("goo"),[BinaryOp("+",BinaryOp("*",Id("c"),IntLiteral(5)),Id("d"))])))])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,321))

	def test_exp_12(self):
		input = """void main(){
			f = a + 5.5e-10 + 4.4e-1*arr[10*arr[5] - 8*f(g(a))];
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("f"),BinaryOp("+",BinaryOp("+",Id("a"),FloatLiteral(5.5e-10)),BinaryOp("*",FloatLiteral(0.44),ArrayCell(Id("arr"),BinaryOp("-",BinaryOp("*",IntLiteral(10),ArrayCell(Id("arr"),IntLiteral(5))),BinaryOp("*",IntLiteral(8),CallExpr(Id("f"),[CallExpr(Id("g"),[Id("a")])])))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,322))

	def test_exp_13(self):
		input = """int main(){
			flag = t = ((a == b) + c) != d * g && a < c + 5 || !!(a >= 10 + !-g);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("flag"),BinaryOp("=",Id("t"),BinaryOp("||",BinaryOp("&&",BinaryOp("!=",BinaryOp("+",BinaryOp("==",Id("a"),Id("b")),Id("c")),BinaryOp("*",Id("d"),Id("g"))),BinaryOp("<",Id("a"),BinaryOp("+",Id("c"),IntLiteral(5)))),UnaryOp("!",UnaryOp("!",BinaryOp(">=",Id("a"),BinaryOp("+",IntLiteral(10),UnaryOp("!",UnaryOp("-",Id("g"))))))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,323))

	def test_exp_14(self):
		input = """void main(){
			n = (func(func(arr[0], 1 - b*2)[arr[3] + 4], -- (b*5 + 6)) - h[arr[7]]*foo(!!!a[8] >= 10))[a[9] - 10];
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("n"),ArrayCell(BinaryOp("-",CallExpr(Id("func"),[ArrayCell(CallExpr(Id("func"),[ArrayCell(Id("arr"),IntLiteral(0)),BinaryOp("-",IntLiteral(1),BinaryOp("*",Id("b"),IntLiteral(2)))]),BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(3)),IntLiteral(4))),UnaryOp("-",UnaryOp("-",BinaryOp("+",BinaryOp("*",Id("b"),IntLiteral(5)),IntLiteral(6))))]),BinaryOp("*",ArrayCell(Id("h"),ArrayCell(Id("arr"),IntLiteral(7))),CallExpr(Id("foo"),[BinaryOp(">=",UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(Id("a"),IntLiteral(8))))),IntLiteral(10))]))),BinaryOp("-",ArrayCell(Id("a"),IntLiteral(9)),IntLiteral(10))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,324))

#TEST_IFSTMT========================================================================================(05)
	def test_ifstmt_0(self):
		input = """int main(){
			if (flag) a = a + 1;
			else a = a - 1;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("flag"),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,325))

	def test_ifstmt_1(self):
		input = """void main(){
			flag = false;
			if (foo(a)[0] > b - c) flag = true;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("flag"),BooleanLiteral(False)),If(BinaryOp(">",ArrayCell(CallExpr(Id("foo"),[Id("a")]),IntLiteral(0)),BinaryOp("-",Id("b"),Id("c"))),BinaryOp("=",Id("flag"),BooleanLiteral(True)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,326))

	def test_ifstmt_2(self):
		input = """int main(){
			if (f1 && f2) swap(a, b);
			else if (f1 == true) c = a + b;
			else if (f2 == true) c = a - b;
			else a = b = 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",Id("f1"),Id("f2")),CallExpr(Id("swap"),[Id("a"),Id("b")]),If(BinaryOp("==",Id("f1"),BooleanLiteral(True)),BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),Id("b"))),If(BinaryOp("==",Id("f2"),BooleanLiteral(True)),BinaryOp("=",Id("c"),BinaryOp("-",Id("a"),Id("b"))),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),IntLiteral(0))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,327))

	def test_ifstmt_3(self):
		input = """void isPerson(int height, string str){ //height in cm
			if (height >= 160) str = "true";
			else str = "NaP"; //Not a Person
		} 
		"""
		expect = str(Program([FuncDecl(Id("isPerson"),[VarDecl("height",IntType()),VarDecl("str",StringType())],VoidType(),Block([If(BinaryOp(">=",Id("height"),IntLiteral(160)),BinaryOp("=",Id("str"),StringLiteral("true")),BinaryOp("=",Id("str"),StringLiteral("NaP")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,328))

	def test_ifstmt_4(self):
		input = """int main() {
			if (a > -10) if (b > -.5e-2) if (c == true) a = a + b - c;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),UnaryOp("-",IntLiteral(10))),If(BinaryOp(">",Id("b"),UnaryOp("-",FloatLiteral(0.005))),If(BinaryOp("==",Id("c"),BooleanLiteral(True)),BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),Id("c"))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,329))

#TEST_FORSTMT=======================================================================================(05)
	def test_forstmt_0(self):
		input = """int main() {
			for (i = 0; i < 100; i = i + 1) sum = sum + i;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(100)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("i"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,330))

	def test_forstmt_1(self):
		input = """int main() {
			for (1; i < 100; 1) {
				sum = sum + i;
				i = i + 1;
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(1),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("i"))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,331))

	def test_forstmt_2(self):
		input = """void main() {
			for (i = 4; i < 100; i = i + 8)
				for (j = 6; j < 100; j = j + 9) {}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<",Id("i"),IntLiteral(100)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(8))),For(BinaryOp("=",Id("j"),IntLiteral(6)),BinaryOp("<",Id("j"),IntLiteral(100)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(9))),Block([])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,332))

	def test_forstmt_3(self):
		input = """int main() {
            for (1; i < 100; i = i * 3) print("Everything'll be okay!");
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(100)),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(3))),CallExpr(Id("print"),[StringLiteral("Everything'll be okay!")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,333))

	def test_forstmt_4(self):
		input = """int a[10];
        int sum(int a[]) {
            int i, sum;
            for (i = 0; i < 10; i = i+1) sum = sum + a[i];
            return sum;
        }"""
		expect = str(Program([VarDecl("a",ArrayType(10,IntType())),FuncDecl(Id("sum"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("i",IntType()),VarDecl("sum",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("a"),Id("i"))))),Return(Id("sum"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,334))

#TEST_BLOCKSTMT=====================================================================================(05)
	def test_blockstmt_0(self):
		input = """void main() {
			/*
			Play with some blocks
			*/
			{{{}}}
			{{}}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([Block([Block([])])]),Block([Block([])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,335))

	def test_blockstmt_1(self):
		input = """void main() {
			{
				int a[10], b, c[2];
				b = 3;
				{
					float d[1], e;
					d[0] = .5;
					{
						b = 5;
					}
					//b = ??
				}
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType())),BinaryOp("=",Id("b"),IntLiteral(3)),Block([VarDecl("d",ArrayType(1,FloatType())),VarDecl("e",FloatType()),BinaryOp("=",ArrayCell(Id("d"),IntLiteral(0)),FloatLiteral(0.5)),Block([BinaryOp("=",Id("b"),IntLiteral(5))])])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,336))

	def test_blockstmt_2(self):
		input = """boolean __testSomeBlocks() {
		{ a * b = b * c = c * d; }
		{ 
			str = "There's always only one truth!";
			printf(str);
			toJapanese(str);
			{
				return str == "Shinjitsu wa itsumo hitotsu!";
			}
		}
		}"""
		expect = str(Program([FuncDecl(Id("__testSomeBlocks"),[],BoolType(),Block([Block([BinaryOp("=",BinaryOp("*",Id("a"),Id("b")),BinaryOp("=",BinaryOp("*",Id("b"),Id("c")),BinaryOp("*",Id("c"),Id("d"))))]),Block([BinaryOp("=",Id("str"),StringLiteral("There's always only one truth!")),CallExpr(Id("printf"),[Id("str")]),CallExpr(Id("toJapanese"),[Id("str")]),Block([Return(BinaryOp("==",Id("str"),StringLiteral("Shinjitsu wa itsumo hitotsu!")))])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,337))

	def test_blockstmt_3(self):
		input = """void main() {
		a = -foo(a)[5] + 8 * goo(a); 
		{
			a = newValue = 9.5e-3;
			{
				a = true;
				{
					a = "I'm trying!";
				}
			}
		}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",UnaryOp("-",ArrayCell(CallExpr(Id("foo"),[Id("a")]),IntLiteral(5))),BinaryOp("*",IntLiteral(8),CallExpr(Id("goo"),[Id("a")])))),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("newValue"),FloatLiteral(0.0095))),Block([BinaryOp("=",Id("a"),BooleanLiteral(True)),Block([BinaryOp("=",Id("a"),StringLiteral("I'm trying!"))])])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,338))

	def test_blockstmt_4(self):
		input = """void main() {
		{
			int a[5], b[5], c[5];
			{
				boolean flag, q[2];
			}
			{
				string t[5];
				t = foo(a);
				{
					t[0] = "2019.12.08 - 20th Anniversary"; 
				}
			}
		}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl("a",ArrayType(5,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(5,IntType())),Block([VarDecl("flag",BoolType()),VarDecl("q",ArrayType(2,BoolType()))]),Block([VarDecl("t",ArrayType(5,StringType())),BinaryOp("=",Id("t"),CallExpr(Id("foo"),[Id("a")])),Block([BinaryOp("=",ArrayCell(Id("t"),IntLiteral(0)),StringLiteral("2019.12.08 - 20th Anniversary"))])])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,339))

#TEST_DOWHILESTMT===================================================================================(05)
	def test_dowhilestmt_0(self):
		input = """void main() {
			do double(x); while true;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([CallExpr(Id("double"),[Id("x")])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,340))

	def test_dowhilestmt_1(self):
		input = """void main() {
			do {
				x = exp(x, 2);
				sum = sum + x;
			} while x < 2e10;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([BinaryOp("=",Id("x"),CallExpr(Id("exp"),[Id("x"),IntLiteral(2)])),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("x")))])],BinaryOp("<",Id("x"),FloatLiteral(20000000000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,341))

	def test_dowhilestmt_2(self):
		input = """void main() {
			int x, a[99];
			do x = x + 3;
            printf(x);
            a[i] = x;
            i = i + 1;
            while (i < 99);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",IntType()),VarDecl("a",ArrayType(99,IntType())),Dowhile([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(3))),CallExpr(Id("printf"),[Id("x")]),BinaryOp("=",ArrayCell(Id("a"),Id("i")),Id("x")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(99)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,342))

	def test_dowhilestmt_3(self):
		input = """void main() {
			do do do do do x(); while y(); while z(); while t(); while u(); while v();
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([Dowhile([CallExpr(Id("x"),[])],CallExpr(Id("y"),[]))],CallExpr(Id("z"),[]))],CallExpr(Id("t"),[]))],CallExpr(Id("u"),[]))],CallExpr(Id("v"),[]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,343))

	def test_dowhilestmt_4(self):
		input = """void main() {
			//Variable declaration
			float s[2], k;
			boolean flag;
			/*
			Dowhile statement
			*/
			do {double(x);}
			x = x + 1;
			{triple(x);}
			x = x + 2;
			while x < 1e3;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("s",ArrayType(2,FloatType())),VarDecl("k",FloatType()),VarDecl("flag",BoolType()),Dowhile([Block([CallExpr(Id("double"),[Id("x")])]),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Block([CallExpr(Id("triple"),[Id("x")])]),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))],BinaryOp("<",Id("x"),FloatLiteral(1000.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,344))

#TEST_OTHERSTMT=====================================================================================(10)
	def test_otherstmt_0(self):
		input = """void _donothing() {
			return;
		}"""
		expect = str(Program([FuncDecl(Id("_donothing"),[],VoidType(),Block([Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,345))

	def test_otherstmt_1(self):
		input = """int _dosomething() {
			create(something);
			return something;
		}"""
		expect = str(Program([FuncDecl(Id("_dosomething"),[],IntType(),Block([CallExpr(Id("create"),[Id("something")]),Return(Id("something"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	
	def test_otherstmt_2(self):
		input = """int main() {
			if (flag == true) break;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("flag"),BooleanLiteral(True)),Break())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,347))
	
	def test_otherstmt_3(self):
		input = """float calculate(string op, float a, float b) {
            if (op == "*") return a * b;
            if (op == "/") return a / b;
            else error(op);
        }"""
		expect = str(Program([FuncDecl(Id("calculate"),[VarDecl("op",StringType()),VarDecl("a",FloatType()),VarDecl("b",FloatType())],FloatType(),Block([If(BinaryOp("==",Id("op"),StringLiteral("*")),Return(BinaryOp("*",Id("a"),Id("b")))),If(BinaryOp("==",Id("op"),StringLiteral("/")),Return(BinaryOp("/",Id("a"),Id("b"))),CallExpr(Id("error"),[Id("op")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,348))

	def test_otherstmt_4(self):
		input = """int fibonacci(int n) {
            if (n == 0) return 1;
            if (n == 1) return 1;
            return fibonacci(n - 1) + fibonacci(n - 2);
        }"""
		expect = str(Program([FuncDecl(Id("fibonacci"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(0)),Return(IntLiteral(1))),If(BinaryOp("==",Id("n"),IntLiteral(1)),Return(IntLiteral(1))),Return(BinaryOp("+",CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(1))]),CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(2))])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,349))

	def test_otherstmt_5(self):
		input = """int main() {
        if (flag) continue;
        else break;
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("flag"),Continue(),Break())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,350))

	def test_otherstmt_6(self):
		input = """void foo() {
		break;
		continue;
		return;
		}"""
		expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Break(),Continue(),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,351))

	def test_otherstmt_7(self):
		input = """float mul(float a[], int n) {
		for (i = 0; true; true) {
			result = result * a[i];
			i = i + 1;
			if (i == n) break;
		}
		}"""
		expect = str(Program([FuncDecl(Id("mul"),[VarDecl("a",ArrayPointerType(FloatType())),VarDecl("n",IntType())],FloatType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BooleanLiteral(True),BooleanLiteral(True),Block([BinaryOp("=",Id("result"),BinaryOp("*",Id("result"),ArrayCell(Id("a"),Id("i")))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),Id("n")),Break())]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,352))

	def test_otherstmt_8(self):
		input = """void life(string e){
		if (happy(e)) continue;
		if (unhappy(e)) life("happy");
		}"""
		expect = str(Program([FuncDecl(Id("life"),[VarDecl("e",StringType())],VoidType(),Block([If(CallExpr(Id("happy"),[Id("e")]),Continue()),If(CallExpr(Id("unhappy"),[Id("e")]),CallExpr(Id("life"),[StringLiteral("happy")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,353))

	def test_otherstmt_9(self):
		input = """string compare(float a, float b){
		if (a < b) return "<";
		if (a > b) return ">";
		return "=";
		}"""
		expect = str(Program([FuncDecl(Id("compare"),[VarDecl("a",FloatType()),VarDecl("b",FloatType())],StringType(),Block([If(BinaryOp("<",Id("a"),Id("b")),Return(StringLiteral("<"))),If(BinaryOp(">",Id("a"),Id("b")),Return(StringLiteral(">"))),Return(StringLiteral("="))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,354))

#TEST_STMTEXPCOMBINE================================================================================(15)
	def test_stmtexpcombine_0(self):
		input = """int main(){
			if (-a > -100 + b)
				for (i = 0; i = i + 4; i < b)
					if (i < a) printf(i*a);
			else return;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",UnaryOp("-",Id("a")),BinaryOp("+",UnaryOp("-",IntLiteral(100)),Id("b"))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(4))),BinaryOp("<",Id("i"),Id("b")),If(BinaryOp("<",Id("i"),Id("a")),CallExpr(Id("printf"),[BinaryOp("*",Id("i"),Id("a"))]),Return())))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,355))

	def test_stmtexpcombine_1(self):
		input = """int main(){
			int a[100], sum;
			a = random(1, 100, 100);
			for (i = 0; i = i + 1; i < 100) {
					if (a[i] % 2 == 0) continue;
					sum = sum + a[i];
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(100,IntType())),VarDecl("sum",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("random"),[IntLiteral(1),IntLiteral(100),IntLiteral(100)])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("<",Id("i"),IntLiteral(100)),Block([If(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),Id("i")),IntLiteral(2)),IntLiteral(0)),Continue()),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("a"),Id("i"))))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,356))

	def test_stmtexpcombine_2(self):
		input = """int main(){
			do for (true; x < random(1,100); true) if (isSad()) printf("Waratte hoshii!");
			while true;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([For(BooleanLiteral(True),BinaryOp("<",Id("x"),CallExpr(Id("random"),[IntLiteral(1),IntLiteral(100)])),BooleanLiteral(True),If(CallExpr(Id("isSad"),[]),CallExpr(Id("printf"),[StringLiteral("Waratte hoshii!")])))],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,357))

	def test_stmtexpcombine_3(self):
		input = """int find_gcd(int n1, int n2){
            if (n2 != 0)
            	return find_gcd(n2, n1%n2);
            else return n1;
        }"""
		expect = str(Program([FuncDecl(Id("find_gcd"),[VarDecl("n1",IntType()),VarDecl("n2",IntType())],IntType(),Block([If(BinaryOp("!=",Id("n2"),IntLiteral(0)),Return(CallExpr(Id("find_gcd"),[Id("n2"),BinaryOp("%",Id("n1"),Id("n2"))])),Return(Id("n1")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,358))

	def test_stmtexpcombine_4(self):
		input = """int main(){
			a = (func(4)[arr[0] * 5] + 6) * 5 + .3;
			do {
				a = a - 3;
				if (!flag) a = a/2;
				else a = a + 2; 
			}
			while a > 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("*",BinaryOp("+",ArrayCell(CallExpr(Id("func"),[IntLiteral(4)]),BinaryOp("*",ArrayCell(Id("arr"),IntLiteral(0)),IntLiteral(5))),IntLiteral(6)),IntLiteral(5)),FloatLiteral(0.3))),Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(3))),If(UnaryOp("!",Id("flag")),BinaryOp("=",Id("a"),BinaryOp("/",Id("a"),IntLiteral(2))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))))])],BinaryOp(">",Id("a"),IntLiteral(0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,359))

	def test_stmtexpcombine_5(self):
		input = """void main(){
			for (count = 0; count < 100; 1) {
				for (i = 0; i < foo(count)[10]; 1) {
					do goo(i);
					while i < count;
					if (i >= count) break;
					else continue;
				}
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("count"),IntLiteral(0)),BinaryOp("<",Id("count"),IntLiteral(100)),IntLiteral(1),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),ArrayCell(CallExpr(Id("foo"),[Id("count")]),IntLiteral(10))),IntLiteral(1),Block([Dowhile([CallExpr(Id("goo"),[Id("i")])],BinaryOp("<",Id("i"),Id("count"))),If(BinaryOp(">=",Id("i"),Id("count")),Break(),Continue())]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,360))

	def test_stmtexpcombine_6(self):
		input = """int main(){
			do nothing();
			something();
			{
				anything();
				if (false) nothing();
			}
			while true;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([CallExpr(Id("nothing"),[]),CallExpr(Id("something"),[]),Block([CallExpr(Id("anything"),[]),If(BooleanLiteral(False),CallExpr(Id("nothing"),[]))])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,361))

	def test_stmtexpcombine_7(self):
		input = """int main(){
			if (!!!!a != b)
				for (true; true; 1)
					do printf("I have no idea what to write. -_-\\n");
					printf("100 testcases - too much!");
					while exhausted();
			else process(next);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a"))))),Id("b")),For(BooleanLiteral(True),BooleanLiteral(True),IntLiteral(1),Dowhile([CallExpr(Id("printf"),[StringLiteral("I have no idea what to write. -_-\\n")]),CallExpr(Id("printf"),[StringLiteral("100 testcases - too much!")])],CallExpr(Id("exhausted"),[]))),CallExpr(Id("process"),[Id("next")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,362))

	def test_stmtexpcombine_8(self):
		input = """int main(){
			if (1) for (2; 3; 4) for (5; 6; 7) {}
			else if (8) do 9; 10; while 11;
			else return 12;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),For(IntLiteral(2),IntLiteral(3),IntLiteral(4),For(IntLiteral(5),IntLiteral(6),IntLiteral(7),Block([]))),If(IntLiteral(8),Dowhile([IntLiteral(9),IntLiteral(10)],IntLiteral(11)),Return(IntLiteral(12))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,363))

	def test_stmtexpcombine_9(self):
		input = """int _anomynous(){
			break;
			continue;
			{
				continue;
				break;
			}
			return (foo(a[5] * 9)[2019])[100] + (a[a[a[2]]] != .5e-2) * "kai" - true / 10e2 * false;
		}"""
		expect = str(Program([FuncDecl(Id("_anomynous"),[],IntType(),Block([Break(),Continue(),Block([Continue(),Break()]),Return(BinaryOp("-",BinaryOp("+",ArrayCell(ArrayCell(CallExpr(Id("foo"),[BinaryOp("*",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(9))]),IntLiteral(2019)),IntLiteral(100)),BinaryOp("*",BinaryOp("!=",ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(2)))),FloatLiteral(0.005)),StringLiteral("kai"))),BinaryOp("*",BinaryOp("/",BooleanLiteral(True),FloatLiteral(1000.0)),BooleanLiteral(False))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,364))

	def test_stmtexpcombine_10(self):
		input = """void main(){
			a = b = c = foo(.5e-2, 10, b[12*c[1]]) + 10 * what;
			for (a; b <= 100; c) {
				do a = d();
				while (a == goo(a));
				for (true; 1; 1) really();
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("+",CallExpr(Id("foo"),[FloatLiteral(0.005),IntLiteral(10),ArrayCell(Id("b"),BinaryOp("*",IntLiteral(12),ArrayCell(Id("c"),IntLiteral(1))))]),BinaryOp("*",IntLiteral(10),Id("what")))))),For(Id("a"),BinaryOp("<=",Id("b"),IntLiteral(100)),Id("c"),Block([Dowhile([BinaryOp("=",Id("a"),CallExpr(Id("d"),[]))],BinaryOp("==",Id("a"),CallExpr(Id("goo"),[Id("a")]))),For(BooleanLiteral(True),IntLiteral(1),IntLiteral(1),CallExpr(Id("really"),[]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,365))

	def test_stmtexpcombine_11(self):
		input = """int __noname(){
			str = "Sissy Sky" + "+"/"|" + date(11/6);
			if (inConanSongsList(str)) printf("This song is wonderful!");
			{
				gaugau = meomeo(10e1 - 10, 10)[10] + (true || false) * "true";
			}
		}"""
		expect = str(Program([FuncDecl(Id("__noname"),[],IntType(),Block([BinaryOp("=",Id("str"),BinaryOp("+",BinaryOp("+",StringLiteral("Sissy Sky"),BinaryOp("/",StringLiteral("+"),StringLiteral("|"))),CallExpr(Id("date"),[BinaryOp("/",IntLiteral(11),IntLiteral(6))]))),If(CallExpr(Id("inConanSongsList"),[Id("str")]),CallExpr(Id("printf"),[StringLiteral("This song is wonderful!")])),Block([BinaryOp("=",Id("gaugau"),BinaryOp("+",ArrayCell(CallExpr(Id("meomeo"),[BinaryOp("-",FloatLiteral(100.0),IntLiteral(10)),IntLiteral(10)]),IntLiteral(10)),BinaryOp("*",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),StringLiteral("true"))))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,366))

	def test_stmtexpcombine_12(self):
		input = """int main(){
			do {{}}
			{{}}
			{{}}
			for (1; 1; 1) {{}}
			if (1) {{}} else {{}}
			while (1);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([])]),Block([Block([])]),Block([Block([])]),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([Block([])])),If(IntLiteral(1),Block([Block([])]),Block([Block([])]))],IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,367))

	def test_stmtexpcombine_13(self):
		input = """int main(){
			if (1 || 2 && 3 * 4 <= (5 + 6) * 7 && 8 == foo(9))
				{
					a = func1(arr[2] * arr[3], arr[0] / arr[1]);
				}
					if (10) do 11; while 13;
			else func2(14);
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",IntLiteral(1),BinaryOp("&&",BinaryOp("&&",IntLiteral(2),BinaryOp("<=",BinaryOp("*",IntLiteral(3),IntLiteral(4)),BinaryOp("*",BinaryOp("+",IntLiteral(5),IntLiteral(6)),IntLiteral(7)))),BinaryOp("==",IntLiteral(8),CallExpr(Id("foo"),[IntLiteral(9)])))),Block([BinaryOp("=",Id("a"),CallExpr(Id("func1"),[BinaryOp("*",ArrayCell(Id("arr"),IntLiteral(2)),ArrayCell(Id("arr"),IntLiteral(3))),BinaryOp("/",ArrayCell(Id("arr"),IntLiteral(0)),ArrayCell(Id("arr"),IntLiteral(1)))]))])),If(IntLiteral(10),Dowhile([IntLiteral(11)],IntLiteral(13)),CallExpr(Id("func2"),[IntLiteral(14)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,368))

	def test_stmtexpcombine_14(self):
		input = """float __(){
			break;
			{
				continue;
				return;
			}
			for (_;_;_) if (_) _; else if (__) __; else do _; __; ___; while _;
			return -5.2e-2 * toFloat(___);
		}"""
		expect = str(Program([FuncDecl(Id("__"),[],FloatType(),Block([Break(),Block([Continue(),Return()]),For(Id("_"),Id("_"),Id("_"),If(Id("_"),Id("_"),If(Id("__"),Id("__"),Dowhile([Id("_"),Id("__"),Id("___")],Id("_"))))),Return(BinaryOp("*",UnaryOp("-",FloatLiteral(0.052)),CallExpr(Id("toFloat"),[Id("___")])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,369))

#TEST_ALL===========================================================================================(10)
	def test_all_0(self):
		input = """int[] foo(int a[], int b, boolean flag) {
			{
				float c, d, e[100];
				string str;
			}
			if (a[1]) a[2] = toString(a[2])[a[3]];
		}
		int a[10], b[20], c;"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType()),VarDecl("flag",BoolType())],ArrayPointerType(IntType()),Block([Block([VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("e",ArrayType(100,FloatType())),VarDecl("str",StringType())]),If(ArrayCell(Id("a"),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(CallExpr(Id("toString"),[ArrayCell(Id("a"),IntLiteral(2))]),ArrayCell(Id("a"),IntLiteral(3)))))])),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(20,IntType())),VarDecl("c",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,370))

	def test_all_1(self):
		input = """float a, b[0009], c[00012];
		boolean func(int _[], int d) {
			if (_[00] + .6e3 < _[01] * d) return func(_, d + 10);
			for (i; i >= 0010; i = i - 2) {
				do _[00] = _[001];
				while !!!!___;
				if (_[0]) break;
			}
		}"""
		expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",ArrayType(9,FloatType())),VarDecl("c",ArrayType(12,FloatType())),FuncDecl(Id("func"),[VarDecl("_",ArrayPointerType(IntType())),VarDecl("d",IntType())],BoolType(),Block([If(BinaryOp("<",BinaryOp("+",ArrayCell(Id("_"),IntLiteral(0)),FloatLiteral(600.0)),BinaryOp("*",ArrayCell(Id("_"),IntLiteral(1)),Id("d"))),Return(CallExpr(Id("func"),[Id("_"),BinaryOp("+",Id("d"),IntLiteral(10))]))),For(Id("i"),BinaryOp(">=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(2))),Block([Dowhile([BinaryOp("=",ArrayCell(Id("_"),IntLiteral(0)),ArrayCell(Id("_"),IntLiteral(1)))],UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("___")))))),If(ArrayCell(Id("_"),IntLiteral(0)),Break())]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,371))

	def test_all_2(self):
		input = """int main() {
			int a, b[10];
			gaugau(a);
			meomeo(2e1 + b[1]*b[2]);
			{
				boolean flag[5], a, b;
				if (flag[01] <= a = random(1, 10)) print(a);
				return a;
			}
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),CallExpr(Id("gaugau"),[Id("a")]),CallExpr(Id("meomeo"),[BinaryOp("+",FloatLiteral(20.0),BinaryOp("*",ArrayCell(Id("b"),IntLiteral(1)),ArrayCell(Id("b"),IntLiteral(2))))]),Block([VarDecl("flag",ArrayType(5,BoolType())),VarDecl("a",BoolType()),VarDecl("b",BoolType()),If(BinaryOp("=",BinaryOp("<=",ArrayCell(Id("flag"),IntLiteral(1)),Id("a")),CallExpr(Id("random"),[IntLiteral(1),IntLiteral(10)])),CallExpr(Id("print"),[Id("a")])),Return(Id("a"))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,372))

	def test_all_3(self):
		input = """string str[00009], char;
		int main() {
			for (FALSE; TRUE; false) {
				if (TRUE == true) break;
				else do falseTrueTrueFalse(TRUE, false);
				while (true >= false);
			}
			{{
				a = b = c = str[007] + 777;
			}}
		}
		"""
		expect = str(Program([VarDecl("str",ArrayType(9,StringType())),VarDecl("char",StringType()),FuncDecl(Id("main"),[],IntType(),Block([For(Id("FALSE"),Id("TRUE"),BooleanLiteral(False),Block([If(BinaryOp("==",Id("TRUE"),BooleanLiteral(True)),Break(),Dowhile([CallExpr(Id("falseTrueTrueFalse"),[Id("TRUE"),BooleanLiteral(False)])],BinaryOp(">=",BooleanLiteral(True),BooleanLiteral(False))))])),Block([Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("+",ArrayCell(Id("str"),IntLiteral(7)),IntLiteral(777)))))])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,373))

	def test_all_4(self):
		input = """float calc(float a[]) {
			float result;
			result = .8E2 * .8e-4 + mul(a[0], a[1]);
			float b[4], c;
			b = calc(a) + 8e-6 * 007;
			{
				float result;
				result = -8.1e-5 * 6 + 1e-2;
			}
			return result * 000003 - 5.1E2;	
		}"""
		expect = str(Program([FuncDecl(Id("calc"),[VarDecl("a",ArrayPointerType(FloatType()))],FloatType(),Block([VarDecl("result",FloatType()),BinaryOp("=",Id("result"),BinaryOp("+",BinaryOp("*",FloatLiteral(80.0),FloatLiteral(8e-05)),CallExpr(Id("mul"),[ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("a"),IntLiteral(1))]))),VarDecl("b",ArrayType(4,FloatType())),VarDecl("c",FloatType()),BinaryOp("=",Id("b"),BinaryOp("+",CallExpr(Id("calc"),[Id("a")]),BinaryOp("*",FloatLiteral(8e-06),IntLiteral(7)))),Block([VarDecl("result",FloatType()),BinaryOp("=",Id("result"),BinaryOp("+",BinaryOp("*",UnaryOp("-",FloatLiteral(8.1e-05)),IntLiteral(6)),FloatLiteral(0.01)))]),Return(BinaryOp("-",BinaryOp("*",Id("result"),IntLiteral(3)),FloatLiteral(510.0)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,374))

	def test_all_5(self):
		input = """float a, b, c[10];
		void main() {
			for (true; double(i) < 110; a + b <= c + d) {
				{
					boolean a[10], b, c;
					string str;
					str = str + toString(i) + " ";
				}
				if (triple(i) < 100) continue;
				else break;
			}
		}"""
		expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",ArrayType(10,FloatType())),FuncDecl(Id("main"),[],VoidType(),Block([For(BooleanLiteral(True),BinaryOp("<",CallExpr(Id("double"),[Id("i")]),IntLiteral(110)),BinaryOp("<=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",Id("c"),Id("d"))),Block([Block([VarDecl("a",ArrayType(10,BoolType())),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("str",StringType()),BinaryOp("=",Id("str"),BinaryOp("+",BinaryOp("+",Id("str"),CallExpr(Id("toString"),[Id("i")])),StringLiteral(" ")))]),If(BinaryOp("<",CallExpr(Id("triple"),[Id("i")]),IntLiteral(100)),Continue(),Break())]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,375))

	def test_all_6(self):
		input = """/* func1 implementation */
		int[] func1(int a, int b[]) {
			func2(a, b, b[b[3]]);						//call func2 
			a = b[0] * 1e-3 + 9;
			return b;
		}
		/*
		func2 implementation
		*/
		void func2(int a, int b[], int n) {
			func1(b[b[1]] + a, b);						//call func1
			return;
		}"""
		expect = str(Program([FuncDecl(Id("func1"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([CallExpr(Id("func2"),[Id("a"),Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(3)))]),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("*",ArrayCell(Id("b"),IntLiteral(0)),FloatLiteral(0.001)),IntLiteral(9))),Return(Id("b"))])),FuncDecl(Id("func2"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType())),VarDecl("n",IntType())],VoidType(),Block([CallExpr(Id("func1"),[BinaryOp("+",ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(1))),Id("a")),Id("b")]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,376))

	def test_all_7(self):
		input = """boolean flag[100], f;
		int main() {
			{
				int flag;
				flag = false || true || flag[flag[2]];
				if (flag) f = decode("00010110110001111");
			}
			int g, h, k;
			k = decode("9713","97139","1739","14863","1739") == "CONAN";
			print(k);
			return;
		}"""
		expect = str(Program([VarDecl("flag",ArrayType(100,BoolType())),VarDecl("f",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl("flag",IntType()),BinaryOp("=",Id("flag"),BinaryOp("||",BinaryOp("||",BooleanLiteral(False),BooleanLiteral(True)),ArrayCell(Id("flag"),ArrayCell(Id("flag"),IntLiteral(2))))),If(Id("flag"),BinaryOp("=",Id("f"),CallExpr(Id("decode"),[StringLiteral("00010110110001111")])))]),VarDecl("g",IntType()),VarDecl("h",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("k"),BinaryOp("==",CallExpr(Id("decode"),[StringLiteral("9713"),StringLiteral("97139"),StringLiteral("1739"),StringLiteral("14863"),StringLiteral("1739")]),StringLiteral("CONAN"))),CallExpr(Id("print"),[Id("k")]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,377))

	def test_all_8(self):
		input = """int a, b, c[2];
		void main(){
			int a, b[2];
			{
				int b, c[3];
				{
					int c, a[4];
					for (c; c < 3E2; c = c + 2)
						do if (c / 2 > 100) c = foo(b[b[2]]*3)[10*5e2*foo(1)[a[2]]];
						while true;
				}
			}
			releaseMutex();
		}"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(2,IntType())),Block([VarDecl("b",IntType()),VarDecl("c",ArrayType(3,IntType())),Block([VarDecl("c",IntType()),VarDecl("a",ArrayType(4,IntType())),For(Id("c"),BinaryOp("<",Id("c"),FloatLiteral(300.0)),BinaryOp("=",Id("c"),BinaryOp("+",Id("c"),IntLiteral(2))),Dowhile([If(BinaryOp(">",BinaryOp("/",Id("c"),IntLiteral(2)),IntLiteral(100)),BinaryOp("=",Id("c"),ArrayCell(CallExpr(Id("foo"),[BinaryOp("*",ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))]),BinaryOp("*",BinaryOp("*",IntLiteral(10),FloatLiteral(500.0)),ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),ArrayCell(Id("a"),IntLiteral(2)))))))],BooleanLiteral(True)))])]),CallExpr(Id("releaseMutex"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,378))

	def test_all_9(self):
		input = """string str[00001111], s1, s2;
		int a, b, c[2];
		int main(string argv) {
			for (1; i < 1e4; i = i * 2) {
				if (i % 3 * 4 == 0 + 5) break;
				else if (foo(i)[i * 2] < 2E3) continue;
				do a = double(b[b[2]]);
				while a < 2e2;
			}
			a[2] = str[a[001]] = "Meitantei" + " " + "Conan";
			a[002] = a[2] + "\\n" + "I love U!";
			printf("Thank u so much!");
			return 0;
		}"""
		expect = str(Program([VarDecl("str",ArrayType(1111,StringType())),VarDecl("s1",StringType()),VarDecl("s2",StringType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType())),FuncDecl(Id("main"),[VarDecl("argv",StringType())],IntType(),Block([For(IntLiteral(1),BinaryOp("<",Id("i"),FloatLiteral(10000.0)),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))),Block([If(BinaryOp("==",BinaryOp("*",BinaryOp("%",Id("i"),IntLiteral(3)),IntLiteral(4)),BinaryOp("+",IntLiteral(0),IntLiteral(5))),Break(),If(BinaryOp("<",ArrayCell(CallExpr(Id("foo"),[Id("i")]),BinaryOp("*",Id("i"),IntLiteral(2))),FloatLiteral(2000.0)),Continue())),Dowhile([BinaryOp("=",Id("a"),CallExpr(Id("double"),[ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(2)))]))],BinaryOp("<",Id("a"),FloatLiteral(200.0)))])),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(2)),BinaryOp("=",ArrayCell(Id("str"),ArrayCell(Id("a"),IntLiteral(1))),BinaryOp("+",BinaryOp("+",StringLiteral("Meitantei"),StringLiteral(" ")),StringLiteral("Conan")))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(2)),BinaryOp("+",BinaryOp("+",ArrayCell(Id("a"),IntLiteral(2)),StringLiteral("\\n")),StringLiteral("I love U!"))),CallExpr(Id("printf"),[StringLiteral("Thank u so much!")]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,379))

#TEST_SIMPLEPROGRAM=================================================================================(10)
	def test_siprogram_0(self):
		input = """
		/*
		Hello World Program!
		*/
		int main()
        {
            printf("Hello, World!\\n");
            return 0;
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Hello, World!\\n")]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,380))

	def test_siprogram_1(self):
		input = """//Print entered number program
		int main()
        {
            int number;
            printf("Enter an integer: ");
            scanf("%d", number);
            printf("You entered: %d", number);
            return 0;
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("number")]),CallExpr(Id("printf"),[StringLiteral("You entered: %d"),Id("number")]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,381))

	def test_siprogram_2(self):
		input = """//Simple expression
		int main()
        {
            int a[2], b;
            a[0] = 2 * b + func(a[1])[2];
            a[1] = 0012 * 2e2;
            return 0;
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(2,IntType())),VarDecl("b",IntType()),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("b")),ArrayCell(CallExpr(Id("func"),[ArrayCell(Id("a"),IntLiteral(1))]),IntLiteral(2)))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),BinaryOp("*",IntLiteral(12),FloatLiteral(200.0))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,382))

	def test_siprogram_3(self):
		input = """
		void swap(int a, int b)
        {
            int temp;
            temp = a;
            a = b;
            b = temp;
        }

		void main() {
			int a[2];
			a[0] = 1;
			a[1] = 2e2;
			swap(a[0], a[1]);
			return;
		}"""
		expect = str(Program([FuncDecl(Id("swap"),[VarDecl("a",IntType()),VarDecl("b",IntType())],VoidType(),Block([VarDecl("temp",IntType()),BinaryOp("=",Id("temp"),Id("a")),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("temp"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(2,IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),FloatLiteral(200.0)),CallExpr(Id("swap"),[ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("a"),IntLiteral(1))]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,383))

	def test_siprogram_4(self):
		input = """
		boolean flag[2], q;
        int main()
        {
            q = true;
			string str;
			str = "It's over!";
            if (flag[0]) if (flag[1]) printf(str);
            return 0;
        }"""
		expect = str(Program([VarDecl("flag",ArrayType(2,BoolType())),VarDecl("q",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("q"),BooleanLiteral(True)),VarDecl("str",StringType()),BinaryOp("=",Id("str"),StringLiteral("It's over!")),If(ArrayCell(Id("flag"),IntLiteral(0)),If(ArrayCell(Id("flag"),IntLiteral(1)),CallExpr(Id("printf"),[Id("str")]))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,384))

	def test_siprogram_5(self):
		input = """
		int i, a[10];
        int[] foo() {
			{
				int a[10], i;
				for (i = 0; i < 10; i = i + 1) a[i] = random(1, 100);
				return a;
			}
		}

        void main(){
            i = 9;
            a = foo();
			i = i + foo()[2];
            if (i < 9 && i > a[1]) print("True");				//check if i < 9 and i > a[1]
            else print("False");
        }"""
		expect = str(Program([VarDecl("i",IntType()),VarDecl("a",ArrayType(10,IntType())),FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("a"),Id("i")),CallExpr(Id("random"),[IntLiteral(1),IntLiteral(100)]))),Return(Id("a"))])])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),IntLiteral(9)),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(2)))),If(BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(9)),BinaryOp(">",Id("i"),ArrayCell(Id("a"),IntLiteral(1)))),CallExpr(Id("print"),[StringLiteral("True")]),CallExpr(Id("print"),[StringLiteral("False")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,385))

	def test_siprogram_6(self):
		input = """
		//Check whether an integer is odd or even
        int main()
        {
            int n, m[10];
            printf("Enter an integer: ");
            scanf("%d", n);
            if (n%2 == 0) printf("%d is an even integer.",n);
            else printf("%d is an odd integer.",n);
            return 0;
        }"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("m",ArrayType(10,IntType())),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),If(BinaryOp("==",BinaryOp("%",Id("n"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is an even integer."),Id("n")]),CallExpr(Id("printf"),[StringLiteral("%d is an odd integer."),Id("n")])),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,386))

	def test_siprogram_7(self):
		input = """
		boolean flag;
        int round(float a) {/*???!!!*/}
        void main() {
            float number;
            flag = true;
            do {
                number = random(1, 200) / 10;
                if (number == round(number)) flag = false;
            } 
            while (flag);
            printf("%d", number);
			return;
        }"""
		expect = str(Program([VarDecl("flag",BoolType()),FuncDecl(Id("round"),[VarDecl("a",FloatType())],IntType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("number",FloatType()),BinaryOp("=",Id("flag"),BooleanLiteral(True)),Dowhile([Block([BinaryOp("=",Id("number"),BinaryOp("/",CallExpr(Id("random"),[IntLiteral(1),IntLiteral(200)]),IntLiteral(10))),If(BinaryOp("==",Id("number"),CallExpr(Id("round"),[Id("number")])),BinaryOp("=",Id("flag"),BooleanLiteral(False)))])],Id("flag")),CallExpr(Id("printf"),[StringLiteral("%d"),Id("number")]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,387))

	def test_siprogram_8(self):
		input = """
		int main()
		{
    		int a;
    		float b;
    		boolean c;
    		printf("Size of int = %ld bytes \\n", sizeof(a));
    		printf("Size of float = %ld bytes\\n", sizeof(b));
    		printf("Size of boolean = %ld bytes\\n", sizeof(c));
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",BoolType()),CallExpr(Id("printf"),[StringLiteral("Size of int = %ld bytes \\n"),CallExpr(Id("sizeof"),[Id("a")])]),CallExpr(Id("printf"),[StringLiteral("Size of float = %ld bytes\\n"),CallExpr(Id("sizeof"),[Id("b")])]),CallExpr(Id("printf"),[StringLiteral("Size of boolean = %ld bytes\\n"),CallExpr(Id("sizeof"),[Id("c")])]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,388))

	def test_siprogram_9(self):
		input = """
		int main()
		{
    		int n, i;
    		printf("Enter an integer: ");
    		scanf("%d", n);
    		for (i = 1; i <= 10; i = i + 1)
    		{
        		printf("%d * %d = %d \\n", n, i, n*i);
    		}
    
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("%d * %d = %d \\n"),Id("n"),Id("i"),BinaryOp("*",Id("n"),Id("i"))])])),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,389))

#TEST_COMPLEXPROGRAM================================================================================(10)
	def test_coprogram_0(self):
		input = """
		int main()
		{
    		int n, count;
			count = 0;
    		printf("Enter an integer: ");
    		scanf("%d", n);
			do {
        		n = n / 10;
        		count = count + 1;
    		}
    		while (n != 0);
    
    		printf("Number of digits: %d", count);
			return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),Dowhile([Block([BinaryOp("=",Id("n"),BinaryOp("/",Id("n"),IntLiteral(10))),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])],BinaryOp("!=",Id("n"),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("Number of digits: %d"),Id("count")]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,390))

	def test_coprogram_1(self):
		input = """
		int main()
		{
    		int i, n;
    		float arr[100];
    		printf("Enter total number of elements(1 to 100): ");
    		scanf("%d", n);
    		printf("\\n");
    		//Stores number entered by the user
    		for (i = 0; i < n; i = i + 1)
    		{
       			printf("Enter Number %d: ", i+1);
       			scanf("%f", arr[i]);
    		}
    		//Loop to store largest number to arr[0]
    		for (i = 1; i < n; i = i + 1)
    		{
       			if (arr[0] < arr[i])					//Change < to > if you want to find the smallest element
           			arr[0] = arr[i];
    		}
    		printf("Largest element = %.2f", arr[0]);
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("n",IntType()),VarDecl("arr",ArrayType(100,FloatType())),CallExpr(Id("printf"),[StringLiteral("Enter total number of elements(1 to 100): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral("\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Enter Number %d: "),BinaryOp("+",Id("i"),IntLiteral(1))]),CallExpr(Id("scanf"),[StringLiteral("%f"),ArrayCell(Id("arr"),Id("i"))])])),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<",ArrayCell(Id("arr"),IntLiteral(0)),ArrayCell(Id("arr"),Id("i"))),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),ArrayCell(Id("arr"),Id("i"))))])),CallExpr(Id("printf"),[StringLiteral("Largest element = %.2f"),ArrayCell(Id("arr"),IntLiteral(0))]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,391))

	def test_coprogram_2(self):
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
		}"""
		expect = str(Program([FuncDecl(Id("convertBinarytoOctal"),[VarDecl("binaryNumber",IntType())],IntType(),Block([VarDecl("octalNumber",IntType()),VarDecl("decimalNumber",IntType()),VarDecl("i",IntType()),BinaryOp("=",Id("octalNumber"),BinaryOp("=",Id("decimalNumber"),BinaryOp("=",Id("i"),IntLiteral(0)))),Dowhile([Block([BinaryOp("=",Id("decimalNumber"),BinaryOp("+",Id("decimalNumber"),BinaryOp("*",BinaryOp("%",Id("binaryNumber"),IntLiteral(10)),CallExpr(Id("pow"),[IntLiteral(2),Id("i")])))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("binaryNumber"),BinaryOp("/",Id("binaryNumber"),IntLiteral(10)))])],BinaryOp("!=",Id("binaryNumber"),IntLiteral(0))),BinaryOp("=",Id("i"),IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("octalNumber"),BinaryOp("+",Id("octalNumber"),BinaryOp("*",BinaryOp("%",Id("decimalNumber"),IntLiteral(8)),Id("i")))),BinaryOp("=",Id("decimalNumber"),BinaryOp("/",Id("decimalNumber"),IntLiteral(8))),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(10)))])],BinaryOp("!=",Id("decimalNumber"),IntLiteral(0))),Return(Id("octalNumber"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,392))

	def test_coprogram_3(self):
		input = """
		int main()
		{
    		int year;
    		printf("Enter a year: ");
    		scanf("%d", year);
    		if (year % 4 == 0)
    		{
        		if (year % 100 == 0)
        		{
            	//Year is divisible by 400, hence the year is a leap year
            	if (year % 400 == 0)
                	printf("%d is a leap year.", year);
            	else
                	printf("%d is not a leap year.", year);
        		}
        		else
            		printf("%d is a leap year.", year);
    		}
    		else
        		printf("%d is not a leap year.", year);
    
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("year",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a year: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("year")]),If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(4)),IntLiteral(0)),Block([If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(100)),IntLiteral(0)),Block([If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(400)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a leap year."),Id("year")]),CallExpr(Id("printf"),[StringLiteral("%d is not a leap year."),Id("year")]))]),CallExpr(Id("printf"),[StringLiteral("%d is a leap year."),Id("year")]))]),CallExpr(Id("printf"),[StringLiteral("%d is not a leap year."),Id("year")])),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,393))

	def test_coprogram_4(self):
		input = """
		int main()
		{
    		float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    		printf("Enter coefficients a, b and c: ");
    		scanf("%f %f %f", a, b, c);
    		discriminant = b*b - 4*a*c;
    		//condition for real and different roots
    		if (discriminant > 0)
    		{
    			//sqrt() function returns square root
        		root1 = (-b+sqrt(discriminant))/(2*a);
        		root2 = (-b-sqrt(discriminant))/(2*a);
        		printf("root1 = %.2f and root2 = %.2f",root1 , root2);
    		}
    		//condition for real and equal roots
    		else if (discriminant == 0)
    		{
        		root1 = root2 = -b/(2*a);
        		printf("root1 = root2 = %.2lf;", root1);
    		}
    		//if roots are not real 
    		else
    		{
        		realPart = -b/(2*a);
        		imaginaryPart = sqrt(-discriminant)/(2*a);
        		printf("root1 = %.2f+%.2fi and root2 = %.2f-%.2fi", realPart, imaginaryPart, realPart, imaginaryPart);
    		}
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("discriminant",FloatType()),VarDecl("root1",FloatType()),VarDecl("root2",FloatType()),VarDecl("realPart",FloatType()),VarDecl("imaginaryPart",FloatType()),CallExpr(Id("printf"),[StringLiteral("Enter coefficients a, b and c: ")]),CallExpr(Id("scanf"),[StringLiteral("%f %f %f"),Id("a"),Id("b"),Id("c")]),BinaryOp("=",Id("discriminant"),BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c")))),If(BinaryOp(">",Id("discriminant"),IntLiteral(0)),Block([BinaryOp("=",Id("root1"),BinaryOp("/",BinaryOp("+",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("discriminant")])),BinaryOp("*",IntLiteral(2),Id("a")))),BinaryOp("=",Id("root2"),BinaryOp("/",BinaryOp("-",UnaryOp("-",Id("b")),CallExpr(Id("sqrt"),[Id("discriminant")])),BinaryOp("*",IntLiteral(2),Id("a")))),CallExpr(Id("printf"),[StringLiteral("root1 = %.2f and root2 = %.2f"),Id("root1"),Id("root2")])]),If(BinaryOp("==",Id("discriminant"),IntLiteral(0)),Block([BinaryOp("=",Id("root1"),BinaryOp("=",Id("root2"),BinaryOp("/",UnaryOp("-",Id("b")),BinaryOp("*",IntLiteral(2),Id("a"))))),CallExpr(Id("printf"),[StringLiteral("root1 = root2 = %.2lf;"),Id("root1")])]),Block([BinaryOp("=",Id("realPart"),BinaryOp("/",UnaryOp("-",Id("b")),BinaryOp("*",IntLiteral(2),Id("a")))),BinaryOp("=",Id("imaginaryPart"),BinaryOp("/",CallExpr(Id("sqrt"),[UnaryOp("-",Id("discriminant"))]),BinaryOp("*",IntLiteral(2),Id("a")))),CallExpr(Id("printf"),[StringLiteral("root1 = %.2f+%.2fi and root2 = %.2f-%.2fi"),Id("realPart"),Id("imaginaryPart"),Id("realPart"),Id("imaginaryPart")])]))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,394))

	def test_coprogram_5(self):
		input = """
		//Check if a number is prime number

		boolean isPrime(int n)
        {
            int j, flag;
            for (j = 2; j <= n/2; j = j + 1)
            {
                if (n % j == 0)
                {
                    flag = 0;
                    break;
                }
            }
            return flag;
        }

		int main() {
			int n;
			scanf("%d", n);
			if (isPrime(n)) printf("%d is a prime number.", n);
			else printf("%d is not a prime number.", n);
			return 0;
		}"""
		expect = str(Program([FuncDecl(Id("isPrime"),[VarDecl("n",IntType())],BoolType(),Block([VarDecl("j",IntType()),VarDecl("flag",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(2)),BinaryOp("<=",Id("j"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("j")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),Break()]))])),Return(Id("flag"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),If(CallExpr(Id("isPrime"),[Id("n")]),CallExpr(Id("printf"),[StringLiteral("%d is a prime number."),Id("n")]),CallExpr(Id("printf"),[StringLiteral("%d is not a prime number."),Id("n")])),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,395))

	def test_coprogram_6(self):
		input = """
		/*Enter and print an array of integers*/
		int a[10], b;
		void enter(int a[], int n) {
			int i, j[2];
			for (i = 0; i < n; i = i + 1) {
				printf("Enter an integer: ");
            	scanf("%d", a[i]);
			}
		}
		void print(int a[], int n) {
			int i;
			for (i = 0; i < n; i = i + 1) print("%d, ", a[i]);
		}
		int main() {
			enter(a, 10);
			print(a, 10);
			return 0;
		}
		"""
		expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),FuncDecl(Id("enter"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("n",IntType())],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",ArrayType(2,IntType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(Id("a"),Id("i"))])]))])),FuncDecl(Id("print"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("n",IntType())],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("print"),[StringLiteral("%d, "),ArrayCell(Id("a"),Id("i"))]))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("enter"),[Id("a"),IntLiteral(10)]),CallExpr(Id("print"),[Id("a"),IntLiteral(10)]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,396))

	def test_coprogram_7(self):
		input = """
		int a[10], b;
		string[] generate() {
			string list[10];
			insert("YESTERDAY LOVE", 0, list);
			insert("Togetsukyou ~Kimi Omou~", 0, list);
			insert("always", 0, list);
			insert("Growing of my heart", 0, list);
			insert("Secret of my heart", 0, list);
			insert("Your Best Friend", 0, list);
			insert("TRY AGAIN", 0, list);
			insert("Barairo no Jinsei", 0, list);
			insert("Time after time ~Hana Mau Machi de~", 0, list);
			insert("Kimi to Koi no Mama de Owarenai Itsumo no Yume no Mama ja Irarenai", 0, list);
			return list;
		}

		int main() {
			int i;
			{
				string listMaiKxConanCollaboration;
				listMaiKxConanCollaboration = generate();
				for (i = 0; i < 10; i = i + 1) {
					printf("%s", listMaiKxConanCollaboration[i]);
					if (true) printf("This song is so good! \\n");
				}
			}
			return 0;
		}
		"""
		expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),FuncDecl(Id("generate"),[],ArrayPointerType(StringType()),Block([VarDecl("list",ArrayType(10,StringType())),CallExpr(Id("insert"),[StringLiteral("YESTERDAY LOVE"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Togetsukyou ~Kimi Omou~"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("always"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Growing of my heart"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Secret of my heart"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Your Best Friend"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("TRY AGAIN"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Barairo no Jinsei"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Time after time ~Hana Mau Machi de~"),IntLiteral(0),Id("list")]),CallExpr(Id("insert"),[StringLiteral("Kimi to Koi no Mama de Owarenai Itsumo no Yume no Mama ja Irarenai"),IntLiteral(0),Id("list")]),Return(Id("list"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),Block([VarDecl("listMaiKxConanCollaboration",StringType()),BinaryOp("=",Id("listMaiKxConanCollaboration"),CallExpr(Id("generate"),[])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("%s"),ArrayCell(Id("listMaiKxConanCollaboration"),Id("i"))]),If(BooleanLiteral(True),CallExpr(Id("printf"),[StringLiteral("This song is so good! \\n")]))]))]),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,397))

	def test_coprogram_8(self):
		input = """
		int i ;
        int f(){
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
        }
		"""
		expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,398))

	def test_coprogram_9(self):
		input = """
		int main()
		{
    		int n, reversedInteger, remainder, originalInteger;
			reversedInteger = 0;
    		printf("Enter an integer: ");
    		scanf("%d", n);
    		originalInteger = n;
    		//reversed integer is stored in variable 
			do
        		remainder = n%10;
        		reversedInteger = reversedInteger*10 + remainder;
        		n = n / 10;
    		while (n != 0);
    		
    		//palindrome if orignalInteger and reversedInteger are equal
    		if (originalInteger == reversedInteger)
        		printf("%d is a palindrome.", originalInteger);
    		else
        		printf("%d is not a palindrome.", originalInteger);
    
    		return 0;
		}"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("reversedInteger",IntType()),VarDecl("remainder",IntType()),VarDecl("originalInteger",IntType()),BinaryOp("=",Id("reversedInteger"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),BinaryOp("=",Id("originalInteger"),Id("n")),Dowhile([BinaryOp("=",Id("remainder"),BinaryOp("%",Id("n"),IntLiteral(10))),BinaryOp("=",Id("reversedInteger"),BinaryOp("+",BinaryOp("*",Id("reversedInteger"),IntLiteral(10)),Id("remainder"))),BinaryOp("=",Id("n"),BinaryOp("/",Id("n"),IntLiteral(10)))],BinaryOp("!=",Id("n"),IntLiteral(0))),If(BinaryOp("==",Id("originalInteger"),Id("reversedInteger")),CallExpr(Id("printf"),[StringLiteral("%d is a palindrome."),Id("originalInteger")]),CallExpr(Id("printf"),[StringLiteral("%d is not a palindrome."),Id("originalInteger")])),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,399))
