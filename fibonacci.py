# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def fibonacci(n):
    x,v=0,1
    if n>1:
        while x<n: 
            print(x,end=" ")
            z=(x+v)
            x=v
            v=z  
            'x,v=v,x+v'
    else:
       print('El numero ingresado debe ser mayor a 1')   

fibonacci(8)