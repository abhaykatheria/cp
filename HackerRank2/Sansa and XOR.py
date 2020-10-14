# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:58:38 2019

@author: Mithilesh
"""

def manupl(n,arr):
    ans=0
    if n%2==0:
        ans=0
    else:
        for i in range(0,n,2):
            ans^=arr[i]
    print(ans)

t=int(input())
for q in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    manupl(n,arr)