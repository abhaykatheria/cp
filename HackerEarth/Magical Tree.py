# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:21:50 2018

@author: Mithilesh
"""

t=int(input())
arr=[]
for j in range(t):
    a=input()
    a=list(a)
    sum1=int(a[0])
    for i in range(1,len(a)-1):
        if a[i]=='+':
            sum1+=int(a[i+1])
        elif a[i]=="-":
            sum1-=int(a[i+1])
        else:
            continue
    arr.append(sum1)
print(max(arr))
