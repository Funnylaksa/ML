# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:26:01 2017

@author: Ivan
"""

import numpy as np
import pandas as pd
import pylab
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('clustering.csv')
avg = pd.read_csv('normalised.csv')

#print (df.head())

df_norm = (df - df.mean()) / (df.max() - df.min())

kmeans = KMeans(n_clusters = 3,random_state=0).fit(df_norm)
label = kmeans.labels_

df_norm['label'] = label

#print(df_norm.head())

#data = {}
#for i in label:
#    for j in len(3):
#        if i == j:
#            data.keys 
##    print (i)
#    if i == 0:
#        count +=1
#        
#print (count)

grp0 = df_norm[df_norm['label'] == 0] 
grp1 = df_norm[df_norm['label'] == 1] 
grp2 = df_norm[df_norm['label'] == 2] 

plt.scatter(grp0["Height"] , grp0["Length"], color = 'r')
plt.scatter(grp1["Height"] , grp1["Length"], color = 'k')
plt.scatter(grp2["Height"] , grp2["Length"], color = 'g')
plt.show()
