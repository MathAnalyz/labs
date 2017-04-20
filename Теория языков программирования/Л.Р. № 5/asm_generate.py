from LL1 import *

registers = []
stack_registers = Stack()


class Register:
    def __init__(self, n: str, value: int):
        self.name = n
        self.value = value
        self.busy = False


def init_registers():
    global registers
    registers.append(Register('eax', 0))
    registers.append(Register('ebx', 0))
    registers.append(Register('ecx', 0))
    registers.append(Register('edx', 0))


def get_register(prev=False):
    r = False
    if not prev:
        for register in registers:
            if not register.busy:
                r = register
                break
        if r:
            r.busy = True
        else:
            r = registers.pop(0)
            print('push ' + r.name)
            stack_registers.push(r.name)
            r.busy = True
            registers.append(r)
    else:
        for i in range(len(registers)):
            if registers[i].name == prev:
                r = registers[i-1]
    return r


def pop_register(top=False):
    if len(stack_registers):
        name = stack_registers.pop()
        prev = 0
        if registers[0].name == name:
            prev = len(registers) - 1
        else:
            for i in range(len(registers)):
                if registers[i].name == name:
                    if top:
                        prev = i
                    else:
                        prev = i - 1
                    break
        return prev
    return -1


def generate_asm_code(triads: List, tree: Node):
    init_registers()
    main = False
    reg1 = 0
    reg2 = 0
    for triad in triads:
        if triad.value[0] == TDiv:
            if main:
                m = tree.find_down('блок', tree)
                v1 = tree.find_down(triad.value[1].value, tree) \
                    if tree.find_down(triad.value[1].value, m.right) is None \
                    else tree.find_down(triad.value[1].value,
                                        m.right)
                v2 = tree.find_down(triad.value[2].value, tree) \
                    if tree.find_down(triad.value[2].value, m.right) is None \
                    else tree.find_down(triad.value[2].value,
                                        m.right)
                if triad.value[1].is_address:
                    if not triad.value[2].is_address:
                        if v2 is None:
                            print('div ' + reg1.name + ',', triad.value[2].value)
                        else:
                            if v2.data.glob:
                                print('div ' + reg1.name + ',', '[' + v2.data.id + ']')
                            else:
                                print('div ' + reg1.name + ',', '[ebp-' + str(v2.data.shift) + ']')
                    else:
                        pos = pop_register()
                        if pos > -1:
                            reg2 = registers[pos]
                            # stack_registers.push(reg2.name)
                            print('div ' + reg2.name + ',', reg1.name)
                            print('pop ' + reg1.name)
                            reg1 = reg2
                        else:
                            reg2 = get_register(reg1.name)
                            print('div ' + reg2.name + ',', reg1.name)
                            reg1.busy = False
                            reg1 = reg2
                else:
                    if not triad.value[2].is_address:
                        reg1 = get_register()
                        if v1 is None:
                            print('mov ' + reg1.name + ',', triad.value[1].value)
                        else:
                            if v1.data.glob:
                                print('div ' + reg1.name + ',', '[' + v1.data.id + ']')
                            else:
                                print('mov ' + reg1.name + ',', '[ebp-' + str(v1.data.shift) + ']')
                        if v2 is None:
                            print('div ' + reg1.name + ',', triad.value[2].value)
                        else:
                            if v2.data.glob:
                                print('div ' + reg1.name + ',', '[' + v2.data.id + ']')
                            else:
                                print('div ' + reg1.name + ',', '[ebp-' + str(v2.data.shift) + ']')
                    else:
                        reg2 = get_register()
                        if v1 is None:
                            print('mov ' + reg2.name + ',', triad.value[1].value)
                        else:
                            if v1.data.glob:
                                print('div ' + reg1.name + ',', '[' + v1.data.id + ']')
                            else:
                                print('mov ' + reg1.name + ',', '[ebp-' + str(v1.data.shift) + ']')
                        print('div ' + reg1.name + ',', reg2.name)
                        reg2.busy = False
            else:
                if triad.value[1].is_address:
                    if not triad.value[2].is_address:
                        if isinstance(triad.value[2].value, int):
                            print('div ' + reg1.name + ',', triad.value[2].value)
                        else:
                            print('div ' + reg1.name + ',', '[' + triad.value[2].value + ']')
                    else:
                        pos = pop_register()
                        if pos > -1:
                            reg2 = registers[pos]
                            # stack_registers.push(reg2.name)
                            print('div ' + reg2.name + ',', reg1.name)
                            print('pop ' + reg1.name)
                            reg1 = reg2
                        else:
                            reg2 = get_register(reg1.name)
                            print('div ' + reg2.name + ',', reg1.name)
                            reg1.busy = False
                            reg1 = reg2
                else:
                    if not triad.value[2].is_address:
                        reg1 = get_register()
                        if isinstance(triad.value[1].value, int):
                            print('mov ' + reg1.name + ',', triad.value[1].value)
                        else:
                            print('mov ' + reg1.name + ',', '[' + triad.value[1].value + ']')
                        if isinstance(triad.value[2].value, int):
                            print('div ' + reg1.name + ',', triad.value[2].value)
                        else:
                            print('div ' + reg1.name + ',', '[' + triad.value[2].value + ']')
                    else:
                        reg2 = get_register()
                        if isinstance(triad.value[1].value, int):
                            print('mov ' + reg2.name + ',', triad.value[1].value)
                        else:
                            print('mov ' + reg2.name + ',', '[' + triad.value[1].value + ']')
                        print('div ' + reg1.name + ',', reg2.name)
                        reg2.busy = False
        elif triad.value[0] == TAssignment:
            if main:
                m = tree.find_down('блок', tree)
                v = tree.find_down(triad.value[1].value, m.right)
                if triad.value[2].is_address:
                    print('mov [ebp-' + str(v.data.shift) + '], eax')
                else:
                    print('mov [ebp-' + str(v.data.shift) + '],', triad.value[2].value)
            else:
                if triad.value[2].is_address:
                    print('mov [' + str(triad.value[1].value) + '], eax')
                else:
                    print('mov [' + str(triad.value[1].value) + '],', triad.value[2].value)
        elif triad.value[0] == TMain:
            print('?my_main PROC')
            print('push ebp')
            print('mov ebp, esp')
            print('sub esp,', tree.get_size_int(0))
            print('push ebx')
            print('push esi')
            print('push edi')
            main = True
        elif triad.value[0] == TEnd:
            print('pop edi')
            print('pop esi')
            print('pop ebx')
            print('mov esp, ebp')
            print('pop ebp')
            print('ret 0')
            print('?my_main ENDP')


def __main__():
    sc = TScanner('test.txt')
    triads, tree = ll1(sc)
    # print_triads(triads)
    generate_asm_code(triads, tree)


if __name__ == '__main__':
    __main__()
