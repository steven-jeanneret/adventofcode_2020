def get_input_from_file():
    with open('input') as f:
        input = f.read().split('\n')

        return [int(i) for i in input if i != '']


def solve_1():
    input = get_input_from_file()
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k


def solve_2():
    input = get_input_from_file()
    for i in input:
        for j in input:
            if i + j == 2020:
                return i * j


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())