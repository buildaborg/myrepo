# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:10:34 2022

@author: mckeo
"""

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid arguement')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
