# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:43:38 2017

@author: Ivan
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
pd.set_option('display.max_colwidth', -1)


iris = load_iris()
#print (iris.feature_names)
#print (iris.target_names)

X = (iris.data)
y = (iris.target)

knn = KNeighborsClassifier()

X_train,X_test,y_train,y_test = train_test_split(X,y)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

#print (metrics.accuracy_score(y_test,y_pred))

#pd.DataFrame(simple_train_dtm.toarray() , columns = vect.get_feature_names())
url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
sms = pd.read_table(url  , names = ['label' , 'message'])
sms['label_num'] = sms.label.map({'ham':0 , 'spam':1})


X = sms.message
y = sms.label

vect = CountVectorizer()

X_train , X_test , y_train , y_test = train_test_split(X,y)

vect.fit(X)

X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)

knn = KNeighborsClassifier()
knn.fit(X_train_dtm,y_train)
y_pred = knn.predict(X_test_dtm)
print (metrics.accuracy_score(y_test , y_pred))

nb = MultinomialNB()
nb.fit(X_train_dtm,y_train)
y_pred = nb.predict(X_test_dtm)
print (metrics.accuracy_score(y_test , y_pred))

#print(y_test.value_counts())


#words = vect.get_feature_names()
#ham_count = nb.feature_count_[0,:]
#spam_count = nb.feature_count_[1,:]
#
#tokens = pd.DataFrame({'ham': ham_count , 'spam' : spam_count})
#
#tokens.ham = tokens.ham + 1
#tokens.spam = tokens.spam + 1
#
#tokens['spam_ratio'] = tokens.spam/tokens.ham
#tokens['words'] = words
#print (tokens.sort_values('spam_ratio')) 


words = vect.get_feature_names()
ham_count = nb.feature_count_[0,:]
spam_count = nb.feature_count_[1,:]

tokens = pd.DataFrame({'ham': ham_count , 'spam': spam_count})

tokens.ham = tokens.ham + 1
tokens.spam = tokens.spam + 1
tokens['spam_ratio'] = tokens.spam/tokens.ham
tokens['words'] = words

print (tokens.sort_values('spam_ratio'))





