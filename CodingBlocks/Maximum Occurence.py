# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:10:27 2018

@author: Mithilesh
"""

def maxm(st):
    b=list(set(st))
    arr=[]
    for ch in b:
        arr.append(st.count(ch))
    ind=b[arr.index(max(arr))]
    print(ind)

st=input()
maxm(st)