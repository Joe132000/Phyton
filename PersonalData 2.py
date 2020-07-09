# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:26:43 2020

@author: JOSEPH
"""
espacio=' '
nombre=input('ingrese su nombre: ')
lastname=input('ingrese su apellido: ')
age=int(input('ingrese su edad: '))
location=input('ingrese su localizacion(Pais): ')

print('\n','Sus datos personales son:','\n'
      ,'NOMBRE: ',nombre,'\n',
      'APELLIDO: ',lastname,'\n',
      'EDAD: ',age,'\n',
      'Localizacion: ',location,'\n',
      )
if age>=1 and age<=12:
    print('su edad esta en el rango de 1-12 \'niñez\'')
elif age>=13 and age<=18:
    print('su edad esta en el rango de 13-18 \'adolescencia\'')
elif age>=19 and age<=30:
    print('su edad esta en el rango de 19-30 \'juventud\'')
elif age>=31 and age<=59:
    print('su edad esta en el rango de 31-59 \'adultez\'')
elif age>=60 and age<=120:
    print('su edad esta en el rango de 60-120 \'vejez\'')
else:
    print('su edad se encuentra fuera de los rangos predeterminados')
