# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:52:32 2018

@author: Mithilesh
"""

def catch(x,v,u):
    if u>=v:
        print(-1)
    else:
        net_v=v-u
        t=x/(v-u)
        print(2*t)

x,v,u=map(int,input().split())
catch(x,v,u)