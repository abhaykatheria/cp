# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:32:02 2018

@author: Mithilesh
"""

n=int(input())
p=1
for i in range(1,n+1):
    for j in range(p):
        if p<3:
            print(p,end="    ")
        else:
            if j==0:
                print(p,end="    ")
            elif 0<j<(p-1):
                print(0,end="    ")
            else:
                print(p,end="    ")
    print()
    p+=1