import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b, c, d = [int(i) for i in input().split()]
n = int(input())
program = []

registers = {
    "a":a,
    "b":b,
    "c":c,
    "d":d
}

for i in range(n):
    instruction = input()
    operation = instruction[0:3]
    data = instruction[4:].split()
    line=[operation,data]
    print(operation,data,line, file=sys.stderr, flush=True)
    program.append(line)

print(program, file=sys.stderr, flush=True)
print(registers, file=sys.stderr, flush=True)
exec=0

# loop until program falls through
while exec<len(program):
    op = program[exec][0]
    data = program[exec][1]
    print(exec,":",op,data, file=sys.stderr, flush=True)
    if op=="MOV":
        exec+=1
        dest = data[0]
        srcimm = data[1]
        if not(srcimm.strip("-+").isnumeric()):
            srcimm=registers[srcimm]
        registers[dest]=int(srcimm)   
        print(int(srcimm),"-> Register",dest,file=sys.stderr) 
    elif op=="ADD":    
        exec+=1
        dest = data[0]
        srcimm1 = data[1]
        if not(srcimm1.strip("-+").isnumeric()):
            srcimm1=registers[srcimm1]
        srcimm2 = data[2]
        if not(srcimm2.strip("-+").isnumeric()):
            srcimm2=registers[srcimm2]
        result=int(srcimm1)+int(srcimm2)    
        registers[dest]=result       
        print(result,"-> Register",dest,file=sys.stderr) 
    elif op=="SUB":
        exec+=1
        dest = data[0]
        srcimm1 = data[1]
        if not(srcimm1.strip("-+").isnumeric()):
            srcimm1=registers[srcimm1]
        srcimm2 = data[2]
        if not(srcimm2.strip("-+").isnumeric()):
            srcimm2=registers[srcimm2]
        result=int(srcimm1)-int(srcimm2)    
        registers[dest]=result       
        print(result,"-> Register",dest,file=sys.stderr) 
    elif op=="JNE":
        exec+=1 # unless other
        jump = int(data[0])
        reg = registers[str(data[1])]
        test = data[2]
        if not(test.strip("-+").isnumeric()):
            test=registers[test]        
        print("JNE",reg,"!=",test,"-->",jump,"else",exec,file=sys.stderr) 
        exec = exec if reg==int(test) else jump
        print("Next line:",exec,file=sys.stderr) 

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(registers['a'],registers['b'],registers['c'],registers['d'])
