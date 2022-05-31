import random, sys

print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' (wins, losses, ties))
    while True: #The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of the player input loop.
        print('Type one of r, p, r or q.')
    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus..')
    elif playerMove == 'p':
        print('PAPER versus..')
    elif playerMove == 's':
        print('SCISSORS versus..')
    #Display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')