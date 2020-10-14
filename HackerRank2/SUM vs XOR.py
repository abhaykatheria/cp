# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:12:44 2019

@author: Mithilesh
"""

def SUMXOR(n):
    count=0
    if n==0:
        count=0
    else:
        for i in range(n):
            if(i^n==i+n):
                count+=1
    print(count)

n=int(input())
SUMXOR(n)