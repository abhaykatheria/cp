# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:57:03 2019

@author: Mithilesh
"""

def priyanka(n,arr):
    containers=0
    arr.sort()
    ind=0
    while(ind<n):
        minm=arr[ind]
        maxm=minm+4
        if maxm>max(arr):
            containers+=1
            break
        if maxm in arr:
            ind=n-arr[-1::-1].index(maxm)
            containers+=1
        else:
            for ch in arr[ind:]:
                if ch>maxm:
                    containers+=1
                    ind=arr.index(ch)+1
                    break
        print(containers)

n=int(input())
arr=list(map(int,input().split()))
priyanka(n,arr)