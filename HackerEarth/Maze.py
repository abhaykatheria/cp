# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:34:48 2019

@author: Mithilesh
"""

def maze(string):
    x,y=0,0
    for step in string:
        if step=='L':
            x-=1
        elif step=='R':
            x+=1
        elif step=='U':
            y+=1
        elif step=='D':
            y-=1
    print(x,y)

string=str(input())
maze(string)