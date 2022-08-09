# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""
import csv, datetime,calendar

file2 = 'E:/Downloads/pcbanking7.csv'
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
MonthlySum = {}
for x in range(1,13):
    month = str(x)
    #print(calendar.month_abbr[x])
    val = calendar.month_abbr[x]
    currentval = val
    months[month] = val
    MonthlySum[val] = []

grocerylist = ['hyska', "steven & julie's", 'pc express']
takeoutlist = ['mcdonald',"wendy's",'hortons','dairy queen','starbucks','grill','little caesars',"kelseys"]
hardwarelist = ['cdn tire','rona','home harware']
reclist = ['mecp','hugli']
householdlist = ["hubert's",'wal-mart','dollarama','amzn','shoppers','looking glass','siegel']
gaslist = ['mrgas','ultramar','shell']
vehiclecat = ['autoparts']
subscriptionList = ['google','disney','globe and mail']
dogList = ['animal hosp']
boozeList = ['beer store','lcbo']

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
        elif 'autoparts' in row[1].lower():
            row.append('Vehicle')
        elif 'CIBC' in row[1]:
            row.append('Payment')
        elif [True for x in boozeList if x in row[1].lower()]:
            row.append('Booze')
        elif [True for x in subscriptionList if x in row[1].lower()]:
            row.append('Subscriptions')
        elif [True for x in dogList if x in row[1].lower()]:
            row.append('Vet Bills')
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
            print(row[1])
        
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
        #append row values to MonthlySum Dict
        targetMonth = months[str(datest.month)]
        MonthlySum[targetMonth] = MonthlySum[targetMonth] + [row]

                                            
    print(f"There are {rowcount +1} rows in this file")

#Function to determine total value for each category by month
def sumMonth(monthlysummary):
    storageDict = {}
    for x in monthlysummary:
        #print(x[3])
        if x[3] not in storageDict:
            storageDict.setdefault(x[3],x[2])
        else:
           currentval = storageDict[x[3]]
           storageDict[x[3]] = x[2] + currentval
    #print('Monthly expenses for:')
    #print(storageDict)


sumMonth(Jun)
sumMonth(Jul)


    