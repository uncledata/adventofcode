import os 
def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [list(line.rstrip()) for line in file]
        return lines
    
def draw_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()
    

contents = read_file("day6.txt")

guard_moves = {
    "^":(0,-1),
    ">":(1,0),
    "v":(0,1),
    "<":(-1,0)
    }

rows = len(contents)
cols = len(contents[0])
visited = set()

# find guard
for y in range(len(contents)):
    for x in range(len(contents[0])):
        if contents[y][x] == '^':
            guard_pos = (x,y)
            guard_dir = contents[y][x]
        if contents[y][x] == '>':
            guard_pos = (x,y)
            guard_dir = contents[y][x]
        if contents[y][x] == 'v':
            guard_pos = (x,y)
            guard_dir = contents[y][x]
        if contents[y][x] == '<':
            guard_pos = (x,y)
            guard_dir = contents[y][x]
            break
        
        
init_guard_dir = guard_dir
init_guard_pos = guard_pos
cur_x, cur_y = guard_pos
visited.add((cur_x, cur_y))
contents[cur_y][cur_x] = "."

while True:
    # out of bounds
    if (cur_x+guard_moves[guard_dir][0] < 0 or cur_x+guard_moves[guard_dir][0] >= len(contents[0]) 
        or cur_y+guard_moves[guard_dir][1] < 0 or cur_y+guard_moves[guard_dir][1] >= len(contents)):
        break
    else:
        if contents[cur_y + guard_moves[guard_dir][1]][cur_x+guard_moves[guard_dir][0]]==".":
            cur_x += guard_moves[guard_dir][0]
            cur_y += guard_moves[guard_dir][1]
        else:
            if guard_dir == "^":
                guard_dir = ">"
            elif guard_dir == ">":
                guard_dir = "v"
            elif guard_dir == "v":
                guard_dir = "<"
            elif guard_dir == "<":
                guard_dir = "^"
            #draw_grid(grid)
        visited.add((cur_x, cur_y))
    
print(len(visited))

initial_x = init_guard_pos[0]
initial_y = init_guard_pos[1]
initial_dir = init_guard_dir

obstacles = set()


for obstacle in visited:
    if obstacle != init_guard_pos:
        cur_x, cur_y, guard_dir = initial_x, initial_y, initial_dir
        visited_positions = set()
        contents = read_file("day6.txt")
        contents[cur_y][cur_x] = "."
        # fake obstacle
        contents[obstacle[1]][obstacle[0]] = "#"
        while True:
            if (cur_x + guard_moves[guard_dir][0] < 0 or cur_x + guard_moves[guard_dir][0] >= len(contents[0]) 
                    or cur_y + guard_moves[guard_dir][1] < 0 or cur_y + guard_moves[guard_dir][1] >= len(contents)):
                break
            else:
                if contents[cur_y + guard_moves[guard_dir][1]][cur_x + guard_moves[guard_dir][0]] == ".":
                    cur_x += guard_moves[guard_dir][0]
                    cur_y += guard_moves[guard_dir][1]
                else:
                    if guard_dir == "^":
                        guard_dir = ">"
                    elif guard_dir == ">":
                        guard_dir = "v"
                    elif guard_dir == "v":
                        guard_dir = "<"
                    elif guard_dir == "<":
                        guard_dir = "^"
                # Check for loop if we already came to this position from same direction
                if (cur_x, cur_y, guard_dir) in visited_positions:
                    obstacles.add(obstacle)
                    break
                visited_positions.add((cur_x, cur_y, guard_dir))
    

print(len(obstacles))