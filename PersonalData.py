# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:26:43 2020

@author: JOSEPH
"""
espacio=' '
nombre=input('ingrese su nombre: ')
lastname=input('ingrese su apellido: ')
age=input('ingrese su edad: ')
location=input('ingrese su localizacion(Pais): ')

print('\n','Sus datos personales son:','\n'
      ,'NOMBRE: ',nombre,'\n',
      'APELLIDO: ',lastname,'\n',
      'EDAD: ',age,'\n',
      'Localizacion: ',location,'\n',
      )
print(nombre+espacio+lastname+espacio+age+espacio+location)