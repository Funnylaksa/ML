# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:54:16 2017

@author: Ivan
"""
##from __future__ import print_function
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#path = 'data/yelp.csv'
#yelp = pd.read_csv(path)
#
#print(yelp.shape)


yelp = pd.read_csv('C://Users//Ivan//Downloads//pycon-2016-tutorial-master//data//yelp.csv')
#print (yelp.shape)

data = pd.DataFrame(yelp)
boolean = []
for stars in data.stars:
    if stars == 1 or stars ==5:
        boolean.append(True)
    else:
        boolean.append(False)

#print (len(boolean))
five_one_star = data[boolean]
#print (five_one_star.head())

X = five_one_star.text
y = five_one_star.stars

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)

vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)

nb = MultinomialNB()
nb.fit(X_train_dtm,y_train)

y_pred = nb.predict(X_test_dtm)
#print(y_pred.shape)
#print (metrics.accuracy_score(y_test,y_pred))
#print (metrics.confusion_matrix(y_test,y_pred))
#print(y_test.shape)
#print (y_test.value_counts().head(1)/y_test.shape)
#print(y)

#print (X_test[y_test<y_pred].head(10))
#print (X_test[y_test>y_pred].head(10))

X_train_tokens = vect.get_feature_names()
print (nb.feature_count_.shape)
one = nb.feature_count_[0,:]
five = nb.feature_count_[1,:]

tokens = pd.DataFrame({'token' :X_train_tokens  , 'one_star':one , 'five_star':five} )
print (tokens.head(10))


