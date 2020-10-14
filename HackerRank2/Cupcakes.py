# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:12:57 2019

@author: Mithilesh
"""

def cupcakes(n,arr):
    arr.sort(reverse=True)
    cal=0
    for j in range(n):
        cal+=(2**j)*arr[j]
    print(cal)

n=int(input())
arr=list(map(int,input().split()))
cupcakes(n,arr)