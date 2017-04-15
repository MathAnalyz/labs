class Operand:
    def __init__(self, value, is_address=False):
        self.value = value if not is_address else value
        self.is_address = is_address

    def __ne__(self, operand2):
        if self.value != operand2.value or self.is_address != operand2.is_address:
            return True
        return False


class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self, position=None):
        self.top -= 1
        if position is None:
            return self.stack.pop()
        else:
            return self.stack.pop(position)

    def get_top(self, top=None):
        if top is None:
            return self.stack[self.top - 1]
        return self.stack[top]

    def __len__(self):
        return self.top


