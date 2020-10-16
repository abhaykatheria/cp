# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:07:23 2019

@author: Mithilesh
"""

def frequency(string):
    l=list(set(list(string)))
    count=[]
    for ch in l:
        count.append(string.count(ch))
    ind=count.index(max(count))
    print(l[ind])

string=input()
frequency(string)