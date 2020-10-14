# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:56:22 2017

@author: Mithilesh
"""

def birds(n,list1):
    list2=[0,0,0,0,0]
    for i in range(1,6):
        for j in range(0,n):
            if i==list1[j]:
                list2[i-1] +=1
            else:
                continue
    print(list2.index(max(list2))+1)
    print(list2)

n=int(input())
list1=list(map(int,input().split()))
birds(n,list1)