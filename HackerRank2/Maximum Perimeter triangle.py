# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:03:50 2019

@author: Mithilesh
"""

def triangle(n,arr):
    arr2,a,b,c=[0,(0,0,0)],0,0,0
    arr.sort()
    for i in range(0,n-2):
        a,b,c=arr[i],arr[i+1],arr[i+2]
        if(a<(b+c) and b<(a+c) and c<(a+b)):
            if arr2[0]<(a+b+c):
                arr2[0]=a+b+c
                arr2[1]=(a,b,c)
    if arr2[0]==0:
        print("-1")
    else:
        print(arr2[1][0],arr2[1][1],arr2[1][2])

n=int(input())
arr=list(map(int,input().split()))
triangle(n,arr)
