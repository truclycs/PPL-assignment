import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_1(self):
        ip = """
        int std_id;
        float sem_score;
        boolean isStudent;
        string myString;
        """
        expect = str(
            Program([VarDecl("std_id",IntType()),VarDecl("sem_score",FloatType()),VarDecl("isStudent",BoolType()),VarDecl("myString",StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 301))

    def test_var_decl_2(self):
        ip = """
        int alpha;
        int alpha, beta, gama;
        """
        expect = str(
            Program([VarDecl("alpha", IntType()), VarDecl("alpha", IntType()), VarDecl("beta", IntType()), VarDecl("gama", IntType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 302))

    def test_var_decl_3(self):
        ip = """
        float math_score[5], phys_score, chem_score;
        """
        expect = str(
            Program([VarDecl("math_score", ArrayType(5, FloatType())), VarDecl("phys_score", FloatType()),VarDecl("chem_score", FloatType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 303))

    def test_var_decl_4(self):
        ip = """
        int my_Arr[0], my_Arr[1], my_Arr[2];
        """
        expect = str(
            Program([VarDecl("my_Arr",ArrayType(0,IntType())),VarDecl("my_Arr",ArrayType(1,IntType())),VarDecl("my_Arr",ArrayType(2,IntType()))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 304))

    def test_var_decl_5(self):
        ip = """
        int i; float j; string k;
        """
        expect = str(
            Program([VarDecl("i", IntType()), VarDecl("j", FloatType()), VarDecl("k", StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 305))

    def test_var_decl_6(self):
        ip = """
        int a, b, c, d[4], e[5], f[6];
        """
        expect = str(
            Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(4,IntType())),VarDecl("e",ArrayType(5,IntType())),VarDecl("f",ArrayType(6,IntType()))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 306))

    def test_func_decl_1(self):
        ip = """
        void main(){}
        int main1(){}
        float main2(){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("main1"),[],IntType(),Block([])),FuncDecl(Id("main2"),[],FloatType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 307))

    def test_func_decl_2(self):
        ip = """
        float[] main1() {}
        boolean[] main2() {}
        """
        expect = str(
            Program([FuncDecl(Id("main1"),[],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("main2"),[],ArrayPointerType(BoolType()),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 308))

    def test_func_decl_3(self):
        ip = """
        void main(int a, int b, float c){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",FloatType())],VoidType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 309))

    def test_func_decl_4(self):
        ip = """
        int[] main(string a[], float b[], boolean c){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[VarDecl("a", ArrayPointerType(StringType())), VarDecl("b", ArrayPointerType(FloatType())),VarDecl("c", BoolType())], ArrayPointerType(IntType()), Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 310))

    def test_func_decl_5(self):
        ip = """
        boolean checksum(boolean etc, boolean check[])
        {
            \t
        }
        """
        expect = str(
            Program([FuncDecl(Id("checksum"),[VarDecl("etc",BoolType()),VarDecl("check",ArrayPointerType(BoolType()))],BoolType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 311))

    def test_program_1(self):
        ip = """
        int x, y, z;
        void main(){
            int x, y, z;
        }
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType())]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 312))

    def test_program_2(self):
        ip = """
        int x, y;
        void main(){
            //nothing in block
        }
        string z;
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([])),VarDecl("z",StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 313))

    def test_program_3(self):
        ip = """
        int x, y;
        void main(int x[], int y){
            //nothing in block
        }
        string z;
        int[] prime(string z[]){
            //nothing in block
        }
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),FuncDecl(Id("main"),[VarDecl("x",ArrayPointerType(IntType())),VarDecl("y",IntType())],VoidType(),Block([])),VarDecl("z",StringType()),FuncDecl(Id("prime"),[VarDecl("z",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 314))

    def test_if_and_block_1(self):
        ip = """
        void main(){
            if ( a && b )
                if( a || b )
                    a || b ;
            else
                a && b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),BinaryOp("||",Id("a"),Id("b")),BinaryOp("&&",Id("a"),Id("b"))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 315))

    def test_if_and_block_2(self):
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b )
                    a || b ;
            }
            else
                a && b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"), [], VoidType(), Block([If(BinaryOp("&&", Id("a"), Id("b")), Block([If(BinaryOp("||", Id("a"), Id("b")), BinaryOp("||", Id("a"), Id("b")))]), BinaryOp("&&", Id("a"), Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 316))

    def test_if_and_block_3(self):
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b ){a || b ;}
                else
                {}
            }
            else{a && b ;}
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),Block([If(BinaryOp("||",Id("a"),Id("b")),Block([BinaryOp("||",Id("a"),Id("b"))]),Block([]))]),Block([BinaryOp("&&",Id("a"),Id("b"))]))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 317))

    def test_if_and_block_4(self):
        ip = """
        void main(){
            if (a && b)
            if (a || b)
            if (a == b)
            {}
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),If(BinaryOp("==",Id("a"),Id("b")),Block([]))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 318))

    def test_if_and_block_5(self):
        ip = """
        int main(){
            if (a == b){
                if((a == b)){
                    if(((a == b))){ return 1; }
                    else{
                        return 0;
                    }
                }
            }
            else{
                if(a != b)
                {
                    return 0;
                }
                else
                    return 1;
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))]),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([Return(IntLiteral(0))]),Return(IntLiteral(1)))]))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 319))

    def test_dowhile_and_block_1(self):
        ip = """
        void main(){
            do {} {} {} {} {} {}
            {}
            while a == b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])],BinaryOp("==",Id("a"),Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 320))

    def test_dowhile_and_block_2(self):
        ip = """
        int[] main(){
        do {
            do {//\n} while ( a < 0);
        } while a == b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"), [], ArrayPointerType(IntType()),Block([Dowhile([Block([Dowhile([Block([])],BinaryOp("<",Id("a"),IntLiteral(0)))])],BinaryOp("==",Id("a"),Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 321))

    def test_dowhile_and_block_3(self):
        ip = """
        void main(){
            do {{{int i;}}} while b<0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Block([Block([VarDecl("i",IntType())])])])],BinaryOp("<", Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 322))

    def test_dowhile_and_block_4(self):
        ip = """
        void main(){
            do i = 5; while b<=0;
            do j = 5; while b>=0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(5))],BinaryOp("<=",Id("b"),IntLiteral(0))),Dowhile([BinaryOp("=",Id("j"),IntLiteral(5))],BinaryOp(">=",Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 323))

    def test_dowhile_and_block_5(self):
        ip = """
        void main(){
            do i =5; j = 5; k = 5; while b>=0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("j"),IntLiteral(5)),BinaryOp("=",Id("k"),IntLiteral(5))],BinaryOp(">=",Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 324))

    def test_dowhile_and_block_6(self):
        ip = """
        void main(){
        do do {{if(a){}}} while 5 == 0 ; while 5 >= 10 ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Block([Block([If(Id("a"),Block([]))])])],BinaryOp("==",IntLiteral(5),IntLiteral(0)))],BinaryOp(">=",IntLiteral(5),IntLiteral(10)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 325))

    def test_dowhile_and_block_7(self):
        ip = """
        void main(){
        do
            {int a;}
            a = 0;
            a = a + 1;
        while a != 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType())]),BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("!=",Id("a"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 326))

    def test_dowhile_and_block_8(self):
        ip = """
        void main(){
            int i[5];
            boolean check;
            do{
                int count;
                count = 0;
                if(count != 0)
                    break;
                count = count*count;
                {}
            } while count == 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  VarDecl('i', ArrayType(5, IntType())),
                                  VarDecl('check', BoolType()),
                                  Dowhile([Block([
                                      VarDecl('count', IntType()),
                                      BinaryOp('=', Id('count'), IntLiteral(0)),
                                      If(BinaryOp('!=', Id('count'), IntLiteral(0)),
                                         Break()
                                         ),
                                      BinaryOp('=', Id('count'), BinaryOp('*', Id('count'), Id('count'))),
                                      Block([

                                      ])
                                  ])],
                                      BinaryOp('==', Id('count'), IntLiteral(0))
                                  )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 327))

    def test_for_and_block_1(self):
        ip = """
        int main(){
            for (i = 0; i < alpha; i = i + 1){}
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('alpha')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([

                                      ])
                                      ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 328))

    def test_for_and_block_2(self):
        ip = """
        int main(){
            for (i = 0; i < alpha; i = i + 1){}
            for (i; j; k) {}
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('alpha')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([

                                      ])
                                      ),
                                  For(Id('i'),
                                      Id('j'),
                                      Id('k'),
                                      Block([

                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 329))

    def test_for_and_block_3(self):
        ip = """
        int main(){
            for (i = 1; j = 1; k = 1){
                i = i + 2;
                if ( i > j )
                    print(i);
                else
                    print(j);
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('=', Id('j'), IntLiteral(1)),
                                      BinaryOp('=', Id('k'), IntLiteral(1)),
                                      Block([
                                          BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(2))),
                                          If(BinaryOp('>', Id('i'), Id('j')),
                                             CallExpr(Id('print'), [Id('i')]),
                                             CallExpr(Id('print'), [Id('j')])
                                             )
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 330))

    def test_for_and_block_4(self):
        ip = """
        void main(){
            for(i = 0; i < MATRIX; i = i + 1)
            {
                    matA[i] = -rand % 2;
            }
            return;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('MATRIX')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', ArrayCell(Id('matA'), Id('i')),
                                                   BinaryOp('%', UnaryOp('-', Id('rand')), IntLiteral(2)))
                                      ])
                                      ),
                                  Return()
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 331))

    def test_for_and_block_5(self):
        ip = """
        void main(){
            for(changeA = 0; changeA < MATRIX/n_pros; changeA = changeA + 1)
            {
                for(i = 0; i < MATRIX; i = i + 1)
                {
                    matA[i] = rand % 2;
                }
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  For(BinaryOp('=', Id('changeA'), IntLiteral(0)),
                                      BinaryOp('<', Id('changeA'), BinaryOp('/', Id('MATRIX'), Id('n_pros'))),
                                      BinaryOp('=', Id('changeA'), BinaryOp('+', Id('changeA'), IntLiteral(1))),
                                      Block([
                                          For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                              BinaryOp('<', Id('i'), Id('MATRIX')),
                                              BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                              Block([
                                                  BinaryOp('=', ArrayCell(Id('matA'), Id('i')),
                                                           BinaryOp('%', Id('rand'), IntLiteral(2)))
                                              ])
                                              )
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 332))

    def test_for_and_block_6(self):
        ip = """
        boolean isPrime(int n)
        {
            // Corner case
            // Check from 2 to n-1
            int i;
            for (i = 2; i < n; i = i + 1)
                if (n % i == 0)
                    return false;
            return true;
        }
        """
        expect = str(
            Program([FuncDecl(Id('isPrime'),
                              [VarDecl('n', IntType())],
                              BoolType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(2)),
                                      BinaryOp('<', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      If(BinaryOp('==', BinaryOp('%', Id('n'), Id('i')), IntLiteral(0)),
                                         Return(BooleanLiteral(False))
                                         )
                                      ),
                                  Return(BooleanLiteral(True))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 333))

    def test_for_and_block_7(self):
        ip = """
        void printPrime(int n)
        {
            int i;
            for (i = 2; i <= n; i = i + 1) {
                if (isPrime(i))
                    print(i);
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('printPrime'),
                              [VarDecl('n', IntType())],
                              VoidType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(2)),
                                      BinaryOp('<=', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          If(CallExpr(Id('isPrime'), [Id('i')]),
                                             CallExpr(Id('print'), [Id('i')])
                                             )
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 334))

    def test_for_and_block_8(self):
        ip = """
        int main(){
            for (j = 0; j < c; j = j + 1)
                print("i"); // for
                print("i"); // main
                print("i"); // main
                print("i"); // main
                print("i"); // main
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('j'), IntLiteral(0)),
                                      BinaryOp('<', Id('j'), Id('c')),
                                      BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                      CallExpr(Id('print'), [StringLiteral('i')])
                                      ),
                                  CallExpr(Id('print'), [StringLiteral('i')]),
                                  CallExpr(Id('print'), [StringLiteral('i')]),
                                  CallExpr(Id('print'), [StringLiteral('i')]),
                                  CallExpr(Id('print'), [StringLiteral('i')])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 335))

    def test_stmt_1(self):
        ip = """
        int main() {
            int i;
            i = 20;
            if (i < 15)
                printf("i is smaller than 15");
            else
                printf("i is greater than 15");
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  BinaryOp('=', Id('i'), IntLiteral(20)),
                                  If(BinaryOp('<', Id('i'), IntLiteral(15)),
                                     CallExpr(Id('printf'), [StringLiteral('i is smaller than 15')]),
                                     CallExpr(Id('printf'), [StringLiteral('i is greater than 15')])
                                     ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 336))

    def test_stmt_2(self):
        ip = """
        void findElement(int arr[], int size, int key)
        {
            int i;
            // loop to traverse array and search for key
            for (i = 0; i < size; i = i + 1)
                if (arr[i] == key)
                    printf("Element found at position: %d", (i + 1));
        }
        """
        expect = str(
            Program([FuncDecl(Id('findElement'),
                              [VarDecl('arr', ArrayPointerType(IntType())),
                               VarDecl('size', IntType()),
                               VarDecl('key', IntType())],
                              VoidType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('size')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      If(BinaryOp('==', ArrayCell(Id('arr'), Id('i')), Id('key')),
                                         CallExpr(Id('printf'), [StringLiteral('Element found at position: %d'),
                                                                 BinaryOp('+', Id('i'), IntLiteral(1))])
                                         )
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 337))

    def test_stmt_3(self):
        ip = """
        int main() {
            // loop from 1 to 10
            int i;
            for (i = 1; i <= 10; i = i + 1) {
                if (i == 6)
                    continue;
                else
                    //
                    printf("%d ", i);
            }
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('<=', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          If(BinaryOp('==', Id('i'), IntLiteral(6)),
                                             Continue(),
                                             CallExpr(Id('printf'), [StringLiteral('%d '), Id('i')])
                                             )
                                      ])
                                      ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 338))

    def test_stmt_4(self):
        ip = """
        int main()
        {
            int i, j;
            do{
                j = 1;
                do{
                    j = j + 1;
                } while ( j <= 10 );
                i = i + 1;
            } while ( i <= 10 );
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  VarDecl('j', IntType()),
                                  Dowhile([Block([
                                      BinaryOp('=', Id('j'), IntLiteral(1)),
                                      Dowhile([Block([
                                          BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1)))
                                      ])],
                                          BinaryOp('<=', Id('j'), IntLiteral(10))
                                      ),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1)))
                                  ])],
                                      BinaryOp('<=', Id('i'), IntLiteral(10))
                                  ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 339))

    def test_stmt_5(self):
        ip = """
        int main(){
            int i;
            i = 1;
            do {
            int j;
            for (j=1; j<=i; j = j + 1)
            {
                Write(i + " ");
            }
                WriteLine();
                i = i + 1;
            }
            while (i<=5);
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  BinaryOp('=', Id('i'), IntLiteral(1)),
                                  Dowhile([Block([
                                      VarDecl('j', IntType()),
                                      For(BinaryOp('=', Id('j'), IntLiteral(1)),
                                          BinaryOp('<=', Id('j'), Id('i')),
                                          BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                          Block([
                                              CallExpr(Id('Write'), [BinaryOp('+', Id('i'), StringLiteral(' '))])
                                          ])
                                          ),
                                      CallExpr(Id('WriteLine'), []),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1)))
                                  ])],
                                      BinaryOp('<=', Id('i'), IntLiteral(5))
                                  )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 340))

    def test_stmt_6(self):
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                continue;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Continue()
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 341))

    def test_stmt_7(self):
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                j = 1;
                for(j = 0; j < 10 ; j = j + 1){
                int k;
                k = 1;
                }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      BinaryOp('=', Id('j'), IntLiteral(1))
                                      ),
                                  For(BinaryOp('=', Id('j'), IntLiteral(0)),
                                      BinaryOp('<', Id('j'), IntLiteral(10)),
                                      BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                      Block([
                                          VarDecl('k', IntType()),
                                          BinaryOp('=', Id('k'), IntLiteral(1))
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 342))

    def test_stmt_8(self):
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                j = 1; int j;
                for(j = 0; j < 10 ; j = j + 1){
                int k;
                k = 1;
                }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      BinaryOp('=', Id('j'), IntLiteral(1))
                                      ),
                                  VarDecl('j', IntType()),
                                  For(BinaryOp('=', Id('j'), IntLiteral(0)),
                                      BinaryOp('<', Id('j'), IntLiteral(10)),
                                      BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                      Block([
                                          VarDecl('k', IntType()),
                                          BinaryOp('=', Id('k'), IntLiteral(1))
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 343))

    def test_stmt_9(self):
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                if( i == 0)
            break ;
            else
                continue;
                int j;
                j = 10;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      If(BinaryOp('==', Id('i'), IntLiteral(0)),
                                         Break(),
                                         Continue()
                                         )
                                      ),
                                  VarDecl('j', IntType()),
                                  BinaryOp('=', Id('j'), IntLiteral(10))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 344))

    def test_stmt_10(self):
        ip = """
        void main() {
            if (a == b)
                if (c == d)
                    foo();
                else
                    foo();
            else
                foo();
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  If(BinaryOp('==', Id('a'), Id('b')),
                                     If(BinaryOp('==', Id('c'), Id('d')),
                                        CallExpr(Id('foo'), []),
                                        CallExpr(Id('foo'), [])
                                        ),
                                     CallExpr(Id('foo'), [])
                                     )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 345))

    def test_stmt_11(self):
        ip = """
        int main(int argc){
            int a;
            {
                int b;
                {
                    int c;
                }
            }
            return;
            return 0;
            return 0 + 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [VarDecl('argc', IntType())],
                              IntType(),
                              Block([
                                  VarDecl('a', IntType()),
                                  Block([
                                      VarDecl('b', IntType()),
                                      Block([
                                          VarDecl('c', IntType())
                                      ])
                                  ]),
                                  Return(),
                                  Return(IntLiteral(0)),
                                  Return(BinaryOp('+', IntLiteral(0), IntLiteral(0)))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 346))

    def test_stmt_12(self):
        ip = """
        int main(int argc){
            return;
            return a = a + 0;
            return a;
            return main;
            return "nothing";
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [VarDecl('argc', IntType())],
                              IntType(),
                              Block([
                                  Return(),
                                  Return(BinaryOp('=', Id('a'), BinaryOp('+', Id('a'), IntLiteral(0)))),
                                  Return(Id('a')),
                                  Return(Id('main')),
                                  Return(StringLiteral('nothing'))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 347))

    def test_stmt_13(self):
        ip = """
        int main(int argc){
            int argc;
            int argv[10];
            {
                if (argv[1] == argc){
                    return 0;
                }
                return 1;
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [VarDecl('argc', IntType())],
                              IntType(),
                              Block([
                                  VarDecl('argc', IntType()),
                                  VarDecl('argv', ArrayType(10, IntType())),
                                  Block([
                                      If(BinaryOp('==', ArrayCell(Id('argv'), IntLiteral(1)), Id('argc')),
                                         Block([
                                             Return(IntLiteral(0))
                                         ])
                                         ),
                                      Return(IntLiteral(1))
                                  ])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 348))

    def test_stmt_14(self):
        ip = """
        int main(int argc){
            int a, b, c; // variable declaration
            a=b=c=5; // assignment statement
            float f[5]; // variable declaration
            if ( a==b ) f[0] = 1.0; // if statement
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [VarDecl('argc', IntType())],
                              IntType(),
                              Block([
                                  VarDecl('a', IntType()),
                                  VarDecl('b', IntType()),
                                  VarDecl('c', IntType()),
                                  BinaryOp('=', Id('a'), BinaryOp('=', Id('b'), BinaryOp('=', Id('c'), IntLiteral(5)))),
                                  VarDecl('f', ArrayType(5, FloatType())),
                                  If(BinaryOp('==', Id('a'), Id('b')),
                                     BinaryOp('=', ArrayCell(Id('f'), IntLiteral(0)), FloatLiteral(1.0))
                                     )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 349))

    def test_expr_1(self):
        ip = """
        int main(){
            arr[5]; //pass
            (arr)[5]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), IntLiteral(5)),
                                  ArrayCell(Id('arr'), IntLiteral(5))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 350))

    def test_expr_2(self):
        ip = """
        int main(){
            foo()[5]; //pass
            (foo())[5]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(CallExpr(Id('foo'), []), IntLiteral(5)),
                                  ArrayCell(CallExpr(Id('foo'), []), IntLiteral(5))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 351))

    def test_expr_3(self):
        ip = """
        int main(){
            foo(2)[5]; //pass
            foo(1,2,3)[5]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(CallExpr(Id('foo'), [IntLiteral(2)]), IntLiteral(5)),
                                  ArrayCell(CallExpr(Id('foo'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                            IntLiteral(5))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 352))

    def test_expr_4(self):
        ip = """
        int main(){
            (foo(1,2,3))[5]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(CallExpr(Id('foo'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                            IntLiteral(5))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 353))

    def test_expr_5(self):
        ip = """
        int main(){
            func(1+2, a[5], a < 5)[5]; //pass
            func(func(1), a, a == b)[10]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(CallExpr(Id('func'), [BinaryOp('+', IntLiteral(1), IntLiteral(2)),ArrayCell(Id('a'), IntLiteral(5)),BinaryOp('<', Id('a'), IntLiteral(5))]), IntLiteral(5)),
                                  ArrayCell(CallExpr(Id('func'), [CallExpr(Id('func'), [IntLiteral(1)]), Id('a'), BinaryOp('==', Id('a'), Id('b'))]), IntLiteral(10))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 354))

    def test_expr_6(self):
        ip = """
        int main(){
            ((arr))[5]; //pass
            ((foo()))[5]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), IntLiteral(5)),
                                  ArrayCell(CallExpr(Id('foo'), []), IntLiteral(5))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 355))

    def test_expr_7(self):
        ip = """
        int main(){
            foo(2)[3+x] = a[b[2]] +3; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('=', ArrayCell(CallExpr(Id('foo'), [IntLiteral(2)]),BinaryOp('+', IntLiteral(3), Id('x'))),BinaryOp('+', ArrayCell(Id('a'), ArrayCell(Id('b'), IntLiteral(2))),IntLiteral(3)))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 356))

    def test_expr_8(self):
        ip = """
        void goo(float x[]) {
            float y[10];
            int z [10];
            foo(x) ;
            foo(y) ;
            foo(z) ;
        }
        """
        expect = str(
            Program([FuncDecl(Id('goo'),
                              [VarDecl('x', ArrayPointerType(FloatType()))],
                              VoidType(),
                              Block([
                                  VarDecl('y', ArrayType(10, FloatType())),
                                  VarDecl('z', ArrayType(10, IntType())),
                                  CallExpr(Id('foo'), [Id('x')]),
                                  CallExpr(Id('foo'), [Id('y')]),
                                  CallExpr(Id('foo'), [Id('z')])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 357))

    def test_expr_9(self):
        ip = """
        void goo(float x[]) {
            arr[func()]; //pass
            arr[func(1)]; //pass
            arr[func(1,2,3, another_arr[4])]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('goo'),
                              [VarDecl('x', ArrayPointerType(FloatType()))],
                              VoidType(),
                              Block([
                                  ArrayCell(Id('arr'), CallExpr(Id('func'), [])),
                                  ArrayCell(Id('arr'), CallExpr(Id('func'), [IntLiteral(1)])),
                                  ArrayCell(Id('arr'), CallExpr(Id('func'),[IntLiteral(1), IntLiteral(2), IntLiteral(3),ArrayCell(Id('another_arr'), IntLiteral(4))]))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 358))

    def test_expr_10(self):
        ip = """
        int main(){
            arr[(func())]; //pass
            arr[((func(1)))]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), CallExpr(Id('func'), [])),
                                  ArrayCell(Id('arr'), CallExpr(Id('func'), [IntLiteral(1)]))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 359))

    def test_expr_11(self):
        ip = """
        int main(){
            arr[arr[5]]; //pass
            arr1[arr2[arr3[5]]]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), ArrayCell(Id('arr'), IntLiteral(5))),
                                  ArrayCell(Id('arr1'), ArrayCell(Id('arr2'), ArrayCell(Id('arr3'), IntLiteral(5))))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 360))

    def test_expr_12(self):
        ip = """
        int main(){
            arr [ ( arr[5] ) ]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), ArrayCell(Id('arr'), IntLiteral(5)))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 361))

    def test_expr_13(self):
        ip = """
        int main(){
            arr[i]; //pass
            arr[1 + 2 - 3 * 4 / 5 % 6]; //pass
            arr[----------3]; //pass
            arr[ a = b ]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), Id('i')),
                                  ArrayCell(Id('arr'), BinaryOp('-', BinaryOp('+', IntLiteral(1), IntLiteral(2)),BinaryOp('%', BinaryOp('/', BinaryOp('*', IntLiteral(3),IntLiteral(4)),IntLiteral(5)), IntLiteral(6)))),
                                  ArrayCell(Id('arr'), UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',IntLiteral(3)))))))))))),
                                  ArrayCell(Id('arr'), BinaryOp('=', Id('a'), Id('b')))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 362))

    def test_expr_14(self):
        ip = """
        int main(){
            arr[(i)]; //pass
            arr[(1 + 2 - 3 * 4 / 5 % 6)]; //pass
            arr[ (a = b) ]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), Id('i')),
                                  ArrayCell(Id('arr'), BinaryOp('-', BinaryOp('+', IntLiteral(1), IntLiteral(2)),BinaryOp('%', BinaryOp('/', BinaryOp('*', IntLiteral(3),IntLiteral(4)),IntLiteral(5)), IntLiteral(6)))),
                                  ArrayCell(Id('arr'), BinaryOp('=', Id('a'), Id('b')))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 363))

    def test_expr_15(self):
        ip = """
        int main(){
            arr[((i))]; //pass
            arr[((a + b - c * d / e % f))]; //pass
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  ArrayCell(Id('arr'), Id('i')),
                                  ArrayCell(Id('arr'), BinaryOp('-', BinaryOp('+', Id('a'), Id('b')), BinaryOp('%',BinaryOp('/',BinaryOp('*',Id('c'),Id('d')),Id('e')),Id('f'))))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 364))

    def test_expr_16(self):
        ip = """
        int main(){
            func(1 + 2 - 3 * 4 / 5 % 6);
            func((1 + 2 - 3 * 4 / 5 % 6));
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('func'), [BinaryOp('-', BinaryOp('+', IntLiteral(1), IntLiteral(2)),BinaryOp('%', BinaryOp('/',BinaryOp('*', IntLiteral(3),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)))]),
                                  CallExpr(Id('func'), [BinaryOp('-', BinaryOp('+', IntLiteral(1), IntLiteral(2)),BinaryOp('%', BinaryOp('/',BinaryOp('*', IntLiteral(3),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)))])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 365))

    def test_expr_17(self):
        ip = """
        int main(){
            func(a < b, 1 >= b, a <= 2, 1 < 2);
            func(a || b && c, -a-b, !a && !b || !!c);
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('func'),[BinaryOp('<', Id('a'), Id('b')), BinaryOp('>=', IntLiteral(1), Id('b')),BinaryOp('<=', Id('a'), IntLiteral(2)),BinaryOp('<', IntLiteral(1), IntLiteral(2))]),
                                  CallExpr(Id('func'), [BinaryOp('||', Id('a'), BinaryOp('&&', Id('b'), Id('c'))),BinaryOp('-', UnaryOp('-', Id('a')), Id('b')), BinaryOp('||',BinaryOp('&&',UnaryOp('!',Id('a')),UnaryOp('!',Id('b'))),UnaryOp('!',UnaryOp('!',Id('c'))))])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 366))

    def test_expr_18(self):
        ip = """
        int main(){
            func(arr[num], arr[num + 1], arr[num + 2]);
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('func'), [ArrayCell(Id('arr'), Id('num')),
                                                        ArrayCell(Id('arr'), BinaryOp('+', Id('num'), IntLiteral(1))),
                                                        ArrayCell(Id('arr'), BinaryOp('+', Id('num'), IntLiteral(2)))])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 367))

    def test_expr_19(self):
        ip = """
        int main(){
            func(foo(1), foo(2), foo(3));
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('func'),[CallExpr(Id('foo'), [IntLiteral(1)]), CallExpr(Id('foo'), [IntLiteral(2)]),CallExpr(Id('foo'), [IntLiteral(3)])])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 368))

    def test_expr_20(self):
        ip = """
        int main(){
            func(foo(1), arr[5], i, a + 5, a < 5);
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('func'),[CallExpr(Id('foo'), [IntLiteral(1)]), ArrayCell(Id('arr'), IntLiteral(5)),Id('i'), BinaryOp('+', Id('a'), IntLiteral(5)),BinaryOp('<', Id('a'), IntLiteral(5))])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 369))

    def test_expr_21(self):
        ip = """
        int main(){
            a = 5;
            a = (5 + 5) - 5;
            a[5] = a * (5 / b);
            func(5)[--3] = --3;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('=', Id('a'), IntLiteral(5)),
                                  BinaryOp('=', Id('a'),BinaryOp('-', BinaryOp('+', IntLiteral(5), IntLiteral(5)), IntLiteral(5))),
                                  BinaryOp('=', ArrayCell(Id('a'), IntLiteral(5)),BinaryOp('*', Id('a'), BinaryOp('/', IntLiteral(5), Id('b')))),
                                  BinaryOp('=', ArrayCell(CallExpr(Id('func'), [IntLiteral(5)]),UnaryOp('-', UnaryOp('-', IntLiteral(3)))),UnaryOp('-', UnaryOp('-', IntLiteral(3))))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 370))

    def test_expr_22(self):
        ip = """
        int main(){
            a = arr[a+a] = func(a);
            a = b = c = 5 + (a + b) + c;
            a = b && c || d;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('=', Id('a'),BinaryOp('=', ArrayCell(Id('arr'), BinaryOp('+', Id('a'), Id('a'))),CallExpr(Id('func'), [Id('a')]))),
                                  BinaryOp('=', Id('a'), BinaryOp('=', Id('b'), BinaryOp('=', Id('c'), BinaryOp('+',BinaryOp('+',IntLiteral(5),BinaryOp('+',Id('a'),Id('b'))),Id('c'))))),
                                  BinaryOp('=', Id('a'), BinaryOp('||', BinaryOp('&&', Id('b'), Id('c')), Id('d')))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 371))

    def test_expr_23(self):
        ip = """
        int main(){
            (a > a) > 5;
            a == (a != b);
            (a >= ((b >= c) >= d));
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('>', BinaryOp('>', Id('a'), Id('a')), IntLiteral(5)),
                                  BinaryOp('==', Id('a'), BinaryOp('!=', Id('a'), Id('b'))),
                                  BinaryOp('>=', Id('a'), BinaryOp('>=', BinaryOp('>=', Id('b'), Id('c')), Id('d')))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 372))

    def test_expr_24(self):
        ip = """
        int main(){
            a = !(((--3 - 4) --5) -- 6 - 7 - 8);
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('=', Id('a'), UnaryOp('!', BinaryOp('-', BinaryOp('-', BinaryOp('-',BinaryOp('-',BinaryOp('-',UnaryOp('-',UnaryOp('-',IntLiteral(3))),IntLiteral(4)),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(6))),IntLiteral(7)),IntLiteral(8))))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 373))

    def test_all_program_1(self):
        ip = """
        int a;
        float b[3];
        int[] foo(int a, float b[]) {
            int c[3];
            if (a>0)
                foo(a-1, b);
            return c;
        }
        void foo(int a) {
            float f;
        }
        """
        expect = str(
            Program([VarDecl('a', IntType()),
                     VarDecl('b', ArrayType(3, FloatType())),
                     FuncDecl(Id('foo'),[VarDecl('a', IntType()),VarDecl('b', ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),
                              Block([VarDecl('c', ArrayType(3, IntType())),If(BinaryOp('>', Id('a'), IntLiteral(0)),CallExpr(Id('foo'), [BinaryOp('-', Id('a'), IntLiteral(1)), Id('b')])),Return(Id('c'))])),
                     FuncDecl(Id('foo'),[VarDecl('a', IntType())],VoidType(),
                              Block([VarDecl('f', FloatType())]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 374))

    def test_all_program_2(self):
        ip = """
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a + 3 ;
            if (i > 0) {
                int d;
                d = i + 3;
                putInt( d );
            }
            return i;
        }
        """
        expect = str(
            Program([FuncDecl(Id('foo'),
                              [VarDecl('a', IntType()),
                               VarDecl('b', ArrayPointerType(FloatType()))],
                              IntType(),
                              Block([
                                  VarDecl('c', BoolType()),
                                  VarDecl('i', IntType()),
                                  BinaryOp('=', Id('i'), BinaryOp('+', Id('a'), IntLiteral(3))),
                                  If(BinaryOp('>', Id('i'), IntLiteral(0)),
                                     Block([
                                         VarDecl('d', IntType()),
                                         BinaryOp('=', Id('d'), BinaryOp('+', Id('i'), IntLiteral(3))),
                                         CallExpr(Id('putInt'), [Id('d')])
                                     ])
                                     ),
                                  Return(Id('i'))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 375))

    def test_all_program_3(self):
        ip = """
        int i;
        int f() {
            return 200;
        }
        void main () {
            int main ;
            main = f() ;
            putIntLn( main ) ;
        }
        """
        expect = str(
            Program([VarDecl('i', IntType()),
                     FuncDecl(Id('f'),
                              [],
                              IntType(),
                              Block([
                                  Return(IntLiteral(200))
                              ])),
                     FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  VarDecl('main', IntType()),
                                  BinaryOp('=', Id('main'), CallExpr(Id('f'), [])),
                                  CallExpr(Id('putIntLn'), [Id('main')])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 376))

    def test_all_program_4(self):
        ip = """
        void main () {
            int main ;
            main = f() ;
            putIntLn( main ) ;
            {
                int i ;
                int main ;
                int f ;
                main = f = i = 100;
                putIntLn( i ) ;
                putIntLn( main ) ;
                putIntLn ( f ) ;
            }
            putIntLn( main ) ;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  VarDecl('main', IntType()),
                                  BinaryOp('=', Id('main'), CallExpr(Id('f'), [])),
                                  CallExpr(Id('putIntLn'), [Id('main')]),
                                  Block([
                                      VarDecl('i', IntType()),
                                      VarDecl('main', IntType()),
                                      VarDecl('f', IntType()),
                                      BinaryOp('=', Id('main'),
                                               BinaryOp('=', Id('f'), BinaryOp('=', Id('i'), IntLiteral(100)))),
                                      CallExpr(Id('putIntLn'), [Id('i')]),
                                      CallExpr(Id('putIntLn'), [Id('main')]),
                                      CallExpr(Id('putIntLn'), [Id('f')])
                                  ]),
                                  CallExpr(Id('putIntLn'), [Id('main')])
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 377))

    def test_all_program_5(self):
        ip = """
        int main() {
            // printf() displays the string inside quotation
            printf("Hello, World!");
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  CallExpr(Id('printf'), [StringLiteral('Hello, World!')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 378))

    def test_all_program_6(self):
        ip = """
        int main()
        {
            int number;
            //printf() displays the formatted output 
            printf("Enter an integer: ");

            //scanf() reads the formatted input and stores them
            //scanf("%d", &number);

            //printf() displays the formatted output
            printf("You entered: %d", number);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('number', IntType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter an integer: ')]),
                                  CallExpr(Id('printf'), [StringLiteral('You entered: %d'), Id('number')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 379))

    def test_all_program_7(self):
        ip = """
        int main()
        {
            float firstNumber, secondNumber, product;
            firstNumber = 90e-1;
            secondNumber = 85e-1;

            // Performs multiplication and stores the result in variable productOfTwoNumbers
            product = firstNumber * secondNumber;  
            // Result up to 2 decimal point is displayed using %.2lf
            printf("Product = %.2lf\\n", product);

            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('firstNumber', FloatType()),
                                  VarDecl('secondNumber', FloatType()),
                                  VarDecl('product', FloatType()),
                                  BinaryOp('=', Id('firstNumber'), FloatLiteral(9.0)),
                                  BinaryOp('=', Id('secondNumber'), FloatLiteral(8.5)),
                                  BinaryOp('=', Id('product'), BinaryOp('*', Id('firstNumber'), Id('secondNumber'))),
                                  CallExpr(Id('printf'), [StringLiteral('Product = %.2lf\\n'), Id('product')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 380))

    def test_all_program_8(self):
        ip = """
        int main()
        {
            int integerType;
            float floatType;

            // Sizeof operator is used to evaluate the size of a variable
            printf("Size of int: %ld bytes\\n",sizeof(integerType));
            printf("Size of float: %ld bytes\\n",sizeof(floatType));
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('integerType', IntType()),
                                  VarDecl('floatType', FloatType()),
                                  CallExpr(Id('printf'), [StringLiteral('Size of int: %ld bytes\\n'),
                                                          CallExpr(Id('sizeof'), [Id('integerType')])]),
                                  CallExpr(Id('printf'), [StringLiteral('Size of float: %ld bytes\\n'),
                                                          CallExpr(Id('sizeof'), [Id('floatType')])]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 381))

    def test_all_program_9(self):
        ip = """
        int main()
        {
            int number; number = 15;
            // True if the number is perfectly divisible by 2
            if(number % 2 == 0)
                printf("%d is even.", number);
            else
                printf("%d is odd.", number);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('number', IntType()),
                                  BinaryOp('=', Id('number'), IntLiteral(15)),
                                  If(BinaryOp('==', BinaryOp('%', Id('number'), IntLiteral(2)), IntLiteral(0)),
                                     CallExpr(Id('printf'), [StringLiteral('%d is even.'), Id('number')]),
                                     CallExpr(Id('printf'), [StringLiteral('%d is odd.'), Id('number')])
                                     ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 382))

    def test_all_program_10(self):
        ip = """
        int main()
        {
            float n1, n2, n3;
            n1 = n2 = n3 = 109.0e-1; 
            if (n1>=n2)
            {
                if(n1>=n3)
                    printf("%.2lf is the largest number.", n1);
                else
                    printf("%.2lf is the largest number.", n3);
            }
            else
            {
                if(n2>=n3)
                    printf("%.2lf is the largest number.", n2);
                else
                    printf("%.2lf is the largest number.",n3);
            }
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('n1', FloatType()),
                                  VarDecl('n2', FloatType()),
                                  VarDecl('n3', FloatType()),
                                  BinaryOp('=', Id('n1'),
                                           BinaryOp('=', Id('n2'), BinaryOp('=', Id('n3'), FloatLiteral(10.9)))),
                                  If(BinaryOp('>=', Id('n1'), Id('n2')),
                                     Block([
                                         If(BinaryOp('>=', Id('n1'), Id('n3')),
                                            CallExpr(Id('printf'),
                                                     [StringLiteral('%.2lf is the largest number.'), Id('n1')]),
                                            CallExpr(Id('printf'),
                                                     [StringLiteral('%.2lf is the largest number.'), Id('n3')])
                                            )
                                     ]),
                                     Block([
                                         If(BinaryOp('>=', Id('n2'), Id('n3')),
                                            CallExpr(Id('printf'),
                                                     [StringLiteral('%.2lf is the largest number.'), Id('n2')]),
                                            CallExpr(Id('printf'),
                                                     [StringLiteral('%.2lf is the largest number.'), Id('n3')])
                                            )
                                     ])
                                     ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 383))

    def test_all_program_11(self):
        ip = """
        int main()
        {
            int n, i, sum;
            sum = 0;
            n = 100;
            for(i = 1; i <= n; i = i + 1)
            {
                sum = sum + i;
            }
            printf("Sum = %d",sum);
            return 0;
        } 
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('n', IntType()),
                                  VarDecl('i', IntType()),
                                  VarDecl('sum', IntType()),
                                  BinaryOp('=', Id('sum'), IntLiteral(0)),
                                  BinaryOp('=', Id('n'), IntLiteral(100)),
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('<=', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', Id('sum'), BinaryOp('+', Id('sum'), Id('i')))
                                      ])
                                      ),
                                  CallExpr(Id('printf'), [StringLiteral('Sum = %d'), Id('sum')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 384))

    def test_all_program_12(self):
        ip = """
        int main()
        {
            int n, i;
            int factorial;
            factorial = 1;
            n = 19;
            printf("integer: %d \\n", n);
            // show error if the user enters a negative integer
            if (n < 0)
                printf("Error! Factorial of a negative number doesn't exist.");
            else
            {
                for(i=1; i<=n; i=i+1)
                {
                    factorial = factorial * i;
                }
                printf("Factorial of %d = %ld", n, factorial);
            }
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),[],IntType(),
                    Block([
                        VarDecl('n', IntType()),
                        VarDecl('i', IntType()),
                        VarDecl('factorial', IntType()),
                        BinaryOp('=', Id('factorial'), IntLiteral(1)),
                        BinaryOp('=', Id('n'), IntLiteral(19)),
                        CallExpr(Id('printf'), [StringLiteral('integer: %d \\n'), Id('n')]),
                        If(BinaryOp('<', Id('n'), IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral("Error! Factorial of a negative number doesn't exist.")]),
                            Block([
                                For(BinaryOp('=', Id('i'), IntLiteral(1)),BinaryOp('<=', Id('i'), Id('n')),BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),Block([BinaryOp('=', Id('factorial'),BinaryOp('*', Id('factorial'), Id('i')))])),
                                CallExpr(Id('printf'),[StringLiteral('Factorial of %d = %ld'), Id('n'),Id('factorial')])
                            ])),
                        Return(IntLiteral(0))
                        ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 385))

    def test_all_program_13(self):
        ip = """
        int main()
        {
            int i, n, t1, t2, nextTerm;
            t1 = 0; t2 = 1;
            N = 100;
            printf("Fibonacci Series: ");
            for (i = 1; i <= n; i = i + 1)
            {
                printf("%d, ", t1);
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0 + 0 + 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  VarDecl('n', IntType()),
                                  VarDecl('t1', IntType()),
                                  VarDecl('t2', IntType()),
                                  VarDecl('nextTerm', IntType()),
                                  BinaryOp('=', Id('t1'), IntLiteral(0)),
                                  BinaryOp('=', Id('t2'), IntLiteral(1)),
                                  BinaryOp('=', Id('N'), IntLiteral(100)),
                                  CallExpr(Id('printf'), [StringLiteral('Fibonacci Series: ')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('<=', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          CallExpr(Id('printf'), [StringLiteral('%d, '), Id('t1')]),
                                          BinaryOp('=', Id('nextTerm'), BinaryOp('+', Id('t1'), Id('t2'))),
                                          BinaryOp('=', Id('t1'), Id('t2')),
                                          BinaryOp('=', Id('t2'), Id('nextTerm'))
                                      ])
                                      ),
                                  Return(BinaryOp('+', BinaryOp('+', IntLiteral(0), IntLiteral(0)), IntLiteral(0)))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 386))

    def test_all_program_14(self):
        ip = """
        int main()
        {
            int number, i;
            printf("Factors of %d are: ", number);
            for(i=1; i <= number; i = i + 1)
            {
                if (number%i == 0)
                {
                    printf("%d ",i);
                }
            }
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('number', IntType()),
                                  VarDecl('i', IntType()),
                                  CallExpr(Id('printf'), [StringLiteral('Factors of %d are: '), Id('number')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('<=', Id('i'), Id('number')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          If(BinaryOp('==', BinaryOp('%', Id('number'), Id('i')), IntLiteral(0)),
                                             Block([
                                                 CallExpr(Id('printf'), [StringLiteral('%d '), Id('i')])
                                             ])
                                             )
                                      ])
                                      ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 387))

    def test_all_program_15(self):
        ip = """
        int checkPrimeNumber(int n)
        {
            int j, flag;
            flag = 1;
            for(j = 2; j <= n/2; j = j + 1)
            {
                if (n%j == 0)
                {
                    flag =0 ;
                    break;
                }
            }
            return flag;
        }
        """
        expect = str(
            Program([FuncDecl(Id('checkPrimeNumber'),
                              [VarDecl('n', IntType())],
                              IntType(),
                              Block([
                                  VarDecl('j', IntType()),
                                  VarDecl('flag', IntType()),
                                  BinaryOp('=', Id('flag'), IntLiteral(1)),
                                  For(BinaryOp('=', Id('j'), IntLiteral(2)),
                                      BinaryOp('<=', Id('j'), BinaryOp('/', Id('n'), IntLiteral(2))),
                                      BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                      Block([
                                          If(BinaryOp('==', BinaryOp('%', Id('n'), Id('j')), IntLiteral(0)),
                                             Block([
                                                 BinaryOp('=', Id('flag'), IntLiteral(0)),
                                                 Break()
                                             ])
                                             )
                                      ])
                                      ),
                                  Return(Id('flag'))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 388))

    def test_all_program_16(self):
        ip = """
        int main()
        {
            int n;
            printf("Enter a positive integer: ");
            n = 20;
            printf("Factorial of %d = %ld", n, multiplyNumbers(n));
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('n', IntType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter a positive integer: ')]),
                                  BinaryOp('=', Id('n'), IntLiteral(20)),
                                  CallExpr(Id('printf'), [StringLiteral('Factorial of %d = %ld'), Id('n'),
                                                          CallExpr(Id('multiplyNumbers'), [Id('n')])]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 389))

    def test_all_program_17(self):
        ip = """
        int multiplyNumbers(int n)
        {
            if (n >= 1)
                return n*multiplyNumbers(n-1);
            else
                return 1;
        }
        """
        expect = str(
            Program([FuncDecl(Id('multiplyNumbers'),
                              [VarDecl('n', IntType())],
                              IntType(),
                              Block([
                                  If(BinaryOp('>=', Id('n'), IntLiteral(1)),
                                     Return(BinaryOp('*', Id('n'), CallExpr(Id('multiplyNumbers'),
                                                                            [BinaryOp('-', Id('n'), IntLiteral(1))]))),
                                     Return(IntLiteral(1))
                                     )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 390))

    def test_all_program_18(self):
        ip = """
        int main()
        {
            int i, n;
            float arr[100];
            printf("Enter total number of elements(1 to 100): ");
            n = 100;
            printf("\\n");
            // Stores number entered by the user
            for(i = 0; i < n; i = i + 1)
            {
                arr[i] = rand() ;
            }
            // Loop to store largest number to arr[0]
            for(i = 1; i < n; i = i + 1)
            {
                // Change < to > if you want to find the smallest element
                if(arr[0] < arr[i])
                    arr[0] = arr[i];
            }
            printf("Largest element = %.2f", arr[0]);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  VarDecl('n', IntType()),
                                  VarDecl('arr', ArrayType(100, FloatType())),
                                  CallExpr(Id('printf'), [StringLiteral('Enter total number of elements(1 to 100): ')]),
                                  BinaryOp('=', Id('n'), IntLiteral(100)),
                                  CallExpr(Id('printf'), [StringLiteral('\\n')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', ArrayCell(Id('arr'), Id('i')), CallExpr(Id('rand'), []))
                                      ])
                                      ),
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('<', Id('i'), Id('n')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          If(BinaryOp('<', ArrayCell(Id('arr'), IntLiteral(0)),
                                                      ArrayCell(Id('arr'), Id('i'))),
                                             BinaryOp('=', ArrayCell(Id('arr'), IntLiteral(0)),
                                                      ArrayCell(Id('arr'), Id('i')))
                                             )
                                      ])
                                      ),
                                  CallExpr(Id('printf'), [StringLiteral('Largest element = %.2f'),
                                                          ArrayCell(Id('arr'), IntLiteral(0))]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 391))

    def test_all_program_19(self):
        ip = """
        float calculateSD(float data[])
        {
            float sum, mean, standardDeviation;
            sum = 0.0;
            standardDeviation = 0.0;
            int i;
            for(i=0; i<10; i=i+1)
            {
                sum = sum + data[i];
            }
            mean = sum/10;
            for(i = 0; i < 10; i = i + 1)
            standardDeviation = standardDeviation + pow(data[i] - mean, 2);
            return sqrt(standardDeviation/10);
        }
        """
        expect = str(
            Program([FuncDecl(Id('calculateSD'),
                              [VarDecl('data', ArrayPointerType(FloatType()))],
                              FloatType(),
                              Block([
                                  VarDecl('sum', FloatType()),
                                  VarDecl('mean', FloatType()),
                                  VarDecl('standardDeviation', FloatType()),
                                  BinaryOp('=', Id('sum'), FloatLiteral(0.0)),
                                  BinaryOp('=', Id('standardDeviation'), FloatLiteral(0.0)),
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', Id('sum'),
                                                   BinaryOp('+', Id('sum'), ArrayCell(Id('data'), Id('i'))))
                                      ])
                                      ),
                                  BinaryOp('=', Id('mean'), BinaryOp('/', Id('sum'), IntLiteral(10))),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), IntLiteral(10)),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      BinaryOp('=', Id('standardDeviation'), BinaryOp('+', Id('standardDeviation'),CallExpr(Id('pow'), [BinaryOp('-',ArrayCell(Id('data'),Id('i')),Id('mean')),IntLiteral(2)])))
                                      ),
                                  Return(CallExpr(Id('sqrt'), [BinaryOp('/', Id('standardDeviation'), IntLiteral(10))]))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 392))

    def test_all_program_20(self):
        ip = """
        int main()
        {
            string str;
            int i, frequency; frequency = 0;
            printf("Enter a string: ");
            gets(str);
            for(i = 0; str[i] != ""; i = i + 1)
            {
                if("a" == str[i])
                    frequency = frequency + 1;
            }
            printf("Frequency of %c = %d", "a", frequency);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('str', StringType()),
                                  VarDecl('i', IntType()),
                                  VarDecl('frequency', IntType()),
                                  BinaryOp('=', Id('frequency'), IntLiteral(0)),
                                  CallExpr(Id('printf'), [StringLiteral('Enter a string: ')]),
                                  CallExpr(Id('gets'), [Id('str')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('!=', ArrayCell(Id('str'), Id('i')), StringLiteral('')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          If(BinaryOp('==', StringLiteral('a'), ArrayCell(Id('str'), Id('i'))),
                                             BinaryOp('=', Id('frequency'),
                                                      BinaryOp('+', Id('frequency'), IntLiteral(1)))
                                             )
                                      ])
                                      ),
                                  CallExpr(Id('printf'), [StringLiteral('Frequency of %c = %d'), StringLiteral('a'),
                                                          Id('frequency')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 393))

    def test_all_program_21(self):
        ip = """
        int main()
        {
            string s;
            int i;
            printf("Enter a string: ");
            gets(s);
            for(i = 0; s[i] != ""; i = i + 1)
                printf("Length of string: %d", i);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('s', StringType()),
                                  VarDecl('i', IntType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter a string: ')]),
                                  CallExpr(Id('gets'), [Id('s')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('!=', ArrayCell(Id('s'), Id('i')), StringLiteral('')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      CallExpr(Id('printf'), [StringLiteral('Length of string: %d'), Id('i')])
                                      ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 394))

    def test_all_program_22(self):
        ip = """
        int main()
        {
            string s1, s2, i;
            printf("Enter string s1: ");
            gets(s1);
            for(i = 0; s1[i] != ""; i = i + 1)
            {
                s2[i] = s1[i];
            }
            s2[i] = "";
            printf("String s2: %s", s2);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('s1', StringType()),
                                  VarDecl('s2', StringType()),
                                  VarDecl('i', StringType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter string s1: ')]),
                                  CallExpr(Id('gets'), [Id('s1')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('!=', ArrayCell(Id('s1'), Id('i')), StringLiteral('')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', ArrayCell(Id('s2'), Id('i')), ArrayCell(Id('s1'), Id('i')))
                                      ])
                                      ),
                                  BinaryOp('=', ArrayCell(Id('s2'), Id('i')), StringLiteral('')),
                                  CallExpr(Id('printf'), [StringLiteral('String s2: %s'), Id('s2')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 395))

    def test_all_program_23(self):
        ip = """
        int main()
        {
            string s1, s2, i, j;
            printf("Enter first string: ");
            gets(s1);
            printf("Enter second string: ");
            gets(s2);
            // calculate the length of string s1
            // and store it in i
            for(i = 0; s1[i] != ""; i = i + 1)
                for(j = 0; s2[j] != ""; j = j + 1)
                {
                    s1[i] = s2[j];
                }
            s1[i] = "";
            printf("After concatenation: %s", s1);
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('s1', StringType()),
                                  VarDecl('s2', StringType()),
                                  VarDecl('i', StringType()),
                                  VarDecl('j', StringType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter first string: ')]),
                                  CallExpr(Id('gets'), [Id('s1')]),
                                  CallExpr(Id('printf'), [StringLiteral('Enter second string: ')]),
                                  CallExpr(Id('gets'), [Id('s2')]),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('!=', ArrayCell(Id('s1'), Id('i')), StringLiteral('')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      For(BinaryOp('=', Id('j'), IntLiteral(0)),
                                          BinaryOp('!=', ArrayCell(Id('s2'), Id('j')), StringLiteral('')),
                                          BinaryOp('=', Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                          Block([
                                              BinaryOp('=', ArrayCell(Id('s1'), Id('i')), ArrayCell(Id('s2'), Id('j')))
                                          ])
                                          )
                                      ),
                                  BinaryOp('=', ArrayCell(Id('s1'), Id('i')), StringLiteral('')),
                                  CallExpr(Id('printf'), [StringLiteral('After concatenation: %s'), Id('s1')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 396))

    def test_all_program_24(self):
        ip = """
        int hcf(int n1, int n2)
        {
            if (n2 != 0)
                return hcf(n2, n1%n2);
            else 
                return n1;
        }
        int main()
        {
            int n1, n2;
            printf("Enter two positive integers: ");
            n1 = 8; n2 = 73;
            printf("G.C.D of %d and %d is %d.", n1, n2, hcf(n1,n2));
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('hcf'),
                              [VarDecl('n1', IntType()),
                               VarDecl('n2', IntType())],
                              IntType(),
                              Block([
                                  If(BinaryOp('!=', Id('n2'), IntLiteral(0)),
                                     Return(CallExpr(Id('hcf'), [Id('n2'), BinaryOp('%', Id('n1'), Id('n2'))])),
                                     Return(Id('n1'))
                                     )
                              ])),
                     FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('n1', IntType()),
                                  VarDecl('n2', IntType()),
                                  CallExpr(Id('printf'), [StringLiteral('Enter two positive integers: ')]),
                                  BinaryOp('=', Id('n1'), IntLiteral(8)),
                                  BinaryOp('=', Id('n2'), IntLiteral(73)),
                                  CallExpr(Id('printf'),
                                           [StringLiteral('G.C.D of %d and %d is %d.'), Id('n1'), Id('n2'),
                                            CallExpr(Id('hcf'), [Id('n1'), Id('n2')])]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 397))

    def test_all_program_25(self):
        ip = """
        int main() 
        { 
            // Calculate the time taken by fun() 
            // clock_t t;
            t = clock(); 
            fun(); 
            t = clock() - t; 
            float time_taken;
            time_taken = (t/CLOCKS_PER_SEC); // in seconds 

            printf("fun() took %f seconds to execute \\n", time_taken); 
            return 0;
        } 
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  BinaryOp('=', Id('t'), CallExpr(Id('clock'), [])),
                                  CallExpr(Id('fun'), []),
                                  BinaryOp('=', Id('t'), BinaryOp('-', CallExpr(Id('clock'), []), Id('t'))),
                                  VarDecl('time_taken', FloatType()),
                                  BinaryOp('=', Id('time_taken'), BinaryOp('/', Id('t'), Id('CLOCKS_PER_SEC'))),
                                  CallExpr(Id('printf'),
                                           [StringLiteral('fun() took %f seconds to execute \\n'), Id('time_taken')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 398))

    def test_all_program_26(self):
        ip = """
        void printRandoms(int lower, int upper, int count)
        {
            int i;
            for (i = 0; i < count; i = i + 1) { 
                int num;
                num = rand() % (upper - lower + 1) + lower; 
                printf("%d ", num);
            }
        }  
        """
        expect = str(
            Program([FuncDecl(Id('printRandoms'),
                              [VarDecl('lower', IntType()),
                               VarDecl('upper', IntType()),
                               VarDecl('count', IntType())],
                              VoidType(),
                              Block([
                                  VarDecl('i', IntType()),
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('count')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          VarDecl('num', IntType()),
                                          BinaryOp('=', Id('num'), BinaryOp('+', BinaryOp('%', CallExpr(Id('rand'), []),BinaryOp('+', BinaryOp('-',Id('upper'),Id('lower')),IntLiteral(1))),Id('lower'))),
                                          CallExpr(Id('printf'), [StringLiteral('%d '), Id('num')])
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 399))

    def test_all_program_27(self):
        ip = """
        int main() 
        {
            int lower, upper, count;
            lower = 5; upper = 7; count = 1;  
            // Use current time as 
            // seed for random generator 
            srand(time(0));
            printRandoms(lower, upper, count);  
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  VarDecl('lower', IntType()),
                                  VarDecl('upper', IntType()),
                                  VarDecl('count', IntType()),
                                  BinaryOp('=', Id('lower'), IntLiteral(5)),
                                  BinaryOp('=', Id('upper'), IntLiteral(7)),
                                  BinaryOp('=', Id('count'), IntLiteral(1)),
                                  CallExpr(Id('srand'), [CallExpr(Id('time'), [IntLiteral(0)])]),
                                  CallExpr(Id('printRandoms'), [Id('lower'), Id('upper'), Id('count')]),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 400))