from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        lines = []

        for line in f.readlines():
            data = line.strip('\n')
            line = list(data)
            lines.append(line)

        return lines


def seat_value(lines, row, col):
    if lines[row][col] == '.':
        return None

    adjacent_count = 0

    for i in range(max(row - 1, 0), min(row + 2, len(lines))):
        for k in range(max(col - 1, 0), min(col + 2, len(lines[i]))):
            if i != row or k != col:
                if lines[i][k] == "#":
                    adjacent_count += 1

    if lines[row][col] == '#' and adjacent_count >= 4:
        return 'L'

    if lines[row][col] == 'L' and adjacent_count == 0:
        return '#'

    return None


def seat_value_2(lines, row, col):
    if lines[row][col] == '.':
        return None

    adjacent_count = 0
    for row_dir in range(-1, 2):
        for col_dir in range(-1, 2):
            if row_dir != 0 or col_dir != 0:
                curr_row = row + row_dir
                curr_col = col + col_dir

                while curr_row >= 0 and curr_row < len(lines) and curr_col >= 0 and curr_col < len(lines[curr_row]):
                    if lines[curr_row][curr_col] == "#":
                        adjacent_count += 1
                        break
                    elif lines[curr_row][curr_col] == "L":
                        break

                    curr_row += row_dir
                    curr_col += col_dir

    if lines[row][col] == '#' and adjacent_count >= 5:
        return 'L'

    if lines[row][col] == 'L' and adjacent_count == 0:
        return '#'

    return None


def count_occupied_places(lines):
    count = 0
    for line in lines:
        for c in line:
            if c == '#':
                count += 1

    return count


def solve_1():
    lines = get_input_from_file()
    has_changed = True

    while has_changed:
        has_changed = False
        old_lines = deepcopy(lines)
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                new_value = seat_value(old_lines, x, y)

                if new_value:
                    has_changed = True
                    lines[x][y] = new_value

    return count_occupied_places(lines)


def solve_2():
    lines = get_input_from_file()
    has_changed = True

    while has_changed:
        has_changed = False
        old_lines = deepcopy(lines)
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                new_value = seat_value_2(old_lines, x, y)

                if new_value:
                    has_changed = True
                    lines[x][y] = new_value

    return count_occupied_places(lines)


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
