from Tree import *
from Scanner import TScanner


class TDiagram:
    """ Класс, реализующий синтаксический анализатор методом рекурсивного спуска. """

    def __init__(self, scan: TScanner):
        """
        Инициализирует синтаксический анализатор.
        """
        self.sc = scan
        self.root = Tree()
        set_scanner(self.sc)
        self.root.set_cur(self.root)

    def program(self):
        """ <Программа> """
        uk1 = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        t1 = self.sc.scan()[1]
        t2 = self.sc.scan()[1]
        self.sc.put_uk(uk1)
        while type_lexeme != TEnd:
            if type_lexeme == TStruct:
                self.struct()
            else:
                if (type_lexeme == TMain) | (t1 == TMain) | (t2 == TMain):
                    self.main()
                else:
                    self.data()
            uk1 = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            t1 = self.sc.scan()[1]
            t2 = self.sc.scan()[1]
            self.sc.put_uk(uk1)

    def main(self):
        """ <функция> """
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TShort:
            self.sc.print_error("Ожидалось short", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TInt:
            self.sc.print_error("Ожидалось int", lexeme)
        self.root.get_data_type(lexeme, type_lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TMain:
            self.sc.print_error("Ожидалось main", lexeme)
        self.root.sem_include(lexeme, DATA_TYPE.index('TYPE_FUNCT'))
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBracket:
            self.sc.print_error("Ожидалось (", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TRBracket:
            self.sc.print_error("Ожидалось )", lexeme)
        self.block()

    def data(self):
        """<данные>"""
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        lex2, type_lexeme = self.sc.scan()
        if (type_lexeme != TShort) & (type_lexeme != TDouble) & (type_lexeme != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lexeme)
        if type_lexeme == TShort:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TInt:
                self.sc.print_error("Ожидалось int", lexeme)
        self.root.get_data_type(lexeme, type_lexeme)
        while True:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            v = self.root.sem_include(lexeme, type_lexeme, lex2)
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme == TAssigment:
                a, value = self.priority_level_1()
                value = to_common_type(v.check_data_types(a), value)
                v.node.set_value(value)
                lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TComma:
                break
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    def data_in_struct(self):
        """<данные структуры>"""
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        lex2, type_lexeme = self.sc.scan()
        if (type_lexeme != TShort) & (type_lexeme != TDouble) & (type_lexeme != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lexeme)
        if type_lexeme == TShort:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TInt:
                self.sc.print_error("Ожидалось int", lexeme)
            self.root.get_data_type(lexeme + lex2, type_lexeme)
        else:
            self.root.get_data_type(lexeme, type_lexeme)
        while True:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            v = self.root.sem_include(lexeme, type_lexeme, lex2)
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TComma:
                break
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    def struct(self):
        """<struct>"""
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TStruct:
            self.sc.print_error("Ожидалось struct", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TIdent:
            self.sc.print_error("Ожидался идентификатор", lexeme)
        v = self.root.sem_include(lexeme, DATA_TYPE.index('TYPE_STRUCT'))
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBrace:
            self.sc.print_error("Ожидалась {", lexeme)
        while True:
            self.data_in_struct()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme == TRBrace:
                break
            self.sc.put_uk(uk)
        if type_lexeme != TRBrace:
            self.sc.print_error("Ожидалась }", lexeme)
        self.root.set_cur(v)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    def block(self):
        """<блок>"""
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBrace:
            self.sc.print_error("Ожидалось {", lexeme)
        v = self.root.sem_include("EMPTY", EMPTY)
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        uk2 = self.sc.get_uk()
        lexeme, t2 = self.sc.scan()
        while type_lexeme != TRBrace:
            self.sc.put_uk(uk)
            if ((type_lexeme == TShort) and (t2 == TInt)) or \
                    (type_lexeme == TDouble) or \
                    ((type_lexeme == TIdent) and (t2 == TIdent)):
                self.data()
            else:
                self.operators()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            uk2 = self.sc.get_uk()
            lexeme, t2 = self.sc.scan()
        self.sc.put_uk(uk2)
        if type_lexeme != TRBrace:
            self.sc.print_error("Ожидалась }", lexeme)
        self.root.set_cur(v)

    def operators(self):
        """<операторы>"""
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        if type_lexeme == TSemicolon:
            self.sc.scan()
        elif type_lexeme == TLBrace:
            self.block()
        elif type_lexeme == TIf:
            self.if_operator()
        else:
            self.assignment()

    def assignment(self):
        """<присваивание>"""
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TIdent:
            self.sc.print_error("Ожидался идентификатор", lexeme)
        v = self.root.sem_get_type(lexeme)
        lexeme, type_lexeme = self.sc.scan()
        while type_lexeme == TDotLink:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            v = v.get_node_struct(lexeme)
            lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TAssigment:
            self.sc.print_error("Ожидалось =", lexeme)
        type_v, value = self.priority_level_1()
        v.check_data_types(type_v)
        value = to_common_type(v.check_data_types(type_v), value)
        v.node.set_value(value)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалось ;", lexeme)

    def priority_level_1(self):
        """Операции сравнения."""
        type1, value = self.priority_level_2()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        while (type_lexeme == TMore) or \
                (type_lexeme == TMoreEqual) or \
                (type_lexeme == TLess) or \
                (type_lexeme == TLessEqual):
            type2, value = self.priority_level_2()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        return type1, value

    def priority_level_2(self):
        """Операции сдвига."""
        type1, value = self.priority_level_3()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        while (type_lexeme == TRShift) | (type_lexeme == TLShift):
            type2, value2 = self.priority_level_3()
            type1 = self.root.check_data_types(type1, type2)
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        return type1, value

    def priority_level_3(self):
        """Сложение и вычитание."""
        type1, value = self.priority_level_4()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        while (type_lexeme == TPlus) | (type_lexeme == TMinus):
            type2, value2 = self.priority_level_4()
            type1 = self.root.check_data_types(type1, type2)
            value = to_common_type(type1, value)
            value2 = to_common_type(type1, value2)
            if type_lexeme == TPlus:
                value = value + value2
            elif type_lexeme == TMinus:
                value = value - value2
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        return type1, value

    def priority_level_4(self):
        """Умножение, деление, остаток от деления."""
        type1, value = self.elementary_expression()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        while (type_lexeme == TMod) | (type_lexeme == TDiv) | (type_lexeme == TMul):
            type2, value2 = self.elementary_expression()
            type1 = self.root.check_data_types(type1, type2)
            value = to_common_type(type1, value)
            value2 = to_common_type(type1, value2)
            if type_lexeme == TMod:
                if type1 == DATA_TYPE.index('TYPE_INTEGER'):
                    value = value % value2
                else:
                    self.sc.print_error('Неправильное использование %.', lexeme)
            elif type_lexeme == TDiv:
                value = value / value2
            elif type_lexeme == TMul:
                value = value * value2
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        return type1, value

    def elementary_expression(self):
        """Элементарное выражение."""
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme == TLBracket:
            type_v, value = self.priority_level_1()
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TRBracket:
                self.sc.print_error("Ожидалась )", lexeme)
            return type_v, value
        elif type_lexeme == TIdent:
            v = self.root.sem_get_type(lexeme)
            type_v = v.get_this_type()
            value = v.node.get_value()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            while type_lexeme == TDotLink:
                lexeme, type_lexeme = self.sc.scan()
                if type_lexeme != TIdent:
                    self.sc.print_error('Ожидался идентификатор', lexeme)
                v = v.get_node_struct(lexeme)
                type_v = v.get_this_type()
                value = v.node.get_value()
                uk = self.sc.get_uk()
                lexeme, type_lexeme = self.sc.scan()
            self.sc.put_uk(uk)
            return type_v, value
        elif (type_lexeme != TConstDoubleExp) & (type_lexeme != TConstInt10):
            self.sc.print_error("Ожидался идентификатор или константа", lexeme)
        elif type_lexeme == TConstInt10:
            return DATA_TYPE.index('TYPE_INTEGER'), int(lexeme)
        elif type_lexeme == TConstDoubleExp:
            return DATA_TYPE.index('TYPE_DOUBLE'), float(lexeme)
        return DATA_TYPE.index('TYPE_UNKNOWN'), None

    def if_operator(self):
        """<условный оператор>"""
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TIf:
            self.sc.print_error("Ожидался if", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBracket:
            self.sc.print_error("Ожидался (", lexeme)
        type_v = self.priority_level_1()
        self.root.check_data_type_to_bool(type_v)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TRBracket:
            self.sc.print_error("Ожидался )", lexeme)
        self.operators()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme == TElse:
            self.operators()
        else:
            self.sc.put_uk(uk)

    def print_tree(self):
        """Вывод дерева."""
        self.root.print()


def to_common_type(common_type: DATA_TYPE, val):
    """Приводит число val к соответствующему типу (int, double)."""
    v = val
    if common_type == DATA_TYPE.index('TYPE_INTEGER'):
        v = int(v)
    elif common_type == DATA_TYPE.index('TYPE_DOUBLE'):
        v = float(v)
    return v


def __main__():
    scn = TScanner("for_tree.txt")
    td = TDiagram(scn)
    td.program()
    td.print_tree()


__main__()
