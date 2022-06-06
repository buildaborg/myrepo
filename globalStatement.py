# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:14:23 2022

@author: Steve
"""

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)