# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""
import csv, datetime, calendar
import numpy as np

outputFile2 = 'S:/Python/CSVTest.csv'
file2 = 'E:/Downloads/pcbanking2022.csv'
outputFile = 'D:/CSVTest.csv'
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

months = {}
allExpensesByMonth = {}
for x in range(1,13):
    month = str(x)
    #print(calendar.month_abbr[x])
    val = calendar.month_abbr[x]
    currentval = val
    months[month] = val
    allExpensesByMonth[val] = []

grocerylist = ['hyska', "steven & julie's", 'pc express','food basics','mapleside', 'bulk barn', 'costco']
takeoutlist = ['mcdonald',"wendy's",'hortons','dairy queen','starbucks','grill',
               'little caesars',"kelsey",'zaffran','mount molson','pho','aramark',
               'mcgees','dominos','subway','nelson street pub','boston pizza','valleysmoke',
               'skipthedishes', 'thai', 'a & w', 'fijisan', 'j  es', 'swiss chalet', 'milano']
hardwarelist = ['cdn tire','rona','home harware','peaveymart','home depot','canadiantire', 'lee valley']
reclist = ['mecp','hugli','starz in motion','prohockeylife','ticketmaster', 'ripleys','town of petawawa', 'museum']
householdlist = ['amazon',"hubert's",'wal-mart','dollarama','amzn','shoppers','looking glass','siegel','rexall',"mac's",'indigo','value village', 'mckie']
gaslist = ['mrgas','ultramar','shell','esso', 'petrocan','hamilton convenience']
vehiclecat = ['autoparts','mto', 'line-x', 'murphy ford', 'true-centre']
subscriptionList = ['google','disney','globe and mail','siriusxm','spotify','the athletic']
dogList = ['animal hosp', 'petsmart', 'bright eyes']
boozeList = ['beer store','lcbo', 'dog house']
clothingList = ['oshkosh','calikids','sportchek', 'decathlon', 'sport chek']
schoolStuff = ['rcdsb','well.ca','teacherspayteachers', 'canva']

rowcount = 0
colcount = 0

#Assigns category to expense and 
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
            row.append('Dog Bills')
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
        #adds row to datastorage file
        datastorage.append(row)
        if row[3] == 'Uncategorized' :
            print(row[1], '- ', row[2],'- ', row[0],'- ', row[3])
        
        #determine month
        adate = datastorage[rowcount][0]
        datestring = datetime.datetime.strptime(adate,"%m/%d/%Y")
        #append to correct month
        #for x in months:
            #print('MONTH')
            #print(months[str(x)]) # prints month string
            #print(str(v))
        ## THIS BLOCK IS ANTIQUATED
        if datestring.month == 7:
            Jul.append(row)
        if datestring.month == 8:
            Aug.append(row)
        if datestring.month == 6:
            Jun.append(row)
        
      
        
        rowcount += 1
        ##


        
        ###append row values to allExpensesByMonth Dict
        targetMonth = months[str(datestring.month)]
        allExpensesByMonth[targetMonth] = allExpensesByMonth[targetMonth] + [row]
      #saving each expense to CSV file
    CSV = open(outputFile, 'w', newline = '')
    
    writer = csv.writer(CSV)

    writer.writerows(datastorage)
    CSV.close()
                  
    print(f"There are {rowcount +1} rows in this file")

#function to split and match similar entries
splitclass = []
cnt = 0
cellLength = 0
splitList = []
for x in datastorage:

    ds = enumerate(datastorage)

    cellSplit = datastorage[cnt][1].split()
    cellLengthCheck = len(cellSplit)
    #print(x)
    splitclass.append(cellSplit)
    cnt += 1
    '''
    if cellLengthCheck > cellLength:
        cellLength = cellLengthCheck
        print(cellLength)
    else:
        continue
    print(f'Longest cell = {cellLength}')
    '''
#evaluateMatch = []
#for line in range(len(splitclass)):
    #do something
    #print('')
    
   

ExpenseSummaryByMonth = {}

#Function to determine total value for each category by month
#ExpenseSummaryByMonth lists each months total for each category
#identified by month number as the dict key
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
        #print(f'Monthly expenses for: {months[str(k)]}')
        #@todo sort alphabetically first
        sortedvals = sorted(ExpenseSummaryByMonth.keys())
        #for g, h in storageDict.items():

            #print(g, ':', h)
        #print('\n\n\n')

#summarizes how many time a store was visited
#add a line for the total cost for each store


def transaction_summary():
    purchaseSum_dict = {}
    counter = 0
    for x in datastorage:
        targetcell = datastorage[counter][1]
   
        if targetcell not in purchaseSum_dict:
            purchaseSum_dict.setdefault(datastorage[counter][1],1)
            #for testing only
            #if 'AMZN' in targetcell:
                #print(targetcell)
            #else:
                #print('not in target cell')
        else:
            #print(purchaseSum_dict[x[1]])
            purchaseSum_dict[x[1]] = purchaseSum_dict[x[1]] + 1
            #for testing only
            #if 'AMZN' in targetcell:
                #print(targetcell)
            #else:
                #print('not in target cell')
            
        counter += 1   
    #print(purchaseSum_dict)
    #print('TRANSACTION SUMMARY')     
    return purchaseSum_dict
    print(purchaseSum_dict)

transaction_summary()

#prints each months values using sumMonth function
for k in months:
    sumMonth(allExpensesByMonth[months[k]])

#create list from dict
forGraphing = ExpenseSummaryByMonth['7']
listGraph = forGraphing.keys()
#print(listGraph)
graphlist = []

for c in listGraph:
    graphlist.append([c, forGraphing[c] ])
    #graphlist.append(str(c))
    #graphlist.append(forGraphing[c])
#print('Here:')
print(graphlist)

## FUNCTION - to see montly costs and average
'''###
searchval = input('What category did you want? /n')
valsum = 0

for x in ExpenseSummaryByMonth:
    print(months[str(x)] + ': $' + str(ExpenseSummaryByMonth[str(x)][str(searchval)]))
    valsum = valsum + int(ExpenseSummaryByMonth[str(x)][str(searchval)])
averagemonthlySpend = round((valsum / 12),2)
print(f'On average you spend ${averagemonthlySpend} per month on {searchval}')
print(f'You spent ${valsum} on {searchval} in {datestring.year}')
'''
#Function to create Summary - could also have input within fucntion and while loop
def summary_stats(searchval):
    
    valsum = 0
    for x in ExpenseSummaryByMonth:
        ExpenseSummaryByMonth[x].setdefault(searchval, '0')
        print(months[str(x)] + ': $' + str(ExpenseSummaryByMonth[str(x)][str(searchval)]))        
        
        valsum = valsum + int(ExpenseSummaryByMonth[str(x)][str(searchval)])
    averagemonthlySpend = round((valsum / 12),2)
    print(f'On average you spend ${averagemonthlySpend} per month on {searchval}')
    print(f'You spent ${valsum} on {searchval} in {datestring.year}')

#summary_stats(input('What Would you like to search?'))

#listGraph.values()