# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 21:32:43 2018

@author: Mithilesh
"""

def attendence(a,b):
    if (b/a)>=0.75:
        print(0)
    else:
        print(3*a-4*b)

t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    attendence(a,b)