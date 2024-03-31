import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = int(input())
cheatround = 0
guesslower = 0
guessupper = 101
previous = {}
for round in range(rounds):
    line = input()
    guess = int(line[:line.index(" ")])
    answer = line[line.index(" "):].strip()
    print("Round",round+1,">> Bob: ",guess,">> Alice: ",answer,file=sys.stderr)

    
    if cheatround==0:
        if guess<guesslower or guess>guessupper:
            print(">> Bob is an idiot",file=sys.stderr)

        # easy case, alice sends bob out of bounds
        if (cheatround==0) and  ((guess>=100 and "low" in answer) or (guess<=1 and "high" in answer)):
            print(">> Going out of range",file=sys.stderr)
            cheatround=round+1
            print("Alice cheated in round",cheatround)

        # bob guesses at edge of range and gets pushed to range edge
        if (cheatround==0) and ((guess<=guesslower and "high" in answer) or (guess>=guessupper and "low" in answer)):
            print(">> Going wrong direction",file=sys.stderr)
            cheatround=round+1
            print("Alice cheated in round",cheatround)

        # bob guesses and gets pointed outside of bounds
        if (cheatround==0) and ((guess==guesslower+1 and "high" in answer) or (guess==guessupper-1 and "low" in answer)):
            print(">> Going to a boundry",file=sys.stderr)
            cheatround=round+1
            print("Alice cheated in round",cheatround)


        # out of bounds right answer
        if (cheatround==0) and ((guess<guesslower or guess>guessupper)) and "right" in answer:
            print(">> Correct answer was out of bounds",file=sys.stderr)
            cheatround=round+1
            print("Alice cheated in round",cheatround)

        # alice gave different answers to same guess
        if (cheatround==0) and (guess in previous) and not(previous[guess]==answer):
            print(">> Different answer to same guess",file=sys.stderr)
            cheatround=round+1
            print("Alice cheated in round",cheatround)
            
        # bob gets it right    
        if (cheatround==0) and "right" in answer:
            print(">> Correct answer was in bounds",file=sys.stderr)

        if (cheatround==0) and not("right" in answer):
            print(">> No cheating detected, establish new bounds",file=sys.stderr)
            # set new upper and lower bounds
            guessupper = min(101,guessupper,guess) if "high" in answer else guessupper
            guesslower = max(0,guesslower,guess) if "low" in answer else guesslower
            print("Range >>",guesslower,"to",guessupper,file=sys.stderr)
            previous.update({guess:answer})

            # nowhere to go?
            if (guessupper<=guesslower):
                print(">> Ran out of space to guess",file=sys.stderr)
                cheatround=round+1
                print("Alice cheated in round",cheatround)




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if cheatround==0:
    print("No evidence of cheating")

