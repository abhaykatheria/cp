# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:07:55 2019

@author: Mithilesh
"""

def weighted_string(string):
    ans=0
    for ch in string:
        ans+=ord(ch)-97+1
    print(ans)

string=str(input())
weighted_string(string)