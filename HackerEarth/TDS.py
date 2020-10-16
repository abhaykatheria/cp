# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:06:26 2018

@author: Mithilesh
"""

def TDS(R):
    sol=0
    if R<8:
        sol=0
    else:
        for i in range(1,R-6):
            for j in range(1,int((R-2)/3)):
                for k in range(1,int(R/4)):
                    if i+3*j+4*k==R:
                        sol+=1
    print(sol)

t=int(input())
for q in range(t):
    R=int(input())
    TDS(R)