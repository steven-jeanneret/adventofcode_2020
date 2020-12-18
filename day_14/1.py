from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        return [b.strip('\n').split(' = ') for b in f.readlines()]


def to_binary(number):
    list_number = list(str(bin(int(number)))[2:])
    while len(list_number) < 36:
        list_number.insert(0, 0)

    return list_number


def to_decimal(number):
    return int(number, 2)


def apply_mask_to_decimal(mask, value):
    value_bin = to_binary(value)
    new_value = []

    for i in range(len(mask)):
        if mask[i] == 'X':
            new_value.append(value_bin[i])
        else:
            new_value.append(mask[i])

    new_value = "".join([str(v) for v in new_value])
    return to_decimal(new_value)


def apply_mask_to_decimal_2(mask, value):
    value_bin = to_binary(value)
    new_values = [[]]

    for i in range(len(mask)):
        for j in range(len(new_values)):
            new_value = new_values[j]
            if mask[i] == 'X':
                n = deepcopy(new_value)
                n.append('0')
                new_values.append(n)

                new_value.append('1')
            elif mask[i] == '0':
                new_value.append(value_bin[i])
            else:
                new_value.append(mask[i])

    return [to_decimal("".join([str(v) for v in addr])) for addr in new_values]


def solve_1():
    instructions = get_input_from_file()
    current_mask = None
    memory = defaultdict(int)

    for instr, value in instructions:
        if instr == 'mask':
            current_mask = value
        else:
            addr = instr.strip('mem[').strip(']')
            memory[addr] = apply_mask_to_decimal(current_mask, value)

    return sum(memory.values())


def solve_2():
    instructions = get_input_from_file()
    current_mask = None
    memory = defaultdict(int)

    for instr, value in instructions:
        if instr == 'mask':
            current_mask = value
        else:
            addr = instr.strip('mem[').strip(']')
            addresses = apply_mask_to_decimal_2(current_mask, addr)
            for addr in addresses:
                memory[addr] = int(value)

    return sum(memory.values())


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())



