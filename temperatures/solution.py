import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

closest = 5527 # the closest to zero, initially out of bounds

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    # if the absolute temp is lower than closest, new candidate
    if abs(t) < abs(closest) :
        closest = t
    # if the absolute temp is equal to closest, only take positive temps
    elif abs(t) == abs(closest) and t>0:
        closest = t


# at the end, if no temperatures, then report 0
if n == 0 :
    closest = 0

print(closest)
