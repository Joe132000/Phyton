# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:03:11 2020

@author: JOSEPH
"""
from random import randint
from time import sleep
print('''
      Este algoritmo le permitira crear y ordenar una lista de 3 a 30 
      elementos basada en:
      0.Terminar programa
      1. Numeros
      2. Caracteres
      ''')

opcion=int(input('Ingrese el numero de la opcion que desea ejecutar: '))

while opcion!=0:
    if opcion==1:
        temp = int()
        lista=[int()for ind0 in range(100)]
        lenght=int(input("Ingrese el tamaño del vector: "))
        if lenght>=3 and lenght<=30:
            for i in range(1,lenght+1):
                lista[i-1]=randint(0,99)
                print("El valor en la posicion  ",i,"  es  ", lista[i-1]) 
                sleep(1)
            for j in range(1,lenght+1):
               for l in range(1,lenght):
                   if lista[l-1]<lista[l]:
                       temp = lista[l-1]
                       lista[l-1]=lista[l]
                       lista[l]=temp
            for k in range(1,lenght+1):
                print("El vector ordenado en la posicion  ",k,"  es ",lista[k-1])
                sleep(1)
        else:
            print('Error. El tamaño del vector debe ser entre 3 a 30')
    elif opcion==2:
        temp = int()
        nombre=str()
        lista2=[int()for ind0 in range(100)]
        lenght=int(input("Ingrese el tamaño del vector: "))
        if lenght>=3 and lenght<=30:
            for i in range(1,lenght+1):
                print("Ingrese el caracter: ",i)
                caracter=input()
                lista2[i-1]=caracter
                print("El caracter en la posicion  ",i,"  es  ", lista2[i-1],'\n')
                sleep(1)
            for j in range(1,lenght+1):
                for l in range(1,lenght):
                    if lista2[l-1]>lista2[l]:
                        temp = lista2[l-1]
                        lista2[l-1]=lista2[l]
                        lista2[l]=temp
            for k in range(1,lenght+1):
                print("El vector ordenado en la posicion  ",k,"  es ",lista2[k-1])
                sleep(1)
        else:
            print('Error. El tamaño del vector debe ser entre 3 a 30')
    else:
        print('La opcion ingresada es incorrecta')
    opcion=int(input('Ingrese el numero de la opcion que desea ejecutaro ingrese 0 si desea termianar el programa: '))