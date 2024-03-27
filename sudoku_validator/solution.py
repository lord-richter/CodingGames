import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


passed = True
column = [[ '' for a in range(9)] for b in range(9)]
cell = [[] for a in range(3)]

for i in range(9):
    row = input().split()
    print(row,file=sys.stderr)
    # check row
    rowsize = len(sorted(set(row)))
    passed = passed and rowsize==9
    print(row,rowsize,passed,file=sys.stderr)
    # save column for later
    for j in range(9):
        column[j][i]=row[j]
        # while we are here, make sure numbers are in range
        if int(row[j])>9 or int(row[j])<1: passed=False
    # cells
    cell[0].extend(row[0:3])
    cell[1].extend(row[3:6])
    cell[2].extend(row[6:9])
    # every third row (9 values) check
    if len(cell[0])==9 and passed:
        passed = passed and len(sorted(set(cell[0])))==9
        passed = passed and len(sorted(set(cell[1])))==9
        passed = passed and len(sorted(set(cell[2])))==9
        # new cell
        cell=[[] for a in range(3)]
    
# column check    
if passed:
    for i in range(9):
        colsize = len(sorted(set(column[i])))
        passed = passed and colsize==9


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("true" if passed else "false")
