# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:51:47 2018

@author: Mithilesh
"""

def reverse(n,arr,l,r):
    l,r=l-1,r-1
    if l-1>=0:
        arr=arr[:l]+arr[r:l-1:-1]+arr[r+1:]
    else:
        arr=arr[:l]+arr[r::-1]+arr[r+1:]
    return(max_sum(n,arr))

def max_sum(n,arr):
    max1,max_ending_index=0,0
    for i in range(n):
        max_ending_index+=arr[i]
        if max1<max_ending_index:
            max1=max_ending_index
        if max_ending_index<0:
            max_ending_index=0
    print(max1)

n,q=map(int,input().split())
arr=list(map(int,input().split()))
for t in range(q):
    l,r=map(int,input().split())
    reverse(n,arr,l,r)
        