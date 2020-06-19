# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:38:08 2020

@author: JOSEPH
"""


ipadd={'R1':'10.0.0.1','R2':'10.0.0.2',
       'R3':'10.0.0.3','S1':'10.1.0.1',
       'S2':'10.1.0.2'}
print(type(ipadd))

dict1={'usuario1':'1713195590','valor':5000,'edad':39,
       'casado':True,'RATE en %':52.2}

print(ipadd['S2'])
ipadd['S5']='10.1.0.5'
print('S5'in ipadd)
print('edad' in dict1)