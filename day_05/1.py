def get_input_from_file():
    with open('input') as f:
        boarding_passes = []

        for line in f.readlines():
            boarding_pass = {}
            data = line.strip('\n')
            if data:
                begin = 0
                end = 127
                for i in range(7):
                    current_range_size = (end - begin + 1) / 2
                    if data[i] == 'F':
                        end -= current_range_size
                    else:
                        begin += current_range_size
                    
                boarding_pass['rows'] = int(begin)

                begin = 0
                end = 7
                
                for i in range(7, 10):
                    current_range_size = (end - begin + 1) / 2
                    if data[i] == 'L':
                        end -= current_range_size
                    else:
                        begin += current_range_size
                
                boarding_pass['col'] = int(begin)

                boarding_pass['id'] = boarding_pass['rows'] * 8 + boarding_pass['col']
                    

                boarding_passes.append(boarding_pass)

        return boarding_passes


def solve_1():
    boarding_passes = get_input_from_file()
    ids = [b['id'] for b in boarding_passes]
    return max(ids)



def solve_2():
    boarding_passes = get_input_from_file()
    ids = [b['id'] for b in boarding_passes]
    number_of_passenger = max(ids)

    unused_place = []
    for i in range(1, number_of_passenger):
        if i not in ids:
            unused_place.append(i)

    return unused_place

if __name__ == '__main__':
    print(solve_1())
    print(solve_2())