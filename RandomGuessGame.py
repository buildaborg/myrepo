# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:58:22 2022

@author: Steve
"""

import random

secretNumber = random.randint(1, 50)
print('I am thinking of a random number between 1 and 20')

# Ask player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess between 1 and 50')
    guess = int(input())
    
    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break #This condition is the correct guess
        
if guess == secretNumber:
    print("You guessed the correct number! in " + str(guessesTaken) + ' guesses')
else:
    print('You did not guess the correct number which was: ', guessesTaken)