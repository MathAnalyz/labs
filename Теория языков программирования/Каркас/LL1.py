from Scanner import *
from deff import *

m = []
z = 0


def epsilon():
    m.pop()


def ll1(sc: TScanner):
    global m
    fl = 1
    m.append(TEnd)
    m.append(neterm_Program)
    lex, t = sc.scan()
    while fl == 1:
        if m[len(m) - 1] < MinTypeTerminal:
            if m[len(m) - 1] == t:
                if t == TEnd:
                    fl = 0
                else:
                    lex, t = sc.scan()
                    m.pop()
            else:
                sc.print_error("Ожидался символ", lex)
        else:
            if m[len(m) - 1] == neterm_Program:
                m.pop()
                if t == TEnd:
                    epsilon()
                    break
                else:
                    m.append(neterm_Program)
                    m.append(neterm_Description)

            elif m[len(m) - 1] == neterm_Description:
                m.pop()
                if t == TStruct:
                    m.append(neterm_Struct)
                elif t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    lex2, t2 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        if t2 == TMain:
                            m.append(neterm_Function)
                        else:
                            m.append(TSemicolon)
                            m.append(neterm_ListOfVariables)
                            m.append(neterm_Type)
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                else:
                    m.append(TSemicolon)
                    m.append(neterm_ListOfVariables)
                    m.append(neterm_Type)
            elif m[len(m) - 1] == neterm_Type:
                m.pop()
                if t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        m.append(TInt)
                        m.append(TShort)
                elif t == TDouble:
                    m.append(TDouble)
                elif t == TIdent:
                    m.append(TIdent)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Function:
                m.pop()
                m.append(neterm_Block)
                m.append(TRBracket)
                m.append(TLBracket)
                m.append(TMain)
                m.append(TInt)
                m.append(TShort)

            elif m[len(m) - 1] == neterm_ListOfVariables:
                m.pop()
                m.append(neterm_AdditionallyList)
                m.append(neterm_Variable)

            elif m[len(m) - 1] == neterm_AdditionallyList:
                if t == TComma:
                    m.append(neterm_AdditionallyList)
                    m.append(neterm_Variable)
                    m.append(TComma)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Struct:
                m.pop()
                m.append(TSemicolon)
                m.append(TRBrace)
                m.append(neterm_DescriptionsStruct)
                m.append(TLBrace)
                m.append(TIdent)
                m.append(TStruct)

            elif m[len(m) - 1] == neterm_DescriptionsStruct:
                if t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        m.append(neterm_DescriptionsStruct)
                        m.append(TSemicolon)
                        m.append(neterm_ListOfVariables)
                        m.append(neterm_Type)
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                elif (t == TDouble) | (t == TIdent):
                    m.append(neterm_DescriptionsStruct)
                    m.append(TSemicolon)
                    m.append(neterm_ListOfVariables)
                    m.append(neterm_Type)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Variable:
                m.pop()
                m.append(neterm_Initialization)
                m.append(TIdent)

            elif m[len(m) - 1] == neterm_Initialization:
                if t == TAssigment:
                    m.append(neterm_V)
                    m.append(TAssigment)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Block:
                m.pop()
                m.append(TRBrace)
                m.append(neterm_Content)
                m.append(TLBrace)
            elif m[len(m) - 1] == neterm_DescriptionsInBlock:
                m.pop()
                if t == TStruct:
                    m.append(neterm_Struct)
                elif t == TShort:
                    uk1 = sc.get_uk()
                    lex1, t1 = sc.scan()
                    lex2, t2 = sc.scan()
                    sc.put_uk(uk1)
                    if t1 == TInt:
                        m.append(TSemicolon)
                        m.append(neterm_ListOfVariables)
                        m.append(neterm_Type)
                    else:
                        sc.print_error("Ошибка, ожидался", "int")
                else:
                    m.append(TSemicolon)
                    m.append(neterm_ListOfVariables)
                    m.append(neterm_Type)
            elif m[len(m) - 1] == neterm_Content:
                uk = sc.get_uk()
                lex1, t1 = sc.scan()
                sc.put_uk(uk)
                if ((t1 == TIdent) | (t == TShort)) & (t != TLBrace):
                    m.append(neterm_Content)
                    m.append(neterm_DescriptionsInBlock)
                elif (t == TLBrace) | (t1 != TIdent) & (t != TRBrace):
                    m.append(neterm_Content)
                    m.append(neterm_Operator)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Operator:
                m.pop()
                if t == TLBrace:
                    m.append(neterm_CompositeOperator)
                elif t == TSemicolon:
                    m.append(TSemicolon)
                elif t == TIf:
                    m.append(neterm_If)
                elif t == TIdent:
                    m.append(neterm_Assignment)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_CompositeOperator:
                m.pop()
                m.append(neterm_Block)

            elif m[len(m) - 1] == neterm_Assignment:
                m.pop()
                m.append(TSemicolon)
                m.append(neterm_V)
                m.append(TAssigment)
                m.append(neterm_VarOrElStruct)

            elif m[len(m) - 1] == neterm_VarOrElStruct:
                m.pop()
                m.append(neterm_ElementOfStruct)
                m.append(TIdent)

            elif m[len(m) - 1] == neterm_ElementOfStruct:
                if t == TDotLink:
                    m.append(neterm_ElementOfStruct)
                    m.append(TIdent)
                    m.append(TDotLink)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_If:
                m.pop()
                m.append(neterm_Else)
                m.append(neterm_Operator)
                m.append(TRBracket)
                m.append(neterm_V)
                m.append(TLBracket)
                m.append(TIf)

            elif m[len(m) - 1] == neterm_Else:
                m.pop()
                if t == TElse:
                    m.append(neterm_Operator)
                    m.append(TElse)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_V:
                m.pop()
                m.append(neterm_V1)
                m.append(neterm_W)

            elif m[len(m) - 1] == neterm_V1:
                if t == TMore:
                    m.append(neterm_V1)
                    m.append(neterm_W)
                    m.append(TMore)
                elif t == TLess:
                    m.append(neterm_V1)
                    m.append(neterm_W)
                    m.append(TLess)
                elif t == TMoreEqual:
                    m.append(neterm_V1)
                    m.append(neterm_W)
                    m.append(TMoreEqual)
                elif t == TLessEqual:
                    m.append(neterm_V1)
                    m.append(neterm_W)
                    m.append(TLessEqual)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_W:
                m.pop()
                m.append(neterm_W1)
                m.append(neterm_X)

            elif m[len(m) - 1] == neterm_W1:
                if t == TRShift:
                    m.append(neterm_W1)
                    m.append(neterm_X)
                    m.append(TRShift)
                elif t == TLShift:
                    m.append(neterm_W1)
                    m.append(neterm_X)
                    m.append(TLShift)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_X:
                m.pop()
                m.append(neterm_X1)
                m.append(neterm_Y)

            elif m[len(m) - 1] == neterm_X1:
                if t == TPlus:
                    m.append(neterm_X1)
                    m.append(neterm_Y)
                    m.append(TPlus)
                elif t == TMinus:
                    m.append(neterm_X1)
                    m.append(neterm_Y)
                    m.append(TMinus)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Y:
                m.pop()
                m.append(neterm_Y1)
                m.append(neterm_Z)

            elif m[len(m) - 1] == neterm_Y1:
                if t == TMul:
                    m.append(neterm_Y1)
                    m.append(neterm_Z)
                    m.append(TMul)
                elif t == TMod:
                    m.append(neterm_Y1)
                    m.append(neterm_Z)
                    m.append(TMod)
                elif t == TDiv:
                    m.append(neterm_Y1)
                    m.append(neterm_Z)
                    m.append(TDiv)
                else:
                    epsilon()

            elif m[len(m) - 1] == neterm_Z:
                m.pop()
                if t == TIdent:
                    m.append(neterm_VarOrElStruct)
                elif t == TLBracket:
                    m.append(TRBracket)
                    m.append(neterm_V)
                    m.append(TLBracket)
                else:
                    m.append(neterm_Const)
            elif m[len(m) - 1] == neterm_Const:
                m.pop()
                if (t == TConstInt10) | (t == TConstDoubleExp):
                    m.append(t)
                else:
                    sc.print_error("Неверный символ", lex)
    return 0


