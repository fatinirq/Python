# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:02:51 2020

@author: Fatin
"""

import numpy as np;
import time
a=np.array([1,2,3,4,5]);
print(a);
a= np.random.rand(1000000)
b=np.random.rand(1000000)
tic=time.time()
c=np.dot(a,b)
toc=time.time()
print ("Vectorize Version Time =" , str(1000 * (toc-tic)) , "ms   " , "c=" , c)
c=0
tic=time.time()
for i in range(1000000):
    c+= a[i] * b[i]
toc=time.time()
print ("For Version Time =" , str(1000 * (toc-tic)) ,"ms   " , "c=" , c)