# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:04:27 2020

@author: ASUS
"""


# constructor

class student:
    name = ''
    id = ''
    cgpa = ''
    
    
    def __init__(self,name,id,cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
        
    def display(self):
        print(f' Name : {self.name} , ID : {self.id} , CGPA : {self.cgpa}')
            

d = student('Mahadi Rahman', 177, 3.46)
d.display()



s = student('Sadia Rahman', 444, 3.88)
s.display()






















