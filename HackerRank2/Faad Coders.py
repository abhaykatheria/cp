# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:38:17 2018

@author: Mithilesh
"""

def faad(c,d,f):
    if c+f<=d:
        c+=f
    else:
        c+=f//2
    if d+f<=c:
        d+=f
    else:
        d+=f//2
    if c<d:
        print(2*c)
    else:
        print(2*d)

c,d,f=map(int,input().split())
faad(c,d,f)