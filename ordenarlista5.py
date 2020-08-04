# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:02:29 2020

@author: JOSEPH
"""
temp = int()
nombre=str()
lista=[int()for ind0 in range(100)]
print("Ingrese el tamaño del vector: ")
tamaño=int(input())
for i in range(1,tamaño+1):
    print("Ingrese el nombre del estudiante",i) 
    nombre=input()
    lista[i-1]=nombre
    print("El valor en la posicion  ",i,"  es  ", lista[i-1]) 
for j in range(1,tamaño+1):
    for l in range(1,tamaño):
        if lista[l-1]>lista[l]:
            temp = lista[l-1]
            lista[l-1]=lista[l]
            lista[l]=temp
for k in range(1,tamaño+1):
    print("El vector ordenado en la posicion  ",k,"  es ",lista[k-1])