import os

FINAL = "day1.txt"
DEMO = "in.txt"
ANSWER_1 = 11
ANSWER_2 = 31


def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    array1 = []
    array2 = []
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            array1.append(num1)
            array2.append(num2)
    return array1, array2
    
def part1(ar1, ar2):
    arr1 = sorted(ar1)
    arr2 = sorted(ar2)
    tot = 0
    for i in range(len(arr1)):
        tot+= abs(arr1[i] - arr2[i])
    return tot

def part2(ar1, ar2):
    from collections import Counter
    cnt = dict(Counter(ar2))
    tot = 0
    for i in ar1:
        tot += cnt.get(i,0) * i
    return tot

if __name__ == "__main__":
    demo_path = get_file_path(DEMO)
    final_path = get_file_path(FINAL)
    
    ar1, ar2 = read_file(demo_path)
    answ1 = part1(ar1, ar2)
    if answ1 == ANSWER_1:
        ar1, ar2 = read_file(final_path)
        print(part1(ar1, ar2))
    
    ar1, ar2 = read_file(demo_path)
    answ1 = part2(ar1, ar2)
    if answ1 == ANSWER_2:
        ar1, ar2 = read_file(final_path)
        print(part2(ar1, ar2))
    