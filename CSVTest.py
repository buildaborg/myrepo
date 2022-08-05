# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""

file2 = 'E:/Downloads/pcbanking7.csv'
file = 'D:/pcbanking5.csv'
datastorage =[]
date = []
item = []
cost = []
jan = []
feb =[]
mar =[]
jun = []
jul = []
aug = []
allMonths = []

grocerylist = ['hyska', "steven & julie's", 'pc express']
takeoutlist = ['mcdonald',"wendy's",'hortons','dairy queen','starbucks','grill','little ceasers']

rowcount = 0
colcount = 0
import csv, datetime

with open(file, newline='') as csvfile:
    #dialectclass = csv.sniffer.sniff(file)
    #print(dialectclass)
    #writer = csv.writer(csvfile, dialect=dialectclass)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        if [True for x in grocerylist if x in row[1].lower()]: #('hyska' or "steven & julie's" or 'pc express') in row[1].lower():
            row.append('Grocery')
            cat = 'Grocery'
        elif [True for x in takeoutlist if x in row[1].lower()]:
            row.append('Take-out')
            cat = 'Take-out'
        elif ('cdn tire' or 'rona' or 'home harware') in row[1].lower():
            row.append('Hardware Store')
            cat = 'Hardware Store'
        elif ('mecp' or 'hugli') in row[1].lower():
            row.append('Recreation')
            cat = 'Recreation'
        elif ('wal-mart' or 'dollarama' or 'amzn' or 'shoppers' or 'looking glass' or 'siegel') in row[1].lower():
            row.append('Household')
            cat = 'Household'
        elif ('ultramar' or 'mrgas' or 'shell') in row[1].lower():
            row.append('Gas')
            cat = 'household'
        elif 'autoparts' in row[1].lower():
            row.append('Vehicle')
            cat = 'vehicle'            
        else:
            row.append('Uncategorized')
            cat = 'uncat'
        #print(row)
        print(row[1])
        print(cat)
        datastorage.append(row)
        
        adate = datastorage[rowcount][0]
        datest = datetime.datetime.strptime(adate,"%m/%d/%Y")
        if datest.month == 7:
            jul.append(row)
        if datest.month == 8:
            aug.append(row)
        if datest.month == 6:
            jun.append(row)
        rowcount += 1
        #for col in row:
         #   print(col + 'colcount')
          #  colcount += 1
           # print(colcount)
                                                    
    print(f"There are {rowcount +1} rows in this file")


