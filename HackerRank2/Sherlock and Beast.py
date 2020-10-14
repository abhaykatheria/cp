# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:40:56 2019

@author: Mithilesh
"""

def sherlock(n):
    if n==1 or n==2 or n==4 or n==7:
        print("-1")
    elif n%3==0:
        x=n//3
        print("5"*3*x)
    else:
        y=0
        while(n>=0 and n%3!=0):
            n-=5
            y+=1
        x=n//3
        print('5'*3*x+'3'*5*y)

t=int(input())
for i in range(t):
    n=int(input())
    sherlock(n)    
    