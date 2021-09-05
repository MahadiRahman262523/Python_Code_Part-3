# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:05:26 2020

@author: ASUS
"""
# Exception Handling part 2

try:
   a = int(input("enter a value = ")) 
   b = int(input("enter b value = "))
   c = a/b
   print(c)
   
except (ValueError,TypeError,ZeroDivisionError):
        print("invalid input")