# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:28:03 2017

@author: Ivan
"""

print(ord("H"))

import numpy as np
import pandas as pd
import pylab

x = np.array([1,2,4,7,15])
y = np.array([0.5,1,2,3,4])

pylab.plot(x,y,'bo',label='sampled')
a,b = pylab.polyfit(x,y,1)
estYVals = a * x + b
pylab.plot(x,estYVals)

a,b,c = pylab.polyfit(x,y,2)
estYVals = a*x**2 + b*x + c
pylab.plot(x, estYVals)

#print(a,b)


