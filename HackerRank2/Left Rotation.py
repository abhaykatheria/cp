# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 03:46:18 2018

@author: Mithilesh
"""

def left_rotation(n,r,arr):
    arr2=list(arr)
    temp=r%n
    for i in range(0,n):
        arr[i-temp]=arr2[i]
    for j in arr:
        print(j,end=" ")
    
n,r=map(int,input().split())
arr=list(map(int,input().split()))
left_rotation(n,r,arr)