# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:48:00 2020

@author: JOSEPH
"""
import numpy as np

filas=int(input("Ingrese el numero de filas de su matriz: "))
columnas=int(input("Ingrese el numero de columnas de su matriz: "))
matrix=np.zeros((columnas,filas))
m=-1
s=-1
x=filas
v=filas
for i in range(0,columnas):
    for n in range(0,filas):
        print('Ingrese la posicion',i,n,': ')
        matrix[i][n]=float(input())
print('\nSu matriz es: ')
print(matrix,'\n')
print('El valor de la diagonal principal de la matriz es: \n')
for j in range(0,filas):
    if m<filas:
        m+=1
        x-=1
    print(' |-|'*m, matrix[j][m] ,'|-| '*x)
    
print('\nEl valor de la diagonal secundaria de la matriz es: \n')
for k in range(0,filas):
    if s<filas:
        s+=1
        v-=1
    print(' |-|'*v, matrix[k][v] ,'|-| '*s)

input('presione enter para terminar el programa: ')