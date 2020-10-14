# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:46:52 2018

@author: Mithilesh
"""

n,m=map(int,input().split())
arr=[0 for x in range(n)]
for q in range(m):
    a,b,k=map(int,input().split())
    arr[a-1:b]=[arr[i]+k for i in range(a-1,b)]
    print(arr)
print(max(arr))
