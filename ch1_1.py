# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:26:43 2022

@author: mckeo
"""

print("Hello")
print("What is your name?")

myName = input()

print("It is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))

print('What is your age?')
myAge = input()
print("You will be " + str(int(myAge)+ 1) + ' in 1 year')