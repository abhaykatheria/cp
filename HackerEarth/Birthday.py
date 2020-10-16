# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:08:14 2018

@author: Mithilesh
"""

def Birthday(n,sweets):
    if sweets%n==0:
        print("YES")
    else:
        print("NO")

t=int(input())
for q in range(0,t):
    n,sweets=map(int,input().split())
    Birthday(n,sweets)