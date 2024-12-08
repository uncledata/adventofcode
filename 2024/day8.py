import os 

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [line.rstrip() for line in file]
        return lines
    
FILE = "day8.txt"



contents = read_file(FILE)
antenas = dict()

max_x = len(contents[0])   
max_y = len(contents)


for idy, i in enumerate(contents):
    for idx, j in enumerate(i):
        if j!=".":
            if antenas.get(j) is None:
                antenas[j] = [(idx, idy)]
            else:
                antenas[j].append((idx, idy))
                
# part1
anti_antenas = set()
for antena, coords in antenas.items():
    for id1, antena_coord in enumerate(coords):
        for id2, antena_coord2 in enumerate(coords):
            if id1!=id2:
                diff_x = antena_coord[0] - antena_coord2[0]
                diff_y = antena_coord[1] - antena_coord2[1]
                if (antena_coord[0] + diff_x >= 0 and antena_coord[0] + diff_x < max_x) and (antena_coord[1] + diff_y >= 0 and antena_coord[1] + diff_y < max_y):
                    anti_antenas.add((antena_coord[0] + diff_x, antena_coord[1] + diff_y))
                if (antena_coord2[0] - diff_x >= 0 and antena_coord2[0] - diff_x < max_x) and (antena_coord2[1] - diff_y >= 0 and antena_coord2[1] - diff_y < max_y):
                    anti_antenas.add((antena_coord2[0] - diff_x, antena_coord2[1] - diff_y))
                    
                
print(len(anti_antenas))

#part2

pairs_checked = set()
anti_antenas = set()
for antena, coords in antenas.items():
    for id1, antena_coord in enumerate(coords):
        for id2, antena_coord2 in enumerate(coords):
            if id1<id2:
                diff_x = antena_coord[0] - antena_coord2[0]
                diff_y = antena_coord[1] - antena_coord2[1]
                    
                anti_coord_x = antena_coord[0] + diff_x
                anti_coord_y = antena_coord[1] + diff_y
                    
                anti_coord2_x = antena_coord2[0] - diff_x
                anti_coord2_y = antena_coord2[1] - diff_y
                    
                while anti_coord_x >= 0 and anti_coord_x < max_x and anti_coord_y >= 0 and anti_coord_y < max_y:
                    anti_antenas.add((anti_coord_x, anti_coord_y))
                    anti_coord_x += diff_x
                    anti_coord_y += diff_y
                while anti_coord2_x >= 0 and anti_coord2_x < max_x and anti_coord2_y >= 0 and anti_coord2_y < max_y:
                    anti_antenas.add((anti_coord2_x, anti_coord2_y))
                    anti_coord2_x -= diff_x
                    anti_coord2_y -= diff_y
                # antenas apparently are in the same line, so they will always be anti-antennas as well 
                anti_antenas.add(antena_coord)                  
                anti_antenas.add(antena_coord2)
                
print(len(anti_antenas))
