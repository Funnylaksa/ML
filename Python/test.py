# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:08:15 2017

@author: Ivan
"""

#import tensorflow as tf
#
#class people(object):
#    def __init__(self,side):
#        self.side = side 
#        
#    def area(self):
#        return self.side**2
#    
#hi = people(3)
#print (hi.area())
#
#print ('hello')
#
#
#sess = tf.Session()
#
#W = tf.Variable([0.3], tf.float32)
#b = tf.Variable([-0.3], tf.float32)
#x = tf.placeholder(tf.float32)
#linear_model = W*x + b
#
#init = tf.global_variables_initializer()
#sess.run(init)
#
#y = tf.placeholder(tf.float32)
#square_deltas = tf.square(linear_model - y)
#loss = tf.reduce_sum(square_deltas)
#
##print (sess.run(loss, {x:[1,2,3] , y:[4,5,6]} ))
#print (sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
# 
#ww = tf.assign(W,[-1])
#bb = tf.assign(b,[1])
#sess.run([ww,bb])
#print (sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
#
#optimiser = tf.train.GradientDescentOptimizer(0.01)
#train = optimiser.minimize(loss)
#
#sess.run(init)
#for i in range(1000):
#    sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
#    
#print (sess.run([W,b]))
#
#
##W = tf.Variable([.3], dtype=tf.float32)
##b = tf.Variable([-.3], dtype=tf.float32)
##x = tf.placeholder(tf.float32)
##linear_model = W * x + b
##
##init = tf.global_variables_initializer()
##sess.run(init)
##
##
###print (sess.run(linear_model, {x:[1,2,3,4]}))
##
##y = tf.placeholder(tf.float32)
##square_deltas = tf.square(linear_model - y)
##loss = tf.reduce_sum(square_deltas)
##print (sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
#
#
#W = tf.Variable(tf.zeros([784, 10]))
##sess.run(W)


#node1 = tf.constant(5.0)
#node2 = tf.constant(6.0)
#c = node1*node2
#sess = tf.Session()
#
#file_writer = tf.summary.FileWriter('C:\\Users\\Ivan\\Desktop\\Coding\\python' , sess.graph)
#
#print (sess.run([c]))
#
#sess.close()


#a = tf.placeholder(tf.float32)
#b = tf.placeholder(tf.float32)
#
#adder_node = a+b
#
#sess = tf.Session()
#print (sess.run([adder_node] , {a:[1,3], b:[2,4]}))

import tensorflow as tf

W = tf.Variable([.3])
b = tf.Variable([-.3])
x = tf.placeholder(tf.float32)

linear_model = W*x + b

y = tf.placeholder(tf.float32)

#loss
squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)

#Optimise
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train,{x:[1,2,3,4] , y:[0,-1,-2,-3]})

print (sess.run([W,b]))

#print (sess.run(loss , {x:[1,2,3,4] , y:[0,-1,-2,-3]}))


#from sklearn.feature_extraction.text import CountVectorizer

x = ['hi my name is ivan afs']
vect = CountVectorizer()
vect.fit(x)
print (vect.get_feature_names())














