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
                        if (a = b)  
                            if (a = x) 
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
                            if (a = x) 
                                b = y;
                            else
                                c = z;
                        else
                    }"""
        expect = "Error on line 9 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test212(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    # def test(self):
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,2))

    # def test(self):
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,2))

    # def test(self):
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,2))

    # def test(self):
        # inp = """void foo ( int i ) {
        #             int i,j,k[5];
        #             // ABC XYZ
        #         }
        #         void main() {
        #             int abc;
        #             continue;
        #             putInt(i);
        #         }
        #         """
        # expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,2))