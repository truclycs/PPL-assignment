import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # test simple program _ 20 test
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_simple_program_2(self):
        input = """void hello(int a, float b)"""
        expect = "Error on line 1 col 26: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_simple_program_3(self):
        input = """float hello(int 0.2a, float b){}"""
        expect = "Error on line 1 col 16: 0.2"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_simple_program_4(self):
        input = """boolean hell_o0.2(int 0.2a, float b){}"""
        expect = "Error on line 1 col 15: .2"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_simple_program_5(self):
        input = """void ndhnam(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_simple_program_6(self):
        input = """void ndhnam(){}
        int main(){
            int a,b,c, d;
            a = b = c = 10;
            float f[2];
            if (a == b) f[2] = .1e9;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_simple_program_7(self):
        input = """boolean True(){
            int[] nam;
            return True();
        }"""
        expect = "Error on line 2 col 15: ["
        self.assertTrue(TestParser.checkParser(input,expect, 207))
    def test_simple_program_8(self):
        input = """
                void main(){
                    int * a;
                }"""
        expect = """Error on line 3 col 24: *"""
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_simple_program_9(self):
        input = """ """
        expect = """Error on line 1 col 1: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_simple_program_10(self):
        input = """int[] void(string hello){}  """
        expect = """Error on line 1 col 6: void"""
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_simple_program_11(self):
        input = """int main(){void error[6]}"""
        expect = """Error on line 1 col 11: void"""
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_simple_program_12(self):
        input = """string STR123(){string STR[0123456]}"""
        expect = """Error on line 1 col 35: }"""
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_simple_program_13(self):
        input = """boolean TRUEORFALSE(boolean True){True = false;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_simple_program_14(self):
        input = """in thisiswrongtest14(){}"""
        expect = """Error on line 1 col 0: in"""
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_simple_program_15(self):
        input = """float main()}"""
        expect = """Error on line 1 col 12: }"""
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_simple_program_16(self):
        input = """string main(){;}"""
        expect = """Error on line 1 col 14: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_simple_program_17(self):
        input = """void void hello(){}"""
        expect = """Error on line 1 col 5: void"""
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_simple_program_18(self):
        input = """void Hello Name(){int a[3]}"""
        expect = """Error on line 1 col 11: Name"""
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_simplie_program_19(self):
        input = """string main(string main){a = 5;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_simple_program_20(self):
        input = """string Ha_Nam(string _30121999){string Hello; Hello = "Happy birthday!" + 30 + 12 + 1999;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,220))


    # test more complex program _ 20 test
    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_more_complex_program_2(self):
        """more complex program"""
        input = """int main(){
        int a;
        a = 2 + 2;
        if ( a != 4 )
            return;
        else
             a = 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_more_complex_program_3(self):
        input = """
        int main(){
            int a,b,c, d;
            a = b = c = 10;
            float foo[5];
            if (a == b) foo(2)[n[2]] = .1e9;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_more_complex_program_4(self):
        input = """
        int[] foo(float a, boolean b[]){
        int c[9];
        if (b != false){
            c[10] = 9;
        }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_more_complex_program_5(self):
        input = """
        int[] a(){}
        boolean b(){}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_more_complex_program_6(self):
        input = """void foo ( int i ) {int child_of_foo (floatf) //ERROR}"""
        expect = """Error on line 1 col 37: ("""
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_more_complex_program_7(self):
        input = """void feeder(string player){
            while(true){
                player = "why you always feed," + player + "?";
            }
        }"""
        expect = """Error on line 2 col 12: while"""
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_more_complex_program_8(self):
        input = """void feeder(string player){
            int i;
            i = 0;
            do
                i = i + 1;
                player = "why you always feed," + player + "?";
            while i <= 3;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_more_complex_program_9(self):
        input = """int main(int a[]){
            int i;
            for (i = 0; i < 5; i = i + 1)
                ok();
            return ok();
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_more_complex_program_10(self):
        input = """float fooo(fooo(foooo(foooo))){
            int a[];
            b = b[] + d[];
        }"""
        expect = """Error on line 1 col 11: fooo"""
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_more_complex_program_11(self):
        input = """int main(){a[5] = b[] + c[10];}"""
        expect = """Error on line 1 col 20: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_more_complex_program_12(self):
        input = """int main(){
        do
            int nam;
            nam[9517538624] = float;
            break;
            return -1;
        while EE < 0.12354;
        }"""
        expect = """Error on line 3 col 12: int"""
        self.assertTrue((TestParser.checkParser(input,expect,232)))
    def test_more_complex_program_13(self):
        input = """int main(int a[]){
        for(a; a < (5 + 6)[5];i = i + 2)
            a[951]*5 = 8 && 2;
            a = 5;
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,233)))
    def test_more_complex_program_14(self):
        input = """int main(int a[]){
        for(a; a < (5 + 6)[5];i = i + 2)
            if(i == 5) return true; else return hello(a[b]);
            a = 5;
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,234)))
    def test_more_complex_program_15(self):
        input = """int main(int a[]){
        for(a; a < (5 + 6)[5];i = i + 2)
            if(i == 5) return true; else return hello(a[b]);
            a = 5;
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,235)))
    def test_more_complex_program_16(self):
        input = """int[] main(int a[]){
            else return hello(a[b]);
            a = 5;
        }"""
        expect = """Error on line 2 col 12: else"""
        self.assertTrue((TestParser.checkParser(input,expect,236)))
    def test_more_complex_program_17(self):
        input = """int main(int a[]){
        return;
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,237)))
    def test_more_complex_program_18(self):
        input = """int main(int a[], float ok, void ok, string s = ""){
        break;
        }"""
        expect = """Error on line 1 col 28: void"""
        self.assertTrue((TestParser.checkParser(input,expect,238)))
    def test_more_complex_program_19(self):
        input = """int main(string a){
        this == b * 5 = a = main(foo, a, b, f, d, h);
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,239)))
    def test_more_complex_program_20(self):
        input = """int main(string a){
        this / a = main(foo, a, b, f, d, h);
        }"""
        expect = """successful"""
        self.assertTrue((TestParser.checkParser(input,expect,240)))

    # test wrong miss close 20 test
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_wrong_miss_close_2(self):
        """Miss ] int main( {}"""
        input = """int a[2;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_wrong_miss_close_3(self):
        """Miss ] int main( {}"""
        input = """if"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_wrong_miss_close_4(self):
        input = """float nam[;]{}"""
        expect = "Error on line 1 col 10: ;"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_wrong_miss_close_5(self):
        input = """float nam[](int a){}"""
        expect = "Error on line 1 col 11: ("
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_wrong_miss_close_6(self):
        input = """float nam(){float f[];}"""
        expect = "Error on line 1 col 20: ]"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_wrong_miss_close_7(self):
        input = """float nam(){
        float f[5] = {0.215; 0.625}
        }"""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_wrong_miss_close_8(self):
        input = """float nam(){
        float1 = {0.25, 0.5}
        }"""
        expect = """Error on line 2 col 17: {"""
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_wrong_miss_close_9(self):
        input = """float nam(){
        float1 = (true || flase)*("ok");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_wrong_miss_close_10(self):
        input = """void nam(int ques[5]){
        1.e-2 = (true || false)*("ok");
        }"""
        expect = """Error on line 1 col 18: 5"""
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_wrong_miss_close_11(self):
        input = """void hello(int hello, float hello, string snsnsn[])"""
        expect = """Error on line 1 col 51: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_wrong_miss_close_12(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            helo = "\\n";
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_wrong_miss_close_13(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            helo = "\\rrrrrrrrrrrrrrrrrr";
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_wrong_miss_close_14(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            if (helo == 5)
                if (ok) return;
                else ok = 8;
            else pass;
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_wrong_miss_close_15(self):
        input = """void hello(int hello, float hello string snsnsn[])
        {
            if (helo == 5)
                if (ok) return;
                else ok = 8;
            else pass;
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = """Error on line 1 col 34: string"""
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_wrong_miss_close_16(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            if (helo == 5) doit()[5];
                if (ok) return;
                else ok = 8;
            else pass;
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = """Error on line 6 col 12: else"""
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_wrong_miss_close_17(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            if (helo == 5) doit()[5];
                if (ok) if(i,k = 5) i;;
                else ok = 8;
            helo(helo(helo(helo(helo, ola))));
        }"""
        expect = """Error on line 4 col 28: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_wrong_miss_close_18(self):
        input = """void hello(int hello, float hello, string snsnsn[])
        {
            if (helo == 5) doit()[5];
                if (ok) if(k = 5) i;;
                else ok = 8;
            helo(helo(helo(helo(helo, ola))));
        }
        int main(){}"""
        expect = """Error on line 4 col 36: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_wrong_miss_clone_19(self):
        input = """void Void()
        int main(){}
        string String(string ____){_;}"""
        expect = """Error on line 2 col 8: int"""
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_wrong_miss_clone_20(self):
        input = """void Void(){}
        int main(){}
        string String(string ____){_;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,260))

    # test more all program _ 20 test
    def test_more_all_program(self):
        input = """void Add(int a, int b){
        c = a + b = b / a = a * a = a / b;
        int c,d,f,g;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_more_all_program_2(self):
        input = """void Add(int a, int b){
        c = a + b = b / a = a * a = a / b;
        int c,d,f,g;
        }
        int Main(int arr[]){
        arr = .1e-5 + 1.e7 * 8;
        Add(5,6);
        return;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_more_all_program_3(self):
        input = """void Add(int a, int b){
        c = a + b = b / a = a * a = a / b = true = false;
        float floatt c,d,f,g;
        break;
        }
        int Main(int arr[]){
        arr = .1e-5 + 1.e7 * 8;
        return;
        }"""
        expect = """Error on line 3 col 21: c"""
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_more_all_program_4(self):
        input = """void Add(int a, int b){
        c = a + b = b / a = a * a = a / b = true = false;
        float floatt, c,d,f,g, flase , false;
        break;
        }
        int NULL(int arr[]){
        arr = .1e-5 + 1.e7 * 8;
        exit();
        }"""
        expect = """Error on line 3 col 39: false"""
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_more_all_program_5(self):
        input = """void Add(int a, int b){
        c = a + b = b / a = a * a = a / b = true = false;
        float floatt, c,d,f,g, flase;
        break;
        }
        int NULL(int arr[]){
        arr = .1e-5 + 1.e7 * 8;
        exit();
        continue;
        }
        true main(){}"""
        expect = """Error on line 11 col 8: true"""
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_more_all_program_6(self):
        input = """it Main(int a, int b){
        while(ok == clear)
            run_py(runnnnn);
        break;
        }"""
        expect = """Error on line 1 col 0: it"""
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_more_all_program_7(self):
        input = """int Main(int a, int b){
        while(ok == clear)
            run_py(runnnnn);
        break;
        }"""
        expect = """Error on line 2 col 8: while"""
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_more_all_program_8(self):
        input = """int Main(int a, int b){
        do
            break;
            a[5][5] = 8.2e-9;
        while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 4 col 16: ["""
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_more_all_program_9(self):
        input = """int Main(int a, int b){
        do
            break;
            countinue 2;
        while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 4 col 22: 2"""
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_more_all_program_10(self):
        input = """int Main(int a, int b){
        do
            int a , b , c ; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f loatf [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 3 col 12: int"""
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_more_all_program_11(self):
        input = """int Main(int a, int b){
        do
            a , b , c  = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f loatf [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 3 col 14: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_more_all_program_12(self):
        input = """int Main(int a, int b){
        do
            a = b * c  = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
        while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 6 col 12: run_py"""
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_more_all_program_13(self):
        input = """int Main(int a, int b){
        do
            a  = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f loatf [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        while(ok == clear);
            run_py(runnnnn);
        }"""
        expect = """Error on line 5 col 14: loatf"""
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_more_all_program_14(self):
        input = """int Main(int a, int b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        /*while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 7 col 8: /"""
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_more_all_program_15(self):
        input = """int Main(int a, int b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        /*while(ok == clear)
            run_py(runnnnn);
        }*/"""
        expect = """Error on line 9 col 11: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_more_all_program_16(self):
        input = """int Main(int a, int b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a t em e n t
        //while(ok == clear)
            run_py(runnnnn);
        }"""
        expect = """Error on line 9 col 8: }"""
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_more_all_program_17(self):
        input = """int Main(int a, int b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \n t em e n t
        while(ok == clear);
            run_py(runnnnn);
        }"""
        expect = """Error on line 7 col 3: em"""
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_more_all_program_18(self):
        input = """int Main(int a, int b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \r t em e n t
        while(ok == clear);
            run_py(runnnnn);
        }"""
        expect = """Error on line 6 col 52: em"""
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_more_all_program_19(self):
        input = """int Main(int a, float b){
        do
            a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \\r \\\\ t em e n t
        while(ok(ok)[5]);
            run_py(runnnnn);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_more_all_program_20(self):
        input = """int Main(int a, float b){
        do
            /*a = 5; // v a r i a b l e d e c l a r a t i o n
            a=b=c =5; // a s s ignmen t s t a t em e n t
            f [ 5 ] ; // v a r i a b l e d e c l a r a t i o n
            if (a==b) f[0] = 1.0 ; // i f s t a \\r \\\\ t em e n t*/
            ok();
        while(ok(ok)[5]);
            run_py(runnnnn);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,280))

    #test_complete_program
    def test_complete_program(self):
        input = """int main() {
        float alpha;
        cin = alpha;
        float result; sin(alpha);
        cout(fixed, setprecision(4) , result);
        return 0;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_complete_program_2(self):
        input = """void Matrix(int _x, int _y, int _z) {
        x = _x;
        y = _y;
        z = _z;
        mat = inr[x];
        for (i = 0; i < x; i +1 =i) 
            for(j = 0; j < y; j + 1 =j)
                mat[i] && mat[j] = inr[z];
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_complete_program_3(self):
        input = """
        int a[8];
        void tapcon(int k, int i) {
        for (j = 0; j < 5; j = j + 1)
            x[i] = a[j];
            if (i == k - 1) 
                for (j = 0; j < k; j = j * 2)
                    cout(x[j]);
            else tapcon(k, i + 1);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_complete_program_3(self):
        input = """
        int a[8];
        void tapcon(int k, int i) {
        for (j = 0; j < 5; j = j + 1)
            x[i] = a[j];
            if (i == k - 1) 
                for (j = 0; j < k; j = j * 2)
                    cout(x[j]);
            else tapcon(k, i + 1);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_complete_program_4(self):
        input = """
        int a[8];
        void setthuc(int thuc) {
        thisthuc = thuc;
        }
        int getthuc() {
            return thuc;
            }
        void setao(int ao) {
            thisao = ao;
            }
        int getao() {
        int a;
            return ao;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_complete_program_5(self):
        input = """
        int a[8];
        void hello(int thuc) {
            print("hello");
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_complete_program_6(self):
        input = """
        int a[8];
        int main() {
        int n;

        cout("ban dang tinh sin(x) voi x -> 0 \\n Hay nhap x ~ 0: ");
        system("pause");
        return 0;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_complete_program_7(self):
        input = """
        int main() {
        int songay, nam, tuan, ngay;
        cout = "Nhap so ngay: ";
        cin = songay;
        nam = songay / 365;
        tuan = (songay % 365) / 7;
        ngay = songay - nam * 365 - tuan * 7;
        cout = songay + " ngay = " + nam + " nam + " + tuan + " tuan + " + ngay + " ngay" + endl;
        system("pause");
        return 0;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_complete_program_8(self):
        input = """
        int main() {
        int songay, nam, tuan, ngay;
        cout = "Nhap so ngay: ";
        cin = songay;
        nam = songay / 365;
        tuan = (songay % 365) / 7;
        ngay = songay - nam * 365 - tuan * 7;
        cout = songay + " ngay = " + nam + " nam + " + tuan + " tuan + " + ngay + " ngay" + endl;
        system("pause");
        return 0;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_complete_program_9(self):
        input = """
        int main() {
        int soao;
        boolean thoat;
        return true;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_complete_program_10(self):
        input = """
        int main() {
        return soao;
        break;
        countinue;
        return true;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_complete_program_11(self):
        input = """
        int main() {
        return soao;
        break;
        countinue;
        return true;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_complete_program_12(self):
        input = """
        int intlit;
        int main() {
        int i, F, F1, F2, k, n;
        F1 = 1;
        F2 = 1;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_complete_program_13(self):
        input = """int main() {
        int n;
        cout ( "nhap n: ");
        cin ( n);
        for ( k = 0; k <= n; k = k + 1) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        pi = 2 * sum;
        cout ( "so pi la: \\" << setprecision(8) << fixed << pi << endl");
        system("pause");
        return 0;}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_complete_program_14(self):
        input = """int main() {
        void n;
        cin ( n);
        for ( k = 0; k <= n; k++) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        }"""
        expect = """Error on line 2 col 8: void"""
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_complete_program_15(self):
        input = """int main() {
        boolean n;
        cin ( n);
        for ( k = 0; k <= n; k++) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        }"""
        expect = """Error on line 4 col 31: +"""
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_complete_program_16(self):
        input = """int main() {
        boolean n;
        cin ( n);
        for ( k = 0; ; k) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        }"""
        expect = """Error on line 4 col 21: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_complete_program_17(self):
        input = """int main() {
        boolean n;
        cin ( n);
        for ( k = 0; ; k) {
            tuso = 2 * (k + 1);
            mau1 = 1 + 2 * k;
            mau2 = 3 + 2 * k;
            nhantu = tuso * tuso / (mau1*mau2);
            sum = sum * nhantu;
        }
        }"""
        expect = """Error on line 4 col 21: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_complete_program_18(self):
        input = """string chim {
            char name;
            int tuoitho;
            int cannang;
            int chieucao;
            };"""
        expect = """Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_complete_program_19(self):
        input = """string ca(string ca) {
            char name;
            int tuoitho;
            int cannang;
            int chieucao;
            };"""
        expect = """Error on line 2 col 17: name"""
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_complete_program_20(self):
        input = """string Name(string Ho, string Ten){
        Ho = "Nguyen Dang Ha";
        Ten = "Nam";
        print("My name is: ", Ho, Ten);
        Myemail = "nam.nguyen999@hcmut.edu.vn" || "ndhnam99@gmail.com";
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,300))