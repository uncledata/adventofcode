from functools import cache

def read_input(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        return [int(x) for x in f.readline().strip().split()]
@cache
def transform_number(number, remaining_steps):
    num_str = str(number) 
    if remaining_steps == 0:
        return 1
    if num_str == '0':
        return transform_number('1', remaining_steps - 1)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left_half = num_str[:mid]
        right_half = num_str[mid:]
        return (transform_number(int(left_half), remaining_steps - 1) + 
                transform_number(int(right_half), remaining_steps - 1))
                
    return transform_number(int(num_str) * 2024, remaining_steps - 1)

def process_input(numbers, steps):
    return sum(transform_number(num, steps) for num in numbers)

if __name__ == '__main__':
    input_numbers = read_input('day11.txt')
    result = process_input(input_numbers, 25)
    print(f"part1: {result}")
    result = process_input(input_numbers, 75)
    print(f"part2: {result}")
