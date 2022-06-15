#
import copy
WIDTH = 6
LENGTH = 9

def commaCode():
    emptyList = []
    for x in range(WIDTH):
        column = []
        for y in range(LENGTH):
            column.append('o')
            #print(column)

        emptyList.append(column)
    print(emptyList)
    newList = copy.deepcopy(emptyList)
    
    for y in range(LENGTH):
        print('\n')
        for x in range(WIDTH):
            print(newList[x][y], end ='')

        
        
commaCode()
"""     
   thelist = ['one', 'two', 'three']
commaCode(thelist)
emptyList = []
commaCode(emptyList)
commaCode(list(input()))

newlist = copy.copy(thelist)

print(newlist)

"""