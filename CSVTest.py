# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:17:26 2022

@author: Steve
"""

file = 'E:/Downloads/pcbanking7.csv'
datastorage =[]
date = []
item = []
cost = []
jan = []
feb =[]
mar =[]
allMonths = []


rowcount = 0
colcount = 0
import csv, datetime

with open(file, newline='') as csvfile:
    #dialectclass = csv.sniffer.sniff(file)
    #print(dialectclass)
    #writer = csv.writer(csvfile, dialect=dialectclass)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
        datastorage.append(row)
        
        adate = datastorage[rowcount][0]
        datest = datetime.datetime.strptime(adate,"%m/%d/%Y")
        if datest.month == 1:
            jan.append(row)
        if datest.month == 2:
            feb.append(row)
        rowcount += 1
        for col in row:
            print(col)
            colcount += 1
            print(colcount)
                                                    
    print(f"There are {rowcount +1} rows in this file")


