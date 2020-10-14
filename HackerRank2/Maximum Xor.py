# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:42:03 2019

@author: Mithilesh
"""

def XOR(l,r):
    n,p=0,r
    while(p!=0):
        p=int(p/2)
        n+=1
    maxm=2**n - 1
    if(maxm^r>=l):
        print(maxm)
    else:
        for i in range(maxm,1,-1):
            if(i^l>=l and i^l<=r):
                newmax=i
                break
        for i in range(maxm,1,-1):
            if(i^r>=l and i^r<=r):
                newmax2=i
                break
        print(max(newmax,newmax2))
    
l=int(input())
r=int(input())
XOR(l,r)