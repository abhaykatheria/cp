# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 00:12:10 2019

@author: Mithilesh
"""

k=int(input())
s=str(input())
l=len(s)
a_c=s.count('a')
b_c=l-a_c
minm=min(a_c,b_c)
if minm<=k:
    print(l)
else:
    count_arr=[]
    