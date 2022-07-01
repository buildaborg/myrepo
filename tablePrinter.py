# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 22:00:20 2022

@author: mckeo
"""

def tablePrint(inputTable):
    #TODO
    blankList =[]
    for li in range(0, len(inputTable)):
        innerList = []
        print(li)
        print('#' * 20)
        inputTable[li]
        currentList = inputTable[li]
        #return currentList
        for y in currentList:
           innerList.append(len(currentList(y)))
            
        blankList.append(innerList)
    
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#tablePrint(tableData)

blankList =[]
for li in range(0, len(tableData)):
    innerList = []
    print(li)
    print('#' * 20)
    tableData[li]
    currentList = tableData[li]
    #return currentList
    for y in range(0, len(currentList)):
        innerList.append(len(currentList[y]))
            
    blankList.append(innerList)