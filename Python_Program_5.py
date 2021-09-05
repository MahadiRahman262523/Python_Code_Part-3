# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:36:31 2020

@author: ASUS
"""

# Dictionary

a = {}
print(a)

a = {1:'mahadi', 2:'sadia', 3:2526}
print(a)

a1 = {'mahadi':'m', 'sadia':'s'}
print(a1)

a2 = {1:[1,2,3],3:'Hello',4:('mrd','srs')}
print(a2)

a3 = dict({1:'deep',7:1845})
print(a3)

a4 = dict([(1,'mahadi'),(2,'sadia')])
print(a4)

x = {1:'mrd',2:'srs',3:{1:'mahadi',2:'sadia'}}
print(x)

x[4] = "mrdsrs" #add
print(x)

x[3] = 2625 # changed
print(x)

x["mrdsrs"] = 2625
print(x)

print(x[4]) # excess
print(x.get(2)) # excess

del x[3]
print(x)

x = {1:'mrd',2:'srs',3:{1:'mahadi',2:'sadia'}}
print(x[3][1])

del x[3][1]
print(x)

x.pop(1)
print(x)

x.popitem()
print(x)

x.clear()
print(x)

y = a2.copy()
print(y)

print(y.keys())

print(y.items())










