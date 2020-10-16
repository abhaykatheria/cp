# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:33:49 2018

@author: Mithilesh
"""

def digit(x,k):
    x=str(x)
    count=0
    for i in range(0,len(x)):
        if count==k:
            break
        if x[i]!='9':
            x=x.replace(x[i],'9',1)
            count+=1
    print(x)
    
x,k=map(int,input().split())
digit(x,k)
            