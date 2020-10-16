# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:35:30 2018

@author: Mithilesh
"""

n=int(input())
p,q=n,1
for i in range(1,n+1):
    for j in range(1,p+1):
        print(j,end=" ")
    if p<n:
        for k in range(1,2*q):
            print("*",end=" ")
        q+=1
    print()
    p-=1
    
    