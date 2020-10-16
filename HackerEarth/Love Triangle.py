# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:50:55 2018

@author: Mithilesh
"""

def Love(n):
    x=n%9+10*int(n/9)
    print(x)
a=0
while a<5:
    n=int(input())
    Love(n)
    a+=1