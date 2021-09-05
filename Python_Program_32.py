# -*- coding: utf-8 -*-
"""
Created on Thu May 14 02:52:11 2020

@author: ASUS
"""

# Method

class student:
    name = ''
    id = ''
    cgpa = ''
    
    
    def setValue(self,name,id,cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
        
    def display(self):
        print(f' Name : {self.name} , ID : {self.id} , CGPA : {self.cgpa}')
            

d = student()
d.setValue('Mahadi Rahman', 177, 3.46)
d.display()



s = student()
s.setValue('Sadia Rahman', 444, 3.88)
s.display()


















