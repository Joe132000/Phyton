# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def fibonacci(n):
    x=0
    v=1
    if n>1:
        while x<n: 
            print(x,end=" ")
            z=(x+v)
            x=v
            v=z
            
    else:
       print('El numero ingresado debe ser mayor a 1')   

fibonacci(8)