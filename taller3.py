# -*- coding: utf-8 -*-
print("""
Created on Thu Jun 25 14:06:20 2020

@author: JOSEPH
""")
cal1=float(input('Ingrese su primera calificacion: '))
cal2=float(input('Ingrese su segunda calificacion: '))
cal3=float(input('Ingrese su tercera calificacion: '))

x=max(cal1,cal2,cal3)
z=min(cal1,cal2,cal3)

if cal1<=z:
    y=min(cal2,cal3)
elif cal2<=z:
    y=min(cal1,cal3)
else:
    y=min(cal1,cal2)
        
r=y+x

print('su calificacion total es: ',r)
        
    

input('Press ENTER to exit')