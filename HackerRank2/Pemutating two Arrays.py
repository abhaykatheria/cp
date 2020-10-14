# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 01:26:34 2019

@author: Mithilesh
"""

def perm(arr1,arr2,k):
    arr1.sort(reverse=True)
    arr2.sort()
    flag=0
    maxx=arr1[0]+arr2[-1]
    if k>maxx:
        print("NO")
    else:
        for i in range(len(arr1)):
            if k>arr1[i]+arr2[i]:
                print("NO")
                flag=0
                break
            else:
                flag=1
        if flag==1:
            print("YES")
    
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    perm(arr1,arr2,k)