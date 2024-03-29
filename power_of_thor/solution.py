import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# current_tx: Thor's starting and current X position
# current_ty: Thor's starting and current Y position
light_x, light_y, current_tx, current_ty = [int(i) for i in input().split()]
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # clear direction for each loop
    direction = ""

    # Assign N and S first, to build proper string
    # If directly N or S, then this gets skipped
    # update the current location
    # bounds check to ensure staying within the area
    if light_y>current_ty:
        direction += "S"
        current_ty = min(39,current_ty + 1)
    elif light_y<current_ty :
        direction += "N"
        current_ty = max(0,current_ty - 1)

    # Assign E and W second, to build proper string
    # If directly E or W, then this gets skipped
    if light_x>current_tx :
        direction += "E"
        current_tx = min(17,current_tx+1)
    elif light_x<current_tx :
        direction += "W"
        current_tx = max(0,current_tx+1)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
