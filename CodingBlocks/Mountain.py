# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:54:07 2018

@author: Mithilesh
"""

n=int(input())
k,p=2*n-4,1
for i in range(n):
    for j in range(1,p+1):
        print(j,end="    ")
    if k>0: 
        print("     "*k,end="     ")
        k-=2
        for q in range(p,0,-1):
            print(q,end="    ")
    elif k==0:
        print(end="     ")
        for q in range(p,0,-1):
            print(q,end="    ")  
        k-=2
    else:
        for q in range(p-1,0,-1):
            print(q,end="    ")
    p+=1
    print()