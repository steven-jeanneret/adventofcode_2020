def get_input_from_file():
    with open('input') as f:
        input = f.read().split('\n')

        return input


def solve_1():
    return solve_path(3, 1)

def solve_2():
    patterns = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    product = 1

    for right, down in patterns:
        product *= solve_path(right, down)

    return product



def solve_path(right, down):
    data = get_input_from_file()
    tree_count = 0
    x = 0
    y = 0

    while x < len(data):
        line = data[x]
        if line[y] == '#':
            tree_count += 1

        x += down
        y += right
        y %= len(line)


    return tree_count


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())