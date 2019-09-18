import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):	

# ------------------------------ ID--------------------------------
	
	def testID1(self):
		inp = "PPL"
		out = "PPL,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 101))  

	def testID2(self):
		inp = "int main(int x, int y, int z) { return 0;}"
		out = "int,main,(,int,x,,,int,y,,,int,z,),{,return,0,;,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 102))

	def testID3(self):
		inp = "trucly1802"
		out = "trucly1802,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 103))

	def testID4(self):
		inp = "1802trucly++"
		out = "1802,trucly,+,+,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 104))

	def testID5(self):
		inp = "123TV123"
		out = "123,TV123,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 105))

	def testID6(self):
		inp = "int    float     boolean  for 123breakifdowhile277"
		out = "int,float,boolean,for,123,breakifdowhile277,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 106))
    
	def testID7(self):
		inp = "123,;[]{}1507()"
		out = "123,,,;,[,],{,},1507,(,),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 107))

# -----------------------------STRING------------------------------
	def testString1(self):
		inp = """ "NTTL\\nVTT" """
		out = "NTTL\\nVTT,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 108))
	
	def testString2(self):
		inp = """ "NTTL" """
		out = "NTTL,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 109))
	
	def testString3(self):
		inp = """ 123abc "NTTL\\\\PPL" "122" 11+ """
		out = """123,abc,NTTL\\\\PPL,122,11,+,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp, out, 110))
	
	def testString4(self):
		inp = """ "T\\rV" """
		out = """T\\rV,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp, out, 111))
	
	def testString5(self):
		inp = """ "^^ NGUYEN   THI    TRUC    LY ^^" """
		out = "^^ NGUYEN   THI    TRUC    LY ^^,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 112))

	def testString6(self):
		inp = """ "PPL\n" """ 
		out = "Unclosed String: PPL"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 113))
	
	def testString7(self):
		inp = """ 1 "TL"""
		out = "1,Unclosed String: TL"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 114))

	def testString8(self):
		inp = """ 5 "TL """
		out = "5,Unclosed String: TL "
		self.assertTrue(TestLexer.checkLexeme(inp, out, 115))
	
	def testString9(self):
		inp = """ 0 "TL\r" """
		out = "0,Unclosed String: TL"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 116))

	def testString(self):
		inp = """ "+_)(*&^%$#@!P|)" """
		out = "+_)(*&^%$#@!P|),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 117))
	
	def testString10(self):
		inp = """ 7 "UnclosedString?\\" """
		out = """7,Unclosed String: UnclosedString?\\" """
		self.assertTrue(TestLexer.checkLexeme(inp, out, 118))

	def testString11(self):
		inp = "!@#$%^&yujk0]-*()"
		out = "!,Error Token @"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 119))

	def testString12(self):
		inp = "Why?"
		out = "Why,Error Token ?"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 120))

	def testString13(self):
		inp = "..."
		out = "Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 121))

	def testString14(self):
		inp = """  "Lazy \\s" """
		out = "Illegal Escape In String: Lazy \s"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 122))

	def testString15(self):
		inp = """  "Lazy \\s" """
		out = "Illegal Escape In String: Lazy \s"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 123))

	def testString16(self):
		inp = """ "BK \\a" """
		out = """Illegal Escape In String: BK \\a"""
		self.assertTrue(TestLexer.checkLexeme(inp, out, 124))

	def testString17(self):
		inp = """ "CSE \\n BK" """
		out = """CSE \\n BK,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp, out, 125))

	def testString18(self):
		inp = """ "CSE \n BK" """
		out = """Unclosed String: CSE """
		self.assertTrue(TestLexer.checkLexeme(inp, out, 126))

	def testString19(self):
		inp = """ "CSE \\zzz BK" """
		out = """Illegal Escape In String: CSE \z"""
		self.assertTrue(TestLexer.checkLexeme(inp, out, 127))

	def testString20(self):
		inp = """ "LAST!!! ^_^ '_' ~_~ @_@ =.= !_!" """
		out = "LAST!!! ^_^ '_' ~_~ @_@ =.= !_!,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 128))

# # --------------------------OPERATOR -------------------------

	def testOP1(self):
		inp = "a % b"
		out = "a,%,b,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 129))
	
	def testOP2(self):
		inp = "a = b + c"
		out = "a,=,b,+,c,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 130))
	
	def testOP3(self):
		inp = "+-*/"
		out = "+,-,*,/,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 131))
	
	def testOP4(self):
		inp = "foo(2)[3+x]=a[b[5]]+2;"
		out = "foo,(,2,),[,3,+,x,],=,a,[,b,[,5,],],+,2,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 132))

	def testOP5(self):
		inp = "==!=>=<=<>&&||!"
		out = "==,!=,>=,<=,<,>,&&,||,!,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 133))

	def testOP6(self):
		inp = "a[b[c[d[a + b + 2 * c + d]]]] = x * y / z + 5 - 6;"
		out = "a,[,b,[,c,[,d,[,a,+,b,+,2,*,c,+,d,],],],],=,x,*,y,/,z,+,5,-,6,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 134))

	def testOP7(self):
		inp = "a + b = c => a = c - b"
		out = "a,+,b,=,c,=,>,a,=,c,-,b,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 135))

	def testOP8(self):
		inp = """abbb/*654+8hkl;l-2&*RAWoir2][lpsdk"{IPP#"p3[]"" """
		out = "abbb,/,*,654,+,8,hkl,;,l,-,2,Error Token &"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 136))

	def testOP9(self):
		inp = ";,km83po[)(*&^%QW#)+6]"
		out = ";,,,km83po,[,),(,*,Error Token &"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 137))

	def testOP10(self):
		inp = "{a[b + c / (d - e)] - x} % 18 = 123, @_@ ^_^"
		out = "{,a,[,b,+,c,/,(,d,-,e,),],-,x,},%,18,=,123,,,Error Token @"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 138))

# ----------------------------COMMENT------------------------------
	def testComment1(self):
		inp = """//This is a line commnent!"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 139))
	
	def testComment2(self):
		inp = """/*This is a block comment*/"""
		out = "<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 140))
	
    
	def testComment3(self):
		inp = """//This is a line commnent///////// Still comment line"""
		out = "<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 141))
	
	def testComment4(self):
		inp = """//This is a line commnent//
        //
        //
        /// Still comment line"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 142))
	
	def testComment5(self):
		inp = """/********This is a block comment???*/"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 143))

	def testComment6(self):
		inp = """/******This is \\n
   			            a block comment
   		                in many lines*/"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 144))

# -----------------------------FLOAT-------------------------------

	def testFloat1(self):
		inp = "1507."
		out = "1507.,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 145))

	def testFloat2(self):
		inp = ".1802"
		out = ".1802,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 146))

	def testFloat3(self):
		inp = "15.07"
		out = "15.07,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 147))

	def testFloat4(self):
		inp = "15e07"
		out = "15e07,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 148))

	def testFloat5(self):
		inp = "15E07"
		out = "15E07,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 149))

	def testFloat6(self):
		inp = "-1507"
		out = "-,1507,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 150))

	def testFloat7(self):
		inp = "15e-7"
		out = "15e-7,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 151))

	def testFloat8(self):
		inp = "15E7 9.0"
		out = "15E7,9.0,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 152))

	def testFloat9(self):
		inp = "1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42"
		out = "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 153))

	def testFloat10(self):
		inp = "1.21..11e21.2E-21.2e-2.1E29.012e80.33E-3128e-42"
		out = "1.21,Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 154))

	def testFloat11(self):
		inp = "1.21.11e21.2E-21.2e-2.1E29.012e80.33E-3128e-42"
		out = "1.21,.11e21,.2E-21,.2e-2,.1E29,.012e80,.33E-3128,e,-,42,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 155))

	def testFloat12(self):
		inp = "e-12 113e"
		out = "e,-,12,113,e,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 156))

	def testFloat13(self):
		inp = "00000150721071802.15855e-131365.957"
		out = "00000150721071802.15855e-131365,.957,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 157))

	def testFloat14(self):
		inp = "12e-87+04.43-3E-341+428e-44-2"
		out = "12e-87,+,04.43,-,3E-341,+,428e-44,-,2,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 158))

	def testFloat15(self):
		inp = "11.2 11. .21 15e2"
		out = "11.2,11.,.21,15e2,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 159))
	
	def testFloat16(self):
		inp = "78.2E-2 234.2e-2 .155E2 9.10"
		out = "78.2E-2,234.2e-2,.155E2,9.10,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 160))
	
	def testFloat17(self):
		inp = "12e87 0.433E-34 1428e-442"
		out = "12e87,0.433E-34,1428e-442,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 161))
	
	def testFloat18(self):
		inp = "12e8704.433E-341428e-442"
		out ="12e8704,.433E-341428,e,-,442,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp, out, 162))
	
	def testFloat19(self):
		inp ="""12e8704.433E+341428e-+442"""
		out ="12e8704,.433,E,+,341428,e,-,+,442,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 163))
	
	def testFloat20(self):
		inp = "15.4.3+14E3.0+143e5+14.3e-5+14-3.e5+143.15e5"
		out = "15.4,.3,+,14E3,.0,+,143e5,+,14.3e-5,+,14,-,3.e5,+,143.15e5,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 164))

#------------------------------------------------------------------
	def test1(self):
		inp = """using namespace std;
				int main() {
					int n;
					cin >> n;
					int a[n], d[n] = {false};
					for (int i = 0; i < n; i++) {
						cin >> a[i];
					}
					sort(a, a + n);
					int res = 0;
					for (int i = 0; i < n; i++) {
						if (!d[i]) {
							res++;
							for (int j = i + 1; j < n; j++) {
								if (a[j] % a[i] == 0) {
									d[j] = true;
								}
							}
						}
					}
					cout << res;
					return 0;
				}"""
		out = "using,namespace,std,;,int,main,(,),{,int,n,;,cin,>,>,n,;,int,a,[,n,],,,d,[,n,],=,{,false,},;,for,(,int,i,=,0,;,i,<,n,;,i,+,+,),{,cin,>,>,a,[,i,],;,},sort,(,a,,,a,+,n,),;,int,res,=,0,;,for,(,int,i,=,0,;,i,<,n,;,i,+,+,),{,if,(,!,d,[,i,],),{,res,+,+,;,for,(,int,j,=,i,+,1,;,j,<,n,;,j,+,+,),{,if,(,a,[,j,],%,a,[,i,],==,0,),{,d,[,j,],=,true,;,},},},},cout,<,<,res,;,return,0,;,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 165))
		
	def test2(self):
		inp = """ "#include <iostream>
				using namespace std;" """
		out = "Unclosed String: #include <iostream>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 166))

	def test3(self):
		inp = " __Thoai Ngoc Hau__"
		out = "__Thoai,Ngoc,Hau__,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 167))

	def test4(self):
		inp = "__2014-2017__"
		out = "__2014,-,2017,__,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 168))

	def test5(self):
		inp ="""!a!a!a!a!a=!=!=aaa!<><>"""
		out ="!,a,!,a,!,a,!,a,!,a,=,!=,!=,aaa,!,<,>,<,>,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 169))

	def test6(self):
		inp = "boolean int float void string"
		out = "boolean,int,float,void,string,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 170))

	def test7(self):
		inp = """ PPL ppl PPL 123 456 "kssd" skldjf" """
		out = "PPL,ppl,PPL,123,456,kssd,skldjf,Unclosed String:  "
		self.assertTrue(TestLexer.checkLexeme(inp, out, 171))

	def test8(self):
		inp = """ "\\assignment PPL" """
		out = "Illegal Escape In String: \\a"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 172))

	def test9(self):
		inp = """ "\\n\\b\\f\\r" """
		out = "\\n\\b\\f\\r,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 173))


	def test10(self):
		inp = ")(*&^%$#@1489fghjkl;gvhbn.ml/;sdfpweik zmit03wepokfz/)"
		out = "),(,*,Error Token &"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 174))

	def test11(self):
		inp = ",/;'[]{}*/-+%&&8*()/21564khtn/;__8512"
		out = ",,/,;,Error Token '"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 175))

	def test12(self):
		inp = "cin >> x[i].first >> x[i].second;"
		out = "cin,>,>,x,[,i,],Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 176))

	def test13(self):
		inp = "for (int i = 0; i < n; i++) {"
		out = "for,(,int,i,=,0,;,i,<,n,;,i,+,+,),{,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 177))

	def test14(self):
		inp = """ cout << "YES"; """
		out = "cout,<,<,YES,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 178))

	def test15(self):
		inp = """ cout << "NO"; """
		out = "cout,<,<,NO,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 179))

	def test16(self):
		inp = """ "if (a[j] % a[i] == 0) {
                    d[j] = true;
            	}" """
		out = "Unclosed String: if (a[j] % a[i] == 0) {"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 180))

	def test17(self):
		inp = """ if (a[j] % a[i] == 0) {
                    d[j] = true;
            	} """
		out = "if,(,a,[,j,],%,a,[,i,],==,0,),{,d,[,j,],=,true,;,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 181))

	def test18(self):
		inp = "Bubble Cup 8 - Finals [Online Mirror]"
		out = "Bubble,Cup,8,-,Finals,[,Online,Mirror,],<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 182))

	def test19(self):
		inp = """return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";"""
		out = "return,(,+,to_string,(,get,<,0,>,(,p,),),+,, ,+,to_string,(,get,<,1,>,(,p,),),+,, ,+,to_string,(,get,<,2,>,(,p,),),+,),;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 183))

	def test20(self):
		inp = "double mid = 0.5 * (low + high);"
		out = "double,mid,=,0.5,*,(,low,+,high,),;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 184))

	def test21(self):
		inp = "if (t < segs[segs.size() - 2].t + segs.back().t) {"
		out = "if,(,t,<,segs,[,segs,Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 185))

	def test22(self):
		inp = "var g = Array(n, { ArrayList<Pair<Int, Int>>() })"
		out = "var,g,=,Array,(,n,,,{,ArrayList,<,Pair,<,Int,,,Int,>,>,(,),},),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 186))

	def test23(self):
		inp = "var knap = BooleanArray(sum + 1, {false})"
		out = "var,knap,=,BooleanArray,(,sum,+,1,,,{,false,},),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 187))

	def test24(self):
		inp = "private fun readDoubles() = readStrings().map { it.toDouble() } // list of doubles"
		out = "private,fun,readDoubles,(,),=,readStrings,(,),Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 188))

	def test25(self):
		inp = "if (dp[n - 1] <= 0) {"
		out = "if,(,dp,[,n,-,1,],<=,0,),{,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 189))

	def test26(self):
		inp = " vector<vector<int>> a(n, vector<int>(n));"
		out = "vector,<,vector,<,int,>,>,a,(,n,,,vector,<,int,>,(,n,),),;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 190))

	def test27(self):
		inp = "ios::sync_with_stdio(false); cin.tie(0);"
		out = "ios,Error Token :"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 191))

	def test28(self):
		inp = "f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1] - f[i][j] + (s[i][j] == '#');"
		out = "f,[,i,+,1,],[,j,+,1,],=,f,[,i,+,1,],[,j,],+,f,[,i,],[,j,+,1,],-,f,[,i,],[,j,],+,(,s,[,i,],[,j,],==,Error Token '"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 192))

	def test29(self):
		inp = "res = min(res, dp[i][j][ii][k] + dp[i][k + 1][ii][jj]);"
		out = "res,=,min,(,res,,,dp,[,i,],[,j,],[,ii,],[,k,],+,dp,[,i,],[,k,+,1,],[,ii,],[,jj,],),;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 193))

	def test30(self):
		inp = "ans += (long long) len * (len + 1) / 2;"
		out = "ans,+,=,(,long,long,),len,*,(,len,+,1,),/,2,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 194))

	def test31(self):
		inp = "mp[make_pair(foo, bar)]++;"
		out = "mp,[,make_pair,(,foo,,,bar,),],+,+,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 195))

	def test32(self):
		inp = "f[t-(1 shl (b[i]-1))]:=f[t-(1 shl (b[i]-1))]+f[t]*a[b[j],b[i]]/tot;"
		out = "f,[,t,-,(,1,shl,(,b,[,i,],-,1,),),],Error Token :"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 196))

	def test33(self):
		inp = "cin >> x[i].first >> x[i].second;"
		out = "cin,>,>,x,[,i,],Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 197))

	def test34(self):
		inp = "cin >> x[i].first >> x[i].second;"
		out = "cin,>,>,x,[,i,],Error Token ."
		self.assertTrue(TestLexer.checkLexeme(inp, out, 198))

	def test35(self):
		inp = "//  assign(output,'out'); rewrite(output);"
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 199))

	def test36(self):
		inp = "{R+,S+,Q+,I+,O-}"
		out = "{,R,+,,,S,+,,,Q,+,,,I,+,,,O,-,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp, out, 200))