import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

signalin = int(input())
signalout = int(input())

inputs = {}
for i in range(signalin):
    input_name, input_signal = input().split()
    inputs.update({input_name:input_signal})

print("Input:", inputs,file=sys.stderr, flush=True)

outputs = []
for i in range(signalout):
    output_name, operation, input_name_1, input_name_2 = input().split()
    signal1 = str(inputs.get(input_name_1))
    signal2 = str(inputs.get(input_name_2))
    result = ""
    for c in range(len(signal1)) :
        b1 = True if signal1[c]=="-" else False
        b2 = True if signal2[c]=="-" else False

        b = False
        if (operation == "AND"):
            b = b1 and b2
        elif (operation == "OR"):
            b = b1 or b2
        elif (operation == "XOR"):
            b = b1 != b2
        elif (operation == "NAND"):
            b = not(b1 and b2)
        elif (operation == "NOR"):
            b = not(b1 or b2)
        elif (operation == "NXOR"):    
            b = not(b1 != b2)

        result += "-" if b else "_"

    print(output_name,result)
