# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:16:26 2020

@author: ASUS
"""

# sets

a = {}
print(a)

a = {1,34,2.4,'mahadi'}
print(a)

a = set('mahadi')
print(a)

a.add(18)
print(a)

a.update([18,45])
print(a)

a.remove(18)
print(a)

a.discard('a')
print(a)

a.pop()
print(a)

a.clear()
print(a)

a = {1,2,3,4,5,6}
b = a.copy()
print(b)

# frozen set
s = {12,23,34,45}
print(s)
s1 = frozenset(s)
print(s1)

s.add(14)
print(s)
print(s1)

