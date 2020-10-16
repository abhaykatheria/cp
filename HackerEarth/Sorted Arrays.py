# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 00:11:04 2018

@author: Mithilesh
"""

def sorted_arrays(n,arr):
    steps=0
    arr2=list(arr)
    for i in range(n-1):
        if arr[i]>=arr[i+1]:
            arr[i+1]+=arr[i]-arr[i+1]+1
            steps+=arr[i+1]-arr2[i+1]
    print(steps)

n=int(input())
arr=list(map(int,input().split()))
sorted_arrays(n,arr)