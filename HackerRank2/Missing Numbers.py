# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:48:01 2019

@author: Mithilesh
"""

def missin(n,arr1,m,arr2):
    for ch in arr1:
        arr2.remove(ch)
    arr2=sorted(list(set(arr2)))
    for ch in arr2:
        print(ch,end=" ")
        
n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
missin(n,arr1,m,arr2)