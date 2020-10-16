# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:33:45 2019

@author: Mithilesh
"""

from itertools import permutations 
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        lst.append("".join(map(str,i)))
    return max(lst)

t=int(input())
for q in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(largest(arr))        
