# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:22:26 2020

@author: ASUS
"""

# List

n = input("enter a text of numbers = ")

list = n.split()

sum = 0

for num in list:
    sum = sum + int(num)
    
print(sum)    
    
"""a = ['Mahadi','Rahman',10,2.4]
print(a)
print(a[1])
print(a[3])
print(a[0:])
print(a[2:])
print(a[1:2])
print(a[0:3])
print(a[-1])

b = [30,40,'YouTube']
print(b)

c = [a,b]
print(c)

b.insert(3,"Google")
print(b)

b.insert(4,"Facebook")
print(b)

a.remove(10)
print(a)

b.append("Sadia")
print(b)

b.append("Rahman")
print(b)

b.pop(0)
print(b)

b.pop(0)
print(b)

a.pop()
print(a)

del b[1:2]
print(b)

del b[2:4]
print(b)

b.extend(['sadia','rahman','mahadi','rahman'])
print(b)

d = [10,20,30,40,1,1234,56,789]
print(min(d))
print(max(d))
print(sum(d))

d.sort()
print(d)"""



