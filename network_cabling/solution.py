import sys
import math
import statistics

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

central = [] # list of y values to calculate where the main cable should be
runlength = []  # list of x values to calculate how wide the houses are

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    central.append(y)
    runlength.append(x)

# find the center, where the main cable will be
middle = int(statistics.median(central))

# the range of X will determine the width
width = int(max(runlength)) - int(min(runlength))

# cable length starts off as the width 
# located on the middle line
mainline = middle
cable = width

# just calculate distance from the mainline for each house
# add to cable length
for z in central :
    # distance from main line
    d = abs(mainline - z)
    # add to cable
    cable = cable + d

print(cable)
