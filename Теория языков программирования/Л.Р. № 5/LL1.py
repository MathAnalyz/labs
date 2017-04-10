from Scanner import *
from nonterminal_for_LL1 import *
from Tree import *
from stack import *
from procedures_for_sup import *


class Variable:
    type_ = 0
    value = 0
    name = ''
    id_struct = None


def ll1(sc: TScanner):
    def epsilon():
        magazine.pop()

    magazine = Stack()
    triads = []
    tree = Node()
    tree.set_current(tree)
    set_scanner(sc)
    v0 = 0
    fl = 1
    stack_for_ifs = Stack()
    operands = Stack()
    operations = Stack()
    current_variable = Variable()
    magazine.push(TEnd)
    magazine.push(neterm_Program)
    lex, t = sc.scan()

    while fl == 1:
        if magazine.get_top() < MinTypeTerminal:
            if magazine.get_top() == t:
                if t == TEnd:
                    fl = 0
                else:
                    lex, t = sc.scan()
                    magazine.pop()
            else:
                sc.print_error("Ожидался символ", lex)
        else:
            if magazine.get_top() == neterm_Program:
                magazine.pop()
                if t == TEnd:
                    epsilon()
                    break
                else:
                    magazine.push(neterm_Program)
                    magazine.push(neterm_Description)
                    current_variable.id_struct = None

            elif magazine.get_top() == neterm_Description:
                magazine.pop()
                if t == TStruct:
                    magazine.push(neterm_Struct)
                    current_variable.type_ = DATA_TYPE.index('TYPE_STRUCT')
                    current_variable.is_struct = True
                elif t == TShort:
                    uk = sc.get_uk()
                    lex1, t1 = sc.scan()
                    lex2, t2 = sc.scan()
                    sc.put_uk(uk)
                    if t1 == TInt:
                        if t2 == TMain:
                            magazine.push(neterm_Main)
                            current_variable.type_ = DATA_TYPE.index('TYPE_MAIN')
                        else:
                            magazine.push(TSemicolon)
                            magazine.push(neterm_ListOfVariables)
                            magazine.push(neterm_Type)
                            current_variable.type_ = DATA_TYPE.index('TYPE_SHORT_INT')
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                    del lex1, lex2, t1, t2, uk
                else:
                    magazine.push(TSemicolon)
                    magazine.push(neterm_ListOfVariables)
                    magazine.push(neterm_Type)
                    if t == TDouble:
                        current_variable.type_ = DATA_TYPE.index('TYPE_DOUBLE')
                    else:
                        current_variable.type_ = DATA_TYPE.index('TYPE_STRUCT')
                        current_variable.id_struct = lex

            elif magazine.get_top() == neterm_Type:
                magazine.pop()
                if t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        magazine.push(TInt)
                        magazine.push(TShort)
                    del lex1, t1
                elif t == TDouble:
                    magazine.push(TDouble)
                elif t == TIdent:
                    magazine.push(TIdent)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_Main:
                magazine.pop()
                magazine.push(proc_end_main)
                magazine.push(neterm_Block)
                magazine.push(proc_main)
                magazine.push(TRBracket)
                magazine.push(TLBracket)
                magazine.push(TMain)
                magazine.push(TInt)
                magazine.push(TShort)
                current_variable.name = 'блок'
                v0 = tree.semantic_include(current_variable.name, current_variable.type_)

            elif magazine.get_top() == proc_main:
                magazine.pop()
                triads.append(generate_triad(TMain, operand1=Operand('main')))
            elif magazine.get_top() == proc_end_main:
                magazine.pop()
                triads.append(generate_triad(TEnd, operand1=Operand('main')))

            elif magazine.get_top() == neterm_ListOfVariables:
                magazine.pop()
                magazine.push(neterm_AdditionallyList)
                magazine.push(neterm_Variable)
            elif magazine.get_top() == neterm_AdditionallyList:
                if t == TComma:
                    magazine.push(neterm_AdditionallyList)
                    magazine.push(neterm_Variable)
                    magazine.push(TComma)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_Struct:
                magazine.pop()
                magazine.push(TSemicolon)
                magazine.push(TRBrace)
                magazine.push(neterm_DescriptionsStruct)
                magazine.push(TLBrace)
                magazine.push(TIdent)
                magazine.push(TStruct)
                uk = sc.get_uk()
                current_variable.name, t1 = sc.scan()
                del t1
                sc.put_uk(uk)
                v0 = tree.semantic_include(current_variable.name,
                                           current_variable.type_,
                                           current_variable.id_struct)
            elif magazine.get_top() == neterm_DescriptionsStruct:
                if t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        magazine.push(neterm_DescriptionsStruct)
                        magazine.push(TSemicolon)
                        magazine.push(neterm_ListOfVariables)
                        magazine.push(neterm_Type)
                        current_variable.type_ = DATA_TYPE.index('TYPE_SHORT_INT')
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                    del lex1, t1
                elif (t == TDouble) | (t == TIdent):
                    magazine.push(neterm_DescriptionsStruct)
                    magazine.push(TSemicolon)
                    magazine.push(neterm_ListOfVariables)
                    magazine.push(neterm_Type)
                    if t == TDouble:
                        current_variable.type_ = DATA_TYPE.index('TYPE_DOUBLE')
                    else:
                        current_variable.type_ = DATA_TYPE.index('TYPE_STRUCT')
                        current_variable.id_struct = lex
                else:
                    tree.set_current(v0)
                    epsilon()

            elif magazine.get_top() == neterm_Variable:
                magazine.pop()
                magazine.push(neterm_Initialization)
                magazine.push(TIdent)
                current_variable.name = lex
                tree.semantic_include(current_variable.name,
                                      current_variable.type_,
                                      current_variable.id_struct)
                operands.push(Operand(lex))
            elif magazine.get_top() == neterm_Initialization:
                if t == TAssigment:
                    magazine.pop()
                    magazine.push(proc_initialization)
                    magazine.push(neterm_PriorityLevel1)
                    magazine.push(TAssigment)
                    operations.push(TAssigment)
                else:
                    epsilon()
                    operands.pop()
            elif magazine.get_top() == proc_initialization:
                magazine.pop()
                triads.append(generate_triad(operations.pop(), operands.pop(), operands.pop()))

            elif magazine.get_top() == neterm_Block:
                magazine.pop()
                magazine.push(TRBrace)
                magazine.push(neterm_ContentOfBlock)
                magazine.push(TLBrace)
            elif magazine.get_top() == neterm_DescriptionsInBlock:
                magazine.pop()
                if t == TStruct:
                    magazine.push(neterm_Struct)
                    current_variable.type_ = DATA_TYPE.index('TYPE_STRUCT')
                    current_variable.is_struct = True
                elif t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        magazine.push(TSemicolon)
                        magazine.push(neterm_ListOfVariables)
                        magazine.push(neterm_Type)
                        current_variable.type_ = DATA_TYPE.index('TYPE_SHORT_INT')
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                    del lex1, t1
                else:
                    magazine.push(TSemicolon)
                    magazine.push(neterm_ListOfVariables)
                    magazine.push(neterm_Type)
                    if t == TDouble:
                        current_variable.type_ = DATA_TYPE.index('TYPE_DOUBLE')
                    else:
                        current_variable.type_ = DATA_TYPE.index('TYPE_STRUCT')
                        current_variable.id_struct = lex
            elif magazine.get_top() == neterm_ContentOfBlock:
                uk = sc.get_uk()
                lex1, t1 = sc.scan()
                sc.put_uk(uk)
                if ((t1 == TIdent) or (t == TShort)) and (t != TLBrace):
                    magazine.push(neterm_ContentOfBlock)
                    magazine.push(neterm_DescriptionsInBlock)
                elif (t == TLBrace) or (t1 != TIdent) and (t != TRBrace):
                    magazine.push(neterm_ContentOfBlock)
                    magazine.push(neterm_Operator)
                else:
                    epsilon()
                current_variable.id_struct = None
                del lex1, t1

            elif magazine.get_top() == neterm_Operator:
                magazine.pop()
                if t == TLBrace:
                    magazine.push(neterm_CompositeOperator)
                elif t == TSemicolon:
                    magazine.push(TSemicolon)
                elif t == TIf:
                    magazine.push(neterm_If)
                elif t == TIdent:
                    magazine.push(neterm_Assignment)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_CompositeOperator:
                magazine.pop()
                magazine.push(neterm_Block)
                current_variable.name = 'блок'
                v0 = tree.semantic_include(current_variable.name, 0)

            elif magazine.get_top() == neterm_Assignment:
                magazine.pop()
                magazine.push(TSemicolon)
                magazine.push(proc_assignement)
                magazine.push(neterm_PriorityLevel1)
                magazine.push(TAssigment)
                magazine.push(neterm_VariableOrElementOfStruct)
                operations.push(TAssigment)
            elif magazine.get_top() == proc_assignement:
                magazine.pop()
                triads.append(generate_triad(operations.pop(), operands.pop(), operands.pop()))

            elif magazine.get_top() == neterm_VariableOrElementOfStruct:
                magazine.pop()
                magazine.push(neterm_ElementOfStruct)
                magazine.push(TIdent)
                operands.push(Operand(lex))
            elif magazine.get_top() == neterm_ElementOfStruct:
                if t == TDotLink:
                    magazine.push(neterm_ElementOfStruct)
                    magazine.push(TIdent)
                    magazine.push(TDotLink)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_If:
                magazine.pop()
                magazine.push(neterm_Else)
                magazine.push(proc_goto)
                magazine.push(neterm_Operator)
                magazine.push(proc_if)
                magazine.push(TRBracket)
                magazine.push(neterm_PriorityLevel1)
                magazine.push(TLBracket)
                magazine.push(TIf)
            elif magazine.get_top() == neterm_Else:
                magazine.pop()
                if t == TElse:
                    magazine.push(proc_exit_from_if)
                    magazine.push(neterm_Operator)
                    magazine.push(TElse)
                else:
                    epsilon()
                    magazine.push(proc_exit_from_if)
            elif magazine.get_top() == proc_if:
                magazine.pop()
                address_if = len(triads)
                stack_for_ifs.push(address_if)
                del address_if
                triads.append(generate_triad(TIf,
                                             operand1=Operand(len(triads) + 1, is_address=True),
                                             operand2=Operand('_')))
            elif magazine.get_top() == proc_goto:
                magazine.pop()
                triads[stack_for_ifs.pop()][2] = Operand(len(triads) + 1, is_address=True)
                address_goto = len(triads)
                stack_for_ifs.push(address_goto)
                del address_goto
                triads.append(generate_triad(TGoto, operand1=Operand('_')))
            elif magazine.get_top() == proc_exit_from_if:
                magazine.pop()
                triads[stack_for_ifs.pop()][1] = Operand(len(triads), is_address=True)
                triads.append(generate_triad(TNope))

            elif magazine.get_top() == proc_generate_triad_for_operation:
                magazine.pop()
                triads.append(generate_triad(operations.pop(), operands.pop(), operands.pop()))
                operands.push(Operand(len(triads) - 1, is_address=True))

            elif magazine.get_top() == neterm_PriorityLevel1:
                magazine.pop()
                magazine.push(neterm_PL1)
                magazine.push(neterm_PriorityLevel2)
            elif magazine.get_top() == neterm_PL1:
                if t == TMore:
                    magazine.push(neterm_PL1)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel2)
                    magazine.push(TMore)
                    operations.push(TMore)
                elif t == TLess:
                    magazine.push(neterm_PL1)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel2)
                    magazine.push(TLess)
                    operations.push(TLess)
                elif t == TMoreEqual:
                    magazine.push(neterm_PL1)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel2)
                    magazine.push(TMoreEqual)
                    operations.push(TMoreEqual)
                elif t == TLessEqual:
                    magazine.push(neterm_PL1)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel2)
                    magazine.push(TLessEqual)
                    operations.push(TLessEqual)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_PriorityLevel2:
                magazine.pop()
                magazine.push(neterm_PL2)
                magazine.push(neterm_PriorityLevel3)
            elif magazine.get_top() == neterm_PL2:
                if t == TRShift:
                    magazine.push(neterm_PL2)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel3)
                    magazine.push(TRShift)
                    operations.push(TRShift)
                elif t == TLShift:
                    magazine.push(neterm_PL2)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriorityLevel3)
                    magazine.push(TLShift)
                    operations.push(TLShift)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_PriorityLevel3:
                magazine.pop()
                magazine.push(neterm_PL3)
                magazine.push(neterm_PriotityLevel4)
            elif magazine.get_top() == neterm_PL3:
                if t == TPlus:
                    magazine.push(neterm_PL3)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriotityLevel4)
                    magazine.push(TPlus)
                    operations.push(TPlus)
                elif t == TMinus:
                    magazine.push(neterm_PL3)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_PriotityLevel4)
                    magazine.push(TMinus)
                    operations.push(TMinus)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_PriotityLevel4:
                magazine.pop()
                magazine.push(neterm_PL4)
                magazine.push(neterm_ElementaryExpression)
            elif magazine.get_top() == neterm_PL4:
                if t == TMul:
                    magazine.push(neterm_PL4)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_ElementaryExpression)
                    magazine.push(TMul)
                    operations.push(TMul)
                elif t == TMod:
                    magazine.push(neterm_PL4)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_ElementaryExpression)
                    magazine.push(TMod)
                    operations.push(TMod)
                elif t == TDiv:
                    magazine.push(neterm_PL4)
                    magazine.push(proc_generate_triad_for_operation)
                    magazine.push(neterm_ElementaryExpression)
                    magazine.push(TDiv)
                    operations.push(TDiv)
                else:
                    epsilon()

            elif magazine.get_top() == neterm_ElementaryExpression:
                magazine.pop()
                if t == TIdent:
                    magazine.push(neterm_VariableOrElementOfStruct)
                elif t == TLBracket:
                    magazine.push(TRBracket)
                    magazine.push(neterm_PriorityLevel1)
                    magazine.push(TLBracket)
                else:
                    magazine.push(neterm_Const)

            elif magazine.get_top() == neterm_Const:
                magazine.pop()
                if (t == TConstInt10) | (t == TConstDoubleExp):
                    magazine.push(t)
                    if t == TConstInt10:
                        operands.push(Operand(int(lex)))
                    else:
                        operands.push(Operand(float(lex)))
            else:
                sc.print_error("Неверный символ", lex)

    # tree.print()
    print_triads(triads)
    return 0


