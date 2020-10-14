# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:57:28 2019

@author: Mithilesh
"""

def luck(arr1,arr2,k):
    arr1.sort()
    s=0
    for i in range(len(arr1)-k):
        s+=arr1[i]
    print(sum(arr1)+sum(arr2)-2s)

n,k=map(int,input().split())
arr1,arr2=[],[]
for j in range(n):
    l,t=map(int,input().split())
    if t==0:
        arr2.append(l)
    else:
        arr1.append(l)
luck(arr1,arr2,k)