import string
chessBoard = {}

allLetters = string.ascii_lowercase
print(allLetters)
letters = list(allLetters)
boardLetters = letters[0:8]

# create board
for x in range(8):
    print(x + 1)
    for l in range(8):
        #print(chessBoard[str(x) + boardLetters[x] + ':' + '' + ','])
        chessBoard[boardLetters[l] + str(x)] = ' '
    

print(chessBoard)
"""
for f, g in chessBoard:
    print(f)
    print(g)
    
for k, v in chessBoard.items():
    num = 0
    print(str(v.get(' ', 0)))
    num = num + v.get(' ', 0)
    print(num)
    
    
    print(str(v))
    #print(str(v.get(chessBoard, v))
    print(chessBoard[str(v)]) 
    print(chessBoard.values())
    print(str(v.get(chessBoard.values())))     
"""

