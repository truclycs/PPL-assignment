import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_for_stmt(self):
        """More complex program"""
        input = """int main () {
            for (i=4;i<n;i=i+1){
                int a;
                a=(n/2)+1;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))