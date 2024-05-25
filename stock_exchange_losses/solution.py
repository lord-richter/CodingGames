import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
highestV = 0
lossV = 0
for i in input().split():
    currentV = int(i)
    
    if (highestV > currentV) and (currentV - highestV)<lossV:
        lossV = currentV - highestV
    else :
        highestV = max(currentV,highestV)

    print("currentV", currentV, "maxV",highestV, "maxLoss",lossV, file=sys.stderr, flush=True)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lossV)
