import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    #############################################################################BEGINNING_TEST(2)
    
    def test_simple_program(self):
        input = """void main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
<<<<<<< HEAD
        self.assertTrue(TestParser.checkParser(input,expect,202))

    #############################################################################VARDECL_TEST(5)
    
    def test_vardecl1(self):
        input = """int a, b, c;
        boolean x, y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_vardecl2(self):
        input = """int a[10], b;
        int main(){
            float k;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_vardecl3(self):
        input = """string str;
        void main(){
            float k[3];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_vardecl4(self):
        """ Missing number of array elements"""
        input = """int a, b[];"""
        expect = "Error on line 1 col 9: ]"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_vardecl5(self):
        """ Miss ; in line 3 """
        input = """boolean flag[5];
        int main(){
            float a,b
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    #############################################################################FUNCDECL_TEST(5)
    
    def test_funcdecl1(self):
        input = """int foo(int a, int b) {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test_funcdecl2(self):
        input = """float[] goo(int a[], float b, boolean flag) {}
        void main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_funcdecl3(self):
        """ Grammar error in parameters declaration """
        input = """void _swap2(int x, y) {}"""
        expect = "Error on line 1 col 19: y"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_funcdecl4(self):
        input = """boolean isPrime(int a) {}
        boolean[] isArmstrong(int a[]) {}
        void main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_funcdecl5(self):
        """ Missing function body """
        input = """string func1(string str)"""
        expect = "Error on line 1 col 24: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    #############################################################################EXP_TEST(10)
    
    def test_exp1(self):
        input = """void main(){
            a = b + c - d*5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test_exp2(self):
        input = """int main(){
            k = -b - a + 3*6/9;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_exp3(self):
        input = """void main(){
            a = 9*(-(3*6)%(7*x));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_exp4(self):
        input = """void main(){
            flag = !full || (empty == 0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_exp5(self):
        input = """void main(){
            _x = (a <= 3) && (b > 5.6e-6) || (c!=3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_exp6(self):
        input = """float main(){
            a[1] = c[2][3] - d[5] * k[55];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_exp7(self):
        """ Missing operator """
        input = """void main(){
            a = 4 + (5-7.8)(b-6);
        }"""
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_exp8(self):
        """ Undefined operator ^ in expression """
        input = """int main(){
            exp = b^4*c;
        }"""
        expect = "^"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_exp9(self):
        """ Test index expression """
        input = """int main(){
            exp = foo(5, 1)[2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_exp10(self):
        """ Test invocation expression """
        input = """int main(){
            _a = func(5-b) - func1(5.e-3,4-b)*6/12;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    #############################################################################IF_STMT_TEST(8)
    
    def test_ifstmt1(self):
        """ If without else """
        input = """void main(){
            if (k != 3) k = foo(k-3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test_ifstmt2(self):
        """ If with else """
        input = """void main(){
            if (n - 3 == 0) print("Error!");
            else n = goo(0,n-3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_ifstmt3(self):
        """ Many if-else """
        input = """void main(){
            if (flag == 0) x = 5;
            else if (flag == 1) x = 6;
            else x = 7;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test_ifstmt4(self):
        input = """/* 
        This is the program
        */
        void main(){
            if (t == true) {
                if (u  < 3) k = 6;
                else k = goo(3);
            }
            else k = foo(u - 3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test_ifstmt5(self):
        """ Missing () in condition """
        input = """void main(){
            if !empty {next(ptr);}
        }"""
        expect = "Error on line 2 col 15: !"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test_ifstmt6(self):
        """ More complicate if stmt """
        input = """int main(){
            if (isPrime(n)) {
                if (n > 1000) flag = true; //check if n > 1000
                else n = 3 + n * 7;
                print(n);
            }
            else print("n isn't a prime number!");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_ifstmt7(self):
        """ Too many elses """
        input = """void main(){
            if (n >= 5) k = 3;
            else k = 4;
            else k = 5;
        }"""
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_ifstmt8(self):
        """ Missing ; after stmt if """
        input = """void main(){
            if (flag) swap(a, b)
            else swap(a, c);
        }"""
        expect = "Error on line 3 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    #############################################################################BREAK_STMT_TEST(2)
    
    def test_breakstmt1(self):
        input = """int main () {
            if (t == true) break;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_breakstmt2(self):
        """ Error break return with a value??"""
        input = """
        int main () {               //what's wrong with this program?
            if (empty) break 123;
        }"""
        expect = "Error on line 3 col 29: 123"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    #############################################################################CONTINUE_STMT_TEST(1)
    
    def test_continuestmt(self):
        input = """int main () {
            if (flag) continue;
            else break;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    #############################################################################RETURN_STMT_TEST(5)
    
    def test_returnstmt1(self):
        input = """void main() {
            return;                 //use for what???
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_returnstmt2(self):
        input = """int main() {
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_returnstmt3(self):
        """ Return in function """
        input = """int eval(int a, int b, string op) {
            if (op == "+") return a + b;
            if (op == "-") return a - b;
            else error(op);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_returnstmt4(self):
        """ Return undefined object """
        input = """int sowrong() {
            return 1e;
        }"""
        expect = "Error on line 2 col 20: e"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_returnstmt5(self):
        """ Example with recursive function """
        input = """int fibonacci(int a) {
            if (a == 0) return 1;
            if (a == 1) return 1;
            return fibonacci(a - 1) + fibonacci(a-2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    #############################################################################FOR_STMT_TEST(6)
    
    def test_forstmt1(self):
        """ Simple for loop """
        input = """int main() {
            for (i = 0; i < 100; i = i+1) sum = sum + i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_forstmt2(self):
        input = """int main() {
            for (1; i < 100; i = i * 2) print("Okay!");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_forstmt3(self):
        """ Leave an exp empty """
        input = """int main() {
            for (i = 0; i < 100;) {
                sum = sum + i;
                i = i + 5;
            }
        }"""
        expect = "Error on line 2 col 32: )"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_forstmt4(self):
        """ Missing an exp """
        input = """int main() {
            for (i < 100; i = i + 2) s = s + i;
        }"""
        expect = "Error on line 2 col 35: )"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_forstmt5(self):
        """ For loop in for loop """
        input = """int main() {
            for (h = 1; h <= 12; h = h + 1) 
                for (k = 1; k <= 24; k = k + 2) n = n + h*k;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    
    def test_forstmt6(self):
        input = """
        int a[10];
        int sum(int a[]) {
            int i, sum;
            for (i = 0; i < 10; i = i+1) sum = sum + a[i];
            return sum;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    #############################################################################BLOCK_STMT_TEST(7)
    
    def test_blockstmt1(self):
        input = """void main() {
            {int i, k;}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_blockstmt2(self):
        """ Nothing in blockstmt """
        input = """void main() {
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    
    def test_blockstmt3(self):
        """ Block in block """
        input = """void main() {
            {int i, k;
                {
                    int z;
                    i = k = z = 5;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_blockstmt4(self):
        """ Many blocks """
        input = """void main() {
            {
                int a, b, c;         //variable declaration
                a=b=c=5;             //assignment statement  
            }
            {
                float f[5];         //variable declaration
                if (a==b) f[0] = 1.0; //if statement
            }
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    
    def test_blockstmt5(self):
        """ Error ; after block stament """
        input = """int main() {
            {
                string str;
            };
        }"""
        expect = "Error on line 4 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_blockstmt6(self):
        """ Stand-alone block error """
        input = """{boolean _f;}"""
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_blockstmt7(self):
        """ Stand-alone block after variable declaration """
        input = """int a;
        {boolean _f;}"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    #############################################################################DOWHILE_STMT_TEST(5)
    
    def test_dowhilestmt1(self):
        input = """void main() {
            do x = x + 3; while true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_dowhilestmt2(self):
        input = """void main() {
            do {
                x = x * 3;
                i = i + 1;
                }
            while i < exp;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test_dowhilestmt3(self):
        """ do while with many statements """
        input = """void main() {
            int a[99], x, i;
            x = 0;
            i = 0;
            do x = x + 3;
            print(x);
            a[i] = x;
            i = i + 1;
            while (i < 99);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_dowhilestmt4(self):
        """ Error do nothing """
        input = """int do_nothing(){
            do while true;
        }"""
        expect = "Error on line 2 col 15: while"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_dowhilestmt5(self):
        """ Error do without while """
        input = """int main() {
            do x = foo(x);
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    #############################################################################SOME_ERRORS_TEST(23)

    def test_error1(self):
        """ Empty program """
        input = """/* /////////////////////////////////
        Empty program
        /////////////////////////////////////////////*/"""
        expect = "Error on line 3 col 55: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_error2(self):
        """ Strange line after correct grammar """
        input = """int a[2];
        Cao Nhan;"""
        expect = "Error on line 2 col 8: Cao"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_error3(self):
        """ More variable declaration errors - variable initialization """
        input = """float f = .5;"""
        expect = "Error on line 1 col 8: ="
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_error4(self):
        """ More variable declaration errors - array variable with negative number of element """
        input = """int a[-99];"""
        expect = "Error on line 1 col 6: -"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_error5(self):
        """ More variable declaration errors - unacceptable name declaration """
        input = """boolean 30s;"""
        expect = "Error on line 1 col 8: 30"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
    def test_error6(self):
        """ More variable declaration errors - unknown variable type """
        input = """VIP Conan;"""
        expect = "Error on line 1 col 0: VIP"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_error7(self):
        """ More function declaration errors - wrong seperator """
        input = """boolean isLover(string boyname; string girlname){
            return false;
        }"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_error8(self):
        """ More function declaration errors - nested function """
        input = """void foo(int i){
            int child_of_foo(float f){} //ERROR
        }"""
        expect = "Error on line 2 col 28: ("
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_error9(self):
        """ More function declaration errors - missing type of parameters """
        input = """float hoo(i){};"""
        expect = "Error on line 1 col 10: i"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_error10(self):
        """ More function declaration errors - initialization """
        input = """int func1(int a, float b = 0){}"""
        expect = "Error on line 1 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_error11(self):
        """ More function declaration errors - number of array elements in parameters """
        input = """boolean[] flag(int a[5], int b[5]){}"""
        expect = "Error on line 1 col 21: 5"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_error12(self):
        """ More function declaration errors - other mistakes """
        input = """int[] goo(int[] a, int b){};"""
        expect = "Error on line 1 col 13: ["
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_error13(self):
        """ More expression errors - two consecutive infix operators """
        input = """void main(){
            err = a / 7 */ 56;
        }"""
        expect = "Error on line 2 col 25: /"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_error14(self):
        """ More expression errors - missing a RB """
        input = """void main(){
            isTiredNow = ((yes && ofCourse) || !no || true;
        }"""
        expect = "Error on line 2 col 58: ;"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_error15(self):
        """ More expression errors - no associativity operators """
        input = """void main(){
            boo = a >= b <= c > d < e;
        }"""
        expect = "Error on line 2 col 25: <="
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_error16(self):
        """ More expression errors - unclosed string """
        input = """void main(){
            myFavorites = "MeitanteiConan" + "MaiK" + "Sherlock" + "PPL;
        }"""
        expect = "PPL;"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_error17(self):
        """ More expression errors - error in prefix - """
        input = """void main(){
            myPoints = -(a + b * );
        }"""
        expect = "Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_error18(self):
        """ Unknown statement """
        input = """int please(){
            do it for me;
        }"""
        expect = "Error on line 2 col 18: for"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_error19(self):
        """ Comment error """
        input = """
        ///*This is an example
        */
        void main(){}"""
        expect = "Error on line 3 col 8: *"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_error20(self):
        """ Wrong grammar funcall  """
        input = """void main(){
            result = exponent(2 random(1,40));
        }"""
        expect = "Error on line 2 col 32: random"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_error21(self):
        """ Error ; after function"""
        input = """void main(){};
        """
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_error22(self):
        """ Undefined prefix + """
        input = """void main(){
            float a;
            a = +.5; 
        }
        """
        expect = "Error on line 3 col 16: +"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_error23(self):
        """ Others statements after main function """
        input = """void main(){}
        {unknown} //Do you think this is acceptable?
        """
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    #############################################################################VARIABLE_TEST(5)

    def test_variable1(self):
        input = """int a[10], b;
        boolean _flag;
        float f, arr[5];
        string str;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_variable2(self):
        input = """int main()
        {
            int a, b;
            a = 3;
            b = 5;
            a = (6 - 5 * (b % a));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_variable3(self):
        input = """float a, b[2];
        int main()
        {
            int c;
            a = a * b[0] + (a - 3) * b[1];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_variable4(self):
        input = """int main()
        {
            int a[5];
            return (a[0] && (a[1] >= a[2])) || (a[3] != a[4]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_variable5(self):
        input = """int main()
        {
            string s;
            boolean flag;
            s = "true" +"orfalse";
            if (s == "true") flag = true;
            else flag = false;
            return flag;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    #############################################################################FUNCTION_TEST(5)

    def test_function1(self):
        input = """float sum(float a, float b){
            return a + b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_function2(self):
        input = """int find_gcd(int n1, int n2)
        {
            if (n2 != 0)
            return find_gcd(n2, n1%n2);
            else return n1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_function3(self):
        input = """int sumArray(int n[], int n)
        {
            int i, sum;
            sum = 0;
            for (i = 0; i < n; i = i + 1) {
                sum = sum + n[i];
            }
            return sum;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_function4(self):
        input = """void swap(int a, int b)
        {
            int temp;
            temp = a;
            a = b;
            b = temp;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    def test_function5(self):
        input = """boolean isPrime(int n)
        {
            int j, flag;
            for(j=2; j <= n/2; j = j+1)
            {
                if (n%j == 0)
                {
                    flag = 0;
                    break;
                }
            }
            return flag;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    #############################################################################SIMPLE_PROGRAM_TEST(5)
    
    def test_simple_program1(self):
        input = """int main()
        {
            printf("Hello, World!\\n");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_simple_program2(self):
        input = """int main()
        {
            int number;
            printf("Enter an integer: ");
            scanf("%d", number);
            printf("You entered: %d", number);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_simple_program3(self):
        input = """string str;
        int main()
        {   
            str = "Conan " + "Meitantei";
            printf(str);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_simple_program4(self):
        input = """int main()
        {
            int a[2];
            a[0] = 2;
            a[1] = 12;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_simple_program5(self):
        input = """boolean flag;
        int main()
        {
            flag = true;
            if (flag) printf("It's over!");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    #############################################################################MORE_COMPLEX_PROGRAM_TEST(6)

    def test_more_complex_program1(self):
        input = """int i;
        int[] foo(){}
        void main(){
            i = 9;
            i = i + foo()[2];
            if (i < 9) print("True");
            else print("False");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_more_complex_program2(self):
        input = """boolean flag;
        int round(float a){}
        void main(){
            float number;
            flag = true;
            do {
                number = random(1, 200) / 10;
                if (number == round(number)) flag = false;
            } 
            while (flag);
            print(number);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_more_complex_program3(self):
        input = """/*This is a program*/
        void main(){
            int n, i;
            n = 100;
            for (i = 0; true; i = i + 1)
            {
                n = n - i;
                if (n < i) break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_more_complex_program4(self):
        input = """//Check whether an integer is odd or even
        int main()
        {
            int number;
            printf("Enter an integer: ");
            scanf("%d", number);
            if  (number%2 == 0) printf("%d is an even integer.",number);
            else printf("%d is an odd integer.",number);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_more_complex_program5(self):
        input = """float[] func(int a[], float b){}
        void main(){
            int a[5];
            b = 1e-3;
            float n;
            n = (func(func(a[3], 3 - b*4)[a[1] + 6], - (b*5 + 3)) - h[a[0]]*foo(a[4]))[a[2] - 1];
            print(n);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_more_complex_program6(self):
        input = """int i ;
        int f(){
            return 200;
        }
        void main(){
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
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
=======
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test(self):
        inp = """int main() {x = false; y = true;}"""
        out = "successful"
        self.assertTrue(TestParser.checkParser(inp,out,204))



>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
