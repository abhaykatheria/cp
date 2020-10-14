# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:20:16 2018

@author: Mithilesh
"""

def picking_numbers(n,arr):
    arr.sort()
    nos=0
    temp=0
    new_arr=[]
    for i in range(0,n-1):
        for j in range(i,n):
            if (arr[j]-arr[i]==0 or arr[j]-arr[i]==1):
                nos+=1
            else:
                new_arr.append(nos)
                nos=0
                break
        if nos==n:
            temp=n
            break
    if temp==n:
        print(n)
    else:
        print(max(new_arr))
    
n=int(input())
arr=list(map(int,input().split()))
picking_numbers(n,arr)
            
        