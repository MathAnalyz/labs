from Scaner import *

EMPTY = -1
DATA_TYPE = ['TYPE_UNKNOWN', 'TYPE_INTEGER', 'TYPE_SHORT_INT',
             'TYPE_DOUBLE', 'TYPE_STRUCT', 'TYPE_FUNCT', 'TYPE_STRUCT_ITEM']

scaner = None


class Node:
    def __init__(self, id, dataType):
        self.id = id
        self.dataType = dataType
        self.idStruct = ''


class Tree:
    def __init__(self):
        self.node = Node('----', -1)
        self.up = None
        self.left = None
        self.right = None
        self.current = None

    def init(self,  left, right, up, node):
        self.node = node
        self.up = up
        self.left = left
        self.right = right

    def setLeft(self, data):
        t = Tree()
        t.init(None, None, self, data)
        self.left = t

    def setRight(self, data):
        t = Tree()
        t.init(None, None, self, data)
        self.right = t

    def findUp(self, id, fromNode=None):
        if fromNode is None:
            return self.findUp(id, self)
        else:
            i = fromNode
            while i is not None:
                if id == i.node.id:
                    break
                i = i.up
            return i

    def findDown(self, id, fromNode):
        i = fromNode
        while i is not None:
            if id == i.node.id:
                return i
            i = i.left
        return i

    def findUpOneLevel(self, id, fromNode):
        i = fromNode
        while i is not None:
            if i.up is None:
                break
            elif i.up.right == i:
                break
            if id == i.node.id:
                return i
            i = i.up
        return None

    def findRightLeft(self, id, fromNode=None):
        if fromNode is None:
            return self.findRightLeft(id, self)
        else:
            i = fromNode.right
            while (i is not None):
                if id == self.node.id:
                    break
                i = i.left
            return i

    def print(self):
        print('Вершина с данными', self.node.id, '--->')
        if self.left is not None:
            print('     слева данные', self.left.node.id)
        if self.right is not None:
            print('     справа данные', self.right.node.id)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

    # Сематнические подпрограммы
    def setCur(self, tree):
        self.current = tree

    def setScaner(self, sc):
        global scaner
        scaner = sc

    def getCur(self):
        return self.current

    def semInclude(self, a, t, identStruct=None):
        if self.duplicateControl(a, self.current):
            scaner.print_error('Повторное описание идентификатора', a)
        if t == DATA_TYPE.index('TYPE_FUNCT'):
            b = Node(a, t)
            self.current.setLeft(b)
            self.current = self.current.left
            return self.current
        if t == EMPTY:
            b = Node('', -1)
            if self.current.node.dataType != DATA_TYPE.index('TYPE_FUNCT'):
                b.id = a
                b.dataType = t
                self.current.setLeft(b)
                self.current = self.current.left
            v = self.current
            b = Node('EMPTY', EMPTY)
            self.current.setRight(b)
            self.current = self.current.right
            return v
        elif t == DATA_TYPE.index('TYPE_STRUCT'):
            b = Node(a, t)
            self.current.setLeft(b)
            self.current = self.current.left
            v = self.current
            b = Node('EMPTYStruct', EMPTY)
            self.current.setRight(b)
            self.current = self.current.right
            return v
        elif t == DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            b = Node(a, t)
            b.idStruct = identStruct
            self.current.setLeft(b)
            self.current = self.current.left
            v = self.semCheckStructOnLevel(identStruct)
            self.current.right = v.right
            return self.current
        else:
            b = Node(a, t)
            self.current.setLeft(b)
            self.current = self.current.left
            return self.current

    def semSetType(self, address, t):
        address.node.dataType = t

    def semGetType(self, a):
        v = self.findUp(a, self.current)
        if v is None:
            scaner.print_error('Отсутствует описание идентификатора', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_FUNCT'):
            scaner.print_error('Неверное использование вызова функции', a)
        return v

    def semGetFunction(self, a):
        v = self.findUp(a, self.current)
        if v is None:
            scaner.print_error('Отсутствует описание функции', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_FUNCT'):
            scaner.print_error('Не является функцией идентификатор', a)
        return v

    def duplicateControl(self, a, address):
        if (a == 'EMPTY') | (a == 'EMPTYStruct'):
            return 0
        if self.findUpOneLevel(a, address) is None:
            return 0
        return 1

    def getDataType(self, a, t):
        if t == TInt:
            return DATA_TYPE.index('TYPE_INTEGER')
        elif t == TDouble:
            return DATA_TYPE.index('TYPE_DOUBLE')
        elif (t == TIdent) & (self.semCheckStructOnLevel(a) is not None):
            return DATA_TYPE.index('TYPE_STRUCT_ITEM')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def semCheckStructOnLevel(self, a):
        v = self.findUp(a, self.current)
        if v is None:
            scaner.print_error('Отсутствует описание структуры', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_FUNCT'):
            scaner.print_error('Неверное использование вызова функции', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_INTEGER'):
            scaner.print_error('Неверное использование int', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_DOUBLE'):
            scaner.print_error('Неверное использование double', a)
        elif v.node.dataType == DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            scaner.print_error('Неверное использование элемента структууры', a)
        return v

    def getUzelStruct(self, a):
        if self.node.dataType != DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            scaner.print_error('Идентификатор должен быть структурой', self.node.id)
        v = self.findDown(a, self.right)
        if v is None:
            scaner.print_error('Такого идентификатора нет в указанной структуре', a)
        return v

    def getThisType(self):
        return self.node.dataType

    def checkDataTypes(self, type1, type2=None):
        if type2 is None:
            if (self.node.dataType == DATA_TYPE.index('TYPE_STRUCT_ITEM')) & \
                    (type1 == DATA_TYPE.index('TYPE_STRUCT_ITEM')):
                return DATA_TYPE.index('TYPE_STRUCT_ITEM')
            elif (self.node.dataType == DATA_TYPE.index('TYPE_DOUBLE')) & \
                    ((type1 == DATA_TYPE.index('TYPE_DOUBLE')) | (type1 == DATA_TYPE.index('TYPE_INTEGER'))):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif (self.node.dataType == DATA_TYPE.index('TYPE_INTEGER')) & \
                    (type1 == DATA_TYPE.index('TYPE_INTEGER')):
                return DATA_TYPE.index('TYPE_INTEGER')
            elif (self.node.dataType == DATA_TYPE.index('TYPE_INTEGER')) & \
                    (type1 == DATA_TYPE.index('TYPE_DOUBLE')):
                return DATA_TYPE.index('TYPE_DOUBLE')
        else:
            if (type1 == DATA_TYPE.index('TYPE_STRUCT_ITEM')) & \
                    (type2 == DATA_TYPE.index('TYPE_STRUCT_ITEM')):
                return DATA_TYPE.index('TYPE_STRUCT_ITEM')
            elif (type1 == DATA_TYPE.index('TYPE_DOUBLE')) & \
                    ((type2 == DATA_TYPE.index('TYPE_DOUBLE')) | (type2 == DATA_TYPE.index('TYPE_INTEGER'))):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif (type1 == DATA_TYPE.index('TYPE_INTEGER')) & \
                    (type2 == DATA_TYPE.index('TYPE_INTEGER')):
                return DATA_TYPE.index('TYPE_INTEGER')
            elif (type1 == DATA_TYPE.index('TYPE_INTEGER')) & \
                    (type2 == DATA_TYPE.index('TYPE_DOUBLE')):
                return DATA_TYPE.index('TYPE_DOUBLE')
        scaner.print_error('Приведение типов невозможно', '')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def checkDataTypeToBool(self, t):
        if (t == DATA_TYPE.index('TYPE_DOUBLE')) | (t == DATA_TYPE.index('TYPE_INTEGER')):
            return t
        scaner.print_error('Приведение типа к bool невозможно', '')
