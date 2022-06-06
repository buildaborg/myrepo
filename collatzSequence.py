# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:36:21 2022

@author: mckeo
"""

def collatz(number):
    numberEntered = number
    print('Starting number is %s' % number)
    while numberEntered != 1:
        if number % 2 == 0 and number != 1:
            number = number // 2
            print(f'The current number is: {number}')
            
        elif number % 2 == 1 and number != 1:
            number = 3 * number + 1
            print(f'The current number is: {number}')

def userInput():
    try:
        numb = input('Enter a number')
        collatz(int(numb))
    except ValueError:
        print('Enter a real number')
        userInput()
        
userInput()