def print_triads(triads):
    znak = ''
    i = 0
    for triad in triads:
        if triad[0] == TAssigment:
            znak = '='
        elif triad[0] == TPlus:
            znak = '+'
        elif triad[0] == TMinus:
            znak = '-'
        elif triad[0] == TDiv:
            znak = '/'
        elif triad[0] == TMod:
            znak = '%'
        elif triad[0] == TMul:
            znak = '*'
        elif triad[0] == TRShift:
            znak = '>>'
        elif triad[0] == TLShift:
            znak = '<<'
        elif triad[0] == TMore:
            znak = '>'
        elif triad[0] == TLess:
            znak = '<'
        elif triad[0] == TMoreEqual:
            znak = '>='
        elif triad[0] == TLessEqual:
            znak = '<='
        elif triad[0] == TMain:
            znak = 'proc'
        elif triad[0] == TEnd:
            znak = 'endproc'
        elif triad[0] == TIf:
            znak = 'if'
        elif triad[0] == TGoto:
            znak = 'goto'
        elif triad[0] == TNope:
            znak = 'nope'
        if triad[1] is None:
            print(str(i) + ')', znak)
        elif triad[2] is None:
            print(str(i) + ')', znak, triad[1].value)
        else:
            print(str(i) + ')', znak, triad[1].value, triad[2].value)
        i += 1


def generate_triad(operation, operand2=None, operand1=None):
    return [operation, operand1, operand2]


def __main__():
    sc = TScanner('test.txt')
    ll1(sc)
    print('Синтаксических ошибок не обнаружено!')


if __name__ == '__main__':
    __main__()
