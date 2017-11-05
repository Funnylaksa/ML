# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:31:16 2017

@author: Ivan
"""

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

mjp = Series([0,2,4,6,8])       #Creating a simple series
print (mjp)                     #Index on the left, values on the right
print (mjp.values)              #

    
#jeeva = Series(["A","A","A","B"],index = ["Capstone","AFC","MEMS","econs"])
#print(jeeva[["Capstone","econs"]])
#
#print (jeeva[jeeva=="A"])
#
#dict = {"Ivan":4.65 , "HW":4.2 , "LY":4.0}
#score = Series(dict)
#print(score)
#print(np.mean(score))
#
#student = ["Amos","Ivan","LQ"]
#score_1 = Series(dict, index=student)
#print (score_1)
#print(pd.isnull(score_1))
#score_1.name = "Students in SUTD"
#score_1.index.name = "Students"
#print(score_1)
#
#states= {"State": ["Bedok","Kembangan","Aljunied","Choa Chu Kang"]
#,"Population": [2,3,5,7]
#,"Initial" : ["B","K","A","C"]}
#
#stations = DataFrame(states)
##print(stations)
##print(DataFrame(states,columns = ["State","Population","Initial"]))
#new_frame = DataFrame(states,columns =["State","Population","Initial","Money"], index = ["a","b","c","d"])
#new_frame.Money = np.arange(4)
#print (new_frame)
#
#series = Series(['a','b','c'], index = ['a','b','c'])
#new_frame.Population = series
#print(new_frame)
#
#new_frame['Development'] = new_frame.State == "Aljunied"
#print (new_frame)
#
#
#new_data = {"Ivan": {2017:24, 2016:23, 2018:25} , "Huiwen": {2017:21 , 2016:20}}
#new_frame = DataFrame(new_data , columns = ["Ivan","Huiwen"], index = [2018,2017,2016])
#
#print(new_frame)

#SERIES
var = Series(["python", "C++", "JavaScript", "Matlab"], index = [0,2,4,6])
print (var.reindex(range(7) , method = "ffill"))

#DATAFRAME
student = {"Students":["Ivan", "Huiwen" , " LQ"] , "Grades":["A","A","B"], "Gender":["M","F","M"]}
data = DataFrame(student, columns = ["Students", "Gender","Grades"] , index=[2,4,6])
print(data)




























































