# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:36:11 2019

@author: Mithilesh
"""

import operator as op
from functools import reduce

def combo(n, r):
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n-r, -1), 1)
    den = reduce(op.mul, range(1, r+1), 1)
    ans = int(num / den)
    return(ans % (10**+7))
    
n,r=map(int,input().split())
print(int(combo(n,r)))