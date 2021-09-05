# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:42:36 2020

@author: ASUS
"""

# Heirarical inheritance


class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        
        
class triangle(shape):

        def area(self):
            area = 0.5*self.dim1*self.dim2
            print("Area of a triangle = ",area)
            
            
            
class rectangle(shape):

        def area(self):
            area = self.dim1*self.dim2
            print("Area of a rectangle = ",area)            
            
            
t = triangle(23,34)
t.area()

r = rectangle(45,67)
r.area()

           
            
            
            
            
            
            
            
            