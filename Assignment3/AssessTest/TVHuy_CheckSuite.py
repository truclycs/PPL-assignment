import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """int main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Undeclare function"""
        input = Program([

            FuncDecl(Id("main"),[],IntType(),Block([
                Dowhile([Continue()], IntLiteral(1)),
                CallExpr(Id("putIntLnxxx"),[IntLiteral(4)])
            ]))
            ])
        expect = "Undeclared Function: putIntLnxxx"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program""" 
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                    CallExpr(Id("getInt"),[IntLiteral(4)])
                ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,405))

    
    def test_main_declare_1(self):
        """Redeclare variable"""
        input = Program([
                VarDecl("xxx", IntType()),
                VarDecl("xxx", IntType()),
                FuncDecl(Id("main"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ]))
                ])
        expect = "Redeclared Variable: xxx"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_main_declare_08(self):
        """Redeclare function"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ])),
                FuncDecl(Id("main"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ]))
                ])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_main_declare_09(self):
        """Redeclare param"""
        input = Program([
                FuncDecl(Id("bar"),[VarDecl("a",IntType()), VarDecl("a",IntType())],VoidType(),Block([
                CallExpr(Id("putIntLn"),[IntLiteral(4)])])),
                FuncDecl(Id("main"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ]))
                ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_function_not_return(self):
        """Function not return"""
        input = Program([

            FuncDecl(Id("main"),[],IntType(),Block([
                
            ]))
            ])
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,410))


    def test_break_in_loop(self):
        """Undeclare function"""
        input = Program([

            FuncDecl(Id("main"),[],IntType(),Block([
                Break(),
                Return(IntLiteral(1))
            ]))
            ])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,411))


    def test_continue_in_loop(self):
        """Continue Not In Loop"""
        input = Program([

            FuncDecl(Id("main"),[],IntType(),Block([
                Continue(),
                Return(IntLiteral(1))
            ]))
            ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_has_no_entry_point(self):
        """No Entry point"""
        input = Program([

            ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_has_no_entry_point(self):
        """Unreachable function"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ])),
                FuncDecl(Id("mainx"),[],IntType(),Block([
                    Return(IntLiteral(1))
                ]))
            ])
        expect = "Unreachable Function: mainx"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_function_1(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_function_not_return_2(self):
        """Undeclare Function true"""
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("putIntLn"),[IntLiteral(4)]),
            Return(IntLiteral(4))]
            ))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

   
    

    def test_has_no_entry_point_2(self):
        """No Entry point"""
        input = Program(
            [FuncDecl(Id("foo1"),[],VoidType(),Block([]
            
            ))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,417))	
    def test_has_no_entry_point_3(self):
        """No Entry Ponit"""
        input = Program([
                FuncDecl(Id("foo1"),[],VoidType(),Block(
                [CallExpr(Id("foo2"),[]),Return()])),
                FuncDecl(Id("foo2"),[],VoidType(),Block([CallExpr(Id("foo1"),[]),Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,418))	

    def test_has_no_entry_point_4(self):
        """No Entry Point"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
                VoidType(),Block([Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_has_no_entry_point_5(self):
        """No Entry Point"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),Block(
                [Return()])),
                FuncDecl(Id("foo1"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_has_no_entry_point_6(self):
        """No Entry Point"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
                VoidType(),Block([Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_break_in_loop_1(self):
        """test In Loop"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),Block([Break()])),
                FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())]))])
                
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_has_no_entry_point_7(self):
        """No Entry Point"""
        input = Program([FuncDecl(Id("foo1"),[],VoidType(),
                Block([CallExpr(Id("foo2"),[]),Return()])),
                FuncDecl(Id("foo2"),[],VoidType(),Block([CallExpr(Id("foo3"),[]),Return()])),
                FuncDecl(Id("foo3"),[],VoidType(),
                Block([Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,423))	

    def test_function_not_return_3(self):
        """test """
        input = Program([FuncDecl(Id("fifa"),[],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("a"),IntType())]))])
        expect = "Function fifa Not Return "
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function_3(self):
        """"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("b"),IntType())],IntType(),
                Block(Return(Id("b")
                #)))
                #,FuncDecl(Id("main"),[],VoidType(),
                # Block([VarDecl(Id("a"),IntType())])
                )))
                ])
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_func_declare(self):
        """test function declare """
        input = Program([FuncDecl(Id("main"),[],
                VoidType(),Block([Return()])),
                FuncDecl(Id("main"),[],VoidType(),
                Block([Return()]))])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_func_declare_1(self):
        """test function declare 3"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),
                Block([Return()])),FuncDecl(Id("main"),[],VoidType(),
                Block([Return()])),FuncDecl(Id("foo"),[],VoidType(),
                Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_para_declare_1(self):
        """test parameter declare 1"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("a"),IntType()),
                VarDecl(Id("a"),IntType())],
                VoidType(),Block([])),
                FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),
                [IntLiteral(5),IntLiteral(6)]),
                Return()]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_para_declare_2(self):
        """test parameter declare 2"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),
                VarDecl(Id("b"),IntType()),
                FuncDecl(Id("main"),[],IntType(),Block([
                CallExpr(Id("putIntLn"),[IntLiteral(4)]),
                Return(IntLiteral(4))]
                ))])])
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_break_in_loop_2(self):
        """test break: 2"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),
                Block([Break()])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_para_declare_3(self):
        """test parameter declare 3"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
                VoidType(),Block([])),FuncDecl(Id("foo1"),
                [VarDecl(Id("a"),IntType()),VarDecl(Id("a"),IntType())],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),
                [IntLiteral(5)]),CallExpr(Id("foo1"),
                [IntLiteral(4),IntLiteral(1)]),Return()]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,429))	

    def test_mismatch_return_state(self):
        """test return type match in statement"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("putIntLn"),[IntLiteral(4)]),
                Return(BinaryOp("",IntLiteral(1),IntLiteral(2)))]
                ))])
                
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))    
    
    def test_var_declare_4(self):
        """test variable declare 4"""
        input = Program([VarDecl(Id("a"),IntType()),VarDecl(Id("a"),
                IntType()),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_var_declare_5(self):
        """test variable declare 5"""
        input = Program([VarDecl(Id("a"),IntType()),
                VarDecl(Id("a"),FloatType()),
                FuncDecl(Id("main"),[],VoidType(),
                Block([Return()]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,432))
	
		
    def test_para_declare_4(self):
        """test parameter declare 4"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),
                IntType()),VarDecl(Id("b"),IntType()),
                VarDecl(Id("b"),IntType())],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(4),
                IntLiteral(5)]),Return()]))])
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,433))

    
		
    def test_main_declare_4(self):
        """test main function declare 4"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),
                IntType())],VoidType(),Block([Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_main_declare_5(self):
        """test main function declare 5"""
        input = Program([VarDecl(Id("a"),IntType()),
                FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],VoidType(),Block([Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,435))
		
    def test_id_1(self):
        """test identifier 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),IntLiteral(5)),
                BinaryOp("=",Id("j"),IntLiteral(6)),
                Return()]))])
        expect = "Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input,expect,436))

   

   
	
    def test_mismatch_if_state_1(self):
        """test if type match in statement 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([If(BinaryOp("=",Id("i"),IntLiteral(10)),
                BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))
                ),
                Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(=,Id(i),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,437))
		
    def test_mismatch_if_state_2(self):
        """test if type match in statement 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("+",Id("i"),Id("j")),
                BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(+,Id(i),Id(j))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_mismatch_if_state_3(self):
        """test if type match in statement 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([If(BinaryOp("*",Id("i"),Id("j")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(*,Id(i),Id(j))"
        self.assertTrue(TestChecker.test(input,expect,439))		
		
    def test_mismatch_for_state_1(self):
        """test for type match in statement 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block(For(BinaryOp("=",Id("i"),IntLiteral(0)),
                BinaryOp("=",Id("i"),IntLiteral(10)),
                BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1))))))])
        expect = "Type Mismatch In Statement: BinaryOp(=,Id(i),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,440))		
		
    def test_mismatch_for_state_2(self):
        """test for type match in statement 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("+",Id("i"),
                IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(+,Id(i),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,441))		
		
    def test_mismatch_for_state_3(self):
        """test for type match in statement 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("/",Id("i"),
                IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(/,Id(i),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,442))	

    def test_mismatch_for_state_4(self):
        """test for type match in statement 4"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block(
                    [For(BinaryOp("==",Id("i"),IntLiteral(0)),
                    BinaryOp("<",Id("i"),IntLiteral(5)),
                    BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(==,Id(i),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_mismatch_for_state_5(self):
        """test for type match in statement 5"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([For(BooleanLiteral(True),BinaryOp("<",Id("i"),
                IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),
                IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_mismatch_for_state_6(self):
        """test for type match in statement 6"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([For(BinaryOp("||",BooleanLiteral(True),
                BooleanLiteral(False)),BinaryOp("<",Id("i"),IntLiteral(5)),
                BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("i"),
                BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_id_4(self):
        """test identifier 4"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("j"),IntLiteral(5)),Return()]))])
        expect = "Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_mismatch_for_state_7(self):
        """test for type match in statement 7"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("==",Id("j"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(==,Id(j),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_mismatch_for_state_8(self):
        """test for type match in statement 8"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("<=",Id("i"),Id("j")),BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(<=,Id(i),Id(j))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_mismatch_for_state_9(self):
        """test for type match in statement 9"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BooleanLiteral(False),BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(1)))),Return()]))])
        expect = "Type Mismatch In Statement: BooleanLiteral(False)"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_mismatch_while_state_1(self):
        """test while type match in statement 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),IntLiteral(1)))],BinaryOp("=",Id("j"),IntLiteral(10)))]))])
        expect = "Type Mismatch In Statement: BinaryOp(=,Id(j),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_mismatch_while_state_2(self):
        """test while type match in statement 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),IntLiteral(1)))],StringLiteral("\"abc\"")),Return()]))])
        expect = "Type Mismatch In Statement: StringLiteral(abc)"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_mismatch_while_state_3(self):
        """test while type match in statement 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),IntLiteral(1)))],BinaryOp("+",IntLiteral(1),IntLiteral(1))),Return()]))])
        expect = "Type Mismatch In Statement: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,452))		
		
    def test_mismatch_return_state_1(self):
        """test return type match in statement 1 correct"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block(
                [Return(BinaryOp("=",Id("i"),IntLiteral(1)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))

    

    def test_mismatch_return_state_3(self):
        """test return type match in statement 3 correct"""
        input = Program([FuncDecl(Id("main"),[],
                VoidType(),
                Block([Return(FloatLiteral(1.5))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))		
		
    def test_mismatch_return_state_4(self):
        """test return type match in statement 4"""
        input = Program([FuncDecl(Id("foo"),[],IntType(),
                Block([VarDecl(Id("a"),IntType())],[Return(FloatLiteral(3.5))])),
                FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("i"),
                CallExpr(Id("foo"),[IntLiteral(5)])),Return()]))])
        expect = "Type Mismatch In Statement: Return(FloatLiteral(3.5))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_mismatch_return_state_5(self):
        """test return type match in statement 5"""
        input = Program([FuncDecl(Id("foo"),[],FloatType(),
                Block([VarDecl(Id("a"),IntType())],[Return(StringLiteral("\"abc\""))])),
                FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("i"),
                FloatType()),VarDecl(Id("j"),FloatType())],[BinaryOp("=",Id("i"),CallExpr(Id("foo"),[])),Return()]))])
        expect = "Type Mismatch In Statement: ReturnStringLiteral(\"abc\"))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_mismatch_return_state_6(self):
        """test return type match in statement 6"""
        input = Program([FuncDecl(Id("foo"),[],BoolType(),
                Block([VarDecl(Id("a"),IntType())],[Return(IntLiteral(7))])),
                FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("i"),BoolType()),
                VarDecl(Id("j"),BoolType())],[BinaryOp("=",Id("i"),
                CallExpr(Id("foo"),[])),Return()]))])
        expect = "Type Mismatch In Statement: Return(IntLiteral(7))"
        self.assertTrue(TestChecker.test(input,expect,458))			
				
    def test_mismatch_array_exp_1(self):
        """test array type match in expression 1"""
        input = Program([FuncDecl(Id("main"),[],
                VoidType(),Block([VarDecl(Id("i"),
                ArrayType(IntLiteral(5),IntType())),VarDecl(Id("j"),IntType()),
                VarDecl(Id("k"),FloatType())],[BinaryOp("=",Id("j"),ArrayCell(Id("i"),Id("k"))),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(i),Id(k))"
        self.assertTrue(TestChecker.test(input,expect,459))
		
    def test_mismatch_array_exp_2(self):
        """test array type match in expression 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),ArrayType(IntLiteral(5),
                IntType())),VarDecl(Id("j"),IntType())],[BinaryOp("=",
                Id("j"),ArrayCell(Id("i"),BooleanLiteral(True))),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(i),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,460))		
		
    def test_mismatch_array_exp_3(self):
        """test array type match in expression 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),ArrayPointerType(IntType())),
                VarDecl(Id("j"),IntType())],[BinaryOp("=",Id("j"),ArrayCell(Id("i"),
                IntLiteral(2))),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(i),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,461))		
		
    def test_mismatch_array_exp_4(self):
        """test array type match in expression 4"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),
                VarDecl(Id("j"),IntType())],[BinaryOp("=",Id("j"),
                ArrayCell(Id("i"),IntLiteral(2))),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(i),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,462))	

    def test_mismatch_binary_exp_1(self):
        """test binary type match in expression 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("+",BooleanLiteral(True),
                BooleanLiteral(False)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_mismatch_binary_exp_2(self):
        """test binary type match in expression 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp(">",BooleanLiteral(True),
                BooleanLiteral(False)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(true),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_mismatch_binary_exp_3(self):
        """test binary type match in expression 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("&&",IntLiteral(4),IntLiteral(3)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLiteral(4),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_mismatch_binary_exp_4(self):
        """test binary type match in expression 4 Correct"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("||",IntLiteral(4),IntLiteral(3)),Return()]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_mismatch_binary_exp_5(self):
        """test binary type match in expression 5"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("||",Id("i"),Id("j")),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(i),Id(j))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_mismatch_binary_exp_6(self):
        """test binary type match in expression 6"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),
                VarDecl(Id("j"),FloatType())],[BinaryOp("&&",Id("i"),IntLiteral(3.5)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(i),IntLiteral(3.5))"
        self.assertTrue(TestChecker.test(input,expect,468))
				
    def test_mismatch_unary_exp_1(self):
        """test unary type match in expression 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("=",Id("i"),UnaryOp("-",BooleanLiteral(True))),Return()]))])
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,469))
		
    def test_mismatch_unary_exp_2(self):
        """test unary type match in expression 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("=",Id("i"),UnaryOp("-",StringLiteral("\"abc\""))),Return()]))])
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLiteral(\"abc\"))"
        self.assertTrue(TestChecker.test(input,expect,470))		
	
    def test_mismatch_assign_exp_1(self):
        """test assignment type match in expression 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("i"),
                FloatLiteral(5.6)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),FloatLiteral(5.6))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_mismatch_assign_exp_2(self):
        """test assignment type match in expression 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),IntLiteral(1))),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(+,Id(j),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_mismatch_assign_exp_3(self):
        """test assignment type match in expression 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("=",Id("i"),StringLiteral("\"abc\"")),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_mismatch_assign_exp_4(self):
        """test assignment type match in expression 4"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),
                FloatType())],[BinaryOp("=",Id("i"),BooleanLiteral(True)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_mismatch_assign_exp_5(self):
        """test assignment type match in expression 5"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),StringType()),VarDecl(Id("j"),
                BoolType())],[BinaryOp("=",Id("i"),BooleanLiteral(False)),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_mismatch_assign_exp_6(self):
        """test assignment type match in expression 6"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),StringType()),VarDecl(Id("j"),
                BoolType())],[BinaryOp("=",Id("j"),StringLiteral("\"abc\"")),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(j),StringType(abc))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_mismatch_assign_exp_7(self):
        """test assignment type match in expression 7"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),StringType()),VarDecl(Id("j"),
                BoolType())],[BinaryOp("=",Id("j"),StringLiteral("\"abc\"")),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(j),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_mismatch_assign_exp_8(self):
        """test assignment type match in expression 8"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("i"),FloatType()),VarDecl(Id("j"),IntType())],
                [BinaryOp("=",Id("i"),BinaryOp("-",Id("j"),IntLiteral(10))),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(-,Id(j),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_call_exp_1(self):
        """test call expression 1"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),
                Block([],[])),FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("a"),IntType())],[BinaryOp("=",Id("a"),IntLiteral(6)),Return()]))])
        expect = "Unreachable function: foo"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_call_exp_2(self):
        """test call expression 2"""
        input = Program([FuncDecl(Id("fifa"),[],VoidType(),
                Block([],[])),FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("a"),IntType())],[BinaryOp("=",Id("a"),IntLiteral(6)),Return()]))])
        expect = "Unreachable function: fifa"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_call_exp_3(self):
        """test call expression 3"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("b"),IntType())],IntType(),
                Block([],[Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("a"),IntType())],[CallExpr(Id("foo"),[IntLiteral(4)]),Return()]))])
        expect = "Unreachable function: foo"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_call_exp_4(self):
        """test call expression 4"""
        input = Program([FuncDecl(Id("foo"),[
                    VarDecl(Id("b"),IntType())],StringType(),
                    Block([],[Return(StringLiteral("\"abc\""))])),
                    FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType())],[BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(6)])),Return()]))])
        expect = "Unreachable function: foo"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_mismatch_call_exp_1(self):
        """test call expression type match in expression: 1"""
        input = Program([FuncDecl(Id("foo"),[
                VarDecl(Id("b"),IntType())],VoidType(),
                Block([],[])),FuncDecl(Id("main"),[],VoidType(),
                Block([VarDecl(Id("a"),IntType())],
                [CallExpr(Id("foo"),[IntLiteral(6),IntLiteral(10)]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(6),IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,482))		

    def test_mismatch_call_exp_2(self):
        """test call expression type match in expression: 2"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("b"),
                IntType())],VoidType(),Block([],[])),
                FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType())],[CallExpr(Id("foo"),[]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),List())"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_mismatch_call_exp_3(self):
        """test call expression type match in expression: 3"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("b"),
                IntType())],VoidType(),Block([],[])),FuncDecl(Id("main"),[],
                VoidType(),Block([VarDecl(Id("a"),IntType())],[CallExpr(Id("foo"),[StringLiteral("\"abc\"")]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[StringLiteral(abc)])"
        self.assertTrue(TestChecker.test(input,expect,485))

    

    

    def test_break_2(self):
        """test break: 2"""
        input = Program([FuncDecl(Id("foo"),[
                    VarDecl(Id("b"),IntType())],VoidType(),
                    Block([If(BinaryOp("<",Id("b"),IntLiteral(10)),
                    BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Break())])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())],[CallExpr(Id("foo"),[]),Return()]))])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_continue_1(self):
        """test continue: 1"""
        input = Program([FuncDecl(Id("foo"),[
                    VarDecl(Id("b"),IntType())],VoidType(),
                    Block([If(BinaryOp("<",Id("b"),IntLiteral(10)),BinaryOp("=",Id("b"),
                    BinaryOp("+",Id("b"),IntLiteral(1))),Continue())])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())],[CallExpr(Id("foo"),[]),Return()]))])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_continue_2(self):
        """test continue: 2"""
        input = Program([FuncDecl(Id("foo"),[
                VarDecl(Id("b"),IntType())],VoidType(),
                Block([BinaryOp("=",Id("b"),IntLiteral(5)),Continue()])),
                FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())],[CallExpr(Id("foo"),[]),Return()]))])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_unreach_state_1(self):
        """test unreach statement: 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([If(BooleanLiteral(False),
                BinaryOp("=",Id("a"),IntLiteral(10)),None),Return()]))])
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_unreach_state_2(self):
        """test unreach statement: 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block(If(BooleanLiteral(False),Block([],
                [BinaryOp("=",Id("a"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(10))]),None),Return()))])
        expect = "Unreachable statement: Block([BinaryOp(=,Id(a),IntLiteral(5)),BinaryOp(=,Id(b),IntLiteral(10))])"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_unreach_state_3(self):
        """test unreach statement: 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("a"),IntLiteral(1)),Return(),BinaryOp("=",Id("b"),Id("a"))]))])
        expect = "Unreachable statement: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_unreach_state_4(self):
        """test unreach statement: 4"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("a"),IntLiteral(1)),Return(),BinaryOp("=",Id("b"),BinaryOp("*",IntLiteral(5),IntLiteral(5)))]))])
        expect = "Unreachable statement: BinaryOp(*,IntLiteral(5),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,492))		
		
    def test_mismatch_return_state_7(self):
        """test return type match in statement 7"""
        input = Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),
                Block([Return(IntLiteral(10))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("i"),BoolType()),VarDecl(Id("j"),BoolType())],[BinaryOp("=",Id("i"),CallExpr(Id("foo"),[])),Return()]))])
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,493))
		
    def test_mismatch_return_state_8(self):
        """test return type match in statement 8"""
        input = Program([FuncDecl(Id("foo"),[],
                ArrayPointerType(StringType()),
                Block([Return(ArrayCell(Id("a"),IntType()))])),FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("i"),CallExpr(Id("foo"),[])),Return()]))])
        expect = "Type Mismatch In Statement: Return(Some(ArrayCell(Id(a),IntType)))"
        self.assertTrue(TestChecker.test(input,expect,494))
		
    def test_program_1(self):
        """test complex program: 1"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([If(BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(4)),IntLiteral(3)),
                BinaryOp("=",Id("a"),BinaryOp("*",Id("b"),Id("b"))),None),Return()]))])
        expect = "Unreachable statement: BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(4)),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_program_2(self):
        """test complex program: 2"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("-",BinaryOp("*",Id("i"),Id("j")),IntLiteral(5)),
                BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),Id("i"))),Block([],[BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),
                IntLiteral(5))),BinaryOp("=",Id("j"),BinaryOp("-",Id("i"),IntLiteral(5)))])),Return()]))])
        expect = "Unreachable statement: BinaryOp(*,Id(i),Id(j)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,496))
		
    def test_program_3(self):
        """test complex program: 3"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),Id("j")))],
                BinaryOp("=",Id("b"),IntLiteral(6))),Return()]))])
        expect = "Unreachable statement: BinaryOp(*,Id(i),Id(j)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,497))
		
    def test_program_4(self):
        """test complex program: 4"""
        input = Program([FuncDecl(Id("foo"),[],VoidType(),
                Block([Return()])),FuncDecl(Id("foo1"),[],
                VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,498))
		
    def test_program_5(self):
        """test complex program: 5"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("a"),IntType()),VarDecl(Id("a"),
                IntType()),VarDecl(Id("a"),IntType())],VoidType(),Block(
                [Return()])),FuncDecl(Id("main"),[],VoidType(),
                Block(CallExpr(Id("foo"),[IntLiteral(6),
                IntLiteral(7),IntLiteral(8)]),Return()))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,499))
		
    def test_program_6(self):
        """test complex program: 6"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
                VoidType(),Block([],[])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[IntLiteral(6),
                IntLiteral(7),IntLiteral(8)]),Return()]))])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,4100))		
		
    def test_program_7(self):
        """test complex program: 7"""
        input = Program([FuncDecl(Id("main"),[],VoidType(),
                Block([If(BooleanLiteral(False),BinaryOp("=",Id("i"),BinaryOp("+",Id("j"),IntLiteral(1))),None),Return()]))])
        expect = "Unreachable statement: BinaryOp(Id(i),BinaryOp(+,Id(j),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,4101))		
		
    def test_program_8(self):
        """test complex program: 8"""
        input = Program([FuncDecl(Id("foo1"),[],VoidType(),
                Block([CallExpr(Id("foo2"),[]),Return()])),
                FuncDecl(Id("foo2"),[],VoidType(),
                Block([CallExpr(Id("foo1"),[]),Return()]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,4102))		
		
    def test_mismatch_call_exp_4(self):
        """test call expression type match in expression: 4"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("b"),IntType())],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[BooleanLiteral(True)]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,4103))
		
    def test_mismatch_call_exp_5(self):
        """test call expression type match in expression: 5"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("b"),
                ArrayPointerType(IntType()))],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[IntLiteral(6)]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(6)])"
        self.assertTrue(TestChecker.test(input,expect,4104))

    def test_mismatch_call_exp_6(self):
        """test call expression type match in expression: 6"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("b"),
                ArrayPointerType(IntType()))],VoidType(),
                Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([CallExpr(Id("foo"),[FloatLiteral(6)]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(6)])"
        self.assertTrue(TestChecker.test(input,expect,4105))

    def test_func_return_1(self):
        """test function not return: 1"""
        input = Program([FuncDecl(Id("foo"),[VarDecl(Id("b"),IntType())],
                IntType(),Block([])),FuncDecl(Id("main"),[],VoidType(),
                Block([BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(6)])),Return()]))])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,4106))

    def test_func_return_2(self):
        """test function not return: 2"""
        input = Program([FuncDecl(Id("foo"),
                [VarDecl(Id("b"),IntType())],FloatType(),
                Block([])),FuncDecl(Id("main"),[],
                VoidType(),Block([VarDecl(Id("a"),FloatType())],
                [BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(6)])),Return()]))])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,4107))
    