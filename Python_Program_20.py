# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:26:43 2020

@author: ASUS
"""


from calendar import *
from datetime import date

"""a = calendar(2022)
print(a)


a = month(2020,8)
print(a)

a = isleap(2028)
print(a)


a = leapdays(1998,2020)
print(a)

a = monthrange(2020,5)
print(a)

a = weekday(2020,5,12)
print(a)"""


y = int(input("enter year = "))
m = int(input("enter month = "))
d = int(input("enter date = "))


b = date(y,m,d)
print(b)

c = date.today()
print(c)

a = ((c-b).days)/365
print(a)
















