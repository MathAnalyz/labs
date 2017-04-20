# coding=utf-8
import re

from sklearn.preprocessing import label
import goto
from goto import with_goto

from constants_for_scanner import *


class TScanner:
    def __init__(self, filename):
        self.text = ''
        self.position = 0
        self.num_str = 1
        self.get_data(filename)
        self.save_num_str = 0

    def put_uk(self, position):
        self.num_str = self.save_num_str
        self.position = position

    def get_uk(self):
        self.save_num_str = self.num_str
        return self.position

    def print_error(self, error, symbol):
        text = ''
        for i in range(self.position):
            text += self.text[i]
        print(text)
        if symbol == '\0':
            print('Ошибка : ', error)
        else:
            print('Ошибка(', self.num_str, ') :', error, '(', symbol, ').')
        exit(0)

    def get_data(self, filename):
        inp_file = open(filename)
        self.text = inp_file.read()
        self.text = re.sub('^\s+|^\n+|\s+$|\n+$', '', self.text)
        inp_file.close()

    @with_goto
    def scan(self):
        i = 0
        lexeme = ''
        label.start
        if self.position != len(self.text):
            while self.text[self.position] == ' ' or self.text[self.position] == '\n' or \
                            self.text[self.position] == '\t':
                if self.text[self.position] == '\n' or self.text[self.position] == '\t' or \
                                self.text[self.position] == '\r':
                    self.num_str += 1
                self.position += 1
            if self.text[self.position] == '/':
                if self.text[self.position + 1] == '/':
                    while self.text[self.position] != '\n':
                        if self.position + 1 == len(self.text):
                            return '', TEnd
                        else:
                            self.position += 1
                    goto.start
            if self.position == len(self.text):
                return lexeme, TEnd
            if (self.text[self.position] <= '9') and (self.text[self.position] >= '0'):
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                while (self.text[self.position] <= '9') and (self.text[self.position] >= '0'):
                    if i < (MAX_LEX - 1):
                        lexeme += self.text[self.position]
                        i += 1
                    if len(self.text) != self.position + 1:
                        self.position += 1
                    else:
                        goto.start
                if len(lexeme) > MAX_CONST:
                    self.print_error('Слишком длинная константа', lexeme)
                if self.text[self.position] == '.':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    goto.N1
                if (self.text[self.position] == 'E') | (self.text[self.position] == 'e'):
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    goto.N2
                return lexeme, TConstInt10
            elif ('z' >= self.text[self.position]) and (self.text[self.position] >= 'a') or \
                            ('Z' >= self.text[self.position]) and (self.text[self.position] >= 'A'):
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                while (self.text[self.position] <= '9') and (self.text[self.position] >= '0') or \
                                (self.text[self.position] <= 'z') and (self.text[self.position] >= 'a') or \
                                (self.text[self.position] <= 'Z') and (self.text[self.position] >= 'A'):
                    if i < (MAX_LEX - 1):
                        lexeme += self.text[self.position]
                        i += 1
                    if len(self.text) != self.position + 1:
                        self.position += 1
                    else:
                        goto.start
                for j in range(len(keywords)):
                    if keywords[j] == lexeme:
                        return lexeme, index_keywords[j]
                return lexeme, TIdent
            elif self.text[self.position] == '.':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                if self.text[self.position] == '.':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    goto.N1
                return lexeme, TDotLink
            elif self.text[self.position] == ';':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TSemicolon
            elif self.text[self.position] == ',':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TComma
            elif self.text[self.position] == '(':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TLBracket
            elif self.text[self.position] == ')':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TRBracket
            elif self.text[self.position] == '{':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TLBrace
            elif self.text[self.position] == '}':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TRBrace
            elif self.text[self.position] == '+':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TPlus
            elif self.text[self.position] == '-':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TMinus
            elif self.text[self.position] == '*':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TMul
            elif self.text[self.position] == '/':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TDiv
            elif self.text[self.position] == '%':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TMod
            elif self.text[self.position] == '=':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                return lexeme, TAssignment
            elif self.text[self.position] == '>':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                if self.text[self.position] == '=':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    return lexeme, TMoreEqual
                if self.text[self.position] == '>':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    return lexeme, TLShift
                return lexeme, TMore
            elif self.text[self.position] == '<':
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                if self.text[self.position] == '=':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    return lexeme, TLessEqual
                if self.text[self.position] == '>':
                    lexeme += self.text[self.position]
                    i += 1
                    self.position += 1
                    return lexeme, TRShift
                return lexeme, TLess
            else:
                self.print_error('Неверный символ', lexeme)
                self.position += 1
                return lexeme, TErr

            label.N1
            while (self.text[self.position] <= '9') & (self.text[self.position] >= '0'):
                if i < (MAX_LEX - 1):
                    lexeme += self.text[self.position]
                    i += 1
                if len(self.text) != self.position + 1:
                    self.position += 1
                else:
                    goto.start
            if (self.text[self.position] == 'E') | (self.text[self.position] == 'e'):
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                goto.N2
            self.print_error('Неверная константа', lexeme)
            return lexeme, TErr

            label.N2
            if (self.text[self.position] == '-') | (self.text[self.position] == '+'):
                lexeme += self.text[self.position]
                i += 1
                self.position += 1
                if (self.text[self.position] <= '9') & (self.text[self.position] >= '0'):
                    if i < (MAX_LEX - 1):
                        lexeme += self.text[self.position]
                        i += 1
                    if len(self.text) != self.position + 1:
                        self.position += 1
                    else:
                        goto.start
                    goto.N3
                else:
                    self.print_error('Неверная константа', lexeme)
                    return lexeme, TErr

            label.N3
            while (self.text[self.position] <= '9') & (self.text[self.position] >= '0'):
                if i < (MAX_LEX - 1):
                    lexeme += self.text[self.position]
                    i += 1
                if len(self.text) != self.position + 1:
                    self.position += 1
                else:
                    goto.start
            if len(lexeme) > MAX_CONST:
                self.print_error('Слишком длинная константа', lexeme)
            return lexeme, TConstDoubleExp
        else:
            return '', TEnd


def __main__():
    sc = TScanner('for_diagrams.txt')
    while True:
        lexeme, type_lex = sc.scan()
        print(lexeme, ' - тип ', type_lex)
        if type_lex == TEnd:
            break

# __main__()