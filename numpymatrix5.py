# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:54:38 2020

@author: JOSEPH
"""


import numpy as np
x=np.array([(3,2,1,0),(6,5,4,3)])
y=np.array([(1,2,3,4),(5,6,7,8)])
print(x+y,'\n')
print(x*y,'\n')
print(x/y,'\n')
print(x-y,'\n')
c=np.ones((4,4))
print(c,'\n')
d=np.ones((4,2))
print(d,'\n')
print(c.dot(d),'\n')
print(np.dot(c,d),'\n')