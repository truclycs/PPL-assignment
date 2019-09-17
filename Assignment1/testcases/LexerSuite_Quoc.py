import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abcde""","abcde,<EOF>",100))
    def test_lower_upper_id1(self):
        self.assertTrue(TestLexer.checkLexeme("""A12_12A""","A12_12A,<EOF>",101))
    def test_lower_upper_id2(self):
        self.assertTrue(TestLexer.checkLexeme("""AcdBd""","AcdBd,<EOF>",102))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("""aA?sVN""","aA,Error Token ?",103))
    def test_letter_digit(self):
        self.assertTrue(TestLexer.checkLexeme("""Ab1c23Bc""", "Ab1c23Bc,<EOF>",104))
    def test_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("""__123bc""","__123bc,<EOF>", 105))
    def test_digitfirst(self):
        self.assertTrue(TestLexer.checkLexeme("""123_Abc123""","123,_Abc123,<EOF>", 106))
    def test_ID1(self):
        self.assertTrue(TestLexer.checkLexeme("""123+abc""","123,+,abc,<EOF>", 107))
    def test_ID2(self):
        self.assertTrue(TestLexer.checkLexeme("""BcA_45ab_Ab4""","BcA_45ab_Ab4,<EOF>", 108))
    def test_ID3(self):
        self.assertTrue(TestLexer.checkLexeme("""123_Abc123""","123,_Abc123,<EOF>", 109))
    def test_ID4(self):
        self.assertTrue(TestLexer.checkLexeme("""123+deg==abc""","123,+,deg,==,abc,<EOF>", 110))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""9453""","9453,<EOF>",111))
    def test_integer_letter(self):
        self.assertTrue(TestLexer.checkLexeme("""34#13""","34,Error Token #",112))
    def test_integer1(self):
        self.assertTrue(TestLexer.checkLexeme("""+-186""","+,-,186,<EOF>",113))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("""-621""","-,621,<EOF>",114))
    def test_floatlit_lower(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("""5.62e-18""","5.62e-18,<EOF>",115))
    def test_floatlit_upper(self):
        self.assertTrue(TestLexer.checkLexeme("""32.56E13""","32.56E13,<EOF>",116))
    def test_float_without_expo(self):
        self.assertTrue(TestLexer.checkLexeme("""8.001""","8.001,<EOF>",117))
    def test_float_fraction(self):
        self.assertTrue(TestLexer.checkLexeme(""".001""",".001,<EOF>",118))
    def test_float_wholenum(self):
        self.assertTrue(TestLexer.checkLexeme("""134.""","134.,<EOF>",119))
    def test_float_wholenum_expo(self):
        self.assertTrue(TestLexer.checkLexeme("""1e-35""","1e-35,<EOF>",120))
    def test_float_fraction_expo(self):
        self.assertTrue(TestLexer.checkLexeme(""".3E19""",".3E19,<EOF>",121))
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("""0.93E-5""","0.93E-5,<EOF>",122))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("""543e57""","543e57,<EOF>",123))
    def test_float_wrong(self):
        self.assertTrue(TestLexer.checkLexeme("""e-35""","e,-,35,<EOF>",124))
    def test_float_wrong2(self):
        self.assertTrue(TestLexer.checkLexeme("""145e""","145,e,<EOF>",125))
    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("""1+1.3e-5""","1,+,1.3e-5,<EOF>",126))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("""0.34E2==.0007 ""","0.34E2,==,.0007,<EOF>",127))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("""1.59 / 5E12 == 945.""","1.59,/,5E12,==,945.,<EOF>",128))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("""12E12 + e3""","12E12,+,e3,<EOF>",129))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("""12.r54 + 3e""","12.,r54,+,3,e,<EOF>",130))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("""12E45e54""","12E45,e54,<EOF>",131))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("""789e-12-45""","789e-12,-,45,<EOF>",132))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme(""".4e4-5e5""",".4e4,-,5e5,<EOF>",133))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("""0.3ee23""","0.3,ee23,<EOF>",134))
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme("""0.004@e-12 ""","0.004,Error Token @",135))
    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme(""".45;1e-53""",".45,;,1e-53,<EOF>",136))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("""e145 + .54e-12""","e145,+,.54e-12,<EOF>",137))



    
    

    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abchd" ""","""abchd,<EOF>""",138))
    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "12AbC"123"KL" ""","""12AbC,123,KL,<EOF>""",139))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1="ABC"+"abc" ""","""1,=,ABC,+,abc,<EOF>""",140))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 3*4=="3.19" ""","""3,*,4,==,3.19,<EOF>""",141))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "A" "B" "C" "1" "2" ""","""A,B,C,1,2,<EOF>""",142))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" true"1+3=5"Abc ""","""true,1+3=5,Abc,<EOF>""",143))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "return123"true ""","""return123,true,<EOF>""",144))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "(A+b)=C"*3 ""","""(A+b)=C,*,3,<EOF>""",145))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123cbd"" ""","""123,cbd,,<EOF>""",146))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "//t;Abc" ""","""//t;Abc,<EOF>""",147))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.3e3 + "1.3e3" "" ""","""1.3e3,+,1.3e3,,<EOF>""",148))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" 14E12 - "" ""","""14E12,-,,<EOF>""",149))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "0.0.4""==1"23""","""0.0.4,==1,23,<EOF>""",150))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "[A-Z]+1"Cd_a ""","""[A-Z]+1,Cd_a,<EOF>""",151))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "A_86+/"23N ""","""A_86+/,23,N,<EOF>""",152))
    


    def test_string_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "try\\t3c2" ""","""try\\t3c2,<EOF>""",153))
    def test_string_legal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t\\f45" ""","""\\t\\f45,<EOF>""",154))
    def test_string_legal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc"\\f"123 ""","""abc,\\f,123,<EOF>""",155))
    def test_string_legal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123"\\\\nmo""\\n" ""","""123,\\\\nmo,\\n,<EOF>""",156))
    def test_string_legal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t+3.7" ""","""\\t+3.7,<EOF>""",157))
    def test_string_legal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\f_Ab_cd*" ""","""\\f_Ab_cd*,<EOF>""",158))
    def test_string_legal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "53\\\\4"+"" ""","""53\\\\4,+,,<EOF>""",159))
    def test_string_legal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\"g_53\\"G4" ""","""\\"g_53\\"G4,<EOF>""",160))
    def test_string_legal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\t+-3.6"  ""","""\\\\\\t+-3.6,<EOF>""",161))
    def test_string_legal_escape10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\r+3\\f"  ""","""\\r+3\\f,<EOF>""",162))
    def test_string_legal_escape11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t;"+"\\f)"  ""","""\\t;,+,\\f),<EOF>""",163))
    def test_string_legal_escape12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\""  ""","""\\",<EOF>""",164))
    def test_string_legal_escape13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\"\\"_123"  ""","""\\"\\"_123,<EOF>""",165))
    def test_string_legal_escape14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "A_b\\"\\t+1" ""","""A_b\\"\\t+1,<EOF>""",166))
    def test_string_legal_escape15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\r+3\\f"  ""","""\\r+3\\f,<EOF>""",167))
    def test_string_legal_escape16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\"\\t\\""  ""","""\\"\\t\\",<EOF>""",168))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Abr3c2 ""","""Unclosed String: Abr3c2 """,169))
    def test_unclose_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""b"22Trn """,""",b,Unclosed String: 22Trn """,170))
    def test_unclose_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "45t\\""ter"12 ""","""45t\\",ter,Unclosed String: 12 """,171))
    def test_unclose_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t\\f ""","""Unclosed String: \\t\\f """,172))
    def test_unclose_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " """,""",Unclosed String:  """,173))
    def test_unclose_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" _v23"\\" ""","""_v23,Unclosed String: \\" """,174))
    def test_unclose_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "1*/3\\" ""","""Unclosed String: 1*/3\\" """,175))
    def test_unclose_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" V_3"\\\\\\" ""","""V_3,Unclosed String: \\\\\\" """,176))
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123ab\\m2137" ""","""Illegal Escape In String: 123ab\\m""",177))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "fgg"123"\\o2137" ""","""fgg,123,Illegal Escape In String: \\o""",178))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ab"23\\k" ""","""ab,Illegal Escape In String: 23\\k""",179))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "V_13\\\\\\o" ""","""Illegal Escape In String: V_13\\\\\\o""",180))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\y123" ""","""Illegal Escape In String: \\y""",181))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t\\l" ""","""Illegal Escape In String: \\t\\l""",182))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc" + "\\g" ""","""abc,+,Illegal Escape In String: \\g""",183))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\d + \\t" ""","""Illegal Escape In String: \\d""",184))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aB_c+\\h" ""","""Illegal Escape In String: aB_c+\\h""",185))

    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" tfh23 "5a\\\\123" ""","""tfh23,5a\\\\123,<EOF>""",186))
    def test_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abd254\\"wr" ""","""abd254\\"wr,<EOF>""",187))
    def test_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b\\f\\r\\n\\t\\"\\\\" ""","""\\b\\f\\r\\n\\t\\"\\\\,<EOF>""",188))
    def test_legal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h ""","""Illegal Escape In String: abc\\h""",189))
    
    
    def test_expression(self):
        self.assertTrue(TestLexer.checkLexeme(""" x + y=10 ""","""x,+,y,=,10,<EOF>""",190))
    def test_expression1(self):
        self.assertTrue(TestLexer.checkLexeme("""12a3 + 123AB""","12,a3,+,123,AB,<EOF>", 191))
    def test_expression2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "x + y = 10" ""","""x + y = 10,<EOF>""",192))
    def test_expression3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.e34 - "\\t" ""","""1.e34,-,\\t,<EOF>""",193))
    def test_expression4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\ abcs" ""","""Illegal Escape In String: \\ """,194))
    def test_expression5(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123\\ ""","""123,Error Token \\""",195))
    def test_expression6(self):
        self.assertTrue(TestLexer.checkLexeme(""" a_b' ""","""a_b,Error Token '""",196))
    def test_expression7(self):
        self.assertTrue(TestLexer.checkLexeme(""" (3+1)*"\\t" ""","""(,3,+,1,),*,\\t,<EOF>""",197))
    def test_expression8(self):
        self.assertTrue(TestLexer.checkLexeme(""" Ans34 ==== Mon ""","""Ans34,==,==,Mon,<EOF>""",198))
    def test_expression9(self):
        self.assertTrue(TestLexer.checkLexeme(""" Tks >= 123 || 34 && 47 ""","""Tks,>=,123,||,34,&&,47,<EOF>""",199))
    
    
    