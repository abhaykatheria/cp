# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:44:40 2018

@author: Mithilesh
"""
import math
def magical_word(n,st):
    temp,minm,arr,arr2=0,0,[],[]
    prime=[67,71,73,79,83,89,97,101,103,107,109,113]
    new_message=""
    for ch in st:
        for i in range(0,12):
            temp=ord(ch)-prime[i]
            arr.append(int(math.fabs(temp)))
        for k in arr:
            arr2.append(int(math.fabs(k)))
        minm=min(arr2)
        if ord(ch)-minm in prime:
            new_message+=chr(ord(ch)-minm)
        else:
            new_message+=chr(ord(ch)+minm)
        arr.clear()
        arr2.clear()
    print(new_message)

n=int(input())
st=str(input())
magical_word(n,st)