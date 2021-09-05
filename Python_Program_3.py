# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:15:09 2020

@author: ASUS
"""

# Tuples

import sys
t = (21,35,6.7,"mahadi")
print(t)
print(t[3])
print(len(t))
print(dir(t))

print(sys.getsizeof(t))

#t1 = [21,35,6.7,"mahadi"]
#print(sys.getsizeof(t1))

t = tuple ('mahadi')
print(t)

t = ()
print(t)

t=(1,2,3)
t1=(4,5,6)
t2=(t,t1)
print(t2)

t2=t+t1
print(t2)

t=tuple('sadia')
print(t)
print(t[0:])
print(t[-1])
print(t[::-1])

#del t
#print(t)



