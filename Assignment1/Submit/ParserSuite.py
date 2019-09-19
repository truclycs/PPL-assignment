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

    def test241(self):
        input = """ int cal(int a) {
                        if (a) print("OK");
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test242(self):
        input = """ int cal(int a) {
                        do res = 1 + 1; while 1 + 1 == 2;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test243(self):
        input = """ int cal(int a) {
                        do res = 1 + 1 while 1 + 1 == 2;
                    }"""
        expect = "Error on line 2 col 39: while"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test244(self):
        input = """ int cal(int a) {
                        do res = 1 + 1; while 1 + 1 == 2
                    }"""
        expect = "Error on line 3 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test245(self):
        input = """ int cal(int a) {
                        do  while 1 + 1 == 2
                    }"""
        expect = "Error on line 2 col 28: while"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test246(self):
        input = """ int cal(int a) {
                        do res = 1 + 1;
                    }"""
        expect = "Error on line 3 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test247(self):
        input = """ int cal(int a) {
                        while 1 + 1 == 2;
                    }"""
        expect = "Error on line 2 col 24: while"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test248(self):
        input = """ int cal(int a) {
                        do res = 1 + 1 while
                    }"""
        expect = "Error on line 2 col 39: while"
        self.assertTrue(TestParser.checkParser(input,expect,248))


    def test249(self):
        input = """ int cal(int a) {
                        cal((a + 3) % 2 * 8);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test250(self):
        input = """ int cal(int a) {
                        cal((a + 3) % 2 * 8 = b == c);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test251(self):
        input = """int a[4][4]; """
        expect = "Error on line 1 col 8: ["
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test252(self):
        input = """int a[[4]]; """
        expect = "Error on line 1 col 6: ["
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test253(self):
        input = """int a[4]; 
                    void main() {
                        a[3] = 1;
                        a[2 + a[5]] = 6;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test254(self):
        input = """ void main() {
                        i = 1;
                        foo (1 ,2);
                        i + 2;
                        100;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test255(self):
        input = """ void main() {
                        float a[10];
                        a[0] = 1.5;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))


    def test256(self):
        input = """int func(int a, float b){
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
                continue;
                }
                void main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test257(self):
        input = """int func(int a){
                for(a = 10; a < 20; a = a + 1 ) i = i + 1;
                continue;
                void main() {}"""
        expect = "Error on line 4 col 16: void"
        self.assertTrue(TestParser.checkParser(input,expect,257))


    def test258(self):
        input = """int func(int a){
                for(a = 10; a < 20; a = a + 1 ) i = i + 1;
                continue;
                void main() {}"""
        expect = "Error on line 4 col 16: void"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test259(self):
        input = """int main() {
                    int t, b, p, f, h, c;
                    cin(t);
                    while (t--) 
                        cin >> b >> p >> f >> h >> c;
                        if (h > c) 
                            int x = min(p, b / 2);
                            cexpect << h * x + c * min(f, (b - x * 2) / 2);
                        
                        else {
                            int x = min(f, b / 2);
                            cexpect << h * min(p, (b - x * 2) / 2) + c * x;
                        }
                        cexpect << "\n";
                    }
                    return 0;
                }"""
        expect = "Error on line 4 col 20: while"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test260(self):
        input = """int main() {
                    int t, b, p, f, h, c;
                    cin(t);
                    if (h > c) x = min(p, b / 2);
                    cexpect(h * x + c * min(f, (b - x * 2) / 2));
                    else int x = min(f, b / 2);
                    cexpect(h * min(p, (b - x * 2) / 2) + c * x);
                    cexpect("\n");
                    }
                    return 0;
                }"""
        expect = "Error on line 6 col 20: else"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test261(self):
        input = """int main() {
                    int t, b, p, f, h, c;
                    cin(t);
                    if (h > c) x = min(p, b / 2);
                    else (h * x + c * min(f, (b - x * 2) / 2));
                    int x = min(f, b / 2);
                    ch * min(p, (b - x * 2) / 2) + c * x);
                    c("...");
                    }
                    return 0;
                }"""
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test262(self):
        input = """int main() {
                    int t, b, p, f, h, c;
                    cin(t);
                    if (h > c) x = min(p, b / 2);
                    else (h * x + c * min(f, (b - x * 2) / 2));
                    int x = min(f, b / 2);
                    cexpect(h * min(p, (b - x * 2) / 2) + c * x);
                    }
                    return 0;
                }"""
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test263(self):
        input = """int main() {
                    if (h > c) x = min(p, b / 2);
                    else (h * x + c * min(f, (b - x * 2) / 2));
                    cexpect(h * min(p, (b - x * 2) / 2) + c * x);
                    }
                    return 0;
                }"""
        expect = "Error on line 6 col 20: return"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test264(self):
        input = """int main() {
                    if (h > c) x = min(p, b / 2);
                    else (h * x + c * min(f, (b - x * 2) / 2));
                    cexpect(h * min(p, (b - x * 2) / 2) + c * x);
                    return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test265(self):
        input = """ 
                    int main() {
                        int s, n;
                        cin >> s >> n;
                        pair<int, int> x[n];
                        for (int i = 0; i < n; i++) {
                            cin >> x[i].first >> x[i].second;
                        }
                        sort(x, x + n);                    
                        for (int i = 0; i < n; i++) {
                            if (x[i].first >= s) {
                                cexpect << "NO";
                                return 0;
                            }
                            s += x[i].second;
                        }                    
                        cexpect << "YES";
                        return 0;
                    }"""
        expect = "."
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test266(self):
        input = """ 
                    int main() {
                        int s, n;
                        cin >> s >> n;
                        pair<int, int> x[n];
                        for (int i = 0; i < n; i++) sort(x, x + n);                    
                        for (int i = 0; i < n; i++) {
                            if (x[i] >= s) {
                                cexpect << "NO";
                                return 0;
                            }
                        }                    
                        cexpect << "YES";
                        return 0;
                    }"""
        expect = "Error on line 4 col 29: >"
        self.assertTrue(TestParser.checkParser(input,expect,266))


    def test267(self):
        input = """ 
                    int main() {
                        int s, n;
                        pair<int, int> x[n];
                        for (int i = 0; i < n; i++) sort(x, x + n);                    
                        for (int i = 0; i < n; i++) {
                            if (x[i] >= s) {
                                cexpect << "NO";
                                return 0;
                            }
                        }                    
                        cexpect << "YES";
                        return 0;
                    }"""
        expect = "Error on line 4 col 29: int"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test268(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i++) sort(x, x + n);                    
                        for (i = 0; i < n; i++) {
                            if (x[i] >= s) {
                                cexpect << "NO";
                                return 0;
                            }
                        }                    
                        cexpect << "YES";
                        return 0;
                    }"""
        expect = "Error on line 4 col 45: +"
        self.assertTrue(TestParser.checkParser(input,expect,268))


    def test269(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i) sort(x, x + n);                    
                        for (i = 0; i < n; i) {
                            if (x[i] >= s) {
                                cexpect << "NO";
                                return 0;
                            }
                        }                    
                        cexpect << "YES";
                        return 0;
                    }"""
        expect = "Error on line 7 col 41: <"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test270(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i) sort(x, x + n);                    
                        for (i = 0; i < n; i) {
                            if (x[i] >= s) {
                                return 0;
                            }
                        }                    
                        return 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test271(self):
        input = """ 
                    int main() {
                        int s, n;
                        for (i = 0; i < n; i) sort(x, x + n);                    
                        for (i = 0; i < n; i) {
                            if (x[i] >= s) {
                                a = a + 1;
                                return 0;
                            }
                            b = b + 1;
                        }                    
                        return 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test272(self):
        input = """int main() {
                    int n;
                    int a[n], d[n] = {false};
                    for (int i = 0; i < n; i++) {
                        cin(a[i]);
                    }                
                    return 0;
                }"""
        expect = "Error on line 3 col 26: n"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test273(self):
        input = """int main() {
                    int n;
                    for (i = 0; i < n; i) {
                        cin([i]);
                    }                
                }"""
        expect = "Error on line 4 col 28: ["
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test274(self):
        input = """int main() {
                    int n;
                    for (i = 0; i < n; i) {
                        cin(a[i]);
                    }                
                    sort(a, a + n);
                    int res = 0;                
                }"""
        expect = "Error on line 7 col 28: ="
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test275(self):
        input = """int main() {
                    int n;
                    for (i = 0; i < n; i) {
                        cin(a[i]);
                    }                
                    sort(a, a + n);             
                    for (i = 0; i < n; i) {
                        if (!d[i]) {
                            res;
                            for (j = i + 1; j < n; j) {
                                if (a[j] % a[i] == 0) {
                                    d[j] = true;
                                }
                            }
                        }
                    }
                    return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test276(self):
        input = """  int main() {
                //  freopen("in.inp", "r", stdin);
                //    freopen("in.expect", "w", stdexpect);
                    int n, m;
                    string s;
                    for (i = 0; i < n; i) {
                        cins[i];
                    }
                    int a[10];
                    for (i = 0; i < m; i) {
                        cina[i];
                    }
                
                   /* int res = 0;
                    for (int i = 0; i < m; i++) {
                        int A = 0, B = 0, C = 0, D = 0, E = 0;
                        for (int j = 0; j < n; j++) {
                            if (s[j][i] == 'A') {
                                A++;
                            }
                            if (s[j][i] == 'B') {
                                B++;
                            }
                            if (s[j][i] == 'C') {
                                C++;
                            }
                            if (s[j][i] == 'D') {
                                D++;
                            }
                            if (s[j][i] == 'E') {
                                E++;
                            }
                        }
                        res += max(max(max(max(A, B), C), D), E) * a[i];
                    }
                
                    cexpect << res;
                    return 0;*/
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test277(self):
        input = """  int main() {                
                    int res;
                    for (i = 0; i < m; i) {
                        int A , B, B, C, D, E;
                        for (j = 0; j < n; j) {
                            if (s[j][i] == 'A') {
                                A++;
                            }
                            if (s[j][i] == 'B') {
                                B++;
                            }
                            if (s[j][i] == 'C') {
                                C++;
                            }
                            if (s[j][i] == 'D') {
                                D++;
                            }
                            if (s[j][i] == 'E') {
                                E++;
                            }
                        }
                        res += max(max(max(max(A, B), C), D), E) * a[i];
                    }
                
                    cexpect << res;
                    return 0;*/
                }"""
        expect = "Error on line 6 col 36: ["
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test278(self):
        input = """  int main() {                
                    int res;
                    for (i = 0; i < m; i) {
                        int A , B, B, C, D, E;
                        for (j = 0; j < n; j) {
                            if (s[j][i] == A) {
                                A;
                            }
                            if (s[j][i] != B) {
                                B;
                            }
                            if (s[j][i] >= C) {
                                C;
                            }
                            if (s[j][i] >= D) {
                                D;
                            }
                            if (s[j][i] || E) {
                                E;
                            }
                        }
                        res += max(max(max(max(A, B), C), D), E) * a[i];
                    }
                
                    cexpect << res;
                    return 0;*/
                }"""
        expect = "Error on line 6 col 36: ["
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test279(self):
        input = """  int main() {                
                    int res;
                    for (i = 0; i < m; i) {
                        int A , B, B, C, D, E;
                        for (j = 0; j < n; j) {
                            if (s[j] == A) {
                                A;
                            }
                            if (s[i] != B) {
                                B;
                            }
                            if (s[i] >= C) {
                                C;
                            }
                            if (s[i] >= D) {
                                D;
                            }
                            if (s[i] || E) {
                                E;
                            }
                        }
                        res = max(max(max(max(A, B), C), D), E) * a[i];
                    }
                    return 0;*/
                }"""
        expect = "Error on line 24 col 29: *"
        self.assertTrue(TestParser.checkParser(input,expect,279))


    def test280(self):
        input = """  int main() {                
                    int res;
                    for (i = 0; i < m; i) {
                        int A , B, B, C, D, E;
                        for (j = 0; j < n; j) {
                            if (s[j] == A) {
                                A;
                            }
                        }
                        res = max(max(max(max(A, B), C), D), E) * a[i];
                    }
                    return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test281(self):
        input = """  int main() {                
                    \*abcyz;
                    return 0;
                }"""
        expect = "\\"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test282(self):
        input = """  int main() {                
                    if (a=b=c=d=e=f=d=f=e|1){
                        break;
                    }
                    return 0;
                }"""
        expect = "|"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test283(self):
        input = """  int main() {                
                    if (a=b=c=d=e=f=d=f=e||1){
                        break;
                    }
                    else {
                        continue;
                    }
                    return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test284(self):
        input = """int abc, xyz;
            int f(boolean bl) {
                x = false;
                do abc = abc + 1;
                while xyz != false;
                return 0;
            }
            float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }"""

        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))


    def test285(self):
        input = """int [ ] foo ( int b [ ] ) {
                    if (ABC ) return a ;
                    else return b ;
            }
            void main() {
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test286(self):
        input = """float foo(){
                i=2;
                foo(1.2);
                foo(3*4);
                100;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test287(self):
        input ="""float foo(){
                return x;
            }
            float foo(){
                y = y * 13.7878;
                return y;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test288(self):
        input = """float foo(){
                foo(x);
                return x;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test289(self):
        input = """void main() {
                    abc = foo();
                    for( abc = 1; xyz == true; abc = abc + 1)
                        if(abc == 1)
                            abc = 0;
                        else
                            do abc = abc + 1;
                            while xyz != false;
                    string foo(){return x;}
                }"""
        expect = "Error on line 9 col 30: ("
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test290(self):
        input = """ int x; //int a[];
                    float string; """
        expect = "Error on line 2 col 26: string"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test291(self):
        input = """ int x;
                    float int[5]; """
        expect = "Error on line 2 col 26: int"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test292(self):
        input = """ int x; 
                    float a[4];
                    int foo(b) {
                        a[1] - 3;
                    } """
        expect = "Error on line 3 col 28: b"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test293(self):
        input = """ int x; 
                    int foo() {
                        a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[a[aa[a[a[a[a[a[a[a[a[a[a[a[a]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]];
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    
    def test294(self):
        input = """ int foo() {
                    a[((((0.0))))];
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test295(self):
        input = """ int foo() {
                        return (-1+2*3+4/5%6)[2];
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test296(self):
        input = """ int foo() {
                    a(-1+2*3+4/5%6)[2];
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test297(self):
        input = """ int foo() {
                    (-1+2*3+4/5%6)[2];
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test298(self):
        input = """ int foo() {
                    [2](-1+2*3+4/5%6);
                    } """
        expect = "Error on line 2 col 20: ["
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test299(self):
        input = """ int[] func() {
                        int a, b, c, x[10];
                        if (flag == true) a = x[1];
                        else break;
                        continue;
                        do (x[2] = 1); while a = b;
                        x[3] = a * b - c + d / f % g;
                        return a[1];
                        return x;
                        return;

                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test300(self):
        input = """ void funcEnd() {
                        print("END!");
                    } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
