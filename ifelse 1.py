# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:25:28 2020

@author: JOSEPH
"""

num=int(input('cual es el numero Ipv4 ACL?'+'\n'))
if num>=1 and num<=99:
    print('este es un Ipv4 ACL estandar')
elif num>=100 and num<=199:
    print('este es un IPv4 ACL extendido')
else:
    print('este no es un numero estandar o extendido para IPv4 ACL')
         
