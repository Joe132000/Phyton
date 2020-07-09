# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:40:17 2020

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
        return 50 

def dayOfYear(year,month,day):
    days=month*30
    dtrans=daysInMonth(year,month)-day
    if month==1:
        days+=1
        days-=dtrans     
    elif year%4==0 and year%100!=0 and month!=1 or year%400==0:
        days-=1
    else:
        days-=2     
    if month==2:
        days+=1
        days-=dtrans
    elif month==3:
        days+=2
        days-=dtrans
    elif month==4:
        days+=2
        days-=dtrans
    elif month==5:
        days+=3
        days-=dtrans
    elif month==6:
        days+=3
        days-=dtrans
    elif month==7:
        days+=4
        days-=dtrans
    elif month==8:
        days+=5
        days-=dtrans
    elif month==9:
        days+=5
        days-=dtrans
    elif month==10:
        days+=6
        days-=dtrans
    elif month==11:
        days+=6
        days-=dtrans
    elif month==12:
        days+=7
        days-=dtrans
    else:
        return None
    while year<0 or month<1 or month>12 or day>31 or day<1:
        print('un dato ingresado es incorrecto')
        break
    else:
        return days
    
print(dayOfYear(2020,12,31)) 
