# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:29:31 2018

@author: Mithilesh
"""

def string_sum(st):
    sum1=0
    for ch in st:
        sum1+=ord(ch)-96
    print(sum1)
st=str(input())
string_sum(st)