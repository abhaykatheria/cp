# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:54:01 2018

@author: Mithilesh
"""

n=int(input())
k,q=2,n
for i in range(n+1):
    if k<n+2:
        for j in range(1,k):
            print(j,end="")
    if q>1:
        for p in range(1,q):
            print("*",end="")
        q-=1
    print()
    k+=1