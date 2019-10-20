import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    #Test variable declarate : 5 tests case
    def test_variable_declarate_1(self): #Simple variable declarate type 1
        input = """
                int x;
                float y;
                string z;
                boolean m;
        """
        expect = str(
            Program([
                VarDecl("x", IntType()   ),
                VarDecl("y", FloatType() ),
                VarDecl("z", StringType()),
                VarDecl("m", BoolType()  )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_variable_declarate_2(self): #Simple variable declarate type 2
        input = """
                int x,y,z;
                float x,y,z;
                string x,y,z;
                boolean x,y,z;
        """
        expect = str(
            Program([
                VarDecl("x", IntType()   ),
                VarDecl("y", IntType()   ),
                VarDecl("z", IntType()   ),
                VarDecl("x", FloatType() ),
                VarDecl("y", FloatType() ),
                VarDecl("z", FloatType() ),
                VarDecl("x", StringType()),
                VarDecl("y", StringType()),
                VarDecl("z", StringType()),
                VarDecl("x", BoolType()  ),
                VarDecl("y", BoolType()  ),
                VarDecl("z", BoolType()  )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_variable_declarate_3(self): #Simple variable declarate type 2
        input = """
                int x[10];
                float x[10];
                string x[10];
                boolean x[10];
        """
        expect = str(
            Program([
                VarDecl("x", ArrayType(10,IntType()   )),
                VarDecl("x", ArrayType(10,FloatType() )),
                VarDecl("x", ArrayType(10,StringType())),
                VarDecl("x", ArrayType(10,BoolType()  ))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_variable_declarate_4(self):#A complex variable declarate
        input = """
            int x,y[10],_z5;
            float y,m[11];
            string t[100],m,_k_;
            boolean not_true;
        """
        expect = str(
            Program([
                VarDecl("x",        IntType()                  ),
                VarDecl("y",        ArrayType(10,IntType())    ),
                VarDecl("_z5",      IntType()                  ),
                VarDecl("y",        FloatType()                ),
                VarDecl("m",        ArrayType(11, FloatType() )),
                VarDecl("t",        ArrayType(100,StringType())),
                VarDecl("m",        StringType()               ),
                VarDecl("_k_",      StringType()               ),
                VarDecl("not_true", BoolType()                 )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_variable_declarate_5(self):#Sixteen times variable declarate
        input = """
            int x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x; 
        """
        expect = str(
            Program([
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType()),
                VarDecl("x", IntType())
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    #Test function declarate : 5 tests case
    def test_function_declarate_1(self): #A simple function declarate
        input = """
            void main(){ /* Nothing here */}
            int main(){
                // Your code here
            }
            string main(){
                // This is just a test
                // Test the code 
            }
            boolean main(){}
        """
        expect = str(
            Program([
                FuncDecl(Id("main"), [], VoidType()   , Block([])),
                FuncDecl(Id("main"), [], IntType()    , Block([])),
                FuncDecl(Id("main"), [], StringType() , Block([])),
                FuncDecl(Id("main"), [], BoolType()   , Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_function_declarate_2(self): #Function declarate as array
        input = """
            int[] test_1(){}
            float[] test_2(){}
            string[] test_3(){}
            boolean[] test_4(){}
        """
        expect = str(
            Program([
                FuncDecl(Id("test_1") , [] , ArrayPointerType( IntType()    ) , Block([])),
                FuncDecl(Id("test_2") , [] , ArrayPointerType( FloatType()  ) , Block([])),
                FuncDecl(Id("test_3") , [] , ArrayPointerType( StringType() ) , Block([])),
                FuncDecl(Id("test_4") , [] , ArrayPointerType( BoolType()   ) , Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_function_declarate_3(self): #Function declarate with parameter
        input = """
            void what_the_test(int x, string y){}
            string _test_the_code_by_a_code(boolean y){}
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("what_the_test"),
                    [
                        VarDecl("x", IntType()   ),
                        VarDecl("y", StringType())
                    ],
                    VoidType(),
                    Block([])
                ),
                FuncDecl(
                    Id("_test_the_code_by_a_code"),
                    [
                        VarDecl("y", BoolType())
                    ],
                    StringType(),
                    Block([])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_function_declarate_4(self):#Function declarate with array parameter
        input = """
            int trichomobas_hominis(int a_varaiable[]){ /* Nothing to do */}
        """
        expect  = str(
            Program([
                FuncDecl(
                    Id("trichomobas_hominis"),
                    [
                        VarDecl("a_varaiable", ArrayPointerType(IntType()))
                    ],
                    IntType(),
                    Block([])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_function_declarate_5(self): #Mix the parameter
        input = """
            int main(int x, float y, string z, boolean m, int t[], float k[], string h[], boolean i[]){}
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),
                    [
                        VarDecl("x", IntType()                     ),
                        VarDecl("y", FloatType()                   ),
                        VarDecl("z", StringType()                  ),
                        VarDecl("m", BoolType()                    ),
                        VarDecl("t", ArrayPointerType(IntType())   ),
                        VarDecl("k", ArrayPointerType(FloatType()) ),
                        VarDecl("h", ArrayPointerType(StringType())),
                        VarDecl("i", ArrayPointerType(BoolType())  )
                    ],
                    IntType(),
                    Block([
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    #Test operands : 5 tests case
    def test_operands_1(self):
        input = """
            void main(){
                the_id;
                id;
                _std21_;
                _sddas_[3];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Id("the_id"),Id("id"),Id("_std21_"),ArrayCell(Id("_sddas_"),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_operands_2(self):
        input = """
            void main(){
                1;
                2;
                3;
                4;
                5;
                6;
                7;
                8;
                9;
                10;
                11;
                12345567890;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10),IntLiteral(11),IntLiteral(12345567890)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_operands_3(self):
        input = """
            void main(){
                1.23445;
                1.3e2;
                1.45e-100;
                .456;
                .456e3;
                1e3;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([FloatLiteral(1.23445),FloatLiteral(130.0),FloatLiteral(1.45e-100),FloatLiteral(0.456),FloatLiteral(456.0),FloatLiteral(1000.0)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_operands_4(self):
        input = """
            void main(){
                "^ What are words";
                "@ Anywhere you are, I am near";
                "# Anywhere you go, Ill be there";
                "$ Anytime you whisper my name, youll see";
                "% How every single promise Ill keep";
                "^ Cause what kind of guy would I be";
                "& If I was to leave when you need me most";
                true;
                false;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([StringLiteral("^ What are words"),StringLiteral("@ Anywhere you are, I am near"),StringLiteral("# Anywhere you go, Ill be there),StringLiteral($ Anytime you whisper my name, youll see"),StringLiteral("% How every single promise Ill keep"),StringLiteral("^ Cause what kind of guy would I be"),StringLiteral("& If I was to leave when you need me most"),BooleanLiteral(True),BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_operands_5(self):
        input = """
            void main(){
                foo("x","y",a[3],test);
                _test_not_a_test(1,3e3);   
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[StringLiteral("x"),StringLiteral("y"),ArrayCell(Id("a"),IntLiteral(3)),Id("test")]),CallExpr(Id("_test_not_a_test"),[IntLiteral(1),FloatLiteral(3000.0)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    #Test expression : 15 tests case
    def test_expression_1(self):#Test all experssion
        input = """
            void main(){
                a == b;
                a != b;
                a && b;
                a || b;
                a =  b;
                a >= b;
                a <= b;
                a >  b;
                a <  b;
                a[b];
                -a;
                !b;
                a *  b;
                a /  b;
                a %  b;
                a +  b;
                a -  b;
                foo(a,b,c);
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),[],VoidType(),
                    Block([
                        BinaryOp( "==", Id("a"), Id("b")),
                        BinaryOp( "!=", Id("a"), Id("b")),
                        BinaryOp( "&&", Id("a"), Id("b")),
                        BinaryOp( "||", Id("a"), Id("b")),
                        BinaryOp( "=" , Id("a"), Id("b")),
                        BinaryOp( ">=", Id("a"), Id("b")),
                        BinaryOp( "<=", Id("a"), Id("b")),
                        BinaryOp( ">" , Id("a"), Id("b")),
                        BinaryOp( "<" , Id("a"), Id("b")),
                        ArrayCell(      Id("a"), Id("b")),
                        UnaryOp(  "-" , Id("a")         ),
                        UnaryOp(  "!" , Id("b")         ),
                        BinaryOp( "*" , Id("a"), Id("b")),
                        BinaryOp( "/" , Id("a"), Id("b")),
                        BinaryOp( "%" , Id("a"), Id("b")),
                        BinaryOp( "+" , Id("a"), Id("b")),
                        BinaryOp( "-" , Id("a"), Id("b")),
                        CallExpr(Id("foo"),[Id("a"),Id("b"),Id("c")])
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_expression_2(self):#Test association of "=" expression
        input = """
            void main(){
                a = b = c = d;
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),[],VoidType(),
                    Block([
                        BinaryOp(
                            "=",
                            Id("a"),
                            BinaryOp(
                                "=",
                                Id("b"),
                                BinaryOp(
                                    "=",
                                    Id("c"),
                                    Id("d")
                                )
                            )
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_expression_3(self):#Test association of "||" and "&&" expression
        input = """
            void main(){
                a || b || c;
                a && b && c;
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),[],VoidType(),
                    Block([
                        BinaryOp(
                            "||",
                            BinaryOp(
                                "||",
                                Id("a"),
                                Id("b")
                            ),
                            Id("c")
                        ),
                        BinaryOp(
                            "&&",
                            BinaryOp(
                                "&&",
                                Id("a"),
                                Id("b")
                            ),
                            Id("c")
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_expression_4(self):#"==" and "!=" non-association
        input = """
            void main(){
                a == b > c;
                a != b < c;
            }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("==",Id("a"),BinaryOp(">",Id("b"),Id("c"))),BinaryOp("!=",Id("a"),BinaryOp("<",Id("b"),Id("c")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_expression_5(self):#Test preccedene of "==","!=","&&","||","=" expression
        input = """
            void main(){
                a = b && c || d == e;
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),[],VoidType(),
                    Block([
                        BinaryOp(
                            "=",
                            Id("a"),
                            BinaryOp(
                                "||",
                                BinaryOp(
                                    "&&",
                                    Id("b"),
                                    Id("c")
                                ),
                                BinaryOp(
                                    "==",
                                    Id("d"),
                                    Id("e")
                                )
                            )
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_expression_6(self): #Test array cell
        input = """
            void main(){
                a[b + c - d[ 7 * 2 ] - e[4]] = 1;
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),[],VoidType(),
                    Block([
                        BinaryOp(
                            "=",
                            ArrayCell(
                                Id("a"),
                                BinaryOp(
                                    "-",
                                    BinaryOp(
                                        "-",
                                        BinaryOp(
                                            "+",
                                            Id("b"),
                                            Id("c")
                                        ),
                                        ArrayCell(
                                            Id("d"),
                                            BinaryOp(
                                                "*",
                                                IntLiteral(7),
                                                IntLiteral(2)
                                            )
                                        )
                                    ),
                                    ArrayCell(
                                        Id("e"),
                                        IntLiteral(4)
                                    )
                                )
                            ),
                            IntLiteral(1)
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_expression_7(self):
        input = """
            void main(){
                -------!!!!!!a;
            }
        """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"), [], VoidType(),
                    Block([
                        UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a"))))))))))))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_expression_8(self):
        input = """
            void main(){
                a + b + c + d;
                a - b - c - d;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("d")),BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("a"),Id("b")),Id("c")),Id("d"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_expression_9(self):
        input = """
            void main(){
                a * b * c;
                a / b / c;
                a % b % c;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),BinaryOp("/",BinaryOp("/",Id("a"),Id("b")),Id("c")),BinaryOp("%",BinaryOp("%",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_expression_10(self):
        input = """
            void main(){
                a * (b - c) / (d + e);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",BinaryOp("*",Id("a"),BinaryOp("-",Id("b"),Id("c"))),BinaryOp("+",Id("d"),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_expression_11(self):
        input = """
            void main(){
                print(foo(foo(a)));
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("a")])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_expression_12(self):
        input = """
            void main(){
                print(a = b + c * foo(a/d) % a[1000],"Test" + str(isEqual(1000,100) == true));
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),BinaryOp("%",BinaryOp("*",Id("c"),CallExpr(Id("foo"),[BinaryOp("/",Id("a"),Id("d"))])),ArrayCell(Id("a"),IntLiteral(1000))))),BinaryOp("+",StringLiteral("Test"),CallExpr(Id("str"),[BinaryOp("==",CallExpr(Id("isEqual"),[IntLiteral(1000),IntLiteral(100)]),BooleanLiteral(True))]))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_expression_13(self):
        input = """
            void main(){
                a = (((((((((((((((((((((((((((((((((((((((((((((a/3)))))))))))))))))))))))))))))))))))))))))))));
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_expression_14(self):
        input = """
            void main(){
                a = (b > c[3]) * (d - e[(10 - 5) * 4]);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("*",BinaryOp(">",Id("b"),ArrayCell(Id("c"),IntLiteral(3))),BinaryOp("-",Id("d"),ArrayCell(Id("e"),BinaryOp("*",BinaryOp("-",IntLiteral(10),IntLiteral(5)),IntLiteral(4))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_expression_15(self):
        input = """
            void main(){
                foo(a = b - c % foo(a[10 + (5 - 3) / 4])) - foo(_a + true * -1.2e-3 + 5.7e9 - 9.10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",CallExpr(Id("foo"),[BinaryOp("=",Id("a"),BinaryOp("-",Id("b"),BinaryOp("%",Id("c"),CallExpr(Id("foo"),[ArrayCell(Id("a"),BinaryOp("+",IntLiteral(10),BinaryOp("/",BinaryOp("-",IntLiteral(5),IntLiteral(3)),IntLiteral(4))))]))))]),CallExpr(Id("foo"),[BinaryOp("-",BinaryOp("+",BinaryOp("+",Id("_a"),BinaryOp("*",BooleanLiteral(True),UnaryOp("-",FloatLiteral(0.0012)))),FloatLiteral(5700000000.0)),FloatLiteral(9.1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    #Test if statement : 10 tests case
    def test_if_statement_1(self):
        input = """
            void main(){
                int b;
                b = 0;
                if (5 == 6)
                    b = b -3;
                else 
                    b = b /5;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),IntLiteral(0)),If(BinaryOp("==",IntLiteral(5),IntLiteral(6)),BinaryOp("=",Id("b"),BinaryOp("-",Id("b"),IntLiteral(3))),BinaryOp("=",Id("b"),BinaryOp("/",Id("b"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_if_statement_2(self):
        input = """
            void main(){
                int x;
                x = 3;
                if (x < 5){
                    x = x -10;
                    foo(x);
                } else {
                    x = x * 1.3e-3;
                    foo(x);
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(3)),If(BinaryOp("<",Id("x"),IntLiteral(5)),Block([BinaryOp("=",Id("x"),BinaryOp("-",Id("x"),IntLiteral(10))),CallExpr(Id("foo"),[Id("x")])]),Block([BinaryOp("=",Id("x"),BinaryOp("*",Id("x"),FloatLiteral(0.0013))),CallExpr(Id("foo"),[Id("x")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_if_statement_3(self):
        input = """
            void main(){
                if (6 < 7)
                    if ( 8 < 9)
                        print("True");
                    else
                        print("False");
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("<",IntLiteral(6),IntLiteral(7)),If(BinaryOp("<",IntLiteral(8),IntLiteral(9)),CallExpr(Id("print"),[StringLiteral("True")]),CallExpr(Id("print"),[StringLiteral("False")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_if_statement_4(self):
        input = """
            void main(){
                if (6<7){
                    if (8 < 9)
                        print("True");
                } else 
                    print("False");
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("<",IntLiteral(6),IntLiteral(7)),Block([If(BinaryOp("<",IntLiteral(8),IntLiteral(9)),CallExpr(Id("print"),[StringLiteral("True")]))]),CallExpr(Id("print"),[StringLiteral("False")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_if_statement_5(self):
        input = """
            void main(){
                if ((a == b - d + c) && (4 < d - e)){
                    int x,y;
                    x = y + foo(x,y);
                    if (x = a){
                        e = f;
                    } else {
                        print(10);
                        a && b - f;
                    }
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",BinaryOp("==",Id("a"),BinaryOp("+",BinaryOp("-",Id("b"),Id("d")),Id("c"))),BinaryOp("<",IntLiteral(4),BinaryOp("-",Id("d"),Id("e")))),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),BinaryOp("=",Id("x"),BinaryOp("+",Id("y"),CallExpr(Id("foo"),[Id("x"),Id("y")]))),If(BinaryOp("=",Id("x"),Id("a")),Block([BinaryOp("=",Id("e"),Id("f"))]),Block([CallExpr(Id("print"),[IntLiteral(10)]),BinaryOp("&&",Id("a"),BinaryOp("-",Id("b"),Id("f")))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_if_statement_6(self):
        input = """
            void main(){
                if ( a != b ){
                    if( 3.E5 )
                        a = b + true ;
                } else 
                    j || -7;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([If(FloatLiteral(300000.0),BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),BooleanLiteral(True))))]),BinaryOp("||",Id("j"),UnaryOp("-",IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_if_statement_7(self):
        input = """
            void main(){
                if ( a != b )
                    if( 3.E5 )
                        a = b + true ;
                    else 
                        j = 7;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("!=",Id("a"),Id("b")),If(FloatLiteral(300000.0),BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),BooleanLiteral(True))),BinaryOp("=",Id("j"),IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_if_statement_8(self):
        input = """
            void main(){
                if ( a != b )
                    a && 9 = 6;
                else 
                    if (a = 5)
                        a >= 7;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("!=",Id("a"),Id("b")),BinaryOp("=",BinaryOp("&&",Id("a"),IntLiteral(9)),IntLiteral(6)),If(BinaryOp("=",Id("a"),IntLiteral(5)),BinaryOp(">=",Id("a"),IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_if_statement_9(self):
        input = """
            void main(){
                if ( a != b ){
                    a && 9 = 6;
                } else { 
                    math_score = math_score + 1;
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([BinaryOp("=",BinaryOp("&&",Id("a"),IntLiteral(9)),IntLiteral(6))]),Block([BinaryOp("=",Id("math_score"),BinaryOp("+",Id("math_score"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_if_statement_10(self):
        input = """
            void main(){
                if ( a != b ){
                    a && 9 = 6;
                } else {}
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([BinaryOp("=",BinaryOp("&&",Id("a"),IntLiteral(9)),IntLiteral(6))]),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    #Test for statement : 10 tests case
    def test_for_statement_1(self):
        input = """
            void main(){
                for (x = 0; x < 10; x = x + 1) 
                    print(x);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("x"),IntLiteral(0)),BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallExpr(Id("print"),[Id("x")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_for_statement_2(self):
        input = """
            void main(){
                for (x < 100; x >= x + 1; x = x * foo(x)[100]){
                    int x;
                    print(x);
                    if (x == 10){
                        x = x + 1;
                    }
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp(">=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),BinaryOp("=",Id("x"),BinaryOp("*",Id("x"),ArrayCell(CallExpr(Id("foo"),[Id("x")]),IntLiteral(100)))),Block([VarDecl("x",IntType()),CallExpr(Id("print"),[Id("x")]),If(BinaryOp("==",Id("x"),IntLiteral(10)),Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_for_statement_3(self):
        input = """
            void main(){
                if (x < 10){
                    for (x = false;True;x = foo(3)){
                        x = x + 1;
                    }
                } else {
                    for (x;y;z){
                        foo(x,y,z,t);
                    }
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([For(BinaryOp("=",Id("x"),BooleanLiteral(False)),Id("True"),BinaryOp("=",Id("x"),CallExpr(Id("foo"),[IntLiteral(3)])),Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]),Block([For(Id("x"),Id("y"),Id("z"),Block([CallExpr(Id("foo"),[Id("x"),Id("y"),Id("z"),Id("t")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_for_statement_4(self):
        input = """
            void main(){
                for (x;y;z)               
                    for (x;y;z)           
                        for (x;y;z)       
                            for (x;y;z)   
                                foo(x,y,z);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("x"),Id("y"),Id("z"),For(Id("x"),Id("y"),Id("z"),For(Id("x"),Id("y"),Id("z"),For(Id("x"),Id("y"),Id("z"),CallExpr(Id("foo"),[Id("x"),Id("y"),Id("z")])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_for_statement_5(self):
        input = """
            void main(){
                if (x == 10){
                    for (x = 10; x < 100; x = x + 1)
                        if (x % 3 == 0)
                            print(x);
                        else 
                            if (x % 5 == 0)
                                print(x - 10);
                    for (y = x; y < 2 * x; y = y + 3){
                        int z;
                        z = 1;
                        for (i = 1; i < y; i = i + 1){
                            z = z * i;
                        }
                        print(z);
                    }
                }
            }       
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("x"),IntLiteral(10)),Block([For(BinaryOp("=",Id("x"),IntLiteral(10)),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),If(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(3)),IntLiteral(0)),CallExpr(Id("print"),[Id("x")]),If(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(5)),IntLiteral(0)),CallExpr(Id("print"),[BinaryOp("-",Id("x"),IntLiteral(10))])))),For(BinaryOp("=",Id("y"),Id("x")),BinaryOp("<",Id("y"),BinaryOp("*",IntLiteral(2),Id("x"))),BinaryOp("=",Id("y"),BinaryOp("+",Id("y"),IntLiteral(3))),Block([VarDecl("z",IntType()),BinaryOp("=",Id("z"),IntLiteral(1)),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),Id("y")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("z"),BinaryOp("*",Id("z"),Id("i")))])),CallExpr(Id("print"),[Id("z")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_for_statement_6(self):
        input = """
            int main(){
                for ( i = 0; i < alpha; i = i + 1){
                    // This is just a comment 
                    /* Don't have code here
                    */ 
                }
                for ( i; j; k) {}
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("alpha")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])),For(Id("i"),Id("j"),Id("k"),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_for_statement_7(self):
        input = """
            string main(){
                for ( i = 0; i < 3E5; i = i + 1) 
                    if (a == 10) 
                        a = a + 5;
                    else {
                        a = a -5;
                    }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],StringType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FloatLiteral(300000.0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(5)))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_for_statement_8(self):
        input = """
            float main(){
                for ( i = 0; i < 3E5; i = i + 1){
                    do {} {} {} {a == 10;} while a == 10;
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FloatLiteral(300000.0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Dowhile([Block([]),Block([]),Block([]),Block([BinaryOp("==",Id("a"),IntLiteral(10))])],BinaryOp("==",Id("a"),IntLiteral(10)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_for_statement_9(self):
        input = """
            float main(){
                for ( i = 0; i < 3E5; i = i + 1){
                    for (i = 100 + a < 10; i > 6; i = i / 2 *3){
                        for (i > 3; i = 10; i + 3 = 3)
                            //Do nothing here
                            a = 10;
                    }
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FloatLiteral(300000.0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("i"),BinaryOp("<",BinaryOp("+",IntLiteral(100),Id("a")),IntLiteral(10))),BinaryOp(">",Id("i"),IntLiteral(6)),BinaryOp("=",Id("i"),BinaryOp("*",BinaryOp("/",Id("i"),IntLiteral(2)),IntLiteral(3))),Block([For(BinaryOp(">",Id("i"),IntLiteral(3)),BinaryOp("=",Id("i"),IntLiteral(10)),BinaryOp("=",BinaryOp("+",Id("i"),IntLiteral(3)),IntLiteral(3)),BinaryOp("=",Id("a"),IntLiteral(10)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_for_statement_10(self):
        input = """
            string main(){
                for ( i = 0; i < 3E5; i = i + 1){
                    {}
                    {{}}
                    {{{}}}
                    {{{{}}}}
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],StringType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FloatLiteral(300000.0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Block([]),Block([Block([])]),Block([Block([Block([])])]),Block([Block([Block([Block([])])])])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    #Test do while statement : 10 tests case
    def test_do_while_statement_1(self):
        input = """
            void main(){
                do
                    x = x + 3;
                    x = x - 10;
                while (x < 3);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("=",Id("x"),BinaryOp("-",Id("x"),IntLiteral(10)))],BinaryOp("<",Id("x"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_do_while_statement_2(self):
        input = """
            void main(){
                do
                    {
                        x = x + 3;
                    }
                    {
                        x = x - 10;
                    }
                while (x < 3);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))]),Block([BinaryOp("=",Id("x"),BinaryOp("-",Id("x"),IntLiteral(10)))])],BinaryOp("<",Id("x"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_do_while_statement_3(self):
        input = """
            void main(){
                do 
                    {
                        x = x + 3;
                    }
                    x = x - 10;
                while (x < 3);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))]),BinaryOp("=",Id("x"),BinaryOp("-",Id("x"),IntLiteral(10)))],BinaryOp("<",Id("x"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_do_while_statement_4(self):
        input = """
            void main(){
                do
                    if ( x = 4)
                        do 
                            x = 5;
                        while (x < 10);
                    for (x;x;x)
                        do 
                            x = 5;
                        while (x < 10);
                while (x < 10); 
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([If(BinaryOp("=",Id("x"),IntLiteral(4)),Dowhile([BinaryOp("=",Id("x"),IntLiteral(5))],BinaryOp("<",Id("x"),IntLiteral(10)))),For(Id("x"),Id("x"),Id("x"),Dowhile([BinaryOp("=",Id("x"),IntLiteral(5))],BinaryOp("<",Id("x"),IntLiteral(10))))],BinaryOp("<",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_do_while_statement_5(self):
        input = """
            void main(){
                do 
                    do 
                        do 
                            do 
                                x = x + 1;
                            while (x < 3);
                        while (x < 5);
                    while (x < 7);
                while (x < 9);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))],BinaryOp("<",Id("x"),IntLiteral(3)))],BinaryOp("<",Id("x"),IntLiteral(5)))],BinaryOp("<",Id("x"),IntLiteral(7)))],BinaryOp("<",Id("x"),IntLiteral(9)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_do_while_statement_6(self):
        input = """
            void main(){
                int a, c[10];
                int i;
                i = 1;
                a = c[0];
                if (c[1] > a)
                    do 
                        a = a + 5;
                        { int z;}
                        //This is a test
                    while (a == 10) && (b + c >= d);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("a"),ArrayCell(Id("c"),IntLiteral(0))),If(BinaryOp(">",ArrayCell(Id("c"),IntLiteral(1)),Id("a")),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),Block([VarDecl("z",IntType())])],BinaryOp("&&",BinaryOp("==",Id("a"),IntLiteral(10)),BinaryOp(">=",BinaryOp("+",Id("b"),Id("c")),Id("d")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_do_while_statement_7(self):
        input = """
            void main(){
                int a, c[10];
                int i;
                i = 1;
                a = c[0];
                if (c[1] > a)
                    do 
                        a = a + 5;
                        { int z;}
                        //This is a test
                    while a == 10;
                else {
                    do 
                        {game = 10;}
                        {game = true;}
                    while a != 5;
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("a"),ArrayCell(Id("c"),IntLiteral(0))),If(BinaryOp(">",ArrayCell(Id("c"),IntLiteral(1)),Id("a")),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),Block([VarDecl("z",IntType())])],BinaryOp("==",Id("a"),IntLiteral(10))),Block([Dowhile([Block([BinaryOp("=",Id("game"),IntLiteral(10))]),Block([BinaryOp("=",Id("game"),BooleanLiteral(True))])],BinaryOp("!=",Id("a"),IntLiteral(5)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_do_while_statement_8(self):
        input = """
            void main(){
                int a, c[10];
                int i;
                i = 1;
                a = c[0];
                do 
                    if (a < c[i]) {
                        int b;
                        b = a;
                        a = c[i];
                        c[i] = b;
                    }
                    i = i + 1;
                while i < 10;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("a"),ArrayCell(Id("c"),IntLiteral(0))),Dowhile([If(BinaryOp("<",Id("a"),ArrayCell(Id("c"),Id("i"))),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),Id("a")),BinaryOp("=",Id("a"),ArrayCell(Id("c"),Id("i"))),BinaryOp("=",ArrayCell(Id("c"),Id("i")),Id("b"))])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_do_while_statement_9(self):
        input = """
            void main(){
                do 
                    if (a == b) {
                        //Not a test case 
                    } else {
                        //Just a block
                    } 
                while a != b ;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([If(BinaryOp("==",Id("a"),Id("b")),Block([]),Block([]))],BinaryOp("!=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_do_while_statement_10(self):
        input = """
            void main(){
                do 
                    {}
                    {{}}
                    {{{}}}
                    {{{{}}}}
                while (1);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([]),Block([Block([])]),Block([Block([Block([])])]),Block([Block([Block([Block([])])])])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    #Test break statement : 7 tests case
    def test_break_statement_1(self):
        input = """
            void main(){
                break;
                break;
                break;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break(),Break(),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_break_statement_2(self):
        input = """
            void main(){
                if (a == 5) break;
                else break;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(5)),Break(),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_break_statement_3(self):
        input = """
            void main(){
                for (x;y;z) break;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("x"),Id("y"),Id("z"),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_break_statement_4(self):
        input = """
            void main(){
                do
                    break;
                    break;
                while (x = 10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Break(),Break()],BinaryOp("=",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_break_statement_5(self):
        input = """                                                                                                                                                                                                                                                                                                                                                                      
            void main(){                                                                                                                                                                                                                                                                                                                                                                 
                do                                                                                                                                                                                                                                                                                                                                                                       
                    x = -2e-3;                                                                                                                                                                                                                                                                                                                                                           
                    do                                                                                                                                                                                                                                                                                                                                                                   
                        if (x < 9.9) break;                                                                                                                                                                                                                                                                                                                                              
                        else x = x + 0.1;                                                                                                                                                                                                                                                                                                                                                
                    while ( x < 10);                                                                                                                                                                                                                                                                                                                                                     
                while !( x != - false);                                                                                                                                                                                                                                                                                                                                                  
            }                                                                                                                                                                                                                                                                                                                                                                            
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("x"),UnaryOp("-",FloatLiteral(0.002))),Dowhile([If(BinaryOp("<",Id("x"),FloatLiteral(9.9)),Break(),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),FloatLiteral(0.1))))],BinaryOp("<",Id("x"),IntLiteral(10)))],UnaryOp("!",BinaryOp("!=",Id("x"),UnaryOp("-",BooleanLiteral(False)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_break_statement_6(self):
        input = """
            float foo(){
                do {
                    if (a % 3 == 0) break;
                    a = a + 1;
                } while (a < 100);
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Dowhile([Block([If(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(3)),IntLiteral(0)),Break()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("<",Id("a"),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_break_statement_7(self):
        input = """
            float foo(){
                 break;
                 if (a == 10){
                    break;
                    break;
                 }
                 break;
                 //break
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Break(),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Break(),Break()])),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    #Test continue statement : 8 tests case
    def test_continue_statement_1(self):
        input = """
            void main(){
                continue;
                continue;
                continue;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Continue(),Continue(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_continue_statement_2(self):
        input = """
            void main(){
                if (a == 5) continue;
                else continue;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(5)),Continue(),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_continue_statement_3(self):
        input = """
            void main(){
                for (x;y;z) continue;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("x"),Id("y"),Id("z"),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_continue_statement_4(self):
        input = """
            void main(){
                do
                    continue;
                    continue;
                while (x = 10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Continue(),Continue()],BinaryOp("=",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_continue_statement_5(self):
        input = """                                                                                                                                                                                                                                                                                                                                                                      
            void main(){                                                                                                                                                                                                                                                                                                                                                                 
                do                                                                                                                                                                                                                                                                                                                                                                       
                    x = -2e-3;                                                                                                                                                                                                                                                                                                                                                           
                    do                                                                                                                                                                                                                                                                                                                                                                   
                        if (x < 9.9) continue;                                                                                                                                                                                                                                                                                                                                              
                        else x = x + 0.1;                                                                                                                                                                                                                                                                                                                                                
                    while ( x < 10);                                                                                                                                                                                                                                                                                                                                                     
                while !( x != - false);                                                                                                                                                                                                                                                                                                                                                  
            }                                                                                                                                                                                                                                                                                                                                                                            
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("x"),UnaryOp("-",FloatLiteral(0.002))),Dowhile([If(BinaryOp("<",Id("x"),FloatLiteral(9.9)),Continue(),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),FloatLiteral(0.1))))],BinaryOp("<",Id("x"),IntLiteral(10)))],UnaryOp("!",BinaryOp("!=",Id("x"),UnaryOp("-",BooleanLiteral(False)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_continue_statement_6(self):
        input = """
            float foo(){
                 do {
                    if (a % 3 == 0) continue;
                    a = a + 1;
                } while (a < 100);
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Dowhile([Block([If(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(3)),IntLiteral(0)),Continue()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("<",Id("a"),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    def test_continue_statement_7(self):
        input = """
            float foo(){
                 continue;
                 if (a == 10){
                    continue;
                    continue;
                 }
                 continue;
                 //continue
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Continue(),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Continue(),Continue()])),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_continue_statement_8(self):
        input = """
            string main(){{{{{{{continue;}}}}}}}
        """
        expect = str(Program([FuncDecl(Id("main"),[],StringType(),Block([Block([Block([Block([Block([Block([Block([Continue()])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    #Test return statement : 10 tests case
    def test_return_statement_1(self):
        input = """
            void main(){
                return x;
                return y;
                return z;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(Id("x")),Return(Id("y")),Return(Id("z"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_return_statement_2(self):
        input = """
            void main(){
                if (x < 3)
                    return (3 * a) % foo(x)[10];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("<",Id("x"),IntLiteral(3)),Return(BinaryOp("%",BinaryOp("*",IntLiteral(3),Id("a")),ArrayCell(CallExpr(Id("foo"),[Id("x")]),IntLiteral(10)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_return_statement_3(self):
        input = """
            void main(){
                for (x;y;z)
                    return (-(x - 3) % x) * (3 / 4);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("x"),Id("y"),Id("z"),Return(BinaryOp("*",BinaryOp("%",UnaryOp("-",BinaryOp("-",Id("x"),IntLiteral(3))),Id("x")),BinaryOp("/",IntLiteral(3),IntLiteral(4)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_return_statement_4(self):
        input = """
            void main(){
                do
                    return a_p_t_x_4_8_6_9;
                    return this_is_just_a_test_for_the_return_statement;
                while (yes_this_is_true);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Return(Id("a_p_t_x_4_8_6_9")),Return(Id("this_is_just_a_test_for_the_return_statement"))],Id("yes_this_is_true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_return_statement_5(self):
        input = """
            void main(){
                do
                    a = random();
                    if ( a < 10 ) 
                        continue;
                    else 
                        return a * 3 - 100;
                while true;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),CallExpr(Id("random"),[])),If(BinaryOp("<",Id("a"),IntLiteral(10)),Continue(),Return(BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(3)),IntLiteral(100))))],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_return_statement_6(self):
        input = """
            void main(){
                return the_id;
                return id;
                return _std21_;
                return _sddas_[3];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(Id("the_id")),Return(Id("id")),Return(Id("_std21_")),Return(ArrayCell(Id("_sddas_"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_return_statement_7(self):
        input = """
            void main(){
                return 1;
                return 2;
                return 3;
                return 4;
                return 5;
                return 6;
                return 7;
                return 8;
                return 9;
                return 10;
                return 11;
                return 12345567890;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(IntLiteral(1)),Return(IntLiteral(2)),Return(IntLiteral(3)),Return(IntLiteral(4)),Return(IntLiteral(5)),Return(IntLiteral(6)),Return(IntLiteral(7)),Return(IntLiteral(8)),Return(IntLiteral(9)),Return(IntLiteral(10)),Return(IntLiteral(11)),Return(IntLiteral(12345567890))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_return_statement_8(self):
        input = """
            void main(){
                return 1.23445;
                return 1.3e2;
                return 1.45e-100;
                return .456;
                return .456e3;
                return 1e3;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(FloatLiteral(1.23445)),Return(FloatLiteral(130.0)),Return(FloatLiteral(1.45e-100)),Return(FloatLiteral(0.456)),Return(FloatLiteral(456.0)),Return(FloatLiteral(1000.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_return_statement_9(self):
        input = """
            void main(){
                return "^ What are words";
                return "@ Anywhere you are, I am near";
                return "# Anywhere you go, Ill be there";
                return "$ Anytime you whisper my name, youll see";
                return "% How every single promise Ill keep";
                return "^ Cause what kind of guy would I be";
                return "& If I was to leave when you need me most";
                return true;
                return false;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(StringLiteral("^ What are words")),Return(StringLiteral("@ Anywhere you are, I am near")),Return(StringLiteral("# Anywhere you go, Ill be there")),Return(StringLiteral("$ Anytime you whisper my name, youll see")),Return(StringLiteral("% How every single promise Ill keep")),Return(StringLiteral("^ Cause what kind of guy would I be")),Return(StringLiteral("& If I was to leave when you need me most")),Return(BooleanLiteral(True)),Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_return_statement_10(self):
        input = """
            void main(){
                return foo("x","y",a[3],test);
                return _test_not_a_test(1,3e3);   
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(CallExpr(Id("foo"),[StringLiteral("x"),StringLiteral("y"),ArrayCell(Id("a"),IntLiteral(3)),Id("test")])),Return(CallExpr(Id("_test_not_a_test"),[IntLiteral(1),FloatLiteral(3000.0)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    #Test all : 15 tests case
    def test_all_1(self):
        input = """
            int main(){
                string c;
                printf("Enter a character: ");
                scanf("%c",c);
                if (( c >= "a" && c <= "z") || (c >= "A" && c <= "Z"))
                    printf("%c is an alphabet.",c);
                else
                    printf("%c is not an alphabet.",c);
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",StringType()),CallExpr(Id("printf"),[StringLiteral("Enter a character: ")]),CallExpr(Id("scanf"),[StringLiteral("%c"),Id("c")]),If(BinaryOp("||",BinaryOp("&&",BinaryOp(">=",Id("c"),StringLiteral("a")),BinaryOp("<=",Id("c"),StringLiteral("z"))),BinaryOp("&&",BinaryOp(">=",Id("c"),StringLiteral("A")),BinaryOp("<=",Id("c"),StringLiteral("Z")))),CallExpr(Id("printf"),[StringLiteral("%c is an alphabet."),Id("c")]),CallExpr(Id("printf"),[StringLiteral("%c is not an alphabet."),Id("c")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_all_2(self):
        input = """         
            int A[8],X[8],Y[8], dem, n;
            void xuat() {
                int i,j;
                for (i = 0; i < n; i = i + 1) {
                    for (j = 0; j < n; j = j + 1)
                        printf("%2d ", A[i]);
                }
            }
 
            void diChuyen(int x, int y) {
                int u,v;
                dem = dem + 1;
                A[x] = dem;
                for (i = 0; i < 8; i = i + 1)    {
                    if (dem == n * n) {
                        printf("Cac buoc di la: \\n");
                    xuat();
                    exit(0);
                }
                u = x + X[i];
                v = y + Y[i];
                if (u >= 0 && u < n&&v >= 0 && v < n&& A[u] == 0)
                    diChuyen(u, v);
                }
                dem = dem - 1;
                A[x] = 0;
            }   
        """
        expect = str(Program([VarDecl("A",ArrayType(8,IntType())),VarDecl("X",ArrayType(8,IntType())),VarDecl("Y",ArrayType(8,IntType(),)),VarDecl("dem",IntType()),VarDecl("n",IntType()),FuncDecl(Id("xuat"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("%2d "),ArrayCell(Id("A"),Id("i"))]))]))])),FuncDecl(Id("diChuyen"),[VarDecl("x",IntType()),VarDecl("y",IntType())],VoidType(),Block([VarDecl("u",IntType()),VarDecl("v",IntType()),BinaryOp("=",Id("dem"),BinaryOp("+",Id("dem"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("A"),Id("x")),Id("dem")),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(8)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("dem"),BinaryOp("*",Id("n"),Id("n"))),Block([CallExpr(Id("printf"),[StringLiteral("Cac buoc di la: \\n")]),CallExpr(Id("xuat"),[]),CallExpr(Id("exit"),[IntLiteral(0)])])),BinaryOp("=",Id("u"),BinaryOp("+",Id("x"),ArrayCell(Id("X"),Id("i")))),BinaryOp("=",Id("v"),BinaryOp("+",Id("y"),ArrayCell(Id("Y"),Id("i")))),If(BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BinaryOp(">=",Id("u"),IntLiteral(0)),BinaryOp("<",Id("u"),Id("n"))),BinaryOp(">=",Id("v"),IntLiteral(0))),BinaryOp("<",Id("v"),Id("n"))),BinaryOp("==",ArrayCell(Id("A"),Id("u")),IntLiteral(0))),CallExpr(Id("diChuyen"),[Id("u"),Id("v")]))])),BinaryOp("=",Id("dem"),BinaryOp("-",Id("dem"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("A"),Id("x")),IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_all_3(self):
        input = """
            int main() {
                printf("Enter a sentence: ");
                reverseSentence();
                return 0;
            }
            void reverseSentence() {
                string c;
                scanf("%c", c);
                if( c != "\\n") {
                    reverseSentence();
                    printf("%c",c);
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Enter a sentence: ")]),CallExpr(Id("reverseSentence"),[]),Return(IntLiteral(0))])),FuncDecl(Id("reverseSentence"),[],VoidType(),Block([VarDecl("c",StringType()),CallExpr(Id("scanf"),[StringLiteral("%c"),Id("c")]),If(BinaryOp("!=",Id("c"),StringLiteral("\\n")),Block([CallExpr(Id("reverseSentence"),[]),CallExpr(Id("printf"),[StringLiteral("%c"),Id("c")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_all_4(self):
        input = """
            int main() {
                int i, n;
                float arr[100];
                printf("Enter total number of elements(1 to 100): ");
                scanf("%d", n);
                printf("\\n");
                // Stores number entered by the user
                for(i = 0; i < n; i = i + 1) {
                    printf("Enter Number %d: ", i+1);
                    scanf("%f", arr[i]);
                }
                // Loop to store largest number to arr[0]
                for(i = 1; i < n; i = i + 1) {
                    // Change < to > if you want to find the smallest element
                    if(arr[0] < arr[i])
                        arr[0] = arr[i];
                }
                printf("Largest element = %.2f", arr[0]);
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("n",IntType()),VarDecl("arr",ArrayType(100,FloatType())),CallExpr(Id("printf"),[StringLiteral("Enter total number of elements(1 to 100): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral("\\n")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Enter Number %d: "),BinaryOp("+",Id("i"),IntLiteral(1))]),CallExpr(Id("scanf"),[StringLiteral("%f"),ArrayCell(Id("arr"),Id("i"))])])),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<",ArrayCell(Id("arr"),IntLiteral(0)),ArrayCell(Id("arr"),Id("i"))),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),ArrayCell(Id("arr"),Id("i"))))])),CallExpr(Id("printf"),[StringLiteral("Largest element = %.2f"),ArrayCell(Id("arr"),IntLiteral(0))]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_all_5(self):
        input = """
            int main() {
                int base, powerRaised, result;
                printf("Enter base number: ");
                scanf("%d",base);
                printf("Enter power number(positive integer): ");
                scanf("%d",powerRaised);
                result = power(base, powerRaised);
                printf("%d^%d = %d", base, powerRaised, result);
                return 0;
            }
            int power(int base, int powerRaised) {
                if (powerRaised != 0)
                    return (base*power(base, powerRaised-1));
                else
                    return 1;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("base",IntType()),VarDecl("powerRaised",IntType()),VarDecl("result",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter base number: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("base")]),CallExpr(Id("printf"),[StringLiteral("Enter power number(positive integer): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("powerRaised")]),BinaryOp("=",Id("result"),CallExpr(Id("power"),[Id("base"),Id("powerRaised")])),CallExpr(Id("printf"),[StringLiteral("%d^%d = %d"),Id("base"),Id("powerRaised"),Id("result")]),Return(IntLiteral(0))])),FuncDecl(Id("power"),[VarDecl("base",IntType()),VarDecl("powerRaised",IntType())],IntType(),Block([If(BinaryOp("!=",Id("powerRaised"),IntLiteral(0)),Return(BinaryOp("*",Id("base"),CallExpr(Id("power"),[Id("base"),BinaryOp("-",Id("powerRaised"),IntLiteral(1))]))),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_all_6(self):
        input = """
            int main(){
                uppercase_alphabet = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"; 
                lowercase_alphabet = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z";
                number             = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9";
                special_character  = "\\\\, \\b, \\n, \\t, \\n, \\f, @, #, $, %, &, *, +";
                print(uppercase_alphabet, lowercase_alphabet, number, special_character);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("uppercase_alphabet"),StringLiteral("A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z")),BinaryOp("=",Id("lowercase_alphabet"),StringLiteral("a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z")),BinaryOp("=",Id("number"),StringLiteral("0, 1, 2, 3, 4, 5, 6, 7, 8, 9")),BinaryOp("=",Id("special_character"),StringLiteral("\\\\, \\b, \\n, \\t, \\n, \\f, @, #, $, %, &, *, +")),CallExpr(Id("print"),[Id("uppercase_alphabet"),Id("lowercase_alphabet"),Id("number"),Id("special_character")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_all_7(self):
        input = """
            int main(){
                main(main(main(main(main(main(main(main(main(main(main(main(main(main(main))))))))))))));
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[Id("main")])])])])])])])])])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_all_8(self):
        input = """
            int main(int argc, string argv){
                string input;
                print("Hello, This is Chat Bot made by Ryan \\n") ;
                print("say hi");
                do {
                    scanf("%s",input);
                    for (i=0; i<length(input); i = i + 1)
                        input[i] = tolower(input[i],loc);
                    if (input == "hi")
                        print("hello there \\n");
                    else if (input == "hi")
                        print("Hey, what's up?\\n");
                    else
                        print("Well i didn't understand. I hope i will be able to, soon! \\n");
                } while (input != "exit");
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",IntType()),VarDecl("argv",StringType())],IntType(),Block([VarDecl("input",StringType()),CallExpr(Id("print"),[StringLiteral("Hello, This is Chat Bot made by Ryan \\n")]),CallExpr(Id("print"),[StringLiteral("say hi")]),Dowhile([Block([CallExpr(Id("scanf"),[StringLiteral("%s"),Id("input")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("length"),[Id("input")])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("input"),Id("i")),CallExpr(Id("tolower"),[ArrayCell(Id("input"),Id("i")),Id("loc")]))),If(BinaryOp("==",Id("input"),StringLiteral("hi")),CallExpr(Id("print"),[StringLiteral("hello there \\n")]),If(BinaryOp("==",Id("input"),StringLiteral("hi")),CallExpr(Id("print"),[StringLiteral("Hey, what's up?\\n")]),CallExpr(Id("print"),[StringLiteral("Well i didn't understand. I hope i will be able to, soon! \\n")])))])],BinaryOp("!=",Id("input"),StringLiteral("exit"))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_all_9(self):
        input = """
            int main(){
                {}
                {{}}
                {{{}}}
                {{{{}}}}
                {{{{{}}}}}
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([Block([])]),Block([Block([Block([])])]),Block([Block([Block([Block([])])])]),Block([Block([Block([Block([Block([])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_all_10(self):
        input = """
            int foo(int a,float b[]) {
                boolean c ;
                int i; 
                i=a+3; 
                if (i>0) {
                    int d; 
                    d=i+3; 
                    putInt(d);
                }
                return i; 
            }
            int main(){
                foo(10,x);
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[IntLiteral(10),Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_all_11(self):
        input = """
            int[] foo(int a, float b[]) {int c[3]; if (a>0) foo(a-1,b); return c; }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_all_12(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_all_13(self):
        input = """
            int main() {
                int n, t1, t2, nextTerm;
                for (i = 1; i <= n; i = i + 1) {
                     // Prints the first two terms.
                    if ((i == 1) || (i == 2)) {
                        print( "%d",t1);
                        continue;
                    }
                    nextTerm = t1 + t2;
                    t1 = t2;
                    t2 = nextTerm;
                    print("%d ",nextTerm);
                }
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("t1",IntType()),VarDecl("t2",IntType()),VarDecl("nextTerm",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(1)),BinaryOp("==",Id("i"),IntLiteral(2))),Block([CallExpr(Id("print"),[StringLiteral("%d"),Id("t1")]),Continue()])),BinaryOp("=",Id("nextTerm"),BinaryOp("+",Id("t1"),Id("t2"))),BinaryOp("=",Id("t1"),Id("t2")),BinaryOp("=",Id("t2"),Id("nextTerm")),CallExpr(Id("print"),[StringLiteral("%d "),Id("nextTerm")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_all_14(self):
        input = """
            // Check prime number
            boolean checkPrime(int n) {
                int i;
                boolean isPrime; 
                isPrime = true;
                for(i = 2; i <= n/2; i = i + 1) {
                    if(n % i == 0) {
                        isPrime = false;
                        break;
                    }
                }
                return isPrime;
            }
        """
        expect = str(Program([FuncDecl(Id("checkPrime"),[VarDecl("n",IntType())],BoolType(),Block([VarDecl("i",IntType()),VarDecl("isPrime",BoolType()),BinaryOp("=",Id("isPrime"),BooleanLiteral(True)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("isPrime"),BooleanLiteral(False)),Break()]))])),Return(Id("isPrime"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_all_15(self):
        input = """
            int main(int x) {
                int low, high, i, flag;
                do {
                    flag = 0;
                    for(i = 2; i <= low/2; i = i + 1) {
                        if(low % i == 0) {
                            flag = 1;
                            break;
                        }
                    }
                    if (flag == 0)
                        low = low + 1;
                } while (low < high);
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType())],IntType(),Block([VarDecl("low",IntType()),VarDecl("high",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),Dowhile([Block([BinaryOp("=",Id("flag"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("low"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("low"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("flag"),IntLiteral(0)),BinaryOp("=",Id("low"),BinaryOp("+",Id("low"),IntLiteral(1))))])],BinaryOp("<",Id("low"),Id("high"))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))