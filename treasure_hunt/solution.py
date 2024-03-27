import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def bestPath(start_x,start_y,prevpath=[[]]):
    print("Checking",start_x,start_y,  file=sys.stderr, flush=True)
    gold = 0

    # out of bounds    
    if not(start_x<h and start_x>=0 and start_y<w and start_y>=0):
        print("Out of Bounds!", file=sys.stderr, flush=True)
        return gold


    # do not go where we have already been
    thisplace = [start_x,start_y]
    print("This place:",thisplace, file=sys.stderr, flush=True)
    #print(start_x,start_x,"Previously",prevpath, file=sys.stderr, flush=True)
    if thisplace in prevpath:
        print("Been here before!", file=sys.stderr, flush=True)
        return gold

    mypath = list(prevpath)
    #print("My path:",mypath, file=sys.stderr, flush=True)
    if not(thisplace in mypath):
        if not(mypath[0]):mypath=[thisplace]
        else:mypath.append(thisplace)
    #print("My path append:",mypath, file=sys.stderr, flush=True)

    loc = str(field[start_x][start_y])


    # wall... stop here
    if loc=="#":
        #print("Can't go this way!", file=sys.stderr, flush=True)
        return gold

    # standing on gold?    
    if loc.isnumeric():
        gold = int(loc)
        print("Gold!",loc,"=",gold, file=sys.stderr, flush=True)

    # try each direction  
    pathGold = int(bestPath(start_x-1,start_y,mypath))
    pathGold = max(pathGold,int(bestPath(start_x+1,start_y,mypath)))
    pathGold = max(pathGold,int(bestPath(start_x-1,start_y,mypath)))
    pathGold = max(pathGold,int(bestPath(start_x,start_y+1,mypath)))
    pathGold = max(pathGold,int(bestPath(start_x,start_y-1,mypath)))
    
    gold = gold + pathGold
    print("Path Gold =",gold, file=sys.stderr, flush=True)
    return int(gold)
    
    



h, w = [int(i) for i in input().split()]

field=[]
begin_x = -1
begin_y = -1

for i in range(h):
    row = list(str(input()))
    if "X" in row:
        begin_x = i
        begin_y = row.index("X")
    print("Row",i,row, file=sys.stderr, flush=True)
    field.append(row)

print("Start",begin_x,begin_y, file=sys.stderr, flush=True)

gold = bestPath(begin_x,begin_y)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(gold)
