# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:22:08 2019

@author: Mithilesh
"""

def arraysum(n,arr1,m,arr2):
    a1="".join(arr1)
    a2="".join(arr2)
    som=str(int(a1)+int(a2))
    for ch in som:
        print(ch,end=", ")
    print("END")
    
n=int(input())
arr1=list(map(str,input().split()))
m=int(input())
arr2=list(map(str,input().split()))
arraysum(n,arr1,m,arr2)
    
    