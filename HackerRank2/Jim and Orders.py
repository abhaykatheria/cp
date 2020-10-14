# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:40:48 2019

@author: Mithilesh
"""

def jim(arr1,n):
    arr2=list(arr1)
    arr2.sort()
    for i in range(n):
        print(arr1.index(arr2[i])+1,end=" ")
        arr1[arr1.index(arr2[i])]=0
n=int(input())
arr1=[]
for i in range(n):
    c_id,pre_t=map(int,input().split())
    arr1.append(c_id+pre_t)
jim(arr1,n)