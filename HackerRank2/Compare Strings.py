# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:38:58 2019

@author: Mithilesh
"""

def comp(s1,s2):
    s1,s2,flag=set(s1),set(s2),0
    for ch in s1:
        if ch in s2:
            print("YES")
            flag=0
            break
        else:
            flag=1
    if flag==1:
        print("NO")

t=int(input())
for i in range(t):
    s1=str(input())
    s2=str(input())
    comp(s1,s2)