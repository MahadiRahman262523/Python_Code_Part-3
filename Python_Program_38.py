# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:25:25 2020

@author: ASUS
"""


# multiple inheritance


class A:
    def display(self):
        print("I am inside in A class")



class B:
    def display(self):
        print("I am inside in B class")



class C(A,B):
    pass
   # def display(self):
        
       # print("I am inside in C class")



ob1 = C()
#ob1.display1()
#ob1.display2()
ob1.display()










