import string
import random
import pprint

chessBoard = {}

allLetters = string.ascii_lowercase
#print(allLetters)
letters = list(allLetters)
boardLetters = letters[0:8]

# create board
for x in range(8):
    #print(x + 1)
    for l in range(8):
        #print(chessBoard[str(x) + boardLetters[x] + ':' + '' + ','])
        chessBoard[boardLetters[l] + str(x)] = ' '
    
maxPieces = { 'bpawn' : 8,
             'wpawn' : 8,
             'wknight' : 2,
             'bknight' : 2,
             'bking' : 1,
             'wking' : 1,
             'wrook' : 2,
             'brook' : 2,
             'wqueen' : 1,
             'bqueen' : 1,
             'wbishop' : 2,
             'bbishop' : 2}


#chess pieces
chessPieces = ['pawn', 'knight', 'king', 'rook', 'queen', 'bishop']
allPieces = []
#dictPieces = {}

#create a full set of pieces
for c in range(len(chessPieces)):
    print(c)
    if chessPieces[c] == 'pawn':
        for x in range(8):
            allPieces.append('w' + chessPieces[c])
            allPieces.append('b' + chessPieces[c])
    elif chessPieces[c] == 'knight' or chessPieces[c] == 'rook' or chessPieces[c] == 'bishop':
        for x in range(2):
            allPieces.append('w' + chessPieces[c])
            allPieces.append('b' + chessPieces[c])
    else:        
        allPieces.append('w' + chessPieces[c])
        allPieces.append('b' + chessPieces[c])


print(allPieces)
ListOfBoardPositions = list(chessBoard.keys())

#generate a random board one piece of each
for b in range(len(allPieces)):
    randNum = random.randint(0,64)
    #print(randNum)
    #print(ListOfBoardPositions[b])
    #print(ListOfBoardPositions[random.randint(0,64)])
    chessBoard[ListOfBoardPositions[random.randint(0,63)]] = allPieces[b]
    #print(allPieces[b])
    #chessBoard[ListOfBoardPositions[random.randint(0,64)]] = allPieces(b)
    #print(random.randint(0,64))


pprint.pprint(chessBoard)
'''
# Verification of board location and piece
while True:
    print('What piece would you like to move? (Press Enter to quit')
    thePiece = input('> ')
    
    ## 'testing IN'
    if thePiece == '':
        break
    if thePiece not in allPieces:
        print('Invalid entry, please choose a valid piece')
    if thePiece in allPieces:
        print('Where would you like to move the piece from?')
        boardOrigin = input('>')
        if boardOrigin in chessBoard.keys():
            chessBoard[boardOrigin] = ' '
        if boardOrigin not in chessBoard.keys():
            print('That is not a valid location')
        print('Where would you like to move the piece?')
        boardDestination = input('>')
        if boardDestination in chessBoard.keys():
            print(f'You have moved {thePiece} to {boardDestination}')
            #update chess board
            chessBoard[boardDestination] = thePiece
            print(chessBoard)
        if boardDestination not in chessBoard.keys():
            print('That is not a valid location')
'''
# add code to check whether location piece is being moved from currently has that piece
def checkBoard(boardDict):
    numOfPieces = 0
    for l in boardDict.values():
        #print(l)
        numOfPieces = numOfPieces + boardDict.get(l, 0)
        return numOfPieces

dictPieceCount = {}
cbVals = list(chessBoard.values())
print('The count:')
print(cbVals)

#Counting the number of pieces on the board
#def CheckPieces(allPotentialPieces, boardDictionary)
for x in allPieces:
    count = 0
    for c in chessBoard.values():
        #print(x)
        if x == c:
            count = count + 1
            #print(f"{x} : {count}")
            dictPieceCount[x] = count


#check if too many pieces

for v in maxPieces:
    print(v)
    if dictPieceCount.get(v, 0) > maxPieces[v]:
        print(f'Too many {v} pieces on the board!')
        break
    else:
        print('all good!')

    
pprint.pprint(dictPieceCount)
       # print(c)
        #valcount = operator.countOf(allPieces[x], chessBoard.values())
        #print(f"{c} : {valcount} xxx")
    
        #valcount = operator.countOf(allPieces[x], chessBoard.values())
        #print(f"{x} : {valcount} bbb")
    #print(count)
#checkBoard(chessBoard)
        