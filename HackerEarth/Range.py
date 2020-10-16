# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:12:42 2018

@author: Mithilesh
"""

def nos_range(n,x,y,arr):
    if max(arr)<=y and min(arr)>=x:
        print("YES")
    else:
        print("NO")
        
n,x,y=map(int,input().split())
arr=list(map(int,input().split()))
nos_range(n,x,y,arr)    