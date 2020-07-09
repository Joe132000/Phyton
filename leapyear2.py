# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:16:50 2020

@author: JOSEPH
"""

def isYearLeap(year):
    if  year%4==0 and  year%100!=0 or year%400==0:
        return True
    else:
        return False

def daysInMonth(year,month):
    if isYearLeap(year) and month==2:
        return 29  
    elif  month==2:
        return 28      
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return None 

print(daysInMonth(1900,2))


