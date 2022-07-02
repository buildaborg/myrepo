# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 22:00:20 2022

@author: mckeo
"""
#
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
innerList = []
blankList =[]
#Checking the length of each string in list
for li in range(0, len(tableData)):
    
    print(li)
    print('#' * 20)
    tableData[li]
    currentList = tableData[li]
    #return currentList
    for y in range(0, len(currentList)):
        innerList.append(len(currentList[y]))
        print(currentList[y])

maxWidth = max(innerList)
print(maxWidth)
print(f"Blank list: {blankList}")
print(f"innerList: {innerList}")


#printing with adjusted list
for x in range(0, len(tableData)):
   justified = ''
   #print(f"Is this doing anything: str{tableData[x]}.rjust{maxWidth}")
   #print(f'{x} is x')
   sublist = tableData[x]
   #print('\n')
   for y in range(0,len(sublist)):
       #print(f"This is y: {y}")
       listStr = sublist[y]
       rjustStr = listStr.rjust(maxWidth+ 1)
       #print(f'{listStr} is listStr')
       justified += rjustStr
   print(justified)
       

