# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:58:22 2017

@author: Ivan
"""

#Find the cube root of a perfect cube
#x = int(input("Enter integer: "))
#i = 0
#while i**3<x:
#    i=i+1
#print("Current answer is :" ,i)
#    
#if i**3 == x:
#    print("The cube root of x is " , i )
#else:
#    print(x , "is not a perfect cube")

#Problem Set 1
#balance = int(input("Enter the outstanding balance on your credit card: "))
#interest_annual = float(input("Enter the annual credit card interest rate as a decimal: "))
#rate_monthly = float(input("Enter the minimym monthly payment rate as a decimal: "))
#
#
#def bank(balance,interest_annual,rate_monthly,month):
#    total = 0
#    for i in range(month):
#        min_monthly_payment = balance * rate_monthly
#        interest_paid = balance * interest_annual/12
#        principal_paid = min_monthly_payment - interest_paid
#        balance = balance - principal_paid
#        total+=min_monthly_payment
#        print ("Month:",i)
#        print ("Principal paid: ",principal_paid)
#        print ("Remaining balance: ", balance)
#        print ("Total paid: ",total)
#    return balance

#balance_initial = int(input("Enter the outstanding amount on your credit card: "))
#interest = float(input("Enter the annual credit card interest rate as a decimal: "))
#balance = balance_initial
#min_payment = 0
#while balance >0:
#    balance = balance_initial
#    min_payment += 0.1
#        month = 0
#    while month <12 and balance >0:
#        balance = balance * (1+interest/12) - min_payment
#        month = month +1      
#print("Monthly payment to payy off debt in 1 year: " ,min_payment)
#print("Number of months needed: " , month)
#print(balance)

#x = 100
#divisors = ()
#for i in range(1,x):
#    if x%i == 0:
#        divisors = divisors + (i,)
#print (divisors)

#poly = (0.0, 0.0, 5.0, 9.3, 7.0)
#x = -13
#poly = (-13.39,0.0,17.5,3.0,1.0)
#x_0 = 8
#epsilon = .0001
#
#def evaluate_poly(poly,x):
#    ans = 0.0
#    for i in range(len(poly)):
#        ans += poly[i]*x**i
#    return (ans)
#
#def compute_deriv(poly):
#    x = []
#    for i in range(len(poly)):
#        x.append(poly[i]*i)
#    return (x[1:])
#
#def compute_root(poly,x_0,epsilon):
#    x = x_0
#  
#    while abs(evaluate_poly(poly,x)) >= epsilon:
#        x = x - evaluate_poly(poly,x)/evaluate_poly(compute_deriv(poly),x)
#               
#    return (x)
#
#print (compute_root(poly,x_0,epsilon))
        
#def buildCodeBook():
#    letters ='.abcdefghijklnopqrstuvwxyz'
#    codeBook = {}
#    key = 0
#    for c in letters:
#        codeBook[key] = c
#        key += 1
#    return codeBook 
#    
#def decode(cypherText, codeBook):
#    plainText = ''
#    for e in cypherText:
#        if e in codeBook:
#            plainText += codeBook[e]
#        else:
#            plainText += ' '
#    return plainText
#codeBook = buildCodeBook()
#msg = (3,2,41,1,0)
#print (decode(msg, codeBook)   )    
#
#T = (0.1, 0.1)
#x = 0.0
#for i in range(len(T)):
#    for j in T:
#        x += i + j
#        print (x)
#print (i)

#def f(x):
#    if x == 0:
#        return 1
#    else:
#        return f(x-1) *x

#def build_coder(shift):
# """
# Returns a dict that can apply a Caesar cipher to a letter.
# The cipher is defined by the shift value. Ignores non-letter characters
# like punctuation and numbers.
# shift: -27 < int < 27
# returns: dict
# Example: >>> build_coder(3)
# {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
# 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
# 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
# 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
# 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
# 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
# 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
# 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
# (The order of the key-value pairs may be different.)
# """
# 
# 
# 
# ### TODO.
#def build_encoder(shift):
# """
# Returns a dict that can be used to encode a plain text. For example, you
# could encrypt the plain text by calling the following commands
# >>>encoder = build_encoder(shift)
# >>>encrypted_text = apply_coder(plain_text, encoder)
# The cipher is defined by the shift value. Ignores non-letter characters
# like punctuation and numbers.
# shift: 0 <= int < 27
# returns: dict
# Example: >>> build_encoder(3)
# {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
# 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
# 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 
# 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
# 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
# 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
# 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
# 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
# (The order of the key-value pairs may be different.)
# HINT : Use build_coder.
# """
# ### TODO.
#def build_decoder(shift):
# """
# Returns a dict that can be used to decode an encrypted text. For example,
#you
# could decrypt an encrypted text by calling the following commands
# >>>encoder = build_encoder(shift)
# >>>encrypted_text = apply_coder(plain_text, encoder)
# >>>decrypted_text = apply_coder(plain_text, decoder)
# The cipher is defined by the shift value. Ignores non-letter characters
# like punctuation and numbers.
# shift: 0 <= int < 27
# returns: dict
# Example: >>> build_decoder(3)
# {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
# 'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
# 'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
# 'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
# 'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
# 'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
# 'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
# 'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
# (The order of the key-value pairs may be different.)
# HINT : Use build_coder.
# """
# ### TODO.
#def apply_coder(text, coder):
# """
# Applies the coder to the text. Returns the encoded text.
# text: string
# coder: dict with mappings of characters to shifted characters
# returns: text after mapping coder chars to original text
# Example:
# >>> apply_coder("Hello, world!", build_encoder(3))
# 'Khoor,czruog!'
# >>> apply_coder("Khoor,czruog!", build_decoder(3))
# 'Hello, world!'
# """
# ### TODO.
#def apply_shift(text, shift):
# """
# Given a text, returns a new text Caesar shifted by the given shift
# offset. The empty space counts as the 27th letter of the alphabet,
# so spaces should be replaced by a lowercase letter as appropriate.
# Otherwise, lower case letters should remain lower case, upper case 
# letters should remain upper case, and all other punctuation should
# stay as it is.
# text: string to apply the shift to
# shift: amount to shift the text
# returns: text after being shifted by specified amount.
# Example:
# >>> apply_shift('This is a test.', 8)
# 'Apq hq hiham a.'
# """
# ### TODO. 
#
#

