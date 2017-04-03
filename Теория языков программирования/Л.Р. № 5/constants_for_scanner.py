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
