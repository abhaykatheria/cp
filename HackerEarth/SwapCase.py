# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:24:49 2018

@author: Mithilesh
"""

def change_case(s):
    s_new=""
    for ch in s:
        if ch.isupper()==True:
            s_new+=ch.lower()
        else:
            s_new+=ch.upper()
    print(s_new)
            
s=str(input())
change_case(s)
        