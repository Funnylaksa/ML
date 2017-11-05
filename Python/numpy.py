# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:57:56 2017

@author: Ivan
"""
import numpy as np
import pandas as pd
from numpy import random
from pandas import Series,DataFrame
from numpy.linalg import inv, qr

#SERIES
letters = Series(['a','b','c','d'], index=[0,2,4,7])
letters1 = letters.reindex(index = range(8),method = "ffill")
#print (letters1)

#DATAFRAME
countries = {"Countries":["Singapore","Malaysia","Indonesia","Thailand"]
,"Wealth":["Rich","Poor","Poor","Average"]
,"Number": [123,456,789,12]}
frame = DataFrame(countries, columns = ["Countries","Wealth","Number"])
#print(frame.Countries)


#ARRAY
scores1 = [99,88,77,66]
array1 = np.array(scores1)
#print(array1)

scores2 = [[11,22,33],[44,55,66]]
array2 = np.array(scores2)
#print (array2)

x = np.zeros((3,4))
eye =np.eye((3))
#print(eye)

#Any modifications on the modified array will be shown in the main array
modi_array = array1[1:3]
modi_array[1] = 101
#print (array1)

#matrix_arr =np.array( [[1,2,3],[4,5,6],[7,8,9]] )
#print (matrix_arr[0])
#
#
#algebra = random.rand(6,4)
#for i in range(6):
#    algebra[i] = i
#print(algebra)
#print (algebra[[4,5,1]])

x1= np.array([1,2,3,4,5])
y1 = np.array([6,7,8,9,10])
cond =[True, False, True, True, False]
#If you want to take a value from x1 whenever the corresponding value in cond is true, otherwise take value from y.
z1 = [(x,y,z) for x,y,z in zip(x1, y1, cond)] # I have used zip function To illustrate the concept
#print (z1)
#print (np.where(cond, x1, y1)) 

#ZIP
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a3 = np.array([True,False,False])
zippo = list(zip(a1,a2,a3))
#print (zippo)
#print (np.where(a3,a1,a2))

#ra = random.rand(5,5)
#print(ra)
#ra_positive = np.where(ra>0.5,1,-1)
#print(ra_positive)
#print (ra_positive.sum())
#print(ra_positive.mean())

#STATISTICAL MODEL
thie = np.random.rand(1,2,3,4)
#print (thie.sum())
#print (np.sum(thie))

jp = np.arange(6).reshape(2,3)
#print ("The array is :{}" .format(jp))
#print ("The sum of each column are :{}" .format(np.sum(jp,axis=0))) #sum of columns
#
#print (jp.sum(1))       #sum of rows
#print (jp.cumsum(0))

x = np.random.rand(5)
x.sort()
#print (x)
#list1 = [1,1,1,2,2,2,3,3,3,3,3,3]
#print (np.unique(list1))
#print (set(list1))
#print (np.in1d(list1,1))


#LINEAR ALGEBRA
array1 = np.array([[0,1,2],[3,4,5],[2,4,5]])
array2 = np.random.rand(3,3)
x = np.dot(array1,array2)
array3 = np.arange(9).reshape(3,3)
print (array1)
print (array3)

inv = inv(array1)
print (np.dot(array1,inv))








