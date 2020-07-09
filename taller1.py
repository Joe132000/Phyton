# -*- coding: utf-8 -*-
print("""
Created on Thu Jun 25 14:06:20 2020

@author: JOSEPH
""")

numllant=int(input('Cantidad de llantas: \n'))
pruni=float(input('Precio unitario: \n'))
x=0
if numllant>4:
    x=pruni*.10
    
pruni=pruni-x
pago=numllant*pruni

print('Valor a pagar:  ',pago)

input('Press ENTER to exit')