#principal = 10000
#interest = 0.05
#years = 20 
#values = []
#
#for i in range(years + 1):
#    values.append(principal)
#    principal += principal*interest
#    
#pylab.plot(values)
#pylab.title("5% growth, compound interest")
#pylab.xlabel("Years of compounding")
#pylab.ylabel("Value of Principal($)")

#import random
#import pylab
#def clear(n,p,steps):
#    number_of_molecules = [n]
#    for i in range(steps):
#        number_of_molecules.append(n*(1-p)**i)
#    pylab.plot(number_of_molecules, label = "Exponential Decay")
##pylab.plot(clear(1000,0.01,500))
#def clearSim(n,p,steps):
#    number_of_molecules = [n]
#    for i in range(steps):
#        num_left = number_of_molecules[-1]
#        for j in range(num_left):
#            if random.random()<=p:
#                print(random.random())
#                num_left = num_left - 1
#        number_of_molecules.append(num_left)
#    pylab.plot(number_of_molecules, label = "Simulation")
#clear(1000,0.01,500)
#clearSim(1000,0.01,500)

#import pylab
#import numpy as np
#dataFile = open('springData.txt','r')
#removeHeader = dataFile.readline()
#distance = []
#weight = []
#for line in dataFile:
#    d,w = line.split(" ")
#    distance.append(float(d))
#    weight.append(float(w))
#
#weight_array = np.array(weight)
#print (weight_array)
#force = weight_array *9.81
#print(force)
#
#pylab.plot(force,distance,"ro")
#pylab.xlabel("Force(N)")
#pylab.ylabel("Extension(m)")


#class Shape(object):
#    def __init__(self,side):
#        self.side = side
#    
#    def area(self):
#        return self.side**2
#
#class Square(Shape):
#    def __init__(self,side):
#        self.side=side
#        
#    def area(self):
#        return self.side**2
#    
#    def parameter(self):
#        return self.side*4
#    
#    def sizeOf(self):
#        if self.side > 4:
#            return "Big"
#        else:
#            return "Small"
#            
#        
#class Triangle(Shape):
#    def __init__(self,side):
#        self.side=side
#        
#    def area(self):
#        return 0.5 * self.side**2
#        
#    
#
#
#square1 = Square(8)
#print (square1.area())
#tri1= Triangle(4)
#print(tri1.area())
#
#print(square1.area())
#print(square1.parameter())
#print(square1.sizeOf())
#

#string1 = input("write sentence")
#letters = 0
#numbers = 0
#
#for i in (string1):
#    if i.isdigit():
#        numbers = numbers + 1
#    elif i.isalpha and i != "!" and i != " ":
#        letters = letters + 1
#        print(i)
#    else:
#        pass
#        
#print ("LETTERS" + str(letters))
#
#print ("DIGITS" + str(numbers))
#for i in string1:
    

