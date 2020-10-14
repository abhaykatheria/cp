# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:30:35 2019

@author: Mithilesh
"""

def fair(n,arr):
    loaf=0
    for i in range(n-1):
        if arr[i]%2!=0:
            arr[i]+=1
            arr[i+1]+=1
            loaf+=2
    if arr[n-1]%2==0:
        print(loaf)
    else:
        print("NO")
    
n=int(input())
arr=list(map(int,input().split()))
fair(n,arr)
