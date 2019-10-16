import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test_vardec_0(self):
		input = """
		int main()
		{
			int a;
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,300))

	def test_vardec_1(self):
		input = """float x,y[12],z;
		"""
		expect = str(Program([VarDecl("x",FloatType()),VarDecl("y",ArrayType(12,FloatType())),VarDecl("z",FloatType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,301))

	def test_vardec_2(self):
		input = """
		int a,b,c;

		int main()
		{
			int d,e,f;
		}
		"""
		expect=str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,302))

	def test_vardec_3(self):
		input = """string b,c[123],d,e[1234534];
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,303))

	def test_vardec_4(self):
		input = """boolean b,c[123],d,e[1234534];
		"""
		expect = str(Program([VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,304))

	def test_vardec_5(self):
		input = """
		string b,c[123],d,e[1234534];
		boolean b,c[123],d,e[1234534];
		int a,b,c;
		float x,y,z;
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,305))

	def test_vardec_6(self):
		input = """int main()
		{
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}

		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,306))

	def test_vardec_7(self):
		input = """int main(){
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
			int a[321],b,c[34];
			float x,y,z;

			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
			int a,b,c;
			float x,y[43],z,q[32];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),VarDecl("a",ArrayType(321,IntType())),VarDecl("b",IntType()),VarDecl("c",ArrayType(34,IntType())),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",ArrayType(43,FloatType())),VarDecl("z",FloatType()),VarDecl("q",ArrayType(32,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,307))

	def test_vardec_8(self):
		input = """int main()
		{
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
			int a,b,c;
			float x,y,z;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,308))

	def test_vardec_9(self):
		input = """int main()
		{	
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,309))

	def test_vardec_10(self):
		input = """
		int enter()
		{	
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
			string b,c[123],d,e[1234534];
		}	
	

		int main()
		{
			int a,b,c;
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("enter"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType()))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,310))

	def test_vardec_11(self):
		input = """
		int print()
		{	
		}	
	

		void join()
		{
		}

		int enter()
		{	
		}	
	

		int main()
		{
			int a,b,c;
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("print"),[],IntType(),Block([])),FuncDecl(Id("join"),[],VoidType(),Block([])),FuncDecl(Id("enter"),[],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,311))

	def test_vardec_12(self):
		input = """
		int print()
		{	
			string b,c[123],d,e[1234534];
		}	
	

		void join()
		{
			int a,b,c;
		}

		void fit()
		{
			int a,b,c;
		}

		int enter()
		{	
		}	
	

		int main()
		{
			boolean b,c[123],d,e[1234534];
		}

		"""
		expect = str(Program([FuncDecl(Id("print"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType()))])),FuncDecl(Id("join"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())])),FuncDecl(Id("fit"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())])),FuncDecl(Id("enter"),[],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,312))

	def test_vardec_13(self):
		input = """int main()
		{
			int a,b,c;
			int a,b,c;
			int a,b,c;
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,313))

	def test_vardec_14(self):
		input = """string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,314))

	def test_vardec_15(self):
		input = """
		string b,c[123],d,e[1234534];
		boolean b,c[123],d,e[1234534];
		string b,c[123],d,e[1234534];
		float x,y,z;
		string b,c[123],d,e[1234534];
		boolean b,c[123],d,e[1234534];
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,315))

	def test_vardec_16(self):
		input = """int main(float q[]){
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("q",ArrayPointerType(FloatType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,316))

	def test_vardec_17(self):
		input = """int b(){}
		"""
		expect = str(Program([FuncDecl(Id("b"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,317))

	def test_vardec_18(self):
		input = """
		int main()
		{
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,318))

	def test_vardec_19(self):
		input = """
		float x,y,z;

		int main()
		{
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,319))

	def test_vardec_20(self):
		input = """
		boolean c[123],e[1234534];

		int main()
		{
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([VarDecl("c",ArrayType(123,BoolType())),VarDecl("e",ArrayType(1234534,BoolType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,320))

	def test_vardec_21(self):
		input = """
		string b,c[123],d,e[1234534];

		int main()
		{
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,321))

	def test_vardec_22(self):
		input = """
		int main()
		{
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,322))

	def test_vardec_23(self):
		input = """
		string b,c[123],d,e[1234534];

		int main()
		{
			float x,y,z;
			string b,c[123],d,e[5413];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(5413,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,323))

	def test_vardec_24(self):
		input = """
		int main()
		{
			float x,y,z[43];
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",ArrayType(43,FloatType())),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,324))

	def test_funcdec_25(self):
		input = """
		void enter()
		{}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,325))

	def test_funcdec_26(self):
		input = """
		string enter()
		{}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],StringType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,326))

	def test_funcdec_27(self):
		input = """
		boolean enter(){}
	
		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],BoolType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,327))

	def test_funcdec_28(self):
		input = """
		float enter(){}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],FloatType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,328))

	def test_funcdec_29(self):
		input = """
		string enter(){}
		boolean enter(){}
		float enter(){}
		void enter(){}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],StringType(),Block([])),FuncDecl(Id("enter"),[],BoolType(),Block([])),FuncDecl(Id("enter"),[],FloatType(),Block([])),FuncDecl(Id("enter"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,329))

	def test_funcdec_30(self):
		input = """
		int main(int a,int b)
		{}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,330))

	def test_funcdec_31(self):
		input = """int main(int a,int b[],int c[],int d,int e[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType())),VarDecl("c",ArrayPointerType(IntType())),VarDecl("d",IntType()),VarDecl("e",ArrayPointerType(IntType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,331))

	def test_funcdec_32(self):
		input = """int main(float a,float b){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",FloatType()),VarDecl("b",FloatType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,332))

	def test_funcdec_33(self):
		input = """int main(float a,float b[],float c[],float d,float e[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",FloatType()),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",FloatType()),VarDecl("e",ArrayPointerType(FloatType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,333))

	def test_funcdec_34(self):
		input = """int main(string a,string b){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",StringType()),VarDecl("b",StringType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,334))

	def test_funcdec_35(self):
		input = """int main(string a,string b[],string c[],string d,string e[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",StringType()),VarDecl("b",ArrayPointerType(StringType())),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayPointerType(StringType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,335))

	def test_funcdec_36(self):
		input = """int main(boolean a,boolean b){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",BoolType()),VarDecl("b",BoolType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,336))

	def test_funcdec_37(self):
		input = """int main(boolean a,boolean b[],boolean c[],boolean d,boolean e[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",BoolType()),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayPointerType(BoolType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,337))

	def test_funcdec_38(self):
		input = """int main(int a,float b,string c,boolean d){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,338))

	def test_funcdec_39(self):
		input = """int main(int a[],float b[],string c[],boolean d[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",ArrayPointerType(BoolType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,339))

	def test_funcdec_40(self):
		input = """int main(int a,float b[],string c,boolean d[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",StringType()),VarDecl("d",ArrayPointerType(BoolType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,340))

	def test_funcdec_41(self):
		input = """
		int main(int a,float b,string c,boolean d){}

		int main(int a,float b[],string c,boolean d[]){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())],IntType(),Block([])),FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",StringType()),VarDecl("d",ArrayPointerType(BoolType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,341))

	def test_funcdec_42(self):
		input = """
		int main(int a[],float b[],string c[],boolean d[]){}

		int main(int a,float b,string c,boolean d){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",ArrayPointerType(BoolType()))],IntType(),Block([])),FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,342))

	def test_funcdec_43(self):
		input = """
		int[] main(int a[],float b[],string c[],boolean d[]){}

		float main(int a[],float b,string c[],boolean d){}
	
		int main(int a,float b,string c,boolean d){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",BoolType())],FloatType(),Block([])),FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,343))

	def test_funcdec_44(self):
		input = """
		int main(){}

		void main(int a[],float b,string c[],boolean d){}
	
		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(StringType())),VarDecl("d",BoolType())],VoidType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,344))

	def test_funcdec_45(self):
		input = """ void foo(int x, int y, float z, string s, int a[]) {
            x = y+c+d;
        }
		"""
		expect=str(Program([FuncDecl(Id("foo"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",FloatType()),VarDecl("s",StringType()),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",Id("x"),BinaryOp("+",BinaryOp("+",Id("y"),Id("c")),Id("d")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,345))

	def test_funcdec_46(self):
		input = """void foo(int x, int y, float z, string s[], int a[]) {
        }
		"""
		expect=str(Program([FuncDecl(Id("foo"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",FloatType()),VarDecl("s",ArrayPointerType(StringType())),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,346))

	def test_funcdec_47(self):
		input = """int main () {
                     int a, b, c;
                   }
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,347))

	def test_funcdec_48(self):
		input = """int main (int b,int c[]) {
                        int a; float a;
                             int c;
                        }
		"""
		expect=str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("c",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("a",IntType()),VarDecl("a",FloatType()),VarDecl("c",IntType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,348))

	def test_funcdec_49(self):
		input = """int _mai_n () {
                                    int a, c[5], d[5], _, _123;
                                    float asdas; boolean x;
                            }
		"""
		expect=str(Program([FuncDecl(Id("_mai_n"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("c",ArrayType(5,IntType())),VarDecl("d",ArrayType(5,IntType())),VarDecl("_",IntType()),VarDecl("_123",IntType()),VarDecl("asdas",FloatType()),VarDecl("x",BoolType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,349))

	def test_stmtdec_50(self):
		input = """int main()
		{
			if (a = 3) a >= 4;
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp(">=",Id("a"),IntLiteral(4)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,350))

	def test_stmtdec_51(self):
		input = """int main()
		{
			if (a > 3) {
                a >= 4;
            }
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(3)),Block([BinaryOp(">=",Id("a"),IntLiteral(4))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,351))

	def test_stmtdec_52(self):
		input = """int main()
		{
			if (a > 3 && a < 5) a = 10;
            else if (a <= 3) a = - a / 2;
            else a = a[2];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(3)),BinaryOp("<",Id("a"),IntLiteral(5))),BinaryOp("=",Id("a"),IntLiteral(10)),If(BinaryOp("<=",Id("a"),IntLiteral(3)),BinaryOp("=",Id("a"),BinaryOp("/",UnaryOp("-",Id("a")),IntLiteral(2))),BinaryOp("=",Id("a"),ArrayCell(Id("a"),IntLiteral(2)))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,352))

	def test_stmtdec_53(self):
		input = """int main()
		{
            if (a < 4) a = 10; else a = foo(3, a[5], !4);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(4)),BinaryOp("=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(3),ArrayCell(Id("a"),IntLiteral(5)),UnaryOp("!",IntLiteral(4))])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,353))

	def test_stmtdec_54(self):
		input = """int main()
		{
            if (number%2) return;
            else numberToBin(number);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("%",Id("number"),IntLiteral(2)),Return(),CallExpr(Id("numberToBin"),[Id("number")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,354))

	def test_stmtdec_55(self):
		input = """int main()
		{
            if (true) a = b;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),BinaryOp("=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,355))

	def test_stmtdec_56(self):
		input = """int main()
		{
			if (abc != cdf) {
                a = b + 1;
                b = c + 1;
                if(a) a = b;
                {
                    ah(2);
                }
            }
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",Id("abc"),Id("cdf")),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),IntLiteral(1))),BinaryOp("=",Id("b"),BinaryOp("+",Id("c"),IntLiteral(1))),If(Id("a"),BinaryOp("=",Id("a"),Id("b"))),Block([CallExpr(Id("ah"),[IntLiteral(2)])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,356))

	def test_stmtdec_57(self):
		input = """int main()
		{
			do
			{
				a=2;
			}
			while (a!=2);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("a"),IntLiteral(2))])],BinaryOp("!=",Id("a"),IntLiteral(2)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,357))

	def test_stmtdec_58(self):
		input = """int main()
		{
			do
    		{}{}
    		while true;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,358))

	def test_stmtdec_59(self):
		input = """int main()
		{
            do do do do i = 0; while(9); while(true); while(false); while(1);
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("i"),IntLiteral(0))],IntLiteral(9))],BooleanLiteral(True))],BooleanLiteral(False))],IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,359))

	def test_stmtdec_60(self):
		input = """int main()
		{
			do 
			{}{}{}{}{}
			while (a==2);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),Block([])],BinaryOp("==",Id("a"),IntLiteral(2)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,360))

	def test_stmtdec_61(self):
		input = """int main()
		{
			do 
			{}
			{
				a=2;
				b=3;
			}
			while (a==2);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([]),Block([BinaryOp("=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(3))])],BinaryOp("==",Id("a"),IntLiteral(2)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,361))

	def test_stmtdec_62(self):
		input = """int main()
		{
			do (3*4); (a==4);
             if (x%2) x = 2; else x = 3;
             {
                for (i = 4; i <5; i = i+2) a=2;
             }
            while (!2);
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("*",IntLiteral(3),IntLiteral(4)),BinaryOp("==",Id("a"),IntLiteral(4)),If(BinaryOp("%",Id("x"),IntLiteral(2)),BinaryOp("=",Id("x"),IntLiteral(2)),BinaryOp("=",Id("x"),IntLiteral(3))),Block([For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),BinaryOp("=",Id("a"),IntLiteral(2)))])],UnaryOp("!",IntLiteral(2)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,362))

	def test_stmtdec_63(self):
		input = """int main()
		{
			do a=1; a=3; a=4; {}{} a=2;
            while (foo());
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp("=",Id("a"),IntLiteral(4)),Block([]),Block([]),BinaryOp("=",Id("a"),IntLiteral(2))],CallExpr(Id("foo"),[]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,363))

	def test_stmtdec_64(self):
		input = """int main()
		{
			for (i=1;i<=5;i=i%2) getPrimeNumber(i);
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("%",Id("i"),IntLiteral(2))),CallExpr(Id("getPrimeNumber"),[Id("i")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,364))

	def test_stmtdec_65(self):
		input = """int main()
		{
           	for (i = 4; i <5; i = i+2) if (x == 2) x= 3;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),If(BinaryOp("==",Id("x"),IntLiteral(2)),BinaryOp("=",Id("x"),IntLiteral(3))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,365))

	def test_stmtdec_66(self):
		input = """int main()
		{
			for (i = 5; i < 6; i == 5) x +2 ;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(5)),BinaryOp("<",Id("i"),IntLiteral(6)),BinaryOp("==",Id("i"),IntLiteral(5)),BinaryOp("+",Id("x"),IntLiteral(2)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,366))

	def test_stmtdec_67(self):
		input = """int main()
		{
			for (i = 4; i < 5; i +2 ){
                if (a = 5) false;
            }
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("+",Id("i"),IntLiteral(2)),Block([If(BinaryOp("=",Id("a"),IntLiteral(5)),BooleanLiteral(False))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,367))

	def test_stmtdec_68(self):
		input = """int main()
		{
			for(a[2]; i < 2; i = a[2] + 1) 
            {
                b = a + 1;
                foo(3);
                for(t; true; abc) ahihi(21);
            }

            for(i + 3 + a[2]; bcd < 2; a[b] = a[foo(2)]) {
                bcd = bcd + 1;
            }

            for(true;true;false) a = 6 <= b;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(ArrayCell(Id("a"),IntLiteral(2)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(1))),Block([BinaryOp("=",Id("b"),BinaryOp("+",Id("a"),IntLiteral(1))),CallExpr(Id("foo"),[IntLiteral(3)]),For(Id("t"),BooleanLiteral(True),Id("abc"),CallExpr(Id("ahihi"),[IntLiteral(21)]))])),For(BinaryOp("+",BinaryOp("+",Id("i"),IntLiteral(3)),ArrayCell(Id("a"),IntLiteral(2))),BinaryOp("<",Id("bcd"),IntLiteral(2)),BinaryOp("=",ArrayCell(Id("a"),Id("b")),ArrayCell(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)]))),Block([BinaryOp("=",Id("bcd"),BinaryOp("+",Id("bcd"),IntLiteral(1)))])),For(BooleanLiteral(True),BooleanLiteral(True),BooleanLiteral(False),BinaryOp("=",Id("a"),BinaryOp("<=",IntLiteral(6),Id("b"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,368))

	def test_stmtdec_69(self):
		input = """int main()
		{
			for (i;j;t) {
            }
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("i"),Id("j"),Id("t"),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,369))

	def test_stmtdec_70(self):
		input = """int main()
		{
			for(i=4;i<=10;i=i+1) break;
			for(i=4;i<=10;i=i+1) continue;
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Break()),For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Continue())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,370))

	def test_stmtdec_71(self):
		input = """
		float cmp(int a,int b)
		{
			if (a>b) return 1;
			if (a<b) return -1;
			return 0;
			i+2;
			100;
			{
				int a,b,c;
				a=b=c=5;
				float f[5];
				if (a==b) f[0]=1.0;
			}
		}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("cmp"),[VarDecl("a",IntType()),VarDecl("b",IntType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Return(IntLiteral(1))),If(BinaryOp("<",Id("a"),Id("b")),Return(UnaryOp("-",IntLiteral(1)))),Return(IntLiteral(0)),BinaryOp("+",Id("i"),IntLiteral(2)),IntLiteral(100),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),VarDecl("f",ArrayType(5,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0)))])])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,371))

	def test_stmtdec_72(self):
		input = """
		void enter()
		{
			int k;
			v = 5;
			for(i=0;i<n-1;i)
			{
				for(i=0;i<n-1;i) return;		
			}
		}

		void process()
		{
			system("pause");
		}

		int main()
		{
			enter();
			process();
		}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],VoidType(),Block([VarDecl("k",IntType()),BinaryOp("=",Id("v"),IntLiteral(5)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),Id("i"),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),Id("i"),Return())]))])),FuncDecl(Id("process"),[],VoidType(),Block([CallExpr(Id("system"),[StringLiteral("pause")])])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("enter"),[]),CallExpr(Id("process"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,372))

	def test_stmtdec_73(self):
		input = """
		int main()
		{
			for(2;a==2||b=4&&c==true;p=p*2)
			{
				{}{}{}{}{}{}{}
				{
					{
						{
							a=3;
						}
					}
				}
             	do do do do i = 0; while(9); while(true); while(false); while(1);
             	foo(foo(foo(foo(foo(foo())))));
			}
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(2),BinaryOp("=",BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),Id("b")),BinaryOp("&&",IntLiteral(4),BinaryOp("==",Id("c"),BooleanLiteral(True)))),BinaryOp("=",Id("p"),BinaryOp("*",Id("p"),IntLiteral(2))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([BinaryOp("=",Id("a"),IntLiteral(3))])])]),Dowhile([Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("i"),IntLiteral(0))],IntLiteral(9))],BooleanLiteral(True))],BooleanLiteral(False))],IntLiteral(1)),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])])])])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,373))

	def test_stmtdec_74(self):
		input = """
		int main()
		{
			foo(foo(foo(foo(foo(foo(foo(foo(foo("a",1,43,1.2,"fdasfq")))))))));
			if (a==b)
			{
				if (PPL="harsh")
				{
					{
						{
							{
								{
									foo(foo(foo(foo(foo(foo(foo(foo(foo("a",1,43,1.2,"fdasfq")))))))));
									int a[5];
						            boolean b;
						            return 1;
						            function();
						            for (i = 4; i < 5; i +2 ){
						                if (a = 5) break;
						            }
								}
							}
						}
					}
				}
			}
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[StringLiteral("a"),IntLiteral(1),IntLiteral(43),FloatLiteral(1.2),StringLiteral("fdasfq")])])])])])])])])]),If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("=",Id("PPL"),StringLiteral("harsh")),Block([Block([Block([Block([Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[StringLiteral("a"),IntLiteral(1),IntLiteral(43),FloatLiteral(1.2),StringLiteral("fdasfq")])])])])])])])])]),VarDecl("a",ArrayType(5,IntType())),VarDecl("b",BoolType()),Return(IntLiteral(1)),CallExpr(Id("function"),[]),For(BinaryOp("=",Id("i"),IntLiteral(4)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("+",Id("i"),IntLiteral(2)),Block([If(BinaryOp("=",Id("a"),IntLiteral(5)),Break())]))])])])])]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,374))

	def test_all_75(self):
		input = """
		int main()
		{
			int xyzz,abcc,hcmut;
			float xyzz[999],abcc[999],hcmut,apple,NHMR;
			string xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			boolean xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
			_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
			_-_-_-_-_-_-_-_-_-_-_-_-_-_;

		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("xyzz",IntType()),VarDecl("abcc",IntType()),VarDecl("hcmut",IntType()),VarDecl("xyzz",ArrayType(999,FloatType())),VarDecl("abcc",ArrayType(999,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("apple",FloatType()),VarDecl("NHMR",FloatType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",ArrayType(999,StringType())),VarDecl("xyzz",BoolType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",BoolType()),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",BoolType()),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",BoolType()),VarDecl("NHMR",ArrayType(999,BoolType())),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,375))

	def test_all_76(self):
		input = """
		float xyzz()
		{   
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}
		"""
		expect = str(Program([FuncDecl(Id("xyzz"),[],FloatType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType())),VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType())),VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,376))

	def test_all_77(self):
		input = """
		boolean xyzz()
		{   
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}   


		boolean[] xyzz()
		{
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}
		"""
		expect=str(Program([FuncDecl(Id("xyzz"),[],BoolType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType())),VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))])),FuncDecl(Id("xyzz"),[],ArrayPointerType(BoolType()),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType())),VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,377))

	def test_all_78(self):
		input = """
		int xyzz()
		{   
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}   


		void abcc()
		{
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}

		float hcmut()
		{   
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}   


		string apple()
		{
			float xyzz,abcc,hcmut;
			int xyzz[999],abcc[999],hcmut,apple,NHMR;
			boolean xyzz[999],abcc[999],hcmut[999],apple[999],NHMR[999];
			string xyzz,xyzz[999],abcc,abcc[999],hcmut,hcmut[999],apple,apple[999],NHMR,NHMR[999];
		}
		"""
		expect = str(Program([FuncDecl(Id("xyzz"),[],IntType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))])),FuncDecl(Id("abcc"),[],VoidType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))])),FuncDecl(Id("hcmut"),[],FloatType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))])),FuncDecl(Id("apple"),[],StringType(),Block([VarDecl("xyzz",FloatType()),VarDecl("abcc",FloatType()),VarDecl("hcmut",FloatType()),VarDecl("xyzz",ArrayType(999,IntType())),VarDecl("abcc",ArrayType(999,IntType())),VarDecl("hcmut",IntType()),VarDecl("apple",IntType()),VarDecl("NHMR",IntType()),VarDecl("xyzz",ArrayType(999,BoolType())),VarDecl("abcc",ArrayType(999,BoolType())),VarDecl("hcmut",ArrayType(999,BoolType())),VarDecl("apple",ArrayType(999,BoolType())),VarDecl("NHMR",ArrayType(999,BoolType())),VarDecl("xyzz",StringType()),VarDecl("xyzz",ArrayType(999,StringType())),VarDecl("abcc",StringType()),VarDecl("abcc",ArrayType(999,StringType())),VarDecl("hcmut",StringType()),VarDecl("hcmut",ArrayType(999,StringType())),VarDecl("apple",StringType()),VarDecl("apple",ArrayType(999,StringType())),VarDecl("NHMR",StringType()),VarDecl("NHMR",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,378))

	def test_all_79(self):
		input = """
		float main(){
			if(sky)
				if(sea){}
			else{earth;}
			else{rain;}
			if(light){}
			else{dark;}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([If(Id("sky"),If(Id("sea"),Block([]),Block([Id("earth")])),Block([Id("rain")])),If(Id("light"),Block([]),Block([Id("dark")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,379))

	def test_all_80(self):
		input = """
		void main()
		{
			do
				do
					do
						do
						{
						
						}
						while true;
					while false;
				while (true&&true);
			while (false || true && false);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,380))

	def test_all_81(self):
		input = """int main()
		{
			if (earth)
				do
				{
					taylorSwift;
				}
				while edSheeran;
			else
				MTP;
		}

		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("earth"),Dowhile([Block([Id("taylorSwift")])],Id("edSheeran")),Id("MTP"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,381))

	def test_all_82(self):
		input = """int main(){
			int a,a,a,a,a,a,a,a,a,a,a;
			float _,_,_,_,_,_,_;
			string qqqqqqqqqq,wwwwwwwwwwwwwww,pppppppppppppppp[123],ewqqqewqewqe,_123123;
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("qqqqqqqqqq",StringType()),VarDecl("wwwwwwwwwwwwwww",StringType()),VarDecl("pppppppppppppppp",ArrayType(123,StringType())),VarDecl("ewqqqewqewqe",StringType()),VarDecl("_123123",StringType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,382))

	def test_all_83(self):
		input = """int main()
		{
			(((((a)))));
		}
		"""
		expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("a")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,383))

	def test_all_84(self):
		input = """int main()
		{	
			for(i = 3; i < infinity; i = i + 1)
				if(tesserract)
					whoCares();
			for(exp; exp; exp){
				{
					stillWhoCares();
				}
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("<",Id("i"),Id("infinity")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(Id("tesserract"),CallExpr(Id("whoCares"),[]))),For(Id("exp"),Id("exp"),Id("exp"),Block([Block([CallExpr(Id("stillWhoCares"),[])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,384))

	def test_all_85(self):
		input = """
		int enter()
		{	
			if (m)
			{
				break;
				continue;
				break;
				return 1;
				return abcc;
				if(a)
				{
					if(b)
					{

					}
				}
			}
		}	
	

		int main()
		{
			int a,b,c;
			float x,y,z;
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("enter"),[],IntType(),Block([If(Id("m"),Block([Break(),Continue(),Break(),Return(IntLiteral(1)),Return(Id("abcc")),If(Id("a"),Block([If(Id("b"),Block([]))]))]))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,385))

	def test_all_86(self):
		input = """
		int print()
		{	
		}	
	

		void join()
		{
		}

		int enter()
		{	
		}	
	

		int main()
		{
			for(thanos;captainAmerica;ironMan) 
			{
				sherlock(watson);
				do
				{
					for(exp;exp;exp)
					{
						for(exp;exp;exp)
						{
							sherlock(watson);
						}
						{{{}}{{}}{{}}{{}}{{}}{{}}{{}}}
					}
				}
				while (spiderman);
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("print"),[],IntType(),Block([])),FuncDecl(Id("join"),[],VoidType(),Block([])),FuncDecl(Id("enter"),[],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([For(Id("thanos"),Id("captainAmerica"),Id("ironMan"),Block([CallExpr(Id("sherlock"),[Id("watson")]),Dowhile([Block([For(Id("exp"),Id("exp"),Id("exp"),Block([For(Id("exp"),Id("exp"),Id("exp"),Block([CallExpr(Id("sherlock"),[Id("watson")])])),Block([Block([Block([])]),Block([Block([])]),Block([Block([])]),Block([Block([])]),Block([Block([])]),Block([Block([])]),Block([Block([])])])]))])],Id("spiderman"))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,386))

	def test_all_87(self):
		input = """
		int print()
		{	
			string b,c[123],d,e[1234534];
		}	
	

		void join()
		{
			int a,b,c;
		}

		void fit()
		{
			int a,b,c;
		}

		int enter()
		{	
			{}{}{}{}{}{}{}{}{}{}{}{}{}
			{{{{{{{}}}}}}}
		}	
	

		int main()
		{
			boolean b,c[123],d,e[1234534];
		}

		"""
		expect = str(Program([FuncDecl(Id("print"),[],IntType(),Block([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType()))])),FuncDecl(Id("join"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())])),FuncDecl(Id("fit"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())])),FuncDecl(Id("enter"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([Block([Block([])])])])])])])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,387))

	def test_all_88(self):
		input = """int main()
		{
			int a,b,c;
			do
				yolo();
				haveGirlfriends(_,_,_,_,_);
				{{}{}{}{}{}{}{{{{{}}}}}{}{}}
			while (young);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([CallExpr(Id("yolo"),[]),CallExpr(Id("haveGirlfriends"),[Id("_"),Id("_"),Id("_"),Id("_"),Id("_")]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([])])])])]),Block([]),Block([])])],Id("young"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,388))

	def test_all_89(self):
		input = """string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];

			int enter()
			{	
				{}{}{}{}{}{}{}{}{}{}{}{}{}
				{{{{{{{}}}}}}}
			}	


			int main()
			{
				int a,b,c;
				do
					yolo();
					haveGirlfriends(_,_,_,_,_);
					{{}{}{}{}{}{}{{{{{}}}}}{}{}}
				while (young);
			}
		"""
		expect = str(Program([VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType())),FuncDecl(Id("enter"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([Block([Block([])])])])])])])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([CallExpr(Id("yolo"),[]),CallExpr(Id("haveGirlfriends"),[Id("_"),Id("_"),Id("_"),Id("_"),Id("_")]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([])])])])]),Block([]),Block([])])],Id("young"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,389))

	def test_all_90(self):
		input = """
		int a,a,a,a,a,a,a,a,a,a,a;
		float _,_,_,_,_,_,_;

		int enter()
		{	
			{}{}{}{}{}{}{}{}{}{}{}{}{}
			{{{{{{{}}}}}}}
		}	


		int main()
		{
			int a,b,c;
			do
				yolo();
				haveGirlfriends(_,_,_,_,_);
				{{}{}{}{}{}{}{{{{{}}}}}{}{}}
			while (young);
		}

		string qqqqqqqqqq,wwwwwwwwwwwwwww,pppppppppppppppp[123],ewqqqewqewqe,_123123;
		"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("a",IntType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),VarDecl("_",FloatType()),FuncDecl(Id("enter"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([Block([Block([])])])])])])])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([CallExpr(Id("yolo"),[]),CallExpr(Id("haveGirlfriends"),[Id("_"),Id("_"),Id("_"),Id("_"),Id("_")]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([])])])])]),Block([]),Block([])])],Id("young"))])),VarDecl("qqqqqqqqqq",StringType()),VarDecl("wwwwwwwwwwwwwww",StringType()),VarDecl("pppppppppppppppp",ArrayType(123,StringType())),VarDecl("ewqqqewqewqe",StringType()),VarDecl("_123123",StringType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,390))

	def test_all_91(self):
		input = """int main(float q[],string a[],float _[],float _[]){
			int a,b,c;
			do
				yolo();
				haveGirlfriends(_,_,_,_,_);
				{{}{}{}{}{}{}{{{{{}}}}}{}{}}
			while (young);
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("q",ArrayPointerType(FloatType())),VarDecl("a",ArrayPointerType(StringType())),VarDecl("_",ArrayPointerType(FloatType())),VarDecl("_",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([CallExpr(Id("yolo"),[]),CallExpr(Id("haveGirlfriends"),[Id("_"),Id("_"),Id("_"),Id("_"),Id("_")]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([Block([])])])])]),Block([]),Block([])])],Id("young"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,391))

	def test_all_92(self):
		input = """int b()
		{
			do
			{
				_();
				_();
				_();
				_();
			}
			{
				_();_();_();_();_();
			}
			{
				{
				
				}
				{

				}
			}
			while (1+2+3+4+5+6+7*8*9*10/11/12/13%14%15%16);
		}
		float x,y,z;
		"""
		expect = str(Program([FuncDecl(Id("b"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[])]),Block([CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[])]),Block([Block([]),Block([])])],BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("*",BinaryOp("*",BinaryOp("*",IntLiteral(7),IntLiteral(8)),IntLiteral(9)),IntLiteral(10)),IntLiteral(11)),IntLiteral(12)),IntLiteral(13)),IntLiteral(14)),IntLiteral(15)),IntLiteral(16))))])),VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,392))

	def test_all_93(self):
		input = """
		int main()
		{
			float x,y,z;
			_();
			_();
			_();
			_();
			string b,c[123],d,e[1234534];
			boolean b,c[123],d,e[1234534];
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),VarDecl("y",FloatType()),VarDecl("z",FloatType()),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),CallExpr(Id("_"),[]),VarDecl("b",StringType()),VarDecl("c",ArrayType(123,StringType())),VarDecl("d",StringType()),VarDecl("e",ArrayType(1234534,StringType())),VarDecl("b",BoolType()),VarDecl("c",ArrayType(123,BoolType())),VarDecl("d",BoolType()),VarDecl("e",ArrayType(1234534,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,393))

	def test_all_94(self):
		input = """
		void main(){
			"So this is the last testcase of this section! Good luck!";
			for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}

			printf("Yayyyyyyyyyyyyyyyyyyyyyy!");
		}
		"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([StringLiteral("So this is the last testcase of this section! Good luck!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),CallExpr(Id("printf"),[StringLiteral("Yayyyyyyyyyyyyyyyyyyyyyy!")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,394))

	def test_all_95(self):
		input = """
		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{

			}
		}
		"""
		expect = str(Program([FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,395))

	def test_all_96(self):
		input = """
		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,396))

	def test_all_97(self):
		input = """
		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
						_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,397))

	def test_all_98(self):
		input = """
		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}


		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}
		"""
		expect = str(Program([FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,398))

	def test_funcdec_99(self):
		input = """
		void enter()
		{
			// Oh you're so good. I can't give you any more stress.

			"Please remember me as a tester friend of yours. Hic hic huhu";
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}
		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"Final challenge!";
				for(test; all; statements)
				for(test; all_again; statements)
					if(thisTestcase == true)
					do
						"Yeah you nailed the statements";
						break;
						return true;
						continue;
						do
							statement1;
							if(youCanPassedThis)
								yourStatement = good;
							else
								needToCheck();
						while(stillRunning);
					while(stillRunning());
					else{
						if(fuckingShitIDareYouToPassThisFuckingStuff[3000]){
							do
								do
									do
										for(1;2;3){
											what = doesnot;
											kill = you;
											makes = youStronger;
										}
										passed = stronger;
									while(thisIsGoingToEnd);
								while(butThereAreStillManyToCome());
							while(goodLuck);
						}
					}
					do
						do
							do
								do
								{}
								while true;
							while false;
						while (true&&true);
					while (false || true && false);
					{{}{}{}{}{}{}{}{}}
					_+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
					_-_-_-_-_-_-_-_-_-_-_-_-_-_;
			}
		}

		void execution()
		{
			"Five final tests!!!!!!";
			//Pass or die;
			/*
			{
				"You will be sentenced to death if you treat me as a block!";
			}
			*/
			{
				"Hi hi, are you scared right now??????????";
			}

			{
				"HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA";
				{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
				foo(foo(foo(foo(foo(foo(foo(foo(foo()))))))));
			}
		}

		int main(){}
		"""
		expect=str(Program([FuncDecl(Id("enter"),[],VoidType(),Block([StringLiteral("Please remember me as a tester friend of yours. Hic hic huhu")])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("Final challenge!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("fuckingShitIDareYouToPassThisFuckingStuff"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(False))],BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))],BinaryOp("||",BooleanLiteral(False),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])])),FuncDecl(Id("execution"),[],VoidType(),Block([StringLiteral("Five final tests!!!!!!"),Block([StringLiteral("Hi hi, are you scared right now??????????")]),Block([StringLiteral("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])])])])])])])])])])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,399))