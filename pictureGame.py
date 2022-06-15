# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:35:18 2022

@author: Steve
"""
import random

WIDTH = 9
HEIGHT = 5

nextCells = []
for x in range(WIDTH):
    column = [] #create a column
    print('column')
    print(column)
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
            print(column)
        else:
            column.append(' ') # add a dead cell
            print(column)
            
    nextCells.append(column) # nextCells is a list of colum lists
    
print(nextCells)