import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # test_identifier  10_test
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("""abc""","""abc,<EOF>""",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("""aCBbdc""","""aCBbdc,<EOF>""",102))
    def test_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("""int aC_B""","""int,aC_B,<EOF>""",103))
    def test_id_2(self):
        self.assertTrue(TestLexer.checkLexeme("""1.9hello""","""1.9,hello,<EOF>""",104))
    def test_id_3(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e-23""","""1.e-23,<EOF>""",105))
    def test_id_4(self):
        # test dot, test id, test float
        self.assertTrue(TestLexer.checkLexeme("""float i = .e5""","""float,i,=,.,e5,<EOF>""",106)) 
    def test_id_5(self):
        self.assertTrue(TestLexer.checkLexeme("""int aC_B""","""int,aC_B,<EOF>""",107))
    def test_id_6(self):
        self.assertTrue(TestLexer.checkLexeme("""boolean ndhanam""","""boolean,ndhanam,<EOF>""",108))
    def test_id_7(self):
        self.assertTrue(TestLexer.checkLexeme("""void nguyen_dang_ha_nam3012""","""void,nguyen_dang_ha_nam3012,<EOF>""",109))
    def test_id_8(self):
        self.assertTrue(TestLexer.checkLexeme("""int io\\tth""","""int,io,Error Token \\""",110))

    # test_token 30_test
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("""aA?sVN""","""aA,Error Token ?""",111))
    def test_wrong_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("""@""","""Error Token @""",112))
    def test_wrong_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("""flase""","""flase,<EOF>""",113))
    def test_wrong_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("""true""","""true,<EOF>""",114))
    def test_wrong_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("""true123""","""true123,<EOF>""",115))
    def test_wrong_token_6(self):
        self.assertTrue(TestLexer.checkLexeme("""123true""","""123,true,<EOF>""",116))
    def test_wrong_token_7(self):
        self.assertTrue(TestLexer.checkLexeme(""".2e5""",""".2e5,<EOF>""",117))
    def test_wrong_token_8(self):
        self.assertTrue(TestLexer.checkLexeme(""".e5""",""".,e5,<EOF>""",118))
    def test_wrong_token_9(self):
        self.assertTrue(TestLexer.checkLexeme("""continue""","""continue,<EOF>""",119))
    def test_wrong_token_10(self):
        self.assertTrue(TestLexer.checkLexeme("""break""","""break,<EOF>""",120))
    def test_wrong_token_11(self):
        self.assertTrue(TestLexer.checkLexeme("""eheoeoe"odj""","""eheoeoe,Unclosed String: odj""",121))
    def test_wrong_token_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" void 55.2e5 ""","""void,55.2e5,<EOF>""",122))
    def test_wrong_token_13(self):
        self.assertTrue(TestLexer.checkLexeme("""ehe"oeoe"odj""","""ehe,oeoe,odj,<EOF>""",123))
    def test_wrong_token_14(self):
        self.assertTrue(TestLexer.checkLexeme("""eh"eoe\\noe"odj""","""eh,eoe\\noe,odj,<EOF>""",124))
    def test_wrong_token_15(self):
        self.assertTrue(TestLexer.checkLexeme("""test#test""","""test,Error Token #""",125))
    def test_wrong_token_16(self):
        self.assertTrue(TestLexer.checkLexeme("""test\test""","""test,est,<EOF>""",126))
    def test_wrong_token_17(self):
        self.assertTrue(TestLexer.checkLexeme("""tes\t\ntest""","""tes,test,<EOF>""",127))
    def test_wrong_token_18(self):
        self.assertTrue(TestLexer.checkLexeme(""" \\ ""","""Error Token \\""",128))  #?????
    def test_wrong_token_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" " ""","""Unclosed String:  """,129))
    def test_wrong_token_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",130))
    def test_wrong_token_21(self):
        self.assertTrue(TestLexer.checkLexeme("""  ""","""<EOF>""",131))
    def test_wrong_token_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.2 1. ""","""1.2,1.,<EOF>""",132))
    def test_wrong_token_23(self):
        self.assertTrue(TestLexer.checkLexeme(""" .3.23. """,""".3,.23,.,<EOF>""",133))    #?????
    def test_wrong_token_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" 4..34 ""","""4.,.34,<EOF>""",134))   #????
    def test_wrong_token_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5..65 ""","""5.,.65,<EOF>""",135))
    def test_wrong_token_26(self):
        self.assertTrue(TestLexer.checkLexeme(""" if_ ""","""if_,<EOF>""",136))
    def test_wrong_token_27(self):
        self.assertTrue(TestLexer.checkLexeme(""" void|25 ""","""void,Error Token |""",137))
    def test_wrong_token_28(self):
        self.assertTrue(TestLexer.checkLexeme("""comeback?""","""comeback,Error Token ?""",138))
    def test_wrong_token_29(self):
        self.assertTrue(TestLexer.checkLexeme("""come || back""","""come,||,back,<EOF>""",139))
    def test_wrong_token_30(self):
        self.assertTrue(TestLexer.checkLexeme("""comeback!""","""comeback,!,<EOF>""",140))
    
    
    # test_comment 10_test
    # test_line_comment    
    def test_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""//int 4""","""<EOF>""",141))
    def test_line_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""// ////////""","""<EOF>""",142))
    def test_line_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""// bbbb \\nhe\nha\nho\nhi\n""","""ha,ho,hi,<EOF>""",143))
    def test_line_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""// \5\\""","""<EOF>""",144))
    def test_line_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("""// \\//\\//\\//\\//\\//\\//\\//\\//""","""<EOF>""",145))
    #test_block_comment
    def test_block_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/* ~!@#$%^&*() */ int ahle""","""int,ahle,<EOF>""",146))
    def test_block_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""/* ~!@#$%^&*()\n\b\t\\o */ int""","""int,<EOF>""",147))
    def test_block_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""/* dsd""","""/,*,dsd,<EOF>""",148)) #???
    def test_block_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""chamhoi */ float""","""chamhoi,*,/,float,<EOF>""",149))
    def test_block_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" // h\n /* hhh */ int a""","""int,a,<EOF>""",150))
    
    
    # test_string 15_test
    def test_integer4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string Name = \"name\" ""","""string Name = ,name,Unclosed String:  """,151))   
    def test_integer5(self):
        self.assertTrue(TestLexer.checkLexeme("""string Name = "name""","string,Name,=,Unclosed String: name",152))  
    def test_integer6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string Name " ""","""string Name ,<EOF>""",153)) 
    def test_integer7(self):
        self.assertTrue(TestLexer.checkLexeme(" \"string \" ","string ,<EOF>",154))  
    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "12223a\\n123" ""","""12223a\\n123,<EOF>""",155))
    def test_unclose_string(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(""" "99123a\\n123 ""","""Unclosed String: 99123a\\n123 """,156))
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",157))
    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1293 "123a\\\\123" ""","""1293,123a\\\\123,<EOF>""",158))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""n2"\\\\o" """,""",n2,\\\\o,<EOF>""",159)) #??? \o
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""n2"\\ \\o" """,""",n2,Illegal Escape In String: \\ """,160)) #???
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\5123" ""","""Illegal Escape In String: 123a\\5""",161))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\n" ""","""\\n,<EOF>""",162))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\b" ""","""Unclosed String: """,163))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\r" ""","""Unclosed String: """,164))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\n" ""","""Unclosed String: """,165))

    # test_unclose_string 5_test
    def test_unclose_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a\\n1 ""","""Unclosed String: a\\n1 """,166))
    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "unclose\n ""","""Unclosed String: unclose""",167))
    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "un"close\n hh"2 ""","""un,close,hh,Unclosed String: 2 """,168))
    def test_unclose_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "un"close ""","""un,close,<EOF>""",169))
    def test_unclose_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" " ""","""Unclosed String:  """,170))
    
    # test_illegal_escape 5_test
    def test_illegal_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "un\\h ""","""Illegal Escape In String: un\\h""",171))
    def test_illegal_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ha\\n\\am" ""","""Illegal Escape In String: ha\\n\\a""",172))
    def test_illegal_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ha\\nam" ""","""ha\\nam,<EOF>""",173))
    def test_illegal_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ha\\na \\m" ""","""Illegal Escape In String: ha\\na \\m""",174))
    def test_illegal_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ha.nam\\." ""","""Illegal Escape In String: ha.nam\\.""",175))
    # test_statement 15_test

    def test_statement_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" if(a|b) ""","""if,(,a,Error Token |""",176))
    def test_statement_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" if(a == b) ""","""if,(,a,==,b,),<EOF>""",177))
    def test_statement_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" do(a == b) ""","""do,(,a,==,b,),<EOF>""",178))
    def test_statement_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" for(a != b) ""","""for,(,a,!=,b,),<EOF>""",179))
    def test_statement_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" continue(a == b) ""","""continue,(,a,==,b,),<EOF>""",180))
    def test_statement_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" continue; ""","""continue,;,<EOF>""",181))
    def test_statement_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" continue;442 ""","""continue,;,442,<EOF>""",182))
    def test_statement_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" break; ""","""break,;,<EOF>""",183))
    def test_statement_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" break0[0); ""","""break0,[,0,),;,<EOF>""",184))
    def test_statement_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" return[foo ""","""return,[,foo,<EOF>""",185))
    def test_statement_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" return -1; ""","""return,-,1,;,<EOF>""",186))
    def test_statement_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" nam(_"nguyendangha") ""","""nam,(,_,nguyendangha,),<EOF>""",187))
    def test_statement_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" nam[??]""","""nam,[,Error Token ?""",188))
    def test_statement_14(self):
        self.assertTrue(TestLexer.checkLexeme(""" python[0.2]?\\n? ""","""python,[,0.2,],Error Token ?""",189))
    def test_statement_15(self):
        self.assertTrue(TestLexer.checkLexeme(""" while(nam?) ""","""while,(,nam,Error Token ?""",190))

    # test_expression 10_test
    def test_exp_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5 == 56 ""","""5,==,56,<EOF>""",191))
    def test_exp_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" res = 56 + 5? ""","""res,=,56,+,5,Error Token ?""",192))
    def test_exp_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5 == 5/6 ""","""5,==,5,/,6,<EOF>""",193))
    def test_exp_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" res == 5 + (6*6); ""","""res,==,5,+,(,6,*,6,),;,<EOF>""",194))
    def test_exp_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" res = "res`" + "res'" ""","""res,=,res`,+,res',<EOF>""",195))
    def test_exp_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5 != 56 ""","""5,!=,56,<EOF>""",196))
    def test_exp_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5 |= 56 ""","""5,Error Token |""",197))
    def test_exp_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 4 || 4 ""","""4,||,4,<EOF>""",198))
    def test_exp_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" 'a' ""","""Error Token '""",199))
    def test_exp_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" 9 <= 10 ""","""9,<=,10,<EOF>""",200))