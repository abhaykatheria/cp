# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 01:23:05 2019

@author: Mithilesh
"""

def bits(arr,n):
    bit_arr=[0]*64
    ans=0
    for num in arr:
        i=0
        while(num>0):
            bit_arr[i]+=num&1
            num=num>>1
            i+=1
    bit_arr=[i%3 for i in bit_arr]
    for i in range(64):
        ans+=bit_arr[i]*(2**i)
    print(ans)
    
n=int(input())
arr=list(map(int,input().split()))
bits(arr,n)