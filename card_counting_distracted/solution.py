import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cards = [
    ["K",10,4],
    ["Q",10,4],
    ["J",10,4],
    ["T",10,4],
    ["9",9,4],
    ["8",8,4],
    ["7",7,4],
    ["6",6,4],
    ["5",5,4],
    ["4",4,4],
    ["3",3,4],
    ["2",2,4],
    ["A",1,4]
]

def cardsRemaining():
    count = int(0)
    for card in cards:
        count = count + card[2]
    print("Cards left=",count,file=sys.stderr, flush=True)    
    return count

def validThought(thought):
    valid = True
    for c in thought:
        valid = valid and any(c in cardinfo for cardinfo in cards)
    return valid

def cardDrawn(draw):
    for index in range(len(cards)):
        card = cards[index]
        if draw in card:
            count = cards[index][2]
            if count>0:
                count = count - 1
            cards[index][2]=count
            print("Drawn:",draw,"Left=",count,file=sys.stderr, flush=True)



thoughts = str(input()).split(".")
bust_threshold = int(input())

print("Cards:",cards,file=sys.stderr, flush=True)
print("Thoughts:",thoughts,file=sys.stderr, flush=True)

# process thoughts
for thought in thoughts:
    if validThought(thought):
        print("Draws:",thought,file=sys.stderr, flush=True)
        for draw in thought:
            print("Card:",draw,file=sys.stderr, flush=True)
            cardDrawn(draw)
    else:
        print("Distraction:",thought,file=sys.stderr, flush=True)

# wake up and see what is left
remaining = cardsRemaining()

# cound cards within bounds
possible = 0
for card in cards:
    if card[1]<bust_threshold:
        possible = possible + card[2]

# percentage is possible to remaining
percentage = (possible/remaining)*100
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("{0:0.0f}%".format(percentage))
