# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:22:22 2019

@author: Mithilesh
"""

def grid_search(arr,r,c,rt,ct,pat):
    flag=1
    for i in range(0,r-rt):
        if pat[0] in arr[i]:
            l=arr[i].find(pat[0])
            r=l+ct
            for j in range(i+1,i+rt):
                if arr[j].find(pat[j-i])!=l:
                    flag=0
                    break
                else:
                    flag=1
            if flag==1:
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
    
t=int(input())
for q in range(t):
    arr=[]
    pat=[]
    r,c=map(int,input().split())
    for i in range(r):
        s=input()
        arr.append(s)
    rt,ct=map(int,input().split())
    for i in range(rt):
        p=input()
        pat.append(p)
    grid_search(arr,r,c,rt,ct,pat)