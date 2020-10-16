# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:17:37 2018

@author: Mithilesh
"""
arr=[]
arr2=[]
try:
    while True:
        n=int(input())
        arr.append(n)
except:
    k=len(arr)
    for j in range(0,k):
        if arr[j]==42:
            break
        else:
            arr2.append(arr[j])
    for k in arr2:
        print(k)    

