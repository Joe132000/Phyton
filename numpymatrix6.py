# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:35 2020

@author: JOSEPH
"""

matrix=[[0,0,0,0],[0,0,0,0],
       [0,0,0,0],[0,0,0,0],]

for i in range(0,3):
    for n in range(0,3):
        print('Ingrese la posicion',i,n,': ')
        matrix[i][n]=int(input())
print(matrix)

for j in range(0,3):
    for m in range(0,3):
        print(matrix[j][m])