import sys
from antlr4 import *
from gen.my_cLexer import my_cLexer
from gen.my_cParser import my_cParser


def main(argv):
    input = FileStream(argv[1])
    lexer = my_cLexer(input)
    stream = CommonTokenStream(lexer)
    parser = my_cParser(stream)
    tree = parser.run_program()
    print(tree.toStringTree(ruleNames=[''], recog=parser))


if __name__ == '__main__':
    main(sys.argv)