import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def getArrayIndex(arrname,index) :
    thisarray = arrays[arrname]
    offset = 0 - int(thisarray[0][0])
    actualindex = int(index) + offset
    value = thisarray[1][actualindex]
    print("getArrayIndex",thisarray,actualindex,"--->",value,file=sys.stderr)
    return value

def findValue(expression):
    arrayname = expression.split("[")[0]
    arrayvalue = expression[expression.index("[")+1:expression.rindex("]")]
    answer = 0
    if "[" in arrayvalue: 
        newindex = findValue(arrayvalue)
        answer = getArrayIndex(arrayname,newindex)
    else:
        answer = getArrayIndex(arrayname,arrayvalue)

    print("findValue:",arrayname," get index ",arrayvalue," = ",answer,file=sys.stderr)
    return answer


n = int(input())
arrays = {}
for i in range(n):
    assignment = str(input())
    print(assignment,file=sys.stderr)
    identifier = assignment.split("[",1)[0]
    range = assignment.split("[",1)[1].split("]")[0].split("..")
    values = list(assignment.split("=")[1].strip().split())
    print("Array",identifier," Range:",range," Values:",values, file=sys.stderr, flush=True)
    arrays.update({identifier:[range,values]})

interpret = input()
print("Interpret",interpret, file=sys.stderr, flush=True)

answer = findValue(interpret)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(answer)
