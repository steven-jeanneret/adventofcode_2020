from collections import defaultdict
from copy import deepcopy


def get_input_from_file():
    with open('input') as f:
        rules = defaultdict(list)

        for line in f.readlines():
            data = line.strip('\n')
            if "no other bags." not in data:
                parent, childs = data.split(' bags contain ')

                for child in childs.split(','):
                    rules[parent].append(" ".join(child.split()[1:-1]))

        return rules


def get_input_from_file_2():
    with open('input') as f:
        rules = defaultdict(list)

        for line in f.readlines():
            data = line.strip('\n')
            if "no other bags." not in data:
                parent, childs = data.split(' bags contain ')

                for child in childs.split(','):
                    count = int(child.split()[0])
                    rules[parent].append((" ".join(child.split()[1:-1]), count))

        return rules


def solve_1():
    rules = get_input_from_file()
    count = 0
    to_find = "shiny gold"

    for parent in list(rules.keys()):
        to_visit = deepcopy(rules[parent])
        visited = [parent]

        while to_visit:
            current = to_visit.pop()
            while current in visited and to_visit:
                current = to_visit.pop()

            if current in visited:
                continue

            if current == to_find:
                count += 1
                to_visit = []
                continue

            to_visit += rules[current]

            visited.append(current)

    return count


def solve_2():
    rules = get_input_from_file_2()
    to_find = "shiny gold"
    count = 0

    to_visit = deepcopy(rules[to_find])
    while to_visit:
        current_key, current_count = to_visit.pop()
        if current_key in rules:
            count += current_count
            for i in range(current_count):
                to_visit += deepcopy(rules[current_key])
        else:
            count += current_count

    return count


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
