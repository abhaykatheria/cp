# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:39:35 2018

@author: Mithilesh
"""
import math
def even_odd(n,arr,k,l,r):
    count=0
    if k==1:
        for i in range(l-1,r):
            if arr[i]%2==1:
                count+=1
    else:
        for j in range(l-1,r):
            if arr[j]%2==0:
                count+=1
    if count==0:
        print(0)
    elif count==(r-l+1):
        print(1)
    else:
        gcd=math.gcd(count,r-l+1)
        print(count//gcd,(r-l+1)//gcd)

t=int(input())
for p in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    for z in range(q):
        k,l,r=map(int,input().split())
        even_odd(n,arr,k,l,r)