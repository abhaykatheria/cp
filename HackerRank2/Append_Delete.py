# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:16:27 2018

@author: Mithilesh
"""

def append_delete(s,t,k):
    s2,t2,ls,lt="","",len(s),len(t)
    for i in range(0,min(ls,lt)):
        if t[i]==s[i]:
            s2=s[i+1::]
            t2=t[i+1::]
        else:
            s2=s[i::]
            t2=t[i::]
            break
    if (len(s2)+len(t2))<=k:
        print("Yes")
    else:
        print("No")
        
s=str(input())
t=str(input())
k=int(input())
append_delete(s,t,k)