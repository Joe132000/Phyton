# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:38:44 2020

@author: JOSEPH
"""

def direccion(calle,interseccion,sector,codigopostal,referencia,numcasa):
    print('Su direccion es:\n',
          'Sector:', sector,'\n',
          'Calles: ',calle,' y ',interseccion,'\n',
          'Codigo postal: ',codigopostal,'\n',
          'Numero de casa: ',numcasa,'\n',
          'Referencia: ', referencia)
print('Ingrese los datos de su direccion')
a=(input('Ingrese la calle principal: '))
b=(input('Ingrese la calle secundaria: '))
c=(input('Ingrese sector: '))
d=(input('Ingrese codigo postal: '))
e=(input('Ingrese una referencia cercana: '))
f=(input('Ingrese el numero de casa: '))

direccion(a,b,c,d,e,f)