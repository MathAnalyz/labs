class Item:
    def __init__(self, value, number):
        self.value = value
        self.number = number
        self.is_optimised = False

    def __eq__(self, other):
        if self.value == other.value and self.number == other.number and self.is_optimised == other.is_optimised:
            return True
        return False

class List:
    def __init__(self):
        self.list = []
        self.len = 0

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        v = self.list[item]
        return v

    def __setitem__(self, key, value):
        v = self.list[key]
        v.value = value

    def append(self, value: list):
        self.list.append(Item(value, self.len))
        self.len += 1

    def insert(self, position: int, value: list, number=None):
        if number is None:
            max = 0
            for item in self.list:
                max = item.number if item.number > max else max
            self.list.insert(position, Item(value, max))
            self.len += 1
        else:
            self.list.insert(position, Item(value, number))
            self.len += 1

    def pop(self, position: int):
        self.len -= 1
        return self.list.pop(position)

    def get_item(self, number):
        ret = 0
        for item in self.list:
            if item.number == number:
                ret = item
                break
        return ret

    def index(self, item):
        ret = 0
        for i in range(len(self.list)):
            if self.list[i] == item:
                ret = i
                break
        return ret
