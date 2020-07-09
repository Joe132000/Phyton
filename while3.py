# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:12:11 2020

@author: JOSEPH
"""

x=input('Ingrese el numero de veces que contare: ',
        'o ingrese q quit para cerrar')

contador=1
while True:
    if x=='q' or x=='quit':
        break
    x=int(x)
    print(contador)
    contador+=1
    if contador>x:
        break
