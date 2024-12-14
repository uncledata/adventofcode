import re
import os

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    p_list = []
    v_list = []
    with open(get_file_path(file_path), 'r') as file:
        for line in file:
            parts = line.strip().split()
            p_values = parts[0].split('=')[1].split(',')
            v_values = parts[1].split('=')[1].split(',')
            
            p_list.append((int(p_values[0]), int(p_values[1])))
            v_list.append((int(v_values[0]), int(v_values[1])))
    return p_list, v_list

def split_into_quadrants(coordinates, max_x, max_y):
    top_left = []
    top_right = []
    bottom_right = []
    bottom_left = []

    mid_x = max_x // 2
    mid_y = max_y // 2

    for x, y in coordinates:
        if x == mid_x or y == mid_y:
            continue
        elif x < mid_x and y < mid_y:
            top_left.append((x, y))
        elif x >= mid_x and y < mid_y:
            top_right.append((x, y))
        elif x >= mid_x and y >= mid_y:
            bottom_right.append((x, y))
        elif x < mid_x and y >= mid_y:
            bottom_left.append((x, y))

    return len(top_left)* len(top_right)* len(bottom_right)* len(bottom_left)

FILE = "day14.txt"

max_x = 101
max_y = 103
seconds = 100
p_list, v_list = read_file(FILE)

coords = []
for i in range(len(p_list)):
    coords.append(((p_list[i][0] + v_list[i][0]*seconds)%max_x, (p_list[i][1] + v_list[i][1]*seconds)%max_y))

print(split_into_quadrants(coords, max_x, max_y))



def visualize_coordinates(coordinates, max_x, max_y):
    grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for x, y in coordinates:
        if 0 <= x < max_x and 0 <= y < max_y:
            grid[y][x] = '#'
    for row in grid:
        print(''.join(row))

def check_for_christmas_tree(grid, max_x, max_y):
    tree_pattern = [
        "...#...",
        "..###..",
        ".#####.",
        "#######"
    ]
    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])

    for y in range(max_y - pattern_height + 1):
        for x in range(max_x - pattern_width + 1):
            match = True
            for dy in range(pattern_height):
                for dx in range(pattern_width):
                    if tree_pattern[dy][dx] == '#' and grid[y + dy][x + dx] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

coords = p_list.copy()
seconds = 0
while True:
    for i in range(len(p_list)):
        coords[i]=((p_list[i][0] + v_list[i][0] * seconds)%max_x, (p_list[i][1] + v_list[i][1] * seconds)%max_y)
    
    grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for x, y in coords:
        if 0 <= x < max_x and 0 <= y < max_y:
            grid[y][x] = '#'
            
    #visualize_coordinates(coords, max_x, max_y)
    
    if seconds % 1000 == 0:
        print(f"Checking at {seconds} seconds")
    
    if check_for_christmas_tree(grid, max_x, max_y):
        print(f"Easter egg found at {seconds} seconds")
        visualize_coordinates(coords, max_x, max_y)
        break
    
    seconds += 1