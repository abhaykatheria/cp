# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:20:07 2019

@author: Mithilesh
"""

def champ(n,a,b,t,st):
    count=0
    for ch in st:
        if ch=='w':
            t-=(1+b)
            if t>=0:
                count+=1
                t-=a
        else:
            t-=1
            if t>=0:
                count+=1
                t-=a
    if t>0:
        count+=t
    print(count)
    
n,a,b,t=map(int,input().split())
st=input()
champ(n,a,b,t,st)