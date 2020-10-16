# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:41:06 2018

@author: Mithilesh
"""

def min_max(l,arr):
    flag=0
    arr.sort()
    for i in range(0,l-1):
        if (arr[i+1]-arr[i])==0 or (arr[i+1]-arr[i])==1:
            flag=0
        else:
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
        
l=int(input())
arr=list(map(int,input().split()))
min_max(l,arr)
        