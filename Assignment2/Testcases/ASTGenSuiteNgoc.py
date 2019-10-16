import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_declarations(self):
        """Test declarations"""
        input = """int a;
        boolean BTS[7],__y00ng1_;
        string[] _Army(float arr[], int num) {
            //Block comment
        }"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("BTS",ArrayType(7,BoolType())),VarDecl("__y00ng1_",BoolType()),FuncDecl(Id("_Army"),[VarDecl("arr",ArrayPointerType(FloatType())),VarDecl("num",IntType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_declarations(self):
        """Test var declarations"""
        input = """
        int _06_13_13,_BTS,JJJJJIN,JOOON; boolean ARMYYYYY[130613];
        string army,BTS[7],_[4499], _; 
        """
        expect = str(Program([VarDecl("_06_13_13",IntType()),VarDecl("_BTS",IntType()),VarDecl("JJJJJIN",IntType()),VarDecl("JOOON",IntType()),VarDecl("ARMYYYYY",ArrayType(130613,BoolType())),VarDecl("army",StringType()),VarDecl("BTS",ArrayType(7,StringType())),VarDecl("_",ArrayType(4499,StringType())),VarDecl("_",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_declarations_1(self):
        input = """
        float _2_25e, i[111111111111];
        string str[33333333];
        boolean true_1, false_0;
        """
        expect = str(Program([VarDecl("_2_25e",FloatType()),VarDecl("i",ArrayType(111111111111,FloatType())),VarDecl("str",ArrayType(33333333,StringType())),VarDecl("true_1",BoolType()),VarDecl("false_0",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_declarations_2(self):
        input = """
        boolean Dont;
        float Givep[0];
        int __Y_S___[0000000000];
        string up;
        """
        expect = str(Program([VarDecl("Dont",BoolType()),VarDecl("Givep",ArrayType(0,FloatType())),VarDecl("__Y_S___",ArrayType(0,IntType())),VarDecl("up",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_func_declarations(self):
        input = """
        void swap(int me, int you) {
            /*No way to swap*/
        }
        """
        expect = str(Program([FuncDecl(Id("swap"),[VarDecl("me",IntType()),VarDecl("you",IntType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_func_declarations_1(self):
        input = """
        int a() {}
        boolean b(string str) {
            a = b;
        }
        string[] print(boolean t,string intput[],int b, int a) {
            "Hello World!";
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[],IntType(),Block([])),FuncDecl(Id("b"),[VarDecl("str",StringType())],BoolType(),Block([BinaryOp("=",Id("a"),Id("b"))])),FuncDecl(Id("print"),[VarDecl("t",BoolType()),VarDecl("intput",ArrayPointerType(StringType())),VarDecl("b",IntType()),VarDecl("a",IntType())],ArrayPointerType(StringType()),Block([StringLiteral("Hello World!")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_declarations_2(self):
        input = """
        void main(string argv[], int argc) {
            string str[7], IVIVIVIVIVIVIVIV;
            str = "Born Coder";

        }
        void _() {
            {
                {
                    ((((((((((("Rabbit Doubt"))))))))))); // Nonsense function
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],VoidType(),Block([VarDecl("str",ArrayType(7,StringType())),VarDecl("IVIVIVIVIVIVIVIV",StringType()),BinaryOp("=",Id("str"),StringLiteral("Born Coder"))])),FuncDecl(Id("_"),[],VoidType(),Block([Block([Block([StringLiteral("Rabbit Doubt")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_func_declarations_3(self):
        input = """
        int _1(int no1) {}
        float _2(string no2[], int _, boolean _) {
            ____________________________________;
        }
        void _(float _4_) {
            run;
        }
        boolean[] will(int i, int j,string true_[])
        {{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}
        """
        expect = str(Program([FuncDecl(Id("_1"),[VarDecl("no1",IntType())],IntType(),Block([])),FuncDecl(Id("_2"),[VarDecl("no2",ArrayPointerType(StringType())),VarDecl("_",IntType()),VarDecl("_",BoolType())],FloatType(),Block([Id("____________________________________")])),FuncDecl(Id("_"),[VarDecl("_4_",FloatType())],VoidType(),Block([Id("run")])),FuncDecl(Id("will"),[VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("true_",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])])])])])])])])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_combine_declarations(self):
        input = """
        int global_1;
        void foo(float var1, string var_2[], boolean XXX) {
            // Do nothing
            return XXX;
            int ARR[1000000000000000000000000], BRR[9999999999999];
        }
        float rand, num, XYZ[123];
        int[] new() {
            a = "None";
        }
        """
        expect = str(Program([VarDecl("global_1",IntType()),FuncDecl(Id("foo"),[VarDecl("var1",FloatType()),VarDecl("var_2",ArrayPointerType(StringType())),VarDecl("XXX",BoolType())],VoidType(),Block([Return(Id("XXX")),VarDecl("ARR",ArrayType(1000000000000000000000000,IntType())),VarDecl("BRR",ArrayType(9999999999999,IntType()))])),VarDecl("rand",FloatType()),VarDecl("num",FloatType()),VarDecl("XYZ",ArrayType(123,FloatType())),FuncDecl(Id("new"),[],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("a"),StringLiteral("None"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_combine_declarations_1(self):
        input = """
        float[] random(int head, int tail, float arr[]) {
            {
                random(7);
                n = ((((((((((((((((((2))))))))))))))))));
            }
            continue;
        }
        
        int SUGA, suga, Suga[10000000];
        void main() {
            SUGA = random(44,suga(99),Suga[4499]);
        }
        """
        expect = str(Program([FuncDecl(Id("random"),[VarDecl("head",IntType()),VarDecl("tail",IntType()),VarDecl("arr",ArrayPointerType(FloatType()))],ArrayPointerType(FloatType()),Block([Block([CallExpr(Id("random"),[IntLiteral(7)]),BinaryOp("=",Id("n"),IntLiteral(2))]),Continue()])),VarDecl("SUGA",IntType()),VarDecl("suga",IntType()),VarDecl("Suga",ArrayType(10000000,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("SUGA"),CallExpr(Id("random"),[IntLiteral(44),CallExpr(Id("suga"),[IntLiteral(99)]),ArrayCell(Id("Suga"),IntLiteral(4499))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_combine_declarations_2(self):
        input = """
        //define function
        int MAX;

        void inst_Matrix(int row, int col, int Mtx[]) {
            row <= MAX; row >= col;
            // loop
            assign = 1;
        }

        int main(int argc, string argv[]) {
            foo(((((((((((((((((((((run[2])))))))))))))))))))));
            int JK[7], VVV;
        }

        float PPL, ppl, _Ppl123;
        """
        expect = str(Program([VarDecl("MAX",IntType()),FuncDecl(Id("inst_Matrix"),[VarDecl("row",IntType()),VarDecl("col",IntType()),VarDecl("Mtx",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("<=",Id("row"),Id("MAX")),BinaryOp(">=",Id("row"),Id("col")),BinaryOp("=",Id("assign"),IntLiteral(1))])),FuncDecl(Id("main"),[VarDecl("argc",IntType()),VarDecl("argv",ArrayPointerType(StringType()))],IntType(),Block([CallExpr(Id("foo"),[ArrayCell(Id("run"),IntLiteral(2))]),VarDecl("JK",ArrayType(7,IntType())),VarDecl("VVV",IntType())])),VarDecl("PPL",FloatType()),VarDecl("ppl",FloatType()),VarDecl("_Ppl123",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_combine_declarations_3(self):
        input = """
        int _a; int _a; int _a; int _a; int _a; int _a; int _a; int _a; float _a[999],SFA,rr,_ase123, asdf, SDFG_12123;
        float foo(string _, int _, boolean _[]) {
            {{{{{}}}}}
            int _,_,_,_[3],_,_[5],_____;
            {{{{{{{{{{{}}}}}}}}}}}
        }
        int b;
        float ccccccccc;
        boolean trueeeeeeeeeee,         FALSE, FALSE[1000000000];
        int ppl() {}
        void ppl(string test) {
            // Down the rabbit hole ?
        }
        """
        expect = str(Program([VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",IntType()),VarDecl("_a",ArrayType(999,FloatType())),VarDecl("SFA",FloatType()),VarDecl("rr",FloatType()),VarDecl("_ase123",FloatType()),VarDecl("asdf",FloatType()),VarDecl("SDFG_12123",FloatType()),FuncDecl(Id("foo"),[VarDecl("_",StringType()),VarDecl("_",IntType()),VarDecl("_",ArrayPointerType(BoolType()))],FloatType(),Block([Block([Block([Block([Block([Block([])])])])]),VarDecl("_",IntType()),VarDecl("_",IntType()),VarDecl("_",IntType()),VarDecl("_",ArrayType(3,IntType())),VarDecl("_",IntType()),VarDecl("_",ArrayType(5,IntType())),VarDecl("_____",IntType()),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])])])])),VarDecl("b",IntType()),VarDecl("ccccccccc",FloatType()),VarDecl("trueeeeeeeeeee",BoolType()),VarDecl("FALSE",BoolType()),VarDecl("FALSE",ArrayType(1000000000,BoolType())),FuncDecl(Id("ppl"),[],IntType(),Block([])),FuncDecl(Id("ppl"),[VarDecl("test",StringType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_combine_declarations_4(self):
        """Putting comments between declarations"""
        input = """
        int a/*cmt1^^*/,b[2/*isthisok*/]/*not so sure*/;
        int foo/*cmt2*/(int /*vardec in func*/ a, boolean b) {
            ///////////////////////////////////////////////
            {{{////////////
            }}}
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(2,IntType())),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",BoolType())],IntType(),Block([Block([Block([Block([])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_expressions(self):
        input = """
        int main() {
            a = b;
            _ || b;
            a && 1;
            _ == _; 1 != _;
            x <= 3e8; y > _;
            2 + "hello" - _;
            true * 3/7%25;
            3 + - (!23);
            (b*a)[7];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),Id("b")),BinaryOp("||",Id("_"),Id("b")),BinaryOp("&&",Id("a"),IntLiteral(1)),BinaryOp("==",Id("_"),Id("_")),BinaryOp("!=",IntLiteral(1),Id("_")),BinaryOp("<=",Id("x"),FloatLiteral(300000000.0)),BinaryOp(">",Id("y"),Id("_")),BinaryOp("-",BinaryOp("+",IntLiteral(2),StringLiteral("hello")),Id("_")),BinaryOp("%",BinaryOp("/",BinaryOp("*",BooleanLiteral(True),IntLiteral(3)),IntLiteral(7)),IntLiteral(25)),BinaryOp("+",IntLiteral(3),UnaryOp("-",UnaryOp("!",IntLiteral(23)))),ArrayCell(BinaryOp("*",Id("b"),Id("a")),IntLiteral(7))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_expressions_1(self):
        input = """
        int main () {
            abc = BTS || ARMY&&49;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("abc"),BinaryOp("||",Id("BTS"),BinaryOp("&&",Id("ARMY"),IntLiteral(49))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_expressions_2(self):
        input = """
        void foo() {
            c = "helloworld" = b == 7 && 2 != 4e-9;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",Id("c"),BinaryOp("=",StringLiteral("helloworld"),BinaryOp("&&",BinaryOp("==",Id("b"),IntLiteral(7)),BinaryOp("!=",IntLiteral(2),FloatLiteral(4e-09)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_expressions_3(self):
        input = """
        void foo() {
            "PPL" >= 54 != helloworld < 7 = c && 0.0;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",BinaryOp("!=",BinaryOp(">=",StringLiteral("PPL"),IntLiteral(54)),BinaryOp("<",Id("helloworld"),IntLiteral(7))),BinaryOp("&&",Id("c"),FloatLiteral(0.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_expressions_4(self):
        input = """
        int main() {
            2+3+4 < 7.e3 - "id" == 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("==",BinaryOp("<",BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(3)),IntLiteral(4)),BinaryOp("-",FloatLiteral(7000.0),StringLiteral("id"))),IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_expressions_5(self):
        input = """
        int main() {
            2+"h"*2/-(25%!H1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",IntLiteral(2),BinaryOp("/",BinaryOp("*",StringLiteral("h"),IntLiteral(2)),UnaryOp("-",BinaryOp("%",IntLiteral(25),UnaryOp("!",Id("H1"))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_expressions_6(self):
        input = """
        int main() {
            foo(2)[3+x] = a[b[2]] + 3;
            ((((((((((((((((0*((((h-7>=3*foo((((((("str")))))))))))))))))))))))))));
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("*",IntLiteral(0),BinaryOp(">=",BinaryOp("-",Id("h"),IntLiteral(7)),BinaryOp("*",IntLiteral(3),CallExpr(Id("foo"),[StringLiteral("str")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_expressions_7(self):
        input = """
        int foo(int a, float b[]) {
            boolean c;
            int i;
            i = a + 3;
            d = i+3 * swap(foo(3),arr[25]) >= "^string^";
            d && 25E009 = var = "BTS_World";
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),BinaryOp("=",Id("d"),BinaryOp(">=",BinaryOp("+",Id("i"),BinaryOp("*",IntLiteral(3),CallExpr(Id("swap"),[CallExpr(Id("foo"),[IntLiteral(3)]),ArrayCell(Id("arr"),IntLiteral(25))]))),StringLiteral("^string^"))),BinaryOp("=",BinaryOp("&&",Id("d"),FloatLiteral(25000000000.0)),BinaryOp("=",Id("var"),StringLiteral("BTS_World")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_expressions_8(self):
        input = """
        int  [] foo(int bbbbbbbbbbbbb[]) {
            {
                a[2*foo(((((((((57-"str"!=(!var%0.24-(arr[8])[25])[0])))))))))];
            }
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("bbbbbbbbbbbbb",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Block([ArrayCell(Id("a"),BinaryOp("*",IntLiteral(2),CallExpr(Id("foo"),[BinaryOp("!=",BinaryOp("-",IntLiteral(57),StringLiteral("str")),ArrayCell(BinaryOp("-",BinaryOp("%",UnaryOp("!",Id("var")),FloatLiteral(0.24)),ArrayCell(ArrayCell(Id("arr"),IntLiteral(8)),IntLiteral(25))),IntLiteral(0)))])))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_expressions_9(self):
        input = """
        int a,b,cccc;
        int main (int a, string b[]) {
        a=bFFF=c==5 +_+_+__-_-_*_sdfg/sdr%ys && goo(234 - ght[888]);
        float f[5];
        f[0] = ((((((((((((((((((((((arr==5)[(((25)))]))))))))))))))))))))) || false;
        }
        int xxxxxxxxx[999999999999999999], y, _,tt;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("cccc",IntType()),FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(StringType()))],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("bFFF"),BinaryOp("&&",BinaryOp("==",Id("c"),BinaryOp("-",BinaryOp("-",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(5),Id("_")),Id("_")),Id("__")),Id("_")),BinaryOp("%",BinaryOp("/",BinaryOp("*",Id("_"),Id("_sdfg")),Id("sdr")),Id("ys")))),CallExpr(Id("goo"),[BinaryOp("-",IntLiteral(234),ArrayCell(Id("ght"),IntLiteral(888)))])))),VarDecl("f",ArrayType(5,FloatType())),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),BinaryOp("||",ArrayCell(BinaryOp("==",Id("arr"),IntLiteral(5)),IntLiteral(25)),BooleanLiteral(False)))])),VarDecl("xxxxxxxxx",ArrayType(999999999999999999,IntType())),VarDecl("y",IntType()),VarDecl("_",IntType()),VarDecl("tt",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_expressions_10(self):
        input = """
        float[] decimalToBinary(int decimalnum)
        {
            float binarynum ;
            int rem, temp;

    
            rem = decimalnum%2;
            decimalnum = decimalnum / 2;
            binarynum = binarynum + rem*temp;
            temp = temp * 10;
            {
                {
                    // Comment
                }
            }
    
            return binarynum;
        }
        """
        expect = str(Program([FuncDecl(Id("decimalToBinary"),[VarDecl("decimalnum",IntType())],ArrayPointerType(FloatType()),Block([VarDecl("binarynum",FloatType()),VarDecl("rem",IntType()),VarDecl("temp",IntType()),BinaryOp("=",Id("rem"),BinaryOp("%",Id("decimalnum"),IntLiteral(2))),BinaryOp("=",Id("decimalnum"),BinaryOp("/",Id("decimalnum"),IntLiteral(2))),BinaryOp("=",Id("binarynum"),BinaryOp("+",Id("binarynum"),BinaryOp("*",Id("rem"),Id("temp")))),BinaryOp("=",Id("temp"),BinaryOp("*",Id("temp"),IntLiteral(10))),Block([Block([])]),Return(Id("binarynum"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_expressions_11(self):
        input = """
        int main (string argv[], int argc) {
            int rank,size;

            MPI_Init();
            MPI_Comm_rank(MPI_COMM_WORLD,rank);
            MPI_Comm_size(MPI_COMM_WORLD,size);

            srand(time(NULL));
            (res[0])[row] = (res[1])[row] = 0 == 277 * - h > -9;          
      	{
       		(res[0])[row] % Matrx(Matrix_1[rank])[col] * ((((Matrix_2[row]))))[col];    	   		
        	(res[1])[row] >= (Matrix_1[rank])[col] * (Matrix_2[row]-"string")[col];    	   		
	    }
    
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([VarDecl("rank",IntType()),VarDecl("size",IntType()),CallExpr(Id("MPI_Init"),[]),CallExpr(Id("MPI_Comm_rank"),[Id("MPI_COMM_WORLD"),Id("rank")]),CallExpr(Id("MPI_Comm_size"),[Id("MPI_COMM_WORLD"),Id("size")]),CallExpr(Id("srand"),[CallExpr(Id("time"),[Id("NULL")])]),BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),BinaryOp("==",IntLiteral(0),BinaryOp(">",BinaryOp("*",IntLiteral(277),UnaryOp("-",Id("h"))),UnaryOp("-",IntLiteral(9)))))),Block([BinaryOp("*",BinaryOp("%",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),ArrayCell(CallExpr(Id("Matrx"),[ArrayCell(Id("Matrix_1"),Id("rank"))]),Id("col"))),ArrayCell(ArrayCell(Id("Matrix_2"),Id("row")),Id("col"))),BinaryOp(">=",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix_1"),Id("rank")),Id("col")),ArrayCell(BinaryOp("-",ArrayCell(Id("Matrix_2"),Id("row")),StringLiteral("string")),Id("col"))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_expressions_12(self):
        input = """
        int[] main() {
            MPI_Recv(Matrix_R[2*i], ((((SIZE*2))))=true||false, MPI_INTEGER, i, tag, MPI_COMM_WORLD, Stat);

	
        // Print Matrix result:
                int x, y;
                printf("%d", (Matrix_R[x])[y]);
                printf("\\n");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([CallExpr(Id("MPI_Recv"),[ArrayCell(Id("Matrix_R"),BinaryOp("*",IntLiteral(2),Id("i"))),BinaryOp("=",BinaryOp("*",Id("SIZE"),IntLiteral(2)),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False))),Id("MPI_INTEGER"),Id("i"),Id("tag"),Id("MPI_COMM_WORLD"),Id("Stat")]),VarDecl("x",IntType()),VarDecl("y",IntType()),CallExpr(Id("printf"),[StringLiteral("%d"),ArrayCell(ArrayCell(Id("Matrix_R"),Id("x")),Id("y"))]),CallExpr(Id("printf"),[StringLiteral("\\n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_if_statements(self):
        input = """
        // Program to display a number if it is negative
        int main()
        {
            int number;
            printf("Enter an integer: ");
            scanf("%d", number);
            // true if number is less than 0
            if (number < 0)
            {
                printf("You entered %d.n", number);
            }
            printf("The if statement is easy.");
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("number")]),If(BinaryOp("<",Id("number"),IntLiteral(0)),Block([CallExpr(Id("printf"),[StringLiteral("You entered %d.n"),Id("number")])])),CallExpr(Id("printf"),[StringLiteral("The if statement is easy.")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_if_statements_1(self):
        input = """
        void main() {
            if (a) 
                if(true) return false;
                else "what to do now?";
            else
                print("HPBD Jiminie");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(Id("a"),If(BooleanLiteral(True),Return(BooleanLiteral(False)),StringLiteral("what to do now?")),CallExpr(Id("print"),[StringLiteral("HPBD Jiminie")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_if_statements_2(self):
        input = """
        void main() {
            if(t==23.8) 
                if (foo(2*((((bts))))))
                    if(day_like_this)
                        return run;
                    else will >= ((((((((_(_(fight))))))))));
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("t"),FloatLiteral(23.8)),If(CallExpr(Id("foo"),[BinaryOp("*",IntLiteral(2),Id("bts"))]),If(Id("day_like_this"),Return(Id("run")),BinaryOp(">=",Id("will"),CallExpr(Id("_"),[CallExpr(Id("_"),[Id("fight")])])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_if_statements_3(self):
        input = """
        string[] retrieveFlag(int buff[]) {
            string flag[16];
            if (buffer == 0000130613) 
                return flag;
            if (buffer == hexnum) 
            {
                buffer = hexnum || false - "not flag" * flag(255);
            }
            else 
                continue;
                "Successfully retrieved";
        }
        """
        expect = str(Program([FuncDecl(Id("retrieveFlag"),[VarDecl("buff",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([VarDecl("flag",ArrayType(16,StringType())),If(BinaryOp("==",Id("buffer"),IntLiteral(130613)),Return(Id("flag"))),If(BinaryOp("==",Id("buffer"),Id("hexnum")),Block([BinaryOp("=",Id("buffer"),BinaryOp("||",Id("hexnum"),BinaryOp("-",BooleanLiteral(False),BinaryOp("*",StringLiteral("not flag"),CallExpr(Id("flag"),[IntLiteral(255)])))))]),Continue()),StringLiteral("Successfully retrieved")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_if_statements_4(self):
        input = """
        /* C program to find the biggest of three numbers
        */
        void main()
        {
            int num1, num2, num3;
            printf("Enter the values of num1, num2 and num3\\n");
            scanf("%d %d %d", _num1, _num2, _num3);
            printf("num1 = %d\\tnum2 = %d\\tnum3 = %d\\n", num1, num2, num3);
        if (num1 > num2)
        {
            if (num1 > num3)
            {
                printf("num1 is the greatest among three \\n");
            }
            else
            {
                printf("num3 is the greatest among three \\n");
            }
        }
        else if (num2 > num3) printf("num2 is the greatest among three \\n");
            else
                printf("num3 is the greatest among three \\n");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("num1",IntType()),VarDecl("num2",IntType()),VarDecl("num3",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter the values of num1, num2 and num3\\n")]),CallExpr(Id("scanf"),[StringLiteral("%d %d %d"),Id("_num1"),Id("_num2"),Id("_num3")]),CallExpr(Id("printf"),[StringLiteral("num1 = %d\\tnum2 = %d\\tnum3 = %d\\n"),Id("num1"),Id("num2"),Id("num3")]),If(BinaryOp(">",Id("num1"),Id("num2")),Block([If(BinaryOp(">",Id("num1"),Id("num3")),Block([CallExpr(Id("printf"),[StringLiteral("num1 is the greatest among three \\n")])]),Block([CallExpr(Id("printf"),[StringLiteral("num3 is the greatest among three \\n")])]))]),If(BinaryOp(">",Id("num2"),Id("num3")),CallExpr(Id("printf"),[StringLiteral("num2 is the greatest among three \\n")]),CallExpr(Id("printf"),[StringLiteral("num3 is the greatest among three \\n")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_dowhile_statements(self):
        input = """
        int main () {

        /* local variable definition */
        int a;

        /* do loop execution */
        do {
            printf("value of a: %d\\n", a);
            a = a + 1;
        }while( a < 20 );
 
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("value of a: %d\\n"),Id("a")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("<",Id("a"),IntLiteral(20))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_dowhile_statements_1(self):
        input = """
        void foo(int a[], float b, string BTS[], boolean Suga) {
            do 
                first = assign / num * result || false >= !true + ((((foo[35] * - (arr["string"])[res]))));
                second = "confirm" + result && true % 2E009;
                third <= isDone(first,second, ___) * true == func(call[7-"str"]);
                // This is a comment
            while(increment + 1 * loop);
            /* dowhile without 
            brackets*/
        }
        int res, BBBBBBB[6], TTTTTTT[66666666], SSSSSSSS[000000];
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType()),VarDecl("BTS",ArrayPointerType(StringType())),VarDecl("Suga",BoolType())],VoidType(),Block([Dowhile([BinaryOp("=",Id("first"),BinaryOp("||",BinaryOp("*",BinaryOp("/",Id("assign"),Id("num")),Id("result")),BinaryOp(">=",BooleanLiteral(False),BinaryOp("+",UnaryOp("!",BooleanLiteral(True)),BinaryOp("*",ArrayCell(Id("foo"),IntLiteral(35)),UnaryOp("-",ArrayCell(ArrayCell(Id("arr"),StringLiteral("string")),Id("res")))))))),BinaryOp("=",Id("second"),BinaryOp("&&",BinaryOp("+",StringLiteral("confirm"),Id("result")),BinaryOp("%",BooleanLiteral(True),FloatLiteral(2000000000.0)))),BinaryOp("==",BinaryOp("<=",Id("third"),BinaryOp("*",CallExpr(Id("isDone"),[Id("first"),Id("second"),Id("___")]),BooleanLiteral(True))),CallExpr(Id("func"),[ArrayCell(Id("call"),BinaryOp("-",IntLiteral(7),StringLiteral("str")))]))],BinaryOp("+",Id("increment"),BinaryOp("*",IntLiteral(1),Id("loop"))))])),VarDecl("res",IntType()),VarDecl("BBBBBBB",ArrayType(6,IntType())),VarDecl("TTTTTTT",ArrayType(66666666,IntType())),VarDecl("SSSSSSSS",ArrayType(0,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_dowhile_statements_2(self):
        input = """
        float[] foreverYoung(string BTS[]) {
            do 
                assign;
                if (!is(eternal)) 
                    continue;
                else 
                    do 
                        first_step * 25 + "" == 9.000e3;
                        second = step >=25 + 4 && foo((((arr[2]))));
                    while(eternal == "true");
                assign = 9;
            while (Army_G0);
            boolean T,FFFFF[20], TTTT_FFF;
        }
        """
        expect = str(Program([FuncDecl(Id("foreverYoung"),[VarDecl("BTS",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([Dowhile([Id("assign"),If(UnaryOp("!",CallExpr(Id("is"),[Id("eternal")])),Continue(),Dowhile([BinaryOp("==",BinaryOp("+",BinaryOp("*",Id("first_step"),IntLiteral(25)),StringLiteral("")),FloatLiteral(9000.0)),BinaryOp("=",Id("second"),BinaryOp("&&",BinaryOp(">=",Id("step"),BinaryOp("+",IntLiteral(25),IntLiteral(4))),CallExpr(Id("foo"),[ArrayCell(Id("arr"),IntLiteral(2))])))],BinaryOp("==",Id("eternal"),StringLiteral("true")))),BinaryOp("=",Id("assign"),IntLiteral(9))],Id("Army_G0")),VarDecl("T",BoolType()),VarDecl("FFFFF",ArrayType(20,BoolType())),VarDecl("TTTT_FFF",BoolType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_dowhile_statements_3(self):
        input = """
        int Y00NG1[100]; string Seesaw[55], value;
        void Proccess(int main) {
            do
                assign = new_va1+7*25/!t;
                {}
                {
                    {
                        {
                            foo(a+9);
                        }
                    }
                    {
                        // Empty
                    }
                }
                {{{{{{}}}}}}
            while((arr[2]));
        }
        string World; 
        boolean Welcome[997], ATS, PPLLLLL;
        """
        expect = str(Program([VarDecl("Y00NG1",ArrayType(100,IntType())),VarDecl("Seesaw",ArrayType(55,StringType())),VarDecl("value",StringType()),FuncDecl(Id("Proccess"),[VarDecl("main",IntType())],VoidType(),Block([Dowhile([BinaryOp("=",Id("assign"),BinaryOp("+",Id("new_va1"),BinaryOp("/",BinaryOp("*",IntLiteral(7),IntLiteral(25)),UnaryOp("!",Id("t"))))),Block([]),Block([Block([Block([CallExpr(Id("foo"),[BinaryOp("+",Id("a"),IntLiteral(9))])])]),Block([])]),Block([Block([Block([Block([Block([Block([])])])])])])],ArrayCell(Id("arr"),IntLiteral(2)))])),VarDecl("World",StringType()),VarDecl("Welcome",ArrayType(997,BoolType())),VarDecl("ATS",BoolType()),VarDecl("PPLLLLL",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_dowhile_statements_4(self):
        input = """
        int aaaaa,_____, XTSD,_234asf;
        string[] VOID(int _void_, string vvoo[]) {
            if (a - - b*7 < "Real") 
                do 
                    {}
                    {}
                    {}
                    {}
                    {} {{{{}}}}
                    (((((((((multiple * brackets)))))))));
                while (empty * 0);
        }
        boolean r1ght, _wr0ng[2];
        """
        expect = str(Program([VarDecl("aaaaa",IntType()),VarDecl("_____",IntType()),VarDecl("XTSD",IntType()),VarDecl("_234asf",IntType()),FuncDecl(Id("VOID"),[VarDecl("_void_",IntType()),VarDecl("vvoo",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([If(BinaryOp("<",BinaryOp("-",Id("a"),BinaryOp("*",UnaryOp("-",Id("b")),IntLiteral(7))),StringLiteral("Real")),Dowhile([Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([Block([Block([])])])]),BinaryOp("*",Id("multiple"),Id("brackets"))],BinaryOp("*",Id("empty"),IntLiteral(0))))])),VarDecl("r1ght",BoolType()),VarDecl("_wr0ng",ArrayType(2,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_for_statements(self):
        input = """
        int main()
        {
            int i;
            for (i=1; i<=3; i+inc(1))
            {
                printf("%d\\n", i);
            }
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(3)),BinaryOp("+",Id("i"),CallExpr(Id("inc"),[IntLiteral(1)])),Block([CallExpr(Id("printf"),[StringLiteral("%d\\n"),Id("i")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_for_statements_1(self):
        input = """
        void main() {
            int a, jjj[2], q, x;
            for(t;j;5-9||4) 
                return true;
            for(1;2;3) {}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("jjj",ArrayType(2,IntType())),VarDecl("q",IntType()),VarDecl("x",IntType()),For(Id("t"),Id("j"),BinaryOp("||",BinaryOp("-",IntLiteral(5),IntLiteral(9)),IntLiteral(4)),Return(BooleanLiteral(True))),For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_for_statements_2(self):
        input = """
        void main() {
            for(foo(3); a = 9; arr[35] && 0.0E7) {
                for (xxxx;yyyyy;zzzzz)
                    do 
                    {int a;} {} {}
                    //Comment
                    for(loop1; loop2; loop3) {
                        {
                            //Comment
                            for(1==1; 2 + "string"; false) 
                                PPL_is_great(123);
                        }
                    }
                    while(false);

            }
        }
        """    
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(CallExpr(Id("foo"),[IntLiteral(3)]),BinaryOp("=",Id("a"),IntLiteral(9)),BinaryOp("&&",ArrayCell(Id("arr"),IntLiteral(35)),FloatLiteral(0.0)),Block([For(Id("xxxx"),Id("yyyyy"),Id("zzzzz"),Dowhile([Block([VarDecl("a",IntType())]),Block([]),Block([]),For(Id("loop1"),Id("loop2"),Id("loop3"),Block([Block([For(BinaryOp("==",IntLiteral(1),IntLiteral(1)),BinaryOp("+",IntLiteral(2),StringLiteral("string")),BooleanLiteral(False),CallExpr(Id("PPL_is_great"),[IntLiteral(123)]))])]))],BooleanLiteral(False)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_for_statements_3(self):
        input = """
        /* C program to sort N numbers in ascending order using Bubble sort
        * and print both the given and the sorted array
        */
        void main()
        {
            int array[1000];
            int i, j, num, temp;
 
            printf("Enter the value of num ");
            scanf("%d", _num);
            printf("Enter the elements one by one ");
            for (i = 0; i < num; inc(i))
            {
                scanf("%d", _array[i]);
            }
            printf("Input array is ");
            for (i = 0; i < num; inc(arr[i]))
            {
                printf("%d", array[i]);
            }
            /*   Bubble sorting begins */
                for (i = 0; i < num; i)
                {
                    for (j = 0; j < (num - i - 1); j+foo(2)[3])
                    {
                        if (array[j] > array[j + 1])
                    {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        printf("Sorted array is...");
        for (i = 0; i < num; i+-1+"string")
        {
            printf("%d", array[i]);
        }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("array",ArrayType(1000,IntType())),VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("num",IntType()),VarDecl("temp",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter the value of num ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_num")]),CallExpr(Id("printf"),[StringLiteral("Enter the elements one by one ")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("num")),CallExpr(Id("inc"),[Id("i")]),Block([CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(Id("_array"),Id("i"))])])),CallExpr(Id("printf"),[StringLiteral("Input array is ")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("num")),CallExpr(Id("inc"),[ArrayCell(Id("arr"),Id("i"))]),Block([CallExpr(Id("printf"),[StringLiteral("%d"),ArrayCell(Id("array"),Id("i"))])])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("num")),Id("i"),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",BinaryOp("-",Id("num"),Id("i")),IntLiteral(1))),BinaryOp("+",Id("j"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(3))),Block([If(BinaryOp(">",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),Block([BinaryOp("=",Id("temp"),ArrayCell(Id("array"),Id("j"))),BinaryOp("=",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1))),Id("temp"))]))]))])),CallExpr(Id("printf"),[StringLiteral("Sorted array is...")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("num")),BinaryOp("+",BinaryOp("+",Id("i"),UnaryOp("-",IntLiteral(1))),StringLiteral("string")),Block([CallExpr(Id("printf"),[StringLiteral("%d"),ArrayCell(Id("array"),Id("i"))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_for_statements_4(self):
        input = """
        void main()
        {
            int i, num; string odd_sum , even_sum;
 
            printf("Enter the value of num");
            scanf("%d", _num);
            for ("hello"; i <= "world"; i+a)
            {
                if (i % 2 == 0)
                    even_sum = even_sum + i;
                else
                    for(t*t-t+t;_+_-_*_;inc(35)[foo(7)])
                        odd_sum = odd_sum + i;
            }
        printf("Sum of all odd numbers  = %d\\n", odd_sum);
        printf("Sum of all even numbers = %d\\n", even_sum);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("num",IntType()),VarDecl("odd_sum",StringType()),VarDecl("even_sum",StringType()),CallExpr(Id("printf"),[StringLiteral("Enter the value of num")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_num")]),For(StringLiteral("hello"),BinaryOp("<=",Id("i"),StringLiteral("world")),BinaryOp("+",Id("i"),Id("a")),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),BinaryOp("=",Id("even_sum"),BinaryOp("+",Id("even_sum"),Id("i"))),For(BinaryOp("+",BinaryOp("-",BinaryOp("*",Id("t"),Id("t")),Id("t")),Id("t")),BinaryOp("-",BinaryOp("+",Id("_"),Id("_")),BinaryOp("*",Id("_"),Id("_"))),ArrayCell(CallExpr(Id("inc"),[IntLiteral(35)]),CallExpr(Id("foo"),[IntLiteral(7)])),BinaryOp("=",Id("odd_sum"),BinaryOp("+",Id("odd_sum"),Id("i")))))])),CallExpr(Id("printf"),[StringLiteral("Sum of all odd numbers  = %d\\n"),Id("odd_sum")]),CallExpr(Id("printf"),[StringLiteral("Sum of all even numbers = %d\\n"),Id("even_sum")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_other_statements(self):
        input = """
        int i;
        int f() {
            return 200;
        }
        void main() {
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
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_other_statements_1(self):
        input = """
        void binary_search(int list[], int lo, int hi, int key)
        {
            int mid;
 
            if (lo > hi)
            {
                int re, ANS, _404_;
                printf("Key not found\\n");
                break;
            }
            mid = (lo + hi) / 2;
            if (list[mid] == key)
            {
                printf("Key found\\n");
            }
            else if (list[mid] > key)
            {
                binary_search(list, lo, mid - 1, key);
            }
            else if (list[mid] < key)
            {
                binary_search(list, mid + 1, hi, key);
            }
            continue;
            return;
        }
        """
        expect = str(Program([FuncDecl(Id("binary_search"),[VarDecl("list",ArrayPointerType(IntType())),VarDecl("lo",IntType()),VarDecl("hi",IntType()),VarDecl("key",IntType())],VoidType(),Block([VarDecl("mid",IntType()),If(BinaryOp(">",Id("lo"),Id("hi")),Block([VarDecl("re",IntType()),VarDecl("ANS",IntType()),VarDecl("_404_",IntType()),CallExpr(Id("printf"),[StringLiteral("Key not found\\n")]),Break()])),BinaryOp("=",Id("mid"),BinaryOp("/",BinaryOp("+",Id("lo"),Id("hi")),IntLiteral(2))),If(BinaryOp("==",ArrayCell(Id("list"),Id("mid")),Id("key")),Block([CallExpr(Id("printf"),[StringLiteral("Key found\\n")])]),If(BinaryOp(">",ArrayCell(Id("list"),Id("mid")),Id("key")),Block([CallExpr(Id("binary_search"),[Id("list"),Id("lo"),BinaryOp("-",Id("mid"),IntLiteral(1)),Id("key")])]),If(BinaryOp("<",ArrayCell(Id("list"),Id("mid")),Id("key")),Block([CallExpr(Id("binary_search"),[Id("list"),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("hi"),Id("key")])])))),Continue(),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_other_statements_2(self):
        input = """
        int main()
        {
            int size, key; count = 0;
            int list[20];
            int i;
 
            printf("Enter the size of the list: ");
            scanf("%d", _size);
            printf("Printing the list:\\n");
            for (i = 0; i < size; i+1)
            {
                list[i] = rand() % size;
                printf("%d    ", list[i]);
                {
                    return;
                    break;
                }
            }
            printf("\\nEnter the key to find it's occurence: ");
            scanf("%d", _key);
            {
                {
                    //comment
                }
            }
            occur(list, size, 0, key, _count);
            printf("%d occurs for %d times.\\n", key, count);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("size",IntType()),VarDecl("key",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),VarDecl("list",ArrayType(20,IntType())),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter the size of the list: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_size")]),CallExpr(Id("printf"),[StringLiteral("Printing the list:\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("size")),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",ArrayCell(Id("list"),Id("i")),BinaryOp("%",CallExpr(Id("rand"),[]),Id("size"))),CallExpr(Id("printf"),[StringLiteral("%d    "),ArrayCell(Id("list"),Id("i"))]),Block([Return(),Break()])])),CallExpr(Id("printf"),[StringLiteral("\\nEnter the key to find it's occurence: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_key")]),Block([Block([])]),CallExpr(Id("occur"),[Id("list"),Id("size"),IntLiteral(0),Id("key"),Id("_count")]),CallExpr(Id("printf"),[StringLiteral("%d occurs for %d times.\\n"),Id("key"),Id("count")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_other_statements_3(self):
        input = """
        string caps_check(string str[])
        {
            int i;
            do 
            {
                {
                    {break;}
                }
                if ( isupper(  str[i]  ) )
                {
                    return str[i];
                }
                i+1;
            } while(str[i] != "end_of_file");
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("caps_check"),[VarDecl("str",ArrayPointerType(StringType()))],StringType(),Block([VarDecl("i",IntType()),Dowhile([Block([Block([Block([Break()])]),If(CallExpr(Id("isupper"),[ArrayCell(Id("str"),Id("i"))]),Block([Return(ArrayCell(Id("str"),Id("i")))])),BinaryOp("+",Id("i"),IntLiteral(1))])],BinaryOp("!=",ArrayCell(Id("str"),Id("i")),StringLiteral("end_of_file"))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_other_statements_4(self):
        input = """
        void func(int a, float b[], boolean CDXFS[]) {
            int a,b,c;
            a=b=c=5;
            float f[5];
            if (a==b) f[0] = 1.0; break;
            {
                foo(25) - 9.05e3 * "string" || assign = 0 % ax;
                return;
                {{}}
            }
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("CDXFS",ArrayPointerType(BoolType()))],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),VarDecl("f",ArrayType(5,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0))),Break(),Block([BinaryOp("=",BinaryOp("||",BinaryOp("-",CallExpr(Id("foo"),[IntLiteral(25)]),BinaryOp("*",FloatLiteral(9050.0),StringLiteral("string"))),Id("assign")),BinaryOp("%",IntLiteral(0),Id("ax"))),Return(),Block([Block([])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_complete_program(self):
        input = """
        //include <stdio.h>
 
        int main()
        {
            string s[1000], r[1000];
            int begin, end, count;
 
            printf("Input a string\\n");
            gets(s);
 
            // Calculating string length
            do
            {}
            while (s[count] != "\\t");
            count+1;
 
            end = count - 1;
            dec;
            
            for (begin = 0; begin < count; begin - dec(foo(2)[3]) ) {
                r[begin] = s[end];
                end-1;
            }
 
            r[begin] = "";
 
            printf("%s\\n", r);
 
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",ArrayType(1000,StringType())),VarDecl("r",ArrayType(1000,StringType())),VarDecl("begin",IntType()),VarDecl("end",IntType()),VarDecl("count",IntType()),CallExpr(Id("printf"),[StringLiteral("Input a string\\n")]),CallExpr(Id("gets"),[Id("s")]),Dowhile([Block([])],BinaryOp("!=",ArrayCell(Id("s"),Id("count")),StringLiteral("\\t"))),BinaryOp("+",Id("count"),IntLiteral(1)),BinaryOp("=",Id("end"),BinaryOp("-",Id("count"),IntLiteral(1))),Id("dec"),For(BinaryOp("=",Id("begin"),IntLiteral(0)),BinaryOp("<",Id("begin"),Id("count")),BinaryOp("-",Id("begin"),CallExpr(Id("dec"),[ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(3))])),Block([BinaryOp("=",ArrayCell(Id("r"),Id("begin")),ArrayCell(Id("s"),Id("end"))),BinaryOp("-",Id("end"),IntLiteral(1))])),BinaryOp("=",ArrayCell(Id("r"),Id("begin")),StringLiteral("")),CallExpr(Id("printf"),[StringLiteral("%s\\n"),Id("r")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_complete_program_1(self):
        input = """
        int check_armstrong(int n) {
            int sum, temp;
            int remainder; digits = 0;
   
            temp = n;
 
            do
                digits+inc(2,7,"increase")[4];
                temp = temp/10;
            while (temp != 0);
   
            temp = n;
            do remainder = temp%10;
                sum = sum + power(remainder, digits);
                temp = temp/10;
            while (temp != 0);

            if (n == sum)
                return 1;
            else
                return 0;
        }
 
        int  power(int n, int r) {
            int BTS;
            Yoongi = 1;
            for (c = 1; c <= r; c+1)
                p = p*n;
     
            return p;  
        }
        """
        expect = str(Program([FuncDecl(Id("check_armstrong"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("sum",IntType()),VarDecl("temp",IntType()),VarDecl("remainder",IntType()),BinaryOp("=",Id("digits"),IntLiteral(0)),BinaryOp("=",Id("temp"),Id("n")),Dowhile([BinaryOp("+",Id("digits"),ArrayCell(CallExpr(Id("inc"),[IntLiteral(2),IntLiteral(7),StringLiteral("increase")]),IntLiteral(4))),BinaryOp("=",Id("temp"),BinaryOp("/",Id("temp"),IntLiteral(10)))],BinaryOp("!=",Id("temp"),IntLiteral(0))),BinaryOp("=",Id("temp"),Id("n")),Dowhile([BinaryOp("=",Id("remainder"),BinaryOp("%",Id("temp"),IntLiteral(10))),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),CallExpr(Id("power"),[Id("remainder"),Id("digits")]))),BinaryOp("=",Id("temp"),BinaryOp("/",Id("temp"),IntLiteral(10)))],BinaryOp("!=",Id("temp"),IntLiteral(0))),If(BinaryOp("==",Id("n"),Id("sum")),Return(IntLiteral(1)),Return(IntLiteral(0)))])),FuncDecl(Id("power"),[VarDecl("n",IntType()),VarDecl("r",IntType())],IntType(),Block([VarDecl("BTS",IntType()),BinaryOp("=",Id("Yoongi"),IntLiteral(1)),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),Id("r")),BinaryOp("+",Id("c"),IntLiteral(1)),BinaryOp("=",Id("p"),BinaryOp("*",Id("p"),Id("n")))),Return(Id("p"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_complete_program_2(self):
        input = """
        int main () {
            int c, a, b;
   
            printf("Input two integers");
            scanf("%d%d", _a, _b);
   
            for (c == a||b; c <= b; c+1) {
                if (check_armstrong(c) == 1)
                    printf("%dn", c);
            }
     
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",IntType()),VarDecl("a",IntType()),VarDecl("b",IntType()),CallExpr(Id("printf"),[StringLiteral("Input two integers")]),CallExpr(Id("scanf"),[StringLiteral("%d%d"),Id("_a"),Id("_b")]),For(BinaryOp("||",BinaryOp("==",Id("c"),Id("a")),Id("b")),BinaryOp("<=",Id("c"),Id("b")),BinaryOp("+",Id("c"),IntLiteral(1)),Block([If(BinaryOp("==",CallExpr(Id("check_armstrong"),[Id("c")]),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("%dn"),Id("c")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_complete_program_3(self):
        input = """
        int global[444444], local[000000];
        float bxyz[887978], CASGS, JUNG_919;
        boolean Local, _[453400], _234sfds;

        int main () {
            if (rank != SIZE/2) {
	            Stat;    	
    	        // Calculate row value
    	        int res[100]; 
    	        int row, col;   
    	        for (row = 0; row < SIZE; inc(row)) { // row in Matrix 2
        	        (res[0])[row] = 0;
                    (res[1])[row] = 0;          
        	        for (col = 0; col < SIZE; col[0]) {
            		    (res[0])[row] >= (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
            		    (res[1])[row] + (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
		            }
    	        }	

    	        MPI_Send(res, SIZE*2, MPI_INTEGER, SIZE/2, tag, MPI_COMM_WORLD);
            }
    
            if(rank == SIZE/2) {
                printf("Result: ");
                int Matrix_R[10];

	            int i;
                for (i = 0; i < SIZE/2; i+0) {
                    MPI_Recv(Matrix_R[2*i], SIZE*2, MPI_INTEGER, i, tag, MPI_COMM_WORLD, Stat);
	            }
            }
        }"""
        expect = str(Program([VarDecl("global",ArrayType(444444,IntType())),VarDecl("local",ArrayType(0,IntType())),VarDecl("bxyz",ArrayType(887978,FloatType())),VarDecl("CASGS",FloatType()),VarDecl("JUNG_919",FloatType()),VarDecl("Local",BoolType()),VarDecl("_",ArrayType(453400,BoolType())),VarDecl("_234sfds",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",Id("rank"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),Block([Id("Stat"),VarDecl("res",ArrayType(100,IntType())),VarDecl("row",IntType()),VarDecl("col",IntType()),For(BinaryOp("=",Id("row"),IntLiteral(0)),BinaryOp("<",Id("row"),Id("SIZE")),CallExpr(Id("inc"),[Id("row")]),Block([BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),IntLiteral(0)),BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),IntLiteral(0)),For(BinaryOp("=",Id("col"),IntLiteral(0)),BinaryOp("<",Id("col"),Id("SIZE")),ArrayCell(Id("col"),IntLiteral(0)),Block([BinaryOp(">=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col")))),BinaryOp("+",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col"))))]))])),CallExpr(Id("MPI_Send"),[Id("res"),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),BinaryOp("/",Id("SIZE"),IntLiteral(2)),Id("tag"),Id("MPI_COMM_WORLD")])])),If(BinaryOp("==",Id("rank"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),Block([CallExpr(Id("printf"),[StringLiteral("Result: ")]),VarDecl("Matrix_R",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),BinaryOp("+",Id("i"),IntLiteral(0)),Block([CallExpr(Id("MPI_Recv"),[ArrayCell(Id("Matrix_R"),BinaryOp("*",IntLiteral(2),Id("i"))),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),Id("i"),Id("tag"),Id("MPI_COMM_WORLD"),Id("Stat")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_complete_program_4(self):
        input = """
        int global[444444], local[000000];
        float bxyz[887978], CASGS, JUNG_919;
        boolean Local, _[453400], _234sfds;

        int main () {
            if (rank != SIZE/2) {
	            Stat;    	
    	        // Calculate row value
    	        int res[100]; 
    	        int row, col;   
    	        for (row = 0; row < SIZE; inc(row)) { // row in Matrix 2
        	        (res[0])[row] = 0;
                    (res[1])[row] = 0;          
        	        do {
            		    (res[0])[row] >= (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
            		    (res[1])[row] + (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
		            } while(col = 0 * col < SIZE == col[0]); 
    	        }	

                /* cmt
                 * cmt
                */

    	        MPI_Send(res, SIZE*2, MPI_INTEGER, SIZE/2, tag, MPI_COMM_WORLD);
            }
    
            if(rank == SIZE/2) {
                printf("Result: ");
                int Matrix_R[10];
                return "Hello World!";

	            int i;
                for (i = 0; i < SIZE/2; i+0) {
                    MPI_Recv(Matrix_R[2*i], SIZE*2, MPI_INTEGER, i, tag, MPI_COMM_WORLD, Stat);
	            }
            }
        }"""
        expect = str(Program([VarDecl("global",ArrayType(444444,IntType())),VarDecl("local",ArrayType(0,IntType())),VarDecl("bxyz",ArrayType(887978,FloatType())),VarDecl("CASGS",FloatType()),VarDecl("JUNG_919",FloatType()),VarDecl("Local",BoolType()),VarDecl("_",ArrayType(453400,BoolType())),VarDecl("_234sfds",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",Id("rank"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),Block([Id("Stat"),VarDecl("res",ArrayType(100,IntType())),VarDecl("row",IntType()),VarDecl("col",IntType()),For(BinaryOp("=",Id("row"),IntLiteral(0)),BinaryOp("<",Id("row"),Id("SIZE")),CallExpr(Id("inc"),[Id("row")]),Block([BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),IntLiteral(0)),BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),IntLiteral(0)),Dowhile([Block([BinaryOp(">=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col")))),BinaryOp("+",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col"))))])],BinaryOp("=",Id("col"),BinaryOp("==",BinaryOp("<",BinaryOp("*",IntLiteral(0),Id("col")),Id("SIZE")),ArrayCell(Id("col"),IntLiteral(0)))))])),CallExpr(Id("MPI_Send"),[Id("res"),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),BinaryOp("/",Id("SIZE"),IntLiteral(2)),Id("tag"),Id("MPI_COMM_WORLD")])])),If(BinaryOp("==",Id("rank"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),Block([CallExpr(Id("printf"),[StringLiteral("Result: ")]),VarDecl("Matrix_R",ArrayType(10,IntType())),Return(StringLiteral("Hello World!")),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),BinaryOp("+",Id("i"),IntLiteral(0)),Block([CallExpr(Id("MPI_Recv"),[ArrayCell(Id("Matrix_R"),BinaryOp("*",IntLiteral(2),Id("i"))),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),Id("i"),Id("tag"),Id("MPI_COMM_WORLD"),Id("Stat")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_complete_program_5(self):
        input = """
        int global[444444], local[000000];

        int main () {
            if (rank != SIZE/2) {
	            Stat;    	
    	        // Calculate row value
    	        int res[100]; 
    	        int row, col;   
    	        for (row = 0; row < SIZE; inc(row)) { // row in Matrix 2
        	        (res[0])[row] = 0;
                    (res[1])[row] = 0;          
        	        do {
            		    (res[0])[row] >= (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
            		    (res[1])[row] + (Matrix1[rank])[col] * (Matrix2[row])[col];    	   		
		            } while(col = 0 * col < SIZE == col[0]); 
    	        }	

                /* cmt
                 * cmt
                */

    	        MPI_Send(res, SIZE*2, MPI_INTEGER, SIZE/2, tag, MPI_COMM_WORLD);
            }
                {{{}}}
	            int i;
                for (i = 0; i < SIZE/2; i+0) {
                    MPI_Recv(Matrix_R[2*i], SIZE*2, MPI_INTEGER, i, tag, MPI_COMM_WORLD, Stat);
	            }
                {{{}}}
        }
        float bxyz[887978], CASGS, JUNG_919;
        boolean Local, _[453400], _234sfds;"""
        expect = str(Program([VarDecl("global",ArrayType(444444,IntType())),VarDecl("local",ArrayType(0,IntType())),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",Id("rank"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),Block([Id("Stat"),VarDecl("res",ArrayType(100,IntType())),VarDecl("row",IntType()),VarDecl("col",IntType()),For(BinaryOp("=",Id("row"),IntLiteral(0)),BinaryOp("<",Id("row"),Id("SIZE")),CallExpr(Id("inc"),[Id("row")]),Block([BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),IntLiteral(0)),BinaryOp("=",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),IntLiteral(0)),Dowhile([Block([BinaryOp(">=",ArrayCell(ArrayCell(Id("res"),IntLiteral(0)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col")))),BinaryOp("+",ArrayCell(ArrayCell(Id("res"),IntLiteral(1)),Id("row")),BinaryOp("*",ArrayCell(ArrayCell(Id("Matrix1"),Id("rank")),Id("col")),ArrayCell(ArrayCell(Id("Matrix2"),Id("row")),Id("col"))))])],BinaryOp("=",Id("col"),BinaryOp("==",BinaryOp("<",BinaryOp("*",IntLiteral(0),Id("col")),Id("SIZE")),ArrayCell(Id("col"),IntLiteral(0)))))])),CallExpr(Id("MPI_Send"),[Id("res"),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),BinaryOp("/",Id("SIZE"),IntLiteral(2)),Id("tag"),Id("MPI_COMM_WORLD")])])),Block([Block([Block([])])]),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("/",Id("SIZE"),IntLiteral(2))),BinaryOp("+",Id("i"),IntLiteral(0)),Block([CallExpr(Id("MPI_Recv"),[ArrayCell(Id("Matrix_R"),BinaryOp("*",IntLiteral(2),Id("i"))),BinaryOp("*",Id("SIZE"),IntLiteral(2)),Id("MPI_INTEGER"),Id("i"),Id("tag"),Id("MPI_COMM_WORLD"),Id("Stat")])])),Block([Block([Block([])])])])),VarDecl("bxyz",ArrayType(887978,FloatType())),VarDecl("CASGS",FloatType()),VarDecl("JUNG_919",FloatType()),VarDecl("Local",BoolType()),VarDecl("_",ArrayType(453400,BoolType())),VarDecl("_234sfds",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_complete_program_6(self):
        input = """
        int  power(int n, int r) {
            int c, p;
            p = 1;
   
            for (c = 1; c <= r; (2+3)["string"])
                p = p*n;
                break;
     
            return p;  
        }
        """
        expect = str(Program([FuncDecl(Id("power"),[VarDecl("n",IntType()),VarDecl("r",IntType())],IntType(),Block([VarDecl("c",IntType()),VarDecl("p",IntType()),BinaryOp("=",Id("p"),IntLiteral(1)),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),Id("r")),ArrayCell(BinaryOp("+",IntLiteral(2),IntLiteral(3)),StringLiteral("string")),BinaryOp("=",Id("p"),BinaryOp("*",Id("p"),Id("n")))),Break(),Return(Id("p"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_complete_program_7(self):
        input = """
        int main()
        {
            int x, y, t;
 
            printf("Enter two integers\\n");
            scanf("%d%d", _x, _y);
 
            printf("Before Swapping\\nFirst integer = %d\\nSecond integer = %d\\n", x, y);
 
            t = x;
            x = y;
            y = t;
 
            printf("After Swapping\\nFirst integer = %d\\nSecond integer = %d\\n", x, y);
 
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("t",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter two integers\\n")]),CallExpr(Id("scanf"),[StringLiteral("%d%d"),Id("_x"),Id("_y")]),CallExpr(Id("printf"),[StringLiteral("Before Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"),Id("x"),Id("y")]),BinaryOp("=",Id("t"),Id("x")),BinaryOp("=",Id("x"),Id("y")),BinaryOp("=",Id("y"),Id("t")),CallExpr(Id("printf"),[StringLiteral("After Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"),Id("x"),Id("y")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_complete_program_8(self):
        input = """
        int  main()
        {
            int year;
 
            printf("Enter a year to check if it is a leap year\\n");
            scanf("%d", _year);
 
            if (year%400 == 0) // Exactly divisible by 400 e.g. 1600, 2000
                printf("%d is a leap year.\\n", year);
            else if (year%100 == 0) // Exactly divisible by 100 and not by 400 e.g. 1900, 2100
                printf("%d isn't a leap year.\\n", year);
            else if (year%4 == 0) // Exactly divisible by 4 and neither by 100 nor 400 e.g. 2020
                printf("%d is a leap year.\\n", year);
            else // Not divisible by 4 or 100 or 400 e.g. 2017, 2018, 2019
                printf("%d isn't a leap year.\\n", year);  
   
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("year",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a year to check if it is a leap year\\n")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_year")]),If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(400)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a leap year.\\n"),Id("year")]),If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(100)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d isn't a leap year.\\n"),Id("year")]),If(BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(4)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a leap year.\\n"),Id("year")]),CallExpr(Id("printf"),[StringLiteral("%d isn't a leap year.\\n"),Id("year")])))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_complete_program_9(self):
        input = """
        int main()
        {
            int array[100], maximum, size, c; location = 1;
 
            printf("Enter the number of elements in array\\n");
            scanf("%d", size);
            for (c = 0; c < size; c||9e-26)
                scanf("%d", array[c]);
 
            maximum = array[0];
 
            for (c = 1; c < size; c+-0)
            {
                if (array[c] > maximum)
                {
                    maximum  = array[c];
                    location = c+1;
                }
            }
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(100,IntType())),VarDecl("maximum",IntType()),VarDecl("size",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("location"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("Enter the number of elements in array\\n")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("size")]),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),Id("size")),BinaryOp("||",Id("c"),FloatLiteral(9e-26)),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(Id("array"),Id("c"))])),BinaryOp("=",Id("maximum"),ArrayCell(Id("array"),IntLiteral(0))),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<",Id("c"),Id("size")),BinaryOp("+",Id("c"),UnaryOp("-",IntLiteral(0))),Block([If(BinaryOp(">",ArrayCell(Id("array"),Id("c")),Id("maximum")),Block([BinaryOp("=",Id("maximum"),ArrayCell(Id("array"),Id("c"))),BinaryOp("=",Id("location"),BinaryOp("+",Id("c"),IntLiteral(1)))]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_complete_program_10(self):
        input = """
        int main()
        {
            string str[1000];
   
            printf("Input a string to convert to lower case");
            gets(str);
            printf("The string in lower case: %s", strlwr(str));
            break;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("str",ArrayType(1000,StringType())),CallExpr(Id("printf"),[StringLiteral("Input a string to convert to lower case")]),CallExpr(Id("gets"),[Id("str")]),CallExpr(Id("printf"),[StringLiteral("The string in lower case: %s"),CallExpr(Id("strlwr"),[Id("str")])]),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_complete_program_11(self):
        input = """
        string str[100];
        void upper_string(string s[]) {
            c = 0;
            do {
                if (s[c] >= "a" && s[c] <= "0^0") {
                    s[c] = s[c] - 32;
                }
                c+1;
            } while (s[c] != "");
        }
        string[] message(boolean wind) {}
        int func() {}
        """
        expect = str(Program([VarDecl("str",ArrayType(100,StringType())),FuncDecl(Id("upper_string"),[VarDecl("s",ArrayPointerType(StringType()))],VoidType(),Block([BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([Block([If(BinaryOp("&&",BinaryOp(">=",ArrayCell(Id("s"),Id("c")),StringLiteral("a")),BinaryOp("<=",ArrayCell(Id("s"),Id("c")),StringLiteral("0^0"))),Block([BinaryOp("=",ArrayCell(Id("s"),Id("c")),BinaryOp("-",ArrayCell(Id("s"),Id("c")),IntLiteral(32)))])),BinaryOp("+",Id("c"),IntLiteral(1))])],BinaryOp("!=",ArrayCell(Id("s"),Id("c")),StringLiteral("")))])),FuncDecl(Id("message"),[VarDecl("wind",BoolType())],ArrayPointerType(StringType()),Block([])),FuncDecl(Id("func"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_complete_program_12(self):
        input = """
        string str[100];
        string[] main ()
        {
            int c; c = 0;
            string ch, s[1000];
   
        do 
            ch = s[c];
            if (ch >= "A" && ch <= Z)
                s[c] = s[c] + 32;
            else if (ch >= a && ch <= char[z])
                s[c] = s[c] - 32;  
            c+1;  
        while (s[c] != 0);
        return "completed";
        }
        """
        expect = str(Program([VarDecl("str",ArrayType(100,StringType())),FuncDecl(Id("main"),[],ArrayPointerType(StringType()),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),VarDecl("ch",StringType()),VarDecl("s",ArrayType(1000,StringType())),Dowhile([BinaryOp("=",Id("ch"),ArrayCell(Id("s"),Id("c"))),If(BinaryOp("&&",BinaryOp(">=",Id("ch"),StringLiteral("A")),BinaryOp("<=",Id("ch"),Id("Z"))),BinaryOp("=",ArrayCell(Id("s"),Id("c")),BinaryOp("+",ArrayCell(Id("s"),Id("c")),IntLiteral(32))),If(BinaryOp("&&",BinaryOp(">=",Id("ch"),Id("a")),BinaryOp("<=",Id("ch"),ArrayCell(Id("char"),Id("z")))),BinaryOp("=",ArrayCell(Id("s"),Id("c")),BinaryOp("-",ArrayCell(Id("s"),Id("c")),IntLiteral(32))))),BinaryOp("+",Id("c"),IntLiteral(1))],BinaryOp("!=",ArrayCell(Id("s"),Id("c")),IntLiteral(0))),Return(StringLiteral("completed"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_complete_program_13(self):
        input = """
        int main() {
            int first, second, add, subtract, multiply;
            float divide;
 
            add = first + second;
            subtract = first - second;
            multiply = first * second;
            divide = first / (cast_type(flt))[second];   //typecasting
 
            printf("Sum = %d\\n", add);
            printf("Difference = %d\\n", subtract);
            continue;
            printf("Multiplication = %d\\n", multiply);
            printf("Division = %.2f\\n", divide);
 
            return ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("first",IntType()),VarDecl("second",IntType()),VarDecl("add",IntType()),VarDecl("subtract",IntType()),VarDecl("multiply",IntType()),VarDecl("divide",FloatType()),BinaryOp("=",Id("add"),BinaryOp("+",Id("first"),Id("second"))),BinaryOp("=",Id("subtract"),BinaryOp("-",Id("first"),Id("second"))),BinaryOp("=",Id("multiply"),BinaryOp("*",Id("first"),Id("second"))),BinaryOp("=",Id("divide"),BinaryOp("/",Id("first"),ArrayCell(CallExpr(Id("cast_type"),[Id("flt")]),Id("second")))),CallExpr(Id("printf"),[StringLiteral("Sum = %d\\n"),Id("add")]),CallExpr(Id("printf"),[StringLiteral("Difference = %d\\n"),Id("subtract")]),Continue(),CallExpr(Id("printf"),[StringLiteral("Multiplication = %d\\n"),Id("multiply")]),CallExpr(Id("printf"),[StringLiteral("Division = %.2f\\n"),Id("divide")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_complete_program_14(self):
        input = """
        float global;
        void factorial(int n)
        {
            int c;
            result = 1;
 
            for (c = 1; c <= n; c+"str")
                result = result*c;
 
            return null;
        }
        """
        expect = str(Program([VarDecl("global",FloatType()),FuncDecl(Id("factorial"),[VarDecl("n",IntType())],VoidType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("result"),IntLiteral(1)),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),Id("n")),BinaryOp("+",Id("c"),StringLiteral("str")),BinaryOp("=",Id("result"),BinaryOp("*",Id("result"),Id("c")))),Return(Id("null"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_complete_program_15(self):
        input = """
        float global;
        void diamond(int n)
        {
            int n, c, k; space = 1;
            space = n - 1;
 
            for (k = 1; k <= n; true)
            {
                for (c == 1; c <= 0.0E7*-space; "str")
                    printf(" ");
 
                space;
                for (c = 1; c <= 2*k-1; c)
                printf("*");
            }
 
            space = 1;
            for (k = 1; k <= n - 1; k*0)
            {
                for (c = 1; c <= space; false)
                    printf(" ");
 
                space[foo[3*temp(("str")[2])]];
                for (c = 1 ; c <= 2*(n-k)-1; c+0)
                    printf("*");
            }
            return 0;
        }
        """
        expect = str(Program([VarDecl("global",FloatType()),FuncDecl(Id("diamond"),[VarDecl("n",IntType())],VoidType(),Block([VarDecl("n",IntType()),VarDecl("c",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("space"),IntLiteral(1)),BinaryOp("=",Id("space"),BinaryOp("-",Id("n"),IntLiteral(1))),For(BinaryOp("=",Id("k"),IntLiteral(1)),BinaryOp("<=",Id("k"),Id("n")),BooleanLiteral(True),Block([For(BinaryOp("==",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),BinaryOp("*",FloatLiteral(0.0),UnaryOp("-",Id("space")))),StringLiteral("str"),CallExpr(Id("printf"),[StringLiteral(" ")])),Id("space"),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),BinaryOp("-",BinaryOp("*",IntLiteral(2),Id("k")),IntLiteral(1))),Id("c"),CallExpr(Id("printf"),[StringLiteral("*")]))])),BinaryOp("=",Id("space"),IntLiteral(1)),For(BinaryOp("=",Id("k"),IntLiteral(1)),BinaryOp("<=",Id("k"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("*",Id("k"),IntLiteral(0)),Block([For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),Id("space")),BooleanLiteral(False),CallExpr(Id("printf"),[StringLiteral(" ")])),ArrayCell(Id("space"),ArrayCell(Id("foo"),BinaryOp("*",IntLiteral(3),CallExpr(Id("temp"),[ArrayCell(StringLiteral("str"),IntLiteral(2))])))),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),BinaryOp("-",BinaryOp("*",IntLiteral(2),BinaryOp("-",Id("n"),Id("k"))),IntLiteral(1))),BinaryOp("+",Id("c"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("*")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_complete_program_16(self):
        input = """
        float global;
        void factorial(int n)
        {
            int c;
            do
                for(d = 0; d < n; 10)
                scanf("%d", (matrix[c])[d]);
            while(0 != 1);
            for (c = 0; c < m; c+0)
                for( d = 0 ; d < n ; d )
                    (transpose[d])[c] = (matrix[c])[d];
        }
        """
        expect = str(Program([VarDecl("global",FloatType()),FuncDecl(Id("factorial"),[VarDecl("n",IntType())],VoidType(),Block([VarDecl("c",IntType()),Dowhile([For(BinaryOp("=",Id("d"),IntLiteral(0)),BinaryOp("<",Id("d"),Id("n")),IntLiteral(10),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(ArrayCell(Id("matrix"),Id("c")),Id("d"))]))],BinaryOp("!=",IntLiteral(0),IntLiteral(1))),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),Id("m")),BinaryOp("+",Id("c"),IntLiteral(0)),For(BinaryOp("=",Id("d"),IntLiteral(0)),BinaryOp("<",Id("d"),Id("n")),Id("d"),BinaryOp("=",ArrayCell(ArrayCell(Id("transpose"),Id("d")),Id("c")),ArrayCell(ArrayCell(Id("matrix"),Id("c")),Id("d")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_complete_program_17(self):
        input = """
        float global;
        void cmp(int n)
        {
            string a[100], b[100];
 
            if (strcmp(str[a],foo(b)) == 0)
                printf("The strings are equal.");
            else
                printf("The strings are not equal.");
 
            return 0;
        }
        """
        expect = str(Program([VarDecl("global",FloatType()),FuncDecl(Id("cmp"),[VarDecl("n",IntType())],VoidType(),Block([VarDecl("a",ArrayType(100,StringType())),VarDecl("b",ArrayType(100,StringType())),If(BinaryOp("==",CallExpr(Id("strcmp"),[ArrayCell(Id("str"),Id("a")),CallExpr(Id("foo"),[Id("b")])]),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("The strings are equal.")]),CallExpr(Id("printf"),[StringLiteral("The strings are not equal.")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_complete_program_18(self):
        input = """
        int compare_strings(string a[], string b[])
        {
            int c; c = 0;
            do {}
                if (a[c] == 0 || b[c] == _)
                    break;
                inc(35)["str"];
            while (a[c] == b[c]);           
   
            if (a[c] == 404 && b[c] == abc)
                return 0;
            else
                return -1;
        }
        """
        expect = str(Program([FuncDecl(Id("compare_strings"),[VarDecl("a",ArrayPointerType(StringType())),VarDecl("b",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([Block([]),If(BinaryOp("||",BinaryOp("==",ArrayCell(Id("a"),Id("c")),IntLiteral(0)),BinaryOp("==",ArrayCell(Id("b"),Id("c")),Id("_"))),Break()),ArrayCell(CallExpr(Id("inc"),[IntLiteral(35)]),StringLiteral("str"))],BinaryOp("==",ArrayCell(Id("a"),Id("c")),ArrayCell(Id("b"),Id("c")))),If(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("a"),Id("c")),IntLiteral(404)),BinaryOp("==",ArrayCell(Id("b"),Id("c")),Id("abc"))),Return(IntLiteral(0)),Return(UnaryOp("-",IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_complete_program_19(self):
        input = """
        int main(string argv[], int argc)
        {
            100;
            100*25-6||"string" && literals;
            string str[1000], sub[1000];
            int position, length; c = 0;
            do {
                sub[c] = str[position+c-1];
                {inc[1*foo(a,b,"str")];}
            } while (c < length);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([IntLiteral(100),BinaryOp("||",BinaryOp("-",BinaryOp("*",IntLiteral(100),IntLiteral(25)),IntLiteral(6)),BinaryOp("&&",StringLiteral("string"),Id("literals"))),VarDecl("str",ArrayType(1000,StringType())),VarDecl("sub",ArrayType(1000,StringType())),VarDecl("position",IntType()),VarDecl("length",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([Block([BinaryOp("=",ArrayCell(Id("sub"),Id("c")),ArrayCell(Id("str"),BinaryOp("-",BinaryOp("+",Id("position"),Id("c")),IntLiteral(1)))),Block([ArrayCell(Id("inc"),BinaryOp("*",IntLiteral(1),CallExpr(Id("foo"),[Id("a"),Id("b"),StringLiteral("str")])))])])],BinaryOp("<",Id("c"),Id("length")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_complete_program_20(self):
        input = """
        int main(string argv[], int argc)
        {
            100;
            do {
                do 
                    pointer = substring(str, position, length);
                    printf("%s\\n", pointer);
                    free(pointer);
                    length+goo();
                while (length <= temp);
                temp-1;
                position+1;
                length = 1;
            } while (position <= string_length);
            100*25-6||"string" && literals;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([IntLiteral(100),Dowhile([Block([Dowhile([BinaryOp("=",Id("pointer"),CallExpr(Id("substring"),[Id("str"),Id("position"),Id("length")])),CallExpr(Id("printf"),[StringLiteral("%s\\n"),Id("pointer")]),CallExpr(Id("free"),[Id("pointer")]),BinaryOp("+",Id("length"),CallExpr(Id("goo"),[]))],BinaryOp("<=",Id("length"),Id("temp"))),BinaryOp("-",Id("temp"),IntLiteral(1)),BinaryOp("+",Id("position"),IntLiteral(1)),BinaryOp("=",Id("length"),IntLiteral(1))])],BinaryOp("<=",Id("position"),Id("string_length"))),BinaryOp("||",BinaryOp("-",BinaryOp("*",IntLiteral(100),IntLiteral(25)),IntLiteral(6)),BinaryOp("&&",StringLiteral("string"),Id("literals")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_complete_program_21(self):
        input = """
        int main(string argv[], int argc) {   }
        float solve_for_y(float a, float b, float c)
        {
            float Y;
            if(a == 0) {
                printf("Value of Y cannot be predicted");
            }
            else {
                Y = -(b + c) / a;
            }
            return Y;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("solve_for_y"),[VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType())],FloatType(),Block([VarDecl("Y",FloatType()),If(BinaryOp("==",Id("a"),IntLiteral(0)),Block([CallExpr(Id("printf"),[StringLiteral("Value of Y cannot be predicted")])]),Block([BinaryOp("=",Id("Y"),BinaryOp("/",UnaryOp("-",BinaryOp("+",Id("b"),Id("c"))),Id("a")))])),Return(Id("Y"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_complete_program_22(self):
        input = """
        int main(string argv[], int argc) {   }
        void solution( int a[], int var )
        {
            int k, i, l, j;
 
            for ( k = 0;k < var;k() )
            {
                for ( i = 0;i <= var;i[true] )
                {
                    l = (a[ i ])[ k ];
 
                    for ( j = 0;j <= var;j )
                    {
                        if ( i != k )
                            (a[i])[j] = ((a[k])[k]*(a[i])[j])-(l*a[k])[j];
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("solution"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("var",IntType())],VoidType(),Block([VarDecl("k",IntType()),VarDecl("i",IntType()),VarDecl("l",IntType()),VarDecl("j",IntType()),For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),Id("var")),CallExpr(Id("k"),[]),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("var")),ArrayCell(Id("i"),BooleanLiteral(True)),Block([BinaryOp("=",Id("l"),ArrayCell(ArrayCell(Id("a"),Id("i")),Id("k"))),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<=",Id("j"),Id("var")),Id("j"),Block([If(BinaryOp("!=",Id("i"),Id("k")),BinaryOp("=",ArrayCell(ArrayCell(Id("a"),Id("i")),Id("j")),BinaryOp("-",BinaryOp("*",ArrayCell(ArrayCell(Id("a"),Id("k")),Id("k")),ArrayCell(ArrayCell(Id("a"),Id("i")),Id("j"))),ArrayCell(BinaryOp("*",Id("l"),ArrayCell(Id("a"),Id("k"))),Id("j")))))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_complete_program_23(self):
        input = """
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) {
            int min; min = INT_MAX = min_index;
            int v;
            for (v = 0; v < V; ((v)))
            if (sptSet[v] == 0 && dist[v] <= min)
                min = dist[v]; min_index = v;
 
            return min_index;
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("min",IntType()),BinaryOp("=",Id("min"),BinaryOp("=",Id("INT_MAX"),Id("min_index"))),VarDecl("v",IntType()),For(BinaryOp("=",Id("v"),IntLiteral(0)),BinaryOp("<",Id("v"),Id("V")),Id("v"),If(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("sptSet"),Id("v")),IntLiteral(0)),BinaryOp("<=",ArrayCell(Id("dist"),Id("v")),Id("min"))),BinaryOp("=",Id("min"),ArrayCell(Id("dist"),Id("v"))))),BinaryOp("=",Id("min_index"),Id("v")),Return(Id("min_index"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_complete_program_24(self):
        input = """
        int main(string argv[], int argc) {   }
        int[] minDistance(int dist[], int sptSet[]) {
                {
                    {}
                }
        }   
        void shortestLength(int graph[], int src) {
            for (count = 0; count < V - 1; count[0]) {
                u = minDistance(dist, sptSet);
 
                sptSet[u] = 1;
                int v;
                for (v = 0; v < V; run)
 
                if (!sptSet[v] && (graph[u])[v] && dist[u] != INT_MAX && dist[u]
                    + (graph[u])[v] < dist[v])
                    dist[v] = dist[u] + (graph[u])[v];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Block([Block([])])])),FuncDecl(Id("shortestLength"),[VarDecl("graph",ArrayPointerType(IntType())),VarDecl("src",IntType())],VoidType(),Block([For(BinaryOp("=",Id("count"),IntLiteral(0)),BinaryOp("<",Id("count"),BinaryOp("-",Id("V"),IntLiteral(1))),ArrayCell(Id("count"),IntLiteral(0)),Block([BinaryOp("=",Id("u"),CallExpr(Id("minDistance"),[Id("dist"),Id("sptSet")])),BinaryOp("=",ArrayCell(Id("sptSet"),Id("u")),IntLiteral(1)),VarDecl("v",IntType()),For(BinaryOp("=",Id("v"),IntLiteral(0)),BinaryOp("<",Id("v"),Id("V")),Id("run"),If(BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",UnaryOp("!",ArrayCell(Id("sptSet"),Id("v"))),ArrayCell(ArrayCell(Id("graph"),Id("u")),Id("v"))),BinaryOp("!=",ArrayCell(Id("dist"),Id("u")),Id("INT_MAX"))),BinaryOp("<",BinaryOp("+",ArrayCell(Id("dist"),Id("u")),ArrayCell(ArrayCell(Id("graph"),Id("u")),Id("v"))),ArrayCell(Id("dist"),Id("v")))),BinaryOp("=",ArrayCell(Id("dist"),Id("v")),BinaryOp("+",ArrayCell(Id("dist"),Id("u")),ArrayCell(ArrayCell(Id("graph"),Id("u")),Id("v"))))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_complete_program_25(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_complete_program_26(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) { 
            do
                do
                    do
                        if(s) true; else if(2) quest == run = t["index"]; else 1;
                    while(true);
                while((x-"2"));
            while("crawl");
        }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c_XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c_XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([Dowhile([Dowhile([Dowhile([If(Id("s"),BooleanLiteral(True),If(IntLiteral(2),BinaryOp("=",BinaryOp("==",Id("quest"),Id("run")),ArrayCell(Id("t"),StringLiteral("index"))),IntLiteral(1)))],BooleanLiteral(True))],BinaryOp("-",Id("x"),StringLiteral("2")))],StringLiteral("crawl"))])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c_XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c_XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_complete_program_27(self):
        input = """
        string a,b,x;
        void main(string argv[], int argc) {   }
        int[] _Run(int dream[], int unbreakable) { 
            return reality;
            if (true) 
                for (dream = 0; !dream; wake || dream * 100) {}
            else 
                do 
                    {{ wake[up] == call + "!";}}
                while (dream <= Null);
        }
        float b, X0XX, YYY, ___[343434343], hcmut, edu;
        boolean b, _X0XX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],VoidType(),Block([])),FuncDecl(Id("_Run"),[VarDecl("dream",ArrayPointerType(IntType())),VarDecl("unbreakable",IntType())],ArrayPointerType(IntType()),Block([Return(Id("reality")),If(BooleanLiteral(True),For(BinaryOp("=",Id("dream"),IntLiteral(0)),UnaryOp("!",Id("dream")),BinaryOp("||",Id("wake"),BinaryOp("*",Id("dream"),IntLiteral(100))),Block([])),Dowhile([Block([Block([BinaryOp("==",ArrayCell(Id("wake"),Id("up")),BinaryOp("+",Id("call"),StringLiteral("!")))])])],BinaryOp("<=",Id("dream"),Id("Null"))))])),VarDecl("b",FloatType()),VarDecl("X0XX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("_X0XX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_complete_program_28(self):
        input = """
        void magicsq(int size, int a[])
        {
            int sqr; sqr = size * size;
            i = 0; j = size / 2; k;
 
            for (k = 1; k <= sqr; "this">k) 
            {
                (a[i])[j] = k;
                i;
                j(j+i);
 
                if (k % size == 0) 
                { 
                    i + trip = 2; 
                    j; 
                }
                else 
                {
                    if (j == size) 
                    {
                        j = size;
                    }
                    else if (i < 0)
                    {
                        i + size;
                    }
                }
            }
            for (i = 0; i < size; icr)
            {
                for (j = 0; j < size; -2E9+j*index)
                {
                    printf("%d  ", (a[i])[j]);
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("magicsq"),[VarDecl("size",IntType()),VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("sqr",IntType()),BinaryOp("=",Id("sqr"),BinaryOp("*",Id("size"),Id("size"))),BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("/",Id("size"),IntLiteral(2))),Id("k"),For(BinaryOp("=",Id("k"),IntLiteral(1)),BinaryOp("<=",Id("k"),Id("sqr")),BinaryOp(">",StringLiteral("this"),Id("k")),Block([BinaryOp("=",ArrayCell(ArrayCell(Id("a"),Id("i")),Id("j")),Id("k")),Id("i"),CallExpr(Id("j"),[BinaryOp("+",Id("j"),Id("i"))]),If(BinaryOp("==",BinaryOp("%",Id("k"),Id("size")),IntLiteral(0)),Block([BinaryOp("=",BinaryOp("+",Id("i"),Id("trip")),IntLiteral(2)),Id("j")]),Block([If(BinaryOp("==",Id("j"),Id("size")),Block([BinaryOp("=",Id("j"),Id("size"))]),If(BinaryOp("<",Id("i"),IntLiteral(0)),Block([BinaryOp("+",Id("i"),Id("size"))])))]))])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("size")),Id("icr"),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("size")),BinaryOp("+",UnaryOp("-",FloatLiteral(2000000000.0)),BinaryOp("*",Id("j"),Id("index"))),Block([CallExpr(Id("printf"),[StringLiteral("%d  "),ArrayCell(ArrayCell(Id("a"),Id("i")),Id("j"))])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_complete_program_29(self):
        input = """
        string a,b,x;
        int main()
        {
            float octalnum[0];
            string i; i = 0;
 
            printf("Enter any octal number: ");
            scanf("%s", octalnum);
            printf("Equivalent binary value: ");
            do
            {
                switch (octalnum[i]);
                {}
            }while (octalnum[i]);
        }
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("octalnum",ArrayType(0,FloatType())),VarDecl("i",StringType()),BinaryOp("=",Id("i"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Enter any octal number: ")]),CallExpr(Id("scanf"),[StringLiteral("%s"),Id("octalnum")]),CallExpr(Id("printf"),[StringLiteral("Equivalent binary value: ")]),Dowhile([Block([CallExpr(Id("switch"),[ArrayCell(Id("octalnum"),Id("i"))]),Block([])])],ArrayCell(Id("octalnum"),Id("i")))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_complete_program_30(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_complete_program_31(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {
            a[100] * "str" - foo() && b[100];
            strcpy(b, a);  // Copying input string
            strrev(b);  // Reversing the string
 
            if (strcmp(a, b) == 0)  // Comparing input string with the reverse string
                printf("The string is a palindrome.");
            else {
                printf("The string isn't a palindrome.");
                int res;
                break;
            }
            return 0;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([BinaryOp("&&",BinaryOp("-",BinaryOp("*",ArrayCell(Id("a"),IntLiteral(100)),StringLiteral("str")),CallExpr(Id("foo"),[])),ArrayCell(Id("b"),IntLiteral(100))),CallExpr(Id("strcpy"),[Id("b"),Id("a")]),CallExpr(Id("strrev"),[Id("b")]),If(BinaryOp("==",CallExpr(Id("strcmp"),[Id("a"),Id("b")]),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("The string is a palindrome.")]),Block([CallExpr(Id("printf"),[StringLiteral("The string isn't a palindrome.")]),VarDecl("res",IntType()),Break()])),Return(IntLiteral(0))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_complete_program_32(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
            {
                {
                    {}
                }
            }
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index")),Block([Block([Block([])])])])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_complete_program_33(self):
        input = """
        string a,b,x;
        void main(string argv[], int argc) { 
            if (expr) true; else false;
            if (expr) true; else false;
            if (expr) true; else false;
            if (expr) true; else 
                if (expr) true; else 
                    if (expr) true; else false;
        }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],VoidType(),Block([If(Id("expr"),BooleanLiteral(True),BooleanLiteral(False)),If(Id("expr"),BooleanLiteral(True),BooleanLiteral(False)),If(Id("expr"),BooleanLiteral(True),BooleanLiteral(False)),If(Id("expr"),BooleanLiteral(True),If(Id("expr"),BooleanLiteral(True),If(Id("expr"),BooleanLiteral(True),BooleanLiteral(False))))])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_complete_program_34(self):
        input = """
        string a,b,x;
        int main(string argv[], float argc) { 
            {{
                /*empty*/
            }}
        }
        int min(int dist[], int sptSet[]) { 
            break; continue; reverse(str, 2, 9, head[0], tail[last(100)]);
        } 
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",FloatType())],IntType(),Block([Block([Block([])])])),FuncDecl(Id("min"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Break(),Continue(),CallExpr(Id("reverse"),[Id("str"),IntLiteral(2),IntLiteral(9),ArrayCell(Id("head"),IntLiteral(0)),ArrayCell(Id("tail"),CallExpr(Id("last"),[IntLiteral(100)]))])])),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_complete_program_35(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        void _BTS_(int album[], string songs[]) { 
            do 
                RM(lead) - - rap(speed == 27);
                (_Kim_SJ[WWH])[retrieved*0.1e009] + "fanchant";
                M_YG(SG,speed > 100, "go") = SG;
            while ("Concert" == on);
        } 
        float JHS, KTH, PJM, JJK;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("_BTS_"),[VarDecl("album",ArrayPointerType(IntType())),VarDecl("songs",ArrayPointerType(StringType()))],VoidType(),Block([Dowhile([BinaryOp("-",CallExpr(Id("RM"),[Id("lead")]),UnaryOp("-",CallExpr(Id("rap"),[BinaryOp("==",Id("speed"),IntLiteral(27))]))),BinaryOp("+",ArrayCell(ArrayCell(Id("_Kim_SJ"),Id("WWH")),BinaryOp("*",Id("retrieved"),FloatLiteral(100000000.0))),StringLiteral("fanchant")),BinaryOp("=",CallExpr(Id("M_YG"),[Id("SG"),BinaryOp(">",Id("speed"),IntLiteral(100)),StringLiteral("go")]),Id("SG"))],BinaryOp("==",StringLiteral("Concert"),Id("on")))])),VarDecl("JHS",FloatType()),VarDecl("KTH",FloatType()),VarDecl("PJM",FloatType()),VarDecl("JJK",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_complete_program_36(self):
        input = """
        float glob() { // /// ////////////////////// /// //
        }
        int main(string argv[], int argc) {   }
        string[] CTF(int level[], int flag[]) { 
            {}
            {}
            {}
            trap == "trap" = 09;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        //boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([FuncDecl(Id("glob"),[],FloatType(),Block([])),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("CTF"),[VarDecl("level",ArrayPointerType(IntType())),VarDecl("flag",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([Block([]),Block([]),Block([]),BinaryOp("=",BinaryOp("==",Id("trap"),StringLiteral("trap")),IntLiteral(9))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_complete_program_37(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        int main()
        {
            int n;
   
            printf("Enter an integer");
            scanf("%d", _n);
   
            if (n%2 == 0)
                printf("Even");
            else
                printf("Odd");
     
            return 0;
        }
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter an integer")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("_n")]),If(BinaryOp("==",BinaryOp("%",Id("n"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Even")]),CallExpr(Id("printf"),[StringLiteral("Odd")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_complete_program_38(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) { do do {} while(__); while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([Dowhile([Dowhile([Block([])],Id("__"))],BooleanLiteral(True))])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([If(Id("_"),Return(Id("min_index")))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_complete_program_39(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        float factorial(int n) {
            int c;
            long; result = 1;
 
            for (c = 1; c <= n; c+1)
                result = result*c;
 
            return result;
        }
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),FuncDecl(Id("factorial"),[VarDecl("n",IntType())],FloatType(),Block([VarDecl("c",IntType()),Id("long"),BinaryOp("=",Id("result"),IntLiteral(1)),For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),Id("n")),BinaryOp("+",Id("c"),IntLiteral(1)),BinaryOp("=",Id("result"),BinaryOp("*",Id("result"),Id("c")))),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_complete_program_40(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        void find_ncr_npr(int n, int r) {
            npr = find_npr(n, r);
            ncr = "me"*npr/factorial(r);
        }
 
        string[] find_npr(int n, boolean r[], float x) {
            result = 1;
            int c; c = 1;
 
            do {
                result = result * (n - r + c);
            } while (c <= r);
            return result;
        }
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType()),FuncDecl(Id("find_ncr_npr"),[VarDecl("n",IntType()),VarDecl("r",IntType())],VoidType(),Block([BinaryOp("=",Id("npr"),CallExpr(Id("find_npr"),[Id("n"),Id("r")])),BinaryOp("=",Id("ncr"),BinaryOp("/",BinaryOp("*",StringLiteral("me"),Id("npr")),CallExpr(Id("factorial"),[Id("r")])))])),FuncDecl(Id("find_npr"),[VarDecl("n",IntType()),VarDecl("r",ArrayPointerType(BoolType())),VarDecl("x",FloatType())],ArrayPointerType(StringType()),Block([BinaryOp("=",Id("result"),IntLiteral(1)),VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("result"),BinaryOp("*",Id("result"),BinaryOp("+",BinaryOp("-",Id("n"),Id("r")),Id("c"))))])],BinaryOp("<=",Id("c"),Id("r"))),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_complete_program_41(self):
        input = """
        string a,b,x;
        int main() {
            string str[100];
            int c, count[26], x;
 
            printf("Enter a string");
            gets(str);
 
            do {
            /** Considering characters from 'a' to 'z' only and ignoring others. */
 
                if (str[c] >= a && str[c] <= (z)) {
                    x = str[c] - "a";
                    inc(count[x]);
                }
            } while (str[c] != "0");
 
            for (c = 0; c < 26; c)
                printf("%c occurs %d times in the string.", c + "", count[c]);
 
            return 0;
        }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("str",ArrayType(100,StringType())),VarDecl("c",IntType()),VarDecl("count",ArrayType(26,IntType())),VarDecl("x",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a string")]),CallExpr(Id("gets"),[Id("str")]),Dowhile([Block([If(BinaryOp("&&",BinaryOp(">=",ArrayCell(Id("str"),Id("c")),Id("a")),BinaryOp("<=",ArrayCell(Id("str"),Id("c")),Id("z"))),Block([BinaryOp("=",Id("x"),BinaryOp("-",ArrayCell(Id("str"),Id("c")),StringLiteral("a"))),CallExpr(Id("inc"),[ArrayCell(Id("count"),Id("x"))])]))])],BinaryOp("!=",ArrayCell(Id("str"),Id("c")),StringLiteral("0"))),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),IntLiteral(26)),Id("c"),CallExpr(Id("printf"),[StringLiteral("%c occurs %d times in the string."),BinaryOp("+",Id("c"),StringLiteral("")),ArrayCell(Id("count"),Id("c"))])),Return(IntLiteral(0))])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_complete_program_42(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int sort(int arr[]) { 
            for (c = 1 ; c <= n - 1; c+inc[1]) {
                d = c;
 
                do 
                    t          = array[d];
                    array[d]   = array[d-1];
                    array[d-1] = t;
                while ( d > 0 && array[d-1] > array[d]);
            }
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("sort"),[VarDecl("arr",ArrayPointerType(IntType()))],IntType(),Block([For(BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("<=",Id("c"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("+",Id("c"),ArrayCell(Id("inc"),IntLiteral(1))),Block([BinaryOp("=",Id("d"),Id("c")),Dowhile([BinaryOp("=",Id("t"),ArrayCell(Id("array"),Id("d"))),BinaryOp("=",ArrayCell(Id("array"),Id("d")),ArrayCell(Id("array"),BinaryOp("-",Id("d"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("-",Id("d"),IntLiteral(1))),Id("t"))],BinaryOp("&&",BinaryOp(">",Id("d"),IntLiteral(0)),BinaryOp(">",ArrayCell(Id("array"),BinaryOp("-",Id("d"),IntLiteral(1))),ArrayCell(Id("array"),Id("d")))))]))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_complete_program_43(self):
        input = """
        void merge(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;
 
            for (i = 0; i < m + n;check(true)) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                    }
                    i+0;
                }
                else if (j == m) {
                    for (t; i < m + n;q(arr[9])) {
                        sorted[i] = b[k];
                    }
                }
                else {
                    for (t; i < m + n;foo[25]) {
                        sorted[i] = a[j];
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("merge"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("m",IntType()),VarDecl("b",ArrayPointerType(IntType())),VarDecl("n",IntType()),VarDecl("sorted",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("j"),BinaryOp("=",Id("k"),IntLiteral(0))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("+",Id("m"),Id("n"))),CallExpr(Id("check"),[BooleanLiteral(True)]),Block([If(BinaryOp("&&",BinaryOp("<",Id("j"),Id("m")),BinaryOp("<",Id("k"),Id("n"))),Block([If(BinaryOp("<",ArrayCell(Id("a"),Id("j")),ArrayCell(Id("b"),Id("k"))),Block([BinaryOp("=",ArrayCell(Id("sorted"),Id("i")),ArrayCell(Id("a"),Id("j"))),BinaryOp("+",Id("j"),IntLiteral(1))]),Block([BinaryOp("=",ArrayCell(Id("sorted"),Id("i")),ArrayCell(Id("b"),Id("k"))),BinaryOp("+",Id("k"),IntLiteral(2))])),BinaryOp("+",Id("i"),IntLiteral(0))]),If(BinaryOp("==",Id("j"),Id("m")),Block([For(Id("t"),BinaryOp("<",Id("i"),BinaryOp("+",Id("m"),Id("n"))),CallExpr(Id("q"),[ArrayCell(Id("arr"),IntLiteral(9))]),Block([BinaryOp("=",ArrayCell(Id("sorted"),Id("i")),ArrayCell(Id("b"),Id("k")))]))]),Block([For(Id("t"),BinaryOp("<",Id("i"),BinaryOp("+",Id("m"),Id("n"))),ArrayCell(Id("foo"),IntLiteral(25)),Block([BinaryOp("=",ArrayCell(Id("sorted"),Id("i")),ArrayCell(Id("a"),Id("j")))]))])))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_complete_program_44(self):
        input = """
        int main()
        {
            string a[100];
            int length;
 
            printf("Enter a string to calculate it's length");
            gets(a);
 
            length = strlen(a);
            printf("Length of the string = %d", length);
 
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(100,StringType())),VarDecl("length",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a string to calculate it's length")]),CallExpr(Id("gets"),[Id("a")]),BinaryOp("=",Id("length"),CallExpr(Id("strlen"),[Id("a")])),CallExpr(Id("printf"),[StringLiteral("Length of the string = %d"),Id("length")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_complete_program_45(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int string_length(string s[]) {
            int c; c = 0;
            do 
                c + increment[1]*a = increment;
            while (s[c] != zero);
            return c;
        }
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("string_length"),[VarDecl("s",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([BinaryOp("=",BinaryOp("+",Id("c"),BinaryOp("*",ArrayCell(Id("increment"),IntLiteral(1)),Id("a"))),Id("increment"))],BinaryOp("!=",ArrayCell(Id("s"),Id("c")),Id("zero"))),Return(Id("c"))])),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_complete_program_46(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {  
            do
            if (text[c] == _) {
                int temp; tmp = c + 1;
                if (text[temp] != zero) {
                    do {
                        if (text[temp] == "") {
                            c+1 = c;
                        }
                        temp+1;
                    } while (text[temp] == null && text[temp] != zero) ;  
                }
            }
            while (text[c] != null);
            blank[d] = text[c];
        }
        int minDistance(int dist[], int sptSet[]) { 
            return min_index;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([Dowhile([If(BinaryOp("==",ArrayCell(Id("text"),Id("c")),Id("_")),Block([VarDecl("temp",IntType()),BinaryOp("=",Id("tmp"),BinaryOp("+",Id("c"),IntLiteral(1))),If(BinaryOp("!=",ArrayCell(Id("text"),Id("temp")),Id("zero")),Block([Dowhile([Block([If(BinaryOp("==",ArrayCell(Id("text"),Id("temp")),StringLiteral("")),Block([BinaryOp("=",BinaryOp("+",Id("c"),IntLiteral(1)),Id("c"))])),BinaryOp("+",Id("temp"),IntLiteral(1))])],BinaryOp("&&",BinaryOp("==",ArrayCell(Id("text"),Id("temp")),Id("null")),BinaryOp("!=",ArrayCell(Id("text"),Id("temp")),Id("zero"))))]))]))],BinaryOp("!=",ArrayCell(Id("text"),Id("c")),Id("null"))),BinaryOp("=",ArrayCell(Id("blank"),Id("d")),ArrayCell(Id("text"),Id("c")))])),FuncDecl(Id("minDistance"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("min_index"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_complete_program_47(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        int process(int dist[], int sptSet[]) { 
            if (start == NULL)
                exit(EXIT_FAILURE);
 
            do {
                if (2*(text+c) == NULL) {
                    int temp; tmp = c + 1;
                    if (_(text+temp) != "") {
                        do {
                            if (_(text+temp) == 23) {
                                c+1;
                            }  
                            temp+1;
                        } while (2*(text+temp) == 0.0 && 2*(text+temp) != 0e0);
                    }
                }
                arr[(start+d)] = str[(text+c)]; 
            } while (2*(text+c) != "");
            (start+d)= NULL;   
            return start;
        } 
        float b, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("process"),[VarDecl("dist",ArrayPointerType(IntType())),VarDecl("sptSet",ArrayPointerType(IntType()))],IntType(),Block([If(BinaryOp("==",Id("start"),Id("NULL")),CallExpr(Id("exit"),[Id("EXIT_FAILURE")])),Dowhile([Block([If(BinaryOp("==",BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("text"),Id("c"))),Id("NULL")),Block([VarDecl("temp",IntType()),BinaryOp("=",Id("tmp"),BinaryOp("+",Id("c"),IntLiteral(1))),If(BinaryOp("!=",CallExpr(Id("_"),[BinaryOp("+",Id("text"),Id("temp"))]),StringLiteral("")),Block([Dowhile([Block([If(BinaryOp("==",CallExpr(Id("_"),[BinaryOp("+",Id("text"),Id("temp"))]),IntLiteral(23)),Block([BinaryOp("+",Id("c"),IntLiteral(1))])),BinaryOp("+",Id("temp"),IntLiteral(1))])],BinaryOp("&&",BinaryOp("==",BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("text"),Id("temp"))),FloatLiteral(0.0)),BinaryOp("!=",BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("text"),Id("temp"))),FloatLiteral(0.0))))]))])),BinaryOp("=",ArrayCell(Id("arr"),BinaryOp("+",Id("start"),Id("d"))),ArrayCell(Id("str"),BinaryOp("+",Id("text"),Id("c"))))])],BinaryOp("!=",BinaryOp("*",IntLiteral(2),BinaryOp("+",Id("text"),Id("c"))),StringLiteral(""))),BinaryOp("=",BinaryOp("+",Id("start"),Id("d")),Id("NULL")),Return(Id("start"))])),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("XXX",FloatType()),VarDecl("YYY",FloatType()),VarDecl("___",ArrayType(343434343,FloatType())),VarDecl("hcmut",FloatType()),VarDecl("edu",FloatType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_complete_program_48(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   }
        void string_insert(string s[]) {
            for (c = n - 1; c >= position - 1; c[0])
                array[c+1] = array[c];
 
            array[position-1] = value;
 
            printf("Resultant array is");
 
            for (c = 0; c <= n; c+0)
                printf("%d", array[c]);
 
        }
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([])),FuncDecl(Id("string_insert"),[VarDecl("s",ArrayPointerType(StringType()))],VoidType(),Block([For(BinaryOp("=",Id("c"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp(">=",Id("c"),BinaryOp("-",Id("position"),IntLiteral(1))),ArrayCell(Id("c"),IntLiteral(0)),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("+",Id("c"),IntLiteral(1))),ArrayCell(Id("array"),Id("c")))),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("-",Id("position"),IntLiteral(1))),Id("value")),CallExpr(Id("printf"),[StringLiteral("Resultant array is")]),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<=",Id("c"),Id("n")),BinaryOp("+",Id("c"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d"),ArrayCell(Id("array"),Id("c"))]))])),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_complete_program_49(self):
        input = """
        string a,b,x;
        int main(string argv[], int argc) {   
            for (c = 31; c >= 0; c-i)
            {
                k = n % c;
 
                if (k && 1)
                    printf("1");
                else
                    printf("0");
            }
 
            printf("Done!");
            return Null;
        }
        int string_length(string s[]) {
            int c; c = 0;
            do 
                c + increment[1]*a = increment;
            while (s[c] != zero);
            return c;
        }
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([For(BinaryOp("=",Id("c"),IntLiteral(31)),BinaryOp(">=",Id("c"),IntLiteral(0)),BinaryOp("-",Id("c"),Id("i")),Block([BinaryOp("=",Id("k"),BinaryOp("%",Id("n"),Id("c"))),If(BinaryOp("&&",Id("k"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("1")]),CallExpr(Id("printf"),[StringLiteral("0")]))])),CallExpr(Id("printf"),[StringLiteral("Done!")]),Return(Id("Null"))])),FuncDecl(Id("string_length"),[VarDecl("s",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([BinaryOp("=",BinaryOp("+",Id("c"),BinaryOp("*",ArrayCell(Id("increment"),IntLiteral(1)),Id("a"))),Id("increment"))],BinaryOp("!=",ArrayCell(Id("s"),Id("c")),Id("zero"))),Return(Id("c"))])),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_complete_program_50(self):
        input = """
        string a,b,x;
        int main() {
            int m, n, c, d, first[10], second[10], difference[10];
            printf("Enter the number of rows and columns of matrix");
            scanf("%d%d", m, n);
            printf("Enter the elements of first matrix");
 
            for (c = 0; c < m; c+foo((((x)))))
                for (d = 0 ; d < n; d[i])
                    scanf("%d", (first[c])[d]);
 
            printf("Enter the elements of second matrix");
 
            for (c = 0; c < m; i+1)
                for (d = 0; d < n; d+arr[foo(2&&true)])
                    scanf("%d", (second[c])[d]);
 
            printf("Difference of entered matrices:");
 
            for (c = 0; c < m; c+1) {
                for (d = 0; d < n; d) {
                    (difference[c])[d] = (first[c])[d] - (second[c])[d];
                    printf("%d",(difference[c])[d]);
                }
                printf("");
            }
            return 0;
        }
        int string_length(string s[]) {
            int c; c = 0;
            do 
                c + increment[1]*a = increment;
            while (s[c] != zero);
            return c;
        }
        boolean b, c, XXX, YYY, ___[343434343], hcmut, edu;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",StringType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("m",IntType()),VarDecl("n",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("first",ArrayType(10,IntType())),VarDecl("second",ArrayType(10,IntType())),VarDecl("difference",ArrayType(10,IntType())),CallExpr(Id("printf"),[StringLiteral("Enter the number of rows and columns of matrix")]),CallExpr(Id("scanf"),[StringLiteral("%d%d"),Id("m"),Id("n")]),CallExpr(Id("printf"),[StringLiteral("Enter the elements of first matrix")]),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),Id("m")),BinaryOp("+",Id("c"),CallExpr(Id("foo"),[Id("x")])),For(BinaryOp("=",Id("d"),IntLiteral(0)),BinaryOp("<",Id("d"),Id("n")),ArrayCell(Id("d"),Id("i")),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(ArrayCell(Id("first"),Id("c")),Id("d"))]))),CallExpr(Id("printf"),[StringLiteral("Enter the elements of second matrix")]),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),Id("m")),BinaryOp("+",Id("i"),IntLiteral(1)),For(BinaryOp("=",Id("d"),IntLiteral(0)),BinaryOp("<",Id("d"),Id("n")),BinaryOp("+",Id("d"),ArrayCell(Id("arr"),CallExpr(Id("foo"),[BinaryOp("&&",IntLiteral(2),BooleanLiteral(True))]))),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(ArrayCell(Id("second"),Id("c")),Id("d"))]))),CallExpr(Id("printf"),[StringLiteral("Difference of entered matrices:")]),For(BinaryOp("=",Id("c"),IntLiteral(0)),BinaryOp("<",Id("c"),Id("m")),BinaryOp("+",Id("c"),IntLiteral(1)),Block([For(BinaryOp("=",Id("d"),IntLiteral(0)),BinaryOp("<",Id("d"),Id("n")),Id("d"),Block([BinaryOp("=",ArrayCell(ArrayCell(Id("difference"),Id("c")),Id("d")),BinaryOp("-",ArrayCell(ArrayCell(Id("first"),Id("c")),Id("d")),ArrayCell(ArrayCell(Id("second"),Id("c")),Id("d")))),CallExpr(Id("printf"),[StringLiteral("%d"),ArrayCell(ArrayCell(Id("difference"),Id("c")),Id("d"))])])),CallExpr(Id("printf"),[StringLiteral("")])])),Return(IntLiteral(0))])),FuncDecl(Id("string_length"),[VarDecl("s",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),IntLiteral(0)),Dowhile([BinaryOp("=",BinaryOp("+",Id("c"),BinaryOp("*",ArrayCell(Id("increment"),IntLiteral(1)),Id("a"))),Id("increment"))],BinaryOp("!=",ArrayCell(Id("s"),Id("c")),Id("zero"))),Return(Id("c"))])),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("___",ArrayType(343434343,BoolType())),VarDecl("hcmut",BoolType()),VarDecl("edu",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_complete_program_51(self):
        input = """
        string PPL[100];
        int test(int num, string question[]) {
            start(time);
            begin_test = time_out - time_lapse(t)[i] + 100 - arr[2]*90E-0;
            for (i = 0; i < max_ques; skipquest)
            {
                {
                    reveal_question;
                    if(easy) finish = "quick!" % "save time";
                    else do skip; while(!easy);
                }
            }
        }
        """
        expect = str(Program([VarDecl("PPL",ArrayType(100,StringType())),FuncDecl(Id("test"),[VarDecl("num",IntType()),VarDecl("question",ArrayPointerType(StringType()))],IntType(),Block([CallExpr(Id("start"),[Id("time")]),BinaryOp("=",Id("begin_test"),BinaryOp("-",BinaryOp("+",BinaryOp("-",Id("time_out"),ArrayCell(CallExpr(Id("time_lapse"),[Id("t")]),Id("i"))),IntLiteral(100)),BinaryOp("*",ArrayCell(Id("arr"),IntLiteral(2)),FloatLiteral(90.0)))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("max_ques")),Id("skipquest"),Block([Block([Id("reveal_question"),If(Id("easy"),BinaryOp("=",Id("finish"),BinaryOp("%",StringLiteral("quick!"),StringLiteral("save time"))),Dowhile([Id("skip")],UnaryOp("!",Id("easy"))))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_complete_program_52(self):
        input = """
        //////////////// Comment ////////////////////////
        int num; float mark[10];
        void checkAns(boolean correct[], string test) {
            int i;
            for(i = 0; i< len(test[i]) - num; mark[i]) {
                if(isTrue(quest[i])) { 
                    correct[i] == true || 100;
                    do 
                        { "Mark the test";}
                    while (true);
                }
                else
                    continue;
            }
            return mark;
        }
        int result, head[5]; string compliments[100];
        """
        expect = str(Program([VarDecl("num",IntType()),VarDecl("mark",ArrayType(10,FloatType())),FuncDecl(Id("checkAns"),[VarDecl("correct",ArrayPointerType(BoolType())),VarDecl("test",StringType())],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",CallExpr(Id("len"),[ArrayCell(Id("test"),Id("i"))]),Id("num"))),ArrayCell(Id("mark"),Id("i")),Block([If(CallExpr(Id("isTrue"),[ArrayCell(Id("quest"),Id("i"))]),Block([BinaryOp("||",BinaryOp("==",ArrayCell(Id("correct"),Id("i")),BooleanLiteral(True)),IntLiteral(100)),Dowhile([Block([StringLiteral("Mark the test")])],BooleanLiteral(True))]),Continue())])),Return(Id("mark"))])),VarDecl("result",IntType()),VarDecl("head",ArrayType(5,IntType())),VarDecl("compliments",ArrayType(100,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_complete_program_53(self):
        input = """
        string Exp, Mana; 
        int Array[10], PPL_test[100];
        int main(string argv[], int argc) { 
            PPL(Lessons, Action("Study"), Mark[10]) <= "Loading...";
            if (Accomplish)
                return "Done"*0;
        }
        string[] PPL(string s[]) {
            do 
                exp + increment[1]*mana = "Go go go!!!";
            while (Day[i] == Passed * Learned);
            return Compliment;
        }
        boolean HCMUT, CSE[2], VNU;
        string FourIV;
        float _01,Finish,_;
        """
        expect = str(Program([VarDecl("Exp",StringType()),VarDecl("Mana",StringType()),VarDecl("Array",ArrayType(10,IntType())),VarDecl("PPL_test",ArrayType(100,IntType())),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(StringType())),VarDecl("argc",IntType())],IntType(),Block([BinaryOp("<=",CallExpr(Id("PPL"),[Id("Lessons"),CallExpr(Id("Action"),[StringLiteral("Study")]),ArrayCell(Id("Mark"),IntLiteral(10))]),StringLiteral("Loading...")),If(Id("Accomplish"),Return(BinaryOp("*",StringLiteral("Done"),IntLiteral(0))))])),FuncDecl(Id("PPL"),[VarDecl("s",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([Dowhile([BinaryOp("=",BinaryOp("+",Id("exp"),BinaryOp("*",ArrayCell(Id("increment"),IntLiteral(1)),Id("mana"))),StringLiteral("Go go go!!!"))],BinaryOp("==",ArrayCell(Id("Day"),Id("i")),BinaryOp("*",Id("Passed"),Id("Learned")))),Return(Id("Compliment"))])),VarDecl("HCMUT",BoolType()),VarDecl("CSE",ArrayType(2,BoolType())),VarDecl("VNU",BoolType()),VarDecl("FourIV",StringType()),VarDecl("_01",FloatType()),VarDecl("Finish",FloatType()),VarDecl("_",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

   