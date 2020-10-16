# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:50:59 2018

@author: Mithilesh
"""

def pyramid(n):
    for i in range(1,n+1):
        print((n-i)*" ",end="")
        print((2*i-1)*'*')
    
t=int(input())
for q in range(t):
    n=int(input())
    pyramid(n)