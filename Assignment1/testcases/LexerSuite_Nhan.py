import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ppl2019","ppl2019,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("nhanCao","nhanCao,<EOF>",102))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("a12?hjn","a12,Error Token ?",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("560","560,<EOF>",104))
    def test_negative_integer(self):
        self.assertTrue(TestLexer.checkLexeme("-253","-,253,<EOF>",105))
    def test_integer_with_id(self):
        self.assertTrue(TestLexer.checkLexeme("152a354","152,a354,<EOF>",106))
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("22.12","22.12,<EOF>",107))
    def test_float_with_exponent1(self):
        self.assertTrue(TestLexer.checkLexeme("-1.5e-52","-,1.5e-52,<EOF>",108))
    def test_float_with_exponent2(self):
        self.assertTrue(TestLexer.checkLexeme(".23E23 -5.",".23E23,-,5.,<EOF>",109))
    def test_id_vs_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("ifa 1if elsewhile","ifa,1,if,elsewhile,<EOF>",110))
    def test_exp_int(self):
        self.assertTrue(TestLexer.checkLexeme("(15+6)*6-9","(,15,+,6,),*,6,-,9,<EOF>",111))
    def test_exp_var(self):
        self.assertTrue(TestLexer.checkLexeme("_c5 = a/b","_c5,=,a,/,b,<EOF>",112))
    def test_exp_var_num1(self):
        self.assertTrue(TestLexer.checkLexeme("x = (b%5)-68","x,=,(,b,%,5,),-,68,<EOF>",113)) 
    def test_exp_var_num2(self):
        self.assertTrue(TestLexer.checkLexeme("e = (7e-7 + 100)*.2","e,=,(,7e-7,+,100,),*,.2,<EOF>",114))
    def test_logic_exp1(self):
        self.assertTrue(TestLexer.checkLexeme("!(a==b)<=c","!,(,a,==,b,),<=,c,<EOF>",115))
    def test_logic_exp2(self):
        self.assertTrue(TestLexer.checkLexeme("a >= b || a != b && a > 2","a,>=,b,||,a,!=,b,&&,a,>,2,<EOF>",116))      
    def test_arrvar(self):
        self.assertTrue(TestLexer.checkLexeme("q1[15]","q1,[,15,],<EOF>",117))
    def test_exp_arrvar(self):
        self.assertTrue(TestLexer.checkLexeme("t = f[7] + g[9]","t,=,f,[,7,],+,g,[,9,],<EOF>",118))
    def test_complex_exp1(self):
        self.assertTrue(TestLexer.checkLexeme("k[5] = foo(9)*5e-10 - var","k,[,5,],=,foo,(,9,),*,5e-10,-,var,<EOF>",119))
    def test_complex_exp2(self):
        self.assertTrue(TestLexer.checkLexeme("u = arr(2)[5] || k < 10","u,=,arr,(,2,),[,5,],||,k,<,10,<EOF>",120))
    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "MSSV1710214" ""","""MSSV1710214,<EOF>""",121))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""""Cao" "Thanh Nhan" ""","""Cao,Thanh Nhan,<EOF>""",122))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "i3\\thate" ""","""i3\\thate,<EOF>""",123))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Edogawa\\rConan"APTX4869 ""","""Edogawa\\rConan,APTX4869,<EOF>""",124))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.5 e4 "Test\\b?" ""","""1.5,e4,Test\\b?,<EOF>""",125))
    def test_unclose_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "this\nis" ""","""Unclosed String: this""",126))
    def test_unclose_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "this is\\r\r" ""","""Unclosed String: this is\\r""",127))
    def test_unclose_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "77Kid\\nkid ""","""Unclosed String: 77Kid\\nkid """,128))
    def test_unclose_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" kai "77\\t\\"77 ""","""kai,Unclosed String: 77\\t\\"77 """,129))
    def test_unclose_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""77"\\bku17 """,""",77,Unclosed String: \\bku17 """,130))
    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ilove\\iphone" ""","""Illegal Escape In String: ilove\\i""",131))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5. "iphone\\11plus" ""","""5.,Illegal Escape In String: iphone\\1""",132))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "k17\\ 1999" ""","""Illegal Escape In String: k17\\ """,133))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "MaiK\\n 20th\\aishiteru" ""","""Illegal Escape In String: MaiK\\n 20th\\a""",134))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" a56 "123\\xyz ""","""a56,Illegal Escape In String: 123\\x""",135))
    def test_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\"Um\\", said he", ""","""\\"Um\\", said he,,,<EOF>""",136))
    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "\\\\PPL123" ""","""123,\\\\PPL123,<EOF>""",137))
    def test_string_contain1(self):
        self.assertTrue(TestLexer.checkLexeme(""" A Study in Pink "The Sign of Three" ""","""A,Study,in,Pink,The Sign of Three,<EOF>""",138))
    def test_string_contain2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a"1.ea "" ""","""a,1.,ea,,<EOF>""",139))
    def test_string_contain3(self):
        self.assertTrue(TestLexer.checkLexeme("""\t "\\tLexer"Parser ""","""\\tLexer,Parser,<EOF>""",140))
    def test_string_contain4(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""n2"\\f\\b\\o" """,""",n2,Illegal Escape In String: \\f\\b\\o""",141))
    def test_string_contain5(self):
        self.assertTrue(TestLexer.checkLexeme(""" _Hoshi "\\\\kagayaku"_ ""","""_Hoshi,\\\\kagayaku,_,<EOF>""",142))
    def test_string_contain6(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""a123"" """,""",a123,,<EOF>""",143))
    def test_string_contain7(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""a=52" """,""",a,=,52,Unclosed String:  """,144))
    def test_string_contain8(self):
        self.assertTrue(TestLexer.checkLexeme(""" \n "" s\nn"" """,""",s,n,,<EOF>""",145))
    def test_other1(self):
        self.assertTrue(TestLexer.checkLexeme(" -1e ","-,1,e,<EOF>",146))
    def test_other2(self):
        self.assertTrue(TestLexer.checkLexeme(" 1e3_+&&& ","1e3,_,+,&&,Error Token &",147))
    def test_other3(self):
        self.assertTrue(TestLexer.checkLexeme("a,_c,k[7]=5","a,,,_c,,,k,[,7,],=,5,<EOF>",148))
    def test_other4(self):
        self.assertTrue(TestLexer.checkLexeme("while k \n _while h done n = t; ","while,k,_while,h,done,n,=,t,;,<EOF>",149))
    def test_other5(self):
        self.assertTrue(TestLexer.checkLexeme(""" String+Exception took me "lots of time" ""","String,+,Exception,took,me,lots of time,<EOF>",150))
    def test_var_decl_int1(self):
        self.assertTrue(TestLexer.checkLexeme("\rint i;","int,i,;,<EOF>",151))
    def test_var_decl_int2(self):
        self.assertTrue(TestLexer.checkLexeme("int k = -9, h1, _z; ","int,k,=,-,9,,,h1,,,_z,;,<EOF>",152))
    def test_var_decl_float1(self):
        self.assertTrue(TestLexer.checkLexeme("float \t e1 = 5.23e-5;","float,e1,=,5.23e-5,;,<EOF>",153))
    def test_var_decl_float2(self):
        self.assertTrue(TestLexer.checkLexeme("float \n _f = -6e-2, \n iff; ","float,_f,=,-,6e-2,,,iff,;,<EOF>",154))
    def test_var_decl_bool(self):
        self.assertTrue(TestLexer.checkLexeme("boolean bool = true; ","boolean,bool,=,true,;,<EOF>",155))
    def test_var_decl_arr(self):
        self.assertTrue(TestLexer.checkLexeme("int k[3]={1,5,-2}; ","int,k,[,3,],=,{,1,,,5,,,-,2,},;,<EOF>",156))
    def test_var_decl_str1(self):
        self.assertTrue(TestLexer.checkLexeme(""" string str = "Survivor"; ""","string,str,=,Survivor,;,<EOF>",157))
    def test_var_decl_str2(self):
        self.assertTrue(TestLexer.checkLexeme(""" string _str = "abc; ""","string,_str,=,Unclosed String: abc; ",158))
    def test_func_decl_void(self):
        self.assertTrue(TestLexer.checkLexeme("void main(argv){}","void,main,(,argv,),{,},<EOF>",159))
    def test_func_decl1(self):
        self.assertTrue(TestLexer.checkLexeme("int foo(int a, int b = 7);","int,foo,(,int,a,,,int,b,=,7,),;,<EOF>",160))
    def test_func_decl2(self):
        self.assertTrue(TestLexer.checkLexeme("boolean isPrime(int b);","boolean,isPrime,(,int,b,),;,<EOF>",161))
    def test_func_decl3(self):
        self.assertTrue(TestLexer.checkLexeme("float[] goo(float a[], int b);","float,[,],goo,(,float,a,[,],,,int,b,),;,<EOF>",162))
    def test_break(self):
        self.assertTrue(TestLexer.checkLexeme("if !list { break;}","if,!,list,{,break,;,},<EOF>",163))
    def test_continue(self):
        self.assertTrue(TestLexer.checkLexeme("if (a < 100) continue;","if,(,a,<,100,),continue,;,<EOF>",164))
    def test_funcall(self):
        self.assertTrue(TestLexer.checkLexeme("foo(7,5e-7,a);","foo,(,7,,,5e-7,,,a,),;,<EOF>",165))
    def test_for1(self):
        self.assertTrue(TestLexer.checkLexeme("for (int i = 100;i > 50;)\n {i = i - 20;}","for,(,int,i,=,100,;,i,>,50,;,),{,i,=,i,-,20,;,},<EOF>",166))
    def test_for2(self):
        self.assertTrue(TestLexer.checkLexeme("for (int i = 0;i < 5; i = i + 1) print(i);","for,(,int,i,=,0,;,i,<,5,;,i,=,i,+,1,),print,(,i,),;,<EOF>",167))
    def test_if1(self):
        self.assertTrue(TestLexer.checkLexeme("if (t == 10) flag = false; ","if,(,t,==,10,),flag,=,false,;,<EOF>",168))
    def test_if2(self):
        self.assertTrue(TestLexer.checkLexeme("if (_s1 > 10) a = a*b;\relse a = a/b; ","if,(,_s1,>,10,),a,=,a,*,b,;,else,a,=,a,/,b,;,<EOF>",169))
    def test_if3(self):
        self.assertTrue(TestLexer.checkLexeme("if (!empty) {next_element(arr);\nn += 1;\n","if,(,!,empty,),{,next_element,(,arr,),;,n,+,=,1,;,<EOF>",170))
    def test_return(self):
        self.assertTrue(TestLexer.checkLexeme("return 0; ","return,0,;,<EOF>",171))
    def test_do1(self):
        self.assertTrue(TestLexer.checkLexeme(" do {x = x + 3} while (x < 100); ","do,{,x,=,x,+,3,},while,(,x,<,100,),;,<EOF>",172))
    def test_do2(self):
        self.assertTrue(TestLexer.checkLexeme("do {ptr = next} while (!next); ","do,{,ptr,=,next,},while,(,!,next,),;,<EOF>",173))
    def test_expression1(self):
        self.assertTrue(TestLexer.checkLexeme(""" str = "Study" + "PPL" ""","str,=,Study,+,PPL,<EOF>",174))
    def test_expression2(self):
        self.assertTrue(TestLexer.checkLexeme(" a[4] =  .5*1.5e-2 + a[3] - e","a,[,4,],=,.5,*,1.5e-2,+,a,[,3,],-,e,<EOF>",175))
    def test_expression3(self):
        self.assertTrue(TestLexer.checkLexeme(" _k = h6%h5*h4+h3-h2/h1 ","_k,=,h6,%,h5,*,h4,+,h3,-,h2,/,h1,<EOF>",176))
    def test_manyexp1(self):
        self.assertTrue(TestLexer.checkLexeme(" n3 = n1+n2;\n n1 = n2;\n n2 = n3; ","n3,=,n1,+,n2,;,n1,=,n2,;,n2,=,n3,;,<EOF>",177))
    def test_manyexp2(self):
        self.assertTrue(TestLexer.checkLexeme(" x[1] = foo(2,3);\r x[2] = goo(2,3);\r sum = sum(x); ","x,[,1,],=,foo,(,2,,,3,),;,x,[,2,],=,goo,(,2,,,3,),;,sum,=,sum,(,x,),;,<EOF>",178))
    def test_manyexp3(self):
        self.assertTrue(TestLexer.checkLexeme(" r=n%10;\n sum=sum+(r*r*r);\n n=n/10; ","r,=,n,%,10,;,sum,=,sum,+,(,r,*,r,*,r,),;,n,=,n,/,10,;,<EOF>",179))
    def test_manyexp4(self):
        self.assertTrue(TestLexer.checkLexeme(" rem=n%10;\n reverse=reverse*10+rem;\n n = n/10; ","rem,=,n,%,10,;,reverse,=,reverse,*,10,+,rem,;,n,=,n,/,10,;,<EOF>",180))
    def test_all1(self):
        self.assertTrue(TestLexer.checkLexeme("""-4tf51e-3_hy "\\n"^" ""","-,4,tf51e,-,3,_hy,\\n,Error Token ^",181))
    def test_all2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1eAbc "Missing U\n" ""","1,eAbc,Unclosed String: Missing U",182))
    def test_all3(self):
        self.assertTrue(TestLexer.checkLexeme("""&&8*56.2|85+gh_tr-(4-5.6e2) ""","&&,8,*,56.2,Error Token |",183))
    def test_all4(self):
        self.assertTrue(TestLexer.checkLexeme("""notif 1.09-34*45e9"#"ehnv# ""","notif,1.09,-,34,*,45e9,#,ehnv,Error Token #",184))
    def test_all5(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""a=bc0.4e-5"\\fKako\\owa" """,",a,=,bc0,.4e-5,Illegal Escape In String: \\fKako\\o",185))
    def test_all6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" "kantan" de wa nai 1.e-1.8 """,",kantan,de,wa,nai,1.e-1,.8,<EOF>",186))
    def test_all7(self):
        self.assertTrue(TestLexer.checkLexeme(""""123abc123.456e-12" "" 167,45,54.6e-2 ""","123abc123.456e-12,,167,,,45,,,54.6e-2,<EOF>",187))
    def test_all8(self):
        self.assertTrue(TestLexer.checkLexeme("""[67 {fc ak}], gh"bx@" f_34 sd1.5 ""","[,67,{,fc,ak,},],,,gh,bx@,f_34,sd1,.5,<EOF>",188))
    def test_all9(self):
        self.assertTrue(TestLexer.checkLexeme("""/*-+if 6.7 elseif 87.45/5>52<=10 ""","/,*,-,+,if,6.7,elseif,87.45,/,5,>,52,<=,10,<EOF>",189))
    def test_all10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\nabc" 1e "abc\nabc""","abc\\nabc,1,e,Unclosed String: abc",190))
    def test_line_program1(self):
        self.assertTrue(TestLexer.checkLexeme("if (a != 3) {do b++ while true};","if,(,a,!=,3,),{,do,b,+,+,while,true,},;,<EOF>",191))
    def test_line_program2(self):
        self.assertTrue(TestLexer.checkLexeme("""printf("\\n\\n\\tCoding is Fun !\\n\\n");""","printf,(,\\n\\n\\tCoding is Fun !\\n\\n,),;,<EOF>",192))
    def test_line_program3(self):
        self.assertTrue(TestLexer.checkLexeme("p += q[12 * a] + -24 * b+1.e-5;\t//evalp\n","p,+,=,q,[,12,*,a,],+,-,24,*,b,+,1.e-5,;,<EOF>",193))
    def test_line_program4(self):
        self.assertTrue(TestLexer.checkLexeme("/*program*/\nif (flag) return a;\n else return b;","if,(,flag,),return,a,;,else,return,b,;,<EOF>",194))
    def test_line_program5(self):
        self.assertTrue(TestLexer.checkLexeme("for (i = 0; i<length(str); i=i+1) {\nif (i == 100) break;\r}","for,(,i,=,0,;,i,<,length,(,str,),;,i,=,i,+,1,),{,if,(,i,==,100,),break,;,},<EOF>",195))
    def test_line_program6(self):
        self.assertTrue(TestLexer.checkLexeme("if(aj > 0){sum = sum + aj;getSum(aj-1);}\nreturn sum;","if,(,aj,>,0,),{,sum,=,sum,+,aj,;,getSum,(,aj,-,1,),;,},return,sum,;,<EOF>",196))
    def test_line_program7(self):
        self.assertTrue(TestLexer.checkLexeme("if(x > y)find_gcd(x-y, y);\nelse if(y > x)find_gcd(x, y-x);\nelse return x;","if,(,x,>,y,),find_gcd,(,x,-,y,,,y,),;,else,if,(,y,>,x,),find_gcd,(,x,,,y,-,x,),;,else,return,x,;,<EOF>",197))
    def test_line_program8(self):
        self.assertTrue(TestLexer.checkLexeme(""" if (str == "true") return true; else return false; ""","if,(,str,==,true,),return,true,;,else,return,false,;,<EOF>",198))
    def test_line_program9(self):
        self.assertTrue(TestLexer.checkLexeme("int main(){int n;\nscanf(n);\nprintf(n);\n return 0;}","int,main,(,),{,int,n,;,scanf,(,n,),;,printf,(,n,),;,return,0,;,},<EOF>",199))
    def test_line_program10(self):
        self.assertTrue(TestLexer.checkLexeme("void swap(float x, float y) {\nfloat temp = x;\n x = y;\n y = temp;}","void,swap,(,float,x,,,float,y,),{,float,temp,=,x,;,x,=,y,;,y,=,temp,;,},<EOF>",100))