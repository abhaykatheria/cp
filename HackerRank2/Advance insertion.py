# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:35:03 2019

@author: Mithilesh
"""
import math
def insertion(n,arr):
    count=0
    for i in range(n):
        for j in range(i):
            if(arr[j]>arr[i]):
                k=arr[i]
                arr.remove(arr[i])
                arr.insert(j-1,k)
                count+=math.fabs(i-j)
                print(arr,count)
    print(arr,int(count))
  
t=int(input())
for q in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    insertion(n,arr)

