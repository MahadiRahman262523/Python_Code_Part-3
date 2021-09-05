# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:25:57 2020

@author: ASUS
"""


# Exception Handling part 1

# type error,index error,zero division error,syntax error

try:
    list = [10,20,0]
    result = list[0] / list[2]
    print(result)
    
except ZeroDivisionError :
    print("zero division error")
    
finally:
    print("succesful")


















