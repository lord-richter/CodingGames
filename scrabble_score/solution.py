import sys
import math

def boardDelta(previous,current):
    result = []
    for h in range(height):
        for w in range(len(previous[h][0])):
            cell1 = previous[h][0][w]
            cell2 = current[h][0][w]
            if cell1!=cell2:
                result.append([h,w])

    print(result,file=sys.stderr)
    return result

def boardBonus(h,w):
    mult = 1
    bonus = 1
    boardcell = board[h][0][w]
    print("(",boardcell,file=sys.stderr,end='')
    if boardcell=="l":
        bonus = 2
    elif boardcell=="L":
        bonus = 3
    elif boardcell=="w":
        mult = 2
    elif boardcell=="W":
        mult = 3
    print("",bonus,mult,")",file=sys.stderr,end='')    
    return bonus,mult

def findWords(previous,current,h,w):
    wordlist = []
    
    # left/right
    if ((w-1>=0 and current_board[h][0][w-1]!=".") or (w+1<width and current_board[h][0][w+1]!=".")):
        print("Word in Row ",h,file=sys.stderr)
        # find start of word
        pos = w
        wordstart = w
        while pos>=0 and current_board[h][0][pos]!=".":
            wordstart=pos
            pos = pos - 1
        # read word to end
        pos = wordstart
        mult = 1
        word = ""
        score = 0
        while pos<width and current_board[h][0][pos]!=".":
            letter = str(current_board[h][0][pos])
            letterscore = tiles[letter]
            print(h,'x',pos,letter,"(",letterscore,")",file=sys.stderr,end='') 
            # premium cells
            if previous[h][0][pos]==".":   
                bonus,cellmult = boardBonus(h,pos)
                letterscore = letterscore * bonus
                mult = mult * cellmult
              
            print(" scores:",letterscore,mult,file=sys.stderr)    

            word = word + letter
            score = score + letterscore
            pos=pos+1
        score = score * mult
        wordlist.append([word,score])


    # up/down
    if ((h-1>=0 and current_board[h-1][0][w]!=".") or (h+1<height and current_board[h+1][0][w]!=".")):
        print("Word in Column ",w,file=sys.stderr)    
        # find start of word
        pos = h
        wordstart = h
        while pos>=0 and current_board[pos][0][w]!=".":
            wordstart=pos
            pos = pos - 1
        # read word to end
        pos = wordstart
        mult = 1
        word = ""
        score = 0
        while pos<height and current_board[pos][0][w]!=".":
            letter = str(current_board[pos][0][w])
            letterscore = tiles[letter]
            print(pos,'x',w,letter,"(",letterscore,")",file=sys.stderr,end='')    
            # premium cells
            if previous[pos][0][w]==".":   
                bonus,cellmult = boardBonus(pos,w)
                letterscore = letterscore * bonus
                mult = mult * cellmult
            print(" scores:",letterscore,mult,file=sys.stderr)    
            word = word + letter
            score = score + letterscore
            pos=pos+1
        score = score * mult
        wordlist.append([word,score])        

    print(wordlist,file=sys.stderr)    
    return wordlist


nb_tiles = int(input())  # Number of tiles in the tile set
tiles = {}
for i in range(nb_tiles):
    inputs = input().split()
    character = inputs[0]
    score = int(inputs[1])
    tiles.update({character:score})

width, height = [int(i) for i in input().split()]
board = []
for i in range(height):
    empty_board_row = input()  # Empty board with special cells
    board.append([empty_board_row])
    print(empty_board_row,file=sys.stderr)

print(file=sys.stderr)    

previous_board = []
for i in range(height):
    previous_board_row = input()  # Words already played
    previous_board.append([previous_board_row])
    print(previous_board_row,file=sys.stderr)

print(file=sys.stderr)        

current_board = []
for i in range(height):
    current_board_row = input()  # Words after you play
    current_board.append([current_board_row])
    print(current_board_row,file=sys.stderr)

print(file=sys.stderr)        

# get list of cells that have changed
current_delta = boardDelta(previous_board,current_board)
print("Delta:",current_delta,file=sys.stderr,end='')
print("",len(current_delta),file=sys.stderr)
turn_score = {}
total_score = 0 if len(current_delta)<7 else 50
for h,w in current_delta:
    words_here = findWords(previous_board,current_board,h,w)
    for word,score in words_here:
        if word in turn_score:
            print("Duplicate word:",word,file=sys.stderr)
        else:
            print("New word:",word,score,file=sys.stderr)
            turn_score.update({word:score})
            total_score = total_score + score
            

#sorting
turn_score = sorted(turn_score.items())
print("sorted:",turn_score,file=sys.stderr)
for word,score in turn_score:
    print(word,score)

if len(current_delta)>=7: print("Bonus 50")
print("Total",total_score)
