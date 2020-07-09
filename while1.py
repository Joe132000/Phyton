# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:36:52 2020

@author: JOSEPH
"""

dato=int(input('Ingrese el numero de veces que contare: '))
contador=1
acumulador=0
while contador<=dato:
    print(contador,end=' ')
    acumulador+=contador
    contador+=1
    
print('la suma de los numeros es: ',acumulador)
print('el promedio es: 'acumulador/contador())