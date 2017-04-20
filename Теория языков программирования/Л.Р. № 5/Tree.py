from constants_for_scanner import *

EMPTY = -1
DATA_TYPE = ['TYPE_UNKNOWN', 'TYPE_SHORT_INT',
             'TYPE_DOUBLE', 'TYPE_MAIN', 'TYPE_STRUCT']

scanner = None


def set_scanner(sc):
    global scanner
    scanner = sc


def copy_branch(tree, parent):
    right = None
    left = None
    if tree is None:
        return None
    if tree.left is not None:
        left = copy_branch(tree.left, tree)
    if tree.right is not None:
        right = copy_branch(tree.right, tree)
    new_data = DataInNode(tree.data.id, tree.data.type)
    new_data.value = tree.data.value
    new_data.id_struct = tree.data.id_struct
    new_node = Node(parent=parent, right=right, left=left, data=new_data)
    return new_node


class DataInNode:
    def __init__(self, id, data_type, shift=False):
        self.id = id
        self.type = data_type
        self.id_struct = ''
        self.value = None
        self.shift = shift
        self.glob = True


main = False


class Node:
    current = None

    def __init__(self, parent=None, left=None, right=None, data=None):
        self.data = data
        if data is None:
            self.data = DataInNode('Корень', 0)
        self.parent = parent
        self.left = left
        self.right = right

    # ФУНКЦИИ ОБРАБОТКИ БИНАРНОГО ДЕРЕВА
    def set_value(self, value):
        if self.data.type == DATA_TYPE.index('TYPE_SHORT_INT'):
            value = int(value)
        elif self.data.type == DATA_TYPE.index('TYPE_DOUBLE'):
            value = float(value)
        self.data.value = value

    def get_value(self):
        return self.data.value

    def set_left(self, data_left: DataInNode):
        """
        Создает левого потомка.
        """
        left = Node(parent=self, data=data_left)
        self.left = left

    def set_right(self, data_right: DataInNode):
        """
        Создаёт правого потомка.
        """
        right = Node(parent=self, data=data_right)
        self.right = right

    def find_up(self, id, from_node=None):
        """
        Ищет вершину по id на одном уровне вложенности, начиная
        либо с текущей, либо с вершины from_node.
        """
        if from_node is None:
            self.find_up(id, self)
        else:
            i = from_node
            while i is not None:
                if id == i.data.id:
                    break
                i = i.parent
            return i

    def find_down(self, id, from_node):
        """
        Ищет вершину по id на одном уровне вложенности, описанную после текущей,
        либо после заданной.
        """
        i = from_node
        while i is not None:
            if id == i.data.id:
                return i
            i = i.left
        return i

    def find_right_left(self, id, from_node=None):
        """
        Ищет вершину по id описанную на вложенном уровне, относительно текущей,
        либо заданной.
        :param id: Type of lexeme
        :param from_node: Node
        :return: Node
        """
        if from_node is None:
            self.find_right_left(id, self)
        else:
            i = from_node.right
            while i is not None:
                if id == self.data.id:
                    break
                i = i.left
            return i

    def print(self, shift=''):
        """
        Выводит дерево правым обходом в консоль.
        """
        print(shift, 'Вершина', self.data.id, '--->', DATA_TYPE[self.data.type])
        if self.left is not None:
            print(shift, '   слева', self.left.data.id)
        if self.right is not None:
            print(shift, '   справа', self.right.data.id)
        if self.right is not None:
            self.right.print(shift + '      ')
        if self.left is not None:
            self.left.print(shift)

    def find_up_one_level(self, id, from_node):
        """
        Ищет повторное описание вершины по id.
        :param id: Type of lexeme
        :param from_node: Node
        :return: Node or None
        """
        i = from_node
        while i is not None:
            if i.parent is None:
                break
            elif i.parent.right == i:
                break
            if id == i.data.id:
                return i
            i = i.parent
        return None

    # СЕМАНТИЧЕСКИЕ ПОДПРОГРАММЫ
    def set_current(self, node):
        self.current = node

    def get_current(self):
        return self.current

    def get_this_type(self):
        return self.data.type

    def get_data_type(self, type_id):
        if type_id == TShort:
            return DATA_TYPE.index('TYPE_SHORT_INT')
        elif type_id == TDouble:
            return DATA_TYPE.index('TYPE_DOUBLE')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def find_struct_declaration(self, id):
        v = self.find_up(id, self.current)
        return v

    def get_node_struct(self, id):
        v = self.find_down(id, self.right)
        # if v.data.type == DATA_TYPE.index('TYPE_STRUCT'):
        #    scanner.print_error('Нельзя присваивать типу данных.', self.data.id)
        if v is None:
            scanner.print_error('Такого идентификатора нет в указанной структуре', id)
        return v

    def get_shift(self, shift):
        if self.parent is None or self.data.type == DATA_TYPE.index('TYPE_MAIN'):
            return shift
        if self.data.type == DATA_TYPE.index('TYPE_SHORT_INT'):
            return self.parent.get_shift(shift + 4)

    def semantic_include(self, id, type_id, id_struct=None):
        if self.duplicate_control(id, self.current):
            scanner.print_error('Повторное описание идентификатора', id)
        b = DataInNode(id, type_id, shift=int(self.current.get_shift(0) + 4))
        if id == 'блок':
            global main
            main = True
            if self.current.data.type == DATA_TYPE.index('TYPE_MAIN'):
                self.current.set_right(b)
                self.current = self.current.right
            else:
                self.current.set_left(b)
                self.current = self.current.left
                self.current.set_right(b)
                v = self.current
                self.current = self.current.right
                return v
        elif id_struct is not None:
            b.id_struct = id_struct
            self.current.set_left(b)
            self.current = self.current.left
            struct = self.semantic_get_node(id_struct)
            self.current.right = copy_branch(struct.right, self.current.right)
        elif type_id == DATA_TYPE.index('TYPE_STRUCT'):
            self.current.set_left(b)
            self.current = self.current.left
            self.current.set_right(b)
            v = self.current
            self.current = self.current.right
            return v
        else:
            # type_id = self.get_data_type(type_id)
            if main:
                b.glob = False
            self.current.set_left(b)
            self.current = self.current.left
        return self.current

    def semantic_set_type(self, node, new_type):
        node.data.type = new_type

    def semantic_get_node(self, id):
        v = self.find_up(id, self.current)
        if v is None:
            scanner.print_error('Отсутствует описание идентификатора', id)
        return v

    def duplicate_control(self, id, node):
        if self.find_up_one_level(id, node) is None:
            return 0
        return 1

    def check_data_types(self, type1, type2=None):
        if self.data.id_struct != '':
            scanner.print_error('Нельзя присваивать значение типу данных.', self.data.id)
        if type2 is None:
            if (self.data.type == DATA_TYPE.index('TYPE_DOUBLE')) & \
                    ((type1 == DATA_TYPE.index('TYPE_DOUBLE')) | (type1 == DATA_TYPE.index('TYPE_SHORT_INT'))):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif (self.data.type == DATA_TYPE.index('TYPE_SHORT_INT')) & \
                    ((type1 == DATA_TYPE.index('TYPE_SHORT_INT')) | (type1 == DATA_TYPE.index('TYPE_DOUBLE'))):
                return DATA_TYPE.index('TYPE_SHORT_INT')
        else:
            if (type2 == DATA_TYPE.index('TYPE_DOUBLE')) and \
                    (type1 == DATA_TYPE.index('TYPE_DOUBLE') or type1 == DATA_TYPE.index('TYPE_SHORT_INT')):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif type2 == DATA_TYPE.index('TYPE_SHORT_INT'):
                if type1 == DATA_TYPE.index('TYPE_SHORT_INT'):
                    return DATA_TYPE.index('TYPE_SHORT_INT')
                elif type1 == DATA_TYPE.index('TYPE_DOUBLE'):
                    return DATA_TYPE.index('TYPE_DOUBLE')
        scanner.print_error('Приведение типов невозможно', '')
        return DATA_TYPE.index('TYPE_UNKNOWN')

    def check_bool(self, type1):
        if type1 == DATA_TYPE.index('TYPE_SHORT_INT') or type1 == DATA_TYPE.index('TYPE_DOUBLE'):
            return True
        scanner.print_error('Приведение типа к bool невозможно', '')

    def get_size_int(self, size):
        right = 0
        left = 0
        cur_size = 0
        if self.data.type == DATA_TYPE.index('TYPE_SHORT_INT'):
            cur_size = 4
        if self.right is not None:
            right = self.right.get_size_int(size)
        if self.left is not None:
            left = self.left.get_size_int(size)
        return right + left + cur_size