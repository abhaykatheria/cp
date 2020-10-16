# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:13:05 2019

@author: Mithilesh
"""

def camelcase(string):
    l=r=0
    for i in range(1,len(string)):
        if(string[i].isupper()):
            r=i
            print(string[l:r])
            l=r
    print(string[l:i+1])

string=input()
camelcase(string)