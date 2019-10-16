# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u012c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\3\2\3\2\3\3\3\3\6\3H\n\3\r")
        buf.write("\3\16\3I\3\4\3\4\3\4\3\4\7\4P\n\4\f\4\16\4S\13\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\5\5[\n\5\3\6\3\6\3\6\3\6\5\6a\n\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\7\7i\n\7\f\7\16\7l\13\7\3\b\3\b")
        buf.write("\3\b\3\b\5\br\n\b\3\t\3\t\3\t\5\tw\n\t\3\n\3\n\3\13\3")
        buf.write("\13\5\13}\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u0087\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u008f\n\r\f\r\16")
        buf.write("\r\u0092\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u009a")
        buf.write("\n\16\f\16\16\16\u009d\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00a4\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00ab\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00b3\n\21\f\21")
        buf.write("\16\21\u00b6\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00be\n\22\f\22\16\22\u00c1\13\22\3\23\3\23\3\23\5\23")
        buf.write("\u00c6\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00ce\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00da\n\25\3\26\3\26\3\26\5\26\u00df\n\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\7\27\u00e6\n\27\f\27\16\27\u00e9\13")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f3")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00fc\n")
        buf.write("\31\3\32\3\32\6\32\u0100\n\32\r\32\16\32\u0101\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u011a\n\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3")
        buf.write("!\7!\u0127\n!\f!\16!\u012a\13!\3!\2\6\30\32 \"\"\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@\2\b\5\2\6\7\f\f\16\16\4\2\27\27\37\37\4\2\30\31")
        buf.write(" !\4\2\23\23\33\33\4\2\24\24\34\35\4\2\25\25\33\33\2\u0132")
        buf.write("\2B\3\2\2\2\4G\3\2\2\2\6K\3\2\2\2\bV\3\2\2\2\n\\\3\2\2")
        buf.write("\2\fe\3\2\2\2\16m\3\2\2\2\20v\3\2\2\2\22x\3\2\2\2\24z")
        buf.write("\3\2\2\2\26\u0086\3\2\2\2\30\u0088\3\2\2\2\32\u0093\3")
        buf.write("\2\2\2\34\u00a3\3\2\2\2\36\u00aa\3\2\2\2 \u00ac\3\2\2")
        buf.write("\2\"\u00b7\3\2\2\2$\u00c5\3\2\2\2&\u00cd\3\2\2\2(\u00d9")
        buf.write("\3\2\2\2*\u00db\3\2\2\2,\u00e2\3\2\2\2.\u00f2\3\2\2\2")
        buf.write("\60\u00f4\3\2\2\2\62\u00fd\3\2\2\2\64\u0107\3\2\2\2\66")
        buf.write("\u0111\3\2\2\28\u0114\3\2\2\2:\u0117\3\2\2\2<\u011d\3")
        buf.write("\2\2\2>\u0120\3\2\2\2@\u0128\3\2\2\2BC\5\4\3\2CD\7\2\2")
        buf.write("\3D\3\3\2\2\2EH\5\6\4\2FH\5\n\6\2GE\3\2\2\2GF\3\2\2\2")
        buf.write("HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\5\3\2\2\2KL\5\22\n\2L")
        buf.write("Q\5\b\5\2MN\7)\2\2NP\5\b\5\2OM\3\2\2\2PS\3\2\2\2QO\3\2")
        buf.write("\2\2QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TU\7(\2\2U\7\3\2\2\2")
        buf.write("VZ\7-\2\2WX\7\"\2\2XY\7*\2\2Y[\7#\2\2ZW\3\2\2\2Z[\3\2")
        buf.write("\2\2[\t\3\2\2\2\\]\5\20\t\2]^\7-\2\2^`\7$\2\2_a\5\f\7")
        buf.write("\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7%\2\2cd\5> \2d\13")
        buf.write("\3\2\2\2ej\5\16\b\2fg\7)\2\2gi\5\16\b\2hf\3\2\2\2il\3")
        buf.write("\2\2\2jh\3\2\2\2jk\3\2\2\2k\r\3\2\2\2lj\3\2\2\2mn\5\22")
        buf.write("\n\2nq\7-\2\2op\7\"\2\2pr\7#\2\2qo\3\2\2\2qr\3\2\2\2r")
        buf.write("\17\3\2\2\2sw\5\22\n\2tw\5\24\13\2uw\7\20\2\2vs\3\2\2")
        buf.write("\2vt\3\2\2\2vu\3\2\2\2w\21\3\2\2\2xy\t\2\2\2y\23\3\2\2")
        buf.write("\2z|\5\22\n\2{}\7-\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~")
        buf.write("\177\7\"\2\2\177\u0080\7#\2\2\u0080\25\3\2\2\2\u0081\u0082")
        buf.write("\5\30\r\2\u0082\u0083\7\32\2\2\u0083\u0084\5\26\f\2\u0084")
        buf.write("\u0087\3\2\2\2\u0085\u0087\5\30\r\2\u0086\u0081\3\2\2")
        buf.write("\2\u0086\u0085\3\2\2\2\u0087\27\3\2\2\2\u0088\u0089\b")
        buf.write("\r\1\2\u0089\u008a\5\32\16\2\u008a\u0090\3\2\2\2\u008b")
        buf.write("\u008c\f\4\2\2\u008c\u008d\7\26\2\2\u008d\u008f\5\32\16")
        buf.write("\2\u008e\u008b\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\31\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0093\u0094\b\16\1\2\u0094\u0095\5\34\17\2\u0095")
        buf.write("\u009b\3\2\2\2\u0096\u0097\f\4\2\2\u0097\u0098\7\36\2")
        buf.write("\2\u0098\u009a\5\34\17\2\u0099\u0096\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\33\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\5\36\20\2")
        buf.write("\u009f\u00a0\t\3\2\2\u00a0\u00a1\5\36\20\2\u00a1\u00a4")
        buf.write("\3\2\2\2\u00a2\u00a4\5\36\20\2\u00a3\u009e\3\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\35\3\2\2\2\u00a5\u00a6\5 \21\2\u00a6")
        buf.write("\u00a7\t\4\2\2\u00a7\u00a8\5 \21\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00ab\5 \21\2\u00aa\u00a5\3\2\2\2\u00aa\u00a9\3")
        buf.write("\2\2\2\u00ab\37\3\2\2\2\u00ac\u00ad\b\21\1\2\u00ad\u00ae")
        buf.write("\5\"\22\2\u00ae\u00b4\3\2\2\2\u00af\u00b0\f\4\2\2\u00b0")
        buf.write("\u00b1\t\5\2\2\u00b1\u00b3\5\"\22\2\u00b2\u00af\3\2\2")
        buf.write("\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5!\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8")
        buf.write("\b\22\1\2\u00b8\u00b9\5$\23\2\u00b9\u00bf\3\2\2\2\u00ba")
        buf.write("\u00bb\f\4\2\2\u00bb\u00bc\t\6\2\2\u00bc\u00be\5$\23\2")
        buf.write("\u00bd\u00ba\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3")
        buf.write("\2\2\2\u00bf\u00c0\3\2\2\2\u00c0#\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\t\7\2\2\u00c3\u00c6\5$\23\2\u00c4")
        buf.write("\u00c6\5&\24\2\u00c5\u00c2\3\2\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6%\3\2\2\2\u00c7\u00c8\5(\25\2\u00c8\u00c9\7\"\2")
        buf.write("\2\u00c9\u00ca\5\26\f\2\u00ca\u00cb\7#\2\2\u00cb\u00ce")
        buf.write("\3\2\2\2\u00cc\u00ce\5(\25\2\u00cd\u00c7\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\'\3\2\2\2\u00cf\u00da\7*\2\2\u00d0")
        buf.write("\u00da\7+\2\2\u00d1\u00da\7,\2\2\u00d2\u00da\7\60\2\2")
        buf.write("\u00d3\u00d4\7$\2\2\u00d4\u00d5\5\26\f\2\u00d5\u00d6\7")
        buf.write("%\2\2\u00d6\u00da\3\2\2\2\u00d7\u00da\5*\26\2\u00d8\u00da")
        buf.write("\7-\2\2\u00d9\u00cf\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9")
        buf.write("\u00d1\3\2\2\2\u00d9\u00d2\3\2\2\2\u00d9\u00d3\3\2\2\2")
        buf.write("\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da)\3\2\2")
        buf.write("\2\u00db\u00dc\7-\2\2\u00dc\u00de\7$\2\2\u00dd\u00df\5")
        buf.write(",\27\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e1\7%\2\2\u00e1+\3\2\2\2\u00e2\u00e7")
        buf.write("\5\26\f\2\u00e3\u00e4\7)\2\2\u00e4\u00e6\5\26\f\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8-\3\2\2\2\u00e9\u00e7\3\2\2")
        buf.write("\2\u00ea\u00f3\5\60\31\2\u00eb\u00f3\5\64\33\2\u00ec\u00f3")
        buf.write("\5\62\32\2\u00ed\u00f3\5\66\34\2\u00ee\u00f3\58\35\2\u00ef")
        buf.write("\u00f3\5:\36\2\u00f0\u00f3\5<\37\2\u00f1\u00f3\5> \2\u00f2")
        buf.write("\u00ea\3\2\2\2\u00f2\u00eb\3\2\2\2\u00f2\u00ec\3\2\2\2")
        buf.write("\u00f2\u00ed\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f2\u00ef\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3/")
        buf.write("\3\2\2\2\u00f4\u00f5\7\r\2\2\u00f5\u00f6\7$\2\2\u00f6")
        buf.write("\u00f7\5\26\f\2\u00f7\u00f8\7%\2\2\u00f8\u00fb\5.\30\2")
        buf.write("\u00f9\u00fa\7\n\2\2\u00fa\u00fc\5.\30\2\u00fb\u00f9\3")
        buf.write("\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\61\3\2\2\2\u00fd\u00ff")
        buf.write("\7\21\2\2\u00fe\u0100\5.\30\2\u00ff\u00fe\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0104\7\22\2\2\u0104\u0105")
        buf.write("\5\26\f\2\u0105\u0106\7(\2\2\u0106\63\3\2\2\2\u0107\u0108")
        buf.write("\7\13\2\2\u0108\u0109\7$\2\2\u0109\u010a\5\26\f\2\u010a")
        buf.write("\u010b\7(\2\2\u010b\u010c\5\26\f\2\u010c\u010d\7(\2\2")
        buf.write("\u010d\u010e\5\26\f\2\u010e\u010f\7%\2\2\u010f\u0110\5")
        buf.write(".\30\2\u0110\65\3\2\2\2\u0111\u0112\7\b\2\2\u0112\u0113")
        buf.write("\7(\2\2\u0113\67\3\2\2\2\u0114\u0115\7\t\2\2\u0115\u0116")
        buf.write("\7(\2\2\u01169\3\2\2\2\u0117\u0119\7\17\2\2\u0118\u011a")
        buf.write("\5\26\f\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011c\7(\2\2\u011c;\3\2\2\2\u011d")
        buf.write("\u011e\5\26\f\2\u011e\u011f\7(\2\2\u011f=\3\2\2\2\u0120")
        buf.write("\u0121\7&\2\2\u0121\u0122\5@!\2\u0122\u0123\7\'\2\2\u0123")
        buf.write("?\3\2\2\2\u0124\u0127\5\6\4\2\u0125\u0127\5.\30\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129A\3\2\2")
        buf.write("\2\u012a\u0128\3\2\2\2\35GIQZ`jqv|\u0086\u0090\u009b\u00a3")
        buf.write("\u00aa\u00b4\u00bf\u00c5\u00cd\u00d9\u00de\u00e7\u00f2")
        buf.write("\u00fb\u0101\u0119\u0126\u0128")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'string'", "'boolean'", "'break'", "'continue'", "'else'", 
                     "'for'", "'float'", "'if'", "'int'", "'return'", "'void'", 
                     "'do'", "'while'", "'+'", "'*'", "'!'", "'||'", "'!='", 
                     "'<'", "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", 
                     "'=='", "'>'", "'>='", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
                      "STRING", "BOOL", "BREAK", "CONTINUE", "ELSE", "FOR", 
                      "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", "WHILE", 
                      "ADD", "MUL", "NOT", "OR", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQUAL", "GREATER", 
                      "GREATER_EQUAL", "LSB", "RSB", "LB", "RB", "LP", "RP", 
                      "SEMI", "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRINGLIT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decl = 2
    RULE_var = 3
    RULE_func_decl = 4
    RULE_para_list = 5
    RULE_para_decl = 6
    RULE_types = 7
    RULE_primitive_type = 8
    RULE_array_pointer_type = 9
    RULE_exp = 10
    RULE_exp1 = 11
    RULE_exp2 = 12
    RULE_exp3 = 13
    RULE_exp4 = 14
    RULE_exp5 = 15
    RULE_exp6 = 16
    RULE_exp7 = 17
    RULE_exp8 = 18
    RULE_operand = 19
    RULE_func_call = 20
    RULE_list_exp = 21
    RULE_stmt = 22
    RULE_if_stmt = 23
    RULE_while_stmt = 24
    RULE_for_stmt = 25
    RULE_break_stmt = 26
    RULE_continue_stmt = 27
    RULE_return_stmt = 28
    RULE_exp_stmt = 29
    RULE_block_stmt = 30
    RULE_body_block = 31

    ruleNames =  [ "program", "decls", "var_decl", "var", "func_decl", "para_list", 
                   "para_decl", "types", "primitive_type", "array_pointer_type", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "operand", "func_call", "list_exp", "stmt", 
                   "if_stmt", "while_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "exp_stmt", "block_stmt", "body_block" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    WS=3
    STRING=4
    BOOL=5
    BREAK=6
    CONTINUE=7
    ELSE=8
    FOR=9
    FLOAT=10
    IF=11
    INT=12
    RETURN=13
    VOID=14
    DO=15
    WHILE=16
    ADD=17
    MUL=18
    NOT=19
    OR=20
    NOT_EQUAL=21
    LESS=22
    LESS_EQUAL=23
    ASSIGN=24
    SUB=25
    DIV=26
    MOD=27
    AND=28
    EQUAL=29
    GREATER=30
    GREATER_EQUAL=31
    LSB=32
    RSB=33
    LB=34
    RB=35
    LP=36
    RP=37
    SEMI=38
    COMMA=39
    INTLIT=40
    FLOATLIT=41
    BOOLLIT=42
    ID=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45
    STRINGLIT=46
    ERROR_CHAR=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MCParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.decls()
            self.state = 65
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Func_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Func_declContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.var_decl()
                    pass

                elif la_ == 2:
                    self.state = 68
                    self.func_decl()
                    pass


                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT) | (1 << MCParser.VOID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.primitive_type()
            self.state = 74
            self.var()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 75
                self.match(MCParser.COMMA)
                self.state = 76
                self.var()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MCParser.ID)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 85
                self.match(MCParser.LSB)
                self.state = 86
                self.match(MCParser.INTLIT)
                self.state = 87
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(MCParser.TypesContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def para_list(self):
            return self.getTypedRuleContext(MCParser.Para_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.types()
            self.state = 91
            self.match(MCParser.ID)
            self.state = 92
            self.match(MCParser.LB)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0):
                self.state = 93
                self.para_list()


            self.state = 96
            self.match(MCParser.RB)
            self.state = 97
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Para_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Para_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = MCParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.para_decl()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 100
                self.match(MCParser.COMMA)
                self.state = 101
                self.para_decl()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = MCParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.primitive_type()
            self.state = 108
            self.match(MCParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 109
                self.match(MCParser.LSB)
                self.state = 110
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def array_pointer_type(self):
            return self.getTypedRuleContext(MCParser.Array_pointer_typeContext,0)


        def VOID(self):
            return self.getToken(MCParser.VOID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MCParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_types)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.array_pointer_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(MCParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(MCParser.BOOL, 0)

        def INT(self):
            return self.getToken(MCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MCParser.STRING, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_array_pointer_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pointer_type" ):
                return visitor.visitArray_pointer_type(self)
            else:
                return visitor.visitChildren(self)




    def array_pointer_type(self):

        localctx = MCParser.Array_pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_pointer_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.primitive_type()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 121
                self.match(MCParser.ID)


            self.state = 124
            self.match(MCParser.LSB)
            self.state = 125
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.exp1(0)
                self.state = 128
                self.match(MCParser.ASSIGN)
                self.state = 129
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 137
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 138
                    self.match(MCParser.OR)
                    self.state = 139
                    self.exp2(0) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 148
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 149
                    self.match(MCParser.AND)
                    self.state = 150
                    self.exp3() 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp4Context,i)


        def EQUAL(self):
            return self.getToken(MCParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MCParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.exp4()
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT_EQUAL or _la==MCParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp5Context,i)


        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(MCParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MCParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MCParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.exp5(0)
                self.state = 164
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.LESS_EQUAL) | (1 << MCParser.GREATER) | (1 << MCParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.exp5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(MCParser.Exp5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 175
                    self.exp6(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.exp7() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def exp8(self):
            return self.getTypedRuleContext(MCParser.Exp8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MCParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.NOT, MCParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT or _la==MCParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self.exp7()
                pass
            elif token in [MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.exp8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = MCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp8)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.operand()
                self.state = 198
                self.match(MCParser.LSB)
                self.state = 199
                self.exp()
                self.state = 200
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def func_call(self):
            return self.getTypedRuleContext(MCParser.Func_callContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operand)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(MCParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.match(MCParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(MCParser.LB)
                self.state = 210
                self.exp()
                self.state = 211
                self.match(MCParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def list_exp(self):
            return self.getTypedRuleContext(MCParser.List_expContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MCParser.ID)
            self.state = 218
            self.match(MCParser.LB)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 219
                self.list_exp()


            self.state = 222
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = MCParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.exp()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 225
                self.match(MCParser.COMMA)
                self.state = 226
                self.exp()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MCParser.While_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def exp_stmt(self):
            return self.getTypedRuleContext(MCParser.Exp_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.if_stmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.for_stmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.while_stmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.break_stmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.continue_stmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.return_stmt()
                pass
            elif token in [MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 238
                self.exp_stmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 239
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MCParser.IF)
            self.state = 243
            self.match(MCParser.LB)
            self.state = 244
            self.exp()
            self.state = 245
            self.match(MCParser.RB)
            self.state = 246
            self.stmt()
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(MCParser.ELSE)
                self.state = 248
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MCParser.DO)
            self.state = 253 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 252
                self.stmt()
                self.state = 255 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 257
            self.match(MCParser.WHILE)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MCParser.FOR)
            self.state = 262
            self.match(MCParser.LB)
            self.state = 263
            self.exp()
            self.state = 264
            self.match(MCParser.SEMI)
            self.state = 265
            self.exp()
            self.state = 266
            self.match(MCParser.SEMI)
            self.state = 267
            self.exp()
            self.state = 268
            self.match(MCParser.RB)
            self.state = 269
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MCParser.BREAK)
            self.state = 272
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MCParser.CONTINUE)
            self.state = 275
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MCParser.RETURN)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 278
                self.exp()


            self.state = 281
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_stmt" ):
                return visitor.visitExp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def exp_stmt(self):

        localctx = MCParser.Exp_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.exp()
            self.state = 284
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def body_block(self):
            return self.getTypedRuleContext(MCParser.Body_blockContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MCParser.LP)
            self.state = 287
            self.body_block()
            self.state = 288
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_body_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_block" ):
                return visitor.visitBody_block(self)
            else:
                return visitor.visitChildren(self)




    def body_block(self):

        localctx = MCParser.Body_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_body_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.FLOAT) | (1 << MCParser.IF) | (1 << MCParser.INT) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 292
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.STRING, MCParser.BOOL, MCParser.FLOAT, MCParser.INT]:
                    self.state = 290
                    self.var_decl()
                    pass
                elif token in [MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.LP, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                    self.state = 291
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.exp1_sempred
        self._predicates[12] = self.exp2_sempred
        self._predicates[15] = self.exp5_sempred
        self._predicates[16] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




