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

class Person(object):
    def __init__(self,name):
        self.name = name
        try:
            firstBlank = name.rindex(" ")
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self,birthDate):
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
        
    def getAge(self):
        assert self.birthday != None
        return (datetime.date.today()- self.birthday).days
    
    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name<other.name
        return self.lastName<other.lastName
    
    def __str__(self):
        return self.name
    
class MITperson(Person):
    nextID = 0
    def __init__(self,name):
        self.name = name
        self.idNum = MITperson.nextID
        MITperson.nextID = MITperson.nextID+1
    def getID(self):
        return self.idNum
    def __lt__(self,other):
        return self.idNum<other.idNum

import datetime

class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthDate=None
        try:
            space = name.rindex(" ")
            self.lastName = name[space+1:]
        except:
            self.lastName = name
            
    def getLastName(self):
        return self.lastName
    
    def setBirthDate(self,date):
        assert type(date) == datetime.date
        self.birthDate = date
        
    def getAge(self):
        return (datetime.date.today() - self.birthDate).days
        
    def __str__(self):
        return self.name

class SUTDperson(Person):
    nextID = 0
    def __init__(self,name):
        self.name = name
        self.ID = SUTDperson.nextID
        SUTDperson.nextID = SUTDperson.nextID + 1
    def getID(self):
        return self.ID
    
class UG(SUTDperson):
    def __init__(self,name):
        SUTDperson.__init__(self,name)
        self.year = None
        
    
    
p1 = Person("Ivan Lee Chang Hsien")
p1.setBirthDate(datetime.date(1993,11,11))
print (p1.getAge())
print (p1.getLastName())

SUTD1 = SUTDperson("Amos Ho")
SUTD2 = SUTDperson("Ivan Lee")
SUTD3 = SUTDperson("Toh Hui Wen")
print(p1,SUTD1)

UG1 = UG("walao eh")

#p1 = MITperson("Marcus Toh")
#p2 = MITperson("Emily Richard")
#p3 = MITperson("lolhaha")
#print (p1,p1.getID())
#print (p2,p2.getID())
#print (p1<p3)
#print (p3<p2)
#    
#me = Person("Ivan Lee")
#hw = Person("Huiwen Toh")
#me.setBirthday(datetime.date(1993,11,11))
#hw.setBirthday(datetime.date(1995,5 ,27))
#print(me)
#print(me>hw)
#pList = [me,hw]
#for i in pList:
#    print (i)

