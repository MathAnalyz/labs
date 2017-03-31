from constants_for_scanner import *

EMPTY = -1
DATA_TYPE = ['TYPE_UNKNOWN', 'TYPE_INTEGER', 'TYPE_SHORT_INT',
             'TYPE_DOUBLE', 'TYPE_STRUCT', 'TYPE_FUNCT', 'TYPE_STRUCT_ITEM']

scanner = None


class DataValue:
    def __init__(self, value):
        self.value = value


class Node:
    def __init__(self, id, data_type):
        self.id = id
        self.data_type = data_type
        self.data_value = None
        self.id_struct = ''

    def set_value(self, value):
        self.data_value = DataValue(value)

    def get_value(self):
        return self.data_value.value


def set_scanner(sc):
    global scanner
    scanner = sc


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

    def set_left(self, data):
        t = Tree()
        t.init(None, None, self, data)
        self.left = t

    def set_right(self, data):
        t = Tree()
        t.init(None, None, self, data)
        self.right = t

    def find_up(self, id, from_node=None):
        if from_node is None:
            return self.find_up(id, self)
        else:
            i = from_node
            while i is not None:
                if id == i.node.id:
                    break
                i = i.up
            return i

    def find_down(self, id, from_node):
        i = from_node
        while i is not None:
            if id == i.node.id:
                return i
            i = i.left
        return i

    def find_up_one_level(self, id, from_node):
        i = from_node
        while i is not None:
            if i.up is None:
                break
            elif i.up.right == i:
                break
            if id == i.node.id:
                return i
            i = i.up
        return None

    def find_right_left(self, id, from_node=None):
        if from_node is None:
            return self.find_right_left(id, self)
        else:
            i = from_node.right
            while i is not None:
                if id == self.node.id:
                    break
                i = i.left
            return i

    def print(self):
        if self.node.data_value is not None:
            print('Вершина с данными', self.node.id, '--->', self.node.get_value())
        else:
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
    def set_cur(self, tree):
        self.current = tree

    def get_cur(self):
        return self.current

    def sem_include(self, a, t, id_struct=None):
        if self.duplicate_control(a, self.current):
            scanner.print_error('Повторное описание идентификатора', a)
        if t == DATA_TYPE.index('TYPE_FUNCT'):
            b = Node(a, t)
            self.current.set_left(b)
            self.current = self.current.left
            return self.current
        if t == EMPTY:
            b = Node('', -1)
            if self.current.node.data_type != DATA_TYPE.index('TYPE_FUNCT'):
                b.id = a
                b.data_type = t
                self.current.set_left(b)
                self.current = self.current.left
            v = self.current
            b = Node('EMPTY', EMPTY)
            self.current.set_right(b)
            self.current = self.current.right
            return v
        elif t == DATA_TYPE.index('TYPE_STRUCT'):
            b = Node(a, t)
            self.current.set_left(b)
            self.current = self.current.left
            v = self.current
            b = Node('EMPTYStruct', EMPTY)
            self.current.set_right(b)
            self.current = self.current.right
            return v
        elif t == DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            b = Node(a, t)
            b.id_structs = id_struct
            self.current.set_left(b)
            self.current = self.current.left
            v = self.sem_check_struct_on_level(id_struct)
            self.current.right = v.right
            return self.current
        else:
            b = Node(a, t)
            self.current.set_left(b)
            self.current = self.current.left
            return self.current

    def sem_get_type(self, a):
        v = self.find_up(a, self.current)
        if v is None:
            scanner.print_error('Отсутствует описание идентификатора', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_FUNCT'):
            scanner.print_error('Неверное использование вызова функции', a)
        return v

    def sem_get_function(self, a):
        v = self.find_up(a, self.current)
        if v is None:
            scanner.print_error('Отсутствует описание функции', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_FUNCT'):
            scanner.print_error('Не является функцией идентификатор', a)
        return v

    def duplicate_control(self, a, address):
        if (a == 'EMPTY') | (a == 'EMPTYStruct'):
            return 0
        if self.find_up_one_level(a, address) is None:
            return 0
        return 1

    def get_data_type(self, a, t):
        if t == TInt:
            return DATA_TYPE.index('TYPE_INTEGER')
        elif t == TDouble:
            return DATA_TYPE.index('TYPE_DOUBLE')
        elif t == TIdent and self.sem_check_struct_on_level(a) is not None:
            return DATA_TYPE.index('TYPE_STRUCT_ITEM')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def sem_check_struct_on_level(self, a):
        v = self.find_up(a, self.current)
        if v is None:
            scanner.print_error('Отсутствует описание структуры', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_FUNCT'):
            scanner.print_error('Неверное использование вызова функции', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_INTEGER'):
            scanner.print_error('Неверное использование int', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_DOUBLE'):
            scanner.print_error('Неверное использование double', a)
        elif v.node.data_type == DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            scanner.print_error('Неверное использование элемента структууры', a)
        return v

    def get_node_struct(self, a):
        if self.node.data_type != DATA_TYPE.index('TYPE_STRUCT_ITEM'):
            scanner.print_error('Идентификатор должен быть структурой', self.node.id)
        v = self.find_down(a, self.right)
        if v is None:
            scanner.print_error('Такого идентификатора нет в указанной структуре', a)
        return v

    def get_this_type(self):
        return self.node.data_type

    def check_data_types(self, type1, type2=None):
        if type2 is None:
            if (self.node.data_type == DATA_TYPE.index('TYPE_STRUCT_ITEM')) & \
                    (type1 == DATA_TYPE.index('TYPE_STRUCT_ITEM')):
                return DATA_TYPE.index('TYPE_STRUCT_ITEM')
            elif (self.node.data_type == DATA_TYPE.index('TYPE_DOUBLE')) & \
                    ((type1 == DATA_TYPE.index('TYPE_DOUBLE')) | (type1 == DATA_TYPE.index('TYPE_INTEGER'))):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif (self.node.data_type == DATA_TYPE.index('TYPE_INTEGER')) & \
                    ((type1 == DATA_TYPE.index('TYPE_INTEGER')) | (type1 == DATA_TYPE.index('TYPE_DOUBLE'))):
                return DATA_TYPE.index('TYPE_INTEGER')
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
        scanner.print_error('Приведение типов невозможно', '')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def check_data_type_to_bool(self, t):
        if (t == DATA_TYPE.index('TYPE_DOUBLE')) or (t == DATA_TYPE.index('TYPE_INTEGER')):
            return t
        scanner.print_error('Приведение типа к bool невозможно', '')
