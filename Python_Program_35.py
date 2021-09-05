# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:34:11 2020

@author: ASUS
"""


# inheritance


class phone():
    
    def call(self):
        print("You can call")
        
        
    def message(self):
        print("You can message")
        
        
class samsang(phone):

        def photo(self):
            print("You can take some photos")



s = samsang()
s.call()
s.message()
s.photo()

print(issubclass(samsang,phone))














