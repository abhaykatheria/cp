# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:10:12 2019

@author: Mithilesh
"""

def counting(n,arr):
    for i in range(n):
        a,b=arr[i]
        if i<n/2:
            arr[i]=(a,'-')
    arr=sorted(arr,key=lambda x:x[0])
    for (x,y) in arr:
        print(y,end=" ")
    print(arr)

n=int(input())
arr=[]
for i in range(n):
    x,y=map(str,input().split())
    arr.append((int(x),y))
counting(n,arr)
            