from constants_for_scanner import *

EMPTY = -1
DATA_TYPE = ['TYPE_UNKNOWN', 'TYPE_SHORT_INT',
             'TYPE_DOUBLE', 'TYPE_MAIN', 'TYPE_STRUCT']

scanner = None


def set_scanner(sc):
    global scanner
    scanner = sc


class DataInNode:
    def __init__(self, id, data_type):
        self.id = id
        self.data_type = data_type
        self.id_struct = ''


class Node:
    current = None

    def __init__(self, parent=None, left=None, right=None, data=None):
        self.data_in_node = data
        if data is None:
            self.data_in_node = DataInNode('Корень', 0)
        self.parent = parent
        self.left = left
        self.right = right

    # ФУНКЦИИ ОБРАБОТКИ БИНАРНОГО ДЕРЕВА
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
                if id == i.data_in_node.id:
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
            if id == i.data_in_node.id:
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
                if id == self.data_in_node.id:
                    break
                i = i.left
            return i

    def print(self, shift=''):
        """
        Выводит дерево правым обходом в консоль.
        """
        print(shift, 'Вершина', self.data_in_node.id, '--->', DATA_TYPE[self.data_in_node.data_type])
        if self.left is not None:
            print(shift, '   слева', self.left.data_in_node.id)
        if self.right is not None:
            print(shift, '   справа', self.right.data_in_node.id)
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
            if id == i.data_in_node.id:
                return i
            i = i.parent
        return None

    # СЕМАНТИЧЕСКИЕ ПОДПРОГРАММЫ
    def set_current(self, node):
        self.current = node

    def get_current(self):
        return self.current

    def get_this_type(self):
        return self.data_in_node.data_type

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
        # if v.data_in_node.data_type == DATA_TYPE.index('TYPE_STRUCT'):
        #    scanner.print_error('Нельзя присваивать типу данных.', self.data_in_node.id)
        if v is None:
            scanner.print_error('Такого идентификатора нет в указанной структуре', id)
        return v

    def semantic_include(self, id, type_id, id_struct=None):
        if self.duplicate_control(id, self.current):
            scanner.print_error('Повторное описание идентификатора', id)
        if id == 'блок':
            b = DataInNode(id, type_id)
            if self.current.data_in_node.data_type == DATA_TYPE.index('TYPE_MAIN'):
                self.current.set_right(b)
                self.current = self.current.right
            else:
                self.current.set_left(b)
                self.current = self.current.left
                self.current.set_right(b)
                v = self.current
                self.current = self.current.right
                return v
        elif type_id == DATA_TYPE.index('TYPE_STRUCT'):
            b = DataInNode(id, type_id)
            self.current.set_left(b)
            self.current = self.current.left
            self.current.set_right(b)
            v = self.current
            self.current = self.current.right
            return v
        elif id_struct is not None:
            b = DataInNode(id, DATA_TYPE.index('TYPE_UNKNOWN'))
            b.id_struct = id_struct
            self.current.set_left(b)
            self.current = self.current.left
            struct = self.semantic_get_node(id_struct)
            self.current.right = struct.right
        else:
            type_id = self.get_data_type(type_id)
            b = DataInNode(id, type_id)
            self.current.set_left(b)
            self.current = self.current.left
        return self.current

    def semantic_set_type(self, node, new_type):
        node.data_in_node.data_type = new_type

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
        if self.data_in_node.id_struct != '':
            scanner.print_error('Нельзя присваивать значение типу данных.', self.data_in_node.id)
        if type2 is None:
            if (self.data_in_node.data_type == DATA_TYPE.index('TYPE_DOUBLE')) & \
                    ((type1 == DATA_TYPE.index('TYPE_DOUBLE')) | (type1 == DATA_TYPE.index('TYPE_SHORT_INT'))):
                return DATA_TYPE.index('TYPE_DOUBLE')
            elif (self.data_in_node.data_type == DATA_TYPE.index('TYPE_SHORT_INT')) & \
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
