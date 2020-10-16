# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:17:24 2018

@author: Mithilesh
"""

def jump(n,arr):
    for i in range(len(arr)):
        if (i+arr[i]+1)>n:
            print(i+1)
            break
n=int(input())
arr=list(map(int,input().split()))
jump(n,arr)