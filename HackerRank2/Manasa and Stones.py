# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:02:34 2019

@author: Mithilesh
"""

def manasa(n,a,b):
    arr=[]
    for i in range(n):
        k=(n-1-i)*a + i*b
        if k not in arr:
            arr.append(k)
    arr2=sorted(arr)
    for c in arr2:
        print(c,end=" ")
    print()
        
t=int(input())
for tc in range(t):
    n=int(input())
    a=int(input())
    b=int(input())
    manasa(n,a,b)