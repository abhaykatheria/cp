# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:30:39 2019

@author: Mithilesh
"""

from math import factorial

def combo(n,r):
    mod = 10**9 + 7
    ans = factorial(n)*pow(factorial(r)*factorial(n - r), mod - 2, mod) % mod
    return(ans)
    
n,r=map(int,input().split())
print(int(combo(n,r)))