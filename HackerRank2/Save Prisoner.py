# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 02:35:23 2018

@author: Mithilesh
"""

def save(n,m,s):
    temp=m%n
    if temp==0 and s==1:
        print(n)
    elif(s+temp-1)>n:
        print(s+temp-n-1)
    else:
        print(s+temp-1)

t=int(input())
for p in range(0,t):
    n,m,s=map(int,input().split())
    save(n,m,s)