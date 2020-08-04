# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:10:50 2020

@author: JOSEPH
"""

print("""
      (1). Impresion a blanco y negro
      (2). Impresion a color """)
x=int(input("Ingrese la opcion a ejecutar(la opcion ingresada debe ser numerica): "))

if x==1:
    print("Impresion a B/N, costo $0.06")
    cantin=int(input('Digite la cantidad inicial de impresiones del mes: '))
    cantfin=int(input('Digite la cantidad final de impresiones del mes: '))
    while cantfin<cantin:
        print('\nERROR: La contador inicial es menor que el final, digite otro contador final')
        cantfin=int(input('Digite la cantidad final de impresiones del mes: '))
    numimpr=cantfin-cantin
    ventas=numimpr*.06
    print('impresiones: ',numimpr)
    print('costo: ',ventas)
elif x==2:
    print("Impresion a Color, costo $0.12")
    cantin=int(input('Digite la cantidad inicial de impresiones del mes: '))
    cantfin=int(input('Digite la cantidad final de impresiones del mes: '))
    while cantfin<cantin:
        print('\nERROR: La contador inicial es menor que el final, digite otro contador final')
        cantfin=int(input('Digite la cantidad final de impresiones del mes: '))
    numimpr=cantfin-cantin
    ventas=numimpr*.12
    print('impresiones: ',numimpr)
    print('costo: ',ventas)
else:
    print('la opcion ingresada es incorrecta, vuelva a ejecutar el programa')