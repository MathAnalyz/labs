class Operand:
    def __init__(self, value, is_address=False):
        self.value = value if not is_address else '('+str(value)+')'
        self.is_address = is_address


class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        self.top -= 1
        return self.stack.pop()

    def get_two_top_item(self):
        return self.pop(), self.pop()

    def get_top(self):
        return self.stack[self.top - 1]

    def __len__(self):
        return self.top


