import os

FINAL = "day2.txt"
DEMO = "in.txt"
ANSWER_1 = 2
ANSWER_2 = 4


def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            arr_list = list(map(int, line.split()))
            array.append(arr_list)
    return array


def check_list(lst):
    is_inc = all((lst[i] < lst[i + 1]) for i in range(len(lst) - 1))
    is_dec = all((lst[i] > lst[i + 1]) for i in range(len(lst) - 1))
    diffs_good = all(abs(lst[i] - lst[i + 1]) >=1 and abs(lst[i] - lst[i + 1])<=3 for i in range(len(lst) - 1))
    return (is_inc or is_dec) and diffs_good

def part1(file_path):
    lst = read_file(file_path)
    cnt = 0
    for line in lst:
        if check_list(line):
            cnt+=1
    return cnt

def part2(file_path):
    lst = read_file(file_path)
    cnt = 0
    for line in lst:
        if check_list(line):
            cnt+=1
        else:
            for i in range(len(line)):
                new_line = line[:i]+line[i+1:]
                if check_list(new_line):
                    cnt+=1
                    break
    return cnt

if __name__ == '__main__':
    demo_path = get_file_path(DEMO)
    final_path = get_file_path(FINAL)
    
    answ1 = part1(demo_path)
    if answ1 == ANSWER_1:
        print(part1(final_path))
    
    answ1 = part2(demo_path)
    if answ1 == ANSWER_2:
        print(part2(final_path))
