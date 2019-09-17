# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u0260\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\7\34\u00fe\n\34\f\34\16\34\u0101\13\34")
        buf.write("\3\34\3\34\3\35\3\35\7\35\u0107\n\35\f\35\16\35\u010a")
        buf.write("\13\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\7\36\u0114")
        buf.write("\n\36\f\36\16\36\u0117\13\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\39\3:\3:\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\6O\u01e4\nO\rO\16O\u01e5\3P\3P\5P\u01ea")
        buf.write("\nP\3P\6P\u01ed\nP\rP\16P\u01ee\3Q\6Q\u01f2\nQ\rQ\16Q")
        buf.write("\u01f3\3Q\3Q\7Q\u01f8\nQ\fQ\16Q\u01fb\13Q\5Q\u01fd\nQ")
        buf.write("\3Q\5Q\u0200\nQ\3Q\3Q\6Q\u0204\nQ\rQ\16Q\u0205\3Q\5Q\u0209")
        buf.write("\nQ\5Q\u020b\nQ\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3T\3")
        buf.write("T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3")
        buf.write("Z\3Z\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\5\\\u0238")
        buf.write("\n\\\3]\3]\3]\7]\u023d\n]\f]\16]\u0240\13]\3]\3]\3^\3")
        buf.write("^\3^\3^\5^\u0248\n^\3^\3^\3_\3_\3_\3_\3`\3`\7`\u0252\n")
        buf.write("`\f`\16`\u0255\13`\3a\6a\u0258\na\ra\16a\u0259\3a\3a\3")
        buf.write("b\3b\3b\4\u0108\u0115\2c\3\2\5\2\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2")
        buf.write(")\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\n")
        buf.write("G\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30")
        buf.write("c\31e\32g\33i\34k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081")
        buf.write("(\u0083)\u0085*\u0087+\u0089,\u008b-\u008d.\u008f/\u0091")
        buf.write("\60\u0093\61\u0095\62\u0097\63\u0099\64\u009b\2\u009d")
        buf.write("\65\u009f\2\u00a1\66\u00a3\67\u00a58\u00a7\2\u00a9\2\u00ab")
        buf.write("\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9")
        buf.write("9\u00bb:\u00bd;\u00bf<\u00c1=\u00c3>\3\2#\4\2CCcc\4\2")
        buf.write("DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4")
        buf.write("\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQq")
        buf.write("q\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2")
        buf.write("XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\f\f\3\2\62")
        buf.write(";\7\2\f\f\17\17$$))^^\t\2$$))ddhhppttvv\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0253\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009d\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3")
        buf.write("\3\2\2\2\3\u00c5\3\2\2\2\5\u00c7\3\2\2\2\7\u00c9\3\2\2")
        buf.write("\2\t\u00cb\3\2\2\2\13\u00cd\3\2\2\2\r\u00cf\3\2\2\2\17")
        buf.write("\u00d1\3\2\2\2\21\u00d3\3\2\2\2\23\u00d5\3\2\2\2\25\u00d7")
        buf.write("\3\2\2\2\27\u00d9\3\2\2\2\31\u00db\3\2\2\2\33\u00dd\3")
        buf.write("\2\2\2\35\u00df\3\2\2\2\37\u00e1\3\2\2\2!\u00e3\3\2\2")
        buf.write("\2#\u00e5\3\2\2\2%\u00e7\3\2\2\2\'\u00e9\3\2\2\2)\u00eb")
        buf.write("\3\2\2\2+\u00ed\3\2\2\2-\u00ef\3\2\2\2/\u00f1\3\2\2\2")
        buf.write("\61\u00f3\3\2\2\2\63\u00f5\3\2\2\2\65\u00f7\3\2\2\2\67")
        buf.write("\u00f9\3\2\2\29\u0104\3\2\2\2;\u010f\3\2\2\2=\u011d\3")
        buf.write("\2\2\2?\u0123\3\2\2\2A\u012c\3\2\2\2C\u0130\3\2\2\2E\u0136")
        buf.write("\3\2\2\2G\u0139\3\2\2\2I\u0140\3\2\2\2K\u0145\3\2\2\2")
        buf.write("M\u0148\3\2\2\2O\u014b\3\2\2\2Q\u0150\3\2\2\2S\u0155\3")
        buf.write("\2\2\2U\u0159\3\2\2\2W\u015c\3\2\2\2Y\u0162\3\2\2\2[\u0166")
        buf.write("\3\2\2\2]\u016d\3\2\2\2_\u0176\3\2\2\2a\u0180\3\2\2\2")
        buf.write("c\u0186\3\2\2\2e\u018b\3\2\2\2g\u0193\3\2\2\2i\u019b\3")
        buf.write("\2\2\2k\u01a2\3\2\2\2m\u01a6\3\2\2\2o\u01aa\3\2\2\2q\u01ad")
        buf.write("\3\2\2\2s\u01b1\3\2\2\2u\u01b5\3\2\2\2w\u01b7\3\2\2\2")
        buf.write("y\u01b9\3\2\2\2{\u01bb\3\2\2\2}\u01bd\3\2\2\2\177\u01bf")
        buf.write("\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c4\3\2\2\2\u0085")
        buf.write("\u01c6\3\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01cc\3\2\2\2")
        buf.write("\u008b\u01cf\3\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01d3\3")
        buf.write("\2\2\2\u0091\u01d5\3\2\2\2\u0093\u01d7\3\2\2\2\u0095\u01d9")
        buf.write("\3\2\2\2\u0097\u01db\3\2\2\2\u0099\u01de\3\2\2\2\u009b")
        buf.write("\u01e0\3\2\2\2\u009d\u01e3\3\2\2\2\u009f\u01e7\3\2\2\2")
        buf.write("\u00a1\u020a\3\2\2\2\u00a3\u020c\3\2\2\2\u00a5\u0211\3")
        buf.write("\2\2\2\u00a7\u0217\3\2\2\2\u00a9\u021a\3\2\2\2\u00ab\u021d")
        buf.write("\3\2\2\2\u00ad\u0220\3\2\2\2\u00af\u0223\3\2\2\2\u00b1")
        buf.write("\u0226\3\2\2\2\u00b3\u0229\3\2\2\2\u00b5\u022c\3\2\2\2")
        buf.write("\u00b7\u0237\3\2\2\2\u00b9\u0239\3\2\2\2\u00bb\u0243\3")
        buf.write("\2\2\2\u00bd\u024b\3\2\2\2\u00bf\u024f\3\2\2\2\u00c1\u0257")
        buf.write("\3\2\2\2\u00c3\u025d\3\2\2\2\u00c5\u00c6\t\2\2\2\u00c6")
        buf.write("\4\3\2\2\2\u00c7\u00c8\t\3\2\2\u00c8\6\3\2\2\2\u00c9\u00ca")
        buf.write("\t\4\2\2\u00ca\b\3\2\2\2\u00cb\u00cc\t\5\2\2\u00cc\n\3")
        buf.write("\2\2\2\u00cd\u00ce\t\6\2\2\u00ce\f\3\2\2\2\u00cf\u00d0")
        buf.write("\t\7\2\2\u00d0\16\3\2\2\2\u00d1\u00d2\t\b\2\2\u00d2\20")
        buf.write("\3\2\2\2\u00d3\u00d4\t\t\2\2\u00d4\22\3\2\2\2\u00d5\u00d6")
        buf.write("\t\n\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\t\13\2\2\u00d8\26")
        buf.write("\3\2\2\2\u00d9\u00da\t\f\2\2\u00da\30\3\2\2\2\u00db\u00dc")
        buf.write("\t\r\2\2\u00dc\32\3\2\2\2\u00dd\u00de\t\16\2\2\u00de\34")
        buf.write("\3\2\2\2\u00df\u00e0\t\17\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\t\20\2\2\u00e2 \3\2\2\2\u00e3\u00e4\t\21\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\t\22\2\2\u00e6$\3\2\2\2\u00e7\u00e8")
        buf.write("\t\23\2\2\u00e8&\3\2\2\2\u00e9\u00ea\t\24\2\2\u00ea(\3")
        buf.write("\2\2\2\u00eb\u00ec\t\25\2\2\u00ec*\3\2\2\2\u00ed\u00ee")
        buf.write("\t\26\2\2\u00ee,\3\2\2\2\u00ef\u00f0\t\27\2\2\u00f0.\3")
        buf.write("\2\2\2\u00f1\u00f2\t\30\2\2\u00f2\60\3\2\2\2\u00f3\u00f4")
        buf.write("\t\31\2\2\u00f4\62\3\2\2\2\u00f5\u00f6\t\32\2\2\u00f6")
        buf.write("\64\3\2\2\2\u00f7\u00f8\t\33\2\2\u00f8\66\3\2\2\2\u00f9")
        buf.write("\u00fa\7\61\2\2\u00fa\u00fb\7\61\2\2\u00fb\u00ff\3\2\2")
        buf.write("\2\u00fc\u00fe\n\34\2\2\u00fd\u00fc\3\2\2\2\u00fe\u0101")
        buf.write("\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\b\34\2")
        buf.write("\2\u01038\3\2\2\2\u0104\u0108\7}\2\2\u0105\u0107\13\2")
        buf.write("\2\2\u0106\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b\u010c\7\177\2\2\u010c\u010d\3\2\2")
        buf.write("\2\u010d\u010e\b\35\2\2\u010e:\3\2\2\2\u010f\u0110\7*")
        buf.write("\2\2\u0110\u0111\7,\2\2\u0111\u0115\3\2\2\2\u0112\u0114")
        buf.write("\13\2\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0118\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u0119\7,\2\2\u0119\u011a\7")
        buf.write("+\2\2\u011a\u011b\3\2\2\2\u011b\u011c\b\36\2\2\u011c<")
        buf.write("\3\2\2\2\u011d\u011e\5\5\3\2\u011e\u011f\5%\23\2\u011f")
        buf.write("\u0120\5\13\6\2\u0120\u0121\5\3\2\2\u0121\u0122\5\27\f")
        buf.write("\2\u0122>\3\2\2\2\u0123\u0124\5\7\4\2\u0124\u0125\5\37")
        buf.write("\20\2\u0125\u0126\5\35\17\2\u0126\u0127\5)\25\2\u0127")
        buf.write("\u0128\5\23\n\2\u0128\u0129\5\35\17\2\u0129\u012a\5+\26")
        buf.write("\2\u012a\u012b\5\13\6\2\u012b@\3\2\2\2\u012c\u012d\5\r")
        buf.write("\7\2\u012d\u012e\5\37\20\2\u012e\u012f\5%\23\2\u012fB")
        buf.write("\3\2\2\2\u0130\u0131\5/\30\2\u0131\u0132\5\21\t\2\u0132")
        buf.write("\u0133\5\23\n\2\u0133\u0134\5\31\r\2\u0134\u0135\5\13")
        buf.write("\6\2\u0135D\3\2\2\2\u0136\u0137\5)\25\2\u0137\u0138\5")
        buf.write("\37\20\2\u0138F\3\2\2\2\u0139\u013a\5\t\5\2\u013a\u013b")
        buf.write("\5\37\20\2\u013b\u013c\5/\30\2\u013c\u013d\5\35\17\2\u013d")
        buf.write("\u013e\5)\25\2\u013e\u013f\5\37\20\2\u013fH\3\2\2\2\u0140")
        buf.write("\u0141\5/\30\2\u0141\u0142\5\23\n\2\u0142\u0143\5)\25")
        buf.write("\2\u0143\u0144\5\21\t\2\u0144J\3\2\2\2\u0145\u0146\5\t")
        buf.write("\5\2\u0146\u0147\5\37\20\2\u0147L\3\2\2\2\u0148\u0149")
        buf.write("\5\23\n\2\u0149\u014a\5\r\7\2\u014aN\3\2\2\2\u014b\u014c")
        buf.write("\5)\25\2\u014c\u014d\5\21\t\2\u014d\u014e\5\13\6\2\u014e")
        buf.write("\u014f\5\35\17\2\u014fP\3\2\2\2\u0150\u0151\5\13\6\2\u0151")
        buf.write("\u0152\5\31\r\2\u0152\u0153\5\'\24\2\u0153\u0154\5\13")
        buf.write("\6\2\u0154R\3\2\2\2\u0155\u0156\5-\27\2\u0156\u0157\5")
        buf.write("\3\2\2\u0157\u0158\5%\23\2\u0158T\3\2\2\2\u0159\u015a")
        buf.write("\5\37\20\2\u015a\u015b\5\r\7\2\u015bV\3\2\2\2\u015c\u015d")
        buf.write("\5\5\3\2\u015d\u015e\5\13\6\2\u015e\u015f\5\17\b\2\u015f")
        buf.write("\u0160\5\23\n\2\u0160\u0161\5\35\17\2\u0161X\3\2\2\2\u0162")
        buf.write("\u0163\5\13\6\2\u0163\u0164\5\35\17\2\u0164\u0165\5\t")
        buf.write("\5\2\u0165Z\3\2\2\2\u0166\u0167\5%\23\2\u0167\u0168\5")
        buf.write("\13\6\2\u0168\u0169\5)\25\2\u0169\u016a\5+\26\2\u016a")
        buf.write("\u016b\5%\23\2\u016b\u016c\5\35\17\2\u016c\\\3\2\2\2\u016d")
        buf.write("\u016e\5\r\7\2\u016e\u016f\5+\26\2\u016f\u0170\5\35\17")
        buf.write("\2\u0170\u0171\5\7\4\2\u0171\u0172\5)\25\2\u0172\u0173")
        buf.write("\5\23\n\2\u0173\u0174\5\37\20\2\u0174\u0175\5\35\17\2")
        buf.write("\u0175^\3\2\2\2\u0176\u0177\5!\21\2\u0177\u0178\5%\23")
        buf.write("\2\u0178\u0179\5\37\20\2\u0179\u017a\5\7\4\2\u017a\u017b")
        buf.write("\5\13\6\2\u017b\u017c\5\t\5\2\u017c\u017d\5+\26\2\u017d")
        buf.write("\u017e\5%\23\2\u017e\u017f\5\13\6\2\u017f`\3\2\2\2\u0180")
        buf.write("\u0181\5\3\2\2\u0181\u0182\5%\23\2\u0182\u0183\5%\23\2")
        buf.write("\u0183\u0184\5\3\2\2\u0184\u0185\5\63\32\2\u0185b\3\2")
        buf.write("\2\2\u0186\u0187\5%\23\2\u0187\u0188\5\13\6\2\u0188\u0189")
        buf.write("\5\3\2\2\u0189\u018a\5\31\r\2\u018ad\3\2\2\2\u018b\u018c")
        buf.write("\5\5\3\2\u018c\u018d\5\37\20\2\u018d\u018e\5\37\20\2\u018e")
        buf.write("\u018f\5\31\r\2\u018f\u0190\5\13\6\2\u0190\u0191\5\3\2")
        buf.write("\2\u0191\u0192\5\35\17\2\u0192f\3\2\2\2\u0193\u0194\5")
        buf.write("\23\n\2\u0194\u0195\5\35\17\2\u0195\u0196\5)\25\2\u0196")
        buf.write("\u0197\5\13\6\2\u0197\u0198\5\17\b\2\u0198\u0199\5\13")
        buf.write("\6\2\u0199\u019a\5%\23\2\u019ah\3\2\2\2\u019b\u019c\5")
        buf.write("\'\24\2\u019c\u019d\5)\25\2\u019d\u019e\5%\23\2\u019e")
        buf.write("\u019f\5\23\n\2\u019f\u01a0\5\35\17\2\u01a0\u01a1\5\17")
        buf.write("\b\2\u01a1j\3\2\2\2\u01a2\u01a3\5\35\17\2\u01a3\u01a4")
        buf.write("\5\37\20\2\u01a4\u01a5\5)\25\2\u01a5l\3\2\2\2\u01a6\u01a7")
        buf.write("\5\3\2\2\u01a7\u01a8\5\35\17\2\u01a8\u01a9\5\t\5\2\u01a9")
        buf.write("n\3\2\2\2\u01aa\u01ab\5\37\20\2\u01ab\u01ac\5%\23\2\u01ac")
        buf.write("p\3\2\2\2\u01ad\u01ae\5\t\5\2\u01ae\u01af\5\23\n\2\u01af")
        buf.write("\u01b0\5-\27\2\u01b0r\3\2\2\2\u01b1\u01b2\5\33\16\2\u01b2")
        buf.write("\u01b3\5\37\20\2\u01b3\u01b4\5\t\5\2\u01b4t\3\2\2\2\u01b5")
        buf.write("\u01b6\7-\2\2\u01b6v\3\2\2\2\u01b7\u01b8\7/\2\2\u01b8")
        buf.write("x\3\2\2\2\u01b9\u01ba\7,\2\2\u01baz\3\2\2\2\u01bb\u01bc")
        buf.write("\7\61\2\2\u01bc|\3\2\2\2\u01bd\u01be\7?\2\2\u01be~\3\2")
        buf.write("\2\2\u01bf\u01c0\7>\2\2\u01c0\u01c1\7@\2\2\u01c1\u0080")
        buf.write("\3\2\2\2\u01c2\u01c3\7>\2\2\u01c3\u0082\3\2\2\2\u01c4")
        buf.write("\u01c5\7@\2\2\u01c5\u0084\3\2\2\2\u01c6\u01c7\7>\2\2\u01c7")
        buf.write("\u01c8\7?\2\2\u01c8\u0086\3\2\2\2\u01c9\u01ca\7@\2\2\u01ca")
        buf.write("\u01cb\7?\2\2\u01cb\u0088\3\2\2\2\u01cc\u01cd\7<\2\2\u01cd")
        buf.write("\u01ce\7?\2\2\u01ce\u008a\3\2\2\2\u01cf\u01d0\7]\2\2\u01d0")
        buf.write("\u008c\3\2\2\2\u01d1\u01d2\7_\2\2\u01d2\u008e\3\2\2\2")
        buf.write("\u01d3\u01d4\7<\2\2\u01d4\u0090\3\2\2\2\u01d5\u01d6\7")
        buf.write("*\2\2\u01d6\u0092\3\2\2\2\u01d7\u01d8\7+\2\2\u01d8\u0094")
        buf.write("\3\2\2\2\u01d9\u01da\7=\2\2\u01da\u0096\3\2\2\2\u01db")
        buf.write("\u01dc\7\60\2\2\u01dc\u01dd\7\60\2\2\u01dd\u0098\3\2\2")
        buf.write("\2\u01de\u01df\7.\2\2\u01df\u009a\3\2\2\2\u01e0\u01e1")
        buf.write("\t\35\2\2\u01e1\u009c\3\2\2\2\u01e2\u01e4\5\u009bN\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u009e\3\2\2\2\u01e7\u01e9\t")
        buf.write("\6\2\2\u01e8\u01ea\7/\2\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01ed\5\u009bN\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u00a0\3\2\2\2\u01f0\u01f2\5")
        buf.write("\u009bN\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01fc\3\2\2\2")
        buf.write("\u01f5\u01f9\7\60\2\2\u01f6\u01f8\5\u009bN\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01f5\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3")
        buf.write("\2\2\2\u01fe\u0200\5\u009fP\2\u01ff\u01fe\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u020b\3\2\2\2\u0201\u0203\7\60\2")
        buf.write("\2\u0202\u0204\5\u009bN\2\u0203\u0202\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0208\3\2\2\2\u0207\u0209\5\u009fP\2\u0208\u0207\3\2")
        buf.write("\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2\u020a\u01f1")
        buf.write("\3\2\2\2\u020a\u0201\3\2\2\2\u020b\u00a2\3\2\2\2\u020c")
        buf.write("\u020d\5)\25\2\u020d\u020e\5%\23\2\u020e\u020f\5+\26\2")
        buf.write("\u020f\u0210\5\13\6\2\u0210\u00a4\3\2\2\2\u0211\u0212")
        buf.write("\5\r\7\2\u0212\u0213\5\3\2\2\u0213\u0214\5\31\r\2\u0214")
        buf.write("\u0215\5\'\24\2\u0215\u0216\5\13\6\2\u0216\u00a6\3\2\2")
        buf.write("\2\u0217\u0218\7^\2\2\u0218\u0219\7d\2\2\u0219\u00a8\3")
        buf.write("\2\2\2\u021a\u021b\7^\2\2\u021b\u021c\7h\2\2\u021c\u00aa")
        buf.write("\3\2\2\2\u021d\u021e\7^\2\2\u021e\u021f\7t\2\2\u021f\u00ac")
        buf.write("\3\2\2\2\u0220\u0221\7^\2\2\u0221\u0222\7p\2\2\u0222\u00ae")
        buf.write("\3\2\2\2\u0223\u0224\7^\2\2\u0224\u0225\7v\2\2\u0225\u00b0")
        buf.write("\3\2\2\2\u0226\u0227\7^\2\2\u0227\u0228\7)\2\2\u0228\u00b2")
        buf.write("\3\2\2\2\u0229\u022a\7^\2\2\u022a\u022b\7$\2\2\u022b\u00b4")
        buf.write("\3\2\2\2\u022c\u022d\7^\2\2\u022d\u022e\7^\2\2\u022e\u00b6")
        buf.write("\3\2\2\2\u022f\u0238\5\u00a7T\2\u0230\u0238\5\u00a9U\2")
        buf.write("\u0231\u0238\5\u00abV\2\u0232\u0238\5\u00adW\2\u0233\u0238")
        buf.write("\5\u00afX\2\u0234\u0238\5\u00b1Y\2\u0235\u0238\5\u00b3")
        buf.write("Z\2\u0236\u0238\5\u00b5[\2\u0237\u022f\3\2\2\2\u0237\u0230")
        buf.write("\3\2\2\2\u0237\u0231\3\2\2\2\u0237\u0232\3\2\2\2\u0237")
        buf.write("\u0233\3\2\2\2\u0237\u0234\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0237\u0236\3\2\2\2\u0238\u00b8\3\2\2\2\u0239\u023e\7")
        buf.write("$\2\2\u023a\u023d\n\36\2\2\u023b\u023d\5\u00b7\\\2\u023c")
        buf.write("\u023a\3\2\2\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2\2\2")
        buf.write("\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0241\3")
        buf.write("\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\b]\3\2\u0242\u00ba")
        buf.write("\3\2\2\2\u0243\u0247\5\u00b9]\2\u0244\u0245\7^\2\2\u0245")
        buf.write("\u0248\n\37\2\2\u0246\u0248\7)\2\2\u0247\u0244\3\2\2\2")
        buf.write("\u0247\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\b")
        buf.write("^\4\2\u024a\u00bc\3\2\2\2\u024b\u024c\5\u00b9]\2\u024c")
        buf.write("\u024d\7$\2\2\u024d\u024e\b_\5\2\u024e\u00be\3\2\2\2\u024f")
        buf.write("\u0253\t \2\2\u0250\u0252\t!\2\2\u0251\u0250\3\2\2\2\u0252")
        buf.write("\u0255\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2")
        buf.write("\u0254\u00c0\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0258\t")
        buf.write("\"\2\2\u0257\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0257")
        buf.write("\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("\u025c\ba\2\2\u025c\u00c2\3\2\2\2\u025d\u025e\13\2\2\2")
        buf.write("\u025e\u025f\bb\6\2\u025f\u00c4\3\2\2\2\26\2\u00ff\u0108")
        buf.write("\u0115\u01e5\u01e9\u01ee\u01f3\u01f9\u01fc\u01ff\u0205")
        buf.write("\u0208\u020a\u0237\u023c\u023e\u0247\u0253\u0259\7\b\2")
        buf.write("\2\3]\2\3^\3\3_\4\3b\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_CMT = 1
    BLOCK_CMT_1 = 2
    BLOCK_CMT_2 = 3
    BREAK = 4
    CONTINUE = 5
    FOR = 6
    WHILE = 7
    TO = 8
    DOWNTO = 9
    WITH = 10
    DO = 11
    IF = 12
    THEN = 13
    ELSE = 14
    VAR = 15
    OF = 16
    BEGIN = 17
    END = 18
    RETURN = 19
    FUNCTION = 20
    PROCEDURE = 21
    ARRAY = 22
    REAL = 23
    BOOLEAN = 24
    INTEGER = 25
    STRING = 26
    NOT = 27
    AND = 28
    OR = 29
    DIV = 30
    MOD = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV_F = 35
    EQUAL = 36
    NOTEQUAL = 37
    LESSTHAN = 38
    GREATERTHAN = 39
    LESSEQUAL = 40
    GREATEREQUAL = 41
    ASSIGN = 42
    LSB = 43
    RSB = 44
    COLON = 45
    LB = 46
    RB = 47
    SEMI = 48
    DDOT = 49
    COMMA = 50
    INTEGER_LITERAL = 51
    REAL_LITERAL = 52
    TRUE = 53
    FALSE = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    STRING_LITERAL = 57
    IDENTIFIER = 58
    WS = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'<>'", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "LINE_CMT", "BLOCK_CMT_1", "BLOCK_CMT_2", "BREAK", "CONTINUE", 
            "FOR", "WHILE", "TO", "DOWNTO", "WITH", "DO", "IF", "THEN", 
            "ELSE", "VAR", "OF", "BEGIN", "END", "RETURN", "FUNCTION", "PROCEDURE", 
            "ARRAY", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "ADD", "SUB", "MUL", "DIV_F", "EQUAL", "NOTEQUAL", 
            "LESSTHAN", "GREATERTHAN", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
            "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DDOT", "COMMA", 
            "INTEGER_LITERAL", "REAL_LITERAL", "TRUE", "FALSE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "STRING_LITERAL", "IDENTIFIER", "WS", "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "LINE_CMT", "BLOCK_CMT_1", "BLOCK_CMT_2", 
                  "BREAK", "CONTINUE", "FOR", "WHILE", "TO", "DOWNTO", "WITH", 
                  "DO", "IF", "THEN", "ELSE", "VAR", "OF", "BEGIN", "END", 
                  "RETURN", "FUNCTION", "PROCEDURE", "ARRAY", "REAL", "BOOLEAN", 
                  "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", "MOD", 
                  "ADD", "SUB", "MUL", "DIV_F", "EQUAL", "NOTEQUAL", "LESSTHAN", 
                  "GREATERTHAN", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
                  "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DDOT", "COMMA", 
                  "DIGIT", "INTEGER_LITERAL", "EXPONENT", "REAL_LITERAL", 
                  "TRUE", "FALSE", "BSP", "FF", "CR", "NEWLINE", "TAB", 
                  "SQUOTE", "DQUOTE", "BSL", "LEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_LITERAL", "IDENTIFIER", "WS", 
                  "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[91] = self.UNCLOSE_STRING_action 
            actions[92] = self.ILLEGAL_ESCAPE_action 
            actions[93] = self.STRING_LITERAL_action 
            actions[96] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[1:])

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


