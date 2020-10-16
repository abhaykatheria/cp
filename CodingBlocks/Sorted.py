# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:28:08 2019

@author: Mithilesh
"""

import functools
def comp(a,b):
    if int(a[1])!=int(b[1]):
        if(int(a[1])>int(b[1])):
            return(-1)
        else:
            return(1)
        
    else:
        if(a[0]>b[0]):
            return(1)
        else:
            return(-1)
    
n=int(input())
k=int(input())
arr=[]
for i in range(k):
    l=tuple(map(str,input().split()))
    if(int(l[1])>=n):
        arr.append(l)
arr=sorted(arr, key=functools.cmp_to_key(comp))
for ch in arr:
    print(ch[0],ch[1])
