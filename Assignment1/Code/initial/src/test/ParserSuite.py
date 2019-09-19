import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test204(self):
        input = """ int main() {else return 0;}"""
        expect = "Error on line 1 col 13: else"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test205(self):
        input = """ int a, b, c, d[5];
                    float f;
                    string f;
                    boolean flag;
                 """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test206(self):
        input = """int main() {
            if (a == b) c = d;
            else c = e;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test207(self):
        input = """int main() {
            if (a == b) c = d;
            else c = e
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test208(self):
        input = """ void foo(int x, int y, float z, string s, int a[]) {
            x = y + c;
            a[5] = z + x;
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test209(self):
        input = """ void foo(int x, int y, float z, string s, int a[7]) {
            x = y + c;
            a[5] = z + x;
        } """
        expect = "Error on line 1 col 49: 7"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test210(self):
        input = """int x, y, z, d;
                    float foo(int a, int b) {
                        if (a == b)  
                            if (a == x) 
                                b = y;
                            else
                                c = z;
                        else
                            c = d;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test211(self):
        input = """int x, y, z, d;
                    float foo(int a, int b) {
                        if (a = b)  
                            if (a == x) 
                                b == y;
                            else
                                c = z;
                        else
                    }"""
        expect = "Error on line 9 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test212(self):
        input = """ float foo(int a, int b) {
                        if (a == b)  
                                b = y;
                            else
                                c = z;
                        else
                    }"""
        expect = "Error on line 6 col 24: else"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test213(self):
        input = """int func(int par1, float par2){
                        do a = 1; while a = 1;
                        return a = 1;
                    }
                    void main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test214(self):
        input = """int func(int a){
                        do a; while a;
                        return a = 1;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test215(self):
        input = """abc() {x = y + 1}"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test216(self):
        input = """abc() {x; x = y + 1;}"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test217(self): 
        input = """int a, b[];"""
        expect = "Error on line 1 col 9: ]"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test218(self):
        input = """void foo ( int i ) {
                    int i,j,k[5];
                    // ABC XYZ
                }
                void main() {
                    /*trucly*/
                    int abc;
                    continue;
                    res(i);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test219(self):
        input = """ boolean OK(int a) {return true;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))


    def test220(self):
        input = """boolean OK(int a) {return true; a(a);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test221(self):
        input = """ int foo() {
            x = 1;
            y = x + 2;
            if (a < b && b > c || d >= e || e <= f) a = e;
            else a = c;
            return foo();
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test222(self):
        input = """ int foo() {
            if (a < b && b > c || d >= e || e <= f || a != x) a = e;
            return int;
        } """
        expect = "Error on line 3 col 19: int"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test223(self):
        input = "int func(void x){}"
        expect = "Error on line 1 col 9: void"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test224(self):
        input = """void[] func(boolean abc, float xyz) {
                    int x1;
                    float x2;
                }"""
        expect = "Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test225(self):
        input = """boolean[] func(boolean abc, float xyz) {
                    float x;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test226(self):
        input = """ int can11 (int TL) {
            int i;
            for (i = 0; i < n; i = i + 1) TL = TL + 1;
            if (TL != oo) can11(TL);
            else break;
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))


    def test227(self):
        input = """ int a = a + 1; """
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test228(self):
        input = """void foo () {
                    int i, j, k[5];
                    float arr[5];
                    i = (j + i) /(j + k[arr[1]]) + 1999;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test229(self):
        input = """void foo () {
                    int i, j, k[5];
                    float arr[5];
                    i = (j + i) /(j + k[arr[1]]) + 1999;"""
        expect = "Error on line 4 col 56: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test230(self):
        input = """int foo() {
                if (a) int i;
            }"""
        expect = "Error on line 2 col 23: int"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test231(self):
        input = """ int cal(int a, int b, int c) {
                        a = (b + c % a /b - c * a) - e;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test232(self):
        input = """ int cal(int a, int b, int c) {
                        a = (b + c % a /b - c * a) - e;
                        a = a ^ b + d;
                    }"""
        expect = "^"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test233(self):
        input = """/*NGUYEN THI TRUC LY*/
                    // truclybk.cs@gmail.com"""
        expect = "Error on line 2 col 44: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test234(self):
        input = """/*NGUYEN THI TRUC LY*/
                    // truclybk.cs@gmail.com
                    int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test235(self):
        input = """ int tl;
                    /*NGUYEN THI TRUC LY*/// truclybk.cs@gmail.com
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test236(self):
        input = """ int cal(int a, int b, int c) {
                        a = (b + c % a /b - c * a) - e;
                        a = b = c = 10;
                        res =((a * b) / d + (f % 7) - 4);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test237(self):
        input = """ int cal(int a, int b, int c) {
                        res =((a * b) / d + (f % 7 - 4);
                    }"""
        expect = "Error on line 2 col 55: ;"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test238(self):
        input = """ int cal(int a, int b, int c) {
                        res = !((a * b) / d + (-f % 7 - 4));
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test239(self):
        input = """ int cal(int a, int b, int c) {
                        res != ((a * b) / d ) && (-f % 7 - 4);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test240(self):
        input = """ int cal(int a) {
                        return;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    # def test(self):
    #     input = """ """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,)