from Tree import *

class TDiagram:
    def __init__(self, scaner):
        self.sc = scaner
        self.root = Tree()
        self.root.setScaner(self.sc)
        self.root.setCur(self.root)


    # Программа
    def P(self):
        uk1 = self.sc.get_uk()
        lex, t = self.sc.scaner()
        t1 = self.sc.scaner()[1]
        t2 = self.sc.scaner()[1]
        self.sc.put_uk(uk1)
        while t != TEnd:
            if t == TStruct:
                self.S()
            else:
                if (t == TMain) | (t1 == TMain) | (t2 == TMain):
                    self.F()
                else:
                    self.D()
            uk1 = self.sc.get_uk()
            lex, t = self.sc.scaner()
            t1 = self.sc.scaner()[1]
            t2 = self.sc.scaner()[1]
            self.sc.put_uk(uk1)

    # Функция
    def F(self):
        lex, t = self.sc.scaner()
        if t != TShort:
            self.sc.print_error("Ожидалось short", lex)
        lex, t = self.sc.scaner()
        if t != TInt:
            self.sc.print_error("Ожидалось int", lex)
        typeLex = self.root.getDataType(lex, t);
        lex, t = self.sc.scaner()
        if t != TMain:
            self.sc.print_error("Ожидалось main", lex)
        self.root.semInclude(lex, DATA_TYPE.index('TYPE_FUNCT'))
        lex, t = self.sc.scaner()
        if t != TLBracket:
            self.sc.print_error("Ожидалось (", lex)
        lex, t = self.sc.scaner()
        if t != TRBracket:
            self.sc.print_error("Ожидалось )", lex)
        self.B()

    # Данные
    def D(self):
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        lex2, t = self.sc.scaner()
        if (t != TShort) & (t != TDouble) & (t != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lex)
        if t == TShort:
            lex, t = self.sc.scaner()
            if t != TInt:
                self.sc.print_error("Ожидалось int", lex)
        typeLex = self.root.getDataType(lex, t)
        while True:
            lex, t = self.sc.scaner()
            if t != TIdent:
                self.sc.print_error("Ожидался идентификатор", lex)
            v = self.root.semInclude(lex, typeLex, lex2)
            lex, t = self.sc.scaner()
            if t == TAssigment:
                a = self.V()
                v.checkDataTypes(a)
                lex, t = self.sc.scaner()
            if t != TComma:
                break
        if t != TSemicolon:
            self.sc.print_error("Ожидалась ;", lex)

    # Данные структуры
    def DS(self):
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        lex2, t = self.sc.scaner()
        if (t != TShort) & (t != TDouble) & (t != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lex)
        if t == TShort:
            lex, t = self.sc.scaner()
            if t != TInt:
                self.sc.print_error("Ожидалось int", lex)
            typeLex = self.root.getDataType(lex + lex2, t)
        else:
            typeLex = self.root.getDataType(lex, t)
        while True:
            lex, t = self.sc.scaner()
            if t != TIdent:
                self.sc.print_error("Ожидался идентификатор", lex)
            v = self.root.semInclude(lex, typeLex, lex2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
            if t != TComma:
                break
        if t != TSemicolon:
            self.sc.print_error("Ожидалась ;", lex)

    # Структура
    def S(self):
        lex, t = self.sc.scaner()
        if t != TStruct:
            self.sc.print_error("Ожидалось struct", lex)
        lex, t = self.sc.scaner()
        if t != TIdent:
            self.sc.print_error("Ожидался идентификатор", lex)
        v = self.root.semInclude(lex, DATA_TYPE.index('TYPE_STRUCT'))
        lex, t = self.sc.scaner()
        if t != TLBrace:
            self.sc.print_error("Ожидалась {", lex)
        while True:
            self.DS()
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
            if t == TRBrace:
                break
            self.sc.put_uk(uk)
        if t != TRBrace:
            self.sc.print_error("Ожидалась }", lex)
        self.root.setCur(v)
        lex, t = self.sc.scaner()
        if t != TSemicolon:
            self.sc.print_error("Ожидалась ;", lex)

    # Блок
    def B(self):
        lex, t = self.sc.scaner()
        if t != TLBrace:
            self.sc.print_error("Ожидалось {", lex)
        v = self.root.semInclude("EMPTY", EMPTY)
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        uk2 = self.sc.get_uk()
        lex, t2 = self.sc.scaner()
        while t != TRBrace:
            self.sc.put_uk(uk)
            if ((t == TShort) & (t2 == TInt)) | (t == TDouble) | ((t == TIdent) & (t2 == TIdent)):
                self.D()
            else:
                self.O()
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
            uk2 = self.sc.get_uk()
            lex, t2 = self.sc.scaner()
        self.sc.put_uk(uk2)
        if t != TRBrace:
            self.sc.print_error("Ожидалась }", lex)
        self.root.setCur(v)

    # Оператор
    def O(self):
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        if t == TSemicolon:
            lex, t = self.sc.scaner()
        elif t == TLBrace:
            self.B()
        elif t == TIf:
            self.I()
        else:
            self.R()

    # Присваивание
    def R(self):
        lex, t = self.sc.scaner()
        if t != TIdent:
            self.sc.print_error("Ожидался идентификатор", lex)
        v = self.root.semGetType(lex)
        lex, t = self.sc.scaner()
        while t == TDotLink:
            lex, t = self.sc.scaner()
            if t != TIdent:
                self.sc.print_error("Ожидался идентификатор", lex)
            v = v.getUzelStruct(lex)
            lex, t = self.sc.scaner()
        if t != TAssigment:
            self.sc.print_error("Ожидалось =", lex)
        typeV = self.V()
        v.checkDataTypes(typeV)
        lex, t = self.sc.scaner()
        if t != TSemicolon:
            self.sc.print_error("Ожидалось ;", lex)

    def V(self):
        type1 = self.W()
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        while (t == TMore) | (t == TMoreEqual) | (t == TLess) | (t == TLessEqual):
            type2 = self.W()
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        return type1

    def W(self):
        type1 = self.X()
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        while (t == TRShift) | (t == TLShift):
            type2 = self.X()
            type1 = self.root.checkDataTypes(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        return type1

    def X(self):
        type1 = self.Y()
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        while (t == TPlus) | (t == TMinus):
            type2 = self.Y()
            type1 = self.root.checkDataTypes(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        return type1

    def Y(self):
        type1 = self.Z()
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        while (t == TMod) | (t == TDiv) | (t == TMul):
            type2 = self.Z()
            type1 = self.root.checkDataTypes(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
        self.sc.put_uk(uk)
        return type1

    def Z(self):
        lex, t = self.sc.scaner()
        if t == TLBracket:
            typeV = self.V()
            lex, t = self.sc.scaner()
            if t != TRBracket:
                self.sc.print_error("Ожидалась )", lex)
            return typeV
        elif t == TIdent:
            v = self.root.semGetType(lex)
            typeV = v.getThisType()
            uk = self.sc.get_uk()
            lex, t = self.sc.scaner()
            while t == TDotLink:
                lex, t = self.sc.scaner()
                if t != TIdent:
                    self.sc.print_error('Ожидался идентификатор', lex)
                v = v.getUzelStruct(lex)
                typeV = v.getThisType()
                uk = self.sc.get_uk()
                lex, t = self.sc.scaner()
            self.sc.put_uk(uk)
            return typeV
        elif (t != TConstDoubleExp) & (t != TConstInt10):
            self.sc.print_error("Ожидался идентификатор или константа", lex)
        elif t == TConstInt10:
            return DATA_TYPE.index('TYPE_INTEGER')
        elif t == TConstDoubleExp:
            return DATA_TYPE.index('TYPE_DOUBLE')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    # Условный оператор
    def I(self):
        lex, t = self.sc.scaner()
        if t != TIf:
            self.sc.print_error("Ожидался if", lex)
        lex, t = self.sc.scaner()
        if t != TLBracket:
            self.sc.print_error("Ожидался (", lex)
        typeV = self.V()
        self.root.checkDataTypeToBool(typeV)
        lex, t = self.sc.scaner()
        if t != TRBracket:
            self.sc.print_error("Ожидался )", lex)
        self.O()
        uk = self.sc.get_uk()
        lex, t = self.sc.scaner()
        if t == TElse:
            self.O()
        else:
            self.sc.put_uk(uk)

    def printTree(self):
        self.root.print()

def __main__():
    scaner = TScaner("input.txt")
    td = TDiagram(scaner)
    td.P()
    td.printTree()


__main__()