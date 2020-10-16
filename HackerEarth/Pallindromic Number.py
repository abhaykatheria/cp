# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:41:36 2018

@author: Mithilesh
"""

def pallindromic_numbers(a,b):
    count=0
    for i in range(a,b+1):
        temp=str(i)
        if temp==temp[-1::-1]:
            count+=1
    print(count)
    
t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    pallindromic_numbers(a,b)