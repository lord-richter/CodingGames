import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# the cursor is the location of the next character
cursor = 0
output = []

typed_keys = input()

for cin in typed_keys:
    print("'",cin,"'",file=sys.stderr,end='')
    # left ... just move the index
    # only move it if we are not already fully left
    if (cin=="<") and (cursor>0):
        cursor = cursor - 1
    # right ... just move the index    
    # stop at the end of the output so cursor is always the next character
    elif cin==">" and (cursor<len(output)):
        cursor = cursor + 1
    # if this is backspace, delete character to left
    # and move cursor back one. Stop at left bounds.
    elif cin=="-" and (cursor>0):
        # the last character is the one to the left
        cursor = cursor - 1
        # delete that character
        del output[cursor:cursor+1]
    # if not a cursor control, add at cursor, increment cursor
    elif not cin==">" and not cin=="<" and not cin=="-":
        output.insert(cursor,cin)
        cursor = cursor + 1
    
    # all other cases are out of bounds 

    print(output,file=sys.stderr)

# display the output
for cout in output:
    print(cout,end='')
print()    
