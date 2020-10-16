# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:51:49 2019

@author: Mithilesh
"""

def motu_patlu(n):
    i=int((-1+(1+(8*(n/3)))**0.5)/2)
    rem=n-(3*i*(i+1)/2)
    if rem==0 or rem>i+1:
        print("Motu")
    else:
        print("Patlu")
    
n=int(input())
motu_patlu(n)
    