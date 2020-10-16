# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 13:23:07 2018

@author: Mithilesh
"""

def destination(st):
    x,y=0,0
    for com in st:
        if com=="L":
            x-=1
        elif com=="R":
            x+=1
        elif com=="D":
            y-=1
        elif com=="U":
            y+=1
    print(x,y)

st=str(input())
destination(st)