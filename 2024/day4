array = []
with open("day4.txt", 'r') as file:
    for line in file:
        ln = list(line.replace("\n", ""))
        array.append(ln)
#part1
def check_coord(x,y):
    cnt = 0
    #right to left
    if x-3>=0:
        if array[y][x]+array[y][x-1]+array[y][x-2]+array[y][x-3] == "XMAS":
            cnt+=1
    #left to right

    if x+3<len(array[0]):
        if "".join(array[y][x:x+4]) == "XMAS":
            cnt+=1
    #up
    if y-3>=0:
        if array[y-3][x]+array[y-2][x]+array[y-1][x]+array[y][x]=="SAMX":
            cnt+=1
    #down
    if y+3<len(array):
        if array[y][x]+array[y+1][x]+array[y+2][x]+array[y+3][x]=="XMAS":
            cnt+=1
    #left up
    if y-3>=0 and x-3>=0:
        if array[y-3][x-3]+array[y-2][x-2]+array[y-1][x-1]+array[y][x]=="SAMX":
            cnt+=1
    #right up
    if y-3>=0 and x+3<len(array[0]):
        if array[y-3][x+3]+array[y-2][x+2]+array[y-1][x+1]+array[y][x]=="SAMX":
            cnt+=1
    #left down
    if y+3<len(array) and x-3>=0:
        if array[y+3][x-3]+array[y+2][x-2]+array[y+1][x-1]+array[y][x]=="SAMX":
            cnt+=1
    #right down
    if y+3<len(array) and x+3<len(array[0]):
        if array[y+3][x+3]+array[y+2][x+2]+array[y+1][x+1]+array[y][x]=="SAMX":
            cnt+=1
    return cnt

def check_coord_p2(x,y):
    if x>=1 and x+1 <len(array[0]) and y>=1 and y+1<len(array):
        if (array[y-1][x-1]+array[y][x]+array[y+1][x+1]=="MAS" or array[y-1][x-1]+array[y][x]+array[y+1][x+1]=="SAM") and (array[y-1][x+1]+array[y][x]+array[y+1][x-1]=="MAS" or array[y-1][x+1]+array[y][x]+array[y+1][x-1]=="SAM"):
            return 1
    
    return 0

tot_p1 = 0
tot_p2 = 0 
for y in range(len(array)):
    for x in range(len(array[0])):
        tot_p1+= check_coord(x,y) if array[y][x] == 'X' else 0
        tot_p2+= check_coord_p2(x,y) if array[y][x]=='A' else 0

print(tot_p1)
print(tot_p2)
