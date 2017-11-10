# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:37:10 2017

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

#load iris ML
"""
iris = load_iris()


# ## Prints 4 feature names, target = [0 , 1 or 2] , target_names = [ setosa, versicolor or virginica]

#print (iris.feature_names)
#print (iris.target)
#print (iris.target_names)

# ## X = array of data of the features. E.g ([1,1.5,2,2])    Shape = [150,4]
# ## y = array of target                E.g ([0])            Shape = [150,]


X = np.array(iris.data)
y = np.array(iris.target)

X_train,X_test,y_train,y_test = train_test_split(X,y) 

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

y_pred = (knn.predict(X_test))

print (metrics.accuracy_score(y_pred , y_test))
"""

# ## Split phrases into list of individual words
simple_train = ['hi, my name is ivan' , 'your name is hi' , 'ivan']
vect= CountVectorizer(simple_train)
vect.fit(simple_train)
#print (vect.get_feature_names())

# ## From list of words in simple_train, show what words appear in each item in list 
simple_train_dtm = vect.transform(simple_train)
#print (simple_train_dtm)
#print (simple_train_dtm.toarray())

#Make DataFrame
pd.DataFrame(simple_train_dtm.toarray() , columns = vect.get_feature_names())
url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
sms = pd.read_table(url  , names = ['label' , 'message'])

sms['label_num'] = sms.label.map({'ham':0 , 'spam':1})

X = sms.message
y = sms.label

X_train, X_test , y_train, y_test = train_test_split(X,y,random_state = 1)

vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)


knn = KNeighborsClassifier()
knn.fit(X_train_dtm , y_train)
y_pred = knn.predict(X_test_dtm)

print(metrics.accuracy_score(y_test , y_pred))


nb = MultinomialNB()
nb.fit(X_train_dtm , y_train)
y_pred = nb.predict(X_test_dtm)

print(metrics.accuracy_score(y_test , y_pred))

log = LogisticRegression()
log.fit(X_train_dtm , y_train)
y_pred = log.predict(X_test_dtm)

print (metrics.accuracy_score(y_test , y_pred))

# To get all the words in the form of arrays
X_train_tokens = vect.get_feature_names()

#To get count of ham and spam of each word (len of both feature_count_ = 7456)
ham_token_count = nb.feature_count_[0,:]
spam_token_count = nb.feature_count_[1,:]

# To place [word, ham_count and spam_count] in a DataFrame
tokens = pd.DataFrame({'tokens':X_train_tokens  ,  'Ham': ham_token_count , 'Spam':spam_token_count})

# 1 is added to remove all counts of 0(inf error)
tokens['Ham'] = tokens.Ham +1
tokens["Spam"] = tokens.Spam +1

# To normalise the data (class_count_[0] = 3617 / class_count_[1] = 562) 
#tokens.Ham = tokens['Ham']
tokens["Ham"] = tokens.Ham/nb.class_count_[0]
tokens["Spam"] = tokens.Spam/nb.class_count_[1]

tokens['Spam_ratio'] = tokens['Spam']/tokens['Ham']

# prints entire dataFrame, sorting value by spam ratio
#print (tokens.sort_values('Spam_ratio'))
df = tokens[['Spam' , 'Ham']]
print (df)

'release1'


