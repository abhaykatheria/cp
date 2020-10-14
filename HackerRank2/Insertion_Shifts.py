# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 02:39:29 2018

@author: Mithilesh
"""

def insertion(n,arr):
    shift=0
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                shift+=1
    print(shift)

t=int(input())
for k in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    insertion(n,arr)