# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:29:41 2018

@author: Mithilesh
"""

def st_addition(st):
    rev_st=st[-1::-1]
    new_st=''
    for i in range(0,len(st)):
        sum1=ord(st[i])+ord(rev_st[i])-96
        if sum1>122:
            sum1-=26
        new_st+=chr(sum1)
    print(new_st)

t=int(input())
for q in range(t):
    st=str(input())
    st_addition(st)
