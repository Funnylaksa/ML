# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:44:01 2017

@author: Ivan
"""


from math import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

import datetime

#class Person(object):
#    def __init__(self,name):
#        self.name = name
#        self.birthDate = None
#        try:
#            space = name.rindex(" ")
#            self.lastName = self.name[space+1:]
#        except:
#            self.lastName = lastName
#            
#    def setBirthDay(self,birthDate):
#        assert type(birthDate) == datetime.date
#        self.birthDate = birthDate
#        
#    def getAge(self):
#        return (datetime.date.today() - self.birthDate ).days
#        
#    def __str__(self):
#        return self.name
#    
#p1 = Person("Ivan Lee")
#print (p1)
#print (p1.lastName)


from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

iris = load_iris()
#print (type(iris))

#print (iris.feature_names)
#print(iris.target)
#print(iris.target_names)
#
#
X = np.array(iris.data)
y = np.array(iris.target)
#
#print (X)
#print (y)
#
#print(X.shape)
#print(y.shape)
X.reshape(-1,1)

knn = KNeighborsClassifier(n_neighbors = 1)
#print(knn)
knn.fit(X,y)
#
print(knn.predict([[5,3,4,2]]))

X_new = ([[5,4,3,2],[3,5,4,2]])
print (knn.predict(X_new))


knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X,y)
print (knn.predict(X_new))

logreg=LogisticRegression()
logreg.fit(X,y)
print(logreg.predict(X_new))


print (metrics.accuracy_score([0,1,1,1],[0,1,1,0]))






