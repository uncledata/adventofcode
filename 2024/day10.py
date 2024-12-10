import os 

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [list(map(int,list(line.rstrip()))) for line in file]
        return lines
    
FILE = "day10.txt"

move_dir=[(1,0), (0,1), (-1,0), (0,-1)]

contents = read_file(FILE)


def find_trailheads(contents):
    trailheads = []
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def find_paths(x, y, contents, visited, current_height):
    if x < 0 or x >= len(contents) or y < 0 or y >= len(contents[0]) or visited[x][y] or contents[x][y] != current_height:
        return 0
    if contents[x][y] == 9:
        #part1
        #visited[x][y] = True
        return 1
    #part2
    visited[x][y] = True
    count = 0
    for dx, dy in move_dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(contents) and 0 <= ny < len(contents[0]) and contents[nx][ny] == current_height + 1:
            count += find_paths(nx, ny, contents, visited, current_height + 1)
    visited[x][y] = False
    return count

def calculate_scores(contents):
    trailheads = find_trailheads(contents)
    total_score = 0
    for x, y in trailheads:
        visited = [[False for _ in range(len(contents[0]))] for _ in range(len(contents))]
        score = find_paths(x, y, contents, visited, 0)
        total_score += score
    return total_score

total_score = calculate_scores(contents)
print(total_score)