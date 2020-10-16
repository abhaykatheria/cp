# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:56:48 2018

@author: Mithilesh
"""

def great_kian(n,arr):
    sum1,sum2,sum3=0,0,0
    for i in range(0,n,3):
        sum1+=arr[i]
    for j in range(1,n,3):
        sum2+=arr[j]    
    for k in range(2,n,3):
        sum3+=arr[k]
    print(sum1,sum2,sum3)

n=int(input())
arr=list(map(int,input().split()))
great_kian(n,arr)