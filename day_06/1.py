def get_input_from_file():
    with open('input') as f:
        groups = []
        current_group = set()

        for line in f.readlines():
            data = line.strip('\n')
            if data:
                for i in range(len(data)):
                    current_group.add(data[i])
            else:
                groups.append(current_group)
                current_group = set()

        groups.append(current_group)

        return groups


def get_input_from_file_2():
    with open('input') as f:
        groups = []
        current_group = []

        for line in f.readlines():
            data = line.strip('\n')
            if data:
                current_answer = set()
                for i in range(len(data)):
                    current_answer.add(data[i])
                
                current_group.append(current_answer)
                
            else:
                groups.append(set.intersection(*current_group))
                current_group = []
        
        groups.append(set.intersection(*current_group))

        return groups


def solve_1():
    groups_answers = get_input_from_file()
    return sum(len(answer) for answer in groups_answers)



def solve_2():
    groups_answers = get_input_from_file_2()
    return sum(len(answer) for answer in groups_answers)

if __name__ == '__main__':
    print(solve_1())
    print(solve_2())