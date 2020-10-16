# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:23:51 2018

@author: Mithilesh
"""

def diwali(a,k,n):
    sum1=a+k*(n-1)
    print(sum1)
t=int(input())
for q in range(t):
    a,k,n=map(int,input().split())
    diwali(a,k,n)