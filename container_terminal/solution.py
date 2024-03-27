import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    line = list(input())
    print("",line, file=sys.stderr, flush=True)
    # make space to stack stuff
    stacks = [[]]
    # handle each container as it arrives
    for destination in line:
        print("--->",destination, file=sys.stderr, flush=True)
        placed=False
        stack=0
        while not(placed):
            print("Stack",stack,"size=",len(stacks[stack]), file=sys.stderr, flush=True)
            # used stack?
            if stacks[stack]:
                print("Top of stack",stack,"=",stacks[stack][-1],file=sys.stderr)
                if destination<=str(stacks[stack][-1]):
                    stacks[stack].append(destination)
                    placed=True
                    print("Existing Stack",stack,"contains",stacks[stack],"size=",len(stacks[stack]), file=sys.stderr, flush=True)
                else:
                    print(destination,"does not belong on stack",stack,file=sys.stderr)
            else:    
                stacks[stack].append(destination)
                stacks.append([])
                placed=True
                print("New Stack",stack,"contains",stacks[stack],"size=",len(stacks[stack]), file=sys.stderr, flush=True)
            stack+=1
        
    print(len(stacks)-1)
    print("-----------------------------------------------------------------------", file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


