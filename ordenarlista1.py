# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:18:48 2020

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
    print('El valor ordenado en la posicion ',i+1,'es: ',x[i])
    sleep(1)
    
print('La lista creada es: ')    
print('A= ',Listacreada)
Listacreada.sort()
print('La lista ordenada: ')  
print('A= ',Listacreada)
