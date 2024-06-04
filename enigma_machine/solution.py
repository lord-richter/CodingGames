import sys
import math
import string

operation = input()

encode = True if operation=="ENCODE" else False

starting_shift = int(input())
print(starting_shift,file=sys.stderr)

rotor = []
for i in range(3):
    j = input()
    rotor.append([j])



message = input()

alphabet = string.ascii_uppercase


print(alphabet,rotor,file=sys.stderr)

#message = "KQF"
#encode = False

shift = 0 

crypt=""
for letter in message:

    print(shift,letter,file=sys.stderr,end="")

    if encode:
        enigma = alphabet.index(letter.upper())
        print("",enigma,file=sys.stderr,end="")

        enigma = enigma + starting_shift + shift
        while enigma>=26: enigma = enigma - 26
        shift = shift + 1
        print("(",enigma,alphabet[enigma],")",file=sys.stderr,end="") 
        for r in (rotor if encode else reversed(rotor)):
            enigma = alphabet.index(r[0][enigma])
            print("(",enigma,alphabet[enigma],")",file=sys.stderr,end="")        
    else:
        enigma = alphabet.index(letter.upper())
        print("",enigma,file=sys.stderr,end="")

        for r in (rotor if encode else reversed(rotor)):
            enigma = r[0].index(alphabet[enigma])
            print("(",enigma,alphabet[enigma],")",file=sys.stderr,end="")

        enigma = enigma - starting_shift - shift
        while enigma<0: enigma = enigma + 26
        shift = shift + 1
        print("",enigma,file=sys.stderr,end="")


    crypt = crypt + alphabet[enigma]
    print("",alphabet[enigma],file=sys.stderr)

print(crypt)    