import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

spreadsheet = []
n = int(input())


# for an argument (1 or 2) get the calculated value of the argument
def getArgValue(arg) :
    #if this is just a number
    if (arg=="_"):
        arg = 0
    elif re.compile("-?[0-9]+").match(arg):
        arg = int(arg)
    # if this is a row reference
    elif re.compile("\$[0-9]+").match(arg):
        row = int(arg[1:])
        # if previously calculated, return value
        if spreadsheet[row][4]:
            arg = spreadsheet[row][3]
        # get the value for the row
        else:
            arg=getValue(row)


    return arg    

def doCalculation(op,a1,a2) :
    print(op,a1,a2,file=sys.stderr,flush=True)
    value = {
        "VALUE":a1,
        "ADD":a1+a2,
        "SUB":a1-a2,
        "MULT":a1*a2
    }[op]
    return value

def getValue(row) :
    # if row has not yet been calculated
    if not(spreadsheet[row][4]):
        a1 = getArgValue(spreadsheet[row][1])
        a2 = getArgValue(spreadsheet[row][2])
        value = doCalculation(spreadsheet[row][0],a1,a2)
        spreadsheet[row] = [spreadsheet[row][0],a1,a2,value,True]
    else:
        value = spreadsheet[row][3]
    return value





# read the spreadsheet

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    spreadsheet.append([operation,arg_1,arg_2,0,False])


# output each row from the spreadsheet
for i in range(n):
    print(getValue(i))
