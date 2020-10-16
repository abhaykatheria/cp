# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:06:39 2018

@author: Mithilesh
"""

def array_sum(n,arr):
    sum1=0
    for i in arr:
        sum1+=i
    print(sum1)

n=int(input())
arr=list(map(int,input().split()))
array_sum(n,arr)