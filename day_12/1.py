from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        lines = []

        for line in f.readlines():
            data = line.strip('\n')
            instr = data[0]
            value = data[1:]
            lines.append((instr, int(value)))

        return lines


def solve_1():
    lines = get_input_from_file()

    direction = 'E'
    current_pos = defaultdict(int)
    card = ['N', 'E', 'S', 'W']

    for instr, value in lines:
        if instr == 'L':
            decal_list = int(value / 90)
            direction = card[(card.index(direction) - decal_list)%len(card)]
        elif instr == 'R':
            decal_list = int(value / 90)
            direction = card[(card.index(direction) + decal_list)%len(card)]
        elif instr == 'F':
            current_pos[direction] += value
        elif instr == 'N':
            current_pos['N'] += value
        elif instr == 'W':
            current_pos['W'] += value
        elif instr == 'S':
            current_pos['S'] += value
        elif instr == 'E':
            current_pos['E'] += value

    x = abs(current_pos['W'] - current_pos['E'])
    y = abs(current_pos['N'] - current_pos['S'])
    return x + y


def solve_2():
    lines = get_input_from_file()

    direction = 'E'
    current_pos = defaultdict(int)
    waypoint = (1, -10)
    card = ['N', 'E', 'S', 'W']

    for instr, value in lines:
        if instr == 'L':
            x, y = waypoint
            if value == 90:
                new_x = -y
                new_y = x
            elif value == 180:
                new_x = -x
                new_y = -y
            elif value == 270:
                new_x = y
                new_y = -x
            waypoint = (new_x, new_y)
        elif instr == 'R':
            x, y = waypoint
            if value == 90:
                new_x = y
                new_y = -x
            elif value == 180:
                new_x = -x
                new_y = -y
            elif value == 270:
                new_x = -y
                new_y = x
            waypoint = (new_x, new_y)
        elif instr == 'F':
            x, y = waypoint
            current_pos['N'] += x * value
            current_pos['W'] += y * value
        elif instr == 'N':
            x, y = waypoint
            waypoint = (x + value, y)
        elif instr == 'W':
            x, y = waypoint
            waypoint = (x , y + value)
        elif instr == 'S':
            x, y = waypoint
            waypoint = (x - value, y)
        elif instr == 'E':
            x, y = waypoint
            waypoint = (x, y - value)

    return abs(current_pos['N']) + abs(current_pos['W'])


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
