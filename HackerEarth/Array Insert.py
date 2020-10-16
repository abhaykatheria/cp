# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 00:21:45 2018

@author: Mithilesh
"""

def array_insert(n,q,arr,que,a,b):
    sum1=0
    if que==1:
        arr[a]=b
    elif que==2:
        for i in range(a,b+1):
          sum1+=arr[i]
        print(sum1)
        
n,q=map(int,input().split())
arr=list(map(int,input().split()))
for g in range(0,q):
    que,a,b=map(int,input().split())
    array_insert(n,q,arr,que,a,b)
