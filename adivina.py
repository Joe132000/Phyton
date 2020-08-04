# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:49:21 2020

@author: JOSEPH
"""
numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
x=int(input('Introduce tu numero: '))

while x != numeroSecreto:
    print("¡Ja, ja, ja! ¡Estás atrapado en mi ciclo!")
    x=int(input('Siga participando: '+'\n'))

print("¡Bien hecho, muggle! Eres libre ahora")   



