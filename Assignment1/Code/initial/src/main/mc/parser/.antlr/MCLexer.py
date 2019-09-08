# Generated from c:\Users\Truc Ly\Documents\GitHub\PPL\Assignment1\Code\initial\src\main\mc\parser\MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


    from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6@\n\6\r")
        buf.write("\6\16\6A\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\17\6\17U\n\17\r\17\16\17V\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\2\2\23\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2a")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3")
        buf.write("%\3\2\2\2\5)\3\2\2\2\7/\3\2\2\2\t\66\3\2\2\2\13?\3\2\2")
        buf.write("\2\rC\3\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23I\3\2\2\2\25K")
        buf.write("\3\2\2\2\27M\3\2\2\2\31O\3\2\2\2\33Q\3\2\2\2\35T\3\2\2")
        buf.write("\2\37Z\3\2\2\2!\\\3\2\2\2#^\3\2\2\2%&\7k\2\2&\'\7p\2\2")
        buf.write("\'(\7v\2\2(\4\3\2\2\2)*\7h\2\2*+\7n\2\2+,\7q\2\2,-\7c")
        buf.write("\2\2-.\7v\2\2.\6\3\2\2\2/\60\7u\2\2\60\61\7v\2\2\61\62")
        buf.write("\7t\2\2\62\63\7k\2\2\63\64\7p\2\2\64\65\7i\2\2\65\b\3")
        buf.write("\2\2\2\66\67\7d\2\2\678\7q\2\289\7q\2\29:\7n\2\2:;\7g")
        buf.write("\2\2;<\7c\2\2<=\7p\2\2=\n\3\2\2\2>@\t\2\2\2?>\3\2\2\2")
        buf.write("@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\f\3\2\2\2CD\7]\2\2D\16")
        buf.write("\3\2\2\2EF\7_\2\2F\20\3\2\2\2GH\7*\2\2H\22\3\2\2\2IJ\7")
        buf.write("+\2\2J\24\3\2\2\2KL\7}\2\2L\26\3\2\2\2MN\7\177\2\2N\30")
        buf.write("\3\2\2\2OP\7=\2\2P\32\3\2\2\2QR\7.\2\2R\34\3\2\2\2SU\t")
        buf.write("\3\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2")
        buf.write("\2XY\b\17\2\2Y\36\3\2\2\2Z[\13\2\2\2[ \3\2\2\2\\]\13\2")
        buf.write("\2\2]\"\3\2\2\2^_\13\2\2\2_$\3\2\2\2\5\2AV\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    STRING = 3
    BOOL = 4
    INTLIT = 5
    LSB = 6
    RSB = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    COMMA = 13
    WS = 14
    ERROR_CHAR = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'string'", "'boolean'", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "STRING", "BOOL", "INTLIT", "LSB", "RSB", "LB", 
            "RB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT", "FLOAT", "STRING", "BOOL", "INTLIT", "LSB", "RSB", 
                  "LB", "RB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


