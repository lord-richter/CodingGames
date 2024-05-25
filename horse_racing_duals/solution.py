import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

horses = int(input())

list=[] # need a place to store horse data

for i in range(horses):
    strength = int(input())
    print(i,strength,file=sys.stderr,flush=True)
    # just add this to a list to be sorted later
    list.append(strength)

# sort list get adjacent gaps
sortedlist = sorted(list)    

# go through sorted list 
# list gaps for items n and n-1, to prevent array bound issues
# sort list
gaps = sorted([(sortedlist[n]-sortedlist[n-1]) for n in range(1,len(sortedlist))])

# first entry in list is the smallest gap
print(gaps[0])
