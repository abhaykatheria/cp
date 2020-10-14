# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:20:44 2019

@author: Mithilesh
"""
import math
def strange(t):
    n=math.log((t/3 +1),2)
    utb=3*(2**(math.ceil(n)) - 1)
    value=utb-t+1
    return(value)

t=int(input())
print(strange(t))