# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:16:30 2020

@author: ASUS
"""


# multilevel inheritance


class A:
    def display1(self):
        print("I am inside in A class")



class B(A):
    def display2(self):
        print("I am inside in B class")



class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside in C class")



ob1 = C()
#ob1.display1()
#ob1.display2()
ob1.display3()
