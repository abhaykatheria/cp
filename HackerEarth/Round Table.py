# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 22:32:42 2018

@author: Mithilesh
"""

def round_table(n,x,k):
    lst=[i for i in range(1,n+1)]
    while(x%k)<len(lst):
        t=x%k
        list2=list(lst)
        for i in range(t):
            