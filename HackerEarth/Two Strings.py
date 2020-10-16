# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:35:29 2018

@author: Mithilesh
"""

def two_strings(s1,s2):
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    if s1==s2:
        print("YES")
    else:
        print("NO")

t=int(input())
for j in range(t):
    s1,s2=map(str,input().split())
    two_strings(s1,s2)