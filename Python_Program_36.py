# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:58:32 2020

@author: ASUS
"""


# method overriding

class phone():
    
    def __init__(self):
        print("I am in phone class")
        
        
class samsung(phone):
        
        def __init__(self):
            super().__init__()
            print("I am in samsung class")
            
            
s = samsung()
s.__init__()           
            
            
            
            
            
            
            
            
            
            
            
            