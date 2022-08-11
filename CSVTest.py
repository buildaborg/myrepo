# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""
import csv, datetime,calendar

file2 = 'E:/Downloads/2022Scotia.csv'
file = 'D:/pcbanking5.csv'
datastorage =[]
date = []
item = []
cost = []
Jan = []; Feb =[] ; Mar =[] ; Apr = [] ; May =[]; Jun = []; Jul = []; Aug = []; Sep =[]
Oct = []
Nov = []
Dec = []
allMonths = []

months = {}
allExpensesByMonth = {}
for x in range(1,13):
    month = str(x)
    #print(calendar.month_abbr[x])
    val = calendar.month_abbr[x]
    currentval = val
    months[month] = val
    allExpensesByMonth[val] = []

grocerylist = ['hyska', "steven & julie's", 'pc express','food basics','mapleside']
takeoutlist = ['mcdonald',"wendy's",'hortons','dairy queen','starbucks','grill',
               'little caesars',"kelsey",'zaffran','mount molson','pho','aramark',
               'mcgees','dominos','subway','nelson street pub','boston pizza','valleysmoke']
hardwarelist = ['cdn tire','rona','home harware','peaveymart','home depot']
reclist = ['mecp','hugli','starz in motion','prohockeylife','ticketmaster']
householdlist = ['amazon',"hubert's",'wal-mart','dollarama','amzn','shoppers','looking glass','siegel','rexall',"mac's"]
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
            row.append('Payment')
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
        cat = row[3]
        absoluteval = abs(float(row[2]))
        row[2] = absoluteval
        #print(row[2])
        datastorage.append(row)
        if row[3] == 'Uncategorized' :
            print(row[1] , row[2])
        
        #determine month
        adate = datastorage[rowcount][0]
        datest = datetime.datetime.strptime(adate,"%m/%d/%Y")
        #append to correct month
        #for x in months:
            #print('MONTH')
            #print(months[str(x)]) # prints month string
            #print(str(v))
        
        if datest.month == 7:
            Jul.append(row)
        if datest.month == 8:
            Aug.append(row)
        if datest.month == 6:
            Jun.append(row)
        rowcount += 1
        #for x in
        #append row values to allExpensesByMonth Dict
        targetMonth = months[str(datest.month)]
        allExpensesByMonth[targetMonth] = allExpensesByMonth[targetMonth] + [row]

                                            
    print(f"There are {rowcount +1} rows in this file")
ExpenseSummaryByMonth = {}
#Function to determine total value for each category by month
def sumMonth(monthlysummary):
    storageDict = {}
    for x in monthlysummary:
        #print(x[3])
        if x[3] not in storageDict:
            storageDict.setdefault(x[3],x[2])
        else:
           currentval = storageDict[x[3]]
           storageDict[x[3]] = round(x[2] + currentval, 2)
    ExpenseSummaryByMonth[k] = storageDict
    if len(ExpenseSummaryByMonth[k]) > 0:
        print(f'Monthly expenses for: {months[str(k)]}')
        #@todo sort alphabetically first
        sortedvals = sorted(ExpenseSummaryByMonth.keys())
        for g, h in storageDict.items():

            print(g, ':', h)
        print('\n\n\n')


#sumMonth(Jun)
#sumMonth(Jul)
for k in months:
    sumMonth(allExpensesByMonth[months[k]])

#create list from dict
forGraphing = ExpenseSummaryByMonth['7']
listGraph = forGraphing.keys()
print(listGraph)
graphlist = []

for c in listGraph:
    graphlist.append([c, forGraphing[c] ])
    #graphlist.append(str(c))
    #graphlist.append(forGraphing[c])
print(graphlist)

listGraph.values()