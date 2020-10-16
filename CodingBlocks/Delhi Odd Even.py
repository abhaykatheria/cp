# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:45:21 2018

@author: Mithilesh
"""

def Delhi_Odd_Even(n):
    n=list(map(int,str(n)))
    even,odd=0,0
    for ch in n:
        if ch%2==0:
            even+=ch
        else:
            odd+=ch
    if even%4==0 or odd%3==0:
        print("Yes")
    else:
        print("No")
    
t=int(input())
for i in range(t):
    n=int(input())
    Delhi_Odd_Even(n)