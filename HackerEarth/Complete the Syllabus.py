# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:16:09 2018

@author: Mithilesh
"""

def syllabus(k,arr):
    arr2=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    top=[]
    sum1=0
    for i in range(0,7):
        sum1+=arr[i]
        top.append(sum1)
    for j in range(0,7):
        if sum1<k:
            k=k%sum1
            if k==0:
                k=sum1
        if top[j]==k or (k<top[j]):
            print(arr2[j])
            break
t=int(input())
for q in range(t):
    k=int(input())
    arr=list(map(int,input().split()))
    syllabus(k,arr)