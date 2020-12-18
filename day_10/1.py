from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        joltages = []

        for line in f.readlines():
            data = line.strip('\n')
            joltages.append(int(data))

        return joltages


def solve_1():
    joltages = get_input_from_file()
    joltages.sort()

    count_one_joltages = 0
    count_three_joltages = 0
    last_joltage = 0

    for joltage in joltages:
        if joltage - last_joltage == 1:
            count_one_joltages += 1
        elif joltage - last_joltage == 3:
            count_three_joltages += 1

        last_joltage = joltage

    count_three_joltages += 1  # Device is 3 higher

    return count_one_joltages * count_three_joltages


def solve_2():
    joltages = get_input_from_file()
    joltages.sort()

    count_solution_by_joltage = defaultdict(int, {0: 1})

    for joltage in joltages:
        count_solution_by_joltage[joltage] = count_solution_by_joltage[joltage - 1] + count_solution_by_joltage[joltage - 2] + count_solution_by_joltage[joltage - 3]

    return count_solution_by_joltage[joltages[-1]]


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
