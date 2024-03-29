import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rules = {
    1:[1,2,4,5],
    2:[1,2,3],
    3:[2,3,5,6],
    4:[1,4,7],
    5:[2,4,5,6,8],
    6:[3,6,9],
    7:[4,5,7,8],
    8:[7,8,9],
    9:[5,6,8,9]
}

def reverse(button):
    button = int(button)-1
    initial = keypad[button]
    keypad[button]=not(keypad[button])
    print("Toggle:",button+1,initial,">",keypad[button], file=sys.stderr, flush=True)


def press(button):
    toggle = rules[int(button)]
    print("Pressing",button,toggle, file=sys.stderr, flush=True)    
    for button in toggle:
        reverse(button)
    return toSolved()    

def toSolved():
    solved = [True,True,True,True,False,True,True,True,True]
    mismatch = []
    for button in range(len(solved)):
        if not(solved[button] == keypad[button]):
            mismatch.extend([int(button+1)])
    return mismatch


# read initial button state and store
keypad = []
board = str(input())+str(input())+str(input())
for button in board.replace(" ",""):
    if button=='*': keypad.extend([True])
    else: keypad.extend([False])
    
print("Starting keypad:",keypad, file=sys.stderr, flush=True)
all_buttons_pressed = input()
unsolved = []
for key in all_buttons_pressed:
    unsolved = press(key)
    print("Unsolved buttons:",unsolved, file=sys.stderr, flush=True)
print("Current keypad:",keypad, file=sys.stderr, flush=True)

# which button will toggle the proper buttons?
answer = ""
for rule in rules.keys():
    print(">",str(rule),rules[rule], file=sys.stderr, flush=True)
    if unsolved == rules[rule]:
        print(str(rule))

