# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:55:28 2018

@author: Mithilesh
"""

def gibo(n):
    a,b=1,1
    for i in range(3,n+1):
        a,b=b,a+b+int(i**2)
    print(b)
n=int(input())
gibo(n)
