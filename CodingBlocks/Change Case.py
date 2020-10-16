# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:15:32 2018

@author: Mithilesh
"""

def change_case(st):
    st2=""
    for ch in st:
        if ch.isupper()==True:
            st2+=ch.lower()
        else:
            st2+=ch.upper()
    print(st2)

st=input()
change_case(st)