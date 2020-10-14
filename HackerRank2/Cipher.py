# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:59:53 2019

@author: Mithilesh
"""

def cipher(s,n,k):
    arr=list(map(int,str(s)))
    temp=[arr[0]]
    xor=temp[0]
    for i in range(1,k):
        temp.append(xor^arr[i])
        xor=arr[i]
    for j in range(k,n):
        xor=xor^temp[j-k]
        temp.append(xor^arr[j])
        xor=arr[j]
    print("".join(str(ch) for ch in temp))
n,k=map(int,input().split())
s=str(input())
cipher(s,n,k)
        