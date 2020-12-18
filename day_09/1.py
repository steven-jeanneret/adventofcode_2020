from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        numbers = []

        for line in f.readlines():
            data = line.strip('\n')
            numbers.append(int(data))

        return numbers


def solve_1():
    numbers = get_input_from_file()

    for i in range(25, len(numbers)):
        valid = False
        current_number = numbers[i]

        for x in range(i-25, i):
            current_x = numbers[x]
            for y in range(i-25, i):
                current_y = numbers[y]

                if current_x == current_y:
                    continue

                if current_x + current_y == current_number:
                    valid = True

        if not valid:
            return current_number


def solve_2():
    numbers = get_input_from_file()
    number_to_sum = solve_1()

    for i in range(len(numbers)):
        j = i + 1
        total = numbers[i]
        numbers_summed = [numbers[i]]

        while j < len(numbers) and total < number_to_sum:
            total += numbers[j]
            numbers_summed.append(numbers[j])
            j += 1

        if total == number_to_sum:
            return min(numbers_summed) + max(numbers_summed)


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
