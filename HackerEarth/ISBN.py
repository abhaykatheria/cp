# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:53:31 2018

@author: Mithilesh
"""

def ISBN(n):
    n=list(str(n))
    sum1=0
    if len(n)==10:
        for i in range(0,10):
            sum1+=int(n[i])*(i+1)
        if sum1%11==0:
            print("Legal ISBN")
    else:
        print("Illegal ISBN")

n=int(input())
ISBN(n)