# -*- coding: utf-8 -*-
print("""
Created on Thu Jun 25 14:06:20 2020

@author: JOSEPH
""")

horas=int(input('Horas trabajadas: \n'))
tarifa=int(input('Tarifa por hora: \n'))
descuento=int(input('Descuentos: \n'))
x=horas
z=tarifa
if horas>40:
   s=horas-40
   z=(tarifa/2)*s
   x=horas*tarifa
   y=x+z-descuento  
else:
    y=(horas*tarifa)-descuento
print('Valor a pagar: $',y)

input('Press ENTER to exit')
