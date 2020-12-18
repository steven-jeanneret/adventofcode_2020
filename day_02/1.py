def get_input_from_file():
    with open('input') as f:
        input = f.read().split('\n')

        data = []

        for i in input:
            if i != '':
                policy, password = i.split(': ')
                range, letter = policy.split(' ')
                min, max = range.split('-')
                data.append({
                    'min': int(min),
                    'max': int(max),
                    'letter': letter,
                    'password': password,
                })

        return data


def solve_1():
    data = get_input_from_file()
    count = 0

    for d in data:
        if d['min'] <= d['password'].count(d['letter']) <= d['max']:
            count += 1

    return count



def solve_2():
    data = get_input_from_file()
    count = 0

    for d in data:
        match = 0
        match += d['password'][d['min'] - 1] == d['letter']
        match += d['password'][d['max'] - 1] == d['letter']
        if match == 1:
            count += 1    

    return count


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())