#def fib(n):
#    global runs
#    runs = runs + 1
#    if n == 0 or n ==1:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#    
#
#steps = []
#for i in range(30):
#    runs = 0
#    print ("fib(" , i, ") is ", fib(i), "Takes" , runs, "steps")

#import random
#def rollDice():
#    return random.choice([0,1,2,3,4,5,6])
#
#def testRoll(n=10):
#    results = ""
#    for i in range(n):
#        results = results +str(rollDice())
#    print(results)
#
#testRoll()
    

#import pylab
#
#dict1 = {1:2, 3:4 , 5:6}
#print (dict1)
#pylab.xlabel("X-Axis")
    #pylab.ylabel("Y-Axis")


#class Shape(object):
#    def __init__(self,side):
#        self.side = side
#        self.x = 24
#        
#    def area(self):
#        return self.side**2
#
#class Triangle(Shape):
#    def __init__(self,side):
#        self.side = side
#        
#    
#
#square1 = Shape(3)
#tri1 = Triangle(3)


#import pylab
#import numpy as np
#
#
#def getData(fileName):
#    data = open(fileName,"r")
#    distance = []
#    mass = []
#    discardHeader = data.readline()
#    for i in data:
#        d,m = i.split()
#        distance.append(float(d))
#        mass.append(float(m))
#    return(distance,mass)
#        
#def plotData(fileName):
#    xVals, yVals = getData(fileName)
#    xVals = np.array(xVals) * 9.81
#    pylab.plot(xVals,yVals)
#    pylab.xlabel("Distance")
#    pylab.ylabel("Force")
#    
#def fitData(fileName):
#    yVals,xVals = getData(fileName)
#    xVals = np.array(xVals[:-6])*9.81 
#    yVals = np.array(yVals[:-6])
#    pylab.plot(xVals,yVals,"bo", label = "measured Displacement")
#    a,b = np.polyfit(xVals,yVals,1)
#    estYVals = a*pylab.array(xVals)+b
#    k=1/a
#    pylab.plot(xVals,estYVals, label = "Linear Fit,k=" + str(round(k,5)))
#    pylab.xlabel("Force")
#    pylab.ylabel("Distance")
#    
#    d,a,b,c = np.polyfit(xVals,yVals,3)
#    estYvals = d*xVals**3 +a*xVals**2 + b*xVals + c
#    pylab.plot(xVals,estYvals, label ="polynomial fit")
#    pylab.legend()
#    
#
#x = fitData("springData.txt")

#x = open("springData.txt","r")
#print (x.readline())
#for i in x:
#    print (i)

import pylab

def stdDev(x):
    mean = sum(x)/float(len(x))
    tot = 0.0
    for i in x:
        tot = tot + (x-mean)**2
    return (tot/len(x))**0.5

def getData(fileN):
    data = open(fileN,"r")
    removeHeader = data.readline()
    distance,height1,height2,height3,height4 = [],[],[],[],[]
    for i in data:
        d,h1,h2,h3,h4 = i.split()
        distance.append(float(d))
        height1.append(float(h1))
        height2.append(float(h2))        
        height3.append(float(h3))
        height4.append(float(h4))
    return (distance,[height1,height2,height3,height4])

def R2 (estimated,measured):
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV

    
    
def curve(fileN):
    distance, heights = getData(fileN)
    distance = pylab.array(distance)
    total = pylab.zeros(len(heights[0]))
    for i in heights:
        total = total + pylab.array(i)
    meanHeight = total/len(heights)
    
    pylab.plot(distance,meanHeight,"bo",label = "rawData")
    pylab.xlabel("Distance")
    pylab.ylabel("Height")
    
    a,b = pylab.polyfit(distance,meanHeight,1)
    estYVals = a*distance + b
    pylab.plot(distance,estYVals,label = "Linear Fit" + ",R2 = " + str(R2(estYVals,meanHeight)))
    
    a,b,c = pylab.polyfit(distance,meanHeight,2)
    estYVals = a*distance**2 + b*distance + c
    pylab.plot(distance,estYVals,label = "Quadratic Fit"+ ",R2 = " + str(R2(estYVals,meanHeight)))
    
    pylab.legend()
    return distance,estYVals

def yPeak(fileN):
    distance,estYVals = curve(fileN)
    yPeak = max(estYVals)
    
    time = ((yPeak*2)/385.92)**0.5
    xVel = 15/(time*12)
#    print (xVel)


yPeak("launcherData.txt")



