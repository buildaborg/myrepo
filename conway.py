# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:42:01 2022

@author: Steve
"""

# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #create a column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
            
    nextCells.append(column) # nextCells is a list of colum lists
    
while True: #main rpogram loop
    print('\n\n\n\n\n') # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    
    #print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end ='')
        print() # Print a newline at the end of the row
        
    # Calculate the next step's cells absed on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Gets neighbouring doordinates
            # '% WIDTH' esnures leftCoord is always between 0 and 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = ( y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            
            #Count  number of living neighbours
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # top left neighbour is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 # Top neighbour is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours[leftCoord][y] == '#' # top right neighbour is alive
            
                