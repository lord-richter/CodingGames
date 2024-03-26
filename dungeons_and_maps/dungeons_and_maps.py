import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def nextStep(curmap,x,y):
    dir = curmap[x][y]

    next_x = 0
    next_y = 0

    if dir in onpath:
        if dir==">": next_y=1 if y+1<w else 0
        elif dir=="<": next_y=-1 if y-1>=0 else 0
        elif dir=="^": next_x=-1 if x-1>=0 else 0
        elif dir=="v": next_x=1 if x+1<h else 0
    
    print(x,">",next_x,y,">",next_y,":",dir, file=sys.stderr, flush=True)
    return next_x,next_y,dir



    
offpath = ".T#"
onpath = "<>^v"

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())
minmap=-1
minstep=9999
for i in range(n):
    print("---------------------------------------------------------", file=sys.stderr, flush=True)
    map=[]
    x = start_row
    y = start_col
    for j in range(h):
        map_row = input()
        print(map_row, file=sys.stderr, flush=True)
        map.append(list(map_row))
    location = ">"
    steps = 0
    while location in onpath:
        steps = steps+1
        nx,ny,location=nextStep(map,x,y)  
        map[x][y]="#"
        x=x+nx
        y=y+ny
    if location=="T" and steps<minstep:
        minstep = steps
        minmap = i
        print("New shortest path:  Map",minmap,"Steps",minstep, file=sys.stderr, flush=True)
    else:    
        print("Disappointment:  Map",i,"Steps",steps,"End:",location, file=sys.stderr, flush=True)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(minmap if minmap>=0 else "TRAP")
