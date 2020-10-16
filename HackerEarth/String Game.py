# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:03:59 2018

@author: Mithilesh
"""

def string_game(st):
    arr=[]
    distinct_st=list(set(st))
    for i in range(len(distinct_st)):
        arr.append(st.count(distinct_st[i]))
    if len(arr)%2==0:
        print("Player2")
    else:
        print("Player1")

t=int(input())
for q in range(t):
    st=str(input())
    string_game(st)