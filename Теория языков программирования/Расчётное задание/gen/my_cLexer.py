# Generated from D:/Git/labs/Теория языков программирования/Расчётное задание\my_c.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2#")
        buf.write("\u0124\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\7\35\u00b7\n\35\f\35\16\35\u00ba")
        buf.write("\13\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\5!\u00c4\n!\3\"")
        buf.write("\3\"\3#\3#\7#\u00ca\n#\f#\16#\u00cd\13#\3#\5#\u00d0\n")
        buf.write("#\3$\3$\3%\3%\3&\3&\5&\u00d8\n&\3&\3&\3&\5&\u00dd\n&\3")
        buf.write("\'\5\'\u00e0\n\'\3\'\3\'\3\'\3\'\3\'\5\'\u00e7\n\'\3(")
        buf.write("\3(\5(\u00eb\n(\3(\3(\3(\5(\u00f0\n(\3(\5(\u00f3\n(\3")
        buf.write(")\3)\3*\6*\u00f8\n*\r*\16*\u00f9\3+\6+\u00fd\n+\r+\16")
        buf.write("+\u00fe\3+\3+\3,\3,\5,\u0105\n,\3,\5,\u0108\n,\3,\3,\3")
        buf.write("-\3-\3-\3-\7-\u0110\n-\f-\16-\u0113\13-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\7.\u011e\n.\f.\16.\u0121\13.\3.\3.\3\u0111")
        buf.write("\2/\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\2=\2?\2A\37C\2E\2G\2")
        buf.write("I\2K\2M\2O\2Q\2S\2U W!Y\"[#\3\2\t\5\2C\\aac|\3\2\62;\3")
        buf.write("\2\62\62\3\2\63;\4\2--//\4\2\13\13\"\"\4\2\f\f\17\17\2")
        buf.write("\u0129\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2A\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\3]\3\2\2\2\5b\3\2\2\2\7i\3")
        buf.write("\2\2\2\tn\3\2\2\2\13q\3\2\2\2\ru\3\2\2\2\17|\3\2\2\2\21")
        buf.write("\u0082\3\2\2\2\23\u0089\3\2\2\2\25\u008b\3\2\2\2\27\u008d")
        buf.write("\3\2\2\2\31\u008f\3\2\2\2\33\u0091\3\2\2\2\35\u0093\3")
        buf.write("\2\2\2\37\u0096\3\2\2\2!\u0098\3\2\2\2#\u009b\3\2\2\2")
        buf.write("%\u009e\3\2\2\2\'\u00a1\3\2\2\2)\u00a3\3\2\2\2+\u00a5")
        buf.write("\3\2\2\2-\u00a7\3\2\2\2/\u00a9\3\2\2\2\61\u00ab\3\2\2")
        buf.write("\2\63\u00ad\3\2\2\2\65\u00af\3\2\2\2\67\u00b1\3\2\2\2")
        buf.write("9\u00b3\3\2\2\2;\u00bb\3\2\2\2=\u00bd\3\2\2\2?\u00bf\3")
        buf.write("\2\2\2A\u00c3\3\2\2\2C\u00c5\3\2\2\2E\u00cf\3\2\2\2G\u00d1")
        buf.write("\3\2\2\2I\u00d3\3\2\2\2K\u00dc\3\2\2\2M\u00e6\3\2\2\2")
        buf.write("O\u00f2\3\2\2\2Q\u00f4\3\2\2\2S\u00f7\3\2\2\2U\u00fc\3")
        buf.write("\2\2\2W\u0107\3\2\2\2Y\u010b\3\2\2\2[\u0119\3\2\2\2]^")
        buf.write("\7o\2\2^_\7c\2\2_`\7k\2\2`a\7p\2\2a\4\3\2\2\2bc\7f\2\2")
        buf.write("cd\7q\2\2de\7w\2\2ef\7d\2\2fg\7n\2\2gh\7g\2\2h\6\3\2\2")
        buf.write("\2ij\7g\2\2jk\7n\2\2kl\7u\2\2lm\7g\2\2m\b\3\2\2\2no\7")
        buf.write("k\2\2op\7h\2\2p\n\3\2\2\2qr\7k\2\2rs\7p\2\2st\7v\2\2t")
        buf.write("\f\3\2\2\2uv\7t\2\2vw\7g\2\2wx\7v\2\2xy\7w\2\2yz\7t\2")
        buf.write("\2z{\7p\2\2{\16\3\2\2\2|}\7u\2\2}~\7j\2\2~\177\7q\2\2")
        buf.write("\177\u0080\7t\2\2\u0080\u0081\7v\2\2\u0081\20\3\2\2\2")
        buf.write("\u0082\u0083\7u\2\2\u0083\u0084\7v\2\2\u0084\u0085\7t")
        buf.write("\2\2\u0085\u0086\7w\2\2\u0086\u0087\7e\2\2\u0087\u0088")
        buf.write("\7v\2\2\u0088\22\3\2\2\2\u0089\u008a\7*\2\2\u008a\24\3")
        buf.write("\2\2\2\u008b\u008c\7+\2\2\u008c\26\3\2\2\2\u008d\u008e")
        buf.write("\7}\2\2\u008e\30\3\2\2\2\u008f\u0090\7\177\2\2\u0090\32")
        buf.write("\3\2\2\2\u0091\u0092\7>\2\2\u0092\34\3\2\2\2\u0093\u0094")
        buf.write("\7>\2\2\u0094\u0095\7?\2\2\u0095\36\3\2\2\2\u0096\u0097")
        buf.write("\7@\2\2\u0097 \3\2\2\2\u0098\u0099\7@\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a\"\3\2\2\2\u009b\u009c\7>\2\2\u009c\u009d")
        buf.write("\7>\2\2\u009d$\3\2\2\2\u009e\u009f\7@\2\2\u009f\u00a0")
        buf.write("\7@\2\2\u00a0&\3\2\2\2\u00a1\u00a2\7-\2\2\u00a2(\3\2\2")
        buf.write("\2\u00a3\u00a4\7/\2\2\u00a4*\3\2\2\2\u00a5\u00a6\7,\2")
        buf.write("\2\u00a6,\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8.\3\2\2\2")
        buf.write("\u00a9\u00aa\7\'\2\2\u00aa\60\3\2\2\2\u00ab\u00ac\7=\2")
        buf.write("\2\u00ac\62\3\2\2\2\u00ad\u00ae\7.\2\2\u00ae\64\3\2\2")
        buf.write("\2\u00af\u00b0\7?\2\2\u00b0\66\3\2\2\2\u00b1\u00b2\7\60")
        buf.write("\2\2\u00b28\3\2\2\2\u00b3\u00b8\5;\36\2\u00b4\u00b7\5")
        buf.write(";\36\2\u00b5\u00b7\5? \2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9:\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00bc\5=\37\2\u00bc<\3\2\2\2\u00bd\u00be\t\2\2\2\u00be")
        buf.write(">\3\2\2\2\u00bf\u00c0\t\3\2\2\u00c0@\3\2\2\2\u00c1\u00c4")
        buf.write("\5C\"\2\u00c2\u00c4\5I%\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4B\3\2\2\2\u00c5\u00c6\5E#\2\u00c6D\3\2\2")
        buf.write("\2\u00c7\u00cb\5G$\2\u00c8\u00ca\5? \2\u00c9\u00c8\3\2")
        buf.write("\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00d0\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00d0\t\4\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00ce\3\2\2\2")
        buf.write("\u00d0F\3\2\2\2\u00d1\u00d2\t\5\2\2\u00d2H\3\2\2\2\u00d3")
        buf.write("\u00d4\5K&\2\u00d4J\3\2\2\2\u00d5\u00d7\5M\'\2\u00d6\u00d8")
        buf.write("\5O(\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00dd")
        buf.write("\3\2\2\2\u00d9\u00da\5S*\2\u00da\u00db\5O(\2\u00db\u00dd")
        buf.write("\3\2\2\2\u00dc\u00d5\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dd")
        buf.write("L\3\2\2\2\u00de\u00e0\5S*\2\u00df\u00de\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\60\2")
        buf.write("\2\u00e2\u00e7\5S*\2\u00e3\u00e4\5S*\2\u00e4\u00e5\7\60")
        buf.write("\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e7N\3\2\2\2\u00e8\u00ea\7g\2\2\u00e9\u00eb")
        buf.write("\5Q)\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec\u00f3\5S*\2\u00ed\u00ef\7G\2\2\u00ee\u00f0")
        buf.write("\5Q)\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f3\5S*\2\u00f2\u00e8\3\2\2\2\u00f2\u00ed")
        buf.write("\3\2\2\2\u00f3P\3\2\2\2\u00f4\u00f5\t\6\2\2\u00f5R\3\2")
        buf.write("\2\2\u00f6\u00f8\5? \2\u00f7\u00f6\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("T\3\2\2\2\u00fb\u00fd\t\7\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\b+\2\2\u0101V\3\2\2\2")
        buf.write("\u0102\u0104\7\17\2\2\u0103\u0105\7\f\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0108\3\2\2\2\u0106")
        buf.write("\u0108\7\f\2\2\u0107\u0102\3\2\2\2\u0107\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010a\b,\2\2\u010aX\3\2\2\2")
        buf.write("\u010b\u010c\7\61\2\2\u010c\u010d\7,\2\2\u010d\u0111\3")
        buf.write("\2\2\2\u010e\u0110\13\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("\u0113\3\2\2\2\u0111\u0112\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7")
        buf.write(",\2\2\u0115\u0116\7\61\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\b-\2\2\u0118Z\3\2\2\2\u0119\u011a\7\61\2\2\u011a\u011b")
        buf.write("\7\61\2\2\u011b\u011f\3\2\2\2\u011c\u011e\n\b\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0122\u0123\b.\2\2\u0123\\\3\2\2\2\25\2\u00b6\u00b8")
        buf.write("\u00c3\u00cb\u00cf\u00d7\u00dc\u00df\u00e6\u00ea\u00ef")
        buf.write("\u00f2\u00f9\u00fe\u0104\u0107\u0111\u011f\3\b\2\2")
        return buf.getvalue()


class my_cLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Double = 2
    Else = 3
    If = 4
    Int = 5
    Return = 6
    Short = 7
    Struct = 8
    LeftParen = 9
    RightParen = 10
    LeftBrace = 11
    RightBrace = 12
    Less = 13
    LessEqual = 14
    Greater = 15
    GreaterEqual = 16
    LeftShift = 17
    RightShift = 18
    Plus = 19
    Minus = 20
    Star = 21
    Div = 22
    Mod = 23
    Semi = 24
    Comma = 25
    Assign = 26
    Dot = 27
    Identifier = 28
    Constant = 29
    Whitespace = 30
    Newline = 31
    BlockComment = 32
    LineComment = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'double'", "'else'", "'if'", "'int'", "'return'", 
            "'short'", "'struct'", "'('", "')'", "'{'", "'}'", "'<'", "'<='", 
            "'>'", "'>='", "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "';'", "','", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "Double", "Else", "If", "Int", "Return", "Short", "Struct", 
            "LeftParen", "RightParen", "LeftBrace", "RightBrace", "Less", 
            "LessEqual", "Greater", "GreaterEqual", "LeftShift", "RightShift", 
            "Plus", "Minus", "Star", "Div", "Mod", "Semi", "Comma", "Assign", 
            "Dot", "Identifier", "Constant", "Whitespace", "Newline", "BlockComment", 
            "LineComment" ]

    ruleNames = [ "T__0", "Double", "Else", "If", "Int", "Return", "Short", 
                  "Struct", "LeftParen", "RightParen", "LeftBrace", "RightBrace", 
                  "Less", "LessEqual", "Greater", "GreaterEqual", "LeftShift", 
                  "RightShift", "Plus", "Minus", "Star", "Div", "Mod", "Semi", 
                  "Comma", "Assign", "Dot", "Identifier", "IdentifierNondigit", 
                  "Nondigit", "Digit", "Constant", "IntegerConstant", "DecimalConstant", 
                  "NonzeroDigit", "FloatingConstant", "DecimalFloatingConstant", 
                  "FractionalConstant", "ExponentPart", "Sign", "DigitSequence", 
                  "Whitespace", "Newline", "BlockComment", "LineComment" ]

    grammarFileName = "my_c.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


