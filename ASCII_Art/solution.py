import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

# to make things simpler, get all upper case characters
# and then slap a question mark at the end
# used for index and to validate each character
letters = string.ascii_uppercase + '?'

for i in range(h):
    # this is the list of all ascii character art for the line
    # in alphabetical order
    asciirow = input()

    # break asciirow into a dictionary for each letter and the corresponding ascii string
    artmatrix={letters[int(m/l)]:asciirow[m:m+l] for m in range(0, len(asciirow), l)}

    # loop over each letter in the message
    for character in t:
        # test for unwanted characters and replace with ?
        if not character.upper() in letters:
            character = "?"

        # append the ascii art to the line, do not add newline
        print(str(artmatrix.get(character.upper())),end='')

    # newline to prepare for the next line
    print()

