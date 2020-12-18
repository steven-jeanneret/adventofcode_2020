from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        coords = []
        for x, line in enumerate(f.readlines()):
            data = line.strip('\n')
            coords_x = []
            for y, chars in enumerate(list(data)):
                coords_x.append(1 if chars == '#' else 0)

            coords.append(coords_x)

        return [coords]


def get_input_from_file_2():
    return [get_input_from_file()]


def count_neighbors(coords, z, x, y):
    count = 0
    for zi in range(-1, 2):
        for xi in range(-1, 2):
            for yi in range(-1, 2):
                if zi == 0 and xi == 0 and yi == 0:
                    continue

                try:
                    count += 1 if coords[z + zi][x + xi][y + yi] == 1 else 0
                except IndexError:
                    pass
    return count


def count_neighbors_2(coords, w, z, x, y):
    count = 0
    for wi in range(-1, 2):
        for zi in range(-1, 2):
            for xi in range(-1, 2):
                for yi in range(-1, 2):
                    if wi == 0 and zi == 0 and xi == 0 and yi == 0:
                        continue

                    try:
                        count += 1 if coords[w + wi][z + zi][x + xi][y + yi] == 1 else 0
                    except IndexError:
                        pass
    return count


def get_new_value(coords, z, x, y):
    neighbors = count_neighbors(coords, z, x, y)

    if neighbors == 3:
        return 1
    if coords[z][x][y] == 1 and neighbors == 2:
        return 1

    return 0


def get_new_value_2(coords, w, z, x, y):
    neighbors = count_neighbors_2(coords, w, z, x, y)

    if neighbors == 3:
        return 1
    if coords[w][z][x][y] == 1 and neighbors == 2:
        return 1

    return 0


def expand_2_row(coords):
    default_list = [[0 for y in range(len(coords[0][0]))] for x in range(len(coords[0]))]

    coords.insert(0, deepcopy(default_list))
    coords.append(deepcopy(default_list))

    for z in range(len(coords)):
        default_list_2 = [0 for y in range(len(coords[z][0]))]
        coords[z].insert(0, deepcopy(default_list_2))
        coords[z].append(deepcopy(default_list_2))

    for z in range(len(coords)):
        for x in range(len(coords[z])):
            coords[z][x].insert(0, 0)
            coords[z][x].append(0)


def expand_2_row_2(coords):
    default_list = [[[0 for y in range(len(coords[0][0][0]))] for x in range(len(coords[0][0]))] for z in range(len(coords[0]))]
    coords.insert(0, deepcopy(default_list))
    coords.append(deepcopy(default_list))

    for w in range(len(coords)):
        default_list = [[0 for y in range(len(coords[w][0][0]))] for x in range(len(coords[w][0]))]
        coords[w].insert(0, deepcopy(default_list))
        coords[w].append(deepcopy(default_list))

    for w in range(len(coords)):
        for z in range(len(coords[w])):
            default_list_2 = [0 for y in range(len(coords[w][z][0]))]
            coords[w][z].insert(0, deepcopy(default_list_2))
            coords[w][z].append(deepcopy(default_list_2))

    for w in range(len(coords)):
        for z in range(len(coords[w])):
            for x in range(len(coords[w][z])):
                coords[w][z][x].insert(0, 0)
                coords[w][z][x].append(0)


def solve_1():
    coords = get_input_from_file()
    for i in range(6):
        expand_2_row(coords)
        new_coords = deepcopy(coords)
        for z in range(len(coords)):
            for x in range(len(coords[z])):
                for y in range(len(coords[z][x])):
                    new_coords[z][x][y] = get_new_value(coords, z, x, y)

        coords = new_coords

        count = 0
        for z in range(len(coords)):
            for x in range(len(coords[z])):
                count += sum(coords[z][x])
        print(f"{i}: {count}")

    return count


def solve_2():
    coords = get_input_from_file_2()
    count = None

    for i in range(6):
        expand_2_row_2(coords)
        new_coords = deepcopy(coords)
        for w in range(len(coords)):
            for z in range(len(coords[w])):
                for x in range(len(coords[w][z])):
                    for y in range(len(coords[w][z][x])):
                        new_coords[w][z][x][y] = get_new_value_2(coords, w, z, x, y)

        coords = new_coords

        count = 0
        for w in range(len(coords)):
            for z in range(len(coords[w])):
                for x in range(len(coords[w][z])):
                    count += sum(coords[w][z][x])
        print(f"{i}: {count}")

    return count

if __name__ == '__main__':
    print(solve_1())
    print(solve_2())



