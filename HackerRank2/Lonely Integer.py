# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:24:27 2019

@author: Mithilesh
"""
def lonely(n,arr):
    newarr=list(set(arr))
    for ele in newarr:
        if arr.count(ele)==1:
            print(ele)
            break

n=int(input())
arr=list(map(int,input().split()))
lonely(n,arr)
    
