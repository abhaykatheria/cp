# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:38:47 2019

@author: Mithilesh
"""
import functools
def compare(s1,s2):
    if s1[0]==s2[0]:
        if len(s1)<=len(s2) and s2.find(s1)==0:
            return(1)
        elif len(s2)<=len(s1) and s1.find(s2)==0:
            return(-1)
        else:
            if s1>s2:
                return(1)
            else:
                return(-1)
                
    else:
        if s1>s2:
            return(1)
        else:
            return(-1)

n=int(input())
s=[]
for i in range(n):
    st=input()
    s.append(st)
s=sorted(s,key=functools.cmp_to_key(compare))
for ch in s:
    print(ch)