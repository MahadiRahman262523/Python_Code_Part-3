# -*- coding: utf-8 -*-
"""
Created on Tue May 12 03:16:41 2020

@author: ASUS
"""


"""def xyz(x):
    switcher = {
        
        0:"zero",
        1:"one",
        2: "two",
        3:"three",
        4: "four",
        5:"five",
        
        
        
        }
    return switcher.get(x,"option not available")

n = int(input("enter any number = "))

c = xyz(n)
print(c)"""


def a():
    return "zero"

def b():
    return "one"

def c():
    return "two"

def d():
    return "three"

def e():
    return "four"


def xyz(x):
    
    switcher = {
        
        0:a(),
        1:b(),
        2:c(),
        3:d(),
        4:e(),
        
        
      }
    
    return switcher.get(x,"option not available") 

n = int(input("enter any number = "))
c = xyz(n)

print(c)


