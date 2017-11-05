# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:24:46 2017

@author: Ivan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sklearn.cluster as cluster


#data = open("clustering.csv", "r")
#for j in range (210):
#    print (data.readline())
    
X = pd.read_csv("normalised.csv")
print (X.head())

kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)
#est = cluster.K
##print (kmeans)

X = X.assign(label=0)

print (kmeans)

data = {}

j=0

color = {0:"Red", 1:"Green", 2:"Blue"}

for i in kmeans.labels_:
    
    X.set_value(j,"label",i)
    if i in data.keys():
        data[i] += 1
    else:
        data[i] = 1
    j += 1

print (data)



ax = X.plot(kind="scatter", x="Height", y="Length", c=X["label"].apply(lambda x: color[x]))
X.plot(kind="scatter", x="leaf_height", y="leaf_width", c=X["label"].apply(lambda x: color[x]))