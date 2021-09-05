# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:09:34 2020

@author: ASUS
"""

# Lambda function

"""c = lambda  a,b,c:a+b+c*a

n = int(input("enter n = "))
m = int(input("enter m = "))
l = int(input("enter l = "))

print(c(n,m,l))"""


# map function

"""def xyz(n):
    return n*n"""

"""b = lambda n:n*n    


l = [3,6,8]

a = map(b,l)
print(tuple(a))"""


"""a = [4,6,9]
b = [7,9,10]

def mul(x,y):
    return x*y

c = map(mul,a,b)
print(list(c))"""


# filter function

def xyz(n):
    if(n%2 == 0):
        return True
    else:
        return False
    
l = [1,23,56,90,4,8,67]    

a = filter(xyz,l)
print(list(a))
















