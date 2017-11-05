# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:43:29 2017

@author: Ivan
"""

from __future__ import print_function 
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
np.set_printoptions(threshold = np.inf)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import LogisticRegression



iris = load_iris()
X = iris.data
y = iris.target

#print (pd.DataFrame(X, columns = iris.feature_names).head())

knn = KNeighborsClassifier()
knn.fit(X,y)
#print (knn.predict([[3,5,4,2]]))

simple_train = ['call me tonight','Call me a cab','Please call me']
vect = CountVectorizer()
vect.fit(simple_train)
#print (vect.get_feature_names())

simple_train_dtm = vect.transform(simple_train)
#print (simple_train_dtm)

#print (simple_train_dtm.toarray())
pd.DataFrame(simple_train_dtm.toarray() , columns = vect.get_feature_names() )

#print (type (simple_train_dtm ))
#print (simple_train_dtm)

simple_test = ["Please don't cal me"]
simple_test_dtm = vect.transform(simple_test)
simple_test_dtm.toarray()

pd.DataFrame (simple_test_dtm.toarray(), columns = vect.get_feature_names() )

url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
sms = pd.read_table(url, header = None, names = ['label','message'])

#print (sms.label.value_counts())
sms['label_num'] = sms.label.map({'ham':0 , 'spam':1})
#print (sms.head(10))

X = sms.message
y = sms.label_num
#print (X.shape)
#print (y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 1)
vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)
#print (X_train_dtm.shape)

nb = MultinomialNB()
nb.fit(X_train_dtm,y_train)

y_pred_class = nb.predict(X_test_dtm)

(metrics.accuracy_score(y_test,y_pred_class))
(metrics.confusion_matrix(y_test,y_pred_class))

#print (X_test[(
) > (y_test)])
#print (X_test[(y_pred_class) < (y_test)])

#print (X_test[3132])
y_pred_prob = nb.predict_proba(X_test_dtm)[:,1]
#print (y_pred_prob)
#print (metrics.roc_auc_score(y_test,y_pred_prob))

logreg = LogisticRegression()
logreg.fit(X_train_dtm,y_train)
y_pred_class = logreg.predict(X_test_dtm)

y_pred_prob = logreg.predict_proba(X_test_dtm)[:,1]
#print (metrics.accuracy_score(y_test,y_pred_class))
#print (metrics.roc_auc_score(y_test, y_pred_prob))
#print (y_pred_prob.shape)
#print (X_test_dtm.shape)

X_train_tokens = vect.get_feature_names()
#print (len(X_train_tokens))
#
#print (X_train_tokens[0:50])
#print (X_train_tokens[-50:])
#print (nb.feature_count_.shape)

ham_token_count = nb.feature_count_[0,:]
spam_token_count = nb.feature_count_[1,:]

#print (ham_token_count)
#print (spam_token_count)

tokens = pd.DataFrame({"Tokens":X_train_tokens , "Ham":ham_token_count, "Spam":spam_token_count})

#print (tokens)
#print (tokens.sample(5,random_state=6))

tokens['Ham'] = tokens.Ham +1
tokens["Spam"] = tokens.Spam +1
#print (tokens.sample(5,random_state=6))

tokens["Ham"] = tokens.Ham/nb.class_count_[0]
tokens["Spam"] = tokens.Spam/nb.class_count_[1]

tokens['Spam Ratio'] =tokens.Spam/tokens.Ham
#print (tokens.sample(5,random_state=6))

print (tokens.sort_values('Spam Ratio' , ascending = False))











