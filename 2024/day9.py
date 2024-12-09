import os 

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def read_file(file_path):
    with open(get_file_path(file_path), 'r') as file:
        lines = [line.rstrip() for line in file]
        return lines
    
def calculate_score(rez):
    answ = 0
    for i in range(len(rez)):
        if rez[i] != ".":
            answ += i * int(rez[i])
    return answ

def initialize_array(contents, track_free_spaces=False, use_strings=False):
    rez = []
    free_spaces = {}
    is_free = False
    current_id = 0
    
    for char in contents:
        if is_free:
            if track_free_spaces:
                free_spaces[len(rez)] = int(char)
            for _ in range(int(char)):
                rez.append(".")
        else:
            for _ in range(int(char)):
                rez.append(str(current_id) if use_strings else current_id)
            current_id += 1
        is_free = not is_free
        
    return rez, free_spaces

def solve_part1(contents):
    rez, _ = initialize_array(contents)

    def check_split(lst):
        try:
            dot_index = lst.index(".")
            return (all(isinstance(x, int) for x in lst[:dot_index]) and 
                    all(x == "." for x in lst[dot_index:]))
        except ValueError:
            return False
        
    rez_copy = rez.copy()

    for idx in range(len(rez)):
        chr = rez[-(idx+1)]
        if chr == ".":
            continue
        elif "." in rez_copy:
            empty_place = rez_copy.index(".")
            if empty_place:
                rez_copy[empty_place] = chr
                rez_copy[-(idx+1)] = "."
        if check_split(rez_copy):
            break

    return calculate_score(rez_copy)

def solve_part2(contents):
    rez, free_spaces = initialize_array(contents, track_free_spaces=True, use_strings=True)

    rez_copy = rez.copy()
    current_pos = len(rez_copy) - 1
    seen = set()
    
    while current_pos > 0:
        if rez_copy[current_pos] == ".":
            current_pos -= 1
            continue
            
        chr = rez_copy[current_pos]
        if chr in seen:
            current_pos -= 1
            continue
        seen.add(chr)

        # Count file size
        file_size = 0
        while current_pos >= 0 and rez_copy[current_pos] == chr:
            file_size += 1
            current_pos -= 1

        # Find suitable empty space
        empty_places = [(pos, size) for pos, size in free_spaces.items() 
                       if pos <= current_pos and size >= file_size]
        
        if not empty_places:
            continue

        # Move to earliest possible position
        empty_place, length = min(empty_places, key=lambda x: x[0])
        
        # Update positions
        for i in range(empty_place, empty_place + file_size):
            rez_copy[i] = chr
        for i in range(current_pos + 1, current_pos + 1 + file_size):
            rez_copy[i] = "."
            
        del free_spaces[empty_place]
        if file_size < length:
            free_spaces[empty_place + file_size] = length - file_size

    return calculate_score(rez_copy)

FILE = "in.txt"
contents = list(read_file(FILE)[0])

print(f"Part 1: {solve_part1(contents)}")
print(f"Part 2: {solve_part2(contents)}")
