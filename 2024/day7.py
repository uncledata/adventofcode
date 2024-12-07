import os 
from itertools import product


def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [line.rstrip().replace(":","").split(" ") for line in file]
        return lines

def generate_combinations(operators, length):
    return list(product(operators, repeat=length))

FILE = "day7.txt"
    
contents = read_file(FILE)
operators = ['+', '*']


def part1():
    bad = []
    cnt =0
    for i in contents:
        found = False
        answ = i[0]
        left = i[1:]
        combinations = generate_combinations(operators, len(left)-1)
        for comb in combinations:
            res = eval(left[0])
            for idx in range(1,len(left)):
                res = eval(str(res)+comb[idx-1]+str(left[idx]))
            if int(answ) == res:
                cnt+=int(answ)
                found = True
                break
        if not found:
            bad.append(i)
                
    print("part1: ",cnt)
    return bad, cnt

bad, cnt = part1()
print("bad count: ", len(bad))
    
operators2 = ['+', '*', '||']
for idx, i in enumerate(bad):
    if idx%100 == 0:
        print(idx)
    found = False
    answ = i[0]
    left = i[1:]
    combinations = [comb for comb in generate_combinations(operators2, len(left)-1) if "||" in comb]
    
    for comb in combinations:
        res = eval(left[0])
        for idx in range(1,len(left)):
            res = eval(str(res)+ ("" if comb[idx-1] == "||" else comb[idx-1]) +str(left[idx]))
        if int(answ) == res:
            cnt+=int(answ)
            found = True
            break
        
print("part2: ", cnt)