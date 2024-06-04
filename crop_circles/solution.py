import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

instructions = input()
alphabet = string.ascii_lowercase

fieldwidth = 19
fieldheight = 25
field = []
for rows in range(fieldheight):
    fieldcolumn=[]
    for columns in range(fieldwidth):
        fieldcolumn.append(True)
    field.append(fieldcolumn)


def circleArea(center_c,center_r,diameter):
    cells = []
    for row in range(0,fieldheight):
        for col in range(0,fieldwidth):
            point = [(row,col)]
            if (row - center_r) * (row - center_r) + (col - center_c) * (col - center_c) <= ((diameter/2) * (diameter/2))+0.5 :
                #print("Add:",point,file=sys.stderr) 
                cells.append(point)

    cells = sorted(cells)

    return cells


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# split instuctions into 
circle_list = instructions.split(" ")
print(circle_list,file=sys.stderr)


for circle in circle_list:
    print("(",circle,file=sys.stderr,end='')

    plant = False
    invert = False


    if circle.startswith("PLANTMOW"):
        invert = True
        circle = circle[8:]
    elif circle.startswith("PLANT"):
        plant = True
        circle = circle[5:]

    print("",circle,")",file=sys.stderr)

    center_column = int(alphabet.index(circle[0]))
    center_row = int(alphabet.index(circle[1]))
    diameter = int(circle[2:])

    print("",center_column,center_row,diameter,file=sys.stderr)

    area = circleArea(center_column,center_row,diameter)

    for fieldlocation in area:
        col = fieldlocation[0][1]
        row = fieldlocation[0][0]
        if row>=0 and row<fieldheight and col>=0 and col<fieldwidth:
            current = field[row][col]
        
            if (plant):
                field[row][col] = True
            elif (invert):
                field[row][col] = not(current)
            else:
                field[row][col] = False


    

for row in field:
    for col in row:
        if col:
            print("{}",end='')
        else:    
            print("  ",end='')
    print()        
