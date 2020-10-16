# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 01:35:45 2018

@author: Mithilesh
"""

def killer(n,k,x):
    arr=[]
    temp=arr.index(x)
    for i in range(1,n+1):
        arr.append(i%k)
    print(arr)
    while True:
        ind=temp+arr[temp]
        if ind<=n:
            if arr[ind]!=-1:
                arr[ind]=-1
                temp=arr.index()
        
    
n,k,x=map(int,input().split())
killer(n,k,x)
                