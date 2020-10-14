# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:54:18 2019

@author: Mithilesh
"""

def mark(n,k,arr):
    arr.sort()
    count=0
    for i in range(n):
        k-=arr[i]
        if k>=0:
            count+=1
        else:
            break
    print(count)

n,k=map(int,input().split())
arr=list(map(int,input().split()))
mark(n,k,arr)