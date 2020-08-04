# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:57:20 2020

@author: JOSEPH
"""

print('-- ANÁLISIS DE TEMPERATURA DEL AGUA --\n')
length=int(input('Ingrese cantidad de temperaturas [1,10]: '))
matrix=[]
matrix2=[]
g=0
l=0
s=0
cont=0
suma=0
suma2=0
while length<1 or length>10:
    print('\nEl valor debe ser entre 1 y 10')
    length=int(input('Ingrese cantidad de temperaturas [1,10]: '))
if length>=1 and length<=10:
    for i in range(1,length+1):
        print('Temperatura ',i,' en °C:')
        x=int(input())
        matrix.append(x)
        cont+=1
    for j in range(0,length):
        if matrix[j]>=100:
            g+=1
        if matrix[j]>1 and matrix[j]<100:
            l+=1
        if matrix[j]<=0:
            s+=1
    print('RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA')
    print('Cantidad de muestras sólidas:',s)
    print('Cantidad de muestras líquidas:',l)
    print('Cantidad de muestras gaseosas:',g)
    for r in range(0,length):
        suma+=matrix[r]
    promedio=suma/cont
    print('Temperatura Promedio °C: ',promedio)
    for t in range(0,length):
        faren=(matrix[t]*1.8)+32
        matrix2.append(faren)
    for u in range(0,length):
        suma2+=matrix2[u]
    promedio2=suma2/cont
    print('Temperatura Promedio °F: ',promedio2)