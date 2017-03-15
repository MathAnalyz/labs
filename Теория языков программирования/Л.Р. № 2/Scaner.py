# coding=utf-8
import re

import goto
from goto import with_goto

# Идентификатор и ключевые слова
from sklearn.preprocessing import label

MAX_LEX = 25
MAX_CONST = 10

TIdent = 1
TMain = 2
TIf = 3
TElse = 4
TShort = 5
TInt = 6
TDouble = 7
TStruct = 8
# Константы
TConstInt10 = 9
TConstDoubleExp = 10
# Точка для обращения к элементу структуры
TDotLink = 11
# знаки операций
TMore = 12
TMoreEqual = 13
TLess = 14
TLessEqual = 15
TRShift = 16
TLShift = 17
TPlus = 18
TMinus = 19
TMul = 20
TDiv = 21
TMod = 22
# Точка с запятой, скобки, присваивание
TSemicolon = 23
TLBracket = 24
TRBracket = 25
TLBrace = 26
TRBrace = 27
TAssigment = 28
TComma = 29
# Ошибочный символ
TErr = 30
# Конец исходного модуля
TEnd = 31

keywords = ['main', 'if', 'else', 'short', 'int', 'double', 'struct']
index_keywords = [TMain, TIf, TElse, TShort, TInt, TDouble, TStruct]


class TScaner:
    def __init__(self, filename):
        self.get_data(filename)
        self.put_uk(0)
        self.num_str = 1

    def put_uk(self, position):
        self.uk = position

    def get_uk(self):
        return self.uk

    def print_error(self, error, symbol):
        text = ''
        for i in range(self.uk):
            text += self.t[i]
        print(text)
        if symbol == '\0':
            print('Ошибка : ', error)
        else:
            print('Ошибка(', self.num_str, ') :', error, '(', symbol, ').')
        exit(0)

    def get_data(self, filename):
        inp_file = open(filename)
        self.t = inp_file.read()
        self.t = re.sub('^\s+|^\n+|\s+$|\n+$', '', self.t)
        inp_file.close()

    @with_goto
    def scaner(self):
        i = 0
        lex = ''
        label .start
        if self.uk != len(self.t):
            while (self.t[self.uk] == ' ') | (self.t[self.uk] == '\n') | (self.t[self.uk] == '\t'):
                if (self.t[self.uk] == '\n') | (self.t[self.uk] == 't') | (self.t[self.uk] == '\r'):
                    self.num_str += 1
                self.uk += 1
            if self.t[self.uk] == '/':
                if self.t[self.uk+1] == '/':
                    self.uk += 2
                    while (self.t[self.uk] != '\n') & (self.t[self.uk] != '#'):
                        self.uk += 1
                    if (self.t[self.uk] == '\0') | (self.uk == len(self.t)):
                        return '', TEnd
                    goto.start
            if self.uk == len(self.t):
                self.uk += 1
                lex += '#'
                return lex, TEnd
            if (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0'):
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                while (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0'):
                    if i < (MAX_LEX - 1):
                        lex += self.t[self.uk]
                        i += 1
                        self.uk += 1
                    else:
                        self.uk += 1
                if len(lex) > MAX_CONST:
                    self.print_error('Слишком длинная константа', lex)
                if self.t[self.uk] == '.':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    goto .N1
                if (self.t[self.uk] == 'E') | (self.t[self.uk] == 'e'):
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    goto .N2
                return lex, TConstInt10
            elif (self.t[self.uk] <= 'z') & (self.t[self.uk] >= 'a') | \
                            (self.t[self.uk] <= 'Z') & (self.t[self.uk] >= 'A'):
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                while (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0') | \
                                (self.t[self.uk] <= 'z') & (self.t[self.uk] >= 'a') | \
                                (self.t[self.uk] <= 'Z') & (self.t[self.uk] >= 'A'):
                    if i < (MAX_LEX - 1):
                        lex += self.t[self.uk]
                        i += 1
                        self.uk += 1
                    else:
                        self.uk += 1
                for j in range(len(keywords)):
                    if keywords[j] == lex:
                        return lex, index_keywords[j]
                return lex, TIdent
            elif self.t[self.uk] == '.':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                if self.t[self.uk] == '.':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    goto .N1
                return lex, TDotLink
            elif self.t[self.uk] == ';':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TSemicolon
            elif self.t[self.uk] == ',':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TComma
            elif self.t[self.uk] == '(':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TLBracket
            elif self.t[self.uk] == ')':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TRBracket
            elif self.t[self.uk] == '{':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TLBrace
            elif self.t[self.uk] == '}':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TRBrace
            elif self.t[self.uk] == '+':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TPlus
            elif self.t[self.uk] == '-':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TMinus
            elif self.t[self.uk] == '*':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TMul
            elif self.t[self.uk] == '/':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TDiv
            elif self.t[self.uk] == '%':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TMod
            elif self.t[self.uk] == '=':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                return lex, TAssigment
            elif self.t[self.uk] == '>':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                if self.t[self.uk] == '=':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    return lex, TMoreEqual
                if self.t[self.uk] == '>':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    return lex, TLShift
                return lex, TMore
            elif self.t[self.uk] == '<':
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                if self.t[self.uk] == '=':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    return lex, TLessEqual
                if self.t[self.uk] == '>':
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                    return lex, TRShift
                return lex, TLess
            else:
                self.print_error('Неверный символ', lex)
                self.uk += 1
                return lex, TErr

            label.N1
            while (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0'):
                if i < (MAX_LEX - 1):
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                else:
                    self.uk += 1
            if (self.t[self.uk] == 'E') | (self.t[self.uk] == 'e'):
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                goto.N2
            self.print_error('Неверная константа', lex)
            return lex, TErr

            label.N2
            if (self.t[self.uk] == '-') | (self.t[self.uk] == '+'):
                lex += self.t[self.uk]
                i += 1
                self.uk += 1
                if (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0'):
                    if i < (MAX_LEX - 1):
                        lex += self.t[self.uk]
                        i += 1
                        self.uk += 1
                    else:
                        self.uk += 1
                    goto.N3
                else:
                    self.print_error('Неверная константа', lex)
                    return lex, TErr

            label.N3
            while (self.t[self.uk] <= '9') & (self.t[self.uk] >= '0'):
                if i < (MAX_LEX - 1):
                    lex += self.t[self.uk]
                    i += 1
                    self.uk += 1
                else:
                    self.uk += 1
            if len(lex) > MAX_CONST:
                self.print_error('Слишком длинная константа', lex)
            return lex, TConstDoubleExp
        else:
            return '', TEnd



'''sc = TScaner('input.txt')
while True:
    lex = ''
    lex, type_lex = sc.scaner(lex)
    print(lex, ' - тип ', type_lex)
    if type_lex == TEnd:
        break
'''