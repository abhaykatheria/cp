# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:29:43 2018

@author: Mithilesh
"""

def tickets(p,s,t,h,x):
    total_cost,flag=0,0
    while s>t:
        total_cost+=p
        s,x=s-1,x-1
        if x==0:
            flag=1
            break
    if flag==1:
        print(total_cost)
    else:
        total_cost+=x*h
        print(total_cost)
    
p,s,t,h,x=map(int,input().split())
tickets(p,s,t,h,x)