# -*- coding: utf-8 -*-
"""
Created on Wed May 13 02:44:43 2020

@author: ASUS
"""

# gueesing game

from random import randint

guessnumber = int(input("enter number between 1 to 5 : "))

randomnumber = randint(1,5)


if guessnumber == randomnumber:
    print("You have won")
    
else:
    print("You have lost")
    print("Random number was : ",randomnumber)