# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\7\61\u0132\n\61\f\61")
        buf.write("\16\61\u0135\13\61\3\61\3\61\6\61\u0139\n\61\r\61\16\61")
        buf.write("\u013a\7\61\u013d\n\61\f\61\16\61\u0140\13\61\3\61\3\61")
        buf.write("\7\61\u0144\n\61\f\61\16\61\u0147\13\61\5\61\u0149\n\61")
        buf.write("\3\61\3\61\3\62\3\62\7\62\u014f\n\62\f\62\16\62\u0152")
        buf.write("\13\62\3\63\3\63\5\63\u0156\n\63\3\63\6\63\u0159\n\63")
        buf.write("\r\63\16\63\u015a\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u0167\n\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0174\n\65\3\66\3")
        buf.write("\66\3\66\3\67\3\67\5\67\u017b\n\67\38\38\78\u017f\n8\f")
        buf.write("8\168\u0182\138\38\38\38\39\39\79\u0189\n9\f9\169\u018c")
        buf.write("\139\3:\3:\3:\3:\7:\u0192\n:\f:\16:\u0195\13:\3:\3:\3")
        buf.write(":\3:\7:\u019b\n:\f:\16:\u019e\13:\3:\3:\5:\u01a2\n:\3")
        buf.write(":\3:\3;\6;\u01a7\n;\r;\16;\u01a8\3;\3;\3<\3<\3<\3=\3=")
        buf.write("\3=\3=\5=\u01b4\n=\3>\3>\7>\u01b8\n>\f>\16>\u01bb\13>")
        buf.write("\3>\3>\3>\3?\3?\7?\u01c2\n?\f?\16?\u01c5\13?\3?\5?\u01c8")
        buf.write("\n?\3?\3?\3\u019c\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\60c\2e\2g\61")
        buf.write("i\62k\2m\2o\63q\64s\65u\66w\67y\2{8}9\3\2\23\3\2--\3\2")
        buf.write("))\3\2$$\3\2\62\62\3\2\63;\3\2\62;\3\2\60\60\5\2GGgg~")
        buf.write("~\5\2--//~~\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13\f\17\17")
        buf.write("\"\"\3\2^^\4\3\f\f\17\17\2\u01d9\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2a\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0084\3")
        buf.write("\2\2\2\7\u008a\3\2\2\2\t\u0092\3\2\2\2\13\u0095\3\2\2")
        buf.write("\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21\u00a4\3\2\2\2\23")
        buf.write("\u00ad\3\2\2\2\25\u00b0\3\2\2\2\27\u00b8\3\2\2\2\31\u00bf")
        buf.write("\3\2\2\2\33\u00c6\3\2\2\2\35\u00cc\3\2\2\2\37\u00d1\3")
        buf.write("\2\2\2!\u00d5\3\2\2\2#\u00de\3\2\2\2%\u00e1\3\2\2\2\'")
        buf.write("\u00e9\3\2\2\2)\u00ef\3\2\2\2+\u00f1\3\2\2\2-\u00f3\3")
        buf.write("\2\2\2/\u00f5\3\2\2\2\61\u00f7\3\2\2\2\63\u00f9\3\2\2")
        buf.write("\2\65\u00fb\3\2\2\2\67\u00fe\3\2\2\29\u0101\3\2\2\2;\u0104")
        buf.write("\3\2\2\2=\u0107\3\2\2\2?\u0109\3\2\2\2A\u010c\3\2\2\2")
        buf.write("C\u010e\3\2\2\2E\u0111\3\2\2\2G\u0114\3\2\2\2I\u0116\3")
        buf.write("\2\2\2K\u0118\3\2\2\2M\u011a\3\2\2\2O\u011c\3\2\2\2Q\u011e")
        buf.write("\3\2\2\2S\u0120\3\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2")
        buf.write("Y\u0126\3\2\2\2[\u0128\3\2\2\2]\u012a\3\2\2\2_\u012c\3")
        buf.write("\2\2\2a\u0148\3\2\2\2c\u014c\3\2\2\2e\u0153\3\2\2\2g\u0166")
        buf.write("\3\2\2\2i\u0173\3\2\2\2k\u0175\3\2\2\2m\u017a\3\2\2\2")
        buf.write("o\u017c\3\2\2\2q\u0186\3\2\2\2s\u01a1\3\2\2\2u\u01a6\3")
        buf.write("\2\2\2w\u01ac\3\2\2\2y\u01b3\3\2\2\2{\u01b5\3\2\2\2}\u01bf")
        buf.write("\3\2\2\2\177\u0080\7c\2\2\u0080\u0081\7w\2\2\u0081\u0082")
        buf.write("\7v\2\2\u0082\u0083\7q\2\2\u0083\4\3\2\2\2\u0084\u0085")
        buf.write("\7d\2\2\u0085\u0086\7t\2\2\u0086\u0087\7g\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7m\2\2\u0089\6\3\2\2\2\u008a\u008b")
        buf.write("\7d\2\2\u008b\u008c\7q\2\2\u008c\u008d\7q\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\u008f\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\b\3\2\2\2\u0092\u0093\7f\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\n\3\2\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099\f")
        buf.write("\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c\7n\2\2\u009c\u009d")
        buf.write("\7q\2\2\u009d\u009e\7c\2\2\u009e\u009f\7v\2\2\u009f\16")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\20\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\24\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\26")
        buf.write("\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\30\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\32\3\2\2\2\u00c6\u00c7")
        buf.write("\7y\2\2\u00c7\u00c8\7j\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7g\2\2\u00cb\34\3\2\2\2\u00cc\u00cd")
        buf.write("\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7f\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7v\2\2\u00d4 \3\2\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7g\2\2\u00dd\"\3\2\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7h\2\2\u00e0$\3\2\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7j\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8&\3\2\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7{\2\2\u00ee(\3\2\2\2\u00ef\u00f0\t\2\2\2\u00f0*\3\2")
        buf.write("\2\2\u00f1\u00f2\7/\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7,")
        buf.write("\2\2\u00f4.\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6\60\3\2")
        buf.write("\2\2\u00f7\u00f8\7\'\2\2\u00f8\62\3\2\2\2\u00f9\u00fa")
        buf.write("\7#\2\2\u00fa\64\3\2\2\2\u00fb\u00fc\7(\2\2\u00fc\u00fd")
        buf.write("\7(\2\2\u00fd\66\3\2\2\2\u00fe\u00ff\7~\2\2\u00ff\u0100")
        buf.write("\7~\2\2\u01008\3\2\2\2\u0101\u0102\7?\2\2\u0102\u0103")
        buf.write("\7?\2\2\u0103:\3\2\2\2\u0104\u0105\7#\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106<\3\2\2\2\u0107\u0108\7>\2\2\u0108>\3\2\2")
        buf.write("\2\u0109\u010a\7>\2\2\u010a\u010b\7?\2\2\u010b@\3\2\2")
        buf.write("\2\u010c\u010d\7@\2\2\u010dB\3\2\2\2\u010e\u010f\7@\2")
        buf.write("\2\u010f\u0110\7?\2\2\u0110D\3\2\2\2\u0111\u0112\7<\2")
        buf.write("\2\u0112\u0113\7<\2\2\u0113F\3\2\2\2\u0114\u0115\7*\2")
        buf.write("\2\u0115H\3\2\2\2\u0116\u0117\7+\2\2\u0117J\3\2\2\2\u0118")
        buf.write("\u0119\7]\2\2\u0119L\3\2\2\2\u011a\u011b\7_\2\2\u011b")
        buf.write("N\3\2\2\2\u011c\u011d\7}\2\2\u011dP\3\2\2\2\u011e\u011f")
        buf.write("\7\177\2\2\u011fR\3\2\2\2\u0120\u0121\7\60\2\2\u0121T")
        buf.write("\3\2\2\2\u0122\u0123\7.\2\2\u0123V\3\2\2\2\u0124\u0125")
        buf.write("\7=\2\2\u0125X\3\2\2\2\u0126\u0127\7<\2\2\u0127Z\3\2\2")
        buf.write("\2\u0128\u0129\7?\2\2\u0129\\\3\2\2\2\u012a\u012b\t\3")
        buf.write("\2\2\u012b^\3\2\2\2\u012c\u012d\t\4\2\2\u012d`\3\2\2\2")
        buf.write("\u012e\u0149\t\5\2\2\u012f\u013e\t\6\2\2\u0130\u0132\t")
        buf.write("\7\2\2\u0131\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u0138\7a\2\2\u0137\u0139\t\7\2\2")
        buf.write("\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3")
        buf.write("\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u0133")
        buf.write("\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0149\3\2\2\2\u0140\u013e\3\2\2\2")
        buf.write("\u0141\u0145\t\6\2\2\u0142\u0144\t\7\2\2\u0143\u0142\3")
        buf.write("\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0148")
        buf.write("\u012e\3\2\2\2\u0148\u012f\3\2\2\2\u0148\u0141\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014b\b\61\2\2\u014bb\3\2\2")
        buf.write("\2\u014c\u0150\t\b\2\2\u014d\u014f\t\7\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151d\3\2\2\2\u0152\u0150\3\2\2\2\u0153")
        buf.write("\u0155\t\t\2\2\u0154\u0156\t\n\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0159\t")
        buf.write("\7\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015bf\3\2\2\2\u015c\u015d")
        buf.write("\5a\61\2\u015d\u015e\5c\62\2\u015e\u0167\3\2\2\2\u015f")
        buf.write("\u0160\5a\61\2\u0160\u0161\5e\63\2\u0161\u0167\3\2\2\2")
        buf.write("\u0162\u0163\5a\61\2\u0163\u0164\5c\62\2\u0164\u0165\5")
        buf.write("e\63\2\u0165\u0167\3\2\2\2\u0166\u015c\3\2\2\2\u0166\u015f")
        buf.write("\3\2\2\2\u0166\u0162\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0169\b\64\3\2\u0169h\3\2\2\2\u016a\u016b\7v\2\2\u016b")
        buf.write("\u016c\7t\2\2\u016c\u016d\7w\2\2\u016d\u0174\7g\2\2\u016e")
        buf.write("\u016f\7h\2\2\u016f\u0170\7c\2\2\u0170\u0171\7n\2\2\u0171")
        buf.write("\u0172\7u\2\2\u0172\u0174\7g\2\2\u0173\u016a\3\2\2\2\u0173")
        buf.write("\u016e\3\2\2\2\u0174j\3\2\2\2\u0175\u0176\7^\2\2\u0176")
        buf.write("\u0177\t\13\2\2\u0177l\3\2\2\2\u0178\u017b\n\f\2\2\u0179")
        buf.write("\u017b\5k\66\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017bn\3\2\2\2\u017c\u0180\5_\60\2\u017d\u017f\5m\67")
        buf.write("\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0183\u0184\5_\60\2\u0184\u0185\b8\4\2")
        buf.write("\u0185p\3\2\2\2\u0186\u018a\t\r\2\2\u0187\u0189\t\16\2")
        buf.write("\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018br\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d\u018e\7\61\2\2\u018e\u018f\7\61\2\2\u018f")
        buf.write("\u0193\3\2\2\2\u0190\u0192\n\17\2\2\u0191\u0190\3\2\2")
        buf.write("\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194\u01a2\3\2\2\2\u0195\u0193\3\2\2\2\u0196")
        buf.write("\u0197\7\61\2\2\u0197\u0198\7,\2\2\u0198\u019c\3\2\2\2")
        buf.write("\u0199\u019b\13\2\2\2\u019a\u0199\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019c\u019a\3\2\2\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\7,\2\2")
        buf.write("\u01a0\u01a2\7\61\2\2\u01a1\u018d\3\2\2\2\u01a1\u0196")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\b:\5\2\u01a4")
        buf.write("t\3\2\2\2\u01a5\u01a7\t\20\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ab\b;\5\2\u01abv\3\2\2\2")
        buf.write("\u01ac\u01ad\13\2\2\2\u01ad\u01ae\b<\6\2\u01aex\3\2\2")
        buf.write("\2\u01af\u01b0\7^\2\2\u01b0\u01b4\n\13\2\2\u01b1\u01b2")
        buf.write("\n\21\2\2\u01b2\u01b4\t\3\2\2\u01b3\u01af\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4z\3\2\2\2\u01b5\u01b9\5_\60\2\u01b6")
        buf.write("\u01b8\5m\67\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\5y=\2\u01bd\u01be")
        buf.write("\b>\7\2\u01be|\3\2\2\2\u01bf\u01c3\5_\60\2\u01c0\u01c2")
        buf.write("\5m\67\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c8\t\22\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\b?\b\2\u01ca")
        buf.write("~\3\2\2\2\30\2\u0133\u013a\u013e\u0145\u0148\u0150\u0155")
        buf.write("\u015a\u0166\u0173\u017a\u0180\u018a\u0193\u019c\u01a1")
        buf.write("\u01a8\u01b3\u01b9\u01c3\u01c7\t\3\61\2\3\64\3\38\4\b")
        buf.write("\2\2\3<\5\3>\6\3?\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FLOAT = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    ADDOP = 20
    SUBOP = 21
    MULOP = 22
    DIVOP = 23
    REMOP = 24
    NOTOP = 25
    ANDOP = 26
    OROP = 27
    EQOP = 28
    NEQOP = 29
    LTOP = 30
    LEQOP = 31
    GTOP = 32
    GEQOP = 33
    SCCOP = 34
    LRB = 35
    RRB = 36
    LSB = 37
    RSB = 38
    LCB = 39
    RCB = 40
    DOT = 41
    COMMA = 42
    SM = 43
    CM = 44
    EQUAL = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLIT = 48
    STRLIT = 49
    ID = 50
    COMMENT = 51
    WS = 52
    ERROR_CHAR = 53
    ILLEGAL_ESCAPE = 54
    UNCLOSE_STRING = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "REMOP", "NOTOP", "ANDOP", "OROP", "EQOP", "NEQOP", 
            "LTOP", "LEQOP", "GTOP", "GEQOP", "SCCOP", "LRB", "RRB", "LSB", 
            "RSB", "LCB", "RCB", "DOT", "COMMA", "SM", "CM", "EQUAL", "INTLIT", 
            "FLOATLIT", "BOOLIT", "STRLIT", "ID", "COMMENT", "WS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "REMOP", "NOTOP", "ANDOP", 
                  "OROP", "EQOP", "NEQOP", "LTOP", "LEQOP", "GTOP", "GEQOP", 
                  "SCCOP", "LRB", "RRB", "LSB", "RSB", "LCB", "RCB", "DOT", 
                  "COMMA", "SM", "CM", "EQUAL", "QUOTE", "DQUOTE", "INTLIT", 
                  "DECPART", "EXPPART", "FLOATLIT", "BOOLIT", "ESCAPE", 
                  "CHAR", "STRLIT", "ID", "COMMENT", "WS", "ERROR_CHAR", 
                  "ILL_ESC", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.INTLIT_action 
            actions[50] = self.FLOATLIT_action 
            actions[54] = self.STRLIT_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	s = str(self.text)
            	s = s[1:-1]
            	self.text = s

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	s = str(self.text)
            	raise IllegalEscape(s[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                s = str(self.text)
                e = '\r\n'
                if s[-1] in e:
                    raise UncloseString(s[1:-1])
                else:
                    raise UncloseString(s[1:])

     


