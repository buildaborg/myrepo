# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 20:49:39 2022

@author: mckeo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""
import csv, datetime, calendar
import numpy as np
import matplotlib.pyplot as plt

file2 = 'E:/Downloads/2022Scotia.csv'
file = 'D:/pcbanking2022.csv'
datastorage =[]
date = []
item = []
cost = []
Jan = []; Feb =[] ; Mar =[] ; Apr = [] ; May =[]; Jun = []; Jul = []; Aug = []; Sep =[]
Oct = []
Nov = []
Dec = []
allMonths = []
CatSplitStorage = []


months = {}
allExpensesByMonth = {}
for x in range(1,13):
    month = str(x)
    print(calendar.month_abbr[x])
    val = calendar.month_abbr[x]
    currentval = val
    months[month] = val
    allExpensesByMonth[val] = []

grocerylist = ['hyska', "steven & julie's", 'pc express','food basics','mapleside']
takeoutlist = ['mcdonald',"wendy's",'hortons','dairy queen','starbucks','grill',
               'little caesars',"kelsey",'zaffran','mount molson','pho','aramark',
               'mcgees','dominos','subway','nelson street pub','boston pizza',
               'valleysmoke', 'fijisan', 'a & w']
hardwarelist = ['cdn tire','rona','home harware','peaveymart','home depot']
reclist = ['mecp','hugli','starz in motion','prohockeylife','ticketmaster']
householdlist = ['costco','amazon',"hubert's",'wal-mart','dollarama','amzn','shoppers','looking glass','siegel','rexall',"mac's"]
gaslist = ['mrgas','ultramar','shell','esso']
vehiclecat = ['autoparts','mto']
subscriptionList = ['google','disney','globe and mail','siriusxm','spotify']
dogList = ['animal hosp']
boozeList = ['beer store','lcbo']
clothingList = ['oshkosh','calikids','sport chek']
schoolStuff = ['rcdsb','well.ca']

rowcount = 0
colcount = 0


with open(file, newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        if [True for x in grocerylist if x in row[1].lower()]: #('hyska' or "steven & julie's" or 'pc express') in row[1].lower():
            row.append('Grocery')
        elif [True for x in takeoutlist if x in row[1].lower()]:
            row.append('Take-out')
        elif [True for x in hardwarelist if x in row[1].lower()]:
            row.append('Hardware Store')
        elif [True for x in reclist if x in row[1].lower()]:
            row.append('Recreation')
        elif [True for x in householdlist if x in row[1].lower()]:
            row.append('Household')
        elif [True for x in gaslist if x in row[1].lower()]:
            row.append('Gas')
        elif [True for x in vehiclecat if x in row[1].lower()]:
            row.append('Vehicle')
        elif 'CIBC' in row[1]:
            continue
            #row.append('Payment')
        elif [True for x in boozeList if x in row[1].lower()]:
            row.append('Booze')
        elif [True for x in subscriptionList if x in row[1].lower()]:
            row.append('Subscriptions')
        elif [True for x in dogList if x in row[1].lower()]:
            row.append('Vet Bills')
        elif [True for x in clothingList if x in row[1].lower()]:
            row.append('Clothing')
        elif [True for x in schoolStuff if x in row[1].lower()]:
            row.append('School-related')
        elif 'cogeco' in row[1].lower():
            row.append('Internet')
        else:
            row.append('Uncategorized')
        category = row[3]
        #removing negative
        absoluteval = abs(float(row[2]))
        row[2] = absoluteval
        #print(row)
        #print(row[2])
        datastorage.append(row)
        if row[3] == 'Uncategorized' :
            print(row[1] , row[2], 'Unclassified')
        
        #determine month
        adate = datastorage[rowcount][0]
        datest = datetime.datetime.strptime(adate,"%m/%d/%Y")
        #print(datest)

        #append to correct month
        #append row values to allExpensesByMonth Dict
        targetMonth = months[str(datest.month)]
        #print(targetMonth)
        allExpensesByMonth[targetMonth] = allExpensesByMonth[targetMonth] + [row]
        CatSplit = row[1].split()
        temp = len(CatSplit)
        for y in range(0,temp):
            CatSplitCheck = []
                
            CatSplitStorage.append(CatSplit)
        
        rowcount += 1
                                            
    
    print(f"There are {rowcount +1} rows in this file")
    
ExpenseSummaryByMonth = {}
ExpenseSummaryByStore = {}
#Function to determine total value for each category by month
def sumMonth(monthlysummary):
    storageDict = {}
    storeDict = {}
    for x in monthlysummary:
        #print(x[3])
        if x[3] not in storageDict:
            storageDict.setdefault(x[3],x[2])
        else:
           currentval = storageDict[x[3]]
           storageDict[x[3]] = round(x[2] + currentval, 2)
           
    for b in monthlysummary:
        if b[1] not in storeDict:
            storeDict.setdefault(b[1],b[2])
        else:
            expense = storeDict[b[1]]
            storeDict[b[1]] = round(b[2] + expense, 2)

    ExpenseSummaryByMonth[k] = storageDict
    ExpenseSummaryByStore[k] = storeDict 
    if len(ExpenseSummaryByMonth[k]) > 0:
        print(f'Monthly expenses for SumMonth: {months[str(k)]}')
        #@todo sort alphabetically first
        sortedvals = sorted(list(ExpenseSummaryByMonth[k].keys()))

        #for g, h in storageDict.items():

            #print(g, ':', h)
        #print('\n\n\n')
        
        #print summary fo expenses for each store
        #for n, m in storeDict.items():
            #print(n, ':', m)
        #print('\n\n\n')
        for v in sortedvals:
            print(v, ': $' + str(ExpenseSummaryByMonth[k][v]))
        print('\n')
            #print(v, ':', ExpenseSummaryByMonth[v])
       

for k in months:
    sumMonth(allExpensesByMonth[months[k]])
#create plots



#create list from dict
forGraphing = ExpenseSummaryByMonth['8']
listGraph = forGraphing.keys()
#print(listGraph)
graphlist = []
graphlist2 = []
valuesOnly = []
keysOnly= []

for c in listGraph:
    if c != 'Payment':    
        keysOnly.append(c)
        graphlist.append([c, forGraphing[c] ])
        valuesOnly.append(forGraphing[c])
        graphlist2.append(([c],[forGraphing[c]]))
    else:
        continue
        #graphlist.append(str(c))
        #graphlist.append(forGraphing[c])
#print(graphlist)


data1 = valuesOnly
arr1 = np.array(data1)
arr2 = np.empty((4,3))
plt.pie(valuesOnly, labels = graphlist, autopct='%.2f')



#plt.pie(valuesOnly)
def SummaryL(SearchID, MthList):
    print('ghg')
    for x in MthList:
        print(MthList)
        if str(MthList[x][3]) in SearchID:
            print(MthList)
        else:
            continue
#SummaryL(1,forGraphing)            