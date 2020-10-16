# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:00:26 2018

@author: Mithilesh
"""

def pythagoras(A):
    flag=0
    st=""
    for i in range(int(A**0.5)+1):
        for j in range(int(A**0.5)+1):
            if i**2+j**2==A:
                if (i>j):
                    flag=1
                    break
                else:
                    st="("+str(i)+","+str(j)+")"
                    print(st)
        if flag==1:
            break
t=int(input())
for q in range(t):
    A=int(input())
    pythagoras(A)          