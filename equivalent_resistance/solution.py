import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def series(rlist):
    print("Series Resistor: ", rlist, file=sys.stderr, flush=True,end='')  
    r = 0.0
    for n in rlist:
        print("", n, resistors[n], file=sys.stderr, flush=True,end='')  
        r = r + resistors[n]
    print(" =", r, file=sys.stderr, flush=True)      
    return r

def parallel(rlist):
    print("Parallel Resistor: ", rlist, file=sys.stderr, flush=True,end='') 
    r = 0.0
    for n in rlist:
        print("", n, resistors[n],file=sys.stderr, flush=True,end='')  
        r = r + 1/resistors[n]
    r = 1/r    
    print(" =", r, file=sys.stderr, flush=True)  
    return r

def sortBranches(subcircuit):
    stack=[]
    for i,c in enumerate(subcircuit):
        if c=="[" or c=="(":
            stack.append(i)
        elif c=="]" and stack:
            start = stack.pop()
            yield (len(stack),"["+subcircuit[start+1:i]+"]")
        elif c==")" and stack:
            start = stack.pop()
            yield (len(stack),"("+subcircuit[start+1:i]+")")


resistor_n = int(input())

resistors = {}
for i in range(resistor_n):
    inputs = input().split()
    name = str(inputs[0])
    r = float(inputs[1])
    resistors.update({name:r})

print("Resistors: ", resistors,file=sys.stderr, flush=True)

circuit = input()

print("Circuit: ", circuit,file=sys.stderr, flush=True)

aliaslist = {}
last_resistance = 0.0

for subcircuit in sortBranches(circuit):
    print("Subciruit: ", circuit,file=sys.stderr, flush=True)
    level = subcircuit[0]
    branch = subcircuit[1]
    
    print("Branch: ", branch,file=sys.stderr, flush=True)

    for alias in aliaslist:
        if alias in branch:
            print("Replacing: ",alias,"->",aliaslist[alias],file=sys.stderr, flush=True)
            branch=branch.replace(alias,aliaslist[alias])
    
    print("Evaluating: ",branch,file=sys.stderr, flush=True)   
    fauxresistor = branch
    newresistor=0
    if branch.startswith("("):
        print("Series: ", branch,file=sys.stderr, flush=True)
        prep = str(branch[1:branch.index(")")])
        newresistor = prep.replace(" ","")+"-"
        last_resistance = float(series(prep.split()))
        aliaslist.update({fauxresistor:newresistor})
        resistors.update({newresistor:last_resistance})
        print("Added: ",fauxresistor,"->",newresistor,"=",last_resistance,file=sys.stderr, flush=True)
    elif branch.startswith("["):
        print("Parallel: ", branch,file=sys.stderr, flush=True)
        prep = str(branch[1:branch.index("]")])
        newresistor = prep.replace(" ","")+"+"
        last_resistance = float(parallel(prep.split()))
        aliaslist.update({fauxresistor:newresistor})
        resistors.update({newresistor:last_resistance})
        print("Added: ",fauxresistor,"->",newresistor,"=",last_resistance,file=sys.stderr, flush=True)


    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("{:10.1f}".format(last_resistance).strip())


