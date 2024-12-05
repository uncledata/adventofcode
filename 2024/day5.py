import os

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [line.rstrip() for line in file]
        return lines
    

contents = read_file("day5.txt")

ordering_rules = contents[:contents.index('')]
order_updates = contents[contents.index('')+1:]


order_updates = [list(map(int,x.split(','))) for x in order_updates]
ordering_rules = [list(map(int,x.split('|'))) for x in ordering_rules]

def check_update_order(rules, update):
    order_dict = {page: i for i, page in enumerate(update)}
    for before, after in rules:
        if before in order_dict and after in order_dict:
            if order_dict[before] > order_dict[after]:
                return False
    return True

def filter_correct_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        if check_update_order(rules, update):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates

correct_updates, incorrect_updates = filter_correct_updates(ordering_rules, order_updates)


part1 = 0
for cor in correct_updates:
    part1 += cor[len(cor)//2]
print(part1)

def fix_order(rules, row):
    ordered = False
    while not ordered:
        for rule in rules:
            page_before, page_after = rule
            if page_before in row and page_after in row:
                index_before = row.index(page_before)
                index_after = row.index(page_after)
                if index_after < index_before:
                    row[index_before], row[index_after] = row[index_after], row[index_before]
        ordered = check_update_order(rules, row)
    return row

def get_fixed(rules, updates):
    ordered = []
    for row in updates:
        if not check_update_order(rules, row):
            ordered.append(fix_order(rules, row))
    return ordered

correct_updates = get_fixed(ordering_rules, incorrect_updates)
part2 = 0
for cor in correct_updates:
    part2 += cor[len(cor)//2]
print(part2)
