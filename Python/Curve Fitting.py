# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:31:36 2017

@author: Ivan
"""
#CURVE FITTING
import pylab
def getData(fileN):
    data = open(fileN,"r")
    clearHeading = data.readline()
    distance = []
    height1,height2,height3,height4 = [],[],[],[]
    for i in data:
        d,h1,h2,h3,h4 = i.split()
        distance.append(float(d))
        height1.append(float(h1))
        height2.append(float(h2))
        height3.append(float(h3))
        height4.append(float(h4))
    return (distance,[height1,height2,height3,height4])

def R2(estimated,measured):
    EE = ((estimated-measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean-measured)**2).sum()
    return 1 - EE/MV

def tryFits(fileN):
    distance,height = getData(fileN)
    distance = pylab.array(distance)
    totalHeight = pylab.zeros(len(height[0]))
    for i in height:
        totalHeight = totalHeight+ pylab.array(i)
    meanHeight = totalHeight/len(height)
    
    pylab.plot(distance,meanHeight,"bo",label ="raw data")
    pylab.xlabel("distance travelled(m)")
    pylab.ylabel("height(m)")
       
    a,b = pylab.polyfit(distance,meanHeight,1)
    estYVals = a*distance + b
    pylab.plot(distance,estYVals,label = "Linear Fit" + ",R2 =" + str(R2(estYVals,meanHeight)))
    a,b,c = pylab.polyfit(distance,meanHeight,2)
    estYVals = a*distance**2 + b*distance + c
    pylab.plot(distance,estYVals,label = "Quadratic Fit" + ",R2 = " +str(R2(estYVals,meanHeight)))
    
    a,b,c,d = pylab.polyfit(distance,meanHeight,3)
    estYVals = a*distance**3 + b*distance**2 + c*distance + d
    pylab.plot(distance,estYVals,label = "Polynomial Fit" + ",R2 = " +str(R2(estYVals,meanHeight)))
    
    pylab.legend()
    
tryFits("C:\\Users\\Ivan\\Desktop\\Coding\\Python\\launcherData.txt")


#TRY EXCEPT
def readVal(valType, msg, errorMsg):
    tries = 0
    while tries<4:
        val = input(msg)
        try:
           val = valType(val)
           return(val)
        except:
            tries = tries + 1
            print(errorMsg)
    raise TypeError("Num tries exceeded")

readVal(int,"type int:","Not int")


