def get_input_from_file():
    with open('input') as f:
        passports = []
        current_passport = {}

        for line in f.readlines():
            data = line.strip('\n')
            if data:
                key_values = data.split(' ')
                for key_value in key_values:
                    key, value = key_value.split(':')
                    current_passport[key] = value
            else:
                passports.append(current_passport)
                current_passport = {}

        passports.append(current_passport)
        current_passport = {}

        return passports


def solve_1():
    passports = get_input_from_file()

    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    count_valid_password = 0

    for passport in passports:
        valid = True
        for required_field in required_fields:
            if required_field not in passport:
                valid = False

        if valid:
            count_valid_password += 1

    return count_valid_password

def solve_2():
    passports = get_input_from_file()

    count_valid_password = 0

    for passport in passports:
        valid = True
        
        byr = int(passport.get('byr', '0'))
        if byr < 1920 or byr > 2002:
            valid = False

        iyr = int(passport.get('iyr', '0'))
        if iyr < 2010 or iyr > 2020:
            valid = False

        eyr = int(passport.get('eyr', '0'))
        if eyr < 2020 or eyr > 2030:
            valid = False

        hgt = passport.get('hgt', '0')
        if hgt.endswith('cm'):
            hgt = int(hgt.strip('cm'))
            if hgt < 150 or hgt > 193:
                valid = False
        elif hgt.endswith('in'):
            hgt = int(hgt.strip('in'))
            if hgt < 59 or hgt > 76:
                valid = False
        else:
            valid = False

        hcl = passport.get('hcl', ' ')
        if hcl[0] == '#' and len(hcl) == 7:
            try:
                int(hcl.strip('#'), 16)
            except ValueError:
                valid = False
        else:
            valid = False

        ecl = passport.get('ecl')
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

        pid = passport.get('pid', '')
        if len(pid) == 9:
            try:
                int(pid)
            except ValueError:
                valid = False
        else:
            valid = False


        if valid:
            count_valid_password += 1

    return count_valid_password

if __name__ == '__main__':
    print(solve_1())
    print(solve_2())