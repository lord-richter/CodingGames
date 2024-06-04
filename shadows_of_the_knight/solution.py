import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# xb: width of the building. (-L/+R)
# yb: height of the building. (-U/+D)
xb, yb = [int(i) for i in input().split()]

# the building is a box that will get smaller
# bomb will always be bounded by these variables
xbL = 0     # left bounds of the building
xbR = xb    # right bounds of the building
ybU = 0     # upper bounds of the building
ybD = yb    # downward bounds of the building

# maximum number of turns before game over.
n = int(input())  

# player starting position
x0, y0 = [int(i) for i in input().split()]

#player current position
x=x0
y=y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    
    dy=0
    if "U" in bomb_dir:
        ybD = y
        dy = int((ybU-y)/2-0.5)  # move half the distance to the upper bound
    elif "D" in bomb_dir:
        ybU = y
        dy = int((ybD-y)/2+0.5)  # move half the distance to the downward bound
    
    dx=0
    if "L" in bomb_dir:
        xbR = x
        dx = int((xbL-x)/2-0.5)  # move half the distance to the left bound
    elif "R" in bomb_dir:
        xbL = x
        dx = int((xbR-x)/2+0.5)  # move half the distance to the right bound

    x = x + dx
    y = y + dy

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(x,y)
