from collections import defaultdict


def get_input_from_file():
    with open('input') as f:
        rules = defaultdict(list)
        our_ticket = None
        others_ticket = []

        stage = 0

        for line in f.readlines():
            data = line.strip('\n')
            if not data:
                stage += 1
                continue

            if stage == 0:
                field, values = data.split(': ')
                first_range, second_range = values.split(' or ')
                rules[field].append((int(first_range.split('-')[0]), int(first_range.split('-')[1])))
                rules[field].append((int(second_range.split('-')[0]), int(second_range.split('-')[1])))
            elif stage == 1:
                values = data.split(',')
                if len(values) > 1:
                    our_ticket = [int(i) for i in values]
            elif stage == 2:
                values = data.split(',')
                if len(values) > 1:
                    others_ticket.append([int(i) for i in values])

        return rules, our_ticket, others_ticket


def is_value_valid(value, rules):
    for ranges in rules.values():
        for start, end in ranges:
            if start <= value <= end:
                return True

    return False


def is_ticket_valid(ticket, rules):
    for value in ticket:
        if not is_value_valid(value, rules):
            return False

    return True


def is_in_range(value, ranges):
    for start, end in ranges:
        if start <= value <= end:
            return True

    return False


def is_field_valid_for_each_ticket(ranges, tickets, i):
    for ticket in tickets:
        if not is_in_range(ticket[i], ranges):
            return False

    return True


def solve_1():
    rules, our_ticket, others_tickets = get_input_from_file()
    invalid_sum = 0

    for ticket in others_tickets:
        for value in ticket:
            if not is_value_valid(value, rules):
                invalid_sum += value

    return invalid_sum


def solve_2():
    rules, our_ticket, others_tickets = get_input_from_file()
    valid_tickets = [our_ticket]
    rules_order = defaultdict(list)

    for ticket in others_tickets:
        if is_ticket_valid(ticket, rules):
            valid_tickets.append(ticket)

    for field, ranges in rules.items():
        for i in range(len(our_ticket)):
            if is_field_valid_for_each_ticket(ranges, valid_tickets, i):
                rules_order[field].append(i)

    idx_used = []
    for field, idxs in sorted(rules_order.items(), key=lambda item: len(item[1])):
        for idx in idxs:
            if idx not in idx_used:
                rules_order[field] = idx
                idx_used.append(idx)

    product = 1
    for field, i in rules_order.items():
        if field.startswith("departure"):
            product *= our_ticket[i]

    return product


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