def __main__():
    sc = TScanner('input.txt')
    ll1(sc)
    print('Синтаксических ошибок не обнаружено!')


__main__()

'''elif m[z] == neterm_Type:
                if t == TInt:
                    m[z] = TInt
                    z += 1
                elif t == TDouble:
                    m[z] = TDouble
                    z += 1
                elif t == TIdent:
                    m[z] = TIdent
                    z += 1
                else:
                    epsilon()
                
            elif m[z] == neterm_ListOfVariables:
                m[z] = neterm_ListOfVariables2
                z += 1
                m[z] = neterm_Variable
                z += 1
                
            elif m[z] == neterm_ListOfVariables2:
                if t == TComma:
                    m[z] = neterm_AListOfVariablesInTheStructure2
                    z += 1
                    m[z] = neterm_Variable
                    z += 1
                    m[z] = TComma
                    z += 1
                else:
                    epsilon()
                
            elif m[z] == neterm_Variable:
                m[z] = neterm_Initialization
                z += 1
                m[z] = TIdent
                z += 1
                
            elif m[z] == neterm_Initialization:
                if t == TAssigment:
                    m[z] = neterm_Expression
                    z += 1
                    m[z] = TAssigment
                    z += 1
                else:
                    epsilon()
                
            elif m[z] == neterm_Block:
                if t == TLBracket:
                    m[z] = TRBracket
                    z += 1
                    m[z] = neterm_OperatorSAndDescriptions
                    z += 1
                    m[z] = TLBracket
                    z += 1
                else:
                    sc.print_error("Ожидался символ", lex)
                
            elif m[z] == neterm_OperatorSAndDescriptions:
                if (t == TInt) | (t == TDouble):
                    m[z] = neterm_OperatorSAndDescriptions
                    z += 1
                    m[z] = neterm_Data
                    z += 1
                elif (t == TLBracket) | (t == TSemicolon) | (t == TIf):
                    m[z] = neterm_OperatorSAndDescriptions
                    z += 1
                    m[z] = neterm_Operator
                    z += 1
                elif t == TIdent:
                    m[z] = neterm_OperatorSAndDescriptions
                    z += 1
                    uk1 = sc.get_uk()
                    lex1, ttt = sc.scaner()
                    sc.put_uk(uk1)
                    if ttt == TIdent:
                        m[z] = neterm_Data
                        z += 1
                    else:
                        m[z] = neterm_Operator
                        z += 1
                else:
                    epsilon()
                
            elif m[z] == neterm_Operator:
                if t == TIdent:
                    m[z] = TSemicolon
                    z += 1
                    m[z] = neterm_Assignment
                    z += 1
                elif t == TIf:
                    m[z] = neterm_While
                    z += 1
                elif t == TLBracket:
                    m[z] = neterm_Block
                    z += 1
                elif t == TSemicolon:
                    m[z] = TSemicolon
                    z += 1
                else:
                    sc.print_error("Неверный символ", lex)
                
            elif m[z] == neterm_Assignment:
                m[z] = neterm_Expression
                z += 1
                m[z] = TAssigment
                z += 1
                m[z] = neterm_Name
                z += 1
                
            elif m[z] == neterm_Name:
                m[z] = neterm_Name1
                z += 1
                m[z] = TIdent
                z += 1
                
            elif m[z] == neterm_Name1:
                if t == TDotLink:
                    m[z] = neterm_Name1
                    z += 1
                    m[z] = TIdent
                    z += 1
                    m[z] = TDotLink
                    z += 1
                else:
                    epsilon()
                
            elif m[z] == neterm_While:
                m[z] = neterm_Operator
                z += 1
                m[z] = TRBracket
                z += 1
                m[z] = neterm_Expression
                z += 1
                m[z] = TLBracket
                z += 1
                m[z] = TIf
                z += 1
                
            elif m[z] == neterm_Expression:
                m[z] = neterm_Expression1
                z += 1
                m[z] = neterm_V
                z += 1
                
            '''
#
