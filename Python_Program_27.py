# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:20:32 2020

@author: ASUS
"""


# recursion


def fact(n):
    
    if(n == 1):
        return 1
    
    else:
        return n*fact(n-1)


n = int(input("enter any number = "))

print(fact(n))






