# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:58:20 2019

@author: Mithilesh
"""

t=int(input())
for q in range(t):
    a,b=map(str,input().split())
    arr=[]
    for i in range(len(a)):
        if(a[i]==b[i]):
            arr.append('0')
        else:
            arr.append('1')
    #if(len(arr)==arr.count('0')):
     #   print(0)

    print("".join(arr))