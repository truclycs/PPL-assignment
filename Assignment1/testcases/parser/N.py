import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_declararation(self):
        """Declaration tests"""
        input = """ int a;
                    int b[10];
                    void func(int a[], int param) {
                        run("now");
                    }
                    void main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_var_dec(self):
        """Variable declaration tests"""
        input ="""float f;
        float f1,f2,f3[15];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_var_dec1(self):
        input ="""int i,_4,oIV;
        int __[6];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_var_dec2(self):
        input ="""boolean t,_____,t7T[99];
        boolean f,t;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_var_dec3(self):
        input ="""string Str[44],aBc, _3hg;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_var_dec4(self):
        input ="""void _v01D,\t try_V[88];
        """
        expect = "Error on line 1 col 10: ,"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_var_dec5(self):
        input ="""int[] list[7], t, _23;
        """
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_var_dec6(self):
        input ="""boolean b;
        int i = 10;
        float t;
        """
        expect = "Error on line 2 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_var_dec7(self):
        input ="""string for;
        """
        expect = "Error on line 1 col 7: for"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_dec8(self):
        input ="""boolean true;
        """
        expect = "Error on line 1 col 8: true"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_var_dec9(self):
        input ="""float t"""
        expect = "Error on line 1 col 7: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_var_dec10(self):
        input ="""
        int i,j,k[];
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_func(self):
        """Function declaration tests"""
        input ="""int foo(int a, float b[]) { i = a + b[3]; } ;
        """
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_func1(self):
        input ="""\nvoid swap(float a, string b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_func2(self):
        input ="""\nvoid swap(float a,b,c[], string t) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 18: b"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_func3(self):
        input ="""\nvoid swap(float a, Type<T> b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 19: Type"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_func4(self):
        input ="""\nint[] _5Um(float a, boolean b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn a+b;  }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_func5(self):
        input ="""\nint[] num(int b[5]) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 16: 5"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_func6(self):
        input ="""\nfloat[5] swap(float a, Type<T> b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 6: 5"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_func7(self):
        input ="""\nvoid[] swap(float a, Type<T> b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_func8(self):
        input ="""\nstring[][5] swap(float a, Type<T> b) \n{\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 2 col 8: ["
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_func9(self):
        input ="""void n0_bl0ck(float a, int b[])\t"""
        expect = "Error on line 1 col 32: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_func10(self):
        input ="""\nvoid swap(float a, boolean b\n\tint t;\nt=a;\na=b;\nb=t;\nreturn;  }
        """
        expect = "Error on line 3 col 1: int"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_nested_func(self):
        input ="""\nstring goo() {\n\tstring t;\n\tt="Min Yoongi!!!";\n\tvoid goo() {\n\t\tprint("BTS"); } return t;  }
        """
        expect = "Error on line 5 col 1: void"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_standard_declaration(self):
        input = """int[] __ARMY__(int S, float U, string G[], boolean A) \n{ int i;\n if (i>0) {\n\tret = S+U+G+A;\n\tprint(ret>="bias");\n\treturn ret; }\n}\nstring Global_scale;\nvoid main() {} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_expression_stmt(self):
        """Expression Statement tests"""
        input = """void main() {\n\tif(i>5e2) {\n\t\ti=a+3; // Basic add op\n\t\tfoo(2)[3+x] = a[b[2]] + 3; // Function invocation\n\t\tboolean t;\n\t\tt = B = T = S = true || (var - 9 % 5 && (.5e7 != sun)); \n\t\t/*A pretty long expression\n\t\tthat makes no sense*/\n\t}\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

###################################################################################################

    def test_expression_stmt_index(self):
        input = """void main() {\n\t23[!a-b];\n\t_abx123[Func[x==4.e8]];\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_expression_stmt_index1(self):
        input = """void main() {\n\tint[(25)*4%(a-bY)];\n\t"Dope"+"Func!^"[index+"3e.0"]} 
        """
        expect ="Error on line 2 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_expression_stmt_index2(self):
        input = """void main() {\n\tbool[_][4] - 7;\n} 
        """
        expect ="Error on line 2 col 8: ["
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_expression_stmt_index3(self):
        input = """void main() {\n\ttrue[false];\n\tif[a&&b];\n} 
        """
        expect ="Error on line 3 col 3: ["
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_expression_stmt_index4(self):
        input = """void main() {\n\tint arr[10];\n\tarr[foo(x)]_list;\n} 
        """
        expect ="Error on line 3 col 12: _list"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_expression_stmt_index5(self):
        input = """void main() {\n\t[idx]_Lst12;\n\t_Lst12[a/9.0];\n} 
        """
        expect ="Error on line 2 col 1: ["
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_expression_stmt_index6(self):
        input = """void main() {\n\tfoo(4)[int];\n\treturn;\n} 
        """
        expect ="Error on line 2 col 8: int"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_expression_stmt_index7(self):
        input = """void main() {\n\tfoo(4)[];\n\treturn;\n} 
        """
        expect ="Error on line 2 col 8: ]"
        self.assertTrue(TestParser.checkParser(input,expect,234))

###################################################################################################

    def test_expression_mathop(self):
        input = """void main() {\n\tfloat discriminant, root1, root2, realPart, imaginaryPart;\n\tdiscriminant = b*b-4*a*c;\n\troot1 = (-b+sqrt(discriminant))/(2*a);\n\t
        root2 = foo(foo(foo(foo(foo(0)))));} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_expression_mathop1(self):
        input = """string[] new() {\n\tstring str1, str2;\n\tfoo(5) = b*b-4*a*c;\n\troot1 = +str1;\n\t
        root2 = (-b-sqrt(discriminant))/(2*a);} 
        """
        expect ="Error on line 4 col 9: +"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_expression_mathop2(self):
        input = """string[] new() {\n\tstring str1, str2;\n\tfoo(5) = _2D_Arr[a[b[c[7]]]]%22%5;\n\troot1 = -str1;\n\t} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_expression_mathop3(self):
        input = """string[] new() {\n\tboolean elem1;\n\telem1 = 34e-0-;\n\t} 
        """
        expect ="Error on line 3 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_expression_mathop4(self):
        input = """float double(int a, float b[]) {\n\tfloat f;\n\tdouble == (2*f)!;\n} 
        """
        expect ="Error on line 3 col 16: !"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_expression_mathop5(self):
        input = """boolean amIwr0ng(string a) {\n\tboolean t;\n\tt = a > b && c <= d;\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_expression_mathop6(self):
        input = """boolean determine() {\n\tint xFactor,a,b[10];\n\ta < b <= c;\n} 
        """
        expect ="Error on line 3 col 7: <="
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_expression_mathop7(self):
        input = """boolean determine() {\n\tint xFactor,RM,Jh0pe[10];\n\t(a < b) <= (c > d >= a);\n} 
        """
        expect ="Error on line 3 col 19: >="
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_expression_mathop8(self):
        input = """boolean assoc_order() {\n\tint xFactor,RM,Jh0pe[10];\n\t(a < b) <= (c > d != a);\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_expression_mathop9(self):
        input = """boolean assoc_order() {\n\tint xFactor,RM,Jh0pe[10];\n\tbool = a != b == c;\n} 
        """
        expect ="Error on line 3 col 15: =="
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_expression_mathop10(self):
        input = """boolean assoc_order() {\n\tint xFactor,RM,Jh0pe[10];\n\tbool = a != b && 2 || foo(strings);\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

###################################################################################################

    def test_if_stmt(self):
        """If - Else statement tests"""
        input = """int[] foo(int b[]) {\n\tint a[1];\n\tif (!a[0]) \n\t\treturn a;\n\t else \n\t\treturn b;\n} 
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_if_stmt1(self):
        input = """int main() {
    if (n == 1) 
    {
      printf("1 is neither a prime nor a composite number.");
    }
    else 
    {
        if (flag == 0)
          printf("%d is a prime number.", n);
        else
          printf("%d is not a prime number.", n);
    }
    
    return 0;
    }"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_if_stmt2(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }
        """
        expect ="Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_if_stmt3(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }
        """
        expect ="Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input,expect,249)) 
   
    def test_if_stmt4(self):
        input = """void main( ){ if () if (b) if (c) a; else a; else }
        """
        expect ="Error on line 1 col 18: )"
        self.assertTrue(TestParser.checkParser(input,expect,250))
   
    def test_if_stmt5(self): #redundant else
        input = """void main( ){ if (a) if(c) a; else arr[0]; else a = 25; else c = a || b== e; }
        """
        expect ="Error on line 1 col 56: else"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_if_stmt6(self): 
        input = """void main( ){ if (a) if(c) a; else arr[0]; else a = 25; }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

###################################################################################################

    def test_dowhile_stmt(self): 
        """Do - While statements tests"""
        input = """void main() { \n\tdo { \n\t\tprint("statement 1");\n\t} \n\twhile (true); \n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_dowhile_stmt1(self): 
        input = """void main() { \n\tdo { \n\t\tprint("statement 1");\n\t} \n\t{ \n\t\ta = b*25+.0e89;\n\t} \n\t{\n\t} \n\t{\n\t\tbreak;\n\t}  \n\twhile (true); \n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_dowhile_stmt2(self): 
        input = """void main() { \n\tdo print("statement 1");a = b*25+.0e89; print(strings); while (true); \n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_dowhile_stmt3(self): 
        input = """void main() { \n\tdo { \n\t\tprint("statement 1");}a = b*25+.0e89;{\n\t}\n\twhile (a*b7||airplane); \n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_dowhile_stmt4(self): 
        input = """void main() { \n\tdo { \n\t\tprint("statement 1");}a = b*25+.0e89;{\n\t}\n\twhile (a*b7||airplane)}
        """
        expect ="Error on line 5 col 23: }"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_dowhile_stmt5(self): 
        input = """void main() { \n\tdo { \n\t\tprint("statement 1");}a = b*25+.0e89;{\n\t}\n\twhile a*b7||airplane; \n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_dowhile_stmt6(self): 
        input = """void main() { do while a*b7||airplane; \n}
        """
        expect ="Error on line 1 col 17: while"
        self.assertTrue(TestParser.checkParser(input,expect,259))

###################################################################################################

    def test_for_stmt(self): 
        """For Statement tests"""
        input = """void main() { for(i=0; line[i]!="<EOF>"; i + 1)
        {
        if(line[i]=="a" || line[i]=="e" || line[i]=="i")
        {
            vowels;
        }
        else if((line[i]>="a"&& line[i]<="z") || (line[i]>="A"&& line[i]<="Z"))
        {
            consonants+1;
        }
        }
    }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    
    def test_for_stmt1(self): 
        input = """void main() { for(i=0; line[i]!="<EOF>"; i + 1) 2;\n }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
    def test_for_stmt2(self): 
        input = """void main() { for(i=0; line[i]!="<EOF>"; i + 1) \n }
        """
        expect ="Error on line 2 col 1: }"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_for_stmt3(self): 
        input = """void main() { for(foo(ar[2==3]); line[i]!="<EOF>"; i + 1) break;\n }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_for_stmt4(self): 
        input = """void main() { for(i=0; ; i + 1) { int a; a = a + .2e-1 % "MOD" };\n }
        """
        expect ="Error on line 1 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_for_stmt5(self): 
        input = """void main() { for(i=0; line[i]!="<EOF>"; i + 1) {}\n }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_for_stmt6(self): 
        input = """void main() { for(i=0; line[i]!="<EOF>"; i + 1) {}\n; }
        """
        expect ="Error on line 2 col 0: ;"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    
    def test_for_stmt7(self): 
        input = """void main() { for(i = "Humble"; i != "42.195^Uptopia"\n;\ni+"Prosperous" ) {}\n }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

###################################################################################################

    def test_break_stsmt(self): 
        """Break Statement test"""
        input = """string[] CTF(string _capture_the_flag_){ break; }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_break_stsmt1(self): 
        input = """float flag(int _MD5checksum){ break true; }
        """
        expect ="Error on line 1 col 36: true"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    
    def test_break_stsmt2(self): 
        input = """float flag(int _MD5checksum){ break }
        """
        expect ="Error on line 1 col 36: }"
        self.assertTrue(TestParser.checkParser(input,expect,270))

####################################################################################################

    def test_continue_stsmt(self): 
        """Continue Statement test"""
        input = """string[] CTF(string _capture_the_flag_){ continue ; }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_continue_stsmt1(self): 
        input = """float flag(int _MD5checksum){ continue \ne_x_pl01it; }
        """
        expect ="Error on line 2 col 0: e_x_pl01it"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test_continue_stsmt2(self): 
        input = """float flag(int _MD5checksum){ \ncontinue\n}
        """
        expect ="Error on line 3 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,273))

####################################################################################################

    def test_return_stsmt(self): 
        """Return Statement test"""
        input = """int PPL(string _capture_the_flag_){ return; }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_return_stsmt1(self): 
        input = """void main(){ return \n25.e-19+"#$random?!"; }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_return_stsmt2(self): 
        input = """float[] _und3rsc0r3(boolean tru3){ \nreturn\n}
        """
        expect ="Error on line 3 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,276))

####################################################################################################

    def test_block_stsmt(self): 
        """Block Statement tests"""
        input = """string[] CTF(string _capture_the_flag_){ \n\tcontinue ; \n\t{ \n\t\tgoo("hello"); \n\t\t{\n\t\t\tsekai == !world;\n\t\t}\n\t}\n}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_block_stsmt1(self): 
        input = """void main() {}
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    
    def test_block_stsmt2(self): 
        input = """void _so_many_block(boolean isOkay, int numBlock) { block1;} {block2;} {block3;}
        """
        expect ="Error on line 1 col 61: {"
        self.assertTrue(TestParser.checkParser(input,expect,279))

####################################################################################################

    def test_complete_program(self): 
        """Completed Programs tests """
        input = """
        // main function is an entry of MC program
        int main()
        {
            printf("Hello, World!\\n");
            return 0;
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    
    def test_complete_program1(self): 
        input = """
        int main()    
        {    
            int n1;
            n1 = n2 = n3 = i = number = 2!=5;    
            printf("Enter the number of elements:");    
            scanf("%d",number);    
            printf("\\n",n1,n2);//printing 0 and 1    
            for(i=2;i<number;i=i+1)//loop starts from 2 because 0 and 1 are already printed    
            {    
                break;    
                print(a(b(c(d(e(f(g(h("strings")))))))));  
            }  
            return 0;  
        }    
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_complete_program2(self): 
        input = """
        int main()    
        {    
            int n1;
            /* make a swap 
            function // make it right
            */
            void swap (int a, int b) {
                swap(a,b);
            }
        }    
        """
        expect ="Error on line 8 col 12: void"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_complete_program3(self): 
        input = """
        int main()    
        {    
            int n1;
            /* make a swap 
            function // make it right
            */
            int swap (int a, int b) {
                swap(a,b);
            }
        }    
        """
        expect ="Error on line 8 col 21: ("
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_complete_program4(self): 
        input = """
        int Global_var;
        string[] printList(string lst[]) 
            print(lst);
        int main()    
        {    
            continue;
        }    
        """
        expect ="Error on line 4 col 12: print"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_complete_program5(self): 
        input = """
        boolean[] pPl;
        string str;
        str = "This is ___3xhau5t1ng___!!!"
        """
        expect ="Error on line 2 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_complete_program6(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                n1 <= 1999;
                continue;
                fac(n1);
                print("this is not working 1234");
            while fac(0);
            return sum(1,"sunshine");
        }    
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_complete_program7(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                n1 <= 1999;
                continue;
                fac(n1);
                print("this is not working 1234");
            while fac(0);
            return sum(1,"sunshine");
        }    
        """
        expect ="Error on line 11 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    
    def test_complete_program8(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                n1 <= 1999;
                do 
                continue;
                for (i;j;k) fac(1);
                while fac(n1);
                print("this is not working 1234");
            while if;
            return;
        }    
        """
        expect ="Error on line 24 col 18: if"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_complete_program9(self): 
        input = """
        float f1;
        int fac(int n,t,k) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 == 39 != 45 * 3;
            
            return;
        }    
        """
        expect ="Error on line 3 col 22: t"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_complete_program10(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                else n*fac(n-1);
        }

        int main()    
        {    
            do 
                n1 <= 1999;
                do 
                continue;
                for (i;j;k) fac(1);
                while fac(n1);
                print("this is not working 1234");
            while you >= "world";
            return;
        }    
        """
        expect ="Error on line 7 col 16: else"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_complete_program11(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                do 
                    do
                        for (i;j;k) fac(1);
                    while fac(n1);
                    print("this is not working 1234");
                while false;
            return;
        }    
        """
        expect ="Error on line 25 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_complete_program12(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                fourIV;
            while (fac(49));
            return;
        }    
        string[] foo() { /*some unknown func*/}
        float goo() //Error should be here
        """
        expect ="Error on line 24 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_complete_program13(self): 
        input = """
        float f1;

        int main()    
        {    
            int n1,t[5],;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            break;
            return;
        }    
        """
        expect ="Error on line 6 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_complete_program14(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }
        f1 = 00044.03e-005;
        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                n1 <= 1999;
                do 
                continue;
                for (i;j;k) fac(1);
                while fac(n1);
                print("this is not working 1234");
            while if;
            return;
        }    
        """
        expect ="Error on line 9 col 8: f1"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_complete_program15(self): 
        input = """"""
        expect ="Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_complete_program16(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        int main()    
        {    
            int n1;
            n1 = 39 != 45 * 3;
            /* make a swap 
            function // make it right
            */
            do 
                n1 <= *1999;
                do 
                continue;
                for (i;j;k) fac(1);
                while fac(n1);
                print("this"+25);
            while if;
            return;
        }    
        """
        expect ="Error on line 18 col 22: *"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_complete_program17(self): 
        input = """
        float f1;
        int fac(int n) {
            if (n == 0)
                return 1;
            else
                return n*fac(n-1);
        }

        void _Army_(int a[], string b = 5) {

        }    
        """
        expect ="Error on line 10 col 38: ="
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_complete_program18(self): 
        input = """
        float f1,t;i;
        int main()    
        {    
            int n1;
            "str" = 39 != 45 * 3;
            return;
        }    
        """
        expect ="Error on line 2 col 19: i"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_complete_program19(self): 
        input = """
        float f1,t,i;
        int main()    
        {    
            "str" = 39 != 45 * 3;
            int n1;
            return;
        }    
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_complete_program20(self): 
        input = """
        string PPL;
        int Assignment1(string ppl) {
            if (effort == 0)
                return fail;
            else
                for (i = "first step"; i == "trials"; i=i+"exp") {
                    return ppl*gain(effort);
                }
        }

        int main()    
        {    
            // Final act - chapter 18.09
            if() {
                return "successful" + 000100.000e-000;
            }
            // nothing was done
            result => fail;
        }    
        """
        expect ="Error on line 15 col 15: )"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    