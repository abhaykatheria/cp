# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:23:01 2018

@author: Mithilesh
"""

def play_with_numbers(arr,l,r):
    mean=0
    for i in range(l-1,r):
        mean+=arr[i]
    print(int(mean/(r-l+1)))

n,q=map(int,input().split())
arr=list(map(int,input().split()))
for j in range(0,q):
    l,r=map(int,input().split())
    play_with_numbers(arr,l,r)
    