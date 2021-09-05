# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:59:20 2020

@author: ASUS
"""


# loop in string

"""a = "Mahadi Rahman"

for i in a :
    print(i)"""
    

# loop in list   
    
"""a = [1,2,3,'sadia','dhrubo',8,9] 

for i in a :
    print(i)"""
    
 
# loop in tuples

"""a = (1,2,3,4,5,"mahadi","Sadia")

for i in a :
    print(i) """
    
# loop in sets

"""for i in {1,2,3,4,5,"mahadi","Sadia"} :
    print(i)"""
    
    
# loop in dictionary

"""d = {1:'Dhrubo',2:'Sadia'}

for i in d:
    print(i,d[i])""" 
    
"""for i in range(1,16):
    print(i)"""
    
    
# loop in factorial

"""n = int(input("enter value of n = "))

f = 1

for i in range(1,n+1):
        f = f*i
        
print(f)    """


n = int(input("enter n = "))

c = 0

for i in range(2,n):

        if(n%i == 0):
            c = c + 1
            
if(c == 0):
    print("Prime number")

else:
    print("Not Prime number")            
    
    
    
    
    
    
    
    
    
    
    