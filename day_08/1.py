from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        code = []

        for line in f.readlines():
            data = line.strip('\n')
            instr, signed_number = data.split(' ')
            signed_number = int(signed_number)
            code.append((instr, signed_number))

        return code


def solve_1():
    code = get_input_from_file()

    accumulator = 0
    i = 0
    already_executed_sequence = []

    while i < len(code):
        if i in already_executed_sequence:
            return accumulator

        already_executed_sequence.append(i)

        instr, number = code[i]
        if instr == 'jmp':
            i += number
            continue

        if instr == 'acc':
            accumulator += number

        i += 1
    return accumulator


def solve_2():
    code = get_input_from_file()

    for j in range(len(code)):
        accumulator = 0
        i = 0
        already_executed_sequence = []
        while i < len(code):
            if i in already_executed_sequence:
                i = len(code) + 1000
                continue

            already_executed_sequence.append(i)

            instr, number = code[i]
            if instr == 'jmp' and i != j:
                i += number
                continue

            if instr == 'acc':
                accumulator += number

            if instr == 'nop' and i == j:
                i += number
                continue

            i += 1

        if i == len(code):
            return accumulator


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
