# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:47:23 2020

@author: ASUS
"""


# Magic method

class bike:
    name = ''
    color = ''
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
        
    def __eq__(self,other):
        return self.name == other.name and self.color == other.color
    
    def __str__(self):
        return (f'Name : {self.name} , Color : {self.color}')
    
    def display(self):
        print(f'Name : {self.name} , Color : {self.color}')
        
        
b1 = bike('yahamar5','blue')  
b2 = bike('yahamar5','blue') 

print(b1==b2)     
        
        
        
        
        
        
        
        
        
        
        
        