# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:24:37 2018

@author: Mithilesh
"""

def sweets(n,k):
    if n%k==0:
        print(0)
    else:
        print(1)
        
n,k=map(int,input().split())
sweets(n,k)