from Scanner import TScanner
from NewTree import *
from constants_for_scanner import *


class TDiagram:
    def __init__(self, scan):
        self.sc = scan
        self.tree = Node()
        set_scanner(self.sc)
        self.tree.set_current(self.tree)

    # Программа
    def program(self):
        uk1 = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        type_lexeme1 = self.sc.scan()[1]
        type_lexeme2 = self.sc.scan()[1]
        self.sc.put_uk(uk1)
        while type_lexeme != TEnd:
            if type_lexeme == TStruct:
                self.struct()
            else:
                if (type_lexeme == TMain) | (type_lexeme1 == TMain) | (type_lexeme2 == TMain):
                    self.main()
                    break
                else:
                    self.data()
            uk1 = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            type_lexeme1 = self.sc.scan()[1]
            type_lexeme2 = self.sc.scan()[1]
            self.sc.put_uk(uk1)

    # Функция
    def main(self):
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TShort:
            self.sc.print_error("Ожидалось short", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TInt:
            self.sc.print_error("Ожидалось int", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TMain:
            self.sc.print_error("Ожидалось main", lexeme)
        self.tree.semantic_include('main', DATA_TYPE.index('TYPE_MAIN'))
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBracket:
            self.sc.print_error("Ожидалось (", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TRBracket:
            self.sc.print_error("Ожидалось )", lexeme)
        self.block()

    # Данные
    def data(self):
        lexeme_data, type_data = self.sc.scan()
        if (type_data != TShort) & (type_data != TDouble) & (type_data != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lexeme_data)
        if type_data == TShort:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TInt:
                self.sc.print_error("Ожидалось int", lexeme)
        while True:
            id_struct = None
            if type_data == TIdent:
                if self.tree.find_struct_declaration(lexeme_data) is None:
                    self.sc.print_error('Отстутствует описание структуры', lexeme_data)
                else:
                    id_struct = lexeme_data
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            if id_struct is not None:
                v = self.tree.semantic_include(lexeme, type_data, id_struct)
            else:
                v = self.tree.semantic_include(lexeme, type_data)
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme == TAssigment:
                a = self.priority_level_1()
                v.check_data_types(a)
                lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TComma:
                break

        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    # Данные структуры
    def data_in_structs(self, id_struct):
        lexeme, type_data = self.sc.scan()
        uk = self.sc.get_uk()
        if (type_data != TShort) & (type_data != TDouble) & (type_data != TIdent):
            self.sc.print_error("Ошибка описания. Ожидалось short, double или название структуры", lexeme)
        if type_data == TShort:
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TInt:
                self.sc.print_error("Ожидалось int", lexeme)
        while True:
            id_struct = None
            if type_data == TIdent:
                if self.tree.find_struct_declaration(lexeme) is None:
                    scanner.print_error('Отстутствует описание структуры', id)
                else:
                    id_struct = lexeme
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            if id_struct is not None:
                v = self.tree.semantic_include(lexeme, type_data, id_struct)
            else:
                v = self.tree.semantic_include(lexeme, type_data)
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TComma:
                break
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    # Структура
    def struct(self):
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TStruct:
            self.sc.print_error("Ожидалось struct", lexeme)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TIdent:
            self.sc.print_error("Ожидался идентификатор", lexeme)
        v = self.tree.semantic_include(lexeme, DATA_TYPE.index('TYPE_STRUCT'))
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBrace:
            self.sc.print_error("Ожидалась {", lexeme)
        while True:
            self.data_in_structs(v.data_in_node.id)
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme == TRBrace:
                break
            self.sc.put_uk(uk)
        if type_lexeme != TRBrace:
            self.sc.print_error("Ожидалась }", lexeme)
        self.tree.set_current(v)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалась ;", lexeme)

    # Блок
    def block(self):
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TLBrace:
            self.sc.print_error("Ожидалось {", lexeme)
        v = self.tree.semantic_include('блок', DATA_TYPE.index('TYPE_UNKNOWN'))
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
                self.operator()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            uk2 = self.sc.get_uk()
            lexeme, t2 = self.sc.scan()
        self.sc.put_uk(uk2)
        if type_lexeme != TRBrace:
            self.sc.print_error("Ожидалась }", lexeme)
        self.tree.set_current(v)

    # Оператор
    def operator(self):
        uk = self.sc.get_uk()
        lex, t = self.sc.scan()
        self.sc.put_uk(uk)
        if t == TSemicolon:
            lex, t = self.sc.scan()
        elif t == TLBrace:
            self.block()
        elif t == TIf:
            self.if_operator()
        else:
            self.assignment()

    # Присваивание
    def assignment(self):
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TIdent:
            self.sc.print_error("Ожидался идентификатор", lexeme)
        v = self.tree.semantic_get_node(lexeme)
        if v.data_in_node.data_type == DATA_TYPE.index('TYPE_STRUCT'):
            self.sc.print_error('Нельзя присваивать значение типу данных.', v.data_in_node.id)
        lexeme, type_lexeme = self.sc.scan()
        while type_lexeme == TDotLink:
            if v.data_in_node.id_struct == '':
                self.sc.print_error("Переменная не является структурой.", v.data_in_node.id)
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TIdent:
                self.sc.print_error("Ожидался идентификатор", lexeme)
            v = v.get_node_struct(lexeme)
            lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TAssigment:
            self.sc.print_error("Ожидалось =", lexeme)
        type1 = self.priority_level_1()
        v.check_data_types(type1)
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme != TSemicolon:
            self.sc.print_error("Ожидалось ;", lexeme)

    def priority_level_1(self):
        type1 = self.priority_level_2()
        uk = self.sc.get_uk()
        lexeme, type_lexeme = self.sc.scan()
        while (type_lexeme == TMore) or (type_lexeme == TMoreEqual) or \
                (type_lexeme == TLess) or (type_lexeme == TLessEqual):
            type2 = self.priority_level_2()
            type1 = self.tree.check_data_types(type1, type2)
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
        self.sc.put_uk(uk)
        return type1

    def priority_level_2(self):
        type1 = self.priority_level_3()
        uk = self.sc.get_uk()
        lex, t = self.sc.scan()
        while (t == TRShift) | (t == TLShift):
            type2 = self.priority_level_3()
            type1 = self.tree.check_data_types(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scan()
        self.sc.put_uk(uk)
        return type1

    def priority_level_3(self):
        type1 = self.priority_level_4()
        uk = self.sc.get_uk()
        lex, t = self.sc.scan()
        while (t == TPlus) | (t == TMinus):
            type2 = self.priority_level_4()
            type1 = self.tree.check_data_types(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scan()
        self.sc.put_uk(uk)
        return type1

    def priority_level_4(self):
        type1 = self.elementary_expression()
        uk = self.sc.get_uk()
        lex, t = self.sc.scan()
        while (t == TMod) | (t == TDiv) | (t == TMul):
            type2 = self.elementary_expression()
            type1 = self.tree.check_data_types(type1, type2)
            uk = self.sc.get_uk()
            lex, t = self.sc.scan()
        self.sc.put_uk(uk)
        return type1

    def elementary_expression(self):
        lexeme, type_lexeme = self.sc.scan()
        if type_lexeme == TLBracket:
            type1 = self.priority_level_1()
            lexeme, type_lexeme = self.sc.scan()
            if type_lexeme != TRBracket:
                self.sc.print_error("Ожидалась )", lexeme)
            return type1
        elif type_lexeme == TIdent:
            v = self.tree.semantic_get_node(lexeme)
            type1 = v.get_this_type()
            uk = self.sc.get_uk()
            lexeme, type_lexeme = self.sc.scan()
            while type_lexeme == TDotLink:
                lexeme, type_lexeme = self.sc.scan()
                if type_lexeme != TIdent:
                    self.sc.print_error('Ожидался идентификатор', lexeme)
                v = v.get_node_struct(lexeme)
                type1 = v.get_this_type()
                uk = self.sc.get_uk()
                lexeme, type_lexeme = self.sc.scan()
            self.sc.put_uk(uk)
            return type1
        elif (type_lexeme != TConstDoubleExp) & (type_lexeme != TConstInt10):
            self.sc.print_error("Ожидался идентификатор или константа", lexeme)
        elif type_lexeme == TConstInt10:
            return DATA_TYPE.index('TYPE_SHORT_INT')
        elif type_lexeme == TConstDoubleExp:
            return DATA_TYPE.index('TYPE_DOUBLE')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    # Условный оператор
    def if_operator(self):
        lex, t = self.sc.scan()
        if t != TIf:
            self.sc.print_error("Ожидался if", lex)
        lex, t = self.sc.scan()
        if t != TLBracket:
            self.sc.print_error("Ожидался (", lex)
        type1 = self.priority_level_1()
        self.tree.check_bool(type1)
        lex, t = self.sc.scan()
        if t != TRBracket:
            self.sc.print_error("Ожидался )", lex)
        self.operator()
        uk = self.sc.get_uk()
        lex, t = self.sc.scan()
        if t == TElse:
            self.operator()
        else:
            self.sc.put_uk(uk)


def __main__():
    scanner = TScanner("for_tree.txt")
    td = TDiagram(scanner)
    td.program()
    td.tree.print()


__main__()