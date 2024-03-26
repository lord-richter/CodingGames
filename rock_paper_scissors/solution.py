import sys
import math

victory = {
    "R":{"L","C"},
    "P":{"R","S"},
    "C":{"P","L"},
    "L":{"S","P"},
    "S":{"C","R"}
}

def contest(player1,player2):
    winner = []
    loser = []

    pick1 = player1[1]
    pick2 = player2[1]

    p1victory = victory[pick1]

    print("FIGHT!  Player 1",player1,"Player 2",player2,"Victory",p1victory, file=sys.stderr, flush=True)
    if pick1==pick2:
        # tie, lower number wins
        if player1[0]<player2[0]:
            winner=player1
            loser=player2
        else:
            winner=player2
            loser=player1

    elif pick2 in p1victory:
        winner=player1
        loser=player2

    else:    
        winner=player2
        loser=player1

    
    winner[2].append(loser[0])
    print("WINDER!", winner, file=sys.stderr, flush=True)
    return winner

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
numplayers = int(input())
players=[]
matches=[[]]

for i in range(numplayers):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    player=[numplayer,signplayer,[]]
    matches[0].append(player)

round=0
matchplayers = matches[round]
matchplayersnum = len(matchplayers)
while matchplayersnum>1:
    print("Round:",round, matchplayers,file=sys.stderr, flush=True)
    for match in range(0,matchplayersnum,2):
        player1 = matchplayers[match]
        player2 = matchplayers[match+1]
        print("Match:",match,"Player 1",player1[0],"Player 2",player2[0], file=sys.stderr, flush=True)
        winner = contest(player1,player2)
        if round+1 in matches:
            matches[round+1].append(winner)
        else:
            matches.append([])
            matches[round+1].append(winner)
        print("Current next round:",matches[round+1], file=sys.stderr, flush=True)    
    round = round + 1  
    print("Next round:",matches[round], file=sys.stderr, flush=True)   
    matchplayers = matches[round]  
    matchplayersnum = len(matchplayers)

print("Winner:",matches[round], file=sys.stderr, flush=True)   

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(matches[round][0][0])
print(" ".join(map(str,matches[round][0][2])))
