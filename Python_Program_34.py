# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:26:52 2020

@author: ASUS
"""


class triangle:
    base = ''
    height = ''
    
    
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
        
    def calculate_area(self):
        area = 0.5*self.base*self.height
        print(area)
        
t1 = triangle(10,20)
t1.calculate_area()

t2 = triangle(30, 45)
t2.calculate_area()       
        
        
        
        
        
        
        
        
        