# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:22:39 2020

@author: JOSEPH
"""
import random
from time import sleep
Listacreada=[]
a=0
n = int(input("Ingrese el tamaño de su matriz: "))

for i in range(n):
    Listacreada.append(random.randint(0,99))
    print('El valor en la posicion ',i+1,'es: ',Listacreada[i])
    sleep(1)
x=Listacreada[:]
for i in range(n):
    x.sort()
    x.reverse()
    print('El valor ordenado en la posicion ',i+1,'es: ',x[i])
    sleep(1)
    
print('La lista creada es: ')    
print('A= ',Listacreada)
Listacreada.sort()
Listacreada.reverse()
print('La lista ordenada de menor a mayo es: ')  
print('A= ',Listacreada)