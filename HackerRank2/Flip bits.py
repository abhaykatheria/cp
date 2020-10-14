# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:49:57 2019

@author: Mithilesh
"""

def binary(n):
    string=str(bin(n))
    arr=str("0"*(32-len(string[2:]))+string[2:])
    ans=0
    arr=arr[-1::-1]
    for i in range(32):
        if int(arr[i])==0:
            ans+=2**i
    print(ans)
    
t=int(input())
for q in range(t):
    n=int(input())
    binary(n)
    