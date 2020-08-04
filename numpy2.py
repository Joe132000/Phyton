# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:07:28 2020

@author: JOSEPH
"""

import numpy as np
matrix=np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.int64)
print(matrix)
print('\n'*2)
unos=np.ones((5,5))
print(unos)
print('\n'*2)
ceros=np.zeros((5,5))
print(ceros)
print('\n'*2)
azarNo=np.random.random((4,4))
print(azarNo)
print('\n'*2)
ept=np.empty((5,5))
print(ept)
print('\n'*2)
full=np.full((5,5),5)
print(full)
print('\n'*2)
space=np.arange(0,101,5)
print(space)
print('\n'*2)
space1=np.linspace(1,100,10)
print(space1)
print('\n'*2)