from collections import defaultdict


def get_input_from_file():
    with open('input') as f:
        return [int(number) for number in f.readline().strip('\n').split(',')]


def solve(end):
    starting_list = get_input_from_file()
    last_seen = defaultdict(list)
    last_spoken_number = None

    for i in range(end):
        if i < len(starting_list):
            last_spoken_number = starting_list[i]
            last_seen[last_spoken_number].append(i)
        else:
            if len(last_seen[last_spoken_number]) == 0:
                last_seen[0].append(i)
                last_spoken_number = 0
            else:
                count_number = len(last_seen[last_spoken_number])
                last_time_spoken = last_seen[last_spoken_number][count_number - 1]
                before_last_time_spoken = last_seen[last_spoken_number][count_number - 2]
                last_spoken_number = last_time_spoken - before_last_time_spoken
                last_seen[last_spoken_number].append(i)

    return last_spoken_number


if __name__ == '__main__':
    print(solve(2020))
    print(solve(30000000))



