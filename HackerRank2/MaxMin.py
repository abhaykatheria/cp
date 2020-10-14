# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:58:46 2019

@author: Mithilesh
"""

def subarr(n,arr,k):
    arr=sorted(arr)
    t=[]
    for i in range(0,n):
        if i+k>n:
            break
        else:
            t.append(max(arr[i:i+k])-min(arr[i:i+k]))
    print(min(t))

n=int(input())
k=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
subarr(n,arr,k)