import re
import os

def part1(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def part2(data):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    mul_enabled = True
    total = 0
    
    # Split the data into tokens based on the patterns
    tokens = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', data)
    
    for token in tokens:
        if not token:
            continue
        elif re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled and re.match(mul_pattern, token):
            x, y = re.findall(mul_pattern, token)[0]
            total += int(x) * int(y)
    
    return total

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

if __name__ == '__main__':
    with open(get_file_path('day3.txt'), 'r') as file:
        data = file.read()
    print(part1(data))
    print(part2(data))
