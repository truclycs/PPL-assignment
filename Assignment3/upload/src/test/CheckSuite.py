import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """void main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        input = """void main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        input = """void main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,405))

    def testRedeclaredVariable1(self):
        input = """
        int a;
        int a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def testRedeclaredVariable2(self):  
        input = """
        int b;
        float b;
        void main() {}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,407))

    def testRedeclaredVariable3(self):  
        input = """
        int c;
        void main() {}
        string c;
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,408))

    def testRedeclaredVariable3(self):  
        input = """
        int c;
        void main() {}
        string c;
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,409))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,419))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,426))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,431))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,432))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,433))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,439))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,440))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,441))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,442))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,449))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,453))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,454))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,458))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,460))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,461))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,462))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,463))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,465))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,466))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,467))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,468))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,470))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,471))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,472))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,473))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,474))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,476))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,477))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,478))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,479))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,481))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,482))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,483))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,484))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,485))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,486))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,487))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,488))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,489))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,490))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,491))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,492))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,493))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,494))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,495))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,496))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,497))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,498))

    # def test(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,499))    