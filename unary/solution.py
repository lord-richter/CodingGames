import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binary=""

for character in message:
    ascii = ord(character)
    binary = binary + "{0:07b}".format(ascii)

# starting values
value = binary[0]
run = 1

encoded = []

# go through remaining values
for position in range(1,len(binary)) :
    bit = binary[position]
    # if run continues, incrment
    if bit==value:
        run = run + 1
    # if run is over, handle and move on    
    else:
        encoded.append(("0" if value=='1' else "00")+" ")
        encoded.append(("0" * run)+" ")
        run=1
        value=bit

# last run of bits
encoded.append(("0" if value=='1' else "00")+" ")
encoded.append(("0" * run))    


print(''.join(encoded))


