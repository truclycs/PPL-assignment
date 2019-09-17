import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("fou?99iv","fou,Error Token ?",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("MinhNgoc f0uR1v","MinhNgoc,f0uR1v,<EOF>",102))
    def test_underscore_id(self):
        self.assertTrue(TestLexer.checkLexeme("_ _2CSE_ KH_12mt ","_,_2CSE_,KH_12mt,<EOF>",103))
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("_1712345# mssv","_1712345,Error Token #",104))
    def test_error_token2(self):
        self.assertTrue(TestLexer.checkLexeme("_@2av  DGSc","_,Error Token @",105))
    def test_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("break h3ll0float boolean","break,h3ll0float,boolean,<EOF>",106))
   
    def test_int(self):
        """Interger literals test"""
        self.assertTrue(TestLexer.checkLexeme("1712345","1712345,<EOF>",107))
    def test_int_prefix_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0024 0449","0024,0449,<EOF>",108))
    def test_int_vs_id(self):
        self.assertTrue(TestLexer.checkLexeme("123_abc 0049sunSh1n3","123,_abc,0049,sunSh1n3,<EOF>",109))
   
    def test_complete_float(self):
        """Floating-point literals tests"""
        self.assertTrue(TestLexer.checkLexeme("12.5e-9","12.5e-9,<EOF>",110))
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("1. .35 0.0","1.,.35,0.0,<EOF>",111))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("1.E6 .4e-5 12e9","1.E6,.4e-5,12e9,<EOF>",112))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("0012e-09 044E99","0012e-09,044E99,<EOF>",113))
    def test_invalid_float(self):
        self.assertTrue(TestLexer.checkLexeme("e-12 143e","e,-,12,143,e,<EOF>",114))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("string.0E25 bUndl3e5","string,.0E25,bUndl3e5,<EOF>",115))
   
    def test_boolean(self):
        """Boolean literals tests"""
        self.assertTrue(TestLexer.checkLexeme("true false","true,false,<EOF>",116))
    def test_boolean_1(self):
        self.assertTrue(TestLexer.checkLexeme("_pa55w0rd true&","_pa55w0rd,true,Error Token &",117))
   
    def test_string(self):
        """String literals tests"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello world!" ""","""hello world!,<EOF>""",118))
    def test_str_escseq(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Run\\n Run\\n BTSRun!!!" ""","""Run\\n Run\\n BTSRun!!!,<EOF>""",119))
    def test_str_escseq_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a\\tb\\f\\b%33\\r\\"hello" """, """a\\tb\\f\\b%33\\r\\"hello,<EOF>""",120))
    def test_str_escseq_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\"\\""hello ""","""\\\\\\"\\",hello,<EOF>""",121))
   
    def test_unclosed_str(self):
        """Unclosed String tests"""
        self.assertTrue(TestLexer.checkLexeme(""" "Unclosed\nString!" ""","""Unclosed String: Unclosed""",122))
    def test_unclosed_str_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is the end ""","""Unclosed String: This is the end """,123))
    def test_unclosed_str_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Carriage\rReturn" ""","""Unclosed String: Carriage""",124))
    def test_unclosed_str_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" Abc123\n"Hello\r"World ""","""Abc123,Unclosed String: Hello""",125))
    def test_unclosed_str_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" Bypass \r "Abyss\\t (R00t)\\b""","""Bypass,Unclosed String: Abyss\\t (R00t)\\b""",126))
    def test_unclosed_str_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" Bypass \n \"""","""Bypass,Unclosed String: """,127))
   
    def test_illegal_esc(self):
        """Illegal Escape tests"""
        self.assertTrue(TestLexer.checkLexeme(""" "Illegal\\Escape!" ""","""Illegal Escape In String: Illegal\\E""",128))
    def test_illegal_esc_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "SUGA\\!" ""","""Illegal Escape In String: SUGA\\!""",129))
    def test_illegal_esc_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\ " ""","""Illegal Escape In String: \\ """,130)) 
    def test_illegal_esc_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" Newline "\\\n (R00t)\\b" ""","""Newline,Illegal Escape In String: \\\n""",131))
    def test_illegal_esc_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\a\\" ""","""Illegal Escape In String: abc\\a""",132))       
    
    def test_WS(self):
        """White Space tests"""
        self.assertTrue(TestLexer.checkLexeme("\b","Error Token \b",133))
    def test_WS_1(self):
        self.assertTrue(TestLexer.checkLexeme("\t\t\r","<EOF>",134))
    def test_WS_2(self):
        self.assertTrue(TestLexer.checkLexeme("\n\t\f","Error Token \f",135))
    def test_WS_3(self):
        self.assertTrue(TestLexer.checkLexeme("\r\tProgramming\nLanguages and Principle  \t","Programming,Languages,and,Principle,<EOF>",136))
    
    def test_comment(self):
        """Comment tests"""
        self.assertTrue(TestLexer.checkLexeme("//1.$ Line comment \n /* 2# Block \ncomment*/","<EOF>",137))
    def test_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("int _i23 // Declare var", "int,_i23,<EOF>",138))
    def test_line_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("/////ab^^&\\\\/*\n*/","*,/,<EOF>",139))
    def test_block_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""foo("In/*out*/put") /* Function\n foo&&% \n*/ ""","foo,(,In/*out*/put,),<EOF>",140))
    def test_block_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("""/* Asterisk ***/*//* \n slash/**/ Hello ""","*,slash,Hello,<EOF>",141))
    def test_ambiguous_cmttype(self):
        self.assertTrue(TestLexer.checkLexeme("//Ambiguous/*case \n can happen*/","can,happen,*,/,<EOF>",142))
    def test_ambiguous_cmttype_1(self):
        self.assertTrue(TestLexer.checkLexeme("/*Another/*\n\\*!case //\n//*/","<EOF>",143))
    def test_ambiguous_cmttype_2(self):
        self.assertTrue(TestLexer.checkLexeme("/*Line1\rLine2\t*/ //Line3","<EOF>",144))
    
    def test_declaration(self):
        """Declaration element tests"""
        self.assertTrue(TestLexer.checkLexeme("bool a; int Arr[6];","bool,a,;,int,Arr,[,6,],;,<EOF>",145))
    def test_declaration_var(self):
        self.assertTrue(TestLexer.checkLexeme("int i,k[5];","int,i,,,k,[,5,],;,<EOF>",146))
    def test_declaration_var1(self):
        self.assertTrue(TestLexer.checkLexeme(" void floatlit=9.e-08","void,floatlit,=,9.e-08,<EOF>",147))
    def test_declaration_var2(self):
        self.assertTrue(TestLexer.checkLexeme(""" str"123Boolean" ""","str,123Boolean,<EOF>",148))
    def test_declaration_func(self):
        self.assertTrue(TestLexer.checkLexeme("int foo(){}","int,foo,(,),{,},<EOF>",149))
    def test_declaration_func1(self):
        self.assertTrue(TestLexer.checkLexeme("void foo(int i[]) { i+1 ","void,foo,(,int,i,[,],),{,i,+,1,<EOF>",150))
    def test_declaration_func2(self):
        self.assertTrue(TestLexer.checkLexeme("v 2e5a() { float b(i) }","v,2e5,a,(,),{,float,b,(,i,),},<EOF>",151))
    def test_declaration_func3(self):
        self.assertTrue(TestLexer.checkLexeme("int[] k(int i, int ) // Error","int,[,],k,(,int,i,,,int,),<EOF>",152))
    
    def test_expr(self):
        """Expressions tests"""
        self.assertTrue(TestLexer.checkLexeme("a+2e.9-foo[8]","a,+,2,e,.9,-,foo,[,8,],<EOF>",153))
    def test_expr_op1(self):
        self.assertTrue(TestLexer.checkLexeme("-25*/0.e-3+a[b]","-,25,*,/,0.e-3,+,a,[,b,],<EOF>",154))
    def test_expr_op2(self):
        self.assertTrue(TestLexer.checkLexeme("false&&2+5","false,&&,2,+,5,<EOF>",155))
    def test_expr_op3(self):
        self.assertTrue(TestLexer.checkLexeme("%bn+-8|| a > 0.0","%,bn,+,-,8,||,a,>,0.0,<EOF>",156))
    def test_expr_op4(self):
        self.assertTrue(TestLexer.checkLexeme("""true=("i = %d, &i = %x", i, &i)""","""true,=,(,i = %d, &i = %x,,,i,,,Error Token &""",157))
    def test_expr_op5(self):
        self.assertTrue(TestLexer.checkLexeme("""1 = 0.e-10 != true""", "1,=,0.e-10,!=,true,<EOF>",158))
    def test_expr_op6(self):
        self.assertTrue(TestLexer.checkLexeme("a /*first*/ --b //unary","a,-,-,b,<EOF>",159))
    def test_expr_arr1(self):
        self.assertTrue(TestLexer.checkLexeme("foo(2)[3+x] = a[b[2]]+3","foo,(,2,),[,3,+,x,],=,a,[,b,[,2,],],+,3,<EOF>",160))
    def test_expr_arr2(self):
        self.assertTrue(TestLexer.checkLexeme("(a+b)[1-y*3] //test2","(,a,+,b,),[,1,-,y,*,3,],<EOF>",161))
    def test_expr_invoke1(self):
        self.assertTrue(TestLexer.checkLexeme("float y[10] foo(y);","float,y,[,10,],foo,(,y,),;,<EOF>",162))
    def test_expr_invoke2(self):
        self.assertTrue(TestLexer.checkLexeme(""" return putString("param")  ""","return,putString,(,param,),<EOF>",163))
    
    def test_stmt(self):
        """Statements tests"""
        self.assertTrue(TestLexer.checkLexeme("""int main() {print(Hello\n world );}""","int,main,(,),{,print,(,Hello,world,),;,},<EOF>",164))
    def test_if_stmt(self):
        self.assertTrue(TestLexer.checkLexeme(""" if (true) \n a+x[t-7] ""","if,(,true,),a,+,x,[,t,-,7,],<EOF>",165))
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme(""" if (_else) IF=-9 //cmt\n else \n "run!" ""","if,(,_else,),IF,=,-,9,else,run!,<EOF>",166))
    def test_do_while(self):
        self.assertTrue(TestLexer.checkLexeme("do a >= b % 99 while(!true)","do,a,>=,b,%,99,while,(,!,true,),<EOF>",167))
    def test_do_while1(self):
        self.assertTrue(TestLexer.checkLexeme("""{ do Do !+== * _while while("do"/*str*/)""","{,do,Do,!,+,==,*,_while,while,(,do,),<EOF>",168))
    def test_for_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("for(int i = 0; i< n; i+=1){}","for,(,int,i,=,0,;,i,<,n,;,i,+,=,1,),{,},<EOF>",169))
    def test_for_stmt1(self):
        self.assertTrue(TestLexer.checkLexeme(" for(for12, true,) break; ^","for,(,for12,,,true,,,),break,;,Error Token ^",170))
    def test_break_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("//test break\n break;","break,;,<EOF>",171))
    def test_continue_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("continue12 _continue continue;","continue12,_continue,continue,;,<EOF>",172))
    def test_return(self):
        self.assertTrue(TestLexer.checkLexeme("if (!return_1==b) return;","if,(,!,return_1,==,b,),return,;,<EOF>",173))
    def test_block_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""{block 1 = "Run BTS!" {blk 2 e.98-pow(a,2)%t} return "bias"+"SUGA"}""","{,block,1,=,Run BTS!,{,blk,2,e,.98,-,pow,(,a,,,2,),%,t,},return,bias,+,SUGA,},<EOF>",174))

    def test_all(self):
        """Combine tests"""
        self.assertTrue(TestLexer.checkLexeme("""//Linecmt\n "\n" Run#""","Unclosed String: ",175))
    def test_all1(self):
        self.assertTrue(TestLexer.checkLexeme("""int main(){ \n a = "Hello World" /*typical line*/; \n}""","int,main,(,),{,a,=,Hello World,;,},<EOF>",176))
    def test_all2(self):
        self.assertTrue(TestLexer.checkLexeme("int[] _mod2(int a, float t) { t = a%2 + 0.0e-0; continue;","int,[,],_mod2,(,int,a,,,float,t,),{,t,=,a,%,2,+,0.0e-0,;,continue,;,<EOF>",177))
    def test_all3(self):
        self.assertTrue(TestLexer.checkLexeme("//Cmt line 1 /*SUGA*/ \n foo(25)[a+9*x] >>= # begin","foo,(,25,),[,a,+,9,*,x,],>,>=,Error Token #",178))
    def test_all4(self):
        self.assertTrue(TestLexer.checkLexeme("""/* Print\r greetings // \\\\ */ print("Hey there**^^ " \"me .5e13) ""","print,(,Hey there**^^ ,Unclosed String: me .5e13) ",179))
    def test_all5(self):
        self.assertTrue(TestLexer.checkLexeme("ksd34 D8.e2SF 45S^dx ==+q&$","ksd34,D8,Error Token .",180))
    def test_all6(self):
        self.assertTrue(TestLexer.checkLexeme(""" str = "Bangya bangya bang bang ya \\!" ep= 01; ""","str,=,Illegal Escape In String: Bangya bangya bang bang ya \\!",181))
    def test_all7(self):
        self.assertTrue(TestLexer.checkLexeme(""" ===>/*RSA*/<=== // Checksum \t\b\n + "can't"[run,walk] then 1E2;3 just ***crawl(12.e04)***""","==,=,>,<=,==,+,can't,[,run,,,walk,],then,1E2,;,3,just,*,*,*,crawl,(,12.e04,),*,*,*,<EOF>",182))
    def test_all8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "How::about some PPL?!" + "Nice!" == "Exploit"+"Just read book" => will that be enough!? ""","How::about some PPL?!,+,Nice!,==,Exploit,+,Just read book,=,>,will,that,be,enough,!,Error Token ?",183))
    def test_all9(self):
        self.assertTrue(TestLexer.checkLexeme("""{{{ brackets[has(s0_many=_type)]}} - int[]; >><<""","{,{,{,brackets,[,has,(,s0_many,=,_type,),],},},-,int,[,],;,>,>,<,<,<EOF>",184))
    def test_all10(self):
        self.assertTrue(TestLexer.checkLexeme(""" //Does an emty /\\\\*^string^//*/ c0unt?! \n "  " {{"How bout unclosed ?! \r}} ""","  ,{,{,Unclosed String: How bout unclosed ?! ",185))
    def test_all11(self):
        self.assertTrue(TestLexer.checkLexeme("""boolean[2]={true,false} life_aint0011.56e34 /bout w1n(yes) 0r lose(0)["0..2\\ "]""","boolean,[,2,],=,{,true,,,false,},life_aint0011,.56e34,/,bout,w1n,(,yes,),0,r,lose,(,0,),[,Illegal Escape In String: 0..2\\ ",186))
    def test_all12(self):
        self.assertTrue(TestLexer.checkLexeme("aAbc123 123_dEf_/*////\n//**\n***/ \n ,-+*/%;\"  ","aAbc123,123,_dEf_,,,-,+,*,/,%,;,Unclosed String:   ",187))
    def test_all13(self):
        self.assertTrue(TestLexer.checkLexeme("unsigned int gate1=gate2=gate3=20;\nsigned int start=sm=0;","unsigned,int,gate1,=,gate2,=,gate3,=,20,;,signed,int,start,=,sm,=,0,;,<EOF>",188))
    def test_all14(self):
        self.assertTrue(TestLexer.checkLexeme("""int x;\nx = 3+= 3.14;\nPI(3.14)// the assignment operation\r (x+3.14), . */""","int,x,;,x,=,3,+,=,3.14,;,PI,(,3.14,),(,x,+,3.14,),,,Error Token .",189))
    def test_all15(self):
        self.assertTrue(TestLexer.checkLexeme("if(expression) {\n___ //\n___,,,+++ // operation1\n^@^}//\nelse\noperation2","if,(,expression,),{,___,___,,,,,,,+,+,+,Error Token ^",190))
    def test_all16(self):
        self.assertTrue(TestLexer.checkLexeme(" _ab=n%10;\n sum=sum+recursive(r*r/r);\n n=n/10; ","_ab,=,n,%,10,;,sum,=,sum,+,recursive,(,r,*,r,/,r,),;,n,=,n,/,10,;,<EOF>",191))
    def test_all17(self):
        self.assertTrue(TestLexer.checkLexeme("*p += q[12 * a] + -24 * b++;","*,p,+,=,q,[,12,*,a,],+,-,24,*,b,+,+,;,<EOF>",192))
    def test_all18(self):
        self.assertTrue(TestLexer.checkLexeme("""(<)(=)* or (>)(=)* "b. (< \\| >)=? c. > | >= | < | <=""","(,<,),(,=,),*,or,(,>,),(,=,),*,Illegal Escape In String: b. (< \\|",193))
    def test_all19(self):
        self.assertTrue(TestLexer.checkLexeme("float[] PPL(a+x/3)\n *p = q[12] + -24 * (10.3e5 - 32); |&","float,[,],PPL,(,a,+,x,/,3,),*,p,=,q,[,12,],+,-,24,*,(,10.3e5,-,32,),;,Error Token |",194))
    def test_all20(self):
        self.assertTrue(TestLexer.checkLexeme(""" str="Terminating Char \\0"; ""","str,=,Illegal Escape In String: Terminating Char \\0",195))
    def test_all21(self):
        self.assertTrue(TestLexer.checkLexeme("""CTF{""CaP7ur3_7h3_Flag"} \n Submit""","CTF,{,,CaP7ur3_7h3_Flag,Unclosed String: } ",196))
    def test_all22(self):
        self.assertTrue(TestLexer.checkLexeme("""(67 {fvour[] dashik}), gh"p@st3B!n" tenshi_44 E1.5 ""","(,67,{,fvour,[,],dashik,},),,,gh,p@st3B!n,tenshi_44,E1,.5,<EOF>",197))
    def test_all23(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Randomly \\nDirichlet\\tRegression\\f\\r\\\\" + "\\"" ""","""Randomly \\nDirichlet\\tRegression\\f\\r\\\\,+,\\",<EOF>""",198))
    def test_all24(self):
        self.assertTrue(TestLexer.checkLexeme(""" "RM_c+\\Rj" ""","""Illegal Escape In String: RM_c+\\R""",199))
    def test_all25(self):
        self.assertTrue(TestLexer.checkLexeme(""" float Effort; do{ k33p _in "m!nd" that[100%]("Programming Languages are beautiful!") } while(Effort <= 100.0e100); Forwarding => ___EndGame___""","float,Effort,;,do,{,k33p,_in,m!nd,that,[,100,%,],(,Programming Languages are beautiful!,),},while,(,Effort,<=,100.0e100,),;,Forwarding,=,>,___EndGame___,<EOF>",200))

    