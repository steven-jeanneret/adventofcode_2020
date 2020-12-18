from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        first_ts = int(f.readline().strip('\n'))

        bus_schedule = [int(b) for b in f.readline().strip('\n').split(',') if b != 'x']
        bus_schedule.sort()
        return first_ts, bus_schedule


def get_input_from_file_2():
    with open('input') as f:
        first_ts = int(f.readline().strip('\n'))

        bus_schedule = f.readline().strip('\n').split(',')

        return first_ts, bus_schedule


def solve_1():
    first_ts, bus_schedule = get_input_from_file()
    current_ts = first_ts
    bus_found = False

    while not bus_found:
        for bus in bus_schedule:
            if current_ts % bus == 0:
                return (current_ts - first_ts) * bus

        current_ts += 1


def solve_2():
    first_ts, bus_schedule = get_input_from_file_2()
    offset_for_bus = []

    for i in range(len(bus_schedule)):
        if bus_schedule[i] != 'x':
            offset_for_bus.append((i, int(bus_schedule[i])))

    jump = offset_for_bus[0][1]
    time_stamp = 0
    for delta, bus in offset_for_bus[1:]:
        while (time_stamp + delta) % bus != 0:
            time_stamp += jump

        jump *= bus

    return time_stamp


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())



