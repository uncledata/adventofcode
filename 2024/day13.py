import re
import os
from sympy import symbols, Eq, solve

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        return file.read()

def parse_input(input_str):
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, input_str)
    parsed_data = []
    for match in matches:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match)
        # part1 without, part2 +10000000000000
        parsed_data.append(((a_x, a_y), (b_x, b_y), (prize_x+10000000000000, prize_y+10000000000000)))
    return parsed_data

def find_button_presses(a_x, a_y, b_x, b_y, prize_x, prize_y):
    x, y = symbols('x y')
    eq1 = Eq(a_x * x + b_x * y, prize_x)
    eq2 = Eq(a_y * x + b_y * y, prize_y)
    solution = solve((eq1, eq2), (x, y))
    return solution[x], solution[y]

def calculate_cost(a_presses, b_presses, cost_a=3, cost_b=1):
    return a_presses * cost_a + b_presses * cost_b

input_str = read_file("day13.txt")
parsed_data = parse_input(input_str)

total_costs = []
for (a_x, a_y), (b_x, b_y), (prize_x, prize_y) in parsed_data:
    a_presses, b_presses = find_button_presses(a_x, a_y, b_x, b_y, prize_x, prize_y)
    if a_presses.is_integer and b_presses.is_integer:
        total_cost = calculate_cost(a_presses, b_presses)
    else:
        total_cost = 0
    
    total_costs.append(total_cost)
    
    print(f"Button A presses: {a_presses}")
    print(f"Button B presses: {b_presses}")
    print(f"Total cost: {total_cost} tokens")

overall_cost = sum(total_costs)
print(f"Overall total cost: {overall_cost} tokens")